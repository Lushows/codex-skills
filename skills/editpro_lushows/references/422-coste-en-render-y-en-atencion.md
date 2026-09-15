# 422 — Coste en render y coste en atención

Todo efecto se paga dos veces. Una en la máquina: segundos de CPU multiplicados por cada fotograma, por
cada escena, por cada episodio, para siempre. Otra en el espectador: cada cosa que se mueve en pantalla
gasta un poco de la atención que tenías reservada para la historia.

La primera se mide con un cronómetro. La segunda no tiene cronómetro, pero tiene reglas y tiene un
presupuesto. Este módulo es cómo se calculan las dos.

---

## PARTE 1 — El coste en render

## 1. La unidad correcta no es «segundos», es `utime`

Medido hoy sobre el mismo archivo y el mismo comando:

| Condición | `rtime` (reloj) | `utime` (CPU del proceso) |
|---|---|---|
| máquina en reposo | **4,49 s** | 2,61 s |
| máquina con otros renders | **44,20 s** | ≈ igual |

El reloj se multiplicó por diez sin que el comando cambiara. `ffmpeg -benchmark` da las tres cifras:

```bash
ffmpeg -hide_banner -benchmark -i base.mp4 -vf "vignette=PI/5.6" -f null - 2>&1 | grep '^bench'
# bench: utime=4.578s stime=0.094s rtime=4.712s
# bench: maxrss=125808KiB
```

Para **comparar efectos entre sí**, `utime`. Para **planificar una entrega** («¿llego a las seis?»),
`rtime` en la máquina real y sin nada más corriendo. `maxrss` es el tercero que importa cuando la
cadena crece: dice cuánta RAM pide, y es el que avisa antes de que el render muera (`428` de memoria en
`109`).

---

## 2. El coste de un efecto es la diferencia, no el total

Tabla medida hoy. Clip de 4 s a 1080p (100 fotogramas), ffmpeg 8.1.2, CRF 20, `preset veryfast`:

| Efecto | `utime` | coste propio | MB | vs. nada |
|---|---|---|---|---|
| **nada** (línea base) | **2,86 s** | — | 1,17 | — |
| `eq=saturation=1.02` | 2,91 | +0,05 | 1,17 | 0% |
| `noise=alls=6:allf=t+u` | 2,83 | **≈ 0** | 2,02 | **+73%** |
| `noise=alls=2:allf=t+u` | 3,13 | +0,27 | 1,18 | +1% |
| `eq` completo del motor | 3,13 | +0,27 | 1,22 | +4% |
| `hqdn3d=4:3:6:4` | 4,30 | +1,44 | 1,00 | −15% |
| `vignette=PI/12` | 4,56 | +1,70 | 1,13 | −3% |
| `vignette=PI/5.6` | 4,58 | +1,72 | 1,06 | −9% |
| `unsharp=5:5:0.2` | 7,19 | +4,33 | 1,34 | +15% |
| `unsharp=5:5:0.8` | 7,45 | **+4,59** | 2,06 | **+76%** |
| `gblur=sigma=20` | 7,59 | **+4,73** | 0,32 | **−73%** |
| cadena real (`eq`+`noise`+`vignette`) | 5,39 | +2,53 | 1,76 | +50% |

Lo que se aprende leyendo la columna «coste propio»:

- **Más de la mitad del `utime` total es descodificar.** Si informas «el grano cuesta 2,83 s» estás
  informando el coste de abrir el archivo. El grano cuesta **cero**.
- **El orden de magnitud entre efectos es de 100 a 1.** `noise` es gratis; `unsharp` y `gblur` cuestan
  casi el doble de todo el resto del proceso. Son convoluciones de 5×5 sobre cada píxel de cada
  fotograma; el resto son tablas de consulta.
- **La cadena de tres cuesta 2,53 s y la suma de sus partes 1,96 s.** No es aditiva: cada filtro
  intermedio obliga a una conversión de formato y a una copia más de búfer. Detalle en `426`.

**Cómo se extrapola.** El clip son 100 fotogramas. Un episodio de 12 minutos a 25 fps son 18.000:
`+4,59 s × 180 = 13 min 47 s` **solo de `unsharp`**, en un render que ya duraba. Ésa es la cifra con
la que se decide, no el «cuatro segundos y medio».

---

## 3. El caso real: el escalado que no hacía nada

> **Frontera.** `458` desmenuza este mismo caso desde el lado del **movimiento sobre imagen fija** (el
> reparto por capa, el remuestreador, el caso del `zoompan`), y `408` pone precio a cada capa de un
> apilado. Aquí está lo que el caso enseña sobre **cualquier efecto**: cómo se atribuye un coste y por
> qué el filtro culpable casi nunca es el caro.

El canal documental (`canales_lushows`) monta cada escena como un `zoompan` sobre un fondo de archivo
más una pila de recortes en PNG. Los fondos se generan a **4320×2430**. La cadena llevaba:

```bash
-vf "scale=4320:-2,zoompan=z='...':d=1:x='...':y='...':s=1920x1080:fps=25,format=yuv420p"
```

