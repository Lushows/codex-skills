# 420 — Un efecto es una hipótesis

Cuando añades `vignette=PI/5.6` a una cadena, estás afirmando algo: *«esto concentra la mirada en el
centro»*. Cuando pones `noise=alls=6`, afirmas *«esto le quita el plástico a la imagen»*. Cuando
dejas `eq=saturation=1.02`, afirmas *«esto reanima el color»*.

Son tres afirmaciones sobre el mundo. Dos se comprueban en un minuto con ffmpeg. La tercera, como vas
a ver en `423`, es falsa: `eq=saturation=1.02` deja el fotograma con **SSIM 0,999988** contra el
original. Nueve nueves. Ni el ojo ni el codificador se enteran de que existe, y sin embargo se
ejecuta 1.586 veces en un episodio de 63 segundos.

Este bloque (420–429) trata los efectos como se tratan las hipótesis: se enuncian, se miden, y el que
no pasa la medida se retira. `56` es la lista negra **cualitativa** —qué se ve barato y por qué—, y
`460–469` hará la versión medida de esa lista. Aquí se construye el instrumental.

> **Frontera.** `directorcreativo_lushows` DECIDE el look (la marca quiere grano de archivo, quiere
> ese azul). `editpro` lo MIDE y lo EJECUTA. Si la discusión es «¿qué estética?», no es este bloque.
> Si es «¿esta cadena está haciendo lo que creemos?», sí lo es.

---

## 1. La forma de una hipótesis de efecto

Un efecto mal enunciado no se puede refutar. «Le da más vida» no se mide. La forma útil tiene tres
partes:

| Parte | Enunciado inútil | Enunciado medible |
|---|---|---|
| **Qué cambia** | «le da vida» | sube la saturación media del cuadro |
| **Cuánto** | «un poco» | SATAVG de 78 a 92 |
| **Dónde se nota** | «en todo» | en el tercio central, en los planos de archivo |

Enunciada así, la hipótesis tiene un experimento obvio: mide SATAVG antes y después. Si pasa de 78 a
79,4 tu hipótesis era falsa —no en su dirección, sino en su **magnitud**, que es donde casi siempre
fallan.

### Las cuatro hipótesis que se repiten

1. **«Separa»** — el efecto distingue un elemento de su fondo. Se mide con el escalón de luminancia y
   de contraste entre las dos regiones (`390`–`393`).
2. **«Unifica»** — hace que material de orígenes distintos parezca del mismo sitio. Se mide con la
   **dispersión** de YAVG y SATAVG entre planos (`427`).
3. **«Dirige la mirada»** — concentra atención. Se mide con la caída de luminancia del borde al
   centro (`444`).
4. **«Da textura»** — rompe la limpieza digital. Se mide con YDIF (diferencia entre fotogramas
   consecutivos) y con el peso codificado (`440`, `446`).

Si tu efecto no cae en ninguna de las cuatro, la primera pregunta no es cómo medirlo: es qué hace.

---

## 2. El arnés completo

Éste es el instrumento de todo el bloque. Mide, sobre el mismo material: coste de cómputo, distancia
al original en dos métricas y coste en bitrate.

```bash
#!/usr/bin/env bash
# medir.sh - un efecto, cuatro numeros
IN=base.mp4

fila () {
  N="$1"; F="$2"
  # 1) COSTE: utime = tiempo de CPU del proceso. Inmune a que la maquina este ocupada.
  U=$(ffmpeg -hide_banner -benchmark -i "$IN" -vf "$F" -f null - 2>&1 \
      | grep -o 'utime=[0-9.]*' | head -1 | cut -d= -f2)
  # 2) DISTANCIA: el original contra si mismo filtrado. Ojo al split (seccion 4).
  P=$(ffmpeg -hide_banner -i "$IN" -filter_complex \
      "[0:v]split=2[a][b];[a]$F[a2];[a2][b]psnr" -f null - 2>&1 \
      | grep -o 'average:[0-9.a-z]*' | head -1 | cut -d: -f2)
  S=$(ffmpeg -hide_banner -i "$IN" -filter_complex \
      "[0:v]split=2[a][b];[a]$F[a2];[a2][b]ssim" -f null - 2>&1 \
      | grep -o 'All:[0-9.]*' | head -1 | cut -d: -f2)
  # 3) BITRATE: lo que el efecto le cuesta al codificador
  ffmpeg -hide_banner -loglevel error -y -i "$IN" -vf "$F,format=yuv420p" \
      -c:v libx264 -crf 20 -preset veryfast -an "o_$N.mp4"
  MB=$(awk -v s="$(stat -c%s o_$N.mp4)" 'BEGIN{printf "%.2f",s/1048576}')
  printf "%-14s | %6s | %-9s | %-8s | %7s\n" "$N" "$U" "$P" "$S" "$MB"
}

printf "%-14s | %6s | %-9s | %-8s | %7s\n" efecto utime PSNR SSIM MB@20
fila nada      "null"
fila mi_efecto "vignette=PI/5.6"
```

