# 267 — Partículas y elementos de luz

**Qué resuelve:** humo, polvo, vapor, chispas, destellos, resplandores, fugas de luz. Son los elementos
que llenan el aire entre la cámara y el sujeto. Bien usados, hacen que un plano de celular se sienta
tridimensional y **caro**. Mal usados, son la definición exacta de video amateur con filtros.

Este módulo dice cuándo suman de verdad, cómo se generan con lo que tienes, y cómo se integran para que
parezcan parte de la escena y no una calcomanía animada.

---

## 1. Para qué sirven de verdad (no es "adorno")

Tres funciones legítimas. Si tu partícula no cumple una de las tres, es adorno.

**Función 1 — Dar profundidad.** El aire real tiene cosas: polvo, vapor, humedad. Una escena sin nada
entre la cámara y el sujeto se siente plana. **El truco clave: la partícula tiene que ir en DOS capas,
una delante del sujeto y otra detrás.** Eso es lo que crea la sensación de espacio. Una sola capa
encima es una calcomanía; dos capas envuelven al sujeto y el plano se vuelve tridimensional.

**Función 2 — Motivar la luz.** Un rayo de luz solo se ve si hay polvo en el aire. Si tu escena tiene un
resplandor de ventana, un poco de polvo flotando lo hace creíble y le da textura.

**Función 3 — Tapar una costura.** Humo en el punto exacto donde el recorte tiene un borde feo, o
partículas justo en el corte entre dos planos que no cortan bien. Es el uso más práctico y el que nunca
sale en los tutoriales.

**Cuándo es adorno (y hay que quitarlo):**

- Chispas y destellos porque sí, sin nada en la escena que los produzca.
- Partículas en un video de producto donde lo único que importa es ver el producto.
- Humo en un video de comida (baja el apetito, literalmente: enturbia la imagen).
- Cualquier partícula que no puedas explicar: **si no hay una razón física visible para que eso esté en
  el aire, no lo pongas.**

---

## 2. La regla física que hace la diferencia

> Las partículas **están en el espacio de la escena**, no sobre la pantalla.

De esa frase salen las cuatro reglas prácticas:

1. **Se mueven con la cámara.** Si el plano hace un paneo, el polvo se desplaza con él. Un polvo clavado
   sobre una imagen que se mueve grita "capa pegada".
2. **Tienen tamaños distintos.** Las partículas cerca de la cámara son grandes y borrosas; las lejanas
   son chicas y nítidas. Todas del mismo tamaño = falso.
3. **Van delante y detrás.** Ver función 1.
4. **Tienen la temperatura de la luz de la escena.** Polvo blanco azulado en un ambiente cálido de
   bombillo se ve mal. Tíñelo.

Y la regla de opacidad, que es la que más se rompe:

> **Polvo: 8% a 20% de opacidad. Humo: 15% a 35%. Destellos: 20% a 40%.** Si tú notas la capa de
> partículas conscientemente, está al doble de lo que debería.

---

## 3. El modo de fusión: Pantalla, siempre

Casi todos los elementos de partículas y luz vienen **sobre fondo negro**. No hay que recortarlos: se
mezclan con modo **Pantalla** (Screen), que hace que el negro desaparezca y solo quede lo luminoso.

> **Modo Pantalla:** suma la luz de las dos capas. El negro puro no aporta nada, así que se vuelve
> invisible. Es la razón por la que todos los elementos de humo, chispas y destellos vienen sobre negro.

**En CapCut:** clip de partículas en la pista de arriba → panel derecho → **Mezclar / Modo de fusión** →
**Pantalla** → baja la opacidad.

**Con ffmpeg:**

```bash
ffmpeg -y -i plano.mp4 -i particulas.mp4 -filter_complex "\
[1:v]scale=1080:1920,setsar=1[p];\
[0:v][p]blend=all_mode=screen:all_opacity=0.22:shortest=1[out]" \
  -map "[out]" -map 0:a? -c:a copy -c:v libx264 -crf 18 -pix_fmt yuv420p con_particulas.mp4
```

