# 390 — La profundidad es separación medida

**Qué resuelve:** el cuadro tiene tres planos en la tabla de montaje y se ve plano en pantalla. El
diagnóstico habitual —"falta profundidad"— no es accionable. Este módulo convierte la profundidad en
**cuatro distancias con unidad**, para poder decir *cuánta* falta y *en qué eje*.

La frontera, para no perder el tiempo: `221` es la profundidad **óptica**, la que da el diafragma en
rodaje. Este bloque es la profundidad **compuesta**, la que se construye en el montaje sobre material
que ya está plano. Y `294`, pese al nombre, es el hermano **sonoro**: la profundidad de la mezcla.

---

## 1. Los cuatro ejes

Un plano no está "detrás". Está **a una distancia** del que tiene delante, y esa distancia se reparte
entre cuatro ejes que el ojo lee a la vez:

| Eje | Qué se mide | Unidad | Instrumento |
|---|---|---|---|
| **Tamaño** | altura aparente del elemento | % de la altura del lienzo | bbox del alfa |
| **Desenfoque** | acutancia: gradiente medio de Y dentro del alfa | ACUT, y su caída en % | `np.gradient` / `blurdetect` |
| **Contraste** | desviación típica de Y dentro del alfa | C, en niveles 0–255 | `signalstats` por región |
| **Saturación** | saturación media dentro del alfa | S, escala 0–100 | `SATAVG` / HSV |

La regla que ordena todo lo demás:

> Un plano de fondo al **92 % del tamaño** del sujeto, con **el mismo contraste** y **la misma
> saturación**, no es un plano de fondo. Es ruido a la misma distancia.

Y eso no es una opinión. Es lo que sale al medirlo (§4).

---

## 2. El medidor

`profundidad.py` devuelve las cuatro coordenadas de cualquier PNG con alfa. Todo el bloque 390–399 se
apoya en esta salida.

```python
#!/usr/bin/env python3
"""profundidad.py <glob> - las cuatro coordenadas de cada elemento."""
import glob, os, sys
import numpy as np
from PIL import Image

def ejes(png):
    im  = Image.open(png).convert("RGBA")
    a   = np.asarray(im)[:, :, 3]
    m   = a > 200                    # solo lo opaco: el halo no es el elemento
    if m.sum() < 50: return None
    rgb = np.asarray(im.convert("RGB")).astype(np.float32)
    Y   = 0.2126*rgb[:,:,0] + 0.7152*rgb[:,:,1] + 0.0722*rgb[:,:,2]
    mx, mn = rgb.max(2), rgb.min(2)
    S   = np.where(mx > 0, (mx-mn)/np.maximum(mx, 1e-6), 0) * 100
    gy, gx = np.gradient(Y)
    ys, xs = np.where(m)
    return dict(alto=int(ys.max()-ys.min()+1),
                Y=float(Y[m].mean()), C=float(Y[m].std()),
                S=float(S[m].mean()), A=float(np.hypot(gx, gy)[m].mean()))

print(f"{'elemento':<26}{'alto':>6}{'Y':>7}{'C':>7}{'S':>7}{'ACUT':>7}")
for p in sorted(glob.glob(sys.argv[1])):
    r = ejes(p)
    if r: print(f"{os.path.basename(p)[:25]:<26}{r['alto']:>6}{r['Y']:>7.1f}"
                f"{r['C']:>7.1f}{r['S']:>7.1f}{r['A']:>7.2f}")
```

**Por qué `a > 200` y no `a > 0`:** el borde semitransparente de un recorte arrastra color del fondo
original. Si entra en la media, dos recortes limpios salen con saturaciones distintas por culpa de su
procedencia, no de su plano. Ese borde es otro problema y vive en `canales 161`.

---

## 3. La salida real, sobre el banco del piloto

`CANALES-LUSHOWS/piloto/ep01-lustig/recortes`, 71 PNG de archivo histórico, medidos hoy. Extracto:

| Elemento | alto px | Y | C | S | ACUT |
|---|---|---|---|---|---|
| `agente_archivador` | 1773 | 112,6 | 69,4 | **3,2** | 4,26 |
| `celda_enseres` | 1467 | 144,7 | 56,0 | 18,2 | **2,85** |
| `retrato_lustig` | 1491 | 133,0 | 40,6 | 27,4 | 5,43 |
| `jardines_torre` | 1426 | 132,2 | 71,2 | 6,4 | **27,11** |
| `certificado_defuncion` | 1369 | 211,8 | 91,7 | **0,0** | 26,80 |
| `bono_20000` | 2044 | 159,1 | **105,0** | 8,1 | 22,81 |
| `coche_prensado` | 1660 | 88,1 | 43,7 | 21,5 | 3,37 |

Lo que la tabla dice antes de que nadie opine:

- **`jardines_torre` da ACUT 27,1 y `celda_enseres` 2,85: un factor 9,5.** En el mismo plano, el ojo se
  va a los jardines aunque la frase hable de la celda: el eje de desenfoque ya los está separando, solo
  que en la dirección equivocada.
