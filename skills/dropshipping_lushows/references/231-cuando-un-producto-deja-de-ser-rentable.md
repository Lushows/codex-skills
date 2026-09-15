# Cuándo un producto deja de ser rentable

## La pregunta correcta

No es "¿está vendiendo?". Es **"¿la holgura sigue por encima del umbral?"**. Un producto puede
vender más que nunca y estar perdiendo dinero en cada pedido.

```
HOLGURA = TECHO DE CAC ÷ CAC REAL
```

| Holgura | Estado | Acción |
|---|---|---|
| < 1,0 | pierdes en cada venta | **apagar hoy** |
| 1,0 - 1,3 | trabajas gratis | 72 horas para arreglarlo o apagar |
| 1,3 - 2,0 | frágil | no escalar, arreglar |
| 2,0 - 3,0 | sano | operar |
| > 3,0 | subinvirtiendo | subir presupuesto |

## Las 6 causas de muerte, en orden de frecuencia

| # | Causa | Cómo se ve | Módulo |
|---|---|---|---|
| 1 | Saturación: entraron competidores al mismo ángulo | CTR cae, CPM sube, CVR cae | `61` |
| 2 | Fatiga del creativo | CTR cae, frecuencia sube, CPM estable | `62` |
| 3 | Sube el costo puesto en bodega | tipo de cambio, flete, arancel | `28`, `13` |
| 4 | Sube el CPM por temporada | todo sube a la vez, en fecha | `238` |
| 5 | Cae la tasa de cobro | más devoluciones, peor operador | `229` |
| 6 | El producto dejó de resolver (novedad agotada) | CVR cae sin que suba el CPM | `62` |

**Diagnóstico rápido:** si cae el CTR pero la CVR aguanta → creativo (2). Si cae la CVR pero el CTR
aguanta → oferta o competencia de precio (1). Si sube el CPM y todo lo demás está igual → temporada
o subasta (4). Si sube el costo y nada más cambió → sourcing (3).

## Las señales, con umbrales

| Señal | Umbral de alarma | Confirmación |
|---|---|---|
| Holgura | < 1,3x tres días seguidos | recalcular con `228` |
| ROAS real vs de equilibrio | ROAS real < equilibrio × 1,3 | `226` |
| CTR | cae > 30% vs su mejor semana | `61` |
| Frecuencia del anuncio | > 2,5-3,0 en 7 días | fatiga |
| CPM | sube > 40% sin temporada | competencia entrando |
| CVR de la página | cae > 25% | oferta o precio de competencia |
| Tasa de cobro | cae > 10 puntos | operador o zonas |
| Tasa de reembolso | > 5% | calidad o promesa inflada |
| Costo puesto en bodega | sube > 15% | recalcular precio (`216`) |

## El protocolo de 72 horas

Cuando la holgura cae bajo 1,3x, tienes tres días. Uno por hipótesis.

```
Día 1 — CREATIVO
  Lanza 2-3 creativos nuevos con ángulo distinto (213).
  Si el CTR se recupera, era fatiga. Sigue.

Día 2 — OFERTA
  Sube el ticket (bundle, bump) o cambia la promesa (215, 218, 219).
  Si la CVR o el ticket se recuperan, era la oferta. Sigue.

Día 3 — COSTOS
  Renegocia flete o producto, revisa fallidos (229).
  Si el techo de CAC sube, era la estructura. Sigue.

Si al final del día 3 la holgura sigue bajo 1,3x → APAGAR.
```

Lo que **no** se hace en esos tres días: bajar el precio. Baja el techo y acelera la muerte (`221`).

## Cómo apagar bien

| Paso | Qué hacer |
|---|---|
| 1 | Pausar campañas, no borrarlas (guardan aprendizaje y datos) |
| 2 | Calcular cuánto inventario queda y su costo hundido |
| 3 | Liquidar el stock: descuento profundo, bundle con el siguiente producto, marketplace |
| 4 | Guardar los creativos, ángulos y públicos que sí funcionaron |
| 5 | Registrar la lección en una línea: qué lo mató y con qué señal se vio primero |
| 6 | Pasar el capital liberado al siguiente test (`232`) |

**El inventario es costo hundido.** No sigas pautando un producto que pierde para "recuperar el
stock": eso convierte una pérdida contenida en una pérdida abierta. Liquida el stock por otro canal
y saca la pauta del producto muerto.

## El error de aguantar

| Racionalización | Realidad |
|---|---|
| "Ya invertí mucho, no puedo parar" | costo hundido; lo invertido no vuelve por insistir |
| "En diciembre se recupera" | si no aguanta CPM base, menos aguanta CPM +50% |
| "Bajo el precio y sale" | baja el techo, empeora la holgura (`221`) |
| "Meta dice ROAS 3" | el panel no es el banco (`226`) |
| "Vendí 40 unidades ayer" | volumen sin margen es una máquina de perder rápido |

## Cuándo NO es muerte

| Situación | Lectura |
|---|---|
| Caída de 2-3 días en fin de mes | estacionalidad de quincena, espera |
| Caída el día que cambiaste la página | revierte el cambio primero |
| CPM alto en Buen Fin con holgura 1,8x | sigues ganando; es temporada (`238`) |
| Una campaña mala entre cinco buenas | apaga la campaña, no el producto |

Antes de declarar muerto un producto, verifica que no cambiaste algo tú mismo en las últimas 48
horas. La mitad de las "muertes súbitas" son un pixel roto, un método de pago caído o un cambio de
precio que no querías.

## El caso especial de la temporada

Un producto de regalo de diciembre no "deja de ser rentable": **se le acaba la ventana**. Eso se
planea, no se diagnostica. Fecha de corte de compra, fecha de corte de pauta, plan de liquidación
del remanente. Ver `238`.

## Relacionados
`13` · `28` · `61` · `62` · `213` · `215` · `216` · `218` · `219` · `221` · `226` · `228` · `229` · `232` · `238` · `239`
