# 396 — El plano que no separa

**Qué resuelve:** la tabla de montaje dice que hay tres planos. El cuadro dice que hay tres recortes.
Este módulo es el diagnóstico: **un script que señala qué eje está en cero**, y el catálogo de los
cinco planos falsos que se repiten siempre.

Es la contracara de `390`: allí se define la distancia, aquí se detecta su ausencia.

---

## 1. El diagnóstico

`separa.py` compara cualquier elemento contra el plano frente y dice, eje por eje, si cruza el umbral.

```python
#!/usr/bin/env python3
"""separa.py <frente.png> <ancho_frente> <candidato.png> <ancho_candidato>"""
import sys
import numpy as np
from PIL import Image

UMBRAL = {"tamano": 25.0, "acut": 30.0, "contraste": 8.0, "saturacion": 10.0}

def ejes(png, w):
    im = Image.open(png).convert("RGBA")
    im = im.resize((w, round(im.height*w/im.width)), Image.LANCZOS)
    a  = np.asarray(im)[:, :, 3]; m = a > 200
    rgb = np.asarray(im.convert("RGB")).astype(np.float32)
    Y = 0.2126*rgb[:,:,0] + 0.7152*rgb[:,:,1] + 0.0722*rgb[:,:,2]
    mx, mn = rgb.max(2), rgb.min(2)
    S = np.where(mx > 0, (mx-mn)/np.maximum(mx, 1e-6), 0)*100
    gy, gx = np.gradient(Y); ys = np.where(m)[0]
    return dict(alto=ys.max()-ys.min()+1, C=Y[m].std(), S=S[m].mean(),
                A=np.hypot(gx, gy)[m].mean())

f = ejes(sys.argv[1], int(sys.argv[2]))
c = ejes(sys.argv[3], int(sys.argv[4]))
d = {"tamano":     100*(1 - c["alto"]/f["alto"]),
     "acut":       100*(1 - c["A"]/f["A"]),
     "contraste":  100*(1 - c["C"]/f["C"]),
     "saturacion": 100*(1 - c["S"]/f["S"])}
ok = 0
for eje, v in d.items():
    cruza = v >= UMBRAL[eje]; ok += cruza
    print(f"{eje:<12}{v:>8.1f}%  umbral {UMBRAL[eje]:>5.1f}%   {'OK' if cruza else '--- PLANO'}")
print(f"\nejes cruzados: {ok}/4  ->  "
      f"{'separa' if ok >= 3 else 'NO SEPARA: es el mismo plano con otro tamano'}")
```

**Un eje negativo no es un fallo del script.** Significa que ese eje va al revés: el candidato está más
afilado, más contrastado o más saturado que el frente. Ocurre constantemente con el tamaño (`392`) y es
información, no ruido.

---

## 2. El caso que da nombre al bloque

`retrato_lustig` a 620 px es el frente. El mismo archivo a 570 px, sin tocar nada más, como "plano de
fondo":

| Eje | Distancia medida | Umbral | Veredicto |
|---|---|---|---|
| tamaño | 8,1 % | 25 % | --- PLANO |
| acutancia | **−2,9 %** | 30 % | --- PLANO |
| contraste | **−0,2 %** | 8 % | --- PLANO |
| saturación | **−0,0 %** | 10 % | --- PLANO |

**0 de 4.** Y no es un caso de laboratorio: es exactamente lo que sale cuando alguien coge un recorte,
lo arrastra "un poco más pequeño" y lo manda a la pista de abajo.

---

## 3. Los cinco planos falsos

### 3.1. El del 8 %
El de arriba. Se arregla con el escalón de `391`: al 75 % o menos, y pagando los otros ejes.

### 3.2. El que solo separa por tamaño
Cruza tamaño y **suspende los otros tres**. Se lee como *lejos pero enfocado*, que no existe en ninguna
fotografía. Peor: al reducirlo subió la acutancia un 15,7 %, así que el eje de desenfoque está en
contra. Es el plano falso más común de todos porque escalar es lo único que cuesta un arrastre.

### 3.3. El que la sombra desmiente
Cruza los cuatro ejes y **sigue leyéndose mal**, porque arrastra la sombra del plano frente
(contacto 7,5 cuando le tocaba 3–5). El desenfoque dice lejos y la sombra dice pegado aquí (`394`).
Síntoma característico: nadie sabe qué está mal, y todos proponen subirle el desenfoque.

