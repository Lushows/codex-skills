# La estructura de campaña para testear (el criterio de negocio)

> **Frontera**: aquí se decide **qué se testea y con qué criterio de negocio**. Cómo se arma la
> campaña —objetivo, tipo de puja, eventos, exclusiones, ventanas de atribución— es mecánica de
> plataforma: **para el detalle de configuración, invoca `facebook_ads_lushows`** (o
> `tiktok_ads_lushows` según el canal).

## Qué estás testeando de verdad

No estás testeando "la campaña". Estás testeando, en este orden y nunca al revés:

| Orden | Variable | Cuánto mueve el resultado | Cuándo se testea |
|---|---|---|---|
| 1 | **Ángulo** (qué dolor atacas) | 3-10x | Siempre primero |
| 2 | **Hook** (primeros 3 s) | 2-4x | Sobre el ángulo ganador |
| 3 | **Formato** (UGC, demo, antes/después) | 1,5-2,5x | Tercero |
| 4 | **Oferta** (bundle, precio, envío) | 1,5-3x | En la página, no en la campaña |
| 5 | Copy del anuncio | 1,1-1,3x | Cuarto |
| 6 | Audiencia | 1,0-1,2x en 2026 | Casi nunca (`245`, `246`) |

Testear audiencias antes que ángulos es el error más caro del principiante: gasta el presupuesto
buscando un 10% de mejora cuando tiene un 400% esperándolo en el creativo. Ver `247`.

## La unidad de test: el ángulo, no el anuncio

Un test válido compara **ángulos distintos del mismo producto**, cada uno con su propio creativo
completo. No compara dos versiones del mismo video con música diferente: eso es iteración (`263`), y
solo tiene sentido cuando ya sabes cuál ángulo gana.

| Test correcto | Test inútil |
|---|---|
| Ángulo "ahorro de tiempo" vs "ahorro de dinero" vs "regalo" | Mismo video con dos músicas |
| Hook pregunta vs hook demostración | Mismo hook con dos tipografías |
| UGC hablando vs demo sin voz | Mismo UGC con dos duraciones de 28 y 30 s |

## Cuántos ángulos a la vez, según presupuesto

| Presupuesto diario | Ángulos simultáneos | Días hasta decidir | Gasto del test |
|---|---|---|---|
| USD 10 | 2 | 5-7 | USD 50-70 |
| USD 15 | 3 | 4-6 | USD 60-90 |
| USD 25 | 4 | 4-5 | USD 100-125 |
| USD 50 | 5-6 | 3-4 | USD 150-200 |

Regla de piso: cada ángulo necesita gastar **al menos 1 vez el CPA objetivo** antes de que su
resultado signifique algo. Con CAC objetivo de USD 10,54 (modelo México), un ángulo con USD 6
gastados no dice nada. Ver `Matematicas_lushows` si quieres el cálculo de significancia.

## Umbrales de decisión del test (criterio de negocio)

| Métrica | Se mira cuando | Mata si | Sigue si |
|---|---|---|---|
| CTR de enlace | 1.000 impresiones | < 1,0% | > 1,5% |
| Costo por clic | 1.000 impresiones | > 2x el CPC país | ≤ CPC país |
| Vistas de página / clics | 50 clics | < 70% (problema técnico o de velocidad) | > 80% |
| Añadir al carrito / vistas | 100 vistas | < 3% | > 6% |
| CPA | 1,5x CAC objetivo gastado | > techo de CAC (30,73 MX) | < CAC objetivo (10,54) |

Referencias de calidad creativa para calibrar: conservador CTR 1,5% / CVR 2,0% prepago · creativo
bueno 2,2% / 3,0% · ganador real 3,0% / 4,0%.

## El presupuesto de test como línea del P&L

El test **no es inversión, es costo de investigación**. Presupuéstalo antes y dalo por perdido:

| Concepto | Proyecto México dic-2026 |
|---|---|
| Capital total | < USD 500 |
| Reservado para inventario local | 40-50% |
| Presupuesto de test | USD 120-180 |
| Presupuesto de escala si hay señal | El resto + reinversión |
| Regla de corte | Si con USD 150 no hay 1 ángulo bajo el techo de CAC, el problema es el producto o la oferta (`267`) |

## Lo que NO debes tocar durante un test

| Cosa | Por qué |
|---|---|
| El precio | Cambia el CVR y contamina la comparación entre ángulos |
| La página de destino | Igual: dos variables a la vez = cero aprendizaje |
| El presupuesto (subirlo a mitad) | Reinicia el aprendizaje del sistema; ver `244` |
| Pausar y reactivar anuncios | Fragmenta los datos |

Una variable por vez. Suena lento; es lo único rápido.

## Qué haces con los perdedores

| Resultado | Acción |
|---|---|
| CTR alto, CVR bajo | El ángulo atrae pero la página o la oferta no cierran (`267`) |
| CTR bajo, CVR alto en los pocos que llegan | Hook malo, mensaje bueno: reescribe los primeros 3 s (`249`) |
| Ambos bajos | Ángulo muerto: archívalo y no lo revivas |
| Ambos altos, CPA alto igual | CPM caro o AOV bajo: sube el bundle (`244` para presupuesto, oferta en la página) |

Archiva todo en una hoja: ángulo, hook, gasto, CTR, CVR, CPA, veredicto. En tres meses esa hoja vale
más que cualquier curso.

## Errores de encuadre (no de configuración)

1. **Testear 8 ángulos con USD 10/día**: ninguno junta datos.
2. **Matar a las 6 horas**: el sistema todavía está explorando.
3. **Dejar correr 14 días "a ver si repunta"**: un perdedor a 5 días sigue perdedor a 14 y te comió
   el capital de escala.
4. **Testear el producto y el ángulo al mismo tiempo**: si fracasa, no sabes cuál falló.
5. **Sacar conclusiones con 1 venta**: 1 venta es ruido. Ver `266`.

## Relacionados
`243` estructura para escalar · `244` presupuestos · `250` generar ángulos · `262` volumen creativo · `265` testear sin quemar plata · `266` métricas · `267` diagnóstico
