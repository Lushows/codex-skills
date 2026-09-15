# Presupuesto de test por producto

## Cuánto cuesta saber si un producto sirve

| Etapa | Medida real | En México (CPC Q4 0,65) | Qué buscas |
|---|---|---|---|
| Validación inicial | **60 clics** | USD 39 | ¿hay clics? ¿hay carritos? |
| Test completo | **175 clics** | USD 114 | 3-5 ventas con economía positiva |
| Confirmación | +150 clics | USD 212 acum. | ¿la holgura aguanta? |
| Escala inicial | según holgura | — | ver `234` |

> ⚠️ **La cifra de "USD 200-300 por test" es un número ESTADOUNIDENSE y no se traduce.** Son ~175
> clics a CPC gringo de USD 3,90 en temporada. En México esos mismos 175 clics cuestan **USD 114**;
> en Colombia, **USD 107**. Repetir el número en dólares de un curso de EE.UU. te hace creer que con
> USD 500 solo tienes dos intentos. **El presupuesto de test se mide en CLICS, no en dólares.**

## La regla correcta: se mide en clics

La pregunta real no es "¿cuánto gasto?" sino **"¿cuántos clics sin venta necesito para afirmar con
confianza que esto no convierte?"**. Lo resuelve la **regla de los tres** de la estadística: con
**0 éxitos en N intentos**, la tasa real está por debajo de **3/N** con 95% de confianza.

| Clics sin venta | CVR máxima al 95% | Conclusión |
|---|---|---|
| 50 | 6,0% | Insuficiente: no puedes descartar nada |
| 100 | 3,0% | Descartas CVR > 3%: aún dudoso |
| **150** | **2,0%** | **Suficiente para matar** |
| 200 | 1,5% | Muy seguro |
| 300 | 1,0% | Exceso: estás pagando por certeza que no usas |

**Umbral práctico: ~175 clics sin venta y el producto se cierra.** Traducido a dinero, en Q4:

| País | CPC Q4 | Costo de 175 clics |
|---|---|---|
| Estados Unidos | 3,90 | **683** |
| Reino Unido | 2,83 | 495 |
| Alemania | 2,10 | 368 |
| España | 1,23 | 216 |
| Chile | 0,87 | 152 |
| **México** | **0,65** | **114** |
| Colombia | 0,61 | 107 |
| Perú | 0,52 | 91 |

## El test escalonado (lo que de verdad se hace)

No pagues los 175 clics de entrada. Mata barato al que no da señal de vida, y reserva el presupuesto
completo para los que sí. Ejemplo con México (CPC Q4 = USD 0,65):

| Etapa | Clics | Costo | Criterio de muerte | % que muere aquí |
|---|---|---|---|---|
| 1 | 60 | USD 39 | Cero adiciones al carrito | **55%** |
| 2 | +115 (175 acum.) | USD 114 acum. | Cero ventas a los 175 clics | 33% |
| 3 | +150 | USD 212 acum. | Hay ventas pero sin margen | 2% |

Un test **completo** cuesta USD 212. Pero como la mayoría muere en la etapa 1, el **costo esperado
por test es de USD 85**. Esa es la cifra con la que se planea el capital, no la del test completo.

## Por qué no menos

Necesitas suficientes impresiones para que el algoritmo salga de la fase de aprendizaje y para que
tus tasas no sean ruido.

```
CAC estimado = CPM ÷ 1.000 ÷ (CTR × CVR × tasa de cobro)
```

México, escenario conservador (CTR 1,5%, CVR 2,0%, cobro 97%, CPM 4,50):

```
pedidos cobrados por impresión = 0,015 × 0,020 × 0,97 = 0,000291
CAC = (4,50 ÷ 1.000) ÷ 0,000291 ≈ USD 15,46
```

Ese CAC es el de un producto que **sí** convierte. Para el que no convierte, el CAC es infinito y lo
único que puedes medir es la **ausencia de ventas** — y eso se mide en clics, no en dólares, porque
es lo que fija el tamaño de la muestra. De ahí el umbral de 175 clics.

## La señal: qué cuenta como "sirve"

| Señal | Umbral |
|---|---|
| Ventas | **3-5 ventas** |
| Economía | holgura ≥ 1,3x en escenario conservador |
| Consistencia | las ventas repartidas, no todas de un mismo día raro |
| Origen | no todas de retargeting ni de conocidos |

**Tres ventas con holgura 0,8x no son señal: son tres pérdidas.** El criterio es ventas *con
economía positiva*, no ventas.

