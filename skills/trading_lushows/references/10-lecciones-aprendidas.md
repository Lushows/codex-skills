# 10 — Lecciones aprendidas (módulo VIVO — agregar con fecha, nunca borrar)

> Fuentes: meta-análisis semanales del propio bot (`/api/meta-analyses`), auditorías nuestras,
> y errores operativos. La skill vale lo que valga este archivo.

## jul-2026 (primeras 6.5 semanas de paper)

### L1 — El FOMO también se programa (6-jul-2026)
Datos: win rate 100% (4/4) en entradas bajo $1760 ETH vs 0% (0/3) en entradas sobre $1788,
tras un rally de +4.5% intra-semana. El bot no siente FOMO, pero sin filtro de "precio extendido"
su prompt produce el mismo comportamiento que un humano ansioso.
**Acción derivada:** agregar filtro anti-extensión (ej. distancia a SMA20 > 3% → convicción baja)
— backlog `11`, candidato #1 a pivote de estrategia.

### L2 — Clustering de entradas = una apuesta comprada 3 veces (6-jul-2026)
3 entradas en un rango de $3.68 (1788.16–1791.85) en pocas horas. Con máx 2 posiciones y un solo
par activo, la "diversificación" era ilusoria: misma tesis, mismo precio, mismo stop.
**Acción derivada:** regla de separación mínima entre entradas del mismo par (precio o tiempo).

### L3 — Trade fuera de protocolo con convicción 0 (6-jul-2026) ⚠️ POSIBLE BUG
El meta-análisis reporta 1 trade ejecutado con régimen `unknown` y convicción 0/10 — el
auto-trader exige convicción ≥8, así que algo lo saltó (¿orden manual?, ¿bug del watcher?,
¿estado corrupto?). **Investigar en el código antes de cualquier go-live**: el sistema debe hacer
IMPOSIBLE lo prohibido.

### L4 — La infraestructura aguanta; la estrategia es lo que se está horneando (6-jul-2026)
44 días de uptime continuo, 0 errores/24h, WS conectado, costo IA $7.70 total (~$5/mes, bajo el
techo de $15). El riesgo controlado funciona: drawdown máximo 1.84% con PF 0.89. Traducción:
**el sistema pierde poquito mientras aprende — exactamente para eso es el paper.**

### L5 — Ritmo de trades insuficiente para la muestra (6-jul-2026)
10 trades en 6.5 semanas → proyección ~20 al 22-ago, bajo el mínimo de 30. Causas: umbral 8 muy
exigente + solo LONG + solo 2 pares. Opciones (elegir UNA, no todas a la vez): SHORT en paper,
tercer par líquido (SOL), o bajar threshold a 7 SOLO si el filtro anti-extensión (L1) compensa.
**Nunca bajar el umbral solo para generar actividad** — eso es comprar muestra con plata.

### L6 — Todo el P&L vino de ETH (6-jul-2026)
Los 10 trades cerrados fueron ETHUSDT. BTC no generó señales ≥8. Vigilar: ¿el prompt/regímenes
tienen sesgo por par, o BTC simplemente no dio setups en el período?

### L7 — El "bug" de convicción 0 era falta de trazabilidad, no un gate roto (6-jul-2026)
Auditoría del código: el auto-trader SIEMPRE tuvo el gate correcto (convicción ≥ threshold y
recomendación BUY). El trade "fuera de protocolo" era una orden manual del dashboard que el
meta-análisis no podía distinguir de una automática, porque las posiciones no guardaban origen.
**Fix aplicado:** toda posición ahora registra `source` (auto/manual), `conviction` y `analysisId`.
**Lección general:** antes de asumir bug en la lógica, verificar si el problema es de OBSERVABILIDAD
— un sistema sin trazabilidad convierte cualquier anomalía en misterio.

### L8 — Los fixes de estrategia se implementan en código, no en el prompt (6-jul-2026)
El filtro anti-extensión (L1) y el anti-clustering (L2) se implementaron como reglas duras en
JS (engine cap + broker reject), no como instrucciones al prompt de Claude. Razón: el prompt
puede ignorar una instrucción; el código no. El prompt DECIDE, el código LIMITA.

### L9 — La memoria existía pero aprendía cosas falsas (6-jul-2026, v1.4)
Auditoría del ciclo de aprendizaje: las lecciones se generaban al cerrar cada trade, PERO se
etiquetaban con el régimen del último análisis disponible al momento del CIERRE, no de la
ENTRADA. Un trade abierto en trending-up que cerraba horas después en ranging quedaba archivado
como lección de ranging — el bot aprendía asociaciones falsas. **Fix v1.4:** las posiciones
guardan régimen + extensión al abrir, y la lección se atribuye vía `analysisId` al análisis
exacto que originó el trade. **Lección general:** en un sistema que aprende, la ATRIBUCIÓN
correcta importa más que la cantidad de datos — datos mal etiquetados enseñan mentiras.

### L10 — Anécdotas + estadística, no solo anécdotas (6-jul-2026, v1.4)
El prompt de convicción recibía 10 lecciones de texto (anécdotas) pero ninguna evidencia
agregada. Un LLM no puede computar "mis convicciones 8 ganan 40%" leyendo prosa. **Fix v1.4:**
bloque CALIBRACION REAL calculado en JS (win rate/PF por régimen, convicción, par) inyectado
al prompt, con advertencia automática si la muestra es <30. Anti-bucle: la calibración es
aritmética determinista — no puede derivar en narrativa que se retroalimente. Complemento:
memoria acotada (FIFO 400, texto ≤400 chars) y selección balanceada (las pérdidas nunca
quedan ahogadas por los wins en el prompt).

### L11 — El paper permite comprar muestra con tiempo, no con plata (6-jul-2026, v1.5)
Modo estudio acelerado activado: 3 pares, cadencia 1h, threshold 7, límites de overtrading
elevados por env (defaults intactos en código). En paper, acelerar la muestra cuesta ~$10-15/mes
extra de IA y cero riesgo; en live costaría capital. La regla "nunca bajar el umbral para generar
actividad" se refina: **se puede bajar en paper SI la calibración mide cada nivel por separado**
— así el umbral óptimo se decide con datos en vez de intuición.

### L12 — El paper optimista es peor que no tener paper (6-jul-2026, auditoría v1.6)
Auditoría de 4 agentes encontró que el watcher creaba fills fantasma (cerraba TP/stops usando
high/low de la vela ANTERIORES a la entrada) y llenaba stops al precio exacto aunque el precio
hubiera saltado de largo (gaps). Ambos sesgos inflan el PF — la evidencia con la que se decidirá
el go-live estaba corrupta hacia el optimismo. También: la vela EN CURSO entraba al análisis
(indicadores que repintan = look-ahead). **Todo corregido y con tests.** Lección: antes de confiar
en las métricas de un simulador, audita el REALISMO del simulador — el PF de un paper optimista
es una promesa que el mercado real no va a cumplir.

### L13 — Un sistema 24/7 muere por lo que no ve (6-jul-2026, auditoría v1.6)
Tres cegueras encontradas: WS zombie (TCP muerto en silencio = stops sin vigilar con /status
diciendo "connected"), velas perdidas en reconexión (stop tocado durante el gap jamás se
ejecutaba), y Socket.IO sin auth (filtraba el portfolio en vivo sin credenciales). Fixes:
watchdog de 3 min + backfill REST post-reconexión + auth en el handshake del socket.

### L14 — Los NO-trades también son datos (6-jul-2026, v1.7)
Implementados los contrafactuales: cada HOLD y cada bloqueo del filtro anti-FOMO se evalúa
24h después contra las velas reales (saved = evitó pérdida / missed = mató un ganador).
Antes el sistema solo aprendía de lo que HIZO (~10 trades); ahora también de lo que NO hizo
(~60-70 decisiones/semana) — la muestra de aprendizaje se multiplicó ~7× sin costo de IA.
El endpoint /api/counterfactuals separa el veredicto del filtro anti-extensión: en 2-3 semanas
sabremos con números si el filtro salva plata o hay que recalibrarlo.

