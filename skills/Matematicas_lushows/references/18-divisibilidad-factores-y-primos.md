# 18 · Divisibilidad, factores y primos

> **Qué resuelve / cuándo usarlo** — Saber si un número cabe exacto en otro (sin sobras), descomponerlo en sus "ladrillos" primos, y calcular MCD/MCM para problemas reales: armar lotes parejos, repartir sin que sobre, o sincronizar ciclos que se repiten (reposiciones, turnos, promociones).

## Concepto (para no-experto)

**Divisibilidad** significa que un número entra exacto en otro, sin que sobre nada. Decimos que "12 es divisible entre 4" porque 12 ÷ 4 = 3 sin residuo. El **residuo** (o resto) es lo que sobra de una división: 13 ÷ 4 = 3 y sobra 1, entonces el residuo es 1.

**Factor** (o **divisor**) de un número es cualquier entero que entra exacto en él. Los factores de 12 son 1, 2, 3, 4, 6 y 12. Piensa en un factor como una forma de partir 12 galletas en grupos iguales sin romper ninguna.

**Múltiplo** es lo contrario: los múltiplos de 4 son 4, 8, 12, 16, 20... (la tabla del 4). Si A es factor de B, entonces B es múltiplo de A.

**Número primo** es un entero mayor que 1 que SOLO tiene dos factores: el 1 y él mismo. Ejemplos: 2, 3, 5, 7, 11, 13. No se pueden partir en grupos iguales más pequeños. Los primos son los "átomos" de los números. Un número que no es primo (y es mayor que 1) se llama **compuesto** (como 12 = 4 × 3).

**Factorización en primos** es escribir un número como multiplicación de solo primos. Por ejemplo 12 = 2 × 2 × 3 = 2² × 3. Es como la "receta" única de cada número: el **Teorema Fundamental de la Aritmética** garantiza que cada entero mayor que 1 tiene UNA sola receta de primos (salvo el orden). Esto es clave: si dos personas factorizan bien el mismo número, obtienen exactamente lo mismo.

**MCD** = Máximo Común Divisor: el número más grande que entra exacto en dos (o más) números a la vez. Sirve para repartir en partes iguales lo más grandes posible. Analogía: tienes 18 empanadas y 24 arepas; el MCD(18,24)=6 te dice que puedes armar como máximo 6 bolsas iguales (3 empanadas y 4 arepas cada una) sin que sobre nada.

**MCM** = Mínimo Común Múltiplo: el número más pequeño que es múltiplo de dos números a la vez. Sirve para sincronizar ciclos. Analogía: si repones harina cada 6 días y gas cada 8 días, ambas reposiciones coinciden cada MCM(6,8)=24 días.

## Fórmulas / método

**Criterios de divisibilidad** (atajos para saber si entra exacto sin dividir):

| Divisor | Criterio |
|---|---|
| 2 | El último dígito es par (0,2,4,6,8) |
| 3 | La suma de los dígitos es múltiplo de 3 |
| 4 | Los dos últimos dígitos forman un múltiplo de 4 |
| 5 | Termina en 0 o 5 |
| 6 | Divisible entre 2 **y** entre 3 |
| 8 | Los tres últimos dígitos forman un múltiplo de 8 |
| 9 | La suma de los dígitos es múltiplo de 9 |
| 10 | Termina en 0 |
| 11 | La suma alternada de dígitos (+,−,+,−...) es múltiplo de 11 |

**Notación de divisibilidad:** `a ∣ b` se lee "a divide a b" (a entra exacto en b). El residuo se denota `b mod a` (en código `b % a`); `a ∣ b` equivale a `b mod a = 0`.

**MCD por el algoritmo de Euclides** (rápido y exacto, sin factorizar):

```
mcd(a, 0) = a
mcd(a, b) = mcd(b, a mod b)
```
Se repite hasta que el segundo número sea 0; el último número distinto de 0 es el MCD.

**MCM a partir del MCD** (la fórmula clave, exacta para enteros):

```
mcm(a, b) = |a · b| / mcd(a, b)
```
donde `| |` es valor absoluto. **Importante:** divide primero o multiplica con cuidado para no inflar números; en código usa enteros, nunca float.

**Por factorización en primos:**
- MCD = producto de los primos COMUNES, cada uno elevado al **menor** exponente que aparezca.
- MCM = producto de TODOS los primos que aparezcan, cada uno elevado al **mayor** exponente.

Unidades: divisibilidad, factores y MCD/MCM trabajan con **enteros adimensionales** (conteos: días, unidades, bolsas). El resultado conserva la unidad del problema (días, empanadas, etc.).

## Verificación en código

```python
# Python estándar: math.gcd para MCD, sympy para factorizar y primos.
from math import gcd, isqrt
from functools import reduce
from sympy import factorint, isprime

# --- MCD y MCM de dos números, EXACTO con enteros ---
a, b = 18, 24
mcd = gcd(a, b)                 # Máximo Común Divisor
mcm = a * b // mcd              # // = división entera exacta (a*b siempre es múltiplo del mcd)
print("MCD(18,24) =", mcd)      # 6
print("MCM(18,24) =", mcm)      # 72

# --- MCD/MCM de una lista (asociativo: se aplica de a pares) ---
def mcm2(x, y): return x * y // gcd(x, y)
nums = [6, 8, 12]
mcd_lista = reduce(gcd, nums)
mcm_lista = reduce(mcm2, nums)
print("MCD[6,8,12] =", mcd_lista)   # 2
print("MCM[6,8,12] =", mcm_lista)   # 24

# --- Factorización en primos (la "receta" única) ---
print("Factores primos de 360:", factorint(360))  # {2:3, 3:2, 5:1} -> 2^3 * 3^2 * 5
```

