# 145 — Presupuesto y control de gestión

Sirve para convertir tu plan en un mapa de números con metas mensuales, y luego comparar lo que pasó contra lo que prometiste — para corregir a tiempo, no en diciembre cuando ya no hay nada que hacer.

Un presupuesto sin control es un deseo. El control sin presupuesto es manejar mirando solo el retrovisor. Necesitas los dos.

## Conceptos en una línea (para no técnicos)
- **Presupuesto:** el plan en cifras. "Esto espero vender, esto espero gastar, esto debería quedarme."
- **Real (ejecutado):** lo que de verdad pasó, sacado de tu contabilidad/banco.
- **Desviación (variance):** Real − Presupuesto. Positiva o negativa según ayude o duela.
- **Forecast:** tu mejor estimación ACTUALIZADA de cómo cerrará el año, ya con lo que llevas visto. Distinto del presupuesto (que se fijó al inicio y no se toca).

## El presupuesto anual (cómo armarlo)
Hazlo por mes, no solo anual: el año en una sola cifra esconde la estacionalidad y te deja sin alertas.

1. **Ingresos:** unidades × precio, por línea de producto/canal. Ancla en realidad (ver 56 sobre proyección de ventas honesta), no en optimismo.
2. **Costos variables / COGS:** lo que sube cuando vendes más (materia prima, comisiones, empaque). Exprésalos como % de la venta.
3. **Margen de contribución:** Ingresos − Costos variables (ver 58 para el concepto y el punto de equilibrio).
4. **Costos fijos (gastos operativos / OPEX):** arriendo, nómina base, software, servicios. No cambian con el volumen.
5. **EBITDA / utilidad operativa:** Margen de contribución − Fijos.
6. **Caja:** la utilidad NO es caja. Cruza con tu flujo de caja proyectado (ver 56) — cobros y pagos reales por fecha.

Regla de oro: presupuesta **conservador en ingresos, realista en costos**. El error universal es lo contrario.

## Presupuesto base cero (ZBB)
El método tradicional es "el año pasado gastamos X, súbele 8%". El base cero arranca cada línea en **cero** y obliga a justificar cada peso desde la utilidad que produce.

- **Cuándo usarlo:** cuando los gastos se inflaron sin que nadie sepa por qué, o antes de una ronda de recorte (ver 189 sobre reestructuración y ahorro de costos).
- **Cómo:** lista todos los gastos. Por cada uno pregunta: ¿qué pasa si lo elimino? ¿qué resultado de negocio compra? Si no hay respuesta clara, va a la zona de recorte.
- **Trampa:** es agotador hacerlo con TODO cada año. Práctica real: base cero rotativo — una o dos categorías grandes por año (ej. este año marketing, el próximo nómina).

## Análisis de desviaciones (presupuesto vs real)
El corazón del control. Cada mes (o semana en negocios rápidos) compara y explica.

- **Desviación absoluta:** Real − Presupuesto (en $).
- **Desviación %:** (Real − Presupuesto) / Presupuesto.
- **Regla de materialidad:** solo investiga lo que supere un umbral (ej. ±5% o un monto mínimo). No pierdas el día explicando $20.000.
- **Descompón el "por qué":** una caída de ingresos puede ser **precio** (vendiste más barato) o **volumen** (vendiste menos unidades). Son problemas distintos con soluciones distintas. Sepáralos siempre.
- **Bueno vs malo no es obvio:** gastar más en publicidad (desviación "mala" en gasto) que trajo el doble de ventas es una buena noticia. Mira siempre la desviación de gasto JUNTO a la de ingreso.

## Ejemplo numérico: tabla presupuesto vs real (cifras ilustrativas)
Negocio pequeño, mes de marzo. Cifras de EJEMPLO (en tu moneda local):

