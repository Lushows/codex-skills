# 89 · Biblioteca de sonido

**Qué resuelve:** el catálogo de los 22 efectos del canal, cada uno con su **LUFS medido
y su ganancia calibrada**. Todo sintetizado (`81`): ninguna pieza puede recibir un
reclamo de Content ID. Se genera con `piloto/sfx.py` y vive en `piloto/sonido/*.wav`.

---

## Nomenclatura

```
<familia>_<objeto>.wav        WAV · pcm_s16le · 44 100 Hz · estéreo
```

| Prefijo | Familia | Qué son |
|---|---|---|
| `amb_` | Ambientes | Colchones largos que sostienen una escena entera. En bucle |
| `dr_` | Dramáticos | Los picos de la narración (`84`) |
| `ob_` | Objetos | Lo que suena en pantalla (`83`) |
| `tr_` | Transición | Acompañan la entrada de un elemento o el cambio de escena |

Minúsculas, sin tildes, sin espacios. El nombre dice **qué es**, no cómo se hizo.

## La referencia de nivel

| Medida | Valor |
|---|---|
| Stem de voz procesado (`episodio01`) | **−24,8 LUFS** |
| Cada pieza de colchón, calibrada | **−41,0 LUFS** |
| Suma de 3-4 colchones simultáneos | −36 a −35 LUFS ≈ **11-12 LU bajo la voz** |
| Lo mismo, con el ducking actuando (`85`) | ≈ **15-16 LU bajo la voz** |

Ese vaivén entre 11-12 (en las pausas) y 15-16 (mientras habla) es exactamente el
comportamiento que buscamos: el fondo nunca desaparece y nunca pelea.

## Ambientes — objetivo −41,0 LUFS · 30 s · en bucle

| Nombre | Qué es | LUFS medido | Ganancia | En mezcla |
|---|---|---|---|---|
| `amb_sala` | Room tone de archivo. **Va en TODO el episodio, de principio a fin** | −48,6 | **2,40** | −41,0 |
| `amb_tension` | Dos graves a distancia de quinta. Amenaza baja | −35,1 | **0,51** | −40,9 |
| `amb_encierro` | Ruido marrón filtrado con eco: túnel, celda, bóveda | −41,0 | **1,00** | −41,0 |
| `amb_oficina` | Fluorescente a 120 Hz + aire: banco, despacho, comisaría | −38,8 | **0,78** | −41,0 |

`amb_sala` es la cola que une escenas de mundos distintos. Nunca se apaga.

## Dramáticos

| Nombre | Dur. | Qué es | LUFS | Gan. | En mezcla |
|---|---|---|---|---|---|
| `dr_riser` | 2,4 s | Ruido que crece `pow(t/D,3.4)` y muere en el golpe | −11,9 | **0,40** | −19,9 |
| `dr_golpe` | 1,2 s | Transitorio seco de percusión. Da pegada al ataque | −28,4 | **0,52** | −34,1 |
| `dr_impacto` | 2,8 s | Grave de 47 Hz. El golpe de la cifra | −30,4 | **0,62** | −34,6 |
| `dr_revela` | 3,5 s | Acorde que se abre con eco. Para entender, no para golpear | −31,4 | **0,50** | −37,4 |
| `dr_latido` | 24 s | Pulso grave cada 2 s. **Convierte un drone en suspenso**. En bucle | −35,8 | **0,55** | −41,0 |

`dr_latido` se calibra como colchón (−41,0), no como pico: está todo el rato.

## Objetos

| Nombre | Dur. | Qué es | LUFS | Gan. | En mezcla |
|---|---|---|---|---|---|
| `ob_papel` | 0,7 s | Hoja que se mueve o se pega | −31,6 | **0,50** | −37,6 |
| `ob_billetes` | 1,6 s | Fajo pasando entre los dedos | −25,1 | **0,42** | −32,6 |
| `ob_moneda` | 1,4 s | Moneda que cae y rebota | −39,4 | **1,32** | −37,0 |
| `ob_boveda` | 2,2 s | Puerta de metal pesado | −28,8 | **0,46** | −35,5 |
| `ob_contadora` | 3,0 s | Máquina contando billetes | −34,1 | **0,40** | −42,1 |
| `ob_obturador` | 0,5 s | Cámara. Marca el gesto de "esto es un documento" | −18,1 | **0,44** | −25,2 |
| `ob_reloj` | 20 s | Tictac de segundero. Repetitivo largo | −32,5 | **0,27** | −43,9 |
| `ob_goteo` | 20 s | Goteo con eco de espacio cerrado. Repetitivo largo | −41,6 | **0,76** | −44,0 |
| `ob_motor` | 12 s | Motor grave con pulso de pistones | −33,9 | **0,39** | −42,1 |
| `ob_teletipo` | 6,0 s | Máquina de escribir. Acompaña el efecto de texto (`41`) | −32,6 | **0,26** | −44,3 |

