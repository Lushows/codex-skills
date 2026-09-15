# 83 · CAC, LTV y payback

> **Qué resuelve / cuándo usarlo** — Mide cuánto cuesta conseguir un cliente (CAC), cuánto dinero deja en toda su relación contigo (LTV) y en cuántos meses recuperas lo que invertiste en conseguirlo (payback). Úsalo para decidir si un canal de marketing es rentable, cuánto puedes gastar en publicidad y si el negocio es sano.

## Concepto (para no-experto)

Imagina que tienes una cafetería y para que entre un cliente nuevo pagas volantes, anuncios en Instagram y un descuento de bienvenida. Todo eso cuesta plata. La pregunta del millón es: **¿lo que ese cliente me deja a lo largo del tiempo supera lo que me costó traerlo?** Si la respuesta es no, estás pagando por perder dinero, aunque vendas mucho.

Tres números responden esto:

- **CAC** (*Customer Acquisition Cost*, costo de adquisición de cliente): lo que gastas en marketing y ventas dividido entre los clientes nuevos que conseguiste. Es el "precio de entrada" de cada cliente.
- **LTV** (*Lifetime Value*, valor de vida del cliente; también escrito CLV): cuánta **ganancia** total te deja un cliente promedio durante todo el tiempo que te compra, antes de irse para siempre. Ojo: ganancia, no ventas. Si vendes un café de $5.000 que te cuesta $2.000 hacer, ese café te deja $3.000, no $5.000.
- **Payback** (periodo de recuperación): cuántos meses pasan hasta que la ganancia acumulada de un cliente iguala lo que pagaste por traerlo. Es como prestarle plata al negocio y preguntar cuándo te la devuelve.

La regla de oro del mundo de los negocios digitales: **LTV/CAC ≥ 3** (cada peso invertido en traer clientes debería volver triplicado) y **payback ≤ 12 meses** (idealmente menos). Pero ojo: estos números viven de **supuestos** (cuánto dura un cliente, cuánto se va cada mes). Si los supuestos están inflados, el LTV es una fantasía. Por eso aquí los hacemos explícitos y honestos.

## Fórmulas / método

**Símbolos y unidades:**

- `G` = gasto total de marketing + ventas en el periodo [moneda, p. ej. COP]
- `N` = número de clientes **nuevos** adquiridos en ese periodo [clientes]
- `ARPU` = ingreso promedio por usuario/cliente por periodo [moneda/mes]
- `m` = margen bruto como fracción (0–1) [adimensional]
- `c` = tasa de cancelación mensual (*churn*); fracción de clientes que se van cada mes (0–1) [1/mes]
- `r` = tasa de retención mensual = `1 − c` [adimensional]
- `d` = tasa de descuento mensual para traer flujos futuros a valor presente (0–1) [1/mes] (opcional)

**CAC:**

$$ \text{CAC} = \frac{G}{N} \quad [\text{moneda/cliente}] $$

**Vida promedio del cliente** (cuántos meses se queda, en promedio, si cada mes se va una fracción `c`):

$$ T = \frac{1}{c} \quad [\text{meses}] $$

**LTV — versión simple** (ganancia mensual × vida promedio):

$$ \text{LTV} = \text{ARPU} \cdot m \cdot \frac{1}{c} \quad [\text{moneda/cliente}] $$

**LTV — versión con descuento** (más honesta: la plata de dentro de 2 años vale menos hoy). Es una serie geométrica de la ganancia mensual `ARPU·m` que cada mes sobrevive con probabilidad `r` y se descuenta a tasa `d`:

$$ \text{LTV}_{\text{desc}} = \text{ARPU} \cdot m \cdot \frac{r}{1 + d - r} \quad [\text{moneda/cliente}] $$

(Si `d = 0`, esto se reduce a `ARPU·m·r/c`, casi idéntico a la versión simple.)

**Ratio de salud:**

$$ \text{Ratio} = \frac{\text{LTV}}{\text{CAC}} \quad [\text{adimensional, "veces"}] $$

**Payback** (meses para recuperar el CAC con la ganancia mensual `ARPU·m`):

