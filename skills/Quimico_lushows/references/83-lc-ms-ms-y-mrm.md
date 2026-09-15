# 83 — LC-MS/MS y MRM: cómo se miden trazas de verdad (micotoxinas, pesticidas, psilocibina)

Cuando el número que necesitas está en partes por billón —una micotoxina a 2 µg/kg, un pesticida a
10 µg/kg, psilocina en plasma a 1 ng/mL— el HPLC con UV ya no sirve: el analito se pierde en el ruido y en
la matriz. La respuesta de la industria es LC-MS/MS en modo MRM, y es hoy el método de referencia para
casi todos los contaminantes de alimentos y suplementos. Entenderlo te sirve para dos cosas muy concretas:
saber cuándo exigirlo (y cuándo te lo están vendiendo de más) y saber leer un COA que lo usa.

Términos:
- **Triple cuadrupolo (triple quadrupole, QqQ)** = tres cuadrupolos en fila: Q1 selecciona, q2 fragmenta,
  Q3 selecciona el fragmento.
- **MRM / SRM (multiple reaction monitoring)** = vigilar un par precursor → producto. Es "un filtro doble".
- **Transición (transition)** = ese par de m/z, por ejemplo 285,1 → 205,1.
- **Cuantificador y cualificador (quantifier / qualifier ion)** = la transición con la que se cuantifica y la
  segunda que confirma la identidad.
- **Razón de iones (ion ratio)** = área del cualificador ÷ área del cuantificador. Debe parecerse a la del
  patrón.
- **Estándar interno isotópico (stable isotope-labeled internal standard, SIL-IS)** = la misma molécula con
  átomos pesados (¹³C, D). Corrige efecto matriz y pérdidas.

## Por qué MRM es tan selectivo

```
Q1 (filtro 1)        q2 (celda de colision)        Q3 (filtro 2)
deja pasar solo      rompe el ion con gas          deja pasar solo un
m/z 285,1            argon/nitrogeno a X eV        fragmento, m/z 205,1

Para que un compuesto de la matriz de un falso positivo tendria que (a) eluir
al mismo tiempo de retencion, (b) tener el mismo m/z de precursor Y (c) producir
el mismo fragmento con la misma abundancia relativa. Esa triple coincidencia es
rarisima: por eso el ruido cae varios ordenes de magnitud y se pueden medir
ug/kg (ppb) e incluso ng/kg (ppt) en matrices sucias.
```

## Los criterios de identificación (lo que hace defendible un positivo)

A agosto de 2026 el marco más usado en alimentos y piensos en la UE es el documento
**SANTE/11312/2021 (con su revisión v2 de 2023)** para residuos de plaguicidas, y la
**Reg. (UE) 2021/808** para residuos en productos de origen animal. En EE. UU. rigen criterios equivalentes
en los métodos oficiales de la FDA y de AOAC. Verifica siempre la versión vigente antes de citarla en un
expediente. Los criterios prácticos son:

| Criterio | Exigencia típica | Por qué existe |
|---|---|---|
| **Tiempo de retención** | Dentro de ±0,1 min (o ±2 %) del patrón en la misma secuencia | Un ion correcto en el tiempo equivocado no es tu analito |
| **Número de transiciones** | Mínimo **2** (1 cuantificador + 1 cualificador) | Una sola transición no confirma nada |
| **Razón de iones** | Dentro de ±30 % de la del patrón (criterio SANTE) | Detecta interferencia coeluyente |
| **Señal/ruido** | ≥ 3 en LOD, ≥ 10 en LOQ (`73`) | Que el pico exista de verdad |
| **Recuperación** | 70–120 % con RSD ≤ 20 % (residuos) | Que el método extraiga lo que dice |

Si un COA reporta un positivo de pesticida y no reporta la razón de iones ni el número de transiciones, no
tienes un positivo confirmado: tienes una señal. Eso es motivo legítimo para impugnar (`112`).

