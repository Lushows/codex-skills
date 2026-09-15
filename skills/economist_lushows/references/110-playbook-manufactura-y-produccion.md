# 110 — Playbook: manufactura y producción

Sirve para entender la economía de fabricar cosas físicas a escala: cómo baja tu costo unitario con el volumen, por qué los costos fijos altos te pueden hundir o disparar, y cuánto capital de verdad necesitas antes de prender la máquina.

> **Aviso país:** capital de arranque, costos de máquinas, energía, mano de obra, impuestos y normas de fábrica (licencias ambientales, sanitarias, seguridad industrial) cambian MUCHO por país y ciudad. Lo que sigue son **rangos orientativos y métodos**, no datos duros. Antes de comprometer dinero: pregunta/verifica tu país y ciudad (ver 21).

---

## Lo que define a este negocio

Manufactura = transformar materia prima en producto terminado con máquinas y procesos repetibles. Su economía gira alrededor de tres palancas:

1. **Costo unitario** — cuánto te cuesta producir UNA unidad (incluyendo la parte que le toca a los costos fijos).
2. **Escala** — entre más produces, más reparten el costo fijo y más barata sale cada unidad (hasta cierto punto).
3. **Utilización de planta** — qué tanto usas la capacidad que ya pagaste. Una máquina parada cuesta igual que una trabajando.

La trampa central: en manufactura los **costos fijos son altos** (máquinas, planta, personal de base). Eso significa punto de equilibrio alto y un negocio que es desastroso a bajo volumen y excelente a alto volumen.

---

## CAPEX vs OPEX (vocabulario clave)

- **CAPEX (inversión de capital):** lo que pagas UNA vez para tener capacidad de producir: maquinaria, montaje, obra civil, moldes. Se "gasta" contablemente repartido en años (depreciación).
- **OPEX (gasto operativo):** lo que pagas CADA mes para operar: materia prima, energía, mano de obra, mantenimiento, arriendo.

Regla práctica: el CAPEX te da el *techo* de cuánto puedes producir (capacidad instalada). El OPEX define tu *costo variable* por unidad. Si compras una máquina gigante (CAPEX alto) pero vendes poco, pagas la máquina sin usarla → costo unitario altísimo.

---

## Estructura de costo unitario

Costo por unidad = **Costo variable por unidad** + **Costos fijos ÷ unidades producidas**

| Componente | Tipo | Ejemplo de qué incluye |
|---|---|---|
| Materia prima | Variable | Insumos que se vuelven producto |
| Mano de obra directa | Variable o semi-fijo | Operarios por turno |
| Energía / consumibles | Variable | Luz, gas, lubricantes |
| Depreciación máquina | Fijo | CAPEX repartido por año |
| Arriendo planta + supervisión | Fijo | Renta, jefe de planta, vigilancia |
| Mantenimiento base | Semi-fijo | Mantenimiento programado |

**Costos fijos altos = mucho apalancamiento operativo.** Cada unidad extra por encima del equilibrio cae casi entera a utilidad. Por eso llenar la planta es la obsesión #1 (ver 58 sobre estructura de costos).

---

## Ejemplo numérico: cómo baja el costo por escala

*(Cifras ILUSTRATIVAS para enseñar el método, no de ningún mercado real.)*

Supón una fábrica con:
- Costos fijos mensuales: **$20.000.000** (depreciación máquina + arriendo + personal base)
- Costo variable por unidad: **$6.000** (materia prima + energía + mano de obra directa)
- Precio de venta: **$12.000** por unidad

| Unidades/mes | Costo fijo por unidad | Costo variable | **Costo unitario total** | Margen por unidad |
|---|---|---|---|---|
| 1.000 | $20.000 | $6.000 | **$26.000** | **–$14.000 (pierde)** |
| 3.000 | $6.667 | $6.000 | **$12.667** | –$667 (casi) |
| 5.000 | $4.000 | $6.000 | **$10.000** | +$2.000 |
| 10.000 | $2.000 | $6.000 | **$8.000** | +$4.000 |

Lección brutal: al vender a $12.000, a 1.000 unidades **pierdes dinero en cada venta**; a 10.000 unidades ganas $4.000 por unidad. **El mismo producto, el mismo precio — solo cambió el volumen.** Esa es la magia y la trampa de los costos fijos altos.

### Punto de equilibrio (¿cuántas unidades para no perder?)

Punto de equilibrio (unidades) = **Costos fijos ÷ (Precio − Costo variable unitario)**
= 20.000.000 ÷ (12.000 − 6.000) = **3.334 unidades/mes**

Por debajo de 3.334 pierdes; por encima ganas. (Ver 53 para el método completo de punto de equilibrio.) En manufactura este número suele ser grande: por eso necesitas demanda *asegurada* antes de invertir, no después.

---

## Capacidad instalada y utilización

- **Capacidad instalada:** máximo que la planta puede producir si trabaja a tope (ej. 12.000 unidades/mes a 2 turnos).
- **Utilización:** lo que realmente produces ÷ capacidad. Si produces 6.000 de 12.000 → 50% de utilización.

