# 18 — Distribución de presupuesto

Lee este módulo cuando tienes que decidir cuánto le pones a cada campaña, cuando una campaña topa presupuesto y otra no gasta, o cuando alguien quiere repartir la plata "en partes iguales" sin lógica. La distribución de presupuesto no es democracia: no todas las campañas merecen lo mismo. El principio rector de Google es **Search-first**: la plata va primero a **capturar la demanda que ya existe** (intención), porque es el dinero que más rápido y más barato convierte. Lo demás expande sobre esa base.

## Search-first: el orden de prioridad del dinero

| Prioridad | Campaña | Por qué primero | Cuánto del presupuesto (cuenta típica) |
|---|---|---|---|
| 1 | **Search — Marca** | CPC bajísimo, conversión altísima; defiende lo que es tuyo (ver 39) | 5-15% (poco, pero intocable) |
| 2 | **Search — Genérico** | Captura intención real; tu motor de conversiones y de señal (ver 03, 14) | 50-70% |
| 3 | **PMax / Shopping** | Expande sobre la señal que generó Search (ver 12, 35) | 20-35% |
| 4 | **Demand Gen / Display / Video** | Remarketing primero; awareness solo con sobra (ver 24, 41) | 0-15% |

**La regla:** no le quitas a Search genérico para alimentar Display a frío. Eso es mover plata de lo que convierte a lo que no. Solo subes el escalón siguiente cuando el anterior **topa presupuesto consistentemente** y **sigue rentable** (ver 73, 74). "Topa presupuesto" en la interfaz aparece como **"limitado por presupuesto"** o un *impression share perdido por presupuesto* alto — esa es tu señal de que hay demanda que no estás capturando y vale la pena subir ahí, no abrir otra cosa.

## Marca vs genérico vs PMax: cómo no engañarte

Estas tres compiten por crédito y se canibalizan si no las separas:

- **Marca**: CPC de centavos, ROAS altísimo en el reporte. **Engaña**: gran parte de esas ventas las tendrías gratis por orgánico. No le metas presupuesto grande "porque rinde"; ponle lo justo para defender el nombre y que no tope (ver 39). Su ROAS no es incremental (ver 65).
- **Genérico**: aquí está la verdad de tu cuenta. CPC más caro, ROAS más realista. Es donde **inviertes para crecer** porque es demanda nueva que no tendrías sin pauta.
- **PMax**: con **brand exclusions** para que no se robe el crédito de marca (ver 12). Su presupuesto expande, no reemplaza Search.

Mide cada una por su **incrementalidad**, no por su ROAS reportado (ver 65). El genérico con ROAS 250% **real** suele ser mejor inversión que la marca con ROAS 900% **no incremental**: la marca solo cobra crédito por ventas que ya tenías.

## Shared budgets (presupuestos compartidos)

Un **shared budget** es un presupuesto único que varias campañas comparten; Google reparte hacia donde mejor rinda en el momento.

| A favor | En contra |
|---|---|
| Menos microgestión; el algoritmo manda plata a lo que convierte | **Oculta** cuánto consumió cada campaña; reporting más difícil (ver 67) |
| Útil cuando varias campañas son del mismo tema/objetivo | Una campaña hambrienta puede ahogar a otra que querías proteger |
| Evita que campañas similares se queden sin gasto | **No mezcles marca con genérico** en un shared budget (canibaliza) |

Úsalo para campañas **homogéneas** (varias Search genéricas del mismo objetivo y CPA target). **No** metas marca y genérico al mismo shared budget: la marca, con su CPC barato, se chupará el gasto y matará al genérico.

## Repartir con POCO presupuesto (1.5-3M COP/mes)

Con poca plata, **fragmentar es muerte**: cada campaña necesita ~3x el CPA diario para que Smart Bidding respire (ver 13, 15) y ~15-30 conv/mes para calibrar. Con 2M COP/mes (~67.000 COP/día):

- Concéntralo: **Marca (poco) + 1 Search genérico fuerte**. Punto.
- No abras PMax todavía si eso deja a Search genérico con <30.000 COP/día.
- Cuando el genérico tope presupuesto y siga rentable varios días, **entonces** sube +20% o abre el siguiente escalón (ver 73).
- Regla de oro: **mejor 1 campaña bien alimentada que 4 muertas de hambre.**

### Ejemplo numérico — 2M COP/mes

| Campaña | Asignación | COP/mes | COP/día | Lógica |
|---|---|---|---|---|
| Search — Marca | 12% | 240.000 | ~8.000 | Defensa barata, no más |
| Search — Genérico | 78% | 1.560.000 | ~52.000 | El motor; toda la fuerza aquí |
| PMax / remarketing | 10% | 200.000 | ~6.700 | Solo si ya hay señal; si no, 0% y todo al genérico |

Si el CPA genérico es ~25.000 COP, esos ~52.000/día dan margen para ~2 conv/día ≈ 60/mes: suficiente para calibrar tCPA. Eso **no pasaría** si partieras los 2M en cinco campañas.

## Repartir con MUCHO presupuesto

Con holgura puedes correr el stack completo (marca + varias genéricas segmentadas + PMax + remarketing):

- Segmenta el genérico por intención/tema para escalar **horizontal** (ver 73): no metas más plata a un grupo saturado, abre otro tema con demanda.
- Usa **shared budgets** por grupo homogéneo para no microgestionar.
- Sube presupuestos en **escalones de ≤20-30%** para no resetear aprendizaje de golpe (ver 13, 74).
- Reasigna **mensualmente**: quita a lo que topó CPA (rinde mal y no mejora) y dale a lo que tiene techo (rinde bien y está limitado por presupuesto) (ver 60, 64).

## Calendario: el presupuesto no es fijo todo el año

El reparto cambia con la estacionalidad (ver 19). Sube presupuesto entrando a un pico (madres, Amor y Amistad, BFCM, navidad) **en escalones** y bájalo **a tiempo** post-pico para no pagar CPCs altos sin la conversión que los justificaba. En Colombia, considera micro-subidas en **quincenas** (15 y 30) si tu producto siente el ciclo de pago (ver 19, 60).

## Errores comunes — blacklist

- **Repartir en partes iguales** sin lógica de prioridad: alimentas Display a frío con la plata que debía ir a Search genérico.
- **Meterle presupuesto grande a Marca "porque rinde"**: su ROAS no es incremental; le quitas a lo que sí crece (ver 39, 65).
- **Fragmentar 2M COP en 5 campañas**: ninguna llega al volumen mínimo de aprendizaje; todas mueren de hambre (ver 13).
- **Marca y genérico en el mismo shared budget**: la marca barata se come el gasto y mata al genérico (canibalización de presupuesto).
- **Subir el presupuesto +200% de golpe** para escalar: reseteas aprendizaje y desestabilizas el CPA (ver 13, 74).
- **No reasignar nunca**: dejas plata en campañas topadas de CPA mientras otras con techo se quedan sin gasto (ver 64).
- **Ignorar "limitado por presupuesto"** en el genérico rentable: hay demanda comprable que estás dejando ir (ver 73).
- **Juzgar reparto por ROAS reportado** sin incrementalidad: sobre-inviertes en canales que solo reclaman crédito (ver 65).
- **Mismo presupuesto en temporada muerta que en pico**: desperdicias en ambos extremos (ver 19).
