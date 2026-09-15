# 53 · Combinatoria

> **Qué resuelve / cuándo usarlo** — Contar de cuántas maneras puede ocurrir algo (arreglos, selecciones, combinaciones de opciones) sin enumerar a mano. Es la base aritmética de la probabilidad: para saber "qué tan probable" primero hay que saber "cuántos casos hay".

## Concepto (para no-experto)

La **combinatoria** es el arte de contar bien sin contar uno por uno. En vez de listar todas las posibilidades (imposible cuando son millones), usamos fórmulas que dan el número exacto.

Tres ideas que definimos antes de usarlas:

- **Principio de conteo (regla del producto):** si una decisión se toma en pasos independientes, y el paso 1 tiene `a` opciones, el paso 2 tiene `b` opciones, etc., el total de resultados es `a × b × …`. Analogía: un combo de almuerzo con 3 entradas, 4 platos fuertes y 2 postres da `3 × 4 × 2 = 24` combos distintos. No sumas, multiplicas, porque cada entrada se puede juntar con cada plato.

- **Factorial** (símbolo `!`): es multiplicar un número por todos los enteros menores hasta 1. `5! = 5×4×3×2×1 = 120`. Por convención `0! = 1`. El factorial cuenta de cuántas formas se pueden **ordenar** `n` objetos distintos en fila.

- **Orden: ¿importa o no?** Esta es LA pregunta clave de la combinatoria:
  - Si **el orden importa** (primero, segundo, tercero son distintos), hablamos de **permutaciones**. Ejemplo: el podio de una carrera — oro, plata y bronce no son intercambiables.
  - Si **el orden NO importa** (solo importa quiénes están, no en qué orden), hablamos de **combinaciones**. Ejemplo: elegir 3 sabores de helado para una copa — da igual cuál pones primero.

Regla mental rápida: *"¿Si reordeno los mismos elementos, es un resultado diferente?"* Sí → permutación. No → combinación.

## Fórmulas / método

Sea `n` = número total de objetos disponibles, `k` = cuántos eliges/arreglas. Ambos son enteros con `0 ≤ k ≤ n`. Los resultados son números puros (sin unidades): "cantidad de maneras".

- **Factorial:**  `n! = n × (n−1) × … × 2 × 1`,  con  `0! = 1`.

- **Regla del producto:**  total `= n₁ × n₂ × … × nₘ` (m pasos independientes).

- **Permutaciones de k entre n (orden SÍ importa, sin repetir):**

  `P(n, k) = n! / (n − k)!`

- **Permutaciones de los n completos:**  `P(n, n) = n!`

- **Combinaciones de k entre n (orden NO importa, sin repetir):**  "coeficiente binomial", se lee "n en k":

  `C(n, k) = n! / [ k! · (n − k)! ]`

- **Relación clave:**  `P(n, k) = C(n, k) · k!`  (las permutaciones son las combinaciones multiplicadas por las `k!` formas de ordenar cada grupo).

- **Con repetición permitida** (cada paso puede repetir):
  - Arreglos con repetición: `nᵏ` (ej.: PIN de 4 dígitos del 0–9 → `10⁴`).
  - Combinaciones con repetición: `C(n + k − 1, k)`.

- **Uso en probabilidad** (cuando todos los resultados son igualmente probables):

  `P(evento) = casos favorables / casos posibles`

  La combinatoria sirve para contar ambos números exactamente.

## Verificación en código

```python
# Python: combinatoria EXACTA con enteros (sin float, sin error de redondeo)
from math import factorial, perm, comb
from itertools import permutations, combinations

# --- Permutaciones P(n, k): orden SÍ importa ---
def P(n, k):
    return factorial(n) // factorial(n - k)   # // = división entera exacta

# --- Combinaciones C(n, k): orden NO importa ---
def C(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

n, k = 10, 3
print("P(10,3) =", P(n, k))   # 720
print("C(10,3) =", C(n, k))   # 120

# VERIFICACIÓN 1 — comparar con las funciones nativas de Python (otra vía)
assert P(n, k) == perm(n, k),  "P discrepa de math.perm"
assert C(n, k) == comb(n, k),  "C discrepa de math.comb"

# VERIFICACIÓN 2 — contar por FUERZA BRUTA enumerando de verdad (n pequeño)
universo = list(range(n))
fuerza_perm = sum(1 for _ in permutations(universo, k))
fuerza_comb = sum(1 for _ in combinations(universo, k))
assert fuerza_perm == P(n, k), "enumeración de permutaciones no cuadra"
assert fuerza_comb == C(n, k), "enumeración de combinaciones no cuadra"

# VERIFICACIÓN 3 — identidad estructural P = C * k!
assert P(n, k) == C(n, k) * factorial(k), "P(n,k) != C(n,k)*k!"

print("Todas las verificaciones OK:", fuerza_perm, fuerza_comb)
```

