# 61 — Corrección vs gradación: el orden sagrado

Hay una sola regla en este bloque que no se negocia nunca:

> **Primero se CORRIGE. Después se GRADÚA.**
> Corregir es dejar cada plano neutro y parejo con los demás.
> Graduar es darle el look a todo el video, ya emparejado.
> **Hacerlo al revés produce un desastre imposible de arreglar.**

Si te llevas una sola cosa de todo el bloque 6, que sea esta. No es teoría de escuela: es la
diferencia entre un video que se ve de una sola pieza y uno que parece un collage de clips que
nadie revisó.

---

## 1. Qué es corregir (technical grade)

Corregir es **quitarle los defectos al plano**. Es reparación, no autoría. El objetivo es que el
plano quede **neutro**: blancos blancos, negros negros, piel con color de piel, exposición
razonable. Nada bonito todavía. Solo correcto.

Lo que se hace al corregir:

| Problema | Herramienta | Cómo se ve el defecto |
|---|---|---|
| Está muy oscuro / muy claro | `eq=gamma=`, `curves` | no se le ve la cara o está reventado |
| Los negros están grises | `curves` punto negro, `eq=contrast=` | video "lavado", sin peso |
| Los blancos están apagados | `curves` punto blanco | se ve mate, como con neblina |
| Domina un color (balance de blancos) | `colorbalance`, `colortemperature` | todo azul, todo amarillo, todo verde |
| El plano está más saturado que el resto | `eq=saturation=` | ese clip "grita" al lado de los otros |
| Rango mal interpretado | `scale=in_range=..:out_range=..` | ver `60` |

Un ejemplo real de corrección de un plano grabado bajo luz de tubo fluorescente (verdoso y frío):

```bash
ffmpeg -i plano_cocina.mp4 -vf \
  "colorbalance=gm=-0.06:gh=-0.04,colortemperature=temperature=5000,eq=gamma=1.04:contrast=1.03" \
  -c:v libx264 -crf 16 -c:a copy plano_cocina_CORREGIDO.mp4
```

Fíjate en la escala de los números: `-0.06`, `1.04`, `1.03`. **La corrección se hace con números
pequeños.** Si estás moviendo algo un 40%, no estás corrigiendo: estás tapando un problema de
rodaje, y eso se ve.

### Cómo sabes que un plano ya está corregido

No por gusto: por medida.

```bash
ffmpeg -hide_banner -ss 3 -t 3 -i plano_cocina_CORREGIDO.mp4 \
  -vf "signalstats,metadata=mode=print:file=-" -f null - 2>&1 \
  | grep -E "YMIN|YAVG|YMAX|UAVG|VAVG"
```

Lo que buscas:
- **YMIN** cerca de 16 pero no clavado en 16 (si está clavado, tapaste sombras).
- **YMAX** cerca de 235 pero no clavado (si está clavado, quemaste luces).
- **UAVG y VAVG** cerca de 128 en un plano de contenido neutro. Si UAVG está en 140, el plano tira
  a azul. Si VAVG está en 140, tira a rojo. (Ojo: en un plano dominado por un objeto rojo grande,
  esto se desvía legítimamente. La medida se lee con cabeza.)

---

## 2. Qué es graduar (creative grade)

Graduar es **decidir cómo se siente el video**. Ya no reparas: autoreas. Es donde nace el "look".

Lo que se hace al graduar:

- **Contraste con carácter** — curva en S, negros con un poco de levante, blancos apretados.
- **Temperatura emocional** — sombras hacia el azul/teal, luces hacia el naranja/dorado.
- **Saturación selectiva** — bajar el verde de la vegetación, subir el rojo de la marca.
- **Paleta impuesta** — duotono de marca, mapeo total de color (ver `64`).
- **Textura** — grano, halación, viñeta (ver `66`).

Y aquí está la clave: **la gradación se aplica a TODOS los planos por igual**. Una sola cadena de
filtros, o una sola LUT, encima de material que ya está parejo.

```bash
# El look va DESPUÉS, e idéntico para todos
LOOK="curves=all='0/0.02 0.25/0.21 0.5/0.5 0.75/0.79 1/0.98',eq=saturation=1.08,vignette=PI/5"

for f in planos_corregidos/*.mp4; do
  ffmpeg -i "$f" -vf "$LOOK,format=yuv420p" -c:v libx264 -crf 18 -c:a copy \
    "planos_graduados/$(basename "$f")"
done
```

---

## 3. Por qué el orden invertido es un desastre

Esto no es dogma. Es aritmética.

