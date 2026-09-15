# 50 — Cuándo usar una transición (y cuándo no)

> **Bloque 5 — Transiciones y efectos.** Este es el módulo que se lee ANTES que el catálogo.
> Si llegaste buscando "qué transición pongo", empieza acá. La respuesta correcta casi siempre es
> "ninguna", y eso no es pereza: es oficio.

---

## La regla del 90%

Mira cualquier comercial de televisión bien hecho, cualquier película, cualquier anuncio de Apple o
de Nike. Cuenta los cortes. Vas a encontrar que **alrededor del 90% son cortes duros**: la imagen A
termina en un fotograma y la imagen B empieza en el siguiente. Sin fundido, sin barrido, sin nada.

El corte duro es el estándar del oficio por una razón física: **el ojo humano ya sabe cortar**. Cuando
mueves la mirada de una cosa a otra en el mundo real, tu cerebro apaga la visión durante el movimiento
(se llama supresión sacádica) y te entrega la siguiente imagen ya montada. Nunca ves un fundido cruzado
en la vida real. El corte duro imita cómo funciona tu cabeza; la transición no.

Por eso una transición **siempre llama la atención sobre sí misma**. Eso es una herramienta poderosa
cuando quieres que la llame, y un error cuando no.

### La formulación corta

> El corte duro es el default. La transición es una excepción que hay que justificar.

Si no puedes decir en una frase qué significa esa transición, quítala.

---

## El test de "¿qué comunica?"

Antes de poner cualquier transición, respóndete en voz alta:

**"Esta transición le está diciendo al espectador que ______."**

Si la frase se completa sola, la transición se queda. Si tienes que inventarte la respuesta, se va.

Respuestas válidas (las únicas cuatro que existen, de verdad):

| Respuesta | Qué está pasando | Transición típica |
|---|---|---|
| **"...pasó tiempo"** | Elipsis: salto de horas, días, años | Fundido a negro, disolvencia |
| **"...cambiamos de lugar"** | Estamos en otro sitio | Barrido, deslizamiento, whip |
| **"...cambiamos de tema"** | Nuevo capítulo, nueva sección, nuevo argumento | Transición de marca, golpe gráfico |
| **"...esto es un recuerdo / un sueño / no es real"** | Cambio de plano de realidad | Disolvencia lenta, desenfoque |

Respuestas inválidas (todas las que oyes en la práctica):

- "...que el video es dinámico" → No. El ritmo lo da el corte, no el efecto. Ver `20`.
- "...que aquí hay una transición" → Circular. No comunica nada.
- "...que sé usar el programa" → Eso lo nota el editor, no el cliente.
- "...que estos dos planos no pegaban" → Ese es el problema real. Arréglalo con un plano de recurso
  (cutaway) o con un reencuadre, no con un barrido. Ver `21` y `22`.

### El diagnóstico más frecuente

Cuando alguien te dice "ponle transiciones para que fluya", casi siempre el problema **no** son las
transiciones. Es una de estas tres cosas:

1. **El material no tiene cobertura.** Faltan planos. Un barrido no crea un plano que no grabaste.
2. **El ritmo está mal.** Los planos duran demasiado. Ver `27-diagnostico-de-video-lento.md`.
3. **Falta continuidad.** Hay un salto de eje, de luz o de posición. Ver `26-continuidad.md`.

Poner transiciones sobre cualquiera de esos tres problemas es maquillaje sobre una fractura.

---

## Qué significa cada familia de transición

No todas dicen lo mismo. Estas son las lecturas que el público ya tiene aprendidas de tanto ver cine
y televisión; no las inventes, aprovéchalas.

### Fundido a negro (`fadeblack`)

**Significa: se acabó un capítulo.** Es el punto y aparte del audiovisual. En una película es el paso
de un acto a otro; en un video corto es el final o la separación entre dos partes muy distintas.

Trampa: en video vertical de 15–60 segundos, un fundido a negro en la mitad **es una invitación a
deslizar el dedo**. El negro se lee como "terminó". No lo pongas antes del final salvo que sea muy
corto (0,15 s) y a propósito.

### Fundido a blanco (`fadewhite`)

