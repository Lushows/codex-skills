# 65 — LUTs

Una LUT (*Look-Up Table*, "tabla de consulta") es un archivo que dice: **este color de entrada se
convierte en este color de salida**. Nada más. Es un diccionario de traducción de colores.

Se usan por dos razones muy distintas, y confundirlas es el error de fondo de este tema:

1. **LUT técnica** — traduce material grabado en *log* (plano, gris, sin contraste) al espacio de
   visualización normal. Es corrección obligatoria, no gusto.
2. **LUT creativa** — aplica un look. Es gradación, y es opcional.

Y la frase que hay que decirle a todo el mundo:

> **Una LUT no arregla un plano mal expuesto. Lo empeora.**

---

## 1. LUT 1D vs LUT 3D

**LUT 1D**: tres tablas independientes, una por canal. "El rojo 128 pasa a ser 140". No puede
cambiar el tono de un color, solo su intensidad por canal. Sirve para curvas de contraste y para
conversiones de gamma. Es lo mismo que hace el filtro `curves`.

**LUT 3D**: una tabla que mapea **combinaciones** de RGB. "Este rojo específico, con este verde y
este azul, se convierte en este otro color completamente distinto". Puede volver azul un rojo. Es lo
que se usa para looks de verdad.

Casi todo lo que te vas a encontrar en el mundo real es 3D en formato `.cube`.

Una LUT 3D no guarda los 16,7 millones de colores posibles: guarda una rejilla. Tamaños típicos:

| Tamaño | Entradas | Peso | Uso |
|---|---|---|---|
| 17×17×17 | 4.913 | ~100 KB | rápido, para monitoreo |
| **33×33×33** | 35.937 | ~1 MB | **el estándar de la industria** |
| 65×65×65 | 274.625 | ~8 MB | masters, cuando importa cada matiz |

Los colores que caen entre dos puntos de la rejilla se calculan por interpolación. De ahí viene el
parámetro `interp` que verás abajo.

---

## 2. Anatomía de un archivo .cube

Ábrelo con un editor de texto. Es texto plano:

```
TITLE "GastroLatam Look v3"
LUT_3D_SIZE 33
DOMAIN_MIN 0.0 0.0 0.0
DOMAIN_MAX 1.0 1.0 1.0

0.035000 0.086000 0.227000
0.038512 0.086901 0.227411
0.042024 0.087802 0.227822
...
```

- `LUT_3D_SIZE 33` → rejilla de 33 por lado.
- `DOMAIN_MIN` / `DOMAIN_MAX` → el rango de entrada (casi siempre 0–1).
- Después vienen **33³ = 35.937 líneas**, cada una con el RGB de salida en escala 0–1.
- **El orden importa:** el rojo es el que cambia más rápido, después el verde, y el azul es el más
  lento. Si armas una LUT a mano y sale con los colores cruzados, casi siempre es que invertiste
  ese orden.

Fíjate en la primera línea del ejemplo: `0.035 0.086 0.227`. Eso es exactamente el punto negro del
azul de marca del módulo `64`. Una LUT puede llevar el duotono adentro.

---

## 3. Aplicar una LUT con ffmpeg

```bash
ffmpeg -i entrada.mp4 -vf "lut3d=file=looks/gastro_v3.cube:interp=tetrahedral,format=yuv420p" \
  -c:v libx264 -crf 18 -preset slow \
  -colorspace bt709 -color_primaries bt709 -color_trc bt709 -color_range tv \
  -c:a copy salida.mp4
```

### Modos de interpolación

| `interp` | Calidad | Velocidad | Cuándo |
|---|---|---|---|
| `nearest` | mala | máxima | nunca en entrega; sirve para probar rápido |
| `trilinear` | buena | rápida | por defecto |
| **`tetrahedral`** | **la mejor** | media | **úsalo siempre para entregar** |
| `pyramid`, `prism` | intermedias | media | casos raros |

`tetrahedral` produce menos banding en degradados. La diferencia con `trilinear` es pequeña pero
real, y no cuesta nada.

