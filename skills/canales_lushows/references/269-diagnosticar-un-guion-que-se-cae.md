# 269 · Diagnosticar un guion que se cae

**Qué resuelve:** saber que un episodio largo no se sostiene **antes** de grabar la
voz. Después ya no es un problema de guion: es rehacer voz, tiempos y guion visual de
cada tramo tocado, y tres horas de render.

Las siete pruebas de abajo se hacen sobre el guion en texto, en una sesión de media
hora, y todas tienen criterio de fallo. No son opiniones sobre si «engancha».

---

## Cuándo se hace

Al terminar la fase 2 (guion) de cada tramo y, **entero**, cuando el mapa de los doce
minutos está escrito y antes de escribir el minuto 2. El orden de trabajo de la skill
no admite atajos: una frase que cambia después de la fase 3 arrastra las fases 4 a 7.

| Dónde se descubre el fallo | Lo que cuesta arreglarlo |
|---|---|
| En el mapa (12 líneas) | Reescribir una línea |
| En el guion en texto | Reescribir un párrafo |
| Con la voz grabada | Regrabar + realinear tiempos + rehacer el guion visual del tramo |
| Con el episodio montado | Lo anterior, más el render, más la mezcla del episodio entero |

## Las siete pruebas

### 1 · La prueba del índice

Escribir **una línea por minuto** con el hecho nuclear, y leerlas seguidas.

- ❌ Dos líneas dicen lo mismo con otras palabras → sobra un tramo, se funden.
- ❌ Una línea necesita un «y además» → son dos tramos, el mapa está mal repartido.
- ❌ Una línea es un tema, no un hecho («la vida en Alcatraz») → falta investigación.

### 2 · La pila de bucles

La tabla de `262`: ID, pregunta, minuto en que abre, minuto en que cierra.

- ❌ Cualquier fila con la columna «cierra» vacía.
- ❌ Más de tres bucles vivos en el mismo minuto.
- ❌ El bucle maestro cierra antes del penúltimo tramo.

### 3 · Los noventa segundos

Marcar en el guion cada reenganche y medir la distancia entre consecutivos.

- ❌ Más de **105 s** entre dos → hay un agujero; ahí se irá la gente.
- ❌ Menos de siete en doce minutos, o más de doce.
- ❌ Dos del mismo tipo seguidos (`261`).

### 4 · La prueba de la columna

Pintar los doce minutos con **C** (consta) y **L** (se cuenta). El arco propuesto en
`260` da:

```
min  1  2  3  4  5  6  7  8  9 10 11 12
     C  C  L  L  L  L  C  C  C  C  C  C
              ^^^^^^^^^^
              cuatro L seguidas: el punto a vigilar
```

- ❌ Cuatro o más tramos seguidos de la misma columna sin ningún asomo de la otra
  (`264`, los dos asomos).
- ❌ Un tramo en el que la columna **no se puede decidir** → falta hoja de hechos.
- 🔴 Un tramo marcado C cuyo dato no está en `hechos.md` con su documento y su
  casilla. Esto no es un defecto de ritmo: es el error que mata el canal (`96`).

### 5 · El cronómetro

Dos números, medidos sobre el minuto 1 ya grabado, y no son el mismo:

| Medida | Valor | Para qué sirve |
|---|---|---|
| Palabras **alineadas** en `tiempos.json` / duración | 155 en 63,454 s = **146,6 ppm** | Es el ritmo real de esta voz con esta puntuación |
| Palabras **contadas sobre el texto** del guion / duración | 163 en 63,454 s = **154 ppm** | Es lo que hay que usar para estimar antes de grabar |

La diferencia (8 palabras, un 5%) es lo que el alineado junta o el texto arrastra. Si
se estima con 146,6 sobre el markdown, cada tramo sale un 5% más largo de lo que será.

- ❌ Un tramo de más de **175 palabras** no dura sesenta segundos: pasa de setenta.
  Doce tramos así son dos minutos y medio de más.
- ❌ Un tramo de menos de 125 palabras se queda corto y arrastra al siguiente.

Se mide con un script, no a ojo (probado sobre `guion.md`: da 57, 72 y 34 palabras
para los tres bloques del minuto 1):