La fila `nada` **no es opcional**: es la línea base. El coste de un efecto es la **diferencia** contra
ella, no el total (ver `422`), y el peso sin efecto es contra lo que se compara el peso con efecto.

---

## 3. 🔴 La trampa que cuesta una tarde: `-loglevel error`

**Los filtros de medida de ffmpeg —`psnr`, `ssim`, `astats`, `volumedetect`, `ebur128`,
`signalstats`, `blackdetect`— imprimen su resultado en nivel `info`.** Con `-loglevel error` no
imprimen **nada**, el comando devuelve 0, y parece que la medición falló o que el efecto no cambió
nada.

Medido hoy, mismo comando, mismo archivo:

```bash
# CON -loglevel error: silencio absoluto, codigo de salida 0
$ ffmpeg -hide_banner -loglevel error -i base.mp4 \
    -filter_complex "[0:v]split=2[a][b];[a]eq=saturation=1.10[a2];[a2][b]psnr" -f null -
$                                  # <- nada. Ni una linea.

# SIN -loglevel (el defecto es 'info'):
$ ffmpeg -hide_banner -i base.mp4 \
    -filter_complex "[0:v]split=2[a][b];[a]eq=saturation=1.10[a2];[a2][b]psnr" -f null - 2>&1 | grep PSNR
[Parsed_psnr_2 @ ...] PSNR y:inf u:40.923547 v:55.116614 average:48.542753 min:47.976056 max:48.966689
```

La confusión es especialmente cruel porque `-loglevel error` es lo correcto en el resto del pipeline
—el `motor.py` del canal documental lo usa en todos sus renders— y uno lo copia por inercia al
comando de medición.

**Regla:** en cualquier comando cuyo propósito sea **medir**, no toques el nivel de registro. Como
mucho `-hide_banner`, que solo quita la cabecera de compilación. Y captura por **stderr**: casi toda
la salida de ffmpeg sale por ahí, así que el `2>&1` no es opcional.

```bash
# Lo que se hace
ffmpeg -hide_banner -i x.mp4 -vf signalstats,metadata=print -f null - 2>&1 | grep YAVG
# Lo que NO
ffmpeg -loglevel error -i x.mp4 -vf signalstats,metadata=print -f null - | grep YAVG
```

---

## 4. La segunda trampa: comparar un archivo consigo mismo

Para medir un efecto quieres enfrentar **el original** contra **el original filtrado**. Son el mismo
archivo dos veces, y ahí empieza el lío. Lo verificado hoy sobre **ffmpeg 8.1.2**:

| Forma | Resultado medido |
|---|---|
| `-vf "eq=...[a];[a][0:v]psnr"` | ❌ `Simple filtergraph ... had 2 input(s) and 1 output(s)` |
| `-filter_complex "[0:v]eq=...[a];[a][0:v]psnr"` | ✅ funciona: ffmpeg inserta el `split` solo |
| `-filter_complex "...[n];[n]eq=...[a];[a][n]psnr"` | ✅ funciona, también con auto-split |
| `-filter_complex "[0:v]split=2[a][b];[a]eq=...[a2];[a2][b]psnr"` | ✅ **la forma que se escribe** |

