# 284 · Una sola pasada

**Qué resuelve:** la regla de orden más incumplida del canal, que en realidad son dos
reglas con la misma raíz:

1. **La locución se genera de una sola vez.** Nunca frase por frase.
2. **La voz se aprueba antes de tocar la imagen.** Fase 3 cerrada antes de la fase 4.

La raíz común: **todo el montaje cuelga de los tiempos de la voz**. Si la voz cambia,
cambia el suelo sobre el que está construido el resto del episodio.

---

## Regla 1 · El audio se genera entero

Medido sobre el minuto de `ep01-lustig`, 155 palabras, `-6%`:

| Método | Duración |
|---|---|
| **Una sola pasada** | **63,43 s** |
| Troceado en sus 14 frases y pegado | 65,71 s (**+3,6%**) |

Los 2,28 s de diferencia no son prosodia: son **0,175 s de relleno por costura**, el
silencio de cabeza y cola que el motor pone en cada trozo. Pero el problema gordo no es
la duración, son otras tres cosas:

- **La entonación se reinicia en cada trozo.** El modelo construye la curva de
  entonación sobre el texto completo; al partirlo, cada fragmento vuelve a empezar en el
  tono de arranque y la cifra final suena despegada de la frase que la trae.
- **Las costuras no coinciden con las pausas reales.** `tiempos.py` empareja grupos de
  texto con los silencios medidos (§ `282`); un silencio artificial en mitad del sitio
  equivocado le corre el emparejamiento.
- **La pausa que compras troceando ya la compra un punto** — 1,06 s, gratis y con la
  entonación intacta.

Si hay que trocear por razones de producción (idiomas, bloques muy largos), se trocea por
**párrafo completo**, nunca por frase, y jamás dentro de una oración.

## Regla 2 · La voz se aprueba antes del visual

```
3. VOZ          → locución completa en UNA pasada. Se aprueba ANTES de tocar imagen.
4. TIEMPOS      → alineación palabra por palabra sobre el audio ya aprobado.
5. MATERIAL     → archivo y recortes que el guion visual va a necesitar.
6. GUION VISUAL → la tabla de eventos, escrita entera antes de renderizar.
7. RENDER       → motor.py + acabar.py.
```

Quién depende de `tiempos.json`, contado en el piloto:

| Fichero | Qué saca de ahí |
|---|---|
| `guion_visual.py` | Carga `tiempos.json` al arrancar: **24** entradas `"ancla"` (5 destellos + 19 elementos) y los **5** límites de bloque, sacados de los silencios medidos |
| `acabar.py` | **12** llamadas a `cuando()`: picos dramáticos, objetos, destellos |
| `motor.py` | `render_escena(esc, i, tiempos["palabras"])`: la colocación de cada elemento |

Son **36 anclas explícitas** —24 + 12— más los 5 límites de bloque, en un solo minuto. En
un episodio de diez, del orden de 350.

## Lo que cuesta romperla, medido

Se quitó **una palabra** del guion —«directamente», cinco sílabas— y se regeneró:

| Palabra | Antes | Después | Desplazamiento |
|---|---|---|---|
| `broma.` (en el mismo grupo fónico) | 33,06 s | 30,30 s | **−2,76 s** |
| `Porque` | 34,41 s | 31,81 s | −2,60 s |
| `Eiffel....` | 41,90 s | 40,91 s | −0,99 s |
| `separar` | 60,38 s | 59,58 s | −0,80 s |
| `consta.` | 62,98 s | 62,17 s | −0,81 s |

Dos lecturas:

- **Todo lo posterior se corre 0,80 s**, que es lo que duraba la palabra. Previsible.
- **Dentro de su propio grupo fónico el desplazamiento es de 2,76 s**, porque el reparto
  por sílabas redistribuye a todos los vecinos. Nada intuitivo, y suficiente para que un
  elemento entre encima de la frase anterior.

Una palabra. Y ninguna de las 36 anclas del minuto sigue en su sitio.

| Cambio en la voz | Qué hay que rehacer |
|---|---|
| Una palabra del guion | Fases 4, 6 y 7 del bloque entero, y revisar los bloques siguientes |
| El `rate` | **Todo**: los tiempos se multiplican por una constante (§ `281`) |
| Regenerar «igual» sin tocar nada | Nada: `edge-tts` es determinista. Misma entrada → misma duración (63,432 s en dos generaciones independientes) |
| Insertar un silencio en el audio | Todo lo posterior se corre exactamente esa cantidad (§ `288`) |

Rehacer 4-7 cuesta una hora. Aprobar la voz primero cuesta cinco minutos.

## Qué se aprueba exactamente en la fase 3

No es «me gusta cómo suena». Es una lista cerrada:

| Se comprueba | Cómo |
|---|---|
| El texto es el del `guion.md` aprobado | `voz.py` lo extrae; se lee el `guion.txt` generado |
| No queda ninguna cifra en dígitos | El detector de § `283` devuelve `[]` |
| Las ppm caen en 130-160 | El `print` final de `voz.py` |
| La duración cuadra con el hueco del bloque | Comparar con el objetivo del `guion.md` |
| Ningún nombre propio suena mal | **Escuchar.** Es la única parte que no se automatiza |
| Ninguna frase se atropella | Escuchar |
| El fichero no está vacío | El `raise` de `voz.py` (§ `289`) |

Y una condición de método: **se escucha entero, de una vez, sin mirar nada más**. La
locución es lo único del episodio que el espectador no puede saltarse.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Generar frase por frase | +3,6% de relleno, entonación reiniciada y el alineador descolocado |
| Pegar silencios entre trozos para «dar aire» | Empeora lo anterior; el punto ya compra 1,06 s |
| Empezar el guion visual con la voz «casi lista» | Las 36 anclas del minuto se caen con una palabra |
| Retocar una palabra «que no cambia nada» | Todo lo posterior se corre 0,80 s; sus vecinos, hasta 2,76 s |
| Cambiar el `rate` después de la fase 4 | Fases 4-7 completas a la basura |
| Aprobar la voz leyendo el texto en vez de escuchándola | Los nombres propios sólo se cazan oyéndolos |
| Guardar los tiempos de una versión y el audio de otra | Fallo silencioso: todo renderiza, todo cae mal |

## Relacionado

`281` ritmo en ppm · `282` la puntuación como partitura · `288` cuando la voz sobra ·
`289` errores de locución · `240` la tabla de eventos · `123` música anclada a palabra ·
`87` voz a fondo
