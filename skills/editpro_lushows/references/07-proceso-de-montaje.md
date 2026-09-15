# 07 — El proceso de montaje

Resuelve el desorden que hace que un video de dos horas de trabajo tome dos días. El montaje tiene
ocho fases, cada una con un objetivo único, y la regla que gobierna todo es: **no hagas en una fase lo
que pertenece a otra.** Corregir color mientras armas el corte bruto es la forma más eficiente de
perder el día.

---

## Las ocho fases

```
1. INGESTA        organizar el material y no perder nada
2. SELECCIÓN      decidir qué sirve, sin montar todavía
3. CORTE BRUTO    el orden y la estructura, feo pero completo
4. CORTE FINO     los cortes al décimo de segundo
5. SONIDO         voz, música, ambiente, niveles
6. COLOR          corregir primero, gradar después
7. GRÁFICOS       texto, rótulos, logo, motion
8. MÁSTER         exportar, verificar, entregar
```

El orden no es negociable por una razón mecánica: **cada fase invalida trabajo de las posteriores si se
hace después.** Si mueves un corte en la fase 4, todos los subtítulos que hiciste en la fase 7 se
desplazan. Si cambias la música en la fase 5, el ritmo de la 4 deja de calzar.

La única fase que se puede adelantar sin costo es la 1.

---

## Fase 1 — Ingesta

**Objetivo:** que el material esté completo, respaldado, nombrado y descrito. Nada más.

### Qué se hace

1. **Copiar todo a una estructura fija.** Una carpeta por proyecto, siempre igual:

```
proyecto/
  01-bruto/          material original, NUNCA se toca ni se renombra el archivo original
  02-audio/          audio externo, música, voz en off
  03-graficos/       logo, PNG con alfa, tipografías
  04-trabajo/        cortes intermedios, pruebas, proxies
  05-entrega/        los masters finales
  brief.md           el brief del modulo 02
  notas.md           decisiones y timecodes
```

2. **Verificar técnicamente cada archivo** antes de confiar en él:

```bash
# Inventario tecnico de toda la carpeta de bruto
for f in 01-bruto/*.mp4; do
  echo "=== $f"
  ffprobe -v error -show_entries format=duration -show_entries stream=codec_name,width,height,r_frame_rate,sample_rate,channels -of default=noprint_wrappers=1 "$f"
done
```

Lo que estás buscando: resoluciones mezcladas, fps distintos (23,976 con 30 es un dolor), audio faltante,
clips corruptos, rotación por metadato.

3. **Respaldar.** El bruto en dos sitios distintos antes de tocar nada. Si el material es irrepetible
   —un evento, una entrevista con alguien difícil de conseguir— esto no es opcional.

### Qué NO se hace en la fase 1

- **No se corta nada.** Ni "solo este pedacito que ya sé que sirve".
- **No se renombran los archivos originales.** Si el nombre es horrible, se crea un índice; el original
  conserva su nombre para poder rastrearlo.
- **No se convierte todo "por si acaso".** Solo se hacen proxies (copias livianas para trabajar) si el
  material es tan pesado que no se puede manipular.

---

## Fase 2 — Selección

**Objetivo:** saber qué hay y qué sirve. Sigue sin haber línea de tiempo.

### Qué se hace

1. **Hoja de contactos de todo el material** (ver `04`, `17`):

```bash
ffmpeg -hide_banner -i 01-bruto/clip01.mp4 -vf "fps=1/2,scale=320:-1,tile=6x8" -frames:v 1 contactos_clip01.png
```

2. **Transcribir con timecodes** todo lo que tenga voz (ver `13`). La transcripción con tiempos es el
   documento más importante del proyecto: convierte el video en texto buscable.

3. **Marcar en `notas.md`** los momentos buenos con su segundo exacto:

```
clip03  s=112.4  "el plato que mas vendo era el que me estaba quebrando"  <- GANCHO
clip03  s=147.0  se rie despues de equivocarse, muy natural
clip05  s=8.2    plano detalle manos emplatando, limpio, 6 s utiles
clip07  s=0-30   INUTIL, movido y desenfocado
clip09  s=41.5   dice el precio mal (dice 15 en vez de 10) -> NO USAR
```

