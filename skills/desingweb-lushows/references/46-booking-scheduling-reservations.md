# 46 — Booking, scheduling & reservas UX

Para reservas de restaurante, citas (servicios/clínicas/salones), clases/eventos y flujos basados en disponibilidad — incl. LatAm/WhatsApp. **Léelo para cualquier flujo de reserva/agendamiento/calendario.** Pareja de 21 (forms), 42 (gastronomía), 44 (zonas), 16 (a11y).

## 1. Date & time picker UX

**Nativo vs custom:** usa **`input[type=date]` nativo en mobile** (invoca el picker del SO, ya accesible) y **custom solo en desktop** cuando necesitas pintar disponibilidad (slots ocupados, "next available", precios por día). Nunca un calendario custom sin replicar la a11y nativa (donde se rompe el 90%).
**Custom accesible (W3C APG Date Picker):** grilla `role="grid"`, cada día `gridcell` en un `button`; **roving tabindex** (solo uno `tabindex="0"`, flechas mueven día a día, PageUp/Down=mes, Shift+PageUp/Down=año, Home/End=semana, Esc cierra); `<th abbr="Lunes">L</th>`; título del mes en `aria-live="polite"`; estados **hoy/seleccionado/deshabilitado** con `aria-disabled` (no solo color).
**Time slots:** disponibles como botones activos, ocupados **deshabilitados visibles** (comunica demanda) salvo que sean demasiados → ocúltalos. Increments 15/30/60. Flujo **fecha → luego hora** (two-step Calendly) reduce carga cognitiva.
**Locale AM/PM vs 24h:** detecta por locale (`Intl.DateTimeFormat`). LatAm coloquial usa 12h a.m./p.m.; no fuerces 24h.
**min/max/disabled + "Next available":** deshabilita pasado/fuera de rango; **pre-selecciona el primer slot libre** (el mayor acelerador de conversión — Calendly/Cal.com abren en el primer día con disponibilidad).

## 2. Booking/appointment flow

**Funnel canónico (minimiza pasos):** `servicio → fecha/hora → datos → confirmar → confirmación`.
**Patrón Calendly/Cal.com:** una pantalla con calendario izq + slots der; al elegir, formulario inline. **Guest booking por defecto** (jamás obligues a crear cuenta antes de reservar).
**Holds/locks contra doble reserva:** al seleccionar, **hold temporal 5-10min** liberándolo si no completa (equivalente al "asiento reservado").
**Duration & buffers:** buffers antes/después (limpieza/notas) descontados de la disponibilidad. Group bookings → "X cupos restantes".
**Mobile:** un paso por pantalla, targets ≥44px, autofill, `type=tel/email`, picker nativo. Pulgar-operable de principio a fin.

## 3. Reservas de restaurante

Inputs en orden: **party size → fecha → hora → disponibilidad de mesa** (la disponibilidad depende del tamaño). Slots contra mesas reales; "large party" dispara flujo especial (depósito/aprobación).
**Prevención de no-shows (clave):** **credit card hold** (no se cobra salvo no-show — Resy) · **depósito/prepago** (modelo Tock para tasting/eventos) · special requests (alergias/ocasión) escalan a humano con contexto.
**Waitlist:** si no hay disponibilidad, lista de espera con alerta automática al liberarse (convierte un "no" en lead).
**Patrón WhatsApp (LatAm, el dominante):** (1) cliente "quiero reservar" → bot pide fecha/hora/personas (con **WhatsApp Flows**/quick-replies, no texto libre frágil); (2) valida disponibilidad contra el calendario y confirma; (3) booking abandonado → recordatorio a los 15min; (4) special needs → transfiere a humano con todo el contexto; (5) post-visita: agradecimiento + loyalty.

## 4. Disponibilidad & tiempo real

- **Sin abrumar:** no vuelques 200 slots — agrupa por mañana/tarde/noche, solo días con disponibilidad, "Next available" como ancla.
- **Escasez honesta** ("quedan 3 mesas") solo si es real (falsa = destruye confianza, ilegal en algunas jurisdicciones).
- **Slot tomado mientras reservas:** valida en el submit; si falló, error claro + slots alternativos cercanos (no error genérico). Holds optimistas mitigan.
- **Timezone (crítico en virtual):** detecta la TZ del invitado y **muestra los horarios en SU zona** + dropdown visible para cambiarla; para **presencial bloquea la TZ del local**. Guarda en UTC, renderiza en local. Confirmaciones/reminders reflejan la TZ visible al reservar.
- **Business hours/blackouts/sync:** disponibilidad = horario base − buffers − bloqueos − tomados. Sincroniza Google/iCal (las citas externas del profesional bloquean slots → evita doble booking real).

## 5. Confirmaciones, reminders & ciclo de vida

- **Confirmación + email + `.ics`:** pantalla inmediata (resumen + nº de reserva), email con **archivo `.ics`** (con TZ correcta, ubicación, link de videollamada, `UID` estable para que reschedules actualicen en vez de duplicar) + botones **"Add to Calendar"** (Google/Apple/Outlook).
- **Reminders (reducen no-shows ~30-50%):** cadencia **3-1-0** (3 días/1 día/~1h antes). Canal: **WhatsApp ~98% open rate vs ~20% email**; SMS >90% en minutos. CTA de dos vías ("C para confirmar, R para reagendar") — dar salida fácil reduce el no-show silencioso.
- **Reschedule/cancel ético:** tan fácil como reservar (link directo sin login, un toque); no esconder cancelar (dark pattern). Cancel fácil hoy = recompra mañana.
- **Post-appointment:** follow-up (gracias, reseña, recompra).

## 6. Tendencias 2026
Booking conversacional/AI scheduling (WhatsApp Flows, asistentes que negocian horario) · calm/frictionless (menos pasos, next-available pre-seleccionado, calendar overlay) · smart defaults (horarios óptimos según historial) · plataformas con ML anti-no-show.

## Booking anti-patterns — blacklist
forzar crear cuenta antes de reservar (26% de abandono; guest sube conversión 20-45%) · no mostrar slots disponibles (calendario vacío sin "next available") · confusión de timezone (sin dropdown visible) · demasiados pasos (5+ para algo que cabe en 2) · no mobile / picker custom roto en touch (targets <44px) · sin hold/lock → doble booking, o validar solo al final sin avisar que expiró · sin confirmación/`.ics`/reminders · cancelar/reagendar imposible o escondido · escasez falsa ("¡último cupo!" siempre) · date picker custom inaccesible (sin teclado/roving tabindex, color como único indicador) · texto libre puro en WhatsApp sin quick-replies/Flows (parsing frágil).
