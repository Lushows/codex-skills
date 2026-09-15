# 59 — Valoración y ROI

Sirve para decidir, con números, si una inversión o proyecto vale la pena: cuánto ganas por cada peso que pones, en cuánto tiempo lo recuperas y si el dinero del futuro realmente compensa. Cuatro métricas — ROI, payback, VPN y TIR — y cuándo usar cada una.

## Primero: los 4 conceptos en lenguaje humano

| Métrica | Pregunta que responde | En una frase |
|---|---|---|
| **ROI** (Retorno sobre la inversión) | ¿Cuánto gané por cada peso invertido? | Ganancia neta ÷ lo que invertí |
| **Payback** (Periodo de recuperación) | ¿En cuánto tiempo recupero lo que puse? | Inversión ÷ flujo que entra por periodo |
| **VPN / VAN** (Valor Presente Neto) | ¿Vale la pena hoy, contando que el dinero futuro vale menos? | Suma de flujos futuros "traídos a hoy" menos la inversión |
| **TIR** (Tasa Interna de Retorno) | ¿Qué rentabilidad anual % me da el proyecto? | El % de interés que hace que el VPN sea cero |

Idea clave detrás de VPN y TIR: **mil pesos hoy valen más que mil pesos dentro de un año** (puedes invertirlos, hay inflación, hay riesgo). Eso se llama "valor del dinero en el tiempo". Para traer plata del futuro a hoy se usa una **tasa de descuento** (ver más abajo).

## 1) ROI — el más simple y el más usado

**Fórmula:** ROI = (Ganancia neta ÷ Inversión) × 100

**Ejemplo ilustrativo (cifras inventadas):** inviertes 5.000.000 en una máquina de empaque. Durante su vida te genera 8.000.000 de ganancia neta total.
- Ganancia neta = 8.000.000 − 5.000.000 = 3.000.000
- ROI = 3.000.000 ÷ 5.000.000 = **60%**

Lectura: por cada 100 que pusiste, recuperaste los 100 y ganaste 60 extra.

**Cuándo importa:** comparar opciones rápidas, justificar una compra, medir una campaña de marketing (ver 82). **Su gran debilidad:** ignora el tiempo. Un ROI del 60% en 6 meses es excelente; el mismo 60% en 8 años es mediocre. Por eso casi nunca decidas solo con ROI.

## 2) Payback — ¿en cuánto recupero mi plata?

**Fórmula simple:** Payback = Inversión ÷ Flujo neto por periodo

**Ejemplo ilustrativo:** inviertes 12.000.000 y el proyecto te deja 3.000.000 de flujo neto al año.
- Payback = 12.000.000 ÷ 3.000.000 = **4 años**

Si los flujos son distintos cada año, lo acumulas hasta llegar a la inversión:

| Año | Flujo del año | Acumulado |
|---|---|---|
| 1 | 4.000.000 | 4.000.000 |
| 2 | 5.000.000 | 9.000.000 |
| 3 | 6.000.000 | 15.000.000 ← ya pasó los 12M |

Recuperas en algún punto del año 3 (a mitad de año aprox.).

**Cuándo importa:** cuando el RIESGO y la LIQUIDEZ mandan. Negocio pequeño, capital escaso, entorno incierto → un payback corto (1–2 años) es oro porque recuperas antes de que cambie el mundo. **Debilidad:** no le importa lo que pasa DESPUÉS de recuperar, ni el valor del dinero en el tiempo. Úsalo como filtro, no como veredicto final.

## 3) VPN / VAN — el veredicto financiero serio

Trae todos los flujos futuros a valor de hoy con una tasa de descuento y les resta la inversión.

**Fórmula:** VPN = −Inversión + Σ [ Flujo_año / (1 + tasa)^año ]

La **tasa de descuento** es tu "costo de oportunidad + riesgo": el % que esperarías ganar en una alternativa parecida. Es un supuesto tuyo, no un dato externo. Regla práctica: empieza con algo entre 10% y 20% según riesgo, y prueba con varias (ver "Análisis de sensibilidad" más abajo). No copies tasas de otros países sin verificar inflación/tasa de tu país (ver 21 para conseguir datos reales).

**Ejemplo ilustrativo (tasa de descuento 12%):** inversión hoy de 10.000.000, flujos de 4.000.000 al año por 3 años.

