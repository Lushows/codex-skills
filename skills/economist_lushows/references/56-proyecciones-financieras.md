# 56 — Proyecciones financieras

Sirve para construir un modelo financiero a 3 años que sea creíble: no inventas crecimiento, lo derivas de "drivers" (palancas) reales y muestras 3 escenarios. Es lo que mira un inversionista, un banco o tú mismo antes de apostar tiempo y plata.

## La regla de oro: drivers, no porcentajes mágicos

El error #1 es escribir "vendo $10M el año 1 y crezco 20% cada año". Nadie te cree y no aprendes nada. En vez de eso, descompón los ingresos en sus **palancas** (drivers): variables físicas y de comportamiento que SÍ puedes estimar y controlar.

**Driver = la causa medible de un número.** Ejemplos:
- Ingreso = `clientes × frecuencia de compra al mes × ticket promedio`
- Clientes = `visitas × % que compra (conversión)`
- Visitas = `inversión en ads ÷ costo por clic × % que llega a la tienda`

Cuando modelas por drivers, cada supuesto se puede discutir, medir y mejorar por separado. Si vendes poco, sabes si es porque entra poca gente o porque convierte mal.

## Anatomía del modelo (las 5 capas)

1. **Drivers de ingreso** → cuántos clientes, cuánto compra cada uno, cada cuánto.
2. **Ingresos** = resultado de los drivers.
3. **Costos variables** (COGS): lo que cuesta cada venta (producto, empaque, comisión pasarela, envío). Suben con las ventas. Margen de contribución = precio − costo variable (ver 53).
4. **Costos fijos**: arriendo, sueldos base, software, contador. No dependen de cuánto vendas.
5. **Resultado**: Utilidad = Ingresos − COGS − Fijos. De aquí sale tu break-even (ver 53) y tu caja (ver 55).

> Importante: utilidad NO es caja. Puedes ser rentable en papel y quedarte sin efectivo si cobras tarde o compras inventario por adelantado. El flujo de caja se modela aparte (ver 55).

## Los 3 escenarios (siempre los tres)

Nunca entregues un solo número: entrega un rango. Cambia SOLO los drivers clave, no inventes tres realidades distintas.

| Escenario | Qué supones | Para qué sirve |
|---|---|---|
| **Pesimista** | Drivers ~30-40% peores que tu base (menos clientes, menor conversión, ticket más bajo) | ¿Sobrevivo? ¿Cuánto colchón de caja necesito? |
| **Base (realista)** | Tu mejor estimación honesta, sustentada en datos reales (ver 21) | El número con el que decides y operas |
| **Optimista** | Drivers ~20-30% mejores, pero alcanzables | El techo si todo sale bien; no es la promesa |

Regla: si el escenario **pesimista te quiebra**, el negocio es demasiado frágil; baja costos fijos o consigue más colchón antes de arrancar.

## Ejemplo numérico (cifras 100% ilustrativas, NO datos reales)

Tienda online de un producto a **$80.000** el pedido. Modelo por drivers, año 1:

**Drivers base:**
- Inversión en ads: $2.000.000/mes
- Costo por visita: $1.000 → **2.000 visitas/mes**
- Conversión: 3% → **60 pedidos/mes**
- Ticket promedio: $80.000

**Cuenta mensual (escenario base):**
| Línea | Cálculo | Valor |
|---|---|---|
| Ingresos | 60 × $80.000 | $4.800.000 |
| Costo variable (40%) | 60 × $32.000 | $1.920.000 |
| **Margen de contribución** | | **$2.880.000** |
| Ads | | $2.000.000 |
| Fijos (software, contador) | | $600.000 |
| **Utilidad mes** | | **$280.000** |

**Los 3 escenarios (cambiando solo conversión y ticket):**
| Escenario | Conversión | Pedidos | Ingresos/mes | Utilidad/mes |
|---|---|---|---|---|
| Pesimista | 2% | 40 | $3.200.000 | −$280.000 |
| Base | 3% | 60 | $4.800.000 | +$280.000 |
| Optimista | 4% | 80 | $6.400.000 | +$840.000 |

