# 20 — El pulso del video

**Qué resuelve:** cuando alguien dice "este video se siente lento" o "se siente atropellado", casi nadie
sabe decir por qué. Este módulo convierte esa sensación en un número que puedes medir, comparar y
corregir: **cuántos cambios visuales hay por segundo**. Con eso dejas de discutir gustos y empiezas a
arreglar el video.

---

## 1. Qué es el pulso

El **pulso** es la frecuencia con la que la imagen cambia. No es lo mismo que "cuántos cortes hay":
un cambio visual es **cualquier cosa que obligue al ojo a re-mirar la pantalla**.

Cuenta como cambio visual:

- Un corte de un plano a otro.
- Un **punch-in** (volver al mismo plano pero más cerrado — ver módulo `22`).
- Un inserto o **cutaway** (un plano de apoyo: las manos, el producto, la pantalla).
- La entrada de un bloque de texto grande en pantalla.
- Un movimiento fuerte dentro del plano (la persona se para, la cámara barre).
- Un cambio de color/look evidente (pasa a blanco y negro, entra un flash).

NO cuenta como cambio visual:

- Un subtítulo que avanza palabra por palabra (eso es lectura continua, no un evento).
- Un zoom lentísimo de fondo (el ojo no lo registra como novedad).
- Un cambio de música sin cambio de imagen.

> **Término nuevo — cutaway (plano de corte):** un plano corto que NO es el plano principal y que se mete
> encima para tapar un salto o mostrar de qué se habla. Si estás hablando de tu carta y aparece la carta
> dos segundos, eso es un cutaway.

---

## 2. El estándar 2026

Esto está verificado contra la práctica actual de contenido corto (agosto 2026):

| Pulso | Cómo se lee | Veredicto |
|---|---|---|
| Menos de 1,2 s por cambio | Ruido. El cerebro no alcanza a procesar y se rinde | ❌ mata retención |
| **1,5 – 2,0 s por cambio** | **Vivo, moderno, se sigue sin esfuerzo** | ✅ **objetivo** |
| 2,0 – 2,5 s por cambio | Aceptable si hay movimiento dentro del plano | ⚠️ zona de riesgo |
| Más de 2,5 s por cambio | Se siente lento. La gente pasa el dedo | ❌ cae retención |

**La meta operativa: 5 a 7 cambios visuales cada 10 segundos.**

Un dato que vale la pena tener en la cabeza: un video con texto dinámico y cortes frecuentes retiene
alrededor de **35% más** que un talking head estático (una persona hablando a cámara sin que nada
cambie). Ese 35% no lo compra ningún efecto bonito: lo compra el pulso.

### El matiz que casi nadie dice

En 2026 el péndulo se corrigió. Durante años se editó "lo más rápido posible" y en 2026 los creadores
grandes bajaron el ritmo, metieron respiros y les subió la retención. La conclusión honesta:

> **El pulso sirve a la historia, no al revés.** Cortar más rápido de lo que tu historia aguanta te baja
> la retención, no te la sube.

Traducido: 1,5–2 s es el objetivo **cuando hay algo que mostrar**. Si estás cortando cada 1,5 s pero los
tres planos son la misma cara desde el mismo ángulo, no ganaste pulso — ganaste mareo.

---

## 3. Cómo contar el pulso (a mano, en 3 minutos)

Método manual, sin herramientas raras:

1. Reproduce el video con un cronómetro al lado o con la línea de tiempo visible.
2. Cada vez que la imagen cambie, anota el segundo. Solo el segundo, no décimas.
3. Al terminar tienes una lista: `0, 1.8, 3.5, 5.0, 8.2, 8.9, 14.0 …`
4. Calcula: `duración total ÷ (número de cambios)` = **segundos por cambio**.

Ejemplo real:

```
Video de 32 s, 14 cambios visuales.
32 / 14 = 2,29 s por cambio  →  zona de riesgo, se siente lento.
Para llegar a 1,8 s necesitas: 32 / 1,8 = ~18 cambios. Faltan 4.
```

Ese número final ("faltan 4 cambios") es lo que convierte una queja en una tarea.

---

## 4. Cómo medirlo con ffmpeg (automático)

ffmpeg trae un detector de cambio de escena. No es perfecto — se pierde los punch-in suaves y a veces
marca de más cuando hay un flash — pero te da el mapa en segundos.

### Detectar los cortes y listarlos

