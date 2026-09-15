# 103 — Instantly a fondo

Instantly (instantly.ai) es el sequencer de cold email a volumen más popular para solistas y agencias porque hace lo difícil fácil: **conectas muchos buzones, los calienta solo, y reparte tus envíos para que ninguno se queme**. En el `33` es la "familia 1" (cold email a volumen); aquí ves cómo montarlo end-to-end — buzones, warmup, campañas, la unibox y cómo escalar de 100 a 1.000+ correos/día sin caer en spam. Instantly *envía*; la infraestructura de deliverability (dominios, DNS) la montas tú en el Bloque 4 (`41`–`45`), y sin eso ninguna herramienta salva tu bandeja.

## El principio: reparte el volumen entre muchos buzones

Un buzón nuevo que manda 200 correos fríos el día 1 es spam a los ojos de Google/Outlook y muere. La solución no es un buzón mandando mucho, sino **muchos buzones mandando poquito** (~20–40/día cada uno) y **rotando** (ver `44`). Instantly automatiza justo eso: conectas 10 buzones, pones la campaña a 300/día, y él reparte ~30 por buzón. Además **calienta** cada buzón (warmup: intercambia correos "buenos" con una red para construir reputación, ver `43`). El resultado es volumen alto **agregado** con riesgo bajo **por buzón**.

## Montar los buzones (la parte que la gente hace mal)

El orden correcto, del que depende todo (detalle en `41`, `42`):

1. **Compra dominios secundarios** (nunca el principal). Ej.: si tu dominio es `gastrolatam.com`, compra `getgastrolatam.com`, `gastrolatam.io`, `try-gastrolatam.com`. 2–3 buzones por dominio.
2. **Configura DNS: SPF, DKIM, DMARC** en cada dominio (ver `42`). Sin esto vas directo a spam.
3. **Redirige los dominios secundarios** a tu web principal (que no parezcan vacíos).
4. **Conéctalos a Instantly.** Soporta Google Workspace, Microsoft 365 y su propio **DFY (done-for-you)**: Instantly te vende buzones ya configurados con DNS listo — más caro pero ahorra el dolor técnico. Para un no-técnico, DFY vale la pena al arrancar.
5. **Enciende warmup en TODOS** y **espera 2–3 semanas** antes de enviar en frío. Sí, esperas. Saltarte esto quema los buzones (ver `43`).

Regla de dimensionamiento: para mandar **N correos/día** necesitas **N ÷ 30 buzones** aprox. ¿Quieres 300/día? ~10 buzones. ¿1.000/día? ~30 buzones. Para calcular esto contra tu meta de reuniones → `05` y `Matematicas_lushows`.

## Warmup en Instantly

- Se activa por buzón; Instantly intercambia correos con su red y **saca del spam** los que caen, subiendo tu reputación gradualmente.
- **Nunca lo apagues** para "enviar más", ni siquiera en buzones viejos: mantenlo al ~20–30% del volumen siempre.
- Sube el envío en frío **en rampa**: semana 1 tras el warmup ~10/día/buzón, y subes de a poco hasta 30–40 (ver `43`, `44`).

## Campañas: la anatomía

```
Campaña: "Restaurantes Bogotá — Q1"
  Leads:        CSV verificado desde Clay (ver 28, 31)
  Buzones:      8 (rotación automática)
  Daily limit:  25/buzón → 200/día
  Sending schedule: L–V, 8:00–17:00 hora Bogotá (ver 62)
  Secuencia:
    Paso 1 (día 0):  opener personalizado (variable {{primer_dato}}, ver 53)
    Paso 2 (día 3):  bump / valor (ver 63)
    Paso 3 (día 7):  caso o prueba social (ver 54)
    Paso 4 (día 12): break-up (ver 63)
  Stop on reply: ON
  Open tracking: OFF   ← el pixel daña deliverability en 2026 (ver 80)
  Spintax:       {Hola|Buenas} {{first_name}}, {una idea|una duda} sobre {{company}}
```

Claves de campaña:
- **Variables** `{{first_name}}`, `{{company}}`, y las columnas que trajiste de Clay para personalizar (ver `52`, `120`). Si una variable viene vacía, usa **fallback** para que no salga "Hola ,".
- **Spintax** (`{opción1|opción2}`) para que cada correo sea ligeramente distinto y no parezca envío masivo idéntico (ver `45`).
- **Stop on reply ON** siempre: si responde, la secuencia se detiene.
- **Tracking de apertura OFF**: el pixel de apertura hoy penaliza deliverability; mide por **respuestas**, no aperturas (ver `80`).

## La Unibox (donde vive tu bandeja unificada)

La **Unibox** junta las respuestas de **todos** tus buzones en una sola bandeja. Sin ella estarías revisando 10 correos a mano. Ahí:
- Ves y respondes desde el buzón correcto sin cambiar de cuenta.
- Etiquetas: *interesado / no ahora / no / referido* → alimenta tu disposición y CRM (ver `77`, `64`).
- Marcas como "won lead" para sacar del flujo.

La respuesta en sí —qué decir, cómo manejar la objeción, cómo agendar— **no es de Instantly**: es la conversación de venta y vive en `ventas_lushows` (ver `64`). Instantly te lleva hasta "el prospecto respondió"; de ahí en adelante es oficio de vendedor.

## Escalar volumen sin morir

| Meta diaria | Buzones aprox | Dominios aprox | Nota |
|---|---|---|---|
| 100/día | ~4 | 2 | arranque de solista |
| 300/día | ~10 | 4–5 | validación seria |
| 1.000/día | ~30 | 10–12 | agencia / operación |

- **Escala en rampa, no de golpe.** Agrega dominios/buzones y caliéntalos 2–3 semanas antes de sumarlos al frío.
- **Vigila la deliverability** con la métrica de la propia herramienta y tests (ver `46`). Si sube el spam-rate, **baja volumen** y revisa DNS/warmup.
- **Lead-list limpia siempre.** Verifica antes de cargar (ver `28`): rebotes = veneno para la reputación (ver `45`).
- Instantly incluye **Leads / B2B database** para sourcing dentro de la app, pero su fuerte es el envío; para datos de calidad sigue mandando Clay/Apollo (ver `29`, `100`).

## Precio (aprox 2026)

Planes de envío desde ~$37/mes (Growth) hasta ~$97/mes (Hypergrowth); los buzones que conectas suelen ser **ilimitados** en los planes de pago (ventaja clave vs. otros). El **warmup** viene incluido. Los buzones DFY y la B2B database se pagan aparte. Confirma en su pricing.

## Errores comunes

- **Enviar antes de calentar** o desde el dominio principal → muerte por spam (ver `41`, `43`).
- **Sin SPF/DKIM/DMARC** → bandeja de spam garantizada (ver `42`).
- **Tracking de apertura ON** → penaliza en 2026.
- **Cargar leads sin verificar** → rebotes y reputación quemada (ver `28`, `45`).
- **Subir el volumen de golpe** para "ir más rápido" → quemas todos los buzones a la vez.
- **No usar fallback en variables** → "Hola ," delata el envío automático.

## Siguiente paso

Compra 2–3 dominios secundarios, configúrales DNS (`42`), conéctalos a Instantly, enciende warmup y **espera 2–3 semanas** mientras preparas la lista en Clay (`31`) y el copy (`50`+). Luego lanza una campaña de 200/día con stop-on-reply ON y open-tracking OFF. Para comparar con Smartlead (más fuerte en agencias/rotación) → `104`; la fontanería completa → `41`–`45`.
