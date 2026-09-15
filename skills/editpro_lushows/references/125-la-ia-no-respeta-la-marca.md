# 125 — La IA no respeta tu marca: por qué deriva y las tres formas de imponérsela

## La prueba que zanja la discusión

Prueba real, agosto de 2026. Una marca con **exactamente dos colores**: azul marino y blanco. Dos.
No es un sistema complejo. Es lo más simple que puede tener una identidad.

Se le pidió a Veo un plano con esa paleta, siendo explícito en el prompt.

Lo que devolvió:

- **piedras color crema**
- **chispas doradas**
- **botellas marrones**

Ninguno de esos colores existe en la marca. No es que se haya acercado y errado un tono: es que
inventó una paleta completa que nadie pidió.

Y aquí está lo importante, la parte que la gente no acepta:

> **Esto no es un fallo. Es cómo funciona el modelo.**
> No lo vas a arreglar pidiéndoselo mejor.

Deja de perder tardes reformulando el prompt. La solución no está ahí.

---

## Por qué deriva (la explicación corta y honesta)

Un modelo generativo no tiene un concepto de "paleta". No tiene una lista de colores permitidos con
una validación al final. Lo que tiene es una distribución estadística aprendida de millones de
imágenes y videos.

Cuando le dices "azul marino y blanco, sobre piedra", el modelo no busca "azul marino" en una tabla.
Busca **la región del espacio latente donde viven las escenas de piedra**. Y en ese territorio, las
piedras son crema, beige y gris, porque así son las piedras en todas las fotos del mundo. El "azul
marino" que le pediste tira hacia un lado; los millones de piedras crema del entrenamiento tiran
hacia el otro. Y los millones ganan.

Tres consecuencias prácticas:

1. **La deriva es proporcional a lo raro que sea tu pedido.** Pedir un cielo azul funciona. Pedir
   una piedra azul marino no, porque el modelo tiene que pelear contra su propio conocimiento.
2. **La deriva empeora con el movimiento.** Un plano de video tiene 24 fotogramas por segundo y cada
   uno es una oportunidad de deslizarse un poco más hacia el promedio. Una imagen fija deriva menos
   que un video.
3. **La deriva empeora con la duración.** El segundo 1 puede estar bien y el segundo 6 ya está en
   otra película.

Lo mismo aplica al estilo, no solo al color. Le pides "ilustración plana de línea gruesa" y a los
tres segundos hay degradados y sombras suaves, porque el promedio de "ilustración" tiene degradados.

---

## Las tres formas de imponer la marca

Hay tres, y **se usan juntas**, no en lugar de. En orden de eficacia:

```
1. REFERENCIA      — enséñale, no le describas       (más eficaz, actúa antes)
2. PROHIBICIÓN     — dile qué NO puede aparecer      (reduce el daño)
3. CORRECCIÓN      — arréglalo en post               (la única garantía)
```

---

## Forma 1 — Referencia: enséñale, no le describas

**Nunca describas tu marca con adjetivos. Pásale el archivo.**

La diferencia entre escribir "estilo retro cartoon, colores cálidos, trazo grueso" y pasarle **el
diseño real de la marca como imagen de referencia** es, verificado en prueba real, **abismal**. Con
adjetivos sale cualquier cosa. Con el archivo sale on-brand a la primera.

Esto está desarrollado en el módulo `126`. Aquí solo la regla operativa:

- Si el modelo acepta imagen de referencia, **úsala siempre**.
- La referencia manda sobre el prompt. El prompt es la acción; la referencia es el aspecto.
- Con Veo, si le pasas imagen de referencia, recuerda la trampa de parámetros del módulo `121`
  (nada de `resolution`, `enhancePrompt:false` ni `negativePrompt`).

Qué pasarle como referencia:
- El diseño ya terminado del fotograma cero (lo mejor)
- Una pieza gráfica existente de la marca, en el estilo exacto
- Un fotograma de un video anterior que sí quedó bien

Qué **no** pasarle:
- Un moodboard con seis estilos distintos (promedia y sale barro)
- El logo suelto sobre blanco (le enseña "logo", no "estilo")
- Una foto de referencia con la paleta equivocada, esperando que solo copie la composición

**Limitación honesta**: la referencia controla mucho mejor el **estilo** que el **color exacto**.
Incluso partiendo de tu diseño real, el video va a derivar de tono. Reduce el daño; no lo elimina.

---

## Forma 2 — Prohibición explícita