- **Los documentos llegan con C por encima de 90 y S por debajo de 8.** Grabados en blanco y negro:
  nacen en un extremo de dos ejes. No se les puede pedir el mismo escalón que a una foto (`395`).
- **`agente_archivador` da S = 3,2 y `retrato_lustig` S = 27,4.** Dos retratos de la misma época; la
  diferencia es de la copia, no del plano. Antes de repartir profundidad hay que empatar procedencias
  (`263`, `canales 23`).

---

## 4. Lo que cada eje aporta, por separado

Prueba real: `retrato_lustig` a 620 px de ancho es el plano frente. Cada tratamiento se mide contra él.

| Variante | % tamaño | ΔC | ΔS | ΔACUT |
|---|---|---|---|---|
| 92 % y nada más | 92 | **+0,2 %** | **0,0 %** | **+2,9 %** |
| 65 % y nada más | 65 | −0,2 % | −0,1 % | **+15,7 %** |
| 92 % + medio escalón (σ 1,0 · sat 0,93 · br 0,98) | 92 | −4,6 % | −5,1 % | −36,2 % |
| 65 % + escalón suave (σ 1,2 · sat 0,90 · br 0,97) | 65 | −7,7 % | −8,1 % | −33,8 % |
| 65 % + receta `canales 22` (σ 2,4 · sat 0,83 · br 0,95) | 65 | −13,7 % | −14,8 % | −58,2 % |
| 55 % + receta fuerte (σ 3,2 · sat 0,80 · br 0,95) | 55 | −17,1 % | −17,8 % | −60,9 % |

Dos lecturas incómodas salen de ahí:

1. **Escalar no separa.** Bajar al 65 % dejó contraste y saturación clavados. Solo se movió el eje de
   tamaño, y el ojo lo compensa: un objeto pequeño y nítido se lee como *lejos pero enfocado*, que es
   exactamente lo que no existe en una fotografía.
2. **Escalar hacia abajo afila.** ACUT subió un **15,7 %** al reducir al 65 %: el remuestreo concentra
   el detalle en menos píxeles. Mandar algo al fondo por tamaño lo mueve en el eje de desenfoque **en
   la dirección contraria**. Lo desarrolla `392`.

---

## 5. El reparto mínimo

Un plano separa cuando cruza el umbral de **al menos tres de los cuatro ejes**. Se justifican en
`391`–`394`; aquí queda el resumen:

| Eje | Escalón mínimo que se lee | Techo: a partir de aquí parece un fallo |
|---|---|---|
| Tamaño | 25 % de diferencia de altura | 70 % (el pequeño desaparece: `canales 21`) |
| Desenfoque | −30 % de ACUT | −75 % (se lee como render roto) |
| Contraste | −8 % de C | −35 % (el elemento se vuelve una mancha) |
| Saturación | −10 % de S | −45 % (gris sucio, no lejanía) |

Con tres ejes cruzados y uno corto, hay profundidad. Con dos, hay una diferencia de escala. Con uno, no
hay nada: hay dos recortes, uno más pequeño. El único caso permitido de un solo eje es el documento que
hay que poder leer, y por eso tiene módulo propio: `395`.

---

## 6. Dónde vive cada cosa

Este bloque **mide**; no decide el look —eso es `directorcreativo_lushows`— y no prescribe los valores
del motor del canal documental: los cuatro planos, las derivas 1 : 2,2 : 3,6 y el cocinado del plano
medio con PIL ya están en **`canales 22`** y no se repiten. Aquí se responde la tercera pregunta:
**cuánta separación hay de verdad en el cuadro que acabo de renderizar.**

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Medir el PNG entero en vez de lo opaco | El halo mete el color del fondo original en la media |
| Llamar profundidad al orden de las capas | El orden decide quién tapa a quién, no a qué distancia está |
| Mover un solo eje | Un elemento pequeño y nítido no está lejos: está mal escalado |
| Reducir el tamaño creyendo que también desenfoca | Medido: reducir al 65 % subió ACUT un 15,7 % |
| Comparar ACUT entre elementos escalados a anchos distintos | El número depende del ancho; se compara a igual ancho |
| Buscar esto en `221` | Ése es el diafragma en rodaje; aquí no hay lente |
| Citar `294` como profundidad visual | Es de audio: reverb y paneo. El nombre engaña |
| Repartir profundidad antes de empatar procedencias | Dos copias de la misma época ya difieren 24 puntos de S |

## Relacionado

`391` el escalón de tamaño · `392` el escalón de desenfoque · `393` el escalón de contraste y color ·
`394` la sombra que asienta · `396` el plano que no separa · `399` comprobarlo sobre gris ·
`221` profundidad de campo (óptica, en rodaje) · `294` espacio y profundidad (**audio**) ·
`204` composición en capas · `263` integrar un elemento · `331` medir la separabilidad ·
`canales 22` profundidad por capas (la receta) · `canales 21` peso visual y jerarquía
