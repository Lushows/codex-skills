# 81 — Playbook servicios locales

Lee este módulo cuando vendas un servicio que se presta en un lugar físico y se agenda con una persona: clínica estética, barbería, taller mecánico, spa, odontología, gimnasio, peluquería, estudio de tatuajes, lavado de autos. No vendes un producto que se despacha — vendes una cita. Eso cambia la geo, el objetivo y cómo cierras. Si vendes producto físico ve a 80; si vendes comida/domicilios ve a 82.

## La estructura concreta de servicios locales

El servicio local tiene tres restricciones que mandan: es **geo-limitado** (solo sirve gente que puede llegar), se **agenda** (el "checkout" es un WhatsApp o un formulario), y el resultado es **visual** (el antes/después es tu mejor creativo). La estructura:

| Capa | Cuántas | Qué define |
|---|---|---|
| Campaign | 1 | Objetivo **Lead Generation** o **Traffic**→WhatsApp (ver 54, 55) |
| Ad group | 1 | **Geo**: ciudad/radio donde atiendes, edad real del cliente |
| Ad | 6–12 | Antes/después, proceso, testimonio (ver abajo) |

La **geo** es la pieza crítica que no existe en e-commerce: no pautes a todo Colombia si tu clínica está en Medellín. Define el radio (TikTok permite ciudad y, según disponibilidad, radio alrededor de una dirección). Pautar fuera de tu zona es quemar plata en gente que nunca podrá ir.

Objetivo: como casi nadie compra una cita en un clic, no optimizas a *Sales*. Optimizas a **Lead** (formulario nativo, ver 54) o mandas a **WhatsApp** (Click-to-WhatsApp / Traffic con cierre humano, ver 55). En Colombia, **WhatsApp gana** para servicios: la gente quiere preguntar precio, disponibilidad y resolver dudas antes de agendar.

## El creativo: muestra el servicio, no lo cuentes

El servicio local tiene una ventaja enorme: **el resultado se ve**. Tu mejor creativo no es hablar del servicio, es **mostrarlo**.

- **Antes/después** — el formato rey. Diente arreglado, carro reparado, piel después del tratamiento, corte de cabello. Sin claims exagerados (en estética/salud cuida los claims, ver 44, 83).
- **El proceso satisfactorio** — la limpieza dental, el detailing del carro, el masaje. TikTok ama el "satisfying"; retiene solo.
- **Testimonio del cliente real** — UGC de alguien que salió feliz (ver 32). Vale oro y da confianza local.
- **Tour del lugar** — "así es nuestra clínica/taller por dentro". Reduce el miedo de "¿será serio?".
- **El especialista hablando** — la doctora/el mecánico explicando algo útil gratis. Genera autoridad (ver 85 para founder content).

Hook geo-local que funciona: *"Si estás en [ciudad] y tienes [problema]..."* — filtra y aterriza. El creativo nativo de celular gana al video pulido también aquí (ver 30).

**Oferta** para servicios (ver 41): primera valoración gratis o a bajo costo, diagnóstico sin compromiso, descuento de primera cita. La meta es **bajar la fricción de la primera visita** — una vez entran, el negocio cierra cara a cara.

## Medición y números reales

El error mortal de servicios locales es medir lo que no importa. Mides:

| Métrica | Qué significa | Trampa |
|---|---|---|
| CPL | Costo por lead/conversación | Lead barato ≠ lead bueno |
| **Costo por cita agendada** | Leads que SÍ agendaron | La que de verdad importa |
| **Costo por cliente que llegó** | Citas que se presentaron | El "no show" es real en Colombia |
| Ticket / LTV | Lo que deja un cliente | Un servicio recurrente vale 5–10× su primera cita |

Como el cierre es humano (WhatsApp/recepción), debes **subir conversiones offline** a TikTok: cuando un lead agenda o paga, lo reportas vía Events API como conversión offline para que el algoritmo aprenda a traer leads que cierran, no solo que escriben (ver 55, 57). Sin esto, TikTok optimiza a "conversaciones baratas" y te llena de curiosos.

Presupuesto realista: un servicio local pequeño arranca con **$40.000–$100.000 COP/día**. Como el ticket suele ser alto y recurrente, un CPL de $3.000–$15.000 COP puede ser muy rentable si la tasa de agendamiento y show son decentes — pero eso lo decide tu cierre, no la pauta. El **guion de WhatsApp que convierte la conversación en cita** lo arma `ventas_lushows`; la **landing/agenda** la arma `desingweb-lushows`; la **viabilidad** (¿cuánto puedes pagar por cliente?) la valida `economist_lushows`.

## Errores comunes — blacklist

- **Pautar a todo el país** cuando atiendes una sola ciudad. Geo mal puesta = presupuesto regalado.
- **Optimizar a tráfico/clics** en vez de leads o conversaciones — atraes mirones que nunca agendan (ver 11, 54).
- **No subir conversiones offline.** TikTok optimiza a leads baratos en vez de leads que cierran (ver 57).
- **Medir CPL y no costo-por-cita-que-llegó.** El lead barato que nunca aparece te arruina (no-show).
- **Video pulido de "comercial de clínica"** en vez de antes/después nativo de celular (ver 30).
- **Claims médicos/estéticos exagerados** ("cura", "garantizado") que TikTok rechaza y que son riesgo legal (ver 44, 83).
- **Dejar el WhatsApp sin respuesta rápida.** El lead local se enfría en minutos; sin cierre ágil, pagaste por nada (ver 55, ventas).
