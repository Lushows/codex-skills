# 27 · Composición de datos

**Qué resuelve:** una cifra sola no significa nada y una cifra con tres explicaciones
alrededor no se lee. El bloque de dato del canal son **tres piezas y ninguna más**:
cifra, comparación y fuente — con un tamaño, un sitio y un momento para cada una.

---

## Las tres piezas

| Pieza | Tamaño | Color | Cuándo entra |
|---|---|---|---|
| **Cifra** | 180 - 260 px de alto de numeral | papel `#E6DCC4`, o amarillo `#E8C547` si es la cifra del episodio | `ancla` − 0,15 s |
| **Comparación** | 34 - 46 px, máx. 52 caracteres | papel `#E6DCC4` | + 0,40 s |
| **Fuente** | 20 - 24 px, versalitas | `#B3A891` | + 0,75 s |

Las tres mueren **a la vez**, con el mismo `fade_out`. Una fuente que sobrevive a su
cifra queda huérfana en pantalla y se lee como basura del render.

El rojo `#E3120B` **no** se usa para la cifra: gana siempre (`21`) y se reserva para el
tachado y el sello. El verde `#0E8A5F` solo para variaciones de mercado con signo.

## La disposición

```
   ┌── zona útil de datos: columnas 1-2, filas 2-3 ────────────┐
   │   1.400.000.000                ← cifra, base en H*0.52    │
   │   ─────────────                ← filete 3 px, 60% del ancho│
   │   el presupuesto anual de la ciudad   ← comparación        │
   │   DOJ · acusación 2017                ← fuente             │
   └────────────────────────────────────────────────────────────┘
```

Coordenadas listas para la tabla (bloque anclado a la izquierda, el recorte que lo
acompaña va en P3/P6):

```python
{"r": "cifra_1400M", "ancla": "millones", "offset": -0.15, "dura": 3.2,
 "x": "W*0.05", "y": "H*0.34", "w": 900, "entrada": "fade", "rot": -1.4},
{"r": "comp_presupuesto", "ancla": "millones", "offset": 0.40, "dura": 2.65,
 "x": "W*0.05", "y": "H*0.60", "w": 760, "entrada": "izq", "rot": -1.1},
{"r": "fuente_doj2017", "ancla": "millones", "offset": 0.75, "dura": 2.30,
 "x": "W*0.05", "y": "H*0.71", "w": 380, "entrada": "fade", "rot": -0.8},
```

Los tres comparten `x` y una inclinación del mismo signo y magnitud parecida: por
semejanza y continuidad (`24`) se leen como un solo bloque, no como tres rótulos.

## La regla del uno

**Una sola cifra grande viva a la vez.** Dos números de 200 px en pantalla se anulan:
el espectador no compara, elige. Si hay que comparar dos cantidades, no van como dos
cifras sino como **una cifra y una barra** o **dos objetos a escala** (`63`).

Para una cifra que evoluciona se usan los estados que ya tiene el proyecto
(`cont_00` … `cont_10`): cada estado vive 0,5 s, con `fade_out: 0.12`, todos en la
misma `x`/`y`, y el último se queda 1,9 s. Es un solo dato contado en cinco eventos —
sube la densidad sin añadir información nueva (`10`).

## La comparación: qué sirve y qué no

| Sirve | No sirve |
|---|---|
| Un objeto que el espectador tiene visto (un estadio, un edificio) | Otra cifra grande |
| Tiempo humano ("lo que gana una familia en 40 años") | Porcentajes sobre un total que no se ha dicho |
| Repetición de una unidad conocida ("14.000 camiones") | Órdenes de magnitud sin referencia ("mil millones") |
| Una operación propia que el canal hace explícita (`92`) | Una cifra de un artículo, sin verificar |

La comparación es el **aporte original** del episodio: sin ella, la cifra es un dato
que cualquiera copia de una noticia.

## La fuente en pantalla

Formato fijo: **organismo · tipo de documento · año**. `DOJ · acusación · 2017`.
Nunca una URL: no se lee y ensucia. La referencia completa vive en
`archivo/fuentes.json` y en la descripción del vídeo.

Si el dato es una **estimación propia**, la fuente lo dice: `cálculo propio sobre datos
de la SEC`. Presentar un cálculo como si fuera oficial es el error que hunde un canal
de documentales.

## Cómo se construye el PNG

Con Chrome headless, como todo el texto del canal — no con `drawtext`. Motivos: control
tipográfico real, separadores de millar correctos, y que `drawtext` obliga a escapar
`:`, `%`, `'` y `\` (error ya cometido con `20:52`).

```css
.cifra   { font: 700 232px/0.9 "Archivo Black", Impact, sans-serif;
           color: #E6DCC4; letter-spacing: -0.02em;
           text-shadow: 3px 5px 0 rgba(18,16,12,.55); }
.filete  { height: 3px; width: 60%; background: #E3120B; margin: 18px 0 14px; }
.comp    { font: 400 42px/1.25 "Archivo", sans-serif; color: #E6DCC4; }
.fuente  { font: 500 22px/1 "Consolas", monospace; color: #B3A891;
           letter-spacing: .14em; text-transform: uppercase; }
```

Los separadores de millar en español van con **punto** (`1.400.000.000`) y el decimal
con coma. Un `1,400,000,000` en un episodio en español delata la traducción.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Dos cifras grandes a la vez | El espectador elige una y descarta la otra |
| Fuente que sobrevive a la cifra | Texto huérfano en pantalla |
| Cifra sin unidad ("1.400 millones" de qué) | Dato inservible y no verificable |
| Comparación con otra cifra | No aclara: duplica el problema |
| Separador de millar con coma en español | Delata que viene traducido |
| Rojo en la cifra | Se lleva todo el peso y aplasta el resto del cuadro |
| Cifra tapada por otro elemento | Justo el dato se pierde en su momento (`26`) |
| Estimación propia sin etiquetar | Error de rigor: es lo que hunde el canal |

## Relacionado

`44` la cifra en pantalla · `63` comparaciones visuales · `36` contadores y cifras
animadas · `92` el aporte original · `96` verificación de datos