`all_opacity` es tu control de dosis. Empieza en 0.15 y sube hasta que se note apenas.

**Modo Suma (`addition`)** si quieres algo más brillante y contrastado; **modo Aclarar (`lighten`)** si
el elemento tiene grises sucios que en Pantalla se ven como una neblina gris.

---

## 4. De dónde sacas las partículas

**4.1. Grabarlas tú (la mejor y la más barata).** Es sorprendentemente fácil y queda mejor que
cualquier cosa generada:

- **Polvo:** un cuarto oscuro, una linterna de celular apuntando a un lado, y sacudes una toalla frente
  a la luz. Graba a 60 fps. Tienes polvo real.
- **Humo:** vapor de agua caliente, o incienso, contra un fondo negro (una cobija oscura) con una luz
  lateral.
- **Bokeh / luces desenfocadas:** cualquier calle de noche, grabada con el enfoque en manual al mínimo.
  Se convierte en círculos de luz preciosos.
- **Fugas de luz:** apunta el celular hacia una lámpara y pasa el dedo o un CD por delante del lente.

Todo eso se graba sobre negro, se mezcla en Pantalla, y **es real**: tiene el movimiento y la
irregularidad que ningún generador reproduce bien.

**4.2. La biblioteca de CapCut.** Efectos → busca "polvo", "humo", "brillo", "partículas". Hay bastante y
está listo. **El problema: son los mismos que usa todo el mundo**, así que si tu marca los usa se ve
genérica. Úsalos con opacidad muy baja y funcionan.

**4.3. Generarlas con ffmpeg.** Se puede, con limitaciones. Ver sección 5.

**4.4. Bancos de stock.** Muchos elementos de humo y chispas en 4K sobre negro, gratis y de pago.
Verifica la licencia (`128`).

---

## 5. Generar luz y partículas con ffmpeg

ffmpeg no tiene un generador de partículas. Lo que sí puede hacer, y muy bien, es **luz**.

### 5.1. Resplandor (glow / bloom) — el mejor efecto del módulo

Coge lo más brillante del plano, lo difumina y lo suma encima. El resultado: las luces "sangran" como en
una cámara de cine, y el video entero se ve más caro. Cuesta un comando.

```bash
ffmpeg -y -i plano.mp4 -filter_complex "\
[0:v]split=2[base][br];\
[br]lutyuv=y='if(gt(val,185),val,16)',gblur=sigma=26[glow];\
[base][glow]blend=all_mode=screen:all_opacity=0.40[out]" \
  -map "[out]" -map 0:a? -c:a copy -c:v libx264 -crf 18 -pix_fmt yuv420p con_glow.mp4
```

Los tres números: `185` es el umbral (qué tan brillante tiene que ser un píxel para brillar; sube a 210
para que solo brillen las luces reales), `sigma=26` es qué tanto se derrama, y `all_opacity=0.40` es la
dosis.

> ⚠️ **Verifica esto en tu equipo antes de usarlo en producción.** El `lutyuv` con umbral puede
> comportarse distinto según el rango de color del material. Pruébalo con `-t 2` y mira el resultado
> antes del render completo. Si todo el plano se vuelve lechoso, sube el umbral.

**Este efecto sí vale siempre la pena.** Es un minuto de trabajo y funciona en casi cualquier plano con
una fuente de luz visible: una ventana, una lámpara, un reflejo en metal.

### 5.2. Rayo de luz de ventana

Un degradado difuminado, en diagonal, en modo Pantalla. Suena tonto y funciona:

```bash
ffmpeg -y -i plano.mp4 -f lavfi -i "color=c=0xFFE7B8:s=1080x1920" -filter_complex "\
[1:v]geq=r='r(X,Y)':g='g(X,Y)':b='b(X,Y)':\
a='if(between(X+Y*0.6, 300, 900), 190*(1-abs((X+Y*0.6)-600)/300), 0)',\
gblur=sigma=60,format=rgba[rayo];\
[0:v][rayo]overlay=0:0[out]" \
  -map "[out]" -map 0:a? -c:a copy -c:v libx264 -crf 18 -pix_fmt yuv420p con_rayo.mp4
```