### L15 — Capas de defensa anti-FOMO completas (6-jul-2026, v1.8)
Tres guardrails nuevos EN CÓDIGO (el prompt decide, el código limita): gate de régimen (jamás
BUY en trending-down/risk-off), guard RSI ≥72 (sobrecomprado = FOMO tardío), y freno de pérdida
diaria (−3% realizado en 24h → BLOCK: "no se recupera apostando más"). Los tres dejan flag
(regimeFiltered/rsiFiltered) para que los contrafactuales midan si salvan plata o matan
ganadores — cada filtro se calibra con evidencia, no con miedo. Defensa completa: régimen →
extensión SMA20 → RSI → psicología (cooldown, overtrading, freno diario) → sizing 1.5% →
anti-clustering. Tests 186/186.

### L16 — Semana 1 del modo estudio: la disciplina paga (14-jul-2026)
7.7 días autónomos sin una caída. Primer trade de la era nueva: ETH auto, convicción 7,
trending-up, +$6.34 en target con MAE de solo -0.39% (el stop nunca corrió peligro).
Contrafactuales: 540 evaluados, 73.7% de los "no operar" fueron correctos (303 saved vs
108 missed) — la disciplina salva plata medible. El meta-análisis semanal recomendó
exactamente las reglas ya implementadas (bloquear convicción baja, no operar ranging)
al leer los trades viejos — validación independiente del rumbo. Costo IA: ~$0.90/día
(~$27/mes, sobre el techo de $15 — aceptado temporalmente por el modo estudio intensivo).

### L17 — v2.0: SHORT en paper (14-jul-2026)
El dato que lo justificó: ~60% de las lecturas de la semana fueron bajistas/risk-off y el
bot long-only no podía operar ninguna. Implementado el espejo completo (broker con margen
retenido simple, watcher con gaps en contra, MAE/MFE en dirección del P&L, prompt BUY|SELL|HOLD,
REGIMES_NO_SELL, anti-extensión <-3%, RSI<=28, contrafactuales direccionales). 220/220 tests.
Trending-down deja de ser hora muerta. Nota para Fase 8: el SHORT en spot real requiere
margen/futuros (otra API, riesgo de liquidación) — en paper enseña el edge; la decisión de
shortear en vivo se toma aparte.

### L18 — v2.1: la Fase 8 técnica existe y duerme (14-jul-2026)
Construida completa con mocks (269/269 tests): cliente firmado HMAC, liveBroker (misma
interfaz que paper, valida local ANTES del exchange, redondeo floor a stepSize/minNotional,
MARKET + OCO — los stops viven EN el exchange), reconciler de boot (OCO faltante → recrear;
fill no visto → cierre con datos reales), killSwitch persistido, cap duro $50/orden.
DORMIDA: en paper los módulos ni se importan (import dinámico). Encendido: MODE=live +
keys de testnet + BINANCE_REST_URL=https://testnet.binance.vision. Pendiente marcado en
código: verificar /api/v3/order/oco vs /api/v3/orderList/oco contra docs al conectar.
También v2.1: el meta-análisis semanal ahora retroalimenta la decisión (AUTO-REVISION
acotada, anti-bucle regla 9) — el ciclo de aprendizaje quedó CERRADO: opera → lección →
calibración → contrafactual → meta-análisis → de vuelta al prompt.

### L19 — v2.2: motor dual (un módulo, dos secciones) (14-jul-2026)
Decisión de Luis para ahorrar costo (no 2 servicios Render): UN proceso ejecuta cada decisión
en paralelo sobre 2 portafolios independientes — paper (maestro, intacto, data/portfolio.json)
y real testnet (data/live/). El análisis de Claude corre UNA vez (un costo de tokens) y la
orden se espeja a ambos brokers. Bono clave: como es la MISMA decisión, se compara "lo que el
simulador dijo" vs "lo que Binance hizo" — la prueba definitiva de que el paper es honesto.
DUAL_MODE=false por defecto (arranque paper byte-idéntico, verificado). SELL no se espeja al
real (spot no shortea). Testnet validado en vivo desde PC (smoke test OK). Tests 288/288.
Deploy pendiente: migrar servicio a Frankfurt copiando el disco (no perder los días de estudio)
+ env DUAL_MODE=true + keys testnet. Pago de Render resuelto 14-jul.

### L20 — El geo-bloqueo del testnet NO aplica (14-jul-2026) — probar > asumir
Asumíamos que Render US bloquearía el testnet de Binance (como el mainnet). Antes de migrar a
Frankfurt + copiar disco (caro y arriesgado), probamos encendiendo DUAL_MODE en el servicio
US existente (seguro: el paper queda intacto por diseño). Resultado: testnet.binance.vision
funciona desde US sin geo-bloqueo. Ahorró un 2º servicio, la migración de disco y complejidad.
Lección: no asumir un bloqueo por analogía — costó 1 variable de entorno confirmarlo.
También clave: separar BINANCE_REST_URL (datos, mercado REAL — el paper aprende con precios
verdaderos) de BINANCE_LIVE_REST_URL (órdenes, testnet). Una sola URL habría contaminado el
estudio con precios falsos del testnet.

### L21 — El bot era breakeven bruto que perdía SOLO por comisiones (21-jul, auditoría v2.3)
Tres auditores + números verificados en código: PF 0.79, pero neto −$6.64 con comisiones $7.38 →
BRUTO +$0.74. El sistema no perdía por malas decisiones sino por operar demasiado con stops muy
justos (los 9 perdedores murieron JUSTO en el stop, MAE≈stopDist). Fix: stops 1.5×→2.2×vol.
Lección: cuando las fees ≈ la pérdida, el problema es frecuencia+stops, no el cerebro.

### L22 — Toda la sangría era el SHORT, por regime-lag (21-jul)
SOL short −$9.16 (7 trades) vs longs +$2.52. Causa raíz mecánica (no mala suerte): el detector
de régimen usa death-cross SMA50/200 REZAGADO → etiquetó SOL lateral (74-77) como trending-down
82-92% y el bot shorteó dentro de un rango. Los 5 perdedores casi no fueron a favor (MFE 3-70%
del camino). Fix: SHORT PAUSADO (SHORT_ENABLED=false) hasta reconstruir la señal con algo
no-rezagado (estructura lower-lows + momentum, no cruce de medias). Lección: un indicador
rezagado convierte "lateral" en "tendencia" y el bot pelea contra un fantasma.

### L23 — El techo de convicción 7 volvía inútil la convicción (21-jul)
En 700 análisis la convicción NUNCA pasó de 7; los 14 trades son TODOS 7 → sizing uniforme (70%
del presupuesto siempre). "Apuesta grande con alta convicción" (Druckenmiller) jamás disparaba, y
la calibración por nivel no discriminaba nada. Fix: anclas explícitas 8/9/10 en el prompt +
regla "un 7 y un 9 que operan igual hacen inútil la convicción". Trampa latente encontrada:
AUTO_EXECUTE_THRESHOLD default es 8 pero ningún análisis llega a 8 → con el default el bot NO
operaría jamás (solo opera por AUTO_EXECUTE_THRESHOLD=7 del modo estudio).

### L24 — El mayor activo de aprendizaje estaba desconectado: EL CEREBRO (21-jul, v2.3)
Los 550 contrafactuales (23× más señal que los 14 trades) solo iban al dashboard, nunca a la
decisión. v2.3 construye brainCalibration.js: fusiona (A) P&L realizado con comisiones, (B) señal
contrafactual por régimen/convicción, (C) auto-diagnóstico del meta — cada fuente etiquetada, y
el prompt pondera ("un edge que existe en contrafactual pero muere tras fees NO es edge"). El
savedPct decisivo ya dice cosas: conv 4 acierta solo 45.7% (los HOLD de conv 4 saltan más
ganadores de los que salvan). Lección: tener la señal calculada no sirve si no llega al cerebro
que decide — conectar 24→570 puntos de calibración sin ejecutar un trade nuevo.

