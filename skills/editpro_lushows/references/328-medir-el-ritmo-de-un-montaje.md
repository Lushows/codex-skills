# 328 — Diagnosticar un montaje que "se siente plano": medir el ritmo real y leerlo

**Qué resuelve:** "se siente plano" no es un diagnóstico, es un síntoma. El módulo `27` te da doce causas
posibles de lentitud; este te da el **instrumento** para saber cuál de ellas tienes, sobre un video ya
montado, en dos minutos y sin opinar. Al final tienes una salida de texto que describe el ritmo de un video
completo y seis firmas que te dicen qué hacer con ella.

---

## 1. De dónde salen los datos: tres fuentes, tres calidades

### Fuente A — El draft de CapCut (verdad absoluta)

Si el proyecto es tuyo, no hace falta detectar nada: la lista de cortes está escrita en el archivo.

```bash
jq -r '.tracks[] | select(.type=="video") | .segments[] |
  "\(.target_timerange.start/1000000)\t\(.target_timerange.duration/1000000)"' \
  draft_content.json | sort -n | awk '{print $2}' > dur.txt
```

**Úsala siempre que puedas** (`111`, `113`). Trabaja sobre una copia; nunca reformatees el draft original.

### Fuente B — Detección de escena (aproximación, con una trampa grande)

Para videos ajenos, o cuando el proyecto se perdió:

```bash
V=reel.mp4
UMBRAL=0.30
ffmpeg -hide_banner -i "$V" -filter:v "select='gt(scene,$UMBRAL)',showinfo" -f null - 2> esc.txt
grep -o "pts_time:[0-9.]*" esc.txt | cut -d: -f2 > t.txt
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$V")
awk -v dur="$DUR" 'BEGIN{p=0}{print $1-p; p=$1} END{print dur-p}' t.txt | awk '$1>0.15' > dur.txt
```

> ### ⚠️ La trampa que invalida la mitad de las mediciones que verás por ahí
>
> **La detección de escena no ve un jump cut sobre el mismo encuadre.** El detector compara un fotograma
> con el anterior; si es la misma persona, en el mismo sitio, con la misma luz, y solo cambió la posición
> de la boca y las manos, la diferencia no supera el umbral. Justo ese es tu corte más frecuente: medido
> con `scene=0.3`, un reel tuyo de 9 planos puede reportar 4 y la mediana sale al doble de la real.

Cómo se calibra, en vez de aceptar el número por fe:

```bash
# Cuántos cortes detecta a distintos umbrales
for U in 0.15 0.20 0.25 0.30 0.40 0.50; do
  N=$(ffmpeg -hide_banner -i "$V" -filter:v "select='gt(scene,$U)',showinfo" -f null - 2>&1 \
      | grep -c "pts_time")
  echo "umbral $U → $N cortes"
done
```

Y el conteo de referencia, hecho a ojo pero en frío, con la hoja de contactos (`17`):

```bash
ffmpeg -hide_banner -y -i "$V" -vf "fps=5,drawtext=text='%{pts\:hms}':fontcolor=yellow:fontsize=20:\
box=1:boxcolor=black@0.7:x=4:y=4,scale=200:-1,tile=10x6" -frames:v 1 -q:v 2 contactos.jpg
```

A 5 fotogramas por segundo no se te escapa ningún plano de más de 0,2 s. Cuentas los cortes en la imagen y
**eliges el umbral cuyo conteo más se acerque**. En material de bar con jump cuts suele caer entre 0,12 y
0,20, y ahí ya se cuelan falsos positivos por movimiento brusco: por eso se cruza, no se confía.

### Fuente C — A mano

Veinte planos se cuentan en la hoja de contactos en tres minutos, y es más fiable que un umbral mal
calibrado.

---

## 2. El script

