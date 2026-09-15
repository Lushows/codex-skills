# 273 · Marcar lo no verificado sin aburrir

**Qué resuelve:** el método se puede aplicar tanto que se rompa. Un sello `SIN FUENTE`
cada cinco segundos deja de significar a la tercera vez, y el episodio pasa de documental
a descargo de responsabilidad. Este módulo es el presupuesto de marcas y la regla que
decide cuándo **no** marcar.

---

## El principio: la columna es un territorio, no una etiqueta

Una marca no califica una frase. Califica **todo lo que viene detrás hasta la siguiente
marca**. El espectador asume continuidad sin que nadie se lo explique: es lo mismo que
hace con un rótulo de lugar en una película.

De ahí la regla que ahorra la mitad de las marcas:

> **Una marca por cambio de terreno. Nunca una marca por afirmación.**

En el minuto 1 hay **cuatro afirmaciones no probadas** —la venta, el chatarrero que no
denuncia, la segunda venta y lo de que «aprendiz» es una broma— y **una sola** marca de
columna las cubre casi todas.

## El presupuesto, medido

Sobre los 59 elementos y 63,45 s del minuto 1:

| Familia | Piezas | Tiempo en pantalla | % del tramo |
|---|---|---|---|
| Marcas `CONSTA` (`m_consta`, `sello_consta`) | 4 | 9,37 s | 14,8% |
| Marcas `SE CUENTA` (`m_cuenta`, `r_sinfuente`) | 3 | 7,32 s | 11,5% |
| **Total de marcas de columna** | **7 de 59** | 16,69 s | **26,3%** |

Añadiendo la cronología (`linea_00`, `linea_02`, `linea_06`) y la balanza del cierre, las
piezas que hablan del método son **11 de 59: el 18,6% de los elementos**. Ese es el techo
razonable. Por encima del 25% el episodio habla más de sí mismo que de su historia.

## Tres intensidades, y cuándo usa cada una

| Intensidad | Pieza | Cuándo entra | Cuántas por minuto |
|---|---|---|---|
| **Terreno** | `m_consta` / `m_cuenta` | al cambiar de columna | 1 por cambio, máx. 3 |
| **Remate de frase** | `sello_consta` (VERIFICADO) / `sello_falta` (SIN FUENTE) | sobre el golpe de una frase concreta | 2, nunca seguidos |
| **Denuncia explícita** | `r_sinfuente`, `linea_06` en rojo | una vez, en el remate de la leyenda | **1** |

El rojo es el recurso escaso del sistema. En el piloto se usa una vez: `r_sinfuente` a
los 48,74 s, justo después de «y la vendió otra vez», que es el punto más alto de la
leyenda. Poner el rojo antes sería desactivarlo; ponerlo dos veces, mobiliario.

## Marcar sin repetir: el contador que avanza

La forma más barata de recordar el método sin volver a poner la misma imagen es que la
imagen **cambie de estado**. El auditor cuenta estados sucesivos como un solo evento
(umbral de gesto, § `254`), así que no penaliza:

- **La balanza**: `balanza_00 … balanza_05`, con el pie `AFIRMACIONES SIN FUENTE
  PRIMARIA · n DE 5`, que pasa de gris a rojo en cuanto n deja de ser cero.
- **La cronología**: siete estados, un hito cada vez, y el último marcando en rojo lo que
  no consta.

El espectador ve el método avanzar, no repetirse. Es la diferencia entre un estribillo y
un contador de daños.

## Cuándo NO se marca

| Situación | Por qué no |
|---|---|
| La voz acaba de decir la fórmula completa | Subrayar lo subrayado: dos avisos para un dato |
| El plano ya es el documento a pantalla completa | El documento se califica solo |
| Dos afirmaciones de la misma columna seguidas | Sigue el mismo terreno |
| Un tramo de puro contexto (época, ciudad, oficio) | No afirma nada sobre el caso |
| El bloque de descanso | Marcar un respiro lo convierte en argumento |

## La comprobación que hay que ejecutar

