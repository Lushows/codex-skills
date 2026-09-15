# 21 · Ecuaciones lineales

> **Qué resuelve / cuándo usarlo** — Cuando tienes UNA incógnita (un número desconocido) que aparece elevada solo a la potencia 1 y necesitas despejarla: "¿cuántas unidades vendo para cubrir un costo?", "¿qué precio me da tal margen?", "¿cuánto invertí si la ganancia fue X?".

## Concepto (para no-experto)

Una **ecuación** es simplemente una afirmación de que dos cosas valen lo mismo: hay un signo `=` en el medio, y lo de la izquierda pesa exactamente igual que lo de la derecha. Piensa en una **balanza de dos platos** perfectamente equilibrada.

Una **incógnita** es el número que no conocemos todavía; por costumbre lo llamamos `x` (pero puede ser cualquier letra).

Una ecuación es **lineal** cuando la incógnita aparece "sola", multiplicada por números y sumada o restada, pero **nunca** elevada al cuadrado (`x²`), ni bajo una raíz, ni en el denominador con otra `x`, ni dentro de un seno o un logaritmo. Su gráfica es una **línea recta** — de ahí el nombre. Ejemplos lineales: `3x + 5 = 20`, `2(x − 1) = x + 4`. NO lineales: `x² = 9`, `1/x = 2`.

**Despejar** la incógnita significa dejarla sola a un lado del `=`. La regla de oro es la balanza: **lo que le hago a un plato, se lo hago al otro plato igualito**. Si sumo 5 a la izquierda, sumo 5 a la derecha; si divido entre 2 a la izquierda, divido entre 2 a la derecha. Así la balanza sigue equilibrada y el valor de `x` no cambia.

**Analogía cotidiana:** "Pensé un número, lo multipliqué por 3, le sumé 5 y me dio 20. ¿Qué número pensé?" Eso es `3x + 5 = 20`. Para descubrirlo deshaces los pasos al revés: primero quitas el +5 (queda `3x = 15`), luego deshaces el ×3 (queda `x = 5`).

## Fórmulas / método

Toda ecuación lineal de una incógnita se puede llevar a la **forma estándar**:

```
a·x + b = 0        →        x = −b / a        (válido solo si a ≠ 0)
```

- `x` = la incógnita (lo que buscamos).
- `a` = coeficiente que multiplica a `x` (un número conocido). **Unidad:** la que corresponda al problema.
- `b` = término independiente (constante conocida, sin `x`).
- Condición **a ≠ 0**: si `a = 0` la `x` desaparece y ya no hay ecuación lineal genuina (ver "Errores comunes").

**Método paso a paso (receta universal):**

1. **Quitar paréntesis** aplicando la propiedad distributiva: `2(x − 1) = 2x − 2`.
2. **Quitar denominadores** multiplicando ambos lados por el mínimo común denominador.
3. **Agrupar:** llevar todos los términos con `x` a un lado y todas las constantes al otro (cambiando de signo lo que cruza el `=`).
4. **Reducir** a la forma `a·x = c`.
5. **Despejar:** `x = c / a`.
6. **Verificar** sustituyendo el valor en la ecuación ORIGINAL (no en una versión ya manipulada, por si te equivocaste a mitad de camino).

## Verificación en código

Regla de la skill: no se despeja "de memoria". Usamos `sympy` para resolver de forma simbólica y EXACTA (sin redondeo), y luego verificamos por una segunda vía.

```python
# pip install sympy
from sympy import symbols, Eq, solve, Rational, simplify

x = symbols('x')

# Ecuación de ejemplo:  3x + 5 = 20
ecuacion = Eq(3*x + 5, 20)

# --- VÍA 1: resolver simbólicamente (exacto, sin floats) ---
soluciones = solve(ecuacion, x)
assert len(soluciones) == 1, "Una lineal bien planteada tiene exactamente UNA solución"
sol = soluciones[0]
print("x =", sol)                      # x = 5

# --- VÍA 2 (verificación inversa): sustituir y comprobar que los dos lados COINCIDEN ---
lado_izq = ecuacion.lhs.subs(x, sol)   # 3*5 + 5
lado_der = ecuacion.rhs.subs(x, sol)   # 20
assert simplify(lado_izq - lado_der) == 0, "La sustitución NO cuadra: revisar"
print("Verificado: ", lado_izq, "==", lado_der)
```

Y la fórmula directa `x = −b/a` con fracciones exactas (sin error de coma flotante):

