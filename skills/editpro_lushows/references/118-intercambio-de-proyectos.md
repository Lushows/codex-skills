# 118 — Qué se pierde en el camino, y cuándo mejor no intercambiar

El módulo 117 explica los formatos. Este explica la parte que nadie te dice hasta que te pasa: **cada
intercambio pierde cosas, y muchas veces la mejor entrega no es un proyecto sino un paquete.**

La honestidad de este módulo se resume en una frase:

> **El intercambio de proyectos entre programas es estructural, no fiel. Transmite el esqueleto del
> montaje. Todo lo demás hay que asumirlo perdido y planificar en consecuencia.**

---

## La matriz de pérdidas

Qué sobrevive realmente a cada formato:

| Elemento | EDL | FCP7 XML | FCPXML | AAF | OTIO |
|---|---|---|---|---|---|
| Puntos de corte (in/out) | ✅ | ✅ | ✅ | ✅ | ✅ |
| Orden de los clips | ✅ | ✅ | ✅ | ✅ | ✅ |
| Rutas a los medios | ⚠️ nombre | ✅ | ✅ | ✅ embebe | ✅ |
| Varias pistas de video | ❌ | ✅ | ✅ | ✅ | ✅ |
| Varias pistas de audio | ⚠️ separado | ✅ | ✅ | ✅ | ✅ |
| Velocidad (uniforme) | ❌ | ⚠️ | ⚠️ | ⚠️ | ✅ |
| Velocidad con curva | ❌ | ❌ | ❌ | ❌ | ❌ |
| Disolvencias simples | ⚠️ `D` | ✅ | ✅ | ✅ | ✅ |
| Transiciones elaboradas | ❌ | ❌ | ❌ | ❌ | ❌ |
| Escala / posición / rotación | ❌ | ⚠️ | ⚠️ | ❌ | ⚠️ |
| Fotogramas clave de movimiento | ❌ | ❌ | ❌ | ❌ | ❌ |
| Volumen por clip | ❌ | ⚠️ | ⚠️ | ✅ | ⚠️ |
| Fades de audio | ❌ | ⚠️ | ⚠️ | ✅ | ⚠️ |
| Ducking / automatización de audio | ❌ | ❌ | ❌ | ⚠️ | ❌ |
| **Texto y títulos** | ❌ | ❌ | ⚠️ | ❌ | ❌ |
| **Corrección de color / LUTs** | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Efectos visuales** | ❌ | ❌ | ❌ | ❌ | ❌ |
| Marcadores / notas | ⚠️ comentario | ⚠️ | ✅ | ✅ | ✅ |
| Clips compuestos / anidados | ❌ | ⚠️ | ⚠️ | ⚠️ | ⚠️ |

**Leé esta tabla dos veces.** La conclusión es incómoda pero clara: **lo único que viaja de verdad son
los cortes.** Todo lo que hace que un video se vea bien — el texto, el color, el movimiento, la mezcla
— se pierde o llega roto.

### Las tres columnas de la verdad

Si simplificamos:

1. **Siempre viaja:** qué clip, desde qué punto, hasta qué punto, en qué orden.
2. **Viaja a veces y hay que revisar:** pistas múltiples, velocidad, volumen, disolvencias.
3. **Nunca viaja:** texto, color, efectos, animación por fotogramas clave.

Planificá con esa lista y no vas a tener sorpresas.

---

## Por qué se pierde

No es que los programas sean malos. Es que **cada uno inventó su propia forma de representar lo mismo**.

Un texto en CapCut es un objeto con su JSON interno, sus offsets UTF-16 y su ruta a una fuente en
caché. Un texto en Premiere es un Essential Graphic con su propio modelo. Un texto en Resolve es un
nodo Fusion. **No hay una representación común de "texto animado" que los tres entiendan.** El formato
de intercambio, para no mentir, prefiere no llevarlo.

