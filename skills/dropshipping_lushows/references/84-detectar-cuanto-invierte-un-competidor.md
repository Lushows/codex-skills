# Detectar cuánto invierte un competidor

> Vigencia: 14-sep-2026. Todos los números de CPM son base USD y se mueven; verificar en tu cuenta.

## Lo primero: lo que NO se puede saber

| Pregunta | ¿Se puede? |
|---|---|
| ¿Cuánto gasta al día? | **No.** Meta solo publica rangos de gasto en anuncios de temas sociales, elecciones o política |
| ¿Cuál es su ROAS? | No |
| ¿Cuántas ventas hace? | No desde la biblioteca. Se estima por otra vía, ver `94` |
| ¿Qué público segmenta? | No |
| ¿Cuánto lleva gastado en total? | No |

Cualquier herramienta o "gurú" que te dé una cifra exacta de gasto de un anunciante comercial está
**estimando con un modelo propio**, y ese modelo puede errar por múltiplos. Trátalo como orden de
magnitud, jamás como dato.

## Los cuatro métodos de estimación indirecta

### Método 1 — Conteo de anuncios activos (el más usado)

Premisa: un anunciante que corre 40 anuncios activos está poniendo más plata que uno que corre 3.
No es lineal (CBO reparte desigual, muchos anuncios reciben céntimos), pero como señal de **escala
relativa** funciona.

| Anuncios activos | Escala probable |
|---|---|
| 1-5 | Prueba o operación mínima |
| 6-20 | Operación en funcionamiento |
| 21-60 | Escalando en serio |
| 60+ | Estructura grande, probablemente agencia o equipo |

Uso correcto: comparar competidores ENTRE SÍ dentro del mismo nicho y país. Uso incorrecto:
convertirlo a pesos.

### Método 2 — Cota inferior por CPM (banda, no número)

Si un anuncio lleva N días activo, tuvo que entregar impresiones. Puedes calcular cuánto costaría
entregar X impresiones al CPM del país. Esto te da una **cota inferior plausible**, no un gasto.

Con CPM base USD por país (verificar, se mueve):

| País | CPM base USD | Q4 (+20-50%) | Black Friday (+50-80%) |
|---|---|---|---|
| EE.UU. | 23,00 | 27,60 - 34,50 | 34,50 - 41,40 |
| España | 5,80 | 6,96 - 8,70 | 8,70 - 10,44 |
| Chile | 5,20 | 6,24 - 7,80 | 7,80 - 9,36 |
| **México** | **4,50** | **5,40 - 6,75** | **6,75 - 8,10** |
| Colombia | 4,00 | 4,80 - 6,00 | 6,00 - 7,20 |
| Perú | 3,70 | 4,44 - 5,55 | 5,55 - 6,66 |

Ejemplo honesto: si asumes que un anuncio necesita al menos ~50.000 impresiones para sostenerse un
mes en México, a CPM 4,50 eso son **USD 225** mínimos. Es un piso de conversación, no un dato. El
supuesto de impresiones lo pones tú y es el eslabón débil.

### Método 3 — Volumen de comentarios como proxy de alcance

Los comentarios visibles en el post del anuncio (cuando es un post público) crecen con el alcance.
Regla de campo, no ley: el ratio comentarios/impresiones en respuesta directa suele estar en el
orden de **0,05%-0,3%**. Es un rango tan amplio que solo sirve para comparar dos anuncios del MISMO
anunciante y nicho: el que tiene 10× comentarios probablemente tiene ~10× alcance.

| Comentarios acumulados | Alcance relativo |
|---|---|
| < 50 | Bajo o anuncio nuevo |
| 100-500 | Está corriendo de verdad |
| 1.000+ | Alcance masivo, lleva tiempo |

Cuidado: comentarios también crecen cuando el anuncio es polémico o el producto genera quejas. Ver
`95`.

### Método 4 — Cruce con señales de la tienda

Si el competidor tiene numeración de pedidos visible o reseñas con fecha, puedes estimar ventas y de
ahí inferir inversión asumiendo un ROAS típico de 1,8-2,5 en dropshipping con oferta simple. Todo el
procedimiento está en `94`. Es el método menos malo porque parte de un dato observable y no de un
supuesto de impresiones.

## Cómo reportarlo sin mentir

Prohibido escribir "gasta $3.000 al mes". Lo correcto:

> "Anunciante X: 34 anuncios activos, el más antiguo del 02-jul-2026 (74 días), 6 variantes del
> creativo principal, ~800 comentarios acumulados. **Escala estimada: media-alta dentro del nicho en
> México.** Gasto no observable; no estimado."

Esa frase se puede defender. "Gasta $3.000" no.

## Para qué te sirve realmente saber la escala

| Lo que aprendes | Decisión que cambia |
|---|---|
| Hay un anunciante enorme y 10 pequeños | El nicho aguanta varios jugadores. Puedes entrar |
| Hay un solo anunciante enorme y nadie más | O tiene el proveedor exclusivo o los demás se quemaron. Averigua por qué |
| Todos pequeños y recientes | Ola temprana. Buen momento, ver `100` |
| Todos enormes y antiguos | CPM alto, márgenes apretados. Con capital < USD 500 no entras |

Ese último caso es el relevante para el proyecto México: con capital bajo, **no compites contra el
que corre 60 anuncios**. Compites donde la escala del nicho es media y el ángulo aún no está gastado.
El techo de CAC manda, ver `11`.

## Relacionados
`81` biblioteca a fondo · `83` antigüedad · `94` estimar ventas · `95` comentarios · `11` techo de CAC · `89` herramientas pagas
