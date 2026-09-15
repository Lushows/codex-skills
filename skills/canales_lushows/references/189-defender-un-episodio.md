# 189 · Defender un episodio ante una reclamación

**Qué resuelve:** qué se hace la mañana en que llega un aviso sobre una imagen de un
episodio publicado. Dónde está la prueba, en qué orden se responde, y por qué un
registro completo convierte un susto en un trámite de veinte minutos.

> ⚠️ **Esto no es asesoría legal.** Es el procedimiento interno del canal. Cualquier
> paso con efectos legales —una impugnación formal, una respuesta a un requerimiento—
> se consulta con un abogado antes de enviarlo, no después.

---

## Lo primero: no es una sola cosa

Antes de responder nada hay que saber **qué ha llegado**, porque el procedimiento y las
consecuencias son distintos:

| Lo que llega | Riesgo típico |
|---|---|
| Coincidencia automática del sistema de identificación de la plataforma | Monetización desviada o bloqueo por países |
| Solicitud de retirada por derechos de autor | Retirada del vídeo y aviso en el canal |
| Correo directo del titular o su representante | Reclamación privada, a veces con petición económica |
| Aviso sobre una **marca**, no sobre copyright | Es otro derecho (§ 183): otro procedimiento |

🔴 **Pendiente de verificar en el momento:** el nombre exacto, los plazos y el
formulario de cada vía cambian con las políticas de la plataforma. Se comprueba en su
centro de ayuda **el día que llega el aviso**, no de memoria ni por lo que decía este
manual hace un año.

## Dónde está la prueba

Aquí es donde el trabajo de tres módulos anteriores se cobra. Todo lo que se necesita
para responder está guardado y no hay que buscar nada:

| Necesitas | Está en |
|---|---|
| Qué pieza es y de dónde salió | `fuentes.json`: `titulo`, `fuente`, `url` |
| Bajo qué licencia entró | `fuentes.json`: `licencia`, texto literal |
| A quién se acreditó y dónde | `creditos.txt` + la descripción publicada (§ 184) |
| Que la pieza pasó el filtro | La salida del sondeo y de la compuerta (§ 188) |
| El archivo original tal como se descargó | `archivo/`, sin tocar |
| En qué segundo aparece | La tabla de eventos del episodio |
| Cuándo se descargó | La fecha del fichero y `sondeo.json` |

Por eso `archivo/` no se limpia al terminar un episodio, y por eso la URL anotada es **la
de la ficha del ítem**: es la página donde cualquiera puede leer, hoy, la licencia que
invocamos.

## El procedimiento, en orden

**1 · No borrar nada.** Ni el vídeo, ni el archivo, ni el registro. Borrar destruye la
prueba y en algunos casos empeora la posición. Si hay que retirar el episodio se hace
después, con criterio, no en caliente.

**2 · Identificar la pieza exacta.** El aviso suele indicar el tramo de tiempo. Con la
tabla de eventos se sabe en diez segundos qué `alias` ocupa ese segundo.

**3 · Abrir su entrada en `fuentes.json` y volver a la ficha.** Tres preguntas:

- ¿La ficha sigue diciendo lo mismo que anotamos?
- ¿La licencia cubre uso comercial y adaptación (§ 180)?
- ¿Cumplimos la atribución que exigía (§ 184)?

**4 · Clasificar el caso.** De aquí salen cuatro finales y solo cuatro:

| Caso | Qué hacemos |
|---|---|
| **Tenemos razón y está documentado** | Se responde por la vía formal adjuntando ficha, licencia y bloque de créditos |
| **Teníamos razón pero faltó el crédito** | Se corrige la descripción **hoy** y se responde explicando la corrección |
| **La ficha cambió o era errónea** | Se sustituye la pieza y se vuelve a subir el corte corregido |
| **Nos equivocamos** | Se retira o se sustituye, sin discutir: un plano no vale un aviso en el canal |

**5 · Responder una vez, corto y con documentos.** Lo que convence es la ficha con la
licencia, no el tono.

**6 · Anotar el caso** en la bitácora del episodio: qué pieza, qué se reclamó, qué se
respondió, cómo acabó. El segundo aviso sobre el mismo tipo de material deja de ser mala
suerte y pasa a ser un fallo de criterio que corregir aguas arriba.

## El molde de respuesta

```
Asunto: <ID del aviso> — episodio «<título>», minuto <mm:ss>

La imagen señalada es «<título de la obra>», de <autor>, obtenida de <fuente>
el <fecha>, publicada bajo <licencia literal>.
Ficha del ítem: <URL>
La atribución figura en la descripción del vídeo desde su publicación:
  «<línea de crédito tal como aparece>»

Adjunto captura de la ficha en la fecha de descarga y el registro de fuentes
del episodio.

Solicito la retirada de la reclamación. Quedo a disposición para cualquier
comprobación adicional.
```

Antes de enviarlo: **si la vía elegida tiene efectos legales** —y muchas
impugnaciones formales los tienen, incluido someterse a una jurisdicción—, lo revisa un
abogado. Este molde sirve para ordenar los hechos, no para sustituir ese paso.

## Lo que nunca se hace

**Ignorar el aviso** (el plazo corre solo). **Borrar el vídeo para quitarlo de en medio**
(se pierde la prueba y el aviso a veces permanece). **Responder enfadado** (al otro lado
casi siempre hay un sistema automático). **Impugnar sin la ficha delante** — si no puedes
enseñar la licencia, no la tienes. **Reeditar en silencio sin contestar.** Y **volver a
subir el mismo material «recortado un poco más»**: es el camino directo al segundo aviso.

## Por qué el registro completo lo cambia todo

Sin registro, una reclamación significa reconstruir de memoria de dónde salieron 80
imágenes, en fin de semana, con un plazo encima y sin saber si tienes razón. Con
registro significa abrir un `.json`, copiar tres campos y contestar. Es la misma pieza
de trabajo —anotar la licencia al descargar— vista desde el otro lado: **media hora
repartida a lo largo de un episodio contra un fin de semana de pánico y un vídeo
retirado.** Esa es toda la justificación de los módulos 180–188.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| No distinguir qué tipo de aviso ha llegado | Se responde por la vía equivocada y se pierde el plazo |
| Borrar el episodio en caliente | Se destruye la prueba y el aviso puede seguir |
| Impugnar «por principio» sin documentación | Escalada innecesaria con efectos legales reales |
| Guardar solo el enlace, no el archivo ni la captura de la ficha | Si la ficha cambió, no queda nada que enseñar |
| Discutir en el correo en vez de adjuntar la licencia | Alarga el trámite y no aporta nada |
| No anotar el caso al cerrarlo | Se repite el mismo fallo en el episodio siguiente |
| Dar por hecho que este manual describe el procedimiento vigente | Las políticas cambian: se comprueban el día del aviso |

## Relacionado

`188` `fuentes.json` como compuerta · `184` la atribución en la descripción ·
`186` fotos de agencia · `133` reclamaciones: qué hacer (sonido) ·
`96` verificación de datos
