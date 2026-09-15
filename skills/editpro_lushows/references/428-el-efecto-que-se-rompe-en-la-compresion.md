# 428 — El efecto que se rompe en la compresión

Un efecto no existe en tu línea de tiempo. Existe en el archivo que la gente abre, después de que el
codificador de tu render y el de la plataforma hayan decidido, dos veces, qué información merece la
pena guardar.

Los codificadores modernos están construidos exactamente para tirar lo que el ojo no nota. Y resulta que
buena parte de lo que los editores llaman «textura» es, técnicamente, indistinguible de lo que un
codificador llama «ruido que no compensa codificar». Ese choque es este módulo.

---

## 1. El criterio del codificador

H.264 con CRF trabaja por transformada: divide cada bloque en frecuencias, cuantiza los coeficientes, y
los que caen bajo el paso de cuantización se van a cero. La consecuencia práctica:

| Lo que sobrevive | Lo que se va |
|---|---|
| cambios **grandes** de nivel | cambios **pequeños** de nivel |
| estructura **espacialmente grande** (viñeta, degradado amplio) | estructura **fina** (grano, ruido, trama) |
| eventos que duran **varios fotogramas** | eventos de **un fotograma** con poco movimiento |
| lo que se **repite** entre fotogramas | lo que cambia **aleatoriamente** cada fotograma |

Grano temporal —`noise=alls=N:allf=t`— es el peor caso posible de esa lista: pequeño, fino y distinto en
cada fotograma. Es lo que un codificador está diseñado para eliminar.

---

## 2. La medida: YDIF como termómetro de textura temporal

`YDIF` (`signalstats`) es la diferencia media de luminancia entre un fotograma y el anterior. Un grano
temporal la sube; un codificador que se lo lleva la baja otra vez. Es el instrumento exacto para esta
pregunta.

```bash
ydif () { ffmpeg -hide_banner -i "$1" \
  -vf "signalstats,metadata=print:key=lavfi.signalstats.YDIF" -f null - 2>&1 \
  | grep -o 'YDIF=[0-9.]*' | cut -d= -f2 | awk '{s+=$1;n++}END{printf "%.2f",s/n}'; }
```

> Sin `-loglevel error` y con `2>&1`. Ver `420`.

---

## 3. Medido: el grano no llega

Clip de 4 s a 1080p25. Tres versiones —limpia, grano fino (`alls=4`), grano grueso (`alls=12`)— pasadas
por cuatro etapas: mezzanine casi sin pérdida (CRF 5), master CRF 18, entrega CRF 24, y un reencode de
red (1080→720 a 2 Mbps con tope, que es aproximadamente lo que le hace una plataforma a tu archivo).

| Fuente | Etapa | YDIF | MB | Grano sobre el limpio |
|---|---|---|---|---|
| limpio | mezzanine | 2,45 | 18,11 | — |
| limpio | CRF 18 | 2,37 | 2,12 | — |
| limpio | CRF 24 | 2,24 | 0,84 | — |
| limpio | red 720p | 1,96 | 0,63 | — |
| **fino** `alls=4` | mezzanine | **2,94** | 67,01 | **+20%** |
| fino | CRF 18 | 2,51 | 3,22 | **+6%** |
| fino | CRF 24 | 2,26 | 0,93 | **+1%** |
| fino | red 720p | 1,97 | 0,67 | **+0,5%** |
| **grueso** `alls=12` | mezzanine | **4,94** | 118,19 | **+102%** |
| grueso | CRF 18 | 4,15 | 31,82 | **+75%** |
| grueso | CRF 24 | 2,42 | 1,60 | **+8%** |
| grueso | red 720p | 2,06 | 0,79 | **+5%** |

Tres conclusiones, y ninguna es opinable:

🔴 **1. El grano fino no llega a la audiencia.** De +20% en el mezzanine a **+0,5%** después del reencode
de red. Es indistinguible de cero. Si tu plan era «un grano finito para quitar el plástico», ese plan
falla en la entrega, no en el montaje.

🔴 **2. El CRF 24 es el acantilado.** El grano grueso conserva el 75% de su energía a CRF 18 y solo el
**8%** a CRF 24. Entre los dos hay un salto de seis puntos de CRF y el efecto desaparece. Éste es el
número que decide tu CRF de entrega cuando hay textura en juego.

