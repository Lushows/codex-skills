# 459 — Cuando el plano se queda quieto

Nueve módulos para mover imágenes fijas y uno para lo contrario, que también hace falta por dos
motivos distintos: hay planos que **deben** quedarse quietos, y hay planos que se quedan quietos sin
que nadie lo haya decidido. El segundo caso es el peligroso, porque no avisa.

---

## 1. El quieto involuntario: cómo se detecta

Un plano puede estar «quieto» de tres maneras, y cada una tiene su medida.

### Congelado del todo

```bash
ffmpeg -hide_banner -i plano.mp4 -vf "freezedetect=n=0.001:d=0.5" -f null -
# [Parsed_freezedetect_1] lavfi.freezedetect.freeze_start: 0
```
⚠️ **Con `-loglevel error` no imprime nada** y parece que no ha encontrado nada. `freezedetect`,
`blackdetect`, `signalstats` y `metadata=print` escriben en nivel `info`.

### Se mueve, pero por debajo de lo perceptible

La medida honesta es la diferencia media entre fotogramas consecutivos:

```bash
ffmpeg -hide_banner -i plano.mp4 \
  -vf "tblend=all_mode=difference,signalstats,metadata=print:key=lavfi.signalstats.YAVG" \
  -f null - 2>&1 | grep -o "YAVG=[0-9.]*"
```

Medido sobre el mismo fondo, a 640×360:

| Plano | Diferencia media |
|---|---:|
| quieto de verdad (`z=1`) | **0,000** |
| empuje del 8% en 12 s | 0,217 |
| empuje del 8% en 4 s | 0,453 |
| empuje del 12% en 6,73 s | 0,468 |

**Cero exacto es congelado. Por debajo de 0,15 el plano se lee como quieto aunque la expresión diga
otra cosa.** Y ojo con la trampa de `mpdecimate`: con sus umbrales de fábrica, ese empuje del 12%
perfectamente sano deja solo 3 fotogramas de 168, porque el filtro está pensado para telecine. Los
umbrales que sirven aquí están en `453 §4`.

### Se mueve en la expresión y no en la pantalla

Es el caso de `456 §1`: la coordenada se sale del rango y `zoompan` la satura sin decir nada. En un
caso real, el 60% de los fotogramas de una deriva diagonal tenían la `x` saturada. La diferencia
media delata el tramo muerto: 0,45 en el primer tercio, 1,09 en el centro.

### La grilla, que sigue siendo la prueba más barata

```bash
ffmpeg -hide_banner -y -i pieza.mp4 -vf "fps=2,scale=240:-1,tile=8x6" -frames:v 1 grilla.png
```
Si hay más de tres cuadritos seguidos idénticos, hay hueco. Cuesta un segundo y se ve de un vistazo.

---

## 2. El quieto deliberado, que es una decisión legítima

Después de nueve módulos de movimiento, hay que decirlo claro: **el movimiento no es una virtud, es una
herramienta.** Hay cuatro casos en los que la quietud es la respuesta correcta.

| Caso | Por qué | Cuánto aguanta |
|---|---|---|
| **Un dato que hay que leer** | un gráfico, una cifra, una captura. El movimiento pelea contra la lectura | 1,2–1,8 s, con el texto grande |
| **El respiro tras una ráfaga** | si el resto va a 1,5 s por corte, la quietud es contraste, no vacío | 0,8–1,2 s |
| **El remate** | el último plano antes del silencio; moverlo lo abarata | hasta 2 s |
| **El retrato que sostiene la mirada** | una cara mirando a cámara aguanta quieta lo que no aguanta un paisaje | 1,5 s |

La regla que los une: **la quietud dura menos que el movimiento.** Un plano con empuje aguanta 2,5 s
antes de aburrir; uno quieto, 0,8 s. Si vas a dejar algo quieto, acórtalo. Las duraciones por tipo de
plano están en `83 §7`.

### Cómo se entra y se sale de un plano quieto

- **Entrar desde movimiento a quieto: bien.** El contraste subraya el dato.
- **Salir de quieto a movimiento: mal.** El corte hace evidente lo muerta que estaba la imagen
  anterior. Si el plano quieto tiene que ir seguido de uno movido, mete algo que cambie en el último
  medio segundo: un rótulo que entra, un destello, un fundido de salida.
- **La salida en movimiento no existe aquí**, así que el corte tiene que apoyarse en el sonido: un
  golpe, un cambio de música, el arranque de una frase (`24`, `75`).

---

## 3. El quieto que no es quieto: el movimiento que no comunica

Peor que un plano parado es uno que se mueve **sin decir nada**: un empuje del 3%, una deriva que
recorre 20 px en cinco segundos. Cuesta exactamente lo mismo renderizarlo que uno bueno (`458`) y no
aporta nada. En la práctica hay dos salidas y ninguna es «dejarlo así»:

1. **Subir el recorrido hasta la banda** (`451`: 13–40 px/s en horizontal, 8–24 en vertical).
2. **Bajar a cero y acortar el plano.** Un plano quieto de 0,9 s es una decisión; uno que se mueve un
   3% durante cuatro segundos es un descuido.

> **La prueba: si al quitar el movimiento el plano no empeora, es que el movimiento no estaba
> haciendo nada.** Renderiza las dos versiones y mira la grilla.

---

## Errores frecuentes

1. **Dejar una imagen fija tal cual** y esperar que se sienta bien. Se lee como que el vídeo se ha
   trabado, siempre (`83`).
2. **Buscar el congelado con `-loglevel error`.** `freezedetect` no imprime nada y parece que todo
   está bien.
3. **Usar `mpdecimate` con los umbrales de fábrica** para saber si un plano se mueve. Un empuje sano
   parece 165 fotogramas duplicados.
4. **No comprobar que el movimiento declarado ocurre de verdad.** La coordenada satura en silencio.
5. **Movimiento del 3%.** Cuesta igual y no sirve para nada: o sube a la banda o se queda a cero.
6. **Dejar quieto un plano tanto tiempo como uno movido.** La quietud aguanta un tercio.
7. **Animar un gráfico de datos.** El movimiento estorba la lectura; déjalo quieto y acórtalo.
8. **Cortar de un plano quieto a uno en movimiento** sin nada que cambie antes del corte.
9. **Confundir el respiro con el descuido.** Un plano quieto entre planos rápidos es ritmo (`20`); un
   plano quieto entre planos quietos es un vídeo muerto.

---

## Relacionado

- `450` — el catálogo de gestos, para decidir si este plano quiere uno o ninguno
- `451` — las bandas de velocidad: por debajo de qué número el movimiento no existe
- `453` — `mpdecimate` con los umbrales apretados, y los tres temblores
- `455` — las trampas que dejan un plano quieto sin que ffmpeg diga nada
- `456` — la coordenada que satura y mata la deriva a mitad de plano
- `458` — lo que cuesta un movimiento que no comunica: exactamente lo mismo que uno bueno
- `83 §7` y `§8` — cuánto dura cada tipo de plano y los tres casos de «no animar»
- `20` y `27` — el pulso del vídeo y el diagnóstico de un montaje lento
- `108` — `freezedetect`, `signalstats` y el instrumental de medida
- `449` — el protocolo de «¿esto suma o solo encarece?», y por qué SSIM no sirve para juzgarlo