## Semáforo de decisión durante el test

Se lee por **clics acumulados**, no por dólares — así la tabla sirve igual en México que en España.
La columna de dólares es solo la traducción a CPC mexicano de temporada (0,65).

| Clics | ≈ USD (MX) | Situación | Acción |
|---|---|---|---|
| 30 | 20 | CTR < 0,7% | matar **creativo**, no producto (`264`) |
| 60 | 39 | CTR bien, **0 carritos** | **matar producto**: no hay deseo (`210`) |
| 60 | 39 | hay carritos, 0 compras | problema de precio, pago o confianza (`216`) |
| 100 | 65 | 1-2 ventas, holgura ≥ 1,3x | seguir hasta 175 |
| **175** | **114** | **0 ventas** | **matar producto** (CVR < 2% al 95%) |
| 325 | 212 | 3-5 ventas, holgura ≥ 2,0x | validado: escalar (`234`) |
| 325 | 212 | ventas pero holgura < 1,3x | arreglar oferta antes de escalar (`218`) |

## Estructura del test

| Parámetro | Recomendación |
|---|---|
| Creativos | 2-3, ángulos distintos (`213`), no variaciones del mismo |
| Presupuesto diario | USD 20-50 |
| Duración | 3-5 días sin tocar nada |
| Público | amplio; deja que el algoritmo busque |
| Objetivo | compras, no clics ni interacción |

**No toques la campaña durante las primeras 48 horas.** Cada edición reinicia el aprendizaje y
quema presupuesto de test en recalibrar.

## Costo total real de un test

El presupuesto de pauta no es todo lo que cuesta probar un producto:

| Renglón | USD típico |
|---|---|
| Pauta (costo **esperado**, escalonado, México) | 85 |
| Muestra del producto (envío express) | 15-60 |
| Producción de creativos (si grabas tú) | 0 |
| Producción con creador/UGC | 30-120 |
| Fotos y página | 0-50 |
| **Total por producto** | **250-500** |

Con capital menor a USD 500 **no puedes** pagar el paquete completo por producto. La salida es:
grabar tú los creativos (`253`), usar el producto como muestra y usar plantillas de página. Con
eso el costo esperado por test en México baja a **USD 85** (esquema escalonado de arriba), que es
lo que deja **~5 tests** con USD 500 menos USD 50 de reserva.

## La tasa de acierto

**1 de cada 10.** No es pesimismo, es la base de la planeación.

```
probabilidad acumulada de hallar al menos un ganador = 1 − (0,9)^n
```

| Tests (n) | Probabilidad |
|---|---|
| 1 | 10% |
| 3 | 27% |
| 5 | 41% |
| 10 | 65% |
| **15** | **79%** |
| 20 | 88% |
| 30 | 96% |

Con menos de USD 500 en México, el esquema escalonado da **~5 tests** y por tanto **41%** de
probabilidad de encontrar un ganador.

**Léelo bien: lo más probable es que ninguno de los cinco funcione.** Eso no es motivo para no
empezar; es motivo para que la selección de candidatos sea rigurosa (`76`) en vez de improvisada,
porque con cinco intentos la calidad de la lista pesa más que cualquier optimización de campaña
posterior. Y es motivo para presupuestar la segunda ronda desde ahora.

⚠️ No uses el atajo de calcular el costo del test como "3 ventas × CAC" (≈ USD 32). Ese número
supone que el producto **ya funciona**, y por definición no sirve para **matar** al que no funciona
— que es el 90% de los casos.

## Separa las dos cuentas

| Cuenta | Qué entra | Cómo se juzga |
|---|---|---|
| **Test / I+D** | pauta de validación, muestras, creativos | por tasa de acierto, no por ROAS |
| **Escala** | pauta de productos validados | por holgura |

Mezclarlas hace que tu ganador se vea peor de lo que es y que nunca sepas cuánto te cuesta
realmente encontrar uno. Ver `224`.

## Errores de test

| Error | Consecuencia |
|---|---|
| Probar 1 producto con USD 300 | una sola bala, 10% de probabilidad |
| Probar 10 productos con USD 30 cada uno sin señal clara | ninguna señal legible |
| Cambiar la campaña a las 6 horas | reinicias el aprendizaje |
| Declarar ganador con 1 venta | ruido |
| Probar sin haber calculado el techo de CAC antes | no sabes qué estás mirando |
| Probar productos que `41` ya descartó | tirar dinero |

## Relacionados
`41` · `210` · `213` · `216` · `218` · `224` · `228` · `231` · `233` · `234` · `235`
