# 30 — Anatomía del anuncio de búsqueda

Lee este módulo cuando estés escribiendo tu primer anuncio de Search, no entiendas qué partes ve el usuario, o quieras saber por qué tu anuncio se ve más chico o más grande que el del competidor que está justo arriba.

En Google, el usuario YA tiene la intención: escribió algo porque quiere resolver algo. Tu anuncio no genera el deseo (eso es trabajo de Meta → `facebook_ads_lushows`, o de TikTok → `tiktok_ads_lushows`), lo CAPTURA. Por eso aquí no vendes con imágenes bonitas ni con storytelling largo: vendes con palabras que confirman que tú eres la respuesta exacta a lo que escribió. Cada milímetro del anuncio existe para responder "¿esto es lo que busco?" en menos de un segundo. Esa es la diferencia mental que separa Search de toda red social: en Meta interrumpes a alguien que veía videos; en Google atiendes a alguien que levantó la mano (ver 03 intención vs interrupción).

## Las partes que ve el usuario

El anuncio de Search se arma con bloques. Google los combina solo (formato RSA, ver 31), pero tú controlas qué materia prima le das.

| Parte | Qué es | Límite | Quién lo arma |
|---|---|---|---|
| Etiqueta "Patrocinado" | Marca legal de que es pauta | fijo | Google |
| Título (headline) | Lo azul, grande, clickeable | hasta 30 caracteres c/u, hasta 15 títulos | tú escribes, Google combina hasta 3 |
| URL visible (display) | El dominio + 2 "paths" decorativos | dominio real + 15+15 car. | tú el path |
| Descripción | El texto gris debajo | hasta 90 caracteres c/u, hasta 4 | tú escribes, Google combina hasta 2 |
| Assets | Sitelinks, llamada, ubicación, precio, imagen, etc. (ver 32) | varios | tú los cargas |

Lo que el usuario realmente lee primero es: **título 1 + título 2** (en azul) y luego baja a la descripción solo si el título lo enganchó. La descripción casi nunca se lee completa. Por eso el peso de la venta está en los títulos, no en las descripciones. En móvil — donde busca el 75-80% de los colombianos en 2026 — caben menos caracteres visibles y los assets se apilan distinto, así que un título que en escritorio se ve completo puede cortarse en celular. Escribe pensando en pantalla de 6 pulgadas, no en tu monitor.

### Ejemplo de anuncio bien armado (calculadora gastronómica)

```
Patrocinado · gastrolatam.co/calculadora
Calculadora de Costos Gastro | Pago Único $10.000 COP
Sabe Cuánto Ganas por Plato. Sin Mensualidad, Tuya para Siempre.
Funciona en Excel · Sin instalar nada · +2.000 negocios la usan.
  Ver precio   Cómo funciona   Para quién es   Descargar ya
```

Léelo como lo lee el cerebro del usuario en 1 segundo: reconoce su búsqueda ("calculadora de costos"), ve el diferenciador ("pago único $10.000", no suscripción), y ve la confianza ("+2.000 negocios"). Tres gatillos en una mirada.

## Por qué clickea (el match psicológico)

El usuario no compara anuncios uno por uno; escanea el SERP (la página de resultados) en segundos buscando la palabra que escribió. Si buscó "calculadora de costos para restaurante" y tu título dice exactamente "Calculadora de Costos para Restaurante", su cerebro la marca como relevante antes de leer nada más. A esto se le llama **message match**: el anuncio refleja la búsqueda (ver 37).

Los tres gatillos que disparan el clic, en orden:

1. **Reconocimiento**: la keyword que escribió aparece en el título. Es el filtro #1. Sin esto, el ojo ni se detiene.
2. **Diferenciador**: algo que lo separa del de arriba — precio, "envío gratis", "pago único $10.000", garantía, "hoy mismo" (ver 38). Es lo que gana el clic, no solo entrar a la conversación.
3. **Confianza**: señales de que no es estafa — reseñas, años, "+2.000 restaurantes", marca conocida. En Colombia el miedo a la estafa online es altísimo; esta señal pesa más que en otros mercados.