Tres cosas que hay que saber:

1. **`-vf` no puede tener dos entradas.** Es un grafo *simple*: una entrada, una salida. En el momento
   en que la medición necesita dos ramas, el comando es `-filter_complex`. Éste es el error que sí te
   para en seco, y el mensaje lo dice con todas las letras.
2. **`split` explícito, siempre.** ffmpeg 8.x inserta el `split` por su cuenta cuando reutilizas una
   etiqueta, pero eso es comportamiento de versión, no contrato: en builds anteriores la misma línea
   fallaba con `Filter has an unconnected output`. En un arnés que va a correr en otra máquina —o
   dentro de dos años— el `split=2` explícito es lo que hace que el comando siga significando lo
   mismo.
3. **`split` no copia píxeles.** Duplica referencias al mismo cuadro. No paga coste medible: la fila
   `nada` con y sin `split` sale igual dentro del ruido de medida (±0,3 s de `utime`).

---

## 5. Cómo se lee un PSNR y un SSIM de efecto

Los dos números dicen cosas distintas, y esa diferencia **es el diagnóstico**:

- **PSNR** mide error cuadrático: castiga los cambios grandes de nivel. Un cambio global de gamma lo
  desploma aunque la imagen siga igual de nítida.
- **SSIM** mide estructura: luminancia local, contraste local y correlación. Castiga lo que rompe el
  detalle e ignora un desplazamiento uniforme de brillo.

| PSNR | SSIM | Qué es | Medido hoy |
|---|---|---|---|
| alto | alto | el efecto casi no existe | `eq=saturation=1.02`: **52,88 dB / 0,999988** |
| bajo | alto | cambio global de nivel, estructura intacta | `eq` del motor: **23,00 dB / 0,9775** |
| alto | bajo | textura añadida, niveles intactos | `noise=alls=6`: **43,08 dB / 0,9643** |
| bajo | bajo | el efecto rehizo la imagen | `gblur=sigma=20` |

La tercera fila es la más útil del bloque. Un PSNR de 43 dB significaría, en el mundo de la
compresión, «indistinguible». Pero el grano baja el SSIM a 0,964 y **encarece el archivo un 73%**
(1,17 → 2,02 MB al mismo CRF; ver `428`). Un efecto que por PSNR «no existe» le está costando al
codificador casi el peso de un archivo entero. Por eso ninguna métrica sola sirve.

**Referencia de PSNR entre antes y después de un efecto** —distinta de la de compresión, que vive en
`108`:

| PSNR antes↔después | Lectura |
|---|---|
| `inf` | el efecto es un `null`. Literalmente no tocó un píxel |
| **> 50 dB** | por debajo del umbral visible. Sospecha fuerte de efecto inútil (`423`) |
| 42–50 dB | cambio real pero menor. Compruébalo en móvil antes de defenderlo |
| 30–42 dB | cambio claro |
| < 30 dB | cambio fuerte. Si no lo esperabas, revisa la cadena |

**Un aviso sobre `y:inf`.** En la salida `PSNR y:inf u:40.92 v:55.11` el `inf` del canal Y significa
que la luminancia no cambió **en absoluto**: el efecto solo tocó croma. Es información, no un fallo.
El número que se compara entre filas es `average`.

---

## 6. El protocolo: cuatro preguntas por efecto

Antes de que un efecto entre en una plantilla de canal —donde se ejecutará en cada escena de cada
episodio para siempre— se responden cuatro preguntas, en este orden:

1. **¿Cambia algo?** `PSNR = inf` o `> 50 dB` → fuera, sin discusión (`423`).
2. **¿Cambia lo que dije que cambiaba?** Mide la magnitud que enunciaste, no una genérica (`421`).
3. **¿Cuánto cuesta?** En segundos de CPU y en megabytes (`422`).
4. **¿Sobrevive a la entrega?** Lo que la compresión de la red se lleva, no existe (`428`).

Un efecto que pasa las cuatro se queda. Uno que falla la primera se borra hoy. Los que fallan la
tercera o la cuarta son los interesantes: ahí se decide si se ajusta la dosis o se cambia de
herramienta.

