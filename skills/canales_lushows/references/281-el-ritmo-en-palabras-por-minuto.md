# 281 · El ritmo en palabras por minuto

**Qué resuelve:** cuánto dura un guion antes de grabarlo, y por qué el `rate` de la voz
es un parámetro **estructural** y no un gusto. De las palabras por minuto sale la
duración del episodio, y de la duración salen los tiempos de todos los elementos del
montaje. Es el primer número del que se cuelga todo lo demás.

---

## El dato del canal

```
es-MX-JorgeNeural · rate -6% · pitch -2Hz  →  147 palabras por minuto
```

Medido sobre `piloto/ep01-lustig`: **155 palabras en 63,432 s** = 146,6 ppm. Un narrador
de documental va entre 130 y 160; a 168 (que es lo que daba `+8%`) el episodio corre y
las cifras no se retienen.

```python
print(f"ritmo: {len(texto.split())/d*60:.0f} palabras por minuto")   # voz.py, al final
```

Ese `print` está en `voz.py` a propósito: es la primera comprobación de la fase 3.

## ⚠️ Las palabras por minuto NO son la duración del episodio

Corregido tras montar el episodio 1 entero. El `rate` gobierna la velocidad del HABLA, pero **el 28% del episodio no era habla**: eran los 1,05 s fijos que edge-tts pone detrás de cada punto. Con 135 puntos en 1.378 palabras, eso son dos minutos y cuarto de silencio en un episodio de diez.

Cuando un episodio se siente largo, **lo primero que hay que medir es el silencio, no el `rate`** (§ `400`). Acelerar la voz se oye; quitar silencio no.

## `rate` es una escala de tiempo exacta

No es una aproximación. Lo verificado, con dos episodios distintos:

| Episodio | palabras | `rate` | duración medida |
|---|---|---|---|
| `ep01-lustig` | 155 | `-6%` | **63,432 s** |
| `episodio01` | 201 | `+8%` | **80,232 s** |
| `episodio01` (mismo texto, regenerado) | 201 | `-6%` | **92,184 s** |

Predicción desde la primera medida: `80,232 × 1,08 / 0,94 = 92,18 s`. Medido:
**92,184 s**. **Error: 4 milésimas sobre 92 segundos.**

> **La ley:** `duración(rate) = duración(0%) / (1 + rate)`. Se genera una vez a
> cualquier velocidad y se sabe la duración a cualquier otra sin volver a generar.

Y la consecuencia operativa, que es la que importa: **cambiar el `rate` después de la
fase 4 multiplica todos los tiempos del episodio por una constante**. Ningún ancla
sobrevive. Pasar `episodio01` de `+8%` a `-6%` mueve la última palabra **11,95 s**.

## Las ppm dependen del texto, no sólo de la voz

Las palabras por minuto **cuentan los silencios**. El mismo motor, la misma voz y el
mismo `rate` dan ritmos distintos según cómo esté puntuado el guion:

| Texto, todo a `-6%` | palabras | duración | ppm | callado |
|---|---|---|---|---|
| `ep01-lustig` (frases cortas, dos `···`) | 155 | 63,43 s | **147** | 28,1% |
| `episodio01` (cifras largas, más comas) | 201 | 92,18 s | **131** | 25,8% |

Un 11% de diferencia entre dos guiones del mismo canal. Por eso «147 ppm» sirve para
**dimensionar** un guion, no para cuadrarlo al segundo.

## Cronometrar el guion antes de grabarlo

El estimador que se usa parte de las sílabas y de las pausas que compra la puntuación
(los valores medidos están en § `282`):

```python
import re, sys
sys.path.insert(0, "piloto")
from tiempos import silabas

K = 0.1554                      # s/sílaba medidos a -6% sobre ep01-lustig
PAUSA = {".": 1.057, ",": 0.342, ";": 0.381, ":": 0.383,
         "?": 0.397, "!": 0.383, "…": 0.398, "»": 0.347}

def estimar(texto):
    t = re.sub(r"\.{2,}", ".", texto)                 # '....' es un punto
    return K * sum(silabas(w) for w in t.split()) + sum(PAUSA.get(c, 0) for c in t)
```

**Qué acierta y qué no, medido:**

| Texto | estimado | real | error |
|---|---|---|---|
| `ep01-lustig` a `-6%` (el de calibración) | 63,43 s | 63,43 s | 0,0% |
| `episodio01` a `-6%` | 88,79 s | 92,18 s | **−3,7%** |

⚠️ **±4% entre textos distintos.** En un episodio de diez minutos eso son ±24 segundos.
Sirve para saber si el bloque cabe en su hueco; **no** sirve para cuadrar al segundo.

Y hay un motivo para no perder tiempo afinando el estimador: **generar la locución
entera cuesta 1,4 s** (medido, dos pasadas sobre el minuto de `ep01-lustig`: 2,5 s la
primera, 1,4 s con la conexión ya caliente). Si necesitas el número exacto, no lo
estimes: genera.

## El presupuesto de palabras por bloque

Con 147 ppm, la aritmética del guion se hace sola:

| Bloque | objetivo | palabras |
|---|---|---|
| Gancho | 20-25 s | **50-60** |
| Promesa | 25-30 s | 60-75 |
| Bloque de desarrollo | 55-65 s | 135-160 |
| Remate | 15-20 s | 37-50 |
| **Episodio de 10 min** | 600 s | **≈1.470** |

Sobre el minuto real de `ep01-lustig`: 155 palabras para 63,45 s. El guion se escribe
contra esa tabla, no contra la sensación de que «va bien de largo».

## Cuándo se toca el `rate` y cuándo no

| Situación | Qué hacer |
|---|---|
| El bloque se pasa 3 s del hueco | **Cortar palabras.** Nunca acelerar |
| El episodio entero va corto de tensión | Se revisa el guion, no la velocidad |
| Un episodio pide un tono más grave y lento | Se decide **antes** de la fase 3 y se deja fijo para todo el canal |
| Las pistas de idiomas no cuadran con la mezcla | Ahí sí se estira, pero con `atempo` y sobre la pista, no con `rate` (§ `88`) |

La velocidad es **una decisión de canal**, no de episodio. Que el espectador reconozca
el ritmo entre episodios vale más que ganar tres segundos en uno.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Cambiar `rate` después de la fase 4 | Todos los tiempos se multiplican por una constante: fases 4-7 a la basura |
| Subir el `rate` para que el bloque quepa | Suena atropellado y las cifras dejan de retenerse |
| Usar 147 ppm como si fuera exacto para cualquier texto | ±11% entre guiones: el bloque se pasa o se queda corto |
| Fiarse del estimador al segundo | ±4% entre textos: son ±24 s en un episodio de diez minutos |
| Estimar en vez de generar | Generar cuesta 1,4 s y te da el número de verdad |
| Cambiar la velocidad de un episodio para otro | El canal deja de tener ritmo propio |
| Medir ppm sobre el texto sin contar los silencios | Casi un tercio del minuto es silencio: el número sale absurdo |

## Relacionado

`282` la puntuación como partitura · `284` una sola pasada · `288` cuando la voz sobra ·
`93` estructura de episodio · `95` escribir para el oído · `88` sonido por idioma ·
`10` densidad de eventos
