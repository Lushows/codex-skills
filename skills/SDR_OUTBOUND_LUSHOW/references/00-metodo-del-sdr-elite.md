# 00 — El método del SDR de élite

Este módulo es el cimiento de toda la skill: qué es el outbound moderno, qué hace exactamente un SDR (Sales Development Representative — el rol que consigue y agenda las conversaciones de venta, no el que cierra), y los principios que separan al que llena el pipeline de forma predecible del que "manda mensajes a ver quién cae". Léelo primero: todo lo demás (listas, correos, herramientas, deliverability, cadencias) es la ejecución de estos principios.

## Qué es el outbound moderno

**Outbound** = tú inicias el contacto con alguien que no te conoce ni te buscó, porque encaja en tu cliente ideal. Lo opuesto es **inbound** (que ellos te encuentren; ver `02`). El outbound existe porque el mejor cliente para ti muchas veces **no está buscando** tu solución hoy — pero la necesita. Tú lo interrumpes con relevancia.

El outbound cambió radicalmente. Lo que funcionaba en 2015 (mandar 500 correos genéricos al día desde tu dominio principal) hoy te hunde: quema tu dominio, te mete en spam y quema tu marca. El outbound de 2026 es lo contrario: **poca gente muy bien elegida, un mensaje que solo tendría sentido para ella, disparado en el momento correcto, sobre una infraestructura de envío que protege tu reputación.** Relevancia a escala, no spam a escala (ver `07`).

## El principio: outbound es un sistema, no suerte

La idea fundacional viene de Aaron Ross (*Predictable Revenue*, el libro que definió el rol de SDR en Salesforce): **si conoces tu ecuación —cuántas cuentas tocas, qué % responde, qué % agenda, qué % cierra— puedes predecir cuántas reuniones y cuánto revenue vas a generar, y multiplicarlo subiendo el input.** Eso convierte "conseguir clientes" de una lotería a una máquina con perillas. La ecuación exacta con números está en `05` (la ecuación del pipeline).

Por eso el SDR de élite no piensa "¿tuve suerte hoy?" sino "¿mi reply rate (% que responde) bajó del 5% al 3%? ¿por qué? ¿lista, copy o deliverability?". Todo es medible y todo es arreglable (diagnóstico por métrica en `83`).

## Qué hace exactamente un SDR

El SDR **no cierra ventas**. Su único trabajo es **conseguir reuniones calificadas** y pasárselas al vendedor (AE — Account Executive; ver el modelo completo en `03`). Su día se ve así:

| Actividad | Qué es | Módulo |
|---|---|---|
| Construir/refinar la lista | Sacar las cuentas y contactos que encajan | Bloque 2 (`20`–`29`) |
| Conseguir datos | Correo, teléfono, WhatsApp del decisor | `23`, `24` |
| Ejecutar la cadencia | Mandar la secuencia multicanal de toques | Bloque 6 (`60`–`69`) |
| Manejar respuestas | Positivas, neutras, objeciones tempranas | `64`, `68` |
| Calificar | ¿Este lead encaja de verdad? | Bloque 7 (`70`–`79`) |
| Agendar y hacer handoff | Booking + pasar el contexto al AE | `69`, `73` |

Lo que el SDR **NO** hace: la conversación profunda de venta, rebatir objeciones difíciles a fondo, negociar, cerrar. Eso es **oficio de vendedor → `ventas_lushows`**. El SDR abre la puerta; el AE entra y cierra. Respetar esta frontera es lo que mantiene el sistema sano: un SDR que se pone a "cerrar" descuida el volumen y pasa leads mal calificados.

## Los principios no negociables

1. **La lista es la mitad del resultado.** Un mensaje perfecto a la persona equivocada no vende nada. 30 cuentas que encajan valen más que 3.000 al azar. El ICP (perfil de cliente ideal; ver `10`) decide todo *antes* de escribir una palabra.
2. **La deliverability es invisible hasta que te hunde.** Si tus correos caen en spam, tu copy perfecto no lo lee nadie. La infraestructura (dominios secundarios, SPF/DKIM/DMARC, warmup) es la fontanería que sostiene todo (Bloque 4, `40`–`49`).
3. **Personaliza la relevancia, no el nombre.** "Hola {nombre}" no es personalización. Una línea que demuestra que investigaste su cuenta, sí (ver `52`, `53`).
4. **El primer toque no pide la venta: pide una micro-conversación.** El objetivo del outbound es la **reunión**, no cerrar en el correo (ver `55`).
5. **Señal > volumen.** Un contacto en el momento correcto (cambió de cargo, levantó una ronda, está contratando) vale por cien fríos sin timing (ver `14`, `37`).
6. **Multicanal, no monocanal.** Email + LinkedIn + teléfono + WhatsApp entrelazados convierten mucho más que cualquier canal solo (ver `61`).
7. **Mide por respuestas positivas y reuniones, no por correos enviados.** El volumen es un medio; la reunión calificada es el resultado (ver `80`).
8. **Califica duro para proteger al vendedor.** Pasar un lead que no encaja es peor que no pasar ninguno: destruye la confianza del AE y ensucia el forecast (ver `78`).

## La ética como ventaja competitiva

El spam no es solo feo: es **mal negocio**. Quema tu dominio (te vas a spam para siempre), quema tu marca (la gente te asocia con basura) y en muchos países es ilegal (Habeas Data en Colombia, GDPR en Europa, CAN-SPAM en USA; ver `49`). El outbound ético —permiso implícito por relevancia B2B legítima, opt-out siempre disponible, datos conseguidos legalmente— es el único que escala sin explotarte en la cara. Detalle completo en `07`.

Esto NO significa ser tímido. Significa: contacta a quien de verdad se beneficia, con un mensaje que respeta su tiempo, y dale una salida fácil. Ese outbound puede correr por años; el spam dura semanas.

## Errores fatales de mentalidad (qué NO hacer)

- Creer que "más volumen" arregla todo. Si tu lista o tu copy están mal, más volumen = más daño más rápido.
- Empezar por la herramienta ("¿qué es mejor, Apollo o Clay?") en vez de por el ICP y la ecuación. La herramienta es la última decisión, no la primera.
- Medir el esfuerzo (correos enviados) en vez del resultado (reuniones).
- Tratar de cerrar en el outbound. Tu trabajo es agendar; el cierre es de `ventas_lushows`.

## Siguiente paso

Si estás empezando: lee `01` (cómo usar esta skill y los 7 modos), luego `05` (la ecuación del pipeline: mete tus números y calcula cuántas reuniones necesitas) y `10` (escribe tu ICP). Sin ICP y sin ecuación, cualquier técnica de correo o herramienta es prematura. Para números exactos de la ecuación, apóyate en `Matematicas_lushows`.
