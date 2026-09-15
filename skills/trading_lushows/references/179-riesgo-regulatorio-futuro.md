# 179 — Riesgo regulatorio futuro: el escenario que no controla ningún stop-loss

## Por qué pensar en esto

El riesgo regulatorio es el riesgo de que **las reglas del juego cambien por decisión de un
gobierno o un banco**, no del mercado. No se cubre con stops ni con sizing: se cubre con
flexibilidad y con no depender de un solo camino. El bot ya vivió una probadita: Binance
geo-bloquea el trading desde IPs de USA — una regla externa que obligó a planear la mudanza a
Frankfurt. Eso ES riesgo regulatorio en acción.

## Escenarios plausibles (sin profecías)

| Escenario | Qué pasaría | Impacto en el proyecto |
|---|---|---|
| **Restricciones bancarias** (bancos locales dificultan entradas/salidas hacia exchanges) | Cuesta más fondear o retirar | No toca al bot: afecta el puente peso↔cripto; conviene tener más de una rampa probada |
| **Impuestos nuevos o reglas de reporte** | Declarar ganancias/patrimonio cripto con más detalle | El bot ya ayuda: historial completo de trades + export CSV = base para el contador. Reglas específicas: **verificar al día con contador** |
| **Prohibiciones parciales** (un país restringe un exchange o un producto, como derivados) | El exchange elegido deja de servir desde cierta jurisdicción | El código habla con Binance vía una capa propia (`src/binance/`); portarlo a otro exchange es trabajo acotado, no reescritura |
| **Cambios del propio exchange** (KYC más duro, límites, salida de un país) | Reglas nuevas de un día para otro | Mismo antídoto: poca dependencia, fondos no acumulados de más en el exchange |
| **Endurecimiento sobre IA/automatización** | Escenario lejano y especulativo | Un sistema personal y pequeño rara vez es el objetivo de estas normas |

Nota honesta: nadie sabe cuál de estos ocurrirá ni cuándo. El punto no es predecir: es que
ninguno de ellos sea fatal.

## Por qué un sistema pequeño y flexible sobrevive mejor

1. **Capital chico = opciones grandes.** Mover $1.000–$5.000 de exchange o de país es un trámite;
   mover millones institucionales es un proyecto. La escala pequeña es una ventaja regulatoria.
2. **Sin apalancamiento ni derivados.** El spot simple (comprar y vender la moneda) es lo último
   que se prohíbe; los derivados y el apalancamiento son lo primero que se restringe.
3. **Arquitectura portable.** Node + JSON + una capa de exchange aislada corre en cualquier
   hosting de cualquier país. La mudanza US→Frankfurt es el ensayo general de esa portabilidad.
4. **Auto-custodia posible.** Los fondos que no están operando no tienen por qué vivir en el
   exchange (ver lección Mt. Gox, módulo 188).

## Reglas de conducta ante cambios regulatorios

- **Cumplir, no torear.** VPNs para saltarse geo-bloqueos de trading violan los términos del
  exchange y arriesgan la cuenta y los fondos. La respuesta correcta al bloqueo de USA fue
  Frankfurt, no un truco.
- **Impuestos: registrar todo desde el día uno.** Es mil veces más fácil declarar con un CSV
  completo que reconstruir dos años de trades después. Las obligaciones concretas en Colombia:
  verificar al día — para eso existe el contador (y la skill contador_lushows).
- **Revisar el mapa 1-2 veces al año:** ¿sigue siendo Binance/Frankfurt la mejor combinación?
  Pregunta de calendario, no de pánico.

## Cómo aplica al AGENTE TRADING

El proyecto ya practica la respuesta correcta: reglas externas cambiaron (geo-bloqueo) → se
adapta la infraestructura (Frankfurt), no se hace trampa. Mantener esa postura: spot sin
apalancamiento, exchange como lugar de paso y no de bodega, historial exportable para impuestos,
y una capa de exchange que se pueda reapuntar. Con eso, cualquier escenario de la tabla es un
inconveniente de semanas, no la muerte del proyecto.