Lo mismo con el color: un grade de Resolve es un grafo de nodos con curvas y llaves; en Premiere son
capas de Lumetri. No hay traducción posible.

Los formatos de intercambio, entonces, se limitan honestamente a lo que **sí** tiene una representación
universal: un clip, un rango de tiempo, una posición en una pista. Eso es lo que la industria acordó
hace cincuenta años y es lo que sigue funcionando.

**La conclusión práctica:** no pelees contra esto. Diseñá tu entrega asumiéndolo.

---

## La alternativa: entregar el paquete, no el proyecto

Muchas veces la mejor entrega no es un archivo de intercambio. Es un **paquete** con el máster, los
recursos sueltos y las instrucciones.

Suena menos elegante. Es dramáticamente más confiable.

### Estructura de un paquete de entrega

```
GastroLatam_Reel001_v1/
│
├── 00_MASTER/
│   ├── reel001_v1_1080x1920.mp4          ← el corte final, tal como lo veo yo
│   └── reel001_v1_proxy.mp4              ← versión liviana para revisar en el celular
│
├── 01_CORTE/
│   ├── reel001.otio                      ← el montaje, formato neutral
│   ├── reel001.edl                       ← el mismo, formato universal
│   ├── reel001.xml                       ← el mismo, para Premiere/Resolve
│   └── hoja_de_montaje.md                ← el corte descrito en palabras + timecodes
│
├── 02_MEDIOS/
│   ├── A001.mp4                          ← nombres cortos, sin acentos
│   ├── A002.mp4
│   ├── B004.mp4
│   └── musica.wav
│
├── 03_GRAFICOS/
│   ├── textos.md                         ← qué dice cada texto, en qué segundo
│   ├── subtitulos.srt                    ← subtítulos como archivo estándar
│   ├── logo.png                          ← con transparencia
│   ├── placa_precio.png
│   └── marca.md                          ← tipografía, colores hex, tamaños
│
├── 04_AUDIO/
│   ├── voz_limpia.wav                    ← ya procesada, -16 LUFS
│   ├── musica.wav
│   └── mezcla_referencia.wav             ← cómo suena mezclado
│
└── LEEME.md                              ← cómo reconstruir esto
```

### El `LEEME.md`

Es el archivo que hace que el paquete funcione. Corto y concreto:

```markdown
# Reel GastroLatam 001 — v1

## Qué es esto
Reel vertical de 38,4 s para Instagram y TikTok. 1080×1920, 30 fps.

## Cómo verlo
`00_MASTER/reel001_v1_1080x1920.mp4` es exactamente lo que apruebo yo.
Todo lo demás sirve para reconstruirlo o modificarlo.

## Cómo reconstruir el corte
1. Importá `02_MEDIOS/` a tu proyecto.
2. Importá `01_CORTE/reel001.xml` (Premiere/Resolve) o `.otio` (Resolve).
3. **El texto NO viaja en el XML.** Está en `03_GRAFICOS/textos.md` con timecodes,
   y los subtítulos como SRT estándar.
4. **El color NO viaja.** El máster tiene el look aplicado; si querés replicarlo,
   `03_GRAFICOS/marca.md` tiene los valores.
5. El audio ya está mezclado en `04_AUDIO/mezcla_referencia.wav`. Si preferís
   mezclar de nuevo, las pistas están separadas.

## Lo que sé que se pierde en el intercambio
- Los 14 textos animados (están en textos.md)
- La corrección de color (está aplicada en el máster)
- Los fades de la música (están descritos en hoja_de_montaje.md)

## Frame rate
Todo a 30 fps exactos, non-drop. No mezclé tasas.
```

**Ese archivo vale más que el formato de intercambio más sofisticado.** Le dice al otro exactamente qué
tiene, qué le falta, y dónde está lo que le falta.

### La hoja de montaje

Es el corte descrito en texto plano. Sirve para reconstruirlo a mano si todo lo demás falla:

