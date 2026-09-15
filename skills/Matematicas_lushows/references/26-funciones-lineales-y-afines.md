# 26 · Funciones lineales y afines

> **Qué resuelve / cuándo usarlo** — Modelar cualquier relación que crece (o decrece) a un ritmo constante: "por cada X más, Y sube tanto". Sirve para costos (fijo + variable por unidad), precios por tramo, consumo, y para ajustar una recta a dos datos reales.

## Concepto (para no-experto)

Una **función** es una regla que a cada número de entrada le asigna un único número de salida (ver [[25-funciones-concepto-dominio-rango]]).

Una **función afín** es la regla más simple después de "todo constante": tiene la forma de una **recta** cuando la dibujas. Se escribe así:

```
y = m·x + b
```

- **x** = la entrada (ej. número de platos vendidos).
- **y** = la salida (ej. costo total en pesos).
- **m** = la **pendiente** (en inglés *slope*): cuánto cambia `y` por **cada unidad** que sube `x`. Es la **tasa** de cambio. Si `m = 3.500`, cada plato extra suma $3.500 al costo.
- **b** = el **intercepto** (o *intercepto en y*): el valor de `y` cuando `x = 0`. En costos es el **costo fijo**: lo que pagas aunque vendas cero (arriendo, etc.).

**Analogía del taxi.** El taxímetro arranca con una **bandera** fija (eso es `b`, lo que pagas solo por subirte) y luego suma una **tarifa por kilómetro** (eso es `m`). El total es `b + m·(kilómetros)`. Es exactamente una función afín.

**Diferencia técnica: lineal vs. afín.** En matemática estricta, **lineal** significa `y = m·x` (pasa por el origen, `b = 0`: si no vendes nada, no cuesta nada). **Afín** es `y = m·x + b` con `b` cualquiera. En la práctica de negocios casi siempre usamos la afín (hay un costo fijo), pero todo el mundo le dice "lineal". Aquí distinguimos cuando importa.

La **pendiente como tasa**: si la pendiente es positiva, la recta sube (más `x` → más `y`); si es negativa, baja; si es cero, es una recta horizontal (`y` no depende de `x`).

## Fórmulas / método

**Forma pendiente-intercepto:**
```
y = m·x + b
```
- `m` = pendiente [unidad de y / unidad de x] — ej. $/plato.
- `b` = intercepto en y [unidad de y] — ej. $.

**Pendiente a partir de dos puntos** P1 = (x1, y1) y P2 = (x2, y2):
```
m = (y2 - y1) / (x2 - x1)        (requiere x2 ≠ x1)
```
"Cuánto subió y, dividido cuánto subió x" (el famoso *rise over run*).

**Intercepto despejando `b`** una vez que tienes `m` (usando cualquiera de los dos puntos):
```
b = y1 - m·x1
```

**Otras formas útiles de la misma recta:**
- Punto-pendiente: `y - y1 = m·(x - x1)`.
- Forma general: `A·x + B·y + C = 0`.

**Modelado lineal de costos** (el caso estrella en negocio):
```
Costo total(q) = Costo fijo + Costo variable unitario · q
        C(q)   =      CF     +        cvu            · q
```
Aquí `b = CF` (intercepto) y `m = cvu` (pendiente = costo por unidad adicional). Relaciona con [[81-costeo-y-costo-unitario]] y [[76-punto-de-equilibrio]].

## Verificación en código

Caso: una cocina paga **$1.200.000** de costos fijos mensuales y cada plato cuesta **$3.500** en insumos. Construimos la recta de costo, la evaluamos, y de paso la reconstruimos desde dos puntos para verificar.

```python
from fractions import Fraction
from decimal import Decimal, ROUND_HALF_UP

# --- Dinero exacto: usamos Decimal (NUNCA float) ---
CF  = Decimal("1200000")   # costo fijo mensual  -> intercepto b  [$]
cvu = Decimal("3500")      # costo variable/plato -> pendiente m [$/plato]

def costo_total(q):
    """C(q) = CF + cvu*q.  q = nº de platos (entero)."""
    return CF + cvu * Decimal(q)

# Evaluamos para 0, 200 y 350 platos
for q in (0, 200, 350):
    print(q, "platos ->", costo_total(q), "COP")

# ===== VERIFICACIÓN 1: pendiente reconstruida desde dos puntos =====
# Tomamos dos resultados ya calculados (200 y 350 platos) y recuperamos m.
x1, y1 = 200, costo_total(200)
x2, y2 = 350, costo_total(350)
m_reconstruida = (y2 - y1) / Decimal(x2 - x1)     # (rise/run)
assert m_reconstruida == cvu, (m_reconstruida, cvu)

# ===== VERIFICACIÓN 2: intercepto despejado b = y1 - m*x1 =====
b_reconstruido = y1 - m_reconstruida * Decimal(x1)
assert b_reconstruido == CF, (b_reconstruido, CF)

# ===== VERIFICACIÓN 3: con Fraction (otra vía, aritmética exacta) =====
m_frac = Fraction(int(y2 - y1), x2 - x1)
assert m_frac == Fraction(3500), m_frac

print("OK: pendiente =", m_reconstruida, "$/plato ; intercepto =", b_reconstruido, "$")
```

