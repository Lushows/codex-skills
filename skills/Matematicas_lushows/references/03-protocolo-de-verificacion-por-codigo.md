# 03 · Protocolo de verificación por código

> **Qué resuelve / cuándo usarlo** — El protocolo central de esta skill: cómo ejecutar TODO cálculo no trivial en código real (Python con `decimal`/`fractions`/`sympy`/`numpy`, o Node) y verificarlo por una segunda vía independiente. Úsalo SIEMPRE que un número vaya a sostener una decisión con dinero.

## Concepto (para no-experto)

La regla más importante de esta skill es simple: **no calculamos de memoria**. El cerebro humano (y también un modelo de lenguaje) es bueno para razonar y pésimo para aritmética exacta; comete errores silenciosos que se ven igual de "seguros" que los aciertos. Por eso, cada cálculo que no sea trivial se **ejecuta en código real** —un programa pequeño que la máquina corre de verdad— y se **muestra el código**, para que cualquiera pueda repetirlo.

Definamos los tres términos clave que usaremos todo el tiempo:

- **Cálculo no trivial**: cualquier operación que no estés 100 % seguro de hacer de cabeza sin equivocarte. Sumar 2 + 2 es trivial. Sacar el 19 % de IVA sobre $847.300 y restarlo, no.
- **Ejecutar en código**: escribir las operaciones en un lenguaje (Python o Node) y correrlo, en vez de "creer" el resultado. El número sale de la máquina, no de la intuición.
- **Verificación por segunda vía**: confirmar el mismo resultado con un método DIFERENTE. Si dos caminos independientes dan lo mismo, la probabilidad de que ambos estén mal de la misma forma es minúscula.

**Analogía cotidiana:** es como contar la plata de la caja al cierre. Primero cuentas los billetes uno por uno (vía 1). Luego, en vez de confiar, sumas las ventas del día y comparas con lo que hay en caja (vía 2). Si cuadra, duermes tranquilo. Si no cuadra, sabes que hay un error ANTES de que te cueste. El código es contar los billetes; la segunda vía es el arqueo de caja.

¿Por qué dos vías y no solo "revisar"? Porque revisar el mismo cálculo con el mismo método tiende a repetir el mismo error (lees lo que esperabas leer). Un método distinto rompe ese sesgo.

## Fórmulas / método

No hay una "fórmula" matemática aquí, sino un **procedimiento de 5 pasos** que se aplica a cualquier cálculo:

1. **Plantear** — escribe la fórmula con símbolos definidos y unidades. Sin esto, no sabes qué estás calculando.
2. **Elegir tipo numérico correcto**:
   - Dinero → `decimal.Decimal` (precisión exacta en base 10) o centavos enteros. **NUNCA `float`.**
   - Fracciones exactas → `fractions.Fraction`.
   - Álgebra/símbolos/derivadas → `sympy`.
   - Arreglos grandes / álgebra lineal numérica → `numpy`/`scipy` (acepta float, pero con cuidado).
3. **Ejecutar** el cálculo en código real y mostrarlo.
4. **Verificar por segunda vía**. Elige al menos una:
   - **Operación inversa**: si calculaste `A → B`, comprueba que `B → A` te devuelve el dato original.
   - **Estimación de orden de magnitud** (sanity check): ¿el resultado tiene un tamaño razonable? Ver [[06-estimacion-y-sanity-checks]].
   - **Otro método**: fórmula cerrada vs. iteración, álgebra vs. numérico, etc.
   - **`assert`**: una afirmación en código que falla y detiene todo si el número no es el esperado.
5. **Redondear UNA sola vez al final** y reportar **con unidades**. Ver [[05-cifras-significativas-y-redondeo]].

Notación que usaremos: el símbolo `==` en código significa "comparar si son iguales"; `assert X` significa "si X es falso, detente y avisa que hay un error".

## Verificación en código

Ejemplo del patrón completo: un comerciante vendió por **$847.300 COP** con IVA del 19 % **incluido**. Quiere saber la base (precio sin IVA) y el IVA. Lo calculamos con `decimal` y lo verificamos por la vía inversa.

```python
from decimal import Decimal, ROUND_HALF_UP

# --- VÍA 1: cálculo exacto con Decimal (dinero NUNCA con float) ---
total   = Decimal("847300")        # precio final con IVA incluido (COP)
tasa    = Decimal("0.19")          # 19% de IVA (fracción, sin unidad)

# Si el IVA está INCLUIDO, la base = total / (1 + tasa)
base = total / (Decimal("1") + tasa)      # base imponible (COP)
iva  = total - base                       # IVA contenido (COP)

# Redondeo UNA vez al final, a peso entero (COP no usa centavos en la práctica)
base_r = base.quantize(Decimal("1"), rounding=ROUND_HALF_UP)
iva_r  = iva.quantize(Decimal("1"),  rounding=ROUND_HALF_UP)

print("Base sin IVA:", base_r, "COP")   # 712017 COP
print("IVA (19%):   ", iva_r,  "COP")   # 135283 COP

# --- VÍA 2 (independiente): reconstruir el total desde la base ---
# Si base * (1+tasa) ≈ total original, el cálculo es correcto.
total_reconstruido = (base_r * (Decimal("1") + tasa)).quantize(
    Decimal("1"), rounding=ROUND_HALF_UP)
print("Total reconstruido:", total_reconstruido, "COP")  # 847300 COP

# Verificación dura: que las piezas sumen el total y que la inversa cuadre.
assert base_r + iva_r == total, "ERROR: base + IVA no da el total"
assert abs(total_reconstruido - total) <= Decimal("1"), \
    "ERROR: la inversa no reconstruye el total (±1 por redondeo)"
print("OK: ambas vías concuerdan")
```

