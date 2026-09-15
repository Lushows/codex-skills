# 472 — La prueba A/B de un efecto

> **Esta prueba no mide si el efecto vende. Mide si el efecto merece su plaza.** El `470` te dio cinco
> plazas. Aquí se decide cuál de los candidatos se queda en una de ellas, con dos archivos, cuatro
> números y un criterio escrito **antes** de mirarlos.

**Frontera, y es estrecha.** El **instrumento** —`utime`, PSNR, SSIM, megabytes— es `420`. La
**magnitud por familia de efecto** (`signalstats`, `YAVG`, `SATAVG`, `YDIF`) es `421`. El **coste en
render y en atención** es `422`. Los **umbrales de retirada** son `429`. Nada de eso se reconstruye
aquí. Lo que aporta este módulo es lo de arriba: **el emparejamiento A/B y el protocolo de decisión** —
el mismo que `429` invoca para probar una retirada.

Y la otra frontera, la de siempre: `304` mide **en la audiencia**; esto mide **en el archivo**. Primero
`472` descarta lo que no está; después `304` prueba lo que sí está.

---

## 1. Por qué emparejado y no en tabla

`420` mide un efecto contra la nada y produce una tabla de candidatos. Sirve para inventariar. No sirve
para elegir, porque en una tabla todos los efectos parecen razonables por separado.

La prueba A/B hace otra cosa: **renderiza la pieza real dos veces, con y sin ese eslabón, y compara las
dos salidas entre sí.** Cambia una sola cosa y la cambia sobre tu material, no sobre un clip de
laboratorio. Es la misma disciplina de variable única de `304`, aplicada a un archivo en vez de a una
audiencia.

---

## 2. El arnés

```bash
#!/bin/bash
# ab.sh — prueba A/B de UN efecto. A = sin efecto, B = con efecto.
SRC="$1"; FX="$2"
[ -z "$FX" ] && { echo "uso: ab.sh fuente.mp4 'filtro de ffmpeg'"; exit 1; }

t0=$(date +%s%N)
ffmpeg -hide_banner -loglevel error -y -i "$SRC" \
  -c:v libx264 -crf 20 -preset medium -pix_fmt yuv420p -an A.mp4
tA=$(( ($(date +%s%N)-t0)/1000000 ))

t0=$(date +%s%N)
ffmpeg -hide_banner -loglevel error -y -i "$SRC" -vf "$FX" \
  -c:v libx264 -crf 20 -preset medium -pix_fmt yuv420p -an B.mp4
tB=$(( ($(date +%s%N)-t0)/1000000 ))

SA=$(stat -c%s A.mp4); SB=$(stat -c%s B.mp4)

# ⚠️ psnr y ssim IMPRIMEN EN NIVEL 'info'. Con -loglevel error no sale NADA
#    y parece que el comando fallo. Aqui NO se pone -loglevel. Ver 420 y 432.
P=$(ffmpeg -hide_banner -i A.mp4 -i B.mp4 -lavfi psnr -f null - 2>&1 | grep -o "average:[0-9.]*" | tail -1)
S=$(ffmpeg -hide_banner -i A.mp4 -i B.mp4 -lavfi ssim  -f null - 2>&1 | grep -o "All:[0-9.]*"     | tail -1)

printf "%-22s %s\n" "psnr (A vs B)" "$P"
printf "%-22s %s\n" "ssim (A vs B)" "$S"
printf "%-22s %d ms  ->  B %+d ms (%+d%%)\n" "render" "$tA" "$((tB-tA))" "$(( (tB-tA)*100/tA ))"
printf "%-22s %d B -> %d B (%+d%%)\n" "peso comprimido" "$SA" "$SB" "$(( (SB-SA)*100/SA ))"
```

**La trampa, comprobada otra vez aquí:** con `-loglevel error` el filtro `psnr` devuelve **cero bytes**.

```
$ ffmpeg -hide_banner -loglevel error -i A.mp4 -i B.mp4 -lavfi psnr -f null - 2>&1 | wc -c
0
```

No falla: su salida va al nivel `info` y la acabas de silenciar. Está documentada en `420` y en `432`, y
se sigue cayendo en ella porque `-loglevel error` es lo normal en un script de render. En el resto del
arnés sí va, porque ahí lo que quieres es silencio.

**Trampa de sintaxis:** con `-vf` no puedes referirte a `[0:v]`. Un glow se escribe
`split[a][b];[b]gblur=sigma=8[g];[a][g]blend=...`. Si escribes `gblur=sigma=8[b];[0:v][b]blend=...`,
ffmpeg contesta *«Simple filtergraph was expected to have exactly 1 input and 1 output»*, que no
menciona el problema real.

---

## 3. Tres efectos medidos, y lo que confirman

Mismo clip de 6 s a 1080×1920 y 30 fps, `crf 20 preset medium`, un efecto por pasada:

| Efecto | Filtro | PSNR | SSIM | Render | Peso |
|---|---|---|---|---|---|
| **Grano** | `noise=alls=9:allf=t+u` | 43,57 dB | 0,9866 | +152 % | **+55 %** |
| **Glow** | `split[a][b];[b]gblur=sigma=8[g];[a][g]blend=all_mode=screen:all_opacity=0.18` | 29,07 dB | 0,9903 | −9 % | −3 % |
| **Viñeta** | `vignette=angle=PI/6` | 20,62 dB | 0,9625 | +60 % | +0 % |
| Glow + grano | los dos encadenados | 28,99 dB | 0,9801 | +32 % | +54 % |

