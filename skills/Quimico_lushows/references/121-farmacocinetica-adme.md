# 121 — Farmacocinética y ADME (lo que el cuerpo le hace a la sustancia)

Farmacocinética es la mitad que casi nadie mide en el mundo de los suplementos y es, con diferencia, la que
más promesas tumba. Puedes tener la molécula más activa del mundo `[in vitro]` y no pasar nada en una
persona porque no se absorbe, se destruye en el hígado o no llega al tejido donde está el receptor. Este
módulo te da el marco ADME y los cuatro parámetros que resumen todo: Cmax, Tmax, AUC y vida media. El error
caro que evita: formular un producto por contenido de activo sin preguntarse jamás cuánto de eso llega a
sangre.

Términos: **ADME** = Absorción, Distribución, Metabolismo, Excreción. **Cmax (peak plasma concentration)** =
concentración máxima en plasma. **Tmax (time to peak)** = cuándo se alcanza. **AUC (area under the curve)**
= área bajo la curva concentración-tiempo; es la medida de **exposición total**. **Vd (volume of
distribution)** = volumen aparente en el que la sustancia parece disolverse; alto = se va a los tejidos.
**Aclaramiento (clearance, CL)** = volumen de plasma depurado por unidad de tiempo (L/h).

## Las cuatro letras

### A — Absorción
Depende de solubilidad, permeabilidad, pH del tracto, transportadores (P-gp expulsa hacia el lumen),
tiempo de tránsito y de la comida. Un cannabinoide muy lipofílico se absorbe mejor con grasa `[clínico]`;
un polisacárido de alto peso molecular prácticamente no se absorbe intacto (ver `130`).

### D — Distribución
Gobernada por lipofilia, unión a proteínas plasmáticas (albúmina, α1-glicoproteína ácida) y barreras.
El THC tiene Vd muy alto y se acumula en tejido adiposo, lo que explica su detección prolongada en orina
`[clínico]` (ver `204`, `205`). Solo la **fracción libre** puede actuar.

### M — Metabolismo
Fase I (oxidación, principalmente CYP450 — ver `124`) y Fase II (conjugación — ver `125`). El hígado es el
sitio principal, pero también hay metabolismo intestinal y microbiano (ver `131`).

### E — Excreción
Renal (favorece lo polar), biliar/fecal (favorece lo grande y conjugado) y, en menor medida, pulmonar y
sudor. La circulación enterohepática puede reciclar el compuesto y alargar su presencia.

## La curva y sus parámetros

```
Concentración plasmática
     │        ╭─╮  ← Cmax
     │      ╭─╯ ╰──╮
     │    ╭─╯      ╰───╮
     │  ╭─╯             ╰────╮
     └──┴───┴──────────────────► tiempo
         Tmax        AUC = toda el área bajo la curva
```

| Parámetro | Qué decide | Por qué te importa comercialmente |
|---|---|---|
| Cmax | Intensidad del pico | Efectos agudos y también efectos adversos de pico |
| Tmax | Rapidez | "En cuánto tiempo se siente" (sublingual vs oral, ver `123`) |
| AUC | Exposición total | Es **el** parámetro para comparar dos formulaciones |
| t½ | Duración | Frecuencia de dosis (ver `126`) |
| F (biodisponibilidad) | Fracción que llega intacta | El número que decide si la formulación sirve (`122`) |

Relaciones que se usan a diario:

```
F  =  (AUC_oral / Dosis_oral)  ÷  (AUC_IV / Dosis_IV)
CL =  Dosis_IV / AUC_IV
Vd =  CL / ke        donde ke = 0,693 / t½
```

Cualquiera de estas cuentas va a `Matematicas_lushows` o a un script, nunca a la cabeza.

## Modelos: uno y dos compartimentos

- **Un compartimento**: el cuerpo se comporta como un solo tanque; el log de la concentración cae en línea
  recta. Aproximación aceptable para muchas moléculas hidrofílicas.
- **Dos compartimentos**: hay una caída rápida (distribución, fase α) y luego una lenta (eliminación, fase
  β). Los cannabinoides son el ejemplo típico: la t½ terminal es larguísima porque salen despacio de la
  grasa, aunque el efecto ya pasó hace horas.

Consecuencia práctica: **la t½ terminal no predice la duración del efecto** cuando hay dos compartimentos.
Es un error que se comete constantemente al hablar de THC.

## Cómo se mide

| Estudio | Diseño | Muestras | Método analítico | Nivel |
|---|---|---|---|---|
| PK preclínica | Roedor, 3–6 puntos por animal | Plasma | LC-MS/MS (`83`) | `[animal]` |
| PK humana básica | 8–16 voluntarios, dosis única, 10–14 tiempos | Plasma, orina | LC-MS/MS validado (ICH M10) | `[clínico fase 1]` |
| Bioequivalencia | Cruzado 2×2, ayuno y con comida | Plasma | LC-MS/MS | `[clínico fase 1]` |
| Balance de masas | Marcaje radiactivo (¹⁴C) | Plasma, orina, heces | Radio-HPLC | `[clínico fase 1]` |

Sin **método bioanalítico validado** (linealidad, LOQ, exactitud, recuperación en matriz, estabilidad en
plasma) no hay dato de PK: hay ruido. Ver `75` para el marco de validación.

## Ejemplo aplicado — la pregunta que hunde un lanzamiento

BIO-SETA quiere lanzar una tintura de melena de león con claim de "absorción superior". Se plantea así:

1. ¿Cuál es el analito que se va a medir en plasma? Si la respuesta es "el extracto", no hay estudio
   posible. Hay que elegir una molécula: hericenona C, erinacina A, o un marcador propio.
2. ¿Existe método bioanalítico para esa molécula en plasma humano? Si no, hay que desarrollarlo y validarlo
   (costo y tiempo reales: meses, no semanas).
3. Costo estimado de un PK cruzado de 12 sujetos **(ILUSTRATIVO)**: decenas de millones de pesos. Ese
   número decide si el claim vale la pena o si se comunica otra cosa.
4. Alternativa honesta y barata: no reclamar absorción superior. Reclamar lo que sí se puede medir —
   contenido de β-glucano por Megazyme, identidad por ITS, ausencia de contaminantes. Eso sí es verificable
   y es lo que diferencia de verdad (ver `247`).

## Errores comunes

- Formular por "mg de activo" sin preguntar cuánto se absorbe. Un mg que no se absorbe es un mg de nada.
- Comparar Cmax entre estudios con distinto estado de ayuno. La comida cambia la absorción radicalmente.
- Usar la t½ terminal para decidir la frecuencia de dosis cuando el modelo es de dos compartimentos.
- Reclamar "mayor biodisponibilidad" sin AUC comparativa contra un producto de referencia (ver `122`).
- Medir en plasma una molécula que no existe en plasma porque se metaboliza toda en el primer paso.
- Olvidar la unión a proteínas: 99 % unido significa que solo el 1 % puede actuar.

## Conexión con otros módulos

→ `122-biodisponibilidad-y-efecto-de-primer-paso.md` — el detalle de F y del hígado.
→ `123-vias-de-administracion.md` — cómo cambia todo según por dónde entre.
→ `124-citocromo-p450-e-interacciones.md` — la M de metabolismo, en detalle.
→ `126-vida-media-y-regimen-de-dosis.md` — de una dosis al régimen diario.
→ `159-potenciadores-de-biodisponibilidad.md` — qué funciona y qué es humo.