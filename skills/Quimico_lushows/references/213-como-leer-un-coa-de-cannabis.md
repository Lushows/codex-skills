# 213 — Cómo leer un COA de cannabis (campo por campo, con las banderas rojas del sector)

Un **certificado de análisis (COA, certificate of analysis)** es el documento con el que se compra, se vende
y se defiende un lote de cannabis. También es el documento que más se falsifica, se recicla y se lee mal.
Este módulo es un COA comentado línea por línea: qué significa cada campo, qué unidad debe tener, qué
resultado es imposible, y cuáles son las banderas rojas propias de este sector —que no son las mismas que en
alimentos o en suplementos—. Si aprendes a leer estas dos páginas, dejas de depender de la buena fe de tu
proveedor.

Términos: **COA** = certificado de análisis. **Lote (batch/lot)** = unidad de producción trazable.
**LOQ (limit of quantitation)** = mínimo cuantificable. **ND (not detected)** = por debajo del LOD.
**Base tal cual (as-is)** frente a **base seca (dry weight)** = con o sin el agua de la muestra.

## Encabezado: seis campos y por qué cada uno importa

| Campo | Qué debe decir | Bandera roja |
|---|---|---|
| Laboratorio, dirección, número de acreditación | Nombre completo y número ISO/IEC 17025 verificable | Solo un logo, sin número de acreditación |
| Cliente | Quien pidió el análisis | Si el cliente es distinto de tu proveedor, ese COA no es de tu cadena |
| Identificación de muestra y **lote** | Código de lote que coincida con tu producto | COA sin número de lote: es publicidad, no un certificado |
| Fecha de recepción y **fecha de análisis** | Ambas, separadas | Un COA de hace tres años usado para un lote nuevo |
| Matriz | Flor, extracto, comestible, tópico | Matriz genérica ("cannabis") cuando el método se valida por matriz |
| Método y su referencia | "HPLC-DAD, SOP-XXX" o método oficial | "Método interno" sin más, o ausencia total del método |

La verificación de acreditación se hace en el directorio del organismo acreditador (A2LA, ANAB, ONAC en
Colombia), no confiando en el PDF. Y hay que mirar el **alcance**: un laboratorio puede estar acreditado para
potencia en flor y no para pesticidas en comestibles (ver `107`).

## Potencia: formas ácidas, neutras y THC total

Así se ve un bloque de potencia bien hecho:

```
CANNABINOIDES — HPLC-DAD, base seca, humedad 10,4 % (Karl Fischer)
Analito        Resultado (% p/p)   Resultado (mg/g)    LOQ (% p/p)
THCA                 18,42              184,2             0,05
Δ9-THC                0,61                6,1             0,03
Δ8-THC                 ND                  ND             0,03
CBDA                  0,42                4,2             0,05
CBD                   0,08                0,8             0,03
CBGA                  0,95                9,5             0,05
CBG                   0,11                1,1             0,03
CBN                   0,07                0,7             0,03
CBC                   0,15                1,5             0,03
THCV                   ND                  ND             0,05
--------------------------------------------------------------
THC total = 0,61 + (18,42 × 0,877) = 16,77 % p/p
CBD total = 0,08 + (0,42 × 0,877) = 0,45 % p/p
Cannabinoides totales = 20,81 % p/p
```

Lo que se verifica en este bloque:

1. **Que estén las formas ácidas Y las neutras separadas.** Si solo aparece "THC" sin THCA, el análisis fue
   por GC (que descarboxila en el inyector) o el laboratorio sumó por su cuenta. En flor, THCA debe ser
   varias veces mayor que Δ9-THC; lo contrario indica material viejo, calentado, o un método equivocado.
2. **Que el THC total esté calculado con 0,877** y que el número cuadre. Rehaz la cuenta: es la comprobación
   más rentable que existe (ver `175`).
3. **Que diga la base y la humedad.** Sin eso no puedes comparar con otro COA (ver `07`).
4. **Que haya LOQ por analito.** "ND" sin LOQ no es un resultado.
5. **Que la suma tenga sentido.** Cannabinoides totales del 35 % en flor seca es fisiológicamente
   inverosímil; en extractos sí, en flor no.

## Terpenos: la sección más manipulada

