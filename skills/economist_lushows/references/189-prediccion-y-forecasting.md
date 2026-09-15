# 189 — Predicción y forecasting

Cómo pronosticar tus ventas/demanda con métodos simples (sin software caro) para planear compras, caja, equipo y producción — y cómo saber cuánto puedes confiar en ese pronóstico.

> **Forecast (pronóstico):** una estimación numérica de lo que va a pasar (ej. "venderé 320 unidades en julio"). No es magia ni adivinanza: es un cálculo basado en tu historial + tu cabeza. Siempre tiene error; el objetivo es que el error sea pequeño y conocido.

## Para qué sirve un forecast (y para qué NO)
Sirve para **tomar decisiones de tamaño**: cuánto inventario comprar, cuánta caja necesitas (ver 56), cuánta gente contratar, cuánto producir. Un mal forecast = plata muerta en bodega o clientes que se van porque te quedaste sin stock.

NO sirve para predecir el futuro exacto. Un forecast siempre se entrega como **rango** (optimista / esperado / conservador), no como un número solo. Si alguien te vende "predicción exacta", desconfía.

## Lo primero: junta tu historial
Necesitas datos de ventas por **periodo igual** (día, semana o mes — escoge UNO). Mínimo útil:
- 6-8 periodos para algo básico.
- 24 meses si tu negocio tiene estacionalidad (épocas fuertes/flojas, ej. diciembre).

Si no tienes historial (negocio nuevo), no inventes: usa el método de **demanda desde cero** (ver 20 y 26) — partes de mercado, conversión y capacidad, no de un histórico.

## Método 1 — Promedio móvil (el más simple)
Promedias los últimos N periodos. Bueno cuando las ventas son **estables, sin tendencia ni estación clara**.

**Ejemplo (cifras ilustrativas):** ventas últimas 4 semanas: 100, 120, 110, 130 unidades.
Pronóstico semana 5 = (100+120+110+130) / 4 = **115 unidades**.

- Ventaja: suaviza los picos raros (una semana loca no te descuadra todo).
- Desventaja: reacciona lento. Si las ventas vienen subiendo, el promedio se queda corto.

## Método 2 — Tendencia (cuando hay crecimiento o caída)
Si los números suben o bajan de forma sostenida, calcula el **cambio promedio por periodo** y proyéctalo.

**Ejemplo (ilustrativo):** mes 1=200, mes 2=230, mes 3=255, mes 4=290.
Crecimientos: +30, +25, +35 → promedio ≈ **+30/mes**.
Forecast mes 5 = 290 + 30 = **320 unidades**.

Regla de oro: nunca extrapoles una tendencia "para siempre". Un crecimiento de +15%/mes no dura años — choca contra tu capacidad y el tamaño del mercado (ver 20 mercado, 168 capacidad). Pon un techo realista.

## Método 3 — Estacionalidad (épocas fuertes y flojas)
Muchos negocios venden distinto según la época (restaurantes en quincena, retail en diciembre, helados en verano). Aquí usas **índices estacionales**: cuánto se desvía cada periodo del promedio.

**Ejemplo (ilustrativo):** promedio mensual del año = 100 unidades.
| Mes | Ventas | Índice (ventas/promedio) |
|---|---|---|
| Noviembre | 90 | 0.90 |
| Diciembre | 160 | 1.60 |
| Enero | 70 | 0.70 |

Si para el **próximo** año esperas un promedio base de 120 unidades/mes:
- Forecast diciembre = 120 × 1.60 = **192 unidades**.
- Forecast enero = 120 × 0.70 = **84 unidades**.

Así no compras inventario de diciembre repartido parejo todo el año (error clásico y carísimo).

## Cómo combinar tendencia + estación (forecast realista)
1. Calcula la **tendencia** (¿el negocio crece, ej. +10% año?). Eso te da el promedio base del próximo periodo.
2. Aplícale el **índice estacional** de cada mes.
3. Ajusta a mano por **eventos conocidos** que el dato no ve: subida de precio, una campaña fuerte, un competidor que abre/cierra, un feriado movido. El dato es el 80%; tu cabeza pone el 20%.

## Márgenes de error: di "más o menos cuánto"
Un forecast sin margen de error es peligroso. Mide qué tan bueno ha sido tu método **comparando pronósticos pasados contra lo que de verdad pasó**.

Métrica fácil y honesta — **MAPE (error porcentual promedio):**
```
Error de un periodo = |real − pronosticado| / real
MAPE = promedio de esos errores
```
**Ejemplo (ilustrativo):**
| Mes | Pronóstico | Real | Error % |
|---|---|---|---|
| 1 | 100 | 110 | 9% |
| 2 | 120 | 115 | 4% |
| 3 | 130 | 150 | 13% |
MAPE = (9+4+13)/3 ≈ **9%**.

Lectura práctica: tu pronóstico se equivoca ~9% en promedio. Entonces para julio (forecast 320) tu rango realista es **320 ± 9% ≈ 290 a 350**. Planeas caja para 290 (conservador) y stock para 350 (no quedarte corto).

Guía orientativa de MAPE (no es ley, depende del sector):
- < 10% → muy bueno.
- 10-20% → aceptable para PyME.
- 30% → tu método o tus datos están flojos; revisa.

## De forecast a decisiones (lo que de verdad importa)
- **Inventario:** compra para el escenario esperado + un colchón ("stock de seguridad") del tamaño de tu error y de lo que tarda en llegar el proveedor.
- **Caja:** proyecta con el escenario **conservador**, no el optimista. La caja se planea con miedo (ver 56).
- **Equipo/producción:** dimensiona para el esperado; ten plan flexible (turnos extra, freelancers) para los picos estacionales.
- **Tres escenarios siempre:** conservador / esperado / optimista. Decides con el conservador, sueñas con el optimista.

## Errores comunes
- **Un solo número, sin rango.** "Voy a vender 500" → desastre asegurado. Siempre rango.
- **Promediar parejo un negocio estacional.** Compras de más en temporada baja y te quedas sin stock en diciembre.
- **Extrapolar el crecimiento al infinito.** Ninguna tendencia sube para siempre; ponle techo (capacidad y mercado, ver 168 y 20).
- **Confundir tu deseo con el forecast.** "Necesito vender X para cubrir gastos" NO es un pronóstico, es una meta. Sepáralos.
- **Forecast de cifras de tu país/sector tomadas de internet como verdad.** No inventes tamaños de mercado; consíguelos bien (ver 21) y recuerda que costos/impuestos/estacionalidad cambian por país y ciudad — **pregunta país/ciudad primero**.
- **No medir el error nunca.** Si no comparas pronóstico vs. real, nunca mejoras.

## Checklist rápido
- [ ] ¿Tengo historial por periodos iguales? (o uso 20 y 26 si soy nuevo)
- [ ] ¿Mi negocio tiene tendencia? ¿Estacionalidad?
- [ ] ¿Elegí el método que encaja (móvil / tendencia / estacional)?
- [ ] ¿Ajusté a mano por eventos conocidos?
- [ ] ¿Calculé mi MAPE y entrego un RANGO, no un número?
- [ ] ¿Planeo caja con el conservador y stock con el optimista?

## Siguiente paso típico
Junta tus ventas de los últimos 6-12 periodos, calcula un forecast por el método que encaje, sácale el MAPE con tus aciertos pasados y conviértelo en un rango. Lleva ese rango a tu proyección de caja (ver 56) y a tu plan de inventario antes de comprar nada.
