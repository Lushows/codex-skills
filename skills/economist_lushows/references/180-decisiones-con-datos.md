# 180 — Decisiones con datos

Para tomar mejores decisiones de negocio usando números, sin caer en parálisis ni en métricas que se ven bonitas pero no sirven. Cultura data-driven práctica: medir lo justo, decidir y actuar.

## Qué significa "decidir con datos" (y qué NO)
"Data-driven" no es tener mil tableros ni esperar a estar 100% seguro. Es esto:
1. Antes de decidir, pregúntate: **"¿qué número me haría cambiar de opinión?"**
2. Mira ese número (o un proxy razonable).
3. Decide, ejecuta, y mide el resultado para aprender.

No es data-driven: justificar con datos una decisión ya tomada (eso es "data-cherry-picking"), ni recolectar datos sin una pregunta detrás.

> **Término:** *proxy* = un dato sustituto, imperfecto pero disponible, que se aproxima a lo que de verdad quieres medir (ej.: "clics en el botón pagar" como proxy de intención de compra).

## Datos > opiniones (pero opiniones bien usadas valen)
Regla de oro de equipos sanos: cuando hay desacuerdo, **el dato gana sobre la jerarquía o el volumen de voz**. El cargo más alto no tiene la razón por ser el más alto; tiene la razón quien trae evidencia.

- Opinión: "creo que los clientes quieren envío gratis."
- Dato: "el 38% de los carritos se abandonan en la pantalla de costo de envío" (ejemplo ilustrativo).

Cuando NO hay datos todavía, las opiniones de quien está más cerca del cliente (ventas, soporte) valen más que las de quien está más lejos. Y una opinión se convierte en hipótesis testeable: "si pongo envío gratis sobre X monto, el abandono baja" → se prueba (ver 181, experimentos).

## Vanity metrics vs métricas accionables
> **Término:** *vanity metric* = número que sube y te hace sentir bien, pero no cambia ninguna decisión ni se conecta con dinero.

| Vanity (evita) | Accionable (usa) |
|---|---|
| Seguidores totales | Clientes nuevos que vinieron de esa red |
| Visitas a la web | Tasa de conversión visita → compra |
| Mensajes recibidos | % de chats que terminan en venta |
| Descargas de la app | Usuarios activos a 30 días (retención) |
| "Likes" | Costo de adquisición (CAC) y valor del cliente (LTV) (ver 52) |

Test rápido: **"si este número se duplica mañana, ¿gano más plata o tomo una decisión distinta?"** Si la respuesta es no, es vanity.

## Qué medir: pocas métricas que importen
No midas todo. Elige **3–5 métricas norte** por negocio. Marco simple:
- **1 métrica de dinero**: ingreso, margen, o caja (ver 56).
- **1 de adquisición**: cuántos clientes nuevos y a qué costo (CAC).
- **1 de valor/retención**: recompra, LTV, churn.
- **1 de eficiencia operativa**: la que más duele en TU negocio (tiempo de respuesta, % de pedidos a tiempo, ocupación).

Una sola "métrica estrella" (North Star) por etapa: el número que mejor resume si el negocio crece sano. Lo demás son métricas de apoyo para diagnosticar.

## Datos suficientes vs datos perfectos (anti-parálisis)
El error #1 del no técnico ambicioso: esperar el dato perfecto. Casi nunca llega.

Regla práctica del **80/20 de la decisión**:
- Si una decisión es **reversible y barata** → decide con 60–70% de certeza y aprende ejecutando. (Jeff Bezos las llama "puertas de doble sentido": puedes volver.)
- Si es **irreversible y cara** (despedir, firmar arriendo de 3 años, endeudarte fuerte) → exige más datos y baja el riesgo.

Pregúntate: *"¿cuánto me cuesta esperar el dato perfecto vs cuánto me cuesta equivocarme y corregir?"* Si esperar cuesta más que el error, **decide ya**.

