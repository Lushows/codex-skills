# 21 — Tipos de concordancia 2026

Lee este módulo cuando estás creando keywords y no sabes si ponerlas en broad, phrase o exact — o cuando alguien te dijo "broad es plata tirada" y eso era verdad en 2018 pero ya no en 2026. La **concordancia** (match type) define cuánto se parece la búsqueda real a tu keyword para que tu anuncio aparezca. Elegir mal aquí es la diferencia entre capturar intención o regalarle plata a Google. Frame que manda: Google captura intención, pero la concordancia decide **qué tan ancha** abres la red. Más ancha = más demanda nueva pero más basura; más cerrada = más control pero menos descubrimiento. El oficio es saber cuándo abrir y cuándo apretar.

## Los 3 tipos hoy — qué disparan

| Tipo | Cómo se escribe | Qué dispara | Control |
|---|---|---|---|
| Amplia (broad) | `calculadora de costos` | Búsquedas relacionadas por **significado e intención**, no solo por la palabra | Bajo (lo gobiernan el algoritmo + tus negativos) |
| De frase (phrase) | `"calculadora de costos"` | Búsquedas que contienen el **significado** de la frase, en cualquier orden razonable | Medio |
| Exacta (exact) | `[calculadora de costos]` | La búsqueda con **ese mismo significado** (incluye sinónimos cercanos y plurales) | Alto |

Ojo: desde hace años los tres son "semánticos". Exacta ya **no** es literal palabra por palabra — Google mete sinónimos y variantes cercanas. *[plantilla de costos]* puede disparar con "plantilla para costear platos". Por eso los negativos importan en los tres (ver 22). Ejemplos de qué dispara cada uno con la raíz *calculadora de costos para restaurante*:

```
BROAD   calculadora de costos para restaurante
        → "software costeo recetas", "control food cost bar",
          "excel para sacar precio de plato", "app gastos cocina"
PHRASE  "calculadora de costos para restaurante"
        → "calculadora de costos para mi restaurante",
          "necesito calculadora de costos para restaurante pequeño"
EXACT   [calculadora de costos para restaurante]
        → "calculadora de costos para restaurantes" (plural),
          "calculador de costos restaurante" (variante cercana)
```

## Por qué broad resucitó (y cómo)

El broad de 2015 era tonto: leía palabras sueltas y te metía en cualquier búsqueda que las tuviera. *Calculadora de costos* te traía "calculadora científica". Por eso todo el mundo le huía.

En 2026 broad cambió porque le pusieron cerebro encima: el **Smart Bidding** (pujas automáticas con IA — ver 13). El broad moderno lee la búsqueda **+ el contexto del usuario** (su historial, dispositivo, ubicación, hora, idioma, señales de intención) y decide en milisegundos si vale la pena pujar y cuánto. Ya no es "¿están las palabras?", es "¿esta persona, en este momento, busca lo que vendo y probablemente convierte?".

**El combo moderno que funciona:**

```
Keyword broad  +  Smart Bidding (tCPA o tROAS)  +  lista de negativos sólida
```

- El **broad** abre el alcance y encuentra búsquedas que tú nunca habrías escrito a mano (la long-tail real, el lenguaje que no imaginaste).
- El **Smart Bidding** filtra: solo puja fuerte donde hay probabilidad de conversión. Sin Smart Bidding, broad SÍ vuelve a ser plata tirada — necesita un cerebro de pujas que mida conversiones reales (ver 14 conversion-tracking; sin conversiones bien medidas, no hay combo).
- Los **negativos** son el cinturón de seguridad: el broad se va a equivocar y traer basura; tú la podas cada semana (ver 22, 68).

Sin los tres, broad falla. Con los tres, suele ganarle a exact en volumen de conversiones al mismo CPA. Es la recomendación por defecto de Google **y** de la mayoría de buyers serios en 2026 — pero solo si haces la tarea de negativos. Dato honesto de jun-2026: Google empuja broad agresivamente en sus recomendaciones automáticas (la pestaña "Recomendaciones" y el "auto-apply") porque le conviene gastar tu presupuesto; revisa antes de aceptar, no apliques en automático.

## Cuándo sigues usando exact y phrase

Broad no es para todo. Usa **exacta** cuando:
- La keyword es tu **marca** (no quieres que el algoritmo se la lleve a búsquedas raras — ver 39).
- Tienes una keyword transaccional **probada** que convierte y quieres control quirúrgico del CPC.
- Presupuesto muy chico y necesitas certeza de a qué entras (cada peso cuenta).

Usa **frase** cuando:
- Quieres un punto medio: más alcance que exacta, más control que broad.
- Estás abriendo un nicho nuevo y aún no tienes datos de conversión para que el Smart Bidding gobierne bien el broad.

**Estructura típica recomendada:** una campaña con keywords broad gobernadas por Smart Bidding + negativos para descubrir y escalar, y keywords exact de tus términos ganadores probados para control. No "broad o exact" — es **broad para descubrir, exact para exprimir**. Tabla de decisión rápida:

| Situación | Concordancia |
|---|---|
| Cuenta nueva, sin conversiones medidas | Frase + exacta |
| Cuenta con 30+ conversiones/mes y tCPA estable | Broad + negativos |
| Keyword de marca | Exacta |
| Término probado que convierte caro y quieres control | Exacta |
| Quieres descubrir demanda nueva | Broad (vigilado) |

## AI Max for Search — el broad con esteroides

Google empuja **AI Max for Search**, que amplía tus keywords automáticamente y mete creatividad de texto generada por IA (parecido a un broad recargado, ver 90). Útil para encontrar demanda nueva, pero **vigílalo con negativos religiosamente** o te mete en búsquedas que no querías. Activa AI Max solo cuando ya tengas conversiones medidas, Enhanced Conversions puesto (ver 28) y rutina de términos de búsqueda (ver 68); si no, es manejar a ciegas. No mezcles AI Max con campañas de marca pura — se las puede llevar a genérico y diluir tu control.

## Errores comunes — blacklist

1. **Broad sin Smart Bidding.** Vuelve a ser el broad tonto de 2015. Si no tienes conversiones bien medidas (ver 14), usa frase o exacta primero.
2. **Broad sin rutina de negativos.** El broad SIEMPRE trae basura; tu trabajo es podarla semanal (ver 22). Sin eso, quema presupuesto.
3. **Creer que exacta es literal.** Hoy incluye sinónimos y variantes. Igual necesita negativos.
4. **Meter todo en broad de un día para otro en una cuenta nueva.** Sin datos de conversión el algoritmo no sabe filtrar. Arranca con frase/exacta, acumula conversiones, luego abre broad.
5. **Pujar la misma keyword en broad, phrase y exact en el mismo conjunto sin estructura.** Compites contigo mismo. Deja que la concordancia más relevante gane y canaliza con negativos.
6. **Apagar AI Max o el broad porque "trajo búsquedas raras" sin antes meter negativos.** El problema no era el broad; era que no lo vigilaste.
7. **No revisar términos de búsqueda tras abrir broad.** Es donde ves qué encontró el algoritmo — bueno y malo (ver 68). Saltártelo es manejar a ciegas.
8. **Aceptar las "Recomendaciones" de Google en automático.** El auto-apply mete broad y sube presupuestos a conveniencia de Google. Revisa cada una antes de aplicar.