Un anuncio sin reconocimiento no se lee. Uno con reconocimiento pero sin diferenciador empata con todos y compite solo por puja (caro). El ganador tiene los tres. Para construir el diferenciador a partir de las objeciones reales del cliente, no de tu imaginación, apóyate en `ventas_lushows` (manejo de objeciones) y valida el precio con `economist_lushows`.

## La jerarquía del SERP (dónde caes y por qué importa)

No todos los anuncios se ven igual. Tu posición la decide el **Ad Rank** = tu puja × tu Quality Score (1-10, ver 36) + el impacto esperado de tus assets. Traducción: no gana el que más paga, gana el que paga bien Y es relevante. Un anuncio con buen Quality Score puede estar arriba pagando MENOS por clic que un competidor con anuncio malo. Esto no es teoría: es la mecánica exacta de la subasta (ver 01).

| Zona del SERP | Qué es | Realidad comercial |
|---|---|---|
| Top (arriba de orgánicos) | 1-4 anuncios | se lleva la mayoría de los clics comerciales |
| Bottom | 1-3 anuncios | clics más baratos, menos volumen |
| AI Overview | resumen IA arriba de todo | roba clics en búsquedas informativas (ver 92) |
| Shopping (si aplica) | fichas con foto y precio | otro formato, otro feed (ver 34) |

Para búsquedas comerciales ("comprar X", "X precio", "X para mi negocio") los anuncios de texto siguen dominando en 2026. Para búsquedas informativas ("cómo calcular food cost") el **AI Overview** (el resumen generado por IA que Google pone arriba de todo) se come parte del clic — la gente lee el resumen y no baja. Por eso en Search te conviene pujar por intención comercial, no por curiosidad (ver 92): el que busca "cómo calcular costos" lee y se va; el que busca "calculadora de costos precio" compra.

Más assets activos = tu anuncio ocupa más alto del SERP, empuja al competidor hacia abajo y sube tu CTR sin pagar más. Es la mejora más barata que existe (ver 32). Cuando el clic llega, todo depende de la landing: si la página no refleja el anuncio, pagaste un clic para nada (ver 33, construcción → `desingweb-lushows`).

### Tabla de referencia: orden de prioridad al escribir

| Prioridad | Dónde | Por qué |
|---|---|---|
| 1 | Título 1 (keyword exacta) | da el reconocimiento, sin esto no hay clic |
| 2 | Título 2-3 (diferenciador + confianza) | ganan el clic frente al competidor |
| 3 | Assets (sitelinks, callouts) | suben CTR gratis, ocupan más SERP (ver 32) |
| 4 | Descripción | refuerzo, casi nadie la lee completa |
| 5 | Paths de la URL | mini-señal de relevancia ("/calculadora") |

Trabaja de arriba hacia abajo. La mayoría de la gente hace lo contrario: pule la descripción durante horas y deja los assets vacíos. Es regalar la subasta.

## Errores comunes — blacklist

- **Escribir el anuncio antes de leer la keyword**: si el título no contiene lo que el usuario escribió, no hay reconocimiento y no hay clic. La búsqueda manda, no tu creatividad.
- **Gastar la creatividad en la descripción**: casi nadie la lee completa. El 80% del trabajo va en los títulos.
- **Escribir para tu monitor y no para el celular**: el título que se ve completo en escritorio se corta en móvil, donde busca el 75-80% en Colombia; prueba en pantalla chica.
- **Dejar assets vacíos**: sin sitelinks, callouts y demás, tu anuncio se ve chiquito y pierdes CTR gratis frente a un competidor más completo (ver 32).
- **Creer que la posición #1 se compra con plata**: el Ad Rank mezcla puja Y Quality Score; un anuncio relevante gana posición pagando menos (ver 36).
- **Mandar todos los clics a la home**: si la landing no refleja el anuncio, el match se rompe en el último metro y la conversión se cae (ver 33).
- **Copiar el anuncio del competidor tal cual**: terminas igual a él, sin diferenciador, compitiendo solo por puja (caro). Encuentra tu ángulo (ver 38).
- **Ignorar que es búsqueda comercial vs informativa**: pujar por "qué es food cost" trae curiosos que no compran; puja por "comprar/precio/para restaurante" (ver 92).
- **Sacar el diferenciador de tu cabeza y no de las objeciones del cliente**: el mejor diferenciador neutraliza un miedo real de compra; sácalo de `ventas_lushows`.
