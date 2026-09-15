# 321 — Cadencia: cortes por minuto, la mediana y por qué la varianza manda

**Qué resuelve:** todo el mundo describe el ritmo de un video con un solo número —"corta cada 2 segundos"—
y ese número es casi siempre el promedio. El promedio es la peor estadística posible para describir un
montaje, y este módulo explica por qué, qué medir en su lugar, y qué valores concretos buscar en un reel
vertical de negocio local.

Al final tienes tres números que describen un montaje mejor que cualquier adjetivo: **mediana, dispersión
y cortes por minuto**. Los tres se sacan con un comando.

---

## 1. Los cuatro números y para qué sirve cada uno

Toma la lista de duraciones de todos los planos de un video. De ahí salen cuatro cosas:

| Número | Qué es | Para qué sirve de verdad |
|---|---|---|
| **Media** | suma / cantidad | Casi para nada. Un solo plano de 8 s te destruye la media de un reel |
| **Mediana (p50)** | el valor del medio | **El pulso real.** El plano típico del video |
| **Dispersión (p75/p25)** | cuánto se abre el abanico | **Si el video tiene arquitectura o es un metrónomo** |
| **Cortes por minuto** | cortes / duración × 60 | Comparar contra otros videos y contra tu propio historial |

### Por qué la media miente

Reel real de 22 segundos, 8 planos:

```
1,2 · 1,4 · 1,1 · 2,8 · 3,0 · 1,3 · 2,2 · 9,0     → media = 2,75 s   mediana = 1,8 s
```

La media dice 2,75 s. **Siete de los ocho planos duran menos que eso.** El video no se siente como 2,75;
se siente rapidísimo con un ladrillo de 9 segundos al final. La media describe un video que no existe.

La mediana dice 1,8 s, que sí es el plano típico. Y la dispersión (p75 ≈ 2,9 / p25 ≈ 1,25 = **2,3**) te
dice que hay abanico. Los tres juntos describen el video; ninguno solo lo hace.

**Regla dura: en montaje nunca reportes media. Reporta mediana.** Las duraciones de plano son una
distribución sesgada a la derecha —muchos planos cortos, pocos larguísimos— y en distribuciones sesgadas
la media es un número decorativo.

---

## 2. Tu cadencia real

De tus 51 proyectos salen dos números duros:

| Medida | Tu valor | Qué implica |
|---|---|---|
| **Mediana de plano** | **2,93 s** | ≈ **20,5 cortes por minuto** de cadencia típica |
| **Percentil 25** | **1,5 s** | 1 de cada 4 planos tuyos es "rápido" |
| p50 / p25 | 1,95 | tu cuartil rápido corre al doble de velocidad que tu plano típico |

Traducción práctica para un reel de 22 segundos con esa gramática: **entre 7 y 8 planos**, de los cuales
**2 deberían estar por debajo de 1,5 s**. Si armaste un reel de 22 s con 5 planos de 4,4 s cada uno, no
estás haciendo tu estilo: estás haciendo otro video.

Y ojo con una confusión que vale la pena resolver aquí: el módulo `20` habla de un pulso de cambio visual
de 1,5–2,0 s, y tu mediana de plano es 2,93 s. **No se contradicen.** Un cambio visual no es solo un corte:
también lo es un punch-in (`22`), una rampa de velocidad (`201`), la entrada de un bloque de texto (`46`).
Tú metes cambio *dentro* del plano. Por eso tu plano puede durar 2,93 s y tu pulso ser de 1,7 s.

> Corolario útil: si un plano tuyo se pasa de 3 s, tienes dos salidas —cortarlo, o **meterle un cambio
> interno**. La segunda suele ser mejor porque no rompe continuidad. Ver `22` y `201`.

---

## 3. Por qué la varianza importa más que la media

Este es el corazón del módulo.

Un montaje con mediana 2,0 s y todos los planos entre 1,9 y 2,1 s **se siente peor** que un montaje con
la misma mediana y planos entre 0,7 y 6,0 s. El primero es un metrónomo; el segundo tiene arquitectura.

La razón es de percepción, no de gusto: **un intervalo perfectamente regular deja de dar información al
cabo de tres o cuatro repeticiones.** El cerebro aprende el patrón, lo predice, y deja de gastar atención
en él. La regularidad se vuelve fondo. Es exactamente el mismo motivo por el que dejas de oír el
ventilador de la nevera.

La varianza es lo que impide que el patrón se aprenda. Y más importante: **la varianza es dónde vive el
significado.** Un plano corto no significa nada por sí solo; significa *rápido* porque los de al lado son
más largos. Un plano de 5 s no es lento en abstracto: es lento **después de una ráfaga**. Ver `323`.

