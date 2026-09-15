# 454 — Movimiento que sigue a la voz

En un montaje de imágenes fijas el movimiento no se cuelga de un reloj: se cuelga de **palabras**. El
elemento no entra «en el segundo 18,4», entra «en *aprendiz*». La diferencia parece cosmética y no lo
es: en cuanto se regraba la locución, el montaje anclado al reloj se cae entero y el anclado a
palabras sigue en su sitio.

Este módulo es el **mecanismo**: cómo se consigue el segundo exacto de cada palabra, con qué precisión,
y dónde falla.

---

## 1. El problema real no es transcribir, es alinear

Ya sabes lo que dice la locución: tienes el guion. Lo que no sabes es **cuándo** lo dice. Pedirle eso
a un reconocedor de voz completo es matar moscas a cañonazos, y en una máquina sin GPU no termina en
un tiempo útil. El alineamiento se resuelve con dos señales, y las dos son baratas:

1. **Los silencios reales del audio**, medidos con `silencedetect`. Marcan dónde acaba cada grupo
   fónico. Son datos medidos, no estimaciones.
2. **El reparto por sílabas dentro de cada grupo.** En español la duración de una palabra es casi
   proporcional a su número de sílabas, así que dentro de un grupo de dos segundos el error es de
   centésimas.

```bash
ffmpeg -hide_banner -i locucion.mp3 -af "silencedetect=noise=-34dB:d=0.12" -f null - 2>&1 \
  | grep -E "silence_(start|end)"
```
⚠️ `silencedetect` escribe en nivel `info`: con `-loglevel error` no imprime nada y parece que ha
fallado. El umbral `-34 dB` y el mínimo `0,12 s` son los que separan grupos fónicos sin partir
palabras; con `-40 dB` se pierden las pausas cortas y con `-25 dB` se corta dentro de las oclusivas.

### La forma real de los datos

Medido sobre una locución de 63,45 s:

| Magnitud | Valor |
|---|---:|
| Palabras | 155 |
| Silencios detectados | 27 |
| Grupos fónicos resultantes | 25 |
| Duración mediana del grupo | 1,55 s |
| Grupo más largo | 3,23 s (13 palabras) |
| Palabras por grupo (mediana) | 5 |

**Dónde está el error:** en los extremos de cada grupo es **cero**, porque son silencios medidos. Crece
hacia el centro del grupo, donde manda el reparto silábico. Con grupos de 1,55 s y cinco palabras el
desvío está en centésimas; en el peor grupo del episodio —3,23 s y trece palabras— puede acercarse a
la décima y media. Es exactamente del orden del adelanto que hay que dar de todas formas, así que no
molesta.

---

## 2. El adelanto: llegar a tiempo es llegar tarde

El oído resuelve una palabra en su ataque. La vista no: hay que mover el ojo hasta el elemento, luego
reconocerlo. Son **100 a 180 ms** de retraso antes de que la imagen signifique algo. Un elemento que
entra exactamente con la sílaba llega tarde.

> **Regla: `offset` de −0,04 a −0,08 s para un elemento que entra con fundido; hasta −0,15 s si entra
> deslizando, porque además hay que descontar su propio gesto de entrada.**

Un destello, en cambio, va prácticamente a tiempo (−0,04 s): no hay que buscarlo con la mirada, ocupa
todo el cuadro. La psicofísica detrás de esos números está en `canales_lushows/39`; aquí importa solo
que **el número entra en el evento como un `offset` negativo** y que quien lo pone es el montador, no
el alineador.

---

## 3. La tabla de eventos

```python
{"r": "ficha_policial", "ancla": "detenido", "offset": -0.06, "dura": 2.4,
 "entrada": "izq", "x": "W*0.62", "y": "H*0.18", "w": 520}
```

El motor resuelve `ancla` → segundo, le suma `offset`, y de ahí salen el `enable='between(t,…)'` del
`overlay` y los `fade` de entrada y salida. El movimiento del elemento (`451`) y su margen (`456`) se
calculan sobre esa ventana.

**Las tres reglas que hacen que esto no se rompa:**

