# 161 — Entrevista y documental

**Qué resuelve:** grabaste a alguien contando algo real — un cliente, un fundador, un cocinero, tu abuela.
Tienes 40 minutos de conversación y necesitas 3 minutos que emocionen. Este módulo es cómo se corta una
respuesta sin traicionar lo que la persona quiso decir, cómo se monta sin que se oigan las preguntas, y
cómo el silencio se vuelve una herramienta en vez de un bache.

> **Diferencia con el talking head (`160`):** allá la persona le habla a la cámara y suele estar guionada.
> Aquí le habla a **otra persona**, la respuesta es espontánea, y la pregunta existe pero casi siempre no
> se va a oír. Eso cambia todo el montaje.

---

## 1. Antes de cortar: la lectura

Una entrevista se lee entera, con transcripción. No hay atajo. Y se lee dos veces:

**Primera pasada — marcar joyas.** Sin pensar en estructura. Solo señalas donde algo te movió: una frase
redonda, una contradicción, una risa, un titubeo que dice más que la frase.

**Segunda pasada — buscar la columna.** ¿Qué historia está contando esta persona sin darse cuenta? Casi
nunca es la que dijo que iba a contar. Ese es el documental que tienes, no el que planeaste.

### Sistema de marcas

```
★★★  Va sí o sí. Si esto no está, no hay video.
★★   Buen material de cuerpo.
★    Sirve para relleno o para tapar.
✂    Bonito pero no aporta. Reserva.
✖    Fuera.
```

Regla: si tienes más de 8 frases ★★★ para un video de 3 minutos, no marcaste, te enamoraste. Vuelve a
pasar y baja la mitad a ★★.

---

## 2. Cortar dentro de una respuesta sin traicionarla

Esta es la habilidad central del formato y donde se comete la falta más grave del oficio.

### Los tres cortes legítimos

**a) Quitar el arranque.** La gente arranca con basura: "Bueno, mira, o sea, yo lo que te diría es que…".
La idea empieza después. Cortar eso siempre es legítimo y casi siempre mejora.

```
Grabado:  "Eh, bueno, o sea, yo creo que... mira, lo que pasa es que el negocio se
           cayó porque no sabíamos cuánto costaba un plato."
Montado:  "El negocio se cayó porque no sabíamos cuánto costaba un plato."
```

**b) Quitar el medio redundante.** La persona dice la idea, la repite con otras palabras, y la vuelve a
decir. Te quedas con la mejor versión.

**c) Juntar dos partes de la MISMA idea** que quedaron separadas por una divagación.

### Los tres cortes que traicionan

**a) Quitar la condición.** "Eso funciona, pero solo si tienes local propio" → "Eso funciona". Es la
manipulación más común y la más fácil de justificar. No.

**b) Juntar respuestas de preguntas distintas** para fabricar una afirmación que no existió.

**c) Cortar la duda.** Si la persona dudó antes de responder, esa duda es información. Quitarla la vuelve
más segura de lo que fue.

> **La prueba del espejo:** si le muestras el corte a la persona entrevistada, ¿diría "sí, eso dije"?
> Si tienes que explicarle por qué quedó así, cruzaste la línea. Ver `197-etica-del-montaje.md`.

---

## 3. Montar sin preguntas en pantalla

El estándar del formato: **no se oyen las preguntas**. La persona habla y suena como si estuviera
contando, no respondiendo. Para que funcione, la respuesta tiene que ser **autoportante**.

### Las respuestas dependientes y cómo se salvan

```
Pregunta: "¿Y cuánto tiempo llevas con el restaurante?"
Respuesta dependiente:  "Once años."      ← inservible sola
```

Tres salidas:

| Salida | Cómo | Cuándo |
|---|---|---|
| **Rótulo** | Texto en pantalla: "11 años con el restaurante" y usas otro audio | Datos duros |
| **Recuperar de otro lado** | Buscar en el bruto donde sí dijo "llevo once años con esto" | Siempre primero |
| **Dejar la pregunta** | Se oye al entrevistador (fuera de cámara) | Solo si aporta tensión |