### Lo que dice la investigación, y lo que no dice

Hay un hallazgo real y pertinente. Cutting, DeLong y Nothelfer (Cornell, *Psychological Science*, 2010,
"Attention and the Evolution of Hollywood Film") midieron la secuencia de duraciones de plano de 150
películas de Hollywood entre 1935 y 2005. Encontraron dos cosas: que las duraciones se volvieron
progresivamente **más correlacionadas con las de sus vecinas**, y que el espectro de potencia de esa
secuencia se fue acercando a un patrón **1/f** — el mismo tipo de fluctuación que se observa en las series
de tiempos de reacción humanos y en muchos procesos naturales. Su hipótesis: una estructura temporal 1/f
puede acoplar mejor la atención del espectador a la narración.

Qué se puede sacar de ahí honestamente:

- ✅ **La secuencia importa, no solo el promedio.** Los planos vecinos se parecen entre sí y los bloques
  varían entre bloques. Eso es una estructura, y es medible.
- ✅ **Es evidencia de que la industria convergió a eso sin proponérselo**, lo cual sugiere que funciona.
- ❌ **No es una receta para un reel de 22 segundos.** El estudio es sobre largometrajes de 90–150 minutos
  con miles de planos. En 8 planos no se puede estimar un espectro de potencia: no hay datos suficientes.
- ❌ **No demuestra causalidad con retención.** Muestra una convergencia histórica y propone un mecanismo.

Lo que sí se traslada al formato corto, y es lo operativo:

> **Los planos parecidos van juntos y los bloques se diferencian entre sí.** No alternes corto-largo-corto-
> largo. Haz **grupos**: tres cortos seguidos, después dos largos, después uno muy corto.

Esa es la diferencia entre varianza con forma y varianza al azar, y es lo que un video "con ritmo" tiene y
un video "picado" no.

---

## 4. El índice de dispersión: un número para saber si eres un metrónomo

Define esto y úsalo siempre:

```
dispersión = p75 / p25
```

Es adimensional (no cambia si el video entero es más rápido o más lento), robusto (no lo mueve un plano
raro) y se calcula con dos percentiles.

| Dispersión | Diagnóstico | Qué hacer |
|---|---|---|
| **< 1,8** | **Metrónomo.** Todos los planos duran casi lo mismo | Alarga dos planos y acorta dos. Ver `323` |
| **1,8 – 2,5** | Poco abanico. Correcto en un tutorial, plano en un reel | Mete una ráfaga o un respiro |
| **2,5 – 4,5** | **Zona sana** para reel vertical | Nada. Verifica que el abanico esté *agrupado*, no al azar |
| **4,5 – 7,0** | Mucho contraste. Puede ser correcto si es a propósito | Confirma que los largos son respiros y no grasa |
| **> 7,0** | Casi siempre hay un plano-ladrillo | Búscalo: es el que hace que el video se sienta lento (`27`) |

**Estos umbrales son heurísticos**, calibrados contra tu corpus y contra práctica corriente de formato
corto. No hay un estudio público que publique rangos de dispersión para reels, y quien te dé uno con
decimales probablemente se lo inventó. Úsalos como semáforo, no como ley.

---

## 5. Sacar los cuatro números con un comando

Detección de cortes por escena, y estadística con `awk`. (El módulo `328` desarrolla esto a fondo,
incluidas las trampas de la detección automática — que son serias en tu estilo, porque un jump cut sobre
el mismo encuadre puede no ser detectado.)

```bash
V=reel.mp4
UMBRAL=0.30

# 1. Tiempos de cambio de escena
ffmpeg -hide_banner -i "$V" -filter:v "select='gt(scene,$UMBRAL)',showinfo" -f null - 2> esc.txt
grep -o "pts_time:[0-9.]*" esc.txt | cut -d: -f2 > cortes.txt

# 2. Duraciones de plano (incluyendo el primero y el último)
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$V")
awk -v dur="$DUR" 'BEGIN{p=0} {print $1-p; p=$1} END{print dur-p}' cortes.txt \
  | awk '$1>0.15' | sort -n > dur.txt

# 3. Los cuatro números
awk -v dur="$DUR" '
{d[NR]=$1; s+=$1}
END{
  n=NR;
  p25=d[int(n*0.25)+ (n*0.25==int(n*0.25)?0:1)];
  p50=d[int(n*0.50)+ (n*0.50==int(n*0.50)?0:1)];
  p75=d[int(n*0.75)+ (n*0.75==int(n*0.75)?0:1)];
  printf "planos      : %d\n", n;
  printf "media       : %.2f s   (ignórala)\n", s/n;
  printf "MEDIANA     : %.2f s\n", p50;
  printf "p25 / p75   : %.2f s / %.2f s\n", p25, p75;
  printf "DISPERSION  : %.2f  (sano 2,5-4,5)\n", p75/p25;
  printf "cortes/min  : %.1f\n", (n-1)/dur*60;
  printf "min / max   : %.2f s / %.2f s\n", d[1], d[n];
}' dur.txt
```

