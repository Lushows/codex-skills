# 151 — Tasas de interés y crédito

Cómo las tasas de interés mueven tu negocio por tres vías: lo que pagas por financiarte, lo que pueden gastar tus clientes y si conviene invertir hoy o esperar. Aquí aprendes a leer el "clima de tasas" y a decidir con número cuándo endeudarte.

## Qué es la tasa de interés (en cristiano)

La **tasa de interés** es el precio del dinero: lo que cuesta usar plata que no es tuya (o lo que te pagan por prestar la tuya). Cuando un banco central sube su tasa, todo el crédito de la economía se encarece en cadena; cuando la baja, se abarata.

Términos para no técnicos:
- **Tasa de política / del banco central**: la tasa "madre". No la pagas tú directo, pero marca el rumbo de todas las demás.
- **Tasa nominal vs. efectiva anual**: la efectiva incluye el efecto de pagar mes a mes; es la real para comparar (ver 72).
- **Tasa real**: tasa menos inflación. Si te prestan al 20% y la inflación es 12%, el costo "real" es ~8% (ver 150 sobre inflación).
- **Spread**: lo que el banco te cobra por encima de su costo de fondeo. A más riesgo tuyo (sin historial, sin garantía), más spread.

> Las tasas, los topes legales de usura y los costos cambian por país y por mes. **Pregunta país/ciudad primero** y verifica las cifras vigentes con el banco o la autoridad financiera local (cómo conseguir el dato real: ver 21). Aquí explico el MÉTODO, no doy la tasa de hoy.

## Las tres vías por las que la tasa te afecta

| Vía | Tasas ALTAS | Tasas BAJAS |
|---|---|---|
| **1. Tu costo de financiamiento** | Crédito caro: cuotas más altas, menos margen | Crédito barato: financiarte cuesta poco |
| **2. Demanda de tus clientes** | La gente compra menos a crédito (autos, electro, cuotas); aprieta el bolsillo | Más consumo a cuotas; sube la demanda |
| **3. Tu decisión de invertir** | Conviene esperar / autofinanciar; el dinero "vale más" quieto rindiendo | Conviene invertir y crecer; el dinero quieto rinde poco |

La idea clave: **una tasa alta no solo encarece TU deuda, también enfría a tus clientes.** Si vendes algo que la gente compra a cuotas (muebles, equipos, planes), un alza de tasas te golpea por los dos lados a la vez.

## Tasas altas vs. tasas bajas: cómo se comporta tu negocio

**Cuando las tasas están ALTAS:**
- Prioriza **caja y márgenes** sobre crecimiento a crédito (ver 143 sobre capital de trabajo).
- Cobra rápido, paga lento (negocia plazo con proveedores: suele ser deuda gratis, ver 72).
- Tu dinero ocioso **renta**: ponlo en instrumentos seguros de corto plazo en vez de dejarlo quieto.
- Ofrece **menos cuotas / pago de contado con descuento**: tus clientes valoran no endeudarse caro.
- Pospón inversiones grandes financiadas salvo que el retorno supere el costo con holgura.

**Cuando las tasas están BAJAS:**
- Es buen momento para **invertir en activos productivos** financiados (máquinas, expansión) si pagan más de lo que cuestan.
- Tus clientes compran más a cuotas: empuja **financiación a la venta** como gancho.
- Refinancia deudas viejas y caras por nuevas más baratas.
- Cuidado con el exceso: tasa baja no vuelve buena una inversión que de por sí no produce.

## Ejemplo numérico: el impacto de la tasa en la cuota (cifras ILUSTRATIVAS)

Pides **$10.000.000** (moneda local de ejemplo) a **24 meses**, cuota fija. Mira cómo cambia todo solo por la tasa efectiva anual:

| Tasa efectiva anual | Cuota mensual aprox. | Total pagado | Intereses pagados |
|---|---|---|---|
| 12% | ~$471.000 | ~$11.300.000 | ~$1.300.000 |
| 24% | ~$529.000 | ~$12.700.000 | ~$2.700.000 |
| 36% | ~$590.000 | ~$14.160.000 | ~$4.160.000 |

