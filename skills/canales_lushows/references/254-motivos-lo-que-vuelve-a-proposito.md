# 254 · Motivos: lo que vuelve a propósito

**Qué resuelve:** distinguir la repetición que es pobreza de la que es gramática. Hay
imágenes **hechas para volver** —las marcas de columna, el logotipo, la línea de tiempo
que se construye hito a hito— y si el antirrepetición las trata como al resto, el
episodio pierde lo que le enseña al espectador a leerlo.

---

## Qué es un motivo

En `ep01-lustig` hay tres, y los tres son el método del episodio hecho imagen:

```python
# Se declaran por FAMILIA, que es como los cuenta el auditor: "linea" cubre
# linea_00, linea_02 y linea_06, que no son tres graficos repetidos sino tres
# hitos de la MISMA linea de tiempo construyendose delante del espectador.
MOTIVOS = {"m_consta", "m_cuenta", "linea"}
```

`m_consta` y `m_cuenta` son las dos marcas de columna: **lo que consta** (documento,
monoespaciada, papel blanco) contra **lo que se cuenta** (leyenda, serif de revista,
papel amarillo). Vuelven en cada cambio de terreno, y esa vuelta es lo que permite al
espectador saber, sin que se lo digan, si lo que oye está probado o solo contado.

## Por FAMILIA, no por nombre

El auditor agrupa los usos por familia y después comprueba la pertenencia:

```python
for a, b, _, r, _, _ in vidas:
    usos.setdefault(familia(r), []).append(a)     # 'linea_02' -> 'linea'
for r, ts in usos.items():
    if r in MOTIVOS:                              # ese 'r' YA es la familia
        continue
```

Y el diccionario, al anotar, tiene que usar el mismo criterio, mirando el nombre **y** la
familia:

```python
def _anotar(r, t):
    _VISTO.setdefault(r, []).append(t)
    f = familia(r)
    if r not in MOTIVOS and f not in MOTIVOS:
        _VISTO.setdefault(f, []).append(t)
```

Si ahí se comprobara solo `r`, la línea **se bloquearía a sí misma** mientras el auditor
la da por buena. Ejecutado:

```
== MOTIVOS por FAMILIA (como está) ==
  _VISTO: {'linea_00': [3.0]}
  _ultima('linea_03', 12.0) = 9999.0  -> bloqueada? False

== si _anotar mirara solo el nombre completo ==
  _VISTO: {'linea_00': [3.0], 'linea': [3.0]}
  _ultima('linea_03', 12.0) = 9.0     -> bloqueada? True
```

Nueve segundos después del primer hito, el segundo queda fuera del montaje y nadie se
entera: el auditor no lo cuenta como repetición, así que no aparece en ninguna lista.
**Un elemento que no llega a existir no deja rastro en las métricas.**

En el episodio 01 el fallo es latente: los hitos van escritos a mano y en `NUNCA_AUTO`,
así que hoy el montaje sale idéntico con las dos versiones. Basta una entrada de
vocabulario que apunte a `linea_04` para que empiece a comerse elementos.

## Qué pasa si no se declaran

Quitando `MOTIVOS`, el montaje no cambia (61 elementos, 1,11 usos) pero el auditor grita:

```
   3x  linea    en 0.8, 31.1, 50.8
   19.7 s  linea    (31.1 y 50.8)
```

Tres usos y una pareja a 19,7 s marcados como defecto cuando son lo que se buscaba. Peor
que no medir: la alarma en falso entrena a quien monta para ignorar la lista (`143`).

## Un motivo no es una excusa

Tres pruebas antes de declarar algo motivo:

1. **¿Significa lo mismo cada vez?** La marca de columna sí: siempre dice «esto está
   probado». Un plano de París no: la segunda vez dice «no teníamos otro».
2. **¿Vuelve en un sitio elegido?** En el cambio de terreno, en el remate, en el hito. Si
   la vuelta la decide el generador, no es motivo.
3. **¿El espectador aprende algo con la vuelta?** Si no, es repetición.

De los 55 recursos distintos del minuto 1, tres son motivos: un 5%. Si esa proporción
sube, falta material y se está legalizando con una lista.

## La serie no es un motivo

Una **serie** son estados sucesivos del mismo elemento encadenados —`usd_03`, `usd_06`,
`usd_09`, `usd_11`: una cifra que sube— y el auditor ya la cuenta como un evento único:

```python
GESTO = 2.5    # usos mas juntos que esto son UN gesto, no repeticion
```

La serie se resuelve con el umbral de gesto; el motivo, con la declaración.

## `recordar()` los salta

```python
for e in elementos:
    if e["r"] in MOTIVOS:
        continue
```

Aquí la comprobación es por nombre completo **a propósito**: se salta la anotación de los
elementos cuyo nombre es literalmente el motivo (`m_consta`, `m_cuenta`). Los hitos
numerados sí se anotan con su nombre, y es `_anotar` quien no contamina la familia.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Declarar motivos por nombre completo | El motivo se bloquea a sí mismo; el auditor no lo ve |
| Meter en `MOTIVOS` lo que falta de material | La métrica de repetición deja de servir |
| Declarar una serie como motivo | Se esconde de la medición algo que el umbral de gesto ya resolvía |
| No declarar los que sí lo son | Alarmas en falso que entrenan a ignorar la lista |
| Motivos que vuelven donde los pone el generador | Dejan de significar y pasan a ser relleno |

## Relacionado

`253` · `252` · `257` · `143` · `147` · `126` · `127`