```markdown
# Hoja de montaje — reel001 v1 · 30 fps · 38,4 s

| # | tc entrada | tc salida | fuente | in | out | notas |
|---|-----------|-----------|--------|-----|-----|-------|
| 1 | 00:00:00:00 | 00:00:02:15 | A001 | 01:00:12:12 | 01:00:14:27 | gancho |
| 2 | 00:00:02:15 | 00:00:06:03 | A001 | 01:00:45:03 | 01:00:48:21 | |
| 3 | 00:00:06:03 | 00:00:08:09 | B004 | 02:00:03:00 | 02:00:05:06 | b-roll cocina |

## Audio
- musica.wav entra en 00:00:02:24, volumen 15%, fade in 400 ms
- fade out desde 00:00:36:00 hasta el final

## Textos
| tc entrada | tc salida | dice | posición |
|---|---|---|---|
| 00:00:01:00 | 00:00:04:00 | "3 errores que te cuestan plata" | centro, tercio inferior |
```

Parece de la prehistoria. Funciona siempre, con cualquier programa, dentro de cinco años, y la puede
leer una persona.

---

## Cuándo usar qué

| Situación | Entregá |
|---|---|
| El otro usa CapCut y solo tiene que aprobar | El proyecto de CapCut + hoja de decisiones |
| El otro usa Premiere/Resolve y va a seguir editando | Paquete completo con XML/OTIO |
| El otro solo tiene que aprobar, no editar | **Solo el máster.** No compliques. |
| El otro va a mezclar el audio | AAF con handles + los WAV sueltos |
| El otro va a hacer color | El máster sin grade + los archivos originales + una referencia gradeada |
| No sabés qué usa el otro | Máster + EDL + medios + LEEME |
| Es un archivo para dentro de dos años | Máster + medios + hoja de montaje en texto |

**La pregunta que resuelve el 90% de los casos: ¿el otro va a *editar* o solo va a *aprobar*?**

Si solo va a aprobar, mandale un MP4 y punto. Todo el aparato de intercambio existe para el caso en que
el otro tiene que seguir trabajando encima.

---

## Conform y relink: el dolor real

Cuando el otro importa tu XML, lo primero que va a pasar es que **los medios no se van a enlazar**. Es
lo normal, no es tu culpa ni la de él: las rutas de tu computador no existen en el suyo.

El proceso de reenlazar se llama **relink**, y funciona mejor si:

1. **Los nombres de archivo son idénticos** a los del proyecto. Si le mandaste `A001.mp4` y en el XML
   dice `Grabación 2 copia.mp4`, el relink automático falla.
2. **Todos los medios están en una carpeta plana.** El relink por carpeta es un clic; el relink por
   subcarpetas anidadas es archivo por archivo.
3. **No hay archivos duplicados con el mismo nombre.** Dos `A001.mp4` en carpetas distintas = el
   programa elige uno al azar.
4. **Los archivos son los mismos.** Si vos editaste sobre proxies y le mandás los originales, las
   duraciones pueden no coincidir y todo se corre.

**El error clásico y carísimo:** editar con archivos re-comprimidos o recortados y después entregar los
originales. Las duraciones no coinciden y todo el montaje queda desfasado. **Editá sobre los mismos
archivos que vas a entregar, o documentá exactamente qué transformación hiciste.**

---

## Verificar la entrega antes de mandarla

Cinco minutos que evitan el mensaje de "no me abre":

1. **Copiá el paquete a otra carpeta** (simula otra máquina).
2. Importá el archivo de intercambio en el programa de destino, si lo tenés.
3. Contá los cortes: ¿son los mismos que en tu montaje?
4. Mirá el primero y el último: ¿coinciden con el máster?
5. Abrí el máster y el corte importado en paralelo: ¿se ven iguales estructuralmente?
6. Leé tu propio `LEEME.md` como si fueras el otro: ¿se entiende?

