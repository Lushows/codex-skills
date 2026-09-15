# 58 · Coherencia entre fondos

**Qué resuelve:** que los seis fondos se vean del mismo episodio y del mismo canal. La
variedad la da el color (`51`); la unidad la dan un puñado de cosas que **no cambian
nunca**. Este módulo separa unas de otras.

---

## La tabla de constantes y variables

| Rasgo | Constante | Variable |
|---|---|---|
| Lienzo 1920×1080 @2,25× | ✅ siempre | — |
| Capa de superficie (`#sup`, `.26`, `overlay`) | ✅ misma opacidad y semilla | — |
| Capa de grano (`#ruido`, `.22`, `overlay`) | ✅ | — |
| Geometría de la viñeta (`76% 70% at 50% 48%`, corte al 34%) | ✅ | Solo el alfa: `.56-.68` |
| Suelo del degradado (esquina más oscura) | ✅ `#080D0B`–`#14110C` | — |
| Grosor de línea (1-3 px) y esquinas a 90° | ✅ | — |
| El rojo `#E3120B` solo como acento | ✅ | — |
| Tono base del degradado | — | ✅ por escena |
| Familia de textura | — | ✅ por escena |
| Posición y color del punto de luz | — | ✅ por escena |
| Cantidad de detalle | — | ✅ datos alto, retrato bajo |

Regla corta: **cambia el color y la materia; no cambia la piel ni la geometría.**

## Por qué el grano es lo que más une

Las tres capas finales (`tex`, `vin`, `gra`) van con la misma semilla de `feTurbulence` en
las seis escenas. Eso hace que el mismo patrón de ruido recorra el episodio entero, y es lo
que el ojo interpreta como "una sola película". Cambiar `seed` entre escenas rompe esa
unidad aunque nadie sepa decir por qué.

En `fondos.py` esto está resuelto con una función única:

```python
def capas(vin=".62"):
    return f"""
<svg class="tex" viewBox="0 0 1920 1080" preserveAspectRatio="none">
  <rect width="1920" height="1080" filter="url(#sup)"/></svg>
<div class="vin" style="background:radial-gradient(76% 70% at 50% 48%,
  transparent 34%,rgba(0,0,0,{vin}) 100%)"></div>
<svg class="gra" viewBox="0 0 1920 1080" preserveAspectRatio="none">
  <rect width="1920" height="1080" filter="url(#ruido)"/></svg>"""
```

**Si una escena necesita capas propias, está mal planteada.** El único parámetro que se le
pasa es el alfa de la viñeta.

## Las cuatro pruebas

### 1 · Hoja de contactos
Los seis fondos en 3×2 (comando en `51`). Se mira a un metro de distancia:

- ¿Se distinguen seis escenas? → si no, falta recorrido de color.
- ¿Parecen de seis canales distintos? → sobra recorrido; hay que acercar tonos base.

### 2 · Prueba del gris
```bash
ffmpeg -y -i render/_paleta.png -vf "hue=s=0" render/_paleta_gris.png
```
En blanco y negro las seis deben tener **una estructura de luz parecida** (claro arriba o
en un lado, oscuro en los bordes) y **luminosidad media parecida**. Si una salta, esa es la
que se ve "de otro vídeo".

### 3 · Prueba de la miniatura
Reducir la hoja de contactos a 320 px de ancho. A ese tamaño solo sobreviven el color y el
punto de luz. Si a 320 px hay dos fondos idénticos, en el vídeo también lo son.

### 4 · Medición de niveles
```bash
for f in render/f_*.png; do
  v=$(ffmpeg -hide_banner -i "$f" -vf "signalstats,metadata=print:file=-" -f null - \
      2>/dev/null | grep -E "YAVG|YMAX=|SATAVG" | tr '\n' ' ')
  echo "$f :: $v"
done
```

**Nunca con `-v error`**: silencia la impresión y la orden devuelve vacío.

Medición real de los seis fondos del episodio 01 —el que salió marrón—:

| Fondo | `YAVG` | `YMAX` | `SATAVG` |
|---|---|---|---|
| f_gancho | 40,1 | 96 | 4,9 |
| f_maquina | 55,6 | 91 | **2,4** |
| f_peso | 49,3 | 82 | 5,6 |
| f_piezas | 34,3 | **70** | 7,0 |
| f_pregunta | 36,9 | 80 | 6,9 |
| f_remate | 49,2 | **72** | 3,6 |

| Métrica | Rango sano | Si se sale |
|---|---|---|
| `YAVG` | 34-58 | Menos: ahogado. Más: lavado |
| `YMAX` | 100-130 | < 90: falta punto de luz (`53`) |
| `SATAVG` | ≥ 8, y ≥ 10 en dos escenas al menos | < 6: gris sucio — el marrón del ep. 01 |

Con viñeta y grano encima, un fondo de este canal no pasa de `YMAX` 130: el umbral útil no
es "blanco puro", es 90. Y la dispersión importa tanto como el valor: si un `YAVG` está en
38 y otro en 71, la segunda escena se siente de otro episodio.

## Coherencia entre episodios

Lo que hace canal, no episodio:

1. Las tres capas finales, idénticas siempre.
2. El negro tinta `#12100C` como suelo.
3. El rojo `#E3120B` reservado.
4. Líneas rectas, sin esquinas redondeadas, sin sombras suaves de interfaz.
5. Una textura de guilloché en algún punto de cada episodio: es la firma temática.

Lo que puede cambiar de un episodio a otro: la **familia dominante de temperatura**. El
caso de un contrabandista puede vivir en ocres y el de un banquero en aceros. Dentro del
episodio, la alternancia sigue mandando.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Cambiar `seed` o la opacidad del grano entre escenas | Se rompe la piel común y no se sabe por qué |
| Cada fondo con su geometría de viñeta | Los cortes saltan de brillo |
| Un fondo mucho más detallado que el resto | Se lee como plantilla ajena |
| Esquinas redondeadas o sombras difusas en el fondo | Lenguaje de interfaz, no de documental |
| Corregir a ojo sin medir | Se ajusta la escena equivocada |
| Repetir la paleta exacta del episodio anterior | El canal deja de tener variedad entre casos |

## Relacionado

`50` · `51` · `52` · `53` · `57` · `59` · `66` grano y textura
