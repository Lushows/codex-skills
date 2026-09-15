# 75 · Tasas: nominal, efectiva y real

> **Qué resuelve / cuándo usarlo** — Cuando una tasa de interés viene expresada de una forma ("18% anual capitalizable mensual") y necesitas la verdad económica: la **tasa efectiva anual (EA)** que de verdad pagas o ganas, y la **tasa real** una vez le quitas la inflación. Es el módulo para comparar peras con peras entre créditos, CDTs e inversiones.

## Concepto (para no-experto)

Imagina que un banco te ofrece un crédito al "**18% nominal anual capitalizable mensualmente**". Tres palabras nuevas:

- **Tasa nominal anual**: es la tasa "de etiqueta", la que sale en grande en el aviso. Es engañosa porque NO te dice cuánto pagas de verdad: solo es la tasa de cada periodo *multiplicada* por cuántos periodos hay en el año. Si dicen "18% nominal capitalizable mensual", significa que cada mes te cobran 18%/12 = 1,5%, y ese 1,5% se aplica 12 veces.

- **Capitalización (o composición)**: es el momento en que los intereses se suman al capital y empiezan a generar más intereses (interés sobre interés). "Capitalizable mensual" = los intereses se acumulan cada mes.

- **Tasa efectiva anual (EA)**: es la tasa REAL que terminas pagando o ganando en un año, ya contando que los intereses se reinvierten. Es la única cifra honesta para comparar. Siempre que haya más de una capitalización al año, **la EA es mayor que la nominal**.

Analogía: la tasa nominal es el precio "desde $X" de un tiquete de avión; la EA es lo que de verdad pagas cuando le sumas impuestos y cargos. Nadie compara vuelos por el "desde"; comparas el total. Igual con tasas: **compara siempre por EA.**

Y falta la **inflación**: el aumento general de precios. Si tu inversión rinde 12% EA pero los precios suben 9% al año, tu dinero solo creció 12% pero compra apenas ~2,75% más cosas. Esa ganancia "de poder de compra" es la **tasa real**. La nominal/efectiva es lo que ves en el extracto; la real es lo que de verdad mejora tu vida.

## Fórmulas / método

Sea:
- `i_nom` = tasa **nominal anual** (decimal, ej. 0,18 para 18%)
- `m` = número de **capitalizaciones por año** (mensual=12, trimestral=4, diaria=365)
- `i_p` = tasa **periódica** = `i_nom / m`
- `EA` = tasa **efectiva anual** (decimal)

**1. Periódica desde nominal:**
```
i_p = i_nom / m
```

**2. Efectiva anual desde nominal (la fórmula clave):**
```
EA = (1 + i_nom/m)^m − 1
```

**3. Nominal desde efectiva (inversa):**
```
i_nom = m · [ (1 + EA)^(1/m) − 1 ]
```

**4. Convertir entre dos periodicidades efectivas** (de una tasa efectiva por periodo `i1` con `n1` periodos/año a otra `i2` con `n2`):
```
i2 = (1 + i1)^(n1/n2) − 1
```
Regla de oro: **las tasas efectivas se convierten elevando a la razón de periodos, NUNCA multiplicando/dividiendo.** Solo las nominales se prorratean linealmente.

**5. Tasa real (ecuación de Fisher), `i_real` con inflación `π`:**
```
1 + i_real = (1 + i_nominal_efectiva) / (1 + π)
  ⇒  i_real = (1 + i) / (1 + π) − 1
```
Aproximación rápida (solo para sanity check, NO para el resultado final): `i_real ≈ i − π`. Es válida solo cuando ambas son pequeñas; con inflación alta exagera la tasa real.

Unidades: todas las tasas son adimensionales (proporción por unidad de tiempo). Reporta siempre el periodo: "EA", "mensual efectiva", "real anual".

## Verificación en código

```python
from decimal import Decimal, getcontext

getcontext().prec = 30  # alta precisión para tasas

def nominal_a_ea(i_nom: Decimal, m: int) -> Decimal:
    """Tasa efectiva anual desde nominal capitalizable m veces/año."""
    i_p = i_nom / Decimal(m)            # tasa periódica
    return (Decimal(1) + i_p) ** m - Decimal(1)

def ea_a_nominal(ea: Decimal, m: int) -> Decimal:
    """Inversa: tasa nominal anual desde la EA."""
    # (1+EA)^(1/m) con decimal: usar ** sobre float controlado o raíz
    base = (Decimal(1) + ea)
    raiz = base ** (Decimal(1) / Decimal(m))   # Decimal soporta exponente fraccionario
    return Decimal(m) * (raiz - Decimal(1))

def convertir_efectiva(i1: Decimal, n1: int, n2: int) -> Decimal:
    """De tasa efectiva por periodo (n1/año) a efectiva por periodo (n2/año)."""
    return (Decimal(1) + i1) ** (Decimal(n1) / Decimal(n2)) - Decimal(1)

def tasa_real(i: Decimal, inflacion: Decimal) -> Decimal:
    """Fisher exacto."""
    return (Decimal(1) + i) / (Decimal(1) + inflacion) - Decimal(1)

# --- Caso: 18% nominal anual capitalizable mensual ---
i_nom = Decimal("0.18")
m = 12
ea = nominal_a_ea(i_nom, m)
print(f"EA = {ea*100:.6f} %")   # 19.561817 %

# --- VERIFICACIÓN POR SEGUNDA VÍA (operación inversa) ---
# Si convierto la EA de vuelta a nominal, debo recuperar 0.18
i_nom_recuperada = ea_a_nominal(ea, m)
print(f"nominal recuperada = {i_nom_recuperada*100:.6f} %")  # 18.000000 %
assert abs(i_nom_recuperada - i_nom) < Decimal("1e-12"), "Inversa falló"

# Segunda vía adicional: la mensual efectiva es 1.5%; un año = 12 meses compuestos
i_mensual = i_nom / m                       # 0.015
ea_por_meses = (Decimal(1) + i_mensual) ** 12 - Decimal(1)
assert abs(ea_por_meses - ea) < Decimal("1e-18"), "Composición mensual no coincide"
print(f"EA vía composición mensual = {ea_por_meses*100:.6f} %")  # 19.561817 %

# --- Tasa real con inflación 9% ---
inflacion = Decimal("0.09")
real = tasa_real(ea, inflacion)
print(f"tasa real = {real*100:.6f} %")  # 9.689741 %

# Verificación tasa real por inversa: (1+real)*(1+infl) debe dar (1+EA)
chequeo = (Decimal(1) + real) * (Decimal(1) + inflacion)
assert abs(chequeo - (Decimal(1) + ea)) < Decimal("1e-18"), "Fisher inverso falló"

# Sanity check con aproximación (debe estar cerca, NO igual)
aprox = ea - inflacion   # 0.1956 - 0.09 = 0.1056 -> exagera vs 0.0969 real
print(f"aprox i-π = {aprox*100:.4f} %  (estimación gruesa, sobreestima)")
```

