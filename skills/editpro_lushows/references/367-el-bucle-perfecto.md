# 367 — El final que rebobina: el bucle perfecto y por qué alguien comparte

> `33` cubre el remate: pagar, pedir, cerrar. Este módulo va por lo otro que hace el final, que es lo que
> más rinde y casi nadie monta a propósito: **conseguir que el video se vuelva a ver y que alguien lo
> mande**. Una repetición vale como una vista nueva sin costar distribución, y un reenvío vale como
> veinte.

---

## Las tres cosas que puede provocar un final

| Efecto | Qué lo dispara | Qué gana |
|---|---|---|
| **Repetición** | El video vuelve a empezar y no se siente el corte | Tiempo de visualización que se multiplica |
| **Reenvío** | El video le sirve a alguien **para algo con otra persona** | Alcance nuevo, el más valioso |
| **Salida limpia** | El video terminó, se entendió, se cerró | Nada, pero tampoco daño |

Y una cuarta, que es la que hay que evitar: **la salida anticipada**, cuando el final avisa que se acaba
y la gente se va antes de que termine. La produce el fundido a negro, la música que se apaga, y la
despedida ("bueno, eso fue todo").

---

## Parte 1 — El bucle perfecto

### Qué es exactamente

Que el **último fotograma empalme con el primero** tan bien que el espectador no perciba dónde terminó y
dónde volvió a empezar. En un feed que reproduce en bucle automático, eso significa que el video se ve
dos o tres veces antes de que la persona se dé cuenta.

No es un truco de retención: es una decisión de montaje, y se decide **antes de grabar**.

### Los cuatro tipos de bucle, de más fácil a más difícil

**1. Bucle de imagen (empalme visual)**
El último plano es el mismo encuadre que el primero. Se graba a propósito: empiezas y terminas con la
mano cerrando sobre la botella, en la misma posición.

- Dificultad: baja
- Requisito: grabar el plano de cierre igual que el de apertura (mismo lugar, misma altura, misma luz)
- Es el más robusto y el que se debería usar por defecto

**2. Bucle de frase (empalme hablado)**
La última palabra del video se convierte en la primera. *"…y por eso nunca pedimos hielo."* → arranca
*"Nunca pedimos hielo."* El oído completa la vuelta.

- Dificultad: media
- Requisito: escribir el guion sabiendo dónde va a cerrar
- Cuidado: no puede sonar a que se repitió por error

**3. Bucle de pregunta (empalme lógico)**
El final entrega una información que **cambia el significado del principio**, y el espectador vuelve a
verlo para comprobarlo. Es el más potente y el más difícil.

- Dificultad: alta
- Requisito: que el principio tenga un detalle que solo se entiende con el final
- Ejemplo: al principio se ve un vaso con una marca rara; al final se explica qué es la marca. La gente
  vuelve a mirar el principio.

**4. Bucle de ritmo (empalme musical)**
El compás de la música cierra justo donde empieza. Requiere que el video dure un número exacto de
compases.

- Dificultad: media-alta
- Requisito: elegir la música antes de montar y cortar contra el compás
- Solo vale la pena si el video ya es musical

### Cómo se monta un bucle de imagen, paso a paso

1. **Al grabar:** después de la última toma, repite el plano de apertura. Diez segundos de grabación,
   mismo sitio, misma luz. Ese es tu material de cierre.
2. **Al montar:** pon ese plano al final y córtalo para que el **gesto esté en el mismo punto** que en el
   fotograma 0. Si el video abre con la mano ya bajando, el final debe terminar con la mano ya bajando.
3. **Sin fundidos.** Ni de imagen ni de audio. Un fundido rompe el bucle por definición.
4. **Sin nada en pantalla al final.** Ni texto, ni logo, ni CTA. Si el último fotograma tiene un rótulo y
   el primero no, el empalme se ve.
5. **El audio también empalma.** El último medio segundo no puede tener una nota que se apaga; tiene que
   entregarle el testigo al arranque.

### Verificar el bucle con ffmpeg (esto sí se puede medir)

**Primero: los dos fotogramas, lado a lado.**

```bash
ffmpeg -y -i reel.mp4 -frames:v 1 primero.png
ffmpeg -y -sseof -0.05 -i reel.mp4 -frames:v 1 ultimo.png
ffmpeg -y -i primero.png -i ultimo.png -filter_complex hstack -frames:v 1 empalme.png
```

**Segundo: qué tan distintos son, en número.** El filtro `blend=difference` más `signalstats` te da el
brillo medio de la diferencia: cuanto más cerca de 0, mejor empalme.

```bash
ffmpeg -y -i primero.png -i ultimo.png -filter_complex \
"[0:v][1:v]blend=all_mode=difference,signalstats,metadata=print" -f null - 2>&1 | grep YAVG
```

Interpretación práctica (es una guía de trabajo, no un estándar): por debajo de **12** el empalme se
siente continuo; por encima de **35** se ve el salto. Entre medio, míralo con los ojos.

**Tercero, y el que de verdad importa: verlo en bucle de verdad.**

```bash
printf "file 'reel.mp4'\nfile 'reel.mp4'\nfile 'reel.mp4'\n" > lista.txt
ffmpeg -y -f concat -safe 0 -i lista.txt -c copy triple.mp4
```

Míralo en el celular, no en el computador. Si en la segunda vuelta te das cuenta de que volvió a
empezar, todavía no está.

**Cuarto: el audio del empalme.**

```bash
# último medio segundo y primer medio segundo, pegados
ffmpeg -y -sseof -0.5 -i reel.mp4 -vn cola.wav
ffmpeg -y -t 0.5 -i reel.mp4 -vn cabeza.wav
ffmpeg -y -i cola.wav -i cabeza.wav -filter_complex "[0:a][1:a]concat=n=2:v=0:a=1" empalme_audio.wav
```

