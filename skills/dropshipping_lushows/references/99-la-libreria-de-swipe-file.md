# La librería de swipe file

> Vigencia: 14-sep-2026.

## Qué es y para qué sirve de verdad

Un **swipe file** es tu archivo personal de referencias: anuncios, landings, ofertas y hooks que
guardaste con su análisis. No es una carpeta de videos bonitos. Es una base de decisión.

Dos razones por las que importa:

1. **Los anuncios desaparecen.** El que hoy lleva 90 días activos, en tres semanas puede estar
   apagado y fuera de la biblioteca. Si no lo capturaste, lo perdiste.
2. **El valor está en la comparación en el tiempo.** Saber que el competidor X tenía 12 anuncios en
   agosto y 41 en septiembre vale más que cualquier foto suelta. Eso solo lo sabes si registras.

## Qué guardar de cada anuncio (y qué no)

| Guardar | No guardar |
|---|---|
| **Captura de pantalla** de la tarjeta de la biblioteca (con fecha de inicio visible) | El archivo de video del competidor para reusarlo |
| **ID de la biblioteca** del anuncio | Sus fotos para tu tienda |
| **Transcripción** del audio y el texto en pantalla | Su copy para pegarlo |
| Enlace al anuncio y a la landing (con UTMs) | |
| Tu **ficha de deconstrucción** (`97`) | |
| Tu formulación del **ángulo** (`96`) | |
| Tu conteo de comentarios (`95`) | |
| Fecha en que lo capturaste | |

La grabación del video ajeno **para estudio privado** es una zona gris que en la práctica nadie
persigue; usarlo o republicarlo es infracción clara. La regla segura: guarda la **transcripción y el
análisis**, no el archivo. Si guardas el archivo, que sea temporal y nunca salga de tu disco. Ver
`105`, `106`.

## Estructura de carpetas

```
swipe/
  _INDICE.csv                  <- la tabla maestra, ver abajo
  nicho-organizacion-hogar/
    2026-09-14_competidorA_anuncio-3f2a/
      captura-biblioteca.png
      captura-landing-movil.png
      transcripcion.md
      deconstruccion.md        <- plantilla de `97`
      comentarios.csv          <- conteo de `95`
      ficha-tienda.md          <- plantilla de `92`
  nicho-cocina/
  _hooks/
    hooks-dolor.md
    hooks-resultado.md
    hooks-precio.md
  _ofertas/
    bundles-mx.md
    garantias.md
```

Nombre de carpeta: **fecha + competidor + id del anuncio**. La fecha primero para que ordene solo.

## El índice maestro (una sola hoja)

Sin esta hoja, el swipe file es un basurero. Columnas exactas:

| id | fecha_captura | pais | nicho | anunciante | producto | fecha_inicio_anuncio | dias_activo | variantes | formato | tipo_hook | angulo_1_frase | precio | bundle | msi | garantia | envio | url_landing | carpeta | veredicto |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

`veredicto` solo admite: **REFERENCIA** (lo estudio), **COMPETIDOR** (lo vigilo semanal), **DESCARTE**
(no volver).

## Regla de captura

Captura **en el momento**, no "luego". Procedimiento de 90 segundos por anuncio:

1. Captura de pantalla de la tarjeta completa (que se vea "Se empezó a publicar el…").
2. Copia el ID de la biblioteca.
3. Abre la landing, captura en vista móvil.
4. Pega todo en una carpeta nueva con el nombre correcto.
5. Añade la fila al índice.
6. **La deconstrucción completa se hace después**, solo para los que marques REFERENCIA.

## Las tres colecciones transversales

Además del archivo por competidor, mantén tres colecciones que atraviesan nichos:

| Colección | Qué entra | Cómo la usas |
|---|---|---|
| **_hooks** | Toda apertura de 0-3 s que te frenó a ti, clasificada por tipo (`88`) | Cuando escribas un guion, lees los 20 hooks del tipo que necesitas |
| **_ofertas** | Bundles, garantías, envíos, MSI, upsells | Cuando diseñes tu oferta (`104`) |
| **_landings** | Estructuras de página que convierten | Cuando construyas la tuya (`102`) |

Los hooks se guardan **parafraseados por ti**, no literales. Doble beneficio: evitas el problema
legal y te obligas a entender el mecanismo.

## Higiene: qué pasa con lo viejo

| Antigüedad del registro | Acción |
|---|---|
| < 30 días | Vigente |
| 30-90 días | Revisar: ¿el anuncio sigue activo? Actualiza `dias_activo` |
| > 90 días | Marca como histórico. Sirve de patrón, no de dato de mercado |
| > 180 días | Archiva. El precio y la saturación ya cambiaron |

Un swipe file sin limpieza se convierte en una mentira ordenada.

## El error más común

Guardar y no volver. Tres anclas para que el archivo se use:

1. En el radar semanal (`107`), el paso 1 es **abrir el índice** y actualizar los COMPETIDOR.
2. Antes de escribir cualquier guion, lees `_hooks`.
3. Antes de fijar cualquier precio, lees `_ofertas`.

Si en un mes no abriste el archivo, no tienes swipe file: tienes acumulación.

## Aplicación México diciembre 2026

Antes del 1 de noviembre debes tener en el archivo:

- [ ] 10 competidores mexicanos fichados con fecha
- [ ] 20 hooks parafraseados y clasificados
- [ ] 8 estructuras de oferta MX con precio, MSI y garantía
- [ ] 5 landings mexicanas capturadas en móvil
- [ ] Arqueología del Buen Fin 2025 (biblioteca con filtro de fecha nov-2025, ver `82`)

Ese último punto se hace **ahora, en septiembre**, no en noviembre.

## Relacionados
`92` espiar tiendas · `95` comentarios · `96` ángulo · `97` deconstruir · `102` landings · `105` qué copiar · `107` radar semanal