🔴 **3. El grano se paga aunque no llegue.** El grano grueso multiplica por **15** el peso a CRF 18
(2,12 → 31,82 MB). En una entrega con tope de bitrate, ese peso no lo paga el grano: lo paga **todo lo
demás**. El codificador reparte un presupuesto fijo, el grano se lleva la mayor parte, y tu cara, tu
texto y tu producto salen con menos. Ésa es la razón real por la que un video con grano y bitrate
limitado se ve peor **en todo**, no solo en la textura.

---

## 4. Medido: el glitch de dos fotogramas sí llega

El otro extremo. Un glitch de 2 fotogramas (`rgbashift` fuerte + ruido puntual) aplicado en los
fotogramas 50 y 51, y medido como el **escalón de PSNR** entre un fotograma normal y el fotograma con
glitch, comparando siempre contra la versión limpia de la misma etapa:

| Etapa | PSNR fot. 49 (normal) | PSNR fot. 51 (glitch) | Escalón |
|---|---|---|---|
| mezzanine | 47,84 dB | 26,32 dB | **21,52 dB** |
| CRF 18 | 44,86 dB | 26,40 dB | **18,46 dB** |
| CRF 24 | 43,39 dB | 26,75 dB | **16,64 dB** |
| red 720p 2 Mbps | 43,55 dB | 29,14 dB | **14,41 dB** |

El glitch pierde un tercio de su contundencia y **sigue siendo un acontecimiento masivo**: 14,4 dB de
escalón después de todo el pipeline. Frente al grano, que se queda en +0,5%.

**Por qué la diferencia.** El glitch es un desplazamiento **grande** de bloques enteros de croma: es
exactamente la clase de información que el codificador está obligado a guardar, porque tirarla produciría
un error enorme. El grano es un error pequeño repartido por todas partes: tirarlo sale barato.

**La regla que sale de aquí:** *lo grande y breve sobrevive; lo pequeño y continuo, no.* Si tu efecto
necesita llegar, hazlo grande y corto. Si es fino, tiene que ser estructural —viñeta, degradado,
gradiente amplio— para que la compresión lo respete.

---

## 5. La tabla de supervivencia

| Efecto | Sobrevive a CRF 24 | Sobrevive al reencode de red | Qué hacer si no |
|---|---|---|---|
| grano fino (`alls≤4`) | ❌ | ❌ | subir a 8–12 y aceptar el peso, o quitarlo |
| grano medio (`alls=6`) | parcial | ❌ | subir, o reservarlo para YouTube largo |
| grano grueso (`alls≥12`) | ✅ 8% | ❌ 5% | es el techo: más ya se ve sucio |
| glitch de 2–3 fotogramas | ✅ | ✅ | — |
| destello (campana 0,12 s) | ✅ | ✅ | — |
| viñeta | ✅ | ✅ | — (además **ahorra** peso: −9%) |
| desenfoque | ✅ | ✅ | — (−73% de peso) |
| aberración cromática sutil | parcial | ❌ | subir el desplazamiento o quitarla |
| trama / halftone fina | ❌ | ❌ | engordar la trama hasta que el bloque la vea |
| `unsharp` | ✅ | parcial | los halos sobreviven; el detalle fino no |
| texto de 1 px de trazo | ❌ | ❌ | trazo mínimo de 3 px (`376`) |

---

## 6. El simulador de entrega

Todo lo anterior es inútil si no lo corres sobre **tu** material. El comando que hay que tener a mano:

```bash
#!/usr/bin/env bash
# entrega.sh — la pieza tal y como la va a recibir la audiencia
M="$1"      # tu master
# 1) lo que hace una red social: baja resolucion y fija el bitrate
ffmpeg -hide_banner -loglevel error -y -i "$M" -vf "scale=1280:-2:flags=bicubic" \
  -c:v libx264 -b:v 2000k -maxrate 2400k -bufsize 4000k -preset medium \
  -pix_fmt yuv420p -movflags +faststart red_720p.mp4
# 2) el caso peor: movil con conexion mala
ffmpeg -hide_banner -loglevel error -y -i "$M" -vf "scale=720:-2:flags=bicubic" \
  -c:v libx264 -b:v 900k -maxrate 1100k -bufsize 2000k -preset medium \
  -pix_fmt yuv420p movil_malo.mp4
# 3) cuanto de tu efecto queda
for f in "$M" red_720p.mp4 movil_malo.mp4; do
  printf "%-22s YDIF=%s\n" "$(basename $f)" \
    "$(ffmpeg -hide_banner -i "$f" -vf "signalstats,metadata=print:key=lavfi.signalstats.YDIF" \
       -f null - 2>&1 | grep -o 'YDIF=[0-9.]*' | cut -d= -f2 | awk '{s+=$1;n++}END{printf "%.2f",s/n}')"
done
```

