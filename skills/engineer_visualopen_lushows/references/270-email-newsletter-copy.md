# 270 · Copy de email y newsletter

> El email muere o vive en dos lugares: el asunto (¿lo abren?) y el primer renglón (¿siguen?).
> En 2026 el copy bueno no basta: si no pasas autenticación, ni llegas al inbox. Copy + deliverability van juntos.

## El asunto (subject line): la batalla por la apertura
- **6-9 palabras / ~40 caracteres** se ven completos en móvil (60% abre ahí).
- Palancas: curiosidad ("Lo que pasó con tu pedido…"), beneficio ("3 formas de dormir mejor"), urgencia real, personalización ({nombre}, comportamiento).
- **Preheader** = segundo asunto: complementa, no repitas. "Ábrelo antes del viernes" extiende el gancho.
- Evita gatillos de spam en asunto: MAYÚSCULAS, "GRATIS!!!", exceso de emojis, "$$$".
- A/B testea solo el asunto primero (mayor palanca de apertura).

## Primer renglón y cuerpo
- El primer renglón continúa el asunto, no lo repite. Entra directo al valor.
- **Una idea, un CTA por email.** Más CTAs = menos clics.
- Escaneable: párrafos de 1-3 líneas, bullets, un botón claro.
- Texto > imágenes pesadas: muchos clientes bloquean imágenes; el email debe leerse sin ellas.
- P.D. funciona: muchos leen asunto → P.D. → cuerpo. Pon ahí el beneficio o la urgencia.

## Secuencias (automatizaciones que venden solas)
| Secuencia | Emails | Objetivo | Disparador |
|---|---|---|---|
| **Bienvenida** | 3-5 | educar + 1ª compra | suscripción |
| **Carrito abandonado** | 2-3 | recuperar venta | no completó checkout |
| **Post-venta / nurture** | 3-4 | uso + reseña + recompra | compra entregada |
| **Win-back** | 2 | reactivar dormidos | sin abrir 60-90 días |

Cada email = 1 objetivo. Espaciado: bienvenida densa (día 0,2,5), nurture más lento (semanal).

## Deliverability-aware: el copy no sirve si cae en spam
Requisitos de remitentes masivos 2026 (Gmail/Yahoo, >5.000 envíos/día a Gmail) [verificado, jun-2026]:
- **SPF + DKIM + DMARC** obligatorios y alineados. `p=none` se acepta como inicio, pero se espera avanzar a `quarantine`/`reject`.
- **One-click unsubscribe (RFC 8058)** obligatorio en marketing/promocional — **no** en transaccional (recibos, resets).
- **Tasa de spam < 0.3%** (umbral de enforcement); apunta a **< 0.1%** para inbox estable.
- Implicación de copy: dar baja fácil y visible **mejora** reputación (un "report spam" daña más que mil unsubs).

## Higiene que protege la entrega
- Lista limpia: quita rebotes duros y dormidos; enviar a muertos sube quejas.
- **Doble opt-in** = listas más sanas y menos quejas.
- Warm-up de dominio/IP nuevos: sube volumen gradual, no 0→50k de golpe.
- Consistencia de cadencia y remitente: cambios bruscos disparan filtros.
- Separa flujos: transaccional y marketing en subdominios/streams distintos protege el recibo crítico (ver [[67-email-transaccional-deliverability]]).

## Métricas que importan (y la trampa)
- **Tasa de apertura** es ruidosa desde Apple MPP (infla aperturas). Mira **CTR y conversión**.
- Quejas de spam y unsubs como señal temprana de fatiga/relevancia.
- Segmenta: enviar relevante a pocos > genérico a todos (sube engagement, baja quejas).

## Errores
- Asunto clickbait que el cuerpo no cumple → unsub y quejas.
- Un solo email gigante con 5 CTAs → cero foco.
- Ignorar móvil (60%+ abre en celular).
- Saltarse autenticación y luego "echarle la culpa al copy".

Cruza con [[67-email-transaccional-deliverability]] y [[267-copywriting-redaccion-persuasiva]].
