# 257 — Look y emulación de película

El módulo `63` te dio el look cinematográfico a nivel práctico: contraste, saturación, curvas, y por
qué el naranja-y-turquesa está gastado. Este módulo va al nivel de colorista: **qué hace "cine" a una
imagen, físicamente**, y cómo se emula honestamente con ffmpeg.

La tesis del módulo, y va en contra de lo que cree la mayoría:

> Lo que lees como "cine" **no es la paleta de colores**. Es cómo la imagen **responde a la luz**:
> cómo entra en el negro, cómo sale del blanco, y qué le pasa a un punto de luz brillante.

Por eso un video con la paleta de *Blade Runner* puede seguir viéndose a video, y una imagen sin
ningún tinte puede verse a cine.

---

## 1. Los cinco rasgos, en orden de importancia

| # | Rasgo | Qué es | ¿Se puede emular? |
|---|---|---|---|
| 1 | **Hombro en las altas** (*shoulder*) | el blanco no llega de golpe: se acerca despacio | ✅ sí, con `curves` |
| 2 | **Pie levantado** (*toe*) | el negro no es 0 puro: tiene un piso mínimo | ✅ sí, con `curves` |
| 3 | **Halación** | los puntos de luz muy brillantes sangran un halo rojizo | ✅ sí, con `blend=screen` |
| 4 | **Grano** | textura orgánica, más en un canal que en otro | ✅ sí, con `noise` |
| 5 | **Diafonía de color** (*crosstalk*) | los colores se contaminan entre sí, ninguno queda puro | ✅ parcialmente |

Y lo que **no** se puede emular, para ser honestos desde el principio:

- El rango dinámico del negativo (14+ pasos). Tu celular tiene 10–11 y lo que se quemó, se quemó.
- El desenfoque de un lente rápido de cine sobre un sensor grande.
- El movimiento a 24 fps con obturador de 180° si grabaste a 60 con obturador rápido.

Sobre lo último: si grabaste con obturador muy rápido, cada cuadro está congelado y el movimiento se
ve "de video". Eso no lo arregla ningún filtro, y es de las cosas que hay que pedir en rodaje (`170`
en adelante).

---

## 2. La curva: el rasgo #1 y #2 juntos

Una película no es una recta. La cantidad de luz que le llega y la densidad que produce se relacionan
con una curva en forma de S **asimétrica**: el pie es corto y el hombro es largo.

Una curva "de cine" honesta con `curves`:

```bash
ffmpeg -i corregido.mp4 -vf "curves=all='0/0.04 0.18/0.13 0.5/0.5 0.82/0.86 1/0.96'" \
  -c:v libx264 -crf 16 cine.mp4
```

Punto por punto:

| Punto | Qué hace |
|---|---|
| `0/0.04` | **el negro no llega a 0**: piso levantado, aire en las sombras |
| `0.18/0.13` | las sombras bajas caen un poco: da cuerpo sin cerrar |
| `0.5/0.5` | los medios no se mueven: **la piel se queda donde estaba** |
| `0.82/0.86` | las altas suben pero cada vez menos: hombro |
| `1/0.96` | **el blanco no llega a 1**: no hay reventón |

Los dos extremos son los que hacen el trabajo. Un negro en 0,04 y un blanco en 0,96 comprimen el
rango... y sin embargo la imagen se ve **más rica**, no más plana. Eso es lo contraintuitivo: la
sensación de profundidad viene del detalle en los extremos, no de tener el rango completo.

### El error del caso real, aplicado aquí

En el bar se usó una S con el punto de sombras en **0,22 / 0,19**. Sobre material bien expuesto, esa
curva le da cuerpo a la imagen. Sobre material que vivía en Y = 70–78 (o sea, entre 0,27 y 0,31 de la
escala), lo que hizo fue **hundir la zona donde estaba toda la imagen**.

> Una curva no es buena o mala en abstracto: es buena **para un rango de entrada**. Antes de aplicar
> una curva, mira dónde vive tu material en la forma de onda (`252`).

Para material oscuro, la curva de cine se invierte en su primera mitad: **se levanta** el pie.