### L25 — "Más rápido" y "más resultados" apuntan a lados opuestos con edge negativo (21-jul)
Luis pidió "más resultados más rápido". Honestidad: con edge negativo, más trades = perder más
rápido. Lo que se acelera es el APRENDIZAJE (contrafactuales al cerebro, backtest sobre velas
guardadas, romper techo de convicción), NO la ejecución. El camino a mejores RESULTADOS es operar
MENOS y MEJOR (solo ETH-long, stops anchos). La portería de go-live NO se movió.

### L26 — Fase 1 del plan de estudio: la base de medición (21-jul, v2.4)
Construida la infraestructura de aprendizaje offline (no cambia decisiones en vivo): (1) journal
estructurado — marketState.js con feature-vector normalizado de orden fijo (semilla de la memoria
por similitud) + rMultiple + playbookClean por trade; (2) backtester walk-forward sobre velas
guardadas con comisiones dentro y anti-look-ahead verificado; (3) baseline LLM-vs-regla determinista
para responder "¿el LLM aporta edge o narra?". Tests 385/385. HALLAZGO OPERATIVO: solo hay ~128
velas guardadas por par (≈5 días) → el backtester funciona pero necesita MÁS HISTORIA para dar
veredictos con muestra. Próximo paso obvio de Fase 1: cargar meses de velas (Binance da 1000/req,
paginar) para que el backtester y el baseline tengan con qué concluir. Lección: construir la
herramienta de medición ANTES de las mejoras de estrategia — así Fase 2/3 se prueban sobre historia.

### L27 — EL HALLAZGO: la estrategia base NO tiene edge (21-jul, backtest 375 días) 🔴
Cargados 27.000 velas (375 días × 3 pares, mirror data-api.binance.vision) y corrido el backtester.
Resultado con MUESTRA REAL (406 trades): la regla determinista (momentum 1h + guardrails +
R:R fijo 1:2 + stop 2.2×vol) da **expectancyR −0.158R, win rate 34.2%, PF ~0.72-0.83, drawdown
40%+**, CONSISTENTE en BTC/ETH/SOL. Con R:R 1:2 el breakeven es ~40% WR (más con fees) → la base
está ~6pp corta. La estrategia core NO tiene ventaja. El backtester lo descubrió en minutos, sin
paper ni un peso — exactamente para esto se construyó (L26). IMPLICACIÓN: el trabajo ya no es
"afinar" ni "seguir corriendo paper esperando" — es ENCONTRAR el edge en el backtester probando
las mejoras de Fase 2/3 una a una, y quedarse solo con la que mueva el expectancyR hacia positivo.
Candidatos más fuertes por la investigación: salidas dinámicas ATR (el R:R fijo con WR 34% es un
asesino — corta las colas ganadoras) y multi-timeframe (no operar contra tendencia mayor).
REFUERZA: NO ir a real; y el LLM tendría que subir el WR de 34% a >40% consistente para justificar
su costo (dato pendiente del baseline cuando haya contrafactuales). La honestidad brutal es un
activo: mejor descubrir esto con velas que con el capital de Luis.

### L28 — Experimento 1 (salidas ATR) DESCARTADO: el problema es la ENTRADA, no la salida (21-jul)
Ciclo de laboratorio, método científico. Hipótesis: con WR 34% el R:R fijo 1:2 corta las ganadoras
→ un trailing ATR daría vuelta el edge. Probadas 5 variantes (fixed + trailing 1.5/2.2/3.0× +
breakeven), split TRAIN60/TEST40, métrica pre-registrada expectancyR. RESULTADO: el trailing subió
el win rate (34%→42-48%) pero EMPEORÓ el drawdown (42%→68-106%) y NO mejoró el edge; ganó solo en
1/3 pares por margen trivial (elegirlo sería data-mining). El mejor en TRAIN out-of-sample sigue
siendo fixed. **HALLAZGO: el R:R fijo NO era el cuello de botella — el edge negativo vive en la
SEÑAL DE ENTRADA. Cambiar el stop no salva una entrada sin ventaja.** Próximo experimento debe
atacar la ENTRADA: multi-timeframe (no operar contra tendencia mayor), régimen sin rezago
(volatilidad/CUSUM en vez de death-cross), funding rate. Bonus: backtester optimizado de ~100s a
400ms (precomputedIndicators O(n)) → iterar es instantáneo. Lección de método: un experimento que
MATA una hipótesis con disciplina out-of-sample vale igual que uno que la confirma — y nos dice
DÓNDE mirar. El paper optimista habría dicho "el trailing mejora el WR!" y nos habría engañado.

### L29 — Experimento 2 (multi-timeframe): PROMETEDOR pero no deploy-grade (21-jul)
Hipótesis: exigir confluencia con el marco superior (4h/1D) filtra las entradas contra-tendencia.
4 variantes (off/4h/1d/both), split TRAIN60/TEST40, expectancyR pre-registrada. RESULTADO
out-of-sample (TEST): off −0.218R → 4h −0.175 → 1d −0.105 → both −0.018 (casi breakeven). Drawdown
COLAPSA de 63.5% a 20.7% (both). Win rate 33%→40%. Mejora en 3/3 pares. PERO donde flipea a
positivo (BTC/SOL both, +0.1/+0.2R) la muestra es n<30 — la trampa que el experimento caza.
VEREDICTO: no es descarte (exp1) ni deploy — el MTF es un FILTRO valioso (reduce ruido
contra-tendencia, baja el riesgo dramáticamente) pero NO crea edge por sí solo; el gatillo de
entrada base (momentum simple) sigue débil. Confirma L28: el problema es la SEÑAL/GATILLO de
entrada. El MTF se GUARDA como capa (cuando haya un gatillo con edge, lo potenciará y bajará el
DD). Siguiente experimento: mejorar el GATILLO mismo — régimen sin rezago (volatilidad/CUSUM),
funding rate cripto, o un gatillo distinto (breakout+volumen, o mean-reversion en rango). higherTimeframe.js
+ el filtro quedan en el laboratorio para combinar con el gatillo nuevo. Tests 411.

### L30 — Exp3 (4 gatillos de entrada): breakout+volumen el candidato, la MUESTRA es el muro (21-jul)
Probados en paralelo 4 gatillos, split TRAIN60/TEST40, corrección multiple-testing. CONTINUACIÓN:
tsMomentum-vol + régimen-CUSUM → mejoran pero siguen negativos (cusum+MTF TEST −0.182 vs base −0.218).
REVERSIÓN: mean-reversion-rango = BUST (falling knives, muestra colapsa); **breakout+volumen = EL
CANDIDATO** — bate la base en 3/3 pares en TEST, cruza a POSITIVO en 2/3 (BTC +0.213 n=27, SOL
+0.267 n=9) pero n<30. PATRÓN en los 4: (1) MTF colapsa el drawdown 63%→4-38% (capa de riesgo
confirmada 3 veces — SE QUEDA); (2) ningún gatillo cruza a positivo CONFIABLE sobre 375 días;
(3) el cuello de botella es la MUESTRA — los gatillos buenos son SELECTIVOS, los cruces positivos
pasan con n<30. INSIGHT: el problema ya no es la idea (breakout+MTF es prometedor y baja el riesgo),
es que 375 días no dan suficientes señales de calidad para concluir. SIGUIENTE PASO MACIZO: cargar
2-3 AÑOS de historia (backfill hasta ~26000 velas) y re-correr breakout+MTF; si el edge positivo
se sostiene con n≥30 en 3/3 → primer sistema deploy-grade. Combinación candidata a producción:
breakout+volumen (gatillo) + MTF-both (filtro/riesgo). Lección de método: 5 experimentos, cero
overfitting, y ahora sabemos exactamente qué probar con más datos — eso es progreso real, no dar
vueltas. Tests 436.

