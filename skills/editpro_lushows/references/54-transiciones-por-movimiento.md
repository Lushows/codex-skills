# 54 — Transiciones por movimiento: el corte que no se ve

> Este es el nivel más alto del oficio en transiciones, y curiosamente el que menos filtros necesita.
> Aquí casi todo se resuelve **eligiendo el fotograma correcto**, no aplicando un efecto.

Las tres técnicas de este módulo son las que usan los editores de cine y los buenos editores de
publicidad. Ninguna es un preset. Todas se basan en la misma idea: **el ojo no nota un corte si en
ese instante ya está ocupado siguiendo un movimiento.**

---

## Por qué funciona (la parte que hay que entender)

Cuando algo se mueve en pantalla, tu atención está pegada a ese movimiento. En ese estado, tu cerebro
tolera un cambio de imagen enorme sin registrarlo como interrupción. Es el mismo mecanismo por el que
no ves el mundo emborronarse cuando giras la cabeza.

De ahí sale la regla:

> **Corta durante el movimiento, no en la quietud.**

Un corte entre dos planos quietos se ve. El mismo corte, hecho mientras un brazo baja o mientras la
cámara se desplaza, desaparece. No necesitas ninguna transición: necesitas el fotograma correcto.

---

## Técnica 1 — Corte por acción (el pan de cada día)

**Qué es:** una acción empieza en el plano A y termina en el plano B. La puerta se abre en general y
se termina de abrir en detalle. La mano coge el vaso en plano abierto y lo levanta en primer plano.

**Es la transición invisible más usada del cine.** Nunca la vas a notar, y por eso funciona.

### Cómo se hace bien

El error clásico es cortar cuando la acción **termina**. Se hace al revés:

1. Encuentra el fotograma donde la acción está **a un tercio de completarse** en el plano A.
2. Corta ahí.
3. En el plano B, empieza en el fotograma donde la acción está **un poco antes** de ese punto.

Ese solape de 2 a 4 fotogramas es lo que hace que el movimiento se sienta continuo. Si empalmas
exacto, se siente entrecortado; el ojo necesita un pelo de repetición para leerlo fluido.

```bash
# Plano A: la accion arranca en 1.40 y corto en 1.85 (a un tercio)
ffmpeg -y -i abierto.mp4 -ss 0 -to 1.85 -c:v libx264 -crf 18 -preset veryfast -pix_fmt yuv420p a1.mp4

# Plano B: empiezo 3 fotogramas ANTES del punto equivalente (0.62 - 0.10 = 0.52)
ffmpeg -y -i detalle.mp4 -ss 0.52 -to 3.0 -c:v libx264 -crf 18 -preset veryfast -pix_fmt yuv420p a2.mp4

printf "file 'a1.mp4'\nfile 'a2.mp4'\n" > lista.txt
ffmpeg -y -f concat -safe 0 -i lista.txt -c copy accion.mp4
```

### Cómo se encuentra el fotograma exacto

No lo adivines. Saca los fotogramas de la zona y míralos:

```bash
ffmpeg -y -i abierto.mp4 -ss 1.6 -to 2.1 -vsync 0 -q:v 2 frames_%03d.jpg
```

Ahora tienes 15 imágenes con el movimiento cuadro por cuadro. Eliges. Esto es lo que hace la
diferencia entre un corte que funciona y uno que casi funciona. Ver `15-medicion-exacta-de-cortes.md`.

### La medida del solape

| Velocidad de la acción | Solape recomendado |
|---|---|
| Lenta (alguien se sienta) | 4–6 fotogramas |
| Media (una mano coge algo) | 2–4 fotogramas |
| Rápida (un golpe, un lanzamiento) | 1–2 fotogramas |

En duda: **3 fotogramas**. Casi siempre acierta.

---

## Técnica 2 — Ocultar el corte con un objeto que barre el cuadro

**Qué es:** algo pasa muy cerca de la cámara y tapa el cuadro por completo durante 2 o 3 fotogramas.
En esos fotogramas negros (o de lo que sea el objeto), haces el corte. Del otro lado ya estás en otro
sitio.

Es el truco de las películas de superhéroes, de los videos de viaje y de casi todo lo que se ve
"caro" sin serlo.

### Qué sirve de objeto

