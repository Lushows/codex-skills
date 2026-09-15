# 106 — DCA estratégico: inversión, entrada y la línea prohibida

**DCA** (*dollar-cost averaging*, "promediar costo en dólares") = comprar un monto fijo a
intervalos fijos — ej. $100.000 COP de BTC cada quincena — sin importar el precio. Compras más
unidades cuando está barato y menos cuando está caro, y tu precio promedio se suaviza. Es de
las pocas ideas de este mundo que funciona mejor cuanto MENOS se piensa... en su contexto
correcto. La palabra clave es contexto: hay tres cosas distintas que la gente llama "DCA".

## 1. DCA como inversión (no es trading)

Es acumular un activo en el que crees a años vista, automatizando la compra para sacar la
emoción de la ecuación. No hay stop, no hay target, no hay edge que medir: hay una tesis de
largo plazo ("BTC valdrá más en 5-10 años") y disciplina de ahorro.

| | DCA inversión | Trading (nuestro juego) |
|---|---|---|
| Horizonte | Años | Días/semanas (swing) |
| Salida | No definida (o muy lejana) | Stop y target ANTES de entrar |
| Riesgo | Todo el capital aportado sigue la tesis | 1.5% por trade, acotado |
| Métrica | Precio promedio vs precio futuro | Expectancy, profit factor |
| Se juzga por | La tesis a años | El proceso trade a trade |

Ninguno es "mejor": son juegos distintos con reglas distintas. El error es mezclarlos — y las
cuentas se mezclan solas si no se separan a propósito: capital de inversión y capital de
trading en bolsillos distintos, con reglas distintas, sin transfusiones entre ellos.

## 2. DCA de entrada (esto sí es técnica de trading)

Escalonar UNA entrada planificada: en vez de comprar toda la posición de un golpe, dividirla
en 2-3 tramos alrededor de la zona de entrada. Es válido SOLO si se cumple todo esto:

- La posición TOTAL (suma de tramos) respeta el riesgo por trade (1.5%) — se planea completa
  desde el inicio, no se improvisa tramo a tramo.
- El stop es UNO para toda la posición, definido antes del primer tramo.
- Los tramos estaban en el plan original. Si el precio invalida la tesis antes de completar,
  no se completan — se ejecuta el stop de lo que haya.

Bien hecho, reduce el riesgo de "entré todo en el peor tick". Es refinamiento, no salvavidas.

## 3. Promediar abajo (la línea prohibida)

**Promediar abajo** = la posición va perdiendo y compras MÁS para "bajar el promedio". Se
disfraza de DCA pero es lo contrario: no es un plan, es la negación de que el trade salió mal.

Por qué está prohibido en este método:
- **Aumenta el riesgo justo cuando el mercado te está dando la razón en contra.** El plan decía
  arriesgar 1.5%; promediando ya son 3%, luego 4.5%, en el mismo trade perdedor.
- **Destruye la matemática del sistema**: el R:R 1:2 y la expectancy suponen pérdidas acotadas.
  Una sola posición promediada que se va al fondo puede borrar meses de trades disciplinados.
- **Es la emoción disfrazada de estrategia**: la incapacidad de aceptar la pérdida chica, que
  es exactamente lo que el stop existe para forzar.

La prueba del algodón para distinguirlo del DCA de entrada legítimo: **¿este tramo estaba en el
plan escrito ANTES de abrir el trade?** Si la respuesta es no, es promediar abajo, sin importar
cómo se le llame.

## Cómo aplica al AGENTE TRADING

- El bot NO hace DCA en ninguna forma hoy: una entrada, un stop, un target. Correcto para esta
  etapa — menos partes móviles, más fácil de auditar.
- Promediar abajo debe ser **imposible por código** (ver `85`), no solo indeseable: el bot no
  agrega tamaño a una posición abierta en pérdida, punto. Guardrail estructural.
- DCA de entrada escalonada es un refinamiento posible POST go-live, solo si la muestra de
  trades sugiere que el timing fino de entrada nos cuesta — medido, no intuido (ver `89`).
- Si Luis quiere acumular BTC a años (DCA inversión), es válido — pero es otro bolsillo y otro
  juego: nunca desde el capital del bot ni mezclado con sus métricas.
