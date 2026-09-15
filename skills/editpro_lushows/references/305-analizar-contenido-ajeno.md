# 305 — Analizar contenido ajeno: desarmar un video con rigor

> Verificado a **agosto de 2026**. "Me gustó cómo lo hizo" no es análisis. Es una reacción. Este módulo
> es el protocolo para desarmar el video de otro y salir con **instrucciones ejecutables** en vez de
> admiración. Se aplica igual a un competidor, a una cuenta grande, a un anuncio que te apareció, o a un
> video tuyo viejo (que a los tres meses ya es "de otro").

## Por qué el análisis casual no sirve

Cuando ves un video que te gusta, tu cerebro registra el **efecto** ("qué chévere", "qué bien montado") y
descarta las **causas**. Las causas son aburridas: duraciones, cortes, encuadres, orden de la información.
Y son justamente lo único que puedes copiar.

Peor: recuerdas mal. Vas a jurar que "arranca con la cara del tipo" y cuando lo revisas fotograma a
fotograma resulta que arranca con un plano de la calle por 0,8 s y la cara entra después. Ese 0,8 s es la
diferencia entre que funcione y que no.

> **El análisis es contra la memoria. Todo lo que no anotes con un número, lo vas a recordar mal.**

---

## Antes de empezar: qué se copia y qué no

Línea clara, porque importa legal y creativamente:

| Se copia | No se copia |
|---|---|
| La **estructura** (orden y duración de los bloques) | El material grabado |
| El **tipo de gancho** | La frase exacta |
| El **ritmo** (cortes por segundo) | La música con derechos |
| La **técnica** (un punch-in en el momento X) | El guion palabra por palabra |
| El **ángulo de la idea** | La marca, el logo, el estilo gráfico registrado |
| El **orden de la información** | La cara de otra persona |

La estructura no es de nadie. La ejecución sí. Copiar la estructura de un video ajeno con tu propio
material es exactamente lo que hacen todos los profesionales del oficio, y se llama estudiar. Copiar el
guion palabra por palabra se llama otra cosa.

---

## Paso 0 — Consigue el archivo

No se puede analizar bien desde el teléfono, con el dedo intentando pausar en el segundo 1,4.

Opciones:
- **Grabación de pantalla** del teléfono o del computador. Es la más simple y siempre funciona.
- Reproducir en el navegador y grabar la pantalla del computador.

Con el archivo en el disco, ya puedes trabajar de verdad.

```bash
# Duración exacta, resolución, fps
ffprobe -v error -show_entries format=duration:stream=width,height,r_frame_rate \
        -of default=noprint_wrappers=1 ajeno.mp4
```

La duración exacta es la base de todo lo que sigue. Si vas a comparar contra tus videos, necesitas los dos
números con decimales.

---

## El protocolo de las seis pasadas

Cada pasada busca **una sola cosa**. Si intentas ver todo a la vez, no ves nada. Toma unos 20 minutos por
video y vale por diez horas de mirar reels distraído.

### Pasada 1 — Sin sonido

Quita el volume completamente y ve el video entero.

Responde por escrito:
- ¿Se entiende de qué va **sin oír nada**?
- ¿En qué segundo entendiste de qué se trataba?
- ¿Hay texto en pantalla? ¿En qué momentos y con cuántas palabras?
- ¿Qué se ve exactamente en el primer fotograma?

**Por qué primero:** una parte enorme de la gente ve sin sonido o con el sonido a medias. Si el video
funciona mudo, está bien construido. Si no funciona mudo, está apostando a que le suban el volumen.

### Pasada 2 — Solo sonido

Ahora al revés: escúchalo sin mirar (o con la pantalla tapada).

- ¿Hay música? ¿Entra desde el segundo 0 o después?
- ¿Hay sonido ambiente real o todo es música?
- ¿Hay efectos marcando los cortes?
- ¿La voz suena grabada aparte o en el momento?
- ¿Hay silencios? ¿Dónde?
- ¿La música cambia de intensidad en algún punto?

Los silencios y los cambios de intensidad marcan la estructura. Casi siempre coinciden con los bloques.

### Pasada 3 — Contar cortes

```bash
ffmpeg -i ajeno.mp4 -filter:v "select='gt(scene,0.3)',showinfo" -f null - 2>&1 | grep showinfo
```

Te da los tiempos aproximados de cada cambio de plano. Con eso:

```
cortes detectados: 14
duración: 21,4 s
ritmo: 21,4 ÷ 14 = 1,53 s por plano
```

Compáralo con el estándar de 2026 (**cambio visual cada 1,5–2 s**) y con tus propios videos.

**Ojo:** la detección automática no ve los punch-ins ni los zooms digitales, que también son cambios
visuales. Cuenta esos a mano en la pasada 4. El número real de "cambios visuales" suele ser 1,3–1,8 veces
el número de cortes detectados.