### L31 — EL PRIMER EDGE POSITIVO PROBADO: breakout+volumen+MTF en BTC (21-jul, 3 años) 🟢
Experimento decisivo con 3+ años (27000 velas/par, backfill TARGET=26280). El breakout+volumen +
filtro MTF-both CRUZA a POSITIVO DEPLOY-GRADE en BTC: TEST expR +0.050, n=45, WR 66.7% vs base
momentum −0.214. Y SUPERA a la base en los 3 pares en TEST. PERO solo 1/3 llega a deploy-grade
(positivo + n≥30): ETH mejora pero sigue ≤0 (−0.025, n=125), SOL positivo pero n=23<30. CONTRASTE
cualitativo: base momentum WR 34% expR negativo; breakout+MTF WR 55-67% expR ~0-positivo — captura
algo REAL. Corrección multiple-testing aplicada (12 celdas, juicio solo en TEST, exigir 3/3).
SIGNIFICADO: pasamos de "la estrategia base pierde en todo" a "tenemos un componente con edge
positivo probado (BTC) que supera a la base en 3/3". Sistema NACIENTE con evidencia, no hobby.
NO desplegar aún (1/3 deploy-grade). CAMINOS: (a) entender por qué BTC sí y ETH/SOL no (BTC más
limpio para breakouts? parámetros por par?), (b) operar breakout+MTF solo donde tiene edge (BTC),
(c) combinar breakout con otra confirmación para ETH/SOL. La combinación candidata: breakout+volumen
(gatillo) + MTF-both (filtro). Método: 6 experimentos, cero overfitting, primer edge real. La
honestidad brutal + backtest sobre historia = descubrimos edge sin arriesgar un peso.

### L32 — EL EDGE DE BTC ERA UN ESPEJISMO: no sobrevive el tribunal de robustez (21-jul) 🔴 CORRIGE L31
Exp4: sometimos el "edge" de L31 a 3 pruebas de robustez brutales (López de Prado / AFML), y
NINGÚN par sobrevive. El +0.050R de BTC era artefacto del split 60/40 + haber elegido el mejor de
~12 variantes (data-mining involuntario). Pruebas:
- **Walk-forward multi-ventana**: BTC se veía OK (71.9% ventanas positivas, mediana +0.079R) — por
  eso engañaba. La estabilidad temporal SOLA no basta.
- **Bootstrap Monte Carlo** (mulberry32 sembrado, resample con reemplazo de los R-multiples):
  BTC IC95 = [−0.195, +0.283] → **INCLUYE 0**, P(expR≤0) = 33.9%. Un tercio de probabilidad de que
  el edge sea ≤0 por puro azar. ETH y SOL igual (IC95 incluyen 0).
- **Deflated Sharpe Ratio** (Bailey & LdP 2014, con corrección Lo-2002 skew/kurtosis + techo de
  suerte por nTrials): BTC DSR = 10.2% (necesita >95%); family-wise p = 99.4%. Para sobrevivir 12
  pruebas necesitaría expR ≈ **+0.42R**; tiene +0.05R. Incluso la muestra completa (+0.056R, n=129)
  está lejísimos → NO es artefacto de n chico, es que NO HAY EDGE.
- Veredicto por par: BTC 1/3, ETH 0/3, SOL 1/3. Ninguno pasa la barra.
**LECCIÓN MADRE (la más importante del proyecto):** un backtest positivo out-of-sample NO es un edge.
El tribunal de robustez (walk-forward + bootstrap + deflated) es OBLIGATORIO antes de creerle a
cualquier resultado, y AHORA es parte del criterio go-live (módulo `08`). Tras 7 experimentos
rigurosos NO tenemos edge robusto en swing 1h con estos enfoques — consistente con la investigación
(LLM no predice; señales técnicas simples ≈ ruido). Esto NO es fracaso: **el método funcionó** — el
tribunal cazó el espejismo ANTES de arriesgar dinero. El valor construido es real (backtester +
tribunal de robustez + cerebro + memoria = infraestructura de fondo cuant). SIGUIENTE honesto: buscar
el edge en OTRA fuente de datos (funding/OI reales, on-chain, otro timeframe) y pasarlo SIEMPRE por
este tribunal — o aceptar que el proyecto es un laboratorio de aprendizaje de clase mundial, no una
máquina de dinero (todavía). Regla nueva de oro: **ningún resultado se cree sin bootstrap + DSR.**

## CACERÍA DE EDGE — una señal a la vez, hasta el veredicto (dueño: "no pares hasta conseguirlo", 22-jul)

### S1 — FUNDING RATE: no hay edge (22-jul) 🔴
Primera señal cazada a fondo. Backfill REAL fapi.binance.com /fapi/v1/fundingRate: 3375 registros/par
(BTC/ETH/SOL, jun-2023→jul-2026, funding cada 8h), alineado causal a las velas (funding con
fundingTime ≤ openTime, anti-look-ahead con test de mutación). 3 hipótesis, 7 variantes:
(a) EXTREMO CONTRARIAN (z-score alto = longs sobre-apalancados → short/salida): TEST −0.32 a −0.38R.
(b) FILTRO anti-euforia (entrar solo si funding no extremo contrario): TEST −0.13 a −0.15R,
indistinguible del baseline momentum (−0.128R) → el funding NO aporta timing.
(c) FLIP/normalización (entrar cuando el extremo se normaliza): TEST −0.24 a −0.36R.
Las 7 celdas NEGATIVAS en TEST en los 3 pares → NINGUNA llegó siquiera al tribunal. Señal de alarma
sana: flip-z2.0-BTC +0.112R y contrarian-z2.5-SOL +0.166R eran POSITIVAS en TRAIN y COLAPSARON en
TEST — overfitting de manual que el split cazó. VEREDICTO: el funding, como contrarian/filtro/flip
después de comisiones, NO da edge desplegable en 1h. Tests 460. ⚠️ HALLAZGO OPERATIVO: Open Interest
histórico (endpoint /futures/data/openInterestHist) solo cubre ~30 días → INÚTIL para backtest de 3
años; OI queda descartado como Señal 2 (no hay historia). Siguiente señal: cambiar el TIMEFRAME
(trend-following diario estilo CTA/managed futures — la evidencia dice que el edge de tendencia vive
en diario/4h, no en 1h; todos nuestros fracasos fueron en 1h).

### S2 — TREND-FOLLOWING en TF alto: no robusto, PERO 1er destello real en ETH-4h (22-jul) 🟡
Señal más documentada del trading (managed futures/CTAs, Time Series Momentum Moskowitz-Ooi-Pedersen).
trendFollowing.js: agrega 1h→4h/1D (via higherTimeframe.js), decide solo en cierre de vela alta
(anti-look-ahead + test de mutación), stop 3×ATR=1R, salida por TRAILING ATR (deja correr — la
asimetría ES la tesis, sin TP apretado). 3 variantes canónicas (Donchian 20/55, MA-trend 50/100/200,
TSMOM 30/60/90) × {1D,4h} × 3 pares = 16 celdas. TRAIN60/TEST40.
VEREDICTO: ninguna cruza deploy-grade. PERO **ETH-4h es el primer destello GENUINO del proyecto**: las
8 variantes 4h-ETH dieron TEST expR POSITIVO con walk-forward estable; la mejor 4h/MA-200/ETH: expR
+0.342, n=38, WR 55%, payoff 1.40, 85% ventanas WF positivas. Muere en el tribunal SOLO por potencia:
bootstrap IC95 incluye 0 (P(≤0) 10-41%), DSR 6-35% tras penalizar 16 intentos; necesitaría expR
~0.7-0.9R. BTC-4h y SOL-4h negativos; 1D todo negativo (n<30 por par, trend opera poco). LECCIÓN: el
trend-following NO está muerto — está SUBDIMENSIONADO. El paper original usa 58 activos; probarlo en 3
cripto es underpowered por diseño (el edge de tendencia se DIVERSIFICA entre muchos mercados, no vive
en uno). Lo que lo mata es la muestra chica (n=38) + penalización de 16 celdas. SIGUIENTE (S2b, jugada
precisa NO overfitting): PRE-REGISTRAR UNA config canónica de trend-4h (a priori, no por el TEST) y
probarla en UNIVERSO AMPLIO (~15-20 pares líquidos) pooling los trades → más n + nTrials=1 (sin
penalización porque pre-registramos 1 hipótesis). Si el destello ETH-4h es real, con potencia
sobrevivirá; si era ruido, morirá limpio. Tests 481.

