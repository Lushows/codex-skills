# 176 — Grabar para vertical

**Qué resuelve:** que el material llegue con la forma correcta. El 95% de lo que se graba en un
bar-restaurante se publica en Reels, TikTok o el estado de WhatsApp — todo vertical 9:16. Grabar
horizontal "por si acaso" y recortar después es la decisión que más calidad destruye, y casi nadie sabe
por qué.

---

## 1. Lo que pasa cuando se graba horizontal y se publica vertical

```
   GRABADO HORIZONTAL 16:9 (1920 × 1080)
   ┌──────────────────────────────────┐
   │        │              │          │
   │        │  se usa esto │          │
   │        │              │          │
   └──────────────────────────────────┘
     se bota      607 px      se bota

   → De 1920 px de ancho, sobreviven 607.
   → Se pierde el 68% de la imagen.
```

**Las tres consecuencias:**

1. **Resolución.** El recorte vertical de un 1080p horizontal da 607×1080. Para llenar un cuadro de
   1080×1920 hay que **agrandarlo**, o sea inventar píxeles. La imagen queda blanda.
2. **Encuadre.** El plano que se compuso para 16:9 queda mal en 9:16. La persona sale descentrada, se le
   corta un hombro, el producto queda fuera del cuadro.
3. **Cabeza cortada o pies cortados.** El vertical es alto: si grabaste un plano medio horizontal, al
   recortar te sobra ancho pero te falta alto, y no hay de dónde sacarlo.

**Cuánto se puede recuperar:** nada. El editor puede recortar bien (`22`, `38`), pero no puede
inventar la imagen que no se grabó.

**La única excepción legítima para grabar horizontal:** cuando el video se va a publicar en los dos
formatos y se graba **en 4K horizontal**, dejando espacio de sobra a los lados. Ahí el recorte vertical
da 1620×2160, que es más que suficiente. Pero eso hay que decidirlo antes y encuadrar pensando en las
dos versiones (`38`).

**La regla:** **si se publica vertical, se graba vertical.** Punto.

---

## 2. La cuadrícula mental del 9:16

El cuadro vertical de 1080×1920 no es un cuadro libre: tiene zonas ocupadas por la interfaz de cada red y
por lo que el editor va a poner encima.

```
   ┌─────────────────────┐  0 %
   │  ✖ ZONA MUERTA      │        ← interfaz de la app (arriba)
   │  ✖  ~12 %           │
   ├─────────────────────┤  12 %
   │                     │
   │   ✅ AIRE / TEXTO   │        ← aquí van rótulos y el gancho escrito
   │                     │
   ├─────────────────────┤  25 %
   │                     │
   │   ✅ ZONA DE ORO    │        ← LA CARA VA AQUÍ
   │      LA CARA        │
   │                     │
   ├─────────────────────┤  62 %
   │   ✅ SUBTÍTULOS     │        ← la banda de texto hablado
   ├─────────────────────┤  78 %
   │  ✖ ZONA MUERTA      │        ← usuario, descripción, botones, música
   │  ✖  ~22 %           │
   └─────────────────────┘  100 %
```

**Traducido a la práctica:**

- **La cara va en el tercio superior-medio**, con los ojos alrededor del **35–40% de la altura**.
- **NO pongas la cara en el centro exacto.** Es el instinto de todo el mundo y está mal: el centro es
  donde va a caer la banda de subtítulos, y donde la app pone cosas encima.
- **NO pongas nada importante en el 20% inferior.** Ahí van el nombre de usuario, la descripción, los
  botones de compartir y el disco de la música. Instagram y TikTok se comen esa franja entera.
- **NO pongas nada importante en el 12% superior.** Ahí va la barra de estado y en algunas vistas los
  botones de la app.

Los números exactos por plataforma están en `45-zona-segura-por-plataforma.md`. Estos de aquí son los
seguros para todas.

---

## 3. Dejar aire para los subtítulos (lo que nadie hace)

La mayoría ve los videos **sin sonido**. El texto es el canal principal, no un accesorio (`40`). Y ese
texto tiene que caber en algún lado.

**Lo que pasa cuando no se deja aire:** el editor tiene que poner los subtítulos encima de la cara o
encima del producto. Se ve amontonado y tapa lo que importa.

**Cuánto aire hace falta:** una banda de **entre el 62% y el 78% de la altura** — unos 300 píxeles de
1920 — donde no haya nada crítico. Ni la boca, ni el logo, ni el producto.

**Cómo se consigue en el rodaje:** encuadrando **un poco más arriba** de lo que dicta el instinto. Si en
la pantalla del celular la persona ocupa el centro y hay mucho espacio abajo que "sobra", vas bien. Ese
espacio no sobra: es donde van a ir las palabras.

**Truco práctico:** pon un papelito o cinta en la pantalla del celular marcando la línea del 62%. Encuadra
para que la barbilla quede por encima de esa línea.

**Lo mismo aplica al b-roll.** Si grabas la copa llenándose y la copa ocupa toda la parte de abajo del
cuadro, los subtítulos van a caer encima. Deja la copa en el medio y aire abajo.

