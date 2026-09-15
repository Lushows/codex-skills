# 26 — Continuidad

**Qué resuelve:** ese momento en que un video "se siente raro" y nadie sabe decir por qué. Casi siempre
es continuidad: la camisa cambió de posición, la luz saltó de tarde a noche, la persona estaba mirando
a la izquierda y ahora mira a la derecha. Este módulo te enseña qué mirar, cómo detectarlo y — más
importante — cómo taparlo cuando ya no puedes volver a grabar.

---

## 1. Qué es la continuidad

> **Continuidad (o raccord):** que los elementos de la escena se mantengan coherentes de un plano al
> siguiente. Si en el plano A tiene el vaso en la mano derecha, en el plano B sigue en la derecha.

El espectador no lleva una lista mental. Lo que hace su cerebro es más traicionero: registra la
inconsistencia sin identificarla, y la traduce en una sensación de "esto no me convence". En un video de
ventas eso se paga en desconfianza.

**La regla honesta de 2026:** en video para redes, la continuidad importa menos que hace veinte años —
el jump cut es aceptado y hasta esperado. Pero hay cinco tipos de error que **siguen doliendo** y son de
los que trata este módulo.

---

## 2. Los cinco tipos de continuidad que importan

### a) Luz

El más grave y el que menos se puede arreglar. Si grabaste a las 5 de la tarde y volviste a las 6:30, la
temperatura de color cambió completamente: el material de la tarde es cálido y el de después es azul.

**Cómo se detecta:** compara fotogramas de los dos bloques lado a lado.

```bash
ffmpeg -hide_banner -ss 4 -i bloqueA.mp4 -frames:v 1 a.png
ffmpeg -hide_banner -ss 4 -i bloqueB.mp4 -frames:v 1 b.png
ffmpeg -hide_banner -i a.png -i b.png -filter_complex hstack comparacion.png
```

Un vistazo a `comparacion.png` y lo ves. Para medirlo en vez de mirarlo:

```bash
ffmpeg -hide_banner -i bloqueA.mp4 -vf "signalstats,metadata=print:key=lavfi.signalstats.YAVG" -f null - 2>&1 | head -5
```

`YAVG` es el brillo promedio. Si un bloque da 118 y el otro 76, tienes un salto de exposición fuerte.

**Cómo se arregla:** emparejando color (módulo `62`). Se ajusta el bloque que está peor hacia el que
está mejor, no al revés:

```bash
ffmpeg -hide_banner -y -i bloqueB.mp4 \
  -vf "eq=brightness=0.06:contrast=1.04:saturation=1.08,colortemperature=temperature=5200" \
  -c:v libx264 -crf 18 -c:a copy bloqueB_emparejado.mp4
```

Ajusta los valores comparando fotogramas hasta que los dos `YAVG` queden a menos de 10 puntos.

### b) Ropa y aspecto

Camisa arremangada en un plano y bajada en el siguiente. Pelo peinado y despeinado. Un botón abierto.
Maquillaje que cambió.

**Cómo se detecta:** la grilla de fotogramas es la herramienta.

```bash
ffmpeg -hide_banner -i toma_completa.mp4 -vf "fps=0.5,scale=200:-1,tile=8x6" -frames:v 1 revision.png
```

Un fotograma cada 2 segundos, todo en una imagen. Los cambios de aspecto saltan a la vista.

**Cómo se tapa:** con un cutaway o inserto entre los dos planos (sección 5).

### c) Posición y props

El vaso estaba lleno y ahora está a la mitad. Estaba a la izquierda de la mesa y ahora a la derecha. La
persona estaba de pie y ahora sentada sin que la veamos sentarse.

**Regla práctica:** los props que están **en la mano** o **en primer plano** importan; los del fondo, no.
Nadie va a notar que la silla del fondo se movió 20 cm. Todo el mundo nota que el vaso cambió de mano.

### d) Eje (la línea imaginaria)

> **Eje (o línea de los 180°):** una línea imaginaria que conecta a los dos sujetos de una escena — o
> que marca la dirección en la que mira una persona. Todas las cámaras tienen que quedarse **del mismo
> lado** de esa línea.