- Una persona que camina cerca de la cámara.
- Un brazo que pasa.
- Un carro, una moto, una bicicleta.
- Una puerta que se cierra.
- La propia mano del que graba.
- Una columna, un poste, un árbol (con la cámara moviéndose).

**El requisito es uno solo:** que en algún fotograma tape el 100% del cuadro. Si tapa el 90%, se ve
el corte por el 10% que queda.

### Cómo se monta

```bash
# Encuentra el fotograma donde el objeto tapa todo
ffmpeg -y -i planoA.mp4 -ss 2.0 -to 2.5 -vsync 0 -q:v 2 tapa_%03d.jpg
# Miras las imagenes, eliges: supongamos que tapa_007.jpg es el fotograma 100% cubierto
# 2.0 + (7-1)/30 = 2.20

ffmpeg -y -i planoA.mp4 -to 2.20 -c:v libx264 -crf 18 -preset veryfast -pix_fmt yuv420p t1.mp4

# En el plano B haces lo mismo: encuentras donde SALE el objeto y empiezas ahi
ffmpeg -y -i planoB.mp4 -ss 0.87 -c:v libx264 -crf 18 -preset veryfast -pix_fmt yuv420p t2.mp4

printf "file 't1.mp4'\nfile 't2.mp4'\n" > lista.txt
ffmpeg -y -f concat -safe 0 -i lista.txt -c copy barrido_real.mp4
```

### Cuando no hay objeto en el plano B

Si solo tienes el objeto en el plano A, el corte se hace igual pero el plano B tiene que **empezar
con movimiento en la misma dirección**. La continuidad de dirección es la que salva el corte.

### La versión simulada (cuando no lo filmaron)

Se puede meter un objeto artificial: una sombra que pasa, un desenfoque de primer plano. Rara vez
queda bien y siempre se nota. **Es mejor pedirlo en el rodaje**: cuesta un take extra y resuelve una
transición imposible. Ver `170-briefing-de-rodaje-desde-la-edicion.md`.

---

## Técnica 3 — Match cut (el corte por semejanza)

**Qué es:** el plano A termina con una forma, un color, un movimiento o una composición, y el plano B
empieza con algo igual o casi igual. El ojo salta sin friccionar porque encuentra lo mismo del otro
lado.

Es la transición más elegante que existe y **no requiere ni un filtro**.

### Los cuatro tipos de coincidencia

| Coincide... | Ejemplo |
|---|---|
| **La forma** | Un plato redondo → la rueda de una moto → un reloj |
| **El movimiento** | Una mano que baja → un telón que baja → una persiana |
| **El color / la masa** | Una pared roja llena el cuadro → una salsa roja llena el cuadro |
| **La composición** | Una silueta a la izquierda del cuadro → otra silueta en el mismo sitio |

Los mejores match cuts combinan dos: misma forma **y** mismo movimiento.

### Cómo se busca uno de verdad

El match cut casi nunca se planea: **se encuentra en el material**. El método es:

1. Saca una hoja de contactos de todo el bruto (ver `17-hoja-de-contactos.md`):

```bash
ffmpeg -y -i bruto.mp4 -vf "fps=1/2,scale=320:-1,tile=6x6" contactos_%03d.jpg
```

2. Miras la lámina buscando **formas repetidas**. Círculos con círculos. Diagonales con diagonales.
3. Cuando encuentras dos, vas al fotograma exacto de cada uno.

Este paso vale la pena hacerlo siempre. En un bruto de 20 minutos suele haber dos o tres match cuts
esperando, y ninguno lo planeó nadie.

### Cómo se ajusta el fotograma

El match cut es **muy** sensible al fotograma. Un cuadro de diferencia y deja de funcionar. Se ajusta
extrayendo los fotogramas candidatos de los dos planos y comparándolos lado a lado:

```bash
ffmpeg -y -i planoA.mp4 -ss 3.10 -frames:v 1 -q:v 2 candA.jpg
ffmpeg -y -i planoB.mp4 -ss 0.00 -frames:v 1 -q:v 2 candB.jpg
```

Y si quieres verlos superpuestos para comprobar que las formas coinciden:

```bash
ffmpeg -y -i candA.jpg -i candB.jpg -filter_complex "[0:v][1:v]blend=all_mode=difference" diff.jpg
```