```bash
#!/bin/bash
# ritmo.sh — lee el ritmo de un montaje.  Uso:  ritmo.sh dur.txt [fps]
# dur.txt = una duración de plano por línea, EN ORDEN de aparición.
F="$1"; FPS="${2:-30}"
[ -z "$F" ] && { echo "uso: ritmo.sh dur.txt [fps]"; exit 1; }
sort -n "$F" > /tmp/dur_ord.txt
awk -v fps="$FPS" '
FILENAME ~ /dur_ord/ { o[++m]=$1; next }
{ d[++n]=$1; total+=$1 }
function pc(p,  i){ i=int(m*p); return o[(m*p==i)?i:i+1] }
END{
  p25=pc(0.25); p50=pc(0.50); p75=pc(0.75); disp=p75/p25;
  printf "\n=== CIFRAS ===\nplanos %d en %.1f s | MEDIANA %.2f s (%.0f fotogramas)\n", n,total,p50,p50*fps;
  printf "p25/p75 %.2f/%.2f s | DISPERSION %.2f (sano 2,5-4,5) | cortes/min %.1f\n", p25,p75,disp,(n-1)/total*60;
  printf "min/max %.2f/%.2f s | max = %.1fx la mediana\n\n=== SECUENCIA ===\n", o[1],o[m],o[m]/p50;
  for(i=1;i<=n;i++){
    bar=""; k=int(d[i]/o[m]*40+0.5); if(k<1)k=1; while(length(bar)<k) bar=bar "#";
    c = (d[i]<p50*0.70) ? "R" : ((d[i]>p50*1.40) ? "L" : "N");   # Rapido / Normal / Lento
    patron = patron c;
    printf "%3d %s %5.2fs %-41s %s\n", i,c,d[i],bar,(i>1?sprintf("x%.2f",d[i]/d[i-1]):"");
  }
  printf "\npatron: %s\n\n=== VEREDICTO ===\n", patron;
  nR=gsub(/R/,"R",patron); nL=gsub(/L/,"L",patron);
  if(disp<1.8)     print "[!] METRONOMO: dispersion", sprintf("%.2f",disp), "-> 323";
  if(nR/n<0.15)    print "[!] SIN RAFAGA: solo", nR, "rapidos de", n, "-> 322";
  if(o[m]/p50<2.0) print "[!] SIN JERARQUIA: el plano mas largo no destaca -> 323";
  if(nL==0)        print "[!] SIN RESPIRO: ningun plano largo -> 323";
  if(p50>3.6)      print "[!] ARRASTRA: mediana", sprintf("%.2f s",p50), "-> 320";
  if(p50<1.2)      print "[!] ATROPELLADO: mediana", sprintf("%.2f s",p50);
  if(match(patron,/NNNNNN/)) print "[!] ZONA MUERTA en la posicion", RSTART, "-> 323";
  if(match(patron,/RRRL/)||match(patron,/RRRRL/)) print "[ok] RUPTURA en la posicion", RSTART;
}' /tmp/dur_ord.txt "$F"
```

Salida real sobre `0.90 2.30 2.80 2.40 1.10 0.90 0.80 4.60 2.90`:

```
=== CIFRAS ===
planos 9 en 18.7 s | MEDIANA 2.30 s (69 fotogramas)
p25/p75 0.90/2.80 s | DISPERSION 3.11 (sano 2,5-4,5) | cortes/min 25.7
min/max 0.80/4.60 s | max = 2.0x la mediana

=== SECUENCIA ===
  1 R  0.90s ########
  2 N  2.30s ####################                      x2.56
  3 N  2.80s ########################                  x1.22
  4 N  2.40s #####################                     x0.86
  5 R  1.10s ##########                                x0.46
  6 R  0.90s ########                                  x0.82
  7 R  0.80s #######                                   x0.89
  8 L  4.60s ########################################  x5.75
  9 N  2.90s #########################                 x0.63

patron: RNNNRRRLN
=== VEREDICTO ===
[ok] RUPTURA en la posicion 5
```

Y el mismo script sobre `2.1 2.0 2.2 2.0 2.1 2.0 2.2 2.1` — un metrónomo de manual:

```
patron: NNNNNNNN
[!] METRONOMO: dispersion 1.05 -> 323
[!] SIN RAFAGA: solo 0 rapidos de 8 -> 322
[!] SIN JERARQUIA: el plano mas largo no destaca -> 323
[!] SIN RESPIRO: ningun plano largo -> 323
[!] ZONA MUERTA en la posicion 1 -> 323
```

`RNNNRRRLN` cuenta la historia entera en nueve letras: arranque corto, cuerpo estable, ráfaga de tres,
ruptura, cierre. **Ese patrón es lo que hay que aprender a leer.**

---

## 3. Las seis firmas de un montaje plano

| Firma en el patrón | Qué es | Arreglo |
|---|---|---|
| `NNNNNNNN` | metrónomo puro | acorta tres seguidos y alarga uno → `323` |
| `NNNNNNNNL` | todo igual y un solo largo al final | mete una ráfaga antes del largo → `322` |
| `RLRLRLRL` | alternancia mecánica | agrupa: `RRRLLNN` en vez de alternar → `321` §3 |
| `RRRRRRRR` | ráfaga infinita | no hay ancla; alarga 2 planos con la carga real → `320` |
| `LLNNNNNN` | arranque lento | corta lo de antes del gancho → `27` causa 1 |
| `NNNNLNNNN` con L enorme | el plano-ladrillo | mira ese plano: casi seguro es toda la lentitud |

La firma sana, para comparar: **`RNNN RRR L N`** — arranque, cuerpo, ráfaga, ruptura, cierre.

---

## 4. Las tres mediciones cruzadas

El ritmo de corte es una de las capas. Si el patrón sale sano y el video sigue sintiéndose plano, el
problema está en otra:

### Cruce 1 — ¿Hay movimiento dentro de los planos?

Un patrón perfecto sobre nueve planos estáticos sigue siendo un video muerto. Saca la curva de movimiento
como en `324` §4 y resúmela:

```bash
awk '{s+=$2; n++; if($2<1.0) q++}
     END{printf "movimiento medio: %.2f | fotogramas casi quietos: %.0f%%\n", s/n, q/n*100}' curva.tsv
```

Más del 40% de fotogramas casi quietos: el problema no es el corte, es que no pasa nada dentro de los
planos (`22`, `201`, `203`).

### Cruce 2 — ¿El texto corre a otra velocidad?

Ver `326` §5. Si más del 60% de los cambios de texto coinciden con cortes, tienes un solo reloj y el video
se siente mecánico aunque las duraciones estén bien.

### Cruce 3 — ¿Hay huecos de habla?

```bash
ffmpeg -hide_banner -i reel.mp4 -af "silencedetect=noise=-35dB:d=0.7" -f null - 2>&1 | grep silence_start
```

Un hueco de 0,8 s se siente como cuatro, y es la causa de lentitud más frecuente que **no** aparece en el
patrón de duraciones.

---

## 5. Comparar contra una referencia

La medición sola no dice si un número es bueno; la comparación sí. Pasa por el script tres reels tuyos que
funcionaron y tres ajenos buenos (`305`), y guarda de cada uno `MEDIANA`, `DISPERSION` y `patron`.

Con seis referencias ya tienes tu propio rango, medido sobre tu contenido, y deja de importarte lo que diga
cualquier artículo. **Ese archivo vale más que este módulo.** Guárdalo en el diario (`306`).

Aviso honesto sobre los videos ajenos: solo puedes medir el corte final. Un reel con 3 millones de vistas
puede tenerlas por el tema, no por el montaje. La medición te da su gramática, no su resultado.

---

## 6. De la medición a la decisión

Orden de intervención, de más barato a más caro:

1. **Un solo plano-ladrillo** (max > 3× mediana): recórtalo. Suele resolver la sensación completa.
2. **Huecos de silencio** de más de 0,7 s: quítalos. Cinco minutos.
3. **Falta de ráfaga** (`nR/n < 0,15`): busca tres planos consecutivos que puedan bajar a 0,8–1,1 s.
4. **Falta de ruptura** (sin `L` después de `RRR`): alarga el plano del mensaje a 2,5× la ráfaga.
5. **Texto sincronizado al 100%**: desfasa 3 fotogramas la mayoría. Media hora.
6. **Metrónomo total**: remontaje de la segunda mitad. Es el caso caro; agota 1–5 antes de decidirlo.

**Vuelve a medir después de cada cambio.** Cambiar un plano cambia el ritmo de sus vecinos.

---

## Errores comunes

1. **Medir con detección de escena sin calibrar el umbral.** En material de jump cuts te devuelve la mitad
   de los cortes y todas las conclusiones salen mal.
2. **No cruzar el conteo contra la hoja de contactos.** Es el único control de calidad que tiene la
   detección automática y cuesta un comando.
3. **Usar el draft original de CapCut en vez de una copia**, u olvidar el primer y el último plano: la
   detección devuelve *cambios*, no planos. Ver `111`.
4. **No filtrar los intervalos menores a 0,15 s.** Los destellos contaminan el p25 y con él la dispersión.
5. **Diagnosticar solo con la mediana.** No distingue un metrónomo de un montaje con arquitectura. Por eso
   está el patrón.
6. **Creer que un patrón sano garantiza un video bueno.** El ritmo es una capa. Si dentro de los planos no
   pasa nada, el patrón no salva nada.
7. **Ignorar los silencios.** Un hueco de audio no aparece en las duraciones de plano y es de las causas más
   frecuentes de "se siente lento".
8. **Comparar tu reel contra una película o contra otro formato.** Compara contra tus propios reels.
9. **Deducir causalidad de un reel ajeno que funcionó.** Mediste su gramática, no la razón de su resultado.
10. **Remontar el video entero antes de probar los arreglos baratos.** El 80% de las veces era un plano.
11. **Medir una vez y no volver a medir después de arreglar.** Cambiar un plano cambia el ritmo de sus
    vecinos.

---

## Checklist

- [ ] Sé de qué **fuente** salieron mis duraciones (draft, detección calibrada o conteo a mano)
- [ ] Si usé detección, **calibré el umbral** y lo crucé con la hoja de contactos
- [ ] Filtré intervalos menores a 0,15 s e incluí primer y último plano
- [ ] Tengo las cifras: **mediana, p25/p75, dispersión, cortes/min, max/mediana**
- [ ] Tengo el **patrón** en letras R/N/L y lo leí
- [ ] Contrasté el patrón contra las **seis firmas** de montaje plano
- [ ] Crucé con la **curva de movimiento**, el **reloj del texto** (`326`) y los **silencios** > 0,7 s
- [ ] Tengo un archivo de **referencias** con la gramática de mis propios reels que funcionaron
- [ ] Intervine de lo barato a lo caro y **volví a medir** después de cada cambio
