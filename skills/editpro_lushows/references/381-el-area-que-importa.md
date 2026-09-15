# 381 — El área que importa: el rectángulo miente en los dos sentidos

**Qué resuelve:** la pregunta que de verdad decide no es *qué porcentaje del elemento quedó tapado*, es
**si lo tapado era legible**. El rectángulo es un sustituto barato de esa pregunta, y falla en las dos
direcciones: dice «grave» donde no se tocó una letra y dice «leve» donde borró media cara. Aquí están las
tres formas de medir la misma pisada y cuándo hace falta cada una.

---

## 1. Tres medidas de la misma pisada

| Medida | Qué es | Coste |
|---|---|---|
| **rectángulo** | fracción de la caja del elemento que queda debajo | instantáneo |
| **caja útil** | igual, pero sobre el `bbox` del canal alfa (sin el aire transparente) | abrir el PNG |
| **tinta** | fracción de los **píxeles opacos** que quedan debajo | recorrer el alfa |

La tinta es la verdad. Las otras dos son aproximaciones, y hay que saber cuándo valen.

---

## 2. Cuánto aire lleva un PNG

Medido sobre las piezas reales del piloto (`ep01-lustig/texto`, `texto`, `ep01-lustig/recortes`), contando
píxeles con alfa > 8:

| Pieza | Tamaño | Tinta | Caja útil |
|---|---|---|---|
| `c_oficio` (titular con plancha) | 1220×400 | **99,6%** | 100,0% |
| `f_cierre` (ficha con plancha) | 1060×346 | **100,0%** | 100,0% |
| `m_consta` (marca de columna) | 900×260 | 96,7% | 100,0% |
| `bajo_la_torre` (recorte de foto) | 2206×1519 | 96,9% | 100,0% |
| `d_everest` (cifra suelta) | 1180×340 | **11,0%** | **57,4%** |
| `d_anos` (cifra suelta) | 1180×262 | 10,3% | 70,9% |
| `r_sinfuente` (rótulo) | 950×200 | 10,7% | **17,0%** |
| `r_hospital` (rótulo) | 1107×200 | 10,6% | 17,1% |

Dos familias claras:

- **Piezas con plancha** (titulares, fichas, marcas, recortes de foto): tinta por encima del 96%. Ahí el
  rectángulo **es** el contenido y medir el alfa no aporta nada.
- **Piezas sueltas sobre transparente** (cifras, rótulos): entre el 8% y el 15% de tinta, y hasta un
  **83% del rectángulo que es aire**. Ahí el rectángulo no significa nada.

---

## 3. El error en el sentido «alarma en falso»

Caso real, `episodio01`, bloque «maquina». El titular `t_ningun` bajo el recorte `boveda`:

| | valor | durante |
|---|---|---|
| rectángulo | **15,6%** | 2,45 s |
| caja útil | 0,0% | |
| **tinta** | **0,0%** | |

El recorte entra por la esquina del PNG, donde no hay una sola letra. El medidor grita durante 2,45 s por
algo que en pantalla no existe. Y el segundo ejemplo, `usd_11` bajo `dinero_real` en el gancho:

| rectángulo | caja útil | tinta | duración |
|---|---|---|---|
| **47,9%** | 7,1% | **4,3%** | 2,10 s |

Once veces de error. El rectángulo dice «casi la mitad enterrada»; la verdad es que le tapa cuatro píxeles
de cada cien.

> **Un comprobador que grita cuando no pasa nada acaba ignorándose, que es peor que no tenerlo.** Es
> exactamente la lección que ya está escrita en `auditar.py` para el comprobador de tildes, y vale igual
> aquí.

---

## 4. El error en el sentido contrario, que es el peligroso

`ep01-lustig`, bloque «torre». El recorte `torre_construccion` bajo `hotel_crillon`:

| rectángulo | caja útil | tinta | duración |
|---|---|---|---|
| 18,9% | 18,9% | **36,3%** | 1,74 s |

