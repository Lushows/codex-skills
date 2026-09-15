---
name: canales_lushows
description: Use when working on PAPER EMPIRES or any faceless documentary channel of Lushows — producing episodes (script, voice, visual script, collage montage, render), the visual language of the channel, the archive bank and its licensing, monetization and multi-language audio tracks, or the pipeline that turns a story into a finished video at zero cost. Triggers "Paper Empires", "canal de documentales", "historias de dinero", "el piloto", "el motor de montaje", "modo revista", "recortes de archivo", "guion visual", "locución del episodio", "pistas de idiomas", "canal faceless".
---

# canales_lushows — el sistema de PAPER EMPIRES

Canal de documentales cortos sobre **historias reales de dinero**: estafas, fortunas
e imperios que cayeron. Cada episodio cuenta el **arco completo** de una persona —
lo que construyó de verdad y el momento en que cruzó la raya.

- **Nombre:** Paper Empires · handle `@thepaperempires_co`
- **Lema:** *Cómo se construyen las fortunas. Y cómo se derrumban.*
- **Proyecto:** `Desktop\CANALES-LUSHOWS\piloto`
- **Coste de producción por episodio: $0.** Ninguna API de pago.

---

## ⛔ EL ORDEN DE TRABAJO (la regla que más se incumple)

**El desorden es el error caro de este proyecto.** Saltarse el orden obliga a rehacer
todo lo posterior, porque cada fase depende de la anterior. Se hace SIEMPRE así:

```
1. INVESTIGAR   → los hechos, las cifras, las fuentes. Sin esto no hay guion.
2. GUION        → texto cerrado, cronometrado, con las palabras clave marcadas.
3. VOZ          → locución completa en UNA pasada. Se aprueba ANTES de tocar imagen.
4. TIEMPOS      → alineación palabra por palabra sobre el audio ya aprobado.
5. MATERIAL     → archivo, recortes y recursos que el guion visual va a necesitar.
6. GUION VISUAL → la tabla de eventos, escrita entera antes de renderizar nada.
7. RENDER       → motor.py + acabar.py.
8. VERIFICAR    → medir, no opinar (§ Verificación).
```

**No se pasa de fase sin cerrar la anterior.** Si la voz cambia, los tiempos cambian
y el guion visual entero se descoloca: rehacer 4-7 cuesta una hora; aprobar la voz
primero cuesta cinco minutos.

**Para episodios largos:** trabajar en tramos de 1 minuto. Cerrar el minuto 1 entero
(voz + visual + render + visto bueno) antes de escribir el minuto 2.

---

## 🎬 Las reglas visuales del canal

### El lenguaje: collage de revista
Todo elemento va **pegado como papel**: margen crema grueso, sombra proyectada y un
ángulo que nunca es recto. Es lo que da el aire hecho a mano y, de paso, un foso
contra la política de contenido no auténtico.

| Regla | Por qué |
|---|---|
| **Opacidad SIEMPRE 1** | Un recorte de papel es opaco. Con 80% se transparenta lo de abajo y se lee como doble exposición, no como collage. Lo que deba pesar menos: más pequeño o detrás |
| **Fotos abiertas → recorte de tijera** | La segmentación falla justo en escenas con varias personas. Recortar un polígono irregular con borde grueso es más fiel al fanzine *y* no puede fallar |
| **Fotos de figura clara → recorte de silueta** | rembg + limpieza de alfa (umbral 150/205 + erosión 5 px). Sin la limpieza quedan figuras fantasma |
| **El recorte tiene que EMPATAR con el fondo** | Un soldado sobre un pasillo de juzgado no empata: se lee como error. Si no empata, no se usa |
| **Los fondos los hacemos nosotros** | Se construyen por código (HTML→Chrome). Las fotos de archivo van ENCIMA, en modo revista, no de fondo |
| **Cada elemento se explica** | Si en pantalla aparece algo que el espectador no puede identificar (una tuneladora, un plano), lleva rótulo. Un objeto sin explicar es ruido |
| **Nada tapa lo importante** | Un elemento nuevo no puede cubrir el que sostiene la frase |

### Jerarquía de tiempo = jerarquía de información
**El tiempo en pantalla se reparte por importancia, no por comodidad de montaje.**
Si la ficha del protagonista es más importante que el plano de contexto, dura más.
Revisar siempre: *¿lo que más dura es lo que más importa?*

### Movimiento
- Recorrido del fondo entre **8% y 16%**; sólo travellings intencionados pasan de ahí
- **Cambiar de dirección entre planos** (acercarse, alejarse, deriva). Si todos
  empujan igual, el ojo lo detecta a los tres planos
- **Nada quieto más de 2 s.** Una cifra fija 6 segundos mata el ritmo: se le da
  entrada, un gesto y salida
- Los elementos entran **0,1-0,2 s ANTES** de su palabra. Justo a tiempo llega tarde

### Color y exposición
El canal es oscuro, **pero no apagado**. Comprobar en la grilla de fotogramas que
cada plano tiene blancos vivos y un punto de color. Un episodio entero en marrón
oscuro es aburrido aunque cada plano por separado parezca correcto.

---

## 🔊 Las reglas de audio

