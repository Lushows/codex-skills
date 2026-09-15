# 186 — Husos horarios y timing internacional

Puedes tener la lista perfecta y el mensaje perfecto, y aun así fallar por una razón tonta: llegaste a la hora equivocada. Cuando el outbound cruza fronteras, el reloj se vuelve una variable de conversión real. Un email que aterriza a las 3am hora del prospecto queda enterrado bajo 40 correos para cuando abre la bandeja; una llamada a la hora del almuerzo local nunca se contesta; un WhatsApp a las 11pm molesta y te reportan. Este módulo es sobre coordinar el contacto internacional para que cada toque caiga cuando el prospecto está disponible y receptivo — no cuando es cómodo para ti.

## El principio: el timing es del prospecto, no tuyo

Toda la mecánica de timing (ver `62`) se multiplica por la distancia horaria. La regla no cambia —llegar cuando el prospecto revisa su canal— pero ejecutarla desde otro huso exige que **programes en la hora local del destinatario, no en la tuya**. Bogotá está en UTC-5; enviarle a un prospecto de Madrid (UTC+1, seis horas adelante) "a media mañana" tuya significa media tarde suya. Enviarle a California (UTC-8, tres horas atrás) tu media mañana es su madrugada. Sin ajustar, tus mejores horas se convierten en las peores del otro lado.

## Las ventanas que funcionan (hora local del prospecto)

- **Email**: martes a jueves, 7–9am (aterriza antes de que llegue la avalancha) o 1–2pm (post-almuerzo). Lunes temprano y viernes tarde, evita (ver `62`).
- **LinkedIn**: horario laboral, media mañana o final de tarde.
- **Llamada / cold call**: primeras horas (8–10am) y final del día (4–6pm), cuando el decisor no está en reuniones; evita la hora de almuerzo local (ver `58`).
- **WhatsApp (LatAm)**: horario laboral y primeras horas de la noche funcionan para pyme, pero **nunca después de las 8–9pm ni domingos** — molesta y te reportan (ver `47`).

Estas ventanas son del reloj del prospecto. Tu trabajo es traducirlas a tu huso al programar.

## La tabla de husos que vas a usar (referencia rápida)

| Mercado | UTC | Diferencia vs. Colombia (UTC-5) |
|---|---|---|
| Colombia / Perú / Ecuador | UTC-5 | — |
| México (centro, CDMX) | UTC-6 | 1h atrás |
| Chile / Argentina | UTC-3 | 2h adelante |
| USA Este (NY, Miami) | UTC-5 | igual (ojo horario de verano) |
| USA Oeste (California) | UTC-8 | 3h atrás |
| España / Europa central | UTC+1 | 6h adelante |
| Reino Unido | UTC±0 | 5h adelante |
| Brasil (São Paulo) | UTC-3 | 2h adelante |

**Ojo con el horario de verano (DST):** USA y Europa cambian la hora dos veces al año; LatAm en su mayoría no. Eso mueve la diferencia una hora en ciertos meses — el gap Colombia–NY o Colombia–Madrid no es fijo todo el año. No lo calcules a mano en cada envío; deja que la herramienta lo maneje.

## Cómo se opera esto en la práctica

1. **Segmenta la lista por huso/país** antes de enviar (ver `12`, `16`). Cada segmento tiene su propia programación.
2. **Usa el envío por zona horaria del sequencer.** Instantly, Smartlead, Lemlist, Outreach, Salesloft (ver `33`) permiten "enviar según la zona horaria del contacto": tú defines "9am" y la herramienta lo dispara a las 9am de cada quien. Es la función que hace escalable el multi-huso — actívala siempre en campañas internacionales.
3. **Registra el huso como campo en el CRM** (ver `32`). Que cada contacto lleve su zona; así el sequencer y tú saben cuándo tocar.
4. **Automatiza email y LinkedIn; agenda manual las llamadas.** El correo se programa solo; las llamadas exigen que tú (o un SDR en ese huso) estés despierto en la ventana del prospecto — por eso un equipo distribuido ayuda (ver `188`).
5. **Cuidado al agendar reuniones cross-huso:** manda siempre la invitación con zona horaria explícita y usa una herramienta de calendario que convierta automáticamente (Calendly detecta la zona del invitado). Un "nos vemos a las 3" sin zona es una reunión perdida.

## El caso Lushows: vender desde Colombia hacia afuera

Desde Colombia (UTC-5) tienes suerte con dos mercados clave:
- **USA Este** está en tu mismo huso (o ±1 por DST): trabajas a la par, ideal para llamadas y respuestas en tiempo real.
- **USA Oeste** va 3h atrás: su mañana es tu mediodía, cómodo.
- **Europa** va 6h adelante: para pillar su horario laboral (9am–6pm Madrid = 3am–12pm Colombia) tu mejor ventana es **la mañana temprano tuya** = tarde suya. Email programado resuelve casi todo; para llamadas o chat en vivo, madruga.
- **México y Sudamérica** están a ±1–2h: prácticamente sin fricción.

Esta cercanía horaria con USA es parte del arbitraje que hace atractivo vender desde LatAm hacia el norte (ver `187`).

## Errores comunes (qué NO hacer)

- Programar en tu hora local sin convertir: tus mejores horas caen en la madrugada del prospecto.
- Ignorar el DST: el gap con USA/Europa se mueve una hora en ciertos meses y descuadra los envíos.
- WhatsApp de noche o domingo en LatAm: molesta y dispara reportes (ver `47`).
- Agendar reuniones sin zona horaria explícita: no-show garantizado.
- No segmentar por huso y mandar todo a la misma hora: media lista lo recibe fuera de ventana.

## Siguiente paso

Añade el campo "zona horaria" a tu CRM (ver `32`), segmenta la lista por país/huso (`12`), y activa el envío por zona horaria del contacto en tu sequencer (`33`). Para las ventanas óptimas de cada canal, la base está en `62`. Si vas a operar llamadas en muchos husos, considera un equipo distribuido (`188`). Para vender cross-border desde LatAm ver `187`. La reunión que agendes y la venta → `ventas_lushows`.
