# 326 — El ciclo de la imagen y el ciclo del texto: por qué no deben coincidir

**Qué resuelve:** tienes los cortes bien y el texto bien, cada uno por su lado, y el video igual se siente
mecánico. La causa casi siempre es la misma y es invisible hasta que te la señalan: **el texto cambia
exactamente cuando cambia la imagen**, en todos y cada uno de los cortes.

Este módulo es sobre las dos velocidades que corren en paralelo en un reel, la relación de fase entre
ellas, y por qué el momento en que las alineas es el recurso más potente que tienes.

> **Hermano de `374`.** Aquel módulo clasifica las cuatro relaciones (unísono, anticipación, retardo,
> contratiempo) y te dice cómo ejecutarlas en CapCut. Este añade lo que falta: **la técnica del texto que
> atraviesa la ráfaga** y **cómo medir la relación real de tu proyecto con datos**. Si vas a ejecutar,
> `374`. Si vas a diagnosticar, aquí. Y ojo con los porcentajes: no comparten denominador, lo explica §5.

---

## 1. Dos relojes, no uno

| | Ciclo de imagen | Ciclo de texto |
|---|---|---|
| Duración típica | **2,93 s** (tu mediana, `321`) | **0,9 s** por golpe (`46`) |
| Qué lo determina | la carga del plano (`320`) | la velocidad del habla, 2 palabras por golpe |
| Cuántos por reel de 25 s | 7–9 | 25–28 |

La relación es de aproximadamente **3 a 1**: por cada plano pasan unos tres golpes de texto.

```
IMAGEN   ├──────plano A──────┤├──────plano B──────┤├────plano C────┤
TEXTO    ├─t1─┤├─t2─┤├─t3─┤├─t4─┤├─t5─┤├─t6─┤├─t7─┤├─t8─┤├─t9─┤
```

Eso no es un problema a resolver. **Es la estructura.** Dos capas a velocidades distintas es lo que hace
que un reel de 25 segundos con 8 planos no se sienta como 8 fotos: el texto llena el espacio interior del
plano y le da pulso sin necesidad de cortar (`20`).

El error empieza cuando alguien decide "ordenarlo" y hace que cada bloque de texto empiece y termine con
su plano. Ahí tienes un solo reloj, corriendo a 2,93 s, y el video pierde la mitad de su energía.

---

## 2. Las tres relaciones de fase

Para cada corte de imagen, el texto puede estar en una de tres relaciones. Las tres son útiles y hacen
cosas distintas.

### A — Coincidencia (el acento)

El texto cambia **en el mismo fotograma** que la imagen.

**Qué produce:** un acento fuerte. Las dos capas golpean juntas y se siente como un énfasis, casi como un
golpe de percusión visual.

**Cuándo:** en el gancho, en la revelación, en el remate. **Dos o tres veces por reel, no más.** Si todos
tus cambios coinciden, ninguno es acento — es simplemente cómo funciona el video, y deja de significar
algo. La coincidencia es un recurso escaso; gástalo donde importa.

### B — Adelanto (el texto empuja)

El texto entra **2 a 5 fotogramas ANTES** del corte de imagen (0,07–0,17 s a 30 fps).

**Qué produce:** la sensación de que el texto *provocó* el corte. Es el efecto más "profesional" de los
tres y el más subutilizado. El ojo lee el cambio de texto, e inmediatamente después la imagen confirma. Se
siente causal.

**Cuándo:** en la mayoría de los cortes normales del cuerpo del video. Es tu ajuste por defecto.

### C — Retraso (el texto atraviesa)

El texto **sigue en pantalla** durante el corte y cambia mucho después, o entra 8+ fotogramas después del
corte.

**Qué produce:** cose los planos. Dos, tres o cuatro planos bajo un mismo bloque de texto se leen como
**una sola unidad de sentido**, aunque visualmente sean cuatro cosas distintas.

**Cuándo:** este es el truco grande, y tiene sección propia.

---

## 3. El truco: el texto que atraviesa la ráfaga

Esta es la técnica más valiosa del módulo y la que resuelve la tensión central del bloque 320–329.

El problema: quieres cortar rápido (energía) pero necesitas que se entienda una idea (comprensión). Cortar
rápido destruye la comprensión porque cada corte reinicia la atención.

La solución: **la idea vive en el texto, y el texto no corta.**

```
IMAGEN   ├─0,8s─┤├─0,9s─┤├─0,8s─┤├─1,0s─┤├────── 3,2 s ──────┤
TEXTO    ├──────── "esto te cuesta 40 mil al mes" ───────┤├─"y no lo sabías"─┤
                        ↑ un solo bloque, 3,5 s
```

