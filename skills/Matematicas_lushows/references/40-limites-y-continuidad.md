# 40 · Límites y continuidad

> **Qué resuelve / cuándo usarlo** — Calcular hacia qué valor se acerca una función cerca de un punto (aunque ahí no esté definida) y verificar si una función "no tiene saltos". Es la base que hace posible derivadas (módulo 41) e integrales (módulo 44).

## Concepto (para no-experto)

Imagina que vas conduciendo hacia una esquina. Aunque nunca llegues exactamente a la esquina, puedes ver claramente *hacia dónde* apunta el carro. Eso es un **límite**: el valor al que se *acerca* una función a medida que su entrada se acerca a un punto, sin importar lo que pase justo *en* ese punto.

Definamos términos clave la primera vez:

- **Función** `f(x)`: una regla que a cada número de entrada `x` le asigna una salida (ya visto en el módulo 25). Ejemplo: `f(x) = 2x` convierte 3 en 6.
- **Límite** (símbolo `lim`): el valor `L` al que se aproxima `f(x)` cuando `x` se aproxima a un número `a`. Se escribe `lim_{x→a} f(x) = L`. Se lee "el límite de f de x cuando x tiende a a es L".
- **Tiende a** (`→`): "se acerca cada vez más, sin necesariamente llegar".

El truco poderoso: el límite puede existir **aunque la función no esté definida** en el punto. Ejemplo cotidiano clásico:

```
f(x) = (x² − 1) / (x − 1)
```

En `x = 1` esto da `0/0`, que es "indeterminado" (no se puede dividir entre cero). Pero si simplificamos: `(x−1)(x+1)/(x−1) = x+1` para todo `x ≠ 1`. Entonces, cuando `x` se acerca a 1, `f(x)` se acerca a `1+1 = 2`. El límite es **2**, aunque la función tenga un "hoyo" exactamente en `x=1`.

**Límites laterales**: te puedes acercar al punto por la izquierda (`x→a⁻`, valores menores) o por la derecha (`x→a⁺`, valores mayores). El límite "completo" existe **solo si ambos lados coinciden**.

**Continuidad**: una función es **continua** en un punto `a` si la puedes dibujar sin levantar el lápiz al pasar por ahí. Formalmente, deben cumplirse 3 cosas a la vez:
1. `f(a)` existe (la función está definida en el punto).
2. `lim_{x→a} f(x)` existe (los dos lados coinciden).
3. Ese límite es igual al valor real: `lim_{x→a} f(x) = f(a)`.

Si falla alguna, hay una **discontinuidad** (un salto, un hoyo o un disparo al infinito). En negocio esto importa: una función de precio con un salto brusco (ej. un descuento que se activa de golpe a cierta cantidad) es discontinua, y eso cambia cómo la optimizas.

## Fórmulas / método

Definición intuitiva (suficiente para este nivel):

```
lim_{x→a} f(x) = L
   ⟺  f(x) se puede hacer tan cercana a L como se quiera,
       tomando x suficientemente cerca de a (pero x ≠ a).
```

Existencia por laterales:

```
lim_{x→a} f(x) = L   ⟺   lim_{x→a⁻} f(x) = L   y   lim_{x→a⁺} f(x) = L
```

Continuidad en a (las 3 condiciones):

```
f continua en a   ⟺   f(a) existe  ∧  lim_{x→a} f(x) existe  ∧  lim_{x→a} f(x) = f(a)
```

Reglas algebraicas de límites (si ambos límites existen y son finitos), con `c` constante:

```
lim (f + g) = lim f + lim g
lim (f · g) = (lim f) · (lim g)
lim (f / g) = (lim f) / (lim g)      siempre que lim g ≠ 0
lim (c · f) = c · lim f
```