Imagínate dos planos del mismo bar: uno con luz de neón morado (croma cargado al magenta), otro en
la terraza a plena luz de día (neutro). Si le aplicas primero el look —digamos una curva que empuja
sombras al teal— pasa esto:

- En el plano **neutro**, el teal cae sobre sombras neutras: se ve como quisiste.
- En el plano **morado**, el teal cae sobre sombras que ya eran magenta. Magenta + teal = gris
  sucio. Las sombras de ese plano se te vuelven barro.

Ahora intenta arreglarlo. Ya no puedes corregir el morado, porque el morado está **mezclado con tu
look**. Cualquier cosa que hagas para quitar el magenta se lleva también tu gradación. Estás
peleando contra tu propia decisión creativa. Por eso "imposible de arreglar" no es exageración: la
única salida real es volver al bruto y empezar de nuevo.

En orden correcto:

1. Corriges el plano morado → sus sombras quedan neutras.
2. Corriges el plano de terraza → sus sombras quedan neutras.
3. Aplicas el teal a los dos → **los dos responden igual**, porque partían del mismo punto.

Esa es toda la magia. La corrección existe para que la gradación tenga un punto de partida común.

---

## 4. El orden completo de la cadena

Este es el orden en que se apilan los filtros dentro de un `-vf`. No es arbitrario: cada paso
asume que el anterior ya se hizo.

```
1. Normalizar técnico     → rango, espacio, pix_fmt, tonemapping si viene HDR
2. Estabilizar / reencuadrar → porque recortar cambia lo que hay en cuadro
3. CORREGIR               → exposición, balance de blancos, contraste base, saturación base
4. EMPAREJAR              → ajustar cada plano contra el plano de referencia (ver 62)
   ────────── aquí termina la corrección; a partir de acá todo es igual para todos ──────────
5. GRADUAR                → curva de look, saturación creativa, paleta de marca
6. PROTEGER PIEL          → si el look movió los tonos de piel (ver 67)
7. TEXTURA                → nitidez, halación, grano, viñeta (ver 66)
8. Formato de salida      → format=yuv420p + etiquetas
```

Ejemplo de una cadena completa sobre un plano ya seleccionado:

```bash
ffmpeg -i bruto/bar_neon_03.mp4 -vf "\
scale=in_range=limited:out_range=limited,\
crop=iw*0.92:ih*0.92:(iw-iw*0.92)/2:(ih-ih*0.92)/2,\
colorbalance=rm=-0.04:bm=0.02,eq=gamma=1.05:contrast=1.04:saturation=0.96,\
curves=all='0/0.02 0.25/0.22 0.5/0.5 0.75/0.78 1/0.98',eq=saturation=1.06,\
unsharp=5:5:0.5:5:5:0.0,vignette=PI/5,\
format=yuv420p" \
  -c:v libx264 -crf 17 -preset slow \
  -colorspace bt709 -color_primaries bt709 -color_trc bt709 -color_range tv \
  -c:a copy final/bar_neon_03.mp4
```

Léela de arriba abajo y vas a reconocer los pasos: normalizar, reencuadrar, corregir, graduar,
textura, formato.

---

## 5. La práctica que te salva: dos pasadas y archivos intermedios

La tentación es hacer todo en un solo comando por cada clip. Funciona, pero cuando el cliente pide
"el look un poco menos verde", te toca volver a correr la corrección de los doce clips.

El flujo profesional son **dos pasadas con material intermedio**:

**Pasada 1 — corrección, un comando distinto por clip.** Guarda en calidad alta (CRF bajo o
directamente ProRes / x264 sin pérdida visible), porque este archivo se va a volver a codificar:

```bash
ffmpeg -i bruto/terraza_01.mp4 -vf "eq=gamma=1.02:saturation=1.02,format=yuv420p" \
  -c:v libx264 -crf 14 -preset medium -c:a copy corregido/terraza_01.mp4

ffmpeg -i bruto/bar_neon_03.mp4 -vf "colorbalance=rm=-0.05:bm=0.02,eq=gamma=1.06,format=yuv420p" \
  -c:v libx264 -crf 14 -preset medium -c:a copy corregido/bar_neon_03.mp4
```

**Pasada 2 — gradación, el MISMO comando para todos:**

```bash
for f in corregido/*.mp4; do
  ffmpeg -y -i "$f" -vf \
    "curves=all='0/0.02 0.25/0.22 0.5/0.5 0.75/0.78 1/0.98',eq=saturation=1.06,unsharp=5:5:0.4:5:5:0.0,vignette=PI/5,format=yuv420p" \
    -c:v libx264 -crf 18 -preset slow -c:a copy "graduado/$(basename "$f")"
done
```