Salida esperada:
```
0 platos -> 1200000 COP
200 platos -> 1900000 COP
350 platos -> 2425000 COP
OK: pendiente = 3500 $/plato ; intercepto = 1200000 $
```

Las tres verificaciones (reconstruir `m`, despejar `b`, repetir con `Fraction`) confirman que la recta es consistente: si parto de los puntos, recupero exactamente los parámetros con los que la construí.

## Ejemplo trabajado

**Pregunta de negocio (LatAm).** Una dark kitchen registró dos meses:
- Mes con **180 platos** → costo total **$1.830.000**.
- Mes con **400 platos** → costo total **$2.600.000**.

Asumiendo costo lineal, ¿cuál es el costo por plato y el costo fijo? ¿Cuánto costarían **500 platos**?

**Paso 1 — Pendiente (costo por plato):**
```
m = (2.600.000 - 1.830.000) / (400 - 180)
  = 770.000 / 220
  = 3.500  [$/plato]
```

**Paso 2 — Intercepto (costo fijo), con el punto (180; 1.830.000):**
```
b = 1.830.000 - 3.500 · 180
  = 1.830.000 - 630.000
  = 1.200.000  [$]
```

**Paso 3 — Modelo:** `C(q) = 1.200.000 + 3.500·q` (pesos).

**Paso 4 — Proyectar 500 platos:**
```
C(500) = 1.200.000 + 3.500·500 = 1.200.000 + 1.750.000 = 2.950.000  [$]
```

**Verificación por segunda vía (con el otro punto):** usando (400; 2.600.000) para hallar `b`:
`b = 2.600.000 - 3.500·400 = 2.600.000 - 1.400.000 = 1.200.000` ✓ — coincide, así que la recta es consistente con ambos datos.

**Resultado:** costo por plato = **$3.500/plato**, costo fijo = **$1.200.000/mes**, y 500 platos costarían **$2.950.000**.

> Interpretación de la pendiente como tasa: cada plato adicional suma exactamente $3.500 al costo total; el costo fijo se reparte y por eso el **costo por plato baja** al vender más volumen (ver [[81-costeo-y-costo-unitario]]).

## Errores comunes / trampas

- **Invertir rise/run:** la pendiente es `Δy/Δx`, no `Δx/Δy`. Pregúntate siempre "por cada **uno** que sube x, ¿cuánto sube y?".
- **Restar los puntos en orden distinto arriba y abajo:** si en el numerador haces `y2 - y1`, en el denominador debe ser `x2 - x1` (mismo orden). Cruzarlos cambia el signo.
- **Confundir intercepto con primer dato:** `b` es `y` cuando `x = 0`, no el primer valor observado. Hay que despejarlo.
- **Asumir linealidad sin chequear:** con descuentos por volumen, horas extra o saltos de capacidad, el costo deja de ser una recta. Una recta ajustada a 2 puntos NO prueba que la relación sea lineal; con 3+ datos verifica que la pendiente entre pares sea (casi) la misma o usa [[64-regresion-lineal]].
- **Float para dinero:** `0.1 + 0.2 ≠ 0.3` en float. Usa `Decimal` o centavos enteros (ver [[12-fracciones-decimales-y-precision]]).
- **División por cero:** si `x2 = x1` la pendiente no existe (recta vertical); no es una función.
- **Redondear a mitad de camino:** calcula con precisión completa y redondea **una sola vez** al final ([[05-cifras-significativas-y-redondeo]]).

## Cruces

- [[25-funciones-concepto-dominio-rango]] — qué es una función (base de este módulo).
- [[21-ecuaciones-lineales]] — resolver `m·x + b = 0` (dónde la recta cruza cero).
- [[34-coordenadas-y-plano-cartesiano]] — graficar la recta y leer pendiente/intercepto.
- [[64-regresion-lineal]] — cuando tienes muchos puntos y quieres la "mejor" recta.
- [[76-punto-de-equilibrio]] — cruce de la recta de costos con la de ingresos.

**Mini-checklist de exactitud**
- [ ] ¿`m` salió de `Δy/Δx` con el **mismo orden** arriba y abajo, y verifiqué `b` con el **otro** punto?
- [ ] ¿El dinero está en `Decimal`/centavos y redondeé solo al final, con unidades ($/plato, $) explícitas?