---

## 4. Dónde NO poner la cara

| Ubicación | Por qué está mal |
|---|---|
| **Centro exacto vertical** | Ahí caen los subtítulos |
| **Muy abajo** | La interfaz de la app tapa la boca |
| **Muy arriba (pegado al borde)** | Se ve encajonado y la barra de estado molesta |
| **Pegada a un lado** | En vertical el aire lateral es escaso; se ve como error de encuadre |
| **Con muchísimo aire arriba** | El error clásico: la persona parece hundida. Aire arriba ≈ un puño. |

**La ubicación correcta, en una frase:** ojos al 35–40% de la altura, cuerpo centrado horizontalmente, un
puño de aire sobre la cabeza, y espacio libre abajo.

**Regla del aire sobre la cabeza (headroom):** en vertical el error más común es dejar demasiado. Si
puedes meter dos puños entre la cabeza y el borde superior, estás dejando demasiado: baja el celular o
acércate.

---

## 5. Cómo se encuadra vertical de verdad

### Distancia y tipo de plano

En vertical, los planos abiertos **no funcionan**. El cuadro es angosto: una persona de cuerpo entero en
9:16 se ve diminuta y el fondo se come todo. Los planos que funcionan:

| Plano | Corte del cuerpo | ¿Sirve en vertical? |
|---|---|---|
| Plano general (cuerpo entero) | Todo | 🟡 Solo para b-roll o transiciones |
| **Plano medio** (de la cintura) | Cintura | ✅ El de trabajo |
| **Plano medio corto** (del pecho) | Pecho | ✅ **El mejor para hablar a cámara** |
| Primer plano (hombros) | Hombros | ✅ Para momentos de énfasis |
| Primerísimo (solo cara) | Barbilla-frente | 🟡 Muy invasivo, usar con criterio |

**Para alguien hablando a cámara en un bar: plano medio corto**, del pecho hacia arriba, con el fondo
visible detrás para que se vea dónde está.

### El fondo importa el doble

En vertical se ve poco fondo. Ese poco tiene que **decir algo**: la barra, el neón, la estantería de
botellas, la terraza. Un fondo de pared blanca en vertical es un desperdicio.

**Y tiene que estar limpio.** Un cable colgando, una caja, un aviso torcido: en vertical eso ocupa una
porción enorme del cuadro. Dedica 30 segundos a mirar el fondo antes de grabar.

**Profundidad:** que haya algo cerca y algo lejos. Un fondo pegado a la espalda de la persona aplana la
imagen. Dos metros de separación entre la persona y la pared cambian todo.

### La altura del celular

**A la altura de los ojos de la persona.** Ni desde abajo (queda con papada y se ve dominante) ni desde
arriba (se ve pequeño y sumiso). Si la persona está sentada, el celular baja. Si está de pie, sube.

En un bar esto significa apoyar el celular en algo alto: una repisa, una pila de cajas, un trípode. El
celular sobre la mesa apuntando hacia arriba es el encuadre más común y el peor.

---

## 6. Cómo se graba vertical con el celular sin sufrir

**Sostén el celular vertical, no lo gires.** Obvio, pero se olvida cuando alguien "sabe de video" y por
costumbre lo pone horizontal.

**Apóyalo.** Un trípode de $40.000 cambia el rodaje. En su defecto: una botella, una pila de servilleteros,
la pared. Un plano estable vale más que uno bien encuadrado pero tembloroso.

**Usa la cuadrícula** (`171`). En vertical la línea del tercio superior es exactamente donde van los
ojos.

**Comprueba que el celular no está torcido.** En vertical un horizonte inclinado de 2 grados se ve
muchísimo, porque hay líneas verticales por todas partes (la barra, las puertas, las estanterías).

**Si vas a grabar caminando**, el celular con las dos manos, pegado al cuerpo, y camina **con las
rodillas suaves**. La estabilización del celular ayuda pero no hace milagros.

---

## 7. La versión honesta: cuándo grabar horizontal sí tiene sentido

No todo es vertical. Tres casos:

1. **YouTube largo** (`144`). Ahí el 16:9 sigue mandando.
2. **El video va a vivir en la web del negocio** o en una pantalla del local.
3. **Se van a hacer las dos versiones** y hay 4K disponible.

**Si es el caso 3, así se hace bien:**

- Graba en **4K horizontal** (3840×2160)
- Encuadra dejando a la persona **en el centro** con aire generoso a los lados
- Que **nada importante toque los bordes laterales**
- El recorte vertical dará 1215×2160 → más que suficiente para 1080×1920

```bash
# Recorte vertical centrado desde 4K horizontal, sin pérdida real
ffmpeg -hide_banner -y -i horizontal_4k.mp4 \
  -vf "crop=ih*9/16:ih,scale=1080:1920:flags=lanczos" \
  -c:v libx264 -crf 18 -c:a copy vertical.mp4
```

Detalle completo del proceso multiformato en `38-adaptar-un-video-a-varios-formatos.md`.

