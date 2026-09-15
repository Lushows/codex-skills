# 147 · Cuándo una métrica deja de servir

**Qué resuelve:** medidas que siguen en el informe y ya no informan de nada. Ocupan
atención, dan sensación de control y esconden que nadie está vigilando ese fallo.

---

## Las cuatro señales

| Señal | Qué significa | Qué se hace |
|---|---|---|
| **Se cumple siempre** | El fallo ya no ocurre, o la medida no puede fallar | Degradar a comprobación silenciosa |
| **Falla siempre** | Está rota, o el umbral no corresponde al canal | Arreglar o jubilar. Nunca dejarla gritando |
| **El episodio la cumple y sigue mal** | Mide otra cosa (`142`) o falta una medida (`144`) | Añadir la que falta; ésta puede quedarse |
| **Nadie mira esa línea** | En la práctica ya está jubilada, sin decirlo | Quitarla del informe o arreglarla |

Las dos primeras se detectan con datos. Las dos últimas, siendo honesto.

## El caso: una alarma que abarcaba el episodio entero

El aviso de **cuadro descompensado** (todo el peso en un rincón) imprimía esto en
`ep01-lustig`:

```
  --- cuadro descompensado (todo el peso en un rincon) ---
     0.00 -  63.45  (63.45 s)  muerte    "el once de marzo de mil novecientos cuarenta"
```

El episodio dura 63,45 s. Un aviso que señala **el 100 % del episodio** como un solo
tramo no está diciendo "todo está mal": está diciendo *"estoy roto"*. Ningún montaje
real produce un tramo continuo de esa longitud, igual que ningún termómetro marca 40°
todo el año.

Causa, encontrada al instrumentar: la variable `n` (número de muestras a 20 Hz, 1269 en
este episodio) la **pisaba** un bucle anterior del propio auditor:

```python
for n, r, ts in sorted(repetidos, reverse=True)[:8]:        # <-- n pasa a valer 4
    print(f"   {n}x  {r:<24} en {', '.join(f'{t:.1f}' for t in ts)}")
```

A partir de ahí, `range(0, n, 4)` recorre **una sola muestra, en t = 0**. Dos medidas
—*planos de sólo texto* y *cuadro descompensado*— medían un instante en vez de todo el
episodio. Y sólo se rompía cuando `repetidos` no estaba vacío: con un episodio sin
repeticiones el bucle no se ejecuta, `n` sobrevive y las dos medidas funcionaban.
**Un fallo intermitente que dependía de otra medida.**

Arreglado (renombrando la variable del bucle a `nrep`), el mismo episodio dice:

```
  --- planos de SOLO TEXTO (1.2 s) ---
     9.40 -  10.60  (1.20 s)  muerte    d_1890

  --- cuadro descompensado (todo el peso en un rincon) ---
     7.00 -   8.60  (1.60 s)  muerte    "en el"
    20.60 -  24.80  (4.20 s)  oficio    "aprendiz de vendedor no se llamaba miller"
    28.40 -  31.00  (2.60 s)  nombre    "según todo lo que se ha contado de él"
    ... 8 tramos, 14,6 s = 23% del episodio
```

Veintitrés por ciento del episodio con el cuadro descompensado, invisible mientras la
medida "funcionaba".

## El caso contrario: la que nunca dice nada

`auditar.py` recoge los recursos que no encuentra en disco:

```python
SIN_RESOLVER = set()
...
        if p is None:
            SIN_RESOLVER.add(recurso)          # se reporta, no se puntua como 0
```

El comentario dice *"se reporta"*. **No se imprime en ninguna parte.** El conjunto se
llena y muere con el proceso. En `ep01-lustig` está vacío, así que nadie lo ha notado;
el día que un recurso se renombre, el elemento valdrá 0 de cobertura en silencio y el
informe dirá que el episodio va flojo sin decir por qué.

Una métrica que se calcula y no se muestra está jubilada de hecho. O se imprime, o se
borra el código: lo que no puede quedarse es el comentario diciendo que sí se reporta.

## Cómo se comprueba que una medida sigue viva

Tres pruebas baratas, una vez por temporada:

1. **Historial.** ¿Ha saltado alguna vez en los últimos N episodios? Si nunca, o si
   siempre, hay conversación pendiente.
2. **Inyección de fallo.** Se estropea el montaje a propósito (se borra un elemento, se
   mueve todo a la mitad derecha) y se comprueba que la medida **lo caza**. Si no salta,
   estaba muerta.
3. **Rango de salida.** Si el tramo reportado dura casi lo mismo que el episodio, o si
   el porcentaje sale 0 % o 100 % clavado, sospechar del código antes que del montaje.

```python
# prueba 2, aplicada al cuadro descompensado
# todo el material amontonado a la derecha: DEBE producir tramos
for esc in ESCENAS:
    for ele in esc["elementos"]:
        ele["x"] = "W*0.70"
# ... recalcular y exigir que desc no esté vacío
```

## Cómo se jubila

No se borra a la ligera: cada medida existe porque **algo se coló al vídeo**. El
procedimiento:

1. Comprobar que el fallo que cazaba ya es imposible por construcción (por ejemplo, el
   generador nunca puede producirlo), no sólo que no ha vuelto a pasar.
2. Bajarla de sección propia a **comprobación silenciosa**: sigue ejecutándose, sólo
   imprime si falla.
3. Dejar en el código una línea con la fecha y el episodio donde se dejó de reportar.
4. Si después vuelve a fallar una sola vez, vuelve al informe.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Dejar en el informe una medida que grita siempre | Se ignora esa sección, y con ella el aviso bueno |
| Dar por buena una medida porque "sale limpia" | Puede estar rota y limpia a la vez |
| Reutilizar nombres de variable en un script largo | Dos medidas midiendo un instante sin avisar |
| Calcular algo y no imprimirlo | El fallo ocurre y el informe no lo menciona |
| Borrar una métrica por molesta | Vuelve el fallo que la hizo nacer |

## Relacionado

`141` elegir un umbral · `142` la medida que miente · `143` la alarma en falso ·
`148` el cuadro de mando · `149` lo que no se puede medir