4. **Decidir la estructura** con base en lo que hay, no en lo que te imaginaste (ver `12`, `32`).

### Qué NO se hace en la fase 2

- **No se monta.** La tentación de "voy armando mientras reviso" produce el video que se te ocurrió en
  el clip 2, no el mejor posible.
- **No se descarta material por calidad técnica sin ver el contenido.** Un plano movido con la mejor
  frase del proyecto se salva con reencuadre y estabilización; una frase mediocre en 4K no se salva.

---

## Fase 3 — Corte bruto

**Objetivo:** que la historia esté completa y en orden. Que se vea horrible es correcto en esta fase.

### Qué se hace

1. Poner los pedazos elegidos **en orden**, uno detrás de otro, con cortes duros.
2. Comprobar que la estructura funciona: gancho, cuerpo, remate (ver `32`).
3. Comprobar la duración aproximada. Si el bruto da 90 s y el objetivo son 30, hay que decidir qué se
   cae **ahora**, no después de haberlo pulido.
4. **Validar todos los cortes de una sola vez antes de armar** (ver `16`): que cada tramo exista de
   verdad en el clip, que no parta palabras, que la duración cuadre.

El error clásico que este paso previene: pedir el tramo 45–52 s de un clip que dura 40 s. Se descubre
al renderizar y hay que rehacer.

```bash
# Comprobar que un tramo existe antes de cortarlo
ffprobe -v error -show_entries format=duration -of csv=p=0 01-bruto/clip03.mp4
```

### Qué NO se hace en la fase 3

- **No se corrige color.** Ninguno. Ni "solo este que está muy oscuro".
- **No se ponen subtítulos.** Se van a mover todos.
- **No se elige música definitiva.** Se puede poner una temporal para sentir el ritmo, marcada como
  temporal.
- **No se buscan transiciones.** Todo va con corte duro.
- **No se pulen los cortes al fotograma.** Eso es fase 4.

**Prueba de que el corte bruto está listo:** puedes verlo entero y entender la pieza, aunque se vea
fea. Si no se entiende, no sigas a la fase 4 — el problema es de estructura y pulir no lo arregla.

---

## Fase 4 — Corte fino

**Objetivo:** el ritmo. Aquí se gana o se pierde el video.

### Qué se hace

1. **Ajustar cada corte al décimo de segundo.** Entradas y salidas exactas (ver `15`).
2. **Quitar respiraciones, muletillas, silencios muertos.** Aquí es donde el video de 45 s se vuelve
   de 28 s sin perder nada.
3. **Meter J-cuts y L-cuts** donde el corte se siente brusco (ver `21`).
4. **Medir el ritmo** y compararlo con el rango del formato (ver `20`):

```bash
ffmpeg -hide_banner -i 04-trabajo/corte_fino.mp4 -filter:v "select='gt(scene,0.25)',showinfo" -f null - 2>&1 | grep -c pts_time
```

5. **Punch-ins y reencuadres** para crear variedad de plano sin más material (ver `22`).
6. **Ver mudo y ver a ciegas** (ver `04`). Los dos, completos.

### Qué NO se hace en la fase 4

- **No se agrega material nuevo.** Si al pulir descubres que falta algo, vuelves a la fase 2 a
  buscarlo. No lo improvises.
- **Sigue sin haber color, ni subtítulos, ni gráficos.**

**Prueba de que el corte fino está listo:** lo ves mudo y se entiende; lo oyes sin ver y no hay
palabras partidas ni baches. **Aquí se congela el corte.** A partir de ahora, mover un corte cuesta
rehacer trabajo de tres fases.

---

## Fase 5 — Sonido

**Objetivo:** que se oiga profesional. Es la fase de mayor retorno por hora invertida y la que más se
salta la gente.

### Qué se hace, en este orden

1. **Limpiar la voz** — ruido, zumbido, golpes (`71`).
2. **Ecualizar** — cuerpo, presencia, quitar retumbe (`72`).
3. **Comprimir** — que las partes suaves y fuertes se acerquen (`73`).
4. **Poner el lecho de ambiente** — un fondo continuo que tape los cambios entre clips (`77`).
5. **Música** — elegida, cortada, con final resuelto (`74`).
6. **Ducking** — la música se agacha bajo la voz automáticamente (`75`).
7. **Diseño sonoro** — golpes, whooshes, risers, con moderación (`76`).
8. **Loudness final** — llevar a la norma de la plataforma (`73`).

