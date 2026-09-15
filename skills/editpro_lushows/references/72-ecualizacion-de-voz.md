# 72 — Ecualización de voz

Ecualizar es subir o bajar el volumen de zonas específicas del sonido. Ni más ni menos. No es magia: es
un volumen selectivo por frecuencia.

Lo que casi nadie sabe es que **una voz es siempre la misma voz, pero puede sonar cara o barata según
qué bandas subas y cuáles bajes**. Este módulo es el mapa de esas bandas, con números que puedes copiar.

Va en el **paso 6** de la cadena de `70`: después de limpiar, antes de comprimir. Con la única excepción
del pasa-altos, que se adelanta al principio para no darle basura a la reducción de ruido.

---

## El mapa de la voz humana

Toda voz, en cualquier idioma, se reparte en las mismas seis zonas. Apréndete esta tabla y ya sabes
ecualizar.

| Zona | Rango | Qué vive ahí | Qué pasa si sobra | Qué pasa si falta |
|---|---|---|---|---|
| **Retumbe** | 20 – 80 Hz | Nada útil de la voz. Mesa, pisadas, viento, aire acondicionado | Suena embarrado, el compresor se vuelve loco | Nada. Quítalo siempre |
| **Cuerpo** | 100 – 250 Hz | La base, el peso, la autoridad de la voz | Suena "gordo", opaco, tapado | Suena flaco, de teléfono |
| **Nasal / cartón** | 300 – 600 Hz | La zona del "suena a caja" | Suena a que hablas dentro de una caja | Suena hueco, sin medio |
| **Presencia** | 1 – 4 kHz | **La inteligibilidad. Aquí se entiende lo que dices** | Suena agresivo, cansa el oído | Suena lejano, apagado, sin fuerza |
| **Sibilancia** | 5 – 9 kHz | La "s", la "ch", la "z" | Silba, raspa, molesta | Suena tapado, ceceoso |
| **Aire** | 10 – 16 kHz | Brillo, sensación de "caro" | Se realza el siseo y el ruido residual | Suena sordo, sin vida |

Si te quedas con una sola idea de este módulo: **la presencia (1–4 kHz) es donde vive la inteligibilidad.**
Es la banda por la que el teléfono transmite voz desde hace un siglo. Si tu voz se entiende mal, casi
siempre es porque le falta ahí, no porque le falte volumen.

---

## Las tres decisiones que resuelven el 90%

### 1. Pasa-altos en 80–100 Hz — quita el retumbe

Corta todo lo que está por debajo. Ahí no hay voz: hay basura.

```bash
ffmpeg -i voz.wav -af "highpass=f=85" salida.wav
```

Dónde poner el corte:

| Voz | Frecuencia de corte |
|---|---|
| Voz masculina grave | **80 Hz** |
| Voz masculina media / general | **85 Hz** |
| Voz femenina | **90 – 100 Hz** |
| Micro de solapa en exteriores (viento) | 100 – 120 Hz |

Con un solo polo el corte es suave. Si el retumbe es fuerte, súbele la pendiente:

```bash
# poles=2 corta más abrupto (12 dB por octava en vez de 6)
ffmpeg -i voz.wav -af "highpass=f=85:poles=2" salida.wav
```

**Este es el filtro con mejor relación beneficio/riesgo de todo el audio.** Casi nunca daña nada y casi
siempre mejora. Si solo vas a hacer una cosa, haz esta.

Cuidado con pasarte: si cortas en 150 Hz le quitas el pecho a la voz y suena a radio de taxi.

### 2. Realce de presencia en 1–4 kHz — la inteligibilidad

```bash
ffmpeg -i voz.wav -af "equalizer=f=2500:t=q:w=1.2:g=3" salida.wav
```

Lectura del comando:
- `f=2500` → centro en 2,5 kHz
- `t=q` → el ancho se expresa como Q
- `w=1.2` → Q de 1,2, o sea una campana ancha (afecta más o menos de 1,5 a 4 kHz)
- `g=3` → sube 3 dB