Si el cliente pide cambiar el look, tocas **una línea** y vuelves a correr la pasada 2. La
corrección no se toca. Esa es toda la ganancia, y es enorme.

> **CRF 14 en el intermedio no es paranoia.** Estás codificando dos veces; el intermedio tiene que
> tener margen. Si dejas el intermedio en CRF 23, la segunda pasada amplifica los artefactos de la
> primera y aparecen bloques en las sombras.

---

## 6. Cómo saber en cuál de las dos estás

Cuando te pierdas en un proyecto, hazte esta pregunta:

**"¿Este ajuste lo aplicaría igual a todos los planos?"**

- **No, este plano necesita algo distinto** → es **corrección**. Va en la pasada 1.
- **Sí, todos igual** → es **gradación**. Va en la pasada 2.

Es infalible. "Subirle el gamma porque este plano quedó oscuro" es corrección (solo ese lo
necesita). "Meterle una curva en S" es gradación (todos igual). "Bajarle el verde a este plano
porque el tubo fluorescente lo puso verde" es corrección. "Bajarle el verde a todo el video porque
la marca no tiene verde" es gradación.

---

## 7. El caso extremo: cuando la corrección no alcanza

Hay material que no se puede corregir. Sé honesto y dilo:

- **Blancos reventados** — si YMAX está clavado en 235 en un área grande, esa información **no
  existe**. Bajarle el brillo solo te da gris plano. No se recupera. Se reencuadra para sacar la
  ventana quemada del cuadro, o se descarta el plano.
- **Negros tapados** — igual al revés. Subir gamma solo saca ruido de compresión.
- **Movimiento borroso (motion blur) por obturador lento** — la nitidez no se inventa. `unsharp`
  solo hace más evidente el borrón.
- **Balance de blancos catastrófico en H.264 de 8 bits** — corregir un plano naranja intenso hacia
  neutro te deja banding visible en las paredes. A veces la mejor decisión es **abrazar el color**:
  volverlo intencional en la gradación en vez de pelearlo.

Decirle al cliente "este plano no se salva, mejor lo sacamos o lo asumimos como look" es un acto
profesional, no una derrota. Lo contrario —entregarle un plano manoseado que igual se ve mal— sí lo
es.

---

## Errores comunes

- **Aplicar la LUT o el look antes de emparejar.** El error madre. Todo lo demás sale de aquí.
- **Corregir con números grandes.** Si mueves algo más de ~15%, no estás corrigiendo: estás tapando.
  Revisa si el problema es de rango (ver `60`) antes de forzar la mano.
- **Hacer todo en un solo comando y no guardar el intermedio corregido.** Al primer cambio de look
  repites todo el trabajo.
- **Guardar el intermedio con CRF alto.** La doble codificación amplifica artefactos. CRF 14–16 o
  un códec intermedio.
- **Corregir mirando un solo fotograma.** El plano cambia: alguien se mueve, entra una nube. Mide
  al menos 3 puntos del clip.
- **Confundir "neutro" con "aburrido" y saltarse la corrección para no perder el ambiente.** El
  ambiente lo pones tú en la gradación, a propósito y de forma reproducible. El ambiente que traía
  el plano por accidente no es tuyo, es del tubo fluorescente.
- **Corregir y graduar en la misma cadena y después no poder explicar qué hizo qué.** Separa con un
  comentario o parte los comandos.
- **Insistir en salvar un plano quemado.** Reencuadra o descártalo, y dilo.
- **Aplicar `eq=saturation` dos veces (una en corrección, otra en gradación) sin darte cuenta.** Se
  multiplican: 1.1 × 1.1 = 1.21, y ahí ya la piel empieza a naranjearse.

---

## Checklist

- [ ] Sé cuál es mi **plano de referencia** (el mejor expuesto, el que define el look) — ver `62`.
- [ ] Cada plano tiene su propio comando de **corrección**, con números pequeños.
- [ ] Verifiqué con `signalstats` que ningún plano corregido tiene YMIN clavado en 16 ni YMAX
      clavado en 235 por culpa mía.
- [ ] Los planos corregidos están guardados en una carpeta aparte, en calidad alta (CRF ≤ 16).
- [ ] La **gradación** es una sola cadena de filtros, idéntica para todos los planos.
- [ ] Puedo cambiar el look tocando una sola línea, sin repetir la corrección.
- [ ] No hay `eq=saturation` duplicado entre las dos etapas.
- [ ] La piel sigue viéndose piel después del look (ver `67`).
- [ ] Los planos que no se pueden salvar están identificados y se lo dije al cliente.
- [ ] El export final lleva `format=yuv420p` y las etiquetas de color.