```
TERPENOS — GC-MS, estándar interno n-tridecano, base tal cual
β-Mirceno              6,81 mg/g     LOQ 0,05 mg/g
D-Limoneno             3,22 mg/g
β-Cariofileno          4,10 mg/g
α-Humuleno             1,52 mg/g
Óxido de cariofileno   0,31 mg/g
Linalool               0,88 mg/g
α-Pineno               1,44 mg/g
[... panel completo, 21 analitos, con los ND declarados ...]
Terpenos totales      18,28 mg/g  (1,83 % p/p)
```

Verificaciones específicas:
- **El panel completo, con los ND.** Si solo listan los que salieron, no sabes qué buscaron.
- **Estándar interno declarado.** Sin él no hay corrección de pérdidas (ver `72`, `199`).
- **La relación óxido de cariofileno / β-cariofileno.** Alta = material oxidado o viejo.
- **Terpenos en un destilado.** Si aparecen, fueron reintroducidos. Legítimo, pero debe estar declarado.
- **Coherencia de la suma**: los individuales deben sumar el total reportado.

## Pesticidas: contra qué límite se compara

```
PESTICIDAS — LC-MS/MS y GC-MS/MS, calibración en matriz, panel de 66 analitos
Analito         Resultado (µg/kg)   LOQ (µg/kg)   Límite aplicado (µg/kg)   Estado
Miclobutanil          ND                 10             Prohibido              Pasa
Bifenazato            42                 10               200                  Pasa
Piperonilbutóxido    118                 10              2.000                 Pasa
[... 63 analitos más ...]
```

Banderas rojas: panel corto (menos de 40 analitos en un mercado que exige más), **LOQ mayor que el límite**
(entonces "pasa" no significa nada), ausencia de la columna de límite aplicado, o límite tomado de alimentos
cuando el producto se inhala (ver `200`).

## Metales pesados

```
METALES PESADOS — ICP-MS, digestión por microondas
Plomo (Pb)       0,082 mg/kg   LOQ 0,010   Límite 0,5   Pasa
Cadmio (Cd)      0,031 mg/kg   LOQ 0,010   Límite 0,2   Pasa
Arsénico (As)    0,044 mg/kg   LOQ 0,010   Límite 0,2   Pasa
Mercurio (Hg)      ND          LOQ 0,005   Límite 0,1   Pasa
```

Qué mirar: que la técnica sea ICP-MS (no AAS si el límite es bajo), que el LOQ sea al menos 5–10 veces menor
que el límite, y que para producto **inhalado** el límite sea el de inhalación, mucho más estricto según el
marco ICH Q3D (ver `202`). Y la pregunta que casi nadie hace: **¿este COA es del extracto o de la flor?**
El extracto concentra metales.

## Solventes residuales

```
SOLVENTES RESIDUALES — GC-MS headspace
n-Butano        380 ppm    LOQ 50    Límite 2.000   Pasa
Isobutano        55 ppm    LOQ 50    Límite 2.000   Pasa
Etanol           ND        LOQ 100   Límite 5.000   Pasa
Benceno          ND        LOQ 0,5   Límite 2        Pasa
```

Banderas rojas: que **no esté listado el solvente que tú sabes que se usó** (un BHO sin butano en el panel es
un COA que no aplica), inyección líquida en vez de headspace, o límites tomados de USP <467> cuando el
mercado tiene su propia tabla más estricta (ver `201`).

## Microbiología, micotoxinas, humedad y actividad de agua

```
MICROBIOLOGÍA
Recuento total aerobio         2,3 × 10³ UFC/g    Límite 10⁵     Pasa
Hongos y levaduras             1,1 × 10³ UFC/g    Límite 10⁴     Pasa
Aspergillus flavus/fumigatus/  No detectado       Ausencia/1 g   Pasa
  niger/terreus (qPCR)
Salmonella spp.                Ausencia/25 g                     Pasa
E. coli productora de toxina   Ausencia/1 g                      Pasa

MICOTOXINAS — LC-MS/MS
Aflatoxinas B1+B2+G1+G2        < 2,0 µg/kg (LOQ)  Límite 20      Pasa
Ocratoxina A                   < 1,0 µg/kg (LOQ)  Límite 20      Pasa

FÍSICOS
Humedad (Karl Fischer)         10,4 %
Actividad de agua              0,58 aW            Objetivo 0,55–0,65
```

