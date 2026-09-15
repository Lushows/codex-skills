# 261 — Separar el sujeto

**Qué resuelve:** cómo sacar a una persona (o un producto) de su fondo para poder ponerle algo detrás,
algo encima, o cambiarle el fondo entero. Es el paso 1 de todo compositing y el que decide si el resto
del trabajo va a ser fácil o un infierno.

Hay **tres formas** de hacerlo y una cuarta que es la que más rinde: **grabar de manera que separar sea
fácil**. Este módulo cubre las cuatro, con lo que tú tienes: celular, CapCut y ffmpeg.

> El módulo `81` cubre el croma a fondo (detectar el color real, `colorkey`, despill, verificar). Este
> módulo no lo repite: se enfoca en **elegir la técnica correcta** y en **el matting por IA**, que es lo
> que tú usas de verdad.

---

## 1. Las tres técnicas y cuándo usar cada una

| Técnica | Cómo funciona | Cuándo es la correcta | Cuánto cuesta |
|---|---|---|---|
| **Croma** | borras un color uniforme | grabaste contra fondo verde, o el elemento lo generó una IA | minutos |
| **Matting por IA** | el programa reconoce "eso es una persona" y la recorta | **el 95% de tus casos**: grabaste en la calle, en la cocina, en tu cuarto | segundos |
| **Rotoscopia** | dibujas el contorno a mano, fotograma a fotograma | cuando las otras dos fallan y el plano es corto e imprescindible | horas |

**La decisión en una frase:** si grabaste con el celular en cualquier lugar del mundo real, usas
**matting por IA en CapCut**. Punto. El croma es para cuando montaste un fondo verde a propósito o
cuando el elemento salió de un generador de imágenes. La rotoscopia es el último recurso y casi nunca
vale la pena en un reel (`269`).

---

## 2. Matting por IA: cómo funciona de verdad

> **Matting:** calcular, para cada píxel, qué tanto pertenece al sujeto y qué tanto al fondo. No es un
> sí/no: los píxeles del borde del pelo son "60% pelo, 40% pared". Por eso un buen matte se ve suave y
> uno malo se ve recortado con tijeras.

En CapCut la función se llama **Quitar fondo → Eliminación automática** (o *Recorte inteligente* según
la versión). Seleccionas el clip, panel derecho, pestaña **Video → Quitar fondo**. Hay tres opciones:

1. **Eliminación automática** — la IA detecta al sujeto. Es la que usas.
2. **Eliminación personalizada** — un pincel para marcar qué se queda y qué se va. Útil cuando la
   automática se come un brazo.
3. **Clave de croma** — el gotero para fondo verde (ver `81`).

**Lo que la IA está buscando es una persona.** Ese es el punto clave que explica casi todos los fallos:
funciona espectacularmente bien con personas, decentemente con mascotas, y mal con objetos sueltos
(una botella sobre una mesa, un plato de comida). Para objetos, croma o máscara de forma.

### Cómo lo guarda CapCut (dato real del proyecto)

Cuando aplicas el recorte, CapCut escribe en el material del `draft_content.json` un campo así:

```json
"matting": {
  "flag": 3,
  "path": "##_draftpath_placeholder_<GUID>_##/matting\\<hash>",
  "custom_matting_id": "<GUID>",
  "interactiveTime": [],
  "reverse": false
}
```

Y ahora el detalle que importa: **los archivos de máscara que hay en esa carpeta pesan 0 KB.** No
contienen la máscara. Son **marcadores**: le dicen a CapCut "acá hay un recorte pendiente", y CapCut
**vuelve a calcular el matting cuando abre el proyecto**.

Tres consecuencias prácticas, y las tres duelen:

1. **El recorte no es portátil.** Si copias el proyecto a otro PC, el recorte se recalcula (y puede
   salir distinto) o se pierde. No confíes en mover proyectos con matting entre máquinas.
