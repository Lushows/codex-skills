# 11 · Operaciones y orden (PEMDAS)

> **Qué resuelve / cuándo usarlo** — Cómo evaluar una expresión con varias operaciones (sumas, restas, multiplicaciones, potencias…) en el orden correcto para obtener UN solo resultado verdadero, sin ambigüedad. Úsalo siempre que una fórmula combine más de una operación: márgenes, precios con IVA, fórmulas financieras, todo.

## Concepto (para no-experto)

Cuando ves `2 + 3 × 4`, ¿da 20 o da 14? No puede dar las dos cosas: el dinero real exige UNA respuesta. Por eso las matemáticas tienen un **orden de operaciones**: un acuerdo universal sobre quién va primero. La respuesta correcta es **14** (primero `3 × 4 = 12`, luego `2 + 12`).

Pensalo como **cocinar una receta**: no metés la torta al horno antes de mezclar los ingredientes. Hay un orden obligatorio, y saltarlo arruina el plato. En matemáticas saltarlo arruina el número… y la decisión de plata que cuelga de él.

La regla se memoriza con la sigla **PEMDAS** (en inglés) o **PJMDAS** en español. Cada letra es un nivel de prioridad, de mayor a menor:

1. **P** — **Paréntesis** (y todo agrupador: corchetes `[]`, llaves `{}`, la línea de fracción, la raíz). Lo que está agrupado se resuelve primero, de adentro hacia afuera.
2. **E** — **Exponentes** (potencias y raíces). *Exponente* = el número pequeño arriba que indica cuántas veces se multiplica algo: `2³ = 2×2×2 = 8`.
3. **MD** — **Multiplicación y División**, con **igual prioridad**, se resuelven **de izquierda a derecha**.
4. **AS** — **Adición (suma) y Sustracción (resta)**, también **igual prioridad**, **de izquierda a derecha**.

Dos trampas que la sigla esconde y casi todo el mundo olvida:

- **M y D están EMPATADAS.** No es "primero toda la multiplicación y luego toda la división". Es: lo que aparezca primero leyendo de izquierda a derecha. Igual para suma y resta.
- **El paréntesis manda sobre todo.** Si querés cambiar el orden natural, ponés paréntesis. Son tu herramienta para eliminar la ambigüedad.

> **Regla de oro de esta skill:** cuando una expresión tenga más de dos operaciones, **no la evalúes de memoria**. Escribila en código (que aplica PEMDAS perfecto) y verificala por una segunda vía. El cerebro humano se salta pasos; el intérprete no.

## Fórmulas / método

No hay "fórmula" sino un **algoritmo de evaluación**. Dada una expresión, repetí hasta que quede un solo número:

```
Paso 1 (P): resolver el agrupador más interno. Volver al paso 1 si quedan agrupadores.
Paso 2 (E): resolver potencias y raíces.
Paso 3 (M/D): barrer de IZQUIERDA a DERECHA; cada × o ÷ que aparezca, resolverlo.
Paso 4 (A/S): barrer de IZQUIERDA a DERECHA; cada + o − que aparezca, resolverlo.
```

Notación de agrupadores (todos fuerzan "primero esto"):

| Agrupador | Significa |
|---|---|
| `( )`, `[ ]`, `{ }` | agrupación explícita |
| `a / b` (fracción) | numerador y denominador se evalúan **completos** antes de dividir |
| `√(a + b)` | la raíz cubre todo lo de adentro |
| `a^(b+c)` | el exponente entero se evalúa antes de elevar |

**Caso espinoso — el menos unario y las potencias.** `-3²` ¿es `9` o `-9`? Por convención matemática estándar (y en Python), el exponente se aplica **antes** que el signo negativo: `-3² = -(3²) = -9`. Si querés `9`, debés escribir `(-3)²`. Esto causa errores de signo silenciosos en finanzas; ante la duda, **poné paréntesis**.

## Verificación en código

Patrón ejecutar + verificar. Primera vía: dejar que Python aplique PEMDAS. Segunda vía: reconstruir el cálculo paso a paso a mano y comparar con `assert`. Para dinero, `decimal`.

```python
from decimal import Decimal, getcontext
getcontext().prec = 28  # alta precisión interna; redondeamos UNA vez al final

# --- Expresión 1: ambigüedad clásica ---
# 2 + 3 * 4   ->  debe dar 14, NO 20
v1 = 2 + 3 * 4
paso_a_mano_1 = 2 + (3 * 4)          # segunda vía: explicito el orden
assert v1 == paso_a_mano_1 == 14, (v1, paso_a_mano_1)

# --- Expresión 2: M y D empatadas, izquierda a derecha ---
# 100 / 5 * 2  ->  (100/5)*2 = 40 , NO 100/(5*2)=10
v2 = 100 / 5 * 2
correcto   = (100 / 5) * 2           # 40.0  (izq->der)
incorrecto = 100 / (5 * 2)           # 10.0  (lo que MUCHA gente cree)
assert v2 == correcto == 40.0
assert v2 != incorrecto              # demuestra que el orden importa

# --- Expresión 3: signo unario y exponente ---
assert -3**2  == -9    # exponente antes que el menos
assert (-3)**2 == 9    # paréntesis cambia el resultado

# --- Expresión 4: caso de NEGOCIO con dinero (decimal) ---
# Precio neto = 50.000 ; descuento 10% ; sobre el resultado, IVA 19%
# Fórmula correcta: neto * (1 - 0.10) * (1 + 0.19)
precio = Decimal("50000")
desc   = Decimal("0.10")
iva    = Decimal("0.19")
total = precio * (1 - desc) * (1 + iva)

# Segunda vía: paso a paso, cada etapa por separado
con_descuento = precio * (1 - desc)          # 45000
con_iva       = con_descuento * (1 + iva)    # 53550
assert total == con_iva

# Redondear UNA sola vez al final, a peso entero (COP no usa centavos)
total_cop = total.quantize(Decimal("1"))
print("Total con descuento + IVA:", total_cop, "COP")   # 53550 COP
```