```bash
# curva de cine para material que ya está oscuro (Y ≈ 70-80)
ffmpeg -i bar_neon.mp4 -vf "curves=all='0/0.06 0.15/0.20 0.5/0.55 0.85/0.88 1/0.97'" \
  -c:v libx264 -crf 16 bar_cine.mp4
```

Fíjate: `0.15/0.20` **sube** en vez de bajar. Abre la penumbra, que es donde está el contenido, y
mantiene el hombro arriba.

---

## 3. Halación: el rasgo que más "cine" da por menos trabajo

En una película física, la luz muy brillante atraviesa la emulsión, rebota en la base y vuelve,
formando un halo suave alrededor de las luces fuertes. Como la capa roja es la más profunda, **ese
halo es rojizo**. Por eso los neones, las velas y los bombillos en cine tienen un resplandor cálido
que en video digital no existe.

Emulación verificada:

```bash
ffmpeg -y -i corregido.mp4 -filter_complex "\
[0:v]split=2[base][hi];\
[hi]format=gbrp,curves=all='0/0 0.72/0 0.92/1 1/1',gblur=sigma=22,\
colorchannelmixer=rr=1:gg=0.35:bb=0.20,format=gbrp[glow];\
[base]format=gbrp[b];\
[b][glow]blend=all_mode=screen:all_opacity=0.35,format=yuv420p" \
  -c:v libx264 -crf 16 -c:a copy halacion.mp4
```

Paso por paso:

1. `curves=all='0/0 0.72/0 0.92/1 1/1'` — **aísla solo las altas luces**. Todo lo que esté por debajo
   del 72 % de brillo queda en negro; entre 72 % y 92 % hay una rampa. Es un calificador de luma
   (`253`).
2. `gblur=sigma=22` — las desenfoca hasta volverlas un resplandor.
3. `colorchannelmixer=rr=1:gg=0.35:bb=0.20` — **tiñe el resplandor de rojo-naranja**. Este es el
   parámetro que hace que se lea como película y no como "glow de plantilla".
4. `blend=all_mode=screen:all_opacity=0.35` — lo suma en modo pantalla, que solo aclara.

Dosis honestas:

| Parámetro | Discreto | Notorio | Se ve falso |
|---|---|---|---|
| `all_opacity` | 0.20 – 0.30 | 0.35 – 0.50 | > 0.60 |
| `sigma` | 12 – 20 | 22 – 35 | > 50 (mancha) |
| umbral de la curva | 0.80 | 0.72 | < 0.60 (brilla todo) |

Dónde luce muchísimo: neones, velas, ventanas, faros, pantallas. **El caso del bar es el escenario
perfecto**: un neón morado con halación se ve rodado; el mismo neón sin halación se ve grabado con
celular.

Ojo con una cosa: si el material ya tiene glow del lente barato del celular, la halación se le suma y
queda sucia. Míralo antes.

---

## 4. Grano: cómo hacerlo bien y no arruinar el archivo

El grano de película **no es ruido parejo**. Tres diferencias que sí importan:

1. **Es distinto en cada canal.** La capa azul tiene el grano más grueso, la verde el más fino.
2. **Es más visible en los medios** que en negros y blancos.
3. **Cambia en cada cuadro** (por eso `allf=t`, *temporal*).

```bash
# Grano con estructura por canal (c0=luma, c1=U, c2=V)
ffmpeg -i cine.mp4 -vf "noise=c0s=6:c1s=3:c2s=3:allf=t+u" -c:v libx264 -crf 16 granulado.mp4
```

| Intensidad (`c0s`) | Resultado |
|---|---|
| 2 – 4 | apenas perceptible. Sirve para matar bandeado (`251`) |
| 5 – 8 | **el rango usable**: textura sin ruido |
| 10 – 15 | grano declarado, estilo Super 8 |
| > 20 | ruido; además destruye la compresión |

**Lo que nadie te dice del grano: cuesta bitrate.** El grano es información aleatoria, lo peor que
existe para un compresor. Un video con `c0s=12` puede pesar 40 % más que el mismo sin grano, y si la
plataforma lo recomprime (todas lo hacen), lo primero que va a destruir es justamente el grano,
dejándote un video ruidoso Y con artefactos.