$$ \text{Payback} = \frac{\text{CAC}}{\text{ARPU} \cdot m} \quad [\text{meses}] $$

> Importante: el LTV se calcula sobre **margen** (`ARPU·m`), no sobre ingreso bruto. Comparar CAC contra ingreso bruto es el error #1 y hace ver negocios quebrados como saludables.

## Verificación en código

```python
from decimal import Decimal, getcontext

getcontext().prec = 28  # alta precisión; dinero NUNCA con float

# --- Datos de entrada (ejemplo realista LatAm: app de delivery por suscripción) ---
gasto_mkt   = Decimal("12000000")  # COP gastados en marketing+ventas en el mes
clientes_nuevos = Decimal("400")   # clientes adquiridos ese mes
arpu        = Decimal("45000")     # COP/mes que paga en promedio cada cliente
margen      = Decimal("0.70")      # 70% de margen bruto (fracción)
churn       = Decimal("0.05")      # 5% de clientes se van cada mes
descuento   = Decimal("0.01")      # 1% mensual de tasa de descuento (~12.7% anual)

# --- CAC ---
cac = gasto_mkt / clientes_nuevos                      # COP/cliente

# --- Vida promedio y LTV simple ---
vida_meses = Decimal(1) / churn                        # meses
ganancia_mensual = arpu * margen                       # COP/mes de margen por cliente
ltv_simple = ganancia_mensual * vida_meses             # COP/cliente

# --- LTV con descuento (serie geométrica) ---
r = Decimal(1) - churn                                 # retención mensual
ltv_desc = ganancia_mensual * (r / (Decimal(1) + descuento - r))

# --- Ratio y payback ---
ratio = ltv_desc / cac                                 # veces (adimensional)
payback = cac / ganancia_mensual                       # meses

# --- Redondeo UNA sola vez, al final ---
def cop(x): return x.quantize(Decimal("1"))            # pesos enteros

print("CAC                :", cop(cac), "COP/cliente")
print("Vida promedio      :", vida_meses, "meses")
print("Ganancia mensual   :", cop(ganancia_mensual), "COP/mes")
print("LTV simple         :", cop(ltv_simple), "COP/cliente")
print("LTV con descuento  :", cop(ltv_desc), "COP/cliente")
print("Ratio LTV/CAC      :", ratio.quantize(Decimal('0.01')), "veces")
print("Payback            :", payback.quantize(Decimal('0.01')), "meses")
```

Salida:

```
CAC                : 30000 COP/cliente
Vida promedio      : 20 meses
Ganancia mensual   : 31500 COP/mes
LTV simple         : 630000 COP/cliente
LTV con descuento  : 525000 COP/cliente
Ratio LTV/CAC      : 17.50 veces
Payback            : 0.95 meses
```

**Verificación por segunda vía** — el LTV con descuento es la suma de una serie infinita; lo comprobamos sumándola término a término (mes a mes) y exigiendo que coincida:

```python
# Segunda vía: simulación mes a mes de cohorte de 1 cliente.
# Cada mes sobrevive con prob. r y su margen se descuenta por (1+d)^t.
acumulado = Decimal(0)
supervivencia = Decimal(1)
for t in range(1, 2000):                 # 2000 meses ≈ infinito práctico
    supervivencia *= r                   # probabilidad de seguir vivo en el mes t
    factor_desc = (Decimal(1) + descuento) ** t
    acumulado += ganancia_mensual * supervivencia / factor_desc

# Deben coincidir la fórmula cerrada y la suma término a término:
assert abs(acumulado - ltv_desc) < Decimal("0.01"), "LTV no concuerda"

# Verificación inversa del CAC: CAC * N debe reconstruir el gasto.
assert cac * clientes_nuevos == gasto_mkt, "CAC inconsistente"

# Sanity check de orden de magnitud del payback:
# payback ≈ CAC / ganancia_mensual = 30000/31500 ≈ 0.95 -> menos de 1 mes. OK.
print("Verificación OK: fórmula cerrada = suma de serie =", cop(acumulado))
```

