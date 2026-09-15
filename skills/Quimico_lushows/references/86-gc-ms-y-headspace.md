# 86 — GC-MS y headspace: identificar por biblioteca y analizar solo lo que se evapora

GC-MS es la combinación que más identificaciones ha producido en la historia de la química analítica, y por
una razón sencilla: la ionización por electrones (EI) a 70 eV produce un espectro de fragmentación tan
reproducible que sirve como **huella digital comparable entre equipos y entre países**. Por eso existen
bibliotecas de cientos de miles de espectros y por eso un GC-MS puede decirte "esto es β-cariofileno" sin
que tú hayas comprado el patrón. El headspace, por su parte, es la técnica de inyección que resuelve el
problema de las matrices sucias: en vez de inyectar el extracto, se inyecta **el aire de encima**.

Términos:
- **EI (electron ionization, 70 eV)** = ionización dura y estandarizada que fragmenta reproduciblemente.
- **Biblioteca espectral (spectral library)** = base de espectros EI (NIST, Wiley, MassBank) para comparar.
- **Match score / similitud** = qué tanto se parece tu espectro al de la biblioteca (0–1000).
- **Índice de retención (retention index, RI)** = posición del pico en la escala de n-alcanos; segundo
  criterio de identidad.
- **Headspace (HS)** = analizar la fase gas en equilibrio con la muestra dentro de un vial sellado y
  termostatado.
- **SPME (solid-phase microextraction)** = fibra que concentra volátiles del headspace antes de inyectar.
- **Coeficiente de reparto (partition coefficient, K)** = cómo se reparte el analito entre la muestra y el
  gas del vial.

## Identificación por GC-MS: dos criterios, no uno

```
Criterio 1: espectro EI vs biblioteca      -> match score >= 800-900 (de 1000)
Criterio 2: indice de retencion (RI)       -> dentro de +-10-20 unidades del
                                              valor publicado para esa fase

SOLO CON LOS DOS se declara identificacion tentativa solida. Con el espectro
solo, los isomeros se confunden todo el tiempo: alfa-pineno y beta-pineno,
limoneno y beta-felandreno, los sesquiterpenos entre si.

Y para IDENTIFICACION CONFIRMADA (nivel 1, ver 84) hace falta correr el
PATRON de referencia en el mismo metodo. Punto.
```

Cómo se calcula el RI, para que puedas leerlo en un informe:

```
Indice de retencion de Kovats (rampa de temperatura, indice lineal):

    RI = 100 * [ n + (tR(x) - tR(n)) / (tR(n+1) - tR(n)) ]

  n     = numero de carbonos del alcano que sale ANTES
  tR(x) = tiempo de retencion de tu compuesto
Ejemplo: si sale entre C10 (tR 8,0 min) y C11 (tR 9,5 min), a 8,6 min:
    RI = 100 * [10 + (8,6-8,0)/(9,5-8,0)] = 100 * 10,4 = 1040
Valores publicados en DB-5 (ILUSTRATIVO): alfa-pineno ~ 932-939,
limoneno ~ 1024-1031, linalool ~ 1095-1101, beta-cariofileno ~ 1417-1424.
Verifica siempre contra la base del NIST o la fuente del metodo.
```

## Headspace: por qué inyectar aire es mejor idea que inyectar la muestra

Cuando la matriz es un aceite, una resina o un polvo con azúcares, inyectarla directo al GC ensucia el
liner, mata la columna y arrastra interferencias. El headspace evita todo eso: se calienta el vial sellado,
los volátiles pasan a la fase gas, y se inyecta solo esa fase gas. **Lo no volátil nunca entra al equipo.**

| Modalidad | Cómo | Cuándo se usa | Sensibilidad |
|---|---|---|---|
| **HS estático (static headspace)** | Equilibrio en vial a T fija, se inyecta un volumen del gas | Solventes residuales USP <467> (`87`), terpenos | Media |
| **HS dinámico / purge & trap** | Se arrastra con gas y se concentra en trampa | Trazas en agua, compuestos de olor | Alta |
| **HS-SPME** | Fibra adsorbente expuesta al headspace, luego desorbida en el inyector | Perfil aromático, screening de volátiles | Alta, pero semicuantitativa |
| **HS de equilibrio múltiple (MHE)** | Varias extracciones sucesivas del mismo vial | Cuando no hay matriz blanco disponible | Alta exactitud, laborioso |

Las variables críticas de un headspace, y por qué te importan al leer un COA:

```
Temperatura de equilibrio (70-105 C) ... define cuanto analito pasa al gas
Tiempo de equilibrio (20-60 min) ....... si es corto, no hay equilibrio real
Solvente/diluyente del vial ............ DMSO, DMF, DMA o agua segun USP <467>
Sal agregada (salting out, NaCl/Na2SO4)  empuja el analito al gas y sube la senal
Volumen de muestra vs volumen del vial . cambia el reparto; hay que fijarlo
Agitacion .............................. acelera el equilibrio

EFECTO MATRIZ EN HEADSPACE: el coeficiente de reparto K depende de la matriz.
Un metanol en un aceite de cannabis NO se reparte igual que en agua. Por eso
la calibracion debe hacerse EN MATRIZ o por adicion de estandar (72). Calibrar
en agua y medir en aceite subestima sistematicamente los solventes (87, 201).
```