Cada punto de utilización que ganas baja tu costo fijo por unidad sin gastar un peso más. **Vender más o tercerizar capacidad ociosa vale oro.** Capacidad ociosa = dinero que ya pagaste y no estás usando.

Economías de escala reales existen hasta un punto: después llegan **deseconomías** (más coordinación, más supervisión, logística enredada, descuentos de volumen que se agotan). No asumas que "más grande = siempre más barato".

---

## KPIs clave del sector (mídelos cada semana/mes)

| KPI | Qué mide | Por qué importa |
|---|---|---|
| **Costo unitario total** | Costo real por unidad producida | Define tu margen y tu precio mínimo |
| **Utilización de planta (%)** | Producción real ÷ capacidad | Capacidad ociosa = dinero quemado |
| **Merma / scrap (%)** | Material o producto desperdiciado | 5% de merma = 5% de margen perdido |
| **Lead time** | Días desde pedido hasta entrega | Define cuánto inventario y capital necesitas |
| **OEE (eficiencia global del equipo)** | Disponibilidad × rendimiento × calidad | Salud real de la máquina/proceso |
| **Rotación de inventario** | Cuántas veces vendes tu inventario al año | Inventario quieto = capital atrapado |

---

## Capital típico de arranque (orientativo)

Depende muchísimo de QUÉ fabricas. Tres niveles:

- **Micro / taller (bajo CAPEX):** ensamble manual, repostería industrial, costura, carpintería básica. Arranque orientativo bajo. Empiezas con 1-2 máquinas y creces.
- **PyME industrial:** plástico, metalmecánica ligera, alimentos procesados, cosmética. CAPEX medio-alto: maquinaria especializada + planta adecuada.
- **Industria pesada / regulada:** farma, química, automotriz. CAPEX muy alto + licencias largas.

> No te puedo dar la cifra exacta sin tu país, máquina y escala. **Método:** cotiza 3 proveedores de la máquina clave, suma montaje + obra civil + capital de trabajo (ver abajo) y multiplica por un colchón de 1,3 (siempre cuesta más). Verifica costos locales (ver 21).

---

## Capital de trabajo: el asesino silencioso

Lo que casi nadie calcula y quiebra fábricas rentables: **el dinero atrapado entre que pagas materia prima y cobras la venta.**

Ciclo: pagas insumos → produces (días) → vendes a crédito (días) → cobras. Todo ese tiempo necesitas plata para seguir operando.

*Ejemplo ilustrativo:* compras materia prima hoy, produces en 10 días, vendes a 30 días de plazo. Son ~40 días de operación financiados por ti. Si vendes $50M/mes, puedes necesitar **$60-70M solo en capital de trabajo**, aparte del CAPEX. Subestimar esto es la causa #1 de quiebras de fábricas que "iban bien" (ver 165 sobre flujo de caja y 143 sobre cadena de suministro / inventario).

---

## Cómo arrancar un MVP en manufactura (mínimo viable)

No compres la fábrica el día 1. Escalera de riesgo:

1. **Maquila / tercerización:** que otro fabrique con tu marca y receta. Validas demanda con CAPEX casi cero.
2. **Lote piloto pequeño:** produce 100-500 unidades, vende, mide merma y costo real.
3. **Una máquina, un turno:** compra solo el cuello de botella crítico; terceriza el resto.
4. **Escala cuando la utilización pase ~70%:** ahí sí justifica más CAPEX.

Esto convierte un negocio de costos fijos altos en uno por etapas, donde cada inversión la respalda demanda ya probada.

---

## Trampas que matan a este negocio

- **Sobre-inversión en capacidad:** comprar la máquina grande "para crecer" y quedar con 30% de utilización. Mata el costo unitario y consume el capital. Compra capacidad *detrás* de la demanda, no adelante.
- **Ignorar el capital de trabajo:** rentable en papel, sin caja para la próxima compra de insumos.
- **Merma no medida:** un 5-10% de desperdicio se come el margen sin que lo veas.
- **Vender por debajo del costo unitario real** porque olvidaste meter la depreciación y los fijos en el cálculo.
- **Un solo cliente grande:** te exige descuentos, paga tarde y si se va, te quedas con la planta vacía.
- **Subestimar mantenimiento:** la máquina parada no produce pero sigue costando.

## Errores comunes

- Calcular el costo "solo con materia prima" e ignorar fijos → precio que parece bueno y pierde dinero.
- Confundir utilidad contable con caja: depreciación no es salida de efectivo, pero el pago del insumo sí.
- Asumir que más volumen *siempre* baja el costo (olvidar deseconomías y límites de capacidad).
- Comprometer CAPEX con demanda "prometida" pero no firmada.

---

## Siguiente paso típico

Calcula tu **costo unitario real** a tu volumen actual (variable + fijos ÷ unidades) y tu **punto de equilibrio** (ver 53). Si tu utilización está por debajo de ~60%, antes de invertir en más capacidad, llena la que ya tienes o terceriza el sobrante.