Lo que le dices que NO haga pesa más de lo que la gente cree. Y funciona mejor cuando es **concreto
y redundante**.

### Para colores

No digas "usa solo azul marino y blanco". Di **qué colores están prohibidos**:

```
Color palette strictly limited to deep navy blue (#0B1E3A) and white (#FFFFFF).
NO gold, no amber, no orange, no cream, no beige, no brown, no warm tones,
no sparks, no glitter, no bokeh highlights.
Monochromatic blue and white only.
```

Fíjate en el detalle: **prohíbe explícitamente lo que sabes que va a inventar**. Si en la prueba
anterior salieron chispas doradas, la próxima vez prohíbes chispas y dorado por nombre. Vas
construyendo la lista negra de tu marca a fuerza de pruebas.

### Para texto

Obligatorio siempre (módulo `122`):

```
absolutely no text, no letters, no words, no numbers, no logos, no watermarks, no signage
```

### Para estilo

```
flat vector illustration, thick uniform outlines, no gradients, no soft shadows,
no photorealism, no 3D rendering, no lens flare
```

### Dos advertencias

- **En inglés funciona mejor.** Aunque el resto del prompt esté en español. Los modelos están
  entrenados con etiquetas en inglés.
- **Con Veo e imagen de referencia, `negativePrompt` como parámetro mata la petición en seco**
  (módulo `121`). Si quieres prohibir algo en ese caso, mételo **dentro del texto del prompt**, no
  en el parámetro.

**Limitación honesta**: la prohibición reduce la frecuencia de la derivación, no la elimina. Vas a
seguir viendo dorado de vez en cuando.

---

## Forma 3 — Corrección en post: la única garantía

Esta es la que de verdad funciona, y es la que te separa de la gente que "usa IA".

> **No le pidas a la IA que respete la paleta. Fuérzala tú después.**

### El duotono forzado

Si tu marca son dos colores, la respuesta es un **duotono**: conviertes el plano a luminancia y
remapeas esa luminancia a un degradado entre tus dos colores. Las sombras van al color oscuro, las
luces al claro. Lo que estaba dorado pasa a ser azul claro. Lo que estaba crema pasa a ser azul
medio. **Deja de existir el problema.**

En ffmpeg, con una tabla de consulta (LUT) de un canal:

```bash
# duotono azul marino (#0B1E3A) → blanco, forzado sobre todo el plano
ffmpeg -i plano.mp4 -vf "
  format=gray,
  lutrgb=
    r='11+(255-11)*val/255':
    g='30+(255-30)*val/255':
    b='58+(255-58)*val/255'
" -c:a copy plano_marca.mp4
```

Cómo se lee: primero `format=gray` mata todo el color original (adiós dorado, adiós crema). Después
`lutrgb` reconstruye color mapeando cada nivel de gris a un punto entre tu azul (11, 30, 58) y el
blanco (255, 255, 255).

Resultado: **matemáticamente imposible que aparezca un color fuera de tu paleta.** No es una
sugerencia al modelo; es una imposición.

### Duotono con mezcla parcial

El duotono al 100% a veces se siente demasiado plano, sobre todo si el plano tenía piel o comida.
Mezcla:

```bash
ffmpeg -i plano.mp4 -filter_complex "
  [0:v]split=2[orig][dt];
  [dt]format=gray,lutrgb=r='11+244*val/255':g='30+225*val/255':b='58+197*val/255'[duo];
  [orig][duo]blend=all_mode=normal:all_opacity=0.75[out]
" -map "[out]" -map 0:a? -c:a copy plano_marca.mp4
```

`all_opacity=0.75` te deja un 25% del color original. Juega entre 0.6 y 0.9 según la pieza.

### Solo matar el color intruso

A veces el plano está casi bien y solo hay que quitar el dorado. Desatura selectivamente ese rango:

```bash
# baja la saturación de los amarillos/dorados y empuja el balance hacia el azul
ffmpeg -i plano.mp4 -vf "
  colorbalance=rm=-0.10:gm=-0.05:bm=0.15,
  eq=saturation=0.75
" -c:a copy plano_corregido.mp4
```

Menos radical, más natural, menos garantizado. Úsalo cuando la derivación es leve.

### La LUT de marca

Si vas a hacer esto muchas veces, no repitas filtros: **construye una LUT `.cube` de tu marca** una
sola vez y aplícala a todo (módulo `61`):

```bash
ffmpeg -i plano.mp4 -vf "lut3d=marca.cube" -c:a copy plano_marca.mp4
```