Si no tenés el programa de destino, por lo menos hacé el paso 6 y mandá el máster. Con el máster, el
otro siempre puede reconstruir; sin él, está a ciegas.

---

## El caso especial: de CapCut hacia afuera

Si el corte nació en CapCut y hay que llevarlo a Premiere o Resolve:

```bash
# capcut-cli exporta a OpenTimelineIO
capcut-cli export-otio ./mi-proyecto/ -o corte.otio

# y de ahí a lo que necesite el destino
otioconvert -i corte.otio -o corte.xml
otioconvert -i corte.otio -o corte.edl
```

**Qué llega:** los cortes, las pistas, los tiempos.
**Qué NO llega:** los textos de CapCut, las plantillas animadas, los efectos, los filtros, los ajustes
de color, las animaciones.

O sea: llega el esqueleto. Que muchas veces es exactamente lo que el editor profesional quiere — él va
a rehacer los gráficos con sus propias herramientas de todos modos, y prefiere partir del corte limpio.

**Decilo explícitamente en la entrega:** "te mando el corte estructural desde CapCut; los textos van
aparte en `textos.md` porque no viajan en ningún formato".

---

## Errores comunes

**Mandar un XML y asumir que el otro ve lo mismo que vos.** Ve los cortes. Nada más. Sin el máster,
tampoco sabe qué debería ver.

**No mandar el máster.** Es el error más caro. El máster es la única fuente de verdad de "así se ve
esto". Todo lo demás es reconstrucción.

**Nombres de archivo distintos entre el proyecto y los medios entregados.** El relink automático falla
y el otro tiene que enlazar archivo por archivo.

**Carpetas anidadas.** Convertí el relink de un clic en una tarde.

**Archivos duplicados con el mismo nombre.** El programa enlaza el equivocado y nadie se da cuenta
hasta el final.

**Editar sobre proxies y entregar originales sin avisar.** Duraciones distintas, montaje desfasado.

**Prometer que el texto viaja.** No viaja. Decilo antes y mandalo aparte.

**Mandar un paquete completo cuando el otro solo tiene que aprobar.** Le complicás la vida por nada.
Un MP4.

**No escribir el LEEME.** El paquete más completo del mundo sin instrucciones genera tres correos de
ida y vuelta.

**No probar la entrega desde otra carpeta antes de mandarla.**

**Asumir que OTIO no pierde nada porque es moderno.** Pierde efectos igual que los demás. Es más limpio
estructuralmente, no mágico.

---

## Checklist

**Antes de decidir el formato**
- [ ] Sé si el otro va a **editar** o solo a **aprobar**
- [ ] Sé qué programa usa
- [ ] Revisé la matriz de pérdidas y sé qué NO va a llegarle

**Armando el paquete**
- [ ] Incluí el **máster** (siempre, sin excepción)
- [ ] Los medios están en una carpeta plana, con nombres cortos, sin acentos ni duplicados
- [ ] Los nombres de los medios coinciden exactamente con los del archivo de intercambio
- [ ] Los archivos entregados son los mismos con los que edité (no proxies)
- [ ] Los textos van aparte, con timecodes, en `textos.md` y/o SRT
- [ ] Los gráficos van sueltos, con transparencia, en su carpeta
- [ ] El audio va mezclado **y** en pistas separadas
- [ ] Hay una hoja de montaje en texto plano por si todo lo demás falla
- [ ] Todo está a un solo frame rate y lo declaré

**El LEEME**
- [ ] Dice qué es y cuánto dura
- [ ] Dice cómo reconstruirlo, paso a paso
- [ ] **Dice explícitamente qué se pierde en el intercambio y dónde está lo perdido**
- [ ] Está escrito para alguien que no estuvo en la conversación

**Antes de mandar**
- [ ] Copié el paquete a otra carpeta y verifiqué que se entiende solo
- [ ] Importé el intercambio y conté los cortes
- [ ] Leí mi propio LEEME poniéndome del otro lado