2. **No se puede sembrar por código de forma confiable.** Puedes escribir el campo `matting` en un draft
   generado (ver `112` y `218`), pero **no puedes generar la máscara**: la calcula CapCut al abrir. Si
   el GUID no coincide con lo que CapCut espera, o el archivo marcador no existe, el clip abre sin
   recorte y sin avisarte.
3. **Abrir el proyecto es lento** cuando hay muchos clips con matting, porque está recalculando todos.

> **Regla operativa:** el recorte de sujeto es una decisión **manual y local**. Se hace en CapCut, en tu
> PC, y el proyecto vive ahí. Todo lo demás del pipeline se puede automatizar; esto no.

### Lo que el matting hace mal (y no es culpa tuya)

| Falla | Cómo se ve | Qué hacer |
|---|---|---|
| **Contorno que hierve** | el borde vibra entre fotogramas | acortar el tramo, o dejar la capa recortada solo 1–2 s |
| **Pelo suelto** | se come mechones o los convierte en una masa | recoger el pelo al grabar; o aceptar y no hacer primer plano |
| **Manos rápidas** | los dedos desaparecen y vuelven | no gesticular en el tramo donde el recorte importa |
| **Objeto en la mano** | recorta a la persona y deja el celular/producto afuera | usar eliminación personalizada con pincel, o replantear el plano |
| **Ropa del color del fondo** | agujero en el torso | cambiar de camiseta. En serio |
| **Dos personas** | recorta una y la otra a medias | separar los planos |

---

## 3. Qué material se separa fácil y cuál no

Esta tabla es la que deberías mirar **antes de grabar**, no después.

| Se separa fácil | Se separa con pelea | No se separa |
|---|---|---|
| persona de frente, quieta, contra pared lisa | persona caminando en la calle | pelo suelto con viento |
| ropa de color plano que contrasta | ropa estampada compleja | humo, vapor, agua |
| fondo desenfocado (retrato) | fondo con gente moviéndose | vidrio, botella transparente |
| luz pareja | contraluz fuerte | cualquier cosa en movimiento borroso |
| grabado a 60 fps | grabado a 24 fps con obturador lento | reflejos y sombras del sujeto |
| sujeto separado del fondo | sujeto pegado a la pared | rejas, mallas, encajes |

**Las cuatro cosas imposibles**, para que no pierdas la tarde intentándolo:

1. **Humo, vapor y agua.** No tienen contorno. Un vapor sobre un café no se recorta: se compone con
   modo de fusión **Pantalla** (`267`).
2. **Vidrio y transparencias.** Una copa recortada pierde lo que se veía a través de ella.
3. **Desenfoque de movimiento fuerte.** Un brazo que es un borrón no tiene borde. Se corta en seco y se
   ve fatal. Solución: grabar a 60 fps (menos borrón por cuadro).
4. **Sombras y reflejos del sujeto.** El matting recorta al sujeto, no a su sombra. La sombra se queda
   en el fondo viejo y hay que volver a fabricarla (`263`).

---

## 4. Cómo grabar pensando en separar (lo más rentable del módulo)

Esto cuesta cero pesos y dos minutos, y te ahorra el 90% del trabajo. Todo con tu celular.

**El fondo:**

- **Pared lisa, de un solo color**, y que ese color **no esté en tu ropa**. Una pared blanca o gris
  clara es perfecta.
- **Sepárate de la pared un metro o metro y medio.** Esto es lo más importante y lo que nadie hace.
  Pegado a la pared: tu sombra cae sobre ella y la IA no sabe dónde terminas tú. A un metro y medio: el
  fondo se desenfoca un poco, tu sombra cae al piso y no a la pared, y el recorte sale limpio.
- **Nada de rejas, persianas ni plantas** detrás. Los huecos entre las hojas son un infierno.

**La luz:**

- **Luz de frente y pareja.** Una ventana grande al frente es el mejor foco del mundo y es gratis.
- **Si puedes, algo de luz por detrás** (una lámpara detrás de ti apuntando a tus hombros). Eso crea un
  filo de luz en el contorno que le facilita muchísimo el trabajo a la IA y además se ve caro. Se llama
  luz de contorno.
