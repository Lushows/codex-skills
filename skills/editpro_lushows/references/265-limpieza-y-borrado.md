# 265 — Limpieza y borrado

**Qué resuelve:** hay algo en el plano que no debería estar. Un logo de otra marca, un cable, el
micrófono asomando arriba, una persona que pasó por detrás, un desorden en la mesa, una marca de agua.
Este módulo dice **qué se puede borrar de verdad con lo que tienes**, cómo se hace, y —más importante—
**qué es imposible** para que no pierdas la tarde.

---

## 1. La jerarquía del borrado (de mejor a peor)

Esta lista está ordenada por resultado y por costo a la vez. Empieza siempre por arriba.

```
1. REENCUADRAR   — sacar la cosa del cuadro recortando           30 segundos   ★★★★★
2. TAPAR         — poner algo encima que tenga sentido en escena  2 minutos    ★★★★☆
3. PARCHEAR      — copiar un pedazo limpio de otro momento        5 minutos    ★★★★☆
4. PROMEDIAR     — combinar varios momentos para que se borre     10 minutos   ★★★☆☆
5. DIFUMINAR     — desenfocar o pixelar la zona                   2 minutos    ★★☆☆☆
6. IA            — que un modelo lo invente                       variable     ★★★☆☆
7. VOLVER A GRABAR — la honesta                                   10 minutos   ★★★★★
```

**La número 1 es la que casi nadie usa y la que gana casi siempre.** Antes de intentar borrar nada,
pregúntate si puedes simplemente **encuadrar más cerrado**. Estás publicando en vertical: casi todo el
material tiene margen de sobra.

---

## 2. Reencuadrar: el borrado que no borra nada

El micrófono asomando arriba, el cable en la esquina, la persona en el borde del cuadro: todo eso
desaparece con un recorte.

```bash
# Recorta 180 px de arriba y reescala a vertical completo
ffmpeg -y -i plano.mp4 -vf "crop=iw:ih-180:0:180,scale=1080:1920,setsar=1" \
  -c:v libx264 -crf 18 -pix_fmt yuv420p limpio.mp4
```

**En CapCut:** sube la escala del clip un 8–15% y muévelo. Diez segundos.

**El costo real:** pierdes resolución. Si grabaste en 4K y publicas en 1080, puedes recortar hasta un
40% sin que se note nada. Si grabaste en 1080, tienes margen para un 15–20%. Más allá, empieza a verse
blando.

> **La regla:** graba siempre **más abierto de lo que vas a publicar** y en la máxima resolución que
> aguante tu celular. Eso convierte el reencuadre en tu herramienta de borrado principal, y es gratis.

---

## 3. Tapar: poner algo que pertenezca a la escena

Si no puedes recortar, tapa. Pero tápalo con algo que **tenga motivo para estar ahí**, no con una mancha.

- Un **texto** grande o un bloque de color de la marca, encima de la zona sucia. Y si además lo metes en
  sándwich (`262`), pasa de parche a decisión de diseño.
- Un **b-roll** en pantalla partida que cubra esa mitad.
- Un **PNG** del producto colocado justo ahí.
- Un **subtítulo** en barra sólida abajo tapa un montón de desorden de suelo.

**Por qué esto funciona mejor que un difuminado:** un difuminado dice "aquí había algo que no querías
que vieras" y el espectador lo mira. Un texto dice "esto es diseño" y el espectador lo lee. **El
difuminado señala; el diseño distrae.**

---

## 4. Parchear con un momento limpio (la técnica buena)

Es la técnica más poderosa que puedes hacer con ffmpeg y casi nadie la conoce.

**La idea:** en algún momento del plano, la zona sucia estuvo limpia. Un momento antes de que entrara la
persona, o después de que saliera. Copias **ese pedazo** y lo pegas sobre la zona sucia durante todo el
clip.

**Condición dura: la cámara tiene que estar quieta.** Trípode o celular apoyado. Si la cámara se mueve,
el parche se despega. Sin excepción.

