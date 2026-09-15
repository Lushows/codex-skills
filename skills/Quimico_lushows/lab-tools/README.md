# lab-tools — las calculadoras del químico

Diez scripts de Python que hacen las cuentas que **no se pueden hacer de memoria**: las que sostienen
un límite regulatorio, una dosis de etiqueta o una decisión de formulación.

La regla de la skill es que **todo cálculo que importe se ejecuta y se verifica por segunda vía**.
Estas herramientas son esa segunda vía.

---

## Cómo se corren

```bash
cd lab-tools
python decarboxilacion.py factor
python thc_total.py evaluar --thca 0.28 --thc 0.05 --unidad pct --base seca --envase-g 3.5
```

Si `python` no existe en tu PC (Windows), usa `py -3`:

```bash
py -3 thc_total.py --help
```

**Requisitos: ninguno.** Python 3 y solo librería estándar (`decimal`, `argparse`, `statistics`).
No hay que instalar numpy, scipy ni pandas. Corre en el PC de Lushows tal como está.

Cada script tiene:

- `--help` — ayuda completa en español, con todas las banderas.
- `--test` — autotests con valores conocidos, verificados por segunda vía (operación inversa, balance
  de masa, identidad matemática o contraste contra `statistics`). Imprime `OK - N pruebas pasaron`
  o falla con el detalle y **sale con código distinto de cero**.
- Un docstring de cabecera que dice **qué calcula, la fórmula, de dónde sale y qué NO hace**.
- Validación de entradas: rechaza negativos imposibles, porcentajes mayores a 100, humedades de 100 %,
  masas cero y demás disparates, con mensaje claro y salida con código 2.

Todas las salidas imprimen **siempre la unidad y la base** (seca o húmeda). Varios scripts te
**obligan** a declarar la base con `--base`, porque un porcentaje sin base no se puede comparar con nada.

---

## Las 10 herramientas

| Herramienta | Qué hace | Ejemplo de comando | Qué imprime |
|---|---|---|---|
| **`decarboxilacion.py`** | THCA → Δ9-THC. Deriva el factor 0,877 desde las masas molares (C21H30O2 / C22H30O4), cierra el balance de masa con el CO₂ que se pierde, y modela la conversión por tiempo y temperatura (primer orden, Arrhenius). | `python decarboxilacion.py cinetica --thca 20 --temp 110 --min 40 --base seca` | Masas molares y factor exacto; k(T) y vida media; THCA remanente, Δ9-THC generado y CO₂ perdido; el % de THC **referido a la masa inicial y a la masa final** (que son distintos). |
| **`thc_total.py`** | THC total = Δ9-THC + (THCA × 0,877). Evalúa los **dos** límites, que son cosas distintas: 0,3 % p/p base seca (concentración) y 0,4 mg por envase (producto terminado). Modo inverso incluido. | `python thc_total.py evaluar --thca 0.28 --thc 0.05 --unidad pct --base seca --humedad 8 --envase-g 3.5` | THC total en ambas bases; veredicto CUMPLE / NO CUMPLE por cada límite; margen al límite y aviso si estás dentro de la incertidumbre del método; concentración máxima permitida para ese envase. |
| **`diluciones.py`** | C1V1 = C2V2 resolviendo la incógnita que falte, series de dilución seriadas, y regresión lineal de curva de calibración. | `python diluciones.py curva --conc 0.5,1,2,5,10 --area 1230,2510,4980,12600,24900 --area-muestra 8000 --factor-dilucion 20` | Volumen de stock y de diluyente a pipetear; tabla de la serie con FD acumulado; ecuación de la recta, pendiente, intercepto, R², s(y/x) residual, y la concentración de la muestra con su factor de dilución aplicado. |
| **`rendimiento_extraccion.py`** | Rendimiento % p/p, ratio planta:extracto **real vs declarado**, factor de concentración del marcador y recuperación del activo. La herramienta para auditar un "10:1". | `python rendimiento_extraccion.py --biomasa-g 1000 --extracto-g 100 --humedad-biomasa 10 --humedad-extracto 5 --activo-biomasa 1.2 --activo-extracto 9 --ratio-declarado 10` | Rendimiento y ratio real en base seca; comparación contra el ratio declarado con bandera roja si está inflado; g de activo en planta, en extracto y perdidos en el bagazo; recuperación % con alarma si supera 100 % (imposible). |
| **`betaglucano_dosis.py`** | Del % de β-glucano del COA (base seca) a mg por cápsula y por porción diaria; el inverso (cuánto extracto para X mg/día); y el aporte real de una mezcla de extractos. | `python betaglucano_dosis.py directo --bg-pct 30 --base seca --mg-capsula 500 --capsulas-dia 2 --humedad 6` | mg de β-glucano por cápsula y por día, corregidos por humedad; en modo inverso, mg de extracto/día y cápsulas enteras (redondeo hacia arriba) con el exceso resultante; recordatorio de que "polisacáridos" ≠ β-glucano. |
| **`base_seca.py`** | Base húmeda ↔ base seca por humedad, reajuste a otra humedad, y comparación de dos COA con humedades distintas. | `python base_seca.py comparar --valor-a 29 --humedad-a 4 --valor-b 29.5 --humedad-b 11` | Ambos COA llevados a base seca, la diferencia absoluta y relativa, y un aviso explícito cuando **el orden se invierte** al corregir por humedad (la trampa más común al comparar proveedores). |
| **`vida_util_arrhenius.py`** | Vida útil desde estudio acelerado por Arrhenius y por regla Q10; Ea desde dos estudios; de un % de pérdida observado a k y a la fecha de vencimiento; traducción Q10 ↔ Ea. | `python vida_util_arrhenius.py q10 --tiempo-acelerado 6 --temp-acelerada 40 --temp-real 25 --q10 2` | Factor de extrapolación y vida útil estimada en la unidad que declares; el Ea (o Q10) equivalente para que juzgues si tu supuesto es creíble; y el bloque de **supuestos que estás aceptando** y cuándo la extrapolación miente. |
| **`unidades.py`** | % p/p ↔ mg/g ↔ ppm ↔ µg/g ↔ g/kg ↔ mg por porción, **exigiendo** que declares la base. | `python unidades.py --valor 0.3 --unidad pct --base seca --humedad 8 --porcion-g 2 --analito THC` | La tabla completa de equivalencias en la base declarada, los mg por porción, y el mismo valor en la otra base si das `--humedad`. Solo masa/masa: no asume ppm = mg/L. |
| **`loq_lod.py`** | LOD/LOQ por relación señal-ruido (3:1 y 10:1) y por σ/pendiente (3,3σ/S y 10σ/S, criterio ICH Q2(R2)). También calcula σ y la pendiente desde los puntos de la curva. | `python loq_lod.py curva --conc 1,2,3,4,5 --area 102,198,305,399,501 --base seca --sigma intercepto` | LOD y LOQ con unidad y base; s(y/x) residual y s(intercepto); alarma si el LOQ calculado está por encima de tu patrón más bajo; y el recordatorio de que el LOQ debe **confirmarse** con muestras fortificadas. |
| **`potencia_formula.py`** | Cuánto extracto poner por unidad para entregar X mg de activo **al final de la vida útil**, con sobredosificación por pérdida en proceso y por degradación. Verificación inversa de una fórmula existente. | `python potencia_formula.py formular --objetivo-mg 100 --activo-pct 25 --base seca --humedad 6 --perdida-proceso 5 --degradacion 10` | mg de extracto teórico vs a dosificar, overage total en %, activo al tiempo 0 y al vencimiento; en modo `verificar`, CUMPLE / NO CUMPLE contra la etiqueta y cuántos mg faltan; y de dónde tienen que salir tus supuestos. |

