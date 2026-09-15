# 183 — Dashboards y visualización

Para que los datos sirvan a algo: convertir números en **decisiones**. Un buen dashboard no es bonito, es accionable: en 10 segundos ves cómo va el negocio y qué hacer hoy.

## La regla de oro: un dashboard responde una pregunta, no muestra todo

El error #1 es el "dashboard navideño": 40 gráficos, todos los colores, nadie lo mira. Un dashboard útil arranca de **una pregunta de dueño**:
- ¿Voy bien este mes o mal? → Dashboard ejecutivo (5-7 números).
- ¿Por qué cayeron las ventas? → Dashboard de diagnóstico.
- ¿Qué hago hoy? → Dashboard operativo (lista de acciones).

Antes de elegir un solo gráfico, escribe: **"Este dashboard ayuda a [quién] a decidir [qué]."** Si no puedes completar la frase, no lo construyas.

## Elegir las métricas correctas (no todas, las que mueven aguja)

Distingue tres tipos (ver 141 para KPIs):
- **Métricas de resultado (lagging):** ventas, utilidad, caja. Te dicen cómo te fue. Llegan tarde.
- **Métricas guía (leading):** leads, cotizaciones enviadas, tasa de conversión. Predicen el resultado y puedes mover hoy.
- **Métricas de salud:** margen, días de caja, % clientes que repiten. Avisan si el motor está sano.

Para un dashboard ejecutivo, máximo **5 a 9 números** (el cerebro no retiene más de un vistazo). Regla: si quitas la métrica y nadie cambiaría una decisión, sobra.

| Pregunta del dueño | Métrica que la responde | Tipo |
|---|---|---|
| ¿Estoy vendiendo? | Ventas del mes vs meta | Resultado |
| ¿Voy a vender el mes que viene? | Cotizaciones / leads activos | Guía |
| ¿Gano plata o solo facturo? | Margen bruto % | Salud |
| ¿Me alcanza la caja? | Días de caja (ver 56) | Salud |
| ¿El cliente vuelve? | % recompra / retención | Salud |

## Cada métrica necesita un contexto (un número solo no dice nada)

"Vendí 12 millones" no significa nada. Acompaña SIEMPRE cada número con al menos uno de:
- **Meta:** 12M vs meta de 15M → vas 80%.
- **Periodo anterior:** 12M vs 10M el mes pasado → +20%.
- **Tendencia:** los últimos 6 meses en una mini-línea.

Sin contexto no hay decisión. Con contexto, el número grita "actúa" o "tranquilo".

## El gráfico correcto para cada cosa

No es estética, es comunicación. Usa el más simple que cuente la historia:

| Quieres mostrar… | Usa | Evita |
|---|---|---|
| Evolución en el tiempo | Línea | Barras apiladas, pie |
| Comparar categorías (productos, ciudades) | Barras horizontales (ordenadas) | Pie con 8 tajadas |
| Un número clave vs meta | Número grande + flecha de tendencia | Velocímetro decorativo |
| Composición (partes de un todo) | Barra 100% o pie SOLO si son 2-3 partes | Pie con 6+ tajadas |
| Relación entre dos variables | Dispersión (scatter) | — |
| Embudo de ventas (ver 127) | Funnel / barras decrecientes | — |

Principios anti-confusión:
- **Ordena las barras** de mayor a menor (no alfabético): el ojo lee el ranking solo.
- **Empieza el eje Y en cero** en barras (si no, exageras diferencias y mientes sin querer).
- **Menos colores:** un color de marca + gris para el resto. El color = "mira aquí".
- **Etiqueta directo** sobre el dato; mata leyendas que obligan a ir y volver.
- Quita rejillas, sombras, 3D, degradados. Cada pixel que no informa, estorba.

## Ejemplo de dashboard ejecutivo (cifras ILUSTRATIVAS de ejemplo)

Dashboard mensual de una tienda de hongos funcionales (datos inventados para ilustrar):

