# 171 — Grabar con celular bien

**Qué resuelve:** el celular de 2026 graba mejor de lo que grababa una cámara profesional de hace diez
años. Lo que arruina el material no es el aparato: son cinco ajustes que nadie toca y tres cosas que se
olvidan antes de empezar. Este módulo es la configuración exacta, explicada por el editor que va a
recibir esos archivos.

---

## 1. Lo que el editor sufre cuando el celular está mal puesto

| Lo que pasó en el rodaje | Qué se ve en el montaje | ¿Arreglo? |
|---|---|---|
| Exposición en automático | La cara cambia de brillo sola a mitad de frase | ❌ Casi nada |
| Foco en automático | La imagen "respira": se desenfoca y vuelve | ❌ No |
| Balance de blancos automático | El morado del neón cambia de tono dentro de la misma toma | 🟡 Difícil |
| Clips en 4K + celular caliente | La toma buena se corta a la mitad | ❌ No |
| Grabó en horizontal, se publica vertical | Se pierde la mitad de la imagen | 🟡 Con recorte y pérdida |
| Llamada entrante | La grabación se detiene | ❌ No |
| Memoria llena | Se acabó el rodaje | ❌ No |

Todos se evitan en 3 minutos de preparación.

---

## 2. Los cinco ajustes que sí importan

### a) Resolución y fps: **1080p a 30 fps**

Lo que casi todo el mundo hace mal: poner 4K "porque se ve mejor".

**Por qué 1080p gana en este caso concreto:**

- El video se va a publicar vertical en redes, y **Instagram y TikTok reencodean todo a alrededor de
  1080 de ancho** (`92`). Los píxeles extra del 4K se botan en la subida.
- El 4K calienta el celular. Un celular caliente **corta la grabación sola** a los pocos minutos, y
  siempre lo hace en la toma que estaba quedando bien.
- Los archivos 4K pesan 3–4 veces más: llenan la memoria y hacen lento todo el montaje.

**Cuándo sí grabar en 4K:** cuando sabes que vas a hacer **punch-in fuerte** (`22`), o sea recortar el
cuadro para simular una segunda cámara. Ahí los píxeles extra sirven de verdad. Si el rodaje es corto y
el celular es reciente, 4K/30 con punch-in planeado es una decisión buena.

**Nunca:** 4K a 60 fps para hablar a cámara. Es el peor de los dos mundos — calienta, pesa, y los 60 fps
no aportan nada a una cara hablando.

| Situación | Ajuste |
|---|---|
| Persona hablando a cámara | **1080p / 30 fps** |
| B-roll de producto donde quiero punch-in | 4K / 30 fps (si el celular aguanta) |
| Algo que quiero en cámara lenta (líquido cayendo, humo) | 1080p / 60 o 120 fps |
| Todo lo demás | 1080p / 30 fps |

> **fps (fotogramas por segundo):** cuántas imágenes por segundo captura. 30 es el estándar de redes.
> 60 sirve para bajar la velocidad después sin que se vea a saltos. 24 se ve "cine" pero se lleva mal
> con la luz artificial de un bar (ver punto de parpadeo, sección 6).

**Regla dura para el editor:** todo el rodaje en **el mismo fps**. Mezclar 30 y 60 en el mismo video
obliga a conversiones que meten micro-tirones. Si vas a grabar algo a 60 para cámara lenta, que sea un
plano aparte y avisado.

### b) Bloqueo de exposición y foco: **el AE/AF Lock**

Este es el ajuste que más cambia la calidad del material y el que menos gente usa.

En automático, el celular está decidiendo el brillo y el foco **todo el tiempo**. Cuando la persona se
mueve, cuando pasa un mesero por detrás, cuando el neón parpadea, la imagen se ajusta sola. En el
montaje eso se ve como una imagen que "late". Y no hay filtro que lo devuelva.

**Cómo se hace:**

- **iPhone:** mantén el dedo presionado sobre la cara de la persona en la pantalla hasta que aparezca
  arriba el rótulo amarillo **AE/AF LOCK**. Ya está: brillo y foco congelados.
- **Android (cámara nativa):** toca la cara y mantén; en la mayoría aparece un candado. Si tu cámara
  nativa no lo tiene, usa **Open Camera** (gratis) o el modo Pro, que sí lo trae siempre.

**Después de bloquear, comprueba:** que la cara no esté ni quemada (blanca sin detalle) ni oscura. Si
quedó muy clara, desliza el dedo hacia abajo sobre la pantalla para bajar la exposición un poco antes de
bloquear.

**Cuándo hay que volver a bloquear:** cada vez que **cambies de sitio o de encuadre**. El bloqueo se
hace para ese plano, no para el día.