```bash
ffmpeg -hide_banner -i entrada.mp4 -filter:v "select='gt(scene,0.3)',showinfo" -f null - 2> escenas.txt
```

`scene,0.3` es el umbral: 0.3 detecta cambios claros. Si tu video tiene planos muy parecidos entre sí,
baja a 0.15 y volverá a correr con más sensibilidad (también con más falsos positivos).

Los tiempos quedan en `escenas.txt` en líneas que dicen `pts_time:12.345`. Para dejar solo los números:

```bash
grep -o "pts_time:[0-9.]*" escenas.txt | cut -d: -f2 > tiempos.txt
```

### Contar los cambios y sacar el pulso

```bash
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 entrada.mp4)
N=$(wc -l < tiempos.txt)
echo "duracion=$DUR  cambios=$N"
awk -v d="$DUR" -v n="$N" 'BEGIN{printf "pulso = %.2f s por cambio\n", d/(n+1)}'
```

`n+1` porque el primer plano no genera evento de cambio pero sí es un plano.

### Ver dónde están los huecos

Lo que de verdad importa no es el promedio: es **el tramo más largo sin cambios**. Un video puede tener
un promedio bonito de 1,8 s y aun así perder gente porque hay un bache de 9 segundos en el medio.

```bash
awk 'NR>1{d=$1-p; if(d>2.5) printf "HUECO de %.1f s entre %.1f y %.1f\n", d, p, $1} {p=$1}' tiempos.txt
```

Eso te imprime exactamente en qué segundo se te duerme el video. Ahí es donde hay que meter un inserto,
un punch-in o un texto.

### Sacar una hoja de contactos del pulso

Ver el video como tira de imágenes deja el problema en evidencia sin reproducir nada:

```bash
ffmpeg -hide_banner -i entrada.mp4 -vf "fps=1,scale=240:-1,tile=10x4" -frames:v 1 pulso_grid.png
```

Un fotograma por segundo, en cuadrícula. Si ves diez cuadritos seguidos idénticos, ahí están tus diez
segundos muertos.

---

## 5. Cómo diagnosticar un video lento midiendo

Este es el procedimiento completo. No opines antes de tener estos cinco números.

| # | Medida | Cómo | Bandera roja |
|---|---|---|---|
| 1 | Pulso promedio | `duración / cambios` | > 2,5 s |
| 2 | Hueco más largo | script `awk` de arriba | > 4 s |
| 3 | Pulso de los primeros 3 s | contar a mano | < 2 cambios en 3 s |
| 4 | % del video que es un solo plano | ver la grilla | > 40% |
| 5 | Cambios en los últimos 5 s | contar a mano | 0 cambios |

**El más importante es el 3.** El arranque manda: si en los primeros 3 segundos la imagen no cambió al
menos dos veces, no importa lo bien montado que esté el resto — la mayoría ya se fue.

### Interpretación rápida

- **Promedio bien, huecos malos** → el video no es lento, tiene zonas muertas. Arréglalas puntualmente
  con insertos. No re-montes.
- **Promedio malo parejo** → falta cobertura. Necesitas más material: punch-ins, b-roll, texto.
- **Promedio bien pero se siente atropellado** → estás por debajo de 1,2 s, o cortas siempre al mismo
  tipo de plano. El problema no es la cantidad, es la variedad.

---

## 6. Cómo subir el pulso cuando no tienes más material

Este es el caso normal: grabaste una sola toma con el celular y ya. Se arregla igual.

| Recurso | Costo | Cuánto pulso agrega |
|---|---|---|
| **Punch-in** (mismo plano, 15% más cerrado) | cero, ya lo tienes | Alto — es tu segunda cámara (`22`) |
| Texto en pantalla con entrada golpeada | cero | Alto (`42`) |
| Inserto de foto del producto | una foto | Medio |
| Reencuadre lateral (mover el marco, no acercar) | cero | Medio |
| Flash / golpe de blanco de 2 frames | cero | Bajo, pero puntual |
| Cambio de look (a blanco y negro 1 s) | cero | Bajo — se gasta rápido |

El punch-in es el más barato que existe y por eso tiene módulo propio. Un ejemplo mínimo:

```bash
ffmpeg -hide_banner -i plano.mp4 -vf "scale=1242:2208,crop=1080:1920" -c:a copy plano_cerrado.mp4
```

Eso te da un plano 15% más cerrado que se lee como otra cámara. Intercalado con el original, duplicas
el número de cambios sin haber grabado un solo segundo extra.