| Regla | Detalle |
|---|---|
| **Locución en UNA sola pasada** | Trocear frases y pegarlas con silencios rompe la prosodia: cada trozo arranca su entonación desde cero y las cifras suenan despegadas. Medido: el mismo párrafo dura 13,99 s troceado y 9,81 s continuo |
| **Las pausas las hace la PUNTUACIÓN** | Los puntos suspensivos son la pausa dramática. No se insertan silencios a mano |
| **El colchón llena las pausas** | El ambiente debe estar 12-15 LU por debajo de la voz, no 24. Si no, cada respiración del guion se oye como un corte |
| **Room tone continuo** | Una capa de sala que nunca se apaga. Es el pegamento de la mezcla |
| **Rampas, no interruptores** | `between(t,a,b)` en un volumen es un clic. Usar trapecio: `min(1,max(0,min((t-a)/f,(b-t)/f)))` |
| **Música y efectos SINTETIZADOS** | Nada descargado: una pista sintetizada no puede recibir un reclamo de Content ID, que es la causa nº 1 de muerte de estos canales |
| **Objetivo** | −14 LUFS integrados, pico real −1,5 dBFS |

---

## 🧪 Antes de cada render, en este orden

```bash
# 1. que TODO compile (un escape roto se descubre 15 min despues, no ahora)
for f in *.py <episodio>/*.py; do python -c "import ast,io;ast.parse(io.open('$f',encoding='utf-8').read())"; done

# 2. que todo recurso declarado EXISTA (si no, revienta a mitad del render)
python -c "import sys;sys.argv=['x','<episodio>'];sys.path.insert(0,'<episodio>');import motor
from guion_visual import ESCENAS
[motor.buscar(e['r']) for s in ESCENAS for e in s['elementos']]"

# 3. la auditoria: las once medidas
python auditar.py <episodio>
```

⚠️ **Parchear Python con heredocs de shell rompe los escapes**: `\n` dentro de una
cadena de reemplazo se convierte en un salto de linea real y el archivo deja de
compilar. Para cualquier reemplazo con escapes, edicion directa del archivo.

⚠️ **No lanzar un render mientras hay otro vivo**: el segundo intenta borrar los
temporales del primero, el `rm` falla con *Device or resource busy* y la cadena se
aborta entera.

---

## 📐 Verificación: medir, no opinar

```bash
# continuidad del audio: cada salto >= 6 LU entre ventanas es un corte audible
ffmpeg -i final.mp4 -af ebur128 -f null - 2>&1 | grep "M:"
# (parsear t: y M:, ignorar valores < -70 dB, contar saltos >= 6 LU)

# loudness final
ffmpeg -i final.mp4 -af ebur128=peak=true -f null - 2>&1 | grep -E "I:|Peak:"

# revisión visual: grilla de fotogramas — los defectos de exposición sólo se ven así
ffmpeg -i final.mp4 -vf "fps=1/2,scale=440:-1,tile=6x4" -frames:v 1 grilla.png
```

**Verificar el PESO de cada render**, no solo que el archivo exista: un fondo de
4320x2430 pesa entre 9 y 11 MB; si pesa 62 KB, esta vacio y el video saldra en negro.

**Auditar los recortes sobre fondo GRIS**, nunca sobre negro: los halos y las figuras
semitransparentes se disimulan sobre oscuro y saltan sobre gris.

---

## 🗂️ El pipeline

```
guion.md ─► voz.py ─► locucion.mp3
                        │
                        ├─► tiempos.py ──► tiempos.json  (palabra → segundo)
                        │
archivo/ ─► recortar.py ─┐                 │
         ─► tijera.py ───┼──► recortes/ ─┐ │
         ─► revista.py ──┘               │ │
fx.py ────────────────────► fx/ ─────────┤ │
texto.py ─────────────────► texto/ ──────┤ │   diccionario.py (palabra → imagen)
fondos.py ────────────────► render/ ─────┤ │        │
                                         ▼ ▼        ▼
                              guion_visual.py = CLAVE (a mano) + AUTO (generado)
                                         │
                              auditar.py ◄┤   ← SE MIDE ANTES DE RENDERIZAR
                                         ▼
                        motor.py <episodio> ──► escenas ──► _mudo.mp4
                                         ▼
                             acabar.py ──► episodioNN.mp4  (voz + música + SFX)
                                         ▼
                             idiomas.py ──► pistas/ (6 idiomas cuadrados)
```

### El guion visual se GENERA desde el texto, no se elige a mano
`diccionario.py` mapea **palabra → imagen**: si la voz dice «banco», «camiones» o
«fábrica», eso entra en pantalla. La densidad deja de ser una decisión de montaje y
pasa a ser una consecuencia del guion. Quedan dos capas:

| Capa | Qué es | Quién manda |
|---|---|---|
| **CLAVE** | escrita a mano: héroes, series de estados, titulares (frases abstractas que ningún objeto representa) y el remate | **manda**: reserva su banda y nadie la tapa |
| **AUTO** | generada palabra por palabra en las bandas libres | rellena alrededor; si no hay sitio libre, el elemento se descarta antes que amontonarse |

**Medido en el episodio 01:** a mano daban 31,4 eventos/min, simultaneidad 0,98 y
**29% del episodio con el fondo solo**. Con el diccionario: **47,9 eventos/min,
simultaneidad 2,04 y 0% de vacío**, sin tocar la locución.

Detalle de cada pieza en `references/01-pipeline.md`.

---

## 💰 Monetización

- **YouTube largo es el que paga**: 100.000 vistas ahí rinden más que esas vistas en
  TikTok + Instagram + Facebook + X + Snapchat **juntas**