## Tamaño de muestra: ¿cuántos datos bastan?
No necesitas ser estadístico. Heurísticas honestas para negocios pequeños:
- **Entrevistas a clientes:** los mismos problemas se repiten alrededor de 5–8 conversaciones; ahí ya hay señal (ver 25, 33).
- **Test A/B chico:** con tráfico bajo, una diferencia debe ser **grande y consistente** para creerla. Si A convierte 2% y B 2.1% con 50 visitas cada uno, eso es ruido, no señal.
- Desconfía de conclusiones sacadas de **1 cliente furioso** o **1 venta enorme**. Un dato extremo (outlier) no es una tendencia.

> Recordatorio de país: cualquier *benchmark* de "tasa de conversión normal" o "CAC típico" depende del sector y del país/ciudad. No tomes cifras de internet como verdad para tu mercado — consíguelas de tus propios números o de fuentes locales (ver 21).

## Ejemplo numérico: decidir si subir la inversión en anuncios
*(Cifras ilustrativas, no datos reales.)* Tienda online de hongos funcionales.

| Métrica | Mes actual |
|---|---|
| Gasto en anuncios | $400 |
| Clientes nuevos por anuncios | 20 |
| **CAC** (gasto / clientes) | **$20** |
| Ticket promedio | $35 |
| Margen por venta | 45% → $15.75 |
| Recompras promedio (LTV bruto) | 2.4 compras |
| **LTV margen** (15.75 × 2.4) | **$37.80** |

Decisión: ¿escalo el presupuesto a $800?
- LTV ($37.80) > CAC ($20) → cada cliente deja casi 2x lo que cuesta traerlo. **Señal verde para escalar.**
- Pero el CAC suele **subir** al escalar (los clientes fáciles se agotan). Regla: subo 50% el presupuesto, **no** el doble de golpe, y vuelvo a medir el CAC en 2–3 semanas.
- **Número que me haría frenar:** si el CAC pasa de ~$32 (donde LTV deja de cubrirlo con holgura), paro y reviso.

Eso es decidir con datos: número claro, umbral de cambio definido, paso reversible, y nueva medición agendada.

## Checklist: ¿esta decisión está bien soportada?
- [ ] ¿Cuál es exactamente la decisión y cuándo hay que tomarla?
- [ ] ¿Qué número (o proxy) la informa?
- [ ] ¿Qué valor de ese número me haría elegir lo contrario? (umbral)
- [ ] ¿La decisión es reversible? Si sí, ¿por qué no decido ya?
- [ ] ¿Estoy mirando una métrica accionable o una vanity?
- [ ] ¿La muestra es suficiente o estoy generalizando de un caso?
- [ ] ¿Cómo y cuándo voy a medir si acerté? (cierre del ciclo)

## Errores comunes
- **Parálisis por análisis:** pedir más datos para no decidir. Pon una fecha límite a la decisión.
- **Vanity metrics:** celebrar seguidores/visitas mientras la caja no mueve.
- **HiPPO:** decidir por la opinión del jefe (*Highest Paid Person's Opinion*) ignorando la evidencia.
- **Cherry-picking:** elegir solo el dato que confirma lo que ya querías hacer.
- **Confundir correlación con causa:** "vendí más el día que llovió" no significa que la lluvia venda; pudo ser otra cosa.
- **Sobre-medir:** 40 KPIs en un tablero que nadie usa para decidir. Menos métricas, más decisiones.
- **No cerrar el ciclo:** tomar la decisión y nunca medir si funcionó. Sin eso no aprendes.

## Cómo empezar mínimo viable (1 hoja de cálculo)
No necesitas software caro. Una planilla con: las 3–5 métricas norte, su valor de este mes vs el anterior, y una columna "¿qué decisión cambia si esto se mueve?". Actualízala semanal o mensual. Eso ya te pone por delante del 90% de los negocios pequeños (ver 183 para construir el tablero/dashboard que la alimente).

## Siguiente paso típico
Define tus 3–5 métricas norte hoy y, para la próxima decisión importante, escribe **una sola línea**: "el número X; si baja de Y, hago Z." Luego pasa a 183 para montar el tablero que las muestre sin que tengas que calcularlas a mano.
