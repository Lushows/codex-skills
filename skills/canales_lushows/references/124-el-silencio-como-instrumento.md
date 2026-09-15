# 124 · El silencio como instrumento

**Qué resuelve:** que un golpe se sienta. Un impacto sobre un colchón que ya estaba
sonando se suma al nivel que había y apenas sube 2 dB de percepción. El mismo impacto
después de que la música se retire pega el doble sin subir ni un decibelio.

---

## Por qué funciona: el oído mide diferencias, no niveles

La sensación de fuerza no la da el nivel absoluto del golpe, la da el **salto** respecto a
lo que sonaba justo antes. Retirar el colchón 0,8 s antes del impacto regala unos 8-10 dB
de contraste percibido **gratis**: no se sube nada, se baja lo de al lado.

Es el recurso con la mejor relación efecto/coste de toda la mezcla, y por eso mismo se
gasta rapidísimo: **uno o dos por episodio, nunca más**.

## La forma del hueco

```
nivel
 1.0 ────────╲                          ╱──────────
             ╲                        ╱
 0.25         ╲______________________╱        ← nunca 0
         |0,35s|      0,9 s          |0,35s|
                      ↑
                 el golpe cae aquí, en el último tercio
```

| Parte | Valor | Por qué |
|---|---|---|
| Bajada | **0,35 s** | Más rápido se oye como corte; más lento no se percibe como retirada |
| Fondo del hueco | **0,6 a 1,2 s** | Menos de 0,6 no da tiempo a notar la ausencia; más de 1,2 se lee como avería |
| Profundidad | **×0,25 (−12 dB)** | Nunca 0: ver abajo |
| Subida | 0,35 s | Simétrica, para que el retorno no sea otro evento |
| El golpe | En el **último tercio** del hueco | Deja oír el vacío antes de llenarlo |

## 🔴 El hueco nunca llega a cero, y el room tone nunca baja

Dos reglas y las dos por la misma razón: el silencio digital absoluto no existe en el
mundo y el oído lo lee como una avería del reproductor, no como intención.

- La **música** baja a ×0,25 de su nivel (−12 dB), no a 0.
- El **room tone** (`amb_sala`) no participa del hueco: sigue sonando igual. Es el que
  sostiene que el archivo sigue vivo mientras la música desaparece.

Lo que se retira es la música y los ambientes de escena, nunca la capa de sala (`80`).

## 🔴 `between()` produce un clic, y está medido

La forma obvia de escribir el hueco es la que rompe la mezcla:

```
volume='0.34*(1-between(t\,20.0\,20.9))'      ← MAL
```

`between()` devuelve 0 o 1 sin nada en medio: el nivel pasa de 0,34 a 0 **entre dos
muestras contiguas**. Eso es un escalón, y un escalón es un clic.

Medición sobre la misma pieza, mismo hueco, con y sin rampas:

| Forma | Nivel en el hueco | Salto máximo entre muestras contiguas |
|---|---|---|
| `between()` | **−inf dB** (silencio digital) | **747 LSB — 2,3 % de fondo de escala** 🔴 |
| trapecio | −47,07 dB (−7,9 dB del entorno) | 162 LSB — 0,5 %, que es el propio material |

Los 747 LSB son el clic. No hace falta oírlo: se cuenta.

## La forma correcta: un trapecio invertido

```python
def hueco(centro, fondo=0.9, r=0.35, prof=0.75):
    """Muesca en la automatización del volumen. prof=0.75 deja el 25% del nivel.
    Devuelve un factor 0-1 para multiplicar por la ganancia de la música."""
    a, b = centro - fondo / 2, centro + fondo / 2
    return (f"(1-{prof}*max(0\\,min(1\\,min((t-({a:.2f}-{r}))/{r}\\,"
            f"(({b:.2f}+{r})-t)/{r}))))")
```

Y en la cadena de la música — probado, y sin clic:

```bash
ffmpeg -hide_banner -stream_loop -1 -i sonido/mus_expediente.wav \
  -filter_complex "[0:a]atrim=0:30,asetpts=PTS-STARTPTS,\
volume='0.34*(1-0.75*max(0\,min(1\,min((t-19.65)/0.35\,(21.25-t)/0.35))))':eval=frame[o]" \
  -map "[o]" -y musica_con_hueco.wav
```

Lo mismo, anclado a una palabra del guion (`123`) en vez de a un segundo a mano:

```python
g = cuando("consta", 62.98)                    # el golpe del remate
expr = f"{0.34*0.88:.3f}*{hueco(g - 0.35, fondo=0.9, r=0.35, prof=0.75)}"
# el centro del hueco va 0,35 s ANTES de la palabra: así el golpe cae en el
# último tercio del vacío y no en mitad de la subida
```

## Dónde va, y dónde no

| Va | No va |
|---|---|
| Antes del golpe que enuncia el método | Antes de cada transición |
| Antes de la cifra que cambia la historia | Antes de cada cifra |
| Antes de la frase final del episodio | Al final de cada bloque |
| Cuando el golpe ya existe y hay que hacerlo pesar | Como sustituto de un golpe que no existe |

Un hueco sin nada detrás es peor que no hacerlo: el espectador oye la preparación, espera
el impacto, y lo que llega es la voz siguiendo como si nada. La promesa incumplida cuesta
más atención de la que el hueco iba a ganar.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| `between()` sobre el volumen | Clic medible de 747 LSB en cada borde |
| Hueco hasta 0 absoluto | Suena a que el reproductor se colgó |
| Retirar también el room tone | Lo mismo: el archivo parece muerto medio segundo |
| Rampas de 0,05 s | Es un corte, no una retirada |
| Hueco de más de 1,2 s | Se lee como avería, y da tiempo a mirar el móvil |
| El golpe en mitad de la bajada | El impacto se come su propia preparación |
| Tres o cuatro huecos por episodio | El recurso se gasta y el del remate ya no vale nada |
| Hueco sin golpe detrás | Promesa incumplida: cuesta más de lo que gana |

## Relacionado

`120` la curva de intensidad · `125` música y destello · `84` picos dramáticos · `123`
anclar a palabra · `11` el hueco prohibido
