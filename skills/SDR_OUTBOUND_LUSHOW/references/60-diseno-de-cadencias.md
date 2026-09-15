# 60 — Diseño de cadencias

Una cadencia (también "secuencia" o "sequence": la serie ordenada de toques que le das a un mismo prospecto en el tiempo hasta que responde o cierras el ciclo) es el motor que convierte tu lista en reuniones. Sin cadencia mandas un correo, no responden, y te rendiste — cuando la mayoría de las reuniones nacen del **toque 4 al 8**, no del primero. Este módulo fija la arquitectura: cuántos toques, en cuántos días, en qué canales y con qué lógica. Los módulos `61`–`69` desarrollan cada pieza (multicanal, timing, follow-ups, respuestas, A/B, volumen, tu día, objeciones tempranas, agendar).

## El principio: la persistencia estructurada gana

Dos datos que gobiernan todo el diseño:

- **La mayoría de las respuestas positivas llegan después del primer toque.** En cold email B2B bien hecho, típicamente solo ~30–40 % de las respuestas vienen del correo 1; el resto se reparte entre los toques 2 a 6. Rendirte en el toque 1 tira a la basura el 60 % de tu pipeline.
- **Hay un techo de rendimientos decrecientes.** Cada toque extra suma menos y molesta más. Pasado ~8–12 toques, sigues quemando reputación sin ganar reuniones. La cadencia tiene principio y **fin definido** (ver el break-up en `63`).

La cadencia existe para exprimir ese rango de valor (toques 2–8) sin caer en acoso. No es "insistir hasta que compre"; es aparecer con relevancia, desde varios ángulos, el número correcto de veces.

## Cuántos toques y en cuántos días — el estándar

| Perfil de campaña | Toques | Duración | Canales |
|---|---|---|---|
| **Cold email puro** (1:many, alto volumen, ver `66`) | 3–5 | 12–18 días | Email + email |
| **Multicanal estándar** (1:few) | 8–10 | 14–21 días | Email + LinkedIn + call + WhatsApp |
| **1:1 high-touch** (cuentas tier A, ver `16`) | 10–14 | 21–30 días | Todos + toques manuales personalizados |

Regla base: **8–12 toques en 2–4 semanas** es el rango sano para outbound multicanal. Menos de eso deja dinero en la mesa; más de eso en una ventana corta es acoso. Cuanto más caro tu ticket y más alto el cargo, **más largo y más humano** el ciclo.

## Los 4 principios de diseño

1. **Espaciado creciente, no fijo.** Al principio los toques van más juntos (día 1, 3, 5) porque estás fresco en su memoria; luego se abren (día 8, 12, 18). Un toque diario es acoso; un toque cada 10 días te olvida.
2. **Cada toque aporta o cambia el ángulo.** Nunca "solo hago seguimiento". Toque 1 = problema. Toque 3 = caso/prueba. Toque 5 = recurso útil sin pedir nada. Toque 7 = break-up. Rotar el ángulo evita el "ya me lo dijiste" (ver `63`).
3. **Multicanal > monocanal.** Un prospecto que ignora tu correo puede aceptar tu invitación de LinkedIn o contestar el WhatsApp. Cada canal tiene una tasa de atención distinta; combinarlos multiplica las probabilidades de que **al menos uno** lo alcance (ver `61`).
4. **Fin claro (break-up).** Toda cadencia termina con un correo de cierre que libera al prospecto y, paradójicamente, es de los que más responde. Después: al CRM como "no ahora", nurture o reintento en 60–90 días (ver `63`, `64`).

## Anatomía de una cadencia de 8 toques (esqueleto)

```
Toque 1  | Día 1  | Email    | Opener + problema/ángulo principal (ver 51,52)
Toque 2  | Día 2  | LinkedIn | Ver perfil + solicitud de conexión (nota corta o sin nota)
Toque 3  | Día 4  | Email    | Bump / seguimiento + prueba (caso, número) (ver 63)
Toque 4  | Día 6  | Call     | Llamada 1 + voicemail si no contesta (opener → ventas_lushows)
Toque 5  | Día 9  | WhatsApp | Mensaje corto y humano (si es canal apropiado, ver 24)
Toque 6  | Día 12 | Email    | Ángulo nuevo: recurso útil, sin pedir reunión
Toque 7  | Día 15 | Call     | Llamada 2 + LinkedIn message
Toque 8  | Día 18 | Email    | Break-up / correo de cierre (ver 63)
```

Este esqueleto es el punto de partida; `61` lo entrega **día por día con el texto de cada toque**.

## Cómo se ejecuta esto (herramientas)

No corras una cadencia multicanal a mano: se te caen los toques. Usa una plataforma de secuencias que dispara las tareas por ti:

| Herramienta | Fuerte en | Nota |
|---|---|---|
| **Instantly / Smartlead** | Cold email a volumen, rotación de buzones | Email-first; LinkedIn/call como tarea manual |
| **Lemlist** | Email + LinkedIn + tareas manuales | Bueno para multicanal pyme |
| **Outreach / Salesloft** | Cadencias multicanal enterprise, reporting | Caro; para equipos SDR |
| **HubSpot Sequences** | Si ya vives en HubSpot | Límite de pasos automáticos |
| **La Growth Machine / Waalaxy** | LinkedIn + email combinados | Fuerte en el lado LinkedIn |

La plataforma **calendariza y recuerda**; tú pones relevancia. Para el detalle de deliverability (calentar dominio, límites de envío ~30–50/buzón/día) ver `40`–`46`.

## Errores comunes (qué NO hacer)

- **Un solo toque y rendirse.** El error #1. Tiras el 60 % de tu pipeline.
- **Cadencia de "solo recordatorios".** 5 correos que dicen "¿lo viste?" sin aportar nada = fatiga y unsubscribe.
- **Toques diarios.** Densidad de acoso; te reportan como spam (ver `40`).
- **Sin break-up.** Dejas cuentas en limbo; nunca cierras el ciclo ni liberas capacidad.
- **Mismo canal siempre.** Si ignora el correo, un correo más tampoco funciona; cambia de canal (ver `61`).
- **Mismo mensaje en todos los canales.** Copiar-pegar el correo en LinkedIn se nota y quema; adapta al canal.

## Siguiente paso

Con el esqueleto claro, abre `61` para la secuencia de 14 días día por día con el texto de cada toque, y `62` para clavar días/horas. La conversación de venta profunda que arranca cuando responden vive en `ventas_lushows`; esta skill te lleva **hasta el "sí, hablemos"** (ver `69`).
