# 15 — Journal y registro

El **journal de trading** es el diario donde queda escrito cada trade con su contexto completo.
Es la diferencia entre "creo que me va bien" y "sé exactamente qué funciona y qué no". Sin journal
no hay aprendizaje: solo anécdotas que la memoria distorsiona (recordamos los ganadores, olvidamos
los perdedores).

## Qué registrar por cada trade (mínimo obligatorio)

| Campo | Por qué importa |
|---|---|
| Fecha/hora de entrada y salida | Detectar patrones por hora/día y clustering |
| Par (BTC/ETH) y dirección (LONG) | Atribución por activo |
| Precio entrada, stop, target | Verificar que R:R ≥ 1:2 se respetó |
| Tamaño y riesgo en USD | Confirmar techo 1.5% |
| Régimen detectado | ¿En qué estado de mercado funciona la estrategia? |
| Convicción (1-10) y su justificación | Auditar si la nota predice resultados |
| Indicadores al momento (RSI, MACD, SMA) | Reconstruir el "por qué" sin memoria selectiva |
| Resultado en $ y en R | Comparar trades entre sí en unidades iguales |
| Costos (comisión + slippage) | El ~0.30% redondo se come edges pequeños |
| ¿Se respetó el protocolo? (sí/no + nota) | Separar error de proceso vs mala suerte |

**Término:** *R* = múltiplo del riesgo. Un trade que arriesgó $15 y ganó $30 hizo "+2R". Medir en R
hace comparables trades de distinto tamaño.

## Cómo lo hace el bot

- **`traderMemory`** guarda cada trade cerrado con su contexto — es el journal automático que
  además alimenta el paso 3 del pipeline (la memoria consulta el pasado antes de cada decisión).
- **`analyses`** guarda cada análisis del ciclo de 2h, incluso los que NO terminaron en trade.
  Esto es oro: permite auditar los "no-trades" (¿nos perdimos entradas buenas? ¿el filtro sirve?).
- Ventaja sobre un humano: el bot registra el 100% sin sesgo. Un humano promedio "olvida"
  anotar sus peores trades.

## La revisión semanal (lo que hace Luis, ~30 min)

1. **Leer cada trade cerrado de la semana** y responder: ¿protocolo respetado? ¿el stop estaba
   donde el análisis lo pedía?
2. **Buscar patrones con ≥3 casos**: por precio (como el hallazgo $1.788 vs $1.760), por hora,
   por régimen, por convicción. Con menos de 3 casos es ruido, no patrón.
3. **Revisar los no-trades de `analyses`**: ¿la convicción alta que no ejecutó (por límites)
   habría ganado? ¿los rechazos fueron correctos?
4. **Anotar UNA lección con fecha** (si la hay) en el módulo `10`/`11` de esta skill. Una por
   semana bien digerida vale más que diez apuntes sueltos.
5. **NO cambiar el sistema en caliente.** Las lecciones se acumulan; los cambios se hacen uno a la
   vez y con hipótesis (ver `195`).

## Trampas del journaling

- **Journal que solo mira resultados**: "gané/perdí" sin contexto no enseña nada (ver `00`).
- **Racionalizar después**: el registro debe capturarse EN el momento de la decisión (el bot lo
  hace por diseño; un humano tiende a reescribir la historia).
- **Sobre-reaccionar a una semana**: con 10 trades totales, una semana son 1-3 trades. Anécdota.

## Cómo aplica al AGENTE TRADING

- El journal ya existe y es automático (traderMemory + analyses). El trabajo pendiente es el
  **hábito humano**: la revisión semanal de Luis con las 5 preguntas de arriba.
- Las dos lecciones reales del proyecto (FOMO en precio extendido, clustering de entradas)
  salieron EXACTAMENTE de este proceso — el journal ya pagó su costo.
- El trade con convicción 0 se detectó gracias al registro: sin journal, ese bug seguiría vivo.
- Estadísticas sobre el journal (promedios, correlaciones) → `Matematicas_lushows`.