El rectángulo dice 18,9% —por debajo de cualquier umbral razonable— y la tinta real tapada es casi el
doble. Pasa cuando el recorte tiene silueta: la caja está medio vacía por las esquinas, la parte llena está
justo donde cae el vecino, y el promedio la disimula.

**La regla:** el rectángulo subestima cuando el que queda debajo es un **recorte con silueta** y el vecino
cae sobre su centro de masa. Sobreestima cuando el que queda debajo es **texto suelto** y el vecino cae en
el aire del PNG.

---

## 5. Medir la tinta, en código

```python
from PIL import Image

def alfa_escalado(ruta, ancho):
    """El canal alfa del PNG, ya al tamano en que se va a mostrar."""
    im = Image.open(ruta).convert("RGBA"); w, h = im.size
    return im.split()[3].resize((int(ancho), max(1, int(round(ancho * h / w)))))

def caja_util(a, c):
    """El rectangulo recortado al contenido real (bbox del alfa)."""
    bb = a.getbbox()
    return c if not bb else (c[0]+bb[0], c[1]+bb[1], c[0]+bb[2], c[1]+bb[3])

def tinta_tapada(a, c, rival, paso=2):
    """Fraccion de los pixeles opacos del elemento que caen bajo 'rival'."""
    px = a.load(); W, H = a.size; rx0, ry0, rx1, ry1 = rival
    dentro = total = 0
    for j in range(0, H, paso):
        for i in range(0, W, paso):
            if px[i, j] > 8:
                total += 1
                if rx0 <= c[0]+i < rx1 and ry0 <= c[1]+j < ry1:
                    dentro += 1
    return dentro / total if total else 0.0
```

`paso=2` muestrea uno de cada cuatro píxeles: sobre las 34 pisadas de `episodio01` el resultado no se movió
ni una décima y el barrido completo tardó menos de un segundo.

---

## 6. La escalera de decisión

No hace falta medir la tinta de todo. Esta escalera cuesta casi nada y acierta:

1. **Rectángulo** para todas las parejas. Descarta el 60–68% de golpe: en el censo de hoy, 65 de 96 parejas
   de `ep01-lustig` y 58 de 93 de `episodio01` ni se tocan.
2. Para las que se tocan, **caja útil**. Es un `getbbox()` cacheado por recurso.
3. Solo para las que siguen por encima del umbral, **tinta**. En el peor episodio eran 34.

---

## 7. Lo que este módulo no contesta

Que una pieza conserve el 92% de su tinta **no prueba que se lea**. Dónde cae el 8% importa más que el 8%:
si es la primera letra de una palabra o los ojos de un retrato, se acabó. Eso es `382` (la zona protegida)
y, para la legibilidad de una palabra concreta bajo un sujeto, `377` §3, que ya da la regla del 60% del
ancho y la primera letra visible. Para cifras en pantalla, `379`.

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Medir el rectángulo de una cifra suelta | Alarmas en falso del 15% sobre 0% de tinta real |
| Medir el rectángulo de un recorte con silueta | Se cuela una pisada del 36% disfrazada de 19% |
| Medir la tinta de todo | Se paga un barrido de píxeles por 1.830 parejas que no se tocan |
| No cachear el alfa por (recurso, ancho) | Se reabre el mismo PNG cientos de veces |
| Recortar el alfa después de rotar | El `bbox` crece con el aire que mete la rotación (`389`) |
| Usar umbral de alfa 0 en vez de 8 | Los bordes antialias cuentan como tinta y la caja útil se infla |
| Creer que 92% de tinta conservada = legible | Depende de **dónde** cae el 8% (`382`, `377` §3) |

## Relacionado

`380` qué es pisar en números · `382` la zona protegida · `383` umbrales por tipo de contenido ·
`384` medir el solape antes de renderizar · `377` §3 cuánto puede taparse una palabra · `379` números y
cifras en pantalla · `canales_lushows/26` cuánto solape es correcto