| Línea | Presupuesto | Real | Desv. $ | Desv. % | Lectura |
|---|---|---|---|---|---|
| Ingresos | 10.000.000 | 8.800.000 | −1.200.000 | −12% | Alerta roja |
| — por menor volumen | | | −900.000 | | Vendiste 12% menos unidades |
| — por menor precio | | | −300.000 | | Diste 3% de descuento extra |
| Costos variables (40%) | −4.000.000 | −3.520.000 | +480.000 | −12% | Bajan con la venta (normal) |
| **Margen contribución** | **6.000.000** | **5.280.000** | **−720.000** | **−12%** | Cae con la venta |
| Costos fijos | −4.500.000 | −4.700.000 | −200.000 | +4% | Te pasaste en fijos |
| **Utilidad operativa** | **1.500.000** | **580.000** | **−920.000** | **−61%** | El golpe se amplifica |

Lección del ejemplo: una caída de **12% en ventas** se convirtió en **−61% en utilidad**. Eso es el apalancamiento operativo: los fijos no perdonan. Acción inmediata: entender por qué cayó el volumen y revisar si esos $200.000 de fijos extra eran evitables.

## Control de gastos (que el presupuesto se respete)
Un número en un Excel no controla nada. Lo que controla es el **proceso**:

- **Dueño por línea:** cada categoría de gasto tiene un responsable con nombre.
- **Aprobación por umbral:** gastos sobre cierto monto requieren visto bueno. Define el umbral.
- **Revisión mensual fija:** un día al mes, sin excepción, miras la tabla de desviaciones. 60 minutos.
- **Suscripciones zombi:** revisa cada trimestre software/servicios que nadie usa. Mueren solas si no las cazas.
- **Caja chica documentada:** todo gasto con soporte (factura/recibo). Sin soporte, no entra.

## Forecast rodante (rolling forecast)
El presupuesto se fija una vez al año y se queda fijo (es tu vara de medir). El **forecast rodante** se actualiza cada mes: tomas los meses reales ya ocurridos + tu mejor estimación de los que faltan, y siempre proyectas 12 meses hacia adelante.

- **Para qué:** decidir HOY con la mejor info de hoy. ¿Contrato? ¿Aguanto? ¿Acelero?
- **Cómo:** cada cierre de mes, reemplaza el mes que pasó por el real y reestima el resto. Nunca toques el presupuesto original — necesitas el contraste.
- **Negocio nuevo o volátil:** revisa el forecast cada mes. Negocio estable: cada trimestre basta.

## KPIs de control de gestión
- **% de cumplimiento de ingresos:** Real / Presupuesto.
- **Desviación de OPEX (%):** ¿gastas más o menos de lo planeado en fijos?
- **EBITDA vs presupuesto.**
- **Días de caja:** cuántos días opera el negocio con la caja actual (ver 56). El KPI que avisa antes de que duela.
- **Burn rate** (si quemas caja): cuánto pierdes por mes y cuántos meses de pista te quedan.

## Errores comunes
- **Presupuesto solo anual:** sin meses no hay alertas tempranas.
- **Hacerlo y guardarlo:** si no lo revisas cada mes, es decoración.
- **No separar precio de volumen:** tratas mal el problema porque no sabes cuál es.
- **Confundir utilidad con caja:** puedes ser "rentable" y quebrar por falta de liquidez (ver 56).
- **Castigar la desviación buena:** penalizar a quien gastó de más en algo que generó retorno enseña a la gente a no invertir.
- **Optimismo en ingresos:** el presupuesto inflado vuelve inútil el control entero.

## Recordatorio de país
Definiciones contables, impuestos sobre la utilidad, qué gastos son deducibles y cómo se registra la nómina **cambian según tu país y régimen tributario**. Antes de cerrar tu presupuesto con cifras fiscales, **pregunta país/ciudad y verifica las reglas vigentes** con tu contador o la fuente oficial (ver 21 para conseguir datos reales).

## Siguiente paso típico
Arma tu presupuesto mensual de 12 meses en una hoja (ingresos, variables, fijos, utilidad, caja). Al cerrar este mes, pon la columna "Real" al lado y calcula desviaciones: ataca primero la línea con mayor desviación negativa en $.