La cadena completa está en `70-cadena-de-voz-profesional.md`. El orden importa: comprimir antes de
ecualizar da un resultado distinto (y peor) que al revés.

Medición final obligatoria:

```bash
ffmpeg -hide_banner -i 04-trabajo/con_sonido.mp4 -af loudnorm=I=-14:TP=-1.5:LRA=11:print_format=summary -f null -
```

### Qué NO se hace en la fase 5

- **No se mueve ningún corte.** El corte está congelado.
- **No se "arregla" una voz mala con más procesamiento.** Hay un punto donde más procesamiento
  empeora. Si la voz está irrecuperable, se regraba o se usa otra toma.
- **No se limpia el ruido al 100%.** Una voz sin nada de ambiente suena a robot metido en una caja.
  Ver `71`.

---

## Fase 6 — Color

**Objetivo:** que todos los planos se sientan del mismo video, y luego que tengan el look definido.

### Qué se hace, en este orden estricto

1. **Corregir**: exposición, balance de blancos, contraste. La meta es una imagen neutra y correcta,
   no bonita (`61`).
2. **Emparejar planos** entre sí. El plano de la terraza y el de la cocina tienen que sentirse del
   mismo día (`62`).
3. **Revisar la piel.** El error más común y más visible: piel verdosa o naranja (`67`).
4. **Gradar**: aplicar el look, o forzar la paleta de marca con duotono (`63`, `64`).
5. **Verificar con scopes**, no con el ojo (`69`):

```bash
# Forma de onda (luma) para ver si hay zonas quemadas o aplastadas
ffmpeg -i 04-trabajo/color.mp4 -vf "waveform=mode=column:display=overlay" -frames:v 1 waveform.png
# Vectorscopio para ver el balance de color y la linea de tono de piel
ffmpeg -i 04-trabajo/color.mp4 -vf "vectorscope=mode=color4" -frames:v 1 vectorscope.png
```

### Qué NO se hace en la fase 6

- **No se grada antes de corregir.** Aplicar un LUT sobre material mal expuesto amplifica el error.
- **No se corrige plano por plano sin tener una referencia.** Se elige un plano de referencia (el
  mejor) y todos se emparejan contra ese.
- **No se confía en el monitor.** El monitor miente; los scopes no.

---

## Fase 7 — Gráficos

**Objetivo:** texto, rótulos, logo, animaciones. Va de penúltimo por una razón: **todo esto se
desplaza si mueves un corte.**

### Qué se hace

1. **Subtítulos o palabras clave**, según lo decidido en el brief (`41`).
2. **Rótulos** para presentar personas o dar datos (`48`).
3. **Marca**: logo, firma, colores (`87`).
4. **Motion**: animaciones, gráficos de datos (`84`, `86`).
5. **Verificar zona segura** de la plataforma destino (`45`).

Los subtítulos se generan sobre el **corte fino ya congelado**, con los timecodes del render de esa
fase — no sobre el bruto.

```bash
# Quemar subtitulos ASS respetando estilos
ffmpeg -i 04-trabajo/color.mp4 -vf "ass=subs/reel.ass" -c:v libx264 -crf 18 -c:a copy 04-trabajo/con_texto.mp4
```

### Qué NO se hace en la fase 7

- **No se cambia el corte.** Ni un fotograma.
- **No se pone el logo en la esquina "porque sí".** Si va, va con criterio y sin tapar nada.
- **No se ponen subtítulos que tapen la zona segura.** Se mide, no se calcula a ojo.

---

## Fase 8 — Máster

**Objetivo:** el archivo que se entrega, verificado.

### Qué se hace

1. **Exportar con los parámetros de la plataforma destino** (`91`, `92`).
2. **Verificar el archivo exportado** — la fase entera está en `98-verificacion-del-corte.md`.
3. **Nombrar bien** (`96`):

```
gastrolatam_calculadora_plato-perdida_9x16_v3_2026-08-04.mp4
```

4. **Generar las adaptaciones** de formato si se necesitan (`38`).
5. **Archivar** lo que hay que guardar y botar lo que no (`97`).

### Qué NO se hace en la fase 8

