# Errores que matan tiendas

> Los 18 errores de abajo están ordenados **por frecuencia**, no por gravedad. Casi ninguno es
> exótico: son los mismos una y otra vez. Si llevas meses sin resultados, tu problema está en los
> primeros seis con una probabilidad muy alta.

## Tabla resumen

| # | Error | Síntoma que ves | Corrección |
|---|---|---|---|
| 1 | Matar productos y campañas demasiado pronto | "Nada funciona" tras 15 intentos de 2 días | Regla escrita: 2× techo de CAC o 3 días |
| 2 | Margen insuficiente desde el principio | Vendes y no queda nada | Múltiplo mínimo antes de testear (`42`) |
| 3 | Un solo creativo | Arranca bien y muere en 5 días | 3-5 nuevos por semana (`262`) |
| 4 | Enviar desde China directo | Entregas de 25 días, quejas, contracargos | **Stock local** (`31`, `136`) |
| 5 | No tener regla de cierre | Empujas un producto en pérdida por semanas | `296` |
| 6 | Capital insuficiente para el número de tiros | Un test malo y se acabó todo | `233` |
| 7 | Copiar el producto sin copiar la oferta | "A él le funciona y a mí no" | `210`, `218` |
| 8 | Página construida para gustar, no para vender | Tráfico bueno, conversión < 1% | `180`, `204` |
| 9 | Prometer plazos que no cumples | Contracargos y reseñas de 1 estrella | Plazos honestos (`170`) |
| 10 | No responder mensajes rápido | Disputas y ventas perdidas | < 2 h (`277`, `279`) |
| 11 | No medir bien (píxel/CAPI mal) | Meta dice 14 ventas, la tienda 9 | `200`, `201` |
| 12 | Escalar de golpe | Subes el presupuesto y el CPA explota | +20-30% por vez (`269`) |
| 13 | Producto de categoría prohibida o con claim de salud | Cuenta bloqueada | `43`, `291` |
| 14 | Sin redundancia de cuentas ni lista propia | Un bloqueo = negocio parado | `291`, `286` |
| 15 | Confundir caja con utilidad | "Vendí mucho" y no hay plata | `234`, `276` |
| 16 | Contratar fijo con los números del mejor mes | Enero te ahoga | `288`, `295` |
| 17 | Vender ropa/calzado por talla | Devolución 15-30% | `43` |
| 18 | Buscar el producto perfecto sin lanzar nunca | 4 meses de investigación, cero tests | Fecha límite de decisión |

---

## Los seis primeros, en detalle

### 1. Matar demasiado pronto
La tasa de acierto es **1 de cada 10**. Eso solo se cumple si cada producto recibe un test real:
USD 200-300, o 50-100 en validación inicial, y una señal definida (3-5 ventas con economía positiva).
Apagar a las 6 horas porque "no vendió" no son 10 tests: son 10 nadas. **Corrección:** presupuesto y
criterio de corte escritos ANTES de encender. Ver `232`, `265`, `268`.

### 2. Margen insuficiente
Un producto que compras a USD 8 y vendes a USD 18 no deja espacio para CAC + envío + devoluciones +
pasarela. **Corrección:** múltiplo mínimo (`42`) y techo de CAC calculado (`11`) antes de gastar el
primer peso. En el modelo verificado de México, el bundle a 1.099 MXN da un techo de CAC de USD 30,73
con un CAC real de 10,54 — holgura de 2,92×. Sin holgura no hay negocio: hay lotería.

### 3. Un solo creativo
El creativo es la segmentación (`247`) y se fatiga siempre (`264`). Una tienda que produce 2
creativos al mes está muerta antes de empezar. **Corrección:** ritmo semanal fijo de producción y un
editor delegado (`290`).

### 4. Enviar desde China directo
Tránsito real de 15+ días, sin control de calidad, sin devoluciones viables, con el arancel de 2026
encima. Genera las tres causas principales de contracargo a la vez: entrega tardía, producto distinto
y cliente sin respuesta. **Corrección:** stock local, aunque sea poco (`136`, `137`).

### 5. Sin regla de cierre
Sin regla, decides con emoción: matas los buenos días malos y sostienes los malos por apego.
**Corrección:** `296`, escrito y pegado al monitor.

### 6. Capital insuficiente por tiro
Con USD 500 y tests de USD 200 tienes dos intentos: probabilidad baja. Con validaciones iniciales de
USD 85 de costo esperado por test escalonado (`232`) tienes ~5 intentos y ~41% de encontrar un
ganador. **El mismo capital, repartido
distinto, cambia el resultado por completo.** Ver `233`.

---

## Los errores de operación (los que matan tiendas que YA vendían)

| Error | Cómo se manifiesta | Costo |
|---|---|---|
| Crecer sin caja | Vendes más y tienes menos plata | Quiebra por crecimiento (`234`) |
| No provisionar contracargos de Q4 | Repartes utilidad en enero, la deuda llega en marzo | `295` |
| No exportar datos nunca | Bloqueo = pérdida total | `291` |
| Delegar sin manual | Promesas imposibles, descuentos inventados | `289` |
| Tocar la estructura de cuentas en temporada | Bloqueo en el peor momento | `291`, `294` |
| Dejar de mirar las entregas | La tasa cae y no te enteras hasta las quejas | `159`, `174` |
| Ignorar los comentarios del anuncio | Una acusación pública mata la campaña | `284` |

## Los errores de mentalidad (la raíz de casi todos)

| Patrón | Qué produce |
|---|---|
| Buscar certeza antes de actuar | Parálisis: meses investigando, cero tests |
| Buscar acción sin criterio | Ruido: 20 productos, ninguno testeado bien |
| Enamorarse del producto | Empujar un cadáver |
| Copiar sin entender | El producto sin el ángulo, la página sin la oferta |
| Medir el ego, no el margen | Celebrar ROAS 4 mientras pierdes por unidad |
| Cambiar de estrategia cada semana | Ningún dato comparable |

Ver `04`.

## Autodiagnóstico: dónde está tu error

| Si tu síntoma es… | Empieza por |
|---|---|
| No vendo nada | `1`, `2`, `3`, `7` → luego `204` |
| Vendo y no gano | `2`, `15` → `223`, `229` |
| Vendía y dejó de vender | `3`, `12` → `264`, `267` |
| Vendo pero todo son problemas | `4`, `9`, `10` → `159`, `282` |
| Me bloquearon la cuenta | `13`, `14` → `291`, `292` |
| Gané en Q4 y ahora no tengo plata | `15`, `16` → `295` |
| Llevo meses "preparándome" | `18` → ponle fecha y lanza |

## La regla que previene la mitad de la lista

**Escribe la regla antes de necesitarla.** Presupuesto de test, criterio de corte, techo de CAC,
plazos que prometes, límites de decisión de tu equipo, fecha de congelamiento de temporada. Todo eso
decidido en frío. Las decisiones tomadas en caliente, con dinero en juego y un número cayendo en la
pantalla, son las que matan tiendas.

## Relacionados
`04` mentalidad y el ciclo de fracaso · `78` matar un producto a tiempo · `209` errores que matan
ventas · `296` cerrar un producto · `267` diagnosticar campaña que no vende · `204` página que no
convierte · `234` flujo de caja · `291` proteger la cuenta · `295` después de diciembre ·
`298` el plan de 90 días
