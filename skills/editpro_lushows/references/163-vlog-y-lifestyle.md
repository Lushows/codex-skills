# 163 — Vlog y lifestyle

**Qué resuelve:** grabaste tu día. Tienes 90 minutos de clips sueltos, la mitad movidos, y hay que sacar
de ahí 6 minutos que se sientan como una historia y no como un archivo de celular. El vlog es el formato
donde **el material manda más que el guion**, porque no hubo guion.

> **La ecuación del vlog:** el espectador no viene por el contenido, viene por **estar contigo**. Por eso
> un vlog perfectamente editado y frío rinde peor que uno imperfecto y presente. El montaje aquí no
> persigue pulcritud: persigue compañía.

---

## 1. Comprimir el tiempo real

Un día tiene 16 horas despierto. El vlog dura 6 minutos. La compresión es de **160:1**. Eso no se logra
cortando: se logra **eligiendo momentos y saltando el resto sin que se sienta un salto**.

### La unidad del vlog no es el clip, es el momento

Un momento tiene tres partes y el error clásico es dejar las tres completas:

```
ENTRADA (llego, abro la puerta, saludo)     ← casi siempre se bota
NÚCLEO  (pasa la cosa: la reacción, el dato, la torpeza)
SALIDA  (me despido, camino, guardo)        ← casi siempre se bota
```

**Se monta el núcleo y 0,5 s de cada lado.** Todo lo demás es transporte y el transporte no se filma para
verse, se filma para llegar.

### La proporción sana

| Bruto | Corte final | Momentos que sobreviven |
|---|---|---|
| 90 min | 6–8 min | 12–18 momentos |
| 3 h (viaje) | 10–12 min | 20–28 momentos |
| 20 min (mini-vlog vertical) | 45–60 s | 5–7 momentos |

Si tu vlog de 8 minutos tiene 40 momentos, ninguno respira. Si tiene 6, es un video de otra cosa.

---

## 2. La mecánica de la elipsis en vlog

> **Término nuevo — elipsis:** saltarse un pedazo de tiempo sin explicarlo. Todo el vlog es una cadena de
> elipsis. Ver `25-elipsis-y-condensacion.md`.

Lo que distingue a un vlog bien montado es **cómo entra y sale de cada elipsis**. Cuatro herramientas:

**a) El puente de voz (lo más usado).** La voz en off cruza el corte. Sigues oyendo la misma frase
mientras la imagen ya está en otro lugar y otra hora. El oído no registra el salto.

**b) El plano de traslado.** 0,8 s de la calle, el carro andando, los pies caminando. Comunica "me moví"
en menos de un segundo.

**c) La coincidencia de forma (match cut).** Cierras la nevera / se abre la puerta del carro. Mismo
movimiento, distinto lugar. Es lo que hace ver "editado de verdad" → `54`.

**d) El corte al ritmo de la música.** Si el corte cae en el golpe, el salto de espacio se perdona solo.

### Lo que NO usar

- **Fundidos a negro entre momentos.** Cortan la energía y se leen a diapositivas.
- **Transiciones de plantilla** (zoom con blur, glitch). Envejecen mal y se ven de plantilla.
- **Textos de "más tarde…" en cada corte.** Uno o dos por vlog, no doce.

---

## 3. La voz en off: el esqueleto invisible

En un vlog moderno la voz en off **no cuenta lo que se ve**, cuenta lo que estabas pensando. Es la
diferencia entre narración y compañía.

```
MAL:   "Aquí estoy llegando al mercado."      (se ve que llegas al mercado)
BIEN:  "No había ido al mercado en tres meses.
        Y la señora de las hierbas se acordaba de mí."
```

### Dos formas de conseguirla

**a) Grabada en el momento (a cámara o hablándole al micrófono).** Más viva, menos ordenada. Es el material
donde vive el carisma.

**b) Grabada después, viendo el material.** Más ordenada, y es la que cose el vlog. Se graba **al final**,
cuando ya montaste el esqueleto de imagen, no antes.

