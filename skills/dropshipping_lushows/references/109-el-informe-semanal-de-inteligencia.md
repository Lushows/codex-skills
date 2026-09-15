# El informe semanal de inteligencia

> Vigencia: 14-sep-2026.

## Para qué existe

El radar (`107`) recoge datos. El informe los convierte en **decisiones**. Sin informe, la
investigación se queda en sensaciones ("creo que el mercado está más caro") y las sensaciones no se
pueden discutir ni revisar en el tiempo.

Regla dura: **el informe cabe en una página y termina en decisiones con responsable y fecha.** Si
ocupa cinco páginas, nadie lo lee, empezando por ti.

## La plantilla

```markdown
# Inteligencia competitiva — Semana NN (DD-mmm-2026)
Mercado: México · Nicho: ______ · Producto: ______

## 1. Números de la semana
| Métrica | Semana pasada | Esta semana | Δ |
|---|---|---|---|
| Anuncios activos competidor A | | | |
| Anuncios activos competidor B | | | |
| Anuncios activos competidor C | | | |
| Anuncios activos competidor D | | | |
| Anuncios activos competidor E | | | |
| Anunciantes totales del producto en MX | | | |
| Mediana de precio del nicho (MXN) | | | |
| Mi precio | | | |

## 2. Movimientos detectados
- (máximo 5 viñetas, cada una con fecha y fuente)

## 3. Productos nuevos en el radar
| Producto | Fuente | Fase (`100`) | Surtible antes de dic | Veredicto |
|---|---|---|---|---|

## 4. Ángulos nuevos vistos
| Ángulo (1 frase, `96`) | Quién lo usa | ¿Lo puedo girar? |
|---|---|---|

## 5. Grietas del competidor
- (entrega, garantía, atención, velocidad de la landing, MSI)

## 6. Riesgos
- (saturación, guerra de precio, proveedor, cuenta publicitaria)

## 7. Decisiones
| # | Decisión | Por qué (dato) | Cuándo |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |

## 8. Qué vigilo la semana entrante
- (máximo 3)
```

## Qué medir (y qué no)

| Medir | No medir |
|---|---|
| Nº de anuncios activos por competidor | "Gasto estimado" (no es observable, `84`) |
| Anunciantes totales del producto en el país | Facturación del competidor como si fuera dato |
| Antigüedad del anuncio más viejo | Impresiones inventadas |
| Mediana de precio y su tendencia | Sensaciones sin número |
| Nº de productos nuevos subidos por competidores | |
| Ángulos nuevos detectados | |

Toda cifra estimada va marcada como **estimada** y con su método. Ver `84` y `94`.

## Cómo se escribe una viñeta de movimiento

Mala:

> "El competidor A está creciendo mucho."

Buena:

> "Competidor A pasó de 19 a 41 anuncios activos en MX entre el 07 y el 14-sep. El 78% de los nuevos
> corresponden al producto X (bundle 2x a 1.249 MXN). Su anuncio más antiguo de X inició el
> 02-jul-2026 (74 días). **Lectura: encontró un ganador y está escalando.**"

Tiene: sujeto, número, fecha, fuente implícita y lectura. Se puede discutir. Se puede revisar dentro
de un mes.

## Cómo se decide con el informe

Cada decisión debe poder rastrearse a un dato del propio informe. Ejemplos de la cadena completa:

| Dato | Lectura | Decisión |
|---|---|---|
| Anunciantes del producto pasan de 6 a 17 en tres semanas | Fase 3 → 4 (`100`) | Diferenciar oferta con bundle propio antes del 1-nov, o descartar |
| Mediana de precio baja 2 semanas seguidas | Guerra de precio | No igualar; añadir garantía de entrega y sostener 1.099 |
| Comentarios del líder llenos de "no me llegó" | Grieta de entrega | Hook de "sale de México, llega en 48 h" en el creativo C |
| Competidor B cae de 28 a 9 anuncios | Perdió el ganador o la cuenta | Revisar si su producto sigue vivo con otros; posible hueco |
| Ningún competidor MX ofrece MSI | Hueco de Buen Fin | Activar MSI 13-17 nov si la pasarela lo permite |

## Ritmo y formato

| Cuándo | Qué |
|---|---|
| **Semanal (5 min de escritura)** | La plantilla completa, después del radar de `107` |
| **Mensual (20 min)** | Resumen de las 4 semanas: qué cambió de verdad, qué decisiones se ejecutaron y qué pasó |
| **Antes y después del Buen Fin** | Informe especial: qué hizo cada competidor del 13 al 17 de nov y qué sostuvo después |
| **Cierre de temporada (fin de dic)** | Informe de aprendizajes para el ciclo siguiente |

Guarda todos en la misma carpeta, numerados por semana. Doce informes seguidos son el mapa real de
tu nicho en México, y nadie más lo tiene.

## Auditoría de decisiones (lo que casi nadie hace)

En el informe mensual, revisa las decisiones de las semanas anteriores:

| Decisión | ¿Se ejecutó? | Resultado | Aprendizaje |
|---|---|---|---|

Si más del 30% de tus decisiones no se ejecutaron, el problema no es la investigación: es que estás
decidiendo cosas que no caben en tu capacidad. Decide menos y hazlas.

## Errores del informe

| Error | Corrección |
|---|---|
| Informe de 6 páginas | Una página. Lo demás va al swipe file (`99`) |
| Adjetivos sin números | Cada afirmación con un dato |
| Cifras estimadas presentadas como hechos | Marca "estimado" y di el método |
| Sin decisiones | Entonces era un boletín, no un informe |
| Sin fecha | Inútil en dos semanas |
| No revisar decisiones pasadas | Repites errores con datos nuevos |

## Frontera

Si el informe deriva en decisiones de precio, margen o punto de equilibrio, invoca
`economist_lushows` y ejecuta los números con `Matematicas_lushows`. Si deriva en cambios de
campaña, invoca `facebook_ads_lushows` o `tiktok_ads_lushows`.

## Relacionados
`107` radar semanal · `99` swipe file · `100` detección temprana · `103` precios · `104` ofertas · `84` estimar inversión
