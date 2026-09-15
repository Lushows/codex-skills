# 114 — Costos y tiempos de análisis (qué es imprescindible y qué puede esperar)

Este es el módulo técnico de la plata: cuánto cuesta y cuánto tarda cada ensayo **por técnica analítica**, por
qué unos cuestan diez veces más que otros, y —la parte que de verdad decide— cuáles son imprescindibles y
cuáles pueden esperar cuando el presupuesto es de pyme. El presupuesto anual completo, con el ejemplo de
costo por unidad vendida, vive en `291`; aquí está el detalle por ensayo y la lógica de priorización. La regla
de fondo: **el precio de un ensayo no se compara sin comparar el método**, porque dos ensayos con el mismo
nombre pueden medir cosas distintas.

Términos: **TAT (turnaround time)** = días desde que el laboratorio recibe la muestra hasta que emite el
informe. **rush fee** = recargo por urgencia. **panel (suite)** = varios ensayos con precio agrupado.
**costo marginal por analito** = lo que cuesta añadir un analito más a una corrida ya montada.
**skip-lot** = analizar 1 de cada N lotes con justificación de riesgo documentada.

## Por qué un ensayo cuesta lo que cuesta

El precio casi nunca es el reactivo. Es la suma de cuatro cosas:

| Componente | Peso típico | Qué lo dispara |
|---|---|---|
| Preparación de muestra | Alto en sólidos | Digestión por microondas, extracción, molienda, derivatización |
| Tiempo de instrumento | Alto en cromatografía | Corridas de 20–40 min por inyección, más blancos y controles |
| Patrones de referencia | Muy alto en multiresiduo | Un panel de 200 pesticidas necesita 200 patrones certificados (`70`) |
| Personal y control de calidad | Constante | Cada corrida lleva blancos, spikes, duplicados y CRM (`77`) |

De ahí la jerarquía que no cambia entre países: **físicos y microbiología son baratos; cromatografía es media;
espectrometría de masas y validación de método son lo caro.** Y el corolario que ahorra plata: añadir un
analito a una corrida ya montada cuesta poco; pedir una técnica nueva cuesta mucho.

## Órdenes de magnitud por técnica (referencia, hay que cotizar)

El único ancla pública con fecha que usamos en esta skill es la lista de precios de **CIA Labs, vigente desde
el 2 de febrero de 2025 (USD)**: *assay* por HPLC o GC de un activo en **USD 290–425**, metales por ICP-OES en
**USD 500–625**, titulación en **USD 235–325**, solventes residuales USP <467> en **USD 1.200–5.000**, y un
recargo del **50 %** por entrega en 5 días. Todo lo demás de esta tabla es **(ILUSTRATIVO)** y debe cotizarse.
Las columnas en COP son conversiones aproximadas, también **(ILUSTRATIVAS)**.

| Ensayo | Técnica | USD por muestra | COP aprox. | TAT hábiles | Marginal por analito extra |
|---|---|---|---|---|---|
| Humedad | Gravimetría / Karl Fischer (`98`) | 20–60 | 80.000–240.000 | 2–5 | — |
| Actividad de agua | Higrómetro (`35`) | 20–50 | 80.000–200.000 | 2–5 | — |
| Cenizas, pH, densidad | Clásicos | 15–50 | 60.000–200.000 | 2–5 | Bajo |
| Microbiología básica | Recuento en placa (`100`) | 40–90 | 160.000–360.000 | 5–7 | Bajo |
| Patógenos (Salmonella, E. coli) | Cultivo / PCR | 60–150 | 240.000–600.000 | 5–10 | Medio |
| Activo por HPLC-UV (1 analito) | HPLC (`79`) | 290–425 | 1,2–1,7 M | 5–15 | Bajo si comparte método |
| β/α-glucano enzimático | Megazyme K-YBGL (`91`) | 120–250 | 480.000–1,0 M | 7–15 | — (son dos ramas fijas) |
| Potencia de cannabinoides | HPLC-DAD (`198`) | 60–200 | 240.000–800.000 | 3–7 | Muy bajo (mismo método) |
| Perfil de terpenos | GC-MS (`199`) | 100–250 | 400.000–1,0 M | 5–10 | Muy bajo |
| Metales pesados (4 elementos) | ICP-MS / ICP-OES (`88`) | 500–625 | 2,0–2,5 M | 7–15 | Muy bajo (multielemental) |
| Micotoxinas (aflatoxinas + OTA) | LC-MS/MS (`101`) | 150–350 | 600.000–1,4 M | 7–15 | Bajo |
| Pesticidas multiresiduo | LC-MS/MS + GC-MS/MS (`102`) | 250–600 | 1,0–2,4 M | 10–20 | Bajo dentro del panel |
| Solventes residuales | GC-headspace USP <467> (`87`) | 1.200–5.000 | 4,8–20 M | 7–15 | Muy bajo |
| Identidad por ADN/ITS | Secuenciación (`103`, `245`) | 100–300 | 400.000–1,2 M | 10–20 | — |
| Estabilidad completa | Cámaras + ensayos por punto (`164`) | 3.000–12.000 por producto | — | 6–24 meses | Por punto de tiempo |
| Desarrollo + validación de método | ICH Q2(R2) (`75`) | 5.000–20.000 | — | 2–6 meses | Se paga una vez |

