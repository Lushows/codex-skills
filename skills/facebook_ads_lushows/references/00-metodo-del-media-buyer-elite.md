# 00 — Método del media buyer de élite

Este es el módulo raíz de toda la biblioteca: el proceso completo que sigue un media buyer profesional (la persona que compra publicidad en Meta de forma rentable) desde que recibe un negocio hasta que escala campañas. Léelo primero, siempre. Los demás módulos son piezas que este proceso invoca bajo demanda.

## El orden de impacto (grábatelo)

**Oferta > Creativo > Estructura > Audiencia.** En Meta 2026, con el motor Andromeda (el sistema de machine learning que decide qué anuncio mostrarle a quién) haciendo el targeting por ti, lo que mueve resultados es, en este orden:

1. **Oferta** — qué vendes, a qué precio, con qué gancho. Una oferta mala no la salva ningún ad. ~50% del resultado.
2. **Creativo** — el anuncio (video/imagen + texto) ES el targeting hoy: Andromeda lo lee y decide a quién mostrarlo (ver 30, 92). ~30%.
3. **Estructura** — cuántas campañas/ad sets, cómo repartes presupuesto. ~15%.
4. **Audiencia** — lo que menos importa: broad (sin segmentar) gana en la mayoría de cuentas modernas (ver 20). ~5%.

Si un cliente te pide "cambiar audiencias" cuando el problema es la oferta, estás puliendo la silla del Titanic. La proporción se invirtió frente a 2018: antes la audiencia era el 60% del trabajo; hoy la cedimos a la máquina (ver 02).

## Lo que cambió en 2026 (contexto obligatorio)

Meta **unificó todo en Advantage+** (feb-2026): la campaña "manual" desapareció como tipo; ahora toda campaña nace con AI activado por default y tú haces *opt-out* sección por sección si quieres control. ASC pasó a llamarse **"Advantage+ Sales"**; existe **Advantage+ Leads** (ver 12). El motor sobre el que corre todo es **GEM** (modelo generativo, nov-2025) montado sobre **Andromeda**. Consecuencia para tu método: pelear contra la automatización ya no es opción; tu trabajo es alimentarla con oferta, creativo y señal limpios (detalle en `actualizacion-2026-06`).

## El proceso en 7 fases

### Fase 1 — Diagnóstico (antes de tocar Ads Manager)
Responde por escrito:
- ¿Qué vende y cuál es el **margen bruto** por unidad? (precio − costo del producto − envío − pasarela). Si el margen no aguanta un CPA realista, NO pautes → rutea a economist_lushows (ver 07).
- ¿Cuál es el **canal de cierre**? En Colombia/LatAm casi siempre es WhatsApp + contraentrega o Nequi/Bancolombia. Eso cambia toda la estructura (campañas CTWA, ver 50, 53 y glosario en 09).
- ¿Presupuesto mensual real en COP? (ver 07 para el mínimo viable).
- ¿Historial? Una cuenta con dataset (antes "píxel") viejo y datos arranca más rápido que una virgen (ver 05, 13).

**Cálculo de servilleta obligatorio**: margen bruto × tasa de cierre del chat. Ejemplo: producto de 89.000 COP, margen 50.000, cierra 1 de cada 4 conversaciones → puedes pagar hasta ~12.500 COP por conversación de WhatsApp y seguir en break-even. Ese es tu CPA techo. Sin este número no pautas.

### Fase 2 — Fundación técnica
Sin esto, todo lo demás es ruido:
1. Business Portfolio bien montado, 2FA, dominio verificado (ver 04).
2. Dataset (píxel) instalado y eventos verificados (ver 05).
3. CAPI activa con **EMQ ≥ 8** (ver 06) — el piso subió: en la era Andromeda la calidad de datos es la mitad del juego.
4. Catálogo de productos si es e-commerce (ver 55, 56).

### Fase 3 — Estructura inicial
Arranca simple: **1 campaña Advantage+ Sales, 1 ad set broad, 10-15 creativos conceptualmente distintos**. Ojo: el viejo consejo de "3-5 creativos" quedó corto. Andromeda colapsa los casi-duplicados en un mismo Entity ID, así que necesitas variedad CONCEPTUAL (ángulos, formatos, ganchos genuinamente distintos), no 5 colores del mismo ad (ver 31, 38, 92). Cuenta pequeña = menos fragmentación = sale de learning antes. Full-funnel solo cuando el volumen lo justifique (ver 03).