**Regla del editor:** es mejor una toma un pelo oscura pero **estable** que una bien expuesta que
cambia de brillo. Lo oscuro se sube en post (`61`). Lo que cambia solo, no.

### c) Balance de blancos: **fijo, no automático**

> **Balance de blancos:** el ajuste que le dice a la cámara "de qué color es la luz de este sitio", para
> que el blanco se vea blanco. Se mide en Kelvin (K).

En un bar-restaurante con neón morado, el automático se vuelve loco: cada vez que la persona se mueve,
la cámara "reinterpreta" el color de la escena y el morado cambia de tono **dentro de la misma toma**.
Eso es lo peor que le puede pasar a un colorista, porque el problema no está entre planos (eso se
empareja, `62`) sino **dentro** de un mismo plano.

**Cómo se hace:** con el modo Pro de la cámara nativa, o con Open Camera / Filmic Pro. Se pone en
manual y se elige un valor:

| Luz | Kelvin aproximado |
|---|---|
| Luz de día por ventana | 5.500 – 6.500 K |
| Interior con bombillos cálidos | 2.800 – 3.200 K |
| Neón de color | Fija el que se vea decente y no lo toques más |
| Terraza con sombra | 6.500 – 7.500 K |

Si el celular no permite balance manual, la alternativa es **bloquear el AE/AF** (que en muchos
teléfonos también congela el balance) y **no cambiar el encuadre a mitad de toma**.

### d) Estabilización: **encendida, pero mejor apoyarse**

La estabilización del celular funciona bien y hay que dejarla activa. Pero tiene dos trampas:

1. Recorta un poco el encuadre. Encuadra un pelín más abierto de lo que quieres.
2. Cuando el celular está quieto sobre una mesa y la estabilización sigue activa, a veces produce un
   micro-deslizamiento del fondo. Si vas a usar trípode y el material se ve "flotando", apágala.

**Lo que de verdad estabiliza:** un trípode de $40.000, una pila de libros, o el celular apoyado contra
una botella. El editor puede estabilizar en post (`59`) pero eso recorta imagen y a veces deforma las
líneas rectas del fondo. Un apoyo físico es gratis y perfecto.

### e) Zoom: **con los pies, no con los dedos**

El zoom digital del celular **inventa píxeles**. La imagen queda blanda y con más ruido, y en post no se
recupera. Si quieres el plano más cerrado, camina.

La excepción: los celulares con varios lentes tienen **zoom óptico real** (típicamente 2x, 3x o 5x). Ese
sí es de verdad. Si tocas exactamente "2x" o "3x" en la interfaz, estás cambiando de lente físico y no
pierdes nada. Lo que hay entre esos números (1,7x, 2,4x) sí es digital.

**Consejo de encuadre para hablar a cámara:** el lente principal (1x) de la mayoría de celulares es
angular y **deforma la cara** si te acercas mucho. Para un primer plano, mejor usar el 2x desde más
lejos: la cara se ve más natural.

---

## 3. Formato y códec: qué le sirve al editor

> **Códec:** la forma en que el video se comprime dentro del archivo. El nombre del archivo (.mp4, .mov)
> no dice cuál es.

| Ajuste del celular | Qué produce | ¿Sirve? |
|---|---|---|
| "Alta eficiencia" / HEVC / H.265 | Archivos pequeños | 🟡 Sí, pero da problemas en PCs viejos |
| "Más compatible" / H.264 | Archivos más grandes | ✅ **La opción segura** |
| HDR / Dolby Vision (iPhone) | Video con rango extendido | ❌ **Apágalo** |
| ProRes (iPhone Pro) | Calidad máxima, archivos enormes | Solo si sobra espacio y hay color serio |

**El HDR merece párrafo aparte porque es la trampa silenciosa.** El iPhone graba HDR por defecto desde
hace años. Ese material se ve espectacular **en el iPhone** y **lavado, gris o con los colores raros**
en casi todo lo demás: el PC del editor, ffmpeg, muchos reproductores, y a veces la propia red social.
Convertirlo bien exige un paso extra de mapeo de tonos que la mayoría no hace.

**Cómo apagarlo en iPhone:** Ajustes → Cámara → Formatos → **Vídeo HDR: desactivado**. Y en la misma
pantalla, "Más compatible" en vez de "Alta eficiencia".

**Cómo lo comprueba el editor cuando ya recibió el material:**

```bash
ffprobe -v error -select_streams v:0 \
  -show_entries stream=codec_name,width,height,r_frame_rate,pix_fmt,color_transfer \
  -of default=nw=1 clip.mp4
```

Si `color_transfer` dice `arib-std-b67` o `smpte2084`, es HDR y hay que tratarlo (ver `60`, `11`). Si
dice `bt709`, todo normal.

---

## 4. Lo que se hace ANTES de la primera toma (3 minutos)

Este es el ritual completo. Se hace una vez, al inicio del rodaje.

