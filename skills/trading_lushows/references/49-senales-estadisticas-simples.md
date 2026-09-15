# 49 — Señales estadísticas simples

Una **señal** es una condición medible que, históricamente, viene seguida de movimientos con
sesgo (sube más veces de las que baja, o al revés). Las señales que sobreviven décadas de
estudio son sorprendentemente simples. Las tres familias clásicas:

## 1. Momentum (seguir la fuerza)

Idea: **lo que viene subiendo tiende a seguir subiendo un tiempo más.** Razón económica: la
información se incorpora lento (no todos compran a la vez) y el comportamiento en manada
alimenta la tendencia. Es la anomalía más documentada en mercados tradicionales y cripto.

- Versión simple: precio sobre su SMA50 y SMA20>SMA50 = régimen alcista, favorecer LONG.
- Su talón de Aquiles: los giros bruscos. El momentum te tiene comprado cuando el mercado da
  la vuelta, y en cripto las vueltas son violentas.

## 2. Reversión a la media (apostar al regreso)

Idea: **lo que se estiró demasiado tiende a devolverse.** Razón económica: los movimientos
extremos suelen ser sobre-reacción (pánico o euforia) que luego se corrige.

- Versión simple: RSI <30 con tendencia de fondo alcista = rebote probable; precio a >3% de la
  SMA20 = estirado, esperar el regreso antes de entrar.
- Su talón de Aquiles: "barato puede volverse más barato". En una tendencia fuerte, comprar la
  caída es ponerse delante del tren.

Momentum y reversión no se contradicen: operan en **escalas distintas**. La tendencia manda en
semanas; la reversión manda en horas/días dentro de esa tendencia. Comprar el retroceso dentro
de una tendencia alcista usa las dos a favor.

## 3. Estacionalidad (patrones de calendario)

Idea: ciertos momentos (horas, días, meses) muestran sesgos recurrentes — por flujos reales:
cierres de mes, horarios de mercados grandes, vencimientos de derivados. Es la familia más
débil de las tres: muchos patrones de calendario son ruido que pasó dos veces. Exigirle más
muestra que a nadie y una razón de flujo verificable — cifras concretas, verificar al día.

## La verdad incómoda: el edge simple decae

Toda señal pública se erosiona: cuando muchos la conocen y la operan, la mueven antes y el
sesgo se achica. Además los mercados cambian de régimen (ver `47`: memorizar un régimen ≠ tener
edge). Consecuencias prácticas:

| Implicación | Qué hacer |
|---|---|
| Ningún edge es eterno | Medirlo continuamente, no asumirlo |
| El edge simple es chico | Los costos pueden comérselo entero (ver `46`) |
| Decae sin avisar | Comparar rendimiento reciente vs histórico por señal |
| "Dejó de funcionar" ≠ mala racha | Distinguirlo requiere muestra — cálculo → `Matematicas_lushows` |

Regla honesta: **una señal que no se mide es una creencia, no una señal.** Y una mala racha de
5 trades no prueba que el edge murió, igual que 5 ganadores no prueban que existe.

## Cómo aplica al AGENTE TRADING

- El bot ya combina las dos familias grandes sin llamarlas así: SMA20/50 + MACD = momentum
  (¿hay tendencia que seguir?); RSI + distancia a la SMA20 = reversión (¿está estirado para
  entrar YA?). La lección FOMO de julio fue exactamente ignorar la parte de reversión: entrar
  por momentum en precio extendido (0/3 sobre SMA20+3%).
- Solo-LONG significa que el bot depende del régimen alcista: cuando el momentum de fondo se
  apaga, su mejor jugada es no operar. Que el clasificador de régimen (Haiku) diga "lateral"
  o "bajista" y el bot se quede quieto ES la señal funcionando.
- Pendiente natural: etiquetar cada trade con la señal que lo motivó (tendencia, retroceso,
  ruptura) para poder medir el edge POR SEÑAL cuando haya muestra — no en bloque.
- Estacionalidad: no usar por ahora. Con 10 trades no hay muestra ni para las señales
  principales, mucho menos para patrones de calendario.
