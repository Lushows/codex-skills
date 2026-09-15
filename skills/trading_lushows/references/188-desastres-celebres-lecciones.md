# 188 — Desastres célebres: LTCM, 3AC, FTX y Mt. Gox como manual de qué no hacer

## Para qué estudiar ruinas ajenas

Es la educación más barata que existe: otros pagaron miles de millones por estas lecciones y
nosotros las leemos gratis. Los cuatro casos son distintos en la superficie y idénticos en el
fondo: **apalancamiento, custodia mal resuelta y hybris** (la soberbia de creerse la excepción).

## Los cuatro desastres en una tabla

| Caso | Qué era | Qué pasó | Causa raíz |
|---|---|---|---|
| **LTCM** (1998) | Hedge fund con dos premios Nobel (Merton, Scholes) en el equipo | Sus apuestas "estadísticamente seguras" se rompieron con la crisis rusa; el apalancamiento enorme (deuda de ~25× el capital o más) convirtió un mal trimestre en colapso sistémico; la Fed coordinó el rescate | Apalancamiento extremo + fe ciega en modelos ("esto no puede pasar") |
| **Three Arrows Capital / 3AC** (2022) | Fondo cripto estrella de Singapur | Apostó apalancado y concentrado (LUNA/UST entre otros); al caer el mercado, impagos en cadena que arrastraron a sus prestamistas (Voyager, BlockFi...) | Apalancamiento + concentración + creer que el ciclo alcista era permanente |
| **FTX / Alameda** (2022) | Exchange top-3 mundial + su trading firm hermana | FTX usó depósitos de clientes para tapar huecos de Alameda; al conocerse, corrida bancaria y quiebra en días; fraude penal (SBF condenado en 2023) | Custodia violada: el exchange usó fondos ajenos; cero separación ni auditoría |
| **Mt. Gox** (2014) | El exchange que llegó a concentrar la mayoría del volumen de BTC | "Perdió" cientos de miles de BTC de clientes (hackeos sostenidos + pésima gestión); quiebra; acreedores esperaron ~una década | Custodia técnica incompetente: guardar cripto ajeno sin la seguridad para hacerlo |

## La lección común, desarmada

1. **El apalancamiento convierte errores en muerte.** Sin deuda, LTCM y 3AC habrían tenido años
   malos; con deuda, dejaron de existir. El apalancamiento no mejora la estrategia — solo acorta
   el tiempo disponible para tener razón.
2. **La custodia es un riesgo aparte del mercado.** FTX y Mt. Gox no perdieron por trades: los
   clientes perdieron por DÓNDE estaba guardado el dinero. Puedes operar perfecto y perderlo
   todo porque tu exchange era un fraude o un colador.
3. **La hybris es el acelerante.** Nobels (LTCM), gurús del ciclo (3AC), el niño genio de la
   industria (FTX): en todos los casos, la reputación desactivó el escepticismo — el propio y
   el ajeno. "Somos demasiado listos para quebrar" es la última frase antes de quebrar.

## Qué regla del bot previene cada desastre

| Desastre | La regla del AGENTE TRADING que lo previene |
|---|---|
| LTCM | **Cero apalancamiento** (spot puro) + riesgo 1.5% por trade: un modelo equivocado cuesta poco y deja tiempo para corregir |
| 3AC | Máx 2 posiciones + sizing capado + régimen primero: la concentración eufórica apalancada no puede ocurrir por diseño |
| FTX | En live: **el exchange es lugar de paso, no bodega** — solo el capital operativo en Binance, el resto en custodia propia; y elegir exchanges grandes/regulados sabiendo que "grande" no fue suficiente para FTX (por eso el monto expuesto se limita) |
| Mt. Gox | La misma regla de custodia + retiros deshabilitados en la API key (módulo 167): ni el bot ni un atacante pueden vaciar la cuenta |

## Cómo aplica al AGENTE TRADING

Estos cuatro nombres son la respuesta preparada a las tentaciones que llegarán con el go-live:
"con 5× de apalancamiento ganaríamos más" → LTCM/3AC; "deja todo el capital en el exchange, es
más cómodo" → FTX/Mt. Gox; "el bot lleva meses ganando, relajemos las reglas" → hybris, el
ingrediente de los cuatro. El proyecto está diseñado para que la versión pequeña de estos
desastres **no pueda ocurrir ni queriendo**. Mantenerlo así.