**Significa: transformación positiva, o un salto brusco de energía.** Se usa muchísimo en publicidad
de producto, en antes/después, y en clínicas/estética. Se siente más "limpio" y menos definitivo que
el negro. También es la base del flash (ver `53`).

### Disolvencia / fundido cruzado (`fade`, `dissolve`, `fadeslow`)

**Significa: pasó tiempo, o estos dos planos están relacionados.** Es la transición del documental y
del montaje de recuerdos. Una disolvencia lenta (0,8–1,5 s) dice "pasaron horas". Una rápida (0,25 s)
dice apenas "son parte de lo mismo".

Trampa: la disolvencia entre dos planos con mucho movimiento se convierte en papilla visual. Funciona
bien entre planos quietos o casi quietos.

### Barridos y deslizamientos (`wipe*`, `slide*`, `cover*`, `reveal*`)

**Significan: cambiamos de lugar, o esto es otra cosa.** Son deliberadamente artificiales — nadie los
confunde con realidad. Por eso funcionan en piezas gráficas, en explicativos, en listas y en anuncios
donde ya aceptaste que estás viendo publicidad.

Los `cover*` y `reveal*` son los más modernos: el plano nuevo **entra tapando** (cover) o el viejo
**se corre dejando ver** (reveal). Se sienten como una interfaz, no como una transición de los 2000.

### Circulares y geométricas (`circleopen`, `circleclose`, `radial`, `iris`)

**Significan: enfoque de atención.** El círculo que se cierra sobre algo es el "y colorín colorado"
de los dibujos animados. Úsalas solo con intención de época o de guiño; fuera de eso se leen viejas.

### De distorsión (`hblur`, `pixelize`, `distance`, `squeeze*`, `zoomin`)

**Significan: energía, tecnología, o un tropiezo.** Son las más peligrosas porque son las más vistosas.
`zoomin` y `hblur` son las que arman el 90% de los reels genéricos que se ven baratos. Ver `56`.

### De viento y rebanada (`hlwind`, `vdslice`, `hlslice`...)

**Significan: nada estándar.** No tienen lectura cultural establecida. Son texturas. Úsalas solo si el
proyecto ya tiene un lenguaje gráfico que las justifique.

---

## Duración: el segundo criterio que casi nadie mide

Una transición mal dosificada arruina un corte bueno. Las cifras que funcionan:

| Contexto | Duración |
|---|---|
| Reel / TikTok / anuncio vertical | **0,15 – 0,3 s** |
| Comercial de TV / spot de 30 s | 0,2 – 0,4 s |
| Corporativo / explicativo | 0,3 – 0,5 s |
| Documental / paso de tiempo | 0,8 – 1,5 s |
| Fundido de apertura o cierre de pieza | 0,5 – 1,0 s |

**Regla práctica:** en video vertical, si la transición dura más de 0,3 s ya se siente lenta. El
espectador de vertical tiene el dedo listo.

Y una que duele: **una transición nunca debe durar más que el plano más corto que une.** Si tu plano
B dura 0,6 s y le pones una transición de 0,5 s, prácticamente nunca se ve el plano B limpio.

---

## Los tres momentos donde la transición sí es la respuesta correcta

### 1. Marcar un bloque de la estructura

Video con tres partes ("el problema / lo que hicimos / el resultado"). La transición de marca entre
partes le dice al espectador dónde está parado. Es orientación, no decoración. Ver `52`.

### 2. Tapar una imposibilidad

Dos planos que no pegan por continuidad y no tienes tercer plano para meter en medio. Un whip o un
golpe blanco resuelve. Es una curita honesta — pero es curita: la próxima vez pide más cobertura
(ver `170`).

### 3. Sostener un ritmo musical

Cuando el video va montado sobre música y hay un golpe fuerte, una transición en ese golpe se siente
inevitable. Ojo: **el corte duro en el golpe también funciona, y casi siempre mejor.** Ver `24`.

---

## Lo que hace un editor profesional (el flujo real)