- **Nunca contraluz.** Ventana a tu espalda = tu cara es una silueta negra y el recorte se rompe.

**El celular:**

- **60 fps** si tu celular puede (Ajustes de cámara → 1080p o 4K a 60). Menos borrón de movimiento,
  recorte más estable, y de paso te deja hacer cámara lenta (`201`).
- **Apaga el modo retrato/cinemático.** Ese modo ya hace su propio recorte, con su propio error, y
  después el matting recorta encima de un recorte. Doble error.
- **Bloquea el enfoque y la exposición** (mantener presionado en la pantalla). Si la cámara reajusta a
  mitad de toma, el brillo salta y el matting se desestabiliza.
- **Trípode o celular apoyado.** Un plano quieto se recorta mejor que uno a pulso.

**Tú:**

- **Ropa de color plano** que contraste con la pared. Nada de rayas finas ni estampados.
- **Pelo recogido** si vas a recortar. El pelo suelto es el enemigo número uno.
- **Manos quietas** en el tramo que vas a recortar. Gesticula antes o después.

> **La prueba de 10 segundos antes de grabar todo:** graba 3 segundos, mételo a CapCut, aplica Quitar
> fondo, y mira. Si sale limpio, graba tranquilo. Si sale mal, mueve la lámpara o cámbiate de camiseta.
> Diez segundos ahí valen más que una hora de rotoscopia después.

---

## 5. Separar con ffmpeg (cuando CapCut no es el sitio)

CapCut no exporta con canal alfa. Si necesitas el sujeto recortado **como archivo** —para reusarlo, para
un pipeline, para componer con ffmpeg— tienes tres caminos.

### 5.1. Croma, si lo grabaste así

Está todo en `81`. Resumen del comando (video real filmado en verde):

```bash
ffmpeg -i toma_verde.mp4 \
  -vf "chromakey=0x1FB93C:similarity=0.16:blend=0.06,despill=type=green:mix=0.5,format=yuva420p" \
  -c:v prores_ks -profile:v 4444 -pix_fmt yuva444p10le recorte.mov
```

Recuerda: **no existe alfa en mp4**. Sale en ProRes 4444 o en WebM VP9 con `-auto-alt-ref 0`.

### 5.2. Máscara por luminancia (`lumakey`), si el fondo es muy claro o muy oscuro

Sirve cuando grabaste contra una pared blanca con luz fuerte, o contra un fondo negro. No es tan bueno
como el croma, pero es instantáneo y para un plano corto alcanza:

```bash
# Quita lo MUY claro (fondo blanco quemado)
ffmpeg -y -i toma.mp4 \
  -vf "format=rgba,lumakey=threshold=0.90:tolerance=0.08:softness=0.10" \
  -c:v prores_ks -profile:v 4444 -pix_fmt yuva444p10le recorte.mov
```

- `threshold` — qué nivel de brillo se vuelve transparente (0 = negro, 1 = blanco).
- `tolerance` — cuánto alrededor de ese nivel también se borra.
- `softness` — el suavizado del borde. Súbelo si queda de sierra.

> ⚠️ **Verifica esto en tu equipo antes de usarlo en producción.** `lumakey` se come cualquier cosa
> clara del sujeto: una camisa blanca, un diente, un reflejo. Míralo siempre sobre fondo magenta
> (`81`, sección 8) antes de confiar.

### 5.3. Matte por diferencia (el truco de la placa limpia)

El más potente de los tres y casi nadie lo conoce. Sirve si **la cámara está en trípode y quieta**:
grabas 2 segundos del plano **vacío** (sin ti), luego entras y actúas. La diferencia entre los dos es tu
silueta.

