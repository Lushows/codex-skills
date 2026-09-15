# 102 — Playbook: SaaS y software

Cómo entender y construir un negocio de **software por suscripción** (SaaS = Software as a Service: el cliente paga mes a mes o año a año por usar tu programa en la nube, no lo compra una sola vez). Aquí está la economía real del negocio, los números que importan y cómo arrancar sin quebrar.

## Por qué el SaaS enamora (y por qué engaña)
La promesa: vendes una vez y cobras para siempre (ingresos recurrentes). Márgenes altísimos, escala casi infinita, valoraciones altas. La trampa: **el cliente también se va para siempre cuando se va** (churn), y si construyes antes de validar, gastas meses programando algo que nadie quiere pagar. El SaaS premia la retención, no la programación bonita.

## Vocabulario que SÍ debes dominar (define cada término)
- **MRR** (Monthly Recurring Revenue): ingreso recurrente mensual. Suma de lo que pagan TODOS tus clientes activos en un mes.
- **ARR** (Annual Recurring Revenue): MRR × 12. El "tamaño" anual de tu negocio recurrente.
- **Churn**: % de clientes (o de ingreso) que cancelan en un periodo. Churn de clientes ≠ churn de ingresos.
- **NRR** (Net Revenue Retention): de los clientes que ya tenías, cuánto ingreso conservas tras 12 meses, contando upgrades menos bajas. >100% = creces SOLO con tus clientes actuales (santo grial).
- **CAC** (Costo de Adquisición de Cliente): cuánto te cuesta conseguir UN cliente que paga (ver 52).
- **LTV** (Lifetime Value): cuánto dinero deja un cliente en toda su vida contigo (ver 52).
- **Payback**: cuántos MESES tardas en recuperar el CAC con lo que paga el cliente.
- **Regla del 40**: (crecimiento % anual) + (margen % de beneficio) ≥ 40 es señal de un SaaS sano. Si creces rápido puedes perder algo; si creces lento debes ser rentable.

## Modelos: ¿quién paga y cómo llega?
| Eje | Opción A | Opción B |
|---|---|---|
| Cliente | **B2B** (empresas): ticket alto, ventas más largas, menos clientes | **B2C** (personas): ticket bajo, volumen, churn más alto |
| Entrada al mercado | **PLG** (Product-Led Growth: el producto se vende solo con prueba gratis/freemium) | **Sales-led** (vendedores cierran cuentas grandes) |

Regla práctica: precio mensual bajo (< ~50 USD/mes) casi obliga a PLG (no puedes pagar un vendedor por cliente). Ticket alto (> ~500 USD/mes) suele necesitar sales-led. **Pregunta país/ciudad primero**: poder adquisitivo, medios de pago (tarjeta vs PSE/Nequi/transferencia) y si las empresas locales compran software en la nube cambian todo.

## KPIs clave del sector (los 5 que importan)
1. **MRR** y su crecimiento mes a mes (% MoM).
2. **Churn mensual** (objetivo orientativo: B2C < 5%/mes, B2B < 2%/mes; varía mucho).
3. **LTV:CAC** — sano ≥ 3:1 (ganas 3 veces lo que cuesta traer al cliente).
4. **Payback** — sano < 12 meses (idealmente < 6 en B2C).
5. **NRR** — bueno ≥ 100%; excelente ≥ 110%.

## Capital típico de arranque (orientativo, NO dato duro)
- **MVP solo o con un socio técnico**: puede ser muy bajo (dominio + hosting + herramientas no-code/cloud: rango orientativo 0–500 USD/mes mientras validas).
- **Equipo pequeño contratado** para construir: sube a miles de USD/mes en salarios (el costo real depende del país — verifica salarios locales, ver 21 para datos reales).
- Clave: el gasto grande NO es servidores, es **tiempo humano**. Cada mes construyendo sin vender es quema de capital.

## Estructura de costos y márgenes (rangos orientativos)
- **COGS** (costo de producir el servicio: hosting/cloud, APIs, soporte): suele ser bajo. Margen bruto SaaS sano: **70–85%** (rango orientativo del sector, no dato de tu caso).
- Lo que se come la caja: **ventas y marketing** (CAC) e **ingeniería** (desarrollo). Un SaaS en crecimiento reinvierte casi todo el margen ahí.
- Por eso un SaaS puede tener 80% de margen bruto y aun así perder dinero: lo gasta en crecer.

