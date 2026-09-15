# 423 — El efecto que no se ve

Hay una categoría de efecto que no es discutible por gusto: el que **no cambia nada medible**. No es
sutil, no es de buen gusto, no es «trabaja por debajo del umbral consciente». Sencillamente no está
ahí, y aun así se ejecuta en cada fotograma de cada escena de cada episodio.

Es el residuo más común de una cadena que ha crecido. Nadie lo pone a propósito: queda de una prueba,
sobrevive a un ajuste que se hizo aguas arriba, o se copia de otra plantilla donde sí hacía falta.

---

## 1. Los cuatro grados

| Grado | Señal | Qué hacer |
|---|---|---|
| **Nulo** | `PSNR = inf` | borrar hoy |
| **Fantasma** | PSNR > 50 dB, SSIM > 0,9999 | borrar, salvo prueba en contra |
| **Subumbral** | PSNR 42–50 dB | verificar en el dispositivo real |
| **Real** | PSNR < 42 dB | se queda; mide su coste (`422`) |

Medido hoy, clip de 4 s a 1080p:

| Efecto | PSNR | SSIM | MB vs. nada | Grado |
|---|---|---|---|---|
| `null` | `inf` | 1,000000 | 0% | nulo |
| `eq=saturation=1.02` | **52,88** | **0,999988** | **0%** | **fantasma** |
| `noise=alls=2:allf=t+u` | 51,07 | 0,996817 | +1% | fantasma |
| `unsharp=5:5:0.2:5:5:0.0` | 47,95 | 0,997492 | +15% | subumbral |
| `hqdn3d=4:3:6:4` | 46,74 | 0,984886 | −15% | subumbral |
| `noise=alls=6:allf=t+u` | 43,08 | 0,964291 | +73% | real |
| `vignette=PI/12` | 35,95 | 0,996553 | −3% | real |
| `eq` completo del motor | 23,00 | 0,977511 | +4% | real |

La fila de `eq=saturation=1.02` es el caso puro: **0% de cambio en el peso codificado**. El
codificador —que es un detector de diferencias mucho más fino que el ojo— no encontró nada que
codificar. Si el codificador no lo ve, el espectador tampoco.

---

## 2. La detección: el barrido de la cadena

Este script coge una cadena de filtros y mide, filtro a filtro, cuánto aporta cada uno **en su sitio**
de la cadena. Es el barrido con el que se limpia una plantilla vieja:

```bash
#!/usr/bin/env bash
# aporte.sh — cuanto aporta cada eslabon de una cadena, en su sitio
IN=base.mp4
CADENA="eq=contrast=1.05:saturation=0.94:gamma=1.16:brightness=0.045|noise=alls=6:allf=t+u|vignette=PI/5.6"

IFS='|' read -ra F <<< "$CADENA"
n=${#F[@]}
for ((i=0; i<n; i++)); do
  completa=$(IFS=,; echo "${F[*]}")
  # la misma cadena SIN el eslabon i
  sin=()
  for ((j=0; j<n; j++)); do [ $j -ne $i ] && sin+=("${F[$j]}"); done
  parcial=$(IFS=,; echo "${sin[*]}")
  [ -z "$parcial" ] && parcial="null"
  P=$(ffmpeg -hide_banner -i "$IN" -filter_complex \
      "[0:v]split=2[a][b];[a]$completa[a2];[b]$parcial[b2];[a2][b2]psnr" \
      -f null - 2>&1 | grep -o 'average:[0-9.a-z]*' | head -1 | cut -d: -f2)
  printf "%-52s aporta PSNR %s\n" "${F[$i]}" "$P"
done
```

La lectura es directa: **el eslabón cuya ausencia da un PSNR alto no está aportando nada en esa
posición.** No es lo mismo que no aportar nada en absoluto —`425` y `426` tratan el caso del efecto que
otro eslabón ya está haciendo— pero para la decisión de borrar da igual: en esta cadena, sobra.

