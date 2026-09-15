# 188 — Volumen y escala

Pasar de 4 piezas al mes a 40 no es hacer diez veces lo mismo. Si intentas escalar haciendo cada pieza
como la primera, a las 15 piezas estás trasnochando, a las 25 estás entregando mal, y a las 40
quebraste — con más facturación que nunca y menos plata que antes.

El volumen no se resuelve con más horas ni, principalmente, con más gente. Se resuelve con **pipeline**:
un sistema donde el trabajo pasa por estaciones, cada decisión se toma una vez, y lo repetible está
codificado. Ese pipeline, además, es tu ventaja competitiva más difícil de copiar.

---

## Por qué la escala rompe lo que funcionaba

A 4 piezas al mes, el desorden es gratis. Buscas un archivo, no encuentras un LUT, rehaces un título:
son 20 minutos y no pasa nada.

**A 40 piezas al mes, cada minuto de fricción se multiplica por 40.** Diez minutos perdidos por pieza
buscando material son 6 horas y media al mes. Rehacer un título por pieza son 8 horas. La fricción que
no se notaba se vuelve el negocio entero.

**Las tres cosas que se rompen primero, en orden:**

1. **Encontrar el material.** A 40 piezas manejas cientos de archivos de media docena de clientes.
2. **Recordar el estándar de cada cliente.** Cuál tipografía, cuál LUT, cuál llamado a la acción.
3. **Saber en qué va cada cosa.** Sin un tablero, vives revisando WhatsApp para saber qué falta.

---

## Los cuatro principios del pipeline

### 1. Por lotes, no por pieza

**Nunca hagas una pieza de principio a fin y después la siguiente.** El costo de cambiar de contexto —
de mentalidad, de software, de cliente — es enorme y no se ve en ninguna estimación.

Se trabaja por **estaciones**: haces la misma tarea para las 8 piezas, y después pasas a la siguiente
tarea.

```
LUNES     Ingesta + organización de TODOS los clientes del ciclo        (2 h)
LUNES     Transcripción + minería de TODO el material                   (2 h)
MARTES    Selección de tomas de las 8 piezas                            (3 h)
MIÉRCOLES Montaje de las 8 piezas, una tras otra                        (6 h)
JUEVES    Subtítulos de las 8 + revisión                                (2 h)
JUEVES    Color y audio de las 8, con LUT y cadena ya armadas           (2 h)
VIERNES   Exportación, versiones y entrega                              (1,5 h)
```

**Por qué funciona:** en la estación de montaje ya tienes la cabeza puesta en montar, los atajos en los
dedos, el material fresco de la minería. Las piezas 5 a 8 te toman la mitad que la 1 y la 2.

**Medición real que puedes hacer esta semana:** cronometra 4 piezas hechas de punta a punta una por una,
y 4 piezas hechas por estaciones. La diferencia típica está entre 25% y 40% de tiempo. Esa es tu primera
gran ganancia de escala y no cuesta un peso.

### 2. Decide una vez, aplica muchas

Cada decisión creativa que tomas debe quedar **capturada** en algo reutilizable.

| Decisión | Dónde queda capturada |
|---|---|
| Cómo se ven los subtítulos de este cliente | plantilla .ass o preset de título (`43`, `44`) |
| Cómo se ve la imagen de este local | LUT o nodo de corrección guardado (`65`) |
| Cómo suena la voz | cadena de audio guardada como preset (`70`–`73`) |
| Cómo empieza y termina cada pieza | plantilla de proyecto con las capas armadas |
| Qué música usa esta marca | carpeta de 20 pistas ya filtradas y aprobadas |
| Qué NO se hace nunca | manual de una página (`185`) |

**Un cliente sin plantilla no es un cliente escalable.** La primera pieza de cada cliente nuevo debe
producir su plantilla; es parte del trabajo, no algo extra.

### 3. Nombra todo, siempre igual

Una convención de nombres estricta es lo que convierte "buscar el archivo" en "abrir el archivo".

```
CLIENTE_AAAAMMDD_PIEZA_VERSION.ext

benditapola_20260804_reel03_v2.mp4
gastrolatam_20260804_reel01_FINAL.mp4
```