Lectura: pasar de 12% a 36% **triplica los intereses** (de ~$1,3M a ~$4,2M) por el MISMO préstamo. La cuota sube ~25%, pero el costo total se dispara porque pagas más interés durante más tiempo.

**Regla rápida para estimar la cuota mensual** (sistema de cuota fija): no la calcules a mano. Usa la función `PAGO` / `PMT` de Excel o Google Sheets:
`=PAGO(tasa_mensual; número_de_meses; -monto)`
donde `tasa_mensual ≈ tasa_anual / 12` (aproximación; para el dato exacto pide la cuota por escrito al banco).

> Estas cifras son ejemplo de CÁLCULO, no datos de mercado. Reemplázalas con la tasa real que te ofrezcan.

## Cuándo endeudarte según el clima de tasas

El filtro es siempre el mismo (ver 72): **endéudate solo si el dinero produce más de lo que cuesta.** Las tasas mueven el listón de "cuánto debe producir":

1. **Calcula el costo total real** del crédito (tasa efectiva + comisiones + seguros).
2. **Estima el retorno** del uso del dinero (margen del inventario, ventas extra de la máquina, etc.).
3. **Margen de seguridad**: con tasas altas exige que el retorno supere el costo por MUCHO (ej. el doble), porque el error se castiga más caro.
4. **Mira la tasa real, no solo la nominal**: si la inflación es alta, una deuda a tasa fija puede "licuarse" con el tiempo (ver 150) — pero nunca apuestes el negocio a eso.

Decisión simple:
- Retorno >> costo total → **adelante**, incluso con tasas altas.
- Retorno ≈ costo total → **espera** o autofinánciate; el riesgo no paga.
- Retorno < costo total → **no te endeudes**; primero mejora márgenes (ver 92).

## KPIs que debes vigilar con el clima de tasas

- **Cobertura de cuotas**: utilidad operativa mensual ÷ suma de cuotas. Que las cuotas no se coman más de ~20-30% (ver 72).
- **% de ventas a crédito/cuotas**: si es alto, eres muy sensible a las tasas; ten plan B.
- **Costo financiero ÷ ventas**: cuánto de cada venta se va en intereses. Si sube, revisa deuda.
- **Tasa real de tus colocaciones** (si tú das crédito a clientes): cóbralo por encima de la inflación o pierdes plata regalando plazo.

## Errores comunes

- **Mirar solo la cuota mensual** y no el costo total: plazos largos con tasa alta esconden intereses enormes (ver el ejemplo).
- **Confundir tasa nominal con efectiva**, o **mensual con anual** (2,5% mensual ≈ 30%+ anual).
- Olvidar la **tasa real**: celebrar una tasa "baja" que en realidad va por debajo de la inflación cuando TÚ das el crédito.
- **Endeudarte solo porque las tasas están bajas**, sin que el activo produzca: tasa barata no salva una mala inversión.
- Ignorar el **efecto en tus clientes**: subir financiación a cuotas cuando las tasas están altas y la gente ya está apretada.
- **No refinanciar** deuda cara cuando las tasas bajan, por pereza o desconocimiento.
- Asumir que las tasas seguirán igual: proyecta también un **escenario de tasas más altas** antes de firmar a tasa variable.

## Checklist de decisión

- [ ] Sé si la tasa ofrecida es nominal o **efectiva anual**, y mensual vs. anual.
- [ ] Comparé el **costo total** (no solo la tasa) de 2-3 ofertas.
- [ ] Estimé el **retorno** del uso del dinero y supera el costo con margen.
- [ ] Consideré la **tasa real** (vs. inflación, ver 150).
- [ ] Si la tasa es variable, simulé un **escenario de alza**.
- [ ] Evalué el efecto en la **demanda de mis clientes** (si venden a cuotas).
- [ ] Verifiqué tasas, usura y reglas vigentes de mi país/ciudad (ver 21).

## Siguiente paso típico

Averigua la tasa efectiva real que te ofrecen hoy (no la nominal), métela en la fórmula `=PAGO()` para ver la cuota y el total, y pásala por la regla "retorno > costo total" de tu uso del dinero (ver 72). Si las tasas están altas, prioriza caja y márgenes (ver 143); si están bajas y tienes una inversión que produce, es buen momento para financiarte y crecer.