```bash
# Paso 1: sacar el fotograma donde la zona está limpia
ffmpeg -y -ss 0.4 -i plano.mp4 -frames:v 1 limpio.png

# Paso 2: recortar SOLO la zona a parchear (ancho:alto:x:y)
ffmpeg -y -i limpio.png -vf "crop=260:200:610:80" parche.png

# Paso 3: pegar el parche sobre el video, entre los segundos 2 y 7
ffmpeg -y -i plano.mp4 -i parche.png -filter_complex \
  "[0:v][1:v]overlay=x=610:y=80:enable='between(t,2.0,7.0)'" \
  -map 0:a? -c:a copy -c:v libx264 -crf 18 -pix_fmt yuv420p parcheado.mp4
```

**El borde duro es el problema.** Un rectángulo pegado se ve porque tiene esquinas. Se arregla
suavizando los bordes del parche antes de pegarlo:

```bash
# Parche con bordes difuminados (máscara ovalada suave)
ffmpeg -y -i parche.png -filter_complex "\
[0:v]format=rgba,\
geq=r='r(X,Y)':g='g(X,Y)':b='b(X,Y)':\
a='255*min(1,min(min(X,W-X),min(Y,H-Y))/22)'" \
  parche_suave.png
```

Esa expresión de alfa hace que los 22 píxeles del borde se vayan volviendo transparentes. El parche
funde con lo que hay debajo y la costura desaparece.

> ⚠️ **Verifica esto en tu equipo antes de usarlo en producción.** `geq` es lento y la sintaxis de las
> expresiones es delicada. Prueba con la imagen fija y míralo antes de meterlo en el video.

**En CapCut** la misma técnica: congelas un fotograma limpio, lo pones en una pista encima, le aplicas
una **máscara de círculo con el difuminado subido**, la colocas sobre la zona sucia, y ajustas el
tamaño. Es igual de válido y más rápido si la zona es pequeña.

---

## 5. Promediar varios momentos: borrar gente que pasa

El truco clásico para quitar transeúntes de un plano fijo. Si grabaste 10 segundos de una fachada y por
delante pasaron cinco personas distintas, **en cada momento la pared estuvo despejada en algún lado**.
Combinando varios fotogramas y quedándote con el valor **mediano** de cada píxel, la gente desaparece.

```bash
# Sacar 5 fotogramas repartidos en el clip
for T in 0.5 2.5 4.5 6.5 8.5; do
  ffmpeg -v error -y -ss $T -i plano.mp4 -frames:v 1 f_$T.png
done

# Combinar quedándose con la mediana de cada píxel
ffmpeg -y -i f_0.5.png -i f_2.5.png -i f_4.5.png -i f_6.5.png -i f_8.5.png \
  -filter_complex "[0][1][2][3][4]xmedian=inputs=5" -frames:v 1 fachada_vacia.png
```

Ahora `fachada_vacia.png` es tu **placa limpia**: la escena sin nadie. La usas como parche (sección 4) o
como fondo para componer.

**Condiciones:** cámara absolutamente quieta, luz estable, y que ninguna persona se quede parada en el
mismo sitio en todos los fotogramas que elegiste. Si alguien está quieto, sigue ahí.

> ⚠️ **Verifica esto en tu equipo antes de usarlo en producción.** `xmedian` necesita mínimo 3 entradas
> y todas del mismo tamaño y formato. Con 5 funciona mejor que con 3. En PowerShell el bucle `for` de
> arriba es de bash: usa `foreach ($t in 0.5,2.5,4.5,6.5,8.5) { ... }`.

---

## 6. Difuminar y pixelar: el último recurso visible

Sirve cuando **la ley o la decencia lo exigen**: una cara que no dio permiso, una placa de carro, un
documento con datos.

```bash
# Difuminar una zona fija entre los segundos 3 y 8
ffmpeg -y -i plano.mp4 -filter_complex "\
[0:v]crop=240:240:600:400,avgblur=30[b];\
[0:v][b]overlay=600:400:enable='between(t,3.0,8.0)'" \
  -map 0:a? -c:a copy -c:v libx264 -crf 18 -pix_fmt yuv420p difuminado.mp4

# Mosaico en vez de desenfoque (más difícil de revertir, más feo)
ffmpeg -y -i plano.mp4 -filter_complex "\
[0:v]crop=240:240:600:400,scale=12:12,scale=240:240:flags=neighbor[m];\
[0:v][m]overlay=600:400:enable='between(t,3.0,8.0)'" \
  -map 0:a? -c:a copy -c:v libx264 -crf 18 -pix_fmt yuv420p pixelado.mp4
```

**Dos reglas:**

