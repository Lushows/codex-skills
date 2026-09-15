# 433 — El destello mudo

> **Un fogonazo mudo se lee como un error de codificación, no como un recurso.** No es una opinión de
> estilo: es lo que hace el cerebro con un salto de luz sin causa. Le busca una explicación, no la
> encuentra en la escena, y la archiva como fallo de reproducción.

Por eso la regla del bloque no tiene excepciones: **cada destello lleva su sonido**. Y si el sonido no
cabe — porque hay locución encima, porque la mezcla está llena —, entonces **no lleva destello**.

---

## 1. Qué sonido

Un impacto corto de agudos, no un golpe grave. El grave es del *golpe* de escala (`53`); la luz suena
brillante. Tres propiedades medibles:

| Propiedad | Valor | Por qué |
|---|---|---|
| Ataque | **el primer sample** | Un impacto con ataque lento se oye después del destello |
| Caída | **0,15–0,25 s** a silencio | Más largo se convierte en ambiente, no en acento |
| Banda | por encima de **3,5 kHz** | Deja libre la zona de la voz (`85`) |

Sintetizado con ffmpeg, sin banco de efectos — es el `tr_flash` del motor documental:

```bash
ffmpeg -y -f lavfi -i "anoisesrc=c=white:a=1:d=0.55:r=48000" \
  -af "highpass=f=3500,volume='pow(max(0\,1-t/0.18)\,2.6)':eval=frame" tr_flash.wav
```

Medido sobre el archivo resultante (RMS por ventanas de 10 ms): **pico en t = 0,000 s a −9,1 dBFS**, y
a los 0,20 s ya está en silencio absoluto. El exponente 2,6 es lo que hace que caiga rápido al
principio y se apague sin cola.

> ⚠️ **La misma trampa del `eval=frame`, pero al revés.** `volume` con una expresión y sin
> `eval=frame` **no** produce un fallo mudo: aborta con `Invalid value NaN for volume` y no escribe el
> archivo. `eq` calla y `volume` grita — vale la pena saber cuál es cuál (`431`).

---

## 2. Dónde va: la sincronía, con criterio, no a ojo

La norma de referencia es **Recomendación UIT-R BT.1359-1**, *Relative timing of sound and vision for
broadcasting*. Sus cifras, con el signo positivo significando **sonido adelantado** respecto a la imagen:

| Umbral | Sonido adelantado | Sonido retrasado |
|---|---|---|
| **Detectabilidad** (el espectador medio lo nota) | +45 ms | −125 ms |
| **Aceptabilidad** (molesta) | +90 ms | −185 ms |
| Tolerancia global que la norma exige no rebasar | +90 ms | −185 ms |

Y la de producción europea, más estricta: **EBU R37-2007** fija la ventana en **+40 ms / −60 ms** a la
salida hacia el transmisor.

**La asimetría es el dato que hay que interiorizar:** el oído perdona el sonido *tarde* casi tres veces
más que el sonido *pronto*. En la vida real el sonido siempre llega después de la luz; adelantarlo es
antinatural y se detecta a los 45 ms.

### Lo que eso significa en fotogramas

| fps | 1 fotograma | ¿Cabe un fotograma de adelanto? |
|---|---|---|
| 60 | 16,7 ms | Sí, sobra margen |
| 30 | 33,3 ms | Sí, justo |
| 25 | **40,0 ms** | **En el límite exacto de EBU R37** |
| 24 | 41,7 ms | **No.** Ya se pasa |

> **Regla operativa: a 25 fps o menos, nunca adelantes el impacto más de un fotograma, y si puedes,
> medio.** Retrasarlo un fotograma es siempre más seguro que adelantarlo uno.

---

## 3. Medido en material real

En el piloto documental el impacto se coloca en `acabar.py` y la luz en `guion_visual.py`, por separado.
Resolviendo ambos contra `tiempos.json`:

| Palabra ancla | Pico de luz | Arranque del impacto | Desfase | ¿Dentro de EBU R37? |
|---|---|---|---|---|
| *broma* (lustig) | 33,02 s | 33,00 s | **sonido +20 ms** | sí |
| *papel* (ep 01) | 50,12 s | 50,09 s | **sonido +30 ms** | sí, al 75 % del margen |
| *fachada* (ep 01) | 63,59 s | 63,56 s | **sonido +30 ms** | sí, al 75 % del margen |