## Efecto matriz: lo que decide si el número sirve

Ya explicado en `82`. En LC-MS/MS se maneja con tres herramientas, en orden de calidad:

| Estrategia | Cómo | Calidad | Costo |
|---|---|---|---|
| **SIL-IS** (estándar interno marcado) | Se agrega ¹³C/D del propio analito antes de extraer | La mejor: corrige extracción y supresión | Alto (patrones marcados caros) |
| **Calibración en matriz (matrix-matched)** | La curva se prepara sobre extracto blanco de tu matriz | Buena si hay blanco real | Medio |
| **Adición de estándar (standard addition)** | Se fortifica la propia muestra a varios niveles (`72`) | Buena, laboriosa | Alto en tiempo |
| Curva en solvente puro | — | **Insuficiente en matrices sucias** | Bajo |

Para hongos y cannabis la respuesta correcta es SIL-IS o matrix-matched. Sin eso, la recuperación se cae y
nadie se entera.

## Caso 1 — psilocibina y psilocina por LC-MS/MS

Este es el análisis que sostiene la investigación clínica y el control de calidad en jurisdicciones donde el
trabajo con psilocibina es legal (ver `263` para el estado regulatorio a agosto de 2026 y `256` para el
método completo). El punto químico clave: **la psilocibina es el éster fosfato, muy polar y zwitteriónico;
la psilocina es su forma desfosforilada, menos polar y muy propensa a oxidarse** (`251`, `255`). Medirlas
juntas exige cromatografía que retenga lo polar y una preparación que no deje oxidar la psilocina.

```
Condiciones tipicas reportadas en la literatura de metodo (ILUSTRATIVO — verifica
contra el metodo del laboratorio que contrates):

  Columna     : C18 compatible con 100 % acuoso, o HILIC (81)
  Fase movil  : A agua + 0,1 % acido formico (o formiato de amonio 5-10 mM)
                B acetonitrilo + 0,1 % acido formico
  Fuente      : ESI positivo
  Precursores : psilocibina [M+H]+ = 285,1  |  psilocina [M+H]+ = 205,1
  Transiciones reportadas:
      psilocibina  285,1 -> 205,1  (cuantificador)
                   285,1 -> 160,1  (cualificador)
      psilocina    205,1 -> 58,1   (cuantificador)
                   205,1 -> 160,1  (cualificador)
  Estandar interno: psilocina-d10 o psilocibina marcada (13C o D)
  Rango tipico en material vegetal: 0,01 - 2 % p/p base seca (254)
  Rango tipico en plasma: 0,1 - 100 ng/mL (258)

Precauciones criticas del metodo:
  - Antioxidante (acido ascorbico) y trabajo protegido de la luz: la psilocina
    se oxida a productos azules en minutos-horas (255).
  - Evitar calor: la psilocibina se desfosforila a psilocina y el reparto entre
    ambas cambia -> hay que reportar LAS DOS y su suma como psilocibina
    equivalente, declarando el factor usado.
  - Homogeneizar de verdad: la variabilidad entre partes del mismo hongo es
    enorme (254, 67) y el muestreo domina la incertidumbre, no el equipo.
```

Frontera de esta skill: aquí se cubre **cómo se mide, con qué unidad y con qué controles**. No se dan rutas
de producción, cultivo ni extracción para uso ilícito.

## Caso 2 — micotoxinas multi-residuo

La aplicación LC-MS/MS más común en suplementos de hongos y cannabis. Detalle completo en `101`; aquí, la
parte técnica:

| Micotoxina | Precursor típico [M+H]+ | Por qué MRM y no UV |
|---|---|---|
| Aflatoxina B1 | 313,1 | Límites de 2–5 µg/kg: fuera del alcance de UV en matriz vegetal |
| Aflatoxina B2, G1, G2 | 315,1 / 329,1 / 331,1 | Se reportan como suma B1+B2+G1+G2 |
| Ocratoxina A | 404,1 | Límites de 2–20 µg/kg según alimento |
| Zearalenona | 319,1 (a menudo ESI−, 317,1) | Modo negativo mejor |
| Deoxinivalenol (DON) | 297,1 | Muy polar; suele necesitar aducto de amonio |

