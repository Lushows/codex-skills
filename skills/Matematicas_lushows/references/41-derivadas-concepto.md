# 41 · Derivadas: concepto

> **Qué resuelve / cuándo usarlo** — Mide qué tan rápido cambia una cosa cuando otra cambia "un poquito": la velocidad en un instante, la pendiente de una curva, o el costo/ingreso de producir **la siguiente unidad** (marginal). Úsalo cuando una decisión depende de "¿cuánto sube X si muevo Y un poco?".

---

## Concepto (para no-experto)

Imagina que vas en carro y miras el odómetro: a las 2:00 p.m. has recorrido 100 km, y a las 3:00 p.m. llevas 160 km. Tu **velocidad promedio** en esa hora fue 60 km/h. Pero eso no te dice a qué velocidad ibas **exactamente a las 2:30 p.m.** — quizá ibas a 90 km/h y luego frenaste. La **derivada** es justamente eso: la velocidad **instantánea**, la tasa de cambio en un punto exacto, no en un intervalo grande.

Definamos los términos clave:

- **Función** — una regla que a cada entrada le asigna una salida. La escribimos `f(x)`. Ejemplo: `f(x) = posición a la hora x`.
- **Variable independiente (`x`)** — lo que tú mueves o controlas (el tiempo, las unidades producidas).
- **Variable dependiente (`y` o `f(x)`)** — lo que cambia como consecuencia (la distancia, el costo).
- **Tasa de cambio** — cuánto cambia la salida por cada unidad que cambia la entrada. Se mide en "salida por entrada" (km **por** hora, pesos **por** unidad).
- **Pendiente** — qué tan inclinada está una línea. Si subes 60 km por cada 1 hora hacia la derecha, la pendiente es 60.

La idea central de la derivada: tomamos dos puntos sobre la curva, calculamos la pendiente de la recta que los une (la **recta secante**, que "corta" la curva en dos puntos), y luego **acercamos el segundo punto al primero** hasta que casi se tocan. Cuando esa distancia tiende a cero, la recta secante se convierte en la **recta tangente** (la que "roza" la curva en un solo punto), y su pendiente es la **derivada en ese punto**.

**Analogía cotidiana:** la derivada es el "acelerador" de una función. La función te dice *dónde estás*; la derivada te dice *qué tan rápido estás cambiando ahí mismo* y *en qué dirección* (positiva = subiendo, negativa = bajando, cero = plano).

**En negocio (lo importante para ti):** si `C(q)` es el **costo total** de producir `q` unidades, la derivada `C'(q)` es el **costo marginal**: lo que cuesta producir **una unidad más** estando en `q`. Si `I(q)` es el **ingreso total**, `I'(q)` es el **ingreso marginal**: lo que entra por vender la siguiente unidad. La regla de oro de la economía: **conviene producir más mientras el ingreso marginal supere al costo marginal**.

---

## Fórmulas / método

**Tasa de cambio promedio** (pendiente de la secante entre `x` y `x+h`):

```
  f(x + h) - f(x)
  ─────────────────
         h
```

- `h` = el "pasito" en la entrada (debe llevar las mismas unidades que `x`).
- El numerador es el cambio en la salida; el denominador, el cambio en la entrada.
- Unidad del resultado: [unidad de f] / [unidad de x].

**Derivada (tasa de cambio instantánea)** = límite de la secante cuando el pasito `h` tiende a 0:

```
  f'(x) = lim   f(x + h) - f(x)
          h→0   ─────────────────
                       h
```

- Se lee "f prima de x". También se escribe `df/dx` (Leibniz) — "cambio en f por cambio en x".
- **Interpretación geométrica:** `f'(x)` es la pendiente de la recta tangente a la curva en el punto `x`.
- **Interpretación de negocio:** si `C(q)` está en COP y `q` en unidades, entonces `C'(q)` está en **COP por unidad**.

**Aproximación marginal práctica** (lo que un dueño de negocio usa de verdad):

```
  Costo marginal en q ≈ C(q + 1) - C(q)
```

