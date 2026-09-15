# 317 — Gestión de archivos

Tres cosas: **nombrar**, **respaldar**, **encontrar**. Si las tres funcionan, nunca pierdes un video
ni gastas media hora buscando el clip bueno. Si alguna falla, tarde o temprano pierdes trabajo.

Este módulo es la versión de producción: **del celular al disco, con una sola persona.**

> **Frontera dentro de la skill:** `10` es la ingesta cuando ya vas a editar. `135` es la
> nomenclatura de un pipeline con código. `97` es archivar proyectos terminados. Este módulo cubre el
> hueco entre esos tres: qué pasa con el material **desde que sales del rodaje hasta que empiezas a
> editar**, hecho por una persona sola.

---

## La regla que ordena todo lo demás

> **El material no existe hasta que está en dos sitios.**

Mientras solo está en el celular, no lo tienes. Un celular se cae, se moja, se roba, se llena, o se
actualiza y borra algo. Ha pasado.

Los dos sitios pueden ser: celular + disco. Disco + nube. Computador + disco. Cualquier par.
Lo que **no** cuenta como dos sitios: dos carpetas del mismo computador.

---

## Nombrar

### El nombre de la carpeta

Una carpeta por video (o por lote). Con este formato:

```
2026-08-09_reel-jueves-alitas
```

**Tres partes, en este orden:**

1. **Fecha al revés** (`AAAA-MM-DD`). Es lo único que hace que las carpetas se ordenen solas.
2. **Guion bajo.**
3. **Nombre corto en minúscula, con guiones.** Sin tildes, sin ñ, sin espacios.

Por qué sin tildes ni espacios: porque el día que quieras subirlo a algún lado, mandarlo por
WhatsApp, o correr un comando de ffmpeg (`100`), los espacios y las tildes rompen cosas.

### Dentro de la carpeta

Cinco subcarpetas. Siempre las mismas cinco, aunque alguna quede vacía.

```
2026-08-09_reel-jueves-alitas/
  01_bruto/          ← lo que salió del celular, sin tocar
  02_seleccion/      ← las tomas buenas, copiadas o marcadas
  03_extras/         ← música, logo, fotos, gráficos
  04_proyecto/       ← el proyecto de CapCut/lo que uses
  05_final/          ← lo exportado, listo para publicar
  plan.jpg           ← foto de la hoja de rodaje marcada
```

**`plan.jpg` es el renglón que nadie pone y el que más sirve.** Antes de guardar la hoja de rodaje,
le tomas una foto y la metes ahí. Seis meses después, es lo único que te va a explicar qué grabaste.

### El nombre de los archivos de video

Aquí hay dos escuelas y las dos sirven:

**Escuela A — no renombrar el bruto.** Dejas los nombres del celular (`IMG_4471.MOV`) y anotas los
números buenos en la hoja de rodaje. Más rápido, más riesgo de confundirse.

**Escuela B — renombrar por plano.** Al copiar, renombras:

```
v1-p05-t2.mov      ← video 1, plano 05, toma 2
```

Toma 10 minutos por rodaje y hace que la edición vuele. **En lote (`316`) es obligatorio**: con
cuatro videos mezclados, los nombres del celular no te dicen nada.

### El nombre del archivo final

```
2026-08-09_jueves-alitas_reel-9x16_v2.mp4
```

Fecha, tema, formato, versión. La versión importa: cuando publiques y quieras el archivo, `v2` te
dice cuál era el bueno. Detalle completo en `96`.

---

## Respaldar

### El respaldo que sí se hace

Todo el mundo sabe que hay que hacer respaldo. Casi nadie lo hace. La razón es siempre la misma: **el
respaldo que se propone es demasiado trabajo.**

El respaldo que sí se hace tiene tres características:

1. **Es un solo paso.**
2. **Ocurre el mismo día del rodaje**, mientras todavía estás en modo trabajo.
3. **No depende de que te acuerdes** de nada complicado.

### El sistema mínimo real

**Paso único, al terminar el rodaje, antes de sentarte:**

> Conecta el celular al computador, copia la carpeta completa a `01_bruto/`, y **no borres nada del
> celular todavía**.

Ya tienes dos copias: celular y computador. Eso es todo lo que hace falta el mismo día.