**Lo que NO cuenta como caso 3:** grabar en 1080p horizontal "por si acaso". Eso no es prevención, es
pérdida garantizada.

---

## 8. Cómo el editor comprueba que el material llegó vertical

Lo primero que se hace al recibir (`11`):

```bash
for f in *.mp4; do
  ffprobe -v error -select_streams v:0 -show_entries stream=width,height \
    -show_entries stream_tags=rotate -of csv=p=0 "$f" | tr '\n' ' '; echo " <- $f"
done
```

**Tres cosas que buscar:**

1. **Ancho mayor que alto** (ej. 1920×1080) → se grabó horizontal. Malas noticias.
2. **Rotación en los metadatos** (`rotate=90`) → el archivo está horizontal pero con una etiqueta que le
   dice al reproductor que lo gire. Algunos programas la respetan y otros no, así que el video se ve
   acostado en unos sitios y bien en otros. Se normaliza antes de montar:

```bash
ffmpeg -hide_banner -y -i entrada.mov -vf "transpose=1" -metadata:s:v rotate=0 \
  -c:v libx264 -crf 18 -c:a copy salida_vertical.mp4
```

3. **Mezcla de orientaciones** en el mismo lote. Si hay clips verticales y horizontales, el montaje
   necesita una decisión: o se recortan los horizontales, o van con barras, o se descartan. Se decide
   **antes** de montar, no en la mitad.

**Verificación de encuadre.** Antes de cortar nada, el editor saca la hoja de contactos (`17`) con las
zonas seguras dibujadas encima:

```bash
# Fotograma con las líneas de zona segura marcadas (12% arriba, 78% abajo)
ffmpeg -hide_banner -y -ss 3 -i clip.mp4 -frames:v 1 \
  -vf "drawbox=y=0:h=ih*0.12:t=fill:color=red@0.35,drawbox=y=ih*0.78:h=ih*0.22:t=fill:color=red@0.35" \
  zona_segura.png
```

Si la cara o el producto caen dentro de las bandas rojas, hay problema de encuadre y hay que decidir qué
hacer antes de montar.

---

## Errores comunes

1. **Grabar horizontal "por si acaso" en 1080p.** Se pierde el 68% de la imagen al recortar y la que
   queda hay que agrandarla. Si se publica vertical, se graba vertical.
2. **Poner la cara en el centro exacto del cuadro.** Ahí van los subtítulos. Los ojos van al 35–40% de la
   altura.
3. **No dejar aire abajo para el texto.** El editor termina poniendo los subtítulos encima de la boca o
   del producto.
4. **Poner algo importante en el 20% inferior.** Instagram y TikTok lo tapan con usuario, descripción y
   botones.
5. **Dejar demasiado aire sobre la cabeza.** La persona parece hundida. Un puño, no dos.
6. **Usar planos abiertos en vertical.** La persona se ve diminuta. Plano medio corto es el de trabajo.
7. **Fondo desordenado.** En vertical se ve poco fondo, así que ese poco pesa mucho. Cable colgando =
   cable protagonista.
8. **Celular sobre la mesa apuntando hacia arriba.** Encuadre desde abajo: papada y ángulo dominante. A
   la altura de los ojos.
9. **Celular torcido.** En vertical hay líneas verticales por todos lados y una inclinación de 2 grados
   se nota muchísimo. Cuadrícula encendida.
10. **Persona pegada a la pared.** Sin profundidad la imagen se aplana. Dos metros de separación.
11. **Mezclar clips verticales y horizontales** sin decidir qué hacer. Se decide antes de montar.
12. **Ignorar la rotación en los metadatos.** El video se ve bien en el celular y acostado en el PC. Se
    normaliza antes de montar.
13. **Grabar b-roll horizontal aunque el a-roll sea vertical.** El b-roll tiene que caber en el mismo
    cuadro. Mismo formato para todo.

---

## Checklist

- [ ] Está decidido **antes de grabar** dónde se publica y en qué formato.
- [ ] Se graba en **9:16 vertical** (celular en vertical, no girado).
- [ ] Los **ojos de la persona quedan al 35–40%** de la altura del cuadro.
- [ ] Hay **aire libre entre el 62% y el 78%** de la altura para la banda de subtítulos.
- [ ] **Nada importante** cae en el **12% superior** ni en el **22% inferior**.
- [ ] El aire sobre la cabeza es de **aproximadamente un puño**, no más.
- [ ] El plano es **medio o medio corto**, no general.
- [ ] El **fondo dice algo** del negocio y está **limpio** (sin cables, cajas ni avisos torcidos).
- [ ] Hay **profundidad**: la persona no está pegada a la pared.
- [ ] El celular está **a la altura de los ojos** de la persona.
- [ ] El celular está **apoyado** (trípode o superficie) y **no está torcido** (cuadrícula encendida).
- [ ] El **b-roll está grabado en el mismo formato vertical** que el a-roll.
- [ ] El editor verificó **ancho, alto y metadatos de rotación** de todos los clips antes de montar.
- [ ] Si se grabó horizontal a propósito, fue en **4K** y con encuadre pensado para las dos versiones.