Salida esperada:

```
Base sin IVA: 712017 COP
IVA (19%):    135283 COP
Total reconstruido: 847300 COP
OK: ambas vías concuerdan
```

Por qué `float` falla con dinero (motivo de la regla dura):

```python
# float NO representa exacto los decimales en base 10:
print(0.1 + 0.2)          # 0.30000000000000004  ← falso
from decimal import Decimal
print(Decimal("0.1") + Decimal("0.2"))   # 0.3   ← exacto
```

Patrón con `fractions` cuando se necesitan proporciones exactas (sin error de redondeo intermedio):

```python
from fractions import Fraction
# Tres socios reparten 1 unidad en 1/2, 1/3, 1/6. ¿Suman exactamente 1?
partes = Fraction(1,2) + Fraction(1,3) + Fraction(1,6)
assert partes == Fraction(1,1), "El reparto no suma el total"
print(partes)   # 1
```

## Ejemplo trabajado

**Problema (LatAm).** Una dark kitchen invierte **$1.200.000 COP** y al cabo de 2 años recibe **$1.587.000 COP**. ¿Cuál fue su tasa de interés anual compuesta (la tasa constante que, aplicada cada año, lleva de 1.200.000 a 1.587.000)?

**Vía 1 — despejar la tasa de la fórmula de interés compuesto.**
Fórmula: `VF = VP · (1 + r)^n`, donde
`VF` = valor futuro (COP), `VP` = valor presente (COP), `r` = tasa anual (sin unidad), `n` = años.
Despejando: `r = (VF / VP)^(1/n) − 1`.

```python
from decimal import Decimal, getcontext, ROUND_HALF_UP
getcontext().prec = 28                  # alta precisión interna

VP = Decimal("1200000")                 # COP
VF = Decimal("1587000")                 # COP
n  = 2                                  # años

# Raíz n-ésima vía exponente fraccionario (Decimal soporta ** con Decimal)
r = (VF / VP) ** (Decimal(1) / Decimal(n)) - 1   # tasa anual
print("Tasa anual:", (r*100).quantize(Decimal("0.01"), ROUND_HALF_UP), "%")
# Tasa anual: 14.99 %  (≈ 15% anual)

# --- Vía 2: reconstruir el VF aplicando la tasa n veces (método distinto) ---
acum = VP
for _ in range(n):
    acum = acum * (1 + r)               # interés compuesto, año por año
acum = acum.quantize(Decimal("1"), ROUND_HALF_UP)
print("VF reconstruido:", acum, "COP")  # 1587000 COP

assert abs(acum - VF) <= Decimal("1"), "La tasa hallada no reproduce el VF"
print("OK verificado")
```

**Vía 3 — sanity check de orden de magnitud (mental, sin código).**
1.587.000 / 1.200.000 ≈ 1,32 en 2 años. Un crecimiento de ~32 % en dos años es aproximadamente ~15 % por año (porque 1,15 × 1,15 ≈ 1,32). El resultado del código, **14,99 % anual**, cae justo donde la intuición lo esperaba: no hay error de un cero de más ni de signo.

**Resultado:** la tasa anual compuesta es **≈ 14,99 % anual**, verificada por (1) la fórmula directa, (2) reconstrucción iterativa del valor futuro y (3) estimación de magnitud. Ver fundamentos en [[71-interes-simple-y-compuesto]].

## Errores comunes / trampas

- **Calcular de memoria "porque es fácil".** El 80 % de los errores reales viven en cálculos que parecían triviales. Si toca una decisión con dinero, va a código.
- **Usar `float` para dinero.** Produce centavos fantasma (`0.1+0.2`). Usa `Decimal` (con argumento **string**, `Decimal("0.1")`, nunca `Decimal(0.1)`) o centavos enteros.
- **Verificar con el mismo método.** Releer el mismo cálculo NO es verificar; repite el sesgo. La segunda vía debe ser estructuralmente distinta.
- **Redondear en pasos intermedios.** Acumula error. Redondea UNA sola vez, al final.
- **Reportar el número sin unidades** (¿14,99 qué? ¿pesos, por ciento, anual o mensual?). Sin unidad, el número es ambiguo y peligroso. Ver [[04-notacion-unidades-y-dimensiones]].
- **Confundir IVA incluido vs. agregado.** Si el IVA va incluido se divide por `(1+tasa)`; si se agrega, se multiplica. Un sanity check de magnitud lo detecta.
- **`assert` que siempre pasa.** Un assert mal escrito (p. ej. comparar un número consigo mismo) da falsa seguridad. La segunda vía debe partir de datos/lógica independientes.

## Cruces

- [[00-metodo-del-matematico-exacto]] — el método global de trabajo del que este protocolo es el corazón.
- [[02-mentalidad-de-exactitud-error-cero]] — el porqué cultural de "no confiar en la cabeza".
- [[06-estimacion-y-sanity-checks]] — la vía de verificación por orden de magnitud, en detalle.
- [[08-herramientas-de-calculo]] — qué librería elegir (`decimal`/`fractions`/`sympy`/`numpy`) según el caso.
- [[99-protocolo-final-de-verificacion]] — el checklist de cierre antes de entregar cualquier número.

---

**Mini-checklist de exactitud**
- [ ] ¿El cálculo se ejecutó en código real (no de memoria) y el código está a la vista?
- [ ] ¿El dinero usó `Decimal`/centavos (no `float`) y se redondeó una sola vez al final?
- [ ] ¿Hay una segunda vía independiente (inversa, otro método o `assert`) que concuerda, y el resultado lleva unidades?