**Al terminar de editar y publicar:**

> Copia la carpeta completa al disco externo o súbela a la nube. **Ahora sí** borra del celular.

Dos pasos en total, uno al final de cada fase. Eso se hace. Un esquema de siete pasos con versionado
y rotación de discos no se hace.

### Qué respaldar y qué no

| Qué | ¿Se respalda? | Por qué |
|---|---|---|
| El bruto (`01_bruto`) | **Sí, hasta publicar** | Es lo único irrepetible |
| La selección (`02`) | No | Son copias del bruto |
| Extras (`03`) | Sí | Logos, música comprada, gráficos: cuesta rehacerlos |
| El proyecto (`04`) | Sí | Es el trabajo de edición |
| El final (`05`) | **Sí, para siempre** | Es lo que publicaste |
| `plan.jpg` | Sí | Pesa nada y explica todo |

### Cuánto cuesta (Colombia, agosto de 2026)

| Opción | Precio | Nota |
|---|---|---|
| Disco duro externo 2 TB | $250.000 – $400.000 | Pago único. Se daña algún día |
| SSD externo 1 TB | $350.000 – $600.000 | Más rápido, más resistente al golpe |
| Nube 2 TB (Google One / iCloud) | $35.000 – $50.000/mes | ~$480.000/año. Sube solo |
| Nube 200 GB | $10.000 – $15.000/mes | Alcanza si borras el bruto viejo |

**La recomendación honesta:** un disco externo de 2 TB **más** un plan de nube pequeño solo para las
carpetas `05_final` y `03_extras`. El bruto vive en el disco; lo publicado y lo irremplazable vive
además en la nube.

Razón: el bruto pesa 20 veces más que el final y sirve 20 veces menos después de publicar.

### La prueba de que el respaldo funciona

Una vez cada tres meses, haz esto:

> Abre el disco externo, busca un video de hace dos meses y ábrelo.

Si se abre, el respaldo sirve. Si el disco no monta, o el archivo está corrupto, mejor enterarte hoy
que el día que lo necesites.

**Un respaldo que nunca has abierto no es un respaldo. Es una esperanza.**

---

## Qué se guarda y qué se bota

Aquí es donde se decide si tu disco dura dos años o se llena en cuatro meses.

### Se bota (después de publicar y esperar 30 días)

- **Las tomas que no usaste.** Las 28 tomas malas del Vol.01 no le sirven a nadie.
- **Los archivos de selección** (`02_seleccion`): son copias.
- **Renders intermedios y pruebas.** `prueba_final_final_2.mp4`.
- **Descargas de música que no usaste.**

### Se guarda para siempre

- **El video final publicado** (`05_final`). Pesa poco. Es tu historia.
- **Los brutos de momentos irrepetibles.** La inauguración, un evento, el día que se llenó, alguien
  que ya no trabaja contigo. **Eso no se vuelve a grabar nunca.**
- **Los extras** (`03`): logos, fondos, gráficos, música con licencia.
- **`plan.jpg`.**

### Se guarda un año

- **El bruto de contenido normal.** Al año, bótalo. Si en un año no lo volviste a usar, no lo vas a
  usar.

### La regla de los treinta días

No botes nada hasta 30 días después de publicar. Esa es la ventana en la que aparece el "oye, ¿tienes
otra versión?" o "¿me puedes mandar solo el pedacito de…". Después de 30 días, ya nadie pregunta.

---

## Encontrar

Nombrar bien es la mitad. La otra mitad es tener **un solo sitio** donde todo vive.

### La estructura de arriba

```
VIDEOS/
  2026/
    2026-08-09_reel-jueves-alitas/
    2026-08-16_lote-agosto/
    2026-08-23_video-aniversario/
  _MARCA/
    logo.png
    logo-blanco.png
    tipografia/
    plantilla-subtitulos/
    paleta.txt
  _MUSICA/
```

Las carpetas que empiezan con `_` se quedan arriba de la lista y son las que usas en todos los
proyectos. Esa es toda la razón del guion bajo.

### Los tres trucos para encontrar rápido

1. **Busca por fecha, no por nombre.** Si las carpetas empiezan con `AAAA-MM-DD`, ordenarlas por
   nombre es ordenarlas por fecha. Siempre.
