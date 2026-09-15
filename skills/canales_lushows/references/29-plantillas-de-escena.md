# 29 · Plantillas de escena

**Qué resuelve:** empezar cada escena desde cero. Doce disposiciones cuadradas contra la retícula de `20`, listas para pegar en la tabla de eventos.

---

Traen `x`, `y`, `w` y `rot`; `ancla`, `offset` y `dura` dependen del guion. El orden de
la lista es el orden de capas (`26`). Aplicar el desvío de `20` al pegarlas, para que
dos escenas con la misma plantilla no salgan calcadas.

## 1 · FICHA — presentar a alguien

```python
{"r": "retrato", "x": "W*0.194-w/2", "y": "H*0.5-h/2", "w": 640, "rot": -1.6, "entrada": "izq"},
{"r": "nombre",  "x": "W*0.56",      "y": "H*0.30",    "w": 700, "rot":  1.2, "entrada": "der"},
{"r": "ficha",   "x": "W*0.56",      "y": "H*0.46",    "w": 620, "rot": -0.9, "entrada": "fade"},
```

## 2 · GOLPE DE CIFRA — la cantidad del episodio

```python
{"r": "obj_izq", "x": "W*0.05",   "y": "H*0.12",     "w": 480, "rot":  2.6, "entrada": "izq"},
{"r": "obj_der", "x": "W*0.62",   "y": "H*0.64",     "w": 520, "rot": -2.2, "entrada": "der"},
{"r": "cifra",   "x": "W*0.5-w/2","y": "H*0.5-h/2",  "w": 980, "rot": -1.3, "entrada": "fade"},
```
Fondo con `mov: ("golpe", 0.26)`. El bloque de dato completo, en `27`.

## 3 · TRÍPTICO — tres cosas del mismo tipo

```python
{"r": "a", "x": "W*0.194-w/2", "y": "H*0.5-h/2", "w": 500, "rot": -2.1, "entrada": "izq",   "deriva": (6, -3)},
{"r": "b", "x": "W*0.5-w/2",   "y": "H*0.5-h/2", "w": 500, "rot":  1.8, "entrada": "abajo", "deriva": (6, -3)},
{"r": "c", "x": "W*0.806-w/2", "y": "H*0.5-h/2", "w": 500, "rot": -1.5, "entrada": "der",   "deriva": (6, -3)},
```
Misma `deriva` = un grupo (`24`); entran escalonados 0,25 s.

## 4 · DOCUMENTO CENTRAL — una prueba

```python
{"r": "documento", "x": "W*0.5-w/2", "y": "H*0.46-h/2", "w": 1180, "rot": -2.4, "entrada": "fade"},
{"r": "sello",     "x": "W*0.62",    "y": "H*0.58",     "w": 420,  "rot":  6.8, "entrada": "fade"},
{"r": "fuente",    "x": "W*0.10",    "y": "H*0.84",     "w": 380,  "rot": -0.7, "entrada": "izq"},
```
El sello entra 0,6 s tras el documento, con ángulo fuerte (6-9°): es un golpe.

## 5 · COMPARACIÓN DE ESCALA — hacer imaginable una cifra

```python
{"r": "conocido",   "x": "W*0.194-w/2", "y": "H*0.44-h/2", "w": 420, "rot": -1.4, "entrada": "izq"},
{"r": "comparado",  "x": "W*0.653-w/2", "y": "H*0.44-h/2", "w": 900, "rot":  1.1, "entrada": "der"},
{"r": "pie_escala", "x": "W*0.10",      "y": "H*0.80",     "w": 760, "rot": -0.8, "entrada": "fade"},
```
Comparten la **base**, no el centro: eso hace legible la escala. El `rot` alterna signo.

## 6 · MAPA Y RUTA — geografía

```python
{"r": "mapa",      "x": "W*0.5-w/2", "y": "H*0.5-h/2", "w": 1560, "rot": -1.1, "entrada": "fade"},
{"r": "chincheta", "x": "W*0.36",    "y": "H*0.38",    "w": 120,  "rot":  3.4, "entrada": "abajo"},
{"r": "rotulo",    "x": "W*0.40",    "y": "H*0.30",    "w": 380,  "rot": -1.0, "entrada": "fade"},
```
El mapa, en plano medio (`22`); chinchetas y rótulos, en frente nítido.