| Año | Flujo | Factor 1/(1,12)^año | Valor a hoy |
|---|---|---|---|
| 1 | 4.000.000 | 0,893 | 3.571.000 |
| 2 | 4.000.000 | 0,797 | 3.189.000 |
| 3 | 4.000.000 | 0,712 | 2.847.000 |
| | | **Suma** | 9.607.000 |

VPN = 9.607.000 − 10.000.000 = **−393.000**

**Regla de oro:** si VPN > 0 → crea valor, adelante. Si VPN < 0 → destruye valor, NO. Aquí da negativo: aunque en plata "bruta" entran 12M por 10M, al castigar el dinero futuro al 12% el proyecto NO compensa. Esto es exactamente lo que ROI y payback no te muestran.

**Cuándo importa:** decisiones grandes, de varios años, donde el tiempo y el riesgo pesan (abrir local, comprar maquinaria, lanzar línea nueva). Es la métrica más confiable para decir sí/no.

## 4) TIR — la rentabilidad anual en %

La TIR es la tasa de descuento que haría el VPN = 0. Es el "% de interés efectivo" que rinde el proyecto.

**Regla de oro:** si TIR > tu tasa de descuento (tu mínimo exigido) → conviene. Si TIR < tu mínimo → no.

**Ejemplo ilustrativo:** inviertes 10.000.000 y recibes 13.310.000 al final del año 3. ¿Qué % anual rindió?
- 10.000.000 × (1 + TIR)^3 = 13.310.000 → (1+TIR)^3 = 1,331 → 1+TIR = 1,10 → **TIR = 10% anual**

Si tu mínimo exigido era 12%, lo rechazas (rinde menos de lo que pides). Si era 8%, lo aceptas.

Nota práctica: la TIR de flujos variables NO se calcula a mano. Usa Excel/Google Sheets con `=TIR(rango)` (en inglés `=IRR`) y para VPN `=VNA(tasa; rango)` (`=NPV`). Pon los flujos en columna (el año 0 negativo = la inversión).

## Cómo decidir: qué métrica manda según el caso

| Situación | Métrica que pesa más | Por qué |
|---|---|---|
| Compra chica, decisión rápida | ROI | Fácil de comunicar |
| Capital escaso, alto riesgo | Payback | Recuperar pronto importa más que maximizar |
| Inversión grande, varios años | **VPN** | Único que juzga bien el sí/no |
| Comparar % entre proyectos distintos | TIR | Habla en lenguaje de rentabilidad anual |
| Decisión seria de verdad | VPN + TIR + payback juntos | Se complementan; nunca una sola |

Orden sugerido: **payback** como filtro inicial (¿recupero en tiempo razonable?), **VPN** como veredicto (¿crea valor?), **TIR** para comunicar la rentabilidad, **ROI** para el resumen de una línea.

## Análisis de sensibilidad (no te cases con un solo número)

Todo esto descansa en supuestos (ventas, costos, tasa). Antes de decidir, recalcula con 3 escenarios:

- **Pesimista:** ventas −30%, costos +15% → ¿sigue VPN > 0?
- **Realista:** tu mejor estimado.
- **Optimista:** referencia, no la base de la decisión.

Si el proyecto solo funciona en el escenario optimista, es frágil. Decide con el realista y revisa que el pesimista no te quiebre (ver 56 para el modelo financiero completo y 30 para los supuestos de fondo).

## Errores comunes

- **Decidir solo con ROI** e ignorar el tiempo. 60% en 6 meses ≠ 60% en 8 años.
- **Olvidar el valor del dinero en el tiempo** en inversiones largas (ahí VPN/TIR son obligatorios).
- **Usar una tasa de descuento sacada del aire** o copiada de otro país. Ajústala a TU inflación, tasas y riesgo (ver 21).
- **Meter flujos "brutos" sin descontar impuestos ni costos reales** (usa flujo NETO, ver 56).
- **Confiar en la TIR con flujos raros** (que cambian de signo varias veces): puede dar resultados engañosos; ahí manda el VPN.
- **No hacer sensibilidad:** un solo escenario optimista no es una decisión, es un deseo.
- **Ignorar el costo de oportunidad:** "¿qué más podría hacer con esa plata?" Si una alternativa simple rinde más con menos riesgo, ese es tu verdadero punto de comparación.

## Siguiente paso típico

Arma los flujos netos del proyecto en una hoja de cálculo (ver 56), define tu tasa de descuento con datos reales de tu país (ver 21) y calcula payback, VPN y TIR con los tres escenarios. Decide con el escenario realista y confirma que el pesimista no te hunda.
