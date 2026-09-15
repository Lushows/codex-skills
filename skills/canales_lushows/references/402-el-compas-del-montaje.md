# 402 · El compás del montaje

**Qué resuelve:** cómo pedirle más ritmo a un episodio ya montado sin reescribir 276
duraciones a mano, y dónde está el muro que ningún parámetro salta.

---

## Qué es

Un factor único sobre la vida de cada elemento, declarado en el guion visual del episodio
y aplicable por minuto:

```python
COMPAS = getattr(_datos, "COMPAS", 0.83)    # guion_visual.py
diccionario.COMPAS = COMPAS                 # lo usa la capa AUTO
for e in clave:                             # y también la capa a mano
    e["dura"] = round(e["dura"] * COMPAS, 2)
```

**Entra la capa CLAVE también.** Dejarla fuera sería arreglar el 40% automático y
conservar el problema en el 60% escrito a mano. **No entra el contrapeso**: existe para
tapar un hueco, y un tapón más corto que el hueco no tapa nada.

## De dónde salió el 0,83 del episodio 1

Dos cosas que se multiplican, y conviene escribirlas separadas en el comentario:

| Factor | Por qué |
|---|---|
| 0,905 | el audio encogió eso al recomponer pausas (§ `400`). Sin esto el montaje se ralentiza solo |
| 0,92 | ritmo pedido: a 1,25× cada imagen duraba 2,5 s; a 1× duraba 3,2 |

## El efecto que no era obvio

Bajar el compás **sube los eventos por minuto**, no sólo baja la duración. Medido:

| Minuto | eventos/min antes | después | duración antes | después |
|---|---|---|---|---|
| 7 | 46,4 | **55,5** | 3,32 s | 2,49 s |
| 10 | 41,3 | **48,7** | 3,95 s | 2,95 s |

Elementos más cortos liberan sitio en el lienzo, y el colocador acepta candidatos que
antes rechazaba por choque. El motor se destapa solo.

## El muro: el banco, no el parámetro

Bajar el compás tiene un precio y llega rápido:

- **la simultaneidad cae** (de 2,15 a 1,84-1,94, con el suelo en 2,00);
- **la repetición sube**, porque las mismas piezas vuelven antes.

Y ahí está el muro de verdad. En el episodio 1, **ocho de los diez minutos pasan el tope
de repetición (1,25 usos por recurso) y seis repiten una pieza a menos de 25 s** — y eso
**ya pasaba antes de tocar el compás** (el minuto 3 estaba en 1,65 y subió a 1,73).

> El compás compra ritmo hasta que el banco se agota. Pasado ese punto no compra ritmo:
> compra repetición, que se ve peor que la lentitud.

Cuando el auditor marca repetición fuera de banda, **el arreglo no es un parámetro: es
material** (§ `403`).

## Cómo se ajusta

Por minuto, con el auditor delante, mirando cuatro números a la vez: eventos/min,
simultaneidad, duración media y repetición. Bajar el compás sólo mientras los cuatro
aguanten. Un minuto de cierre puede querer respirar donde el gancho aprieta — por eso se
declara por minuto y no sólo por episodio.

## Relacionado

§ `10` (densidad de eventos) · § `15` (rampa de ritmo) · § `400` (el silencio) · § `401`
(el reloj) · § `403` (cuántas piezas pide un episodio) · § `246` (equilibrio del cuadro)