La expresión dibuja una banda diagonal que se desvanece hacia los lados, y `gblur=sigma=60` la vuelve un
rayo suave. Cambia `0.6` para la inclinación y `300/900` para la posición.

> ⚠️ **Verifica esto en tu equipo antes de usarlo en producción.** `geq` es lento (puede tardar minutos
> en 1080×1920) y la sintaxis es delicada. Genera el rayo **una vez como PNG** y reúsalo:
>
> ```bash
> ffmpeg -y -f lavfi -i "color=c=0xFFE7B8:s=1080x1920" -vf "geq=...,gblur=sigma=60,format=rgba" \
>   -frames:v 1 rayo.png
> ```

### 5.3. Viñeta de luz y fuga de color

La fuga de luz (light leak) más simple: un óvalo de color cálido en una esquina, en modo Pantalla,
apareciendo y desapareciendo:

```bash
ffmpeg -y -i plano.mp4 -f lavfi -i "color=c=0xFF7A3C:s=1080x1920" -filter_complex "\
[1:v]vignette=angle=PI/2:x0=200:y0=250:mode=backward,gblur=sigma=90[fuga];\
[0:v][fuga]blend=all_mode=screen:all_opacity='0.35*sin(PI*T/2)':shortest=1[out]" \
  -map "[out]" -map 0:a? -c:a copy -c:v libx264 -crf 18 -pix_fmt yuv420p fuga.mp4
```

La opacidad animada con `sin(PI*T/2)` hace que entre y salga sola. **Verifica en tu equipo**: la
expresión de `all_opacity` con variable temporal no funciona en todas las versiones; si falla, usa un
valor fijo y anima la aparición con `fade` sobre la capa.

### 5.4. Lo que ffmpeg NO puede hacer

Sé honesto: **no hay sistema de partículas.** No puedes generar chispas que caen con física, humo
volumétrico, ni polvo con turbulencia. Para eso hace falta After Effects, Blender o un banco de
elementos. Si necesitas partículas de verdad: **grábalas** (4.1) o **descárgalas**.

---

## 6. Integrar las partículas (el paso que se salta todo el mundo)

Una capa de humo puesta encima y ya está, se ve pegada. Cuatro arreglos:

**1. Tíñela con la luz de la escena.** Si tu escena es cálida, el humo tiene que ser cálido:

```bash
[1:v]colortemperature=temperature=3800:mix=0.7,scale=1080:1920[p];
```

**2. Ponla en dos capas, delante y detrás del sujeto.** Con el recorte del sándwich (`262`): partículas
en la pista de abajo (detrás), sujeto recortado arriba, y **otra** capa de partículas encima con opacidad
aún más baja (la mitad). Esa segunda capa es la que envuelve.

**3. Desenfoca la capa de adelante.** Lo que pasa cerca del lente está fuera de foco. `gblur=sigma=6` a
la capa delantera la hace inmediatamente creíble.

**4. Que se muevan con la cámara.** Si el plano hace un paneo lento, desplaza la capa de partículas en
la misma dirección con `overlay=x='...t...'`.

---

## 7. La dosis: cómo saber si te pasaste

**La prueba del interruptor:** exporta dos versiones, con y sin partículas, y mira una detrás de la
otra. Si la diferencia es evidente y llamativa, **te pasaste**. La versión correcta se siente "mejor"
sin que puedas decir exactamente qué cambió.

```bash
ffmpeg -y -i sin_particulas.mp4 -i con_particulas.mp4 -filter_complex \
  "[0:v]scale=540:960[a];[1:v]scale=540:960[b];[a][b]hstack" \
  -c:v libx264 -crf 20 -pix_fmt yuv420p comparacion.mp4
```