Nunca "final_final_v2_bueno.mp4". Detalle completo en `96`.

**Estructura de carpetas idéntica para todos los clientes:**

```
/CLIENTE
  /00_bruto
  /01_seleccion
  /02_proyecto
  /03_assets      (logo, tipografías, plantillas, LUT)
  /04_musica
  /05_exportes
  /06_entregado
```

Idéntica. Siempre. Así, cualquier persona (o tú dentro de 4 meses) encuentra cualquier cosa sin
preguntar. Ver `10`.

### 4. Lo que se puede automatizar, se automatiza

Todo lo que hagas más de tres veces igual es candidato a un script.

```bash
# Normaliza loudness a -14 LUFS y exporta todos los MP4 de una carpeta a la especificación de Reels
for f in *.mp4; do
  ffmpeg -i "$f" \
    -vf "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30" \
    -af "loudnorm=I=-14:TP=-1.5:LRA=11" \
    -c:v libx264 -profile:v high -crf 21 -pix_fmt yuv420p \
    -c:a aac -b:a 192k -movflags +faststart \
    "salida/${f%.mp4}_reels.mp4"
done
```

```bash
# Genera versión de revisión con timecode y marca de agua, para todas las piezas del lote
for f in *.mp4; do
  ffmpeg -i "$f" -i marca.png -filter_complex \
  "[0:v][1:v]overlay=W-w-30:30:format=auto,\
   drawtext=text='REVISION - NO PUBLICAR':fontsize=34:fontcolor=white@0.55:x=(w-tw)/2:y=h/2,\
   drawtext=timecode='00\:00\:00\:00':rate=30:fontsize=26:fontcolor=white:\
   box=1:boxcolor=black@0.6:x=w-tw-20:y=h-th-20" \
  -c:v libx264 -crf 22 -preset veryfast -c:a copy "rev/${f%.mp4}_REV.mp4"
done
```

```bash
# Verifica que todo el lote cumple especificación antes de entregar
for f in *.mp4; do
  echo "=== $f"
  ffprobe -v error -select_streams v:0 \
    -show_entries stream=width,height,r_frame_rate,codec_name -of csv=p=0 "$f"
  ffmpeg -i "$f" -af ebur128=framelog=quiet -f null - 2>&1 | tail -6 | grep -i "I:"
done
```

Ese último script te ahorra la vergüenza de entregar un video a 24 fps cuando el estándar del cliente es
30, o con el audio 6 dB más bajo que el resto del lote. En un lote de 40, revisarlo a mano es imposible.

---

## El cuello de botella se mueve, y hay que perseguirlo

Un sistema tiene un solo cuello de botella a la vez. Optimizar cualquier otra cosa no sirve de nada.

**Cómo encontrarlo:** durante dos semanas, anota cuánto tiempo real pasa cada pieza en cada estación,
incluyendo el tiempo que pasa **esperando** (que suele ser el mayor).

```
Pieza     Espera material  Ingesta  Selección  Montaje  Espera notas  Ajustes  Total
reel01    6 días           15 min   35 min     50 min   4 días        20 min   ← 10 días de espera
reel02    9 días           15 min   30 min     45 min   2 días        10 min
```

Casi siempre la respuesta sorprende: **el cuello de botella no es la edición, es la espera.** Esperar
material del cliente y esperar notas del cliente se comen el 70% del tiempo del ciclo.

**Y eso se ataca con proceso, no con velocidad de edición:**

- Fecha de corte de recepción de material (`184`)
- Plazo de notas con consecuencia escrita (`182`)
- Guía de grabación de una página para que el cliente grabe bien la primera vez
- Trabajar con un mes de adelanto: en agosto produces lo de septiembre

**El buffer de un mes es la mejora operativa más grande que existe en este oficio.** Convierte todas las
urgencias en trabajo normal y elimina el trasnocho estructural.

---

## Los tres saltos de volumen

### De 4 a 10 piezas/mes — el salto de sistema

Todavía lo haces todo tú. Lo que cambia:

- Trabajo por lotes, no por pieza
- Plantilla por cliente
- Nomenclatura y carpetas idénticas
- IA en transcripción y subtítulos (`189`, `124`)
- Un tablero simple (Trello, Notion o hasta una hoja de cálculo) con el estado de cada pieza

