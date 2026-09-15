# 291 — Costos de análisis y presupuesto anual (cuánto cuesta de verdad tener calidad)

La pregunta que todo emprendedor hace tarde: "¿cuánto me cuesta analizar?". La respuesta útil no es un
precio por ensayo, es un **presupuesto anual** amarrado al plan de control por lote (`283`) y repartido en
el costo unitario del producto. Sin ese ejercicio pasan dos cosas: o se analiza de más al principio y no
queda plata para el resto del año, o se analiza de menos y el primer problema de calidad se lleva el margen
de tres meses. Aquí armas el número real, con órdenes de magnitud declarados y con la advertencia de que
**todo precio hay que cotizarlo**.

Términos: **ensayo (test)** = una determinación. **panel (panel/suite)** = paquete de varios ensayos con
precio agrupado. **TAT (turnaround time)** = tiempo de entrega del resultado. **rush fee** = recargo por
urgencia. **desarrollo y validación de método (method development and validation)** = trabajo puntual, caro,
que se paga una vez y sirve por años. **costo por unidad vendida** = el presupuesto anual dividido entre las
unidades que produces.

## Órdenes de magnitud por ensayo (referencia, no cotización)

Datos públicos: la lista de precios de CIA Labs, vigente desde el **2 de febrero de 2025** (USD), reporta
*assay* por HPLC o GC de un activo en **USD 290–425**, metales por ICP-OES en **USD 500–625**, titulación
en **USD 235–325**, solventes residuales USP <467> en **USD 1.200–5.000**, y un recargo del **50 %** por
entrega en 5 días. Los laboratorios grandes de suplementos (tipo Eurofins) reportan procesos completos de
verificación en el orden de **3 a 5 semanas**. Con eso como ancla, la tabla siguiente da órdenes de magnitud
para un laboratorio contratado; los valores en COP son conversiones aproximadas y **(ILUSTRATIVAS)**:

| Ensayo | Técnica | Orden de magnitud (USD) | TAT típico | Nota |
|---|---|---|---|---|
| Humedad | Gravimetría / Karl Fischer | 20–60 | 2–5 días | El más barato y el que más ordena todo (`07`) |
| Actividad de agua | Higrómetro | 20–50 | 2–5 días | Clave para vida útil (`35`) |
| Microbiología básica (aerobios, hongos/levaduras) | Cultivo | 40–90 | 5–7 días | |
| Patógenos (*Salmonella*, *E. coli*, *S. aureus*) | Cultivo / PCR | 60–150 | 5–10 días | |
| Activo por HPLC-UV (1 analito) | HPLC | 290–425 | 5–15 días | Referencia CIA Labs 2025 |
| β-glucano / α-glucano enzimático | Megazyme K-YBGL (`221`) | 120–250 | 7–15 días | **(ILUSTRATIVO)** — pocos labs lo tienen |
| Perfil de cannabinoides (potencia) | HPLC-DAD (`198`) | 60–200 | 3–7 días | Muy variable por país y volumen |
| Perfil de terpenos | GC-MS (`199`) | 100–250 | 5–10 días | |
| Metales pesados (4 elementos) | ICP-MS / ICP-OES (`88`) | 500–625 | 7–15 días | Referencia CIA Labs 2025 (ICP-OES) |
| Micotoxinas (aflatoxinas + OTA) | LC-MS/MS (`101`) | 150–350 | 7–15 días | **(ILUSTRATIVO)** |
| Pesticidas multiresiduo | LC-MS/MS + GC-MS/MS (`102`) | 250–600 | 10–20 días | Depende del número de analitos |
| Solventes residuales | GC-headspace USP <467> (`87`) | 1.200–5.000 | 7–15 días | Rango de la lista citada; suele ser menor por muestra en panel |
| Identidad por ADN/ITS | Secuenciación (`103`) | 100–300 | 10–20 días | **(ILUSTRATIVO)** |
| Estudio de estabilidad completo | Cámaras + ensayos por punto (`164`) | 3.000–12.000 por producto | 6–24 meses | Se paga por punto de tiempo |
| Desarrollo + validación de método | ICH Q2(R2) (`75`) | 5.000–20.000 | 2–6 meses | Una vez; sirve años |

**Todos estos números hay que cotizarlos.** Varían por país, por volumen, por acreditación y por matriz. Un
laboratorio universitario en Colombia puede estar muy por debajo; uno acreditado internacionalmente, por
encima. Lo que no varía es el orden relativo: humedad y microbiología son baratos, cromatografía es media,
espectrometría de masas y validación son lo caro.

## Presupuesto anual de una marca pequeña (ejemplo completo)

Escenario **(ILUSTRATIVO)**: 2 referencias (cápsulas de reishi y de melena de león), 6 lotes al año en
total, 3.000 unidades por lote = 18.000 unidades/año. Plan de control según `283`.

