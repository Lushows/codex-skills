# 145 — Forecasting avanzado

`82` te dio el forecasting base: los dos métodos (hacia adelante desde la actividad y hacia atrás desde la meta), el desfase temporal por cohortes y los tres niveles de confianza. Este módulo sube el rigor para cuando ya tienes datos propios y varios meses de historia: **pipeline ponderado, escenarios, ajuste por capacidad y estacionalidad, y cómo no engañarte con tus propios números.** El objetivo es pasar de "creo que viene X" a un forecast que aguanta que te pregunten "¿por qué ese número?" con una respuesta defendible.

## El principio: un forecast es un rango con supuestos explícitos, nunca un número mágico

Un forecast de una sola cifra ("van a entrar $8.000") es mentira disfrazada de precisión: esconde los supuestos y no deja ver el riesgo. El forecast serio es siempre **un rango (pesimista–esperado–optimista) con los supuestos escritos al lado**. Así, cuando falla, sabes *qué supuesto* falló y corriges el modelo, en vez de solo encogerte de hombros. La honestidad del rango es lo que te da credibilidad —un forecast preciso y falso quema tu palabra; uno con rango y honesto la construye.

## Técnica 1 — Pipeline ponderado (weighted pipeline)

En vez de tratar todo el pipeline como igual de probable, asignas a cada etapa una **probabilidad de cierre histórica** y multiplicas. Es el refinamiento de los "niveles de confianza" de `82`:

```
ETAPA                          $ en etapa   × prob. hist.  = $ ponderado
Reunión agendada (comprom.)     $4.500      × 20%           $900
Reunión realizada                $3.000      × 35%           $1.050
SQL con siguiente paso           $6.000      × 45%           $2.700
Propuesta enviada                $2.500      × 65%           $1.625   ← zona AE
                                                            ─────────
Forecast ponderado del pipeline actual:                    ~$6.275
```

Dos advertencias: (1) las probabilidades deben venir de **tu** historia, no inventadas —al inicio usa benchmarks de `81`/`96` y márcalos como supuestos; (2) de "propuesta" en adelante es terreno del AE, y la gestión fina de probabilidad por etapa es `ventas_lushows`. El SDR pondera con confianza hasta SQL.

## Técnica 2 — Escenarios (pesimista / esperado / optimista)

No proyectes un solo futuro; proyecta tres, variando los 2–3 supuestos que más mueven el resultado (normalmente reply rate y tasa de cierre):

```
Supuesto que varía:    reply rate   ·  tasa de cierre
PESIMISTA              4.0%          ·  22%      → ~$2.400
ESPERADO              5.2%          ·  30%      → ~$3.900   ← el que reportas como centro
OPTIMISTA             6.5%          ·  38%      → ~$5.800
```

Reportas el rango completo y **nombras qué tendría que pasar** para caer al pesimista (ej.: "si el bounce sube y el reply baja a 4%, caemos a $2.400"). Esto convierte el forecast en un semáforo de riesgo, no en una promesa.

## Técnica 3 — Forecast por capacidad (¿el equipo da para la meta?)

El forecast hacia atrás de `82` te dice cuánta actividad necesitas; este cruza esa actividad contra la **capacidad real** del equipo para ver si el número es alcanzable o fantasía:

```
Meta implica:          3.200 contactos/mes  (del forecast hacia atrás, 82)
Capacidad real:        1 SDR × ~800 tocados/día útil × 20 días = ...
                        pero solo ~30–50 correos/buzón/día seguros (44)
                        → con 6 buzones activos = ~1.800 correos/mes limpios
Veredicto:             la meta exige ~1.8x la capacidad de un SDR/6 buzones
                        → o añades buzones/SDR (85, 89) o bajas la meta
```

Si el forecast hacia atrás pide más de lo que el equipo puede entregar, el problema no es el forecast: es que **la meta es imposible con los recursos actuales** y hay que escalar (`89`) o recalibrar. Ajusta además por **ramp**: un SDR nuevo produce ~30% el mes 1 y llega a full hacia el mes 3 (ver `86`) —no le forecast-es capacidad plena desde el día 1.

## Técnica 4 — Estacionalidad y ciclo

Los ratios no son constantes todo el año. Ajusta por patrones conocidos:

- **Diciembre–enero y Semana Santa en LatAm:** reply rates caen (todos fuera). No forecast-es un enero como un marzo.
- **Fin de trimestre:** más urgencia de cierre, pero también bandejas saturadas.
- **Tu propio ciclo de venta:** si es ~45 días, el revenue de un mes ya se determinó 1–2 meses atrás (la ley de cohortes de `82`). El forecast del mes en curso es casi inamovible; donde mueves la aguja es en la actividad de *hoy* para dentro de 60 días.

## Ejemplo: reporte de forecast avanzado (solista/agencia, LatAm)

```
FORECAST — margen próximos 60 días
  Pipeline ponderado (actual):        ~$6.275   (weighted, técnica 1)
  Escenarios (actividad en curso):
     pesimista  $2.400 | esperado $3.900 | optimista $5.800
  ─────────────────────────────────────────────────────────
  RANGO REPORTADO:   $3.900 (centro), banda $2.400–$5.800

  Supuestos:  reply 5.2% · cierre 30% · show 78% · ciclo 45 días
  Ajustes:    -15% por temporada (mitad de diciembre)
              SDR nuevo a 60% de ramp (mes 2)
  Riesgo #1:  bounce en 4% → si sube, caemos al pesimista
  Palanca:    la actividad de HOY define el revenue de ~sep, no de este mes
```

Todo número clave de este reporte —las multiplicaciones ponderadas, los escenarios, si la meta cabe en la capacidad— **córrelo en `Matematicas_lushows`** para que el redondeo y la aritmética no te dejen corto o largo.

## Errores comunes

- **Un solo número.** Sin rango ni supuestos, es una promesa que quema tu credibilidad al fallar.
- **Probabilidades inventadas** en el pipeline ponderado. Usa tu historia; si no la tienes, marca benchmarks como supuestos y corrige al mes 1.
- **Ignorar capacidad y ramp.** Forecast-ear una meta que el equipo no puede físicamente entregar.
- **Constante todo el año.** No ajustar por temporada baja LatAm → forecast inflado en diciembre/enero.
- **Forecast-ear cierres como si el SDR los controlara.** El SDR proyecta con firmeza hasta SQL; el cierre y su probabilidad por etapa es `ventas_lushows`.

## La frontera

El SDR forecast-ea actividad → reuniones → SQL con rigor. La probabilidad fina por etapa del deal ya en manos del AE (weighted pipeline de cierre, commit/best-case del vendedor) → `ventas_lushows`. Toda la aritmética exacta (ponderaciones, escenarios, intervalos, si un cambio es señal o ruido) → `Matematicas_lushows`. Conectar el forecast con el modelo financiero y el CAC del negocio → `economist_lushows` y `149`.

## Siguiente paso

Toma tus ratios reales (`81`, `144`) y arma el reporte de ejemplo: pipeline ponderado + tres escenarios + chequeo de capacidad, con supuestos y riesgo escritos. Reporta rango, nunca punto. Si la meta no cabe en la capacidad → escalar (`89`). Manda cada cálculo a `Matematicas_lushows`; liga el resultado al negocio con `economist_lushows`.