Salida esperada:

```
Total con descuento + IVA: 53550 COP
```

**Tercera verificación — orden de magnitud (sanity check):** el total debería rondar el precio original. `50.000` con −10% baja a `~45.000`, y con +19% sube a `~53.500`. Cae en el rango esperado → el resultado es creíble. Si el código hubiera devuelto `5.355` o `535.500`, un error de paréntesis o de factor saltaría a la vista de inmediato.

## Ejemplo trabajado

**Situación (LatAm):** un restaurante calcula el **costo total de una compra** de insumos. Compra **3 cajas de aceite a $48.900 c/u** y **5 kg de queso a $22.400/kg**, y el proveedor cobra **$12.000 de domicilio**. ¿Cuánto paga en total?

Expresión: `3 × 48900 + 5 × 22400 + 12000`

Aplicando PEMDAS — primero las multiplicaciones (empatadas, izq→der), luego las sumas:

1. `3 × 48900 = 146.700` (aceite)
2. `5 × 22400 = 112.000` (queso)
3. `146.700 + 112.000 + 12.000 = 270.700`

```python
from decimal import Decimal
aceite = Decimal("3") * Decimal("48900")     # 146700
queso  = Decimal("5") * Decimal("22400")     # 112000
domic  = Decimal("12000")
total  = aceite + queso + domic              # PEMDAS: × antes que +
assert total == Decimal("270700")
print(total, "COP")                          # 270700 COP
```

**Resultado: $270.700 COP.**

**El error que arruina la factura:** si alguien evalúa de izquierda a derecha sin respetar PEMDAS — `((3×48900)+5)×22400 + 12000` — porque "suma lo que va viendo", obtiene un número astronómico y falso. El paréntesis o el código lo evitan.

Verificación por segunda vía (estimación): aceite ≈ 3×50.000 = 150.000; queso ≈ 5×22.000 = 110.000; +12.000 ≈ **272.000**. El exacto 270.700 cae justo al lado → correcto. **Unidades: COP (pesos colombianos).**

## Errores comunes / trampas

- **Creer que M va siempre antes que D (o + antes que −).** Están empatadas; manda la posición de izquierda a derecha. `8 ÷ 2 × 4 = 16`, no `1`.
- **Olvidar paréntesis en el denominador.** `a / b + c` significa `(a/b) + c`, NO `a/(b+c)`. En código, `tasa/12+1` no es `tasa/(12+1)`. Esto destroza fórmulas financieras.
- **El menos unario con exponentes:** `-2**2 = -4` en Python. Si querés `4`, escribí `(-2)**2`.
- **Confiar en la calculadora del celular o en escribir la fórmula "de corrido".** Distintas calculadoras interpretan `6÷2(1+3)` distinto. La multiplicación implícita (un número pegado a un paréntesis) NO tiene prioridad universal acordada → **siempre poné el `*` y los paréntesis explícitos.**
- **Encadenar porcentajes sumándolos.** Un −10% seguido de +19% **no** es +9%. Son factores que se multiplican: `(1−0,10)×(1+0,19)`. Ver [[14-porcentajes-sin-errores]].
- **Redondear en cada paso intermedio.** Acumula error. Redondeá UNA sola vez al final → [[05-cifras-significativas-y-redondeo]].

### Mini-checklist de exactitud
- [ ] ¿Toda multiplicación/división y agrupación está **explícita** (sin multiplicación implícita ni denominadores ambiguos)?
- [ ] ¿El resultado lo dio **código** (no la cabeza) y lo confirmé por una **segunda vía** (paso a paso o estimación de orden de magnitud)?
- [ ] ¿Redondeé **una sola vez al final** y el número trae **unidades**?

## Cruces
- [[03-protocolo-de-verificacion-por-codigo]] — por qué todo cálculo no trivial se ejecuta y se verifica, no se confía a la memoria.
- [[06-estimacion-y-sanity-checks]] — la estimación de orden de magnitud como segunda vía rápida.
- [[12-fracciones-decimales-y-precision]] — la línea de fracción como agrupador y el uso de `decimal`.
- [[14-porcentajes-sin-errores]] — por qué los porcentajes encadenados se multiplican, no se suman.
- [[20-expresiones-algebraicas]] — el mismo orden de operaciones aplicado a expresiones con variables.