### Pasada 4 — Fotograma a fotograma en los primeros 3 segundos

Aquí está el 70 % del aprendizaje.

```bash
# Un fotograma cada 0,25 s durante los primeros 3 s
ffmpeg -i ajeno.mp4 -t 3 -vf fps=4 gancho_%02d.png
```

Ahora tienes 12 imágenes. Míralas en fila y llena esto:

| Tiempo | Qué se ve | ¿Movimiento? | ¿Texto? | ¿Cara? |
|---|---|---|---|---|
| 0,00 | | | | |
| 0,25 | | | | |
| 0,50 | | | | |
| 0,75 | | | | |
| 1,00 | | | | |
| ... | | | | |

Preguntas que esta tabla contesta y que la memoria contesta mal:
- ¿Cuántos planos hay en los primeros 3 s?
- ¿En qué segundo aparece la primera palabra de texto?
- ¿En qué segundo aparece la primera cara?
- ¿Hay movimiento de cámara o el movimiento es del sujeto?

### Pasada 5 — Transcripción con tiempos

Transcribe lo que se dice, con el segundo en que empieza cada frase (ver `124` para hacerlo con IA).

```
0,0 – 1,4   "Este es el error que comete todo el mundo con la parrilla"
1,4 – 3,8   "y no es la temperatura"
3,8 – 7,2   "es que la sacan muy pronto"
...
```

Cosas que solo se ven así:
- **Cuántas palabras por segundo.** El estándar de contenido corto va rápido: 3–4 palabras por segundo.
- **Dónde está la promesa.** Casi siempre en los primeros 1,5 s.
- **Dónde está el giro.** Casi siempre entre el 30 % y el 50 % del video.
- **Si hay relleno.** En videos buenos no hay ni un "bueno" ni un "entonces".

### Pasada 6 — El mapa de bloques

Junta todo en un solo dibujo con tiempos y porcentajes:

```
VIDEO AJENO — 21,4 s — 14 cortes — 1,53 s/plano

0,0 ─ 1,4   ( 7 %)  GANCHO      "el error que comete todo el mundo"
                                 plano cerrado de carne, movimiento, sin música
1,4 ─ 3,8   (11 %)  NEGACIÓN    "y no es la temperatura"
                                 entra la música, corte a cara
3,8 ─ 9,0   (24 %)  DESARROLLO  demostración, 4 cortes, sonido real
9,0 ─ 11,5  (12 %)  GIRO        contraejemplo, cambio de encuadre
11,5 ─ 18,0 (30 %)  PAGO        el resultado, plano abierto, música sube
18,0 ─ 21,4 (16 %)  REMATE      texto en pantalla, música baja, bucle al plano 1
```

**Ese mapa es el entregable.** Es lo que te llevas. Lo puedes aplicar a un tema tuyo mañana.

---

## Qué NO puedes saber (y no te inventes)

Sé honesto con los límites. De un video ajeno **no puedes ver**:

- Su curva de retención.
- Su tasa de salto.
- Si tuvo pauta detrás (a veces se nota en la Biblioteca de Anuncios de Meta, a veces no).
- Cuánto vendió.
- Si el creador está contento con ese video.
- Si es el único que funcionó de veinte que publicó.

Lo último es clave: **estás viendo su mejor video, no su promedio.** Comparar tu promedio con su mejor
video es la receta para sentirte mal sin razón (ver `308`).

### Lo que sí puedes estimar

| Señal pública | Qué sugiere |
|---|---|
| Comentarios ÷ vistas | Menos de 0,1 % es bajo; más de 0,5 % es alta conversación |
| Compartidos visibles (TikTok los muestra) | La métrica de alcance real |
| Guardados (visibles en algunos casos) | Intención de volver |
| Que el mismo formato se repita en su perfil | **Le está funcionando.** Nadie repite lo que no funciona |
| Que un video esté fijado en el perfil | Es su mejor pieza, según ellos |
| Que aparezca en la Biblioteca de Anuncios de Meta | Tiene pauta. Su alcance no es orgánico |

**La señal más confiable de todas es la repetición.** Si una cuenta lleva ocho videos con la misma
estructura, esa estructura le está funcionando. Vale más que cualquier número que puedas contar.

---

## Analizar competidores locales (lo que más te sirve)

Para tu bar, la cuenta de otro bar de Tocancipá o de Zipaquirá enseña más que una cuenta gringa de
500.000 seguidores. Están en tu mercado, con tu presupuesto y tu público.

Qué mirar en un competidor local:

| Qué | Por qué |
|---|---|
| Cuántas veces publica por semana | Te dice el ritmo real de tu mercado |
| Qué formato repite | Lo que le funciona |
| Qué dejó de hacer | Lo que no le funcionó (información gratis) |
| Si los comentarios preguntan por precio/horario | Su contenido no lo está diciendo. **Tu oportunidad** |
| Si la gente etiqueta amigos | Ese formato genera invitación. Es el que llena mesas |
| Qué videos tienen 5× su promedio | Su fórmula ganadora |