Regla para redes sociales: **grano suave (4–7) y CRF un punto mejor** (más bajo) para compensar.

```bash
ffmpeg -i cine.mp4 -vf "noise=c0s=5:c1s=2:c2s=2:allf=t+u,format=yuv420p" \
  -c:v libx264 -crf 17 -preset slow -c:a copy final.mp4
```

Y el grano va **al final de la cadena**, después de la LUT y de todo lo demás. Si lo pones antes,
cada filtro posterior lo amplifica.

---

## 5. Diafonía de color: por qué los colores de cine nunca son puros

En película, cada capa de tinte responde un poco a la luz de las otras. Resultado: **ningún color
queda puro**. Un rojo de película siempre tiene algo de verde adentro; un azul siempre tiene algo de
rojo. En digital, un rojo saturado es rojo puro, y eso el ojo lo lee como "de computador".

Emulación simple con `colorchannelmixer`, que es exactamente una matriz de diafonía:

```bash
# 4-6% de contaminación cruzada: sutil, cambia mucho la sensación
ffmpeg -i cine.mp4 -vf "colorchannelmixer=rr=0.94:rg=0.04:rb=0.02:gr=0.04:gg=0.92:gb=0.04:br=0.02:bg=0.05:bb=0.93" \
  -c:v libx264 -crf 16 crosstalk.mp4
```

Los valores de cada fila deben sumar cerca de 1,0 para no cambiar el brillo general. Con 0,02–0,06
fuera de la diagonal basta. Con más, la imagen se vuelve gris.

Y la versión aún más simple, que sirve casi igual: **baja un poco la saturación y sube el contraste**.
Casi todo el efecto "de película" en saturación es que la película satura **menos** de lo que la gente
cree.

---

## 6. Las emulaciones honestas (y las deshonestas)

**Honesto:** "esta cadena aproxima la respuesta de un negativo: hombro largo, pie levantado, halación
cálida, grano fino". Verificable, reproducible, y el cliente sabe qué compró.

**Deshonesto:** "esta es la LUT de Kodak 2383". No lo es. Las emulaciones reales de stock de película
se construyen midiendo el negativo con un espectrofotómetro, y las que circulan gratis por internet
son aproximaciones de aproximaciones, muchas hechas de un screenshot.

Tres cosas ciertas sobre los "film stocks" en la práctica:

1. **Los nombres son de mercadeo.** Una LUT llamada "Kodak Vision3 500T" en un paquete de $20 no tiene
   relación medible con la película.
2. **La película real depende del revelado y del escaneo**, que cambian el resultado más que el stock.
3. **Lo que sí es real y copiable es la forma de la curva**, que es lo que hemos hecho arriba.

Por eso este módulo no te da "presets de stock": te da los cinco rasgos, para que armes el tuyo y
sepas qué hace cada pieza.

---

## 7. La cadena completa de look, en orden

```bash
ffmpeg -y -i corregido.mp4 -filter_complex "\
[0:v]curves=all='0/0.04 0.18/0.13 0.5/0.5 0.82/0.86 1/0.96',\
colorchannelmixer=rr=0.95:rg=0.03:rb=0.02:gr=0.03:gg=0.94:gb=0.03:br=0.02:bg=0.04:bb=0.94,\
eq=saturation=0.96,split=2[base][hi];\
[hi]format=gbrp,curves=all='0/0 0.75/0 0.93/1 1/1',gblur=sigma=20,\
colorchannelmixer=rr=1:gg=0.35:bb=0.20,format=gbrp[glow];\
[base]format=gbrp[b];\
[b][glow]blend=all_mode=screen:all_opacity=0.28,format=yuv420p,\
vignette=PI/5,noise=c0s=5:c1s=2:c2s=2:allf=t+u,limiter=min=16:max=235" \
  -c:v libx264 -crf 17 -preset slow -c:a copy look_final.mp4
```

El orden importa y no es negociable:

```
curva → diafonía → saturación → halación → viñeta → grano → legalizar
```

- La halación va **después** de la curva, porque necesita saber cuáles son las altas luces finales.
- El grano va **al final**, para que nada lo amplifique.
- El `limiter` siempre de último (`251`).