**No necesitas contratar a nadie para llegar a 10.** Si estás contratando a las 10 piezas, tu problema
es de sistema, no de manos.

### De 10 a 25 piezas/mes — el salto de delegación

Aquí sí entra otra persona, y entra por el nivel 1 de `185`: ingesta, transcripción, subtítulos,
exportaciones. Lo que cambia:

- Manual de una página por formato
- Revisión de tres puntos en vez de revisión completa
- Reunión semanal de coordinación
- Calendario de producción fijo, con las fechas de cada cliente escalonadas

**El escalonamiento es clave.** Si tus 6 clientes entregan material el día 1 y quieren todo el día 10,
tienes un pico imposible. Reparte: cliente A cierra el 25, cliente B el 5, cliente C el 15. Se negocia
al firmar, no después.

### De 25 a 40+ piezas/mes — el salto de rol

Aquí dejas de ser el que edita y pasas a ser el que decide y revisa. Lo que cambia:

- Dos o tres personas ejecutando, cada una con estaciones asignadas
- Tú haces: brief, ángulo, gancho, revisión, cliente
- Control de calidad automatizado (el script de verificación de arriba, corrido sobre todo el lote)
- Estándares escritos que sobreviven sin ti
- Un editor senior que revisa antes que tú

**Advertencia honesta:** este salto cambia tu oficio. Si te metiste a esto porque te gusta editar,
llegar a 40 piezas/mes significa dejar de editar. Mucha gente descubre en este punto que prefiere
quedarse en 15 piezas con márgenes altos y clientes buenos. **Esa es una decisión válida, no un
fracaso.** Ver `189`.

---

## El tablero: saber en qué va cada cosa

Sin esto, a partir de 15 piezas vives en modo de pánico buscando en WhatsApp qué falta.

Estados mínimos:

```
ESPERANDO MATERIAL → EN SELECCIÓN → EN MONTAJE → EN REVISIÓN INTERNA →
ENVIADO A CLIENTE → EN NOTAS → AJUSTES → ENTREGADO → PUBLICADO
```

Cada pieza es una tarjeta con: cliente, fecha comprometida, quién la tiene, y enlace a la carpeta.

**La regla que hace que el tablero funcione:** si no está en el tablero, no existe. Un pedido que llegó
por WhatsApp y no se convirtió en tarjeta se va a olvidar, y ese olvido es lo que quema la relación con
el cliente.

**Métrica semanal, cinco números:**

| Métrica | Qué te dice |
|---|---|
| Piezas entregadas | volumen real |
| Horas totales invertidas | costo real |
| Horas por pieza (promedio) | si el sistema está mejorando o empeorando |
| Piezas entregadas a tiempo (%) | salud de la operación |
| Piezas esperando material del cliente | dónde está atascado el negocio |

**Si horas-por-pieza no baja mes a mes, no estás escalando: estás corriendo más rápido.**

---

## La ventaja competitiva que nadie te puede copiar

Este es el punto que hace que valga la pena todo lo anterior.

Un competidor puede copiar tu precio en una tarde. Puede copiar tu estilo visual en un mes. Puede
contratar a tu editor.

**Lo que no puede copiar es tu pipeline**, porque no es un archivo: es la suma de decisiones ya tomadas,
plantillas ya afinadas contra el gusto real de cada cliente, scripts que ya atraparon todos los errores
que se pueden cometer, y un manual escrito con los tropiezos de 300 piezas.

**Cómo se ve esa ventaja en la práctica:**

- Puedes cotizar más barato por pieza y ganar más por hora que quien cotiza más caro.
- Puedes aceptar el trabajo urgente que los demás rechazan, y cobrar recargo por él.
- Puedes probar más variantes de gancho por el mismo costo, lo que mejora tus resultados, lo que
  mejora tus casos de estudio (`186`), lo que sube tu precio (`180`).
- Puedes contratar gente junior y producir a nivel senior.

**Y el círculo se cierra:** más volumen produce más datos sobre qué funciona; más datos producen mejor
criterio; mejor criterio produce mejores resultados; mejores resultados producen mejores precios. El
pipeline no es solo eficiencia — es la máquina de aprender.