Este es el punto que hay que auditar en un COA de solventes residuales de un extracto oleoso: **¿la curva se
preparó en la misma matriz?** Si no, el número está sesgado y casi siempre hacia abajo, es decir, a favor
del proveedor.

## Modos de adquisición en GC-MS

| Modo | Qué hace | Uso |
|---|---|---|
| **Full scan** (p. ej. m/z 40–450) | Guarda el espectro completo | Identificación por biblioteca, screening |
| **SIM** | Vigila 2–4 iones por analito | Cuantificación de trazas; 10–100× más sensible |
| **SIM/scan simultáneo** | Ambos | Lo mejor de los dos mundos en equipos modernos |
| **GC-MS/MS (triple cuadrupolo)** | Transiciones MRM | Pesticidas a µg/kg en matriz vegetal (`102`) |

Para cuantificar por SIM se declara un **ion cuantificador** y 1–2 **cualificadores**, con su razón de iones,
igual que en LC-MS/MS (`83`).

## Ejemplo aplicado — screening de volátiles de un extracto de reishi por HS-SPME-GC-MS

```
Pregunta de negocio: el lote nuevo de extracto huele distinto. Cambio el proceso
o cambio la materia prima?

Metodo (ILUSTRATIVO):
  1 g de extracto en polvo en vial de 20 mL, sellado.
  Equilibrio 60 C, 15 min. Fibra SPME DVB/CAR/PDMS expuesta 30 min.
  Desorcion 250 C, 3 min, splitless. Columna DB-5ms 30 m.
  Horno 40 C (3 min) -> 4 C/min -> 240 C. MS full scan 35-400.

Salida: lista de 30-60 picos con match de biblioteca y RI.
  - Si aparecen 2-metilbutanal, 3-metilbutanal, furfural y pirazinas ->
    reaccion de Maillard: el secado o la concentracion se hicieron mas
    calientes (62, 240). No cambio la materia prima; cambio el proceso.
  - Si aparecen hexanal, nonanal, 2-pentilfurano -> oxidacion de lipidos:
    problema de almacenamiento o de envase (61, 163).
  - Si aparecen etanol o acetato de etilo residuales -> secado incompleto
    tras extraccion hidroalcoholica (145, 87).

Costo (ILUSTRATIVO): COP 400.000-900.000 por muestra; 1-3 semanas.
Este analisis es SEMICUANTITATIVO: la fibra SPME no responde igual a todo.
Sirve para COMPARAR lotes bajo condiciones identicas, no para poner un
numero en la etiqueta.
```

Esa última frase es la regla de oro del SPME: **compara, no cuantifica**, salvo que se valide con estándares
marcados.

## Qué preguntarle al laboratorio

1. ¿La identificación es por **espectro solo** o por **espectro + RI**? ¿Corrieron patrón?
2. ¿Qué **biblioteca** usan y qué **match score mínimo** aceptan para reportar?
3. En headspace: ¿temperatura y tiempo de equilibrio, y en qué **diluyente**?
4. ¿La **calibración es en matriz** o en solvente? (Definitorio en extractos oleosos.)
5. ¿Usan **estándar interno**? ¿Cuál y en qué momento se agrega?
6. ¿El reporte es **cuantitativo** (mg/g, ppm) o **semicuantitativo** (% de área)? Que quede escrito.

## Errores comunes

- **Aceptar un "match 95 %" como identificación.** El score de biblioteca no es un porcentaje de certeza y
  confunde isómeros con facilidad.
- **Reportar % de área como si fuera concentración.** Sin factores de respuesta, el % de área no es masa.
- **Calibrar solventes residuales en agua para medirlos en aceite.** Sesgo sistemático a la baja (`87`).
- **Headspace con tiempo de equilibrio corto** "para ir más rápido": el resultado depende del reloj, no de
  la muestra.
- **Usar SPME para poner números en una etiqueta.** Es comparativo salvo validación específica.
- **Olvidar que el vial de headspace también aporta:** septum y tapas liberan siloxanos y volátiles; sin
  blanco de vial, aparecen "hallazgos" que son del consumible.

## Conexión con otros módulos

→ `82-espectrometria-de-masas-fundamentos.md` — por qué EI produce espectros de biblioteca.
→ `84-hrms-qtof-orbitrap-e-identificacion.md` — los niveles de confianza en identificación.
→ `85-cromatografia-de-gases.md` — la separación que alimenta este detector.
→ `87-solventes-residuales.md` — la aplicación regulada de headspace.
→ `62-maillard-y-pardeamiento.md` y `61-estabilidad-quimica-luz-calor-oxigeno.md` — qué significan los volátiles que aparecen.
→ `199-analisis-de-perfil-de-terpenos.md` — el perfil aromático del cannabis, con método.
→ `104-metabolomica-y-huella-quimica.md` — comparar lotes con datos de perfil.