1. **Una sola función resuelve el ancla.** Si el motor, el auditor y el medidor de solapes hacen cada
   uno su cuenta, acaban discrepando y estás auditando un vídeo que nadie va a ver. El detalle está en
   `canales_lushows/241`.
2. **Un ancla sin coincidencia avisa, no cae al defecto en silencio.** Si la palabra no aparece en la
   ventana de la escena, lo correcto es imprimir el aviso; lo que no puede pasar es que el elemento
   aterrice calladamente en el inicio de la escena.
3. **Si la palabra se repite, hay que decir cuál.** La normalización quita puntuación y baja a
   minúsculas, así que «vendió» aparece dos veces en la misma escena y sin un índice se coge la
   primera: el plano de la segunda venta se va a la primera, y todo parece correcto. Un campo
   `ancla_n` (0 = la primera, 1 = la segunda) lo resuelve.

---

## 4. Los límites, que son reales

- **El alineador reparte, no reconoce.** Si la locución se sale del guion —una palabra improvisada, una
  repetición del locutor— el reparto se desplaza dentro de ese grupo. Se arregla corrigiendo el
  guion, no el motor.
- **Palabras funcionales son malas anclas.** En este episodio «de», «y» y «que» salen ocho veces cada
  una. Se ancla a sustantivos, nombres propios y cifras.
- **Regrabar la voz invalida todos los tiempos, no el montaje.** Vuelves a correr el alineador y todo
  el episodio se recoloca solo. Ese es el rendimiento de todo este mecanismo.
- **El MP3 con tasa variable miente en la duración.** Comprueba con `ffprobe` que la duración del
  archivo y el último `fin` del alineador cuadran; si no, remuxea a un contenedor con índice.
- **No sirve para música.** Un corte sobre el pulso es otro problema: `24` y `325`.

### La verificación de dos minutos

```bash
python tiempos.py ep01 && python - <<'PY'
import json, io
pal = json.load(io.open("ep01/tiempos.json", encoding="utf-8"))["palabras"]
for a in ("aprendiz", "Eiffel", "consta"):
    print([f"{p['t']:.2f}" for p in pal if p["limpia"] == a.lower()], a)
PY
```
Imprime en qué segundo cae cada ancla. Se abre el audio, se salta a ese segundo y se escucha. Tres
anclas comprobadas a oído valen más que cualquier suposición sobre la precisión del alineador.

---

## Errores frecuentes

1. **Anclar al reloj.** Se regraba la voz y el episodio entero se descoloca.
2. **Anclar a palabras funcionales.** «de», «que», «y» salen ocho veces: el elemento cae donde le
   toque.
3. **No resolver la repetición.** Sin índice de aparición se coge la primera y no se nota nunca.
4. **Dejar que un ancla sin coincidencia caiga al inicio de la escena en silencio.** Un aviso por
   consola cuesta una línea.
5. **Resolver el ancla en tres sitios distintos.** El auditor mide un montaje que no es el que se va a
   ver.
6. **Poner el elemento exactamente en la palabra.** Llega tarde: hay que adelantarlo entre 40 y 150 ms.
7. **Dar el mismo adelanto a un destello que a un recorte que entra deslizando.** El segundo necesita
   además el tiempo de su propio gesto.
8. **Medir los silencios con `-loglevel error`** y concluir que `silencedetect` no funciona.
9. **Cambiar el umbral de `silencedetect` sin volver a mirar el número de grupos.** Con 25 grupos y
   25 tramos el reparto cuadra; con 40, el alineador empieza a unir trozos y el error crece.

---

## Relacionado

- `451` — la velocidad del movimiento que arranca en esa palabra
- `456` — el margen del elemento que acaba de entrar
- `459` — qué hacer con el plano cuando la voz calla
- `124` — transcripción y timecodes con IA: la otra vía para conseguir tiempos por palabra
- `325` — el corte en la sílaba: el mismo principio aplicado al montaje de vídeo
- `103` y `108` — `silencedetect`, `astats` y el instrumental de medida de audio
- `canales_lushows/39` — por qué el ojo exige adelanto, con los números de la sacada
- `canales_lushows/241` — la resolución de anclas como fuente única de verdad
- `437` — la misma idea aplicada a la luz: el destello anclado a la palabra, con su desfase medido