Esto es la fórmula de arriba con `h = 1` (una unidad más). Es exacta para tablas/datos discretos y muy buena aproximación de `C'(q)` cuando la curva es suave.

---

## Verificación en código

Calculamos la derivada de tres formas y exigimos que coincidan: (1) **simbólica exacta** con SymPy, (2) **numérica por límite** (diferencia centrada), y (3) **marginal discreta** (`+1 unidad`). Usamos `decimal` cuando el resultado es dinero.

```python
import sympy as sp
from decimal import Decimal, getcontext
getcontext().prec = 28

# --- Función de costo de un negocio gastronómico ---
# C(q) = costo total en COP de producir q porciones.
# Costo fijo 50.000 + 800 por porción + un término que crece (saturación de cocina).
q = sp.symbols('q', positive=True)
C = 50000 + 800*q + 5*q**2          # COP

# (1) Derivada SIMBÓLICA exacta  ->  costo marginal C'(q)
Cp = sp.diff(C, q)
print("C'(q) simbólica =", Cp)       # 10*q + 800

q0 = 100                             # evaluamos en q = 100 porciones
marg_simb = Cp.subs(q, q0)
print("Costo marginal exacto en q=100:", marg_simb, "COP/porcion")

# (2) Derivada NUMÉRICA por límite (diferencia centrada, más precisa que la simple)
#     f'(x) ≈ [f(x+h) - f(x-h)] / (2h)
def Cnum(x):
    return 50000 + 800*x + 5*x**2
h = Decimal("1e-6")
x = Decimal(q0)
marg_num = (Decimal(Cnum(x+h)) - Decimal(Cnum(x-h))) / (2*h)
print("Costo marginal numérico en q=100:", round(marg_num, 6), "COP/porcion")

# (3) Marginal DISCRETA: costo de la porción #101 menos la #100
marg_disc = Decimal(Cnum(101)) - Decimal(Cnum(100))
print("Costo de producir la porcion 101:", marg_disc, "COP")
```

```python
# --- VERIFICACIÓN POR SEGUNDA VÍA: las tres rutas deben concordar ---
# La simbólica es la verdad. La numérica debe acercarse muchísimo.
# La discreta (+1) difiere un poco porque salta de 1 en 1, no infinitesimal:
#   discreta = C'(q + 1/2) por simetría  => 10*100.5 + 800 = 1805
assert int(marg_simb) == 1800, "fallo simbólico"

# numérica vs simbólica: error < 0.01 COP
assert abs(marg_num - Decimal(1800)) < Decimal("0.01"), "fallo numérico"

# discreta esperada = C(101)-C(100) = (10*100.5 + 800) = 1805
assert marg_disc == Decimal(1805), "fallo discreto"

# Sanity de orden de magnitud: en q=100, derivada = 10*100+800 = 1800 ✓ (cientos-miles)
print("OK: 1800 COP/porcion (simbólica) ≈ 1800.000... (numérica); discreta 1805 COP")
```

Salida esperada:

```
C'(q) simbólica = 10*q + 800
Costo marginal exacto en q=100: 1800 COP/porcion
Costo marginal numérico en q=100: 1800.000000 COP/porcion
Costo de producir la porcion 101: 1805 COP
OK: 1800 COP/porcion (simbólica) ≈ 1800.000... (numérica); discreta 1805 COP
```

Las tres rutas coinciden alrededor de **1800 COP/porción** (la discreta da 1805 porque salta una unidad entera; equivale a la derivada evaluada en el punto medio 100.5). Triple confirmación → resultado confiable.

---

## Ejemplo trabajado

**Caso (LatAm):** Un food-truck en Bogotá tiene este costo total diario, en pesos colombianos, según las `q` porciones que prepara:

```
C(q) = 50.000 + 800·q + 5·q²   [COP]
```

- `50.000 COP` = costo fijo (gas, parqueo, lavado) — no depende de cuántas vendas.
- `800·q` = insumos directos: cada porción cuesta 800 COP en ingredientes base.
- `5·q²` = término creciente: a más porciones, la cocina se satura (más afán, desperdicio, horas extra). Sube **acelerándose**.

