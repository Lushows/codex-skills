# 74 · Flash, golpe y plano detalle

**Qué resuelve:** los tres recursos que dan sensación de comercial en un corte duro.
Duran entre 2 y 5 fotogramas, se construyen dentro de cada escena y no cuestan ni un
segundo de recodificación.

---

## Por qué estos tres no son "transiciones"

Un flash o un golpe de negro **no cruzan dos imágenes**: oscurecen o queman el final de
A y el principio de B por separado. Eso significa que se escriben en el propio comando
de cada escena (`motor.py`, al final de la cadena de filtros) y que **la unión sigue
siendo un corte duro**: `concat -c copy` intacto, cero riesgo de descuadre con la voz.

A 25 fps, **1 fotograma = 0,04 s**. Todo lo que sigue está en fotogramas porque a esta
escala la diferencia entre 2 y 5 es la diferencia entre un golpe y un parpadeo.

---

## 1. Flash de blanco

| Parte | Duración | Valor |
|---|---|---|
| Salida a blanco al final de A | **2 fotogramas (0,08 s)** | `#F4EEE0` |
| Entrada desde blanco al inicio de B | **3 fotogramas (0,12 s)** | `#F4EEE0` |
| Total del destello | **5 fotogramas (0,20 s)** | — |

El blanco **nunca es `#FFFFFF`**: se usa un blanco de papel `0xF4EEE0`, que es la misma
familia del `#E6DCC4` de la marca. El blanco puro es de vídeo digital y rompe la piel del
canal en el único fotograma en que el ojo mira fijo.

Al final de la cadena de la escena A (sustituye a `[{ultimo}]format=yuv420p[out]`):

```
[v7]fade=t=out:st=DURA-0.08:d=0.08:color=0xF4EEE0,format=yuv420p[out]
```

Y al principio de la escena B:

```
[v6]fade=t=in:st=0:d=0.12:color=0xF4EEE0,format=yuv420p[out]
```

**Cuándo se justifica:** cuando hay una razón en pantalla — una foto de archivo que se
toma, la prensa en la puerta del juzgado, un obturador. Se acompaña **siempre** de
`ob_obturador` en el fotograma del pico. Un flash sin motivo es un efecto de plantilla.

⚠️ Máximo **2 flashes por episodio** y nunca más de tres destellos por segundo (política
de contenido y accesibilidad).

---

## 2. Golpe de negro

| Parte | Duración | Valor |
|---|---|---|
| Salida a negro al final de A | **2 fotogramas (0,08 s)** | `#12100C` (la tinta de marca) |
| Negro pleno | **0 a 1 fotograma** | — |
| Entrada desde negro al inicio de B | **3 fotogramas (0,12 s)** | `#12100C` |

```
[v5]fade=t=out:st=DURA-0.08:d=0.08:color=0x12100C,format=yuv420p[out]
```

```
[v4]fade=t=in:st=0:d=0.12:color=0x12100C,format=yuv420p[out]
```

> **Regla dura: más de 6 fotogramas en negro y el espectador cree que el vídeo terminó
> o que falló la reproducción.** El negro largo es solo para el remate del episodio
> (0,80 s, `76`).

**Cuándo se justifica:** el dato duro. La cifra que cierra un tramo, la sentencia, el
"veintiséis años". El golpe de negro es un punto y aparte, y suena con `dr_golpe` en el
primer fotograma oscuro (no antes: aquí el sonido NO se adelanta, es el único caso).

---

## 3. Corte a plano detalle

No hay fundido de ningún tipo: se corta seco a una ampliación de **2,5× a 3,5×** de la
misma imagen que se estaba viendo, se aguanta **0,40-0,60 s** y se vuelve.

Se monta como una escena propia de 0,48 s en el guion visual:

```python
{"id": "det_firma", "ini": 78.60, "fin": 79.08, "fondo": "f_contrato",
 "mov": ("golpe", 0.05),
 "elementos": [{"r": "firma_recorte", "w": 1500, "x": 300, "y": 240,
                "dura": 0.48, "fade_out": 0}]},
```

El `mov: ("golpe", 0.05)` de `motor.py` da el arranque brusco que se frena en el 16% del
tiempo: es lo que hace que el plano detalle "aterrice" en lugar de aparecer.

**Cuándo se justifica:** cuando la voz nombra un objeto concreto que ya está en pantalla
—una firma, una cifra en un documento, unos ojos—. El detalle no se inventa: es un trozo
de lo que el espectador acaba de ver. Suena con `dr_impacto` a −8 dB bajo la voz.

---

## Tabla de decisión

| Lo que hace la voz | Recurso | Fotogramas |
|---|---|---|
| Nombra una foto, una detención, la prensa | Flash de blanco | 2 + 3 |
| Suelta la cifra o la condena | Golpe de negro | 2 + 3 |
| Señala un objeto ya visible | Plano detalle | corte seco + 12 |
| No hace nada de lo anterior | **corte duro pelado** (`70`) | 0 |

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Flash de 8-10 fotogramas | Deja de ser un golpe: se lee como un fundido a blanco mal hecho |
| Blanco `#FFFFFF` o negro `#000000` | Se sale de la paleta; el fotograma quemado delata que es un filtro |
| Flash sin `ob_obturador` | Efecto vacío: el oído no lo confirma y se ve barato |
| Encadenar flash + golpe + detalle en la misma unión | Parece un tráiler de acción, no un documental |
| Adelantar el `dr_golpe` del golpe de negro | El golpe suena antes de ver el negro y se percibe como error de sincronía |
| Plano detalle de una imagen que no estaba en pantalla | El espectador no lo reconoce y el corte se lee como error de continuidad |
| Usar el negro largo entre escenas | Caída de retención medible: parece el final del vídeo |

## Relacionado

`70` · `73` · `75` · `76` · `78` · `67`
