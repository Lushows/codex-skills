# 476 — El efecto y la retención

> **Este es el módulo que te va a decepcionar, y conviene.** La pregunta «¿este efecto sube la
> retención?» casi nunca tiene respuesta, y cuando la tiene, la respuesta casi siempre es no. Lo que sí
> se puede responder —y es lo que aporta este oficio— son dos preguntas anteriores que nadie se hace:
> **¿el efecto llega?** y **¿está donde la curva se cae?**

**Frontera, primero, para no reescribir lo que ya existe.** Leer una curva de retención es `301`.
Elegir qué métrica mirar y cuál ignorar es `300`. Localizar el fotograma culpable es `366`. Probar una
hipótesis con audiencia y muestra suficiente es `304`. Y el rendimiento de un creativo **en pauta**
—hook rate, hold rate, fatiga, volumen creativo— vive entero en las skills de anuncios:
`facebook_ads_lushows/68-creative-analytics`, `.../39-volumen-y-fatiga-creativa`,
`.../17-framework-de-testing` y sus equivalentes de `tiktok_ads_lushows`. Nada de eso se repite aquí.

---

## 1. La aritmética que cierra la discusión

Un episodio de 63,45 s con cinco destellos. Cada destello es una campana de 0,075 s de medio ancho, o
sea unos 0,2 s de presencia real:

```
5 destellos * 0,2 s = 1 s de efecto
1 s / 63,45 s = 1,6 % del metraje
```

**Un efecto no puede sostener el 98,4 % del vídeo en el que no está.** Lo que sostiene la retención es
lo que ocupa el otro 98 %: el guion, el ritmo, la densidad de eventos, la duración. Si la curva se cae
en el segundo 18, el culpable vive en el segundo 18 y casi nunca es un efecto — es una frase que sobra,
un plano que dura de más o un tramo sin nada en pantalla.

Lo que un efecto **sí** puede hacer, y no es poco:

| Puede | No puede |
|---|---|
| marcar cuál es el momento importante | hacer que un momento sea importante |
| evitar que un cambio de bloque pase de largo | arreglar un bloque aburrido |
| dar peso a una cifra que si no pasa desapercibida | dar interés a una cifra irrelevante |
| cerrar el remate | salvar un remate mal escrito |

---

## 2. La pregunta previa: ¿el efecto llega?

Un efecto que la plataforma destruye al recomprimir no puede afectar a nada. **Esa pregunta la contesta
entera `428`**, con su criterio del codificador —sobrevive lo grande y lo que se repite, se va lo fino y
lo aleatorio— y su medida de `YDIF` a lo largo de las cuatro etapas de entrega. `446` da la versión
práctica: qué ruido sí sobrevive. No se reconstruye aquí.

Lo único que añade este módulo es el atajo de comprobarlo **con la prueba que ya tienes montada**: corre
el arnés de `472` dos veces, antes y después de recomprimir, y mira si el PSNR entre A y B se mueve.

```bash
for f in A B; do
  ffmpeg -hide_banner -loglevel error -y -i $f.mp4 -vf "scale=720:-2" \
    -c:v libx264 -b:v 400k -maxrate 400k -bufsize 800k -preset veryfast \
    -pix_fmt yuv420p -an ${f}p.mp4
done
ffmpeg -hide_banner -i Ap.mp4 -i Bp.mp4 -lavfi psnr -f null - 2>&1 | grep -o "average:[0-9.]*"
```

Recuerda que `psnr` imprime en nivel `info`: con `-loglevel error` no sale nada (`420`, `432`).

Medido sobre el clip de `472` —PSNR entre la versión sin efecto y la versión con efecto, cuanto más bajo
más presente está el efecto:

| Efecto | Original | A 1.500 kbps | A 400 kbps |
|---|---|---|---|
| **Viñeta** | 20,62 dB | 20,62 | **20,59** |
| **Glow** | 29,07 dB | 29,02 | — |
| **Grano** | 43,57 dB | 42,66 | **38,98** |

La viñeta atraviesa una recompresión al cuarto del bitrate y sale idéntica. El grano no: su diferencia
con el original **crece** según se estrecha el canal. No es que sobreviva mejor — es que lo que llega ya
no es tu grano, sino lo que el códec hizo intentando guardarlo. Mismo resultado que `428` obtiene por
`YDIF`, por otro camino y sobre otro material.

> **Para la retención, el corolario:** si tu efecto vive en la alta frecuencia, el espectador no está
> viendo lo que tú aprobaste. Preguntarse si eso retiene no tiene sentido.

---

## 3. La segunda pregunta: ¿está donde la curva se cae?

Esto sí es accionable y sí se hace con datos reales, pero el dato lo da `301` y el fotograma lo da
`366`. El procedimiento, encadenado:

```
1. Curva de retencion -> el segundo donde cae        (301)
2. Ese segundo -> el fotograma culpable              (366)
3. Ese fotograma -> que hay ahi: plano, texto, efecto
4. Si hay un efecto ahi: quitalo y vuelve a medir    (304)
5. Si NO hay nada ahi: el problema es el guion o el ritmo, no los efectos
```

El paso 5 es el resultado más frecuente con diferencia. Anótalo cuando pase: un «no era el efecto» bien
documentado ahorra las tres discusiones siguientes.

Y una comprobación de reparto que cuesta un minuto: **pon los segundos de tus efectos al lado de los
segundos donde la curva cae.** En el piloto los efectos están en 6,88 / 20,55 / 33,02 / 41,85 / 62,93.
Si la curva se desploma en el 27 y no tienes nada entre el 20,55 y el 33,02, ya sabes dónde mirar — y no
es para meter un efecto ahí: es para ver por qué ese tramo está vacío.

---

## 4. Por qué casi nunca vas a poder probarlo con audiencia

`304` lo dice con números y aquí solo hay que aplicarlo: en orgánico, la variación entre dos vídeos del
mismo tipo ronda los **±10 puntos** de retención sin que hayas cambiado nada. Un efecto que afecta al
1,6 % del metraje no produce diferencias de diez puntos. Traducción directa:

> **No vas a poder medir el efecto de un efecto.** Para diferencias pequeñas harían falta más de treinta
> vídeos por grupo, y no los tienes.

Lo que sí puedes hacer, y es lo honesto:

- **Decidir los efectos por criterio** (`471`, `473`) y dejar de discutirlos.
- **Gastar la capacidad de experimentar en lo que sí mueve diez puntos**: el gancho, la duración, el
  formato (`304`).
- **Si vas a pagar por muestra**, que sea en pauta y para probar ganchos, no destellos. Y ahí la
  mecánica es la de las skills de anuncios, no la de esta.

---

## Errores frecuentes

1. **Atribuir a un efecto una subida de retención.** También recortaste, cambiaste la música y publicaste
   otro día (`304`).
2. **Meter un efecto donde la curva se cae.** El hueco no se tapa: se arregla con contenido.
3. **Dar por bueno un efecto sin comprobar que llega.** El grano que exportaste no es el que se ve.
4. **Poner `-loglevel error` al medir.** `psnr` no imprime nada y parece que falló (`472`).
5. **Confiar en un efecto de detalle fino** en una plataforma que recomprime.
6. **Probar efectos en orgánico.** No hay muestra para diferencias tan pequeñas.
7. **Repetir aquí el análisis de creativos de pauta.** Eso vive en las skills de Meta y TikTok.
8. **Mirar la curva sin bajar al fotograma.** El porcentaje no dice qué pasó; `366` sí.
9. **No anotar los «no era el efecto».** Es el resultado más frecuente y el que más discusiones ahorra.
10. **Creer que el efecto puede hacer importante un momento** que no lo es. Solo puede señalarlo.
11. **Subir la fuerza de los efectos cuando la retención baja.** Es la reacción instintiva y la peor:
    ahora tienes un vídeo aburrido y ruidoso.

---

## Relacionado

- `301` — leer una curva de retención: el método completo. **Ahí, no aquí.**
- `300` — qué medir y qué ignorar.
- `366` — del porcentaje al fotograma culpable.
- `304` — experimentar con método: cuánta muestra hace falta y por qué esto casi nunca se puede probar.
- `302`, `303` — diagnosticar un vídeo que falló y uno que funcionó.
- `428` — **el efecto que se rompe en la compresión**: el módulo que posee esta pregunta, con el criterio
  del codificador y la medida por `YDIF`. `446` — qué ruido sí sobrevive.
- `472` — el arnés A/B del que sale la tabla de supervivencia de arriba.
- `471` — dónde se ponen los efectos, que se decide por criterio y no por curva.
- `423` — el efecto que no se ve; `424` — el efecto que tapa un problema. Los dos casos en los que la
  respuesta a «¿sube la retención?» es que el efecto no debería estar.
- `93` — compresión sin perder calidad: por qué la alta frecuencia no sobrevive.
- `facebook_ads_lushows/68-creative-analytics`, `.../39-volumen-y-fatiga-creativa`,
  `.../17-framework-de-testing`, `.../37-hooks-los-primeros-3-segundos` — **rendimiento de creativos en
  pauta**. Todo lo de anuncios pagados vive ahí.
- `tiktok_ads_lushows/68-creative-analytics`, `.../49-testing-de-hooks-y-angulos` — lo mismo para TikTok.