---

## Aviso sobre los límites regulatorios

> **Todos los valores regulatorios que traen estos scripts por defecto están fechados a AGOSTO DE 2026
> y deben verificarse antes de tomar cualquier decisión comercial.**

En particular:

- **0,3 % p/p de THC total en base seca** (`thc_total.py`) es la definición federal de *hemp* en
  EE.UU. (Agricultural Improvement Act de 2018 y regla final de la USDA), que además define THC total
  exactamente como Δ9-THC + 0,877 × THCA. **Colombia y la Unión Europea tienen sus propios umbrales y
  su propia definición.** No asumas que el 0,3 % aplica en tu país.
- **0,4 mg de THC total por envase** (`thc_total.py`) es el umbral por contenedor de la normativa
  federal estadounidense para productos de hemp de consumo. Este límite y su fecha de entrada en vigor
  han cambiado varias veces.
- Ambos son configurables (`--limite-pct`, `--limite-mg-envase`) **precisamente porque cambian**.
- El THC total de estos scripts cubre **solo Δ9-THC y THCA**. Varias normas cuentan también Δ8-THC,
  THCP, HHC y otros análogos. Revisa la definición aplicable a tu producto y a tu destino.
- Los criterios de `loq_lod.py` (3,3σ/S y 10σ/S) vienen de **ICH Q2(R2)**; los de
  `vida_util_arrhenius.py` de **ICH Q1A(R2) / Q1E**; el overage justificado de `potencia_formula.py`
  de **ICH Q8**. Son guías internacionales que también se actualizan.

**Nada de esto es asesoría legal.** El número que sale de un script es un insumo para hablar con tu
laboratorio, tu abogado regulatorio y la autoridad sanitaria del país de destino.

---

## Lo que estas herramientas NO hacen

Cada script lo dice en su propio docstring, pero vale repetir lo transversal:

- **No miden nada.** Consumen datos de balanza y de COA. Si el dato de entrada es basura, la salida es
  basura con más decimales.
- **No validan el método analítico.** Un β-glucano medido como "polisacáridos totales" no se arregla
  con aritmética. Un THC total sobre un COA sin límite de cuantificación no sostiene cumplimiento.
- **No calculan incertidumbre de medida.** Un resultado de 0,29 % con incertidumbre expandida de
  ±0,03 % **no** está limpiamente por debajo de 0,3 %. Pídele la incertidumbre al laboratorio.
- **No hacen ningún claim de salud.** Un miligramo no es un beneficio.

---

## Índice rápido por pregunta

| Si tu pregunta es… | Usa |
|---|---|
| "¿Cuánto THC me da esta flor si la descarboxilo?" | `decarboxilacion.py` |
| "¿Este producto es legal por THC?" | `thc_total.py` |
| "¿Cómo preparo el patrón / cuánto dio la muestra?" | `diluciones.py` |
| "¿Este extracto 10:1 es de verdad 10:1?" | `rendimiento_extraccion.py` |
| "¿Cuántos mg de β-glucano entrega mi cápsula?" | `betaglucano_dosis.py` |
| "Estos dos COA no se parecen, ¿cuál es mejor?" | `base_seca.py` |
| "¿Qué fecha de vencimiento le pongo?" | `vida_util_arrhenius.py` |
| "¿Cuánto es 0,3 % en ppm / en mg por porción?" | `unidades.py` |
| "¿Hasta dónde puede medir este método?" | `loq_lod.py` |
| "¿Cuánto extracto pongo para cumplir la etiqueta?" | `potencia_formula.py` |

Para cualquier cálculo que no esté aquí y sostenga una decisión, la skill rutea a
`Matematicas_lushows`. Aritmética mental: prohibida.
