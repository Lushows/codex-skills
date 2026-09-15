# 72 · Match cut de forma

**Qué resuelve:** unir dos escenas por una forma que se repite —un círculo que se
convierte en otro círculo, una silueta que hereda otra silueta— para que el corte duro
sea el más fuerte del episodio. Y dejar claro que **esto se planifica en el guion visual,
nunca se improvisa en el render**.

---

## Qué es y por qué es la transición más barata que existe

El match cut es un **corte duro**. No lleva fundido, no lleva filtro, no cuesta un
fotograma de render extra: cuesta *elegir bien las dos imágenes*. Funciona porque el ojo
sigue una forma; si la forma sigue ahí después del corte, la atención cruza sin romperse
y el cerebro entiende que las dos cosas están relacionadas. Eso es exactamente lo que
hace un documental de dinero: relacionar.

| Escena A cierra en… | Escena B abre en… | Lo que dice el corte |
|---|---|---|
| La moneda que gira | El disco de un carrete de cinta del juzgado | Lo que era dinero ahora es prueba |
| El círculo del sello de "APROBADO" | El círculo de una mira / un objetivo de cámara | Lo aprobado quedó vigilado |
| Silueta del edificio corporativo | Silueta de la torre de una cárcel | El imperio y su final, misma forma |
| El fajo de billetes visto de canto | La pila de expedientes vista de canto | Cada billete tiene su papel |
| La huella del pulgar | El mapa del país con la misma mancha | De una persona a un país |

---

## La regla de las tres coincidencias

Para que el corte funcione, las dos formas tienen que coincidir en **tres cosas**:

| Coincidencia | Tolerancia | Cómo se consigue |
|---|---|---|
| **Posición** del centro | ±40 px sobre 1920×1080 | Se fija en el guion visual, con coordenadas |
| **Tamaño** (diámetro o alto) | ±8% | Se ajusta el `w` del elemento, no se "acerca a ojo" |
| **Dirección del movimiento** | La misma en las dos | Si A se acerca, B sigue acercándose |

Si falla la posición, se lee como error de montaje. Si falla el tamaño, se lee como
salto. Si falla la dirección, se lee como dos planos distintos pegados.

---

## Cómo se planifica (esto es lo importante)

El match cut nace **en la fase 6, el guion visual**, y condiciona la fase 5 (material):
si no existe una foto de archivo con la forma en el sitio correcto, **el match cut no se
hace**. No se fuerza con una foto que no empata.

En la tabla de escenas se declara explícito, para que quien renderice sepa que esas dos
coordenadas no se tocan:

```python
{"id": "auge", "ini": 41.2, "fin": 52.0, "fondo": "f_torre",
 "cierra_en": {"forma": "circulo", "cx": 960, "cy": 470, "d": 360},
 "elementos": [ ... ]},
{"id": "caida", "ini": 52.0, "fin": 63.4, "fondo": "f_juzgado",
 "abre_en":   {"forma": "circulo", "cx": 960, "cy": 470, "d": 360},
 "elementos": [ ... ]},
```

`cierra_en` y `abre_en` no los usa el motor: son un **contrato entre las dos escenas**.
El que coloca los elementos de `caida` está obligado a poner su círculo en 960/470 con
360 px de diámetro. Sin ese contrato escrito, se descubre el descuadre al ver el vídeo
montado, cuando ya cuesta una hora rehacerlo.

Regla de escritura: el elemento que sostiene la forma **no puede tener `fade_out`** en A
(desaparecería antes del corte) ni `fade` de entrada en B (aparecería después). En los
dos casos se pone `fade_out: 0` y entrada `dura` para que la forma esté completa en el
fotograma del corte.

---

## Verificación: comparar el último fotograma con el primero

Nunca se da por bueno "a ojo". Se extraen los dos fotogramas y se superponen:

```bash
# último fotograma de la escena A (0,04 s antes del final = 1 fotograma a 25 fps)
ffmpeg -sseof -0.04 -i salida/e03_auge.mp4  -frames:v 1 -y /tmp/ult.png
# primer fotograma de la escena B
ffmpeg          -i salida/e04_caida.mp4     -frames:v 1 -y /tmp/pri.png
# promedio de los dos: si la forma coincide, se ve UNA forma nítida; si no, se ve doble
ffmpeg -i /tmp/ult.png -i /tmp/pri.png \
  -filter_complex "[0:v][1:v]blend=all_mode=average" -y /tmp/match.png
```

Si en `match.png` se ven **dos círculos fantasma**, hay descuadre: se corrigen las
coordenadas del elemento de B y se vuelve a renderizar esa escena (no todo el episodio).

---

## Duración: cuánto tiene que durar la forma antes del corte

| Momento | Tiempo | Por qué |
|---|---|---|
| La forma aparece en A | ≥ **0,8 s** antes del corte | El ojo necesita tiempo para fijarla |
| La forma está sola o dominando | últimos **0,4 s** de A | Si compite con tres elementos, no se fija |
| El corte | 0 fotogramas de fundido | Un fundido de 2 fotogramas ya destruye el efecto |
| La forma se mantiene en B | ≥ **0,6 s** | Antes de eso no se puede mover ni salir |

Total: el match cut se come unos **2 segundos** de episodio. Es la transición más cara
en tiempo de pantalla y la más barata en render.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Decidirlo en el render, con el material ya cerrado | Se termina forzando una foto que no empata y el corte se lee como error |
| Poner un `xfade` "por si acaso" | El efecto desaparece: el match cut vive del corte seco |
| Formas parecidas pero de tamaño distinto | Se lee como un salto de zoom, no como una relación |
| La forma tapada a medias por otro elemento en B | El ojo no la reconoce y el corte no significa nada |
| Dos match cuts en el mismo episodio | El segundo delata al primero como truco; uno por episodio |
| Elegir la forma antes que la idea | El match cut tiene que *decir* algo; si no dice nada, es decoración |

## Relacionado

`70` · `73` · `78` · `21` · `29` · `93`
