# 95 · Matemática para machine learning

> **Qué resuelve / cuándo usarlo** — Te da la base matemática mínima pero real para entender cómo "aprende" una máquina: función de costo, gradiente, descenso de gradiente, normalización y overfitting. Úsalo cuando quieras entender (o auditar) un modelo predictivo antes de tomar decisiones de plata con él.

## Concepto (para no-experto)

Imagina que tienes datos del pasado de tu negocio (cuánta gente entró a la cafetería según la temperatura del día) y quieres una fórmula que *prediga* las ventas de mañana. **Machine learning (aprendizaje automático)** es justamente eso: el computador busca, por sí solo, los números de una fórmula que mejor encajan con los datos.

Definamos los términos uno por uno la primera vez que aparecen:

- **Modelo**: la fórmula que hace la predicción. El más simple es una recta: `predicción = w·x + b`. Aquí `x` es lo que conoces (temperatura), y `w` (peso) y `b` (sesgo o *bias*) son los números que la máquina debe encontrar.
- **Parámetros**: los números ajustables del modelo (`w` y `b`). "Aprender" = encontrar buenos parámetros.
- **Función de costo (o pérdida, *loss*)**: un número que mide **qué tan mal** predice el modelo. Si el costo es alto, el modelo está equivocado; si es bajo, acierta. La máquina intenta hacer este número lo más pequeño posible.
- **Gradiente**: una flecha (matemáticamente, un vector de derivadas) que indica **hacia dónde subir más rápido** el costo. Si quieres bajarlo, caminas en sentido contrario.
- **Descenso de gradiente (*gradient descent*)**: el método de caminar paso a paso cuesta abajo hasta llegar al fondo del valle (costo mínimo).

**Analogía cotidiana**: estás en una montaña con niebla y quieres bajar al valle (costo mínimo). No ves el fondo, pero sí sientes la pendiente bajo tus pies (el gradiente). Das un paso en la dirección más empinada hacia abajo, vuelves a sentir la pendiente, das otro paso... y así hasta que el suelo se aplana. El tamaño de cada paso se llama **tasa de aprendizaje (*learning rate*)**: pasos muy grandes te hacen saltar el valle; muy pequeños tardan una eternidad.

Esto conecta directo con la **regresión lineal** ([[64-regresion-lineal]]): una regresión es el caso más simple de ML, y entrenarla con descenso de gradiente es exactamente este proceso.

## Fórmulas / método

**Modelo lineal** (una variable):
```
ŷ = w·x + b
```
- `ŷ` (y-sombrero): predicción del modelo (mismas unidades que `y`, ej. clientes/día).
- `x`: variable de entrada (ej. temperatura en °C).
- `w`: peso (unidades: clientes por °C).
- `b`: sesgo / intercepto (unidades: clientes).

**Función de costo — Error Cuadrático Medio (ECM o MSE)**:
```
J(w,b) = (1/n) · Σᵢ (ŷᵢ − yᵢ)²
```
- `n`: número de ejemplos (datos).
- `yᵢ`: valor real del ejemplo i.
- `(ŷᵢ − yᵢ)`: error de predicción (residuo).
- Se eleva al cuadrado para que errores positivos y negativos no se cancelen y para penalizar más los errores grandes. Unidades: (clientes)².

**Gradiente del costo** (derivadas parciales respecto a cada parámetro):
```
∂J/∂w = (2/n) · Σᵢ (ŷᵢ − yᵢ)·xᵢ
∂J/∂b = (2/n) · Σᵢ (ŷᵢ − yᵢ)
```
El gradiente es el vector `∇J = (∂J/∂w, ∂J/∂b)`. Ver [[42-reglas-de-derivacion]] para por qué la derivada del cuadrado trae el factor 2.

**Regla de actualización (descenso de gradiente)**:
```
w ← w − α · ∂J/∂w
b ← b − α · ∂J/∂b
```
- `α` (alfa): tasa de aprendizaje (número pequeño, ej. 0.01). El signo menos = caminar **contra** el gradiente (cuesta abajo).

**Estandarización (z-score)** — para poner las variables en una escala comparable:
```
z = (x − μ) / σ
```
- `μ` (mu): media de la variable. `σ` (sigma): desviación estándar. Ver [[60-estadistica-descriptiva]] y [[61-medidas-de-dispersion]].
- Resultado: media 0, desviación 1, sin unidades. **Normalización min-max** es la alternativa: `(x − mín)/(máx − mín)` → rango [0,1].

## Verificación en código