**1. Limpia el lente.** Con la camisa. El celular vive en un bolsillo: el lente tiene grasa de dedos y
eso produce un velo lechoso y halos alrededor de las luces — que en un bar con neones es brutal. Es el
arreglo más barato del mundo y el más ignorado.

**2. Modo avión + No molestar.** Una llamada entrante **detiene la grabación**. Si necesitas internet
(por ejemplo para un apuntador en la nube), deja los datos pero activa No molestar y silencia llamadas.

**3. Revisa el espacio libre.** Regla: **10 GB mínimo**. En 1080p/30, un minuto pesa cerca de 130 MB;
en 4K/30, cerca de 350 MB. Diez minutos de material en 4K son ~3,5 GB, y el celular necesita margen para
procesar. Si tienes 2 GB libres, el rodaje se cae.

```
1080p/30  ≈ 130 MB por minuto
4K/30     ≈ 350 MB por minuto
4K/60     ≈ 700 MB por minuto
```

**4. Batería.** Más del 60%, o cargador conectado. Grabar consume mucho y con calor consume más.

**5. Apaga el "video optimizado" / la subida automática a la nube.** iCloud y Google Fotos pueden dejar
en el teléfono una **versión liviana** y guardar el original en la nube. Cuando el editor copia por
cable, se lleva la versión liviana sin saberlo. En iPhone: Ajustes → Fotos → **Descargar y conservar
originales**.

**6. Cuadrícula encendida.** Ajustes → Cámara → Cuadrícula. Sirve para dos cosas: encuadrar por tercios
y **ver si el celular está torcido**. Un horizonte inclinado en un plano de barra se nota muchísimo.

---

## 5. Durante el rodaje: los cinco hábitos

1. **Empieza a grabar 2 segundos antes y termina 2 segundos después.** Sin esos colchones el editor no
   puede hacer un corte limpio ni una transición.
2. **No pares de grabar entre toma y toma de la misma frase.** Es mejor un clip con cinco intentos
   seguidos que cinco archivos. Menos archivos = menos desorden, y el color y el audio son idénticos
   entre intentos.
3. **Di en voz alta "bloque 3, toma 2"** antes de cada intento. Queda grabado y el editor lo encuentra
   en la transcripción (`13`).
4. **Revisa la primera toma completa.** Mírala entera, con el volumen arriba. Es el único momento del
   día en que descubrir un problema es barato.
5. **No borres nada en el celular.** Ni las tomas malas. Los bloopers son material (`18`) y a veces la
   toma "mala" tiene el mejor gesto.

---

## 6. Trampas específicas de un bar-restaurante

**Parpadeo de las luces (flicker).** Los bombillos LED baratos y los neones parpadean a 60 Hz (o 50,
según el país). Si grabas a 24 fps o con obturador raro, aparecen bandas que suben por la imagen. En
Colombia la red es de **60 Hz**, así que **30 o 60 fps** son seguros. **24 fps es el que da problemas**.
Regla simple: en interiores con luz artificial, graba a 30 fps.

**Reflejos en botellas y vidrios.** El celular se ve reflejado en la barra, en la nevera, en el espejo.
Se resuelve moviéndote 30 cm, no en post.

**Contraluz de la puerta.** Si la persona está de espaldas a la entrada, el celular expone para la calle
y la cara queda negra. Ver `173`.

**El neón morado sobre la piel.** El morado tiñe la cara y la piel queda violeta. Se puede corregir en
post (`67`) pero nunca del todo. Si se puede, que la cara reciba una luz neutra y el neón quede de fondo.

**Calor.** Un bar en Colombia a mediodía + celular grabando 4K = aviso de temperatura. Si aparece, baja a
1080p y deja el celular fuera del bolsillo entre tomas.

---

## 7. Apps: cuándo vale la pena salir de la cámara nativa

| App | Para qué | Costo |
|---|---|---|
| Cámara nativa | 90% de los casos, si sabes bloquear AE/AF | Gratis |
| **Open Camera** (Android) | Bloqueo manual real, balance de blancos, niveles de audio | Gratis |
| **Blackmagic Camera** (iOS/Android) | Control completo tipo cámara de cine, muy buena y gratis | Gratis |
| Filmic Pro | Control total, medidores de audio, log | Pago |

**Recomendación práctica para el bar:** cámara nativa con AE/AF bloqueado alcanza. Si vas a grabar más
de una vez al mes, instala **Blackmagic Camera**: da balance de blancos manual, obturador fijo y
medidores de audio en pantalla, que es justo lo que faltó en el rodaje real.

**Ojo con una cosa:** las apps de terceros a veces guardan en un formato o carpeta distinta. Comprueba
en la primera toma que el archivo aparece donde esperas y que el editor lo puede abrir.

