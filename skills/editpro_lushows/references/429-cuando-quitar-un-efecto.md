# 429 — Cuándo quitar un efecto

Añadir un efecto es fácil: hay una razón, se escribe una línea, se ve bonito en la escena de prueba.
Quitarlo es difícil, y no por razones técnicas. Un efecto puesto se convierte en «cómo se ve el canal»
en tres episodios, y a partir de ahí retirarlo se siente como romper algo.

Este módulo cierra el bloque con el procedimiento de retirada: **los seis disparadores que obligan a
revisarlo, cómo se prueba la retirada sin destruir el trabajo, y cómo se documenta.**

---

## 1. Los seis disparadores

Un efecto entra en revisión —no se borra automáticamente, entra en revisión— cuando ocurre una de estas
seis cosas.

| # | Disparador | Umbral duro | Módulo |
|---|---|---|---|
| 1 | **No se mide** | PSNR > 50 dB o `inf` contra la versión sin él | `423` |
| 2 | **No sobrevive a la entrega** | su magnitud cae >70% tras el reencode de red | `428` |
| 3 | **Cuesta más que su vecino más caro** | `utime` propio > el del resto de la cadena junta | `422` |
| 4 | **Otro eslabón ya lo hace** | quitarlo cambia el resultado menos de 2 dB | `425` |
| 5 | **Tapa en vez de resolver** | existe una versión del material sin el problema | `424` |
| 6 | **Se volvió la firma de todos** | aparece en la plantilla por defecto de las apps | `56`, `460` |

Los cinco primeros se disparan con un número. El sexto es de criterio y es el que más tarda en
reconocerse: un efecto que era distintivo cuando se adoptó deja de serlo cuando se vuelve el preset del
año. Ver `469` para la operación inversa —rehabilitar uno quemado.

---

## 2. Cómo se prueba la retirada

**No se borra la línea.** Se renderiza la pieza completa en sus dos versiones y se comparan con el mismo
protocolo con el que se compara cualquier cosa (`369`, `472`):

```bash
#!/usr/bin/env bash
# retirar.sh — compara la pieza con y sin un eslabon
CON="eq=contrast=1.05:saturation=0.94:gamma=1.16:brightness=0.045,noise=alls=6:allf=t+u,vignette=PI/5.6"
SIN="eq=contrast=1.05:saturation=0.94:gamma=1.16:brightness=0.045,noise=alls=6:allf=t+u"

for v in CON SIN; do
  F=$(eval echo \$$v)
  ffmpeg -hide_banner -loglevel error -y -i mudo.mp4 -vf "$F,format=yuv420p" \
    -c:v libx264 -crf 18 -preset slow -an "ep_$v.mp4"
done

# 1) cuanto cambio, en numeros
ffmpeg -hide_banner -i ep_CON.mp4 -i ep_SIN.mp4 -lavfi "[0:v][1:v]psnr" -f null - 2>&1 | grep PSNR
ffmpeg -hide_banner -i ep_CON.mp4 -i ep_SIN.mp4 -lavfi "[0:v][1:v]ssim" -f null - 2>&1 | grep SSIM
# 2) cuanto peso ahorra
ls -l ep_CON.mp4 ep_SIN.mp4
# 3) y despues del reencode de la red (428)
for v in CON SIN; do
  ffmpeg -hide_banner -loglevel error -y -i "ep_$v.mp4" -vf "scale=1280:-2" \
    -c:v libx264 -b:v 2000k -maxrate 2400k -bufsize 4000k -preset medium -an "red_$v.mp4"
done
ffmpeg -hide_banner -i red_CON.mp4 -i red_SIN.mp4 -lavfi "[0:v][1:v]psnr" -f null - 2>&1 | grep PSNR
```

**La línea 3 es la que decide en la mayoría de los casos.** Un efecto puede separarse 38 dB en el master
y solo 49 dB después del reencode de la red: eso significa que en lo que la gente ve, las dos versiones
son casi la misma, y la versión sin el efecto es la que cuesta menos y da más bitrate al resto.

---

## 3. La prueba del día después

Las métricas deciden los casos claros. Los que quedan en la zona media se deciden mirando, y mirar tiene
su propio protocolo, porque el ojo del editor está contaminado por haber pasado seis horas ajustando
justo ese efecto.

1. Renderiza las dos versiones y **nómbralas para no saber cuál es cuál** (`a.mp4`, `b.mp4`, con el
   mapeo en un archivo aparte).
2. **Un día de separación.** No el mismo día: el ojo se acostumbra dentro de una sesión.
3. Míralas **en el dispositivo real**, a tamaño real, con el brillo real (`376`).
4. Escribe qué ves **antes** de mirar el mapeo.
5. Si no distingues cuál es cuál, gana la barata. Sin discusión y sin pena.

Esa última regla es todo el módulo en una línea: **cuando dos versiones empatan, gana la que cuesta
menos.** Menos CPU, menos bitrate, menos presupuesto de atención, menos eslabones que depurar.

---

## 4. Cómo se retira sin romper nada

El error operativo es borrar la línea y seguir. Lo que se hace:

```python
# En la plantilla, el efecto se retira comentado, con su motivo y su fecha.
# RETIRADO 2026-09-11 — eq=saturation=1.02
#   PSNR 52.88 dB / SSIM 0.999988 contra la version sin el: no se mide.
#   0% de cambio en el peso codificado. El codificador tampoco lo veia.
#   Para volver a ponerlo haria falta subir a 1.15 y volver a medir.
FILTROS = "eq=contrast=1.05:gamma=1.16:brightness=0.045,noise=alls=6:allf=t+u,vignette=PI/5.6"
```

Tres razones para esa forma:

- **El motivo, no solo el hecho.** «Quitado» invita a volver a ponerlo; «quitado porque da 52,88 dB»
  cierra la discusión.
- **La condición de reingreso.** Deja escrito qué tendría que pasar para que vuelva. Así la revisión de
  dentro de un año es de treinta segundos.
- **El número y la fecha.** La medida envejece: si cambias de fuente, de resolución o de codificador,
  hay que repetirla.

Y en el repositorio, el cambio va **solo**: un commit por efecto retirado, con la medida en el mensaje.
Un commit que quita tres efectos a la vez no se puede revertir a medias.

---

## 5. La revisión periódica

Los efectos no se revisan cuando molestan: se revisan en calendario, porque el momento en que molestan
es el momento en que ya llevan seis meses costando.

**Cada cierre de episodio** (o cada mes, si no hay episodios):

```bash
# el barrido de 423 sobre la cadena de acabado, entero
bash aporte.sh                        # cuanto aporta cada eslabon
# la tabla de coste de 422
bash medir.sh                         # utime, PSNR, SSIM, MB por efecto
# la supervivencia de 428
bash m5_compresion.sh                 # que queda tras CRF 24 y el reencode de red
```

Tres comandos, veinte minutos, y sale una lista de candidatos. La regla de la casa: **de cada revisión
sale al menos un efecto retirado o un umbral ajustado.** Si nunca sale nada, la revisión se está
haciendo para confirmar, no para comprobar.

---

## 6. Los cuatro que no se retiran por métrica

Hay efectos cuya justificación no cabe en un PSNR y que por tanto **no se someten a este procedimiento**
tal cual:

1. **La firma de marca.** Si la identidad es el grano de archivo, el grano no es un efecto: es la marca.
   Se revisa en `directorcreativo_lushows`, no aquí.
2. **El acumulativo.** Un grano fino sostenido nueve minutos cambia la sensación del conjunto sin que
   ningún fotograma lo delate. Su prueba es la del día después sobre la pieza completa, no el PSNR de
   una escena (`472`).
3. **El de accesibilidad.** Un contorno en el subtítulo que sube el contraste sobre fondos claros existe
   para que se lea, no para que se vea bonito. El umbral es de legibilidad (`376`), no de distancia.
4. **El de compatibilidad.** `format=yuv420p`, `setsar=1`, `fps=30`. No son efectos: son requisitos, y
   quitarlos rompe la reproducción (`102`).

Los cuatro tienen una cosa en común: su hipótesis no es «cambia la imagen». Por eso medir la imagen no
los juzga.

---

## 7. El manifiesto de la retirada

La cadena de acabado de una plantilla que lleva tres años viva tiende a crecer y nunca a menguar. Cada
episodio añade un ajuste, nadie quita nada, y al cuarto año hay once filtros de los que cinco no hacen
nada, dos se contradicen y uno tapa un problema que ya no existe.

La única defensa es la asimetría deliberada: **cuesta más dejar un efecto que quitarlo.** Para dejarlo
hace falta una medida, una ficha y una fecha. Para quitarlo basta con que no pase la medida.

Un canal con una cadena de cuatro filtros, los cuatro medidos y defendibles, se ve más caro que uno con
once de los que nadie sabe cuáles hacen algo. Y renderiza en la mitad de tiempo.

---

## Errores frecuentes

- **Borrar la línea sin dejar el motivo.** Alguien la vuelve a poner en tres meses.
- **Decidir sobre el master.** La decisión se toma sobre lo que sale después del reencode de la red.
- **Comparar el mismo día.** El ojo se acostumbra dentro de una sesión. Un día de separación.
- **Comparar sabiendo cuál es cuál.** Renombra y guarda el mapeo aparte.
- **Empatar y quedarse con la versión cara.** Si empatan, gana la barata.
- **Retirar varios efectos en un commit.** No se puede revertir a medias.
- **Revisar solo cuando algo molesta.** Para entonces lleva medio año costando.
- **Someter la firma de marca al PSNR.** Esa decisión no es de este bloque.
- **Quitar `format=yuv420p` o `setsar=1` porque «no se miden».** No son efectos: son requisitos.
- **Confundir «no lo distingo en la escena de prueba» con «no aporta».** Si la hipótesis es acumulativa,
  la prueba es sobre la pieza completa.

---

## Checklist

- [ ] Sé cuál de los seis disparadores se activó.
- [ ] Rendericé la pieza completa en las dos versiones, no una escena.
- [ ] Comparé también **después** del reencode de la red.
- [ ] Si estaba en la zona media, hice la prueba a ciegas con un día de separación.
- [ ] En caso de empate, me quedé con la versión más barata.
- [ ] El efecto retirado quedó comentado con motivo, medida, fecha y condición de reingreso.
- [ ] El cambio va en su propio commit, con la medida en el mensaje.
- [ ] Anoté cuánto tiempo de render y cuánto peso ahorra la retirada.
- [ ] La revisión periódica está en el calendario, no en «cuando moleste».
- [ ] Los efectos de marca, acumulativos, de accesibilidad y de compatibilidad quedaron fuera del
      procedimiento y sé por qué.

---

## Relacionado

- `420`–`423` — el arnés, las magnitudes, el coste y el efecto que no se ve
- `424` — el parche: cuándo es legítimo y cuándo se retira
- `425`, `426` — el efecto redundante y el que cambia de aporte al moverse de sitio
- `428` — la supervivencia a la entrega, que es la prueba que más retiradas provoca
- `469` — rehabilitar un efecto quemado: la operación inversa
- `472`, `477` — la prueba A/B de un efecto y la revisión final
- `478` — documentar la receta
- `369` — comparar dos videos sin engañarse
- `139` — mantener un pipeline vivo