- **CPM del nicho: $15-30.** Contar cómo cayó alguien **no es asesoría financiera**:
  cero riesgo regulatorio con el CPM de finanzas
- **Narco monetiza si el foco es el dinero y la ingeniería, no la violencia.**
  Violencia y drogas activan el icono amarillo y hunden el CPM
- **Seis pistas de audio por vídeo** (inglés, alemán, japonés, francés, español,
  portugués). La pista debe durar lo mismo que el vídeo: YouTube rechaza más de 1 s
  de diferencia. Se cuadra con `atempo` entre 0,85 y 1,15; más allá, se acorta el TEXTO
- **El título traducido es el desbloqueo de SEO**, no el audio: un doblaje automático
  no posiciona en búsquedas de otro idioma; los metadatos localizados sí

---

## ⚖️ Derechos: la línea que no se cruza

| Sí | No |
|---|---|
| Dominio público (obra del gobierno federal de EE.UU.: DEA, FBI, NASA, tribunales) | Fotos de agencia (Getty, AP, Reuters) |
| CC0 y Wikimedia con licencia libre verificada | Fotogramas de películas o series |
| Gráficos y reconstrucciones propias, **etiquetadas como tal** | Música con derechos |
| IA sólo para lo que **no es persona identificable** | **Caras reales generadas con IA** |

**Registrar la procedencia de cada pieza** en `archivo/fuentes.json` (título, licencia,
autor, URL). No es burocracia: es lo que hace defendible el episodio.

⚠️ **Verificar que la imagen corresponde a lo que dice la voz.** Un mapa etiquetado
"Altiplano" resultó ser el altiplano andino, no el penal mexicano. Poner eso mientras
se habla de la cárcel es el error factual que hunde un canal de documentales.

---

## 🧯 Errores cometidos y su lección

