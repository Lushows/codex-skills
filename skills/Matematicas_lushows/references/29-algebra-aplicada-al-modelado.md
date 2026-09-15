# 29 · Álgebra aplicada al modelado

> **Qué resuelve / cuándo usarlo** — Cuando tienes un problema real (de negocio, mezcla, costos, reparto) descrito en palabras y necesitas convertirlo en ecuaciones, resolverlas con exactitud y comprobar que la solución tiene sentido frente al problema original.

## Concepto (para no-experto)

**Modelar** significa traducir una situación de la vida real al idioma de las matemáticas: ecuaciones. Es como hacer una receta: primero describes con palabras "necesito que la mezcla quede al 20% de sal", y luego lo escribes con símbolos para poder calcular cantidades exactas.

El proceso tiene cuatro pasos, siempre los mismos:

1. **Definir variables.** Una *variable* es una letra que representa un número que no conocemos todavía (la *incógnita*). Ejemplo: `x = kilos de café tipo A`. La clave es escribir SIEMPRE qué representa y en qué unidad ("x en kilos", no solo "x").
2. **Plantear ecuaciones.** Una *ecuación* es una igualdad con incógnitas: dice que dos cosas valen lo mismo. Traduces cada frase del problema a una igualdad. "El total son 50 kilos" → `x + y = 50`.
3. **Resolver.** Despejas las incógnitas con álgebra (las técnicas de [[21-ecuaciones-lineales]] y [[22-sistemas-de-ecuaciones]]).
4. **Verificar contra el problema.** Metes la solución de vuelta en las frases originales y confirmas que cuadra y que es físicamente posible (no puedes vender -3 kilos de café).

**Analogía cotidiana:** modelar es como traducir del español al inglés y luego volver a traducir para revisar. Si la traducción de ida y vuelta no dice lo mismo, algo salió mal. El paso 4 es esa traducción de regreso, y es donde se atrapan los errores que cuestan dinero.

## Fórmulas / método

No hay "una fórmula": hay un **patrón de traducción**. Frases comunes y su forma algebraica:

| Frase en español | Álgebra |
|---|---|
| "la suma de A y B es T" | `A + B = T` |
| "A es el doble de B" | `A = 2·B` |
| "el 18% de V" | `0.18·V` |
| "precio por unidad p, q unidades" | `ingreso = p·q` |
| "cuesta fijo F más c por unidad" | `costo = F + c·q` |
| "ganancia = ingreso − costo" | `G = p·q − (F + c·q)` |

**Modelo de mezcla (muy usado en gastronomía y compras):** si mezclas cantidades `x₁, x₂, …` con concentraciones (o precios) `r₁, r₂, …` para obtener un total `T` con valor objetivo `r*`:

- Balance de cantidad: `x₁ + x₂ + … = T`  (unidades: kg, L, etc.)
- Balance de valor: `r₁·x₁ + r₂·x₂ + … = r*·T`  (unidades: $·kg, %·kg, etc.)

**Símbolos:** `xᵢ` = cantidad del ingrediente i (kg o L); `rᵢ` = su precio unitario ($/kg) o concentración (fracción); `T` = total de mezcla (kg o L); `r*` = precio o concentración objetivo de la mezcla. Las unidades de los dos lados de cada ecuación DEBEN coincidir (ver [[04-notacion-unidades-y-dimensiones]]).

## Verificación en código

Problema: una cafetería de Bogotá mezcla café Premium ($28.000/kg) con café Estándar ($16.000/kg) para producir **50 kg** de una mezcla que debe costar exactamente **$20.000/kg**. ¿Cuántos kilos de cada uno?

Variables: `x` = kg de Premium, `y` = kg de Estándar.
Ecuaciones: `x + y = 50` y `28000·x + 16000·y = 20000·50`.

```python
from fractions import Fraction
import sympy as sp

# --- Vía 1: resolver el sistema EXACTO con sympy (sin floats) ---
x, y = sp.symbols('x y', real=True)
precio_prem  = sp.Integer(28000)   # $/kg
precio_est   = sp.Integer(16000)   # $/kg
total_kg     = sp.Integer(50)      # kg
precio_obj   = sp.Integer(20000)   # $/kg

eq1 = sp.Eq(x + y, total_kg)                                  # balance de cantidad (kg)
eq2 = sp.Eq(precio_prem*x + precio_est*y, precio_obj*total_kg)  # balance de valor ($)

sol = sp.solve([eq1, eq2], [x, y], dict=True)[0]
print("Premium  x =", sol[x], "kg")   # esperado 50/3
print("Estandar y =", sol[y], "kg")   # esperado 100/3
```