Lo primero que hay que decir es que **esto no descubre nada nuevo: confirma `420` en otro clip.** Allí
`noise=alls=6` dio **43,08 dB / SSIM 0,9643 / +73 % de peso**; aquí `noise=alls=9` da **43,57 dB /
0,9866 / +55 %**. Dos fuentes distintas, dos dosis distintas, el mismo retrato: **el grano es el efecto
que por PSNR «casi no existe» y por bitrate es el más caro de todos.** Cuando una medida se repite en
material distinto, deja de ser una anécdota.

Y la lectura de las otras dos:

**La viñeta es el mejor negocio.** PSNR 20,62 dB —el cambio más grande de los tres— con **+0 % de
peso**. Oscurecer esquinas es exactamente lo que a un códec le gusta: menos detalle que guardar. (Su
dosis correcta y su medida sobre gris están en `444`, que es donde vive ese efecto.)

**El glow adelgaza el archivo.** −3 %, porque desenfocar quita alta frecuencia. Y su SSIM es el más alto
de los tres (0,9903): cambia el brillo sin tocar la estructura, que es justo lo que se le pide.

---

## 4. La columna de la que no te puedes fiar

En esta máquina, la **misma** orden A —idéntica, sin efecto— tardó **25,0 / 36,4 / 41,8 / 51,2 s** en
cuatro pasadas. Por eso el glow marca −9 %, que es imposible: añadir trabajo no puede ser más rápido.

Esto es exactamente lo que advierte `422`: el reloj se multiplica por diez sin que el comando cambie, y
**la unidad correcta para comparar efectos entre sí es `utime`, no `rtime`**:

```bash
ffmpeg -hide_banner -benchmark -i base.mp4 -vf "$FX" -f null - 2>&1 | grep '^bench'
# bench: utime=4.578s stime=0.094s rtime=4.712s
```

Usa el arnés de arriba para PSNR, SSIM y peso —que son deterministas— y saca el coste de render con
`-benchmark`. Si aun así trabajas con el reloj, **solo hazle caso cuando la diferencia sea enorme**,
como el +152 % del grano.

---

## 5. El criterio se escribe antes

Igual que en `304`, y por el mismo motivo: si decides después, siempre te das la razón.

```
Efecto:     grano sobre la mezcla final
Hipotesis:  integra los recortes de archivo con los renders limpios
Coste que acepto:  hasta +15% de peso y hasta +40% de utime
Descarto si:       pasa de +30% de peso, o si al ponerlas lado a lado
                   no distingo cual es cual en un movil
```

Ese último renglón es el que más descartes produce y es gratis:

```bash
ffmpeg -hide_banner -y -i A.mp4 -i B.mp4 -filter_complex \
  "[0:v]scale=540:-1[a];[1:v]scale=540:-1[b];[a][b]hstack" -frames:v 1 comparar.png
```

Si no sabes cuál es cuál mirando esa imagen en un móvil, el efecto no existe para el espectador por
mucho que exista en el PSNR. El grado formal de esa situación —y sus umbrales duros— es `423`.

---

## 6. Cuándo NO hace falta correr esto

- El efecto ya tiene ficha con costes medidos (`478`): se consulta, no se vuelve a medir.
- Estás decidiendo *dónde* va, no *si* va. Eso es `471`, y se decide con el guion.
- Estás retirando un eslabón de la cadena: el protocolo es el mismo, pero los disparadores y el
  procedimiento son `429`.

---

## Errores frecuentes

1. **Poner `-loglevel error` en la medición.** `psnr` y `ssim` imprimen en `info`: no sale nada y parece
   que falló.
2. **Referirse a `[0:v]` dentro de `-vf`.** El error de ffmpeg no menciona el problema real.
3. **Decidir con el reloj de pared.** Aquí la misma orden varió de 25 a 51 s. Para comparar, `utime`.
4. **Medir con distinto CRF en A y en B.** Entonces no mides el efecto, mides el códec.
5. **Creer que PSNR alto es bueno.** PSNR alto significa «apenas cambia nada»: por encima de 50 dB el
   efecto se retira sin discusión (`423`).
6. **Quedarse solo con PSNR o solo con SSIM.** El grano engaña al primero; un cambio de gamma, al segundo.
7. **Ignorar el peso.** El grano sube el archivo entre un 55 % y un 73 % según la dosis.
8. **Escribir el criterio después de ver los números.** El error de `304` con otra ropa.
9. **Medir sobre un clip que no se parece a tu material.** El grano sobre un fondo plano y sobre una
   textura no cuestan lo mismo.
10. **Saltarse la comparación visual.** Los números dicen que cambia; el ojo dice si importa.
11. **Confundir esto con un test de audiencia.** Esta dice si el efecto está; `304` dice si sirve.
12. **Medir y no escribirlo.** Lo vas a volver a medir dentro de tres meses (`478`).

---

## Relacionado

- `420` — **un efecto es una hipótesis**: el instrumento, los cuatro números y cómo se leen. Esta prueba
  lo usa; no lo sustituye.
- `421` — la magnitud específica de cada familia de efecto, cuando PSNR y SSIM no bastan.
- `422` — coste en render y en atención: por qué `utime` y no el reloj.
- `423` — el efecto que no se ve, con sus umbrales duros.
- `429` — cuándo quitar un efecto: los seis disparadores, y el protocolo de retirada que invoca este.
- `428`, `446` — si el efecto sobrevive a la entrega. Ahí, no aquí.
- `444` — la viñeta, medida como corresponde (sobre gris, no sobre material).
- `304` — experimentar con método: la prueba que sí mide en la audiencia. Va **después**.
- `369` — comparar dos vídeos sin engañarse.
- `478` — dónde se guarda el resultado de esta medición.