```python
from fractions import Fraction

# Forma estándar  a·x + b = 0   →   aquí 3x + 5 = 20  ⇒  3x + (5 − 20) = 0  ⇒  a=3, b=−15
a = Fraction(3)
b = Fraction(5 - 20)          # = −15
assert a != 0, "Si a == 0 NO es lineal con solución única"
x_directo = -b / a            # = 5
assert x_directo == Fraction(5), "La fórmula directa debe dar lo mismo que sympy"
print("x (fórmula directa) =", x_directo)
```

Dos vías independientes (solver simbólico + fórmula con fracciones) dan `x = 5`. Coinciden ⇒ confianza.

## Ejemplo trabajado

**Problema (negocio, LatAm).** Vendes la *Calculadora de Costos Gastronómicos* a **$10.000 COP** cada una. Tienes un costo fijo mensual de **$80.000 COP** (hosting + herramientas) y un costo variable de **$2.000 COP** por venta (comisión de pasarela). ¿Cuántas unidades `x` debes vender en el mes para **quedar en cero** (ni ganar ni perder)?

Quedar en cero significa: **ingresos = costos totales**.

- Ingresos: `10000·x`  (COP)
- Costos totales: `80000 + 2000·x`  (COP)

Ecuación lineal:

```
10000·x = 80000 + 2000·x
```

Paso a paso (balanza):

1. Resto `2000·x` a ambos lados: `10000x − 2000x = 80000`  →  `8000x = 80000`.
2. Divido ambos lados entre `8000`: `x = 80000 / 8000 = 10`.

```python
from fractions import Fraction
x = symbols('x')  # sympy ya importado arriba
eq = Eq(10000*x, 80000 + 2000*x)
sol = solve(eq, x)[0]
print("Punto de equilibrio:", sol, "unidades")   # 10

# Verificación inversa CON UNIDADES (en COP, dinero como entero exacto):
ingresos = 10000 * sol            # 100000
costos   = 80000 + 2000 * sol     # 100000
assert ingresos == costos, "No cuadra el equilibrio"
print(f"Ingresos = {ingresos} COP ; Costos = {costos} COP ; iguales ✔")
```

**Resultado:** `x = 10 unidades`. Vendiendo **10 unidades al mes** ingresas $100.000 COP y gastas $100.000 COP: quedas exactamente en cero. A partir de la unidad 11 empiezas a ganar.

*Sanity check de orden de magnitud:* cada unidad deja un margen de $10.000 − $2.000 = $8.000 COP; para cubrir $80.000 de fijos necesitas $80.000 / $8.000 = 10. Coincide.

## Errores comunes / trampas

- **No cambiar el signo al pasar un término al otro lado.** Pasar `+5` a la derecha lo convierte en `−5`. La regla real no es "pasar", es "restar 5 en ambos lados".
- **Distribuir mal el negativo:** `−(x − 3)` es `−x + 3`, NO `−x − 3`.
- **Olvidar multiplicar TODOS los términos** al quitar denominadores o al distribuir un factor.
- **Dividir entre cero.** Si al reducir te queda `0·x = c`: si `c ≠ 0` no hay solución (ecuación imposible); si `c = 0` hay infinitas soluciones (identidad). No es un fallo del código: es la matemática avisando.
- **Redondear a mitad de camino.** Trabaja con fracciones exactas (`Fraction`/`sympy`) y redondea UNA sola vez al final (ver [[05-cifras-significativas-y-redondeo]]).
- **Dinero con `float`.** `0.1 + 0.2 != 0.3` en flotante. Usa centavos enteros o `decimal`/`Fraction` (ver [[12-fracciones-decimales-y-precision]]).
- **Verificar en la ecuación ya manipulada** en vez de en la original: si te equivocaste despejando, el error se "esconde". Sustituye siempre en la original.

### Mini-checklist de exactitud
- [ ] ¿Sustituí la solución en la ecuación **original** y los dos lados dieron idéntico?
- [ ] ¿Confirmé el resultado por una **segunda vía** (fórmula directa, solver simbólico o estimación de orden de magnitud)?
- [ ] ¿Comprobé que el coeficiente de `x` **no es cero** y arrastré las **unidades** hasta el final?

## Cruces
- [[20-expresiones-algebraicas]] — manipular y simplificar antes de despejar.
- [[22-sistemas-de-ecuaciones]] — cuando hay dos o más incógnitas a la vez.
- [[23-ecuaciones-cuadraticas]] — el escalón siguiente: cuando aparece `x²`.
- [[29-algebra-aplicada-al-modelado]] — traducir un problema de palabras a una ecuación.
- [[76-punto-de-equilibrio]] — aplicación financiera directa del ejemplo de arriba.