```
┌─────────────────────────────────────────────────────────────┐
│  PANEL DEL MES — Mayo                          [vs Abril]    │
├──────────────┬──────────────┬───────────────┬───────────────┤
│ VENTAS       │ MARGEN BRUTO │ DÍAS DE CAJA  │ % RECOMPRA    │
│ $14.2M       │ 58%          │ 42 días       │ 31%           │
│ ▲ +18% │ 80% │ ▲ +3 pts     │ ▼ -6 días ⚠   │ ▲ +4 pts      │
│ de meta 15M  │              │               │               │
├──────────────┴──────────────┴───────────────┴───────────────┤
│ VENTAS ÚLTIMOS 6 MESES (línea)   │ TOP PRODUCTOS (barras)   │
│        ╱╲    ╱                    │ Melena    ████████ 45%   │
│   ╱╲  ╱  ╲  ╱                     │ Cordyceps ████ 28%       │
│  ╱  ╲╱    ╲╱                      │ Ganoderma ███ 19%        │
│                                   │ Combos    █ 8%           │
├───────────────────────────────────┴──────────────────────────┤
│ EMBUDO: 320 chats → 110 interesados → 38 negocian → 22 venden│
│ Conversión chat→venta: 6.9% (mes pasado 8.1%) ⚠              │
└─────────────────────────────────────────────────────────────┘
ACCIÓN DE LA SEMANA: caja bajó 6 días y conversión cayó 1.2 pts →
revisar por qué se enfrían los chats (¿demora de respuesta?).
```

Fíjate: 4 números clave arriba, cada uno con comparación; abajo el "por qué" (tendencia, mix, embudo); y al final **una sola acción**. Eso es accionable, no decorativo. (Para de dónde salen estos números, ver 148 sobre fuentes/recolección de datos; para definir cada KPI, ver 141; para análisis financiero detrás de margen y caja, ver 56 y 144.)

## Regla del semáforo: que el dashboard "grite" qué mirar

Marca cada métrica con verde / amarillo / rojo según umbrales que TÚ defines:
- Verde: dentro de meta. No tocar.
- Amarillo: 80-95% de meta o cayendo. Vigilar.
- Rojo: bajo umbral crítico. Actuar hoy.

Así, en lugar de leer 9 números, tu ojo va directo al rojo. El dashboard hace el trabajo de priorizar por ti.

## Herramientas simples (de menos a más)

Empieza por lo más barato que funcione:
1. **Google Sheets / Excel:** 90% de los negocios pequeños viven aquí perfectamente. Tablas dinámicas + 3-4 gráficos + formato condicional (semáforo automático). Gratis, lo entiendes, lo controlas.
2. **Looker Studio (Google, gratis):** conecta Sheets o tu fuente y hace dashboards web compartibles por link. Buen salto cuando varias personas necesitan verlo.
3. **El dashboard de tu propia herramienta:** muchos sistemas (POS, e-commerce, tu propio software) ya traen panel. Úsalo antes de construir uno nuevo.
4. **Power BI / Metabase / Tableau:** solo cuando los datos crecen y necesitas conectar varias fuentes. No empieces aquí: es matar mosca a cañonazos.

Consejo de aliado: la mejor herramienta es la que **vas a actualizar de verdad cada semana**. Un Sheets vivo gana a un Power BI hermoso que nadie abre.

## Cadencia: el dashboard sin rutina no sirve

Un dashboard es un hábito, no un archivo. Define:
- **Diario (operativo):** ventas del día, caja, pedidos pendientes. 1 minuto al abrir.
- **Semanal (táctico):** embudo, conversión, top productos. 15 min, decide 1-2 acciones.
- **Mensual (estratégico):** márgenes, recompra, tendencia, vs meta. 1 hora, ajusta el plan.

Si no hay reunión/ritual donde se mire, el dashboard muere. La métrica que nadie revisa no existe.

## Errores comunes

- **Dashboard decorativo:** lindo, lleno, inútil. Si no termina en una acción, es arte, no gestión.
- **Demasiadas métricas:** 30 números = 0 decisiones. Menos es más.
- **Vanity metrics:** seguidores, "me gusta", visitas, sin conexión a plata. Suben el ego, no el banco (ver 141).
- **Número sin contexto:** "vendí X" sin meta ni comparación. Imposible decidir.
- **Gráficos que mienten:** eje Y que no empieza en cero, pie de 8 tajadas, 3D. Confunden o engañan.
- **Datos sucios/manuales:** si la fuente es un Excel que copias a mano, habrá errores. Automatiza la entrada antes de confiar (ver 148).
- **No definir umbrales:** sin verde/amarillo/rojo, todo parece igual de importante.
- **Construir y abandonar:** sin cadencia de revisión, el mejor dashboard se vuelve fósil.

## Nota de país

Si el dashboard incluye impuestos, retenciones o márgenes después de impuestos, esas reglas cambian por país y año: **pregunta país/ciudad y verifica la norma vigente** antes de cablear fórmulas (ver 21 para conseguir datos reales). El método de visualización es universal; los datos fiscales no.

## Siguiente paso típico

Define en una frase qué decisión debe ayudar a tomar tu dashboard, elige los 5-7 números clave (cada uno con meta o comparación) y arma una primera versión en Google Sheets con semáforo. Agéndate 15 minutos cada lunes para mirarlo y sacar 1 acción.
