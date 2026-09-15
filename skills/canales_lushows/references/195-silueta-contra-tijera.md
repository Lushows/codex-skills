# 195 · Recorte de silueta contra recorte de tijera

**Qué resuelve:** cuándo se recorta la figura del fondo con segmentación automática y
cuándo se recorta un polígono tosco alrededor de la foto. Equivocarse en un sentido deja
bordes sucios y figuras fantasma; equivocarse en el otro desperdicia el único recurso que
convierte una foto en un elemento de collage recolocable.

---

## La decisión, en una línea

> **Figura clara y aislada → silueta. Foto abierta → tijera. Documento → ni una ni otra.**

«Abierta» significa: varias personas, un interior, un paisaje, o una escena donde no hay
un sujeto que se pueda separar del resto sin que la foto pierda el sentido.

## Por qué la tijera no es el plan B

`rembg` falla justo en las fotos abiertas, pero además **un recorte perfecto no es lo que
hace un fanzine**: en un collage de verdad se recorta a mano, tosco, y queda un margen de
papel. El polígono irregular con borde grueso es más fiel al lenguaje del canal que una
silueta impecable, y no puede fallar porque no depende de reconocer nada.

```python
def poligono_tijera(w, h, vertices=26, irregular=0.045, semilla=7):
    """Rectángulo cuyo borde tiembla. El temblor pequeño (4-5% del lado) es lo que
    separa 'cortado a mano' de 'rasgado'."""
    rnd = random.Random(semilla)
    pts, per = [], 2 * (w + h)
    for i in range(vertices):
        d = per * i / vertices
        if d < w:             x, y = d, 0
        elif d < w + h:       x, y = w, d - w
        elif d < 2 * w + h:   x, y = w - (d - w - h), h
        else:                 x, y = 0, h - (d - 2 * w - h)
        x += rnd.uniform(-1, 1) * w * irregular
        y += rnd.uniform(-1, 1) * h * irregular
        pts.append((max(0, min(w, x)), max(0, min(h, y))))
    return pts
```

Umbrales: **26 vértices** (menos parece un pentágono, más un óvalo), **`irregular`
0,035–0,050** (bajo 0,03 se lee como rectángulo recto; sobre 0,06 parece papel rasgado,
que es otra cosa) y **`semilla` distinta por pieza**, para que dos recortes contiguos no
tengan el mismo temblor.

## La compuerta automática

No se decide a ojo pieza a pieza: se intenta la silueta y se comprueba **cuánto del
cuadro cubre la máscara**. Si cubre casi nada o casi todo, la segmentación se equivocó.

```python
def silueta(rgb, borde=15, semilla=7, umbral=150, sombra=True):
    ses = sesion_rembg()
    if ses is None:                                   # rembg no instalado
        return tijera(rgb, borde=borde, semilla=semilla), False
    bruto = remove(rgb, session=ses)
    mask = limpiar_mascara(bruto.split()[3], umbral=umbral)     # ver 196
    cubierto = (np.asarray(mask, dtype=np.uint8) >= 128).mean()
    if not (0.04 <= cubierto <= 0.45):
        return tijera(rgb, borde=borde, semilla=semilla), False
    return montar(granular(rgb, semilla), mask, borde, sombra, desvio=(5, 9)), True
```

**4% – 45%.** Por debajo del 4% la máscara es un jirón; por encima del 45% rembg se quedó
con medio fondo y el «recorte» es la foto entera con los bordes mordidos. Medido sobre el
archivo del episodio 01 (u2net, lado mayor 1600 px):

| Fuente | Clase | Cubre | Islas | Veredicto |
|---|---|---|---|---|
| Ficha policial de Lustig | figura aislada | 27,2% | 2 | silueta ✅ |
| Torre Eiffel, foto actual | figura aislada | 12,7% | 1 | silueta ✅ |
| Torre en construcción (Durandelle) | figura aislada | 29,2% | 1 | silueta ✅ |
| Galería de celdas de Alcatraz | foto abierta | **0,1%** | 3 | cae a tijera |
| Edificio abandonado en Alcatraz | foto abierta | **2,1%** | 1 | cae a tijera |
| Coche prensado (chatarrería) | foto abierta | **49,0%** | 1 | cae a tijera |
| Patio de Alcatraz | foto abierta | 12,3% | 1 | *pasa, y es un falso positivo* |
| Cartel de busca del FBI | documento | 3,5% | 2 | cae a tijera |
| Reglamento de celda | documento | 64,5% | 1 | cae a tijera |

Tres de cada cuatro fotos abiertas caen por la compuerta. La cuarta —el patio de
Alcatraz— **pasa el filtro y aun así está mal**: rembg recorta un tercio arbitrario de la
escena. Por eso la compuerta es una red de seguridad, no el criterio: la clase la decide
quien mira la foto, y la compuerta atrapa los errores de clasificación.

## El documento es la tercera vía

El certificado de defunción, los planos, los bonos, los telegramas y los reglamentos **no
se recortan**. Van en modo revista: rectángulo entero, margen de papel parejo, sin grano
y con un punto de nitidez, porque en pantalla se **leen** (`48`).

```python
("reglamento_celda", "alcatraz_cell_regulations_jpg", "revista",
 D(virar=0.25, contraste=1.10, nitidez=0.45, grano=False, borde=13, semilla=181)),
```

Mandar un documento por rembg no es solo inútil: cubre el 64,5%, cae por el tope de 45% y
**gasta 6 segundos para acabar en tijera**, que tampoco es su sitio.

## Lo que sale en la práctica — los 69 recortes del episodio 01

```
tijera .......................... 42   (61%)
revista (documentos) ............ 22   (32%)
silueta ......................... 2
silueta + estirada .............. 1
tijera (silueta sucia) .......... 2    ← la compuerta actuando
```

**La tijera es el tratamiento por defecto del canal**, no la excepción. La silueta se
reserva para las piezas que van a recolocarse sobre otro fondo: el protagonista saliendo
de su ficha policial, la torre plantada sobre un titular.

`rembg` con u2net tarda **4,5 – 6,4 s por imagen** en la máquina del canal (CPU, sin
GPU): pasar las 80 piezas por silueta son 7 minutos para tirar 75 resultados.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Pasar todo por rembg «a ver qué sale» | 7 minutos y bordes sucios en la mitad del episodio |
| Tratar la tijera como plan B | Se pierde el lenguaje del canal; todo se ve pegado digital |
| `irregular` por encima de 0,06 | Parece papel rasgado, no cortado |
| La misma semilla en piezas contiguas | Dos recortes con el mismo temblor: se nota |
| Recortar un documento | Deja de leerse, que es lo único que tenía que hacer |
| Confiar solo en la compuerta 4-45% | El patio de Alcatraz pasa y sale mal igual |

## Relacionado

`196` · `194` · `25` · `48` · `23` · `199`