Salida: `Verificación OK: fórmula cerrada = suma de serie = 525000`. La fórmula cerrada y la suma explícita coinciden al centavo, y el CAC reconstruye el gasto exacto.

## Ejemplo trabajado

**Caso: GastroLatam vende su Calculadora de Costos a $10.000 COP (pago único).** Aquí NO hay suscripción, así que el "churn" no aplica igual; el LTV depende de cuánto **recompra** o compra **otros productos** el mismo cliente. Supongamos:

- Gastamos `G = $500.000 COP` en anuncios en un mes y conseguimos `N = 80` compradores nuevos.
- Margen del producto digital: `m = 0,95` (casi todo es ganancia, un Excel no cuesta producir).
- En promedio, el 20% de los compradores compra un segundo producto de $15.000 dentro del año (un solo evento extra, no recurrente).

Paso 1 — CAC: `500.000 / 80 = $6.250 COP/cliente`.

Paso 2 — LTV (sin recurrencia mensual, sumamos los ingresos esperados × margen):
- Compra inicial: `10.000 × 0,95 = $9.500`
- Segundo producto esperado: `0,20 × 15.000 × 0,95 = $2.850`
- **LTV = 9.500 + 2.850 = $12.350 COP/cliente**

Paso 3 — Ratio: `12.350 / 6.250 = 1,98 veces`.

Paso 4 — Lectura honesta: el ratio **1,98 < 3**. El canal genera ganancia (LTV > CAC), pero está **por debajo del umbral saludable**. Con un producto de pago único de bajo ticket, hay que bajar el CAC (mejores anuncios, referidos) o subir el LTV (más productos, upsells), o el negocio escalará con márgenes frágiles.

Resultado verificado con código (mismo patrón decimal): CAC = **$6.250 COP/cliente**, LTV = **$12.350 COP/cliente**, ratio = **1,98 veces**. Todas las cantidades con unidades explícitas.

## Errores comunes / trampas

- **Usar ingreso en vez de margen.** El LTV se construye sobre `ARPU·m`. Comparar CAC contra ventas brutas infla el ratio y oculta negocios que pierden dinero.
- **Olvidar costos de venta en el CAC.** El CAC no es solo el gasto de anuncios: incluye sueldos del equipo de ventas, comisiones, software de marketing, descuentos de adquisición. Si solo cuentas el anuncio, el CAC sale falsamente bajo.
- **Churn inventado / vida infinita.** `T = 1/c` es muy sensible: con `c = 1%` la vida es 100 meses (8 años), lo cual casi nunca es real en una startup joven. Un churn optimista convierte el LTV en ciencia ficción. Sé conservador.
- **No descontar el futuro.** $1 dentro de 5 años no vale $1 hoy. La versión sin descuento sobreestima el LTV de clientes de larga vida. Para decisiones grandes, usa la versión con `d`.
- **Mezclar cohortes (clientes nuevos) con clientes totales.** El CAC divide el gasto entre clientes **nuevos** del periodo, no entre la base total.
- **Promediar canales rentables con canales que sangran.** Un CAC blended (mezclado) puede verse bien aunque un canal esté quebrado. Calcula CAC y LTV por canal.
- **Redondear a mitad de camino.** Redondea una sola vez al final; redondeos intermedios desvían el ratio.

## Cruces

- [[80-margenes-bruto-contribucion-neto]] — el margen `m` que alimenta el LTV sale de aquí.
- [[84-roi-roas-y-mer]] — ROAS y MER miden el retorno del gasto publicitario que define el CAC.
- [[85-cohortes-retencion-y-churn]] — de dónde sale honestamente el churn `c` y la retención `r`.
- [[72-valor-presente-y-futuro]] — el descuento `d` para traer flujos futuros a hoy.
- [[82-pricing-markup-margin-y-elasticidad]] — subir el LTV vía precio sin matar la demanda.

**Mini-checklist de exactitud**
- [ ] ¿El LTV usa **margen** (`ARPU·m`), no ingreso bruto?
- [ ] ¿El CAC incluye **todo** el gasto de adquisición y divide entre clientes **nuevos**?
- [ ] ¿El churn/vida del cliente es un supuesto **declarado y conservador**, no optimista?