```bash
# 1. Saca un fotograma del plano vacío = la "placa limpia"
ffmpeg -y -ss 0.5 -i toma.mp4 -frames:v 1 placa_limpia.png

# 2. Diferencia entre el video y la placa -> máscara -> alfa
ffmpeg -y -i toma.mp4 -i placa_limpia.png -filter_complex "\
[0:v][1:v]blend=all_mode=difference,format=gray,\
maskfun=low=22:high=22:fill=0:sum=10,gblur=sigma=2[m];\
[0:v][m]alphamerge,format=yuva420p" \
  -c:v prores_ks -profile:v 4444 -pix_fmt yuva444p10le recorte.mov
```

Qué hace cada parte: `blend=difference` deja negro donde nada cambió y claro donde apareciste;
`maskfun` convierte eso en blanco/negro con umbral 22; `gblur=sigma=2` suaviza el borde; `alphamerge`
mete esa máscara como canal alfa del video original.

> ⚠️ **Verifica esto en tu equipo antes de usarlo en producción.** Es sensible: si la cámara se movió un
> milímetro, o si la luz cambió, la máscara se llena de basura. Sube o baja `low`/`high` de a 5 hasta
> que el fondo quede totalmente negro y tú totalmente blanco. Míralo primero solo:
>
> ```bash
> ffmpeg -y -i toma.mp4 -i placa_limpia.png -filter_complex \
>   "[0:v][1:v]blend=all_mode=difference,format=gray,maskfun=low=22:high=22:fill=0:sum=10" \
>   -t 2 -c:v libx264 -crf 18 -pix_fmt yuv420p revision_mascara.mp4
> ```

**Cuándo vale la pena:** cuando necesitas el recorte como archivo y no tienes fondo verde. Cuando solo
lo vas a usar dentro de CapCut, no: usa el matting y ya.

---

## 6. Rotoscopia: la verdad

> **Rotoscopia:** dibujar el contorno del sujeto a mano, fotograma a fotograma.

**Tú no tienes las herramientas para hacer rotoscopia de verdad.** Eso es After Effects con Roto Brush o
Mocha, o Nuke. No los tienes y no te hacen falta.

Lo que **sí** puedes hacer en CapCut es una versión simplificada: **máscara de forma con keyframes.**

Cómo se hace:
1. Duplicas el clip.
2. Al de arriba le pones una máscara (rectángulo, círculo o la forma que se acerque).
3. Pones keyframes en la posición, el tamaño y la rotación de la máscara para que siga al sujeto.
4. Usas el método de bisección de `205`: primero y último fotograma, luego la mitad, luego las mitades.

**Para qué sirve de verdad:** para tapar algo, para revelar algo, para una transición. **No sirve** para
recortar una persona con precisión: CapCut solo tiene formas geométricas, no contornos libres.

**El cálculo honesto:** rotoscopiar bien un segundo de video son entre 20 y 60 minutos de trabajo, con
las herramientas correctas. Con las que tú tienes, no se puede. **Si el plano necesita rotoscopia, el
plano está mal grabado. Vuelve a grabarlo** (sección 4) — te toma 5 minutos y queda mejor.

---

## 7. Verificar el recorte antes de montar

Nunca montes sobre un recorte que no verificaste. Dos pruebas, treinta segundos.

**En CapCut:** pon debajo del clip recortado un color chillón (magenta o verde eléctrico) a pantalla
completa y reproduce el tramo a velocidad normal. Los halos y los agujeros aparecen solos.

**Con ffmpeg**, si exportaste el recorte:

```bash
# Sobre magenta, para cazar halos y agujeros
ffmpeg -y -f lavfi -i "color=c=0xFF00AA:s=1080x1920" -i recorte.mov \
  -filter_complex "[0:v][1:v]overlay=(W-w)/2:(H-h)/2:shortest=1" \
  -c:v libx264 -crf 20 -pix_fmt yuv420p prueba_magenta.mp4
```

**La tira de fotogramas, para cazar el borde que hierve:**

```bash
ffmpeg -y -ss 1.0 -i prueba_magenta.mp4 -t 1.6 -vf "fps=25,scale=200:-1,tile=8x5" -frames:v 1 tira.png
```

