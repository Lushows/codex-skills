# 82 — Personajes y mascotas en video

**Qué resuelve:** tienes un personaje de marca (una mascota, un avatar ilustrado, un muñeco) y no sabes
qué hacer con él en un video más allá de "ponerlo al final junto al logo". Este módulo lo convierte en
lo que de verdad es: **una herramienta de montaje**. El personaje tapa cortes que no cuadran, marca sin
que parezca publicidad, y mete humor donde el guion se puso plano. También dice cuándo estorba, que es
la mitad del valor.

---

## 1. El personaje NO es un adorno, es un recurso de montaje

La forma equivocada de pensarlo: "tenemos una mascota, hay que meterla para que se vea la marca".
Resultado: un dibujo quieto en una esquina durante 30 segundos. Nadie lo mira. No hace nada.

La forma correcta: **el personaje es una capa que resuelve problemas concretos del montaje.** Tiene tres
trabajos, y en cada aparición debería estar haciendo al menos uno:

| Trabajo | Qué resuelve | Ejemplo |
|---|---|---|
| **Tapa** | un corte que salta, un error de continuidad, un tramo sin b-roll | entra por el borde justo en el corte feo y lo esconde |
| **Marca** | que el video sea reconociblemente tuyo sin poner un logo gigante | aparece 3 veces en 30 s, siempre igual |
| **Ríe / reacciona** | un tramo de información plana que pierde retención | reacciona a lo que dice el presentador |

Si una aparición no hace ninguna de las tres, sobra. Bórrala.

---

## 2. La ley que rige todo esto: real para lo tangible, ilustración para lo abstracto

Es la ley 6 de la skill y aquí es donde vive.

- **Tangible** (existe y se puede filmar): el producto, la comida, el local, las manos, la persona.
  **Va filmado. Siempre.** Poner una ilustración de un plato de comida cuando tienes el plato es un
  crimen: la ilustración no da hambre y la foto sí (`153`).
- **Abstracto** (no existe físicamente): un concepto, un miedo, un proceso invisible, una emoción, "lo
  que pasa en tu cabeza cuando ves la factura". **Ahí entra el personaje.** Es lo único que puede
  dibujar lo que no se puede filmar.

> El personaje es tu forma de mostrar lo invisible. Si lo usas para mostrar lo visible, estás cambiando
> oro por plástico.

---

## 3. La diferencia que lo cambia todo: encima, no en vez de

Esto es lo mismo que dice el módulo `80`, pero aplicado al personaje es donde más se siente, y por eso
se repite.

Un caso real: se necesitaba meter un personaje ilustrado en un video de alguien hablando a cámara.

- **Versión A (mala):** corte a la lámina del personaje a pantalla completa, dos segundos, y de vuelta.
  Se sintió **muerta**. La ilustración era buena, pero al sacar al humano de la pantalla, el video se
  detuvo. Se leyó como una diapositiva metida a la fuerza.
- **Versión B (buena):** el personaje **recortado** (ver `81`), superpuesto en la esquina inferior
  derecha, mientras el presentador seguía hablando. Se sintió **vivo y acoplado**: el personaje parecía
  estar en la escena.

Misma ilustración. Mismo segundo del video. La diferencia entera fue **inserto vs. capa**.

**Por qué funciona:** el cerebro lee la coexistencia como simultaneidad. Si los dos están en pantalla al
mismo tiempo, están en el mismo mundo. Si uno reemplaza al otro, son dos cosas distintas pegadas.

**Cuándo sí va a pantalla completa:** cuando el personaje **es** el contenido de ese momento — un chiste
visual que necesita toda la pantalla, un remate, un final de marca. Nunca "para explicar algo mientras
alguien habla".

---

## 4. Dónde ubicarlo

Las zonas, en vertical 1080x1920:

```
        +------------------------+
   y=0  |   zona de interfaz     |   <- nada aquí (0-260 px)
        +------------------------+
        |                        |
        |      LA CARA           |   <- nunca tapar (aprox. 380-1050)
        |                        |
        +------------------------+
        |   [PERSONAJE]          |   <- zona buena (1100-1500)
        +------------------------+
        |   subtitulos           |   <- nada aquí
        |   zona de interfaz     |   <- nada aquí (ultimos 380 px)
        +------------------------+
```

Las cuatro reglas de ubicación:

1. **Nunca sobre la cara.** Ni un pedacito. La cara es lo que retiene.
2. **Del lado hacia donde mira la persona.** Si el presentador mira a tu derecha, el personaje va a la
   derecha: parece que interactúan. Al otro lado parece que se ignoran.
3. **Apoyado en un borde**, no flotando en el centro del vacío. Un personaje que se asoma desde el borde
   inferior pertenece a la escena. Uno en el aire parece una calcomanía.
4. **Tamaño: entre el 25% y el 40% de la altura.** Más pequeño no se lee en un celular. Más grande
   compite con la persona.