### S2b — TREND-4h en universo amplio: el destello ERA ruido (definitivo, 22-jul) 🔴
Prueba justa y con potencia del destello S2. Backfill 18 pares USDT (data-api.binance.vision, 37-104
meses c/u, 0 excluidos por el filtro ≥18 meses). 3 configs PRE-REGISTRADAS a priori (Donchian-55,
MA-100 —deliberadamente NO la 200 que ganó en ETH—, TSMOM-90), idénticas a todos, nTrials=3, salida
intocada (atrMult 3 / trail 6). TRAIN60/TEST40, pooling los trades del TEST de los 18 pares.
VEREDICTO: NINGUNA config da pooled-TEST expR positivo → el tribunal ni se invocó. Donchian-55
−0.032R (n=860, 6/18 pares+), MA-100 −0.066R (n=1577, 5/18+), TSMOM-90 −0.052R (n=1850, 7/18+). DOS
hallazgos que lo hacen CONCLUYENTE, no solo underpowered: (1) TRAIN positivo (+0.13 a +0.21R) →TEST
negativo en las 3 = decaimiento out-of-sample de manual (el trend "funcionó" en el bull 2020-21 y
murió hacia adelante); (2) el edge está CONCENTRADO, no distribuido: solo 5-7 de 18 pares positivos
en TEST — un TSMOM real (paper: 58 activos) aparecería en la MAYORÍA. ETH fue uno de los pocos pares
con suerte (TEST +0.276/+0.179/+0.071) → por eso elegir ETH-4h-MA200 a posteriori era ilusión.
Darle su prueba justa (18 pares, decenas de miles de velas, pooled, comisiones reales) ELIMINA la
excusa "underpowered" y confirma: trend-following en 4h cripto spot NO es edge desplegable. Tests 491.
BALANCE de la cacería hasta aquí (S1+S2+S2b): las señales de TIMING DIRECCIONAL sobre activos cripto
individuales (momentum, breakout, funding, trend) NO dan edge robusto tras comisiones. PATRÓN claro.
SIGUIENTE cambia de CATEGORÍA (S3): momentum CROSS-SECTIONAL / fuerza relativa (Jegadeesh-Titman) —
en vez de cada activo vs su propio pasado, RANKEAR los 18 pares entre sí y long los fuertes / evitar
los débiles. Anomalía DISTINTA y documentada, y ya tenemos la data del universo. Si S3 también falla,
toca charla estratégica honesta (5 negativos = el valor está en infraestructura/aprendizaje, o se
necesita fuente de datos fundamentalmente distinta, o aceptar no-edge). Regla intacta: cero peeking,
config pre-registrada, tribunal obligatorio.

### S3 — MOMENTUM CROSS-SECTIONAL (fuerza relativa): NO edge, el 4º negativo (22-jul) 🔴
Anomalía DISTINTA (Jegadeesh-Titman): rankear los ~18 pares entre sí y long los fuertes, no timing
direccional. crossSectional.js: panel diario alineado, señal trailing con skip anti-look-ahead,
ranking por quintiles, motor rebalanceo con fees por turnover L1 (0.15%/lado), survivorship real
(MATIC sale tras delisting 2024-09), rebalanceos no-solapados (serie IID → bootstrap válido). 3
configs pre-registradas (L∈{30,90,180}, skip 7, hold 7, quintil, nTrials=3). Neutralizó BETA con DOS
métricas: (a) long-short dollar-neutral top−bottom (anomalía pura), (b) tilt long-only vs equal-weight.
VEREDICTO TEST: (a) solo L=30 media>0 (+0.0048/reb) pero tribunal lo tumba (IC95 [−0.005,+0.015]
incluye 0, P(≤0)=16.9%, DSR 55%<95%); (b) mejor tilt L=90 +0.0006/reb, INDISTINGUIBLE del beta del
universo (+0.0053) → el top-quintil NO bate a "comprar todo por igual", IC95 incluye 0, DSR 25%. El
cross-section cripto está DOMINADO por beta compartido. No es edge desplegable ni en long-short (que
además requiere shortear) ni en tilt spot. Tests 507.