```
        Persona A  ●───────────────● Persona B
                  ╱        eje       ╲
        [cám 1]  ✅        ✅ [cám 2]
                  ─────────────────────
                       ❌ [cám 3]   ← cruzó el eje
```

Si cruzas el eje, en el plano siguiente A parece estar mirando hacia el mismo lado que B, y el
espectador entiende que ya no se están hablando entre ellos. Es desorientador y funciona incluso cuando
el espectador no sabe nada de esto.

**Dónde te va a morder en la práctica:**
- Entrevista con dos cámaras: si una está a un lado y otra al otro, el entrevistado "cambia de lado" a
  cada corte.
- Talking head donde la persona mira levemente a la izquierda en un bloque y a la derecha en otro.
- Un corte por mirada (módulo `21`) donde el objeto aparece del lado contrario al que se miraba.

**Cómo se arregla en post:** volteando el plano horizontalmente.

```bash
ffmpeg -hide_banner -y -i plano_cruzado.mp4 -vf "hflip" -c:v libx264 -crf 18 -c:a copy plano_corregido.mp4
```

**Cuidado:** `hflip` voltea TODO. Si hay texto en cuadro (una etiqueta, un letrero, un logo), queda al
revés y el arreglo es peor que el problema. Revisa un fotograma antes de aceptarlo.

### e) Dirección de movimiento

Si alguien sale de cuadro por la derecha, en el plano siguiente tiene que entrar por la izquierda. Si
entra también por la derecha, el cerebro entiende que se devolvió.

Lo mismo con los objetos: un carro que va hacia la derecha sigue yendo hacia la derecha en el siguiente
plano, salvo que quieras comunicar que se devolvió.

**Aplicación cotidiana:** en un video de producto, si la mano entra por la derecha en un plano, que
entre por la derecha en todos. Es un detalle que nadie nota cuando está bien y todo el mundo siente
cuando está mal.

---

## 3. La jerarquía honesta: qué importa de verdad

No todos los errores de continuidad cuestan lo mismo. En orden de gravedad para video de redes:

| Gravedad | Error | Por qué |
|---|---|---|
| 🔴 Alta | **Salto de luz/color** entre bloques | Se lee como "dos videos pegados" |
| 🔴 Alta | **Cruce de eje** en escena con dos personas | Desorienta de verdad |
| 🟠 Media | **Prop en la mano** que cambia | Se nota si está en primer plano |
| 🟠 Media | **Ropa** muy distinta | Se nota sobre todo en talking head |
| 🟡 Baja | **Dirección de entrada/salida** | Se siente, no se identifica |
| 🟢 Nula | Fondo, elementos lejanos, sombras | Nadie los ve |

**No pierdas una hora arreglando algo verde.** Ese tiempo vale más metido en el gancho.

---

## 4. Detectar problemas antes de montar

El momento correcto de revisar continuidad es **antes** de armar, no después. Dos herramientas:

### La hoja de contactos completa

```bash
ffmpeg -hide_banner -i bruto.mp4 -vf "fps=0.5,scale=180:-1,tile=10x8" -frames:v 1 contactos.png
```

Ochenta fotogramas de todo el material en una imagen. Todos los cambios de ropa, de luz y de posición
se ven de un vistazo.

### Comparar los extremos de cada corte planificado

Antes de cortar, saca el último fotograma del plano A y el primero del plano B:

```bash
ffmpeg -hide_banner -ss 2.30 -i toma.mp4 -frames:v 1 salida_A.png
ffmpeg -hide_banner -ss 3.20 -i toma.mp4 -frames:v 1 entrada_B.png
ffmpeg -hide_banner -i salida_A.png -i entrada_B.png -filter_complex hstack corte_01.png
```

Esa imagen te dice en dos segundos si el corte va a saltar. Hazlo para los cortes dudosos, no para todos.

---

## 5. Cómo tapar un salto (la parte útil)

Ya está grabado, no se puede repetir, y hay un salto. Cinco soluciones de menor a mayor esfuerzo.

### Solución 1 — Punch-in (la primera que debes intentar)

Cambiar el encuadre en el segundo plano hace que el cerebro atribuya la diferencia al cambio de cámara,
no al error.