```bash
# Personaje apoyado abajo a la derecha, encima de la zona de subtitulos
ffmpeg -i base.mp4 -i pj_alfa.png \
  -filter_complex "[1:v]scale=-1:620,format=rgba,\
fade=t=in:st=4.0:d=0.30:alpha=1,fade=t=out:st=7.2:d=0.30:alpha=1[pj];\
[0:v][pj]overlay=x=W-w-56:y=H-h-470:enable='between(t,3.95,7.55)'" \
  -map 0:a -c:a copy -c:v libx264 -crf 18 -pix_fmt yuv420p salida.mp4
```

620 px de alto sobre 1920 = 32% de la altura. `y=H-h-470` lo deja por encima de la zona de subtítulos.

---

## 5. Cómo entra y cómo sale (esto es el 80% del efecto)

Un personaje que aparece por fundido se ve como un fantasma de plantilla. Un personaje que **se asoma**
se ve vivo. Tres entradas que funcionan, en orden de calidad:

### a) Se asoma desde el borde (la mejor)

Sube desde abajo del cuadro con una curva que frena. Con sobre-impulso pequeño se ve todavía mejor
(ver `84`).

```bash
-filter_complex "[1:v]scale=-1:620,format=rgba[pj];\
[0:v][pj]overlay=x=W-w-56:\
y='st(0,clip((t-4.0)/0.45,0,1)); H - (H-(H-h-470))*(1-pow(1-ld(0),3))'\
:enable='gte(t,4.0)'"
```

Se lee: entre el segundo 4,0 y el 4,45 sube desde fuera de cuadro hasta su sitio, frenando al llegar.

### b) Aparece en un golpe de audio

Entra de un frame al otro, exactamente en un impacto sonoro (`76`). Bien hecho es lo más contundente
que hay. Mal hecho parece un error de render. La regla: **si entra duro, tiene que haber sonido**.

### c) Fundido con un pelín de escala

Aceptable como recurso secundario. Nunca como el único.

**Cómo sale:** casi siempre por donde entró y **más rápido de lo que entró** (entrada 0,45 s, salida
0,25 s). Lo que entra despacio y sale despacio se siente pesado.

---

## 6. Cuánto y cada cuánto

Números que funcionan en video social de 30–60 segundos:

| Duración del video | Apariciones | Duración de cada una |
|---|---|---|
| 15 s | 1, máximo 2 | 1,5 – 2,5 s |
| 30 s | 2 – 3 | 1,5 – 3 s |
| 60 s | 3 – 4 | 2 – 3,5 s |

**La regla de los 3 segundos:** una aparición de más de 3,5 segundos deja de ser un evento y se vuelve
decorado. A partir de ahí el ojo lo ignora y solo te está robando espacio de pantalla.

**La regla del reconocimiento:** el personaje tiene que aparecer **igual** cada vez (mismo tamaño, misma
zona, misma forma de entrar). Es lo que construye reconocimiento de marca. Si cada vez llega distinto,
no se registra como "el personaje de esa marca": se registra como ruido.

---

## 7. Los tres trabajos, en detalle

### Tapar un corte

Es el uso más subvalorado. Tienes un salto de continuidad (la persona cambió de posición entre tomas,
ver `26`) y no tienes b-roll para taparlo. Metes el personaje entrando justo **en** el corte: el ojo se
va con el movimiento nuevo y no registra el salto.

Truco: que la entrada del personaje empiece **2 fotogramas antes** del corte. Así el movimiento ya tiene
la atención cuando ocurre el salto.

### Marcar

Tres apariciones consistentes en 30 segundos marcan más que un logo permanente en la esquina, y molestan
diez veces menos. El logo lo filtra el cerebro en dos segundos; el personaje que aparece y desaparece
nunca se vuelve invisible.

### Reaccionar (el humor)

El personaje reacciona a lo que dice el presentador: se sorprende con el precio, se tapa la cara con el
error, aplaude el resultado. Esto convierte información plana en una escena de dos.

Para esto necesitas **variantes de pose**: mínimo 4 (neutro, sorprendido, feliz, negando). Genéralas
todas en la misma sesión, con el mismo prompt base y el mismo croma, para que sean coherentes entre sí.
Genera de a una pose por imagen — pedir "cuatro poses en una imagen" te da cuatro personajes distintos.

---

## 8. Cuándo el personaje ESTORBA

Sé honesto con esto. El personaje sobra cuando:

- **Es un testimonio real.** Alguien contando su experiencia. Un muñequito animado encima le quita
  exactamente lo que ese video vende: que sea verdad (`154`).
- **El tema es serio.** Un problema del cliente, una disculpa, un tema de plata que salió mal. La
  mascota alegre ahí se lee como burla.
- **El plano ya está lleno.** Mucho texto, mucho movimiento, gráfico de datos. Otra capa es ruido.
- **No lo puedes animar.** Un personaje 100% quieto encima de un plano vivo se ve pegado. Si no tienes
  tiempo de darle al menos una entrada con curva y un movimiento de flotación, no lo pongas.
