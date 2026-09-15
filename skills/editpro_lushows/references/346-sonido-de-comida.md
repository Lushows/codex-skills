# 346 — Sonido de comida

**Qué resuelve:** el recurso más subestimado del contenido de restaurante. El chisporroteo, el crujido,
el destape de la botella, el hielo cayendo, el cuchillo rompiendo la costra. **Vale más que cualquier
canción de moda**, es gratis y está pasando en tu bar todo el día.

**La tesis:** *la música le dice al espectador cómo debe sentirse; el sonido de la comida lo pone dentro
del local.* Solo uno de los dos produce hambre.

---

## 1. Por qué el sonido de comida funciona (no es moda, es reflejo)

Hay un motivo por el que el crujido es el sonido más usado en publicidad de comida desde hace décadas:
**es la única prueba acústica de frescura**. Un pan crujiente suena distinto a un pan de ayer, y tu
cerebro lo aprendió antes de saber hablar. Es información que ninguna imagen puede dar. Lo mismo con:

| Sonido | Qué prueba | Dónde vive en tu bar |
|---|---|---|
| **Chisporroteo** | Que está caliente **ahora** | Plancha, sartén, freidora |
| **Crujido** | Que está fresco / recién hecho | Papas, chicharrón, empanada, pan |
| **Destape de chapa** | Que la cerveza está sellada y con gas | Barra |
| **Hielo cayendo al vaso** | Que está frío | Barra |
| **Chorro y espuma** | Que se está sirviendo ahora | Grifo, botella |
| **Cuchillo rompiendo la costra** | Que hay costra | Corte de carne, pan, empanada |
| **Murmullo del local** | Que hay gente, que el sitio vive | Cualquier noche |

El último es el más ignorado y de los más potentes: **el murmullo del bar lleno** debajo de todo el
reel comunica en un segundo lo que ningún texto comunica.

---

## 2. El problema del celular: te está borrando el sonido que quieres

Esto hay que saberlo porque cambia cómo grabas.

Los celulares modernos tienen dos o tres micrófonos y aplican **supresión de ruido y reducción de viento
en tiempo real**. Ese sistema está diseñado para una llamada: quiere aislar la **voz** y borrar todo lo
demás. El chisporroteo de un sartén y el murmullo de un bar son, para ese algoritmo, exactamente "todo
lo demás".

**Consecuencias prácticas:** (1) el sonido de comida grabado de lejos casi siempre llega **destruido** —
no bajito: procesado y sin brillo, se oye "ahogado"; (2) **la única defensa es la distancia**, porque si
la fuente es lo más fuerte que el micrófono oye, el algoritmo la respeta; (3) **grabar sonido y grabar
imagen son dos tareas distintas** y no siempre caben en la misma toma.

---

## 3. La técnica que resuelve el 90%: grabar el sonido aparte

Se llama **sonido salvaje** (wild sound): grabar el sonido solo, sin importar la imagen, muy cerca, y
después ponerlo bajo el plano en la edición. **Cómo se hace, en tu bar, hoy:**

```
1. Grabas el plano bonito como toca (luz, angulo, distancia, camara lenta).
   Ese plano probablemente tenga sonido inservible. No importa.

2. Repites la accion SOLO PARA EL SONIDO:
   - Celular a 15-25 cm de la fuente (no mas).
   - Apuntando el microfono, no la camara.
   - Silencio en el local: apaga nevera si ruge, musica, TV, extractor.
   - Grabas 15 segundos aunque la accion dure 1.
   - Repites la accion 4 o 5 veces seguidas en la misma grabacion.

3. En la edicion eliges la mejor de las 5 y la pones bajo el plano.
```

**Dónde está el micrófono de tu celular:** abajo (junto al conector) y arriba, cerca de la cámara
trasera; grabando video pesa más el de arriba. Prueba concreta: graba 10 segundos hablando bajito y
tapando con el dedo cada agujero, y escucha cuál mató el sonido. Ese es el que apuntas y **nunca tapas**.

**`[SI CRECES]`** un micrófono de solapa por cable ($40.000–$120.000 COP) o inalámbrico ($250.000+)
mejora muchísimo **la voz**. Para sonido de comida el salto es menor, porque lo que gana la partida es
la proximidad y esa ya la tienes gratis. Primero domina el sonido salvaje.

---

## 4. Distancias y niveles concretos

| Sonido | Distancia del micrófono | Cuidado |
|---|---|---|
| Chisporroteo de sartén | 25–40 cm | **Aceite.** No acerques más el celular |
| Freidora | 40–60 cm | Ruido de motor de fondo, más el aceite |
| Crujido (morder, partir) | 10–20 cm | Muy fuerte: aléjate si satura |
| Destape de chapa | 15–25 cm | Sale bien casi siempre |
| Hielo al vaso | 15–20 cm | Graba 5 veces: una sale perfecta |
| Vertido de cerveza | 20–30 cm | El chorro y la espuma tienen sonidos distintos |
| Cuchillo cortando costra | 15–25 cm | Cuchillo con filo o suena a aplastar |
| Murmullo del local | 1,5–3 m, en medio del salón | 60 segundos limpios, sin hablar |

