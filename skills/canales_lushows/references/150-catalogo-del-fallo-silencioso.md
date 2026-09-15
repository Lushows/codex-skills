# 150 · El catálogo del fallo silencioso

**Qué resuelve:** la familia de errores que **no lanza excepción, no devuelve código
distinto de cero y no deja rastro en el log** — y que por eso llega al vídeo publicado.

---

## Cómo se manifiesta

Los nueve fallos de este bloque ocurrieron de verdad en *Paper Empires*. Ninguno dio
error. Todos tienen la misma firma:

```
$ python fondos.py
6 HTML escritos. Renderizando a 4320x2430...
OK    f_gancho     10.4 MB
OK    f_pregunta    9.8 MB
...
$ echo $?
0
```

Proceso terminado, archivos en disco, pesos normales. Y cinco de los seis fondos
tenían bloques blancos planos dentro.

**La firma común, en tres partes:**

1. **El programa termina bien.** Código 0. No hay `try` que se coma nada: es que no
   hubo nada que coger.
2. **El artefacto existe y parece sano.** El PNG pesa sus 10 MB, el MP4 dura lo que
   debe, el JSON tiene sus 277 entradas.
3. **El contenido está mal.** Y sólo se ve mirando el píxel, la posición o el
   segundo — nunca el nombre, el tamaño o el número de elementos.

## Por qué ocurre

Porque el pipeline está hecho de **piezas que no se deben nada**. Chrome no sabe qué
va a hacer ffmpeg con el PNG; ffmpeg no sabe si el índice `4:v` era el que pedía el
guion; el auditor no sabe si el recurso que puntúa existe. Cada pieza cumple su
contrato pequeño —«escribo un PNG», «monto los índices que me des»— y el contrato
grande —«el episodio dice lo que el guion dice»— no lo firma nadie.

De ahí las cuatro causas raíz que se repiten en los nueve casos:

| Causa | Caso real | Módulo |
|---|---|---|
| **El artefacto miente sobre su contenido** | PNG de 10 MB con un bloque en blanco | `151` |
| **Un filtro más estricto de lo que cree** | `.jpg` exigido con `?utm_source=` detrás → 0 de 277 | `152` |
| **Un índice o un nombre que se desacopla** | `enumerate()` frente a las entradas reales de ffmpeg | `153` `155` |
| **Un valor por defecto que absorbe el fallo** | ancla que no casa → cae al defecto sin avisar | `154` `156` |

La cuarta es la peor, porque es **deliberada**: el `defecto=0.0`, el `return 0.0`, el
`except Exception: pass` se escribieron para que el programa no se cayera. Lo
consiguieron. El programa no se cae y el episodio sale mal.

## Cómo se reconoce esta familia

Tres preguntas. Si alguna da *no*, hay fallo silencioso posible:

1. **¿Qué comprueba el programa además de que el archivo exista?** Si la respuesta es
   «el peso», no comprueba nada: en `151` un rectángulo blanco opaco de 10 KB pasa
   cualquier filtro de «pesa más de 5 KB».
2. **¿Qué pasa si la búsqueda no encuentra nada?** Si devuelve un valor por defecto en
   vez de abortar, el fallo ya está escondido.
3. **¿Se puede desincronizar lo que cuento de lo que uso?** Índices de bucle contra
   índices de ffmpeg, nombres de archivo contra rutas completas, alias del guion
   contra ficheros en disco.

## La guardia automática

La forma canónica de este bloque: **medir el contenido, compararlo con un umbral y
reintentar** — nunca ajustar parámetros y volver a mirar.

```python
def verificar_y_reintentar(producir, medir, umbral, nombre, intentos=3):
    """producir() genera el artefacto; medir() devuelve un número del CONTENIDO.
    Ni uno solo de los nueve fallos se habría colado con este bucle puesto."""
    for intento in range(1, intentos + 1):
        producir()
        valor = medir()
        if valor <= umbral:
            return valor
        print(f"      reintento {intento}: {nombre} mide {valor} (tope {umbral})")
    raise SystemExit(f"ABORTADO: {nombre} no pasó en {intentos} intentos")
```

Tres condiciones, y las tres son obligatorias:

- **`medir()` mira el contenido**, no el continente. Píxeles casi blancos, desviación
  del gris dentro del alfa opaco, fecha de modificación posterior al intento.
- **Reintentar, no reparametrizar.** El fallo de `151` no es determinista: el mismo
  fondo en solitario sale limpio. Bajar la resolución «por si acaso» no arregla nada
  y tapa la medida.
- **Aborta al final.** `motor.py` lo hace explícito: si falla una escena, no concatena
  las demás, porque el episodio quedaría desincronizado de la voz desde ahí hasta el
  final. Un pipeline que sigue con material sospechoso es un pipeline sin guardia.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Comprobar que el archivo existe | El PNG de la pasada anterior lo aprueba todo (`151`) |
| Comprobar sólo el peso | Un rectángulo blanco opaco pesa 10 KB y pasa |
| `except Exception: pass` para «que no se caiga» | Se cae igual, tres fases más tarde y sin pista |
| Valor por defecto en vez de aborto | El efecto suena 7,3 s antes y nadie se entera (`154`) |
| Ajustar parámetros ante un fallo intermitente | Se pierde la medida y el fallo vuelve en el render siguiente |
| Arreglar sin reproducir primero | Se «arregla» lo que no era (`159`) |

## Relacionado

`140` medir antes de renderizar · `142` la medida que miente · `143` una comprobación
que grita en falso se ignora · `151`–`158` los nueve casos · `159` cómo se caza un
fallo que no avisa · `168` reproducir antes de afirmar