**Lo correcto es mezclar las dos.** La grabada en el momento aporta energía; la de después aporta sentido.

### Dónde va exactamente

- **Sobre planos de traslado y b-roll**, nunca sobre un momento donde ya está pasando algo con sonido
- Frases cortas. En vlog, 2–3 frases seguidas ya es un párrafo.
- **Silencios de 3–6 s** entre bloques de voz. El vlog necesita respirar; si hablas todo el rato es un
  podcast con imágenes.

### Nivel

La voz en off va **más íntima** que en tutorial: menos comprimida, más cerca, con algo de cuerpo grave.
Se busca la sensación de que te está hablando al oído, no presentando.

```bash
# Voz en off con presencia y cuerpo (cadena mínima)
ffmpeg -i vo_bruta.wav -af "highpass=f=75,equalizer=f=180:t=q:w=1.2:g=2,\
equalizer=f=3200:t=q:w=1.4:g=3,acompressor=threshold=-20dB:ratio=3:attack=8:release=180,\
loudnorm=I=-16:TP=-1.5:LRA=9" vo_lista.wav
```

Detalle completo en `70-cadena-de-voz-profesional.md`.

---

## 4. Ritmo del "día en la vida"

El vlog no tiene un pulso constante: tiene **olas**.

```
Alto     ██        ███         ██████            ██
Medio  ███  ████ ██   ████ ████      ████    ████  ███
Bajo         ██              ██          ████
       ──────────────────────────────────────────────►
       inicio    mañana     el plan     lo bueno   cierre
```

- **Arranque alto** (0–15 s): el momento más llamativo del día, fuera de orden. Sin contexto.
- **Bajada** (15–40 s): quién eres, qué día es, qué va a pasar. Ritmo tranquilo.
- **Meseta con picos** (el cuerpo): 3 o 4 picos separados por valles. Los valles son obligatorios.
- **El pico grande** (70–80% del video): lo que prometió el arranque.
- **Descenso y cierre**: el momento tranquilo. Casi siempre de noche, casi siempre sin música fuerte.

**El error del principiante es el ritmo plano alto:** todo cortado rápido, música arriba todo el tiempo.
Se siente frenético y se abandona a los 90 s. Los valles son lo que hace que los picos se sientan picos.

### Duración de plano por zona

| Zona | Duración media de plano |
|---|---|
| Arranque | 0,6 – 1,2 s |
| Presentación | 2 – 3,5 s |
| Cuerpo, valle | 2,5 – 4 s |
| Cuerpo, pico | 0,8 – 1,5 s |
| Cierre | 3 – 6 s |

---

## 5. Estabilizar sin que se note

El vlog se graba caminando. La imagen tiembla. Se arregla, pero con cuidado: sobre-estabilizar produce el
efecto "gelatina" que se ve peor que el temblor.

```bash
# Paso 1: analizar el movimiento (genera transformaciones.trf)
ffmpeg -i caminando.mp4 -vf vidstabdetect=shakiness=6:accuracy=12:result=transformaciones.trf -f null -

# Paso 2: aplicar. smoothing bajo = respeta el movimiento real
ffmpeg -i caminando.mp4 -vf \
 "vidstabtransform=input=transformaciones.trf:smoothing=18:zoom=2:optzoom=1,unsharp=5:5:0.6" \
 -c:a copy estabilizado.mp4
```

- `smoothing=18` para caminar normal. Si subes a 40 queda flotante y falso.
- `optzoom=1` deja que decida el recorte necesario; sin eso te salen bordes negros.
- El `unsharp` al final recupera la nitidez que come el reescalado.

**No estabilices todo el vlog.** Un poco de temblor es parte del lenguaje del formato: comunica "esto lo
grabé yo, en la vida real". Estabiliza solo los planos donde el temblor distrae.

---

## 6. Música en vlog

La música no es fondo: **es la que dice cómo hay que sentirse**. Y en vlog cambia varias veces.