Formas indeterminadas (NO valen como respuesta, exigen más trabajo — factorizar, racionalizar o L'Hôpital):

```
0/0 ,  ∞/∞ ,  0·∞ ,  ∞ − ∞ ,  1^∞ ,  0^0 ,  ∞^0
```

**Símbolos:** `x` entrada (adimensional o con la unidad del eje, p. ej. unidades vendidas); `a` punto de aproximación; `L` valor del límite (misma unidad que la salida de `f`); `→` "tiende a"; `⁻`/`⁺` lado izquierdo/derecho.

## Verificación en código

Patrón error-cero: el límite EXACTO con `sympy` (algebraico, sin redondeo) y una SEGUNDA VÍA numérica (acercarse al punto con `decimal` por ambos lados) que debe coincidir.

```python
import sympy as sp
from decimal import Decimal, getcontext

getcontext().prec = 50  # alta precisión decimal para la verificación numérica

x = sp.symbols('x')
f = (x**2 - 1) / (x - 1)   # tiene 0/0 en x = 1

# --- VÍA 1: límite EXACTO con sympy (simbólico, sin error de redondeo) ---
L = sp.limit(f, x, 1)          # límite "bilateral"
L_izq = sp.limit(f, x, 1, '-') # por la izquierda
L_der = sp.limit(f, x, 1, '+') # por la derecha
print("Límite exacto      :", L)       # -> 2
print("Lateral izquierdo  :", L_izq)   # -> 2
print("Lateral derecho    :", L_der)   # -> 2

# El límite existe SOLO si ambos laterales coinciden
assert L_izq == L_der == L, "Los laterales no coinciden: el límite NO existe"

# --- ¿Es f continua en x = 1? Aplicamos las 3 condiciones ---
fa = f.subs(x, 1)              # f(1)
es_definida = fa.is_finite     # ¿f(1) existe y es finita?
es_continua = bool(es_definida) and (L == fa)
print("f(1) =", fa, "| continua en 1:", es_continua)  # f(1)=nan -> NO continua (hoyo)

# --- VÍA 2 (verificación independiente): acercarnos numéricamente con Decimal ---
def f_dec(val):
    val = Decimal(val)
    return (val*val - Decimal(1)) / (val - Decimal(1))

izq = f_dec("0.9999999")   # x un poco menor que 1
der = f_dec("1.0000001")   # x un poco mayor que 1
print("Numérico izq:", izq, "| der:", der)

# Ambos deben aproximarse a 2; toleramos un margen pequeño por el acercamiento finito
assert abs(izq - Decimal(2)) < Decimal("1e-5")
assert abs(der - Decimal(2)) < Decimal("1e-5")
# Y el límite simbólico debe ser exactamente 2
assert L == 2
print("OK: ambas vías coinciden -> límite = 2")
```

Salida esperada: límite exacto `2`, ambos laterales `2`, `f(1)=nan` (no definida → no continua, es un hoyo removible), y los valores numéricos `~2` por los dos lados. Las dos vías —simbólica exacta y numérica con `Decimal`— concuerdan: confianza de error cero.

## Ejemplo trabajado

**Contexto LatAm.** Un proveedor de empaques para una dark kitchen cobra el costo unitario `C(q)` (en COP por caja) según la cantidad `q` de cajas pedidas, con un descuento que se *activa exactamente en 100 cajas*:

```
C(q) = 900   si q < 100
C(q) = 800   si q ≥ 100
```

Pregunta: ¿el costo unitario es **continuo** en `q = 100`? Esto importa porque si hay un salto, el costo total puede tener un brinco raro al pedir justo 100.

Paso 1 — límite por la izquierda (pedir *casi* 100, p. ej. 99 cajas): `C(q) → 900` COP/caja.
Paso 2 — límite por la derecha (pedir 100 o más): `C(q) → 800` COP/caja.
Paso 3 — comparar: `900 ≠ 800`. Los laterales **no coinciden** ⇒ el límite en `q=100` **no existe** ⇒ la función es **discontinua** en `q=100` (salto de 100 COP/caja).

Verificación en código:

```python
import sympy as sp
q = sp.symbols('q')
C = sp.Piecewise((900, q < 100), (800, q >= 100))   # COP/caja
izq = sp.limit(C, q, 100, '-')   # 900
der = sp.limit(C, q, 100, '+')   # 800
print(izq, der, "continua:", izq == der)  # 900 800 continua: False
salto = der - izq
print("Salto:", salto, "COP/caja")        # -100 COP/caja
assert izq == 900 and der == 800 and izq != der
```

**Resultado:** discontinuidad de salto en `q = 100`, con un brinco de **−100 COP/caja**. Implicación práctica con unidades: pedir 100 cajas cuesta `100 × 800 = 80.000 COP`, mientras que pedir 99 cuesta `99 × 900 = 89.100 COP`. Pedir *más* cuesta *menos* total — la discontinuidad crea un incentivo a saltar a 100. Conviene avisar a compras de este umbral.

## Errores comunes / trampas

- **Confundir `f(a)` con el límite.** El límite ignora lo que pasa *en* el punto; mira solo el *entorno*. Una función puede tener límite donde no está definida.
- **Reportar `0/0` (u otra forma indeterminada) como "no existe" o como "0" o "1".** `0/0` no es una respuesta: hay que factorizar, racionalizar o usar L'Hôpital. Puede dar cualquier valor.
- **Olvidar los laterales.** Si `lim⁻ ≠ lim⁺`, el límite NO existe aunque cada lado por separado sea finito (típico en funciones por tramos / `Piecewise`).
- **Asumir continuidad porque "se ve suave".** Verifica las 3 condiciones; un hoyo removible o un salto pequeño no siempre se nota a ojo.
- **Calcular límites con `float`.** El redondeo binario puede simular que `0.1 + 0.2 ≠ 0.3` y ensuciar la verificación numérica. Usa `Decimal` (módulo 12) o, mejor, `sympy` simbólico.
- **Dividir entre algo que tiende a 0 sin revisar el signo.** Puede dar `+∞` por un lado y `−∞` por el otro ⇒ límite inexistente, no "infinito" a secas.

### Mini-checklist de exactitud
- [ ] ¿Calculé el límite EXACTO con `sympy` (no de memoria) y confirmé los dos laterales?
- [ ] ¿Verifiqué por segunda vía (numérica con `Decimal` o L'Hôpital) y ambas coinciden?
- [ ] ¿Reporté el resultado CON unidades y aclaré si hay (dis)continuidad?

## Cruces
- [[25-funciones-concepto-dominio-rango]] — qué es una función, dominio y rango (prerrequisito).
- [[12-fracciones-decimales-y-precision]] — por qué usar `Decimal` y no `float` en la verificación numérica.
- [[41-derivadas-concepto]] — la derivada se define como un límite; este módulo es su cimiento.
- [[44-integrales]] — la integral también nace de un proceso de límite (sumas que se acercan a un área).
- [[03-protocolo-de-verificacion-por-codigo]] — el patrón ejecutar-en-código + segunda vía aplicado aquí.
