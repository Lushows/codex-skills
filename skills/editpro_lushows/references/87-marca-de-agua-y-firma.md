# 87 — Marca de agua y firma


> ⚠️ **Las cifras de zona segura de este módulo no son la referencia.**
> El dueño es `45-zona-segura-por-plataforma`, que además distingue el recorte
> geométrico (se calcula) de la interfaz de la app (se mide, y caduca). Antes de
> montar con un número de aquí, mídelo con `418-medir-la-zona-segura-de-verdad`.
**Qué resuelve:** quieres que se sepa que el video es tuyo, pero la mayoría de las marcas de agua o no
se ven (y entonces no sirven) o estorban tanto que empeoran el video. Este módulo da los números
concretos: dónde va, de qué tamaño, con qué opacidad, y cuándo es mejor no poner nada.

---

## 1. Para qué sirve de verdad una marca de agua

Hay tres razones legítimas y una ilegítima:

| Razón | ¿Vale? | Comentario |
|---|---|---|
| Reconocimiento de marca (que sepan de quién es) | sí | la principal |
| Que el crédito sobreviva si te lo re-suben | sí | por eso no va donde recortan |
| Que el cliente vea que el video se hizo | sí, temporal | va en el corte de revisión, no en el final |
| "Porque hay que ponerle el logo" | **no** | es la razón por la que la mayoría estorba |

**La pregunta honesta antes de ponerla:** ¿qué se pierde si no está? Si la respuesta es "nada", no la
pongas. Un video sin marca de agua que se ve limpio vende más que uno firmado que se ve saturado.

Y un dato incómodo: en video social, el nombre de la cuenta **ya está en pantalla**, arriba o abajo,
puesto por la plataforma. Tu marca de agua está compitiendo con una firma que ya existe.

---

## 2. La regla de la esquina segura

Las plataformas tapan pedazos de tu video con su propia interfaz. Poner el logo ahí es tirarlo a la
basura. En vertical 1080x1920 el mapa es este:

```
 y=0    +--------------------------------+
        |  interfaz superior (0-240)     |  <- no
 y=240  +--------------------------------+
        |                                |
        |   ZONA SEGURA                  |  <- si (pero no tapes la cara)
        |                                |
 y=1540 +--------------------------------+
        | descripcion / subtitulos       |  <- no
        | botones a la derecha (240 px)  |  <- no
 y=1920 +--------------------------------+
```

Las zonas prohibidas por plataforma (agosto 2026, detalle en `45`):

| Plataforma | Arriba | Abajo | Lateral derecho |
|---|---|---|---|
| TikTok | 220 px | 520 px | 260 px |
| Instagram Reels | 240 px | 480 px | 220 px |
| YouTube Shorts | 200 px | 440 px | 230 px |
| **Uso seguro para todas** | **260 px** | **540 px** | **270 px** |

**La conclusión práctica:** en vertical, la marca de agua va **arriba a la izquierda**, en `x=64,
y=290`. Es la única esquina que ninguna plataforma tapa, que no compite con el botón de perfil (que va
arriba a la derecha en varias) y que no cae en la zona de recorte cuando alguien re-sube el video.

En horizontal 1920x1080 la esquina segura es **abajo a la derecha** (`x=W-w-72, y=H-h-72`), que es la
convención de televisión y de YouTube largo.

---

## 3. Los números: tamaño y opacidad

Aquí está el módulo entero en una tabla. Estos valores están calibrados para vertical 1080x1920:

| Parámetro | Valor | Por qué |
|---|---|---|
| **Altura del logo** | 44 – 64 px (2,3% – 3,3% de la altura) | se lee, no compite |
| **Margen al borde** | 56 – 72 px | menos se siente pegado, más se siente flotando |
| **Opacidad** | **50% – 65%** | por debajo no se ve; por encima estorba |
| **Color** | blanco puro, o el logo en monocromo | el logo a todo color pelea con la imagen |

**La opacidad es el parámetro que casi todos se equivocan.** Un logo al 100% en la esquina no es una
firma: es un anuncio dentro de tu anuncio. Al 55% se percibe, se reconoce, y el ojo lo deja de mirar
después del primer segundo, que es exactamente lo que quieres.

```bash
ffmpeg -i base.mp4 -i logo.png \
  -filter_complex "[1:v]scale=-1:56,format=rgba,colorchannelmixer=aa=0.55[wm];\
[0:v][wm]overlay=x=64:y=290" \
  -map 0:a -c:a copy -c:v libx264 -crf 18 -pix_fmt yuv420p salida.mp4
```

`colorchannelmixer=aa=0.55` multiplica el canal alfa por 0,55: baja la opacidad respetando la
transparencia que ya traía el PNG. Es la forma correcta. (Poner un rectángulo semitransparente detrás
NO es lo mismo y se ve peor.)

