# 183 — Ed Seykota: el pionero de seguir reglas sin excepción

## Quién es

Ed Seykota es uno de los padres del **trend following sistemático**: en los años 70 fue pionero
en usar sistemas computarizados (primero con tarjetas perforadas) para operar futuros siguiendo
tendencias con reglas fijas. Se hizo famoso mundialmente por su entrevista en *Market Wizards*
(Jack Schwager, 1989), donde aparece como el trader que multiplicó cuentas de clientes por miles
de veces a lo largo de años (las cifras exactas son las que reporta el libro; el punto es la
magnitud y la consistencia, no el decimal).

**Trend following** = no predecir a dónde va el mercado, sino subirse a la tendencia cuando
existe y bajarse (rápido) cuando se acaba. Sin pronósticos, sin opiniones: reglas.

## Sus ideas núcleo

1. **Reglas sobre intuición.** El sistema decide; el humano solo lo mantiene y lo mejora entre
   sesiones, nunca lo desobedece en caliente. La intuición entra al diseñar las reglas, no al
   ejecutarlas.
2. **Corta las pérdidas ya.** Sus máximas de *Market Wizards*: los elementos del buen trading
   son "(1) cortar pérdidas, (2) cortar pérdidas y (3) cortar pérdidas".
3. **Deja correr las ganancias.** La otra mitad del trend following: los pocos trades enormes
   pagan todos los pequeños stops.
4. **"Everybody gets what they want out of the market."** Su frase más incómoda: *todos obtienen
   del mercado lo que quieren* — a veces lo que la persona busca no es ganar dinero sino emoción,
   drama, castigo o tener razón. El que "siempre pierde por mala suerte" quizás está obteniendo
   exactamente lo que su psicología busca. Es psicoanálisis brutal aplicado al trading, y explica
   por qué gente inteligente repite errores obvios durante años.
5. **La psicología ES el sistema.** Seykota dedicó su carrera posterior (Trading Tribe) a los
   sentimientos del trader, convencido de que el sistema técnico es la parte fácil.

## Regla vs. intuición: la tabla honesta

| | Reglas (Seykota) | Intuición discrecional |
|---|---|---|
| Repetible | Sí — cada decisión es auditable | No — depende del humor del día |
| Testeable | Sí — se puede simular y medir | Casi imposible |
| Inmune al miedo/euforia | Sí, si las reglas están en código | No — falla justo en los extremos, que es cuando más importa |
| Techo | Limitado por la calidad de las reglas | Más alto en manos de un genio... que casi nadie es |

La apuesta de Seykota (y de este proyecto): para el 99.9% de la gente, unas reglas decentes
ejecutadas siempre le ganan a una intuición brillante ejecutada a veces.

## Cómo aplica al AGENTE TRADING

El bot es seykotiano en su esqueleto: **las reglas viven en código y se ejecutan sin excepción**
— el gate de psicología corta antes de gastar tokens, el cooldown tras 3 pérdidas no se negocia,
el umbral de convicción 8 no baja porque "esta vez se siente bien". La wisdom library lo inyecta
precisamente **en rachas perdedoras**, cuando la tentación humana (y la de un LLM adulador)
sería aflojar las reglas para "recuperar".

Y la frase incómoda aplica al dueño: si algún día Luis se descubre queriendo intervenir
manualmente los trades del bot por emoción, la pregunta seykotiana es *"¿qué estás obteniendo
tú del mercado?"*. El bot existe, en parte, para que la respuesta no importe: las reglas corren
solas. Cambiar reglas está permitido — pero en frío, con datos, entre semanas; nunca con una
posición abierta.