**El truco de "qué dejó de hacer":** baja tres meses en su perfil. Si hacía un formato y lo abandonó,
probablemente no funcionaba. Te acabas de ahorrar tres meses de probarlo tú.

---

## El archivo de referencias

El análisis se pierde si no se guarda. Arma esta carpeta:

```
referencias/
  2026-08-12_bar-zipa_estructura-error-negacion/
    video.mp4
    gancho_01.png … gancho_12.png
    mapa.md          ← el mapa de bloques del paso 6
    aplicacion.md    ← cómo lo voy a usar con MI material
```

El archivo `aplicacion.md` es el que hace que esto no sea coleccionismo:

```markdown
# Cómo aplico esto

Estructura: gancho-negación-desarrollo-giro-pago-remate, 21 s, 1,5 s/plano.

Mi versión: "el error que comete todo el mundo pidiendo cerveza"
0,0–1,4  vaso escarchado en primer plano, sin música
1,4–3,8  "y no es la marca"
3,8–9,0  demostración de la temperatura
9,0–11,5 el contraste con la cerveza tibia
11,5–18  el trago, la reacción real
18–21,4  precio + bucle

Grabo el jueves.
```

Diez fichas así y tienes un sistema de trabajo. Cien reels vistos sin anotar nada y no tienes nada.

---

## El error de análisis más común: copiar el efecto sin la causa

Ves un video con transiciones espectaculares y concluyes "necesito mejores transiciones". Pero el video
funcionó por la primera frase, y las transiciones solo estaban ahí sin estorbar.

**Cómo protegerte:** para cada elemento que te llamó la atención, pregúntate:

> *Si le quito esto al video, ¿deja de funcionar?*

- Quítale la primera frase → **deja de funcionar**. Es causa.
- Quítale las transiciones y pon cortes secos → **sigue funcionando**. Es decoración.

Las causas suelen ser aburridas: qué se dice primero, cuánto dura cada cosa, qué se ve en el fotograma 1.
La decoración es lo llamativo. Tu ojo se va a la decoración. Tu cuaderno tiene que ir a las causas.

---

## Errores comunes

- **Ver el video y decir "me gustó cómo lo hizo".** Eso no es análisis, es una reacción.
- **Analizar desde el teléfono.** No puedes pausar en el segundo 1,4 con el dedo.
- **Fiarte de tu memoria del gancho.** Extrae los fotogramas. Vas a recordar mal.
- **No ver primero sin sonido.** Es la pasada que más enseña y la que todos se saltan.
- **Contar solo los cortes detectados automáticamente.** Los punch-ins también son cambios visuales.
- **Copiar el efecto llamativo en vez de la causa aburrida.** Las transiciones casi nunca son la causa.
- **Comparar tu promedio con el mejor video de otro.** Comparación injusta y desmoralizante.
- **Asumir que su alcance es orgánico.** Revisa la Biblioteca de Anuncios de Meta.
- **Estudiar cuentas gringas gigantes en vez del bar de al lado.** El competidor local enseña más.
- **No mirar qué formato ABANDONÓ el competidor.** Ahí están sus fracasos, gratis.
- **Guardar reels en "guardados" y llamarlo estudiar.** Sin el mapa de bloques escrito, no queda nada.
- **Copiar el guion palabra por palabra.** La estructura no es de nadie; la ejecución sí.

---

## Checklist

- [ ] Tengo el **archivo de video** en el disco, no solo el enlace.
- [ ] Saqué **duración exacta, resolución y fps** con `ffprobe`.
- [ ] **Pasada 1:** lo vi sin sonido y anoté si se entiende mudo.
- [ ] **Pasada 2:** lo escuché sin ver y anoté música, ambiente, silencios.
- [ ] **Pasada 3:** conté los cortes y calculé **segundos por plano**.
- [ ] **Pasada 4:** extraje **12 fotogramas de los primeros 3 s** y llené la tabla.
- [ ] **Pasada 5:** transcribí con tiempos y conté **palabras por segundo**.
- [ ] **Pasada 6:** escribí el **mapa de bloques con tiempos y porcentajes**.
- [ ] Para cada elemento llamativo, me pregunté **"¿si lo quito, deja de funcionar?"**.
- [ ] Revisé si el formato **se repite en su perfil** (la señal más confiable).
- [ ] Revisé si tiene **pauta** en la Biblioteca de Anuncios.
- [ ] Guardé la carpeta de referencia con el **mapa** y el **archivo de aplicación**.
- [ ] Escribí **cómo lo voy a aplicar con MI material**, con tiempos, y una fecha de grabación.