2. **La foto del plan es tu índice.** Abres `plan.jpg` y sabes qué hay adentro sin abrir un solo
   video.
3. **Un cuaderno o una nota con una línea por video.** Fecha, nombre, dónde se publicó, cómo le fue.
   Treinta segundos por video. En un año tienes el mapa completo de tu contenido.

```
2026-08-09  jueves-alitas      IG+TikTok   14.200 vistas   funcionó el gancho de la espuma
2026-08-16  lote-agosto (x4)   IG          4-9k c/u        el de la hamburguesa fue el mejor
2026-08-23  aniversario        IG+FB       31.000 vistas   el mejor del año
```

Eso, además de servir para encontrar, es la materia prima para saber qué repetir (`140`).

---

## El error específico del lote

Cuando grabas cuatro videos en una tarde (`316`), todo el material cae en la misma carpeta del
celular, mezclado, con nombres consecutivos que no distinguen nada.

**La solución es de rodaje, no de archivo:** el prefijo `V1-`, `V2-` en la lista de planos, y el
número de toma anotado. Con eso, al copiar renombras en 10 minutos. Sin eso, son dos horas de abrir
archivos uno por uno.

Si ya te pasó y tienes 290 archivos sin identificar: ordénalos por hora de creación y crúzalos con
las horas de tus bloques. Por eso la hoja de rodaje lleva la hora de cada bloque.

---

## Errores comunes

- **Dejar el material solo en el celular.** El error que cuesta un rodaje entero cuando el celular
  se cae.
- **Borrar del celular antes de verificar que la copia se abre.** Copiar no es verificar. Abre un
  archivo de la copia antes de borrar.
- **Nombres con espacios, tildes y ñ.** Rompen comandos, links y subidas. Minúscula y guiones.
- **Fechas al derecho** (`09-08-2026`). No se ordenan. Siempre `AAAA-MM-DD`.
- **`final_final_v3_BUENO.mp4`.** Usa versión numerada y ya (`96`).
- **Un respaldo de siete pasos.** No lo vas a hacer. Dos pasos, o ninguno.
- **Nunca abrir el disco de respaldo.** Un disco que no has abierto en un año puede estar muerto.
- **Guardar todo el bruto para siempre.** Se te llena el disco de tomas que descartaste.
- **Botar el bruto de un momento irrepetible.** Un evento, una inauguración, alguien que ya no está.
  Eso no se regraba.
- **Botar antes de 30 días.** Es justo la ventana en la que alguien pide otra versión.
- **No guardar la foto del plan de rodaje.** Seis meses después no vas a tener ni idea de qué es cada
  carpeta.
- **No renombrar en lote.** Con cuatro videos mezclados, los nombres del celular son inútiles.
- **Tener el material repartido en escritorio, descargas, WhatsApp y el celular.** Un solo sitio.

---

## Checklist

**Al terminar el rodaje, el mismo día:**
- [ ] Creé la carpeta `AAAA-MM-DD_nombre-corto`
- [ ] Copié todo el bruto a `01_bruto/`
- [ ] Verifiqué que al menos un archivo copiado abre
- [ ] **NO borré nada del celular todavía**
- [ ] Le tomé foto a la hoja de rodaje y la guardé como `plan.jpg`
- [ ] Si fue lote: renombré con prefijo de video y número de plano

**Antes de empezar a editar:**
- [ ] Las cinco subcarpetas existen
- [ ] Los extras (logo, música, gráficos) están en `03_extras/`
- [ ] Tengo la lista de planos marcada al lado

**Al publicar:**
- [ ] El final quedó en `05_final/` con nombre completo y versión
- [ ] Copié la carpeta completa al disco externo o a la nube
- [ ] **Ahora sí** borré del celular
- [ ] Escribí la línea del video en mi nota de registro

**Cada mes:**
- [ ] Boté los brutos de videos publicados hace más de 30 días (menos los irrepetibles)
- [ ] Revisé cuánto espacio queda en el disco

**Cada tres meses:**
- [ ] Abrí el disco de respaldo y reproduje un video viejo — funciona
- [ ] Confirmé que `_MARCA` y `05_final` están también en la nube
