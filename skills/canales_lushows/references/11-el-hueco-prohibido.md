# 11 · El hueco prohibido

**Qué resuelve:** el episodio tiene elementos suficientes pero se siente vacío, porque
están agrupados y dejan tramos en que sólo se ve el fondo moviéndose.

---

## La regla

**Ningún tramo del episodio puede quedarse con el fondo solo.** El fondo sostiene la
mirada, no la renueva: un `zoompan` del 12% durante tres segundos es exactamente lo
mismo que una foto fija para el ojo del espectador.

| Tramo con fondo solo | Cómo se lee |
|---|---|
| menos de 0,40 s | respiro entre elementos, invisible. No cuenta como hueco |
| 0,40 - 1,00 s | agujero: se nota que "faltó algo ahí" |
| 1,00 - 2,00 s | el espectador deja de mirar y empieza a escuchar |
| más de 2,00 s | se va del vídeo |

Umbral operativo: **0,40 s**. Por debajo no se persigue; por encima se corrige siempre,
salvo que sea un descanso declarado (`16`).

## ⚠️ Cero huecos no es pantalla llena: hay TRES fallos, no uno

El episodio 01 llegó a **0 huecos** y seguía viéndose vacío. El hueco es sólo el primero
de tres fallos distintos, y cada uno se mide aparte:

| Fallo | Qué es | Cómo se mide | Objetivo |
|---|---|---|---|
| **Hueco** | no hay NADA en pantalla | tramos con 0 elementos vivos | 0 tramos de más de 0,40 s |
| **Cuadro casi vacío** | hay algo, pero ocupa tan poco que se lee como fondo | superficie visible cubierta | ningún tramo bajo el 14% durante más de 0,8 s |
| **Cuadro descompensado** | está lleno, pero todo el peso en un rincón | superficie por mitad izquierda / derecha | ninguna mitad bajo el 4% durante más de 1 s |

**Medido en el episodio 01, con 0 huecos ya conseguidos:** 30% del episodio por debajo
del 14% de cuadro cubierto y 15% con el peso escorado a un lado. Los dos se ven en la
grilla de fotogramas y ninguno aparece en un contador de huecos.

Se corrigen en ese orden — no tiene sentido equilibrar un plano que todavía está vacío:

```
1. hueco              -> meter un elemento
2. cuadro casi vacio  -> agrandarlo, o acompanarlo con imagen (el TEXTO no llena:
                         un titular a 1500 px no pasa del 23% del lienzo)
3. descompensado      -> colocar el siguiente donde equilibre
```

## De dónde salen los huecos

| Origen | Firma en el auditor |
|---|---|
| La cola de la escena: todos los elementos anclados a las primeras palabras | huecos siempre en el último tercio de cada escena |
| Ancla sin coincidencia: el motor tira el elemento al inicio de escena | el auditor lista el ancla huérfana **y** un hueco al final |
| Un elemento corto entre dos largos que ya murieron | hueco corto (0,4-0,7 s) en mitad de la escena |
| Una escena declarada con pocos elementos "porque el fondo es bonito" | hueco largo (>2 s) y simultaneidad de escena por debajo de 1,0 |

## El detector

Se ejecuta **antes de renderizar**: la tabla de eventos ya tiene todos los datos, no
hace falta ver el vídeo. Reutiliza las funciones de `auditar.py` (módulo `17`).

```python
# huecos.py - lista los tramos en que el cuadro se queda con el fondo solo.
import json, os, sys
from auditar import cargar, vidas, huecos

BASE = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else ".")
gv = cargar(os.path.join(BASE, "guion_visual.py"))
with open(os.path.join(BASE, "audio", "tiempos.json"), encoding="utf-8") as f:
    tj = json.load(f)
iv, _ = vidas(gv.ESCENAS, tj["palabras"])
total = max(e["fin"] for e in gv.ESCENAS)
hu = huecos(iv, total, getattr(gv, "DESCANSOS", []))

for a, b in hu:
    esc = next((e["id"] for e in gv.ESCENAS if e["ini"] <= a < e["fin"]), "?")
    dicho = " ".join(p["w"] for p in tj["palabras"] if a - 0.3 <= p["t"] < b)
    print(f"{a:6.2f}-{b:6.2f}  {b-a:4.2f}s  '{esc}'  la voz dice: {dicho or '(silencio)'}")
print(f"\n{len(hu)} huecos · {sum(b-a for a,b in hu):.1f}s "
      f"= {sum(b-a for a,b in hu)/total*100:.0f}% del episodio")
```

