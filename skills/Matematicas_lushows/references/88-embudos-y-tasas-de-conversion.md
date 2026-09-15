# 88 · Embudos y tasas de conversión

> **Qué resuelve / cuándo usarlo** — Calcular cuánta gente avanza de una etapa de venta a la siguiente, cuántos *leads* (contactos interesados) necesitas para lograr X ventas, y dónde exactamente se está fugando tu dinero en el camino.

## Concepto (para no-experto)

Un **embudo de ventas** (en inglés *funnel*) es la representación del recorrido de un cliente desde que te conoce hasta que te compra. Se llama "embudo" porque tiene forma de cono: entra mucha gente arriba y sale poca abajo. Igual que un embudo de cocina, donde echas mucho líquido por la boca ancha y sale un hilito por el pico.

Definamos los términos básicos la primera vez:

- **Etapa**: cada escalón del recorrido. Ejemplo de un bot de WhatsApp: *Visitas al anuncio → Clics → Conversaciones iniciadas → Interesados → Compras*.
- **Volumen de la etapa**: cuántas personas hay en ese escalón (un conteo, sin unidad de dinero, solo "personas").
- **Tasa de conversión de una etapa** (en inglés *conversion rate*): qué fracción de la gente de un escalón pasa al siguiente. Es un número entre 0 y 1 (o un porcentaje entre 0% y 100%). Si de 100 conversaciones, 20 terminan en interés, la tasa de esa etapa es 20/100 = 0,20 = 20%.
- **Conversión compuesta** (o *end-to-end*): qué fracción del total que entró arriba llega hasta el final. NO es la suma ni el promedio de las tasas: es el **producto** (la multiplicación) de todas las tasas por etapa. Esto es lo que más se equivoca la gente.

Analogía: imagina tres filtros de café apilados. Si cada filtro deja pasar la mitad del agua, después de los tres no pasa "la mitad", pasa la mitad de la mitad de la mitad = 1/8. Las conversiones se **multiplican**, no se suman.

## Fórmulas / método

Sea un embudo con etapas con volúmenes $V_0, V_1, V_2, \dots, V_n$ (personas), donde $V_0$ es la entrada y $V_n$ la última (ventas).

**Tasa de conversión de la etapa $i$ (paso $V_{i-1}\to V_i$):**

$$ r_i = \frac{V_i}{V_{i-1}} \quad (\text{adimensional, } 0 \le r_i \le 1) $$

**Conversión compuesta (de la primera a la última etapa):**

$$ R = \frac{V_n}{V_0} = r_1 \cdot r_2 \cdots r_n = \prod_{i=1}^{n} r_i $$

**Leads necesarios para lograr $V_n^{*}$ ventas** (despeje de la fórmula anterior):

$$ V_0^{*} = \frac{V_n^{*}}{R} = \frac{V_n^{*}}{\prod_{i=1}^{n} r_i} $$

**Pérdida absoluta en una etapa** (personas que se caen) y **pérdida relativa**:

$$ \text{Pérdida}_i = V_{i-1} - V_i \quad (\text{personas}) \qquad \text{Fuga}_i = 1 - r_i $$

**Dónde se pierde más (impacto absoluto):** la etapa con mayor $\text{Pérdida}_i$ es donde más volumen se cae; pero la etapa con menor $r_i$ es el "cuello de botella" relativo. Hay que mirar las dos cosas: a veces una etapa con buena tasa pierde más personas simplemente porque recibe mucho volumen.

Unidades: los $V_i$ van en **personas** (o sesiones, conversaciones, según lo que cuentes); las tasas $r_i$ y $R$ son **adimensionales** (proporciones). El dinero solo aparece cuando se cruza con costo por lead o ticket (ver Cruces).

## Verificación en código

```python
from decimal import Decimal, getcontext, ROUND_HALF_UP
from functools import reduce

getcontext().prec = 28  # alta precisión para no arrastrar error

# Embudo real de un bot de WhatsApp (GastroLatam, números de ejemplo).
# Volúmenes por etapa, en PERSONAS (conteos enteros).
etapas = ["Clics anuncio", "Conversaciones", "Interesados", "Ventas"]
V = [Decimal(1000), Decimal(420), Decimal(126), Decimal(38)]

# --- Tasa por etapa: r_i = V_i / V_{i-1} ---
tasas = [V[i] / V[i-1] for i in range(1, len(V))]
for i, r in enumerate(tasas, start=1):
    print(f"{etapas[i-1]:>14} -> {etapas[i]:<14}: r = {r:.4f}  ({r*100:.2f}%)")

# --- Conversión compuesta: producto de las tasas ---
R = reduce(lambda a, b: a * b, tasas, Decimal(1))
print(f"\nConversion compuesta R = {R:.6f}  ({R*100:.3f}%)")

# --- Leads necesarios para una meta de ventas ---
meta_ventas = Decimal(100)
leads_necesarios = (meta_ventas / R).to_integral_value(rounding=ROUND_HALF_UP)
print(f"Para {meta_ventas} ventas necesito {leads_necesarios} clics de entrada")

# --- Donde se pierde (perdida absoluta por etapa) ---
print("\nFugas por etapa:")
for i in range(1, len(V)):
    perdida = V[i-1] - V[i]
    fuga = 1 - tasas[i-1]
    print(f"  {etapas[i-1]:>14} -> {etapas[i]:<14}: "
          f"caen {perdida} personas  (fuga {fuga*100:.2f}%)")

# ===================== VERIFICACIÓN POR SEGUNDA VÍA =====================
# Vía 1 (directa): R = V_n / V_0  debe coincidir con el producto de tasas.
R_directa = V[-1] / V[0]
assert R == R_directa, f"Discrepancia: {R} vs {R_directa}"

# Vía 2 (reconstrucción): aplicar las tasas sobre V_0 debe devolver V_n.
v_reconstruido = V[0]
for r in tasas:
    v_reconstruido *= r
assert v_reconstruido == V[-1], "La cadena de tasas no reproduce las ventas"

# Vía 3 (sanity de leads): meta / R, redondeado, * R debe rondar la meta.
chequeo = leads_necesarios * R
assert abs(chequeo - meta_ventas) < Decimal("1"), "Leads necesarios mal despejados"

print("\nOK: las tres vías de verificacion coinciden.")
```