Dónde poner el centro según lo que necesites:

| Necesidad | Centro | Ganancia |
|---|---|---|
| Que se entienda mejor (consonantes) | **2 – 3 kHz** | +2 a +4 dB |
| Que suene más cerca, más íntimo | 1 – 1,5 kHz | +1 a +2 dB |
| Que corte por encima de la música | 3 – 4 kHz | +2 a +3 dB |

**Regla de oro:** +3 dB es mucho. +6 dB es demasiado. Si necesitas +9 dB para que se entienda, el
problema no es el EQ, es el micrófono o la distancia a la que grabaste.

**El realce de presencia cansa.** Un video de 30 segundos con +4 dB en 3 kHz suena espectacular. Un
podcast de 40 minutos con lo mismo deja al oyente con dolor de cabeza. Ajusta según duración:

| Duración | Presencia |
|---|---|
| Reel / anuncio (< 60 s) | +3 a +4 dB |
| YouTube (5–15 min) | +2 dB |
| Podcast (> 30 min) | +1 dB o nada |

### 3. Caída suave por encima de 10 kHz — baja sibilancia y ruido

```bash
ffmpeg -i voz.wav -af "lowpass=f=12000" salida.wav
```

O, más elegante, una estantería suave que baja sin cortar de golpe:

```bash
ffmpeg -i voz.wav -af "highshelf=f=10000:g=-3:t=q:w=0.7" salida.wav
```

Esto hace dos cosas a la vez: le baja el filo a las eses y **se lleva el siseo residual** que dejó la
reducción de ruido, que casualmente vive justo ahí arriba. Es un dos por uno.

No lo lleves más abajo de 8 kHz o la voz pierde toda la vida y suena a llamada telefónica.

---

## El EQ de voz completo, en un comando

```bash
ffmpeg -i voz_limpia.wav -af "highpass=f=85:poles=2,equalizer=f=200:t=q:w=1.0:g=-2,equalizer=f=400:t=q:w=1.5:g=-3,equalizer=f=2500:t=q:w=1.2:g=3,highshelf=f=10000:g=-3:t=q:w=0.7" voz_eq.wav
```

Traducción, eslabón por eslabón:

| Trozo | Qué hace |
|---|---|
| `highpass=f=85:poles=2` | Corta el retumbe con pendiente firme |
| `equalizer=f=200:g=-2` | Baja 2 dB el exceso de cuerpo (típico de micro muy cerca) |
| `equalizer=f=400:g=-3` | Baja 3 dB el "cartón" nasal |
| `equalizer=f=2500:g=3` | Sube 3 dB la presencia: se entiende |
| `highshelf=f=10000:g=-3` | Baja el filo y el siseo de arriba |

Fíjate en la proporción: **tres cortes y un realce.** Así trabaja la gente que sabe. Los que empiezan
suben todo lo que les gusta y bajan nada, y terminan con un audio saturado y sin espacio.

> **Regla que vale para siempre: es mejor bajar lo que sobra que subir lo que falta.** Cortar no agrega
> ruido ni riesgo de saturación. Realzar sí. Si quieres más presencia, empieza bajando 400 Hz antes de
> subir 2,5 kHz — a veces con eso basta.

---

## Sintaxis de los filtros de ffmpeg, sin misterio

### `equalizer` — campana (sube o baja una zona)

```
equalizer=f=FRECUENCIA:t=TIPO_DE_ANCHO:w=ANCHO:g=GANANCIA_EN_dB
```

- `t=q` → `w` es Q. **Q alto = campana estrecha.** Q 0,7 es ancha, Q 4 es quirúrgica.
- `t=o` → `w` está en octavas. `w=1` es una octava de ancho.
- `t=h` → `w` está en Hz.

Guía de Q:

| Q (`w` con `t=q`) | Ancho | Para qué |
|---|---|---|
| 0,5 – 0,9 | Muy ancha | Cambios de carácter, se oye "musical" |
| 1,0 – 2,0 | Media | **El rango de uso normal en voz** |
| 3 – 8 | Estrecha | Matar una resonancia molesta puntual |
| 10+ | Quirúrgica | Hum eléctrico, pitidos |

### `highshelf` y `lowshelf` — estantería (sube o baja todo de un punto en adelante)

```bash
# subir todo por encima de 8 kHz: aire, brillo
ffmpeg -i voz.wav -af "highshelf=f=8000:g=2:t=q:w=0.7" salida.wav

# bajar todo por debajo de 150 Hz sin cortar del todo
ffmpeg -i voz.wav -af "lowshelf=f=150:g=-4:t=q:w=0.7" salida.wav
```

### `highpass` y `lowpass` — corte (elimina de un punto para allá)

```bash
ffmpeg -i voz.wav -af "highpass=f=85:poles=2,lowpass=f=14000" salida.wav
```

`poles=1` es 6 dB/octava (suave), `poles=2` es 12 dB/octava (firme). Para voz, 2 está bien.

---

## Cómo encontrar la frecuencia molesta (barrido)

Cuando una voz tiene un "algo" que no te gusta y no sabes dónde está, se busca así: subes mucho una
campana estrecha y la paseas hasta que el defecto grite. Cuando lo encuentras, inviertes el signo.

```bash
# 1) subir +12 dB con Q estrecho y escuchar en 400 Hz
ffmpeg -i voz.wav -af "equalizer=f=400:t=q:w=6:g=12" prueba_400.wav

# 2) repetir en 600, 800, 1000... hasta que uno suene horrible
ffmpeg -i voz.wav -af "equalizer=f=600:t=q:w=6:g=12" prueba_600.wav

# 3) el que suene peor es tu culpable. Ahora córtalo, con Q más ancho y poca ganancia
ffmpeg -i voz.wav -af "equalizer=f=600:t=q:w=2:g=-4" voz_corregida.wav
```

Nota la diferencia entre buscar y corregir: **buscas con Q estrecho y mucha ganancia; corriges con Q
ancho y poca ganancia.** Corregir con Q estrecho deja un hueco que se oye como un agujero.

Ver el espectro también ayuda a orientarte:

```bash
ffmpeg -i voz.wav -lavfi showspectrumpic=s=1280x600:legend=1:scale=log espectro.png
```

---

## Recetas por tipo de voz y situación

**Voz masculina grave con exceso de pecho** (micro muy cerca, efecto de proximidad):

```bash
ffmpeg -i voz.wav -af "highpass=f=80:poles=2,lowshelf=f=200:g=-4:t=q:w=0.7,equalizer=f=2800:t=q:w=1.2:g=3" salida.wav
```

**Voz femenina que suena flaca:**

```bash
ffmpeg -i voz.wav -af "highpass=f=95:poles=2,equalizer=f=180:t=q:w=1.0:g=2,equalizer=f=2200:t=q:w=1.4:g=2.5,highshelf=f=10000:g=-2:t=q:w=0.7" salida.wav
```

**Grabado con celular** (todo suena a caja, falta arriba y abajo):

```bash
ffmpeg -i voz.wav -af "highpass=f=90:poles=2,equalizer=f=500:t=q:w=1.5:g=-4,equalizer=f=3000:t=q:w=1.2:g=4,highshelf=f=9000:g=1.5:t=q:w=0.7" salida.wav
```

**Micro de solapa en exteriores** (viento y ropa):

```bash
ffmpeg -i voz.wav -af "highpass=f=110:poles=2,equalizer=f=350:t=q:w=2:g=-3,equalizer=f=2600:t=q:w=1.2:g=3,highshelf=f=11000:g=-2:t=q:w=0.7" salida.wav
```

**Voz que compite con música fuerte** (además del ducking de `75`, dale un carril propio):

