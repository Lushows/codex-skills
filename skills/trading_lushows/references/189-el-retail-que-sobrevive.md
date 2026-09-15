# 189 — El retail que sobrevive: el perfil estadístico y por qué este proyecto lo imita

## La verdad incómoda primero

"Retail" = el trader individual con su propio dinero (nosotros), en contraste con instituciones.
La evidencia disponible es consistente y fea: **la gran mayoría del retail activo pierde
dinero.** Estudios académicos sobre day traders (los de Barber y Odean sobre Taiwán son los más
citados: solo un porcentaje pequeñísimo gana de forma persistente tras costos) y los avisos
obligatorios de los brokers de CFDs en Europa (que suelen declarar que ~70-80% de sus cuentas
retail pierden) apuntan en la misma dirección. Cifras exactas: **verificar estudios al día** —
varían por mercado, época y definición de "trader". Pero la dirección no varía: el juego por
defecto se pierde.

Quien te venda trading sin empezar por este párrafo, te está vendiendo humo.

## Por qué pierde la mayoría (las causas se repiten)

| Causa | Mecánica |
|---|---|
| Sobreoperar | Cada trade paga comisión y slippage; operar por aburrimiento es donar dinero en cuotas |
| Tamaño excesivo | Riesgos de 5-10% por trade → una racha normal de pérdidas es la ruina (ver módulo 184) |
| Sin sistema | Cada decisión se toma en caliente, con miedo o euforia — justo los peores consejeros |
| Cortar ganadores, aguantar perdedores | El sesgo humano documentado (efecto disposición): se asegura lo bueno rápido y se "espera" lo malo hasta el fondo |
| Apalancamiento | Convierte todo lo anterior en fatal más rápido |
| Rendirse en el valle | El aprendizaje real toma años; la mayoría quema su capital y su ánimo en los primeros meses |

## El perfil del que sobrevive

La minoría que persiste comparte rasgos aburridos, no geniales:

1. **Tiene un sistema escrito** y lo sigue incluso cuando pica la mano (Seykota, módulo 183).
2. **Arriesga poco por trade** (1-2%), de modo que ninguna racha lo saca del juego (Kovner, 184).
3. **Opera poco:** espera calidad en vez de fabricar cantidad (Livermore, 181).
4. **Mide con honestidad:** registro de cada trade, costos incluidos, sin contabilidad mental
   creativa. Sabe su win rate y su drawdown reales.
5. **Piensa en años:** su métrica es sobrevivir y componer, no el mes espectacular.
6. **Trata el trading como negocio con costos**, no como casino con vibras.

Nada de esto garantiza ganar (nadie puede garantizarlo). Garantiza algo previo y necesario:
**seguir vivo el tiempo suficiente para que un edge, si existe, se exprese.**

## El espejo del proyecto

El AGENTE TRADING es, punto por punto, ese perfil convertido en código:

| Rasgo del sobreviviente | En el bot |
|---|---|
| Sistema escrito e inviolable | Reglas en código: umbral 8, régimen primero, gates de psicología |
| Sizing chico | 1.5% máx por trade, 2 posiciones máx, cero apalancamiento |
| Operar poco | ~10 trades en 6 semanas; HOLD es el resultado más común, por diseño |
| Medición honesta | Comisión y slippage simulados desde el día uno; equity, drawdown y Sharpe en `/api/metrics`; CSV exportable |
| Años, no meses | Meses de paper antes del go-live (22-ago-2026), y live chico después |
| Sin emociones en caliente | Las decisiones las toma el pipeline, no el estado de ánimo del dueño |

## Cómo aplica al AGENTE TRADING

Este módulo es la respuesta a "¿y para qué tanto freno, si así se gana poquito?": porque la
estadística dice que el retail no pierde por ganar poquito — pierde por intentar ganar mucho,
rápido. La apuesta del proyecto es explícita y humilde: renunciar al jackpot para comprar
**permanencia**, y dejar que años de consistencia (medida, no sentida) demuestren si hay edge.
Si el bot algún día presume rendimientos, este módulo existe para preguntarle: ¿y el drawdown?,
¿y los costos?, ¿y cuántos años lleva? — las tres preguntas que el humo no resiste.
