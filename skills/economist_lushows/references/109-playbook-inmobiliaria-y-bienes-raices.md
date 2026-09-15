# 109 — Playbook: inmobiliaria y bienes raíces

Cómo gana plata el negocio de finca raíz según el modelo (corretaje, arriendo, flipping, desarrollo, renta corta), con la matemática real de cap rate, ROI y apalancamiento. Negocio capital-intensivo e ilíquido: o entras como **intermediario** (poco capital, vives de comisión) o como **dueño/inversor** (mucho capital, vives de la rentabilidad del ladrillo).

> ⚠️ Costos, impuestos (predial, ganancia ocasional, retención en arriendos), comisiones de mercado y regulación de renta corta (Airbnb) **cambian por país y ciudad**. Pregunta país/ciudad primero y verifica reglas vigentes (ver 21 para conseguir datos reales).

## Los 5 modelos: capital, cómo se gana, riesgo

| Modelo | Capital propio típico | De dónde sale la plata | Liquidez | Riesgo |
|---|---|---|---|---|
| **Corretaje / agencia** | Bajo (oficina + marketing) | Comisión % sobre venta o arriendo | Alta (no inmovilizas capital) | Bajo financiero, alto comercial |
| **Arriendo (buy-and-hold)** | Alto (cuota inicial + inmueble) | Renta mensual + valorización | Muy baja | Medio |
| **Flipping** (comprar, remodelar, revender) | Alto | Margen de reventa | Baja | Alto |
| **Desarrollo / construcción** | Muy alto | Margen sobre obra vendida | Muy baja | Muy alto |
| **Renta corta** (Airbnb) | Alto (o sub-arriendo) | Tarifa noche × ocupación | Baja | Medio-alto (regulación) |

**Regla mental:** corretaje es un negocio de **servicio** (vives de tu pipeline). Los otros cuatro son negocios de **capital** (vives de la rentabilidad de un activo grande, lento y caro de vender).

## Conceptos que TIENES que dominar

- **Cap rate (tasa de capitalización):** rentabilidad del inmueble *sin contar deuda*. `Cap rate = Ingreso Operativo Neto (NOI) anual ÷ Precio del inmueble`. El NOI = renta anual − gastos operativos (predial, administración, seguro, mantenimiento, vacancia), *antes* de pagar la hipoteca.
- **ROI / cash-on-cash:** rentabilidad sobre **tu plata real** (la cuota inicial), ya restando la cuota del crédito. Esto es lo que de verdad ganas tú.
- **Apalancamiento:** usar deuda para comprar un activo grande con poca plata propia. Multiplica la ganancia… y multiplica la pérdida. Es el cuchillo de doble filo del negocio (ver 59).
- **Valorización:** subida del precio del inmueble con el tiempo. No es ingreso hasta que vendes (no pagas el mercado con valorización; pagas con renta).
- **Vacancia:** % del año que el inmueble está vacío sin generar renta. Siempre cuéntala (ej. 8%). Quien la pone en 0% se engaña.

## Ejemplo numérico — cap rate y ROI de un apartamento (cifras ILUSTRATIVAS)

Apartamento para arrendar. Moneda genérica "$", cifras de ejemplo, NO de ningún mercado real:

```
Precio de compra:            $200.000.000
Renta mensual:               $1.300.000   →  $15.600.000 / año
Vacancia (1 mes ≈ 8%):       − $1.300.000
Renta efectiva:              $14.300.000
Gastos operativos anuales:
  Predial                    − $1.200.000
  Administración             − $1.800.000
  Mantenimiento + seguro     − $1.000.000
  ─────────────────────────────────────
NOI (ingreso operativo neto) =  $10.300.000 / año
```

**Cap rate** = 10.300.000 ÷ 200.000.000 = **5,15%** anual.
→ Lectura: si compras al contado, el ladrillo te renta ~5% al año *antes* de valorización.

Ahora **con apalancamiento** (crédito hipotecario):

```
Cuota inicial (30%):         $60.000.000   ← tu plata real
Crédito (70%):               $140.000.000
Cuota anual del crédito:     ≈ $13.400.000  (capital + interés, ejemplo)

Flujo de caja anual = NOI − cuota crédito
                    = 10.300.000 − 13.400.000 = − $3.100.000  (NEGATIVO)
```

**Aquí salta la alarma:** apalancado, el inmueble te saca plata del bolsillo cada año (flujo negativo). Solo "ganas" si la valorización supera esa sangría. Cash-on-cash de flujo = −3.100.000 ÷ 60.000.000 = **−5,2%**. Si en cambio la cuota anual fuera $9.000.000, el flujo sería +$1.300.000 y el cash-on-cash +2,2%. **La diferencia entre ganar y perder es la tasa del crédito vs. el cap rate.** Si el cap rate < tasa de interés del crédito, el apalancamiento te hace perder. Regla de oro.

## Estructura de costos y márgenes por modelo (rangos ORIENTATIVOS — verifica país)