### Aplicar una LUT al 60% (dosificar)

Las LUTs suelen venir demasiado fuertes. No hay parámetro de intensidad en `lut3d`, pero se hace
mezclando con el original:

```bash
ffmpeg -i entrada.mp4 -filter_complex "\
[0:v]split=2[orig][lut];\
[lut]lut3d=file=looks/gastro_v3.cube:interp=tetrahedral[l];\
[orig][l]blend=all_mode=normal:all_opacity=0.60,format=yuv420p[v]" \
  -map "[v]" -map 0:a? -c:v libx264 -crf 18 -c:a copy salida_60.mp4
```

Esta es probablemente la técnica más útil de todo el módulo. **Casi ninguna LUT comercial se usa al
100%.** Entre 0.4 y 0.7 es lo normal.

### La trampa de las rutas en Windows

Dentro de un filtergraph, los dos puntos son separadores. Una ruta `C:\luts\mi.cube` rompe el
comando. Hay que escapar:

```bash
# En Git Bash / PowerShell, escapando los dos puntos
ffmpeg -i in.mp4 -vf "lut3d=file='C\:/luts/mi.cube':interp=tetrahedral" out.mp4
```

Lo más fácil es evitar el problema: pon las LUTs en una carpeta dentro del proyecto y usa rutas
relativas (`looks/mi.cube`). Cero dolores de cabeza.

---

## 4. LUT técnica: material en log

Si grabaste en un perfil plano (S-Log, V-Log, C-Log, D-Log de un dron, "Log" del celular con app
profesional), la imagen se ve gris, lavada y sin contraste **a propósito**: está guardando más
rango dinámico del que la pantalla puede mostrar.

Ese material **necesita** una LUT de conversión antes de cualquier otra cosa. No es opcional, no es
gusto: sin ella el material está incompleto.

El orden es:

```
material log → LUT técnica (log → Rec.709) → corrección → emparejado → LUT creativa / look
```

La LUT técnica te la da el fabricante de la cámara. **No la mezcles con una creativa** en el mismo
archivo: si algún día cambias de look, tendrías que rehacer la conversión también.

Cómo saber si tienes material log: se ve gris y plano, con negros levantados hacia el 15–20% y
blancos que no llegan al 80%. Míralo:

```bash
ffmpeg -hide_banner -ss 3 -t 3 -i clip.mp4 \
  -vf "signalstats,metadata=mode=print:file=-" -f null - 2>&1 | grep -E "YMIN|YMAX|SATAVG"
```

Si YMIN está por 40–60 y YMAX no pasa de 190, y encima SATAVG es bajísimo, es log (o está muy mal
expuesto, y eso también hay que saberlo).

---

## 5. Crear tu propia LUT

Tener la LUT de tu marca es la diferencia entre "cada video se ve parecido" y "cada video se ve
idéntico". Es un archivo que le pasas a cualquier editor —o a CapCut, o a Premiere— y aplica tu look
exacto sin que tenga que entender ffmpeg.

### Camino A — HALD CLUT (nativo de ffmpeg, el más fácil)

Una HALD CLUT es una **imagen PNG** que hace de LUT. ffmpeg la genera y la aplica solo.

```bash
# 1) Generar la tabla identidad (64x64x64 colores en un PNG de 512x512)
ffmpeg -y -f lavfi -i haldclutsrc=8 -frames:v 1 identidad.png

# 2) Aplicarle TU cadena de grado — este PNG resultante ES tu LUT
ffmpeg -y -i identidad.png -vf \
"hue=s=0,curves=r='0/0.035 0.5/0.52 1/1':g='0/0.086 0.5/0.55 1/1':b='0/0.227 0.5/0.62 1/1',eq=contrast=1.12" \
  mi_look.png

# 3) Usarla en cualquier video
ffmpeg -i entrada.mp4 -i mi_look.png -filter_complex "[0:v][1:v]haldclut,format=yuv420p" \
  -c:v libx264 -crf 18 -c:a copy salida.mp4
```

