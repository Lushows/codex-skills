# 29 — Leer los Estados para Decidir

Todo lo anterior (módulos 20–28) sirve para una sola cosa: que el dueño **entienda su negocio** y tome mejores decisiones. Este módulo cierra el bloque enseñando a leer los estados con ojos de dueño, no de contador. Y marca una frontera clara y honesta: **el contador organiza, registra y explica los números; la decisión final la toma el dueño con apoyo de economist_lushows**. El contador no dice "despide a tres personas"; dice "aquí están los números que necesitas para decidirlo".

## La pregunta de fondo

Un dueño no necesita memorizar normas. Necesita responder cuatro preguntas con sus estados:

| Pregunta del dueño | Dónde la responde |
|---|---|
| ¿Estoy ganando plata? | Estado de resultados (módulo 21): utilidad y márgenes |
| ¿Tengo plata? | Flujo de efectivo (módulo 22): caja real |
| ¿Cuánto debo y cuánto es mío? | Balance (módulo 20): pasivo vs. patrimonio |
| ¿Voy mejor o peor que antes? | Análisis horizontal (módulo 26) |

> La trampa más común: confundir **utilidad** con **caja**. Puedes ganar en el papel y no tener para la nómina (módulo 22). Por eso se leen JUNTOS.

## Señales que el dueño debe saber detectar

| Señal | Qué puede significar | Dónde verla |
|---|---|---|
| Ventas suben pero la caja baja | Estás vendiendo a crédito y no cobras | Cartera (módulo 20) + flujo (22) |
| Margen bruto bueno, neto flaco | Los gastos se comen la utilidad | Estado de resultados (21) |
| Endeudamiento creciente | Vives de préstamos, no de operación | Balance (20) + flujo (22) |
| Inventario que crece más que las ventas | Plata congelada en bodega | Rotación de inventario (27) |
| Patrimonio que baja sin pérdidas | Estás sacando demasiados retiros/dividendos | Cambios en patrimonio (23) |

## El método de lectura en 5 pasos
1. **Cuadre primero:** confirma que el balance cuadra y la caja amarra con el flujo. Si no, los números no son confiables aún.
2. **Mira la utilidad y los márgenes** (P&L): ¿el negocio gana? ¿el margen mejora o empeora?
3. **Mira la caja** (flujo): ¿la operación genera efectivo o lo quema?
4. **Mira el endeudamiento** (balance + ratios): ¿quién financia el negocio?
5. **Compara con el período anterior** (horizontal): ¿la tendencia es buena?

Todo cálculo que aparezca en estos pasos (márgenes, variaciones, ratios) se **ejecuta y verifica en código vía Matematicas_lushows**.

## Ejemplo rotulado — cifras ILUSTRATIVAS / inventadas

**Lectura para el dueño de La Sazón S.A.S. (2025 vs. 2024):**

| Señal observada | Cifra | Lectura del contador |
|---|---:|---|
| Ventas | +25% | Buen crecimiento comercial |
| Costo de ventas | +33% | Crece más rápido que las ventas: el margen se aprieta |
| Utilidad operacional | +9% | Vendes más pero ganas casi igual |
| Caja de operación | +19,2 M | El negocio sí genera efectivo |
| Endeudamiento | 76% | Alto; dependes mucho de terceros |

**Lo que dice el contador (registrar/explicar):** "Vendiste 25% más, pero el costo subió 33% y por eso la utilidad casi no creció; además, el 76% del negocio lo financian terceros."

**Lo que NO dice el contador (eso es de economist):** "Sube los precios un 8%" o "renegocia con el proveedor" o "no pidas más crédito". Esas son **decisiones**, y se rutean a economist_lushows, que las evalúa con estos números.

## Errores comunes
- **Decidir con un solo estado:** el balance sin el flujo engaña; léelos juntos.
- **Creer que utilidad = plata disponible:** el error más caro de todos.
- **Reaccionar a un mes aislado:** un mal mes no es tendencia; compara períodos.
- **Que el contador tome la decisión del dueño:** el contador informa; el dueño y economist deciden.
- **Decidir sobre números que no cuadran:** primero cuadra, luego analiza.

## Conexión con otros módulos
- **Módulos 20, 21, 22, 23:** son las fuentes que el dueño lee.
- **Módulo 26 y 27:** análisis y ratios afinan la lectura.
- **Módulo 28:** si hay grupo, se lee el consolidado.
- **economist_lushows:** recibe esta lectura y TOMA la decisión (precio, costos, deuda, inversión).
- **Matematicas_lushows:** ejecuta cualquier número que respalde la lectura.
- **AVIS_lushows:** si esta lectura se convierte en conversación con el cliente, AVIS la comunica.

## Siguiente paso típico
Cierra el bloque de estados financieros. Si la lectura revela decisiones por tomar (precios, deuda, inversión), rutea a **economist_lushows**. Si revela obligaciones de reportar o declarar, continúa con los bloques de impuestos y cumplimiento de la skill.