Y la versión que se mira, no se mide: `red_720p.mp4` abierto en el móvil, a tamaño real. Si el efecto no
está ahí, no está.

---

## 7. Lo que sí se puede hacer

**a) Grano al final y solo al final.** El grano tiene que ir en el último filtro antes de `format=yuv420p`
del master. Si va antes de un escalado, el escalado lo promedia y desaparece (`426`).

**b) Subir el CRF de entrega en vez de subir el grano.** Bajar de CRF 24 a CRF 20 conserva más textura
que doblar `alls`, y cuesta menos peso que el grano grueso. Mide las dos rutas antes de decidir.

**c) Grano de grano grueso, no de grano fino.** Contraintuitivo pero medido: si el grano tiene que
sobrevivir, tiene que ser lo bastante grande para que el bloque de 8×8 lo vea. `alls=10–12` con
`allf=t+u`. Por encima se ve sucio.

**d) Aceptar que la textura es para el master.** En un canal de YouTube largo, donde la plataforma da
bitrate generoso, el grano llega. En un reel de Instagram no llega nunca. **La misma pieza puede llevar
grano en una entrega y no en la otra**, y eso no es una inconsistencia: es respetar el canal (`68`, `92`).

**e) Si el efecto es de marca, hazlo estructural.** Un grano no sobrevive; una viñeta sí, y un degradado
de color sí. Si la identidad necesita una textura que llegue, se traduce a estructura grande. Esa
traducción se decide con `directorcreativo_lushows`.

---

## Errores frecuentes

- **Juzgar la textura en el master.** El master tiene bitrate infinito. La audiencia no.
- **Subir el grano «para que se note» después de ver la entrega.** Antes mide si el problema es el grano
  o el CRF.
- **Poner grano antes de un escalado.** El escalado lo promedia y no queda nada.
- **Ignorar que el grano roba bitrate al resto.** ×15 de peso a CRF 18. Ese bitrate sale de la cara.
- **Usar `allf=u` (espacial, congelado) creyendo que es lo mismo.** El grano congelado se comprime
  aún mejor: el codificador lo codifica una vez y lo repite.
- **Medir la supervivencia con PSNR global.** Un grano cambia poco el PSNR. Se mide con `YDIF` y con el
  peso.
- **Comparar YDIF entre clips de escenas distintas.** Solo tiene sentido entre versiones del mismo
  material.
- **Aplicar el mismo master a todas las plataformas.** El grano que llega en YouTube no llega en Reels.
- **Meter texto de trazo fino y esperar que llegue.** Trazo mínimo de 3 px.
- **Creer que el glitch también se pierde.** Medido: conserva 14,4 dB de escalón después de todo.

---

## Checklist

- [ ] Rendericé la versión «reencode de red» y la miré en el móvil.
- [ ] Medí `YDIF` en master, en CRF de entrega y después del reencode.
- [ ] Sé qué porcentaje de mi textura llega a la audiencia.
- [ ] Comprobé cuánto peso extra cuesta el efecto y a costa de qué.
- [ ] El grano es el último filtro antes de `format=yuv420p`.
- [ ] Si el efecto tiene que llegar, es grande y breve, o estructural.
- [ ] Evalué subir el CRF de entrega como alternativa a subir la dosis.
- [ ] La entrega de cada plataforma tiene su propia decisión de textura.
- [ ] Los efectos que no sobreviven están retirados o justificados (`429`).

---

## Relacionado

- `420`, `421` — el arnés y las magnitudes
- `422` — el coste, que se paga aunque el efecto no llegue
- `426` — orden: por qué el grano va al final
- `429` — el disparador de retirada número dos es este módulo
- `440`, `446` — grano: dosis, temporal contra congelado, y ruido que sobrevive
- `93` — comprimir sin perder calidad
- `92`, `68` — especificaciones y color por plataforma
- `108` — `signalstats` y el resto del instrumental
- `376` — trazo mínimo y legibilidad real en móvil