Ese `scale=4320:-2` era un no-operativo: la fuente ya venía a 4320. Medido hoy, escena de 6,73 s
(168 fotogramas), con `-f null -` para aislar el filtro del codificador:

| Cadena | `utime` | `rtime` | RAM pico |
|---|---|---|---|
| A — entrada 4320 **con** `scale=4320:-2` | 58,22 s | 14,01 s | 618 MB |
| A2 — entrada 4320 **sin** el `scale` | 58,42 s | 13,95 s | 600 MB |
| B — entrada **pre-reducida a 2688** | **24,06 s** | **5,53 s** | **268 MB** |

🔴 **Aquí está la lección, y no es la que uno espera.** Quitar el `scale` no ahorró nada: A y A2 son
el mismo número. El filtro inútil no costaba porque `swscale` hace pasarela cuando la entrada y la
salida coinciden. **Lo que costaba era el tamaño que ese `scale` legitimaba**: mientras estuviera ahí,
nadie cuestionaba que el fondo entrara a 4320×2430 en cada fotograma, y `zoompan` trabajaba sobre 10,5
megapíxeles para escupir 2,07.

Reducir el PNG **una sola vez, fuera del bucle**, a 2688 px —1920 × 1,4, margen para la deriva y la
rotación— baja el render de la escena a **2,4× más rápido** y la RAM a menos de la mitad. En el
pipeline completo, con overlays y codificación, el mismo cambio llevó la escena de **33,5 s a 22,6 s**,
y ese PNG reducido se cachea y se reutiliza en todas las escenas que lo usen.

**Lo que no se perdió.** Comparando la salida de A contra la de B sobre el episodio real del canal:
**PSNR 43,3 dB y SSIM 0,972** — indistinguible. En mi reproducción aislada, reduciendo con
`scale=2688:-2:flags=lanczos` de ffmpeg en vez de con PIL, salió **32,58 dB / SSIM 0,941**: sigue
siendo un cambio que nadie ve en movimiento, pero **el remuestreador importa y la diferencia entre los
dos números es él**. Y ojo con la justificación fácil: «bajar en dos pasos suaviza mejor» suena
razonable y está **medido como falso** en `458` (Lanczos en un paso, 56,27 dB; en dos, 40,98 dB). El
pre-escalado se defiende por el tiempo y la RAM, no por la calidad.

**La regla que sale de esto:** *cualquier trabajo que no dependa de `t` ni de `n` no pertenece a la
cadena de filtros.* Escalar un PNG, rotar un logo, aplicar una LUT a un fondo fijo: todo eso se hace
una vez, se guarda en disco y se cachea. La cadena de filtros es para lo que cambia en cada fotograma.

```python
# el patron, tal cual esta en motor.py
_ESCALADOS = {}
def escalado(ruta, ancho):
    clave = (ruta, ancho)
    if clave in _ESCALADOS: return _ESCALADOS[clave]
    ...  # reduce con PIL LANCZOS a int(ancho*1.4) y guarda en salida/_escalados/
    _ESCALADOS[clave] = destino
    return destino
```

---

## 4. Cuándo el codificador es el suelo

Una vez que el filtro deja de ser el cuello de botella, aparece el siguiente. En la escena de arriba,
el render **con** codificación a CRF 12 `ultrafast` tardó 13,8 s en A y 13,9 s en B: idéntico, aunque
el filtro de B tarda un tercio. Los 8 s que le faltan a B se los come libx264.

Traducido: **optimizar el filtro por debajo del coste del codificador no sirve para nada.** El orden
de ataque es siempre:

1. Mide `utime` del grafo con `-f null -` (sin codificar).
2. Mide `utime` del render completo.
3. La diferencia es el codificador. Si el codificador es el 70%, toca el `preset`, no el filtro.

Y el `preset` es la palanca más barata que existe: entre `ultrafast` y `slow` hay un factor de 5 en
tiempo, con el mismo CRF. Los renders intermedios del canal van a `-crf 12 -preset ultrafast` —pesan
mucho y no importa, se borran— y solo el master final va a `-crf 18 -preset slow`.

**El número de referencia del canal:** un episodio de **63,45 s** a 1080p25, con escenas de fondo con
movimiento, entre 3 y 14 recortes superpuestos por escena, destellos y la cadena de acabado completa,
tarda **9 min 42 s** de reloj en la máquina de trabajo. Son **9,2 s de render por segundo de video**.
Con esa cifra se planifica: un episodio de 12 minutos son unas 110 min de render, y eso decide si la
prueba de un efecto nuevo se hace sobre el episodio entero o sobre una escena.

---

## PARTE 2 — El coste en atención

## 5. El presupuesto

La atención del espectador no es infinita y no se recupera. Cada elemento que se mueve, aparece,
destella o cambia de color consume una parte de ella. El marco del canal, y el que `470` desarrolla:

| Tipo de pieza | Eventos visuales por minuto que aguanta |
|---|---|
| Documental narrado | 25–40 (uno cada 1,5–2,5 s) |
| Reel de venta | 40–70 |
| Talking head de marca | 10–20 |
| Video corporativo | 8–15 |