### Logo monocromo desde un logo a color

Si solo tienes el logo a color y lo quieres en blanco:

```bash
ffmpeg -i logo_color.png -vf "format=rgba,colorchannelmixer=rr=0:rg=0:rb=0:rc=1:gr=0:gg=0:gb=0:gc=1:br=0:bg=0:bb=0:bc=1" -y logo_blanco.png
```

Ese filtro pone los tres canales de color en blanco y conserva el alfa. El logo se convierte en una
silueta blanca con la forma exacta del original.

---

## 4. El problema del fondo variable

Un logo blanco al 55% se ve perfecto sobre una imagen oscura y **desaparece** sobre una imagen clara.
Y en un video de 30 segundos vas a tener las dos cosas.

Tres soluciones, de peor a mejor:

**a) Contorno.** Funciona pero se ve tosco en logos con detalle.

**b) Sombra suave detrás del logo.** La buena para la mayoría de los casos:

```bash
-filter_complex "[1:v]scale=-1:56,format=rgba,split=2[wm][sh];\
[sh]colorchannelmixer=rr=0:gg=0:bb=0:aa=0.40,boxblur=6:1[shb];\
[0:v][shb]overlay=x=66:y=292[c1];\
[c1][wm]overlay=x=64:y=290,format=yuv420p[vout]"
```

Duplica el logo, lo vuelve negro difuminado al 40%, y lo pone 2 px desplazado detrás del logo blanco.
Sobre fondo claro, la sombra lo despega; sobre fondo oscuro, no se nota.

**c) Degradado sutil en la esquina.** Un oscurecimiento muy leve detrás de la zona del logo. Es lo que
hacen los canales de televisión. Se ve profesional pero hay que hacerlo muy suave o se nota el parche.

---

## 5. Marca de agua fija vs. intermitente

| | Fija (todo el video) | Intermitente (aparece y se va) |
|---|---|---|
| Cuándo | contenido largo, YouTube, tutoriales | **video social corto** |
| Ventaja | protege todo el metraje | no estorba, se nota más cuando aparece |
| Desventaja | el cerebro la borra en 2 segundos | si te recortan el video puede no aparecer |

**Para reels y TikToks: intermitente.** Aparece 2 segundos al principio y 2 al final. Ya está. El
espectador la ve dos veces conscientemente, que es más de lo que registra de una marca permanente que
lleva 30 segundos siendo ignorada.

```bash
-filter_complex "[1:v]scale=-1:56,format=rgba,colorchannelmixer=aa=0.60,\
fade=t=in:st=0.4:d=0.3:alpha=1,fade=t=out:st=2.6:d=0.3:alpha=1[wm1];\
[1:v]scale=-1:56,format=rgba,colorchannelmixer=aa=0.60,\
fade=t=in:st=26.0:d=0.3:alpha=1[wm2];\
[0:v][wm1]overlay=x=64:y=290:enable='between(t,0.35,2.95)'[c1];\
[c1][wm2]overlay=x=64:y=290:enable='gte(t,25.95)'[vout]"
```

Fíjate que el logo se usa dos veces: cada uso necesita su propia cadena de filtros. Una salida de filtro
no se puede consumir dos veces en ffmpeg — para eso está `split`, o como aquí, se procesa la entrada dos
veces.

---

## 6. Firmas que no son logos

La marca de agua no tiene que ser el logo. A veces funciona mejor:

- **El @usuario en texto.** Más útil que el logo si el objetivo es que te encuentren. Se lee, se busca,
  se escribe. Un logo no se puede googlear.

```bash
drawtext=fontfile='C\:/Windows/Fonts/arialbd.ttf':text='@gastrolatam':\
fontsize=34:fontcolor=white@0.55:x=64:y=290:\
shadowx=0:shadowy=2:shadowcolor=black@0.35
```

- **El elemento de marca, no el logo completo.** El isotipo solo, o una forma característica. Ocupa menos
  y marca igual si la marca ya tiene reconocimiento.
- **El personaje** apareciendo tres veces (`82`). Marca más que cualquier logo y no estorba porque hace
  otro trabajo al mismo tiempo.
- **El color.** Si todo tu contenido tiene el mismo tratamiento de color (`64`), ya está firmado. Es la
  firma más elegante que existe y es invisible.

---

## 7. Marca de agua para revisión de cliente

Caso distinto y con reglas opuestas: aquí **sí** quieres que estorbe, para que el corte de revisión no
se publique sin pagar ni se use por error.

```bash
ffmpeg -i corte_v3.mp4 -vf "\
drawtext=fontfile='C\:/Windows/Fonts/arialbd.ttf':text='REVISION - NO PUBLICAR':\
fontsize=64:fontcolor=white@0.22:x=(w-text_w)/2:y=(h-text_h)/2:\
box=0,\
drawtext=text='v3 - 2026-08-04':fontsize=36:fontcolor=white@0.5:x=48:y=h-70" \
  -c:v libx264 -crf 24 -preset veryfast -c:a copy revision_v3.mp4
```