```python
# --- Vía 2 (segunda verificación): sustituir la solución en las frases originales ---
xv, yv = sol[x], sol[y]

# (a) ¿suman 50 kg?
assert xv + yv == 50, "Falla el balance de cantidad"

# (b) ¿el valor da exactamente 20.000 $/kg * 50 kg?
valor = precio_prem*xv + precio_est*yv
assert valor == precio_obj*total_kg, "Falla el balance de valor"

# (c) sanity check: ambas cantidades deben ser >= 0 y <= 50 (físicamente posibles)
assert 0 <= xv <= 50 and 0 <= yv <= 50, "Cantidad imposible"

# (d) orden de magnitud: 20.000 esta entre 16.000 y 28.000 -> la mezcla es valida
assert precio_est <= precio_obj <= precio_prem, "El objetivo esta fuera de rango: no hay mezcla posible"

# Presentacion redondeada SOLO al final (ver modulo 05)
print("Premium :", round(float(xv), 2), "kg")   # 16.67 kg
print("Estandar:", round(float(yv), 2), "kg")   # 33.33 kg
print("Verificacion OK")
```

La **Vía 1** resuelve el sistema en aritmética exacta (fracciones, nunca `float`). La **Vía 2** no vuelve a resolver: toma la respuesta y la mete de regreso en las afirmaciones del problema (suma, valor, signo, rango). Si cualquier `assert` falla, el número está mal. Así se cumple la doble verificación de [[03-protocolo-de-verificacion-por-codigo]].

## Ejemplo trabajado

**Resultado exacto:** `x = 50/3 kg` de Premium y `y = 100/3 kg` de Estándar.

Paso a paso, despejando a mano para entender el código:

1. De `x + y = 50` → `y = 50 − x`.
2. Sustituyo en la de valor: `28000·x + 16000·(50 − x) = 1.000.000`.
3. `28000·x + 800.000 − 16000·x = 1.000.000`.
4. `12000·x = 200.000` → `x = 200.000 / 12.000 = 50/3 ≈ 16,67 kg`.
5. `y = 50 − 50/3 = 100/3 ≈ 33,33 kg`.

**Verificación contra el problema (la traducción de regreso):**
- Cantidad: `16,67 + 33,33 = 50,00 kg` ✓ (los 50 kg pedidos).
- Valor: `28.000·(50/3) + 16.000·(100/3) = (1.400.000 + 1.600.000)/3 = 3.000.000/3 = 1.000.000` $. Dividido entre 50 kg = **20.000 $/kg** ✓ exactamente el objetivo.
- Sentido físico: ambas cantidades son positivas y menores que 50 ✓.
- Estimación gruesa: 20.000 está justo a la mitad-baja entre 16.000 y 28.000, así que esperaba **más** café barato que caro. En efecto 33,33 kg > 16,67 kg ✓.

**Respuesta con unidades:** mezclar **16,67 kg de café Premium** con **33,33 kg de café Estándar** produce 50 kg de mezcla a 20.000 $/kg exactos. (En la práctica se redondea a, p. ej., 16,7 y 33,3 kg, lo que mueve el costo apenas unas decenas de pesos por kg — ver [[05-cifras-significativas-y-redondeo]].)

## Errores comunes / trampas

- **No escribir qué es cada variable ni su unidad.** "x" sin "= kg de Premium" es la fuente número uno de respuestas absurdas. Define todo por escrito.
- **Mezclar unidades distintas en la misma ecuación.** Sumar kilos con porcentajes, o pesos con litros. Cada ecuación debe ser dimensionalmente coherente ([[04-notacion-unidades-y-dimensiones]]).
- **Plantear menos ecuaciones que incógnitas.** Con 2 incógnitas necesitas 2 condiciones independientes; si solo tienes 1 frase, el problema no tiene solución única ([[22-sistemas-de-ecuaciones]]).
- **No revisar el sentido físico.** El álgebra puede dar `x = −7 kg` o `x = 80 kg` cuando el total es 50: matemáticamente "resuelve", pero es imposible. Siempre filtra por `0 ≤ x ≤ total`.
- **Objetivo fuera de rango en mezclas.** Si pides una mezcla a 30.000 $/kg con ingredientes de 16.000 y 28.000, no existe combinación posible. El objetivo debe quedar entre el mínimo y el máximo de los componentes; verifícalo antes de resolver.
- **Calcular dinero con `float`.** Usa `Fraction`, `sympy` o `decimal` para que 1.000.000 sea exactamente 1.000.000 y no 999.999,9999 ([[12-fracciones-decimales-y-precision]]).
- **Redondear a mitad de camino.** Redondea una sola vez, al final, o los centavos se descuadran.

## Cruces

- [[20-expresiones-algebraicas]] — cómo se construyen y simplifican las expresiones que aquí traducimos.
- [[21-ecuaciones-lineales]] — resolver una sola ecuación con una incógnita.
- [[22-sistemas-de-ecuaciones]] — resolver varias ecuaciones a la vez (mezclas, repartos).
- [[06-estimacion-y-sanity-checks]] — el filtro de "¿esto tiene sentido?" del paso 4.
- [[81-costeo-y-costo-unitario]] — aplicar estos modelos al costeo real de productos.

---

**Mini-checklist de exactitud**
- [ ] Toda variable tiene definición escrita Y unidad.
- [ ] Hay tantas ecuaciones independientes como incógnitas, y cada ecuación es dimensionalmente coherente.
- [ ] La solución se sustituyó de regreso en el problema (assert) y pasó el filtro de sentido físico (signo y rango).
