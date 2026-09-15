# 35 · Vectores

> **Qué resuelve / cuándo usarlo** — Cuando algo tiene *cantidad Y dirección* a la vez (un desplazamiento, una mezcla de precios, una fila de datos de un cliente) y necesitas sumarlo, medir su tamaño o comparar qué tan "parecidos" son dos de ellos. Es la base matemática de datos, ML y geometría analítica.

## Concepto (para no-experto)

Un **número solo** (lo llamamos **escalar** — un valor con magnitud pero sin dirección, como "5 kilos") te dice *cuánto*. Un **vector** te dice *cuánto Y hacia dónde*: es una **lista ordenada de números** llamados **componentes**.

Analogía cotidiana: una instrucción de GPS. "Camina 3 cuadras al este y 4 cuadras al norte" es un vector con dos componentes: **v = (3, 4)**. No es lo mismo que (4, 3) — el *orden importa*, porque (4, 3) sería 4 al este y 3 al norte: otro lugar distinto.

Tres ideas clave:

- **Magnitud** (o **norma**, o **módulo**): la longitud de la flecha, qué tan largo es el vector. En el GPS, *la distancia en línea recta* desde donde empezaste hasta donde terminaste. Se escribe `‖v‖`.
- **Dirección**: hacia dónde apunta la flecha (el ángulo).
- **Componentes**: los números de la lista. Un vector de 2 componentes vive en el plano; uno de 3, en el espacio; uno de 300 componentes describe, por ejemplo, a un cliente con 300 características (edad, gasto, frecuencia…). En **datos y ML cada fila de tu tabla es un vector**.

Por qué importa en negocio: si representas a cada cliente como un vector de números, puedes medir matemáticamente qué tan *parecidos* son dos clientes (eso es lo que hacen los recomendadores y los buscadores semánticos).

## Fórmulas / método

Sea **u = (u₁, u₂, …, uₙ)** y **v = (v₁, v₂, …, vₙ)** dos vectores de **n** componentes.

**Suma** (componente a componente):
```
u + v = (u₁+v₁, u₂+v₂, …, uₙ+vₙ)
```
Geométricamente: pones la cola de un vector en la punta del otro ("regla del paralelogramo"). Unidades: ambos deben estar en la **misma unidad** (no sumes "pesos" con "minutos").

**Multiplicación por escalar** k (estira o encoge):
```
k·v = (k·v₁, k·v₂, …, k·vₙ)
```

**Magnitud / norma euclidiana** (Pitágoras generalizado):
```
‖v‖ = √(v₁² + v₂² + … + vₙ²)
```
Unidad: la misma que las componentes (si las componentes son metros, la magnitud es metros).

**Producto punto** (un número escalar, NO un vector):
```
u · v = u₁v₁ + u₂v₂ + … + uₙvₙ
```
También: `u · v = ‖u‖ · ‖v‖ · cos(θ)`, donde **θ** es el ángulo entre los dos vectores.

**Ángulo entre vectores** (despejando de la fórmula anterior):
```
cos(θ) = (u · v) / (‖u‖ · ‖v‖)        →    θ = arccos(...)
```
Esto se llama **similitud del coseno**: vale 1 si apuntan igual (idénticos en dirección), 0 si son perpendiculares (no relacionados), −1 si apuntan opuestos. Es *el* número que usan los buscadores semánticos y recomendadores.

> Símbolos: `√` raíz cuadrada; `²` al cuadrado; `θ` (theta) ángulo; `arccos` función inversa del coseno; `·` producto punto.

## Verificación en código

```python
import numpy as np

# Dos vectores de ejemplo (2D para poder dibujarlos mentalmente)
u = np.array([3.0, 4.0])
v = np.array([4.0, 3.0])

# --- VÍA 1: con numpy ---
suma      = u + v                       # suma componente a componente
mag_u     = np.linalg.norm(u)           # magnitud de u
prod_pt   = np.dot(u, v)                # producto punto
cos_theta = prod_pt / (np.linalg.norm(u) * np.linalg.norm(v))
theta_deg = np.degrees(np.arccos(cos_theta))

print("u + v      =", suma)             # [7. 7.]
print("‖u‖        =", mag_u)            # 5.0
print("u · v      =", prod_pt)          # 24.0
print("ángulo (°) =", round(theta_deg, 6))

# --- VÍA 2: verificación manual, sin numpy, fórmula a mano ---
import math
suma_m  = (u[0]+v[0], u[1]+v[1])
mag_u_m = math.sqrt(u[0]**2 + u[1]**2)
prod_m  = u[0]*v[0] + u[1]*v[1]
cos_m   = prod_m / (math.sqrt(u[0]**2+u[1]**2) * math.sqrt(v[0]**2+v[1]**2))
theta_m = math.degrees(math.acos(cos_m))

# Aserciones: las dos vías deben coincidir hasta precisión de máquina
assert np.allclose(suma, suma_m)
assert math.isclose(mag_u, mag_u_m)
assert math.isclose(prod_pt, prod_m)
assert math.isclose(theta_deg, theta_m)

# Sanity check de orden de magnitud: u=(3,4) es el clásico triángulo 3-4-5
# → su magnitud DEBE ser exactamente 5
assert math.isclose(mag_u, 5.0), "Pitágoras 3-4-5 falló"
print("OK: ambas vías coinciden y ‖(3,4)‖ = 5 exacto")
```

