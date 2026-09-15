# 337 — La toma falsa como material: cuándo el error es mejor que la toma buena

**Qué resuelve:** el material que se descarta por definición, sin mirarlo. Las tomas donde alguien se
equivocó, se rió, arrancó mal o habló antes de que "empezara". En rodajes con gente que no es actor —o
sea, casi todos los de un negocio— **ahí está la mitad de lo bueno**.

---

## 1. Qué es una toma falsa

Todo lo que quedó grabado y no era "la toma":

- El momento **antes** de que arrancara: la persona acomodándose, riéndose, diciendo "¿ya?".
- El error de dicción y la reacción al error.
- La risa después de trabarse.
- Lo que pasó **después** de decir "corte", cuando el cuerpo se suelta.
- La interrupción: alguien que entra, un vaso que se cae, el ruido de la calle.
- La toma que se abandonó a la mitad.

En la carpeta esas tomas se ven igual que las buenas. Y como se ven igual, casi nadie las abre.

---

## 2. Por qué a veces le ganan a la toma buena

Porque una toma buena de alguien que no es actor suele ser **una toma correcta y muerta**. La persona
está cumpliendo: recuerda el texto, no se equivoca, mira a cámara, y en la cara se le nota que está
recitando.

La toma falsa tiene lo único que no se puede actuar sin oficio: **verdad**. Y en video corto la verdad
retiene más que la corrección.

Hay un patrón que se repite y conviene conocer (`233`): en la toma 1 la persona está tensa; entre la 3 y
la 6 está en su mejor momento; después de la 8 ya está resignada. **Y los mejores segundos casi nunca
están dentro de la toma: están en el borde**, justo antes de empezar o justo después de creer que
terminó.

---

## 3. Las cinco clases y qué hacer con cada una

| Clase | Qué contiene | Dónde va |
|---|---|---|
| **La risa** | se trabó y se rió de sí mismo | remate o corte de aire |
| **El error con gracia** | dijo la palabra al revés | gancho, si el error se entiende solo |
| **El "antes"** | acomodándose, hablando normal | **gancho** — la clase más valiosa |
| **El "después"** | soltó el cuerpo al creer que terminó | desarrollo o remate |
| **La interrupción** | entró alguien, se cayó algo | inserto o gancho, si es visual |

**La clase más valiosa es "el antes"**, y por una razón concreta: es el único material donde la persona
**no está actuando de sí misma**. Camina distinto, habla distinto, la cara está distinta. Es exactamente
lo que el resto del video intenta fingir.

---

## 4. Dónde encaja en la estructura

- **Como gancho.** Un error o una risa en el segundo 0 detiene el pulgar mejor que un plano correcto,
  porque rompe el patrón de "esto es un anuncio" (`30`, `335`).
- **Como remate.** Es el uso clásico y el más seguro: el video termina, y al final aparece la toma falsa
  como propina. Aumenta la sensación de cercanía y no arriesga el mensaje (`33`).
- **Como corte de aire.** Media risa de un segundo entre dos bloques de información deja respirar.
- **Como serie propia.** El "detrás de cámaras" es un pilar de contenido completo (`241`, `34`).

Lo que **no** funciona: meter tomas falsas en medio del desarrollo. Ahí el espectador está entendiendo
algo, y la interrupción lo saca.

---

## 5. Cómo se busca (porque no se encuentra sola)

**a) Los extremos de cada archivo.** El oro está en los primeros y los últimos segundos. Sácalos todos de
una y míralos de corrido:

```bash
for f in *.mp4; do
  ffmpeg -v error -t 4 -i "$f" -c copy "bordes/${f%.mp4}_ini.mp4"        # primeros 4 s
  ffmpeg -v error -sseof -4 -i "$f" -c copy "bordes/${f%.mp4}_fin.mp4"   # últimos 4 s
done
```

`-sseof -4` busca desde el final del archivo. Verificado: devuelve exactamente 4 segundos.

Con 16 tomas eso son 128 segundos de material, se ven en dos minutos, y es donde está lo que nadie ha
visto.

**b) Buscar risas en la transcripción.** Los transcriptores marcan `[risas]`, `[laughs]` o dejan frases
cortadas y repetidas. Busca en el `.srt` (`12`, `124`).

**c) Buscar picos de energía en el audio.** Una risa es un pico corto y fuerte:

```bash
ffmpeg -i toma.mp4 -af "silencedetect=noise=-30dB:d=0.6" -f null - 2>&1 | grep silence_
```

Los tramos **entre** silencios largos suelen ser los intentos; lo que hay justo después del último
silencio suele ser la reacción.