Preparación típica: extracción acetonitrilo/agua, limpieza por inmunoafinidad o QuEChERS (`69`), calibración
en matriz, SIL-IS ¹³C para aflatoxinas. Costo (ILUSTRATIVO): COP 350.000–900.000 para un panel de 5–12
micotoxinas; 5–12 días hábiles.

## Cómo se lee un resultado MRM en un COA

```
Ejemplo de reporte correcto (ILUSTRATIVO):

  Analito      : Aflatoxina B1
  Metodo       : LC-MS/MS, ESI+, MRM, calibracion matrix-matched, SIL-IS 13C17-AFB1
  Transiciones : 313,1 -> 285,1 (cuant.) ; 313,1 -> 241,1 (cualif.)
  Razon de iones: 0,42 (patron 0,45; desviacion 7 % — dentro de +-30 %)
  Recuperacion : 92 % (spike a 4 ug/kg)   |   LOQ: 0,5 ug/kg
  Resultado    : < LOQ  (no "0", no "ausente")
  Incertidumbre: U = 35 % (k=2) al nivel del limite

Ejemplo de reporte insuficiente:
  "Aflatoxinas: negativo."     <- sin metodo, sin LOQ, sin unidad. No sirve (111).
```

## Qué preguntarle al laboratorio

1. ¿Cuántas **transiciones** por analito y cuál es su criterio de **razón de iones**?
2. ¿Calibran **en matriz** o en solvente? ¿Usan **estándar interno isotópico**? ¿Cuál?
3. ¿Cuál es el **LOQ en mi matriz** (no en agua) y cómo lo verificaron? (`73`)
4. ¿Cuál fue la **recuperación del spike** en mi tanda? (`77`)
5. ¿Qué **efecto matriz** midieron para mis analitos en mi tipo de muestra?
6. ¿El ensayo está dentro de su **alcance acreditado ISO 17025** para esta matriz? (`107`)
7. Para psilocibina: ¿reportan psilocibina y psilocina por separado, y con qué factor las suman?

## Errores comunes

- **Aceptar un positivo con una sola transición.** No es confirmación; es una alerta.
- **Reportar "0" en vez de "< LOQ".** Cero no existe en química analítica (`73`).
- **Pagar LC-MS/MS para potencia de cannabinoides.** Es innecesario y peor: los cannabinoides al 10–20 % p/p
  saturan el detector. Para potencia, HPLC-DAD (`79`).
- **Comparar LOQ entre laboratorios sin mirar la matriz.** Un LOQ en agua no dice nada sobre tu extracto.
- **Analizar psilocibina sin antioxidante ni protección de luz** y concluir que el material "perdió potencia"
  cuando la perdió el vial (`255`).
- **Ignorar el muestreo.** En hongos, la variabilidad entre ejemplares supera la del instrumento (`66`, `67`).

## Conexión con otros módulos

→ `82-espectrometria-de-masas-fundamentos.md` — la base de fuentes, aductos y efecto matriz.
→ `72-estandar-interno-y-adicion-de-estandar.md` — la corrección que hace confiable el número.
→ `84-hrms-qtof-orbitrap-e-identificacion.md` — cuando no sabes qué buscar.
→ `101-analisis-de-micotoxinas.md` — límites, matrices y estrategia completa.
→ `102-pesticidas-multiresiduo.md` — el otro gran panel por LC-MS/MS.
→ `256-analisis-de-psilocibina-hplc-y-lc-ms.md` — el método de psilocibios punta a punta.
→ `255-estabilidad-y-degradacion-de-psilocibina.md` — por qué el vial también es parte del método.
