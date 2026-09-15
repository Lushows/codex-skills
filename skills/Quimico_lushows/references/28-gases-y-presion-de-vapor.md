# 28 — Gases y presión de vapor (por qué al vacío todo hierve más frío)

Este módulo es el que explica el vacío. Sin él, "destilación molecular a 0,001 mbar" suena a marketing; con
él entiendes que bajar la presión baja el punto de ebullición y que eso es lo único que permite destilar un
cannabinoide sin cocinarlo. También explica por qué un rotavapor a 40 °C saca etanol igual de bien que un
tanque a 78 °C, por qué la sublimación del hielo en un liofilizador funciona, y por qué el análisis de
solventes residuales se hace por espacio de cabeza. Es física aplicada a tu factura de gas y a tu potencia.

Términos: **presión de vapor (vapor pressure)** = presión que ejerce el vapor de una sustancia en
equilibrio con su líquido, a una temperatura dada; en mbar, kPa o mmHg. **punto de ebullición (boiling
point)** = temperatura a la cual la presión de vapor iguala la presión externa. **volatilidad
(volatility)** = qué tan fácil pasa a vapor; alta presión de vapor = volátil. **vacío (vacuum)** = presión
por debajo de la atmosférica; 1 atm = 1 013 mbar = 760 mmHg. **espacio de cabeza (headspace)** = el gas que
queda encima del líquido o sólido en un vial cerrado.

## Las ecuaciones de trabajo

```
Gas ideal:            P·V = n·R·T          R = 8,314 J/(mol·K) = 0,08206 L·atm/(mol·K)

Clausius-Clapeyron:   ln(P2/P1) = −(ΔHvap/R) · (1/T2 − 1/T1)     T en kelvin
                      → con dos pares (P,T) predices el punto de ebullición a cualquier presión

Raoult (mezcla ideal): P_i = x_i · P°_i     x_i = fracción molar en el líquido
Dalton:                P_total = Σ P_i      → base de la destilación (`29`)

Henry:                 C_liq = k_H · P_gas  → base del headspace y de la carbonatación
```

Regla de bolsillo, útil y aproximada: **bajar la presión a la décima parte baja el punto de ebullición
entre 30 y 50 °C** para líquidos orgánicos comunes. Por eso un rotavapor a 100 mbar saca etanol a ~35 °C.

## La tabla que decide tu equipo

| Sustancia | P vapor a 25 °C (aprox.) | Ebullición a 1 atm | Ebullición a 10 mbar (aprox.) | Dónde importa |
|---|---|---|---|---|
| Agua | 32 mbar | 100 °C | ~7 °C | Concentración, liofilización (`150`) |
| Etanol | 79 mbar | 78,4 °C | ~ −12 °C | Recuperación de solvente (`149`) |
| Metanol | 169 mbar | 64,7 °C | ~ −20 °C | Solo analítico (`87`) |
| n-Hexano | 200 mbar | 68,7 °C | ~ −20 °C | Extracción con hidrocarburos (`188`) |
| Butano | ~2 400 mbar (gas) | −0,5 °C | gas | BHO; riesgo de explosividad (`08`, `188`) |
| α-Pineno | ~0,6 mbar | 156 °C | ~40 °C | Terpenos que se pierden al secar (`182`) |
| Mirceno | ~0,3 mbar | 167 °C | ~48 °C | Se va primero en cualquier evaporación |
| Δ9-THC | del orden de 10⁻⁷ mbar | ~157 °C **a 0,05 mmHg** | — | Destilación molecular (`192`) |
| CBD | del orden de 10⁻⁷ mbar | ~180 °C a 0,1 mmHg | — | Igual |

Nota importante y muy citada mal: el "punto de ebullición del THC = 157 °C" que circula en foros es a
**vacío alto**, no a presión atmosférica. A 1 atm el THC se degrada antes de hervir. Repetir ese dato sin
la presión es el error de dato más común del sector (`02`).

## Por qué los terpenos se van y los cannabinoides se quedan

Compara las presiones de vapor de la tabla: los monoterpenos tienen presiones de vapor **seis o siete
órdenes de magnitud** mayores que los cannabinoides. Consecuencia directa: cualquier operación con calor,
vacío o corriente de aire —secado, curado, evaporación, purga— se lleva terpenos y deja cannabinoides. Por
eso un extracto destilado es potente y **no huele a nada**, y por eso los terpenos se reintroducen después
si se quieren (`182`, `192`). No es un defecto del proceso: es presión de vapor.

Lo mismo aplica al secado de hongos: los volátiles aromáticos (1-octen-3-ol, el olor "a hongo") se van con
el aire caliente. El β-glucano no se va —es un polímero, presión de vapor cero— pero el producto huele
distinto y el cliente lo nota (`142`, `240`).

