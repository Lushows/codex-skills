# 27 · Funciones exponenciales y logarítmicas

> **Qué resuelve / cuándo usarlo** — Modelar lo que crece o decae multiplicándose (interés compuesto, audiencia que se duplica, material radiactivo, base de clientes, deuda) y despejar el tiempo o la tasa usando logaritmos. Úsalo cuando el cambio sea proporcional al tamaño actual, no una cantidad fija por periodo.

## Concepto (para no-experto)

Hay dos formas básicas de crecer:

- **Lineal**: sumas lo mismo cada periodo. Ahorras $100.000 al mes → recta. (Eso es [[26-funciones-lineales-y-afines]].)
- **Exponencial**: multiplicas por lo mismo cada periodo. Tu dinero gana 2% mensual → cada mes es el mes anterior × 1,02. La cantidad que sumas crece porque la base crece.

Una **función exponencial** tiene la forma `f(t) = a · b^t`. Aquí:
- `a` = **valor inicial** (cuando `t = 0`, porque `b^0 = 1`).
- `b` = **base** o **factor de crecimiento** por periodo. Si `b > 1` crece; si `0 < b < 1` decae. La `t` está en el **exponente** — por eso "exponencial".

El **logaritmo** es simplemente la operación inversa de la exponencial: responde *"¿a qué exponente elevo la base para obtener este número?"*. Si `b^x = N`, entonces `x = log_b(N)` (se lee "logaritmo en base b de N"). Es la herramienta para **despejar el tiempo o la tasa** que está atrapada en el exponente. (Las propiedades del logaritmo están en [[16-logaritmos]].)

**Analogía cotidiana.** Un rumor: cada persona que lo sabe se lo cuenta a 2 más cada día. Día 0: 1 persona. Día 1: 3. Día 2: 9. No suma, multiplica. Para preguntar *"¿en qué día lo sabrán 1.000 personas?"* no se "adivina contando": se despeja con un logaritmo.

El número **`e ≈ 2,71828`** (constante de Euler) aparece cuando el crecimiento es **continuo** (se reinvierte a cada instante, no por periodos discretos). `ln` es el logaritmo en base `e` (logaritmo natural).

## Fórmulas / método

**Forma discreta (crecimiento por periodos):**
```
A(t) = A₀ · (1 + r)^t
```
- `A₀` = cantidad inicial (unidades: COP, clientes, gramos…)
- `r` = tasa de crecimiento por periodo en decimal (0,05 = 5%). Si decae, `r` es negativa.
- `t` = número de periodos (adimensional, mismo periodo que `r`)
- `A(t)` = cantidad después de `t` periodos (mismas unidades que `A₀`)

**Interés compuesto (caso clásico, ver [[71-interes-simple-y-compuesto]]):**
```
A = P · (1 + i/n)^(n·t)
```
- `P` = capital inicial, `i` = tasa nominal anual, `n` = capitalizaciones por año, `t` = años.

**Forma continua:**
```
A(t) = A₀ · e^(k·t)
```
- `k` = tasa instantánea de crecimiento (k>0) o decaimiento (k<0).

**Vida media (decaimiento):** tiempo `t½` en que la cantidad se reduce a la mitad.
```
A(t) = A₀ · (1/2)^(t / t½)      ⟺      k = -ln(2) / t½
```

**Despeje del tiempo (la fórmula estrella):** desde `A = A₀ · b^t`,
```
t = ln(A / A₀) / ln(b)        (b = 1+r para discreto, o usar k directo en continuo: t = ln(A/A₀)/k)
```
Funciona con `ln`, `log₁₀` o cualquier base, siempre que uses **la misma base arriba y abajo** (cambio de base, [[16-logaritmos]]).

**Regla del 72 (estimación rápida):** años para duplicar ≈ `72 / (tasa% por periodo)`. Sirve solo como *sanity check*, no como resultado final ([[06-estimacion-y-sanity-checks]]).

## Verificación en código

```python
from decimal import Decimal, getcontext
import math

getcontext().prec = 28  # alta precisión decimal para el dinero

# --- CASO 1: interés compuesto (dinero -> Decimal, nunca float) ---
P = Decimal("1000000")   # capital inicial: $1.000.000 COP
i = Decimal("0.24")      # tasa nominal anual 24%
n = 12                   # capitalización mensual
t = 3                    # 3 años

factor_mensual = (Decimal(1) + i / n)          # 1 + 0,02 = 1,02
A = P * factor_mensual ** (n * t)              # exponente entero -> exacto con Decimal
A_redondeado = A.quantize(Decimal("0.01"))     # redondear UNA sola vez al final
print("Monto final:", A_redondeado, "COP")     # 2039887.32 COP

# Verificacion 1 (segunda via): construir el monto periodo a periodo,
# multiplicando 36 veces. Si la formula es correcta, debe coincidir.
acum = P
for _ in range(n * t):
    acum = acum * factor_mensual
assert acum.quantize(Decimal("0.01")) == A_redondeado
print("OK: formula == iteracion mes a mes")

# --- CASO 2: despejar el tiempo con logaritmo ---
# Una marca crece 8% mensual. Cuantos meses para pasar de 500 a 2000 clientes?
A0, Af, r = 500.0, 2000.0, 0.08
t_meses = math.log(Af / A0) / math.log(1 + r)
print("Meses para 4x:", round(t_meses, 2))     # 18.01 meses

# Verificacion 2 (operacion inversa): meto el t hallado en la exponencial
# y debo recuperar ~2000.
reconstruido = A0 * (1 + r) ** t_meses
assert math.isclose(reconstruido, Af, rel_tol=1e-9)
print("OK: exponencial(t) reconstruye el objetivo:", round(reconstruido, 2))

# --- CASO 3: vida media (decaimiento) ---
# Un cupon promocional pierde la mitad de su efectividad cada 5 dias.
# Que fraccion queda a los 12 dias?
t_half, dias = 5.0, 12.0
fraccion = (0.5) ** (dias / t_half)
print("Fraccion restante a 12 dias:", round(fraccion, 4))  # 0.1895

# Verificacion 3 (estimacion / orden de magnitud):
# 12 dias ~ 2,4 vidas medias -> entre (1/2)^2=0.25 y (1/2)^3=0.125. 0.19 cae en rango. OK.
assert 0.125 < fraccion < 0.25
print("OK: 0.19 cae entre 0.125 y 0.25 (2.4 vidas medias)")
```