**Pregunta del dueño:** "Estoy haciendo 100 porciones al día. ¿Cuánto me cuesta realmente preparar **una más**?"

**Paso 1 — Derivar (costo marginal):**
```
C'(q) = 0 + 800 + 10·q  =  800 + 10·q   [COP por porción]
```
El `50.000` fijo desaparece (su tasa de cambio es 0: no cambia con `q`).

**Paso 2 — Evaluar en q = 100:**
```
C'(100) = 800 + 10·(100) = 800 + 1000 = 1.800 COP por porción
```

**Paso 3 — Interpretar con unidades:** producir la porción número 101 le cuesta **≈ 1.800 COP**. Si la vende a, digamos, 9.000 COP, el ingreso marginal (9.000) supera al costo marginal (1.800) → **le conviene seguir produciendo**.

**Paso 4 — Verificar (segunda vía, a mano):** costo real de pasar de 100 a 101 porciones:
```
C(101) = 50.000 + 800·101 + 5·101² = 50.000 + 80.800 + 51.005 = 181.805 COP
C(100) = 50.000 + 800·100 + 5·100² = 50.000 + 80.000 + 50.000 = 180.000 COP
Diferencia = 181.805 - 180.000 = 1.805 COP  ✓ (≈ 1.800, como predijo la derivada)
```

**Resultado:** el **costo marginal en q = 100 es 1.800 COP/porción** (la aproximación discreta da 1.805 COP, prácticamente igual). Conclusión de negocio: mientras pueda vender la porción por encima de ~1.800 COP de costo variable, cada unidad extra suma margen — hasta que el costo marginal creciente alcance al precio.

---

## Errores comunes / trampas

- **Confundir promedio con instantáneo.** La velocidad promedio del viaje no es la del instante. `(C(q)-C(0))/q` es el costo **promedio**, NO el marginal `C'(q)`. Son números distintos y llevan a decisiones distintas.
- **Olvidar las unidades.** La derivada SIEMPRE tiene unidades de "salida por entrada" (COP/porción, km/h). Un número sin unidad aquí casi siempre esconde un error. Ver [[04-notacion-unidades-y-dimensiones]].
- **Creer que la derivada es el costo total.** `C'(q)` es lo que cuesta **la siguiente** unidad, no lo que llevas gastado. El nivel y la pendiente son cosas separadas.
- **`h` demasiado pequeño en código con float.** Con `h = 1e-15` el cómputo numérico se vuelve ruido por error de redondeo (cancelación catastrófica). Usa `h ≈ 1e-6` y diferencia **centrada**, o mejor, deriva simbólico con SymPy. Ver [[07-falacias-y-errores-numericos-comunes]].
- **Derivar donde la función no es suave.** Si hay un salto o un pico (esquina), la derivada no existe en ese punto. Verifica continuidad primero — ver [[40-limites-y-continuidad]].
- **Signo mal leído.** Derivada negativa = la función **baja** ahí. No es "menos cantidad", es "dirección descendente".

---

## Cruces

- [[40-limites-y-continuidad]] — la derivada se define como un límite; sin continuidad no hay derivada.
- [[42-reglas-de-derivacion]] — cómo derivar rápido sin recalcular el límite cada vez (potencia, producto, cadena).
- [[43-optimizacion-con-derivadas]] — usar `f'(x)=0` para hallar máximos/mínimos (maximizar utilidad, minimizar costo).
- [[26-funciones-lineales-y-afines]] — el caso más simple: la derivada de una recta es su pendiente constante.
- [[81-costeo-y-costo-unitario]] — costo marginal vs. costo unitario promedio en decisiones reales de precio.

---

**Mini-checklist de exactitud**
- [ ] ¿El resultado lleva unidades de "salida por entrada" (p. ej. COP/unidad)?
- [ ] ¿Verifiqué por una 2ª vía (marginal discreta `C(q+1)−C(q)` o numérica) y concuerda?
- [ ] ¿Distinguí marginal (derivada) de promedio (total ÷ cantidad)?