Salida esperada:
```
EA = 19.561817 %
nominal recuperada = 18.000000 %
EA vía composición mensual = 19.561817 %
tasa real = 9.689741 %
aprox i-π = 10.5618 %  (estimación gruesa, sobreestima)
```

Las tres verificaciones (inversa de nominal, composición mes a mes, e inversa de Fisher) confirman el resultado por caminos distintos.

## Ejemplo trabajado

**Decisión real (Colombia, COP):** Vas a tomar un crédito de **$5.000.000 COP**. Un banco lo ofrece al **24% nominal anual capitalizable mensual**; otro al **25% EA**. ¿Cuál es más barato? Y si la inflación es del 7% anual, ¿cuál es el costo real?

Paso 1 — Llevar todo a EA (peras con peras):
- Banco A: `i_p = 0,24/12 = 0,02` (2% mensual). `EA = (1 + 0,02)^12 − 1 = 0,268242 = 26,8242% EA`.
- Banco B: ya está en **25,0000% EA**.

Paso 2 — Comparar: el Banco B (25% EA) es **más barato** que el Banco A (26,82% EA), aunque su número "de etiqueta" (25) parezca mayor que 24. Esta es exactamente la trampa que el módulo evita.

Paso 3 — Costo en dinero a un año sobre $5.000.000:
- Banco A: `5.000.000 × 0,268242 = $1.341.211 COP` de intereses.
- Banco B: `5.000.000 × 0,25 = $1.250.000 COP` de intereses.
- Diferencia a favor de B: **$91.211 COP/año.**

Paso 4 — Costo **real** (descontando inflación 7%), con Fisher:
- Banco B: `i_real = (1 + 0,25)/(1 + 0,07) − 1 = 0,168224 = 16,8224% real anual`.

Interpretación con unidades: aunque pagas 25% EA en pesos nominales, el costo en **poder de compra** es 16,82% real anual, porque parte de lo que pagas solo compensa que el dinero vale menos. (Verificado: `(1,168224)(1,07) = 1,25` ✓.)

## Errores comunes / trampas

- **Comparar por la nominal en vez de la EA.** "24%" puede ser más caro que "25% EA". Siempre convierte todo a EA antes de decidir.
- **Sumar o restar tasas efectivas** ("2% mensual × 12 = 24% anual"). FALSO: 2% mensual efectivo = 26,82% EA. Las efectivas se componen, no se multiplican.
- **Olvidar `m` (la periodicidad).** "18% nominal" sin decir capitalizable cada cuánto es ambiguo; la EA cambia con `m`. A mayor `m`, mayor EA (el límite cuando `m→∞` es la capitalización continua: `EA = e^(i_nom) − 1`).
- **Usar `i_real ≈ i − π` como resultado final.** Es solo sanity check; con inflación alta sobreestima la tasa real (en el ejemplo daba 10,56% vs 9,69% real).
- **Mezclar la inflación con tasa periódica equivocada.** Fisher usa tasas del mismo horizonte (anual con anual, mensual con mensual).
- **Float para dinero.** Usa `decimal`; redondea una sola vez al final.

## Cruces

- [[71-interes-simple-y-compuesto.md]] — de dónde sale la composición que genera la EA.
- [[70-valor-del-dinero-en-el-tiempo.md]] — el principio que hace que tasa y tiempo importen.
- [[74-vpn-y-tir.md]] — la TIR es una tasa efectiva; debe compararse contra la EA del costo de capital.
- [[79-moneda-inflacion-y-devaluacion.md]] — la inflación que entra en la fórmula de Fisher.
- [[14-porcentajes-sin-errores.md]] — base para no confundir puntos porcentuales con proporciones.

**Mini-checklist de exactitud**
- [ ] ¿Todo está en EA antes de comparar dos tasas?
- [ ] ¿Verifiqué la EA por la inversa (volver a nominal) y recuperé el dato original?
- [ ] ¿La tasa real la saqué con Fisher exacto, no con la resta `i − π`?
