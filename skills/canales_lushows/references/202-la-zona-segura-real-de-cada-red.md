# 202 · La zona segura real de cada red

**Qué resuelve:** este módulo **no trae una tabla de zonas seguras**. Trae el
procedimiento para producir la del canal, y la razón por la que no se copia ninguna de
las que ya existen.

El problema no es la falta de cifras: es que sobran y no concuerdan. Buscando el margen
inferior de Instagram sobre 1080×1920 entre los manuales que ya usa esta casa aparecen
**400, 420, 480, 192 y un rango de 384–672 px**, y **todos fechados en agosto de 2026**.
Cinco números para la misma medida el mismo mes. Añadir un sexto no resuelve nada: lo
que hace falta es que el canal mida el suyo, lo firme y lo feche.

`editpro 45` tiene la tabla por plataforma, `editpro 415` la herramienta genérica y
`editpro 418` el protocolo de campo. Nada de eso se repite. Aquí está **qué mide este
canal, con qué carta, y qué hace mientras no lo haya medido**.

---

## El estado honesto, hoy

> **11-sep-2026 — el canal no ha medido ninguna zona segura propia.** No se ha publicado
> ningún corte vertical, así que no hay captura de ninguna app con material del canal
> dentro. Cualquier cifra de interfaz que aparezca en esta skill antes de esa medición es
> **hipótesis de trabajo heredada**, no dato.

La hipótesis de trabajo es la de `49` —200 arriba, 520 abajo, 200 a la derecha, 60 a la
izquierda; zona útil **820 × 1200**— elegida por ser la unión conservadora de las tres
redes. Es lo que usan `201` y `203`. Se mantiene hasta que la medición la sustituya, y
entonces se sustituye en `49` y en ningún otro sitio, para que no haya dos.

## La carta fiducial del canal

Una captura sola no sirve: dice cuántos píxeles **de la captura** tapa un botón, y eso
depende del teléfono. Hace falta una carta con marcas de posición conocida para poder
hacer la resta. Generada y verificada el **11-sep-2026**:

```bash
ffmpeg -f lavfi -i "color=c=0x101010:s=1080x1920" -vf "
drawgrid=w=108:h=96:t=2:c=0x303030@1,
drawbox=x=0:y=0:w=1080:h=8:color=0xFF0000@1:t=fill,
drawbox=x=0:y=1912:w=1080:h=8:color=0xFF0000@1:t=fill,
drawbox=x=0:y=956:w=1080:h=8:color=0x00FF00@1:t=fill,
drawbox=x=536:y=0:w=8:h=1920:color=0x00AAFF@1:t=fill" -frames:v 1 -y carta.png
```

Diez columnas de 108 px y veinte filas de 96 px. Las tres barras no son adorno: la roja
de arriba y la de abajo son los **fiduciales de escala** (su separación son 1912 px
conocidos) y la verde marca la mitad exacta. La azul da la vertical, que es la que
delata si la app recortó a los lados en vez de encajar por alto.

La carta se convierte en vídeo de 12 s y se sube **sin publicar** —borrador, o publicado
como privado— a cada una de las cuatro superficies. Doce segundos porque hay que darle
tiempo a que aparezcan los controles del reproductor, que en Shorts tardan.

## La resta

Con la captura del móvil en la mano:

```python
# 1 · escala: cuántos píxeles de captura vale un píxel de lienzo
alto_en_captura = y_barra_roja_abajo - y_barra_roja_arriba     # medido en la captura
escala = alto_en_captura / 1912.0

# 2 · cada margen, de captura a lienzo
def a_lienzo(px_captura):
    return px_captura / escala
```

Ejecutado sobre una captura de prueba con `alto_en_captura = 2400` (escala 1,2500):

| Medido en la captura | En el lienzo |
|---|---|
| 312 px | **250 px** |
| 640 px | **512 px** |

Sin la escala, esos 640 px se apuntarían como «640 abajo» y quedarían un 25 % largos.
**Esa es exactamente la clase de error que produce cinco tablas distintas del mismo mes.**

## Los tres casos de cada margen, no uno

Un margen inferior no es un número: son tres, y publicar sólo el del medio es lo que
hace que la tabla falle en producción.

| Caso | Cómo se provoca en la prueba | Para qué sirve |
|---|---|---|
| **Vacío** | Sin descripción, sin hashtags, orgánico | El suelo: por debajo de esto nunca tapa |
| **Lleno** | Descripción de 3 líneas con hashtags | El que se usa para componer |
| **Pauta** | El mismo vídeo como anuncio, con botón de acción | Sólo si el corte se va a promocionar |

El canal compone contra el caso **lleno**, porque sus descripciones llevan fuentes y las
fuentes son largas (`381`). Si algún día se promociona un corte, se vuelve a medir: el
botón de acción no está en ninguna tabla orgánica.

## Lo que se guarda

Una medición que no se puede auditar dentro de seis meses no vale más que un recuerdo.
El formato de registro es este, y va en el repositorio, no en la cabeza de nadie:

```
red        margen   px_lienzo  caso    dispositivo          medido_por  fecha
tiktok     inferior       ---  lleno   ---                  ---         PENDIENTE
shorts     inferior       ---  lleno   ---                  ---         PENDIENTE
reels      inferior       ---  lleno   ---                  ---         PENDIENTE
facebook   inferior       ---  lleno   ---                  ---         PENDIENTE
```

Cuatro filas por margen (superior, inferior, derecha, izquierda) y cuatro redes: dieciséis
medidas. Con la carta ya hecha, la sesión entera son unos veinte minutos y se repite
cuando una app se rediseña, no cada vez que alguien duda.

## Mientras tanto, la regla que no depende de medir

Hay una comprobación que funciona sin cifras y que ninguna tabla sustituye: **subir el
corte, mirarlo en el teléfono y ver si se lee**. `166` da la prueba del pulgar para el
monitor; esta es la de verdad, con la interfaz encima. Un corte que no ha pasado por un
teléfono real no se publica, tenga la tabla que tenga detrás.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Copiar la tabla de zona segura de otro manual | Ya hay cinco contradictorias del mismo mes |
| Medir sobre la captura sin fiduciales | El margen sale un 25 % largo con una captura de 2400 px |
| Publicar un margen sin fecha ni dispositivo | A seis meses es un recuerdo, no un dato |
| Medir sólo el caso vacío | La descripción con fuentes crece y se come el rótulo |
| Dar por buena la zona de un anuncio en orgánico | El botón de acción no existe en orgánico, y al revés |
| Guardar la cifra en dos sitios | Vuelve a haber dos tablas y gana la equivocada |
| Fiarse de la vista previa del escritorio | Ahí no hay interfaz: es el sitio donde todo se lee |

## Relacionado

`49` zona segura y tamaños (la hipótesis de trabajo vigente) · `166` la prueba del pulgar ·
`168` reproducir antes de afirmar · `201` la columna · `203` densidad en vertical ·
editpro `45` zona segura por plataforma · editpro `415` la interfaz de cada red ·
editpro `418` medir la zona segura de verdad