| Momento | Tipo | Nivel |
|---|---|---|
| Arranque | Enérgica, entra en el segundo 1–2 | -18 LUFS |
| Presentación | Baja, casi textura | -26 LUFS |
| Cuerpo, valle | Instrumental suave | -26 LUFS |
| Cuerpo, pico | Sube, con percusión | -20 LUFS |
| Cierre | Lenta, se apaga sola | -24 → silencio |

### Reglas propias del formato

- **3–5 canciones en un vlog de 8 minutos.** Menos suena monótono, más suena a mezcla aleatoria.
- **El cambio de canción marca el cambio de bloque.** Es tu estructura audible.
- **La música se calla cuando pasa algo real.** Si alguien dice algo gracioso o emotivo, se baja o se
  quita. Ahí manda el sonido directo.
- **Nunca termines una canción con fade lineal de 2 s.** Se oye a plantilla. Termínala en un golpe de la
  propia canción o córtala en seco cuando entra la voz → `74`.

```bash
# Ducking automático: la música baja sola cuando hay voz
ffmpeg -i vlog.mp4 -i musica.mp3 -filter_complex \
 "[1:a]volume=-8dB[m];[m][0:a]sidechaincompress=threshold=0.05:ratio=8:attack=15:release=350[mduck]; \
  [0:a][mduck]amix=inputs=2:duration=first[a]" \
 -map 0:v -map "[a]" -c:v copy vlog_mix.mp4
```

Explicación en `75-ducking.md`.

---

## 7. Sonido directo: el activo escondido

El vlog es el formato donde el sonido real vale más que la música. La sartén, la lluvia, la gente hablando
en el mercado, el perro. Ese ambiente es lo que produce la sensación de estar ahí.

**No lo entierres bajo la música.** Deja el sonido directo audible (-28 a -22 LUFS) por debajo de todo. Y
en los momentos de textura (café que se sirve, puerta que se abre), **súbelo por encima de la música**
durante 1–2 s. Es gratis y transforma la percepción de calidad.

```bash
# Sacar el ambiente de un clip y guardarlo aparte para reusarlo
ffmpeg -i mercado.mp4 -vn -af "highpass=f=60,loudnorm=I=-26" ambiente_mercado.wav
```

---

## 8. Texto en el vlog

Distinto del video corto: aquí el texto **no lleva la información**, la acompaña.

- **Rótulo de lugar y hora**: `7:40 a.m. · Usaquén` — 2 s, esquina, discreto
- **Subtítulos solo cuando el audio es difícil** (viento, calle, alguien lejos)
- **Textos de comentario / chiste**: el aparte gracioso, con tipografía distinta a la de los rótulos
- **Nunca subtítulos de karaoke amarillos** en vlog largo. Ese lenguaje es de vertical corto.

En mini-vlog vertical (45–60 s) sí van subtítulos completos, porque es video corto disfrazado de vlog.

---

## 9. Estructura tipo (vlog de 6–8 min)

```
0:00 – 0:12   El pico del día, fuera de orden. Sin explicar. Música ya arriba.
0:12 – 0:18   Corte a negro corto o rótulo. Baja todo.
0:18 – 0:50   Arranque real: dónde estás, qué día es, qué se va a hacer. Voz en off.
0:50 – 2:30   Bloque 1. Un momento con núcleo. Valle al final.
2:30 – 4:00   Bloque 2. Sube. Aquí suele ir la comida / el encuentro.
4:00 – 5:40   Bloque 3. EL PICO. Lo que prometiste en el arranque, ahora completo.
5:40 – 6:40   Descenso. Noche, cansancio, reflexión corta.
6:40 – 7:00   Cierre. Una frase. Música que se apaga. Sin CTA gritado.
```

**El vlog no lleva CTA agresivo.** Si el formato es compañía, terminar vendiendo rompe el contrato. Si hay
que pedir algo, va bajito y al final: "si te gustó, nos vemos el martes".

---

## 10. Montaje por lote: la técnica que salva vlogs

Con 90 minutos de bruto no puedes montar clip por clip. Se hace en tres pasadas:

**Pasada 1 — descarte brutal.** Ves todo a 2x y botas lo obviamente malo (desenfocado, tapado, repetido).
Quedan ~35 minutos.

**Pasada 2 — extraer núcleos.** De cada clip que sobrevivió sacas SOLO el núcleo, sin transporte. Los
guardas numerados por orden cronológico. Quedan ~12 minutos.

```bash
# Extraer núcleos rápido, sin recodificar (corte al keyframe más cercano)
ffmpeg -ss 00:04:12 -to 00:04:19 -i DIA_clip07.mp4 -c copy nucleos/07_mercado.mp4
```

⚠️ Con `-c copy` el corte se pega al fotograma clave más cercano y puede desviarse hasta 1 s. Para el corte
fino del montaje final hay que recodificar. Ver `101-ffmpeg-cortar-y-unir.md`.

**Pasada 3 — armar.** Ahora sí ordenas, quitas la mitad, y montas el ritmo. De 12 min salen los 7 finales.

Sacar la hoja de contactos de los núcleos te deja ver el vlog entero de un vistazo:

```bash
ffmpeg -i nucleos_concatenados.mp4 -vf "fps=1/4,scale=240:-1,tile=8x6" contactos_vlog.png
```

---

## Errores comunes

1. **Dejar el transporte.** Llegar, saludar, despedirse, caminar al carro. Es el 60% del bruto y el 0% del
   interés.
2. **Ritmo plano alto.** Todo cortado rápido con música arriba. Sin valles, los picos no existen.
3. **Voz en off que describe lo que se ve.** "Aquí estoy en el mercado." Redundante y aburrido.
4. **Grabar la voz en off antes de montar la imagen.** Terminas forzando la imagen a la voz. Va al revés.
5. **Sobre-estabilizar.** Efecto gelatina, bordes que se deforman, y se pierde la sensación de real.
6. **Una sola canción de 8 minutos.** Sin cambio de música no hay estructura audible.
7. **Enterrar el sonido directo.** El ambiente real es lo que produce presencia; la música sola aplana.
8. **Fundido a negro entre cada momento.** Mata la energía y alarga el video sin aportar.
9. **Transiciones de plantilla** (zoom-blur, glitch) en cada corte.
10. **Empezar por el principio cronológico.** El desayuno no es un gancho. Arranca por el pico.
11. **Subtítulos de karaoke en vlog largo.** Lenguaje equivocado de formato.
12. **CTA agresivo al final.** Rompe el contrato de compañía que el formato construyó.
13. **No usar puentes de voz sobre las elipsis.** Cada salto se siente y el vlog se lee a colección de clips.

---

## Checklist

- [ ] Tres pasadas hechas: descarte → núcleos → armado
- [ ] De cada momento sobrevive el núcleo + 0,5 s de cada lado; el transporte se botó
- [ ] Entre 12 y 18 momentos en un vlog de 6–8 min
- [ ] El arranque es el pico del día, fuera de orden cronológico
- [ ] Hay al menos 3 valles claros; el ritmo tiene olas, no una meseta alta
- [ ] Cada elipsis tiene puente: voz que cruza, plano de traslado, match cut o corte al beat
- [ ] Ningún fundido a negro entre momentos
- [ ] Voz en off grabada DESPUÉS del esqueleto de imagen
- [ ] La voz en off aporta pensamiento, no descripción
- [ ] Silencios de 3–6 s entre bloques de voz
- [ ] 3–5 canciones; el cambio de canción coincide con cambio de bloque
- [ ] La música se calla o baja cuando pasa algo real
- [ ] Sonido directo audible por debajo, y por encima en los momentos de textura
- [ ] Estabilización solo donde el temblor distrae, con smoothing ≤ 20
- [ ] Rótulos de lugar/hora discretos; sin subtítulos de karaoke si es vlog largo
- [ ] Cierre tranquilo, CTA suave o ninguno
- [ ] Pasó `98-verificacion-del-corte.md`