Los cuatro **repetitivos largos** (`ob_reloj`, `ob_goteo`, `ob_motor`, `ob_teletipo`) van
a −42/−44 LUFS: a nivel de objeto normal se vuelven insoportables al medio minuto.

## Transición — tienen que oírse por encima del colchón

| Nombre | Dur. | Qué es | LUFS | Gan. | En mezcla |
|---|---|---|---|---|---|
| `tr_whoosh` | 1,0 s | Acompaña la entrada de un recorte | −18,0 | **0,34** | −27,4 |
| `tr_flash` | 0,55 s | Golpe corto de agudos | −17,6 | **0,38** | −26,0 |
| `tr_cierre` | 1,8 s | Barrido descendente para cerrar bloque | −35,1 | **2,02** | −29,0 |

Entran **0,25-0,35 s antes** del corte, no encima (`75`).

## Objetivos por familia (para calibrar uno nuevo)

| Familia | Objetivo | Por qué |
|---|---|---|
| Ambientes y latido | **−41,0 LUFS** | Suman 3-4 a la vez; es el colchón de `80` |
| Objeto repetitivo largo | **−44 a −42** | Se oye durante medio minuto |
| Objeto de acompañamiento | **−38 a −35** | Está, pero no es el plano |
| Objeto protagonista | **−33 a −25** | ES el plano (obturador, billetes) |
| Impacto y golpe | **−35 a −34** | El peso lo da el silencio, no el nivel (`84`) |
| Riser | **−20** | Tiene que construir por encima de todo |
| Transición | **−29 a −26** | Cruza el corte: si no se oye, no sirve |

## Variar sin crear archivo nuevo

Antes de añadir una pieza, casi siempre basta con retocar la que ya hay:

| Quiero | Sin crear nada |
|---|---|
| El mismo objeto más lejos | Bajar `volume` 4-6 dB y añadir `lowpass=f=2500` |
| Más grande / más pesado | `atempo=0.85` + `lowpass` |
| Más pequeño / más nervioso | `atempo=1.20` + `highpass` |
| El mismo espacio, otra sala | Cambiar los retardos de `aecho` |
| Que no se note la repetición | Alternar `atempo` 0,97 / 1,03 entre usos |

## Criterio para añadir uno nuevo

1. **¿Hay uno que sirva?** Con la tabla de arriba, el 80% de las veces sí.
2. **¿Lo pide el guion visual?** Un objeto en pantalla (`83`) o un pico del guion (`84`).
   Un sonido que no responde a nada es ruido.
3. **Sintetizado, nunca descargado.** Sin excepción (`81`).
4. **Duración = la del objeto real**, con un poco de margen para el `afade`.
5. **Medir su LUFS y calcular la ganancia** contra el objetivo de su familia (`86`).
   Nunca a ojo: así se llegó a 44 saltos audibles.
6. Añadirlo a `sfx.py` con un comentario que diga **qué es**, no cómo se hizo.
7. Regenerar la biblioteca entera: `python sfx.py`. Es determinista, no hay riesgo.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Poner la ganancia a oído | 44 saltos y piezas inaudibles: la calibración se calcula |
| Calibrar un repetitivo largo como un objeto puntual | Insoportable al medio minuto |
| Tratar `dr_latido` como pico | Está siempre: va calibrado como colchón |
| Crear una pieza nueva en vez de variar una existente | Biblioteca inflada y sin coherencia de nivel |
| Descargar "un efecto suelto, solo esta vez" | Es la vía por la que muere un canal así |
| Cambiar `sfx.py` sin regenerar | Las ganancias de la tabla dejan de corresponder |
| Nombre que describe el método (`ruido_pink_2`) | En seis meses nadie sabe qué es |

## Relacionado

`81` sintetizar · `83` diegético · `84` picos · `86` medir · `80` arquitectura