El filtro `$1>0.15` descarta detecciones espurias de menos de 5 fotogramas, que casi siempre son destellos
o movimiento brusco, no cortes.

### La verdad exacta, si el proyecto es tuyo

Para tus propios reels no hace falta adivinar: el proyecto de CapCut tiene la lista de cortes escrita.
Ver `111` y `113`.

```bash
jq -r '.tracks[] | select(.type=="video") | .segments[] |
  (.target_timerange.duration/1000000)' draft_content.json | sort -n > dur.txt
```

Eso es **ground truth**: no detecta nada, lee lo que hiciste. Úsalo siempre que puedas y deja la detección
de escenas para videos ajenos (`305`).

---

## 6. Qué hacer con el resultado

| Lo que ves | Diagnóstico | Acción |
|---|---|---|
| Mediana > 3,5 s | El video arrastra | Recorta salidas de ciclo (`320` §2) antes de cortar más |
| Mediana < 1,2 s | Atropellado; nada se entiende | Alarga los planos con carga. Los de revelación no bajan de 0,8 s |
| Dispersión < 1,8 | Metrónomo | `323` — mete un plano largo después de una ráfaga |
| p25 > 2,0 s | No tienes cuartil rápido | Te falta una ráfaga. Busca 3 planos seguidos que puedan ir a 0,8–1,2 s |
| Máximo > 3 × mediana | Hay un ladrillo | Ve a ese plano. Casi seguro es toda tu sensación de lentitud |
| Cortes/min > 40 en un reel de 30 s | Es un videoclip, no un mensaje | Si hay algo que entender, no cabe. Ver `329` |

---

## Errores comunes

1. **Reportar la media.** Un solo plano largo la corrompe. En montaje, mediana siempre.
2. **Perseguir un número de cortes por minuto.** Los cortes por minuto son el *resultado* de decidir cada
   ciclo bien, no el objetivo. Ver `329`.
3. **Creer que más varianza es siempre mejor.** Varianza al azar es un video incoherente. La varianza
   tiene que estar **agrupada**: bloques rápidos, bloques lentos.
4. **Alternar corto-largo-corto-largo.** Es un patrón tan predecible como todos iguales, solo que con dos
   pasos en vez de uno. El cerebro lo aprende igual de rápido.
5. **Medir el ritmo con detección de escenas en un video de jump cuts.** Sobre el mismo encuadre, el
   detector no ve el corte y te reporta un montaje mucho más lento del que hiciste. Ver `328`.
6. **Comparar tu dispersión contra la de una película.** Un largometraje tiene miles de planos y otro
   contrato con el espectador. Compárate contra tus propios reels.
7. **Citar el estudio de Cutting como si dijera "tu reel debe tener estructura 1/f".** No lo dice, y en 8
   planos ni siquiera se puede calcular.
8. **Ignorar el mínimo y el máximo.** Los dos extremos suelen contener el problema entero, y no aparecen
   en la mediana.
9. **No contar el primer y el último plano.** La detección de escenas te da los *cambios*; el primer plano
   va desde 0 y el último hasta el final. Si no los agregas, tu mediana está sesgada.
10. **Contar como corte cualquier destello.** Filtra los intervalos por debajo de ~0,15 s antes de calcular
    nada, o tu p25 será basura.
11. **Medir el corte exportado con música y creer que la música no afecta.** La música no cambia los
    números, pero sí cambia la percepción: un montaje "plano" con la música correcta puede estar bien. Mide
    con datos, decide con oído (`24`).

---

## Checklist

- [ ] Tengo la lista de duraciones de plano, sacada del **draft de CapCut** si el proyecto es mío
- [ ] Si usé detección de escenas, verifiqué el conteo contra la hoja de contactos (`17`)
- [ ] Filtré los intervalos menores a 0,15 s
- [ ] Incluí el **primer** y el **último** plano en la lista de duraciones
- [ ] Reporté **mediana**, no media
- [ ] La mediana está entre 1,5 y 3,5 s (tu zona: alrededor de 2,9 s)
- [ ] La **dispersión p75/p25** está entre 2,5 y 4,5
- [ ] Al menos **1 de cada 4 planos** está por debajo de 1,5 s
- [ ] La varianza está **agrupada en bloques**, no repartida al azar ni alternando
- [ ] Revisé el plano más largo y sé por qué es el más largo
- [ ] Ningún número de este módulo me hizo cortar un momento emocional que funcionaba
