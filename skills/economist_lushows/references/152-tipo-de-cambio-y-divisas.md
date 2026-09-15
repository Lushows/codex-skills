# 152 — Tipo de cambio y divisas

Para cuando tu negocio toca otra moneda: importas, exportas, pagas servicios en dólares o cobras a clientes de afuera. Aquí aprendes a NO perder plata cuando el dólar se mueve.

## Conceptos en cristiano (para no técnicos)

- **Tipo de cambio:** cuánto vale una moneda en otra. Ej: 1 USD = 4.000 (de tu moneda local). El número exacto cambia cada día — **pregunta país y consulta el valor de HOY** (ver 21 para fuentes oficiales: banco central de tu país).
- **Devaluación / depreciación:** tu moneda local pierde valor → el dólar "sube" → todo lo importado se vuelve más caro.
- **Apreciación / revaluación:** tu moneda se fortalece → el dólar "baja" → lo importado se abarata (y exportar rinde menos).
- **Riesgo cambiario:** la posibilidad de ganar o perder plata SOLO porque cambió el tipo de cambio, sin que tú hagas nada distinto.
- **Spread:** la diferencia entre el precio al que la casa de cambio/banco te COMPRA dólares y al que te los VENDE. Ahí ganan ellos; tú pierdes. Puede ser 1%–5%.

## ¿Tienes riesgo cambiario? (checklist)

Tienes exposición si marcas alguna:

- [ ] Compras producto o insumos **importados** (aunque pagues en local, el proveedor ajusta por dólar).
- [ ] Pagas software/servicios en USD o EUR (hosting, Meta Ads, Stripe, SaaS).
- [ ] **Exportas** o cobras a clientes del exterior.
- [ ] Tienes deuda en moneda extranjera.
- [ ] Tu competencia importa y sus precios mueven los tuyos.

Si no marcas ninguna, tu riesgo cambiario es casi nulo — sáltate este módulo.

## La regla de oro: calza tus monedas

El objetivo es que tus **ingresos y tus costos estén en la misma moneda** ("calce" / *matching*). Si cobras en local pero pagas en dólares, una devaluación te aplasta el margen.

| Situación | Te beneficia si el dólar… | Te perjudica si el dólar… |
|---|---|---|
| Importas, vendes local | baja | sube |
| Exportas, costos locales | sube | baja |
| Cobras y pagas en USD | (neutro) | (neutro) |
| Deuda en USD, ingresos locales | baja | sube |

## Ejemplo numérico: el golpe de una devaluación (cifras ILUSTRATIVAS)

Importas un equipo. Tipo de cambio de hoy = **4.000** local por USD.

| Concepto | Antes (USD=4.000) | Después devaluación 20% (USD=4.800) |
|---|---|---|
| Costo importado | 100 USD = 400.000 | 100 USD = **480.000** |
| Precio de venta (fijo en local) | 600.000 | 600.000 |
| Margen bruto | 200.000 (33%) | **120.000 (20%)** |

Con SOLO el dólar subiendo 20%, tu margen cayó de 33% a 20% — perdiste **40% de tu ganancia** sin vender una unidad menos. Si tu margen original fuera más delgado (ej. 15%), una devaluación así te deja **vendiendo a pérdida**. Por eso esto importa tanto (ver 53 sobre punto de equilibrio y 150 sobre inflación, que suele venir de la mano).

## Cómo cubrirte (de lo más simple a lo más avanzado)

1. **Cláusula de ajuste por dólar** (lo más fácil y barato): en cotizaciones grandes, escribe "precio válido a TRM/tipo de cambio de hoy; si sube más de X% al momento de pagar, se reajusta". Trasladas el riesgo al cliente.
2. **Cobra anticipo / cobra rápido:** entre más corto el tiempo entre cotizar y cobrar, menos te mueve el dólar.
3. **Sube precio con colchón:** si sabes que repones inventario en dólares, fija precio asumiendo un dólar un poco más alto que el de hoy.
4. **Compra el dólar cuando cotizas, no cuando pagas:** si tienes la liquidez, adquiere las divisas al momento de cerrar la venta para fijar tu costo (cuenta en USD, si tu país lo permite — **verifica**).
5. **Forward / seguro de cambio** (avanzado): contrato con el banco que te fija HOY el tipo de cambio para pagar en 30/60/90 días. Ideal para importaciones grandes con fecha conocida. Tiene costo y requiere cupo bancario — **pregunta a tu banco local**.
6. **Diversifica proveedores:** tener una opción de proveedor local (aunque más caro) te da plan B si el dólar se dispara.

> Para el negocio pequeño, el 80% del beneficio viene de los puntos 1–3. Los derivados (forward) son para volúmenes grandes.

## ¿Pongo mis precios en dólares o en moneda local?

| Precio en USD | Precio en local |
|---|---|
| Te protege de la devaluación | El cliente entiende mejor / más confianza |
| Sirve si tus costos son en USD | Obligatorio en muchos retail B2C (verifica ley) |
| Puede asustar/confundir al cliente local | Te deja expuesto si tus costos son importados |
| Común en B2B, exportación, tech | Común en consumo masivo |

**Híbrido práctico:** muestra el precio en local, pero internamente recalcula desde un dólar de referencia y actualízalo cuando el dólar se mueva más de cierto umbral (ej. 3%). Así no asustas al cliente pero proteges tu margen.

> **Legal:** en varios países hay reglas sobre cobrar en moneda extranjera, facturación y controles cambiarios. Nunca asumas — **pregunta país/ciudad y verifica con un contador local** (ver 62 sobre formalización).

## KPIs que debes vigilar

- **% de costos en moneda extranjera** sobre tus costos totales (tu nivel de exposición).
- **Tipo de cambio "de equilibrio":** a qué valor del dólar tu margen llega a cero (calcúlalo con el ejemplo de arriba).
- **Días entre cotizar y cobrar** (ventana de riesgo).
- **Margen bruto recalculado al dólar de hoy** (no al de cuando compraste el inventario).

## Errores comunes

- **Fijar precios con el dólar de hace 3 meses** y descubrir que vendes a pérdida al reponer inventario.
- Confundir el dólar al que **compraste** con el que **necesitas para reponer** (tu margen real depende del costo de reposición, no del histórico).
- Olvidar el **spread y comisiones** de bancos/pasarelas (Stripe, PayPal cobran conversión).
- Endeudarte en dólares teniendo ingresos solo en local: la trampa clásica que quiebra negocios en una devaluación.
- Especular ("guardo dólares porque va a subir"): eso es apuesta, no gestión. Tu trabajo es **proteger el margen**, no adivinar el mercado.
- Usar el tipo de cambio "de la calle" en tus cálculos cuando tus operaciones reales pasan por el bancario (o viceversa).

## Cómo empezar (mínimo viable)

1. Mide tu exposición: ¿qué % de tus costos depende del dólar?
2. Calcula tu tipo de cambio de equilibrio (dólar al que pierdes margen).
3. Mete una cláusula de ajuste en tus cotizaciones grandes.
4. Recalcula tus precios con el dólar de HOY cada vez que se mueva más de un umbral que tú definas.

## Siguiente paso típico

Calcula tu **% de costos en dólares** y tu **dólar de equilibrio** hoy mismo; si la exposición es alta, añade ya una cláusula de ajuste cambiario a tus cotizaciones y revisa precios (ver 53 y 150).
