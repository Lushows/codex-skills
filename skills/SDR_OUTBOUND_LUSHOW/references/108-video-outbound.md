# 108 — Video en el outbound

Un video corto y personalizado dentro de tu secuencia puede **duplicar o triplicar la tasa de respuesta** en el segmento correcto, porque hace algo que ningún correo de texto logra: **prueba que un humano real dedicó tiempo a esta cuenta específica**. Este módulo cubre las herramientas (Loom, Vidyard, Sendspark), cómo insertar el video en la cadencia sin romper deliverability, y —lo más importante— **cuándo el video sube respuestas y cuándo es puro trabajo desperdiciado**. El video es una palanca de personalización (ver `52`, `66`); no reemplaza al copy (`50`) ni al sistema.

## El principio: el video demuestra esfuerzo y baja la guardia

El outbound frío choca con dos muros: "esto es masivo" y "no confío en quien me escribe". Un video de 30–60 segundos donde el prospecto **ve tu cara, oye tu voz y ve tu pantalla mostrando SU sitio web** derrumba los dos de golpe: no puede ser masivo si dijiste su nombre y mostraste su negocio, y ver a un humano genera confianza que el texto no da. Por eso el video rinde en respuestas — pero **cuesta tiempo grabar cada uno**, así que la matemática solo cierra en cuentas de suficiente valor (ver abajo y `66`).

## Las herramientas

| Herramienta | Fuerte en | Ideal para | Precio aprox 2026 |
|---|---|---|---|
| **Loom** | Rapidísimo de grabar (pantalla+cara), links instantáneos | Arrancar, 1-a-1 ágil | Free limitado; ~$12–15/mes |
| **Vidyard** | Analítica (quién vio, cuánto), CTAs, integración CRM/ventas | Equipos que miden y escalan | Free; planes de pago para features |
| **Sendspark** | **Personalización a escala**: fondos/pantallas dinámicas por prospecto, AI | Volumen medio con toque personal | ~$39+/mes según plan |

- **Loom** = velocidad. Grabas, copias link, pegas. Perfecto para el toque manual a Tier A.
- **Vidyard** = medición. Te dice si lo vieron y cuánto, lo que te dice a quién seguir (ver `80`).
- **Sendspark** = escala. Genera muchos videos con partes personalizadas (el nombre en pantalla, su web de fondo) sin grabar uno por uno; el punto medio entre "manual" y "masivo".

## Cómo insertarlo sin romper deliverability

El error técnico que mata todo: **incrustar el video/GIF pesado directo en el correo** dispara filtros de spam y ensucia tu deliverability (ver `45`). La forma correcta:

1. **No adjuntes ni incrustes el video.** En el cuerpo va una **imagen thumbnail (miniatura) con botón de play** que **enlaza** a la página del video (Loom/Vidyard/Sendspark la hospedan).
2. **Un solo link**, idealmente al mismo dominio de la herramienta, sin acortadores raros (los acortadores levantan sospecha, ver `45`).
3. **Miniatura personalizada:** que el thumbnail muestre tu cara señalando + el logo/sitio del prospecto de fondo → el gancho visual que hace clic.
4. **Texto igual de bueno.** El correo debe funcionar aunque no vean el video: opener + una línea de por qué grabaste esto + CTA (ver `53`, `55`).

```
Asunto: {{first_name}}, te grabé algo de {{company}} (55 seg)

Hola {{first_name}}:
Estaba viendo {sitio/perfil de {{company}}} y noté {observación específica}.
Te grabé un video corto con una idea para {resultado} sin {dolor}:

[ ▶ miniatura con tu cara + su sitio → enlace a Loom/Vidyard/Sendspark ]

Si tiene sentido, ¿10 min esta semana? (ver CTA 55)
```

## Guion del video (30–60 segundos, ni uno más)

1. **Nombre + gancho (0–8s):** "Hola María, vi que El Fogón abrió una segunda sede — felicitaciones." (Muestras su web en pantalla.)
2. **La observación / idea (8–35s):** un problema o una oportunidad concreta que viste, no un pitch genérico. Enséñalo en pantalla si aplica.
3. **CTA suave (35–55s):** "Si quieres te muestro cómo lo resolvimos con otro restaurante parecido — ¿te va bien un café virtual de 10 min el jueves?" (ver `55`).

Reglas: **corto** (más de 90s y lo cierran), **energía alta**, **su nombre y su negocio en los primeros 8 segundos**, y termina con un CTA claro. El video **abre** la conversación; la venta profunda que viene después es `ventas_lushows`.

## Cuándo el video SÍ sube respuestas (y cuándo no)

**Úsalo cuando:**
- El **ticket/LTV es alto** y el tiempo de grabar (~3–5 min por video) se paga con una reunión (ver `66`, `96`). Cuentas Tier A/B (ver `16`).
- El prospecto **no respondió** a los primeros correos de texto → el video como paso de reactivación rompe el silencio (ver `63`, `75`).
- Vendes algo **visual o de demo** (software, diseño, un proceso) donde mostrar la pantalla comunica más que el texto.
- Es **ABM**: pocas cuentas, mucho valor, personalización máxima (ver `94`).

**NO lo uses cuando:**
- **Volumen alto / ticket bajo** → la matemática no cierra; grabar 500 videos no escala (ver `66`). Ahí, personalización por texto con Clay (ver `52`, `120`).
- Tu **oferta o lista aún no están validadas** → primero prueba con texto barato que el mensaje funciona; el video amplifica un mensaje que ya convierte, no arregla uno malo.
- El **primer toque en frío** a puerta totalmente fría de bajo valor → resérvalo para cuando ya haya algo de contexto o para Tier A.

Regla de decisión (ver `66`): **valor de la cuenta × probabilidad de que el video mueva la aguja > costo de tu tiempo grabándolo.** Si dudas, calcula el costo por reunión con y sin video → `Matematicas_lushows`.

## Errores comunes

- **Incrustar el video en el correo** → spam. Siempre miniatura + link (ver `45`).
- **Videos largos** (2–3 min) → nadie los ve. 30–60 seg.
- **Genérico disfrazado de personal:** "Hola, quería contarte de nuestra solución…" sin decir su nombre ni mostrar su negocio → cero ventaja sobre el texto.
- **Video a volumen masivo de bajo ticket** → horas tiradas; usa texto personalizado (ver `66`).
- **Sin CTA claro** al final → el prospecto ve el video y no sabe qué hacer (ver `55`).
- **Descuidar el copy del correo** confiando en que el video hace todo → si no dan play, no queda nada.

## Siguiente paso

Elige **10 cuentas Tier A** que no te hayan respondido y grábales un Loom de 45 segundos siguiendo el guion, con miniatura personalizada + link (no incrustado). Mide la respuesta contra tu baseline de texto. Si sube y el ticket lo justifica, escala con Sendspark. Para decidir volumen vs. personalización → `66`; para el CTA → `55`; para la conversación que abre el video → `ventas_lushows`.
