# 68 — Manipulación y wash trading

Cripto es un mercado parcialmente regulado donde conviven fondos serios y estafadores. Este
módulo es el mapa de las trampas — y la explicación de por qué el universo BTC/ETH del bot
es en sí mismo un escudo.

## Las tres trampas principales

### Spoofing (órdenes fantasma)
Poner órdenes limit **gigantes y visibles** en el libro sin intención de ejecutarlas, para
fingir demanda u oferta. Los demás reaccionan al "muro", el spoofer logra el precio que
quería y cancela. Cómo se ve: muros enormes que aparecen y desaparecen en segundos sin
ejecutarse jamás. Lección práctica: el libro visible es teatro parcial (`62`) — no tomar
decisiones por "muros".

### Wash trading (volumen falso)
La misma entidad se compra y se vende a sí misma para inflar el volumen. Un token "mueve"
$50M diarios pero es una manguera dándose vueltas. Objetivo: aparecer en rankings, atraer
listados y víctimas. Estudios de la industria han estimado durante años que una fracción
enorme del volumen reportado en exchanges menores es lavado (proporciones exactas: verificar
al día). Señales: volumen altísimo con libro delgado y spread ancho — volumen real crea
profundidad; el falso, no.

### Pump & dump (inflar y soltar)
Un grupo acumula un token ilíquido en silencio, lo infla con compras coordinadas + bombo en
redes ("¡va a explotar!"), el retail entra por FOMO, y los organizadores venden todo en la
cima. El gráfico: subida vertical en minutos-horas, colapso igual de vertical. En tokens de
micro-capitalización, mover el precio 100% cuesta relativamente poco. Quien entra tarde no
está "llegando temprano a la fiesta": es el pagador de la fiesta (exit liquidity, `59`).

## Por qué BTC/ETH grandes nos protegen

| Factor | Token chico | BTC/ETH en Binance |
|---|---|---|
| Costo de mover el precio 5% | Bajo (miles de $) | Astronómico (cientos de millones) |
| Wash trading creíble | Fácil | Inútil: el volumen real ya es enorme |
| Pump & dump viable | Sí — es el hábitat natural | No a escala relevante |
| Vigilancia regulatoria | Casi nula | Alta (ETFs, mercados de futuros regulados) |

La manipulación no desaparece en BTC/ETH (el spoofing y la caza de stops existen ahí
también, `67`), pero pasa de "riesgo existencial" a "ruido de fondo" que el stop por
volatilidad y el tamaño prudente ya absorben.

## Cómo aplica al AGENTE TRADING

- La elección BTC/ETH spot en el exchange más líquido es la **defensa estructural**: el bot
  simplemente no habita el ecosistema donde el pump & dump y el wash trading operan.
- Regla permanente: si algún día se evalúa añadir un par, el filtro previo es liquidez REAL
  (profundidad de libro y spread, no volumen reportado — el volumen se falsifica, la
  profundidad cuesta plata).
- El bot no lee libro ni volumen de terceros exchanges, así que el spoofing y el wash
  trading no pueden engañar sus señales actuales (velas + régimen). Mantener esa dieta simple
  es una virtud, no una carencia.