## 🔴 BALANCE DE LA CACERÍA (22-jul) — 4 negativos limpios, CONCLUSIÓN ESTRATÉGICA
Probadas a fondo, con tribunal, cero peeking, fees dentro: momentum 1h (base), breakout+vol+MTF (era
espejismo/Exp4), funding rate (S1), trend-following 1h/4h/1d 3-pares (S2), trend-4h universo 18-pares
(S2b), cross-sectional 18-pares (S3). TODAS sin edge robusto. PATRÓN INEQUÍVOCO: **las señales
basadas en PRECIO/derivados sobre cripto líquida a plazos de swing NO baten a las comisiones de forma
robusta.** Consistente con la academia (mercados semi-eficientes + fees; LLM no predice precio —
LiveTradeBench). NO es fracaso: el MÉTODO funcionó — descubrimos la verdad sin arriesgar un peso, y
el tribunal cazó cada espejismo. VALOR REAL construido: backtester + tribunal de robustez (walk-forward
+bootstrap+DSR) + cerebro + memoria + journal = infraestructura de fondo cuant + un método a prueba de
autoengaño. DECISIÓN ABIERTA CON LUIS (no seguir perforando la misma veta = eso SERÍA el autoengaño
que el método evita): (1) aceptar no-edge y que el valor es laboratorio/aprendizaje, NO tradear real;
(2) lo único categóricamente distinto que queda = FUNDING CARRY (delta-neutral: long spot + short perp
para cosechar el funding — estructural, NO predictivo; real y documentado pero yield modesto ~5-15%
APR variable y requiere perp/margen); (3) honestidad económica: el tiempo de Luis rinde MUCHO más en
sus negocios con ingresos (AVISPA'O) que persiguiendo un edge cripto que 4 experimentos dicen que no
está. Recomendación del trader: (1)+ mencionar (2) como única vía no-predictiva, y (3) como la verdad
económica. Regla de oro reforzada: ningún resultado se cree sin bootstrap+DSR; y saber PARAR también
es disciplina.

### S4 — FUNDING CARRY: 🟢 EL PRIMER EDGE ROBUSTO DEL PROYECTO (22-jul)
Luis eligió SEGUIR tras los 4 negativos → PIVOTE de señales PREDICTIVAS a ESTRUCTURALES, y PAGÓ.
Funding carry delta-neutral (LONG spot + SHORT perp mismo notional → el precio se cancela, cosechas el
funding cada 8h). backfill-perp.mjs: 27009 klines perp/par de fapi.binance.com (basis real).
fundingCarry.js: P&L por periodo = funding + basis − fees(ambas patas). 3 variantes pre-registradas, nTrials=3.
VEREDICTO 🟢 HAY EDGE ROBUSTO (out-of-sample TEST + el MISMO tribunal que mató a los otros 5):
- BTC always-on: TEST +3.3% (APR ~2.1%), Sharpe 6.24, MDD 0.3%, DSR 98.6%, bootstrap CI excluye 0. ROBUSTO.
- ETH always-on: APR ~1.7%, DSR 97.5%, CI excluye 0. ROBUSTO. Pooled 3-pares DSR 99.2%. ROBUSTO.
- SOL always-on: NEGATIVO (−0.7% APR) — funding SOL positivo solo 57.8% del TEST vs ~81% BTC. Edge NO
  universal: vive donde el funding se mantiene persistentemente positivo.
DE DÓNDE SALE (BTC, % notional): funding_bruto +3.85%, basis +0.01% (delta-neutral FUNCIONA), fees
−0.60% → neto +3.26%. Cosecha PURA de funding; entras/sales UNA vez. HALLAZGO CLAVE: las 2 variantes
"inteligentes" (gating por funding+/umbral) DESTRUYEN el edge — el churn paga fees 6.6-22.8% del notional
y hunde todo a negativo. El enemigo del carry es el COSTO DE ROTACIÓN, no el funding negativo; always-on
gana por pagar fees una vez. Re-optimizar el gate = data-mining; el pre-registro manda.
LETRA CHICA (crítica, no ilusionarse): (1) ~2% APR SIN apalancar → en $100 = $2/año, NO es ingreso;
(2) los desks apalancan 3-5× para ~6-10% APR PERO añade liquidación/margen + contraparte del exchange +
saltos de basis que el modelo NO cotiza del todo ("recoger monedas frente a la aplanadora"); (3) Sharpe
~6 es firma de carry low-vol y SE COMPRIME en real; (4) desplegar requiere infra perp/margen + monitoreo
de funding en vivo = decisión aparte, NO es el bot spot paper actual. CONCLUSIÓN: método VALIDADO (halló
edge donde lo había, lo negó donde no) + existe edge estructural real pero MODESTO en BTC/ETH. SIGUIENTE
(S4b antes de cualquier real): ¿qué pares tienen funding persistentemente positivo? + stress-test de
saltos de basis/liquidación bajo leverage + testnet futures de la mecánica delta-neutral. Tests 519.

### S4b — CARRY BLINDADO: canasto + riesgo de cola cuantificados (22-jul)
Dos frentes en paralelo, mismo tribunal, cero peeking (selección por TRAIN, juicio por TEST, fees 2 patas).
FRENTE A (universo, fundingPersistence.js + experiment-carry-universe.mjs): backfill funding+perp de 17/17
pares con perp (MATIC excluido, perp delistado por POL). Persistencia (solo TRAIN): 15/17 con funding>0
en ≥70% periodos; solo BNB falla (28.9%, contango invertido). Fuera de muestra 12/17 con APR neto+ (SOL
−0.7%, BCH −2.3%, ATOM −2.7%, TRX −1.7% se voltearon por rachas negativas ~20d). CANASTO amplio 15-pares:
1.9% APR Sharpe 4.02 — NO supera a BTC-solo (diversificar ingenuo mete ruido de basis/drag). CANASTO
ESTRICTO 10-pares (pct≥80% y APR bruto>2%): 2.9% APR, Sharpe 6.20, MDD 0.4%, DSR 100% — SÍ supera a
BTC-solo ~40% en APR sin perder Sharpe (nTrials=3 contados, sobrevive). LECCIÓN: premia CALIDAD de funding,
no cantidad de pares.
FRENTE B (riesgo, carryRisk.js + experiment-carry-stress.mjs): supuesto conservador margen ISOLATED
(x_liq=1/L−m). Basis es casi ruido (peor widen 3yr: 0.2% BTC, 1.0% ETH). El killer = salto DIRECCIONAL del
perp que liquida el short aislado (peor 1d: BTC +13.8%, ETH +24.7%). Leverage máx que sobrevive el peor
evento 3yr: BTC L5, ETH L3 → PORTAFOLIO L3 (ETH eslabón débil); L2 prudente. Sangrado peor régimen negativo
(94-98d funding neg en 2026) trivial: −0.7 a −1.0% a L3. Riesgos NO modelados (leverage seguro real MENOR):
cascadas intra-vela (1h no ve el wick), contraparte del exchange (quiebra/ADL/de-peg colateral/retiros
congelados), cambios de régimen margen/funding. MATIZ CLAVE: L3 viene del supuesto isolated; con CROSS-margin
(cash-and-carry misma cuenta, el spot ES el margen del perp) la dirección se cancela y solo pesa el basis
(≤1%) → hasta L10 sobrevive el basis y el binding pasa a operativo/contraparte. La ARQUITECTURA DE MARGEN es
la decisión que más mueve el número.
🔢 RECONCILIACIÓN DE APR (crítica, honesta): Frente B citó ~5.7% base / 18% a L3 pero eso es sobre 3 AÑOS
COMPLETOS (backward, inflado por bull 2023-24). El número FORWARD-LOOKING (out-of-sample TEST, el que vale
para decidir): canasto estricto ~2.9% SIN apalancar → **~6% a L2 prudente, ~8-9% a L3 máx-seguro** (para un
canasto con alts, L2 es lo prudente porque los alts tienen wicks direccionales mayores). NO 18%.
💵 ECONOMÍA REAL (lo que Luis DEBE oír): ~6% forward a L2 → en $100 = $6/año, en $1.000 = $60, en $10.000 =
$600. Solo es "ingreso" con capital que Luis no tiene libre (dijo "ando corto"). El edge es REAL y ya bien
caracterizado, pero a su capital es HITO/prueba-de-concepto, no sueldo. Camino responsable: (1) validar la
mecánica delta-neutral en TESTNET de futuros (dinero de juguete, motor dual) — SIN plata real; (2) NO poner
plata que necesita; (3) el triunfo real = método validado + infraestructura + un edge estructural medido con
su perfil de riesgo. Tests 548. PENDIENTE si Luis sigue: S4c = testnet futures delta-neutral (requiere que
Luis cree llaves de Binance Futures TESTNET — dinero de juguete, OK compartir; llaves REALES jamás en chat).

### S4c — MECÁNICA DELTA-NEUTRAL VALIDADA en demo de futuros (22-jul) ✅
Infra Fase-8 acotada al carry (OFF por defecto, no cableada al auto-trader). src/liveTrading/
futuresSignedClient.js (HMAC, reusa signQuery del cliente spot) + carryExecutor.js (openCarryLeg short
perp con cap+floor, closeCarryLeg reduceOnly, carryStatus=monitor de riesgo, reconcile) + scripts/
smoke-futures-testnet.mjs (validación MANUAL, único disparador, fuerza carryModeEnabled solo en su
corrida). Config aditivo: futuresLiveRestUrl, carryModeEnabled(false), carryMaxNotionalUsd(50),
BINANCE_FUTURES_TESTNET_API_KEY/SECRET. ⚠️ HALLAZGO OPERATIVO: Binance MIGRÓ el testnet de futuros al
"Demo Trading" — testnet.binancefuture.com ahora redirige al login unificado (ya NO hay botón GitHub);
el demo vive en demo.binance.com (login Google/etc), da llaves HMAC en menú→Demo Trading API→API
Management→Create API→System generated. Base REST del demo de futuros = **https://demo-fapi.binance.com**
(NO testnet.binancefuture.com; verificado en developers.binance.com/docs/derivatives). Ajustado el default
+ el guard de seguridad del smoke (acepta testnet/demo, rechaza fapi real). SMOKE PASÓ COMPLETO end-to-end
(cuenta 5000 USDT juguete, margin CROSSED, leverage 2x, mark+funding +0.00007, short 0.0012 BTC ~$79,
carryStatus con liquidationPrice+distancia, cierre reduceOnly, reconcile PLANO). minNotional BTC futuros
~$50 → el smoke necesita notional ≥~$66 (CARRY_SMOKE_NOTIONAL=80, cap subido a 120 solo para la corrida).
La pata spot va como paper (spot demo ≠ futures demo, sistemas separados); el riesgo novedoso validado es
la pata PERP. Llaves demo de Luis en .env local (gitignored). Tests 570. SIGNIFICADO: la mecánica funciona
en un exchange real de juguete — pipeline probado SIN un peso real. PENDIENTE si Luis sigue (S4d): dejar el
carry corriendo en demo unos días acumulando funding real (validar el P&L vivo vs el backtest), y/o cablear
un monitor de carryStatus al dashboard. NADA de plata real hasta ver el carry vivo sostenido + decidir infra.

### AUDIT-1 — Auditoría general 4 frentes + fixes (22-jul) 🔍
4 auditores paralelos (ruta de dinero, backtester/tribunal, pipeline decisión, seguridad/ops). SÓLIDO
verificado: motor backtest sin look-ahead + fees en ambos lados (→ los 5 descartes son confiables); motor
decisión sin path catastrófico, "convicción 0" no reproducible, sin repintado, estado sin corrupción;
secretos sin fugas, password timing-safe. HALLAZGO ESTRELLA (FIX-1, commit ab26db2): el tribunal usaba
stats IID; se añadió block-bootstrap + n_eff + deflatedEdgeHAC. VEREDICTO: **el edge del carry SOBREVIVE**
(IC95 sigue sin tocar 0, DSR>95%). GIRO: el funding sí autocorrelaciona (ρ~0.62) pero el tribunal juzga el
RETORNO/período (funding+basis−fees), ρ~−0.14 (dominado por basis ruidoso) → n_eff≈n, no había sesgo. La
FRAGILIDAD REAL no es estadística sino de COSTOS: edge delgado, 0.2bps/período de rebalanceo HALVA el APR,
0.5bps lo vuelve negativo; el delta-neutral se modeló sin coste de rebalanceo; con nTrials=8-15 BTC/ETH solos
caen <95% DSR (pooled/canasto aguantan). → antes de real, MEDIR coste rebalanceo/slippage + funding vivo (S4d).
FIX-2 (commit 272079d, 13 correcciones TDD, tests 621): #1 config COMPLETO al motor (STOP_VOL_MULT/
SHORT_ENABLED estaban MUERTOS, systemVersion=undefined ensuciaba calibración; near-miss alineado a umbral 8);
#2 idempotencia carry por estado del exchange (evita doble short); #3 cap carry inviolable min(env,cap);
#4 openCarryLeg valida executedQty>0; #5 FuturesSignedClient rechaza fapi real salvo allowReal; #6 guard
ALLOW_REAL_MONEY en ruta spot live; #7 SIGTERM; #8 handlers unhandledRejection/uncaughtException (+KillSwitch
en live); #9 AbortSignal.timeout(10s) en fetch; #10 barrido de .tmp huérfanos; #11 auth fail-closed en prod;
#12 rate-limit rutas Claude + CORS por env + json 32kb; #13 jitter en retry. DECISIONES ABIERTAS DE LUIS:
(a) poner DASHBOARD_USER/PASS en Render; (b) ¿órdenes manuales POST /api/orders deben respetar guardrails o
ser override humano libre?; (c) ¿mover reconcile de boot tras listen? Lección madre: auditar las PROPIAS
herramientas (el tribunal) es tan importante como auditar la estrategia — casi desinflamos el carry por un
sesgo que resultó no estar en la serie juzgada, pero el ejercicio reveló la fragilidad de COSTOS que sí importa.