> Recordatorio: sin `-loglevel error`, con `2>&1`, y `split` explícito. Ver `420`.

---

## 3. Las cuatro causas del efecto fantasma

**a) La dosis quedó del experimento.** Se probó `saturation=1.25`, se vio exagerado, se bajó a 1,02
«para dejar un poquito» y ahí se quedó. El poquito no existe. **Si la dosis correcta es tan baja que no
se mide, la dosis correcta es cero.**

**b) Algo aguas arriba ya lo hace.** Una LUT que ya sube saturación deja sin trabajo al `eq` que viene
detrás. El barrido de la sección 2 lo caza.

**c) El efecto se aplica donde no hay sobre qué.** `unsharp` sobre un fondo desenfocado, `hqdn3d` sobre
material que ya venía limpio, `vignette` sobre un plano que ya tiene las esquinas oscuras. El filtro
corre y no encuentra nada.

**d) El efecto no llegó a ejecutarse.** Éste es distinto y peor: el filtro está en la cadena, el
comando no falla, y aun así no hace nada. Las tres formas habituales:

```bash
# 1) eq con expresiones y SIN eval=frame: se evalua una vez, al iniciar
eq=brightness='0.14*exp(-pow((t-2.0)/0.075\,2))'              # NO ocurre
eq=brightness='0.14*exp(-pow((t-2.0)/0.075\,2))':eval=frame   # SI ocurre

# 2) enable sobre un rango que cae fuera del clip
rgbashift=rh=-18:enable='between(n,300,301)'   # en un clip de 100 fotogramas: nada

# 3) overlay cuyo enable nunca es cierto porque t se conto sobre el original
overlay=...:enable='between(t,14.2,15.0)'      # tras un -ss, el reloj arranca en 0
```

El caso (1) está documentado dentro del propio `motor.py` del canal documental porque costó
encontrarlo: *«`eq` solo evalúa expresiones si se le pide `eval=frame`. Sin eso lee el valor una vez al
iniciar y el destello no ocurre.»* No hay aviso, no hay error, y la serie de `YAVG` sale plana.

**Cómo se distingue (d) de (a):** un efecto que no se ejecutó da `PSNR = inf` exacto. Un efecto de
dosis mínima da 50-y-pico. El `inf` es un bug; el 52,88 es una decisión mala.

---

## 4. El otro lado: el efecto que solo se ve en tu monitor

Hay un fantasma inverso, y es el que más discusiones cuesta: el efecto que **tú sí ves** porque lo
estás mirando al 100% en un monitor calibrado de 27 pulgadas, y que **nadie más va a ver** porque el
video se consume a 5 cm de ancho en un móvil con brillo automático a media tarde.

La prueba honesta cuesta un comando:

```bash
# La pieza tal y como la va a ver el 80% de la audiencia
ffmpeg -hide_banner -y -i entrega.mp4 \
  -vf "scale=506:-2:flags=bicubic,eq=brightness=-0.06:contrast=0.94" \
  -c:v libx264 -crf 26 -preset veryfast prueba_movil.mp4
```

506 px de ancho es aproximadamente lo que ocupa un reel en un móvil de gama media; el `eq` simula
brillo de pantalla bajo y el contraste que pierde un panel barato a plena luz. Lo que no se distingue
ahí, no existe para el negocio. Ver `376` para los milímetros reales sobre el vidrio.

**El matiz honesto.** Hay efectos que se defienden aunque no se vean uno a uno: un grano fino sostenido
durante nueve minutos cambia la sensación acumulada aunque ningún fotograma suyo pase el umbral.
Legítimo. Pero entonces **la hipótesis es otra** —«hace que el conjunto no se sienta plástico»— y se
prueba de otra manera: dos versiones del episodio completo, vistas con un día de separación (`472`).
Lo que no vale es defender un efecto medible-en-cero con una hipótesis que nunca se enuncia.

---

