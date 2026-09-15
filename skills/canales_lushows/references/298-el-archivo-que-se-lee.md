# 298 · El archivo que se lee

**Qué resuelve:** un documento en pantalla no es una ilustración: es un objeto de prueba.
Y un objeto de prueba solo prueba algo si el espectador **lee la línea concreta** de la que
está hablando la voz. Enseñar el certificado entero mientras la voz dice «en el certificado
pone que se llamaba Robert Miller» es enseñar un papel; enseñar la casilla del nombre, con
el nombre dentro, en el momento en que se dice, es enseñar la prueba.

`48` explica por qué una cita textual en pantalla convierte una afirmación en prueba y cómo
se compone. `297` da el suelo de legibilidad. `39` sincroniza gesto y palabra. Aquí: **cómo
se recorta la línea que importa y cómo se ancla a la voz**, con el caso de `ep01-lustig`.

---

## La regla: el documento no sale entero, sale por la línea

El certificado de defunción de Lustig entra en el episodio **cinco veces y nunca completo**.
La receta declara cuatro recortes normalizados del mismo archivo:

```python
("certificado_defuncion", "victor_lustig_death_certificate_png", "revista",
 D(virar=0, contraste=1.10, nitidez=0.55, grano=False, borde=15, semilla=101)),
("casilla_nombre", "victor_lustig_death_certificate_png", "revista",
 D(encuadre=(.038, .282, .535, .332), escala=1.75, virar=0, contraste=1.12,
   nitidez=0.7, grano=False, borde=12, semilla=107)),
("casilla_oficio", "victor_lustig_death_certificate_png", "revista",
 D(encuadre=(.038, .600, .535, .655), escala=1.75, ...)),
```

Tres cosas del `encuadre`:

- **Coordenadas normalizadas (0–1), no píxeles.** La casilla del nombre es la banda
  `y ∈ [0,282 · 0,332]`, o sea el 5 % de la altura del documento. Si mañana se sustituye el
  escaneo por uno de más resolución, los recortes siguen cayendo donde tienen que caer.
- **`escala=1.75`.** El recorte se amplía *antes* de generar el PNG. Es lo que permite que
  una banda del 5 % del certificado llegue a pantalla con su texto por encima del suelo de
  28 px (`297`) sin estirar nada en el montaje.
- **El documento entero también existe**, y se queda en el banco (`296`). Está para el día
  en que la voz hable del certificado como objeto y no de una de sus casillas.

## El anclaje: la palabra manda

Cada elemento se cuelga de una palabra del guion, no de un segundo del reloj:

```python
{"r": "casilla_oficio", "ancla": "casilla", "offset": -0.25, "dura": 4.2, ...}

# en diccionario.py, al resolver:
t0 = max(ini, t - 0.16)      # el elemento entra ANTES de su palabra:
                             # justo a tiempo llega tarde
```

Los 0,16 s de adelanto son del motor y son para todos. El `offset` de la ficha es el ajuste
fino de quien escribió la escena, y **siempre es negativo** en los documentos: el papel
tiene que estar en pantalla cuando la voz llega a la palabra, no llegar con ella.

## El episodio, línea a línea

| Documento | Ancla | Lo que dice la voz |
|---|---|---|
| `casilla_hospital` | — | «en un hospital para presos federales de Missouri» |
| `casilla_nombre` | `miller` | «En el certificado pone que se llamaba Robert Miller» |
| `reglamento_celda` | `cuatro` | «Preso cinco mil novecientos cincuenta y cuatro, hache» |
| `casilla_fecha` | `hache` | (la misma línea, el otro lado del formulario) |
| **`casilla_oficio`** | **`casilla`** | **«Y en la casilla del oficio, alguien escribió a máquina dos palabras…»** |
| `lupa_casilla` | `vendedor` | «…aprendiz de vendedor» |
| `ficha_policial` | `Nunca` | «Nunca se llamó Miller» |
| `aviso_falsos` | `contado` | «según todo lo que se ha contado de él durante cien años» |
| `telegrama_union` | `versión` | «la versión que ha llegado hasta hoy dice…» |
| `plano_paris_1922` | `libros` | «La han repetido libros, periódicos y documentales» |
| `telegrama_marshal` | `periódicos` | (la misma línea) |

