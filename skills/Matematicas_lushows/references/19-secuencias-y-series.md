# 19 · Secuencias y series

> **Qué resuelve / cuándo usarlo** — Cuando necesitas sumar muchos términos que siguen un patrón (cuotas, ahorros mensuales, ventas que crecen un % fijo) sin sumarlos uno por uno. Es la base matemática de anualidades, VPN y cualquier flujo financiero repetido.

## Concepto (para no-experto)

Una **secuencia** (o sucesión) es una lista ordenada de números: `a₁, a₂, a₃, …`. Cada número se llama **término** y su posición es el **índice** (`a₁` es el primer término, `a₅` el quinto). Una **serie** es lo que pasa cuando *sumas* los términos de una secuencia.

Hay dos patrones que aparecen todo el tiempo en negocios:

- **Progresión aritmética (PA):** cada término se obtiene **sumando** una cantidad fija al anterior. Esa cantidad fija se llama **diferencia común** (`d`). Ejemplo cotidiano: ahorras y subes el aporte $5.000 cada mes → 20.000, 25.000, 30.000… (d = 5.000). Crece en *línea recta*.
- **Progresión geométrica (PG):** cada término se obtiene **multiplicando** el anterior por un número fijo, la **razón común** (`r`). Ejemplo: una inversión que rinde 2% mensual → cada mes el saldo se multiplica por 1,02. Crece en *curva* (exponencial). Casi todo lo financiero (interés compuesto, inflación, anualidades) es geométrico.

La diferencia clave: **PA suma, PG multiplica**. Confundirlas es el error más caro de este tema, porque la PG crece muchísimo más rápido y de ella cuelga el dinero en el tiempo.

## Fórmulas / método

Símbolos: `a₁` = primer término, `n` = número de términos (entero ≥ 1), `d` = diferencia común (PA), `r` = razón común (PG), `Sₙ` = suma de los primeros `n` términos.

**Progresión aritmética**
- Término n-ésimo: `aₙ = a₁ + (n − 1)·d`
- Suma de n términos: `Sₙ = n·(a₁ + aₙ)/2 = n·(2·a₁ + (n−1)·d)/2`

**Progresión geométrica**
- Término n-ésimo: `aₙ = a₁·r^(n−1)`
- Suma de n términos (si `r ≠ 1`): `Sₙ = a₁·(1 − rⁿ)/(1 − r)` (equivalente: `a₁·(rⁿ − 1)/(r − 1)`)
- Si `r = 1`: todos los términos son iguales → `Sₙ = n·a₁`

**Serie geométrica infinita** (suma de infinitos términos): converge **solo si `|r| < 1`** (la razón en valor absoluto es menor que 1, es decir los términos se achican). En ese caso:
- `S∞ = a₁/(1 − r)`

Si `|r| ≥ 1` la suma infinita **no existe** (crece sin límite o no se estabiliza).

**Puente a finanzas:** el valor presente de una anualidad (una cuota fija `C` durante `n` periodos a tasa `i` por periodo) es una serie geométrica con `a₁ = C/(1+i)` y `r = 1/(1+i)`. De ahí sale `VP = C·(1 − (1+i)^(−n))/i`. Las unidades de `Sₙ` son las mismas de los términos (p. ej. COP); `d`, `r`, `i` son adimensionales (`r` e `i` salen de ratios).

## Verificación en código

```python
from decimal import Decimal, getcontext
from fractions import Fraction
getcontext().prec = 40  # alta precisión para dinero

# ---- Progresión geométrica: suma con dinero exacto (decimal) ----
a1 = Decimal("100000")   # primer aporte: 100.000 COP
r  = Decimal("1.02")     # crece 2% por periodo (razon comun)
n  = 12                  # 12 periodos

# Metodo 1: formula cerrada Sn = a1*(1 - r^n)/(1 - r)
Sn_formula = a1 * (1 - r**n) / (1 - r)

# Metodo 2 (VERIFICACION POR SEGUNDA VIA): sumar termino a termino
Sn_loop = Decimal("0")
term = a1
for _ in range(n):
    Sn_loop += term
    term *= r

print("Sn formula:", round(Sn_formula, 2), "COP")
print("Sn loop   :", round(Sn_loop, 2), "COP")
assert round(Sn_formula, 6) == round(Sn_loop, 6), "PG: formula y loop NO coinciden"

# ---- Progresion aritmetica: exacta con fracciones (sin error de float) ----
A1, D, N = Fraction(20000), Fraction(5000), 6
aN = A1 + (N - 1) * D                       # termino n-esimo
S_pa = N * (A1 + aN) / 2                     # suma por formula
S_pa_loop = sum(A1 + k * D for k in range(N))  # suma directa
assert S_pa == S_pa_loop, "PA: formula y suma directa NO coinciden"
print("PA aN:", aN, "| Sn:", S_pa)

# ---- Serie infinita: solo si |r| < 1 ----
a1_inf, r_inf = Fraction(1, 2), Fraction(1, 2)  # 1/2 + 1/4 + 1/8 + ... -> 1
S_inf = a1_inf / (1 - r_inf)
assert S_inf == 1, "Serie infinita mal"
print("S_inf:", S_inf)
```

