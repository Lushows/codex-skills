# 27 — Riesgo de cola y cisnes negros

**Riesgo de cola** = el riesgo de los eventos raros pero devastadores que viven en las
"colas" de la distribución de retornos (los extremos). **Cisne negro** = un evento extremo
que casi nadie vio venir y que lo cambia todo (término de Nassim Taleb). Este módulo trata
del día que los modelos dicen que "no debería pasar" — y en cripto pasa.

## Cripto tiene colas gordas

Si los retornos de BTC siguieran una campana normal, las caídas de 20%+ en horas serían
imposibles en la práctica. En la realidad han ocurrido varias veces: crashes intradía
violentos, cascadas de liquidaciones, colapsos de plataformas (fechas y magnitudes exactas:
verificar antes de citar — la lección no depende del decimal). **Colas gordas** significa:
los extremos son mucho más frecuentes de lo que la intuición (y la estadística ingenua)
predicen. Diseñar como si no existieran es diseñar para quebrar en cámara lenta.

## Por qué el stop no siempre protege

El stop es una orden que se DISPARA a un precio, pero se EJECUTA al precio que haya:

1. **Slippage extremo**: en una caída violenta, entre que el stop se dispara y ejecuta, el
   precio ya está más abajo. El stop "a −2%" puede ejecutar a −5% o peor. El 0.05% de
   slippage modelado (módulo 07) es para días normales — en pánico es una ficción.
2. **Gaps / saltos**: cripto opera 24/7 (no hay gaps de apertura como en acciones), pero el
   precio puede SALTAR niveles en segundos cuando se evapora la liquidez del libro de
   órdenes. El stop no se ejecuta "en el nivel": se ejecuta después del salto.
3. **Fallas de infraestructura**: en los peores momentos los exchanges se congestionan,
   la API no responde, el bot no puede cerrar. Justo cuando más se necesita, el sistema de
   salida es menos confiable. (Y si el stop solo vive en el watcher local y Render se cae,
   no hay stop — módulo 02.)

Conclusión incómoda: en el evento de cola, la pérdida real puede ser un múltiplo de la
planeada. 1R planeado puede ser 2-3R ejecutado.

## Sizing: la única defensa real

Contra la cola no hay stop, ni indicador, ni predicción que valga. La única variable que
sigue bajo control cuando todo lo demás falla es **cuánto había en juego**:

| Defensa | ¿Funciona en el crash? |
|---|---|
| Stop loss | Parcial (slippage, saltos, API caída) |
| "Verlo venir" | No — por definición del cisne negro |
| Diversificar en cripto | No — correlación → 1 en pánico (módulo 25) |
| **Tamaño pequeño + techo de exposición** | **Sí — es aritmética, no predicción** |

Sobrevivir al peor día no se logra prediciéndolo: se logra habiendo apostado poco.

## Cómo aplica al AGENTE TRADING

Escenario de cola realista para el bot: 2 posiciones long (BTC+ETH, ~3% de riesgo efectivo,
módulo 25) + crash violento + slippage 2-3× el planeado → un solo evento podría costar
~5-9% del capital, no el 3% del plan. Con el techo de 1.5%/trade eso DUELE pero no mata —
esa es exactamente la función del techo. Reglas derivadas: (1) el techo de 1.5% y el máx de
2 posiciones NO se relajan por buen desempeño; (2) para el go-live, stops OCO en el exchange
y API keys sin permiso de retiro (módulo 29); (3) al evaluar el sistema, estresar los
números con slippage multiplicado — escenarios vía `Matematicas_lushows`; (4) capital en
vivo = solo dinero cuya pérdida TOTAL es aceptable, porque la cola existe.