Centrado, grande, al 22% de opacidad: se lee, no impide juzgar el montaje, e imposibilita publicarlo.
Y con la **versión y la fecha** abajo, que resuelve la mitad de las confusiones de las rondas de notas
(`182`, `96`).

---

## 8. Cuándo NO poner marca de agua

- **En un anuncio pagado.** El anuncio ya lleva el nombre de la marca, el botón de acción y el perfil.
  Otra firma es saturación y baja el rendimiento. En Meta y TikTok, los creativos que parecen contenido
  orgánico rinden mejor: una marca de agua grita "esto es publicidad" (`145`, `158`).
- **En contenido UGC / de creador.** El punto es que no parezca corporativo. La marca de agua lo mata.
- **En un testimonio.** Igual: cualquier cosa que huela a producción baja la credibilidad.
- **Cuando el video ya tiene el logo en el remate.** Firmar dos veces es firmar cero veces.
- **Cuando el video es cuadrado o vertical y ya va lleno de texto.** No hay espacio limpio; forzarlo
  ensucia.

---

## 9. Verificar que quedó bien

```bash
# Fotograma en un momento con fondo claro y en uno con fondo oscuro
ffmpeg -ss 4.0 -i salida.mp4 -frames:v 1 -y wm_claro.png
ffmpeg -ss 18.0 -i salida.mp4 -frames:v 1 -y wm_oscuro.png

# Miniatura, para ver si se lee en tamaño real de celular
ffmpeg -i wm_claro.png -vf "scale=-1:520" -y wm_claro_mini.png
```

Lo que buscas:

- Se **lee** en la miniatura (si no, está muy chico o muy transparente).
- **No compite** con la cara ni con el texto.
- **No cae** en zona de interfaz.
- Se ve **igual de bien** sobre fondo claro y oscuro.
- No hay **borde blanco** alrededor del logo (PNG mal recortado, ver `81`).

---

## Errores comunes

1. **Logo al 100% de opacidad.** No es una firma, es un anuncio dentro del anuncio. 50–65%.
2. **Logo gigante.** Más del 4% de la altura y ya compite con el contenido.
3. **Ponerlo abajo a la derecha en vertical.** Es exactamente donde TikTok e Instagram ponen sus botones.
   Se pierde entero.
4. **Ponerlo abajo en vertical, punto.** Ahí van los subtítulos y la descripción.
5. **Logo blanco sobre fondo que a veces es blanco.** Desaparece la mitad del video. Sombra suave detrás.
6. **Logo a todo color.** Pelea con la imagen. Monocromo, casi siempre blanco.
7. **Marca de agua fija en un reel de 20 segundos.** El cerebro la borra a los 2 segundos y solo te
   ensucia el cuadro. Intermitente.
8. **Poner marca de agua en un anuncio pagado.** Grita publicidad y baja el rendimiento.
9. **Reusar la misma salida de filtro dos veces.** ffmpeg no deja. Usa `split` o procesa la entrada de
   nuevo.
10. **Poner un rectángulo semitransparente detrás en vez de bajar el alfa del logo.** Se ve como un
    parche pegado.
11. **Firmar dos veces:** marca de agua + logo en el remate. Elige una.
12. **Mandar el corte de revisión sin versión ni fecha.** Media ronda de notas se pierde en "¿cuál era
    el bueno?".

---

## Checklist

Antes de dar por buena una firma:

- [ ] Me pregunté **qué se pierde si no está**. Si la respuesta era "nada", no la puse.
- [ ] Está en la **esquina segura** (vertical: arriba-izquierda `x=64, y=290`).
- [ ] Altura entre **44 y 64 px** (2,3%–3,3% de la altura del cuadro).
- [ ] Opacidad entre **50% y 65%**, aplicada con `colorchannelmixer=aa=`, no con un rectángulo.
- [ ] El logo va **monocromo**, no a todo color.
- [ ] Tiene **sombra suave** o contorno para sobrevivir sobre fondo claro.
- [ ] En video corto es **intermitente** (2 s al inicio, 2 s al final), no permanente.
- [ ] No tapa la cara, ni el subtítulo, ni el dato principal.
- [ ] Verifiqué un fotograma sobre **fondo claro** y uno sobre **fondo oscuro**.
- [ ] Lo revisé en **miniatura de 520 px**: se lee.
- [ ] El PNG no tiene borde blanco ni halo (`81`).
- [ ] Si es un anuncio pagado, UGC o testimonio, **decidí no ponerla** y lo dejé dicho.
- [ ] Si es un corte de revisión, lleva **texto de revisión + versión + fecha**.