Ventaja enorme: **el material generado y el material filmado pasan por la misma LUT**, así que
terminan pareciendo del mismo mundo. Esa es la diferencia entre una pieza que se siente cosida y una
que se siente coherente.

---

## El flujo completo, en orden

```
1. Diseña el fotograma cero en TUS colores (módulo 122)
2. Pásalo como IMAGEN DE REFERENCIA (forma 1)
3. En el texto del prompt, PROHÍBE los colores intrusos que ya sabes que va a inventar (forma 2)
4. Genera
5. Míralo esperando derivación. Va a haber. Es normal.
6. FUERZA el color en post con duotono o LUT (forma 3)
7. Pon logo y texto encima, con los archivos reales
8. Compara el resultado final contra una pieza anterior de la marca. ¿Se ven hermanas?
```

El paso 5 es el cambio de mentalidad. **Espera la derivación.** No te frustres, no reformules el
prompt cuarenta veces. Presupuesta el paso de corrección como parte del trabajo, igual que
presupuestas exportar.

---

## Lo que nunca le confías a la IA

Lista corta y sin excepciones:

| Elemento | Por qué | Qué haces |
|---|---|---|
| **El logo** | Lo va a deformar, siempre | Superponer el archivo vectorial real |
| **El texto** | Letras deformadas, marca mal escrita | Tipografía real en post (módulo `40`) |
| **El color exacto de marca** | Deriva por diseño | Duotono / LUT en post |
| **La tipografía** | No sabe qué fuente es | Post |
| **El empaque del producto** | Inventa etiquetas | Foto real o composición |
| **Un dato numérico en pantalla** | Puede cambiar un dígito | Post |

Todo eso es **post**. La IA hace el fondo, el movimiento y la atmósfera. La marca la pones tú.

---

## Errores comunes

- **Creer que la derivación es un fallo que se arregla.** Es cómo funciona el modelo. Presupuesta la
  corrección.
- **Reformular el prompt cuarenta veces.** Nunca vas a ganar esa pelea. Se gana en post.
- **Describir la marca con adjetivos.** "Retro cálido artesanal" te da cualquier cosa. Pásale el
  archivo.
- **No prohibir explícitamente los colores intrusos.** Si ya salió dorado una vez, prohíbe "gold" y
  "sparks" por nombre en el siguiente intento.
- **Prohibir solo en español.** Ponlo en inglés.
- **Mandar `negativePrompt` como parámetro a Veo con imagen de referencia.** Rechazo en seco
  (módulo `121`). Mete la prohibición dentro del texto del prompt.
- **Aplicar el duotono al 100% en todo.** A veces mata la piel y la comida. Mezcla al 70–80%.
- **Corregir cada plano a mano con valores distintos.** Construye una LUT de marca y aplícala a
  todos.
- **No pasar el material filmado por la misma LUT.** Ahí es donde se ve la costura entre lo generado
  y lo real.
- **Dejar que la IA escriba el logo o el texto.** Nunca. Van encima, con los archivos reales.
- **Aprobar un plano mirándolo solo.** Míralo al lado de una pieza anterior de la marca. Si no se
  ven hermanas, no está listo.
- **Prometerle al cliente "la IA respeta tu identidad".** No la respeta. Tú se la impones. Dile la
  verdad y cóbrale ese trabajo.

---

## Checklist

- [ ] Tengo los códigos exactos de la paleta de marca a la vista (hex o RGB)
- [ ] Pasé el diseño real como **imagen de referencia**, no una descripción con adjetivos
- [ ] El prompt **prohíbe por nombre** los colores intrusos que ya vi derivar antes
- [ ] Las prohibiciones están en **inglés** y son redundantes
- [ ] Si es Veo con imagen de referencia, la prohibición va **dentro del prompt**, no en
      `negativePrompt`
- [ ] Miré el resultado **esperando** derivación, no confiando en que salió bien
- [ ] Forcé el color en post: **duotono, LUT o corrección selectiva**
- [ ] La misma LUT de marca se aplica al material generado **y** al material filmado
- [ ] El **logo** va superpuesto desde el archivo original
- [ ] El **texto** va en post, con la tipografía real
- [ ] Ningún dato numérico en pantalla lo escribió el modelo
- [ ] Comparé el resultado final contra una pieza anterior de la marca, lado a lado
- [ ] El presupuesto y el tiempo de entrega incluyen el paso de corrección de color