**Cuándo SÍ dejar la pregunta:** cuando la pregunta es incómoda y la reacción es la escena. "¿Y usted
sabía que estaba perdiendo plata?" — silencio de 3 segundos — "…no". Ahí la pregunta es la mitad del
momento.

### Truco de rodaje que te salva el montaje

Pídele a quien entreviste que **incorpore la pregunta en la respuesta**: no "once años", sino "llevo once
años con el restaurante". Se le dice antes de empezar y se le recuerda dos veces. Un editor que hace esto
en rodaje se ahorra el 60% del sufrimiento. Ver `170-briefing-de-rodaje-desde-la-edicion.md`.

---

## 4. Dos cámaras: el montaje cómodo

Con dos cámaras al mismo sujeto (una abierta, una cerrada) tienes corte invisible: cortas donde quieras y
el jump cut desaparece porque cambia el punto de vista.

### Configuración estándar

```
CAM A — plano medio, la persona a un tercio, mirando al otro lado del cuadro
CAM B — primer plano, más cerrada, ángulo distinto (no el mismo eje)
```

⚠️ **La regla del ángulo:** entre A y B tiene que haber al menos **30° de diferencia**. Si son casi el
mismo ángulo, el corte se lee como un salto y no como otra cámara.

### Sincronizar las dos cámaras

Con palmada al inicio (la forma barata del claqueta):

```bash
# Ver la forma de onda para ubicar la palmada a ojo
ffmpeg -i camA.mp4 -filter_complex "showwavespic=s=1920x240" -frames:v 1 ondaA.png
ffmpeg -i camB.mp4 -filter_complex "showwavespic=s=1920x240" -frames:v 1 ondaB.png
```

Y una vez sabes el desfase (por ejemplo B arranca 1,84 s después):

```bash
# Recorta B para que arranque igual que A
ffmpeg -i camB.mp4 -ss 1.84 -c copy camB_sync.mp4
```

Si grabaste audio aparte con grabadora (lo normal en documental), sustituyes la pista:

```bash
# Video de la cámara + audio de la grabadora, ya sincronizados
ffmpeg -i camA_sync.mp4 -i grabadora.wav -map 0:v -map 1:a \
  -c:v copy -c:a aac -b:a 192k -shortest entrevista_sync.mp4
```

### Cuándo cortar a la cerrada

No cada 5 segundos por deporte. Cortas a la cerrada cuando **sube la emoción**: cuando baja la voz, cuando
se le quiebra, cuando llega el dato duro. La cerrada es el subrayado. Si la usas todo el rato, deja de
subrayar nada.

---

## 5. Una sola cámara: cómo se salva

Sin segunda cámara, cada corte es un jump cut. Se tapa con:

1. **B-roll** — lo estándar. Se necesita mucho más del que la gente cree: **3 minutos de b-roll por cada
   minuto de corte final**.
2. **Punch-in** — la segunda cámara falsa → `22`
3. **Fotos y documentos** — en documental valen oro: la foto vieja, la factura, el recorte
4. **Plano de escucha** — si grabaste al entrevistador asintiendo, ahí tienes tus cortes gratis
5. **Manos, objetos, el lugar** — planos de detalle grabados después de la entrevista

> **Término nuevo — plano de escucha (o "noddy"):** plano del entrevistador escuchando, grabado después,
> que se usa para tapar cortes de la respuesta. Truco de televisión de toda la vida.

---

## 6. J-cuts y L-cuts: el pegamento del documental

Aquí es donde una entrevista deja de sonar a "trozos pegados" y empieza a sonar a película.

> **Término nuevo — J-cut:** el audio del siguiente plano **entra antes** que su imagen. Oyes al que va a
> hablar mientras todavía ves lo anterior.
>
> **Término nuevo — L-cut:** la imagen cambia pero el audio anterior **sigue sonando** un rato más.

