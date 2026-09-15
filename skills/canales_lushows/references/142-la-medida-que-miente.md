# 142 · La medida que miente

**Qué resuelve:** una métrica que da un número correcto de algo que no es lo que se
quería saber. Es peor que no medir: da permiso para publicar.

---

## El caso de la balanza

El auditor tiene un control de repetición: avisa si un mismo recurso vuelve demasiado
pronto o sale demasiadas veces. Contaba **el nombre literal del recurso**.

En el episodio de Lustig la balanza está dibujada en cinco estados (`balanza_01` …
`balanza_05`: los platillos inclinándose). Para el contador eran cinco recursos
distintos. Para el espectador es **el mismo dibujo**, cuatro veces en pantalla.

Lo mismo con la línea de tiempo: `linea_00`, `linea_02`, `linea_03`, `linea_06`.

Las dos cuentas, sobre el mismo episodio, medidas hoy:

| | Gestos | Recursos distintos | Usos por recurso | Avisos |
|---|---|---|---|---|
| Por nombre literal | 50 | 46 | **1,09** | 1 |
| Por familia | 48 | 39 | **1,23** | 6 |

El objetivo es ≤ 1,25. Con el nombre literal el informe imprimía *"sin repeticiones:
ningún recurso sale de más ni vuelve demasiado pronto"* — **con la misma balanza cuatro
veces en el episodio**, dos de ellas a 2,5 segundos de distancia.

## La corrección

Se agrupa por familia: si el nombre acaba en `_` + dígitos, es un estado del mismo
dibujo.

```python
def familia(r):
    return r.rsplit("_", 1)[0] if r.rsplit("_", 1)[-1].isdigit() else r
```

Y una serie encadenada (estados sucesivos del mismo recurso, en el mismo sitio) cuenta
como **un solo evento**, no como cuatro: el ojo ve una cifra que sube, no cuatro
elementos entrando.

```python
entradas, ultimo = 0, {}
for a, b, _, r, _, _ in vidas:
    k = familia(r)
    if k in ultimo and a - ultimo[k] < 0.45:   # encadenado: misma serie
        ultimo[k] = b
        continue
    ultimo[k] = b
    entradas += 1
```

Con la familia arreglada el informe delata lo que se ve de verdad:

```
  Repeticion: 48 gestos · 39 recursos distintos · 1.23 usos por recurso  (objetivo <= 1,25)
  --- recursos que salen demasiadas veces ---
   4x  linea      en 0.7, 31.0, 37.7, 50.7
   4x  balanza    en 32.9, 54.8, 58.9, 61.4
  --- mismo recurso repetido a menos de 25 s ---
     2.5 s  balanza  (58.9 y 61.4)
     4.1 s  balanza  (54.8 y 58.9)
```

## Cómo se detecta que una métrica mide otra cosa

Cuatro pruebas, por orden de coste:

1. **Contradicción con el ojo.** La métrica dice bien y la rejilla de fotogramas dice
   mal. Eso no es "criterio distinto": es que la métrica no mide lo que importa. Cuando
   pasa, gana el ojo y se arregla la métrica.
2. **Caso de prueba fabricado.** Se construye a mano un montaje que DEBE fallar y se
   pasa la medida. Si no salta, miente. El de repetición: un episodio con la misma foto
   cuatro veces separadas 3 segundos.
3. **Recontar por otro camino.** La misma magnitud calculada de una segunda forma. Si
   por nombre literal da 1,09 y por familia 1,23, hay que decidir cuál corresponde a lo
   que ve el espectador; el desacuerdo ya es la señal.
4. **Preguntar qué unidad tiene.** "Usos por recurso" sólo significa algo si *recurso*
   quiere decir *cosa que el espectador reconoce*. La unidad estaba mal definida; el
   número era impecable.

## La regla de fondo

**La unidad de medida es la unidad de percepción.** El canal no mide ficheros, mide lo
que el espectador cuenta como una cosa:

| Se cuenta | Unidad correcta |
|---|---|
| Repetición | La familia del recurso (el dibujo), no el fichero |
| Eventos | El gesto, no el elemento (`10`) |
| Cobertura | Píxeles dentro del lienzo, no del elemento (`146`) |
| Presencia | Superficie ocupada, no "hay algo" (`144`) |

Cada vez que una de esas unidades se confundió con la del sistema de ficheros, la
métrica dio un aprobado falso.

## La salida de emergencia, declarada

Hay recursos que vuelven **a propósito**: las marcas de columna, el logotipo, la línea
de tiempo que se construye. No son falta de material, son la gramática del episodio. Se
declaran en el guion visual:

```python
MOTIVOS = {"m_consta", "m_cuenta"}
```

y el control los salta. La excepción se declara **una vez y por escrito**; no se
resuelve relajando el umbral para todos.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Contar ficheros en vez de cosas reconocibles | "Sin repeticiones" con la misma balanza 4 veces |
| Creer a la métrica antes que a la rejilla | Se publica un episodio que se ve repetitivo |
| Arreglar el umbral en vez de la unidad | El aviso salta donde no toca y calla donde toca |
| No declarar los motivos | El control grita por el logotipo y se acaba apagando (`143`) |
| Dar por buena una métrica sin caso de prueba | Puede llevar meses aprobando episodios flojos |

## Relacionado

`10` densidad de eventos · `141` elegir un umbral · `143` la alarma en falso ·
`146` medir lo que se ve · `147` cuándo una métrica deja de servir