Cuatro cortes rápidos, cuatro imágenes distintas, **una sola frase en pantalla**. El espectador recibe
energía visual y coherencia semántica al mismo tiempo, que es exactamente lo que un reel necesita y lo que
casi ningún reel amateur consigue.

Reglas para que funcione:

1. El texto tiene que ser **una unidad de sentido completa**, no dos palabras sueltas. Aquí es donde se
   rompe la regla de 2 palabras por golpe de `46`: durante la ráfaga, el texto se comporta como cartel, no
   como subtítulo cinético.
2. **Posición fija.** Si el texto se mueve entre planos, deja de ser el elemento estable y el efecto se
   pierde. Mismo tamaño, misma posición, mismo color a lo largo de toda la ráfaga.
3. Las imágenes de abajo tienen que ser **variaciones de lo mismo** (el mismo local desde 4 ángulos, el
   mismo producto en 4 momentos), no cuatro temas distintos. El texto une, no arregla incoherencia.
4. El texto **sale en la ruptura**, no antes. Cuando llega el plano largo (`323`), ahí cambia el texto: la
   coincidencia de los dos cambios en ese punto es el acento del video.

Y la operación inversa, igual de útil: **la imagen quieta con el texto cambiando**. Un plano de 3,5 s con
tres golpes de texto encima no se siente largo, porque el reloj rápido sigue corriendo. Es la forma más
barata de rescatar un plano bueno que dura demasiado.

---

## 4. La tabla de decisión

| Momento del video | Relación | Desfase |
|---|---|---|
| Gancho (0–2 s) | **Coincidencia** | 0 fotogramas |
| Cuerpo, corte normal | **Adelanto** | texto 2–5 fotogramas antes |
| Ráfaga / secuencia rápida | **Atraviesa** | un solo bloque sobre 3–5 planos |
| Entrada al plano de ruptura | **Retraso** | texto entra 8–12 fotogramas después del corte |
| Revelación / dato clave | **Coincidencia** | 0 fotogramas |
| Remate | **Coincidencia** | 0 fotogramas |
| Cierre / llamado a la acción | **Retraso** | texto entra ~0,4 s después, ya en el plano quieto |

Ese "retraso de 8–12 fotogramas" al entrar en el plano de ruptura merece un párrafo: si el texto entra a la
vez que el plano largo, el espectador tiene dos cosas nuevas que procesar simultáneamente y procesa mal las
dos. Dándole 0,3 s de aire, primero registra la imagen y después recibe el texto. **Es la diferencia entre
un cierre que se lee y uno que se pasa por encima.**

---

## 5. Medirlo en tu propio proyecto

El draft de CapCut tiene las dos pistas con sus tiempos. Se pueden cruzar (`111`, `113`).

```bash
# 1. Tiempos de corte de imagen (segundos)
jq -r '.tracks[] | select(.type=="video") | .segments[] |
  (.target_timerange.start/1000000)' draft_content.json | sort -n > cortes_img.txt

# 2. Tiempos de entrada de cada bloque de texto
jq -r '.tracks[] | select(.type=="text") | .segments[] |
  (.target_timerange.start/1000000)' draft_content.json | sort -n > cortes_txt.txt

# 3. Para cada entrada de texto: distancia al corte de imagen más cercano, en fotogramas
FPS=30
awk -v fps=$FPS 'NR==FNR{c[FNR]=$1; n=FNR; next}
{
  best=999;
  for(i=1;i<=n;i++){ d=$1-c[i]; if(d<0) d=-d; if(d<best){best=d; sd=$1-c[i]} }
  f=sd*fps;
  if(best*fps<1.0)      rel="COINCIDENCIA";
  else if(sd<0 && best*fps<=6)  rel="adelanto";
  else if(sd>0 && best*fps<=6)  rel="retraso corto";
  else                  rel="independiente";
  printf "texto en %6.2f s   desfase %+5.1f fotogramas   %s\n", $1, f, rel;
}' cortes_img.txt cortes_txt.txt
```

### Cómo leer el resultado

```bash
# Cuántos son coincidencia exacta
awk -v fps=30 'NR==FNR{c[FNR]=$1;n=FNR;next}
{best=999; for(i=1;i<=n;i++){d=$1-c[i]; if(d<0)d=-d; if(d<best)best=d}
 if(best*fps<1.0) k++} END{printf "coincidencias exactas: %d de %d (%.0f%%)\n", k, FNR, k/FNR*100}' \
 cortes_img.txt cortes_txt.txt
```