En `diff.jpg`, **lo negro es lo que coincide**. Si la forma clave sale negra, el match cut está bien
alineado. Si sale brillante, están desalineados: mueve un fotograma y repite.

Este truco del `blend=difference` es la forma objetiva de verificar un match cut. Verificado y
funciona.

### Cuándo ajustar la escala

A veces las formas coinciden pero de distinto tamaño. Se corrige escalando uno de los dos planos:

```bash
ffmpeg -y -i planoB.mp4 -vf "scale=iw*1.12:ih*1.12,crop=w=iw/1.12:h=ih/1.12:x=(iw-ow)/2:y=(ih-oh)/2" \
  -c:v libx264 -crf 18 -preset veryfast -pix_fmt yuv420p planoB_ajustado.mp4
```

Hasta un 20% de reescalado no se nota. Más allá empieza a verse el reencuadre.

---

## La jerarquía honesta

Si tuvieras que elegir en qué invertir tu tiempo:

1. **Corte por acción** — se usa docenas de veces por video, es invisible, cuesta encontrar el
   fotograma. **Máximo retorno.**
2. **Objeto que barre** — se usa 1 o 2 veces, resuelve saltos imposibles, requiere que esté filmado.
3. **Match cut** — se usa 0 o 1 vez, es memorable cuando sale, no se puede forzar.

Un editor que domina el corte por acción monta mejor que uno que sabe las 58 transiciones de `xfade`.

---

## Lo que tienes que pedir en el rodaje

Estas técnicas mueren si el material no las permite. Lo que hay que pedir (detalle en `170`):

- **Cada acción importante, filmada dos veces**: una en plano abierto y una en detalle, la acción
  completa las dos veces. Sin eso no hay corte por acción.
- **Un take con alguien pasando cerca de la cámara** al final de cada bloque. Es el objeto que barre.
- **Que dejen correr la cámara 2 segundos antes y después** de cada acción. El fotograma que necesitas
  siempre está justo fuera del recorte que hizo el que grabó.

---

## Errores comunes

- **Cortar cuando la acción termina.** El corte se ve. Se corta a un tercio del movimiento, no al
  final.

- **Empalmar sin solape.** El movimiento se siente entrecortado. Necesitas 2–4 fotogramas de
  repetición para que el ojo lo lea continuo.

- **Elegir el fotograma "a ojo" arrastrando la barra.** Saca los fotogramas a JPG y míralos. La
  diferencia entre un corte bueno y uno regular son dos cuadros.

- **Usar un objeto que tapa el 90%.** El corte se ve por el borde. Tiene que tapar el 100% en algún
  fotograma.

- **Cortar contra la dirección del movimiento.** Si en A algo va a la derecha y en B va a la
  izquierda, el ojo choca. La dirección se respeta. Ver `26-continuidad.md`.

- **Forzar un match cut que no está.** Si tienes que estirar mucho la semejanza, no es un match cut:
  es un corte raro. Se descarta sin dolor.

- **No verificar el match cut objetivamente.** El `blend=all_mode=difference` te dice en dos segundos
  si las formas coinciden. Úsalo.

- **Reescalar más del 20% para forzar la coincidencia.** Se nota el reencuadre y pierdes nitidez.

- **Ponerle una transición encima.** Si el corte por movimiento funciona, no lleva nada. Añadirle un
  fundido lo arruina: subraya justo lo que querías esconder.

---

## Checklist

- [ ] Antes de montar, revisé la hoja de contactos buscando match cuts en el material.
- [ ] Cada corte por acción está a un tercio del movimiento, no al final.
- [ ] Cada corte por acción tiene 2–4 fotogramas de solape.
- [ ] Los fotogramas de corte los elegí extrayendo imágenes, no arrastrando la barra.
- [ ] Si uso un objeto que barre, verifiqué que tapa el 100% del cuadro en algún fotograma.
- [ ] La dirección del movimiento se mantiene entre plano y plano.
- [ ] Si hay match cut, lo verifiqué con `blend=all_mode=difference` y las formas salen oscuras.
- [ ] Si escalé para ajustar, no pasé del 20%.
- [ ] Ninguno de estos cortes lleva transición encima.
- [ ] Anoté para el próximo rodaje qué faltó filmar (acción doble, objeto que pasa, colas de 2 s).
- [ ] Verifiqué el render final cuadro por cuadro en las zonas de corte (`98`).