Un «evento» es cualquier cosa que reclama la mirada: un recorte que entra, un destello, un texto, un
corte. La cuenta no distingue de qué tipo es: **compiten por el mismo recurso**.

**La consecuencia operativa es incómoda:** si metes un efecto nuevo, algo tiene que salir. Un destello
añadido en el segundo 14 no es gratis porque «solo dura 0,12 s»: es gratis en CPU y caro en el
presupuesto, porque llega justo cuando el espectador estaba leyendo una cifra.

---

## 6. Los tres efectos que cuestan atención y no lo parecen

**a) El efecto continuo.** Un grano temporal cuesta atención cero —es una superficie, no un evento—.
Un desenfoque que respira, un color que pulsa o un temblor permanente cuestan mucho: el ojo los
re-evalúa constantemente porque no consigue predecirlos. Regla: **si el efecto cambia con `t`, cuesta
atención; si es estático, cuesta CPU.**

**b) El efecto que llega solo.** Un destello sin sonido obliga al espectador a decidir si era
intencionado (`433`). Esa decisión es atención gastada en el montaje en vez de en la historia. Un
destello con su golpe de audio se procesa como un evento único y no cuesta la mitad.

**c) El efecto en el sitio donde estaba leyendo.** Un movimiento en la zona del texto mientras el texto
todavía se está leyendo cuesta el doble: el ojo salta, vuelve y relee. Por eso `374` separa en el
tiempo el corte y la entrada del texto. Un efecto en una esquina vacía es casi gratis.

---

## 7. La contabilidad conjunta

El cuadro con el que se decide, y que junta las dos monedas:

| | Barato en CPU | Caro en CPU |
|---|---|---|
| **Barato en atención** | `eq`, `noise`, LUT, viñeta suave → **úsalos sin miedo** | `unsharp`, `gblur`, denoise → **hazlos una vez, fuera del bucle** |
| **Caro en atención** | destellos, entradas, `eval=frame` → **presupuéstalos** (`439`, `470`) | desenfoque animado, glitch continuo, partículas → **casi siempre la decisión es no** |

La casilla más peligrosa es la de arriba a la derecha: efectos caros de calcular y baratos de mirar. Es
donde vive el error del canal —el escalado que no hacía nada— y es la que se arregla con ingeniería, no
con criterio estético. La casilla de abajo a la izquierda es la que se arregla con criterio.

---

## Errores frecuentes

- **Informar el `utime` total como coste del efecto.** Más de la mitad es descodificar. El coste es la
  diferencia contra la fila `nada`.
- **Medir con `rtime` y la máquina ocupada.** Medido: 4,49 s contra 44,20 s por el mismo trabajo.
- **Optimizar el filtro cuando el codificador es el 70% del tiempo.** Toca el `preset` primero.
- **Escalar dentro de la cadena algo que no cambia con el tiempo.** Se hace una vez y se cachea.
- **Creer que el filtro inútil es el que costaba.** Medido: quitarlo no ahorró nada. Lo que costaba era
  el tamaño de cuadro que mantenía vivo.
- **Extrapolar de un clip de 4 s sin multiplicar.** Cuatro segundos y medio por 180 son catorce
  minutos.
- **Ignorar `maxrss`.** Una cadena con doce overlays a 4320 px se lleva la RAM por delante antes que el
  tiempo.
- **Contar el presupuesto de atención por efecto.** Se cuenta por **evento visual**: los cortes, los
  textos y los efectos salen del mismo bolsillo.
- **Justificar un efecto porque «es gratis».** Gratis en CPU no es gratis en atención, y al revés.
- **Renderizar el episodio entero para probar un efecto.** 9,2 s de render por segundo de video. Prueba
  sobre una escena.

---

## Checklist

- [ ] Medí con `-benchmark` y comparo `utime`, no el reloj.
- [ ] La tabla tiene fila `nada` y hablo de coste **propio**, no total.
- [ ] Extrapolé el coste al metraje real del entregable.
- [ ] Comprobé si el cuello de botella es el filtro o el codificador (`-f null -` contra render).
- [ ] Todo lo que no depende de `t` ni de `n` está fuera de la cadena y cacheado.
- [ ] Las entradas entran a la cadena al tamaño que se van a usar, no al que vienen.
- [ ] Miré `maxrss` antes de escalar la cadena a un episodio largo.
- [ ] Conté los eventos visuales por minuto y estoy dentro del presupuesto del formato.
- [ ] El efecto nuevo entró sacando otra cosa, no sumándose.
- [ ] Los efectos con `t` variable tienen su evento de audio (`433`).

---

## Relacionado

- `420`, `421` — el arnés de medición y las magnitudes por familia
- `423` — el efecto que no se ve: el coste sin contrapartida
- `426` — orden de aplicación: por qué la cadena no es aditiva
- `428` — lo que la compresión se lleva
- `470`, `471` — presupuesto de efectos por minuto y dónde pagan
- `132`, `134` — render reproducible y procesar por lotes
- `109` — trampas de ffmpeg, incluidas las de memoria
- `canales_lushows` — el motor de montaje del que salen estas cifras
- `engineer_visualopen_lushows` — si el cuello de botella pide GPU o auto-hospedaje, es esa skill