**Colombia vs exterior.** Con cotización directa —a agosto de 2026 no encontramos listas públicas de precios
de laboratorios colombianos de alimentos— la experiencia del sector es que un laboratorio universitario
colombiano acreditado por ONAC suele quedar por debajo de la referencia estadounidense en rutina
(microbiología, fisicoquímicos, metales), mientras que los métodos de nicho —K-YBGL, terpenos, panel amplio de
pesticidas, ITS— o no existen localmente o cuestan parecido, porque los patrones y los kits se importan en
dólares. A eso hay que sumarle, cuando se manda afuera, **flete internacional, permisos de material vegetal y
1 a 3 semanas extra** de logística (`285`). Todos estos órdenes de magnitud son **(ILUSTRATIVOS)** y hay que
pedir cotización: varían por país, volumen, matriz y acreditación.

## Qué es imprescindible y qué puede esperar (presupuesto de pyme)

Esta es la tabla que hay que tener pegada al escritorio. La prioridad no se decide por gusto: se decide por
**qué daño evita** el ensayo y **qué claim sostiene**.

| Prioridad | Ensayo | Por qué | Frecuencia mínima |
|---|---|---|---|
| **1. Imprescindible** | Identidad de especie (ITS) | Si no sabes qué es, nada más importa | 1 vez por proveedor y por cambio de origen |
| **1. Imprescindible** | Humedad y actividad de agua | Base de todo cálculo y predictor de estabilidad | Cada lote (se hace en casa) |
| **1. Imprescindible** | Microbiología básica + patógenos | Riesgo de daño directo al consumidor | Cada lote de producto terminado |
| **1. Imprescindible** | El activo que sostiene tu claim (β-glucano por K-YBGL) | Sin él la etiqueta es publicidad (`268`) | Cada lote de producto terminado |
| **2. Alta** | Metales pesados | Riesgo real en hongos y en cannabis, acumulativo (`243`) | 1 de cada 3 lotes, o por cambio de origen |
| **2. Alta** | Micotoxinas | Riesgo por sustrato y almacenamiento (`244`) | 1 de cada 3 lotes |
| **3. Media** | Solventes residuales | Solo si hay extracción con solvente (`87`) | Cada lote de extracto; nunca en polvo simple |
| **3. Media** | Estabilidad acelerada | Define la vida útil que ya imprimiste (`165`) | 1 producto por año |
| **4. Puede esperar** | Pesticidas multiresiduo | Alto costo; prioriza si el origen es de campo abierto | Anual o por cambio de proveedor |
| **4. Puede esperar** | Perfil de triterpenos, ergotioneína | Diferenciación, no seguridad (`224`, `235`) | Cuando el claim lo exija |
| **4. Puede esperar** | Metabolómica / huella química | Investigación y disputas (`104`) | Solo por proyecto |
| **4. Puede esperar** | Validación de método propia | Solo si vas a analizar en casa (`75`) | Cuando montes laboratorio |