### S4e — COSTO REAL DE MANTENER EL CARRY: coin-matched es mantenimiento-cero, edge DESPLEGABLE (22-jul) 🟢
Resuelve la fragilidad de costos de AUDIT-1. carryMaintenance.js: coin-matched (long N monedas spot +
short N monedas perp) es delta-neutral POR CONSTRUCCIÓN → |delta|/notional máx = solo el basis
(~0.08-0.20%, bajo banda 2%) → 0 rebalanceos por deriva en 934 periodos → coste de trading = 0.000
bps/periodo → APR_coin = APR_ideal SIEMPRE. La fragilidad era del escenario NOTIONAL-matched (rebalanceo
cada periodo, 0.38-0.69 bps → APR negativo). Margen: se repone con TRANSFERENCIAS (~gratis), no trades;
riesgo real = liquidación por salto (leverage bajo), no coste corriente. APR NETO REALISTA coin-matched
(TEST): BTC 2.05% (tribunal correcto SÍ, DSR 98.6%), ETH 1.66% (DSR 97.5%), SOL −0.71% (NO, funding
negativo en ventana = par, no mantenimiento). VEREDICTO: carry coin-matched DELGADO pero DESPLEGABLE en
BTC/ETH. LECCIÓN: la ESTRUCTURA importa tanto como la señal — coin-matched vs notional-matched cambia el
edge de vivible a muerto. Tests 639.

## GO-LIVE GATE del carry (contrato antes de UN peso real, 22-jul)
El carry es el 1er edge real del proyecto pero DELGADO (~2% APR sin apalancar en BTC/ETH). Antes de real,
TODO esto en verde (si algo falla, NO se opera con dinero de Luis): (1) medir en VIVO en demo ≥1-2 semanas:
funding realmente cobrado ≈ backtest, y slippage de apertura/cierre real de ambas patas; (2) estructura
COIN-matched (no notional) confirmada en la ejecución; (3) leverage ≤ L2 (o cross-collateral cash-and-carry)
para sobrevivir el peor salto histórico; (4) selección de par con funding persistente positivo (BTC/ETH sí,
SOL no en 2024+); (5) capital que a Luis LE SOBRE (nunca el que necesita — dijo "ando corto"); (6) DSR con
nTrials honesto (canasto/pooled aguanta hasta 8; BTC/ETH solos <95% si se cuentan ≥8 familias) → preferir
CANASTO diversificado; (7) las 3 decisiones de AUDIT-1 resueltas (creds Render, política órdenes manuales).
Economía: ~2% en $100 = $2/año → el carry NO es sueldo a capital chico; es prueba-de-concepto/aprendizaje
hasta tener capital ocioso significativo. El VALOR del proyecto sigue siendo el método + infraestructura.

### S5 — PORTERO de funding + canasto multi-par + control (22-jul) 🟢
Luis pidió estabilidad: BTC/ETH núcleo, SOL pausado, abrir mercado poco a poco. Solución = portero
AUTOMÁTICO en vez de lista fija. carryUniverse.js (evaluatePair/evaluateUniverse): un par es ELEGIBLE
si funding positivo ≥70% de los últimos N días (default 30) Y APR bruto >2%; si no, PAUSADO con razón
legible. Reusa pctPositive/grossApr de fundingPersistence (misma lógica que el backtest). carryStore v2
multi-posición (positions por símbolo, migración lazy sin perder la BTC viva). carry-open-hold loopea
CARRY_PAIRS, abre elegibles, reporta pausados; monitor/close multi-símbolo; carry-universe.mjs = vista
de control read-only. Env: CARRY_PAIRS, CARRY_FUNDING_MIN_POS_PCT, CARRY_FUNDING_MIN_APR, CARRY_LOOKBACK_DAYS.
Tests 659. commit 5a44b08.
⚠️ HALLAZGO CLAVE (la elegibilidad ROTA): apuntado al funding demo RECIENTE (30d), el portero dio BTC
✅(90%,6.78%), SOL ✅(87.8%,4.6%), ETH ⏸(APR −1.77%) — OPUESTO a la ventana del backtest (donde ETH era
bueno y SOL malo). Lección: la elegibilidad por par es REGIME-DEPENDENT y rota con el tiempo → por eso un
portero automático > lista fija de pares. CAVEAT: ese funding es del DEMO de Binance (puede ser sintético,
NO refleja mainnet); para decisiones reales apuntar el portero al funding MAINNET. La máquina de decisión
está lista; el veredicto depende del dato. NO hardcodear "BTC/ETH siempre" — dejar que el portero decida
con funding real, y así "abrir mercado poco a poco" se vuelve automático (un par entra solo si se lo gana).

