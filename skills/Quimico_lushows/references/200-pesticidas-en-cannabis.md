# 200 — Pesticidas en cannabis (el ensayo que más lotes reprueba)

El cannabis concentra. Un pesticida presente en la flor a nivel de trazas puede multiplicarse por 5 o por 10
en el extracto, porque el proceso de extracción no distingue entre un cannabinoide y un plaguicida
liposoluble. A eso se suma que la flor y los extractos suelen **inhalarse**, y las tolerancias agrícolas
tradicionales fueron pensadas para alimentos que se comen, no para humo que llega directo al pulmón. El
resultado es el ensayo más severo del panel: en mercados regulados, los pesticidas son una de las principales
causas de lote rechazado.

Términos: **LMR / MRL (maximum residue limit)** = límite máximo de residuo permitido. **Multiresiduo
(multiresidue)** = método que busca decenas o centenares de plaguicidas a la vez. **QuEChERS** = quick, easy,
cheap, effective, rugged, safe; la preparación de muestra estándar del análisis de residuos. **Efecto matriz
(matrix effect)** = supresión o aumento de señal causado por lo que acompaña al analito.

## Por qué los límites de cannabis no se parecen a los de alimentos

| Factor | Alimento típico | Cannabis inhalado |
|---|---|---|
| Vía de exposición | Oral, con primer paso hepático | Pulmonar, directo a circulación |
| Transformación del residuo | Cocción moderada | **Pirólisis**: crea productos nuevos |
| Factor de concentración | Bajo | Alto en extractos (5–10× o más) |
| Marco de límites | LMR agrícolas establecidos (Codex, EPA, UE) | Listas específicas por jurisdicción, muchas veces "cero tolerancia" a nivel de LOQ |

El caso emblemático es el **miclobutanil**: fungicida de uso agrícola permitido en varios cultivos, que al
pirolizarse puede liberar cianuro de hidrógeno `[química de combustión]`. Por eso figura en listas de
prohibición total en varios mercados de cannabis. Un pesticida "legal en tomate" no es legal en flor de
cannabis para inhalar.

**A agosto de 2026 no existe una lista internacional armonizada de pesticidas para cannabis.** Cada
jurisdicción define la suya: en EE.UU. cada estado tiene su propia lista y límites (California y Colorado
entre las más citadas); en Canadá, Health Canada mantiene una lista obligatoria de plaguicidas con límites a
nivel de LOQ; en la UE aplican los LMR del Reglamento (CE) 396/2005 al cáñamo como cultivo agrícola. Antes de
fijar tu especificación, **verifica la lista vigente del mercado de destino** en la autoridad correspondiente,
no en un blog.

## El método: LC-MS/MS y GC-MS/MS, casi siempre los dos

Ningún método único cubre todos los plaguicidas. La partición es química:

| Familia de plaguicida | Técnica adecuada | Por qué |
|---|---|---|
| Polares, termolábiles (carbamatos, neonicotinoides, triazoles) | LC-MS/MS | No sobreviven al inyector caliente |
| Apolares, volátiles (organoclorados, piretroides, PCNB) | GC-MS/MS | No ionizan bien por electrospray |
| Casos especiales (glifosato, ditiocarbamatos, etefón) | Métodos dedicados | Requieren derivatización o cromatografía específica |

Un laboratorio que te ofrece un panel de 60+ pesticidas **con un solo instrumento** está dejando familias
enteras fuera. Pregúntale explícitamente qué analitos van por LC y cuáles por GC, y cuáles **no cubre**.

### Preparación de muestra: QuEChERS y sus límites en cannabis

QuEChERS funciona: extracción con acetonitrilo, partición con sales (MgSO4 + NaCl o buffer citrato) y
limpieza dispersiva (**dSPE**) con PSA, C18 y a veces GCB. El problema en cannabis es que la matriz está
llena de **cannabinoides, clorofila, ceras y terpenos**, que ensucian la fuente y causan supresión iónica.

Consecuencias prácticas que debes exigir en el informe:
- **Calibración en matriz (matrix-matched calibration)**, no en solvente puro.
- **Estándares internos marcados isotópicamente** para los analitos críticos.
- **Recuperación demostrada en la matriz real** (flor, extracto, comestible son matrices distintas y hay que
  validar cada una) — ver `74`.