Como el pico de energía de `tr_flash` está en su primer sample, el arranque del archivo **es** el
impacto. Los tres casos adelantan el sonido entre 20 y 30 ms: legales, pero consumiendo la mitad o tres
cuartos del margen del lado peligroso. **Lo correcto sería el mismo instante o 10 ms después**, y se
consigue cambiando un `-0.06` por `-0.04` en la tabla de pistas.

---

## 4. El arnés para comprobarlo

No se comprueba mirando la línea de tiempo: se comprueba midiendo el archivo final, que es donde ya
actuaron todos los retardos de filtros y del mezclador.

```bash
# pico de luz, fotograma a fotograma
ffmpeg -hide_banner -i final.mp4 -vf "signalstats,metadata=print:key=lavfi.signalstats.YAVG" \
  -f null - 2>&1 | grep -E "pts_time|YAVG"

# envolvente de audio en ventanas de 10 ms
ffmpeg -hide_banner -i final.mp4 \
  -af "astats=metadata=1:reset=1:length=0.01,ametadata=print:key=lavfi.astats.Overall.RMS_level" \
  -f null - 2>&1 | grep -E "pts_time|RMS_level"
```

Se busca el máximo de cada serie en la ventana de ±0,3 s alrededor del destello y se restan. El
resultado, en milisegundos, se compara con la tabla del §2. Con `-loglevel error` no sale nada (`432`).

**El caso límite que hay que vigilar:** si la pieza lleva locución, el pico de RMS de esa ventana puede
ser una sílaba, no el impacto. Mide la envolvente **de la pista de efectos antes de mezclar**, o filtra
por encima de 3,5 kHz para aislar el impacto de la voz.

---

## 5. Cuando no hay sitio para el sonido

Tres salidas, en orden de preferencia:

1. **Quitar el destello.** Si la mezcla está llena en ese instante, ese momento ya tiene acento. Dos
   acentos a la vez no suman: se estorban.
2. **Bajar la voz 1 dB durante 0,25 s** alrededor del impacto, con una automatización, no con un
   compresor lateral: el *ducking* automático se oye bombear en un evento tan corto (`75`).
3. **Usar el acento que ya existe.** Si justo ahí cae un golpe de la música, ancla el destello a él y no
   añadas nada. Es la opción más barata y la que mejor suena.

---

## Errores frecuentes

- **Dejar el destello mudo.** El error central del módulo: se lee como fallo de codificación.
- **Poner un golpe grave.** Es el sonido del *golpe* de escala (`53`), no el de la luz. Suena a otro
  recurso.
- **Impacto con ataque lento.** Si el pico de energía está a 40 ms del inicio del archivo, ya llegas
  tarde aunque el archivo empiece a tiempo. Mide el pico, no el inicio.
- **Adelantar el sonido "un par de fotogramas".** A 25 fps son 80 ms: por encima del umbral de
  detectabilidad de BT.1359 y del doble del margen de EBU R37.
- **Comprobar la sincronía en la línea de tiempo del editor.** Los filtros y el mezclador introducen
  retardos. Se mide sobre el archivo final.
- **Medir la envolvente con la voz dentro.** El pico que encuentras es una sílaba. Aísla la pista o
  filtra por encima de 3,5 kHz.
- **`volume` con expresión sin `eval=frame`.** Aborta con `Invalid value NaN for volume`. Aquí sí avisa.
- **Un impacto con cola de 0,5 s.** Deja de ser acento y se convierte en ambiente.

---

## Relacionado

- `430` — qué destellos merecen existir (y por tanto merecen sonido).
- `431` — la campana de luz que este sonido acompaña.
- `432` — el arnés de luminancia del que sale la mitad de esta medición.
- `53` — flash, whip y golpe: cada uno con su sonido propio.
- `76`, `77`, `85` — diseño sonoro, sonido real contra efecto, y sitio para la voz.
- `canales_lushows` `125-musica-y-destello.md` y `81-sintetizar-efectos.md` — el golpe completo en el
  motor del canal documental: luz, impacto y **acorde de piano** en el mismo fotograma.

**Fuentes:** [Rec. UIT-R BT.1359-1](https://www.itu.int/dms_pubrec/itu-r/rec/bt/R-REC-BT.1359-1-199811-I!!PDF-E.pdf) ·
[EBU Recommendation R37-2007](https://tech.ebu.ch/docs/r/r037.pdf)