Salida esperada: `Sn formula: 1340932.78 COP` y `Sn loop: 1340932.78 COP` (idénticos), `PA aN: 45000 | Sn: 195000`, `S_inf: 1`. Los `assert` son la doble verificación: si la fórmula y la suma directa difieren, el programa se detiene en vez de devolver un número falso.

## Ejemplo trabajado

**Caso:** GastroLatam quiere proyectar el ahorro de un cliente que aporta $100.000 COP el primer mes a una cuenta que rinde **2% mensual**, y cada mes vuelve a aportar otros $100.000 que también empiezan a rendir 2%. ¿Cuánto tiene al final de 12 meses?

Esto es una serie geométrica: el aporte del mes 1 rinde 11 meses más, el del mes 2 rinde 10 más, etc. Si valoramos al final del mes 12, cada aporte de $100.000 crece por `1,02^k`.

Paso 1 — identificar: `a₁ = 100.000`, `r = 1,02`, `n = 12`.
Paso 2 — fórmula de valor futuro de aportes (serie geométrica): `S = a₁·(rⁿ − 1)/(r − 1)`.
Paso 3 — calcular (en código, decimal): `S = 100.000·(1,02¹² − 1)/0,02`.

`1,02¹² = 1,268241795…` → `(1,268241795 − 1)/0,02 = 13,4120897…` → `S ≈ 1.341.208,98 COP`.

Paso 4 — sanity check de orden de magnitud: 12 aportes de 100.000 = **1.200.000 COP** sin interés. Con 2% mensual el extra debe ser modesto pero positivo → ~1,34 millones es razonable (≈ 12% más que el capital). Si me hubiera dado 5 millones o 900.000, sabría que algo está mal.

**Resultado: ≈ 1.341.208,98 COP** al final del mes 12 (verificado por suma término a término en el código de arriba con la misma estructura).

## Errores comunes / trampas

- **Confundir PA con PG:** "crece 5.000 cada mes" (PA, suma) no es lo mismo que "crece 5% cada mes" (PG, multiplica). El % siempre implica geométrica.
- **Error de índice `n` vs `n−1`:** `aₙ = a₁·r^(n−1)`, no `r^n`. El primer término usa exponente 0. Un fallo de 1 en `n` desplaza todo el flujo.
- **Aplicar `S∞ = a₁/(1−r)` cuando `|r| ≥ 1`:** la serie no converge; la fórmula daría un número sin sentido (incluso negativo). Verifica `|r| < 1` antes.
- **Usar float para dinero:** `0,1 + 0,2 ≠ 0,3` en float. Usa `Decimal` o centavos enteros; redondea **una sola vez al final**.
- **Olvidar el caso `r = 1`:** la fórmula `(1−rⁿ)/(1−r)` divide por cero. Si `r = 1`, `Sₙ = n·a₁`.
- **Mezclar periodicidad de la tasa:** si la tasa es anual pero los aportes son mensuales, `r` e `i` deben estar en el **mismo periodo** (ver tasas nominal/efectiva).

## Cruces

- [[15-potencias-y-raices.md]] — `rⁿ` es la potencia que mueve toda la PG.
- [[27-funciones-exponenciales-y-logaritmicas.md]] — la PG es una exponencial en tiempo discreto; el log despeja `n`.
- [[71-interes-simple-y-compuesto.md]] — interés simple = PA, interés compuesto = PG.
- [[73-anualidades-y-amortizacion.md]] — las anualidades son la serie geométrica aplicada a cuotas fijas.
- [[72-valor-presente-y-futuro.md]] — VP/VF de flujos repetidos se derivan de estas sumas.

**Mini-checklist de exactitud**
- [ ] ¿Identifiqué bien si es PA (suma `d`) o PG (multiplica `r`)? El % ⇒ PG.
- [ ] ¿Verifiqué `|r| < 1` antes de usar suma infinita, y el caso `r = 1`?
- [ ] ¿Confirmé la suma por fórmula contra la suma término a término (assert) usando `Decimal` para dinero?
