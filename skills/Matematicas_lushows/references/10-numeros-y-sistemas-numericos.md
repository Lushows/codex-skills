# 10 · Números y sistemas numéricos

> **Qué resuelve / cuándo usarlo** — Saber QUÉ tipo de número estás manejando (¿entero?, ¿fracción?, ¿algo con decimales infinitos?) para elegir la representación EXACTA y no introducir error desde el primer paso. Es la base de todo cálculo confiable.

## Concepto (para no-experto)

Un **número** es una cantidad. Pero no todos los números se comportan igual, y de ahí salen los sistemas (conjuntos) numéricos. Imagina cajas, cada una más grande que la anterior, donde cada caja contiene a la anterior:

- **Naturales (ℕ)** — los de contar: 0, 1, 2, 3, … (el cero a veces se incluye, a veces no; aquí lo incluimos). Sirven para *contar cosas enteras*: 3 mesas, 12 clientes. No hay "media mesa" aquí.

- **Enteros (ℤ)** — los naturales **más sus negativos**: …, −2, −1, 0, 1, 2, … La palabra clave nueva es **negativo**: una cantidad por debajo de cero. Sirven para *deudas, temperaturas, saldos*: −5.000 COP en la cuenta.

- **Racionales (ℚ)** — todo número que se puede escribir como una **fracción** `a/b` (una división de dos enteros, con `b` distinto de 0). "Racional" viene de *ratio* = razón = división, no de "razonable". Aquí caben 1/2, 0,75 (= 3/4) y también 1/3 = 0,333… Sirven para *partir cosas*: tres personas se reparten una cuenta. **Clave:** su forma decimal o termina (0,75) o se **repite** en ciclo (0,3333…).

- **Irracionales (𝕀)** — números que **NO** se pueden escribir como fracción exacta de enteros. Su decimal es **infinito y SIN patrón que se repita**. Ejemplos: π ≈ 3,14159… (la razón entre el perímetro de un círculo y su diámetro) y √2 ≈ 1,41421… (el lado de la diagonal de un cuadrado de lado 1). No existe ninguna fracción que valga EXACTAMENTE π.

- **Reales (ℝ)** — la unión de racionales + irracionales: TODOS los puntos de una recta continua. Cualquier medida física (longitud, peso, tiempo) vive aquí. Es la "caja" con la que trabajamos casi siempre en negocio.

- **Complejos (ℂ)** — los reales **más** un número nuevo llamado **i** (la "unidad imaginaria"), definido como la solución de `i² = −1`. Suena raro porque ningún número real elevado al cuadrado da negativo. Sirven en ingeniería eléctrica, señales, física cuántica… raramente en finanzas del día a día, pero aparecen como raíces de ecuaciones (ver [[23-ecuaciones-cuadraticas]]).

**La cadena de inclusión:** ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ ⊂ ℂ. (El símbolo ⊂ significa "está contenido en".) Cada número natural es también entero, racional, real y complejo.

**Idea más importante para error cero:** algunos números (racionales) tienen **representación exacta** como fracción; otros (irracionales) solo se pueden **aproximar** con decimales. El error nace cuando guardas un número exacto en formato aproximado (float) sin darte cuenta. Por eso el dinero (que es racional, son centavos enteros) JAMÁS se guarda como float.

## Fórmulas / método

- Un número `x` es **racional** ⟺ existen enteros `a, b` con `b ≠ 0` tales que `x = a/b`.
- **Decimal periódico → fracción** (volver exacto un decimal que se repite). Si la parte que se repite tiene `k` dígitos, multiplica por `10^k` y resta:
  - Sea `x = 0,\overline{d_1…d_k}` (la barra ⎯ marca lo que se repite). Entonces `x = (d_1…d_k) / (10^k − 1)`.
  - Ejemplo: `0,\overline{3} = 3/9 = 1/3`; `0,\overline{27} = 27/99 = 3/11`.
- **Número complejo:** `z = a + b·i`, con `a` = parte real, `b` = parte imaginaria, e `i² = −1`. Su **módulo** (tamaño/distancia al origen) es `|z| = √(a² + b²)` (unidad: la misma de `a` y `b`).
- **Densidad de ℚ y ℝ:** entre dos números reales distintos siempre hay infinitos racionales e infinitos irracionales. No existe "el siguiente número real".

Símbolos: ℕ naturales, ℤ enteros, ℚ racionales, ℝ reales, ℂ complejos, ⊂ "subconjunto de", ⟺ "si y solo si". (Glosario completo en [[09-glosario-matematico]].)

## Verificación en código

```python
# Demostramos: representación EXACTA (Fraction/sympy) vs APROXIMADA (float).
from fractions import Fraction
import sympy as sp

# 1) Un racional simple: 1/3. Float lo aproxima; Fraction lo guarda EXACTO.
aprox = 1/3                  # float: aproximación binaria
exacto = Fraction(1, 3)     # exacto: numerador/denominador enteros
print("float 1/3      :", aprox)            # 0.3333333333333333 (cortado)
print("Fraction 1/3   :", exacto)           # 1/3

# El clasico fallo del float: 0.1 + 0.2 NO da 0.3 exacto
print("float 0.1+0.2  :", 0.1 + 0.2)        # 0.30000000000000004  <- error!
print("Fraction 0.1+0.2:", Fraction(1,10) + Fraction(2,10))  # 3/10 exacto

# 2) Convertir un decimal periodico a fraccion EXACTA: 0.272727...
x = Fraction(27, 99)
print("0.272727... = ", x)                  # 3/11

# 3) Irracional: sqrt(2) NO es fraccion. sympy lo mantiene simbolico y exacto.
r2 = sp.sqrt(2)
print("sqrt(2) simbolico:", r2, "| es racional?", r2.is_rational)  # False

# 4) Complejo: resolver x^2 + 1 = 0 -> raices imaginarias i, -i
soluciones = sp.solve(sp.Symbol('x')**2 + 1, sp.Symbol('x'))
print("raices de x^2+1=0:", soluciones)     # [-I, I]
```