---

## 8. Cómo se le pasa el material al editor

**Nunca por WhatsApp.** WhatsApp recomprime a resolución baja, baja el bitrate y a veces cambia la
rotación. Lo que llega no se parece a lo que se grabó.

| Método | Calidad | Comentario |
|---|---|---|
| Cable USB al PC | ✅ Original | El mejor. En iPhone, copiar desde "DCIM". |
| AirDrop (iPhone→Mac) | ✅ Original | Perfecto |
| Google Drive / Dropbox (subir archivo) | ✅ Original | Sube "archivo", no "foto/video comprimido" |
| WeTransfer | ✅ Original | Bien para lotes grandes |
| Telegram "enviar como archivo" | ✅ Original | Sirve, si se marca "archivo" |
| **WhatsApp** | ❌ Destruido | Nunca |
| **AirDrop con "optimizado"** | 🟡 | Revisa que no esté activo |

El editor comprueba lo que le llegó antes de montar nada (`11`):

```bash
for f in *.mp4; do
  ffprobe -v error -show_entries stream=width,height,r_frame_rate,codec_name \
    -show_entries format=duration -of csv=p=0 "$f" | tr '\n' ' '; echo "  <- $f"
done
```

Si un clip tiene 848×480, ese pasó por WhatsApp. Pídelo otra vez.

---

## Errores comunes

1. **Grabar en 4K sin necesidad.** Calienta el celular, corta tomas, llena la memoria y las redes lo
   bajan a 1080 de todos modos. 4K solo si vas a hacer punch-in.
2. **Dejar exposición y foco en automático.** La imagen "late" durante la frase y eso no se arregla.
   Bloquea AE/AF en cada plano nuevo.
3. **No apagar el HDR del iPhone.** El material se ve lavado o con colores raros en todo lo que no sea
   un iPhone. Ajustes → Cámara → Formatos → Vídeo HDR: desactivado.
4. **Mezclar 30 y 60 fps en el mismo rodaje.** Obliga a conversiones que meten micro-tirones. Un solo
   fps para todo, salvo el plano de cámara lenta avisado.
5. **Grabar a 24 fps bajo luz artificial.** Aparecen bandas de parpadeo. En Colombia (60 Hz), graba a 30.
6. **Zoom con los dedos.** Es digital: pierde nitidez para siempre. Camina, o toca exactamente el 2x/3x
   del lente óptico.
7. **No limpiar el lente.** Velo lechoso y halos alrededor de cada luz del bar. Tres segundos con la
   camisa.
8. **Olvidar el modo avión.** Una llamada entrante mata la toma buena.
9. **Empezar sin revisar el espacio libre.** Diez GB mínimo. Un rodaje que se cae por memoria llena no
   se recupera.
10. **Dejar activa la optimización de iCloud/Google Fotos.** Al copiar por cable te llevas la versión
    liviana en vez del original.
11. **Cortar la grabación entre toma y toma de la misma frase.** Genera decenas de archivos y desordena
    todo. Un solo clip con los intentos seguidos.
12. **Pasar el material por WhatsApp.** Llega destrozado. Cable, Drive o AirDrop.
13. **Grabar horizontal para publicar vertical.** Se pierde la mitad del cuadro. Decide el formato antes
    (`176`).
14. **Borrar tomas malas en el celular.** Los bloopers son material (`18`) y el editor decide, no el que
    graba.

---

## Checklist

- [ ] Resolución y fps definidos y **iguales en todo el rodaje** (por defecto 1080p / 30 fps).
- [ ] **HDR / Dolby Vision desactivado**; formato "Más compatible" (H.264).
- [ ] **AE/AF Lock aplicado** en cada plano nuevo; la cara no está ni quemada ni negra.
- [ ] **Balance de blancos fijo** (manual si el celular lo permite), sobre todo bajo el neón.
- [ ] Estabilización activa **y** el celular apoyado en algo físico.
- [ ] **Sin zoom digital**; si se acerca, es con el lente óptico o caminando.
- [ ] **Lente limpio.**
- [ ] **Modo avión / No molestar** activo.
- [ ] **Mínimo 10 GB libres** y batería > 60% o cargador conectado.
- [ ] **Descarga de originales** activada (iCloud/Google Fotos no deja versión liviana).
- [ ] **Cuadrícula encendida**; el celular no está torcido.
- [ ] Cada toma tiene **2 segundos de colchón** al inicio y al final.
- [ ] Los intentos de una misma frase van **en un solo clip**, no en archivos separados.
- [ ] Se **revisó la primera toma completa** con volumen antes de seguir.
- [ ] En interiores con luz artificial se grabó a **30 fps** (sin bandas de parpadeo).
- [ ] El material se entregó **sin pasar por WhatsApp** y el editor verificó resolución y códec reales.