## 5. Qué se hace con un fantasma

```
PSNR = inf  ────────────► ¿esperabas que cambiara?
                            │ no → borrar
                            │ si → BUG: mira eval=frame, enable, y el reloj tras -ss
PSNR > 50 dB ───────────► ¿la dosis es minima por miedo?
                            │ si → o subes hasta que se mida, o lo quitas
                            │ no → ¿lo hace otro eslabon? -> barrido (seccion 2)
PSNR 42-50 dB ──────────► prueba en movil. Si ahi no se ve, fuera.
```

La regla de la casa: **subir hasta que se mida, luego bajar un escalón, y quedarse ahí.** Un efecto
que solo es defendible en su dosis invisible no es un efecto: es superstición con coste de CPU.

---

## 6. El coste de dejarlos

Un fantasma parece inofensivo. Sumados, no lo son:

- **CPU.** Cuatro fantasmas de +1,5 s por cada 100 fotogramas, en un episodio de 12 minutos (18.000
  fotogramas), son **18 minutos de render** por episodio, para siempre.
- **Depuración.** Cada eslabón inútil es un sospechoso más cuando algo sale mal. Una cadena de once
  filtros de los que cinco no hacen nada es una cadena de once filtros que revisar.
- **Falsa seguridad.** Lo peor: crees que tu material lleva grano, y no lo lleva. Cuando alguien
  comente que el video «se ve muy digital», vas a defender una textura que no existe.
- **Herencia.** Las plantillas se copian. Un fantasma en la plantilla del canal se reproduce en todos
  los formatos que salgan de ella.

---

## Errores frecuentes

- **Confundir «sutil» con «inexistente».** Sutil se mide y da 43 dB. Inexistente da 52 o `inf`.
- **Leer `PSNR = inf` como «todo bien».** Es el filtro que no tocó un solo píxel: o sobra, o es un bug.
- **No distinguir `inf` de 52 dB.** El primero es un fallo de ejecución; el segundo, una dosis absurda.
- **`eq` con expresiones sin `eval=frame`.** El efecto está escrito y no ocurre.
- **`enable` con tiempos del original después de un `-ss`.** El reloj del clip filtrado arranca en 0.
- **Bajar la dosis «para que no se note».** Si no se nota, no está. O sube, o quita.
- **Juzgar en el monitor grande.** La pieza se ve en un móvil, de día, a media luminosidad.
- **Quitar un fantasma y no volver a medir la cadena.** Al quitar un eslabón, los demás cambian de
  posición y su aporte puede cambiar (`426`).
- **Borrar sin registrar.** Sin nota, alguien lo vuelve a poner en tres meses.

---

## Checklist

- [ ] Medí PSNR y SSIM de cada efecto contra la versión sin él.
- [ ] Ningún eslabón de la cadena da `PSNR = inf`.
- [ ] Ningún eslabón da PSNR > 50 dB sin una hipótesis acumulativa escrita.
- [ ] Los efectos con expresiones llevan `eval=frame`.
- [ ] Los `enable` caen dentro del rango real del clip filtrado.
- [ ] Corrí el barrido eslabón a eslabón sobre la cadena completa.
- [ ] Los efectos de 42–50 dB los verifiqué en la versión móvil.
- [ ] Lo que quité quedó anotado, con su medida y la fecha.
- [ ] Volví a medir la cadena después de limpiarla.

---

## Relacionado

- `420` — el arnés y la escala de PSNR para efectos
- `421` — medir la magnitud concreta, no la genérica
- `422` — lo que cuesta dejarlos puestos
- `424` — el efecto que sí cambia algo, pero tapando un problema en vez de resolverlo
- `426` — orden de aplicación: por qué un eslabón cambia de aporte al moverse
- `429` — el protocolo de retirada
- `472` — la prueba A/B cuando la hipótesis es acumulativa
- `376` — legibilidad real en móvil, en milímetros
- `56` — la lista negra cualitativa
