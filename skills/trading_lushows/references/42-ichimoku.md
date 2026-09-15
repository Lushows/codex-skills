# 42 — Ichimoku (en simple)

El **Ichimoku Kinko Hyo** ("gráfico de equilibrio de un vistazo") es un sistema japonés que
dibuja cinco líneas y una "nube" sobre el precio. Promete leer tendencia, momentum y
soportes/resistencias de una sola mirada. Vamos por partes — y con la pregunta honesta al final:
¿qué aporta que no tengamos ya?

## Los componentes, traducidos

| Componente | Qué es (sin japonés) | Equivalente conceptual |
|---|---|---|
| **Tenkan-sen** | Punto medio del rango de las últimas 9 velas | Una "media" rápida (usa extremos, no cierres) |
| **Kijun-sen** | Punto medio del rango de las últimas 26 velas | Una "media" lenta; zona de retroceso |
| **Senkou A** | Promedio de Tenkan y Kijun, dibujado 26 velas ADELANTE | Borde 1 de la nube |
| **Senkou B** | Punto medio de 52 velas, también desplazado adelante | Borde 2 de la nube |
| **Kumo (nube)** | El área entre Senkou A y B | Zona de soporte/resistencia proyectada |
| **Chikou** | El cierre actual dibujado 26 velas ATRÁS | Comparador "¿estamos arriba de hace 26 velas?" |

Lecturas clásicas: precio sobre la nube = tendencia alcista; nube gruesa = soporte fuerte;
cruce Tenkan/Kijun = señal (el equivalente del cruce de medias de `33`).

## Qué aporta de verdad

- **Todo en un vistazo**: condensa tendencia + momentum + zonas en una imagen. Para trading
  discrecional visual, es eficiente.
- **La nube como zona (no línea)**: coincide con la idea correcta de `31` — los niveles son áreas.
- Usa puntos medios de rangos (high/low) en vez de cierres: una textura levemente distinta.

## Qué duplica de lo que ya tenemos (la parte honesta)

- Tenkan/Kijun y su cruce ≈ nuestras SMA20/50 y su golden cross (`33`), con otros períodos.
- La nube como soporte dinámico ≈ la SMA20 como zona de retroceso + nuestros soportes (`31`).
- "Precio sobre la nube = alcista" ≈ "precio sobre SMA20 y SMA50" que el bot ya evalúa (`04`).
- Chikou ≈ momentum de 26 velas, que RSI y MACD ya cubren (`34`, `35`).
- Todo deriva del mismo precio: sumarlo no agrega evidencia independiente, agrega **redundancia
  con disfraz japonés** (`45`). Y sus 5 líneas × períodos configurables son un buffet de
  parámetros para sobreajustar (`47`).
- Los períodos originales (9/26/52) vienen del calendario laboral japonés de los años 60
  (semanas de 6 días). En cripto 24/7 son herencia histórica, no diseño.

## Cómo aplica al AGENTE TRADING

- **No agregarlo al bot.** El sistema ya tiene tendencia (SMA + régimen), momentum (RSI, MACD)
  y zonas (S/R). Ichimoku re-empaquetaría lo mismo con más parámetros y cero información nueva —
  el caso de manual del indicador que se apila por coleccionismo.
- Vale conocerlo por dos razones: mucha gente en cripto lo mira (sus niveles pueden funcionar
  como profecía autocumplida, igual que Fibonacci `41`), y si Claude encuentra menciones a
  "la nube" en contexto, debe saber traducirlas a lo que ya medimos.