Ventaja: tres comandos y no necesitas nada más. Desventaja: el PNG solo lo entiende ffmpeg. Ni
Premiere ni DaVinci ni CapCut lo leen.

### Camino B — Generar un .cube de verdad

Si necesitas que otro editor lo use, tiene que ser `.cube`. ffmpeg no escribe `.cube`, pero se puede
hornear con un script corto: creas una imagen identidad con la rejilla, le pasas tu cadena de
filtros, y lees los píxeles de vuelta.

```python
# hornear_cube.py — requiere Pillow:  pip install pillow
# Uso: python hornear_cube.py "<cadena de filtros ffmpeg>" mi_look.cube
import subprocess, sys
from PIL import Image

CADENA, SALIDA, N = sys.argv[1], sys.argv[2], 33

# 1) identidad: ancho = N*N (azul x rojo), alto = N (verde)
ident = Image.new("RGB", (N*N, N))
px = ident.load()
for b in range(N):
    for g in range(N):
        for r in range(N):
            px[b*N + r, g] = (round(r*255/(N-1)), round(g*255/(N-1)), round(b*255/(N-1)))
ident.save("_ident.png")

# 2) aplicar la cadena (rgb24 de entrada y de salida para no perder por conversión a YUV)
subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", "_ident.png",
                "-vf", CADENA + ",format=rgb24", "-pix_fmt", "rgb24", "_grad.png"], check=True)

# 3) leer y escribir el .cube (el rojo varía primero)
out = Image.open("_grad.png").convert("RGB").load()
with open(SALIDA, "w") as f:
    f.write(f'TITLE "{SALIDA}"\nLUT_3D_SIZE {N}\nDOMAIN_MIN 0.0 0.0 0.0\nDOMAIN_MAX 1.0 1.0 1.0\n\n')
    for b in range(N):
        for g in range(N):
            for r in range(N):
                R, G, B = out[b*N + r, g]
                f.write(f"{R/255:.6f} {G/255:.6f} {B/255:.6f}\n")
print("Listo:", SALIDA)
```

```bash
python hornear_cube.py \
"curves=all='0/0.030 0.25/0.21 0.5/0.5 0.75/0.80 1/0.99',colorbalance=rs=-0.05:bs=0.07:rh=0.04:bh=-0.03,eq=saturation=1.04" \
  looks/gastro_v3.cube
```

**Aviso honesto:** algunos filtros de ffmpeg (`hue`, por ejemplo) trabajan internamente en YUV, y al
hornear vas a tener un redondeo de ±1 nivel. Para un look creativo es invisible. Para una conversión
técnica de precisión, no uses este método: usa la LUT del fabricante.

**Lo que NO se puede hornear en una LUT:** nada que dependa del vecino de cada píxel o del tiempo.
O sea: viñeta, desenfoque, nitidez (`unsharp`), grano, halación, estabilización. Todo eso es
espacial o temporal, y una LUT solo sabe traducir color por color. Esos van aparte, después de la
LUT (ver `66`).

---

## 6. Por qué una LUT no arregla un plano mal expuesto

Esta es la parte que hay que decirle a la gente y no se dice suficiente.

Una LUT dice "el color X pasa a ser el color Y". Punto. Es una traducción **fija, ciega y sin
contexto**. No sabe si tu plano está oscuro. No sabe que la ventana está quemada. Le da igual.

Entonces:

- **Plano subexpuesto** → la LUT recibe todo apiñado en la parte baja y lo traduce apiñado. Si la
  LUT además baja las sombras (casi todas lo hacen), el plano se te va a negro sólido.
- **Plano sobreexpuesto** → los blancos ya están en 235. La LUT los manda al mismo lugar. La
  información quemada sigue sin existir; nada la inventa.
- **Balance de blancos malo** → la LUT aplica su desviación **encima** de tu desviación. Un plano
  verdoso más una LUT que empuja al teal = un plano insalvable.