**La regla de saturación:** si la barra de nivel toca el tope o los picos se oyen "rotos", **aléjate
10 cm**. Un sonido saturado no se arregla nunca; mejor grabar bajito y subirlo después.

---

## 5. Limpieza y refuerzo con ffmpeg (verificado)

Cadena base para un sonido de comida grabado con celular:

```bash
ffmpeg -i sonido_crudo.m4a -af "
highpass=f=80,
afftdn=nr=12:nf=-25,
acompressor=threshold=-20dB:ratio=3:attack=5:release=120:makeup=3,
alimiter=limit=0.95
" -c:a aac -b:a 192k sonido_limpio.m4a
```

Qué hace cada eslabón:

- **`highpass=f=80`** — corta por debajo de 80 Hz. Ahí no hay sonido de comida: hay retumbe de mesa,
  motor de nevera y golpes del celular.
- **`afftdn=nr=12:nf=-25`** — reducción de ruido; `nr` es cuánto reduce en dB. **No te pases de 15:** por
  encima el chisporroteo suena metálico y con burbujeo digital. Es preferible dejar algo de ruido que
  destruir el brillo.
- **`acompressor`** — nivela: baja picos y sube lo bajito. Es lo que hace que un crujido "suene grande"
  en un celular a medio volumen.
- **`alimiter=limit=0.95`** — techo de seguridad para que nada sature al exportar.

**Medir el resultado** (`108`, `73`): `ffmpeg -i sonido_limpio.m4a -af ebur128=peak=true -f null -`
devuelve la sonoridad integrada (LUFS) y el pico real. Lo que importa **no es acertarle a un número
mágico de plataforma** —eso cambia y no siempre está documentado públicamente— sino que el **pico real
no pase de −1 dBFS** y que el sonido de comida quede **por encima de la música** (sección 7).

**Reforzar un chisporroteo apagado:**

```bash
ffmpeg -i chisporroteo.m4a -af "highpass=f=120,equalizer=f=5000:t=q:w=1.2:g=4,alimiter=limit=0.95" -c:a aac reforzado.m4a
```

El brillo del chisporroteo y del crujido vive entre **3 kHz y 8 kHz**. Subir ahí 3–5 dB los revive; más
de 6 dB suena a estática.

---

## 6. Sonido real vs. efecto descargado

Se puede usar un banco de efectos y a veces es la salida (`77`, `76`). Pero **el sonido real de tu
cocina suena a tu cocina**, mientras que los efectos de banco suenan a todos los videos que usan ese
mismo banco, y la gente ya los reconoce. El **destape, el hielo y el crujido** salen perfectos con
celular: no hay razón para descargarlos. El **chisporroteo y el ambiente de local** sí son difíciles;
ahí un efecto puede complementar, puesto **debajo** del real, nunca en su lugar. Y ojo con los
derechos: los bancos gratuitos suelen exigir atribución o prohibir uso comercial (`78`).

---

## 7. Cómo se mezcla: el sonido de comida por encima de la música

Este es el error de mezcla que hace que todo el trabajo anterior no sirva de nada.

```
CAPA 1 — sonido de comida (chisporroteo, crujido, vertido)   <- MANDA
CAPA 2 — ambiente del local (murmullo, continuo, bajito)     <- pega todo
CAPA 3 — musica                                              <- OBEDECE
CAPA 4 — voz, si hay                                         <- manda sobre todo
```

**La regla:** cuando entra un sonido de comida, **la música baja**. Es el mismo ducking de la voz
(`75`), aplicado a otra cosa:

```bash
ffmpeg -i musica.m4a -i comida.m4a -filter_complex "
[0:a][1:a]sidechaincompress=threshold=0.05:ratio=6:attack=15:release=250[m];
[m][1:a]amix=inputs=2:duration=longest:weights=1 1.4[out]
" -map "[out]" -c:a aac mezcla.m4a
```

El `weights=1 1.4` deja el sonido de comida por encima de la música a propósito.

**El truco de montaje que multiplica el efecto:** el sonido entra **2 o 3 fotogramas ANTES** del corte a
la imagen. Oyes el "tsss" y un instante después ves el sartén. El cerebro lo lee como que la escena ya
estaba pasando, y el corte se siente inevitable en vez de brusco. Es un corte en J y está en `24`.

---

## 8. El caso especial: la cámara lenta

Todo plano lento queda mudo o con audio inservible (`344`). No es un problema: es la oportunidad.