## Cómo se mide / cómo se comprueba (qué exigirle al laboratorio)

1. **Lista completa de analitos** con su LOD y LOQ individual en **µg/kg (ppb)** o mg/kg (ppm), en la matriz
   que le mandas.
2. **Comparación explícita contra el límite de tu mercado de destino**, no contra un límite genérico.
3. **Matriz validada**: no aceptes un COA de extracto respaldado por una validación hecha en flor.
4. **Recuperación (% recovery)** y precisión, típicamente aceptables entre 70 % y 120 % con %RSD ≤ 20 %,
   siguiendo el marco de guías de residuos como SANTE (guía europea de validación de métodos de residuos);
   confirma la versión vigente del documento SANTE al citarlo.
5. **Blancos y controles de calidad** del lote analítico.
6. **Acreditación ISO/IEC 17025 con pesticidas en cannabis dentro del alcance** (ver `107`).

## Ejemplo aplicado (ILUSTRATIVO)

Flor con un residuo de bifenazato a 0,08 mg/kg. Se extrae con etanol y se destila; el rendimiento de extracto
es 12 % en masa (100 g de flor → 12 g de extracto), y se asume que el residuo pasa completo al extracto
(supuesto conservador).

```
Masa de residuo en 100 g de flor = 0,08 mg/kg × 0,100 kg = 0,008 mg
Concentración en 12 g de extracto = 0,008 mg / 0,012 kg = 0,67 mg/kg
Factor de concentración = 0,67 / 0,08 = 8,3×
```

Cifras **(ILUSTRATIVO)**. Un residuo que estaba 8 veces por debajo de un límite hipotético de 0,1 mg/kg en
flor termina 6,7 veces por encima de ese mismo límite en el extracto. Por eso **flor conforme no implica
extracto conforme**, y por eso hay que analizar ambos. La cuenta hay que ejecutarla: `Matematicas_lushows`.

## Estrategia de control (más barata que analizar todo, siempre)

- **Controla la entrada, no la salida.** Especificación de materia prima con lista de plaguicidas prohibidos
  firmada por el cultivador, y auditoría (ver `141`, `284`).
- **Analiza flor antes de comprar el lote**, no después de extraer. Extraer material contaminado es
  multiplicar un problema y perder el costo del proceso.
- **Muestreo compuesto correcto**: la contaminación por plaguicidas es heterogénea; el muestreo manda (ver
  `66`).
- **Rastrea el origen del residuo**: muchas veces no viene del cultivo propio sino de deriva del vecino, del
  sustrato o del agua (ver `106`).
- **Guarda contramuestra** para poder impugnar un resultado (ver `112`).

## Errores comunes

- **Usar los LMR de alimentos como referencia** para producto inhalado. Es la confusión conceptual de fondo.
- **Aceptar un panel corto.** Si el laboratorio busca 25 plaguicidas y el mercado exige 66, tienes 41 huecos.
- **No mirar el LOQ frente al límite.** Si el límite es 0,01 mg/kg y el LOQ del laboratorio es 0,05 mg/kg,
  el "cumple" no significa nada.
- **Analizar solo el producto terminado** y descubrir el problema cuando ya invertiste en procesarlo.
- **Calibrar en solvente en vez de en matriz** y subestimar por supresión iónica.
- **Confiar en el COA del proveedor sin verificar la fecha, el lote y el laboratorio.** Un COA sin lote es
  publicidad (ver `111`).

## Conexión con otros módulos

→ `102-pesticidas-multiresiduo.md` — el método general, fuera del contexto de cannabis.
→ `69-extraccion-para-analisis-spe-y-quechers.md` — la preparación de muestra por dentro.
→ `83-lc-ms-ms-y-mrm.md` — cómo se cuantifica a nivel de ppb.
→ `197-vapeo-quimica-y-riesgos.md` — por qué la pirólisis cambia el riesgo del residuo.
→ `141-especificacion-de-materia-prima.md` — el control que de verdad ahorra plata.
→ `213-como-leer-un-coa-de-cannabis.md` — cómo se lee la sección de pesticidas.