- **No se hacen cambios creativos.** Si en esta fase quieres cambiar algo, o vuelves a la fase que
  corresponde o lo dejas para la versión siguiente. Cambiar en el máster es como se producen los
  archivos donde el audio no cuadra con la imagen.
- **No se entrega sin verificar.** Nunca.

---

## El costo de saltarse el orden

Números reales de por qué esto importa, sobre un reel de 30 segundos:

| Lo que hiciste mal | Lo que cuesta |
|---|---|
| Subtitulaste antes de cerrar el corte fino | rehacer los 14 bloques de subtítulo: ~40 min |
| Corregiste color en el corte bruto | corregiste 8 planos y usaste 5: ~25 min botados |
| Elegiste música definitiva antes del corte fino | el ritmo se armó contra esa música; cambiarla = rehacer fase 4 |
| No verificaste que el tramo existía | render fallido, diagnóstico, recorte: ~20 min |
| No respaldaste el bruto y se borró la tarjeta | el proyecto entero |

---

## Cuándo se puede comprimir el proceso

Con honestidad: no todo proyecto merece ocho fases formales. Un reel de 15 s con tres clips se hace en
un pase de 20 minutos. Se pueden fusionar las fases 1 con 2, 5 con 6 si el material es homogéneo, y 7
con 8 si no hay motion. Lo que **nunca** se comprime, ni en el proyecto más pequeño: ver todo el
material antes de decidir, congelar el corte antes de poner texto, corregir antes de gradar, y
verificar el render final.

---

## Errores comunes

- **Montar mientras se revisa el material.** Produce el video que se te ocurrió primero.
- **Corregir color en el corte bruto.** Corriges planos que después botas.
- **Poner subtítulos antes de congelar el corte.** Se desplazan todos.
- **Elegir la música definitiva antes del corte fino.** Encadena el ritmo a una decisión provisional.
- **Renombrar los archivos originales.** Pierdes la trazabilidad con la tarjeta y con quien grabó.
- **No respaldar el bruto antes de trabajar.** El único error de esta lista que es irreversible.
- **Descartar un clip por calidad técnica sin oír lo que dice.** La mejor frase suele estar en el peor plano.
- **Agregar material nuevo en el corte fino.** Si falta algo, se vuelve a la fase 2.
- **Aplicar un LUT antes de corregir la exposición.** Amplifica el error en vez de arreglarlo.
- **Juzgar el color en el monitor** en vez de en los scopes, o **limpiar el ruido de la voz al máximo**
  (queda una voz muerta dentro de una caja).
- **Hacer cambios creativos en la fase de máster** o **entregar sin correr la verificación de `98`**.

---

## Checklist

Una casilla por fase, antes de pasar a la siguiente:

- [ ] **Ingesta** — todo copiado en la estructura, respaldado en dos sitios, `ffprobe` corrido sobre
      todo (resoluciones, fps, audio, rotaciones), y ningún archivo original renombrado.
- [ ] **Selección** — hoja de contactos hecha, voz transcrita con timecodes, `notas.md` con los
      momentos buenos por segundo exacto y los descartes con su razón, estructura decidida **después**
      de ver todo.
- [ ] **Corte bruto** — todos los tramos validados como existentes, la pieza se entiende entera aunque
      se vea fea, duración en el orden del objetivo, sin tocar color ni texto ni transiciones.
- [ ] **Corte fino** — cortes al décimo de segundo, respiraciones y muletillas fuera, J-cuts donde
      hacía falta, ritmo medido y en rango, visto mudo y oído a ciegas. **Corte congelado.**
- [ ] **Sonido** — cadena de voz completa en orden, lecho de ambiente continuo, ducking calibrado,
      LUFS integrados y pico real medidos contra la norma de la plataforma.
- [ ] **Color** — corregido antes de gradar, todos los planos emparejados contra uno de referencia,
      piel revisada en el vectorscopio, verificado con scopes y no con el ojo.
- [ ] **Gráficos** — subtítulos hechos sobre el corte congelado, todo el texto dentro de la zona segura
      medida en píxeles, marca puesta con criterio y no por inercia.
- [ ] **Máster** — exportado con los parámetros de la plataforma, verificación de `98` corrida
      completa, nombre según convención, archivo guardado.