Salida esperada: `P(10,3) = 720`, `C(10,3) = 120`, y todos los `assert` pasan. Usamos enteros (`//`) en todo momento: la combinatoria es conteo exacto, jamás debe aparecer un decimal a mitad de camino.

## Ejemplo trabajado

**Contexto (GastroLatam):** un restaurante arma un menú degustación. Tiene **8 platos** candidatos y quiere ofrecer un combo de **3 platos**. Dos preguntas:

1. ¿Cuántos combos distintos puede ofrecer (solo importa qué 3 platos, no el orden)?
2. ¿Cuántas "experiencias por tiempos" distintas si el orden de servicio SÍ importa (entrada → fuerte → postre)?

Paso a paso:

1. Orden NO importa → **combinación**:
   `C(8, 3) = 8! / (3! · 5!) = 40320 / (6 · 120) = 40320 / 720 = 56 combos`.

2. Orden SÍ importa → **permutación**:
   `P(8, 3) = 8! / 5! = 40320 / 120 = 336 experiencias`.

Comprobación de coherencia: `P(8,3) = C(8,3) × 3! = 56 × 6 = 336`. ✔️ Cuadra.

```python
from math import comb, perm, factorial
combos = comb(8, 3)
experiencias = perm(8, 3)
print(combos, experiencias)                 # 56 336
assert experiencias == combos * factorial(3)  # 56*6 = 336  ✔
```

**Resultado:** 56 combos posibles (unidad: *combos distintos*) y 336 experiencias ordenadas (unidad: *secuencias distintas*). Las experiencias son exactamente 6 veces más porque cada combo de 3 platos se puede servir en `3! = 6` órdenes.

**Mini-uso en probabilidad:** si el chef elige 3 platos al azar de los 8, ¿probabilidad de que salga justo tu combo favorito? `1 / C(8,3) = 1/56 ≈ 0,0179 = 1,79 %`.

## Errores comunes / trampas

- **Confundir permutación con combinación.** Si dudas, pregúntate: "¿reordenar es un caso nuevo?". Contraseñas, podios, códigos → permutación. Equipos, comités, combos, manos de cartas → combinación.
- **Olvidar si hay repetición.** Un PIN puede repetir dígitos (`10⁴`), pero elegir 3 personas distintas de un grupo no. La fórmula cambia por completo.
- **Sumar en vez de multiplicar (o al revés).** Pasos *independientes encadenados* → multiplica. Opciones *mutuamente excluyentes* ("o esto o aquello") → suma.
- **Calcular `n!` "de memoria" para n grande.** `13!` ya supera 6 mil millones; `20!` no cabe en un `int` de 64 bits en muchos lenguajes. En Python los enteros son ilimitados, pero en JavaScript usa `BigInt`. Nunca uses `float` para factoriales: pierde exactitud.
- **No simplificar antes de dividir.** `C(n,k)` evaluado como factoriales completos genera números gigantes innecesarios; `math.comb` lo hace de forma estable. Para n muy grande, usa esa función nativa.
- **Doble conteo.** Contar como distintos casos que en realidad son el mismo (típico cuando el orden no debería importar pero lo metiste). Verificación por enumeración con `itertools` lo caza en casos chicos.

## Cruces

- [[50-fundamentos-de-probabilidad]] — casos favorables / casos posibles se cuentan con combinatoria.
- [[51-reglas-de-probabilidad]] — suma vs. producto de probabilidades, espejo del principio de conteo.
- [[55-distribuciones-discretas]] — la binomial usa `C(n,k)` en su fórmula.
- [[19-secuencias-y-series]] — factoriales y series donde aparecen coeficientes binomiales.
- [[58-simulacion-monte-carlo]] — cuando contar exacto es inviable, se estima muestreando.

### Mini-checklist de exactitud
- [ ] Decidí explícitamente si **el orden importa** (permutación) o no (combinación), y si **hay repetición**.
- [ ] Calculé en código con **enteros** (`//`, `math.comb`/`math.perm`/`BigInt`), nunca con float.
- [ ] Verifiqué por **segunda vía** (identidad `P = C·k!`, función nativa o enumeración con `itertools`).