El guion se lee por territorios, no por frases. `atribucion.py` corta el tramo por las
marcas de columna, imprime lo que dice la voz dentro de cada territorio y avisa si un
territorio de leyenda no contiene ninguna fórmula:

```python
FORMULAS = ("pone que", "consta", "según", "la versión", "dice que", "se ha contado",
            "han repetido", "se le atribuye", "no hemos encontrado")
COL = {"m_consta": "CONSTA", "sello_consta": "CONSTA",
       "m_cuenta": "CUENTA", "sello_falta": "CUENTA", "r_sinfuente": "CUENTA"}
# ... resolver cada marca contra la locucion y cortar el tramo por sus tiempos
marcas = sorted((resolver(e, el), COL[el["r"]], el["r"])
                for e in gv.ESCENAS for el in e["elementos"] if el["r"] in COL)
for i, (t, col, r) in enumerate(marcas):
    hasta = marcas[i + 1][0] if i + 1 < len(marcas) else fin
    dicho = " ".join(p["w"] for p in PAL if t <= p["t"] < hasta)
    if col == "CUENTA" and not any(f in dicho.lower() for f in FORMULAS):
        print("   <-- SIN FORMULA EN LA VOZ")
```

Salida real sobre el piloto:

```
  0.60- 17.94  CONSTA m_consta      de marzo de mil novecientos cuarenta y siete, en un hospital...
 17.94- 34.58  CONSTA sello_consta  alguien escribió a máquina dos palabras:... aprendiz de vendedor...
 34.58- 48.74  CUENTA m_cuenta      la versión que ha llegado hasta hoy dice que ese hombre...
 48.74- 58.15  CUENTA r_sinfuente   vez. Esa es la historia. La han repetido libros, periódicos...
 58.15- 60.68  CONSTA sello_consta  cosa que casi nadie hace con ella: separar
 60.68- 63.45  CUENTA m_cuenta      lo que se cuenta de lo que consta.
```

### Lo que encontró, que no es poco

Dos hallazgos reales del piloto, los dos invisibles leyendo el guion:

1. **El territorio 17,94 - 34,58 está marcado `CONSTA` y contiene una afirmación de
   leyenda.** A los 28,52 s la voz dice *«y lo de aprendiz, según todo lo que se ha
   contado de él durante cien años, es directamente una broma»*. La fórmula está en la
   voz —y es correcta—, pero la marca visible sigue siendo la del documento. La columna
   visual y la voz **discrepan durante 3,31 s**. No es un error factual; es un desajuste
   de terreno, y el arreglo es barato: adelantar `m_cuenta` a «según» o adelantar el
   corte de bloque. Se apunta porque **este es exactamente el hueco que el método promete
   no tener**.
2. **El plano del cierre rompe el modelo a propósito.** A los 60,68 s entran las dos
   marcas a la vez, una a cada lado. El script las lee como dos territorios consecutivos
   y produce uno de duración cero. No es un fallo del episodio: es el límite de la
   herramienta, y conviene saberlo antes de creerse su salida.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Una marca por afirmación | A la cuarta el espectador deja de leerlas |
| Gastar el rojo antes del remate | Cuando llega el momento fuerte no queda nada que subir |
| Marcar y además decir la fórmula en la misma frase | Dos avisos para un dato: suena a miedo |
| Repetir la misma marca en vez de avanzar un estado | El auditor lo cuenta como repetición y tiene razón |
| Creer que la marca dura solo lo que dura en pantalla | Se remarca lo que ya estaba marcado |
| Fiarse de la salida del script sin mirar sus límites | El plano de las dos marcas da un territorio vacío |
| No comprobar territorio contra voz | La columna dice una cosa y la locución otra, 3,31 s |

## Relacionado

`270` el método · `271` las dos columnas en pantalla · `272` fórmulas de atribución ·
`254` motivos · `143` la alarma en falso · `147` cuándo una métrica deja de servir ·
`16` el plano de descanso · `43` rótulos y etiquetas