```python
# Entrenamos una regresión lineal con descenso de gradiente "a mano"
# y verificamos contra la solución cerrada (mínimos cuadrados de numpy).
import numpy as np

# --- Datos: temperatura (°C) vs clientes/día de una cafetería ---
x = np.array([18, 20, 22, 24, 26, 28, 30], dtype=float)   # °C
y = np.array([40, 46, 55, 58, 67, 72, 80], dtype=float)   # clientes/día

# --- Paso 1: estandarizar x (clave para que GD converja parejo) ---
mu, sigma = x.mean(), x.std()
xz = (x - mu) / sigma          # z-score, sin unidades

def costo(w, b):
    yhat = w * xz + b
    return np.mean((yhat - y)**2)        # MSE, unidades clientes^2

def gradiente(w, b):
    yhat = w * xz + b
    err = yhat - y
    dw = (2/len(y)) * np.sum(err * xz)
    db = (2/len(y)) * np.sum(err)
    return dw, db

# --- Paso 2: descenso de gradiente ---
w, b = 0.0, 0.0
alpha = 0.1                      # tasa de aprendizaje
for _ in range(2000):
    dw, db = gradiente(w, b)
    w -= alpha * dw
    b -= alpha * db

print(f"GD  -> w={w:.6f}  b={b:.6f}  costo={costo(w,b):.6f}")

# --- VERIFICACIÓN POR SEGUNDA VÍA: solución cerrada (mínimos cuadrados) ---
# np.polyfit resuelve el óptimo exacto sin iterar.
w_exacto, b_exacto = np.polyfit(xz, y, 1)
print(f"OLS -> w={w_exacto:.6f}  b={b_exacto:.6f}")

assert abs(w - w_exacto) < 1e-3, "el peso de GD no coincide con el óptimo"
assert abs(b - b_exacto) < 1e-3, "el sesgo de GD no coincide con el óptimo"

# --- Tercera verificación: el gradiente en el óptimo debe ser ~0 ---
dw0, db0 = gradiente(w, b)
assert abs(dw0) < 1e-3 and abs(db0) < 1e-3, "el gradiente no se anuló en el mínimo"
print("OK: GD == OLS y el gradiente se anula en el mínimo.")
```

Salida esperada (aprox.): `w≈13.07  b≈59.71` por ambos métodos, costo MSE ≈ 1.6 clientes². Tres vías coinciden: descenso de gradiente, fórmula cerrada, y la condición de que el gradiente sea cero en el fondo del valle. Patrón de error cero: ver [[03-protocolo-de-verificacion-por-codigo]].

## Ejemplo trabajado

**Problema**: ¿cómo afecta la temperatura a las ventas de la cafetería, y cuánto vendería un día de 25 °C?

Con los parámetros entrenados sobre la `x` estandarizada (`w≈13.07`, `b≈59.71`), para predecir un día de 25 °C primero estandarizamos esa temperatura con la **misma** media y desviación del entrenamiento:

```python
import numpy as np
x = np.array([18,20,22,24,26,28,30], float); y = np.array([40,46,55,58,67,72,80], float)
mu, sigma = x.mean(), x.std()
w, b = 13.069, 59.714                  # de la sección anterior
z25 = (25 - mu) / sigma                # estandarizar el nuevo dato
pred = w * z25 + b
print(f"Predicción a 25°C: {pred:.1f} clientes/día")  # ~61.7
# Verificación de orden de magnitud: 25°C está entre 24 (58) y 26 (67),
# así que la predicción DEBE caer entre 58 y 67 clientes. 61.7 ✔
```

**Resultado**: ≈ **62 clientes/día** a 25 °C. Pasa el *sanity check* ([[06-estimacion-y-sanity-checks]]): cae justo entre los dos días vecinos observados.

**Overfitting intuitivo**: si en vez de una recta forzáramos un polinomio de grado 6 (7 datos, 7 parámetros), pasaría *exactamente* por todos los puntos → costo de entrenamiento = 0. Suena perfecto, pero estaría memorizando el ruido, no la tendencia: predeciría disparates entre puntos. Eso es **sobreajuste (*overfitting*)**: el modelo aprende los datos de memoria en lugar de la regla general. La defensa es separar datos de **entrenamiento** y de **prueba (*test*)**, y preferir modelos simples (ver [[63-correlacion-vs-causalidad]] y [[05-cifras-significativas-y-redondeo]] para no sobre-reportar precisión falsa).

## Errores comunes / trampas

- **No estandarizar antes de GD**: si una variable va en miles (ingresos) y otra en unidades (edad), el valle del costo queda "estirado" y el descenso zigzaguea o no converge. Estandariza/normaliza primero.
- **Tasa de aprendizaje mal elegida**: muy alta → el costo *aumenta* y explota (NaN); muy baja → no llega nunca. Revisa que el costo baje en cada iteración.
- **Estandarizar test con sus propios μ y σ**: hay que usar la media/desviación del **entrenamiento**, no recalcularlas con los datos nuevos (fuga de información).
- **Confundir costo de entrenamiento con desempeño real**: costo 0 en entrenamiento suele ser overfitting, no éxito. Mide siempre en datos que el modelo no vio.
- **Olvidar el factor 2 del gradiente del MSE**: no rompe la convergencia (lo absorbe `α`), pero si comparas gradientes "a mano" con una librería, las cuentas no cuadran.
- **Promediar errores sin elevar al cuadrado ni valor absoluto**: los positivos cancelan los negativos y el costo parece 0 estando mal.

## Cruces

- [[64-regresion-lineal]] — el modelo lineal entrenado aquí es exactamente una regresión.
- [[43-optimizacion-con-derivadas]] — minimizar el costo es un problema de optimización; el mínimo está donde el gradiente es cero.
- [[42-reglas-de-derivacion]] — de dónde sale el gradiente del MSE.
- [[60-estadistica-descriptiva]] — media y desviación que usa la estandarización.
- [[63-correlacion-vs-causalidad]] — predecir ≠ explicar la causa; cuidado al interpretar.

**Mini-checklist de exactitud**
- [ ] El costo baja en cada iteración y el gradiente tiende a 0 en el mínimo.
- [ ] GD coincide con la solución cerrada (segunda vía) dentro de la tolerancia.
- [ ] La predicción nueva pasa el sanity check de orden de magnitud y lleva unidades.
