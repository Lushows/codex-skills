# 152 — Estandarización de extractos (la única promesa que se puede medir y defender)

Estandarizar es fijar un compuesto marcador, un método para medirlo y un rango que todos tus lotes deben
cumplir; y ajustar el proceso o la mezcla para que lo cumplan. Es lo contrario del ratio (`151`): en vez de
describir cómo se hizo, describe **qué hay adentro**. Un extracto estandarizado se puede comprar, vender,
auditar, reclamar y defender ante INVIMA. Un extracto "10:1" no. Esta es la diferencia entre tener un producto
y tener una historia.

Términos: **marcador (marker compound)** = compuesto que se mide para representar la calidad del extracto.
**Marcador activo (active marker)** = el responsable del efecto. **Marcador analítico (analytical marker)** =
el que se mide por conveniencia, sin ser necesariamente el activo. **Estandarización (standardization)** =
ajustar el lote a un contenido definido de marcador. **Ajuste (blending / spiking con soporte)** = mezclar
lotes o agregar soporte para llegar al rango.

## Marcador activo vs marcador analítico: la distinción honesta

| Producto | Marcador | ¿Activo o analítico? | Método |
|---|---|---|---|
| Reishi acuoso | β-glucano | Activo respaldado `[in vitro]`/`[animal]` para inmunomodulación (`130`) | Megazyme K-YBGL (`221`) |
| Reishi alcohólico | Ácidos triterpénicos totales | Mixto; se expresa como ác. ganodérico A | HPLC-DAD (`224`) |
| Melena de león | Hericenonas / erinacinas | Activo candidato, evidencia limitada (`226`) | HPLC / LC-MS |
| Cordyceps | Cordicepina, adenosina | Activo/analítico según especie (`228`) | HPLC |
| Chaga | Polifenoles, betulina | Analítico | HPLC / colorimétrico |
| Cannabis CBD | CBD y THC total | Activo | HPLC-DAD (`198`) |
| Cualquier hongo | Ergosterol | **Analítico puro** — marca presencia de biomasa fúngica | HPLC (`238`) |

Regla de honestidad: si tu marcador es **analítico**, dilo. "Estandarizado a 2 % de ergosterol" no implica un
efecto; implica que hay hongo de verdad. Es un dato de identidad, no de potencia funcional. Presentarlo como
activo es exactamente el tipo de exageración que después no se puede sostener (`293`).

## Cómo se elige el marcador

Cuatro criterios, en orden:

1. **¿Sostiene tu claim?** Si vas a decir "aporta β-glucanos", el marcador es β-glucano. Punto.
2. **¿Existe un método validado y accesible en Colombia?** Un marcador que ningún laboratorio local mide te
   condena a exportar muestras (`108`, `114`).
3. **¿Es estable?** Un marcador que se degrada en 3 meses te va a reprobar la estabilidad (`164`).
4. **¿Es específico?** Que no lo aporten el soporte ni el sustrato. El β-glucano cumple; los "polisacáridos
   totales", no (`222`).

## Las tres formas legítimas de llegar al rango

```
1. AJUSTAR EL PROCESO
   Cambiar solvente, tiempo, etapas o relación S/L hasta que el extracto nativo dé el %.
   La mejor: no diluye nada, mejora el producto de verdad.

2. MEZCLA DE LOTES (blending)
   Combinar un lote alto con uno bajo para caer en el rango.
   Ecuación de mezcla:
       C_mezcla = (m1·C1 + m2·C2) / (m1 + m2)
   Ejemplo (ILUSTRATIVO): 40 kg al 41,0 % + 60 kg al 29,5 %
       C = (40×41,0 + 60×29,5)/100 = 34,1 % p/p b.s.
   Requiere: los dos lotes conformes en TODO lo demás (metales, micro), y registro del blending (`168`).

3. AJUSTE CON SOPORTE (standardization down)
   Bajar un lote muy potente hasta el rango con celulosa, fibra de acacia o el propio polvo de hongo.
   Legítimo SI se declara en la fórmula cuantitativa.
       masa de soporte = m_extracto × (C_real / C_objetivo − 1)
   Ejemplo (ILUSTRATIVO): 10,00 kg al 44,0 %, objetivo 35,0 %
       soporte = 10,00 × (44,0/35,0 − 1) = 2,571 kg  →  total 12,571 kg al 35,0 %
```

Lo que **no** es legítimo: agregar β-glucano de levadura o de avena a un extracto de hongo y seguir llamándolo
extracto de hongo. Eso es adulteración, es detectable (la estructura y el perfil son distintos) y es fraude
(`246`).

## Cómo se comprueba una estandarización

Un extracto estandarizado necesita, mínimo, tres lotes analizados para que el rango tenga sentido estadístico.
Un solo lote no es una especificación (`282`).