### 3.4. El que se apoya en el fondo, no en el escalón
El elemento parece separado porque cae sobre una zona oscura del fondo. Sobre el fondo real de
`f_torre`, `retrato_lustig` da **ΔY = 54,4** con lo que tiene detrás; sobre gris 128 esa diferencia cae
a **8,1**. Los 54 puntos no eran del plano: eran de esa mancha concreta del fondo. Mueve el elemento
50 px y desaparecen. Es la razón entera de `399`.

### 3.5. El que el montaje ordena y el ojo no ve
`motor.py` encadena los overlays y **el último de la lista queda encima**. Perfecto, salvo que si dos
elementos **no se solapan ni un píxel**, ese orden es una ficción: no hay oclusión, y sin oclusión el
ojo no tiene ninguna prueba de quién está delante.

```python
def solape(bbox_a, bbox_b):
    ax0, ay0, ax1, ay1 = bbox_a; bx0, by0, bx1, by1 = bbox_b
    w = max(0, min(ax1, bx1) - max(ax0, bx0))
    h = max(0, min(ay1, by1) - max(ay0, by0))
    menor = min((ax1-ax0)*(ay1-ay0), (bx1-bx0)*(by1-by0))
    return 100.0 * w * h / menor           # % del elemento más pequeño que queda tapado
```

| Solape | Qué prueba |
|---|---|
| 0 % | nada. Dos cosas sueltas; el orden de capas es decorativo |
| **8 – 25 %** | **el mejor rango: se ve quién tapa a quién y no se pierde el pequeño** |
| más del 45 % | el de atrás deja de ser legible; o sube de plano o sobra |

**Al menos una pareja de planos vecinos tiene que solaparse en cada escena.** Sin una sola oclusión, la
profundidad es una afirmación del guion visual que el cuadro no respalda. La técnica con material de
vídeo está en `262`.

---

## 4. El orden de la revisión

Cuando un cuadro "se ve plano", esto en este orden ahorra la tarde:

1. **¿Hay solape entre algún par de planos?** Si no, no hay nada más que mirar (§3.5).
2. **`separa.py` contra el frente.** Cuántos ejes de cuatro.
3. **Si son 3 o 4 y sigue plano: la sombra.** Mide el contacto (`394`).
4. **Si sigue plano: sobre gris.** Puede que la separación fuera del fondo (`399`).
5. **Solo entonces, mirar.** El número ordena; el ojo decide (`332`).

Y dos diagnósticos que se confunden con éste y tienen otra causa: **procedencias sin empatar** —dos
retratos de la misma época con S = 3,2 y S = 27,4 no tienen un problema de profundidad sino de empate
(`263`, `canales 23`), y si repartes planos antes, el escalón que midas será mentira— y **recortes
sucios**, que se ven mal en cualquier plano y son `canales 161`.

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Dar por buena la profundidad porque está en la tabla de eventos | El orden de capas no es distancia |
| Tres planos sin un solo solape | El orden es decorativo: no hay prueba de quién está delante |
| Solape por encima del 45 % | El de atrás deja de leerse: o sube de plano o sobra |
| Separar solo por tamaño | Lejos pero enfocado: no existe en ninguna fotografía |
| Subir el desenfoque cuando el problema es la sombra | Se refuerza la contradicción en vez de quitarla |
| Confundir un eje negativo con un error del medidor | Es información: ese eje va al revés |
| Medir la separación solo contra el fondo | Sobre gris, ΔY = 54,4 se cae a 8,1 |
| Repartir planos con recortes de procedencias sin empatar | El escalón medido es de la copia, no del plano |

## Relacionado

`390` la profundidad es separación medida · `391` el escalón de tamaño ·
`392` el escalón de desenfoque · `394` la sombra que asienta ·
`397` el primer término que se come al sujeto · `399` comprobar la profundidad sobre gris ·
`262` la técnica del sándwich (oclusión con vídeo) · `263` integrar un elemento ·
`332` mirar y medir · `canales 22` profundidad por capas · `canales 161` auditar sobre gris