1. **Haz la zona un 25% más grande de lo que crees.** Si el objeto se mueve un poco, un difuminado
   ajustado lo destapa, y un difuminado que destapa medio segundo no sirve para nada.
2. **Verifica fotograma a fotograma** en los momentos de movimiento (`205`, sección 5).

Si la zona se mueve, en CapCut es más práctico: efecto de mosaico + seguimiento.

---

## 7. Logos y marcas de agua

Caso especial porque ffmpeg tiene dos filtros dedicados.

```bash
# delogo: interpola desde los bordes de la zona. Bueno para logos pequeños sobre fondo simple
ffmpeg -y -i plano.mp4 -vf "delogo=x=820:y=60:w=180:h=90" \
  -c:v libx264 -crf 18 -pix_fmt yuv420p sinlogo.mp4

# Para encontrar la zona exacta, píntala primero
ffmpeg -y -i plano.mp4 -vf "delogo=x=820:y=60:w=180:h=90:show=1" -frames:v 1 zona.png
```

`show=1` te dibuja el rectángulo para que ajustes las coordenadas antes de renderizar. Úsalo siempre.

**Lo que `delogo` hace de verdad:** toma los píxeles del borde del rectángulo y **rellena el interior
interpolando**. Por eso funciona bien sobre un cielo, una pared o un desenfoque, y funciona fatal sobre
una zona con detalle: te deja un manchón borroso con forma de rectángulo, que canta más que el logo.

Para logos con forma irregular está `removelogo`, que usa una imagen de máscara en blanco y negro del
mismo tamaño del video:

```bash
ffmpeg -y -i plano.mp4 -vf "removelogo=filename=mascara_logo.png" \
  -c:v libx264 -crf 18 -pix_fmt yuv420p sinlogo.mp4
```

> ⚠️ **Verifica esto en tu equipo antes de usarlo en producción.** `removelogo` exige que la máscara
> tenga exactamente las mismas dimensiones que el video, con blanco puro donde hay que borrar y negro
> puro en el resto. Si no, falla o hace cosas raras.

**La verdad sobre borrar marcas de agua:** técnicamente se puede, y casi siempre se nota. Si es la marca
de agua de un banco de video o de un generador de IA que no pagaste, **la solución correcta es pagar la
licencia o usar otro material**, no pelear con el filtro. Además de que borrarla no te da derechos sobre
el material (`128`).

---

## 8. Qué es imposible (para que no lo intentes)

| Situación | Por qué no se puede | Qué hacer |
|---|---|---|
| **Borrar algo que tapa al sujeto** | detrás no hay información: nadie grabó eso | reencuadrar o volver a grabar |
| **Borrar algo con la cámara en movimiento** | el parche no se puede anclar sin matchmove | estabilizar primero (`264`) o volver a grabar |
| **Borrar la sombra o el reflejo de lo que borraste** | son parte del fondo, no del objeto | es EL problema difícil; ver abajo |
| **Borrar sobre una zona con mucho detalle** | `delogo` interpola: hace un manchón | tapar con diseño (sección 3) |
| **Borrar algo que ocupa medio cuadro** | no hay de dónde sacar el relleno | volver a grabar |
| **Borrar sin que la compresión lo delate** | el parche tiene otra textura de ruido | grano al final sobre todo (`263`) |

**La sombra y el reflejo son el problema serio.** Quitas la silla y queda su sombra en el piso: ahora el
plano tiene una sombra de nada, que es más raro que la silla. Esto sigue siendo un problema abierto en
investigación —hay un trabajo de CVPR 2026 (**EffectErase**) dedicado justo a eso, porque los borradores
actuales no lo resuelven bien (`268`)—. Si lo que vas a borrar proyecta sombra, **no lo borres: tápalo o
reencuadra.**

---

## 9. Los borradores por IA (agosto 2026)

Lo que puedes usar hoy sin instalar nada:

- **CapCut — Eliminador de objetos con IA.** Está en la app y en la web. Marcas el objeto y lo quita.
  Funciona razonable en objetos pequeños sobre fondos simples; se le nota en fondos con detalle y en
  objetos que se mueven. **Para un objeto quieto en un plano quieto, es la vía más rápida.**
- **Runway (Gen-4 Aleph).** Editas video con instrucciones: quitar objeto, cambiar luz, cambiar
  perspectiva. Es lo más capaz del mercado abierto a agosto de 2026, cuesta créditos, y **regenera el
  plano**: la textura cambia, no es el mismo material. Detalle en `268`.
