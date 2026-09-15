# 13 · Ciclo de vida del elemento

**Qué resuelve:** los elementos aparecen, se quedan quietos y desaparecen. Cada uno
está bien colocado y el conjunto se ve muerto, porque ninguno hace nada mientras vive.

---

## Las tres fases

Todo elemento tiene **entrada, gesto y salida**. Si le falta una, se nota.

| Fase | Duración | Qué hace | Dónde se declara |
|---|---|---|---|
| **Entrada** | 0,30-0,45 s | Llega deslizando o fundiendo. Nunca aparece de golpe | `entrada`, `dur_entrada` |
| **Gesto** | el resto de la vida | Deriva lenta, cambio de estado o nada (si dura poco) | `deriva`, o troceo en estados |
| **Salida** | 0,25-0,40 s | Se funde, o cede el sitio al siguiente | `fade_out`, o relevo (`14`) |

`motor.py` da por defecto `dur_entrada = 0,36` y `fade_out = 0,40`. Son buenos valores:
sólo se tocan para una sustitución (bajar `fade_out` a 0,10-0,12) o para un golpe
(entrada de 0,18 s, que se lee como impacto).

**El adelanto es obligatorio:** el elemento entra 0,10-0,20 s **antes** de su palabra.
Si su entrada dura 0,36 s y arranca justo en la palabra, el ojo lo ve completo medio
segundo tarde y todo el montaje se siente desincronizado.

## Duraciones por tipo

El tiempo en pantalla se reparte por importancia, no por comodidad de montaje.

| Tipo | Duración | Por qué |
|---|---|---|
| **Cifra o dato** | 1,4-2,0 s | Un número se lee en menos de un segundo; más tiempo es tiempo muerto |
| **Retrato / ficha** | 2,0-2,8 s | Una cara pide reconocimiento: por debajo de 2 s no se registra quién es |
| **Documento** | 2,6-3,4 s | Hay que leer algo dentro. Es el único que puede pasar de 3 s |
| **Objeto de contexto** | 1,6-2,2 s | Se identifica rápido y aporta poco después |
| **Rótulo / etiqueta** | 1,2-1,8 s | Vive menos que aquello que explica, y entra 0,2 s después |
| **Micro-acento** | 0,6-1,0 s | Sello, tachado, flecha. Puntuación, no información |
| **Estado de una serie** | 0,45-0,60 s | Sólo válido en sustitución: el ojo no lo lee, lo percibe cambiando |
| **Suelo** | toda la escena | Ficha de caso o chapa pegada a un borde |

**Piso absoluto: 0,55 s.** Por debajo, un elemento aislado es un parpadeo y se lee como
fallo de render. La única excepción son los estados de una serie que se sustituyen en
la misma posición, donde el ojo lee la serie, no cada estado.

**Techo sin gesto: 2,0 s.** Pasado eso, el elemento necesita deriva, cambio de estado o
un acento encima. Un elemento clavado 3 s cuesta lo mismo que un hueco.

**Duración mínima de un texto:** `0,6 + n_caracteres / 14` segundos. Un rótulo de 22
caracteres necesita 2,2 s en pantalla; si la escena no da para eso, se acorta el texto,
no la duración.

## El gesto: cuánto se mueve

```python
# deriva en px/s sobre lienzo 1920x1080
{"deriva": (0, 0)}       # solo para elementos de menos de 1,2 s
{"deriva": (6, 0)}       # apoyo: apenas perceptible, evita el efecto clavado
{"deriva": (9, -4)}      # principal de 2-3 s: sube ligeramente mientras vive
{"deriva": (-26, 4)}     # objeto que cruza: helicóptero, avión, vehículo
```

Regla: **la deriva total no pasa de 40 px** en toda la vida del elemento, salvo que sea
un objeto que atraviesa a propósito. `9 px/s × 2,4 s = 22 px`: correcto. `26 px/s ×
2,6 s = 68 px` es un cruce, y debe verse como tal.

**Dirección alternada.** Si tres elementos seguidos derivan hacia arriba, el ojo lo
detecta. Se alterna igual que el movimiento de fondo (`38`).

## El troceo: cuando un elemento tiene que durar más de 2 s

Un elemento largo se convierte en varios cortos que se sustituyen en la misma posición.
Es lo que hace el contador de metros del piloto:

```python
{"r": "cont_02", "ancla": "mil",        "offset": -0.10, "dura": 0.55,
 "x": "W*0.06", "y": "H*0.68", "w": 470, "entrada": "fade", "fade_out": 0.12},
{"r": "cont_05", "ancla": "quinientos", "offset":  0.00, "dura": 0.50,
 "x": "W*0.06", "y": "H*0.68", "w": 470, "entrada": "fade", "fade_out": 0.12},
{"r": "cont_08", "ancla": "metros",     "offset":  0.00, "dura": 0.50,
 "x": "W*0.06", "y": "H*0.68", "w": 470, "entrada": "fade", "fade_out": 0.12},
{"r": "cont_10", "ancla": "túnel.",     "offset": -0.05, "dura": 1.90,
 "x": "W*0.06", "y": "H*0.68", "w": 520, "entrada": "fade"},
```

Cuatro eventos donde había uno, sin material nuevo y sin ocupar más cuadro. El último
estado dura más porque es el que se queda: la cifra final.

Detalle que hay que cuadrar: **la vida de un estado termina donde empieza la del
siguiente**. En el piloto `cont_02` dura 0,55 s desde "mil" y `cont_05` arranca en
"quinientos" 0,25 s después: se pisan 0,30 s al 100%. Corrección: `dura` = distancia
real entre las dos palabras, o `fade_out` de 0,08.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Elemento de 0,4 s aislado | Parpadeo: se lee como fallo de render |
| Retrato de 1,2 s | No da tiempo a reconocer la cara; el material se desperdicia |
| Documento de 1,5 s | Se ve que hay texto y no se puede leer: frustra |
| Elemento de 3 s sin deriva ni estados | Plano muerto, cuesta lo mismo que un hueco |
| Rótulo con la misma vida que su elemento | Compiten. El rótulo entra 0,2 s después y muere 0,3 s antes |
| `fade_out` por defecto en una sustitución | Los dos estados se ven a la vez medio segundo: emborrona la cifra |
| Deriva de 30 px/s en un retrato | Deja de ser papel pegado y parece que flota |

## Relacionado

`10` densidad de eventos · `12` capas simultáneas · `14` encadenar elementos ·
`32` entradas y salidas · `36` contadores y cifras animadas · `39` sincronizar gesto y palabra