Salida esperada (resumen): $r_1=0{,}42$, $r_2=0{,}30$, $r_3 \approx 0{,}3016$; conversión compuesta $R = 38/1000 = 0{,}038 = 3{,}8\%$; para 100 ventas se necesitan $\lceil 100/0{,}038 \rceil = 2632$ clics.

La verificación es robusta porque: (Vía 1) confirma que el producto de tasas es idéntico al cociente extremo $V_n/V_0$ — si me equivoco en una tasa, no cuadran; (Vía 2) reconstruye las ventas multiplicando paso a paso; (Vía 3) comprueba que el despeje de "leads necesarios" es coherente al re-multiplicar por $R$.

## Ejemplo trabajado

**Situación (LatAm):** un anuncio de Meta Ads para el bot de WhatsApp de GastroLatam genera **1.000 clics** en una semana. De esos, **420** inician conversación, **126** muestran interés real y **38** compran la Calculadora de Costos ($10.000 COP cada una).

**Paso 1 — tasas por etapa (adimensionales):**
- Clic → Conversación: $r_1 = 420/1000 = 0{,}42$ (42%)
- Conversación → Interesado: $r_2 = 126/420 = 0{,}30$ (30%)
- Interesado → Venta: $r_3 = 38/126 = 0{,}30159\ldots$ (≈30,16%)

**Paso 2 — conversión compuesta:**
$$R = 0{,}42 \times 0{,}30 \times 0{,}30159 = 0{,}038 = 3{,}8\%$$
Comprobación directa: $38/1000 = 0{,}038$. ✓ Coincide.

**Paso 3 — leads para una meta de 100 ventas:**
$$V_0^{*} = 100 / 0{,}038 = 2631{,}6 \Rightarrow 2632 \text{ clics}$$ (redondeo al entero superior: no puedes "comprar" 0,6 de un clic, y si quieres *al menos* 100 ventas debes redondear hacia arriba).

**Paso 4 — dónde se pierde más (en personas):**
- Clic → Conversación: caen **580** personas (la mayor fuga absoluta).
- Conversación → Interesado: caen 294.
- Interesado → Venta: caen 88.

**Lectura del negocio:** la mayor sangría está al inicio (580 de cada 1.000 clics nunca escriben). Mejorar ese primer paso de 42% a 55% subiría la conversión compuesta a $0{,}55\times0{,}30\times0{,}30159 = 0{,}0498 \approx 5{,}0\%$, es decir pasar de 38 a ~50 ventas con el **mismo** gasto en anuncios. Ese es el punto de mayor apalancamiento, **con unidades: +12 ventas/semana sin gastar un peso más en pauta.**

## Errores comunes / trampas

- **Sumar o promediar tasas en vez de multiplicarlas.** La conversión total NO es $(42+30+30)/3$. Es el producto. Promediar infla el resultado de forma absurda.
- **Usar `float` para los conteos o tasas y arrastrar error.** Usa `decimal` o `fractions`; redondea **una sola vez al final** (ver [[05-cifras-significativas-y-redondeo.md]]).
- **Redondear "leads necesarios" hacia abajo.** Si necesitas *al menos* X ventas, redondea hacia arriba ($\lceil\cdot\rceil$); si redondeas a la baja te quedas corto.
- **Confundir fuga relativa con pérdida absoluta.** Una etapa con tasa baja (30%) puede caer menos personas que una con tasa alta (42%) si recibe poco volumen. Mira ambas: $r_i$ (cuello de botella) y $V_{i-1}-V_i$ (volumen perdido).
- **Comparar tasas de períodos con denominadores distintos** sin normalizar (ventas/clics de una semana de 1.000 clics vs otra de 200). Compara siempre proporciones, no conteos crudos.
- **Doble conteo o etapas no excluyentes:** si alguien puede estar en dos etapas a la vez, las tasas mienten. Cada persona debe contarse en una sola etapa por período.
- **Tomar decisiones con muestras minúsculas.** 38 ventas tiene mucha incertidumbre; antes de "optimizar" verifica significancia (ver [[68-ab-testing.md]] e [[66-intervalos-de-confianza.md]]).

## Cruces

- [[14-porcentajes-sin-errores.md]] — toda tasa de conversión es un porcentaje; base correcta.
- [[83-cac-ltv-y-payback.md]] — cruzar la conversión con costo por lead da el CAC real.
- [[84-roi-roas-y-mer.md]] — la conversión del embudo alimenta el ROAS de la pauta.
- [[86-forecasting-y-proyeccion.md]] — proyectar ventas multiplicando leads esperados por $R$.
- [[68-ab-testing.md]] — validar estadísticamente si una mejora de tasa es real o ruido.

---

**Mini-checklist de exactitud**
1. ¿Multipliqué las tasas (no las sumé) y $R = V_n/V_0$ coincide con el producto?
2. ¿Conteos en `decimal`/enteros, redondeo solo al final, leads hacia arriba?
3. ¿Revisé ambas: cuello de botella ($r_i$ mínimo) y mayor pérdida absoluta ($V_{i-1}-V_i$)?
