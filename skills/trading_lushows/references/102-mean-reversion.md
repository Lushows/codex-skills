# 102 — Mean reversion (reversión a la media)

> La apuesta opuesta al trend following: cuando el precio se estira demasiado lejos de su
> promedio, tiende a volver. Se compra la caída exagerada, se vende el rebote. Funciona…
> hasta el día que no vuelve.

## La idea

La "media" es el precio promedio reciente (ej. una media móvil). En mercados LATERALES
(en rango), el precio oscila alrededor de ella: se aleja, vuelve, se aleja, vuelve. El
mean reverter compra cuando el precio cayó "demasiado" bajo la media y vende cuando regresa.
Herramientas típicas: bandas de Bollinger, RSI en sobreventa, distancia a la media móvil.

Requisito invisible: que el mercado ESTÉ en rango. La misma señal que gana plata en rango
la pierde toda en tendencia.

## La matemática incómoda: el espejo exacto del trend following

| Métrica | Mean reversion típica | Trend following (módulo 101) |
|---|---|---|
| Win rate | Alto (60-80%): casi siempre el precio sí vuelve | Bajo (30-45%) |
| Ganadores | Pequeños: el viaje de vuelta a la media es corto | Grandes |
| Perdedores | **GRANDES o catastróficos** cuando no vuelve | Pequeños (corte rápido) |
| Sensación | Ganar seguido, sentirse genio | Perder seguido, sentirse tonto |

El peligro está en la última fila: el mean reversion SE SIENTE mejor de lo que ES. Rachas
largas de ganancias chicas construyen confianza… y un solo trade donde "esta vez sí es una
tendencia de verdad" devuelve meses de ganancias. Muchos blowups famosos de la historia
financiera son, en el fondo, mean reversion sin límite de pérdida.

## "Recoger cuchillos que caen"

Así se le dice a comprar caídas fuertes: si atrapas el cuchillo en el rebote, aplausos; si lo
atrapas cayendo, te corta. En cripto los cuchillos caen MUY rápido: una caída de 10% puede ser
la sobreventa perfecta para comprar… o la primera pata de un -40%. Sin un stop innegociable,
mean reversion en cripto es jugar a la ruleta con buena racha inicial.

Variante prohibida en nuestra casa: **promediar hacia abajo** ("si bajó más, compro más porque
está más barato") — es mean reversion doblando la apuesta contra la evidencia. Prohibido en el
bot por regla, sin excepciones (ver módulo 106 para la diferencia con DCA legítimo).

## ¿Tiene lugar legítimo?

Sí: con régimen bien identificado (rango confirmado), stops duros, y tamaño chico. Hay quants
serios que la operan. Pero exige DETECTAR el régimen (¿rango o tendencia?) — que es el problema
difícil de verdad — y disciplina de salida perfecta, porque el modelo de error es catastrófico.

## Cómo aplica al AGENTE TRADING

- **No es nuestra estrategia.** El bot busca continuación/estructura alcista, no comprar
  cuchillos. Si Claude propone "comprar porque cayó mucho", esa señal es sospechosa por diseño
  y el filtro de convicción debería matarla.
- La lección FOMO del bot (entrar tarde a un movimiento extendido) es del módulo 104, pero su
  gemela es igual de peligrosa: "está barato porque cayó" no es tesis, es reversión sin régimen.
- Si algún pivote futuro explorara mean reversion, el stop en el exchange (OCO) y el límite
  diario de -3% (módulo 94) serían aún MÁS críticos que hoy — el modelo de error de esta
  familia es exactamente el que esos rieles existen para contener.