```python
# palabras por seccion y duracion estimada. 154 ppm = el texto del ep01 contado
# asi, sobre la locucion real ya aprobada.
import io, re, sys
PPM = 154.0
txt = io.open(sys.argv[1], encoding="utf-8").read()
tramo, cuenta = "(cabecera)", {}
for l in txt.splitlines():
    if l.startswith("#"):
        tramo = l.lstrip("#").strip(); cuenta.setdefault(tramo, 0); continue
    # OJO: descartar SOLO vinetas reales. Una linea que empieza por **negrita**
    # tambien empieza por '*' y por ese filtro se han perdido frases enteras.
    if re.match(r"^(\-|\*|\+)\s", l) or l.startswith("|") or l.startswith(">"):
        continue
    limpio = re.sub(r"[*`_]|···", " ", l)
    cuenta[tramo] = cuenta.get(tramo, 0) + len(limpio.split())
for t, n in cuenta.items():
    if n:
        print("%-44s %4d palabras  ~%5.1f s" % (t[:44], n, n / PPM * 60))
```

Las secciones de control del guion (la tabla de datos, las notas para el guion visual)
salen como filas aparte y se ignoran: lo que se mira son los bloques.

### 6 · La prueba de la imagen

Cada tramo con su columna «qué se ve», cotejada contra `recortes/` y `archivo/`.

- ❌ Un tramo sin material propio → se replantea ahora, no en la fase 6.
- ❌ Un tramo que se apoya en una sola pieza durante sesenta segundos.
- ❌ Una pieza que ya se ha usado en un tramo vecino y no es motivo (`253`, `254`).

### 7 · La lectura seguida de dos tramos

Leer en voz alta el final de un tramo y el principio del siguiente, sin pausa.

- ❌ Hay que explicar dónde estamos → falta la frase de enlace.
- ❌ Las dos frases repiten el mismo sustantivo → costurón audible.
- ❌ Se puede quitar el final del primero y no se nota → ese reenganche no existe.

## Los síntomas y su causa real

Lo que se dice al ver un episodio flojo casi nunca nombra el problema:

| Lo que se siente | Lo que de verdad pasa | Dónde se arregla |
|---|---|---|
| «Se hace largo por la mitad» | El acto II no tiene motor: los tramos no suben la apuesta | `264` |
| «No me acuerdo de qué iba» | Bucle maestro abierto seis minutos sin recordatorio | `262` |
| «El final no remata» | El dato guardado se gastó antes, o no había ninguno | `266`, `267` |
| «Parece que se ha ido por las ramas» | Digresión sin frase de entrada ni de vuelta | `265` |
| «Suena a lista de datos» | Tramos con dos hechos nucleares cada uno | `98` |
| «Es bueno pero no me lo creo» | Demasiados tramos seguidos en la columna de la leyenda | `264`, `96` |
| «Se acaba de golpe» | Falta la bisagra corta antes del último tramo | `267` |
| «Sobra el minuto 4» | Es una digresión que no hace falta para creer el 5 | `265` |

## Cuándo se tira un tramo, y cuándo el episodio

- **Se tira un tramo** cuando no abre ni cierra ningún bucle, no aporta hecho nuevo y
  no sube la apuesta. Diez minutos sólidos rinden más que doce con dos de relleno.
- **Se replantea el episodio** cuando la prueba de la columna sale **L en más del 60%**
  y no hay ningún documento pendiente que pueda cambiarlo. Ahí el problema no es el
  guion: es que el caso no se puede sostener con papeles y hay que devolverlo al banco
  de historias (`97`) o declararlo inviable (`176`).

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Diagnosticar «a ojo» leyendo el guion entero de un tirón | Se detecta que algo falla, nunca qué |
| Saltarse las pruebas porque el tramo «se lee bien» | Un tramo puede leerse bien y estar en el sitio equivocado del arco |
| Hacer el diagnóstico con la voz ya grabada | Cada arreglo cuesta voz + tiempos + guion visual del tramo |
| Contar palabras a ojo | 165 y 210 palabras se parecen en el papel y son 25 s de diferencia |
| Filtrar las líneas del guion por «empieza por `*`» | Se pierden las frases que arrancan en negrita: ya pasó |
| Arreglar un síntoma de ritmo acelerando el montaje | Si el problema es estructural, el montaje rápido sólo lo hace ruidoso |
| Aprobar un tramo marcado `consta` sin su fila en `hechos.md` | Es el único fallo de esta lista que no se arregla después de publicar |

## Relacionado

`260` el arco de doce minutos · `261` reenganchar cada noventa segundos · `262` el
bucle dentro del bucle · `264` el segundo acto · `265` la digresión que suma ·
`266` el dato que se guarda · `98` episodios largos · `95` escribir para el oído ·
`96` verificación de datos · `97` banco de historias · `176` cuándo un caso no se
puede ilustrar
