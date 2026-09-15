# 51 · Reglas de probabilidad

> **Qué resuelve / cuándo usarlo** — Combinar probabilidades de varios eventos (este O aquel, este Y aquel, "que NO pase") y ajustar una probabilidad cuando ya sabes algo. Úsalo siempre que necesites estimar el chance de un resultado que depende de dos o más cosas.

## Concepto (para no-experto)

Un **evento** es un resultado posible de algo incierto (ejemplo: "que un cliente compre", "que salga cara"). La **probabilidad** de un evento es un número entre 0 y 1 (o 0% a 100%) que mide qué tan probable es: 0 = imposible, 1 = seguro.

Tenemos cuatro reglas básicas para combinar eventos. Imagina una pizzería:

- **Complemento** — "lo contrario". Si la probabilidad de que un pedido llegue tarde es 0.20 (20%), entonces la de que NO llegue tarde es 1 − 0.20 = 0.80 (80%). Lo que pasa + lo que no pasa = 1 (algo tiene que ocurrir). Truco de oro: cuando piden "al menos uno", casi siempre es más fácil calcular "ninguno" y restar de 1.

- **Suma** — el "O" (que ocurra A **o** B). Sumas, pero si los dos pueden pasar a la vez tienes que **restar el solapamiento** para no contarlo dos veces. Ejemplo: clientes que piden bebida (B) o postre (P): si sumas ambos grupos, los que pidieron las dos cosas quedaron contados dos veces, así que los restas una vez.

- **Producto** — el "Y" (que ocurra A **y** B juntos). Multiplicas. Pero hay que tener cuidado: solo se multiplica directo si los eventos son **independientes**.

- **Probabilidad condicional** — "dado que ya sé algo". P(A | B) se lee "probabilidad de A *dado que* ocurrió B". Es recalcular la probabilidad cuando una información reduce el universo de casos posibles.

**Independientes vs dependientes** — Dos eventos son **independientes** si saber que uno ocurrió NO cambia la probabilidad del otro (dos lanzamientos de moneda: la primera no afecta a la segunda). Son **dependientes** cuando sí cambia (sacar dos cartas sin reponer: la primera carta cambia lo que queda en el mazo). Confundir estos dos casos es la fuente número uno de errores en probabilidad con dinero.

## Fórmulas / método

Notación: `P(A)` = probabilidad del evento A. `A∩B` = "A y B" (intersección). `A∪B` = "A o B" (unión). `A'` = complemento de A ("no A"). `P(A|B)` = A dado B.

- **Complemento:** `P(A') = 1 − P(A)`
- **Suma (regla general):** `P(A∪B) = P(A) + P(B) − P(A∩B)`
- **Suma (eventos mutuamente excluyentes**, no pueden ocurrir juntos, `P(A∩B)=0`**):** `P(A∪B) = P(A) + P(B)`
- **Condicional:** `P(A|B) = P(A∩B) / P(B)`, válida si `P(B) > 0`
- **Producto (regla general):** `P(A∩B) = P(B) · P(A|B)`
- **Producto (eventos independientes):** `P(A∩B) = P(A) · P(B)`
- **Definición de independencia:** A y B son independientes ⇔ `P(A|B) = P(A)` ⇔ `P(A∩B) = P(A)·P(B)`
- **"Al menos uno" de n eventos independientes:** `P(al menos uno) = 1 − ∏(1 − pᵢ)`

Todas las probabilidades son adimensionales (sin unidades), en el rango `[0, 1]`. Para expresar en porcentaje se multiplica por 100 (unidad: %).

## Verificación en código

```python
# Probabilidad EXACTA con fracciones (sin error de float).
from fractions import Fraction as F

# --- Datos de una pizzería (proporciones de pedidos) ---
P_B = F(60, 100)   # P(pide Bebida)
P_P = F(40, 100)   # P(pide Postre)
P_ByP = F(25, 100) # P(pide Bebida Y Postre) = solapamiento observado

# Regla del complemento
P_no_B = 1 - P_B
assert P_no_B == F(40, 100)

# Regla de la suma (general): P(B o P)
P_BoP = P_B + P_P - P_ByP
print("P(Bebida o Postre) =", P_BoP, "=", float(P_BoP))  # 75/100 = 0.75

# Probabilidad condicional: dado que pidió bebida, ¿pide postre?
P_P_dado_B = P_ByP / P_B
print("P(Postre | Bebida) =", P_P_dado_B, "=", float(P_P_dado_B))  # 5/12

# ¿Son independientes Bebida y Postre?  Independencia ⇔ P(B∩P)=P(B)·P(P)
print("Independientes?", P_ByP == P_B * P_P)  # 0.25 vs 0.24 -> False
```