Salida esperada:
```
u + v      = [7. 7.]
‖u‖        = 5.0
u · v      = 24.0
ángulo (°) = 16.260205
OK: ambas vías coinciden y ‖(3,4)‖ = 5 exacto
```

Doble verificación incluida: (1) la **segunda vía manual** reproduce cada número sin numpy, y (2) un **sanity check** confirma que el vector (3,4) tiene magnitud 5, porque es el triángulo rectángulo 3-4-5 que conocemos de memoria.

## Ejemplo trabajado

**Problema (recomendador de restaurantes, GastroLatam).** Quieres saber qué tan parecidos son dos platos según su perfil de gasto en insumos, en miles de COP:

- Plato A = (carne 12, vegetales 3, lácteos 5) → **(12, 3, 5)**
- Plato B = (carne 24, vegetales 6, lácteos 10) → **(24, 6, 10)**

Nota que B es exactamente A multiplicado por 2 (mismas proporciones, doble cantidad). Esperamos que su **dirección** sea idéntica aunque su tamaño no.

Paso a paso:

1. Producto punto: `12·24 + 3·6 + 5·10 = 288 + 18 + 50 = 356`
2. `‖A‖ = √(12² + 3² + 5²) = √(144+9+25) = √178 ≈ 13.3417` (miles de COP)
3. `‖B‖ = √(24² + 6² + 10²) = √(576+36+100) = √712 ≈ 26.6833` (miles de COP)
4. `cos(θ) = 356 / (13.3417 · 26.6833) = 356 / 356.0 = 1.0`
5. `θ = arccos(1) = 0°`

**Resultado: similitud del coseno = 1.00, ángulo = 0°** → los dos platos tienen *exactamente el mismo perfil de gasto* (misma dirección), solo que B es el doble de caro. El recomendador los trataría como "idénticos en estilo". La magnitud de A es ≈ **13.34 (miles de COP)** y la de B ≈ **26.68 (miles de COP)** — el doble, como esperábamos. Verificación de orden de magnitud: 13.34 × 2 = 26.68 ✓.

## Errores comunes / trampas

- **Confundir producto punto con suma de vectores.** El producto punto da UN número (escalar); la suma da un vector. No los mezcles.
- **Sumar vectores de distinta dimensión o distinta unidad.** (3,4) + (1,2,5) no existe. Y nunca sumes una componente en pesos con una en minutos: primero normaliza/escala.
- **Olvidar que la dirección no depende del tamaño.** Dos vectores pueden tener magnitudes muy distintas y aun así similitud de coseno = 1. Por eso en ML a menudo se **normalizan** los vectores antes de comparar.
- **Tomar arccos de un valor fuera de [−1, 1].** Por errores de redondeo `cos(θ)` puede salir 1.0000000002 y `arccos` revienta. Recórtalo: `cos = max(-1, min(1, cos))`.
- **El orden de los componentes importa.** (3,4) ≠ (4,3). Mantén siempre el mismo orden de características en todas las filas.
- **Dividir por cero.** Si un vector es (0,0,…,0) su magnitud es 0 y el coseno se indefine. Trátalo aparte.

### Mini-checklist de exactitud
- [ ] ¿Mismas dimensiones y mismas unidades antes de sumar o de hacer producto punto?
- [ ] ¿`cos(θ)` quedó dentro de [−1, 1] antes de aplicar `arccos`?
- [ ] ¿Verifiqué la magnitud contra Pitágoras / un orden de magnitud razonable?

## Cruces
- [[32-teorema-de-pitagoras-y-triangulos]] — la magnitud es Pitágoras generalizado.
- [[34-coordenadas-y-plano-cartesiano]] — los componentes son coordenadas; un vector es un punto/flecha en el plano.
- [[33-trigonometria]] — el ángulo entre vectores sale del coseno.
- [[46-matrices-y-operaciones]] — apilar vectores en filas/columnas da matrices; el producto punto es la pieza base.
- [[95-matematica-para-machine-learning]] — embeddings, similitud del coseno y vectores de características.