Escúchalo suelto. Si hay un bache, un chasquido o una nota que muere, el bucle se siente aunque la imagen
empalme.

### La trampa del último fotograma repetido

Muchos exports dejan el último fotograma congelado unas décimas, o el codificador duplica el fotograma
final. Eso mete una pausa justo en el empalme y arruina el bucle. Compruébalo:

```bash
ffprobe -v error -select_streams v:0 -show_entries frame=pts_time -of csv=p=0 reel.mp4 | tail -5
```

Si los dos últimos tiempos están separados por más de un fotograma, córtale la cola:

```bash
ffmpeg -y -i reel.mp4 -t 41.90 -c:v libx264 -crf 18 -preset slow -pix_fmt yuv420p -c:a aac -b:a 192k reel_v2.mp4
```

### Cuándo NO hacer bucle

- Cuando el video es una explicación con respuesta final clara: el bucle confunde.
- Cuando el remate es emocional y necesita silencio después.
- Cuando el CTA es lo importante (una promoción con fecha): ahí quieres que la gente salga a hacer algo,
  no que se quede dando vueltas.

---

## Parte 2 — Por qué alguien comparte

Compartir no es "le gustó mucho". Compartir es **usar tu video para decir algo suyo**. Nadie reenvía por
ti; reenvían por ellos. Los seis motivos reales:

| Motivo | Qué piensa el que comparte | Cómo se monta el final |
|---|---|---|
| **Ganar una discusión** | "Ves, te lo dije" | Terminar con un veredicto claro y citable |
| **Etiquetar a alguien** | "Este eres tú" | Terminar con un tipo de persona reconocible |
| **Hacer un plan** | "Vamos" | Terminar con el lugar y algo apetecible, sin precio |
| **Quedar bien** | "Miren qué encontré" | Terminar con un dato raro y verificable |
| **Orgullo local** | "Esto es de aquí" | Nombrar el lugar: Tocancipá, la vereda, la calle |
| **Ser útil** | "Te sirve" | Terminar con el paso concreto, hacible hoy |

**La regla de montaje que sale de esto:** el final debe darle al espectador **una frase que él pueda
decir**, no una frase tuya. "El mejor corte de Tocancipá está en un bar que no conoces" es una frase que
alguien reenvía. "Gracias por ver, síganos" no la dice nadie.

### El detalle que multiplica reenvíos: que se pueda mandar sin explicar

Si para que el reenvío tenga sentido hace falta que la persona escriba tres líneas explicando, no lo
manda. El video tiene que **explicarse solo desde el primer segundo**, porque quien lo recibe empieza de
cero y sin contexto.

Prueba concreta: mándate el video a ti mismo por WhatsApp y míralo ahí. Si tuviste que escribir algo
para acompañarlo, el video no está listo para compartirse.

---

## Cómo conviven el bucle y el CTA

Se pelean, y hay que decidir:

- **Video de alcance** (quieres que lo vea gente nueva): bucle sí, CTA no. La marca va dentro del cuadro
  (el vaso, el delantal, el letrero), nunca como rótulo final.
- **Video de conversión** (promoción, evento, reserva): CTA sí, bucle no. Y el CTA va **después del
  pago**, dura 2–3 segundos, y es una sola acción.

Intentar las dos cosas produce lo peor de ambas: un CTA que nadie ejecuta y un bucle que no empalma.

---

## Errores comunes

1. Fundido a negro al final. Mata el bucle y avisa que se acabó.
2. Música que baja de volumen en los últimos segundos: es un cartel de "ya te puedes ir".
3. Poner el logo en el último fotograma. Si el primero no lo tiene, el empalme salta.
4. Despedirse. "Bueno, eso fue todo" ocupa el espacio del remate y anula la repetición.
5. No grabar el plano de cierre igual que el de apertura, y después intentar fabricar el bucle en
   montaje con lo que hay.
6. Dejar el último fotograma congelado o duplicado por el export: mete una pausa en el empalme.
7. Verificar el bucle en el computador, en un reproductor que no repite igual que el feed.
8. Hacer bucle en un video que termina con una respuesta clara: confunde en vez de enganchar.
9. Meter bucle y CTA a la vez. Elige.
10. Un final que solo funciona si viste todo el video. Quien lo recibe reenviado empieza de cero.
11. Terminar con una frase tuya en vez de una frase que el espectador pueda decir como suya.
12. Confundir el repunte final de la curva con gente que llegó: casi siempre son repeticiones.
13. Cerrar con el precio. El precio corta el reenvío: nadie manda un anuncio, mandan un descubrimiento.

---

## Checklist

- [ ] Decidí si este video es de bucle o de CTA, y no las dos
- [ ] Si es de bucle: grabé el plano de cierre igual al de apertura
- [ ] El gesto del último fotograma está en el mismo punto que el del primero
- [ ] No hay fundido, ni texto, ni logo en el último fotograma
- [ ] Saqué primero y último fotograma y los miré lado a lado
- [ ] La diferencia medida está por debajo de ~12, o lo comprobé a ojo
- [ ] Escuché el empalme de audio suelto y no hay bache ni nota que muere
- [ ] Comprobé que no hay fotograma final duplicado ni congelado
- [ ] Vi el archivo triplicado en el celular y no noté dónde volvía a empezar
- [ ] El final le da al espectador una frase que él puede decir como suya
- [ ] Sé cuál de los seis motivos de reenvío estoy activando
- [ ] Me lo mandé por WhatsApp y se entiende sin que yo escriba nada