**Lo que hace útil la salida es la última columna:** un hueco sobre `(silencio)` casi
siempre es un descanso legítimo; un hueco mientras la voz suelta una cifra es un fallo.

Salida real sobre el piloto:

```
 15.35- 15.83  0.48s  'penal'  la voz dice: un punto que ninguna
 22.69- 23.29  0.60s  'tunel'  la voz dice: (silencio)
 30.61- 35.19  4.58s  'moto'   la voz dice: sin agacharse. Construirlo tomó más de un año...
 43.65- 44.55  0.91s  'celda'  la voz dice: Para cuando sonó
```

## Las 6 maneras de rellenar un hueco sin ensuciar

Ordenadas de menos a más trabajo. Se prueba la 1 antes que la 6.

1. **Alargar el que sale.** Sumar `dura` al elemento anterior hasta empatar con el
   siguiente. Sólo hasta **+0,6 s**: pasado eso el elemento se queda clavado y hay que
   darle deriva o trocearlo (`13`).
2. **Adelantar el que entra.** Bajar el `offset` del siguiente hasta −0,6 s respecto a
   su palabra. Más allá de −0,6 s el elemento aparece antes de que la voz lo justifique
   y se lee como error de sincronía.
3. **Rótulo del elemento vivo.** Si algo sigue en pantalla, se le pone su etiqueta:
   nombre, fecha, expediente. Gratis en material (es texto) y obligatorio de todos
   modos por la regla de "cada elemento se explica" (`43`).
4. **Trocear en estados.** Una cifra fija se convierte en tres o cuatro PNG que se
   sustituyen (`cont_02`, `cont_05`, `cont_08`, `cont_10` en el piloto). Cada estado es
   un evento y el hueco desaparece sin añadir material nuevo.
5. **Micro-acento de marca.** Sello, tachado rojo, chincheta, clip, subrayado: entra
   0,6-1,0 s, no aporta información y por eso no puede confundir. Máximo **uno por
   escena**; dos seguidos delatan el relleno.
6. **Capa de suelo.** Un elemento pequeño pegado a un borde (ficha de caso, chapa de
   expediente, cinta de clasificación) que vive **toda la escena** por debajo de los
   demás. Elimina de golpe todos los huecos de esa escena y sube la simultaneidad
   media en +1,00 sin tocar nada más.

**Lo que NO vale como relleno:** un recorte de archivo que no empata con el fondo, un
elemento repetido a los tres segundos en la misma posición, o bajar la opacidad de algo
para "que acompañe" — el papel es opaco (regla del canal).

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Rellenar con el mismo recurso dos veces en la misma escena | Se lee como fallo de render, no como collage |
| Alargar el elemento saliente más de 0,6 s | Queda clavado: el hueco se cambia por un plano muerto |
| Tapar el hueco con un acento en cada escena | El sello pierde su valor de puntuación y pasa a ser mobiliario |
| Corregir huecos mirando el vídeo | Se pierden los de 0,5 s, que son la mayoría. Se detectan leyendo la tabla |
| Dar el hueco por bueno porque "ahí el fondo se ve bien" | El fondo se ve bien 1,5 s; a los 3 s es una foto fija |

## Relacionado

`10` densidad de eventos · `12` capas simultáneas · `13` ciclo de vida del elemento ·
`14` encadenar elementos · `16` el plano de descanso · `17` medir el montaje