**La prueba de la compresión:** las partículas finas y el grano son lo primero que Instagram y TikTok
destruyen al recomprimir. Un polvo delicadísimo que te tomó media hora puede desaparecer por completo o
convertirse en bloques. **Súbelo a una cuenta de prueba y míralo ahí antes de darlo por bueno.** Esta
prueba es específica de partículas y vale oro.

---

## 8. El presupuesto de este módulo

| Efecto | Tiempo | Vale la pena en un reel |
|---|---|---|
| **Glow / resplandor** con ffmpeg | 1 min | **Siempre.** Es el mejor negocio del bloque |
| Preset de partículas de CapCut a opacidad baja | 1 min | Sí, con moderación |
| Fuga de luz en una transición | 2 min | Sí |
| Polvo grabado por ti, una capa | 5 min | Sí, si el plano tiene luz visible |
| Polvo en dos capas (delante y detrás) | 15 min | Solo en el plano principal del video |
| Rayo de luz con `geq` | 10 min | Rara vez; el glow da el 70% del efecto |
| Humo integrado y teñido | 20 min | Solo si el humo tiene motivo en la escena |
| Sistema de partículas real | horas | **No.** Necesitas software que no tienes |

---

## Errores comunes

1. **Poner partículas sin motivo en la escena.** Si no hay nada que produzca ese humo o esas chispas,
   se ve como filtro.
2. **Una sola capa encima.** Sin la capa de atrás no hay profundidad: es una calcomanía animada.
3. **Opacidad al 60% u 80%.** Polvo 8–20%, humo 15–35%. Si lo notas conscientemente, va al doble.
4. **Partículas todas del mismo tamaño.** Las cercanas grandes y borrosas, las lejanas chicas.
5. **No desenfocar la capa de adelante.** Lo que está cerca del lente está fuera de foco.
6. **Partículas frías en una escena cálida.** Tíñelas con la temperatura de la escena.
7. **Partículas clavadas en un plano que se mueve.** Deben desplazarse con la cámara.
8. **Usar Normal en vez de Pantalla.** El elemento viene sobre negro: en Normal tapas el video con un
   rectángulo negro.
9. **Humo en un video de comida.** Enturbia el plato y baja el apetito. La excepción es el vapor que sale
   del plato, que es lo contrario y sí suma.
10. **Usar el preset de partículas de moda de CapCut al 100%.** Lo usa todo el mundo y se reconoce al
    instante.
11. **No probar cómo sobrevive a la compresión.** Las partículas finas son lo primero que Instagram
    destruye. Súbelo a una cuenta de prueba.
12. **Esperar que ffmpeg genere partículas con física.** No las genera. Grábalas o descárgalas.
13. **Renderizar con `geq` sobre video completo.** Es lentísimo. Genera el elemento como PNG una vez y
    reúsalo.
14. **Saltarse el glow.** Es un minuto de trabajo y es el efecto de luz que más rinde de todos.

---

## Checklist

Antes de dar por buena una capa de partículas o luz:

- [ ] Puedo **explicar por qué** esa partícula está en el aire (ventana, vapor, polvo del sitio).
- [ ] Cumple una de las **tres funciones**: profundidad, motivar la luz, o tapar una costura.
- [ ] Está en modo **Pantalla** (o Suma / Aclarar), no en Normal.
- [ ] La **opacidad** está en el rango bajo (polvo 8–20%, humo 15–35%, destellos 20–40%).
- [ ] Hay una capa **detrás** del sujeto y otra **delante**, no solo encima.
- [ ] La capa de adelante está **desenfocada**.
- [ ] Las partículas están **teñidas con la temperatura** de la luz de la escena.
- [ ] Si el plano se mueve, las partículas **se mueven con él**.
- [ ] Probé el **glow** antes de complicarme con partículas: un minuto y rinde más.
- [ ] Hice la **prueba del interruptor**: la diferencia se siente, no se ve.
- [ ] Lo **subí a una cuenta de prueba** y comprobé que sobrevive a la compresión.
- [ ] No usé el preset de moda de CapCut al 100%.
- [ ] Si esto me tomó más de 15 minutos en un reel, leí `269`.
