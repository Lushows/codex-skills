# 407 — Sombras y halos entre capas

**Qué resuelve:** los tres defectos que aparecen **entre** dos capas y que nadie sabe atribuir: el
rectángulo negro que sale al girar un recorte, la sombra con borde recto y el elemento que se ensucia
entero sin motivo aparente. Los tres son errores de orden o de cadena, los tres se miden en el píxel, y
los tres tienen arreglo de una línea.

`394` mide **cuánto** debe oscurecer una sombra para que asiente, y `204` §3.4 da el rango estético. Aquí
está la mecánica: dónde va la sombra en la pila y qué la rompe.

---

## 1. La sombra es una capa, y va justo debajo de su dueño

No es un parámetro: es un PNG duplicado, ennegrecido, desenfocado y desplazado, declarado **antes** que el
elemento. Medido sobre fondo claro `(215,210,200)` con una pieza roja `(230,70,60)`:

| montaje | centro de la pieza | veredicto |
|---|---|---|
| sombra **debajo** de su dueño | `(229, 68, 59)` | la pieza se mantiene |
| sombra **encima** de su dueño | `(160, 47, 40)` | la pieza sale un **30 % más oscura** |

Ese es el síntoma que se describe como «el elemento se ve apagado» o «como sucio» y que nunca se atribuye
a la sombra, porque la sombra *también* se ve bien. La sombra encima no se lee como sombra: se lee como
que el recorte está mal exportado.

En una cadena lineal (`400` §1), poner la sombra debajo es declararla un eslabón antes:

```
[bg][s]overlay=258:88[v1];[v1][e]overlay=250:75[v2]
```

Y en CapCut es lo mismo con una pista: la sombra en la pista inmediatamente inferior a la del elemento,
nunca en la superior.

---

## 2. La sombra con borde recto: `gblur` no tiene dónde desenfocar

El fallo más frecuente y el más desconcertante, porque el filtro es correcto. Perfil vertical del canal
rojo al salir de la pieza, sobre fondo 215:

| cadena | perfil (dentro → fuera) |
|---|---|
| `…,gblur=sigma=14,colorchannelmixer=aa=0.35` | `140 140 140 140 140 214 214 214…` |
| `…,pad=w=iw+120:h=ih+120:x=60:y=60:color=#00000000,gblur=sigma=14,…` | `149 152 157 163 171 183 191 197 201 204 207 210 210 211 213` |

Sin relleno, la sombra **corta en seco**: de 140 a 214 en un píxel. No es que `gblur` falle —`planes` vale
15 por defecto e incluye el alfa; lo comprobé también con `planes=0xF` y `planes=8`, idénticos—. Es que el
PNG es opaco hasta su propio borde: **no hay margen transparente hacia el que difundir.** El desenfoque
necesita sitio.

```
[1:v]format=rgba,colorchannelmixer=rr=0:gg=0:bb=0,
     pad=w=iw+120:h=ih+120:x=60:y=60:color=#00000000,
     gblur=sigma=14,colorchannelmixer=aa=0.35[s]
```

El relleno tiene que ser **del orden de 4× sigma** por cada lado, y después hay que **restar ese relleno a
la posición** del `overlay` (aquí, 60 px en x e y) o la sombra aparece desplazada al revés de lo que
pretendías.

---

## 3. El rectángulo negro del giro

El motor gira cada recorte un par de grados para que el collage se lea como papel pegado a mano. Si el
giro no declara fondo transparente, aparece una caja negra perfecta detrás de la pieza:

| cadena | esquina de la capa | fondo real |
|---|---|---|
| `rotate=0.12:ow=rotw(0.12):oh=roth(0.12)` | `(0, 0, 0)` | `(18, 22, 40)` |
| `rotate=0.12:c=none:ow=…:oh=…` | `(18, 21, 41)` | `(18, 22, 40)` |

Negro puro, no «un poco oscuro». Está en el comentario del propio `motor.py:198` —*rotar con fondo
transparente: si no, aparece un rectangulo negro detras*— y sigue siendo el fallo número uno cuando alguien
añade un giro a mano. **`c=none` no es opcional en ninguna capa con alfa**, y `ow`/`oh` con `rotw`/`roth`
tampoco: sin ellos el giro recorta las esquinas de la propia pieza.

---

## 4. El halo de croma: dónde compone `overlay`

Con `overlay` en modo `auto` y salida `yuv420p`, la mezcla ocurre en YUV con el croma a la mitad de
resolución. Medido, un verde `(60,190,120)` sale como `(60,189,118)`; con `overlay=…:format=rgb` sale
exacto (`401` §4).

Uno o dos niveles no se ven en una foto. **Sí se ven en dos sitios:** el color de marca, que tiene que
empatar entre piezas, y el filo de un rótulo o un logotipo saturado, donde el croma submuestreado produce
un borde sucio de uno o dos píxeles. Regla: `format=rgb` en las capas de marca y de texto quemado; `auto`
en el resto, que es más barato.

---

## 5. El orden dentro de la propia capa

Media docena de halos salen de encadenar mal los filtros de un solo elemento. El orden que usa el motor y
que conviene no tocar:

```
scale → format=rgba → rotate(c=none) → fade(alpha=1) → colorchannelmixer(aa)
```

- `fade` **antes** de `colorchannelmixer`: al revés, la opacidad fija pisa la rampa del fundido.
- `fade` sin `alpha=1` funde a negro, no a transparente: una pieza que se oscurece en su sitio en vez de
  desaparecer.
- `rotate` **después** de `scale`: girar a tamaño de archivo y reducir después cuesta el triple y no mejora
  nada (`408`).
- Cualquier `gblur` de suavizado de borde (el medio píxel de `204` §3.2) va al final, después del giro.

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Declarar la sombra después de su dueño | La pieza sale un 30 % más oscura y se culpa al recorte |
| `gblur` sobre un PNG sin margen transparente | Sombra con borde recto: parece una mancha, no una sombra |
| Rellenar con `pad` y no restar el relleno a la posición | La sombra aparece desplazada al lado contrario |
| `rotate` sin `c=none` | Rectángulo negro puro detrás de la capa |
| `rotate` sin `ow=rotw(…):oh=roth(…)` | El giro recorta las esquinas de la propia pieza |
| `colorchannelmixer` antes del `fade` | La opacidad fija pisa la rampa: el fundido no se ve |
| `fade` sin `alpha=1` | Funde a negro en su sitio en vez de desaparecer |
| `overlay` en `auto` con un color de marca | Deriva de 1–2 niveles y filo sucio en los bordes duros |
| Sombra visible conscientemente | Está al doble de lo que debería (`204` §3.4, `394`) |

## Relacionado

`400` el orden de render es narrativo · `401` quién gana cuando dos coinciden · `405` el fondo no es una
capa más · `408` lo que cuesta cada capa · `409` depurar un apilado · `102` filtros de vídeo ·
`105` superponer capas · `204` §3 las seis cosas que hacen que un gráfico viva en la escena ·
`394` la sombra que asienta · `392` el escalón de desenfoque ·
`canales_lushows/196` limpiar el alfa · `canales_lushows/23` empatar recorte y fondo