1. **Monta todo a corte duro.** El corte completo, de principio a fin, sin una sola transición.
2. **Míralo entero.** Si funciona así, ya está. La mayoría de las veces funciona así.
3. **Marca los sitios donde algo chirría.** No inventes: espera a que te moleste al verlo.
4. **En cada sitio marcado, pregúntate qué está fallando de verdad.** ¿Falta plano? ¿Sobra duración?
   ¿Es un salto de eje? Arregla la causa primero.
5. **Solo lo que sobreviva a los pasos 3 y 4 recibe transición.** Y siempre pasando el test de
   "¿qué comunica?".

Este orden importa. Si empiezas poniendo transiciones vas a tapar los problemas en vez de verlos,
y el corte va a quedar decorado y flojo al tiempo.

---

## Cómo se pega sin transición (y por qué esto no es un detalle técnico)

Para un corte duro puro no necesitas re-codificar nada. El demuxer `concat` pega archivos
compatibles copiando los datos tal cual:

```bash
printf "file 'plano01.mp4'\nfile 'plano02.mp4'\nfile 'plano03.mp4'\n" > lista.txt
ffmpeg -f concat -safe 0 -i lista.txt -c copy corte.mp4
```

Esto es instantáneo y **no pierde ni un gramo de calidad**, porque no vuelve a comprimir.

**En el momento en que pones una sola transición, esto deja de ser posible.** `concat` no sabe
mezclar imágenes: solo pega. Para una transición hay que pasar por `filter_complex` y re-codificar
todo el video. Eso significa: tiempo de render, pérdida de calidad por recompresión, y la obligación
de que todos los clips compartan resolución, fps y formato de píxel.

O sea: la transición no solo cuesta atención del espectador. Cuesta calidad y cuesta tiempo.
Una razón más para que sea la excepción.

> Detalle completo de `concat` y sus trampas (el BOM que rompe la lista, el `-safe 0`, los archivos
> incompatibles) en `101-ffmpeg-cortar-y-unir.md` y `109-ffmpeg-trampas-y-errores.md`.

---

## Errores comunes

- **Poner transiciones para "dar dinamismo".** El dinamismo es duración de plano, no efecto. Un video
  con planos de 4 segundos y barridos entre ellos sigue siendo lento — ahora además es cursi.

- **Usar la misma transición en todos los cortes.** Si la transición significa algo, no puede
  significar lo mismo 40 veces. Repetirla la convierte en ruido de fondo, como un tic.

- **Transición larga en video vertical.** Medio segundo de barrido en un reel es una eternidad.
  El espectador ya se fue.

- **Fundido a negro en la mitad de un video corto.** Le estás dando permiso explícito para irse.

- **Tapar un salto de eje con un barrido.** El salto sigue ahí; ahora está subrayado. Se resuelve con
  un plano de recurso o con un reencuadre (ver `22`, `26`).

- **Poner la transición antes de tener el corte armado.** Decoras problemas en vez de verlos.

- **Transición más larga que el plano que une.** El plano nunca se ve limpio.

- **Aceptar "ponle transiciones" como brief.** Es una petición sobre el síntoma. Devuelve la pregunta:
  ¿qué es lo que no te está gustando al verlo? La respuesta real casi nunca son las transiciones.

- **Creer que el corte duro es "no hacer nada".** El corte duro es la decisión más difícil del oficio:
  hay que elegir el fotograma exacto. Ver `15` y `21`.

---

## Checklist

Antes de dejar una transición en el corte final:

- [ ] El corte completo está montado a corte duro y lo miré entero así.
- [ ] Esta transición pasa el test: puedo completar la frase "le está diciendo al espectador que ___".
- [ ] La causa real (falta de plano, ritmo, continuidad) ya la revisé y no era eso.
- [ ] La duración está dentro del rango del formato (0,15–0,3 s en vertical; hasta 1,5 s en documental).
- [ ] La transición no dura más que el plano más corto que une.
- [ ] No repito la misma transición en todo el video sin motivo.
- [ ] Si es fundido a negro, está al final o es muy breve y deliberado.
- [ ] Conté cuántas transiciones tiene el video: son menos del 10–15% de los cortes totales.
- [ ] Si la transición es de marca, sale del sistema visual del cliente y no de una preset (ver `52`).
- [ ] Verifiqué el render final: la transición cae donde debe, no medio segundo antes o después (`98`).