```bash
ffmpeg -hide_banner -y -ss 3.20 -to 6.40 -i toma.mp4 \
  -vf "scale=1242:2208:flags=lanczos,crop=1080:1920,fps=30,setsar=1" \
  -c:v libx264 -crf 18 -c:a aac planoB_punch.mp4
```

Cubre: ropa levemente distinta, posición del cuerpo, jump cuts. **No cubre** un salto de luz fuerte ni
un cambio de prop en primer plano.

### Solución 2 — Cutaway o inserto de 1–2 s

Metes un plano de otra cosa entre los dos planos problemáticos. Cuando vuelves, el espectador ya no
tiene el fotograma anterior fresco en la memoria y no compara.

```bash
ffmpeg -hide_banner -y -ss 8.0 -t 1.6 -i broll.mp4 -an \
  -vf "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,setsar=1" \
  -c:v libx264 -crf 18 -pix_fmt yuv420p tapa.mp4
```

Cubre: casi todo, incluidos cambios de ropa y de posición. Es la solución universal.
Requiere: tener b-roll. Si no lo tienes, grábalo ahora mismo con el celular: 5 segundos de un objeto
relacionado sirven.

**Duración mínima para que funcione: 1 segundo.** Menos de eso y el espectador conserva la comparación.

### Solución 3 — Elemento gráfico a pantalla completa

Un texto grande, una tarjeta de marca, un número de sección. Ocupa la pantalla 0,8–1,5 s y borra el
recuerdo visual.

```bash
ffmpeg -hide_banner -y -f lavfi -i color=c=0x0F3D2E:s=1080x1920:d=1.2:r=30 \
  -vf "drawtext=fontfile=/c/Windows/Fonts/arialbd.ttf:text='Paso 2':fontcolor=white:fontsize=140:x=(w-text_w)/2:y=(h-text_h)/2" \
  -c:v libx264 -crf 18 -pix_fmt yuv420p tarjeta.mp4
```

Cubre: todo. Es lo más contundente.
Costo: rompe el flujo. Úsalo cuando de verdad haya un cambio de sección, no para tapar cualquier cosa —
si no, el video queda lleno de tarjetas que no significan nada.

### Solución 4 — Corte por acción

Si en los dos planos hay movimiento, corta a mitad del gesto. El ojo persigue el movimiento y no tiene
capacidad libre para comparar detalles.

Cubre: mucho más de lo que parece. Es el mecanismo del montaje invisible.
Requiere: que haya movimiento disponible.

### Solución 5 — Emparejar color (solo para saltos de luz)

Ver sección 2a. Es la única que arregla el problema en vez de esconderlo.

### Tabla de decisión

| El salto es de… | Solución |
|---|---|
| Luz / color | **Emparejar color** (5) — las demás no lo tapan |
| Posición del cuerpo | Punch-in (1) |
| Ropa | Cutaway (2) |
| Prop en la mano | Cutaway (2) — el punch-in no basta |
| Jump cut de condensación | Punch-in (1) |
| Cruce de eje | `hflip` si no hay texto; si hay, cutaway (2) |
| Cambio de sección real | Elemento gráfico (3) |
| Hay movimiento en los dos planos | Corte por acción (4) |

---

## 6. La continuidad de audio (la que se olvida)

Nadie revisa esto y es la que más delata.

- **Ruido de fondo distinto.** Si un bloque se grabó con el aire acondicionado prendido y otro no, al
  cortar entre ellos se oye el "on/off" del ambiente. Es muy evidente.
- **Volumen distinto.** La persona se acercó al micrófono en un bloque.
- **Reverberación distinta.** Se grabó en dos cuartos.

**La solución universal:** una **cama de ambiente** — un fondo sonoro continuo a bajo volumen que
atraviesa todo el video y homogeniza los saltos.

```bash
# 1) Grabar/extraer 10 s de ambiente limpio de la locación
ffmpeg -hide_banner -y -ss 30 -t 10 -i toma.mp4 -vn -af "volume=-30dB" -c:a pcm_s16le ambiente.wav

# 2) Repetirlo bajo todo el video
ffmpeg -hide_banner -y -i video.mp4 -stream_loop -1 -i ambiente.wav \
  -filter_complex "[0:a][1:a]amix=inputs=2:duration=first:normalize=0[a]" \
  -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k video_con_cama.mp4
```