- **Material log al que no le pusiste la LUT técnica** → aplicas la creativa sobre log y sale un
  desastre gris con colores raros.

El orden correcto, siempre:

```
1. Normalizar (rango, espacio, LUT técnica si es log)
2. CORREGIR cada plano hasta neutro      ← aquí es donde se arregla la exposición
3. EMPAREJAR contra el plano de referencia
4. Recién ahora: LUT creativa
5. Textura: viñeta, nitidez, grano
```

Si te sientes tentado a "arreglarlo con la LUT", lo que estás diciendo en realidad es que te saltaste
el paso 2. Vuelve.

---

## 7. Cuándo una LUT sí vale la pena y cuándo estorba

**Vale la pena cuando:**
- Es la LUT técnica de tu cámara. Obligatoria.
- Tienes un look de marca definido y lo vas a repetir en 50 piezas.
- Trabajas con otros editores y necesitas que apliquen tu look sin explicarles nada.
- Quieres que el cliente pueda editar en CapCut manteniendo la identidad.

**Estorba cuando:**
- Bajaste un pack de "50 LUTs cinematográficas gratis" e intentas encontrar la que quede. Eso es
  ruleta, no color.
- Necesitas ajustar un plano específico: para eso está la corrección, no una LUT.
- El look que quieres incluye viñeta, grano o halación: eso no cabe en una LUT.
- Estás iterando el look todavía. Trabaja con la cadena de filtros y hornea la LUT **al final**,
  cuando ya no vas a cambiar.

---

## Errores comunes

- **Aplicar una LUT creativa a material log** sin convertirlo antes. Sale gris y con colores rotos.
- **Aplicar una LUT técnica de otra cámara.** Una LUT de S-Log3 sobre material de D-Log no traduce
  nada: inventa.
- **Usar la LUT al 100% siempre.** Casi todas están hechas para 40–70%. Usa el `blend`.
- **Creer que la LUT arregla la exposición.** No. Corrige primero.
- **Dejar `interp=trilinear` (o `nearest`) en la entrega.** Usa `tetrahedral`.
- **LUT hecha para rango completo aplicada a material limitado** (o al revés). Los negros se tapan o
  se lavan. Normaliza el rango antes (ver `60`).
- **Rutas de Windows sin escapar dentro del filtergraph.** El comando falla con un error críptico
  sobre "Option not found". Usa rutas relativas.
- **Aplicar dos LUTs encajadas** ("la técnica y la creativa juntas") sin saber cuál hace qué. Cuando
  algo salga mal no vas a saber dónde mirar.
- **Hornear una LUT que incluye viñeta o grano.** No se puede; esos efectos no son color por color.
- **Meter la LUT antes del emparejado.** Cada plano responde distinto y amplificas la disparidad.
- **Poner la LUT en el escritorio y perderla.** La LUT es un activo de marca: va en el repositorio
  del proyecto, con versión en el nombre (`gastro_look_v3.cube`).

---

## Checklist

- [ ] Sé si mi material es log. Si lo es, apliqué la LUT técnica del fabricante **primero**.
- [ ] Corregí y empareje los planos **antes** de tocar cualquier LUT creativa.
- [ ] La LUT creativa se aplica igual a todos los planos.
- [ ] Uso `interp=tetrahedral` en la entrega.
- [ ] Probé la LUT a distintas intensidades con `blend` y elegí una a propósito (no 100% por
      defecto).
- [ ] El rango (limitado/completo) de mi material coincide con el que espera la LUT.
- [ ] Los efectos espaciales (viñeta, nitidez, grano, halación) van **después** de la LUT, no dentro.
- [ ] Si horneé mi propia LUT, la generé al final del proceso creativo, no en medio.
- [ ] La LUT está versionada y guardada en el proyecto, no en el escritorio.
- [ ] Verifiqué el resultado con `signalstats` / scopes (`69`), no solo mirando.
- [ ] La piel sigue viéndose piel después de la LUT (`67`).