```python
# === VERIFICACIÓN POR SEGUNDA VÍA ===

# Vía 1: el MCM debe ser divisible por cada número (residuo 0) y el MCD debe dividir a cada uno.
assert mcm % a == 0 and mcm % b == 0, "El MCM no es múltiplo de ambos"
assert a % mcd == 0 and b % mcd == 0, "El MCD no divide a ambos"

# Vía 2: identidad fundamental  mcd(a,b) * mcm(a,b) == a * b
assert mcd * mcm == a * b, "Falla la identidad mcd*mcm = a*b"

# Vía 3: reconstruir el número desde su factorización (operación inversa).
f = factorint(360)
producto = 1
for primo, exp in f.items():
    producto *= primo ** exp
assert producto == 360, "La factorización no reconstruye el original"

# Vía 4: comprobar primalidad por fuerza bruta y comparar con sympy.
def es_primo_bruto(n):
    if n < 2: return False
    for d in range(2, isqrt(n) + 1):   # basta probar hasta la raíz cuadrada
        if n % d == 0:
            return False
    return True
for n in [2, 11, 12, 97, 100, 561]:
    assert es_primo_bruto(n) == isprime(n), f"Discrepancia de primalidad en {n}"

print("Todas las verificaciones pasaron.")
```

Salida esperada: `MCD(18,24) = 6`, `MCM(18,24) = 72`, `MCM[6,8,12] = 24`, factores de 360 = `{2:3, 3:2, 5:1}`, y "Todas las verificaciones pasaron."

## Ejemplo trabajado

**Problema (dark kitchen en Bogotá):** El restaurante repone **harina cada 6 días** y **gas cada 8 días**. Hoy (día 0) repuso ambos. ¿Cada cuántos días vuelven a coincidir las dos reposiciones, y cuántas veces coincidirán en un trimestre de 90 días?

**Paso 1 — Identificar la operación.** "Coincidir dos ciclos" = Mínimo Común Múltiplo. Necesito MCM(6, 8).

**Paso 2 — Factorizar (para entender el porqué).**
- 6 = 2 × 3
- 8 = 2³
- MCM = mayor exponente de cada primo = 2³ × 3 = 8 × 3 = **24**.

**Paso 3 — Verificar con la fórmula del MCD.**
- MCD(6, 8): factor común es solo 2¹ → MCD = 2.
- MCM = (6 × 8) / 2 = 48 / 2 = **24**. ✔ Coincide con la factorización.

**Paso 4 — Responder la segunda parte.** Coinciden cada 24 días. En 90 días: 90 ÷ 24 = 3,75 → coinciden en los días 24, 48 y 72 (el día 96 ya se pasa de 90). Son **3 coincidencias** dentro del trimestre (sin contar el día 0).

**Comprobación de orden de magnitud:** 24 está entre 8 (el ciclo mayor) y 48 (6×8); tiene sentido. 90/24 ≈ 4, y como no llega a 96, son 3 — consistente.

**Resultado:** ambas reposiciones coinciden **cada 24 días**, y habrá **3 coincidencias** en el trimestre de 90 días (días 24, 48 y 72).

## Errores comunes / trampas

- **Confundir MCD con MCM.** Regla rápida: *repartir en partes iguales lo más grandes* → MCD; *sincronizar ciclos / próxima coincidencia* → MCM. El MCD siempre es ≤ el menor número; el MCM siempre es ≥ el mayor número. Si te da al revés, te equivocaste.
- **Creer que 1 es primo.** No lo es: un primo tiene exactamente dos divisores distintos, y 1 solo tiene uno. El 2 sí es primo (el único primo par).
- **Olvidar repetir factores en la factorización.** 12 = 2 × 2 × 3, no "2 × 3". El exponente cuenta cuántas veces se repite el primo.
- **Overflow / float en el MCM.** `a*b/mcd` con división flotante (`/`) puede dar `71.99999...` por error de redondeo. Usa división entera (`//` en Python) o trabaja con el MCD primero. Nunca uses `float` para conteos exactos (ver [[12-fracciones-decimales-y-precision]]).
- **Aplicar criterio de divisibilidad mal.** El de 4 mira los DOS últimos dígitos, no solo el último; el de 8, los TRES últimos. Ante la duda, divide y revisa el residuo en código.
- **Suponer que un número grande es primo "a ojo".** 561 parece primo pero es 3 × 11 × 17. Siempre verifica con código (`isprime`) o probando divisores hasta la raíz cuadrada.

**Mini-checklist de exactitud**
- [ ] ¿El MCD quedó ≤ el menor número y el MCM ≥ el mayor? (sanity check)
- [ ] ¿Se cumple la identidad `mcd × mcm = a × b`? (verificación cruzada)
- [ ] ¿La factorización reconstruye el número original al multiplicar de vuelta?

## Cruces
- [[10-numeros-y-sistemas-numericos]] — qué son los enteros y dónde viven primos y compuestos.
- [[12-fracciones-decimales-y-precision]] — el MCD simplifica fracciones; usar enteros, no float.
- [[15-potencias-y-raices]] — los exponentes de la factorización (2³ × 3²) y la raíz como tope al buscar divisores.
- [[06-estimacion-y-sanity-checks]] — verificar el orden de magnitud de MCD/MCM antes de confiar.
- [[03-protocolo-de-verificacion-por-codigo]] — el patrón ejecutar + verificar por segunda vía aplicado aquí.