| Porcentaje de coincidencias | Diagnóstico |
|---|---|
| **> 60%** | ❌ **Un solo reloj.** El video se siente mecánico. Desfasa la mayoría 3 fotogramas |
| 25 – 50% | 🟡 Demasiadas. Deja solo las del gancho, la revelación y el remate |
| **8 – 20%** | ✅ Zona sana: 2–3 acentos en un reel de 25 s |
| < 5% | ⚠️ Ningún acento. El texto y la imagen corren sueltos y no hay énfasis en ninguna parte |

> **Cuidado con el denominador — y con comparar contra `374`.** Aquí el porcentaje es *sobre todos los
> bloques de texto del video*, y como el texto corre a 3× la velocidad de la imagen, la mayoría de sus
> entradas ni siquiera tiene un corte cerca (salen como "independiente"). En `374` los porcentajes son
> *sobre los bloques que sí están emparejados con un corte*, y ahí el unísono sube al 30–40%.
>
> Los dos números dicen lo mismo: si un tercio de tus textos cae cerca de un corte y de esos un 35% va al
> unísono, eso es ~12% del total — dentro de la zona sana de esta tabla. **Antes de alarmarte, comprueba
> cuál denominador estás mirando.**

---

## 6. El tercer reloj: la música

Hay un reloj más, y conviene nombrarlo aunque el módulo `24` lo desarrolle: el pulso de la música.

Lo importante para este módulo es la advertencia: **no alinees los tres relojes al mismo tiempo, salvo una
vez.** Cuando la imagen corta, el texto cambia y el golpe de la música cae todo en el mismo fotograma, eso
es el momento más fuerte que puedes construir en un video. Si lo haces en cada corte, no has construido un
momento fuerte: has construido un videoclip que se siente cuadriculado, y no queda dónde poner el acento.

Guarda la alineación triple para **un solo fotograma del reel**. Normalmente el remate.

---

## Errores comunes

1. **Hacer que cada bloque de texto empiece y termine con su plano.** Es la causa #1 del reel que se
   siente mecánico. Un solo reloj no es ritmo, es metrónomo.
2. **Creer que "desordenado" es lo mismo que "desfasado".** El desfase es de 2 a 5 fotogramas y es
   deliberado; no significa dejar el texto donde caiga.
3. **Gastar la coincidencia en cortes cualquiera.** Si coincide siempre, no acentúa nunca.
4. **Meter el texto y el plano de ruptura en el mismo fotograma.** Dos cosas nuevas a la vez se procesan
   mal las dos. Dale 8–12 fotogramas de aire al texto.
5. **Mover el texto de posición durante una ráfaga que atraviesa.** El texto es el ancla; si el ancla se
   mueve, no ancla nada.
6. **Usar 2 palabras por golpe dentro de una ráfaga.** Durante la ráfaga, el texto es cartel, no subtítulo:
   una frase completa, quieta.
7. **Unir con texto cuatro imágenes que no tienen nada que ver.** El texto cose planos parecidos; no
   arregla un montaje incoherente.
8. **Alinear imagen, texto y música en cada corte.** El momento máximo se usa una vez.
9. **Poner el texto encima sin comprobar la zona segura.** Todo este módulo es inútil si el texto queda
   debajo de los botones de la app (`45`, `98`).
10. **No verificar el desfase con datos.** Tres fotogramas no se ven reproduciendo; se ven en el JSON del
    proyecto o en la línea de tiempo con el zoom al máximo.
11. **Aplicar esto a subtítulos de accesibilidad.** Los subtítulos de transcripción siguen el habla y no se
    desfasan por gusto. Esto es para el texto de diseño (`40`, `41`).
12. **Comparar el porcentaje de este módulo contra el de `374` sin mirar el denominador.** Miden lo mismo
    sobre bases distintas y parecen contradecirse cuando no lo hacen.

---

## Checklist

- [ ] El texto y la imagen corren a **velocidades distintas** (aprox. 3 golpes de texto por plano)
- [ ] Ningún bloque de texto empieza y termina sistemáticamente con su plano
- [ ] Hay **2 o 3 coincidencias exactas** en todo el reel, y sé cuáles son y por qué
- [ ] Corrí el cruce de §5 y el porcentaje de coincidencias está entre **8% y 20%**
- [ ] Los cortes normales tienen el texto **2–5 fotogramas por delante**
- [ ] Si hay ráfaga, hay **un solo bloque de texto** atravesándola, quieto y en posición fija
- [ ] El texto del plano de ruptura entra **8–12 fotogramas después** del corte
- [ ] El texto del cierre entra en el plano quieto, no en el corte
- [ ] Imagen, texto y música se alinean **una sola vez** en todo el video
- [ ] Todo el texto está en zona segura y pasa la prueba de la uña (`98`)