**d) Mirar la hoja de contactos buscando expresiones**, no encuadres (`333`). En el material real de
Bendita Pola hay cinco tomas del mismo plano de barra en las que **solo cambia la cara**: una sonriendo,
una con los ojos cerrados, una con los brazos arriba. Esa de los brazos arriba no estaba en ningún plan
de rodaje: fue una reacción. Y es la mejor candidata a remate de todo el material (`335`).

---

## 6. La regla del consentimiento

No es un detalle legal: es cómo se consigue que la persona vuelva a ponerse delante de la cámara.

- **Pregunta antes de publicar.** "Quedó esta donde te reíste, ¿la subo?" Treinta segundos.
- **Nunca publiques un error que la deje mal.** Un tropiezo con gracia sí; un olvido que se ve como
  torpeza, no.
- **Si el que se equivoca eres tú, decides tú.** Si es un empleado o un cliente, decide él.
- **Cuidado con quien pasa por detrás.** Un cliente del bar que aparece de fondo en una toma falsa no
  aceptó salir en nada (`319`).

Una toma falsa publicada sin permiso enseña a todo el equipo que delante de la cámara hay que tener
cuidado. Y con gente cuidadosa no se consigue verdad nunca más.

---

## 7. Cuándo NO usarla

- **Cuando el error hace ver mal al producto.** El vaso que se derrama sobre la comida no es simpático:
  es un problema de higiene en video.
- **Cuando el error es de la marca.** Un precio dicho mal, un dato equivocado. Se corta, no se celebra.
- **Cuando es de un cliente que pagó por un video corporativo.** Ese material no se publica ni en
  broma (`181`).
- **Cuando ya usaste tomas falsas en los tres videos anteriores.** Deja de ser verdad y se vuelve un
  recurso; y un recurso repetido se lee como fórmula.
- **Cuando el video tiene un solo trabajo serio** (una disculpa, un aviso, un cierre por reforma).

---

## 8. La regla corta

> **La toma buena prueba que la persona puede hacerlo. La toma falsa prueba que la persona existe.**
> Un video corto necesita las dos, y casi siempre la segunda va en el primer segundo o en el último.

Y una consecuencia práctica sobre el descarte (`336`): antes de mover un archivo a `_descartes` por
"se equivocó", mira los bordes. Se equivocó **en la toma**; a lo mejor lo mejor del rodaje está en el
segundo 3 y en el segundo final.

---

## Errores comunes

1. **No abrir nunca los archivos "malos".** Es donde está el material que nadie ha visto.
2. **Cortar la grabación apenas termina la frase.** Los tres segundos siguientes son los buenos. Deja
   correr la cámara.
3. **Empezar a grabar justo cuando la persona está lista.** Lo mismo por el otro lado: graba mientras se
   acomoda.
4. **Meter la toma falsa en medio del desarrollo.** Saca al espectador de lo que estaba entendiendo.
5. **Publicarla sin preguntar.** Cuesta treinta segundos y evita perder a la persona para siempre.
6. **Usar un error que deja mal a alguien.** Nunca. Ni con permiso dudoso.
7. **Convertir el blooper en fórmula.** Repetido en todos los videos deja de ser verdad.
8. **Confundir toma falsa con toma descuidada.** El valor está en la reacción humana, no en el desorden.
9. **Usar una toma falsa donde el producto queda mal.** Un derrame sobre la comida no es simpático.
10. **Perder los bordes al hacer copias limpias del material.** Si recortas los archivos al importar,
    borraste justo lo bueno.
11. **Creer que se necesita audio limpio.** En la risa el audio sucio no molesta; en el desarrollo sí.
12. **Buscar tomas falsas a ojo en cuatro horas de material.** Saca los bordes con el bucle y míralos de
    corrido.
13. **Descartar una toma "porque se equivocó" sin revisar los últimos cuatro segundos.**

---

## Checklist

- [ ] Extraje los **primeros y últimos 4 segundos** de cada toma y los vi de corrido.
- [ ] Busqué **risas y frases cortadas** en la transcripción.
- [ ] Miré la hoja de contactos buscando **expresiones**, no encuadres.
- [ ] Clasifiqué lo encontrado: risa, error, "antes", "después", interrupción.
- [ ] Le asigné un **puesto** (gancho, remate, corte de aire), no lo metí en el desarrollo.
- [ ] Verifiqué que el error **no deja mal** a la persona ni al producto.
- [ ] **Pregunté** antes de publicar si sale alguien que no soy yo.
- [ ] Revisé que no salga gente de fondo que no dio permiso.
- [ ] No es el cuarto video seguido que usa el mismo recurso.
- [ ] En el próximo rodaje: **grabar antes** de que esté listo y **no cortar** al terminar.
- [ ] Antes de mandar algo a `_descartes`, revisé sus bordes.
- [ ] Guardé las tomas falsas buenas en una carpeta propia: son material de serie (`242`).