La fila en negrita es el mecanismo entero en una frase. La voz **nombra la casilla**, la
casilla **aparece**, y dos palabras después la lupa (`lupa_casilla`) cae sobre lo que pone.
El espectador no tiene que creerse nada: lo está leyendo.

## Dos usos distintos que parecen el mismo

La tabla mezcla dos cosas, y confundirlas es el error caro:

**El documento que se lee.** `casilla_nombre`, `casilla_oficio`, `casilla_fecha`,
`ficha_policial`. La voz dice literalmente lo que pone dentro. Obligaciones: por encima del
suelo de legibilidad (`297`), `virar=0`, `grano=False`, nitidez positiva, y vida suficiente
para leerlo —las casillas duran 3,4 y 4,2 s, no 2,4.

**El documento que solo consta.** `aviso_falsos` sobre «contado», `telegrama_union` sobre
«versión», `plano_paris_1922` sobre «libros». Nadie va a leer ese telegrama y no hace falta:
está diciendo «esto se documentó», que es una afirmación sobre el género del material, no
sobre su contenido. Aquí la letra pequeña **es textura** y el tamaño lo decide el cuadro.

La prueba para separarlos es de un segundo: **¿la voz dice lo que pone dentro?** Si sí, el
suelo de legibilidad es una obligación. Si no, es una sugerencia.

## El destello y el remate

El gancho del episodio remata en «aprendiz», y ese es el único destello de fuerza 0,22 —el
más fuerte de los cinco:

```python
"oficio": [{"ancla": "aprendiz", "offset": -0.05, "fuerza": 0.22, "ancho": 0.09}],
```

Un documento que se lee y un fogonazo sobre la palabra que lo remata es la unidad narrativa
de este canal. Y lleva sonido: la auditoría cruza cada destello con las pistas de audio y
marca los mudos, porque **un fogonazo sin golpe se lee como un fallo de codificación**, no
como énfasis.

## Lo que no se hace

- **Leer en voz alta el documento entero.** La voz da la línea; el papel da el resto. Si la
  voz recita el certificado, el documento sobra.
- **Subrayar con un rectángulo rojo.** Los gestos sobre documento —sello, tachado,
  subrayado, lupa— van en una capa aparte y con el vocabulario del canal (`62`). El
  rectángulo de presentación rompe la ilusión de objeto.
- **Anclar al reloj.** Si el guion cambia media palabra, las anclas se recolocan solas y los
  segundos no.
- **Traducir el documento.** El archivo está en el idioma en que está. La traducción va en
  la voz y, si hace falta, en un rótulo; el papel no se toca, porque tocar el papel es
  falsificarlo (`380` «no inventar», del bloque de ética, aún por escribir).

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Enseñar el documento entero mientras la voz cita una línea | Se ve un papel, no una prueba |
| Recortar la casilla en píxeles del escaneo | Al cambiar de fuente los recortes caen donde no es |
| Ampliar el recorte en el montaje en vez de en la receta | Se estira por encima del nativo y pierde filo |
| Anclar al segundo en vez de a la palabra | Media palabra de cambio en el guion lo desincroniza todo |
| `offset` positivo en un documento | El papel llega después de la frase: no prueba nada |
| Dar 2,4 s a un documento que hay que leer | No da tiempo: las casillas necesitan 3,4–4,2 s |
| Exigir el suelo de legibilidad a un documento de textura | Ocupa medio cuadro para nada |
| Destello sin sonido | Se lee como error de codificación, no como énfasis |
| Retocar el texto del documento | Deja de ser archivo y pasa a ser una falsificación (`380`) |

## Relacionado

`48` citas y documentos · `62` efectos de documento · `92` el aporte original ·
`39` sincronizar gesto y palabra · `251` qué palabra merece imagen ·
`297` documentos como imagen (el suelo de legibilidad) · `296` el recorte que no se usa ·
`125` música y destello · `270` papel contra leyenda · `91` leer un expediente