Lectura honesta: en pesimista PIERDES $280.000/mes → necesitas caja para aguantar mientras subes la conversión, o bajar el costo por visita. La palanca más sensible aquí es la conversión: trabájala antes de meter más plata en ads.

## Cómo proyectar los 3 años (sin inventar)

- **Año 1**: mes a mes (los primeros meses suelen ser flojos; modela la "rampa", no arranques al 100%).
- **Años 2 y 3**: trimestral o anual basta. El crecimiento debe venir de un driver explícito: "abro un segundo canal", "subo presupuesto de ads de $2M a $3.5M", "lanzo recompra que sube frecuencia de 1 a 1.4 al mes". Nunca "+20% porque sí".
- Ata cada salto de ingresos a una **acción concreta y su costo**. Si el año 2 crece, algo costó hacerlo crecer.

## Lista de supuestos explícitos (anéxala SIEMPRE)

Una proyección sin supuestos escritos no vale nada. Documenta:
- [ ] Precio y costo variable por unidad (¿de dónde salen? ver 21, 53)
- [ ] Conversión y ticket (¿benchmark, prueba real, o adivinanza?)
- [ ] Costo de adquisición / costo por visita (ver 52)
- [ ] Costos fijos mensuales reales de TU país/ciudad (arriendo, sueldos, impuestos)
- [ ] Plazos de cobro y pago (afectan la caja, no la utilidad — ver 55)
- [ ] Inflación y tasa de cambio si compras importado (rango orientativo; el dato vigente cámbialo)

> Recordatorio de país: arriendos, sueldos, comisiones de pasarela e impuestos cambian por país y ciudad. Antes de cerrar números, pregunta al usuario su país/ciudad y consigue las cifras reales (ver 21). No uses promedios genéricos como verdad.

## Errores comunes

- **Crecer por porcentaje sin driver** ("+20%/año"). Si no sabes qué lo causa, no pasará.
- **Un solo escenario.** Sin pesimista no ves el riesgo real.
- **Optimista disfrazado de base.** Sé brutalmente honesto: la conversión "promedio de la industria" rara vez es la tuya el primer mes.
- **Confundir utilidad con caja.** Modelo bonito, quiebra por liquidez (ver 55).
- **Olvidar tu sueldo y los impuestos.** No son opcionales; van en los fijos.
- **Costos fijos que crecen escondidos.** Cada cliente nuevo a veces trae soporte, devoluciones, comisiones; revísalo.
- **Decimales falsos.** "$4.812.347" da una falsa precisión. Redondea; lo importante es el orden de magnitud y los drivers.

## Plantilla mínima (cópiala en una hoja de cálculo)

```
SUPUESTOS (drivers)
  Inversión ads/mes ........ $____
  Costo por visita ......... $____   → Visitas = Ads ÷ Costo
  Conversión % ............. ___%    → Pedidos = Visitas × Conv.
  Ticket promedio .......... $____
  Costo variable % ......... ___%
  Costos fijos/mes ......... $____

CÁLCULO (×12 meses, luego años 2 y 3)
  Ingresos = Pedidos × Ticket
  Margen contribución = Ingresos × (1 − Costo var %)
  Utilidad = Margen − Ads − Fijos

3 ESCENARIOS: duplica la hoja cambiando SOLO conversión y ticket
  (pesimista −35%, base, optimista +25%)

SALIDAS: utilidad/mes, break-even (ver 53), caja acumulada (ver 55)
```

(Ver 53 para márgenes y punto de equilibrio; ver 55 para flujo de caja; ver 77 para usar estas proyecciones en el plan de negocio / pitch.)

## Siguiente paso típico

Abre una hoja de cálculo, llena la tabla de drivers con tus números reales (pregúntate de dónde sale cada uno) y construye los 3 escenarios. Luego valida el break-even con el módulo 53 y la caja con el 55 antes de prometerle nada a nadie.