```python
# ---- VERIFICACION POR SEGUNDA VIA (operacion inversa + asserts) ----
from fractions import Fraction
import sympy as sp

# (a) Inversa: si 0.272727... = 3/11, entonces 3/11 reconstruido debe repetir 27.
#     Comprobamos que 3/11 cae entre 0.2727 y 0.2728 (sanity de magnitud).
v = Fraction(3, 11)
assert Fraction(2727, 10000) < v < Fraction(2728, 10000)

# (b) Inversa del periodico via algebra: 100x - x = 27  =>  x = 27/99 = 3/11
assert Fraction(27, 99) == Fraction(3, 11)

# (c) sqrt(2) al cuadrado debe dar EXACTAMENTE 2 (no 1.9999...).
assert sp.simplify(sp.sqrt(2)**2) == 2

# (d) Complejo: (i)^2 == -1, y modulo de 3+4i == 5 (triangulo 3-4-5).
assert sp.I**2 == -1
assert sp.Abs(3 + 4*sp.I) == 5

# (e) El float SI falla la igualdad exacta -> por eso NO se usa para dinero.
assert (0.1 + 0.2) != 0.3
assert (Fraction(1,10) + Fraction(2,10)) == Fraction(3,10)

print("OK: todas las verificaciones por segunda via pasaron.")
```

Salida esperada de la verificación: `OK: todas las verificaciones por segunda via pasaron.`

## Ejemplo trabajado

**Situación (LatAm):** Tres socios de un restaurante reparten una utilidad de **$100.000 COP** en partes iguales y quieren saber el reparto EXACTO antes de redondear a pesos.

Paso 1 — Identificar el tipo de número. El reparto es `100.000 / 3`, un **racional**. En decimal da `33.333,333…` (periódico). NO es un número entero de pesos.

Paso 2 — Calcular exacto como fracción (sin perder un solo peso).

```python
from fractions import Fraction
total = Fraction(100000, 1)        # COP, exacto
por_socio = total / 3              # COP por socio, exacto
print(por_socio)                   # 100000/3  ->  33333.333... COP
entero = por_socio.numerator // por_socio.denominator   # 33333 COP
sobra  = total - entero * 3        # COP que no se pueden partir en pesos enteros
print("cada socio:", entero, "COP | sobrante:", sobra, "COP")
```

Resultado: cada socio recibe **33.333 COP** y queda **1 COP** sobrante (porque 33.333 × 3 = 99.999).

Paso 3 — Verificación inversa (cuadre): `33.333 × 3 + 1 = 99.999 + 1 = 100.000 COP`. ✅ Cuadra al peso, no se evaporó dinero. El "1 COP" debe asignarse a un socio o a caja, NO ignorarse: ahí es donde un float te haría perder centavos sin avisar.

**Resultado final:** 33.333 COP por socio + 1 COP residual a reasignar (total auditado = 100.000 COP).

## Errores comunes / trampas

- **Guardar dinero como float.** `0.1 + 0.2 == 0.30000000000000004`. El dinero es racional (centavos enteros): usa `decimal.Decimal` o `Fraction`, nunca float. Ver [[12-fracciones-decimales-y-precision]].
- **Tratar un periódico como si terminara.** Escribir `1/3 = 0,33` y multiplicar por 3 da 0,99 ≠ 1. Mantén la fracción y redondea UNA sola vez al final (ver [[05-cifras-significativas-y-redondeo]]).
- **Confundir racional con irracional.** 0,75 SÍ es racional (= 3/4); π NO. Si un número viene de medir, casi siempre lo tratas como real aproximado y debes declarar su incertidumbre.
- **Olvidar el residuo al repartir enteros.** Al dividir pesos/unidades indivisibles, la suma de las partes redondeadas puede no dar el total; siempre cuadra el sobrante.
- **Asumir que toda ecuación tiene raíz real.** `x² + 1 = 0` no tiene solución en ℝ; la tiene en ℂ. Si tu software devuelve "i" o "j", no es un bug, es un complejo.
- **Creer que entre dos decimales "no hay nada".** ℝ es denso: siempre hay infinitos números en medio; no existe "el siguiente real".

## Cruces

- [[12-fracciones-decimales-y-precision]] — cómo representar racionales sin perder exactitud (Decimal/Fraction).
- [[05-cifras-significativas-y-redondeo]] — cuándo y cómo redondear los irracionales/reales una sola vez.
- [[17-notacion-cientifica-y-magnitudes]] — escribir números muy grandes o muy pequeños sin error.
- [[23-ecuaciones-cuadraticas]] — de dónde salen las raíces complejas en la práctica.
- [[09-glosario-matematico]] — definiciones de ℕ, ℤ, ℚ, ℝ, ℂ y símbolos.

---

**Mini-checklist de exactitud**
- [ ] ¿Identifiqué si el número es entero, racional o irracional ANTES de elegir su representación?
- [ ] ¿El dinero/cantidades exactas van en `Decimal`/`Fraction` (no float)?
- [ ] ¿Cuadré el residuo al repartir cantidades indivisibles (la suma de partes = total)?
