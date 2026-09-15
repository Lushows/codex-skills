# 328 · Pricing page y packaging (la página que más dinero deja por píxel)

> El precio no es un número en una tabla: es packaging (qué va en cada tier) + anchoring (cómo lo
> percibe el ojo) + value-metric (qué crece con el valor del cliente). El diseño de la página es el
> último 10% que multiplica los otros tres.

## Los tres niveles del problema (resolver en orden)
1. **Value-metric**: la unidad por la que cobras. Debe crecer con el valor que el cliente recibe
   (Slack: usuarios activos; Stripe: % de volumen; Vercel: uso). Mala value-metric (ej. "por feature")
   = techo de ingresos y fricción. Buena = expansion revenue automático (NRR sube sin vender de nuevo).
2. **Packaging**: qué features van en Free/Pro/Enterprise. Regla: el tier de en medio debe ser el que
   quieres vender; el caro existe para anclar; el barato para activar.
3. **Página**: jerarquía visual, anchoring, copy, fricción de checkout. Lo que cubre este doc.

## Estructura de tiers (3-4, no 6)
| Tier | Rol psicológico | Diseño |
|---|---|---|
| Free / Trial | Activación, captura de leads | CTA suave, sin tarjeta |
| **Pro (destacado)** | El que quieres vender | Badge "Más popular", borde/sombra, escalado |
| Business / Team | Upsell, expansion | Features de colaboración/seats |
| Enterprise | **Ancla** + deals grandes | "Contactar ventas", sin precio visible |

- 3-4 columnas máximo. Más → parálisis de elección, todos eligen el barato o ninguno.
- El tier destacado se **resalta visualmente** (no solo color): escala 1.05, borde, badge, primero en
  móvil. El ojo cae ahí.

## Anchoring (el ancla hace barato lo demás)
- Pon el tier **caro a la izquierda o el Enterprise sin precio**: el cerebro ancla alto, el Pro parece ganga.
- **Annual default**: toggle mensual/anual con anual preseleccionado y "ahorra 20%". Tachado del precio mensual.
- Precio mensual mostrado aunque cobres anual ("$20/mes facturado anual") — el número pequeño ancla mejor que "$240/año".
- Charm pricing ($19 vs $20) funciona en self-serve B2C; en B2B alto-ticket, números redondos transmiten premium.

## Copy y fricción
- **Value-first, no feature-first**: "Para equipos que escalan", no "100 GB de storage". Las features
  van en la tabla comparativa de abajo, no en el headline del tier.
- CTA por tier con verbo claro y distinto: "Empezar gratis" / "Probar Pro" / "Hablar con ventas".
- **Tabla comparativa** debajo de las cards (feature × tier con checks). Sticky header al hacer scroll.
- **FAQ** al pie: cancelación, prorrateo, qué pasa al exceder el límite, métodos de pago. Reduce el churn
  pre-compra y los tickets de soporte.
- Quitar fricción del checkout: ver [[294-stripe-a-fondo]] — Payment Element, prorrateo, trials sin tarjeta.
- Social proof cerca del CTA: logos, "X equipos confían", testimonios. Reduce el riesgo percibido.

## Errores caros
- Esconder el precio en todos los tiers ("contactar ventas" en Pro) → el self-serve se va. Solo Enterprise.
- 6+ tiers o add-ons infinitos → el usuario no decide. Empaqueta.
- Value-metric que castiga el crecimiento (cobrar por algo que el cliente quiere minimizar) → resentimiento.
- No mostrar qué pasa al pasar de Free a Pro (el gap de valor debe ser obvio y deseable).
- Toggle anual que no recalcula visiblemente el ahorro → se pierde el anclaje.

Cruza con [[102-pricing-monetizacion-2026]] y [[294-stripe-a-fondo]].
