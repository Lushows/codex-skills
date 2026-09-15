# Velocidad de carga y móvil

> Vigencia: 14-sep-2026. Implementación técnica fina y CSS: invoca `desingweb-lushows`.

Tu tienda se ve en un celular, con datos móviles, en la calle, con una mano. Todo lo demás es teoría.
Si la página tarda, el visitante que ya pagaste se va antes de ver la promesa: pierdes el dinero del
clic sin siquiera haber tenido la oportunidad de vender.

## Los tres números que importan

| Métrica | Qué mide | Objetivo |
|---|---|---|
| **LCP** (Largest Contentful Paint) | Cuándo aparece el elemento principal, casi siempre tu primera imagen | Bajo 2,5 s |
| **INP** (Interaction to Next Paint) | Qué tan rápido responde al tocar | Bajo 200 ms |
| **CLS** (Cumulative Layout Shift) | Cuánto salta el contenido al cargar | Bajo 0,1 |

El CLS es el asesino silencioso: si el botón salta justo cuando el dedo va bajando, el cliente toca
otra cosa, se frustra y se va.

## Cómo medir de verdad

| Herramienta | Para qué |
|---|---|
| PageSpeed Insights (datos de campo) | La verdad: usuarios reales, no laboratorio |
| Lighthouse en Chrome DevTools | Diagnóstico y lista de culpables |
| **Tu propio celular con datos móviles, sin wifi** | La prueba que nadie hace y la única que convence |
| Informe de velocidad de tu plataforma | Tendencia en el tiempo |

Mide **tu página de producto**, no la de inicio. Es donde aterriza la pauta.

## Los seis culpables, en orden

| # | Culpable | Solución |
|---|---|---|
| 1 | **Imágenes pesadas** | WebP/AVIF, menos de 200 KB, tamaño servido = tamaño mostrado. `182` |
| 2 | **Apps instaladas** | Cada app mete scripts. Desinstala lo que no genera ventas |
| 3 | **Video mal montado** | Diferido, comprimido, sin autoplay con sonido. `186` |
| 4 | **Fuentes** | Máximo 2 familias, 2-3 pesos, precargadas, con `font-display: swap` |
| 5 | **Scripts de terceros** | Píxeles, chats, reseñas, pop-ups. Auditar uno por uno |
| 6 | **Tema recargado** | Los temas con animaciones y carruseles pesan |

## La auditoría de apps

Escribe la lista de apps instaladas y frente a cada una: **qué venta genera**. Las que no tienen
respuesta, se van.

| App | ¿Genera venta? | Veredicto |
|---|---|---|
| Reseñas | Sí, directa. `185` | Se queda, versión ligera |
| Carrito abandonado | Sí, medible. `198` | Se queda |
| Upsell post-compra | Sí | Se queda |
| Contador regresivo | No, y además suele ser falso. `189` | **Fuera** |
| "X personas viendo" | No | **Fuera** |
| Rueda de descuentos | Rara vez | **Fuera** |
| Chat en vivo sin nadie atendiendo | No | **Fuera** |
| Traductor de moneda automático | No en un solo país | **Fuera** |
| Galería de Instagram | No | **Fuera** |

Una tienda de un producto necesita 3-5 apps. Si tienes 14, ahí está tu problema de velocidad.

## La regla de las imágenes

| Regla | Detalle |
|---|---|
| Formato | WebP (AVIF si tu plataforma lo sirve bien) |
| Peso | Menos de 200 KB por imagen de galería |
| Dimensiones | No subas 4.000 px para mostrar 600 |
| La primera imagen | **Sin carga diferida y con prioridad alta**: es tu LCP |
| Las demás | Carga diferida siempre |
| Dimensiones declaradas | `width` y `height` en el HTML, o tendrás CLS |

## Móvil: la lista de verificación física

Toma tu celular, apaga el wifi, y recorre la página completa:

1. ¿El botón de compra se ve **sin bajar**? `181`.
2. ¿Puedes tocar todos los botones con el pulgar, sin acercar?
3. ¿Los campos del formulario abren el teclado correcto (numérico para teléfono y CP)?
4. ¿Algo salta mientras carga?
5. ¿El chat o el pop-up tapan el botón?
6. ¿La tabla comparativa se sale de la pantalla?
7. ¿El texto se lee sin hacer zoom? (mínimo 16 px)
8. ¿El video se ve sin ocupar la pantalla completa a la fuerza?
9. ¿Cuánto tarda desde que tocas el enlace hasta que ves la promesa? **Cronométralo.**
10. ¿Pudiste comprar de principio a fin en menos de 90 segundos? `190`.

Si fallas cualquiera de las diez, tienes trabajo antes de encender pauta.

## Cuánto cuesta la lentitud

No hay una cifra universal confiable; lo que sí es estable en cualquier medición es la dirección:
**cada segundo adicional de carga cuesta conversión, y el efecto es más fuerte en móvil y en redes
lentas.** Con el modelo del proyecto (utilidad USD 20,18 por venta), si arreglar la velocidad sube
la conversión de 2,6% a 3,0% sobre 10.000 sesiones, son 40 ventas más: **USD ~807**. Ese es el
orden de magnitud de una tarde de trabajo borrando apps y comprimiendo imágenes.

Mide tu propio antes y después. `202`.

## Lo que NO vale la pena perseguir

| Obsesión | Por qué no |
|---|---|
| Sacar 100/100 en Lighthouse | Los últimos puntos cuestan días y no mueven ventas |
| Cambiar de plataforma por velocidad | El problema casi siempre son tus apps e imágenes, no la plataforma |
| Optimizar la página de inicio | La pauta no aterriza ahí. `175` |
| Minificar CSS a mano | Ganancia marginal |

Concéntrate en: imágenes, apps, video y fuentes. Eso es el 90% del problema.

## Relacionados
`182` galería · `186` video · `190` checkout · `199` analítica · `204` diagnóstico