Lo que buscas: contorno que cambia de forma entre cuadros, dedos que aparecen y desaparecen, un mechón
de pelo que parpadea. Si eso pasa, **acorta el tramo recortado**. Un recorte que dura 1,2 segundos casi
nunca se nota inestable; uno que dura 6 segundos, siempre.

---

## 8. La decisión rápida

```
¿Grabé contra fondo verde a propósito?              → croma (81)
¿El elemento lo generó una IA sobre fondo plano?    → croma leyendo el píxel (81)
¿Grabé con el celular en un lugar real?             → matting de CapCut
¿Necesito el recorte como ARCHIVO, sin croma?       → matte por diferencia con placa limpia (5.3)
¿El fondo es blanco quemado o negro puro?           → lumakey (5.2)
¿Nada de lo anterior funciona?                      → NO es un problema de recorte.
                                                      Vuelve a grabar (sección 4).
```

---

## Errores comunes

1. **Pegarse a la pared al grabar.** Un metro y medio de separación arregla el matting, la sombra y el
   desenfoque de fondo de una sola vez.
2. **Ponerse ropa del color de la pared.** Agujero en el torso garantizado.
3. **Grabar en contraluz.** La cara queda en silueta y el recorte se rompe. Ventana al frente, siempre.
4. **Grabar con modo retrato o cinemático activado.** Ya trae su propio recorte; el matting recorta
   encima y se suman los dos errores.
5. **No bloquear enfoque y exposición.** El brillo salta a mitad de toma y el contorno se desestabiliza.
6. **Dejar el pelo suelto en un plano que vas a recortar.** Es el enemigo número uno del matting.
7. **Esperar que el matting recorte un objeto** (una botella, un plato). Está entrenado para personas.
   Para objetos: croma o máscara de forma.
8. **Intentar recortar humo, vapor, vidrio o agua.** No tienen contorno. Eso se compone con modo
   Pantalla (`267`), no se recorta.
9. **Creer que el recorte de CapCut viaja con el proyecto.** Los archivos de matting pesan 0 KB: son
   marcadores. CapCut recalcula al abrir, y en otro PC puede salir distinto o perderse.
10. **Intentar sembrar el matting por código.** Puedes escribir el campo, no puedes generar la máscara.
    Es una decisión manual y local.
11. **Dejar un tramo recortado de 6 segundos.** El contorno hierve y se nota. Corta a 1–2 segundos.
12. **Intentar rotoscopia en CapCut.** Solo tiene formas geométricas. Si el plano la necesita, el plano
    está mal grabado.
13. **Montar sin verificar el recorte sobre magenta.** Treinta segundos que se pagan solos.

---

## Checklist

Antes de dar por bueno un sujeto separado:

- [ ] Elegí la técnica correcta: **matting** para material real, **croma** para fondo verde o IA,
      **diferencia** cuando necesito archivo.
- [ ] Al grabar: **1,5 m de separación** de la pared, **luz al frente**, **60 fps**, **enfoque y
      exposición bloqueados**, **modo retrato apagado**.
- [ ] La ropa **no tiene el color del fondo** y no es estampada.
- [ ] En el tramo recortado, el sujeto **no gesticula rápido** ni tiene el pelo volando.
- [ ] Hice la **prueba de 3 segundos** antes de grabar la toma completa.
- [ ] Verifiqué el recorte **sobre magenta** a velocidad normal.
- [ ] Revisé la **tira de fotogramas**: el contorno no hierve, no parpadean dedos ni mechones.
- [ ] El tramo recortado dura **menos de 2 segundos**, o comprobé que aguanta más.
- [ ] Si el recorte sale mal, consideré **volver a grabar** antes de pelear con el filtro.
- [ ] Si el proyecto tiene matting, **sé que vive en este PC** y no lo voy a mover esperando que
      sobreviva.
- [ ] Si exporté el recorte, salió en **ProRes 4444** o **WebM VP9**, nunca en mp4.