---

## 7. El pulso no es parejo: la curva

Un video bien montado no tiene el mismo pulso de principio a fin. La forma que funciona:

```
0–3 s     PULSO ALTO      cambio cada 0,8–1,2 s   ← el gancho, aquí sí vale ser agresivo
3–10 s    PULSO OBJETIVO  cambio cada 1,5–2,0 s   ← se establece el ritmo
10–x s    RESPIRO         un plano de 3–4 s        ← una sola vez, en el punto de mayor interés
resto     PULSO OBJETIVO  cambio cada 1,5–2,0 s
final 3 s PULSO ALTO      cambio cada 1,0 s        ← el remate y el llamado a la acción
```

El respiro es contraintuitivo pero funciona: después de 10 segundos de estímulo constante, un plano que
se queda quieto **destaca**. Se usa exactamente donde está la frase más importante del video. Es la
diferencia entre un video que estimula y un video que comunica.

---

## 8. Casos donde el estándar NO aplica

Sé honesto con el cliente cuando toque:

- **Testimonio real de un cliente.** Cortarlo cada 1,5 s lo hace ver manipulado. Ahí el pulso baja a
  2,5–3 s y se compensa con texto y con punch-ins suaves.
- **Video de comida.** Un plano de la carne en la plancha aguanta 4 segundos porque el movimiento está
  dentro del plano. El pulso lo pone el chisporroteo, no el corte.
- **Podcast en video / entrevista larga.** Otro juego completamente: ahí el pulso ronda 4–8 s y lo que
  retiene es el contenido.
- **Video institucional / corporativo.** Pulso lento a propósito comunica solidez. Lo importante es que
  sea una decisión, no un descuido.

---

## Errores comunes

1. **Confundir "muchos cortes" con "buen ritmo".** Diez cortes al mismo plano desde el mismo ángulo no
   son pulso: son parpadeo. El pulso necesita **variedad**, no solo frecuencia.
2. **Optimizar el promedio y no ver los huecos.** El promedio miente. Un video con pulso 1,8 s puede
   tener un bache de 8 segundos que se lleva a la mitad de la audiencia.
3. **Dejar el arranque lento porque "ahí viene lo bueno".** No viene: la gente ya se fue. Los primeros
   3 segundos van más rápido que el resto, siempre.
4. **Cortar por debajo de 1,2 s "para que se vea dinámico".** Por debajo de ese umbral el cerebro deja
   de procesar y se defiende yéndose. Se ve dinámico y rinde peor.
5. **Contar los subtítulos palabra por palabra como cambios visuales.** No lo son. Si tu única "variedad"
   es el subtítulo, tu pulso real es cero.
6. **Meter cortes que parten palabras** por perseguir el número. Eso lo resuelve el módulo `23`
   (voz continua, imagen picada): la imagen puede cortar cuando quiera, la voz nunca se parte.
7. **Aplicar 1,5 s a un testimonio.** Le quita credibilidad. El estándar es para contenido construido,
   no para material que vende justamente por ser crudo.
8. **Fiarse solo del detector de escenas de ffmpeg.** Se pierde los punch-in y los cambios suaves. Úsalo
   como primera pasada y confirma con la grilla de fotogramas.

---

## Checklist

Antes de dar por bueno el ritmo de un video:

- [ ] Medí el **pulso promedio** con `duración ÷ cambios`, no lo estimé de memoria.
- [ ] Está entre **1,5 y 2,0 s por cambio** (o justifiqué por escrito por qué no).
- [ ] Corrí el detector de huecos: **ningún tramo supera 2,5 s sin cambio visual**.
- [ ] En los **primeros 3 segundos** hay al menos **2 cambios visuales**.
- [ ] Hay **al menos un respiro** deliberado (plano de 3–4 s) en el punto de mayor interés.
- [ ] Los cambios son **variados** (no diez punch-ins seguidos al mismo encuadre).
- [ ] En los **últimos 3 segundos** el pulso vuelve a subir para sostener el remate.
- [ ] Generé la **grilla de fotogramas** y no hay más de 3 cuadritos seguidos idénticos.
- [ ] Ningún corte parte una palabra (verificado contra la transcripción, ver `23`).
- [ ] Si el formato es testimonio, comida o corporativo, **ajusté el objetivo a propósito** y lo dejé
      dicho, en vez de aplicar el estándar a ciegas.