```
DEFINIR EL RANGO A PARTIR DE DATOS REALES

  Lote 1: 36,2 %      Lote 2: 34,8 %      Lote 3: 37,5 %   (% p/p β-glucano b.s., Megazyme)
  media = 36,17 %     desviación estándar s = 1,35 %
  incertidumbre del método (`76`): ±2,0 % absoluto (dato del laboratorio)

  Especificación propuesta:  ≥ 32,0 % p/p base seca
  Racional: media − 3s ≈ 32,1 %, y queda margen sobre la incertidumbre analítica.
  (Cifras ILUSTRATIVAS: haz la cuenta con tus lotes, en código.)

  Declaración de etiqueta: usar SIEMPRE el mínimo especificado, nunca la media.
  Si declaras 36 % y un lote da 34 %, incumpliste tu propia etiqueta.
```

Ese último renglón vale un lote entero: **la etiqueta declara el mínimo garantizado, no el promedio bonito.**

## Cómo se escribe en la etiqueta

| Formulación de etiqueta | Veredicto |
|---|---|
| "Extracto de reishi 10:1, 500 mg" | Vacío. Ratio sin activo (`151`) |
| "Extracto de reishi, 500 mg, estandarizado a 30 % de polisacáridos" | Engañoso: polisacáridos incluye almidón (`222`) |
| "Extracto de reishi 500 mg, ≥ 30 % β-glucano (Megazyme), aporta ≥ 150 mg de β-glucano por cápsula" | **Correcto y auditable** |
| "Extracto dual de reishi 500 mg: ≥ 25 % β-glucano y ≥ 1,5 % triterpenos (como ác. ganodérico A)" | **Correcto, extracto dual honesto** (`146`) |

A agosto de 2026, en Colombia el contenido y la forma de la declaración de un suplemento dietario se rigen por
el Decreto 3249 de 2006 y las normas de etiquetado vigentes; verifica el texto exacto exigido antes de imprimir
(`266`, `272`). Ninguna de estas formulaciones incluye un claim de enfermedad, y eso es deliberado (`267`,
`268`).

## Ejemplo aplicado — de proceso a especificación, BIO-SETA

```
1. Claim comercial deseado: "aporta 300 mg de β-glucano por porción diaria" (2 cápsulas).
2. → cada cápsula debe aportar 150 mg de β-glucano.
3. Cápsula tamaño 0 con este polvo llena ~500 mg (verificar por densidad, `154`).
4. % requerido en el extracto = 150 / 500 × 100 = 30,0 % p/p base seca.
5. ¿El proceso lo da? Lotes piloto: 36,2 / 34,8 / 37,5 %  → SÍ, con margen.
6. Especificación del extracto: β-glucano ≥ 32,0 % p/p b.s. (Megazyme K-YBGL),
   α-glucano ≤ 6,0 %, humedad ≤ 5,0 %, soporte declarado.
7. Especificación de producto terminado: 150 mg ± 10 % de β-glucano por cápsula (`282`).
8. Verificación por lote: 1 ensayo de β-glucano sobre muestra compuesta de 10 cápsulas (`283`).
```

Fíjate en el orden: el claim manda, el % se deriva, el proceso se verifica. No al revés. Todos los números de
arriba son **(ILUSTRATIVOS)**; el cálculo real va a `lab-tools/betaglucano_dosis.py` (`161`).

## Errores comunes

- Estandarizar contra "polisacáridos totales". Es el error #1 del sector y hace inútil toda la estandarización.
- Declarar el promedio en vez del mínimo garantizado.
- Fijar la especificación con un solo lote y descubrir en el tercero que el rango era imposible.
- Cambiar de proveedor de extracto y mantener la etiqueta: el marcador cambia y hay que revalidar (`169`).
- Estandarizar con un marcador que ningún laboratorio colombiano mide: cada lote se vuelve una exportación.
- Ajustar hacia abajo con soporte y no declararlo en la fórmula cuantitativa. Es un hallazgo de auditoría.
- Confundir estandarización con adulteración: agregar el marcador aislado de otra fuente no es estandarizar.

## Conexión con otros módulos

→ `151-relacion-planta-extracto-y-ratios.md` — el número que la estandarización viene a reemplazar.
→ `221-medir-beta-glucanos-metodo-megazyme.md` — el método que sostiene el marcador estrella.
→ `161-dosis-y-tamano-de-porcion.md` — cómo se decide el mg objetivo por porción.
→ `282-especificacion-de-producto-terminado.md` — dónde aterriza todo esto.
→ `246-adulteracion-y-fraude-en-suplementos-de-hongos.md` — la frontera con lo ilegítimo.