### Fase 4 — Testing
Las primeras 2-4 semanas son **compra de datos**, no rentabilidad. Testea ángulos de creativo (dolor, beneficio, prueba social, demostración), no colores de botón (ver 17, 38). Mata lo que no funciona con reglas, no con pánico (ver 70, 71). Recuerda: la vida útil de un creativo ganador es **2-4 semanas** antes de fatigarse (ver 39); el testing no termina nunca, es un grifo siempre abierto.

### Fase 5 — Lectura de datos
Mira las métricas en este orden: gasto → CPA/costo por conversación → CTR outbound y thumbstop del creativo → frecuencia (ver 60, 61). Decisiones solo con significancia: regla práctica, **mínimo 50 conversiones o 3-5× tu CPA objetivo gastado** antes de juzgar un ad set. Y mide la verdad, no la atribución inflada: la **atribución incremental** de Meta (ver 16, 65) reporta MENOS conversiones, pero son las reales.

### Fase 6 — Optimización disciplinada
Una variable a la vez. Cambios grandes resetean learning phase (la fase donde el sistema necesita ~50 conversiones/semana por ad set para estabilizar, ver 13). Calendario fijo: revisas a diario, decides 2 veces por semana (ver 19, 70).

### Fase 7 — Escalado
Solo cuando hay 7-14 días estables de CPA aceptable. Vertical (subir presupuesto ≤20-30% cada 2-3 días, ver 72) u horizontal (duplicar ganadores, nuevos creativos del mismo ángulo, ver 73). Para escalar sin que el CPA se dispare, considera cost caps o Minimum ROAS (ver 15, 74).

## Tabla de decisión rápida (qué módulo abrir según el síntoma)

| El cliente dice... | Causa probable | Módulo |
|---|---|---|
| "El CPA subió de la nada" | Fatiga creativa o competencia estacional | 39, 75, 77 |
| "Gasto pero no vendo" | Oferta/cierre/medición, no audiencia | 07, 41, 53 |
| "¿Con cuánto empiezo?" | Matemática de learning phase | 07, 18 |
| "Me rechazaron el anuncio" | Compliance | 08, 44, 93 |
| "Quiero escalar" | Hay base estable o no | 72, 73, 74 |
| "El ROAS de Meta no cuadra con el banco" | Atribución vs incrementalidad | 16, 64, 65 |

## Cómo usar esta biblioteca de módulos

No cargues los 100 módulos: carga bajo demanda según la fase. Diagnóstico → 07. Setup → 04, 05, 06. Entender el sistema → 01, 02. Estrategia → 03. Compliance antes de publicar → 08. ¿Término desconocido? → 09. El cierre en WhatsApp es de ventas_lushows; la landing es de desingweb-lushows; la marca y el creativo visual fino, de directorcreativo_lushows; los unit economics, de economist_lushows; el canal Google es google_ads_lushows y TikTok tiktok_ads_lushows.

## Mentalidad del profesional

- **Paciencia estadística**: 1 día malo no es tendencia; 200 USD gastados no validan nada con un CPA de 80 USD.
- **Honestidad con números**: si el ROAS real (ventas atribuibles / gasto, medido por incrementalidad o MER) no da, se dice. El cliente paga por verdad, no por dashboards bonitos.
- **El algoritmo es tu empleado, no tu enemigo**: dale señal limpia (CAPI, EMQ 8+), creativos variados y presupuesto estable, y deja de microgestionarlo. En 2026 hay MENOS botones que tocar a propósito: Meta quiere que pongas tu energía en oferta y creativo.

## Errores comunes — blacklist

- **Pautar sin margen calculado**: descubres en el mes 2 que cada venta te cuesta plata. El diagnóstico y el CPA techo van primero.
- **10 ad sets con 5 USD/día cada uno**: ninguno junta 50 conversiones/semana, todos viven en learning limited. Consolida.
- **Tocar la campaña todos los días**: cada edición significativa resetea el aprendizaje. Decide en calendario.
- **Optimizar audiencias antes que creativos**: en la era Andromeda el creativo es el targeting; estás moviendo la palanca pequeña.
- **Lanzar solo 3 creativos casi idénticos**: colapsan en un Entity ID y Andromeda no tiene de dónde elegir; necesitas 10-15 conceptualmente distintos.
- **Juzgar con 10 clics**: varianza pura. Espera volumen mínimo.
- **Creer el ROAS de plataforma como verdad absoluta**: la atribución solo-clic (sin view, ene-2026) ya recortó; usa incrementalidad y MER para decidir.
- **Copiar la estructura de un gurú de cuenta grande en una cuenta de 300 USD/mes**: la estructura depende del presupuesto (ver 07).
- **Saltarse compliance "porque el anuncio es inocente"**: un rechazo evitable mancha el historial de la cuenta (ver 08, 93).