---

## Los límites honestos del volumen

No todo escala, y forzar volumen donde no cabe destruye el negocio:

- **La calidad de criterio no escala linealmente.** La pieza 40 del mes recibe menos pensamiento que la
  pieza 4. Si tu producto es criterio, hay un techo real.
- **Los clientes que exigen mucha coordinación no caben en un pipeline.** Uno solo puede consumir el
  tiempo de coordinación de cinco. Identifícalo y súbele el precio o suéltalo.
- **El trabajo de dirección, narrativo o de marca no se lotea.** Se cotiza aparte y se hace aparte.
- **El volumen sin margen es una trampa.** 40 piezas a $80.000 con costos de $2.500.000 es peor negocio
  que 12 piezas a $400.000. Si al escalar tu tarifa efectiva por hora (`180`) baja, estás escalando en
  la dirección equivocada.

**El cálculo que hay que hacer antes de perseguir volumen:**

```
Escenario A: 12 piezas × $400.000 = $4.800.000   /  90 h  = $53.333/h
Escenario B: 40 piezas × $150.000 = $6.000.000   / 180 h  = $33.333/h  ← más plata, peor negocio
Escenario C: 40 piezas × $150.000 = $6.000.000   /  95 h  = $63.158/h  ← esto sí es escalar
```

C solo existe con pipeline. Sin pipeline, escalar te lleva siempre a B.

> **Frontera:** si la pregunta es cuánto puede crecer el negocio entero, qué estructura societaria
> soporta el crecimiento, o si conviene abrir una línea nueva, eso es `economist_lushows`. Aquí solo el
> problema operativo de producir más piezas sin morir.

---

## Errores comunes

- **Escalar contratando en vez de sistematizando.** Sumas costo fijo al desorden y multiplicas el caos.
- **Hacer las piezas una por una de principio a fin.** El costo de cambio de contexto es el impuesto
  invisible más caro del oficio.
- **No tener plantilla por cliente.** Rehacer decisiones ya tomadas, 40 veces al mes.
- **Nomenclatura improvisada.** "final_final_v3" a escala es tiempo perdido garantizado y errores de
  entrega.
- **Optimizar la edición cuando el cuello de botella es la espera del cliente.** Mides mal, arreglas lo
  que no era.
- **No trabajar con buffer.** Producir en el mes lo del mes te condena al trasnocho estructural.
- **Todos los clientes con la misma fecha de entrega.** Escalona los ciclos al firmar.
- **No tener tablero.** A partir de 15 piezas es imposible sostenerlo en la cabeza y en WhatsApp.
- **No medir horas por pieza.** Sin ese número no sabes si estás escalando o solo corriendo más.
- **Perseguir volumen sin verificar margen.** Más facturación con peor tarifa efectiva es un retroceso
  disfrazado de crecimiento.
- **Meter trabajo de dirección al pipeline de redes.** Sale mal y arruina la relación con el mejor
  cliente.
- **Asumir que escalar es lo que quieres.** A 40 piezas ya no editas. Decídelo a propósito.

---

## Checklist

- [ ] Trabajo por estaciones y por lotes, no pieza por pieza
- [ ] Cada cliente tiene plantilla de proyecto, LUT, cadena de audio y biblioteca de música
- [ ] La nomenclatura y la estructura de carpetas es idéntica para todos
- [ ] Tengo scripts para exportación por plataforma, versiones de revisión y verificación
- [ ] Medí dónde está el cuello de botella real, incluyendo tiempos de espera
- [ ] Ataqué la espera con fecha de corte de material y plazo de notas
- [ ] Estoy produciendo con al menos 2 semanas de buffer
- [ ] Los ciclos de mis clientes están escalonados, no todos el mismo día
- [ ] Tengo un tablero con estados y la regla de "si no está, no existe"
- [ ] Mido semanalmente: piezas, horas, horas/pieza, % a tiempo, piezas esperando material
- [ ] Horas por pieza está bajando mes a mes
- [ ] Verifiqué que mi tarifa efectiva por hora SUBE al escalar, no baja
- [ ] El trabajo de dirección y narrativo está fuera del pipeline de volumen
- [ ] Decidí a propósito hasta dónde quiero escalar
