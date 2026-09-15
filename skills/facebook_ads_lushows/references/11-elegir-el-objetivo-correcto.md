# 11 — Elegir el objetivo correcto

El "objetivo" de campaña es lo primero que Meta te pregunta al crearla, y es la decisión que más gente arruina sin saberlo. El objetivo NO es una etiqueta: define **qué tipo de persona busca el algoritmo** y por qué evento cobra/optimiza. Lee este módulo antes de crear cualquier campaña nueva. Atajo mental: el objetivo correcto es casi siempre **el más cercano al dinero que tu volumen aguante** (la matriz completa está en 14).

## Los 6 objetivos ODAX y qué optimizan DE VERDAD

ODAX (Outcome-Driven Ad Experiences) es el menú de objetivos vigente. En 2026, dentro de **Sales** y **Leads** Meta te empuja por defecto a sus flujos automatizados **Advantage+ Sales** (el antiguo ASC, ver 12) y **Advantage+ Leads** — la automatización viene encendida y la apagas por sección (opt-out, ver 90). Lo que cada objetivo realmente persigue:

| Objetivo | Meta busca gente que probablemente... | Úsalo para |
|---|---|---|
| **Awareness** (Reconocimiento) | recuerde haber visto el anuncio (alcance/impresiones baratas) | branding puro, lanzamientos locales, alcance geográfico. Casi nunca para pymes |
| **Traffic** (Tráfico) | haga clic al link / landing page view | casi nada (ver abajo). Solo calentar píxel nuevo unos días o contenido editorial |
| **Engagement** (Interacción) | reaccione, comente, vea video... **o inicie una conversación** (WhatsApp/Messenger/IG Direct) | **Click-to-WhatsApp (CTWA)** — el caso #1 en Colombia (ver 50) |
| **Leads** (Clientes potenciales) | deje sus datos (formulario instantáneo, conversión en web, llamada) | captación de datos: servicios, inmobiliaria, educación, B2B |
| **App promotion** | instale o use tu app | solo si tienes app móvil |
| **Sales** (Ventas) | **compre** (Purchase u otro evento del píxel/CAPI) | e-commerce y cualquier negocio que venda online. El default si vendes |

## El error #1: campaña de Tráfico esperando ventas

Meta tiene perfilada a su gente: sabe quiénes clickean todo y nunca compran, y quiénes compran. Si optimizas por Tráfico, te entrega **clickers profesionales**: CPC de $200-500 COP que se siente baratísimo, cero ventas. Luego "Facebook no sirve". Sí sirve — le pediste clics y te dio clics.

Por qué pasa: el algoritmo optimiza LITERALMENTE el evento que le pides. "Tráfico" = landing page views. Existe un segmento enorme de usuarios que abre todo por curiosidad y nunca saca la tarjeta; esos son los más baratos de conseguir como "clic", así que Meta te los entrega primero. Estás pagando barato por la peor gente.

Regla central: **optimiza por el evento más cercano al dinero que tu volumen aguante** (la matriz volumen×calidad está en 14). Si vendes, el objetivo es Sales aunque el CPC parezca 5× más caro: pagas por compradores, no por turistas.

## Árbol de decisión rápido

```
¿Vendes online con checkout (web/Shopify)?  → SÍ → SALES (Adv+ Sales)
¿Cierras por WhatsApp / contraentrega?       → SÍ → ENGAGEMENT (WhatsApp / CTWA)
¿Necesitas datos para que ventas llame?      → SÍ → LEADS (Adv+ Leads)
¿Tienes app y quieres instalaciones?         → SÍ → APP PROMOTION
¿Eres marca grande con caja para branding?   → SÍ → AWARENESS
Ninguna clara y caja apretada                → ENGAGEMENT-WhatsApp (la más medible en Colombia)
```

## Decisiones típicas en LatAm

- **Cierras ventas por WhatsApp** (contraentrega, servicios, catálogo): objetivo **Engagement → ubicación del mensaje: WhatsApp**, optimizando por "conversaciones iniciadas". Es el caso dominante en Colombia porque el cierre vive en el chat, no en un checkout. Si ya tienes volumen y mides ventas vía CAPI, el siguiente nivel es Sales con evento de conversación calificada o Purchase reportado desde tu bot (ver 14 y 50).
- **Capturas leads**: dos sabores dentro de Leads:
  - *Formulario instantáneo* (instant form): el usuario no sale de Facebook, sus datos se autocompletan. Más volumen, menos calidad, leads más fríos. Bueno para arrancar barato.
  - *Conversión en web* (formulario en TU landing): menos volumen, más calidad (el que llena un form externo está más interesado). Requiere píxel + CAPI bien puestos (ver 22-23).
  - Receta: empieza con instant form + 2-3 preguntas de filtro (presupuesto, ciudad, urgencia); migra a web cuando el equipo de ventas se queje de calidad (guiones de cierre y calificación: skill ventas_lushows).
- **E-commerce**: Sales, siempre, desde el día 1. No "caliento el píxel con tráfico un mes" — eso entrena al píxel con clickers y arrastra el sesgo por semanas.
- **Negocio local / restaurante / servicio de cita**: Engagement-WhatsApp suele ganarle a Awareness local porque genera una acción medible (un chat) en vez de "impresiones a 2km".

## Tabla resumen objetivo → caso de uso → evento

| Tu negocio | Objetivo | Evento de optimización |
|---|---|---|
| Tienda online (web propia/Shopify) | Sales (Adv+ Sales) | Purchase (o proxy, ver 14) |
| Venta por WhatsApp / contraentrega | Engagement (WhatsApp) | Conversaciones iniciadas |
| Servicios profesionales / cursos | Leads (Adv+ Leads) | Form instantáneo o Lead en web / `LeadCalificado` vía CAPI |
| Restaurante / negocio local | Engagement (WhatsApp) | Conversaciones |
| App | App promotion | Instalación o evento in-app |
| Marca grande con presupuesto de branding | Awareness | Alcance / ad recall |

## El objetivo no rescata una oferta floja

Elegir Sales no te salva si tu oferta no convence (ver 41), tu creativo no detiene el scroll (ver 30) o tu landing no carga (desingweb-lushows). El objetivo solo decide a QUIÉN te trae Meta; convertir a esa persona es trabajo de oferta + creativo + página + cierre (ventas_lushows). Antes de culpar al objetivo, revisa esos cuatro. Y antes de gastar un peso, valida que el negocio aguanta el CAC que la pauta va a costar — viabilidad y unit economics: economist_lushows.

## Errores comunes — blacklist

- Tráfico "porque es más barato": optimizas por la métrica equivocada; barato lo inútil sigue siendo caro.
- Engagement optimizado a likes/comentarios esperando ventas: compras vanidad. Engagement solo vale con destino mensajería (WhatsApp).
- Cambiar el objetivo de una campaña andando: no se puede; crea una nueva con otro objetivo y migra presupuesto gradualmente (ver 13 y 18).
- Leads con instant form sin preguntas de filtro: recibirás curiosos que ni recuerdan haberse registrado.
- Awareness para una pyme que necesita vender este mes: el branding es un lujo de flujo de caja positivo (prioriza caja con economist_lushows).
- Elegir Sales pero optimizar por ViewContent teniendo 80 compras/semana: subestimas tu propio volumen (ver 14).
- Aceptar a ciegas el flujo Advantage+ Leads sin filtros y luego quejarte de leads basura: la automatización del objetivo no reemplaza tus preguntas de calificación.
