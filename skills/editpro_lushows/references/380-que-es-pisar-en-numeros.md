# 380 — Qué es pisar, en números

**Qué resuelve:** «este elemento tapa al otro» es una frase; no se puede ordenar, ni comparar entre dos
versiones, ni comprobar antes de renderizar. Este bloque (`380`–`389`) convierte la pisada en cinco
números. Todo lo que sigue está medido sobre el motor real del canal documental, en
`CANALES-LUSHOWS\piloto`, con `auditar.py` y `diccionario.py` ejecutados hoy.

> **Frontera.** `directorcreativo_lushows` decide el look. `canales_lushows/26` da la versión
> **prescriptiva** de la oclusión: cuánto solape queda bien, quién debe tapar a quién, qué cuenta cada
> disposición. **Este bloque es la versión medida:** el número, el script y el umbral. Y `204` §3.5 tiene
> la oclusión como recurso de composición. Nada de eso se repite aquí.

---

## 1. La pisada, definida para que se pueda contar

Una **pisada** es una pareja de elementos que cumple las dos condiciones a la vez:

1. **Coinciden en el sitio** — sus rectángulos se cortan.
2. **Coinciden en el tiempo** — sus vidas se solapan aunque sea una décima.

Las dos, o no es nada. Dos elementos que se solapan al 60% pero nunca están en pantalla a la vez no son un
problema: son dos elementos que comparten sitio en momentos distintos, que es justo lo que se quiere.

De cada pisada salen cinco datos, y ninguno sobra:

| Dato | Qué contesta | De dónde sale |
|---|---|---|
| **quién está debajo** | a quién se le hace el daño | orden de capa (§2) |
| **quién está encima** | quién lo hace | orden de capa (§2) |
| **cuánto** | fracción del de abajo que queda cubierta | `pisa(a, b)` |
| **cuánto tiempo** | segundos de coincidencia | vidas resueltas |
| **qué era lo tapado** | foto, rótulo, cifra, cara | clase del recurso (`381`, `383`) |

El quinto es el que casi nadie mide y el que decide (`381`).

---

## 2. Quién está encima: el orden de lista, no el reloj

Este es el primer error de bulto y hay que matarlo antes de medir nada. `motor.py` encadena los overlays
recorriendo la lista de elementos:

```python
for ele in esc.get("elementos", []):
    ...
    filtros.append(f"[{ultimo}][e{n}]overlay=x='{x}':y='{y}':"
                   f"enable='between(t,{e0:.2f},{e1:.2f})'[v{n}]")
    ultimo = f"v{n}"
```

**El último de la lista queda encima. No hay campo de capa: el orden ES la capa.** Y el orden de la lista
no tiene por qué coincidir con el orden temporal: un elemento declarado antes puede entrar después.

Medido hoy sobre las dos versiones del episodio 01, contando cuántas parejas simultáneas tienen el orden
de capa distinto del orden de entrada:

| Episodio | Parejas simultáneas | Discrepan capa vs. tiempo |
|---|---|---|
| `ep01-lustig` | 96 | **30 (31%)** |
| `episodio01` | 93 | **27 (29%)** |

Una de cada tres. Un medidor que ordene por tiempo está mirando en la dirección equivocada en un tercio de
los casos: mide cuánto tapa el de abajo al de arriba, que es un número que no significa nada.

---

## 3. `pisa(a, b)` no es simétrica

La función real, en `diccionario.py:365`:

```python
def pisa(a, b):
    """Cuanto del rectangulo 'a' queda debajo de 'b', en tanto por uno."""
    if a is None or b is None:
        return 0.0
    sx = max(0.0, min(a[2], b[2]) - max(a[0], b[0]))
    sy = max(0.0, min(a[3], b[3]) - max(a[1], b[1]))
    propia = (a[2] - a[0]) * (a[3] - a[1])
    return (sx * sy / propia) if propia > 0 else 0.0
```

La superficie cortada es la misma en los dos sentidos; lo que cambia es **entre qué se divide**. Un
ejemplo real de `ep01-lustig`, bloque «torre»:

| | `torre_citroen_noche` (1000 px) | `r_sinfuente` (720 px, rótulo) |
|---|---|---|
| cuánto queda debajo del otro | **11,2%** | **46,7%** |

El mismo corte de píxeles. Un plano grande al que le muerden una esquina, y un rótulo al que le borran casi
la mitad. **Siempre se normaliza por el que queda debajo**, nunca por el grande, nunca por la media de los
dos, y nunca `max()` de los dos sentidos «por si acaso»: eso es lo que convierte un mordisco inofensivo en
una alarma.

---

## 4. La unidad de cuenta: el pisada-segundo

Un porcentaje suelto no se puede sumar. Lo que sí se suma es **fracción tapada × segundos de coincidencia**.
Es la unidad que permite decir si una versión está mejor que otra sin discutir caso por caso.

Censo completo de las dos versiones, mismo motor, mismo día:

| | `episodio01` (umbral único) | `ep01-lustig` (umbral doble) |
|---|---|---|
| elementos | 71 | 61 |
| parejas simultáneas | 93 | 96 |
| parejas que se tocan | 35 (38%) | 31 (32%) |
| 2–6% (el mordisco) | 4 | 7 |
| 18–42% | 12 | 5 |
| 42–70% | **4** | **0** |
| más del 70% | **2** | **0** |
| **pisada-segundos** | **7,77** | **3,33** |

Un episodio con más elementos y **menos de la mitad de pisada-segundos**. Eso es una decisión de umbral
(`383`), no suerte.

---

## 5. Lo que este bloque NO es

| No es | Está en |
|---|---|
| cuánto solape queda bien y qué cuenta cada disposición | `canales_lushows/26` |
| la oclusión como recurso para integrar un gráfico | `204` §3.5 |
| cuánto puede taparse una palabra y seguir leyéndose | `377` §3 |
| la zona que tapa la interfaz de la plataforma | `45` |
| máscaras y recortes | `58` · `105` |

Aquí solo se mide.

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Ordenar la pareja por tiempo y llamarlo capa | En un 30% de los casos se mide al revés (`386`) |
| Normalizar por el área del grande | Un rótulo aplastado sale como pisada del 3% |
| Usar `max(pisa(a,b), pisa(b,a))` | Toda pareja con un elemento pequeño salta como grave |
| Medir el solape sin cruzarlo con las vidas | Cientos de parejas falsas que nunca coinciden |
| Sumar porcentajes en vez de pisada-segundos | Una pisada de 0,13 s pesa igual que una de 3,16 s (`385`) |
| Dar por bueno un porcentaje sin saber qué era lo tapado | El 5% sobre una cifra es peor que el 35% sobre una foto (`381`) |
| Medir solo la capa generada y no la escrita a mano | Las pisadas que sobreviven son justo las de la mano (`387`) |

## Relacionado

`381` el área que importa · `382` la zona protegida · `383` umbrales por tipo · `384` medir antes de
renderizar · `385` la pisada que dura · `386` el elemento enterrado · `387` pisar a propósito ·
`canales_lushows/26` superposición y oclusión (prescriptivo) · `204` §3.5 oclusión como recurso