- **Va a competir con la cara.** Si por tamaño o por posición el ojo duda entre mirar a la persona o al
  dibujo, perdiste las dos.
- **Es la única idea del video.** Un video que solo tiene "sale la mascota" no tiene video.

---

## 9. Que respire: la flotación

Un truco barato que cambia mucho. Aunque el personaje sea una imagen fija, si **flota** levemente
mientras está en pantalla, deja de verse pegado.

```bash
-filter_complex "[1:v]scale=-1:620,format=rgba[pj];\
[0:v][pj]overlay=x=W-w-56:y='H-h-470+9*sin(2*PI*t/2.4)'"
```

Sube y baja 9 píxeles con un ciclo de 2,4 segundos. Casi imperceptible conscientemente, evidente en la
sensación. Súbelo a 14 px para un personaje juguetón; bájalo a 5 px para uno serio.

Si además le metes una rotación mínima acompasada, parece animado de verdad:

```bash
[1:v]scale=-1:620,format=rgba,rotate='0.018*sin(2*PI*t/2.4)':c=none:ow=rotw(0.02):oh=roth(0.02)[pj]
```

`c=none` es obligatorio: si no, la rotación te rellena las esquinas de negro y pierdes la transparencia.

---

## 10. Coherencia con la marca

El personaje no lo inventa el editor. Lo define `directorcreativo_lushows`. Antes de meterlo a un video,
verifica que exista lo siguiente; si no existe, para y pídelo:

- **Hoja de personaje:** cómo se ve de frente, de lado, en 4 poses mínimo.
- **Paleta exacta:** para que el duotono de marca (`64`) no lo destruya. Ojo: si aplicas el look de
  color al video completo **después** de superponer el personaje, le cambias los colores. El personaje
  va **encima** del tratamiento de color, nivel 3 de la pila (`80`).
- **Qué NO hace el personaje:** no todas las marcas quieren su mascota bailando. Pregunta.
- **Escala relativa:** si el personaje aparece junto al producto, su tamaño relativo debe ser siempre el
  mismo. Un personaje que a veces es del tamaño de una taza y a veces de una persona rompe el mundo.

---

## Errores comunes

1. **Cortar a la lámina del personaje a pantalla completa.** Es el error que mata el plano. Va encima,
   conviviendo con el presentador, no en vez de él.
2. **Meterlo solo al final junto al logo.** Ahí no hace ninguno de sus tres trabajos. Es relleno.
3. **Dejarlo en pantalla todo el video.** A los 4 segundos el cerebro lo borra. Aparece, hace algo, se
   va.
4. **Usarlo para mostrar algo tangible.** Tienes el producto filmado. La ilustración del producto es
   peor que el producto.
5. **Ponerlo del lado contrario a donde mira la persona.** Se sienten dos elementos que se ignoran.
6. **Cambiarle tamaño y posición en cada aparición.** Sin consistencia no hay reconocimiento de marca.
7. **Personaje totalmente quieto.** Se ve pegado. Mínimo una flotación de 9 px.
8. **Olvidar `c=none` al rotar.** Las esquinas se rellenan de negro y adiós transparencia.
9. **Aplicar el look de color después de superponerlo.** Se lleva los colores del personaje. Va antes.
10. **Meterlo en un testimonio real.** Le quitas la credibilidad, que es lo único que ese formato tiene.
11. **Pedir las 4 poses en una sola imagen generada.** Salen cuatro personajes distintos. De a una.
12. **Que tape el subtítulo.** El texto es el canal principal (`40`); el personaje es apoyo. El apoyo
    nunca tapa al principal.

---

## Checklist

Antes de dar por buena una aparición del personaje:

- [ ] Esta aparición **tapa, marca o reacciona**. Si no hace ninguna, la quité.
- [ ] Está **encima** del plano, no reemplazándolo (salvo remate justificado).
- [ ] El recorte tiene alfa limpio y sin halo, verificado sobre magenta (`81`).
- [ ] **No tapa la cara** ni el subtítulo ni entra en la zona muerta de la plataforma (`45`).
- [ ] Está del **lado hacia donde mira** la persona.
- [ ] Mide entre el **25% y el 40%** de la altura del cuadro.
- [ ] Dura entre **1,5 y 3,5 segundos**. No más.
- [ ] Entra con **curva** (o con golpe de audio), no con fundido plano.
- [ ] Sale **más rápido** de lo que entró.
- [ ] Tiene **flotación** o algún movimiento propio: no está congelado.
- [ ] Todas las apariciones del video usan **mismo tamaño, misma zona y misma entrada**.
- [ ] El look de color se aplicó **antes** de superponerlo: sus colores son los de marca.
- [ ] Si el formato es testimonio o el tema es serio, **decidí no ponerlo** y lo dejé dicho.
