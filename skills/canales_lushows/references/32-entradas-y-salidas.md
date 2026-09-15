# 32 · Entradas y salidas

**Qué resuelve:** un elemento que aparece de golpe se lee como error de render; uno que
tarda demasiado en entrar llega tarde a su palabra. La entrada es la mitad del carácter
de un elemento y solo hay cinco que sirven en este canal.

---

## Las familias

| Familia | Qué comunica | Duración |
|---|---|---|
| **Fundido** (`fade`) | Neutro. Aparece sin afirmar nada | 0,25-0,35 s |
| **Deslizamiento** (`izq`, `der`, `arriba`, `abajo`) | Alguien lo pone ahí. Es la entrada de collage por excelencia | 0,28-0,40 s |
| **Golpe de escala** | Impacto. Aterriza y suena | 0,14-0,20 s |
| **Corte seco** (1 fotograma) | Brutal, documental. Un sello que cae | 0,04 s |
| **Barrido / teletipo** | Documento en curso. Solo para texto (`41`) | 18-26 car/s |

**Nunca:** rebote elástico, giro 3D, entrada desde fuera del cuadro completo, entradas
de más de 0,6 s, ni dos elementos entrando por el mismo lado en el mismo segundo.

---

## Qué entra cómo

| Elemento | Entrada | Por qué |
|---|---|---|
| Retrato / recorte principal | deslizamiento + fundido | Es el que manda; necesita presencia, no violencia |
| Cifra de impacto | golpe de escala | Tiene que pegar |
| Rótulo que explica un objeto | fundido corto (0,22 s) | Es servicio, no protagonista |
| Documento / recorte de prensa | deslizamiento desde el borde más cercano | Se lee como que lo dejaron sobre la mesa |
| Sello, clasificación, tachón | corte seco | Los sellos no se desvanecen: se estampan |
| Cita textual | teletipo (`41`) | — |
| Micro-elemento (marca, subrayado) | fundido 0,18 s | Vive 0,8 s; una entrada larga se lo come |

**La dirección tiene sentido:** un elemento entra desde el borde al que está más cerca.
Un recorte que vive en la esquina superior derecha y entra por la izquierda cruza medio
cuadro y tapa lo que hay en medio.

---

## Deslizamiento, escrito bien

Distancia: **60-140 px**. Menos no se percibe, más cruza el cuadro.

```bash
# Entra por la izquierda: llega a x=1080 en 0,32 s desde el segundo 1,40, con easeOut
[1:v]format=rgba,fade=t=in:st=1.40:d=0.26:alpha=1[el];
[bg][el]overlay=x='1080-90*pow(1-clip((t-1.40)/0.32,0,1),3)':y='412':
                enable='gte(t,1.40)*lt(t,5.10)'
```

Las cuatro direcciones cambian solo qué coordenada lleva el desplazamiento y su signo:

| Entrada | Expresión |
|---|---|
| `izq` | `x='X-90*pow(1-U,3)'` |
| `der` | `x='X+90*pow(1-U,3)'` |
| `arriba` | `y='Y-70*pow(1-U,3)'` |
| `abajo` | `y='Y+70*pow(1-U,3)'` |

donde `U = clip((t-T0)/0.32,0,1)`. Vertical siempre un poco más corto que horizontal:
el cuadro es 16:9 y 90 px arriba pesan más que 90 px al lado.

El fundido acompaña al deslizamiento y termina **antes**: `d` del fade = 0,80 × `D` del
deslizamiento. Si terminan a la vez, el elemento parece llegar todavía translúcido.

---

## Salidas

**Regla: la salida dura el 70% de la entrada.** 0,32 s de entrada → 0,22 s de salida.
Una salida lenta deja el cuadro medio vacío durante un segundo y ese es exactamente el
hueco que mata el ritmo (`11`).

```bash
# Salida: se va por donde vino, acelerando (easeIn)
[1:v]fade=t=out:st=4.88:d=0.22:alpha=1[el];
[bg][el]overlay=x='1080-70*pow(clip((t-4.88)/0.22,0,1),2)':y='412':enable='lt(t,5.10)'
```

Tres modos de salir, por orden de preferencia:

1. **Relevo** — el siguiente elemento entra y lo empuja fuera. Es el mejor: no deja hueco
2. **Fundido corto** — 0,20-0,25 s. El estándar
3. **Corte seco** — solo si entra otro elemento en el mismo fotograma

**El elemento no sale con la palabra.** Sale entre **0,3 y 0,6 s después** de que la voz
termine la frase que sostenía. Si sale exacto con la última sílaba, se lee como recortado.

---

## Cuál nunca

| Entrada | Por qué no |
|---|---|
| Rebote / elástico | Es lenguaje de motion graphics de plantilla; rompe el tono documental |
| Rotación de entrada (girar al aparecer) | Solo para el sello, y como máximo 4°. Más es dibujo animado |
| Zoom desde 0 | El elemento pasa 4 fotogramas siendo un punto ilegible |
| Entrada de más de 0,6 s | Llega tarde a su palabra aunque el arranque esté bien anclado |
| Desenfoque que se enfoca | Cuesta tres veces más render y no se nota a 1080p |

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Entrada de 0,45 s anclada con 0,12 s de adelanto | El elemento está legible 0,33 s TARDE (ver `39`) |
| Misma entrada para todos los elementos | El episodio se vuelve un catálogo; se detecta al cuarto plano |
| Fundido que termina a la vez que el deslizamiento | El elemento aterriza todavía translúcido |
| Salida más lenta que la entrada | Hueco al final de cada frase |
| Dos elementos entrando por el mismo lado a la vez | Se leen como uno solo partido |
| Deslizamiento de 300 px | Cruza el cuadro y tapa al que sostiene la frase |

## Relacionado

`13` ciclo de vida del elemento · `14` encadenar elementos · `31` curvas de aceleración ·
`39` sincronizar gesto y palabra · `41` máquina de escribir