- **ProPainter / DiffuEraser / MiniMax-Remover** — modelos abiertos de borrado en video. Necesitan GPU y
  saber montarlos. Fuera de tu flujo, salvo que quieras el proyecto aparte.

**Lo que hay que saber antes de usarlos:** el resultado **no es reproducible**. Si mañana necesitas
volver a exportar el video, no vas a obtener exactamente lo mismo. Para una marca que repite piezas eso
es un problema real. Guarda el resultado como archivo y trátalo como material grabado.

---

## 10. Verificar un borrado

El borrado se delata en movimiento, no en pausa.

```bash
# Cámara lenta: los bordes del parche y el hervor del relleno saltan
ffmpeg -y -i limpio.mp4 -filter_complex "[0:v]setpts=3*PTS[v]" -map "[v]" -an \
  -c:v libx264 -crf 20 -pix_fmt yuv420p revision_lenta.mp4

# Tira de fotogramas de la zona parcheada
ffmpeg -y -ss 2.0 -i limpio.mp4 -t 2.0 -vf "crop=400:400:530:0,fps=25,scale=160:-1,tile=10x5" \
  -frames:v 1 tira_zona.png
```

Y el remate obligatorio: **grano al final sobre todo el plano** (`263`, sección 4). El parche tiene otra
textura de ruido que el resto; el grano encima iguala las dos y la costura desaparece. Es el paso que
convierte un parche visible en uno invisible.

---

## Errores comunes

1. **No intentar reencuadrar primero.** Es el borrado más rápido, más limpio y gratis. Casi siempre
   funciona en vertical.
2. **Grabar justo al encuadre que vas a publicar.** Deja margen; el margen es tu herramienta de borrado.
3. **Difuminar cuando podías tapar con diseño.** El difuminado señala que había algo; el texto o el
   bloque de color no.
4. **Parchear con la cámara en movimiento.** El parche se despega. Estabiliza primero o abandona.
5. **Parche con bordes duros.** Se ve el rectángulo. Suaviza el borde 20 px.
6. **Usar `delogo` sobre una zona con detalle.** Interpola desde los bordes: te deja un manchón
   rectangular peor que el logo.
7. **No usar `show=1` para encontrar las coordenadas.** Renderizas tres veces por no pintar la zona una.
8. **Difuminar una cara con el área justa.** Hazla 25% más grande; el objeto se mueve y se destapa.
9. **Intentar borrar algo que tapa al sujeto.** No hay información detrás. Nadie grabó eso.
10. **Olvidar la sombra de lo que borraste.** Una sombra sin objeto es más rara que el objeto.
11. **Borrar marcas de agua de material que no licenciaste.** Borrarla no te da derechos, y se nota.
12. **No poner grano al final.** El parche tiene otra textura de ruido y la costura se ve.
13. **Verificar solo en pausa.** El borrado se delata en movimiento; míralo en cámara lenta.
14. **Confiar en un borrado por IA para una pieza que vas a tener que reexportar.** No es reproducible.

---

## Checklist

Antes de dar por bueno un borrado:

- [ ] Probé primero **reencuadrar**. Si el objeto sale del cuadro, terminé.
- [ ] Si no, probé **tapar con algo que pertenece a la pieza** (texto, bloque, b-roll, producto).
- [ ] Si parcheé: la **cámara está quieta**, el parche viene de un momento limpio real, y los **bordes
      están suavizados**.
- [ ] Si promedié con `xmedian`: usé **5 fotogramas o más** y nadie estaba quieto en todos.
- [ ] Si difuminé: la zona es **25% más grande** y la revisé fotograma a fotograma.
- [ ] Si usé `delogo`: comprobé las coordenadas con **`show=1`** y la zona **no tiene detalle**.
- [ ] Comprobé si lo que borré **proyectaba sombra o reflejo**. Si sí, cambié de estrategia.
- [ ] Apliqué **grano al final, sobre todo el plano**, para igualar la textura del parche.
- [ ] Verifiqué en **cámara lenta** y con **tira de fotogramas** de la zona.
- [ ] Si usé IA, guardé el resultado como archivo y sé que **no es reproducible**.
- [ ] Consideré honestamente si **volver a grabar** era más rápido. Muchas veces lo es.
