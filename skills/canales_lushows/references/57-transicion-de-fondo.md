# 57 · Transición de fondo

**Qué resuelve:** el cambio de escena. Seis fondos distintos pegados uno detrás de otro dan
seis chispazos de color. Aquí está cómo se pasa de uno a otro sin que el ojo lo viva como
un golpe.

---

## Lo que se transita no es la imagen, es el color y la luz

Un corte entre dos fondos se lee brusco por tres causas, y solo una se arregla con una
transición de vídeo:

| Causa | Arreglo | Dónde |
|---|---|---|
| Salto de luminosidad | Igualar el nivel de la zona por la que se corta | En el CSS |
| Salto de temperatura | Anclaje de color compartido | En el CSS |
| Salto de composición | Elemento puente | En el montaje |

**El 80% del trabajo se hace al diseñar los fondos, no al montarlos.**

## 1 · El anclaje de color

Cada par de escenas consecutivas comparte **un color exacto**. No parecido: el mismo hex.
Normalmente es el tono de la parada final del degradado —la esquina oscura— o el color del
punto de luz.

| Corte | Anclaje | Hex |
|---|---|---|
| Gancho → Pregunta | La caída oscura | `#080D12` ≈ `#080D0B` |
| Pregunta → Peso | El punto de luz | `#FFE8B4` aparece ya insinuado en el azul |
| Peso → Máquina | La caída oscura | `#14110C` → `#101413` |
| Máquina → Piezas | La luz fría | `#D6F0FF` / `#6E9CD4` |
| Piezas → Remate | La rejilla | Ambos llevan trama de 96-118 px |

Cómo se hace en la práctica: al fondo saliente se le añade **una insinuación** del color
del entrante, en una esquina y muy baja:

```html
<!-- en f_pregunta (azul), un rescoldo ocre abajo a la derecha, que anuncia f_peso -->
<div class="l" style="right:-8%;bottom:-10%;width:46%;height:44%;filter:blur(70px);
  opacity:.16;background:radial-gradient(60% 60% at 80% 90%,rgba(255,232,180,.9),transparent 72%)"></div>
```

Al `.16` nadie lo identifica como ocre, pero al cortar a la escena ocre el ojo ya lo tenía
visto y el cambio se siente preparado.

## 2 · Continuidad de luz

El punto de luz **no salta de lado en cada corte**. Se mueve como se movería una cámara
que rodea un espacio: unos grados por escena.

```
Escena 1  luz at 50%  0%   (cenital)
Escena 2  luz at 62% 12%   (se desplaza a la derecha)
Escena 3  luz at 74% 22%   (sigue)
Escena 4  luz at 50% -6%   ← corte de acto: aquí SÍ se permite el salto
Escena 5  luz at 36%  8%
Escena 6  luz at 24% 16%
```

El salto se reserva para el cambio de acto. Cuando la luz salta, el espectador lo lee como
"cambiamos de tema" — así que hay que gastarlo donde el guion lo diga.

## 3 · El elemento puente

Un recorte que **sobrevive al corte**: sale en los últimos 0,6 s de la escena A y sigue
en los primeros 0,6 s de la B, en la misma posición y tamaño. El fondo cambia debajo de él.

```python
# en la tabla del guion visual, el mismo recurso a caballo de las dos escenas
{"r": "retrato_a", "x": 1180, "y": 300, "w": 520, "desde": 5.4, "dura": 1.0},   # escena A
{"r": "retrato_a", "x": 1180, "y": 300, "w": 520, "desde": 0.0, "dura": 0.9,
 "entrada": "ninguna"},                                                          # escena B
```

`entrada:"ninguna"` es imprescindible: si el puente vuelve a entrar con fundido, deja de
ser puente y se convierte en un elemento repetido.

## 4 · La transición de vídeo (cuando toca)

El 90% de los cortes van duros (`70`). Cuando no:

| Recurso | Comando | Cuándo |
|---|---|---|
| Fundido corto | `xfade=transition=fade:duration=0.25:offset=T` | Paso de tiempo |
| Fundido a negro | `fade=out:st=T:d=0.3` + `fade=in` | Cambio de acto |
| Barrido de papel | Recorte que cruza y arrastra (`73`) | Cambio de tema |
| Destello | `xfade=transition=fadewhite:duration=0.18` | Golpe, revelación |

`duration` por encima de 0,35 s en un canal de este ritmo se siente como que el vídeo se
quedó pensando. Entre 0,18 y 0,28.

## 5 · La escena bisagra

Cuando dos escenas contiguas son inevitablemente muy distintas —de un plano técnico azul a
un almacén ocre— se fabrica un fondo intermedio que lleva **las dos paletas**: base del
entrante y textura del saliente.

```html
<div class="esc" style="background:linear-gradient(120deg,#1B2A38 0%,#2A2419 62%,#14110C 100%)">
  <div class="l" style="inset:0;opacity:.18;background:
    repeating-linear-gradient(0deg,transparent 0 38px,rgba(96,150,200,.34) 38px 39px)"></div>
  <div class="l" style="left:0;right:0;bottom:0;height:44%;background:
    repeating-linear-gradient(90deg,rgba(210,190,150,.10) 0 118px,transparent 118px 124px)"></div>
</div>
```

Dura poco —2-3 s— y suele coincidir con una frase de enlace del guion.

## Comprobar el corte

Se extraen los dos fotogramas del corte y se miran pegados:

```bash
ffmpeg -y -ss 24.9 -i salida/episodio.mp4 -frames:v 1 render/_c_out.png
ffmpeg -y -ss 25.1 -i salida/episodio.mp4 -frames:v 1 render/_c_in.png
ffmpeg -y -i render/_c_out.png -i render/_c_in.png -filter_complex hstack render/_corte.png
```

Si al mirar `_corte.png` el ojo se va primero al salto de brillo y no a lo que cuenta la
escena, hay que igualar niveles antes de seguir.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Seis fondos diseñados por separado | Seis chispazos: el episodio no fluye |
| Fundido largo (más de 0,35 s) | Ritmo muerto; parece presentación |
| Puente que vuelve a entrar con fundido | Se lee como elemento repetido, no como continuidad |
| La luz salta de lado en cada corte | El espacio se vuelve incoherente |
| Anclaje "de color parecido" | No funciona: tiene que ser el mismo hex |
| Bisagra larga | Se convierte en una escena sin contenido |

## Relacionado

`50` · `51` · `53` · `58` · `70` cuándo usar transición · `73` transición por elemento · `76` entrar y salir de escena