```
MATERIA PRIMA
  Identidad ITS               2 proveedores × 1 vez/año × USD 200 =   400
  β/α-glucano                 6 lotes × USD 180                   = 1.080
  Humedad                     6 lotes × USD 40                     =   240
  Metales (1 de cada 3)       2 × USD 550                          = 1.100
  Micotoxinas (1 de cada 3)   2 × USD 250                          =   500
                                                        subtotal   = 3.320

PRODUCTO TERMINADO
  β-glucano (label claim)     6 lotes × USD 180                    = 1.080
  Microbiología completa      6 lotes × USD 120                    =   720
  Actividad de agua           6 lotes × USD 35                     =   210
  Metales (1 de cada 5)       2 × USD 550                          = 1.100
  Disgregación (1 de cada 3)  2 × USD 80                           =   160
                                                        subtotal   = 3.270

ESTABILIDAD
  1 lote/año, 4 puntos de tiempo × 3 ensayos × USD 150             = 1.800

CONTINGENCIA (reanálisis, OOS, muestras extra) 15 %               = 1.259
                                                       -------------------
                                        TOTAL ANUAL ≈ USD 9.649  (ILUSTRATIVO)
```

Costo por unidad vendida: 9.649 / 18.000 ≈ **USD 0,54 por unidad**. Si tu producto se vende a USD 20, la
calidad analítica pesa un 2,7 % del precio; si se vende a USD 6, pesa un 9 % y hay que rediseñar el plan.
Ejecuta y verifica esta división con `Matematicas_lushows`, y lleva el número al modelo de costos con
`economist_lushows` y `contador_lushows` (la calidad es costo indirecto de producción, no gasto de
mercadeo).

Nota importante: el año 1 es más caro porque incluye lo que se paga una sola vez —validación de método,
identidad ITS de cada proveedor, primer estudio de estabilidad—. A partir del año 2, con skip-lot
justificado, el presupuesto recurrente suele bajar entre un 25 % y un 40 % **(ILUSTRATIVO)**.

## Siete formas legítimas de bajar el costo (y dos que no lo son)

Legítimas:

1. **Negociar un panel anual** con un solo laboratorio, con volumen comprometido (`292`). Descuentos
   típicos por volumen: 10–25 % **(ILUSTRATIVO)**.
2. **Skip-lot justificado con datos**, no con ganas (`283`).
3. **Muestra compuesta** para parámetros de seguridad de un mismo origen, cuando la norma lo permite.
4. **Hacer en casa lo barato y robusto**: humedad, a_w, peso, aspecto. Una balanza halógena y un higrómetro
   se pagan solos en meses.
5. **Evitar el rush.** El recargo por urgencia puede ser del 50 % (lista CIA Labs 2025). Planear el
   cronograma de lotes es gratis.
6. **Método propio validado una vez** en vez de pagar método a la medida cada año.
7. **Compartir cámara de estabilidad** con una universidad o un laboratorio aliado.

No legítimas:

- **Lab shopping**: mandar la muestra a varios laboratorios y quedarte con el resultado que te gusta (`113`).
- **Analizar el "mejor lote"** y usar ese COA para todos. Es lo que rompe la confianza de un cliente B2B, y
  cuando lo descubren no hay vuelta.

## Ejemplo aplicado (BIO-SETA)

Con presupuesto anual cerrado en USD ~9.650 **(ILUSTRATIVO)** y 18.000 unidades, la decisión que aparece es
clara: no se puede analizar todo en cada lote, así que la plata va a lo que sostiene el claim (β-glucano) y
a lo que evita el daño (microbiología y metales por origen). Lo que se sacrifica —disgregación, pesticidas—
se documenta con justificación de riesgo, no se omite en silencio. Un plan escrito con lo que **no** haces
y por qué es defendible; un plan sin esa sección parece un olvido.

## Errores comunes

- **Pedir "un análisis completo"** sin decir qué se decide: te venden el panel más caro y falta lo que
  necesitabas (`00`).
- **Presupuestar solo el año 1** y quedarse sin plata para la estabilidad del año 2.
- **Olvidar el costo del producto que se destruye** en el muestreo: cada muestra son unidades que no vendes.
- **No presupuestar reanálisis.** Siempre hay uno. El 15 % de contingencia no es opcional.
- **Comparar precios entre laboratorios sin comparar el método.** Un β-glucano por colorimetría es más
  barato porque **no mide lo mismo** (`222`).
- **Pagar rush por mala planeación** de forma sistemática: es el 50 % más, todos los meses.

## Conexión con otros módulos

→ `114-costos-y-tiempos-de-analisis.md` — el detalle técnico por técnica analítica.
→ `283-plan-de-control-de-calidad-por-lote.md` — el plan que genera este presupuesto.
→ `292-negociar-con-laboratorios-y-maquiladores.md` — cómo bajar el precio sin bajar la calidad.
→ `108-como-elegir-un-laboratorio.md` — a quién le pides la cotización.
→ `113-lab-shopping-e-inflacion-de-potencia.md` — el atajo que no se toma.
→ `164-estabilidad-ich-q1-y-vida-util.md` — la partida más subestimada del presupuesto.