Y la regla que ordena todo lo anterior: **lo que va en la etiqueta se mide en cada lote; lo que evita daño se
mide por riesgo; lo que diferencia se mide cuando haya plata.** Lo que decidas **no** medir se escribe con su
justificación de riesgo — un plan con esa sección es defendible; sin ella parece un olvido (`283`).

## Ejemplo aplicado (ILUSTRATIVO)

Presupuesto de un lote de cápsulas de reishi, 3.000 unidades, plan de `283`:

```
LOTE 4 de 6 del ano (le toca metales por skip-lot 1 de 3)
  Humedad + aW (en casa, costo marginal)                      USD    0
  Identidad ITS (ya hecha para este proveedor este ano)       USD    0
  beta/alfa-glucano en producto terminado (K-YBGL)            USD  180
  Microbiologia completa (recuentos + patogenos)              USD  120
  Metales pesados por ICP-MS (4 elementos)                    USD  550
                                                      total = USD  850
  Costo por unidad: 850 / 3.000 = USD 0,283 por capsula-lote
  TAT critico: metales 15 dias habiles -> planear el muestreo 3 semanas antes del despacho

LOTE 5 (sin metales)
                                                      total = USD  300
  Costo por unidad: 300 / 3.000 = USD 0,100
```

Cifras **(ILUSTRATIVO)**. Las dos lecciones de negocio están en la segunda línea de cada bloque: **el TAT es
tan importante como el precio** —un ensayo de 15 días decide cuándo hay que muestrear, no cuándo hay que
pagar— y el costo por unidad varía cuatro veces entre un lote y otro, así que se promedia al año, no se carga
al lote. Toda la aritmética se ejecuta con `Matematicas_lushows` y el costeo se lleva a `contador_lushows`.

## Cinco formas de bajar el costo sin bajar el rigor

1. **Agrupar analitos en la misma técnica.** Cuatro metales por ICP-MS cuestan casi lo mismo que uno.
2. **Comprometer volumen anual con un laboratorio** a cambio de precio de panel (`292`).
3. **Hacer en casa lo barato y robusto**: humedad, aW, peso, aspecto. La balanza halógena y el higrómetro se
   pagan en meses.
4. **Planear el cronograma para no pagar rush.** El recargo por urgencia puede ser del 50 % (lista CIA Labs,
   2 de febrero de 2025).
5. **Skip-lot documentado con datos históricos**, no con ganas (`283`).

Lo que **no** es una forma de bajar el costo: cambiar a un método más barato que mide otra cosa (`91`, `222`),
ni escoger el laboratorio por el número que reporta (`113`).

## Errores comunes

- **Comparar precios sin comparar métodos.** Un β-glucano por colorimetría es más barato porque no mide lo
  mismo.
- **Presupuestar solo el precio y no el TAT.** El lote parado en cuarentena cuesta más que el ensayo.
- **Pagar rush todos los meses** por no planear el muestreo con tres semanas.
- **Analizar todo en cada lote** al principio y quedarse sin presupuesto para la estabilidad del año 2 (`291`).
- **Olvidar el producto que se destruye en el muestreo**: cada muestra son unidades que no vendes (`109`).
- **No presupuestar reanálisis.** Siempre hay uno; el 15 % de contingencia no es opcional.
- **Pedir "un análisis completo"** sin decir qué decisión se toma: te venden el panel más caro y falta lo que
  necesitabas (`00`, `65`).

## Conexión con otros módulos

→ `291-costos-de-analisis-y-presupuesto.md` — el presupuesto anual y el costo por unidad vendida.
→ `283-plan-de-control-de-calidad-por-lote.md` — el plan que genera esta lista de ensayos.
→ `108-como-elegir-un-laboratorio.md` — a quién le pides la cotización y cómo la comparas.
→ `292-negociar-con-laboratorios-y-maquiladores.md` — cómo se negocia el panel anual.
→ `113-lab-shopping-e-inflacion-de-potencia.md` — el ahorro que no se debe tomar.
→ `164-estabilidad-ich-q1-y-vida-util.md` — la partida más subestimada del presupuesto.