Las letras vienen de la forma que hacía el corte en las líneas de tiempo antiguas.

### Para qué sirve cada uno

| Corte | Efecto | Uso típico |
|---|---|---|
| **J-cut** | Tira hacia adelante, anticipa | Entrar a una respuesta nueva; entrar a una escena |
| **L-cut** | Deja respirar, cierra una idea | Salir de una frase emotiva hacia b-roll |
| **Duro** | Corta seco | Cambio de bloque, golpe |

**Duraciones que funcionan:** J-cut de 0,5–1,2 s de adelanto. L-cut de 0,8–2,0 s de cola. Más de 2,5 s se
vuelve confuso: el espectador no sabe quién habla.

### Cómo se arma en ffmpeg

El montaje real de J/L cuts es de línea de tiempo, pero se puede construir con `filter_complex` separando
las pistas. La idea: el video corta en el segundo 10,0 y el audio en el 9,2.

```bash
# J-cut: audio del clip B entra 0,8 s antes que su imagen
ffmpeg -i A.mp4 -i B.mp4 -filter_complex "\
[0:v]trim=0:10,setpts=PTS-STARTPTS[v0]; \
[1:v]trim=0.8:6,setpts=PTS-STARTPTS[v1]; \
[0:a]atrim=0:9.2,asetpts=PTS-STARTPTS[a0]; \
[1:a]atrim=0:6,asetpts=PTS-STARTPTS[a1]; \
[v0][v1]concat=n=2:v=1:a=0[v]; \
[a0][a1]concat=n=2:v=0:a=1[a]" \
-map "[v]" -map "[a]" -c:v libx264 -crf 18 jcut.mp4
```

Lo importante no es el comando, es el concepto: **el corte de imagen y el de audio no van en el mismo
punto**. Casi nunca deberían ir en el mismo punto.

---

## 7. El silencio como herramienta

En video corto el silencio es un bache. En documental el silencio **es contenido**.

### Los silencios que se conservan

- **Antes de una respuesta difícil.** La persona piensa. Ese aire vale más que cualquier frase.
- **Después de la frase más fuerte.** 1,5–2,5 s para que aterrice. Sin música, sin texto.
- **Cuando se le quiebra la voz.** No lo tapes con música. Taparlo es cobardía de montaje.

### Cómo se hace que un silencio no suene a error

Un silencio en documental **nunca es silencio digital**. Debajo siempre hay algo:

- Room tone del lugar
- Ambiente real (la calle, la cocina, el ventilador)
- Una nota sostenida de música bajísima (-32 LUFS)

```bash
# Extraer 10 s de ambiente del lugar para usarlo como cama
ffmpeg -i entrevista.mp4 -ss 00:03:12 -t 10 -vn -c:a pcm_s16le ambiente.wav

# Ponerlo debajo de todo el corte a -38 dB, en bucle
ffmpeg -i corte.mp4 -stream_loop -1 -i ambiente.wav -filter_complex \
  "[1:a]volume=-38dB[amb];[0:a][amb]amix=inputs=2:duration=first[a]" \
  -map 0:v -map "[a]" -c:v copy corte_con_ambiente.mp4
```

**La prueba:** si al llegar el silencio el espectador mira el teléfono para ver si se dañó — falló. Si se
inclina hacia adelante — funcionó.

---

## 8. Estructura de un documental corto (2–5 min)

```
0:00 – 0:15   COLD OPEN. La frase más fuerte, fuera de contexto. Sin música. Sin títulos.
0:15 – 0:25   Título / respiro. Aquí sí entra música y el rótulo de quién es.
0:25 – 1:10   Quién es y dónde está. B-roll del lugar. La normalidad antes del problema.
1:10 – 2:30   El problema / el giro. Aquí van los planos cerrados y el silencio.
2:30 – 3:30   Qué hizo. Ritmo más alto, más cortes, música que sube.
3:30 – 4:10   Dónde está hoy. Vuelve la calma.
4:10 – 4:30   La frase de cierre. Casi siempre es una que dijo sin darse cuenta.
```