---

## 7. El clip de calibración

Todo esto es inútil sobre un clip que no representa tu material:

```bash
# 4 segundos = 100 fotogramas a 25 fps. Suficiente para estadistica, corto para iterar.
ffmpeg -hide_banner -loglevel error -y -i escena_real.mp4 -t 4 \
  -c:v libx264 -crf 10 -preset veryfast -pix_fmt yuv420p base.mp4
```

Tres requisitos:

- **Material real, no `testsrc2`.** Los patrones sintéticos no tienen piel, ni cielos, ni grano de
  archivo: las tres cosas donde los efectos se rompen.
- **CRF 10 o mejor.** Si la base ya viene comprimida, mides el efecto **más** los artefactos de la
  fuente y el PSNR sale mentiroso.
- **Que contenga movimiento.** Un plano congelado esconde todo lo temporal: el grano que parpadea, el
  destello que salta, el `eval=frame` que nunca se evaluó.

---

## Errores frecuentes

- **`-loglevel error` en un comando de medición.** Silencio total y la conclusión equivocada: «el
  efecto no cambió nada». Es el error número uno de este bloque.
- **Olvidar `2>&1`.** ffmpeg escribe la medición por stderr. Sin redirigir, el `grep` no ve nada.
- **Usar `-vf` para una medición de dos ramas.** Necesita `-filter_complex`.
- **No poner la fila `nada` en la tabla.** Sin línea base, el `utime` y los megabytes no significan
  nada.
- **Enunciar la hipótesis después de ver el número.** Si mides primero y explicas después siempre
  encuentras una historia. Escribe qué esperas **antes** de correr el comando.
- **Quedarse solo con PSNR.** El grano da 43 dB —parecería nada— y cuesta +73% de peso.
- **Quedarse solo con SSIM.** Un cambio de gamma que altera toda la imagen puede dar SSIM 0,98.
- **Leer `y:inf` como error.** Significa que el efecto no tocó la luminancia. Es un dato.
- **Medir sobre `testsrc2`.** No tiene piel, y la piel es donde los efectos se caen.
- **Medir sobre un fotograma.** Los efectos temporales (`allf=t`, `eval=frame`) no existen en un PNG.
- **Comparar clips de duración distinta.** `psnr` empareja fotograma a fotograma; el resultado no
  significa nada si uno es más largo.
- **Medir con la máquina ocupada y usar `rtime`.** Medido hoy: el mismo decodificado dio **4,49 s** de
  `rtime` en reposo y **44,20 s** con otros renders corriendo. El `utime` apenas se movió. Para
  comparar efectos entre sí, `utime`.

---

## Checklist

- [ ] Escribí la hipótesis —qué cambia, cuánto, dónde— antes de medir.
- [ ] El clip base es material real, corto y de CRF 10 o mejor.
- [ ] El comando de medición **no** lleva `-loglevel error` y sí lleva `2>&1`.
- [ ] La comparación usa `-filter_complex` con `split=2` explícito.
- [ ] La tabla tiene fila `nada` como línea base.
- [ ] Tengo los cuatro números: `utime`, PSNR, SSIM y megabytes.
- [ ] Leí PSNR y SSIM juntos, no uno de los dos.
- [ ] El coste lo calculo como diferencia contra la línea base, no como total.
- [ ] Si PSNR es `inf` o mayor de 50 dB, el efecto sale de la cadena (`423`).
- [ ] Comprobé que sobrevive a la compresión de entrega (`428`).

---

## Relacionado

- `421` — qué magnitud medir para cada familia de efecto, y el arnés por familias
- `422` — coste en render y coste en atención, con el caso del canal documental
- `423` — el efecto que no se ve: cómo detectarlo y qué hacer con él
- `428` — lo que la compresión se lleva
- `108` — instrumental general de medición: ffprobe, signalstats, ebur128, blackdetect
- `102` — qué hace cada filtro de video y en qué orden van
- `56` — la lista negra cualitativa de efectos que se ven baratos
- `133` — verificación automática dentro de un pipeline
- `canales_lushows` — el motor del canal documental, de donde salen los números de este bloque
