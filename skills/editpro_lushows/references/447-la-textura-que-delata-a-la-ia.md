# 447 — La textura que delata a la IA

`editpro/129` tiene la lista de lo que la IA hace mal (manos, texto, continuidad, física) y
`editpro/125` explica que la marca hay que imponérsela en post. Ninguno de los dos toca lo que este
módulo mide: **la superficie**. Una imagen generada puede tener las manos perfectas, la paleta
correcta y aun así leerse como generada, y el motivo casi siempre es que su textura tiene una
estadística que la materia real no tiene.

Lo mismo vale para un fondo hecho con degradados en Chrome, que es el caso del canal: no lo generó un
modelo, pero comparte el mismo defecto.

---

## 1. Las dos huellas, y se miden

```python
import numpy as np
from PIL import Image

def bloques(a, n=16):
    h, w = a.shape; h, w = h - h % n, w - w % n
    return a[:h, :w].reshape(h//n, n, w//n, n).swapaxes(1, 2).reshape(-1, n, n)

def huella(im):
    """Energía de alta frecuencia por bloque de 16x16 (laplaciano 3x3)."""
    a = np.asarray(im.convert("L"), dtype=np.float32)
    b = bloques(a)
    lap = (b[:,1:-1,1:-1]*4 - b[:,:-2,1:-1] - b[:,2:,1:-1] - b[:,1:-1,:-2] - b[:,1:-1,2:])
    e = lap.std(axis=(1, 2))
    suelo = np.sort(e)[:max(1, len(e)//20)].mean()     # el 5% de bloques MÁS planos
    return suelo, float(np.median(e)), float(np.percentile(e, 95))
```

**Huella 1 — el suelo de ruido.** En el 5 % de bloques más planos de una foto real **nunca** hay
cero: hay ruido de sensor, grano de película o ruido de escaneo. Un degradado sintético tiene
exactamente cero.

**Huella 2 — la razón p95 / suelo.** En materia real la textura está *estructurada*: mucha energía
donde hay detalle, poca donde no. Una capa de grano uniforme encima aplana esa razón, porque pone la
misma cantidad de ruido en todas partes.

---

## 2. Medido sobre material real del canal

| pieza | suelo | mediana | p95 | **p95 / suelo** |
|---|---|---|---|---|
| `cartel_fbi.png` (impreso, escaneado) | 11,138 | 27,050 | 153,77 | **13,8** |
| `carcel_estampa.png` (grabado) | 4,531 | 20,418 | 63,43 | **14,0** |
| `automovil_1927.png` (foto de archivo) | 4,094 | 17,175 | 63,10 | **15,4** |
| `billetes_falsos.png` | 2,749 | 13,257 | 34,02 | 12,4 |
| `calle_paris.png` | 2,542 | 15,115 | 26,85 | 10,6 |
| fotograma de episodio terminado | 2,881 | 10,854 | 43,64 | 15,1 |
| **degradado generado, desnudo** | **0,000** | 0,357 | 0,66 | **1,27** |
| **el mismo, con manta de grano uniforme** | 11,711 | 13,430 | 14,89 | **1,27** |
| fondo real del canal (`f_oficio`, 4320×2430) | 6,797 | 10,463 | 13,77 | 2,03 |
| fondo real del canal (`f_nombre`) | 1,620 | 4,123 | 10,84 | 6,69 |

Lo que hay que leer aquí no es obvio:

- **Suelo cero.** El degradado desnudo no tiene nada en las zonas planas. Ni ruido, ni fibra. Es el
  aspecto de «renderizado», el que la gente describe como *demasiado limpio*.
- **La manta de grano sube el suelo y no mueve la razón.** 0,000 → 11,711 de suelo, y la razón se
  queda clavada en 1,27 con σ 0,5 y con σ 8,0. Porque **la razón es una propiedad del contenido, no
  del ruido**: un degradado no tiene estructura, y ninguna cantidad de ruido se la da.
- **Los fondos reales del canal ya no están en 1,27.** Las tres tramas cruzadas de periodo primo de
  `piloto/episodio01/fondos.py` les dan suelo (1,6 – 6,8) y razón (2,0 – 6,7). La estructura viene de
  la trama, no del grano. Eso es lo que hay que copiar.

---

## 3. La razón es un presupuesto, y el grano lo gasta

El hallazgo que cambia cómo se dosifica el grano: sobre material **con** estructura, cada punto de
ruido uniforme que añades **baja** la razón. Medido sobre un fotograma de collage real:

| σ del ruido uniforme añadido | suelo | p95 | **razón** |
|---|---|---|---|
| 0 (original) | 2,881 | 43,64 | **15,15** |
| 0,5 | 4,144 | 43,69 | 10,54 |
| **0,99 (= `noise=alls=5:allf=t+u`)** | 5,354 | 43,79 | **8,18** |
| 2,0 | 8,463 | 44,23 | 5,23 |
| 3,0 | 11,751 | 45,12 | 3,84 |

El p95 casi no se mueve (43,6 → 45,1): el ruido no añade detalle. Lo que sube es el suelo, y la razón
cae con él.

> **`noise=alls=5` aplicado a todo el cuadro saca el collage del rango en el que vive el material de
> archivo real (10–16) y lo deja en 8,18.** No es un matiz: es la diferencia entre «archivo» y
> «archivo con filtro».

Y por eso los objetivos no son uno solo, sino uno **por tipo de capa**:

| Capa | suelo | razón p95/suelo |
|---|---|---|
| Recorte de archivo, foto, documento | 2 – 12 | **10 – 16** |
| Fondo del canal (es una superficie, no una foto) | 1,5 – 7 | **2 – 7** |
| Cualquier cosa con suelo 0,000 | — | rechazar: no es materia |
| Cualquier cosa con razón ≈ 1,3 y suelo alto | — | rechazar: es una manta |

Cumplir uno solo no sirve. Y como el objetivo es distinto por capa, el grano no puede ser global: eso
es `editpro/448`.

---

## 4. El otro delator: el color, y la métrica correcta

La textura no es el único rasgo. El segundo es que el material generado (o moderno) **tiene demasiados
tonos vivos** para el resto del montaje. La tentación es medir saturación y comprobar que baja al
envejecer. **No baja de forma monótona**: medido sobre una foto real, 61,1 → 48,0 → 52,5 según sube el
grado de virado, porque el sepia tiene saturación propia. Un control de calidad basado en saturación
aprueba el grado 0,45 y rechaza el 0,90, que es justo al revés.

La medida que sí sirve es la **dispersión de tono** —vector medio circular pesado por saturación,
umbral ≤ 0,005—, y está resuelta, con función y tabla por tipo de material, en `canales/197`. Úsala
tal cual; aquí no se reescribe.

Las dos métricas son independientes y hacen falta las dos:

| | textura (suelo, razón) | color (dispersión de tono) |
|---|---|---|
| Foto moderna a todo color | puede estar bien | **0,606** — canta |
| Degradado generado desnudo | **suelo 0,000** — canta | 0,000 — perfecto |
| El mismo + manta de grano | suelo 11,7 / **razón 1,27** — canta | 0,000 — perfecto |
| Recorte de archivo + `alls=5` global | **razón 8,18** — fuera de rango | correcto |

---

## 5. Lo que la textura no puede arreglar

Un anacronismo (`canales/198`), una mano de seis dedos (`editpro/129`) o una marca que la IA se
inventó (`editpro/125`). Una pieza con el suelo y la razón perfectos y un coche de 2021 dentro de una
escena de 1927 sigue estando mal, y ahora además parece una falsificación cuidada. Cuando el problema
es el contenido, la pieza se descarta.

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Tapar un degradado generado con una manta de grano | Sube el suelo y la razón no se mueve: sigue sin estructura |
| Añadir estructura con ruido en vez de con trama | El ruido no sube el p95; la estructura hay que dibujarla |
| Comprobar solo el suelo de ruido | Se aprueba una manta uniforme |
| Comprobar solo la razón | Se aprueba una imagen con suelo cero y mucho contraste |
| Exigirle a un fondo la razón de una foto | Un fondo es una superficie: su rango es 2–7, no 10–16 |
| Grano global sobre un collage de archivo | Razón 15,15 → 8,18: fuera del rango del material real |
| Medir el color por saturación | No es monótona; aprueba al revés (`canales/197`) |
| Afilar material generado | Ya viene sobreafilado: lo que le falta es suelo de ruido, no nitidez (`editpro/66`) |
| Medir la huella sobre la imagen ya comprimida | La compresión pone su propio suelo (bloques) y falsea los dos números |
| Aplicar el mismo tratamiento a un documento | El documento está para leerse; virarlo o granularlo le quita legibilidad |
| Creer que arreglando la superficie se arregla el contenido | Un anacronismo bien texturado sigue siendo un anacronismo |

---

## Relacionado

`editpro/129` lo que la IA todavía hace mal · `editpro/125` la IA no respeta tu marca ·
`editpro/448` textura por capa, no global · `editpro/449` medir si la textura suma ·
`editpro/440` grano: por qué y cuánto · `editpro/442` papel, polvo y arañazo ·
`canales/197` envejecer para que empate (dispersión de tono, umbral 0,005) ·
`canales/198` el anacronismo · `canales/23` empatar recorte y fondo · `canales/68` efectos que se ven
baratos