```bash
ffmpeg -i voz.wav -af "highpass=f=100:poles=2,equalizer=f=3200:t=q:w=1.0:g=4" salida.wav
```

Y a la música le haces el hueco inverso, en la misma frecuencia:

```bash
ffmpeg -i musica.wav -af "equalizer=f=3200:t=q:w=1.0:g=-4" musica_con_hueco.wav
```

Eso se llama **EQ complementario**: en vez de subir la voz hasta tapar todo, le abres un carril en la
música. Suena más natural que subir el volumen, y es lo que hace que en un anuncio de radio se entienda
todo sin que nada esté gritando.

---

## Cómo escuchar lo que hiciste

Comparar EQ es traicionero porque **subir cualquier cosa suena "mejor"** por puro volumen. Iguala antes
de juzgar:

```bash
ffmpeg -i sin_eq.wav -af loudnorm=I=-14:TP=-1.5 a.wav
ffmpeg -i con_eq.wav -af loudnorm=I=-14:TP=-1.5 b.wav
```

Y escucha en tres sitios, en este orden de importancia:

1. **Parlante de celular.** Ahí es donde el 80% de la gente lo va a oír. Y el parlante del celular casi
   no reproduce debajo de 300 Hz, así que la presencia es todo.
2. **Audífonos baratos**, no los buenos. Los buenos perdonan.
3. Parlantes de computador.

Si suena bien en el parlante del celular, suena bien en todas partes. Al revés no se cumple.

---

## Errores comunes

- **Subir en vez de bajar.** Tres cortes y un realce, no cuatro realces. Cortar es gratis; realzar tiene
  costo (ruido, saturación, fatiga).
- **Realzar la presencia antes del de-esser.** Amplificas el silbido que ibas a domar. El de-esser va
  primero (ver `70`).
- **Pasa-altos demasiado alto.** Cortar en 150 Hz le arranca el pecho a la voz. 80–100 Hz.
- **Q estrecho para corregir.** Deja un hueco audible. Estrecho para *buscar*, ancho para *corregir*.
- **Ecualizar antes de limpiar el ruido.** Le subes el volumen a la suciedad.
- **Usar la misma receta para todas las voces.** Una voz grave y una aguda necesitan cortes distintos.
  La tabla del mapa es el criterio; los comandos son puntos de partida.
- **+6 dB o más en cualquier banda.** Casi siempre significa que el problema es de grabación.
- **Meter mucho "aire" (12–16 kHz) sobre una toma con ruido.** Le subes el volumen al siseo.
- **Juzgar el EQ sin igualar volumen.** Lo más fuerte siempre gana la comparación.
- **Ecualizar solo con audífonos buenos.** Perdonan todo. El juez real es el parlante del celular.
- **Aplicar presencia de anuncio a un podcast de 40 minutos.** Fatiga auditiva. Baja a +1 o +2 dB.

---

## Checklist

- [ ] El EQ va **después** de la limpieza de ruido y del de-esser.
- [ ] Tengo un **pasa-altos entre 80 y 100 Hz**, ajustado al tipo de voz.
- [ ] Hay **más cortes que realces** en mi cadena.
- [ ] Ningún realce pasa de **+4 dB**.
- [ ] El realce de presencia está entre **1 y 4 kHz** y elegí el centro a propósito.
- [ ] La ganancia de presencia está ajustada a la **duración** de la pieza (menos en podcast).
- [ ] Hay una **caída suave por encima de 10 kHz** para sibilancia y siseo.
- [ ] Si había una resonancia molesta, la **encontré con barrido** (Q estrecho, +12 dB) y la corregí con
      **Q ancho y poca ganancia**.
- [ ] Si la voz compite con música, usé **EQ complementario** (hueco en la música) y no solo más volumen.
- [ ] Comparé antes/después **igualando LUFS**.
- [ ] Escuché en **parlante de celular** y ahí se entiende cada palabra.
- [ ] La voz no silba, no retumba, no suena a caja y no suena a teléfono.
