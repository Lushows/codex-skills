# 243 · Bandas y anclaje central

**Qué resuelve:** dónde puede caer un elemento. Nada se coloca a ojo: un elemento a ojo
se solapa con otro tres planos después y no hay forma de saberlo hasta ver el vídeo.

---

## Dieciséis posiciones y ni una más

```python
BANDAS = {
    "centro":  [("W*0.44", "H*0.36"), ("W*0.40", "H*0.50"), ("W*0.54", "H*0.32")],
    "lado":    [("W*0.19", "H*0.42"), ("W*0.79", "H*0.34"), ("W*0.80", "H*0.62"),
                ("W*0.18", "H*0.66")],
    # la banda baja no baja de H*0.80: por debajo vive la barra de YouTube
    "pie":     [("W*0.27", "H*0.76"), ("W*0.66", "H*0.78"), ("W*0.46", "H*0.70")],
    "esquina": [("W*0.82", "H*0.17"), ("W*0.17", "H*0.16"), ("W*0.80", "H*0.80")],
    "cifra":   [("W*0.50", "H*0.62"), ("W*0.48", "H*0.71"), ("W*0.52", "H*0.54")],
}
```

Cinco bandas, 16 posiciones. Un catálogo cerrado tiene una propiedad que un espacio
continuo no tiene: **se puede razonar sobre él**. Se sabe cuántas hay, se pueden probar
todas (`242` mide 672 pruebas en un minuto de episodio) y dos elementos en la misma
posición son detectablemente lo mismo.

Las coordenadas relativas (`"W*0.44"`) sobreviven a un cambio de lienzo; las absolutas
no. El vertical de 1080×1920 reutiliza la misma tabla (`128`).

## La banda de la cifra

`cifra` no está por simetría. Un número arriba a la izquierda se lee como pie de foto y
se pierde; centro-bajo es donde descansa la mirada y donde no pelea con el recorte.
Tener banda propia significa que **un dato nunca compite con un retrato por la misma
posición**, y eso es una decisión de jerarquía, no de geometría (`21`, `44`).

`pie` no baja de `H*0.80` por una razón que no es estética: ahí vive la barra de
progreso de YouTube. Es la zona segura del canal (`49`).

Cada banda trae su gesto de entrada, porque un elemento de lado que entra por abajo se
lee como un error:

```python
ENTRADAS = {"centro": "abajo", "lado": "izq", "pie": "fade",
            "esquina": "fade", "cifra": "abajo"}
```

## Centros, no esquinas

`motor.py` ancla por esquina superior izquierda. Las bandas son **centros**, y `rect()`
traduce:

```python
if centrado:                       # las BANDAS son centros; motor.py usa esquina
    x, y = x - ancho / 2.0, y - alto / 2.0
```

Con anclaje de esquina, un elemento ancho en una banda pensada para uno estrecho se sale
por la derecha: así acabó cortada la cara del protagonista. Con anclaje central cada
tamaño se acomoda alrededor de su zona y el encaje casi nunca tiene que intervenir.

## Lo que cuesta volver a la esquina

Mismo episodio, misma tabla, cambiando solo `centrado=True` por `centrado=False` en la
elección de posición:

| | anclaje central | anclaje de esquina |
|---|---|---|
| elementos | **61** | 55 |
| eventos/min | **62,4** | 56,7 |
| simultaneidad | **2,02** | 1,86 |
| cobertura media | **38,0 %** | 34,8 % |
| cuadro casi vacío | **2,40 s** | 4,40 s |
| huecos | **0** | 1 |
| cuadro descompensado | **0,00 s** | 1,40 s |

Seis elementos perdidos y un hueco, sin haber tocado ni una posición ni un recurso. Los
seis no se pierden por estar mal colocados: se pierden porque el rectángulo resultante
**no cabe** y `cabe()` los rechaza. Un elemento de 1280 px anclado por la esquina en
`W*0.82` empieza fuera del lienzo antes de dibujarse.

## El repliegue de banda

Si ninguna posición de su banda sirve, se prueban las demás antes de rendirse:

```python
orden = BANDAS[banda] + [q for k, v in BANDAS.items() if k != banda for q in v]
```

Mejor moverlo de sitio que perder el elemento. Pero el repliegue **necesita** `cabe()`:
sin esa comprobación metía un retrato de 1280 px en una posición pensada para un rótulo
de 520 y la cara salía cortada por el borde. Las bandas no saben de anchos; los
rectángulos sí.

## La banda no es el orden

Un error tentador es dar por bueno «la primera posición libre de su banda». Si siempre
gana la primera, el peso se acumula en un lado y quedan planos con la mitad del cuadro
desierta. Entre las posiciones válidas la elección la hace la nota de equilibrio
(`246`), no el orden de la lista.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Coordenadas absolutas en vez de `"W*0.44"` | La tabla no sirve para el vertical ni para otro lienzo |
| Anclar por esquina | 6 elementos perdidos y caras cortadas por el borde derecho |
| Bajar `pie` por debajo de `H*0.80` | El rótulo queda bajo la barra de YouTube |
| Meter la cifra en la banda de los objetos | El dato se lee como pie de foto y se pierde |
| Coger siempre la primera posición libre | Todo el peso en un lado, media pantalla desierta |
| Añadir posiciones «para que quepa más» | Se pierde la propiedad de catálogo cerrado y vuelve el ojo |

## Relacionado

`20` retícula del collage · `28` respiración del cuadro · `49` zona segura y tamaños ·
`242` colocación por rectángulo · `244` el techo de altura · `246` equilibrio del cuadro