A -30 dB nadie la oye conscientemente, pero los saltos de ambiente desaparecen. Es de las cosas que más
suben la percepción de calidad por menos esfuerzo.

También: **verifica el nivel de cada bloque** antes de unir.

```bash
ffmpeg -hide_banner -i bloqueA.mp4 -af "loudnorm=print_format=summary" -f null - 2>&1 | grep "Input Integrated"
```

Si un bloque marca -19 LUFS y otro -13 LUFS, normalízalos antes de unir (módulo `73`).

---

## 7. Cuándo la continuidad NO importa

Sé honesto y no pierdas tiempo:

- **Montaje de tipo "lista" o "collage".** Cinco clips de cinco días distintos con cinco camisas
  distintas: nadie espera continuidad ahí. El formato lo comunica solo.
- **Contenido de creador / UGC.** La discontinuidad es parte del código de "esto lo grabé yo". Pulirla
  de más le quita autenticidad y le baja la conversión.
- **Antes y después.** El cambio de aspecto **es** el contenido.
- **Bloopers.** Ver módulo `34`.

En estos casos, lo único que sigue importando es el **color** y el **ambiente sonoro**, porque esos dos
se leen como calidad técnica, no como continuidad narrativa.

---

## Errores comunes

1. **Revisar continuidad después de montar.** Se revisa sobre el bruto, con la hoja de contactos, antes
   de cortar. Encontrarlo después te obliga a re-montar.
2. **Intentar tapar un salto de luz con un cutaway.** No funciona: el cutaway también está iluminado y
   al volver el salto sigue ahí. La luz se arregla con color, punto.
3. **Cutaways de menos de 1 segundo para tapar.** No borran la comparación visual. Mínimo 1 s.
4. **Usar `hflip` en un plano con texto en cuadro.** El logo o el letrero quedan espejados y el arreglo
   se ve peor que el problema. Revisa un fotograma antes.
5. **Perseguir errores de continuidad del fondo.** La silla que se movió, la sombra que cambió: nadie
   los ve. Ese tiempo va al gancho.
6. **Ignorar la continuidad de audio.** El salto de ruido de fondo se oye más de lo que se ve un cambio
   de camisa. La cama de ambiente lo resuelve en cinco minutos.
7. **Cruzar el eje en una entrevista de dos cámaras.** El entrevistado "cambia de lado" a cada corte y
   el espectador se desorienta sin saber por qué.
8. **Aplicar reglas de continuidad de cine a un video de redes.** Un jump cut no es un error en 2026.
   Sabe cuál convención estás usando.
9. **Emparejar el bloque bueno hacia el malo.** Siempre se lleva el peor hacia el mejor, no al revés.
10. **Meter tarjetas gráficas cada vez que hay un salto.** Terminas con un video lleno de rótulos que no
    significan nada. La tarjeta se reserva para cambios de sección reales.

---

## Checklist

- [ ] Saqué la **hoja de contactos** del bruto y revisé cambios de ropa, luz y posición **antes** de
      montar.
- [ ] Medí el **brillo promedio (YAVG)** de cada bloque; ninguno difiere más de ~10 puntos del resto.
- [ ] Comparé fotogramas lado a lado en los **cortes dudosos**.
- [ ] Los props **en la mano o en primer plano** se mantienen coherentes entre planos.
- [ ] No hay **cruce de eje** en escenas con dos personas o con corte por mirada.
- [ ] La **dirección de entrada y salida** de cuadro es coherente.
- [ ] Cada salto que quedó está **tapado con la solución correcta** según la tabla (no con lo primero
      que se me ocurrió).
- [ ] Los cutaways de tapado duran **al menos 1 segundo**.
- [ ] Si usé `hflip`, verifiqué que **no hay texto ni logo** en cuadro.
- [ ] Revisé la **continuidad de audio**: mismo ruido de fondo, mismo nivel, misma reverberación.
- [ ] Hay una **cama de ambiente** a ~-30 dB si el material viene de sesiones distintas.
- [ ] Medí los **LUFS de cada bloque** y están emparejados antes de unir.
- [ ] Si el formato es collage / UGC / antes-y-después, **no gasté tiempo** en continuidad narrativa,
      solo en color y audio.