> **Imagen en cámara lenta + sonido a velocidad normal.**

El chorro de cerveza cayendo lento con el sonido real encima produce esa sensación de "tiempo
suspendido" que buscas. Ponerle el sonido ralentizado (grave y arrastrado) suena a broma.

---

## 9. Enemigos del sonido en un bar real

- **La nevera / el congelador.** Ruge en graves. `highpass=f=80` ayuda, pero si puedes desconectarla 3
  minutos, hazlo (y acuérdate de volver a conectarla).
- **El extractor de la cocina.** El peor: ruido de banda ancha, no se quita. Apágalo.
- **El televisor y la música del local.** Quedan en tu grabación y además pueden meterte música con
  derechos en el video (`78`). Apágalos.
- **El viento en la terraza.** No se arregla en post: es distorsión, no ruido. Afuera, **tapa el
  micrófono con una media de tela o una espuma**, o grábalo adentro.
- **Tu propia mano.** Los golpecitos de los dedos se transmiten por el cuerpo del aparato directo al
  micrófono. Trípode o apoyo.
- **Tu voz.** No comentes mientras grabas: ni un "listo", ni un "ay". Deja 2 segundos de silencio al
  principio y al final.

---

## 10. El banco de sonidos propios (esto vale oro con el tiempo)

En **una sola tarde** grabas el banco de sonidos de tu bar y lo usas el resto del año:

```
/sonidos-bendita-pola/
    destape-chapa-01..05.m4a          crujido-chicharron-01..03.m4a
    hielo-vaso-01..05.m4a             chisporroteo-plancha-01..03.m4a
    servir-cerveza-grifo-01..03.m4a   cuchillo-corte-01..03.m4a
    crujido-papas-01..05.m4a          ambiente-local-lleno-01.m4a  (60 s)
                                      ambiente-local-vacio-01.m4a  (60 s)
```

Tiempo real: **90 minutos**. Después, cada reel tiene sonido bueno sin volver a grabar nada. Es la
inversión de tiempo con mejor retorno de todo el bloque (`316`, `317`).

---

## Errores comunes

1. **Poner solo música y borrar el sonido real.** Es el error #1 del contenido de restaurante. La música
   no da hambre; el crujido sí.
2. **Grabar el sonido de comida desde la misma distancia que la imagen.** El plano bonito está a 40 cm y
   el sonido necesita 15. Son dos tomas.
3. **No saber que el celular tiene supresión de ruido activa** y creer que el chisporroteo "no se
   escuchó" por mala suerte.
4. **Tapar el micrófono con la mano** al sostener el celular.
5. **Grabar con la nevera, el extractor, el TV o la música del local prendidos.**
6. **Grabar sonido en la terraza con viento sin protección.** Es irrecuperable.
7. **Saturar.** Un pico roto no se arregla. Aléjate 10 cm.
8. **Pasarse con `afftdn`** (`nr` por encima de 15). El chisporroteo queda metálico y con burbujeo.
9. **Ralentizar el sonido junto con la imagen** en cámara lenta. Suena ridículo.
10. **Dejar la música por encima del sonido de comida** en la mezcla, o **meter el sonido exactamente en
    el corte** en vez de 2–3 fotogramas antes.
11. **Hablar mientras grabas sonido salvaje.**
12. **Usar efectos descargados sin revisar la licencia** (`78`).
13. **Grabar una sola vez cada sonido.** Se graban 5 seguidos y se elige el mejor; cuesta lo mismo.

---

## Checklist

- [ ] El reel tiene **sonido real de comida**, no solo música.
- [ ] El sonido se grabó **aparte y de cerca** (10–40 cm según la fuente).
- [ ] Se sabe **dónde está el micrófono** del celular y no está tapado.
- [ ] Nevera, extractor, TV y música del local **apagados** durante la toma de sonido.
- [ ] Cada sonido se grabó **4 o 5 veces seguidas** en la misma toma.
- [ ] Hay **2 segundos de silencio** al principio y al final de cada grabación.
- [ ] No hay **saturación** (picos rotos) en el material crudo.
- [ ] Se aplicó `highpass=f=80` para quitar retumbe y motores.
- [ ] `afftdn` con `nr` **≤ 15**.
- [ ] Se midió con `ebur128` y el **pico real no pasa de −1 dBFS**.
- [ ] Hay una capa de **ambiente del local** bajo todo el reel.
- [ ] La **música baja** cuando entra el sonido de comida (ducking, `75`).
- [ ] Los sonidos entran **2–3 fotogramas antes** del corte de imagen (`24`).
- [ ] Los planos en **cámara lenta** llevan sonido a **velocidad normal**.
- [ ] Si se usaron efectos descargados, se **revisó la licencia** (`78`).
- [ ] Existe (o se está construyendo) el **banco de sonidos propios** del bar.