## 7 · TABLERO — el corcho de investigación

```python
{"r": "p1", "x": "W*0.08", "y": "H*0.14", "w": 380, "rot": -3.1, "entrada": "fade", "deriva": (3, 2)},
{"r": "p2", "x": "W*0.40", "y": "H*0.10", "w": 340, "rot":  2.4, "entrada": "fade", "deriva": (3, 2)},
{"r": "p3", "x": "W*0.70", "y": "H*0.20", "w": 400, "rot": -1.8, "entrada": "fade", "deriva": (3, 2)},
{"r": "p4", "x": "W*0.20", "y": "H*0.54", "w": 360, "rot":  2.9, "entrada": "fade", "deriva": (3, 2)},
{"r": "p5", "x": "W*0.58", "y": "H*0.58", "w": 420, "rot": -2.2, "entrada": "fade", "deriva": (3, 2)},
```
Cinco entradas de 0,18 s en cascada. Ocupación ~70%: lo más cargado que admite el canal (`28`).

## 8 · TITULARES APILADOS — la prensa reacciona

```python
{"r": "tit1", "x": "W*0.10", "y": "H*0.16", "w": 880, "rot": -2.8, "entrada": "izq"},
{"r": "tit2", "x": "W*0.22", "y": "H*0.38", "w": 900, "rot":  1.9, "entrada": "der"},
{"r": "tit3", "x": "W*0.14", "y": "H*0.60", "w": 860, "rot": -1.4, "entrada": "abajo"},
```
Solape del 15-20% (`26`); cada uno entra 0,4 s tras el anterior.

## 9 · DIAGONAL — progresión o caída

```python
{"r": "a", "x": "W*0.194-w/2", "y": "H*0.219-h/2", "w": 440, "rot": -1.7, "entrada": "arriba"},
{"r": "b", "x": "W*0.5-w/2",   "y": "H*0.5-h/2",   "w": 500, "rot":  2.1, "entrada": "fade"},
{"r": "c", "x": "W*0.806-w/2", "y": "H*0.781-h/2", "w": 560, "rot": -2.5, "entrada": "abajo"},
```
Tamaño creciente: una diagonal que baja y crece se lee como algo que se agrava.

## 10 · RETRATO Y CONTEXTO — quién, y dónde

```python
{"r": "escena",  "x": "W*0.347-w/2", "y": "H*0.5-h/2", "w": 780, "rot":  1.6, "entrada": "izq", "deriva": (4, 0)},
{"r": "retrato", "x": "W*0.72",      "y": "H*0.22",    "w": 660, "rot": -2.0, "entrada": "der", "deriva": (11, -4)},
```
La escena en plano medio (σ 2,4 · sat 0,83); el retrato en frente. Derivas 1 : 2,7.

## 11 · CADENA DE PASOS — cómo funcionaba el mecanismo

```python
{"r": "paso1",  "x": "W*0.05", "y": "H*0.52", "w": 340, "rot": -1.5, "entrada": "izq"},
{"r": "flecha", "x": "W*0.27", "y": "H*0.60", "w": 110, "rot":  0.6, "entrada": "fade"},
{"r": "paso2",  "x": "W*0.34", "y": "H*0.52", "w": 340, "rot":  1.9, "entrada": "izq"},
{"r": "paso3",  "x": "W*0.63", "y": "H*0.52", "w": 340, "rot": -2.2, "entrada": "izq"},
```
Se construye de izquierda a derecha al ritmo de la voz; cada paso lleva rótulo (`43`).

## 12 · REMATE — la revelación

```python
{"r": "final", "x": "W*0.5-w/2", "y": "H*0.5-h/2", "w": 720, "rot": -1.2, "entrada": "fade", "deriva": (0, 3)},
```
Un elemento, ocupación bajo el 30%, `mov: ("out", 0.09)`: el vacío es el contenido (`28`).

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Repetir la misma plantilla en escenas seguidas | Se nota el molde |
| Copiarla sin aplicar el desvío de `20` | Dos escenas idénticas al píxel |
| Usar el TABLERO más de una vez por episodio | Pierde el efecto de acumulación |
| REMATE con dos elementos | Deja de ser remate: es una escena más |

## Relacionado

`20` retícula del collage · `24` agrupar y separar · `26` superposición y oclusión ·
`28` respiración del cuadro · `27` composición de datos