### S6 — 2º EDGE (reversal/liquidez): DESCARTADO — diversifica pero pierde con fees (23-jul) 🔴
Búsqueda de un 2º edge ESTRUCTURAL no-correlacionado con el carry (Dalio). Estudio (Frente 3) rankeó
candidatos: descartó basis-trimestral (misma familia del carry), VRP/vender-vol (co-crashea en cola),
basis-perp-spot (≈0 empírico), cross-exchange-funding (#2, pero necesita Bybit/OKX = infra nueva).
Ganador a probar: PRIMA DE PROVISIÓN DE LIQUIDEZ / short-term reversal (cobrar por comprar cascadas de
liquidación), cross-seccional dólar-neutral, disparo en dislocaciones extremas. reversalEdge.js + pre-
registro fechado + tribunal (commit 1f0dfd1). VEREDICTO: DESCARTADO limpio. HALLAZGO DOBLE: (a) DIVERSIFICA
EXACTO como la tesis — anti-correlado con el carry (Pearson −0.145/−0.193; en la COLA donde el carry
sangra, el reversal GANA, corr cola −0.12/−0.30); PERO (b) PIERDE plata con fees: V1 media/evento
−0.56%/−0.62% (n=135-198, muestra de sobra → no es n chico, es genuinamente negativo). Fees por rotación
(0.8% round-trip) + cripto siguió cayendo tras dislocaciones sin rebote neto. Portafolio 50/50 (Sharpe
−5.46) EMPEORA al carry solo (9.33). LECCIÓN: un diversificador que pierde plata NO sirve aunque tenga la
correlación perfecta — arrastra el retorno. El funding carry sigue siendo el ÚNICO edge estructural
confirmado. Rescatar la cobertura de cola exigiría ejecución maker-only sin slippage de cascada (re-abrir
pre-registro, futuro). Tests 682. ESTADO: carry validado (offline+demo vivo), portero 75% estable, bug
huérfanas cazado/arreglado, servicio Frankfurt PREPARADO (render.yaml, sin desplegar — Luis pidió calma).

### S7 — CROSS-EXCHANGE FUNDING: edge MUERTO (sonda de factibilidad, 23-jul) 🔴
De-riesgo ANTES de construir (jugada pro): sonda barata con funding público de Bybit+OKX (90d, 6 pares)
vs Binance, para ver si el spread de funding entre exchanges vale la pena antes de conectar 2 venues.
VEREDICTO: NO. Spread medio 0.53 bps/periodo; abrir market-neutral = 2 patas × 2 venues = ~12 bps fee =
~22× el spread. APR neto −83% a −142%. Con umbral operable (>5bps): 0% de periodos lo superan en TODOS
los pares → el spread se arbitra al instante (teoría confirmada). La sonda ahorró SEMANAS de construir
clientes de 2 exchanges para nada. Tests 693. commit c110f87.

## 🎯 RECKONING ESTRATÉGICO (23-jul) — el pozo de edges se está secando, y eso es una VERDAD útil
Post-carry probamos 3 frentes de edge nuevo: reversal/liquidez (diversifica pero pierde), cross-exchange
funding (spread arbitrado, muerto), y antes 5 predictivos (muertos). PATRÓN honesto: los edges reales son
RAROS y ya encontramos EL que hay (funding carry). Esto es consistente con mercados semi-eficientes: el
carry sobrevive porque es compensación por un riesgo/servicio real (prima de apalancamiento) que persiste;
casi todo lo demás está competido/arbitrado. LECCIÓN MADRE: seguir cazando edge #4, #5 sería el autoengaño
que el método combate — rendimientos decrecientes hasta cero. El "avanzar masivamente" honesto YA NO es
descubrir otro edge; es EJECUTAR: hacer que el carry gane plata de verdad (Fase 8 go-live, gated por
tiempo=semanas demo + capital que sobre) o consolidar el proyecto como laboratorio de clase mundial + 1
edge real. Los frentes grandes restantes (opciones/VRP) son infra costosa Y tail-correlacionados con el
carry (mal diversificador). Recomendación del trader: parar la cacería, madurar el carry en demo, y
decidir go-live SOLO cuando el GO-LIVE GATE esté en verde y con capital ocioso. Saber cuándo dejar de
buscar es tan disciplina como saber buscar.

### S8 — DIRECCIONAL REGIME-ADAPTIVE: no hay edge — CIERRA la búsqueda direccional (23-jul) 🔴
El mejor tiro del bot direccional, a pedido de Luis ("mejorar el indicador", quitar el rezago del
death-cross SMA50/200). regimeDetector.js: detector SIN REZAGO (Efficiency Ratio de Kaufman ER=24/0.30
+ estado de volatilidad percentil 80) → TRENDING_UP/DOWN/RANGING/HIGH_VOL_CHOP (bien repartidos, no
degenerado). regimeAdaptive.js: trend en TRENDING, mean-reversion en RANGING, FLAT en CHOP. Pre-registro
fechado, tribunal. VEREDICTO: ninguna celda pasa. Adaptive expR>0 n≥30 solo 2/6 (ambas ETH); ambas al
tribunal, ambas FALLAN (IC95 incluye 0, DSR 0.38/0.56 ≪0.95). Adaptación mejora al baseline 4/6 pero
sigue negativa salvo ETH (mover el edge "menos malo" ≠ crear edge). HALLAZGOS ricos: (a) mean-reversion
en rango PIERDE en los 3 pares → fadear rangos 1h cripto destruye plata tras fees; (b) trend SHORT en
TRENDING_DOWN positivo 2/3 (ETH/SOL +0.145/+0.161, BTC −0.184) — inconsistente, no pasa tribunal solo;
(c) FLAT en chop evitó whipsaw pero no bastó. SIGNIFICADO: ni las señales sueltas NI la adaptación por
régimen con indicador SIN REZAGO rescatan el direccional en cripto 1h. Se CIERRA honestamente la
búsqueda de un bot que PREDICE precio — 6 frentes direccionales agotados. El funding carry (no-predictivo)
es EL edge. La palanca "mejor indicador" era la correcta a probar y se probó a fondo; el techo no es el
indicador, es que el edge direccional no existe a esta escala. Tests 726. commit 1d11ca8. Para el futuro
(NO ahora, sin evidencia de deploy): el único flicker fue trend-SHORT en tendencia-bajista clara (perp).

## 📋 REVISIÓN DE ESTADO (14-sep-2026) — 7 semanas de datos que nadie había leído

### S9 — El carry en demo lleva 53 días cosechando y el APR OBSERVADO < APR ESPERADO (14-sep) 🟡
Primera lectura del `carry-monitor` desde el 23-jul (es MANUAL; nadie lo corrió en 7.5 semanas). Las 4
posiciones perp del demo siguen vivas desde el 22-23 jul. MEDICIÓN REAL (no backtest), notional $437.66,
53.15 días, 158 eventos de funding por par:
- Funding cosechado total **$3.1468 = 0.719% del notional → APR BRUTO observado 4.94%** (neto ~4.34% el
  1er año tras 0.6% de fees round-trip).
- Por par (observado vs esperado por el portero): BTC 6.10% vs 10.95% · LINK 8.28% vs 10.95% ·
  ETH 4.12% vs 8.42% · LTC 1.53% vs 10.95%.
🔑 **LECCIÓN NUEVA (la importante): el "APR esperado" del portero SOBREESTIMA entre 1.3× y 7×.** Se calcula
extrapolando el funding rate del instante (×3×365); el funding realizado es mucho menor porque varía y se
voltea a negativo en rachas. Para decidir con dinero hay que citar el APR OBSERVADO, nunca el esperado.
🔑 El observado bruto (4.94%) SUPERA al backtest OOS (~2% BTC/ETH): el régimen de funding jul-sep fue más
rico. **NO mover la portería por esto** — 53 días es una ventana, no evidencia; el backtest cubre 3 años.
🔑 El portero ACERTÓ: pausó LTC por funding positivo solo 68.2% (<75%) y LTC fue el peor carry (1.53%).
⚠️ HUECO OPERATIVO: el portero PAUSA pero NO CIERRA — LTC sigue abierto 53 días después de ser declarado
no elegible. Un portero que no cierra es media máquina.
⚠️ El −$113.22 de P&L no realizado NO es pérdida del carry: en el demo solo existe la pata PERP (short),
la pata SPOT nunca se abrió. El precio subió (ETH 1881→2515) y el short lo refleja; en un carry real el
spot lo cancela. CONSECUENCIA para el gate: lo validado en vivo es la COSECHA DE FUNDING y el riesgo de
margen, **NO la neutralidad delta end-to-end** (item 2 del GO-LIVE GATE sigue ⚠️, no ✅).
⚠️ AVAXUSDT quedó `pending` en el store desde el 23-jul (intento sin fill confirmado, previo al fix 46182f1).

### S10 — El bot EU está VIVO desde el 28-jul y nadie ha visto un solo resultado (14-sep) 🟡
`https://agente-trading-eu.onrender.com` responde (Express + `www-authenticate: Basic realm="AGENTE TRADING"`
= auth fail-closed funcionando). Corre paper 3 pares, threshold 7, **con las dos mejoras nuevas ENCENDIDAS**
(`REGIME_DISCIPLINE_ENABLED` + `POSITIONING_INTEL_ENABLED`, ambas OFF en local). Son ~7 semanas de paper con
la configuración nueva y la historia reseteada. NO se puede leer desde aquí: `DASHBOARD_USER/PASS` son
`sync:false` (solo Render y Luis los tienen). LECCIÓN: un experimento que corre y nadie mide no es un
experimento, es consumo de $7/mes. El valor está ahí esperando una lectura de 5 minutos.
CONTEXTO: la fecha de evaluación go-live del direccional (22-ago) PASÓ sin evaluación formal — correcto en
el fondo (S8 ya había cerrado el direccional por falta de edge el 23-jul), pero debe decirse explícitamente
en vez de dejarla vencida en silencio.
