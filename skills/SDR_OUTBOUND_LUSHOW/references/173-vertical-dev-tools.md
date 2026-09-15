# 173 — Vertical: Dev tools (venderle a desarrolladores)

Venderle a **desarrolladores y perfiles técnicos** (APIs, librerías, infraestructura, DevOps, bases de datos, seguridad, dev tools en general) es el vertical donde el outbound tradicional **más fácil se rompe**. Los devs odian el spam de ventas, tienen detector de humo afinado, y compran de abajo hacia arriba (**bottom-up**: el ingeniero prueba solo, adopta, y recién después Compras firma). Este playbook te enseña a prospectar sin quemar tu reputación con la comunidad más ruidosa e influyente de internet.

## El principio: bottom-up y PLG mandan, el outbound es de apoyo

En dev tools la compra casi nunca empieza con una demo agendada. Empieza con un dev que encontró tu herramienta, hizo `npm install`, la probó en un side project y la llevó a su equipo. Por eso el motor primario es **PLG** (Product-Led Growth) y comunidad, no cold email. El outbound aquí cumple **dos roles legítimos**:

1. **Expansion / land-and-expand:** ya hay usuarios de tu producto en la empresa (self-serve) → contactas a quien decide presupuesto para pasar a plan de equipo/enterprise. Este NO es frío: es un PQL/PQA (Product-Qualified Account).
2. **Outbound al comprador económico** (VP Eng, Head of Platform, CISO) cuando el ticket enterprise lo justifica — nunca spam masivo al dev individual.

Regla de oro: **nunca hagas outbound de ventas al desarrollador individual como si fuera un lead frío de SaaS genérico.** Lo tomará como spam y puede quemarte públicamente (Twitter/X, HN, Reddit).

## ICP típico del vertical

- **Usuario/champion:** el desarrollador, SRE, o platform engineer que adopta. **No le vendes; lo ayudas y lo conviertes en tu vendedor interno.**
- **Comprador económico (a quien SÍ haces outbound):** VP of Engineering, Head of Platform/Infra, Engineering Manager, CISO/Head of Security. En startups, el CTO.
- Firmographics (`15`): tamaño del equipo de ingeniería, stack tecnológico (technographics — clave aquí), etapa de la empresa, uso de open source.

## Dónde encontrar las cuentas

- **GitHub:** oro puro. Quién usa/forkea proyectos relacionados, quién tiene estrellas en repos de tu categoría, contribuidores de tu ecosistema. Herramientas como Clay pueden enriquecer desde GitHub.
- **Technographics (BuiltWith, Wappalyzer, StackShare):** empresas que usan tecnologías adyacentes/complementarias a la tuya (`134`, `15`).
- **Tu propio producto (product signals):** quién se registró, activó, llegó a límites del free tier → PQL. La mejor "lista" de dev tools es tu telemetría de uso.
- **Job boards:** vacantes que mencionan tu stack o el del competidor ("experiencia con Kubernetes/Postgres/tu-competidor") → señal de que usan esa tecnología.
- **LinkedIn Sales Navigator** (`26`) para los compradores económicos (VP Eng, CISO), no para devs individuales.
- **Comunidades** (Discord, Slack, foros, HN, dev.to) — para escuchar y participar, NO para hacer pitch.

## Señales / triggers propios

- **PQL/PQA:** varios usuarios de tu free tier en la misma empresa (mejor señal posible).
- **Llegaron a un límite** del plan gratis (rate limit, seats, uso).
- **Estrella/fork/issue** en tu repo o en repos de tu categoría.
- **Contratan para tu stack** o el del competidor (job posts).
- **Adoptaron una tecnología adyacente** que tu herramienta complementa (technographic delta).
- **Post de incidente/dolor público** ("nuestra base de datos no escala") — con muchísimo tacto.

## Ángulo de mensaje que funciona

Con devs y sus jefes: **cero jerga de ventas, cero adjetivos vacíos, respeto por su tiempo e inteligencia**. Sé técnico, específico y honesto. Enlaza a docs, no a un "book a demo" genérico. Si hay uso previo, referéncialo. Al VP Eng le hablas de negocio (costo, velocidad de equipo, riesgo); al champion le hablas técnico.

```
Asunto: {empresa} + {tu-herramienta} (ya los usan 4 devs)

Hola {nombre}, 4 personas del equipo de {empresa} están usando
{herramienta} en planes individuales. Cuando pasa eso, suele
convenir consolidar en un plan de equipo — precio por seat más
bajo, SSO, y controles de seguridad que a nivel individual no
existen.

Te dejo el desglose acá: {link}. Si quieres, 15 min y te ayudo a
armar el setup para {empresa}. Si no, ignora este correo sin
problema.
```

Nota el tono: da salida ("ignora sin problema"), aporta antes de pedir, y no infla. Ese respeto es lo que evita que un dev te queme públicamente.

## Canal preferido

**Email técnico + producto (in-app)** para PQL. **LinkedIn** para el comprador económico. Cold call solo a nivel VP/enterprise. Evita WhatsApp/DM invasivo con devs (lo perciben como intrusión). El mejor "canal" real es que el producto y los docs vendan solos y el outbound solo empuje la conversión de cuenta.

## Errores comunes (críticos en este vertical)

- **Spam masivo al dev individual** → daño reputacional público, no solo un correo ignorado.
- Jerga de marketing/ventas a gente que la detesta ("solución sinérgica de próxima generación").
- Pedir demo antes de dar valor (docs, sandbox, ejemplo de código).
- Ignorar que la compra es bottom-up: presionar al VP cuando ni un dev ha probado el producto = muerte.
- No dar salida fácil: el respeto por su tiempo es parte del pitch.

## Frontera y siguiente paso

Tú calientas y agendas con el comprador económico; la negociación enterprise y el cierre técnico-comercial son **`ventas_lushows`**. Estrategia SaaS general en `91` y `170`; señales en `37`; ética anti-spam en `07`, `45`. **Siguiente paso:** monta el disparador de PQL (alerta cuando ≥2 usuarios de una misma empresa entran al free tier) y escribe una sola secuencia de expansion — ese es el 80% del valor del outbound en dev tools.