## Ejemplo numérico: cohorte SaaS (cifras ILUSTRATIVAS de ejemplo)
Imagina un SaaS B2C que cobra **20 USD/mes**. En enero entran **100 clientes nuevos** (una "cohorte" = grupo que entró el mismo mes). Churn mensual = **8%**.

**Cómo se derriten esos 100 clientes:**
| Mes | Clientes activos (≈) | Ingreso del mes |
|---|---|---|
| 1 | 100 | 2.000 USD |
| 2 | 92 | 1.840 USD |
| 3 | 85 | 1.700 USD |
| 6 | 66 | 1.320 USD |
| 12 | 39 | 780 USD |

**Vida promedio del cliente** = 1 ÷ churn = 1 ÷ 0,08 ≈ **12,5 meses**.
**LTV** ≈ vida × pago mensual × margen bruto = 12,5 × 20 × 0,80 = **200 USD** por cliente.
Si tu **CAC = 50 USD** → LTV:CAC = 200/50 = **4:1** (sano). **Payback** = 50 ÷ (20×0,80) = 50/16 ≈ **3,1 meses** (excelente).

**Ahora baja el churn a 4%** (sin tocar nada más): vida ≈ 25 meses → LTV ≈ 400 USD → LTV:CAC = 8:1. **Reducir el churn a la mitad DUPLICÓ el valor del negocio.** Esta es la lección central del SaaS: la retención manda (ver 52 para profundizar en LTV/CAC).

## Cómo arrancar (mínimo viable, sin programar de más)
1. **Valida ANTES de construir** (ver 39): habla con 15–20 clientes potenciales, confirma que el dolor existe y que pagarían. Vende el "humo" (landing + lista de espera + carta de intención) antes que el producto.
2. **MVP estrecho**: resuelve UN problema agudo para UN tipo de cliente. No 10 funciones; una que funcione.
3. **3–5 pilotos pagados** (no gratis): si no pagan ni un descuento, no es dolor real. Cobra desde el día 1, aunque sea poco.
4. **Mide retención semana a semana** desde el primer cliente. Si usan el producto cada semana, hay negocio. Si lo prueban y desaparecen, arregla eso ANTES de buscar más clientes.
5. Solo cuando la retención es sana → **mete dinero en adquisición** (ver 91 para canales y palancas de crecimiento).

## Pricing: el error más caro y silencioso
- Casi todos los SaaS cobran **demasiado poco** al inicio (miedo a cobrar). Sube el precio: filtra clientes malos y financia el crecimiento.
- Cobra por **valor**, no por costo: si ahorras a la empresa 1.000 USD/mes, cobrar 200 es regalo.
- Estructura simple: 2–3 planes (no 7). Un plan barato de entrada, uno "el que casi todos eligen", uno premium.
- **Pregunta país/ciudad primero**: moneda local, impuestos sobre servicios digitales y facturación electrónica (DIAN en Colombia, SAT en México, etc.) — verifica reglas vigentes, no asumas (ver 21).

## Trampas que matan a este negocio
- **Churn alto que tapas trayendo clientes nuevos**: balde con hueco. Creces en MRR pero el negocio está roto. Arregla el hueco primero.
- **Construir 6–12 meses antes de validar**: gastas el capital en un producto que nadie pidió. La causa #1 de muerte.
- **Pricing mal puesto**: cobrar muy poco (no financia crecimiento) o cobrar por la métrica equivocada (penalizas el uso que querías fomentar).
- **Confundir registros gratis con tracción**: 5.000 usuarios free y 3 que pagan = no es un negocio.
- **CAC que sube y nunca baja**: si cada cliente cuesta más que el anterior y el LTV no sube, no escala.
- **Soporte que no escala**: cada cliente nuevo trae 3 tickets → el "negocio de márgenes altos" se vuelve una consultoría disfrazada.

## Errores comunes
- Mirar solo el MRR (vanidad) e ignorar churn y NRR (la salud real).
- Calcular LTV con churn optimista inventado → todo el modelo miente. Usa tu churn REAL medido.
- No separar churn de clientes (cuántos se van) de churn de ingresos (cuánto dinero se va): un cliente grande que cancela duele más que diez pequeños.
- Lanzar features nuevas en vez de arreglar la retención (más juguetes ≠ más retención).

## Siguiente paso típico
Calcula tu **churn mensual real** y con él saca LTV, payback y LTV:CAC (ver 52). Si LTV:CAC < 3 o payback > 12 meses, NO escales aún: baja el churn o sube el precio primero (ver 53 punto de equilibrio y 91 crecimiento).