Y todo esto va **después** de corregir y emparejar (`250`). Un look sobre material disparejo hace la
disparidad más visible, no menos.

---

## 8. El toque que casi nadie usa: micro-movimiento de cuadro

En proyección de película, el cuadro nunca está perfectamente quieto: la ventanilla tiene juego y la
imagen "respira" (*gate weave*). Un movimiento sub-píxel constante hace que el video se sienta
orgánico sin que nadie sepa por qué.

```bash
ffmpeg -y -i look_final.mp4 -vf \
  "crop=in_w-8:in_h-8:4+1.5*sin(2*PI*n/17):4+1.2*cos(2*PI*n/13),scale=1080:1920:flags=lanczos,format=yuv420p" \
  -c:v libx264 -crf 17 -c:a copy respirado.mp4
```

Recorta 8 píxeles y mueve el recorte 1,5 px en horizontal y 1,2 px en vertical, con dos periodos
distintos (17 y 13 cuadros) para que no se sienta un patrón. Después reescala al tamaño original.

Dosis: **por encima de 2,5 píxeles se nota y molesta**. Y no lo uses en un video con texto en pantalla
fijo: el texto tiembla y se ve como un error.

---

## 9. Cuánto look aguanta un video social

Honestamente: **menos del que crees**.

| Formato | Look recomendado |
|---|---|
| Reel / TikTok de producto | curva suave + halación discreta. Nada más |
| Testimonio | prácticamente nada: la piel manda (`254`) |
| Anuncio de marca | look completo si la marca lo pide, siempre protegiendo la piel |
| Pieza de imagen / manifiesto | aquí sí, look declarado |

Dos razones duras: la compresión de las plataformas destroza el grano y el halo (`68`), y el
espectador ve el video en un celular al 40 % de brillo, donde tu pie levantado en 0,04 no se
distingue de 0,00.

---

## Errores comunes

- **Creer que "cine" es la paleta.** Es la respuesta a la luz: hombro, pie, halación.
- **Aplicar una curva en S sin mirar dónde vive el material.** El error del caso real: hundió lo que
  ya estaba oscuro.
- **Mover los medios en la curva de look.** Ahí está la piel. La curva de cine deja `0.5/0.5` quieto.
- **Halación sobre todo el cuadro** (umbral por debajo de 0,60). Deja de ser halo y se vuelve niebla.
- **Halación sin teñir.** Un glow blanco se lee como plantilla de editor, no como película.
- **Grano parejo en los tres canales y sin `allf=t`.** Se ve como ruido digital estático, que es
  justo lo que quieres evitar.
- **Grano fuerte para redes sociales.** La plataforma lo recomprime y quedas con ruido y artefactos.
- **Grano antes de la LUT o antes del escalado.** Se amplifica y se deforma.
- **Vender una LUT como "emulación exacta de Kodak X".** No lo es y alguien lo va a notar.
- **Look sobre material sin corregir ni emparejar.** Hace la disparidad más evidente.
- **Gate weave con texto fijo en pantalla.** El texto tiembla y parece un error de render.

---

## Checklist

- [ ] La corrección y el emparejamiento están cerrados **antes** de empezar el look.
- [ ] Miré la forma de onda para saber en qué rango vive mi material antes de elegir la curva.
- [ ] La curva deja los medios (`0.5/0.5`) quietos para no mover la piel.
- [ ] El negro tiene piso (0,03–0,06) y el blanco techo (0,95–0,97).
- [ ] La halación aísla solo las altas (umbral 0,72–0,85) y está **teñida** de rojo-naranja.
- [ ] La opacidad de la halación está entre 0,20 y 0,40.
- [ ] El grano tiene valores distintos por canal y `allf=t+u`.
- [ ] El grano está entre 4 y 8, y va al **final** de la cadena.
- [ ] Compensé el costo de bitrate del grano bajando un punto el CRF.
- [ ] La cadena va en orden: curva → diafonía → saturación → halación → viñeta → grano → `limiter`.
- [ ] Verifiqué la piel después del look (`254`): el HUE sigue entre 130 y 145.
- [ ] Lo miré en un celular al 40 % de brillo, no solo en el monitor.