Patrón de error cero: **(1)** el dinero se calcula con `Decimal` (exponente entero → exacto, sin error de coma flotante); **(2)** cada resultado se confirma por una segunda vía — iteración, operación inversa o estimación de orden de magnitud ([[03-protocolo-de-verificacion-por-codigo]]).

## Ejemplo trabajado

**Pregunta de negocio (LatAm).** GastroLatam vende 40 calculadoras de costos este mes. Las ventas crecen **15% mensual** de forma sostenida. ¿En cuántos meses se llega a **200 ventas/mes**, y cuántas ventas acumula el mes 12?

Paso 1 — Modelar. `A(t) = 40 · (1,15)^t`, con `t` en meses, `A` en ventas/mes.

Paso 2 — Despejar el tiempo para `A = 200`:
```
200 = 40 · 1,15^t
1,15^t = 5
t = ln(5) / ln(1,15) = 1,60944 / 0,13976 = 11,52 meses
```
Como las ventas se miden por mes completo, el objetivo de 200 se supera en el **mes 12** (en el mes 11 aún no se alcanza).

Paso 3 — Valor al mes 12:
```
A(12) = 40 · 1,15^12 = 40 · 5,3503 = 214,0 ventas/mes
```

Paso 4 — Verificación.
- Inversa: `40 · 1,15^11,52 = 200,0 ✓`.
- Orden de magnitud con regla del 72: duplica cada ≈ `72/15 ≈ 4,8` meses. De 40 a 200 son ~2,32 duplicaciones → `2,32 × 4,8 ≈ 11,1` meses. Cae cerca de 11,52 ✓ (la regla del 72 sobreestima un poco la tasa por ser solo aproximación).

**Resultado:** se cruzan las **200 ventas/mes en ~11,52 meses (mes 12)**, y el **mes 12 rinde ≈ 214 ventas/mes**. (Para acumulado/serie geométrica, ver [[19-secuencias-y-series]].)

## Errores comunes / trampas

- **Confundir lineal con exponencial.** "Crece 15% al mes" NO es sumar 15% del valor inicial cada mes; es multiplicar por 1,15 cada mes. Verifica si el incremento absoluto cambia periodo a periodo (exponencial) o es constante (lineal).
- **Sumar tasas en vez de multiplicar factores.** Dos meses al 10% no es +20%; es `1,10 × 1,10 = 1,21` → +21%. El interés compuesto siempre paga "interés sobre interés".
- **Usar `float` para dinero.** `0.1` no es exacto en binario; en cadenas largas de multiplicación el centavo se corre. Usa `Decimal` o centavos enteros ([[12-fracciones-decimales-y-precision]]).
- **Mezclar bases del logaritmo.** En `t = log(A/A₀)/log(b)`, numerador y denominador deben ser la **misma** base. Con `ln` arriba y `log₁₀` abajo el resultado es basura.
- **Mezclar unidades de periodo.** Si `r` es mensual, `t` está en meses; no metas años. En interés compuesto, `i/n` y `n·t` deben referirse al mismo periodo de capitalización.
- **Redondear a mitad de camino.** Redondea solo el resultado final, una vez ([[05-cifras-significativas-y-redondeo]]). Redondear `1,15^t` intermedio arrastra error.
- **`log` de cero o negativo.** No existe `ln(0)` ni log de negativos; si `A/A₀ ≤ 0` el modelo no aplica (revisa los datos).
- **Tratar la regla del 72 como exacta.** Es estimación; nunca la entregues como cifra final.

## Cruces
- [[16-logaritmos]] — propiedades y cambio de base para despejar el exponente.
- [[15-potencias-y-raices]] — base operativa de los exponentes.
- [[71-interes-simple-y-compuesto]] — el caso financiero más usado del crecimiento exponencial.
- [[86-forecasting-y-proyeccion]] — proyectar ventas/usuarios con modelos de crecimiento.
- [[26-funciones-lineales-y-afines]] — el contraste lineal vs. exponencial.

---

**Mini-checklist de exactitud**
- [ ] ¿El cambio es proporcional al tamaño actual (exponencial) y no fijo (lineal)? Confirmado con los datos.
- [ ] Dinero en `Decimal`; misma unidad de periodo en `r` y `t`; redondeo una sola vez al final.
- [ ] Resultado verificado por segunda vía (inversa, iteración o regla del 72).
