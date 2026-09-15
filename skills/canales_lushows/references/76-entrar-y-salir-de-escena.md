# 76 · Entrar y salir de escena

**Qué resuelve:** cómo abre y cómo cierra cada bloque del episodio. La transición ocurre
en la unión, pero lo que hace que la unión funcione está en los **0,6 s finales de una
escena y los 0,6 s iniciales de la siguiente**.

---

## La regla de los cuatro cuidados

Toda escena, lleve transición o no, se escribe así:

| # | Cuidado | Valor |
|---|---|---|
| 1 | El **fondo ya viene en movimiento** en el fotograma 0 | `zoompan` arranca en `on=0`, sin rampa |
| 2 | El **primer elemento entra** después del arranque | **0,30 a 0,60 s** |
| 3 | El **último elemento sale antes** del final | **0,20 a 0,40 s** |
| 4 | La **dirección del movimiento cambia** respecto a la escena anterior | `in` → `out` → `diag` |

El 2 y el 3 son los que casi nadie escribe y los que más se notan: una escena que empieza
con todo colocado se lee como lámina fija, y una que termina con tres elementos vivos
hace que el corte parezca un tijeretazo.

**Excepción única:** cuando la escena entrega a un **match cut** (`72`), el elemento que
sostiene la forma llega hasta el último fotograma con `fade_out: 0`.

## Cómo abre y cómo cierra cada bloque

| Bloque | Abre | Cierra |
|---|---|---|
| **Gancho** (0-12 s) | Imagen a fotograma 0, **sin fundido de entrada**, movimiento rápido y el primer dato en pantalla antes de 1,5 s | Corte duro seco sobre la promesa: "y aún faltaban catorce años" |
| **Contexto** | Fondo nuevo, elemento grande a 0,4 s | Cuadro limpio 0,3 s antes del corte |
| **Desarrollo** | Relevo: entra un elemento que continúa el anterior (`14`) | El elemento del relevo sobrevive al corte |
| **Giro** (cruza la raya) | Golpe de negro de 3 fotogramas (`74`) o tachado rojo (`77`) | Silencio de 0,4 s antes del corte |
| **Caída** | Ambiente ya cambiado 0,8 s antes (`75`) | Corte duro |
| **Remate** | Densidad a la baja: menos elementos, más aire (`18`) | Fundido a tinta de 0,80 s |

## El arranque del episodio: cero negro

> **El primer fotograma del vídeo es imagen, nunca negro.** Un fundido de entrada desde
> negro cuesta entre 0,4 y 0,8 s de la parte del vídeo donde más gente se va.

Se abre con la imagen ya montada y ya moviéndose. El único fundido admitido al principio
son **4 fotogramas desde tinta** (`0x12100C`) y sólo si la primera frase entra con un
golpe sonoro que lo justifique:

```
[v3]fade=t=in:st=0:d=0.16:color=0x12100C,format=yuv420p[out]
```

## El cierre del episodio

Los últimos 1,2 s son fijos y son marca:

| t (relativo al final) | Qué pasa |
|---|---|
| −1,20 s | Sale el último elemento de contenido |
| −1,00 s | Entra `marca/B_wordmark` centrado, ancho 900 px, con `fade` de 0,30 s |
| −0,90 s | Suena `tr_cierre` |
| −0,80 s | Empieza el fundido a tinta |
| 0,00 s | Negro `#12100C` pleno |

```
[v6]fade=t=out:st=DURFIN-0.80:d=0.80:color=0x12100C,format=yuv420p[out]
```

⚠️ El vídeo **no puede terminar en el fotograma del negro pleno**: se dejan **6
fotogramas (0,24 s)** de negro después, o los reproductores cortan el último cuadro y el
fundido se ve truncado.

## Las tres maneras de salir de una escena

| Salida | Cómo | Cuándo |
|---|---|---|
| **Limpia** | Todos los elementos con `fade_out` de 0,4 s; el corte cae sobre fondo solo | Por defecto, el 70% |
| **Por relevo** | Un elemento no sale: sigue vivo en la escena siguiente, en la misma posición y tamaño | Cuando dos escenas son el mismo tema (`14`) |
| **En pleno** | El cuadro está lleno en el fotograma del corte | Sólo con match cut (`72`) o con la unión tapada por un objeto (`71`, `73`) |

## Cómo se ve esto en la tabla de escenas

```python
{"id": "juicio", "ini": 63.4, "fin": 74.9, "fondo": "f_juzgado",
 "mov": ("out", 0.11),                       # la anterior era ("in", 0.13)
 "elementos": [
   {"r": "sala_recorte", "w": 1180, "x": 300, "y": 180,
    "desde": 0.42, "dura": 5.6, "fade_out": 0.4},        # cuidado 2
   {"r": "fx/sello_prueba", "w": 420, "x": 1180, "y": 620,
    "ancla": "condena", "dura": 3.9, "fade_out": 0.4},
   {"r": "cifra_26", "w": 700, "x": 520, "y": 700,
    "ancla": "veintiséis", "dura": 2.8, "fade_out": 0.4}]},
# el último elemento muere en 74.5 -> 0,4 s de cuadro limpio antes del corte (cuidado 3)
```

Comprobación rápida de que ninguna escena incumple el cuidado 3:

```python
for e in ESCENAS:
    fin = max((el.get("desde", 0) + el.get("dura", 2.0)) for el in e["elementos"])
    hueco = (e["fin"] - e["ini"]) - fin
    if hueco < 0.20:
        print(f"{e['id']}: cierra en pleno ({hueco:+.2f} s) — ¿es a propósito?")
```

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Abrir el episodio con fundido desde negro | Se regala el tramo de mayor abandono |
| Elemento entrando en el fotograma 0 de la escena | Se lee como lámina fija; parece que el vídeo se congeló |
| Cerrar todas las escenas en pleno | Cada corte parece un tijeretazo |
| Repetir la dirección del movimiento tres escenas seguidas | El ojo lo detecta y el episodio se vuelve monótono (`38`) |
| Terminar el vídeo justo en el negro | El reproductor corta el fundido |
| Sacar el elemento del match cut con `fade_out` | La forma desaparece antes del corte y el match cut no existe |

## Relacionado

`70` · `72` · `74` · `75` · `78` · `14` · `18` · `38`