- **Corretaje:** comisión típica de **venta ~3% (rango 2–6%)** y de **arriendo ~un mes de canon (rango medio mes a un mes)**. Costo casi todo variable (el agente cobra split de la comisión, ej. 50/50). Margen alto por operación, pero ingreso irregular y dependiente de cerrar.
- **Arriendo:** cap rate típico de mercado residencial suele moverse en **rangos de un dígito bajo-medio**; renta − gastos − impuestos deja el NOI. El verdadero retorno = renta + valorización.
- **Flipping:** apuntas a **margen sobre costo total ≈ 15–25%** (compra + remodelación + costos de cierre + financiación). Si baja de ~15%, un imprevisto te lo come.
- **Desarrollo:** márgenes objetivo más altos (el promotor busca **20%+ sobre ventas**) porque asume el mayor riesgo (terreno, licencias, obra, ventas en plano).
- **Renta corta:** ingreso = tarifa noche × ocupación × días; puede duplicar la renta tradicional **pero** con costos de operación altos (limpieza, plataforma 3–15%, amoblar, rotación) y riesgo regulatorio. ADR (tarifa media) y ocupación mandan.

## KPIs clave del sector

1. **Cap rate** — rentabilidad del activo sin deuda. Tu termómetro de si el precio de compra tiene sentido.
2. **Cash-on-cash ROI** — retorno sobre tu plata real ya descontando el crédito. Lo que importa para tu bolsillo.
3. **Ocupación** (arriendo y Airbnb) — % del tiempo generando renta. En Airbnb, ADR × ocupación = RevPAR (ingreso por noche disponible).
4. **Días en el mercado / velocidad de venta** — cuánto tarda en vender/arrendar. Mide liquidez e iliquidez.
5. **Corretaje:** comisión cerrada/mes, # de captaciones activas, tasa de cierre (visitas → cierres), comisión promedio por operación.

## Cómo arrancar mínimo viable (sin quemarte el capital)

- **Si tienes poca plata → corretaje.** Es el único modelo que se monta con esfuerzo comercial y no con un activo de cientos de millones. Empieza captando, aprendes el mercado, construyes red de contactos. Ahí entiendes precios reales antes de invertir tu plata.
- **Si vas a invertir → empieza por UN inmueble**, modelado con la matemática de arriba *antes* de firmar. Calcula cap rate y cash-on-cash con vacancia y gastos reales del país/ciudad.
- **Renta corta sin comprar:** modelo de **sub-arriendo/arbitraje** (rentas un inmueble largo plazo y lo operas corto plazo) — menos capital, pero verifica que el contrato y la regulación lo permitan.
- **Valida el supuesto frágil primero (ver 53):** la renta real lograble y la ocupación real. No el optimista del vendedor; el de portales y de inmuebles comparables (ver 154 para comparar mercados/zonas).

## Trampas que matan a este negocio

- **Iliquidez.** No puedes vender un apartamento en una semana si necesitas la plata. Tu capital queda atrapado meses o años. Nunca metas en ladrillo plata que vas a necesitar pronto (ver 72: fondo de emergencia y horizonte).
- **Apalancamiento excesivo.** Comprar con 90% de deuda multiplica el riesgo: si la renta baja, sube la tasa o llega una vacancia larga, el inmueble te ahoga. Si cap rate < tasa del crédito, pierdes (ver ejemplo).
- **Sobreestimar la renta y olvidar gastos.** Predial, administración, mantenimiento, vacancia y comisiones se "olvidan" y convierten un 6% en pérdida real.
- **Regulación de renta corta.** Muchas ciudades limitan, gravan o prohíben Airbnb, o exigen permiso de la copropiedad. Tu modelo entero puede volverse ilegal de un día para otro. **Verifica normativa local antes de invertir.**
- **Comprar "porque siempre sube".** La valorización no está garantizada, no paga las cuotas y depende de zona y ciclo. El flujo de caja sí es real; la valorización es esperanza.
- **Costos de transacción ignorados** (notaría, registro, impuestos de venta, comisión). Se comen buena parte del margen del flipping si compras y vendes seguido.

## Errores comunes

- Confundir **cap rate con ROI**: el cap rate ignora la deuda; tu retorno real (cash-on-cash) la incluye.
- Modelar con **0% de vacancia y 0 mantenimiento** — siempre hay meses vacíos y reparaciones.
- Tratar la valorización como ingreso mensual: no pagas cuotas con valorización.
- En corretaje, vivir de 1–2 negocios grandes sin pipeline: cuando se acaban, el ingreso se va a cero.
- Entrar a desarrollo/construcción sin colchón: licencias, sobrecostos de obra y ventas lentas hunden al promotor sin caja.

## Siguiente paso típico
Define cuál de los 5 modelos encaja con tu capital y tolerancia a iliquidez. Si tienes poco capital, arranca en **corretaje** para aprender precios reales; si vas a invertir, modela UN inmueble con cap rate y cash-on-cash usando renta, vacancia, gastos e impuestos **reales de tu ciudad** (ver 21) antes de firmar nada.