**La frase de cierre nunca es la que la persona preparó.** Búscala entre las respuestas descartadas.

---

## 9. Rótulos: quién es esta persona

Va **una sola vez**, entre el segundo 8 y el 20, y se queda 3–4 s.

```
MARÍA ELENA CASTRO
Dueña · Restaurante La Vecina · Bogotá
```

Dos líneas máximo. Sin cargo inventado, sin adjetivos ("emprendedora visionaria" — no). Formato y
tipografía en `48-rotulos-y-lower-thirds.md`.

---

## 10. Música en documental

- **Entra tarde.** Nunca en el cold open. Ideal: después del primer rótulo.
- **Un solo tema con variaciones**, no cuatro canciones. Cambiar de canción cada minuto se lee a video
  de agencia.
- **Se calla en el momento emotivo.** El instinto es subirla; el efecto real es que la emoción se lee
  como fabricada. Bájala o quítala.
- Nivel bajo la voz: **-24 a -28 LUFS**, más bajo que en video corto. → `74`, `75`

---

## Errores comunes

1. **Cortar la condición de una frase** para que suene más contundente. Es la traición más frecuente y la
   que más pleitos genera con el cliente entrevistado.
2. **Montar solo con las respuestas "buenas".** Un documental de puras frases redondas suena a comercial.
   Los titubeos son la textura que lo hace creíble.
3. **Dejar todos los cortes duros y en el mismo punto de audio e imagen.** Suena a trozos pegados. J y L
   cuts son obligatorios en este formato.
4. **No grabar b-roll suficiente.** Llegas al montaje con 40 min de cara y 2 min de apoyo. Necesitas 3:1.
5. **Poner música bajo el momento emotivo.** Manipula y se nota. Quítala.
6. **Silencio digital absoluto.** Sin ambiente debajo, cada pausa parece archivo dañado.
7. **Dos cámaras con menos de 30° entre ellas.** El corte se ve como falla, no como cámara.
8. **Usar el plano cerrado todo el tiempo.** Si la cerrada es el subrayado y subrayas todo, no subrayas nada.
9. **Rótulo tarde o repetido.** Si a los 40 s el espectador todavía no sabe quién habla, lo perdiste.
10. **No verificar el desfase de audio de la grabadora externa.** 3 fotogramas de desfase ya se ven en los
    labios y te arruinan la pieza entera.
11. **Empezar por el principio cronológico.** Casi nunca es el mejor arranque. El cold open manda.
12. **No mostrarle el corte a la persona** cuando el tema es sensible. No es obligación legal siempre,
    pero es oficio.

---

## Checklist

- [ ] Transcripción completa, marcada en dos pasadas (★★★ / ★★ / ★ / ✂ / ✖)
- [ ] Cada corte dentro de una respuesta pasa la prueba del espejo
- [ ] Ninguna condición ("solo si…", "pero…") fue eliminada
- [ ] Las respuestas se sostienen solas o tienen rótulo que las contextualiza
- [ ] Cámaras sincronizadas y verificadas en labios, no solo en la onda
- [ ] Audio de grabadora externa sustituido y comprobado cuadro a cuadro
- [ ] Al menos 30° de diferencia entre cámaras
- [ ] J-cuts y L-cuts usados; casi ningún corte tiene audio e imagen en el mismo punto
- [ ] Ambiente / room tone continuo bajo todo el corte
- [ ] Al menos un silencio de 1,5 s conservado después de la frase más fuerte
- [ ] Cold open con la frase más fuerte, sin música
- [ ] Rótulo de identificación entre el segundo 8 y el 20, máximo dos líneas
- [ ] Música entra tarde, un solo tema, se calla en el momento emotivo
- [ ] B-roll suficiente: nunca más de 8 s seguidos del mismo encuadre de cara
- [ ] Pasó `98-verificacion-del-corte.md`