| Error | Lección |
|---|---|
| Trocear la locución y pegarla con silencios | Una sola pasada; las pausas las hace la puntuación |
| Culpar a la voz de que "sonaba cortada" | Era el método, no el modelo. **Medir antes de cambiar de herramienta** |
| Diagnosticar los cortes de audio como clics de los SFX | Eran las pausas del guion sin colchón debajo. **Mirar DÓNDE caen los saltos** |
| Opacidad 0,8 en los recortes | El papel es opaco. La transparencia se lee como doble exposición |
| Anclas con puntuación (`"mundo."`) | Normalizar igual que las palabras: sin puntuación, minúsculas |
| Matar Chrome globalmente | Le cierra el navegador al usuario. Usar `--user-data-dir` aislado |
| Fiarse de que un script "corrió" | Leer la salida. Dos iteraciones fallaron en silencio por un f-string roto |
| Verificar handles con HTTP 404 | Sólo el formulario de la plataforma es autoridad |
| `drawtext` con `20:52` | Los `:` son separadores: escapar `:`, `%`, `'`, `\` |
| Una salida de filtro usada dos veces | Duplicar con `asplit` / `split` |
| Extraer texto del guion descartando lineas que empiezan por `*` | Una linea que arranca con **negrita** tambien empieza por `*`. Se perdieron frases enteras y la voz se grabo incompleta. Descartar solo `- `, `* `, `+ ` **con espacio** |
| Renderizar HTML que aun no se habia escrito | El script murio a mitad y los ultimos HTML no existian; Chrome capturaba paginas en blanco. **Escribir TODOS los archivos primero, renderizar despues** |
| Dar por bueno un PNG por su tamano en pixeles | Un PNG de 4320x2430 que pesa 62 KB esta vacio. **Verificar el PESO del archivo**, no solo que exista |
| Poner ganancias de audio a ojo | Los WAV ya venian atenuados: aplicar 0,3 encima los volvio inaudibles. **Medir el LUFS de cada pieza** y calcular la ganancia contra la voz |
| Generar un PNG en una ventana de Chrome de menos de 150 px de alto | Chrome headless devuelve la captura **en blanco**, sin error. 12 rotulos de 780x100 salieron a 0,6 KB. **Alto minimo 200 px**; si la pieza es baja, se le da margen |
| Animar el ANCHO de un `crop` con `t` | `crop` evalua `w` y `h` **una sola vez al configurar el filtro**: aborta con *«Error when evaluating the expression»*. Solo `x`/`y` se evaluan por fotograma. Para revelar texto: `geq` sobre el alfa, o estados progresivos |
| Un heroe reservando su banda ENTERA | Bloqueaba posiciones libres al lado y el generador descartaba elementos que cabian. Solo ocupa la banda entera si mide 1000 px o mas |
| Dar por bueno un montaje porque tiene **cero huecos** | «Hay un elemento» no es «el cuadro esta lleno». Con 0 huecos, el 30% del episodio tenia **menos del 14% de superficie cubierta** y en la grilla los recortes flotaban perdidos. Medir **COBERTURA** (superficie) y el **REPARTO por recuadros 3x3**, no solo presencia |
| Contar con el texto para llenar el cuadro | Los PNG de texto son anchos y bajos (proporcion 0,20-0,29): un titular a 1500 px no pasa del **23% del lienzo**. El texto acompana; lo que llena es la imagen |
| Rotulos en la banda `H*0.78-0.86` | Ahi pinta YouTube la barra de progreso y sus controles. La banda baja util acaba en `H*0.72` |
| Caja de texto con ancho FIJO | «los metodos, segun el expediente» se salia de los 880 px y se cortaba la ultima letra **sin error**. El ancho se calcula desde el numero de caracteres |
| Repetir el mismo recorte cada pocos segundos | El barco salia 5 veces y el organigrama otras 5 en 80 s. Un valor del diccionario puede ser una LISTA de alternativas; no se repite un recurso antes de 14 s |
| Colocar por BANDA en vez de por rectangulo | Las bandas `centro` y `lado` se cruzan en el lienzo: reservar la banda no impide caer encima. Un retrato quedo **100% enterrado 1,8 s** bajo un organigrama y solo se vio en la grilla, ya renderizado. Se comprueba el rectangulo real: 8 solapes graves pasaron a 1 |
| Arreglar un fondo apagado subiendo la LUZ | Son dos palancas distintas. La luz sube `YMAX` (el punto de blanco); lo que quita el marron es la **saturacion del tono base**. Medido: subir la luz llevo `YMAX` de 78 a 242 y dejo `SATAVG` en 5,4; subir el tono base lo llevo a 12,0 |
| 🔴 Fiarse de un PNG de Chrome porque pesa lo que debe | Encadenando paginas de 4320x2430, Chrome falla **a veces** al rasterizar y deja un **bloque blanco plano**, sin error y con el archivo pesando sus 10 MB. Cinco de seis fondos tenian entre 0,33% y 2,36% del cuadro en blanco, y en el video se veian como rectangulos grises en el borde. **No es determinista**: en solitario el mismo fondo sale limpio. Se cuenta los pixeles casi blancos y se REINTENTA |
| Filtros SVG (`feTurbulence`) a 4320x2430 | Son los que mas disparan ese fallo. La textura se hace con degradados repetidos y el grano en ffmpeg (`noise=alls=5:allf=t+u`), donde ademas es temporal y no se congela |
| Elegir "la primera alternativa libre" del diccionario | Si la primera cumple el plazo, siempre gana la primera: no rota. Se coge la **menos usada recientemente** |
| 🔴 Memoria de repeticion guardada DENTRO de la escena | Se reiniciaba en cada escena, asi que el antirrepeticion funcionaba dentro de un plano y **no hacia nada entre escenas** — que es justo donde el espectador lo nota. Medido: el mismo recorte salia 4 veces, siempre en escenas distintas, y ninguna metrica lo veia. La memoria dura **todo el episodio** |
| Medir la repeticion contando ELEMENTOS | Tres fajos que se apilan en un segundo son UN gesto, no tres. Y las marcas de columna vuelven a proposito. Se cuentan **gestos** (usos separados mas de 2,5 s) y se declaran los **MOTIVOS** exentos |
| Rellenar un hueco repitiendo una imagen ya usada | Casi siempre el banco tiene material sin estrenar: en un episodio se usaban 46 recortes de 69. **Primero se mira el banco**, repetir es el ultimo recurso |
| Colocar el primer elemento de un plano lejos del centro de gravedad | Sin nada en pantalla el centro de gravedad ES el centro del cuadro, asi que "lo mas lejos" lo mandaba a una esquina y dejaba media pantalla desierta. **Solo si ya hay algo dentro** se busca el equilibrio |
| 🔴 Equilibrar el cuadro contra lo que solapa **un instante** | El cuadro se juzga instante a instante, pero el equilibrio se calculaba contra todo lo que compartiera un punto de la vida del elemento. Un recorte mandado al extremo derecho para compensar a un vecino de la izquierda **se queda solo en ese extremo en cuanto el vecino muere**. Siete de ocho tramos descompensados eran eso: 14,6 s = 23% del episodio. Cada vecino pesa por la FRACCION de tiempo que comparte, y cuanto menos acompanado esta el elemento, mas tira al centro |
| 🔴 Creer que un plano con UN elemento se arregla moviendolo | No se puede: un elemento no cubre las dos mitades salvo que sea ancho y este centrado, asi que moverlo solo cambia de lado el hueco. Se arregla poniendo algo **enfrente** — una segunda pasada (`contrapeso`) sobre el montaje ya resuelto. Tres cosas que costo descubrir: el lado pelado se decide promediando TODO el tramo (en el punto medio los dos lados empatan a cero y el relleno acababa junto al elemento que venia a compensar); si un vecino estorba se le **recorta la vida** al hueco libre en vez de descartar la pieza (asi entraron 8 de cada 10 que se perdian); y **hay que volver a mirar despues de colocar**, porque el contrapeso se convierte el mismo en el unico elemento y abre el hueco al otro lado |
| 🔴 Comparar la repeticion por NOMBRE de fichero | `balanza_01` y `balanza_05` son la MISMA imagen para quien mira. Contando nombres exactos el sistema decia «sin repeticiones» mientras en pantalla salia cuatro veces la misma figura — y el dueno del canal lo vio en un fotograma antes que ninguna metrica. Se cuenta por **familia** (`_?\d+$` fuera) y los MOTIVOS se declaran tambien por familia, que es como los cuenta el auditor |
| 🔴 Memoria de repeticion que solo mira hacia ATRAS | Un relleno del bloque 4 eligio una pieza que la capa escrita a mano del bloque 5 iba a usar 14 s despues; cuando se coloco, esa mano aun no existia en la memoria. Al ojo le da igual cual vino antes. Se mide la distancia al uso mas cercano **en los dos sentidos**, y toda la capa escrita a mano se anota ANTES de montar el primer bloque |
| 🔴 Contar como presente un elemento a medio fundido | `motor.py` sube en 0,30 s y baja en `fade_out`: casi **un tercio de la vida** de un elemento de 2,4 s es rampa. Contando la vida entera, la medida daba por cubierto un cuadro cuyo unico ocupante estaba al **6% de opacidad** — en la hoja de contactos ese fotograma se ve vacio y las doce medidas decian que todo bien. Se cuenta presente desde el 35% |
| Un cuadro VACIO con el mismo umbral que uno escorado | Con 0,9 s de minimo el relleno no llegaba nunca a huecos de 0,45-0,65 s, que **si se ven**. Umbral escalonado: 0,35 s si el tramo tiene algun instante sin nada, 0,9 s si solo esta escorado |
| 🔴 Tener cuatro copias de «buscar el fichero» | `motor.buscar`, `auditar.hallar`, `auditar.area` y `diccionario.proporcion` buscaban en carpetas y extensiones distintas. La mas estrecha no miraba en `archivo/` ni probaba `.jpg`: para un recorte .jpg el motor lo RENDERIZABA y la medida le daba superficie cero y rectangulo nulo. El montaje medido deja de ser el renderizado **y las metricas mejoran al no medirlo**. Una sola busqueda, y una comprobacion que exige que las tres coincidan para todos los recursos |
| 🔴 `sys.modules` cachea por NOMBRE de modulo, no por ruta | Dos episodios con su `guion_visual.py` son el mismo nombre: **el primero que se importe gana para todo el proceso**. Importar `auditar` sin `sys.argv` cargo el episodio equivocado y se diagnostico una ronda entera sobre el montaje que no era. Mordio tres veces en una sola sesion. Es el mismo error de forma que cachear el pre-escalado por `basename` |
| Un riser con fundido de salida | Su cresta esta al **98% del recorrido** (2,340 s de 2,400). Con `atrim=0:2.30` y `afade=out` desde 1,90 el riser **subia y no llegaba nunca**. Los transitorios (golpe, fogonazo) tienen la cresta en 0,000 y no se adelantan; el barrido la tiene en 0,440 y si |
| Anclar un sonido a una palabra que se repite | `cuando()` devolvia siempre la PRIMERA aparicion. «anos» suena dos veces y el tictac entraba **7,3 s antes**, sobre la frase equivocada. `motor.py` no tiene el fallo porque filtra por la ventana de la escena; la capa de audio no sabe de escenas. Se dice la aparicion a mano (`n=`) y el valor por defecto pasa a ser una **asercion**: si no cuadra con lo encontrado, avisa |
| Medir «la musica contra la voz» metiendo los golpes en la media | La regla de los 12-15 LU es para el colchon **continuo** (musica + ambientes + room tone). Un golpe esta HECHO para asomar, y meterlo en la media hunde lo que deberia sostener: sale 8,2 LU y parece que sobra musica cuando en realidad el continuo esta en 12,4 |
| Dar el ancho de un elemento sin mirar su proporcion | Una imagen vertical a 900 px de ancho mide 977 de alto y no cabe. El retrato del protagonista se caia del gancho **sin avisar**. Cada clase lleva techo de altura y el ancho se recorta |
| 🔴 Medir la PISADA y no medir la PROFUNDIDAD | Un collage no tiene lente: no hay desenfoque que separe los planos, asi que la unica profundidad posible es el **escalon de tamano**. Tres recortes de superficie parecida no son tres planos, son una rejilla, y el ojo no sabe cual mirar — pero la cobertura, la simultaneidad y el reparto 3x3 lo dan todo por bueno. Se mide la parte de la superficie ocupada que se lleva el mayor: con dos elementos iguales sale 0,50 y con tres iguales 0,33. Por debajo de 0,42 el cuadro esta PLANO. Y el arreglo no es a mano: al colocar, si el elemento nuevo entra con una superficie entre 0,74 y 1,35 veces la del mayor que ya vive, se le baja a dos tercios. **Se encoge, nunca se agranda** — crecer lo saca del cuadro o lo mete encima de otro. Efecto medido: la cobertura bajo de 41,1% (fuera de banda) a 36,3% |
| 🔴 Un recorte oscuro sobre un fondo oscuro | Esta en pantalla y NO SE VE, y ninguna de las otras once medidas lo nota: cuenta como presente, suma cobertura y ocupa su recuadro. Medido en el episodio real: el cartel nocturno de la torre tenia **1,1 puntos de luminancia** de diferencia contra su fondo durante 3,2 s — y era el remate de la leyenda. Se compara la luz media del recorte (solo sus pixeles opacos) contra el trozo de fondo que le toca debajo; por debajo de 12 puntos en la escala 0-255, avisa. El arreglo es una gamma, y se busca **la minima** que separe: 0,80 basto para pasar de 1,1 a 18,2. Se guarda el original al lado |
| 🔴 Que la capa visual y la de audio se den por buenas cada una por su lado | Un fogonazo de luz sin sonido no se lee como efecto: se lee como un fallo de codificacion. Es la unica comprobacion que CRUZA las dos capas y no la hacia nadie. Dos trampas al escribirla: (a) lo que acompana a un destello no es el INICIO del sonido sino su **CRESTA** — un riser empieza 2,4 s antes y remata justo en la palabra, asi que midiendo el inicio daba por mudos dos destellos que si tenian golpe; (b) la tolerancia no es a ojo, es la de la ITU-R BT.1359: el sonido puede ir 40 ms por delante y 80 ms por detras. Con la medida bien puesta salieron dos desajustes reales, de 80 y de 50 ms |
| 🔴 `importlib.import_module("acabar")` para cargar el modulo de UN episodio | Hay tres `acabar.py` en el arbol (el del banco y uno por episodio) y gana el primero que caiga en `sys.path`, no el del episodio que se audita: cargaba el del Chapo y se quedaba sin `PISTAS`. **Tercera vez en una sesion** que muerde la misma trampa (antes con `guion_visual`). Se carga por RUTA EXPLICITA con `importlib.util.spec_from_file_location` y no hay ambiguedad posible |
| Ruido sintetizado sin semilla | Las 15 fuentes `anoisesrc` del banco de efectos no llevaban `seed`. Al regenerar los 22 efectos, **tres subieron de nivel y uno cayo 2,20 dB** sin tocar una linea de su definicion. Un episodio publicado tiene que poder rehacerse igual dentro de un ano. Semilla derivada del nombre del efecto y de la posicion en la cadena — distinta en cada fuente, porque dos ruidos con la misma semilla son EL MISMO ruido y al mezclarlos se suman en fase |
| Un desfase de sonido copiado de una medida | El desfase del riser estaba escrito a mano en −2,34 s porque su cresta se midio en 2,340. Al regenerar el material con semilla la cresta se fue a 2,360: el numero caduco sin avisar y el sintoma —un riser que remata 20 ms tarde— no lo caza ninguna prueba. Los desfases se **miden del propio fichero** en cada montaje, no se escriben |
| `alimiter` como red de seguridad | `level` viene ACTIVADO por defecto: entonces no es solo un techo, tambien SUBE el nivel hacia ese techo, y la ganancia declarada deja de ser la que sale. Con `level=disabled` hace lo unico que se le pide. (Ojo: se leyo por ahi que sin eso los efectos salen pegados a 0 dBFS — **medido, es falso**: los 22 del banco van de −39,1 a −2,1 dB. El limitador solo actua sobre lo que ya pasa del techo.) |
| Un `scale` que no escala nada | El fondo entraba a 4320x2430 en CADA fotograma por un `scale=4320:-2`, y los fondos ya venian a 4320: el filtro no hacia nada y costaba **33,5 s de los 89,6 de una escena de 6,73 s**. Pre-escalando el fondo una vez y cacheandolo, 22,6 s. Calidad: PSNR 43,3 dB y SSIM 0,972 — indistinguible, y bajar en dos pasos incluso suaviza mejor que en uno |
| Los filtros de medida de ffmpeg con `-loglevel error` | `psnr`, `ssim`, `astats`, `signalstats` y `volumedetect` imprimen en nivel **info**. Con `-loglevel error` no sale NADA y parece que la medicion fallo. Costo una ronda entera. Y `[0:v][1:v]psnr` con la misma entrada dos veces no funciona: hace falta `split` |
| 🔴 Auditar la oclusion suponiendo que **el ultimo en entrar va encima** | No lo decide el tiempo: lo decide el ORDEN DE LA LISTA, que es como apila el motor. Medido: en un tercio de las parejas los dos ordenes van cruzados, y la comprobacion llevaba reportando **cero** en los dos episodios mientras las pisadas de verdad caian justo ahi. Ademas el motor solo comprueba la capa automatica contra la escrita a mano: **nunca la escrita contra si misma**, y las dos unicas pisadas que sobrevivian eran mano-contra-mano |
| 🔴 Un grafico con texto sin suelo de legibilidad | Los generadores comprobaban su propia legibilidad contra un ancho CONSTANTE (0,80 del lienzo = 1536 px), pero el ancho lo decide el montaje y va de 510 a 1120: **quince de dieciseis piezas pasaban una prueba que media otra cosa**. El suelo no se declara, se CALCULA del propio HTML: `28 px x ancho_nativo / cuerpo_mayor`. Y se mide sobre el cuerpo MAYOR, no el menor — en un documental el papel se ensena como objeto de prueba y la voz lee la linea que importa, asi que la letra pequena puede ser textura; lo que no puede ser es que ni el titular se lea. Si no cabe legible, **no entra**: mas vale el hueco |
| 🔴 Citar la tolerancia de sincronia audio-video como «UIT-R BT.1359: −40/+80 ms» | Esta mal, y lo dije yo. **BT.1359-1 da +45/−125 ms** (detectabilidad) y +90/−185 (aceptabilidad). El **+40/−60 ms es de la EBU R37-2007**, que es la util en produccion — y a 25 fps esos 40 ms son EXACTAMENTE un fotograma, que es la forma de pensarlo sin consultar nada |
| El escalon de tamano peleandose con el suelo de legibilidad | Dos reglas buenas que se anulan: el escalon encoge para crear profundidad y el suelo exige un minimo para que se lea. Encoger un grafico hasta que deje de leerse cambia un defecto por otro peor, asi que **el suelo gana**: `ancho = max(int(ancho * 0.79), suelo)` |
| «Hay algo en las dos mitades» tomado por «el cuadro esta lleno» | Un plano puede tener dos elementos, uno en cada mitad, y estar casi vacio si los dos son pequenos. La segunda pasada tiene que mirar tambien la SUPERFICIE: por debajo del 16% cubierto se trata como hueco aunque el reparto diga que no |
| Comparar el «cuadro casi vacio» de antes y de despues de contar la opacidad | Son dos varas distintas. Desde que un elemento solo cuenta cuando pasa del 35% de opacidad, los fundidos suman cuadro vacio: el mismo montaje paso de 4% a 6% sin empeorar **ni un fotograma**. Al cambiar una medida, la serie historica se corta ahi |
| 🔴 `MarginV` en `force_style` sin declarar `PlayResX`/`PlayResY` | Medido sobre 1080x1920: `MarginV=380` deja el subtitulo **FUERA DE PANTALLA** — el video se genera, pesa lo normal y sale sin subtitulo, y ffmpeg no avisa. Con `PlayResX=1080,PlayResY=1920` el mismo 380 cae a 390 px del borde, que es lo que se pedia. Sin PlayRes, libass interpreta margen Y cuerpo en su resolucion por defecto y los escala por un factor que nadie declaro. Importa el triple en este canal: las seis pistas de idiomas se queman asi |
| Cinco tablas de zona segura que no coinciden | No estaban mal cuatro de cinco: **median dos cosas distintas y ninguna lo decia**. El RECORTE GEOMETRICO (pasar de 9:16 a 4:5 = 1920−1350 = 285 px arriba y abajo) es aritmetica y no cambia nunca. La INTERFAZ que la app pinta encima cambia con cada version y hay que medirla el dia que se usa, con fecha y dispositivo. Una tabla de interfaz sin fecha ni metodo es una trampa a seis meses vista. Un modulo es el dueno de las cifras y los demas rutean |
| 🔴 El dato que se GUARDA para el remate, ensenado en el minuto 1 | El certificado de Lustig dice «Apprentice Salesman & Counter-» y, en el renglon de abajo, «feiter». Esa palabra —falsificador— es el golpe del minuto 12, y el recorte la ensenaba entera a 1180 px durante 4,2 s. Se fugaba por DOS sitios: el recorte del documento y el diccionario, que colocaba por su cuenta la cita completa. Y contradecia al propio guion, que dice «alguien escribio a maquina DOS PALABRAS». La decision de guardar un dato vive en un parrafo del guion y quien monta no la tiene delante: hace falta declararla en el episodio y comprobarla antes de cada render |
| 🔴 Una mascara LLENA no se puede dilatar ni desenfocar | `dilatar()` hace crecer la silueta con una transformada de distancia, pero el trato «revista» le pasaba una mascara llena del tamano exacto de la imagen: sin fuera hacia donde crecer, **no sale margen de papel**; y desenfocar una mascara uniforme la devuelve identica, asi que la sombra deja de ser sombra y es un **rectangulo negro opaco** desplazado 7 y 11 px. Le pasaba a **23 de 72 recortes** — y no a cualquiera: a las casillas, al certificado, a los bonos y a los carteles, que son los heroes. Se ve a simple vista comparando un documento con cualquier foto. El arreglo: llevar la mascara al lienzo grande ANTES de dilatar. De 23 a 1 |
| 🔴 La costura entre bloques es un agujero | Un elemento no puede cruzarla: `resolver()` lo recorta en el limite del bloque. Si la pieza que cierra el bloque anterior muere en la frontera y la que abre el siguiente entra 0,17 s despues, queda cuadro vacio en CADA cambio de bloque. Me pelee tres veces con la misma costura sin ver la causa. Las piezas de frontera se solapan a proposito |
| 🔴 La columna que se VE contradiciendo lo que se OYE | A los 28,52 s la voz decia «segun todo lo que se ha contado de el durante cien anos» —leyenda pura— y la marca visible seguia siendo la del documento durante 3,3 s. La columna no cambia en la frontera del bloque: cambia en la PALABRA donde la voz deja de citar papel. Es el fallo que este canal no se puede permitir, porque su unica promesa es esa |
| El denominador de un aviso | Mi propio informe decia «14 de 56» comparando las piezas ilegibles contra TODOS los recursos del montaje, cuando lo que importa son las que llevan texto: **14 de 22**. Un aviso con el denominador equivocado hace parecer el problema cuatro veces mas pequeno. Y la lista cortaba a 12 cuando habia 14 |
| Regenerar el material sin rehacer los parches | Al regenerar los 72 recortes se perdieron la gamma de los dos que estaban lavados y el recorte de dos palabras, porque los dos eran parches a mano sobre la salida. Lo que se arregla a mano se pierde en la siguiente pasada: o entra en el generador, o se vuelve a perder. Y ademas los tamanos cambian y destapan pisadas nuevas — el certificado quedo al 63% bajo la linea de tiempo |
| 🔴 Una linea de tiempo ancha y centrada CANCELA la capa automatica del bloque | Es texto, y el texto es zona protegida: nada puede pisarlo mas de un 5%. Una linea de 1100 px centrada ocupa de x=96 a x=1196 y no deja entrar NADA colgado de una palabra — las doce piezas del bloque eran todas de contrapeso. Corrida al borde (x=W*0.02) el carril derecho queda libre y el diccionario vuelve a trabajar. Una pieza de texto ancha no se centra nunca |
| 🔴 El contrapeso robando del cajon lo que el guion iba a necesitar | La segunda pasada cogia `celda_respiradero` y `agente_archivador` para tapar un hueco del bloque 1, y cuando llegaban «neumonia» y «horas» —las palabras que SI las significan— la ventana antirrepeticion las descartaba. Resultado: el bloque siguiente con 0,8 s de cuadro vacio y 3,7 s de solo texto. El cajon del contrapeso no puede contener las piezas que el diccionario va a pedir por su palabra |
| 🔴 Una pieza con DESCARGO ensenada por debajo de su ancho minimo | El suelo de legibilidad se calcula sobre el cuerpo MAYOR, porque en un documento la letra pequena suele ser textura. Hay un caso en que NO lo es: cuando dice «NO ES UN DOCUMENTO REAL». La portada reconstruida salia a 504 px y su descargo a **16,5 px** — una portada figurada cuyo aviso de que es figurada no se lee es exactamente el riesgo que el canal existe para evitar. Esas piezas declaran su ancho minimo a mano y manda sobre el calculado |
| Alinear la cresta de un sonido LARGO con una palabra | Un tictac de 20 s tiene su pico al 40% del recorrido, pero eso no es un remate: es el tic mas fuerte de una textura. Alineandolo, el efecto arrancaba 8 s antes y `atrim` lo cortaba 6 s antes de llegar. Un barrido de 1 s tambien tiene la cresta al 48% y ese SI es un acento. Lo que los distingue no es donde esta el pico: es **cuanto duran**. Por encima de 3,5 s, textura |
| Un grafico construido en el orden CANONICO de los hechos, no en el del guion | La serie de balanzas «n DE 5» lista las afirmaciones en su orden de siempre, asi que la cuarta ya nombra a Capone antes de que el guion lo diga. El contador no puede avanzar sin adelantar el episodio. Un grafico que enumera se construye en el orden en que la VOZ los va diciendo, o no sirve para contar |
| Pasarle a alguien «los silencios» sin comprobar que lo son | Le di a un agente seis tiempos como silencios de la locucion y eran **arranques de palabra**. Los silencios de verdad estaban en otros doce sitios. Lo caz0 y uso los medidos. Un limite de bloque sale de medir el audio, nunca de una lista copiada |
| 🔴 Dar por hecho que dos recortes del mismo documento estan a la misma escala | Salen de las MISMAS filas del certificado y solo cambia el borde derecho, pero el generador los rasterizo distinto: relacion medida **1,313**. Para sustituir uno por otro en el sitio —el gesto que remata el episodio— no valen el mismo ancho ni la misma `x`: hay que igualar los anchos MEDIDOS sobre un detalle comun (las barras verticales, el filete inferior). Con 1180 y 1549 px las dos caen en el pixel 121 y el texto se queda clavado; con el mismo ancho para los dos, salta |
| Rotar la pieza de una sustitucion en el sitio | `motor.py` expande la caja al rotar (`ow=rotw`) en proporcion al tamano. Si las dos piezas miden distinto, el texto salta ~3 px en el corte. Las piezas de un reemplazo exacto van con `rot 0` |
| Ilustrar la palabra que SI consta con material de lo que NO consta | El remate del episodio es la palabra «falsificador» escrita a maquina en la casilla 10. En el banco esperan billetes falsos, prensas y carteles del FBI, y la tentacion de ponerlos ahi es enorme. Pero **la condena no consta en ningun expediente**: lo unico documentado es la palabra. Poner al lado una foto de alguien cortando billetes es el pecado que el episodio reprocha, cometido en su ultima escena |
| Un objetivo unico de eventos/min para todos los tramos | El 44 del canal esta calibrado para el GANCHO. El minuto del remate sale a 36,7 con 4,02 s de duracion media y **26 elementos, todos a mano** — y esta bien asi: un remate no se dice corriendo. El aviso del auditor ahi es la consecuencia buscada, y va explicada en el fichero del minuto para que nadie la «arregle» |
| 🔴 Una regla que depende de que alguien se acuerde | «No lances dos renders a la vez» estaba escrito en esta misma tabla **y la rompi igual**, tres horas despues de escribirla: lance el segundo lote mientras el primero seguia vivo, y lo primero que hace cada render es borrar `_mudo.mp4` y los `e0*.mp4` — o sea que le quito los ficheros de debajo al que estaba trabajando. Ahora lo comprueba el programa: `motor.py` deja un cerrojo con su PID, el segundo se niega a arrancar y **explica por que**. El cerrojo guarda el PID y caduca si ese proceso ya no existe: uno que no sabe caducar es peor que no tenerlo, porque un render que se cayo deja el proyecto bloqueado |
| Piezas de archivo que llevan el nombre o el numero de OTRA persona | El cartel del FBI del banco es el de **John Dillinger**, con su nombre y sus numeros. Y un marco titulado «FICHA POLICIAL» llevaba impresa la chapa del CERTIFICADO (`ROBERT V. MILLER · 5954-H`) — una ficha policial con el numero de la prision federal, justo la confusion que el minuto 8 existe para deshacer. Antes de colocar una pieza con texto impreso hay que LEER lo que dice, no fiarse del nombre del fichero |

---

## Referencias

- `references/01-pipeline.md` — cada script, sus parámetros y sus trampas
- `references/02-lenguaje-visual.md` — el sistema de marca y las reglas de composición
- `references/03-produccion.md` — plan de episodio, tiempos de trabajo, checklist