Qué mirar: **si el método microbiológico fue cultivo o qPCR** (no son comparables), si el producto fue
descontaminado —porque qPCR detecta ADN de organismos muertos—, y si hay **actividad de agua**. Un COA sin aW
en flor es un COA incompleto: aW es el mejor predictor de si ese lote va a enmohecerse en la bodega
(ver `203`).

## Las diez banderas rojas propias del sector

1. **COA sin número de lote o sin fecha de análisis.** No es trazable, entonces no certifica nada.
2. **THC total que no cuadra con 0,877.** Rehaz la cuenta siempre. Un total inflado o desinflado delata.
3. **Potencia por GC en flor.** No puede reportar THCA por separado.
4. **"ND" sin LOQ.** El resultado real es el LOQ, y muchas veces el LOQ es más alto que el límite legal.
5. **Base no declarada.** Sin humedad y sin base, el número no se compara con nada.
6. **Panel de pesticidas más corto que el exigido** por el mercado de destino.
7. **Cannabinoides totales imposibles** para la matriz (más de ~30–35 % en flor seca es señal de alerta).
8. **Terpenos altos en un destilado**, sin declarar la reintroducción.
9. **COA "de la marca" y no del lote.** El COA que amparaba un lote de hace ocho meses no ampara el tuyo.
10. **Lab shopping.** Si el proveedor solo te muestra el COA con el número más alto, pídele todos los
    análisis del lote. A agosto de 2026 esta práctica está bajo escrutinio regulatorio en mercados maduros
    de EE.UU. (ver `113`).

Una undécima, técnica y muy reveladora: **el COA no dice quién tomó la muestra**. Si la muestra la tomó el
propio proveedor y la llevó al laboratorio, el resultado describe lo que él quiso mandar, no el lote
(ver `66`, `109`).

## Ejemplo aplicado (ILUSTRATIVO)

Te ofrecen un lote de flor con este COA. Auditoría en cinco minutos:

| Campo del COA | Valor | Veredicto |
|---|---|---|
| Lote | "GLC-2026-07" | Correcto, trazable |
| Fecha de análisis | 14-mar-2026, lote cosechado en jul-2026 | **Imposible: el análisis es anterior a la cosecha** |
| THC total declarado | 24,8 % | THCA 18,42 + Δ9 0,61 → 0,61 + 16,15 = 16,77 %. **No cuadra**, está inflado |
| Base | no declarada | **Incomparable** |
| Pesticidas | panel de 22 analitos | Corto para la mayoría de mercados |
| aW | no reportada | Falta el predictor de estabilidad microbiológica |

Cifras **(ILUSTRATIVO)**. Con dos comprobaciones aritméticas y una lectura de fechas, este lote queda
descartado sin necesidad de pagar un análisis propio. Ese es el retorno de saber leer un COA: se paga solo la
primera vez que lo usas.

## Errores comunes

- **Mirar solo el número grande de THC** y no las diez páginas restantes.
- **No rehacer el cálculo de THC total.** Es aritmética de treinta segundos que detecta fraude.
- **Aceptar el COA del proveedor como control de calidad propio.** Es el punto de partida, no la conclusión:
  el control es tu análisis de verificación por lote (ver `283`).
- **No verificar la acreditación ni el alcance.** El logo no es la acreditación.
- **Comparar COA de matrices distintas.** Flor y extracto no se comparan directo.
- **Perder la trazabilidad de la muestra.** Sin cadena de custodia, el COA no defiende nada ante una
  autoridad (ver `109`).

## Conexión con otros módulos

→ `110-como-leer-un-coa.md` y `111-banderas-rojas-en-un-coa.md` — el marco general, fuera de cannabis.
→ `175-thc-total-y-el-factor-0877.md` — la cuenta que audita el COA.
→ `198`, `199`, `200`, `201`, `202`, `203` — el detalle de cada sección del certificado.
→ `112-como-impugnar-un-resultado.md` — qué hacer cuando el número no te cuadra.
→ `113-lab-shopping-e-inflacion-de-potencia.md` — el fraude estructural del sector; `109` para la custodia.