## Headspace: usar la presión de vapor para medir

Si pones una muestra en un vial sellado y la calientas, los compuestos volátiles se reparten entre el
líquido/sólido y el gas de arriba según la ley de Henry. Inyectas ese gas al cromatógrafo y mides lo
volátil **sin meter la matriz sucia a la columna**. Ese es el fundamento de:

- **Solventes residuales** en extractos (etanol, butano, hexano) — USP <467> y equivalentes (`87`, `201`).
- **Perfil de terpenos** por GC-MS headspace, cuando no se quiere diluir en solvente (`86`, `199`).
- Contaminantes de envase y off-flavors.

Regla dura del headspace: el resultado depende de la temperatura del vial, del tiempo de equilibrio y de
la matriz. Por eso se calibra con **la misma matriz** o con adición de estándar, no con solvente puro
(`72`).

## Cómo se mide

| Pregunta | Método | Unidad |
|---|---|---|
| ¿Cuál es la presión de vapor de mi compuesto? | Isoteniscopio, efusión de Knudsen, o TGA isotérmico | mbar o Pa a T declarada |
| ¿Cuál es el punto de ebullición a mi vacío? | Clausius-Clapeyron con ΔHvap, verificado en el equipo | °C a mbar declarados |
| ¿Cuánto solvente residual quedó? | GC-FID o GC-MS con headspace estático | ppm (mg/kg), contra límite USP <467> (`87`) |
| ¿Qué tan bien evacúa mi bomba? | Vacuómetro en la línea, no en la bomba | mbar absolutos, medidos en el punto de proceso |
| ¿Cuántos terpenos perdí en el secado? | GC-MS de la biomasa antes y después | mg/g b.s., por terpeno (`199`) |
| ¿Cuánto O₂ hay en el envase? | Analizador de headspace de O₂ | % v/v (`24`, `163`) |

Advertencia práctica: el vacuómetro barato del equipo mide la presión **en la bomba**, no en el balón. La
diferencia puede ser de un orden de magnitud y es la razón número uno de "mi destilación no sube".

## Ejemplo aplicado — recuperar etanol de una tintura sin cocinar el activo

Tintura hidroalcohólica de reishi, 50 L en EtOH 70 %, se quiere concentrar a 5 L **(ILUSTRATIVO)**:

```
Opción            Presión (mbar)   T de ebullición   T de baño   Tiempo   Triterpenos conservados
Atmosférica         1 013             ~80 °C           95 °C      6 h            88 %
Vacío moderado        175             ~50 °C           60 °C      4 h            96 %
Vacío alto             60             ~35 °C           45 °C      5 h            99 %

Energía latente para 35 kg de etanol: 35 kg × 841 kJ/kg ≈ 29 400 kJ ≈ 8,2 kWh teóricos (`25`)
```

Lectura: bajar de 1 013 a 175 mbar cuesta una bomba de vacío decente y devuelve 8 puntos de activo. Bajar
más aporta 3 puntos y alarga el ciclo porque la transferencia de calor empeora a baja presión. El punto
económico razonable está en el vacío moderado, y la decisión se toma con el dato de termolabilidad del
activo, no con la intuición. Con `Matematicas_lushows` se cierra el número de costo por lote.

## Errores comunes

- Citar puntos de ebullición de cannabinoides o terpenos sin decir la presión. El dato no significa nada.
- Medir el vacío en la bomba y no en el proceso.
- Creer que el vacío "no calienta" el producto. El vacío baja la T necesaria; si el baño sigue a 95 °C, el
  producto sigue a 95 °C.
- Purgar un extracto y suponer que quedó sin solvente. "Sin olor" no es "por debajo del límite"; se mide
  por headspace GC (`87`).
- Diseñar un secado sin pensar en los volátiles. Si el producto se vende por aroma, el aroma es un
  atributo crítico de calidad y se mide (`199`).
- Usar la ley del gas ideal para vapores cerca de la condensación. Ahí ya no es ideal.
- Sellar un vial de headspace con septum reutilizado. Fuga = subestimación sistemática.

## Conexión con otros módulos

→ `29-destilacion-y-equilibrio-liquido-vapor.md` — la aplicación directa de Raoult y Dalton.
→ `25-termodinamica-quimica.md` — de dónde sale ΔHvap y cuánto cuesta evaporar.
→ `87-solventes-residuales.md` — headspace GC como método oficial.
→ `86-gc-ms-y-headspace.md` — la técnica analítica completa.
→ `192-destilacion-de-cannabinoides.md` — destilación molecular al vacío, el caso central.
→ `149-concentracion-y-evaporacion.md` — el paso de planta.
→ `182-terpenos-del-cannabis.md` — quién se va primero y por qué.