```python
# ----- SEGUNDA VÍA: conteo directo sobre 10.000 pedidos (frecuencias enteras) -----
# Reconstruimos la tabla de contingencia con cuentas ENTERAS (nada de floats).
N = 10000
n_ByP   = 25 * N // 100      # 2500 piden ambos
n_B     = 60 * N // 100      # 6000 piden bebida (incluye los 2500)
n_P     = 40 * N // 100      # 4000 piden postre (incluye los 2500)
n_solo_B = n_B - n_ByP       # 3500 solo bebida
n_solo_P = n_P - n_ByP       # 1500 solo postre
n_BoP    = n_solo_B + n_ByP + n_solo_P   # 7500 piden bebida o postre

# Verificamos que la suma por conteo da lo mismo que la fórmula
assert F(n_BoP, N) == P_BoP                 # 7500/10000 = 75/100  OK
# Condicional por conteo: de los 6000 con bebida, ¿cuántos con postre?
assert F(n_ByP, n_B) == P_P_dado_B          # 2500/6000 = 5/12     OK
# Sanity check de orden de magnitud: P(B o P) debe estar entre max(P) y P_B+P_P
assert max(P_B, P_P) <= P_BoP <= P_B + P_P  # 0.60 <= 0.75 <= 1.00 OK
print("Verificacion por conteo entero: OK")
```

Las dos vías (fracciones simbólicas y conteo entero sobre 10.000 casos) coinciden: el resultado es exacto, no una aproximación.

## Ejemplo trabajado

**Problema (negocio LatAm).** Una tienda en Bogotá corre dos campañas de WhatsApp independientes. La campaña A convierte al 8% de quienes la reciben; la campaña B, al 5%. Un cliente recibe AMBAS. ¿Probabilidad de que compre por al menos una?

Definimos: `P(A) = 0.08`, `P(B) = 0.05`, independientes (campañas separadas, sin influirse).

Paso 1 — La trampa: NO es 0.08 + 0.05 = 0.13 directo, porque podría comprar por las dos y lo contaríamos doble. Usamos el complemento.

Paso 2 — Probabilidad de que NO compre por A: `1 − 0.08 = 0.92`. De que NO compre por B: `1 − 0.05 = 0.95`.

Paso 3 — Por independencia, NO compra por ninguna: `0.92 × 0.95 = 0.874`.

Paso 4 — Al menos una: `1 − 0.874 = 0.126`.

```python
from decimal import Decimal as D
pA, pB = D("0.08"), D("0.05")
p_ninguna = (1 - pA) * (1 - pB)          # 0.874
p_al_menos_una = 1 - p_ninguna           # 0.126
# Segunda via: suma general P(A)+P(B)-P(A)*P(B)  (independientes)
p_suma = pA + pB - pA*pB                  # 0.126
assert p_al_menos_una == p_suma
print(p_al_menos_una)  # 0.1260
```

**Resultado: 0.126 = 12.60%** de probabilidad de que compre por al menos una campaña (no 13%). Verificado por dos métodos que coinciden exactamente.

## Errores comunes / trampas

- **Sumar el "O" sin restar el solapamiento.** `P(A∪B) ≠ P(A)+P(B)` salvo que sean mutuamente excluyentes. Restar `P(A∩B)` siempre que A y B puedan ocurrir juntos.
- **Multiplicar como si fueran independientes cuando no lo son.** Sacar dos cartas, dos clientes del mismo segmento, dos eventos por la misma causa: usa `P(A∩B)=P(B)·P(A|B)`, no `P(A)·P(B)`.
- **Confundir P(A|B) con P(B|A).** "Probabilidad de tener la enfermedad dado que el test dio positivo" ≠ "probabilidad de positivo dado que estás enfermo". Son distintas (ver Bayes).
- **Probabilidades > 1.** Si una suma te da más de 1, casi seguro contaste doble o multiplicaste donde debías sumar. Es una alarma: revisa.
- **Olvidar el complemento en "al menos uno".** Calcular caso por caso explota; `1 − P(ninguno)` es exacto y simple.
- **Usar float para encadenar muchas multiplicaciones.** Acumula error; usa `Fraction` (exacto) o `Decimal` y redondea una sola vez al final.

## Cruces

- [[50-fundamentos-de-probabilidad.md]] — definición de evento, espacio muestral y la base de estas reglas.
- [[52-teorema-de-bayes.md]] — invertir condicionales: pasar de P(B|A) a P(A|B).
- [[53-combinatoria.md]] — contar casos favorables y totales para alimentar estas fórmulas.
- [[59-falacias-de-probabilidad.md]] — errores de razonamiento (independencia falsa, falacia del fiscal).
- [[03-protocolo-de-verificacion-por-codigo.md]] — el patrón ejecutar+verificar usado aquí.

---

**Mini-checklist de exactitud**
- [ ] ¿Toda probabilidad final quedó en `[0, 1]`? (si pasa de 1, hay doble conteo)
- [ ] ¿Verifiqué independencia con `P(A∩B)=P(A)·P(B)` antes de multiplicar directo?
- [ ] ¿Confirmé el resultado por una segunda vía (complemento, conteo entero o suma general)?
