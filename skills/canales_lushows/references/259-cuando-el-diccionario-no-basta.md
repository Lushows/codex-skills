# 259 · Cuando el diccionario no basta

**Qué resuelve:** qué hacer cuando el generador deja de colocar. El síntoma siempre es el
mismo —huecos que no se tapan, cuadro escorado, elementos que se caen sin ruido— y la
reacción equivocada también: aflojar la ventana de los 25 s. **El fondo del cajón se
agota mucho antes que las ideas; lo que hay que mirar es el banco.**

---

## Los cuatro síntomas, y cómo se leen

`python auditar.py ep01-lustig` más el embudo del generador (`250`):

| Síntoma | Número en el minuto 1 | Qué significa de verdad |
|---|---|---|
| candidatas sin entrada en `V` | 101 de 155 | normal: son artículos y preposiciones |
| descartes por la ventana de 25 s | 10 | el vocabulario tiene pocas alternativas |
| descartes por no caber en ningún sitio | 15 | el cuadro está saturado, no falta material |
| contrapesos que vuelven vacíos | 2 de 18 | el cajón del bloque se está quedando corto |

Los dos primeros se arreglan escribiendo vocabulario. El tercero se arregla quitando, no
poniendo. El cuarto se arregla con material. Confundirlos es lo que lleva a tocar la
ventana, que es lo único que no hay que tocar.

## La reacción equivocada, cuantificada

| Ventana | Elem | Usos/recurso | Lo que se ve |
|---|---|---|---|
| 12 s | 63 | 1,17 | `casilla_nombre` a 12,9 s · `torre_postal` a 13,4 s · `columna_doble` a 13,8 s |
| 25 s | 61 | 1,11 | nada |

Dos elementos de ganancia a cambio de tres repeticiones visibles. En un canal cuyo
producto es la sensación de archivo abundante, ese cambio es ruinoso.

## Lo que hay debajo de la alfombra

Antes de tocar ningún umbral, el recuento del banco del propio episodio:

| Carpeta | Ficheros | Usados en el montaje | Sin tocar |
|---|---|---|---|
| `recortes/` | 70 | 36 | **34** |
| `fx/` | 25 | 15 | 10 |
| `texto/` | 17 | 7 | 10 |
| `archivo/` | 79 | 0 | **79** (fuentes sin recortar) |
| `render/` | 5 | 0 | 5 |

Treinta y cuatro recortes ya curados, recortados, con el alfa limpio y el borde de papel
puesto, esperando. Y setenta y nueve fuentes originales de las que salen los recortes.
Decir «no hay material» con esos números encima de la mesa es decir «no he mirado».

El recuento cuesta ocho líneas y conviene imprimirlo junto a la auditoría:

```python
import os, collections
usados = collections.defaultdict(set)
for e in ESCENAS:
    for x in e["elementos"]:
        r = diccionario.hallar(x["r"])
        if r:
            usados[os.path.basename(os.path.dirname(r))].add(x["r"])
for carp in ("recortes", "fx", "texto", "archivo", "render"):
    p = os.path.join(BASE, carp)
    if os.path.isdir(p):
        n = len([f for f in os.listdir(p) if f.lower().endswith((".png", ".jpg", ".webp"))])
        print("  %-9s %3d ficheros · %3d usados · %3d sin tocar"
              % (carp, n, len(usados[carp]), n - len(usados[carp])))
```

## La escalera, en orden

1. **Mirar el banco.** El recuento de arriba. Casi siempre acaba aquí.
2. **Ampliar el cajón del contrapeso** con piezas de ese bloque. De 3 a 5 piezas: de 6 a
   14 contrapesos colocados y de 3 huecos a 0 (`255`).
3. **Añadir alternativas al vocabulario**, no entradas nuevas: la palabra ya tiene imagen,
   lo que le falta es una segunda (`252`).
4. **Despiezar** una fuente ya curada en dos elementos que signifiquen cosas distintas
   —el certificado entero y la casilla del nombre— sin ponerlos seguidos (`191`).
5. **Escribir el plano a mano.** Si el hueco cae en el remate, merece una decisión humana,
   no un relleno.
6. **Volver al sondeo** y descargar más material para ese escenario (`190`, `191`).
7. **Reescribir el guion** para que ese tramo pida menos pantalla. Es la salida honesta
   cuando las seis anteriores fallan, y es mejor que rellenar con genérico.

Lo que no está en la escalera: bajar la ventana, repetir «porque casi no se nota», y
meter en `MOTIVOS` lo que no es motivo para que el auditor se calle (`254`).

## El caso del episodio 01

El tramo «según todo lo que se ha contado de él durante cien años» se quedó desnudo:
el antirrepetición no dejaba repetir y no había con qué rellenar. En el fichero de
vocabulario está escrito lo que se hizo, que es el resumen de este módulo:

```python
# Hay 69 recortes y solo se usaban 46, asi que no hacia falta repetir:
# hacia falta mirar el banco.
```

## Cuándo el problema es el guion, no el material

Hay un síntoma que no se arregla con imágenes: **descartes por sitio altos con cobertura
ya alta**. Quince descartes con 38% de cobertura significa que el cuadro está lleno, y
meter más elementos solo produce solapes. Ahí lo que sobra es densidad, no lo que falta
es material: el tramo pide respiración (`16`, `28`), no otra foto.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Bajar la ventana de 25 s | Tres repeticiones visibles por dos elementos |
| Decir «no hay material» sin contar el banco | 34 recortes curados sin usar |
| Añadir entradas nuevas cuando faltan alternativas | Más candidatas y los mismos descartes |
| Rellenar con genérico | El espectador nota que la imagen no significa nada |
| Meter en `MOTIVOS` lo que no vuelve a propósito | La métrica de repetición deja de servir |
| Tratar «no cabe» como «no hay» | Se mete material donde sobra densidad |

## Relacionado

`255` · `253` · `252` · `191` · `190` · `176` · `16`
