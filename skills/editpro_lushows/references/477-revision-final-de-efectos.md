# 477 — Revisión final de efectos

> **Una pasada que mira solo los efectos, y se hace antes de la verificación general del corte.** El
> `98` comprueba que el vídeo está sano: que no hay palabras partidas, que el audio existe, que el texto
> cabe. Esta pasada comprueba otra cosa que el `98` no mira: **que los efectos que creías haber puesto
> están de verdad en el archivo, que son los que decidiste, y que ninguno sobra.**

El orden importa y no es negociable: **477 primero, 98 después.** Porque si esta pasada te hace quitar
un efecto, vuelves a renderizar, y todo lo que hubiera verificado el `98` habría caducado.

---

## 1. El fallo que hace falta esta pasada

Un efecto puede desaparecer sin que nada falle. El caso canónico, del motor del piloto:

```python
# Ojo: 'eq' solo evalua expresiones si se le pide 'eval=frame'. Sin eso lee
# el valor una vez al iniciar y el destello no ocurre.
```

Sin `eval=frame` el render **sale perfecto**: código de salida 0, duración correcta, archivo sano,
`ffprobe` contento. Y sin destellos. Ningún checklist de integridad lo detecta, porque el archivo no
tiene nada malo: le falta algo, que es distinto.

La misma familia de fallo: un ancla que no existe en la locución, un `enable='between(...)'` con los
segundos mal, un filtro que se encadenó a la etiqueta equivocada y se quedó colgando. **Todos producen
un vídeo válido sin el efecto.**

---

## 2. La prueba: buscar los efectos en el archivo renderizado

**El instrumento es el de `432`** —extraer `YAVG` fotograma a fotograma y sacar base, pico, Δ y FWHM— y
allí está explicado a fondo, incluida la trampa de `-loglevel error`. Lo que se hace aquí es otra cosa y
es lo propio de una revisión final: **no medir un destello, sino comprobar que están todos.**

Si tu efecto es de luz —destello, flash, fogonazo, fundido a blanco—, deja una firma medible en la
luminancia media por fotograma. Se extrae así:

```bash
ffmpeg -hide_banner -loglevel error -i _mudo.mp4 \
  -vf "signalstats,metadata=print:key=lavfi.signalstats.YAVG:file=yavg.txt" -f null -
```

Y se buscan los picos locales: fotogramas cuya luminancia supera a su entorno de ±0,35 s.

```python
import io, re
t, datos = None, []
for l in io.open("yavg.txt", encoding="utf-8"):
    m = re.match(r"frame:\s*\d+\s+pts:\s*\d+\s+pts_time:([\d.]+)", l)
    if m: t = float(m.group(1))
    m = re.search(r"YAVG=([\d.]+)", l)
    if m and t is not None: datos.append((t, float(m.group(1))))

for i, (t, y) in enumerate(datos):
    ven = [v for tt, v in datos if abs(tt - t) <= 0.35 and tt != t]
    if ven and y - max(ven) > 0.4:
        print(f"   t={t:6.2f}s   YAVG={y:6.2f}   +{y - sum(ven)/len(ven):.2f} sobre su entorno")
```

### Lo que devuelve en el piloto

Corrido sobre `ep01-lustig/salida/_mudo.mp4` (1.586 fotogramas medidos), agrupando picos contiguos:

```
   t=  0.92s   YAVG= 93.25   + 2.67 sobre su entorno
   t=  6.88s   YAVG=104.99   +23.22
   t= 20.56s   YAVG=132.01   +31.97
   t= 33.04s   YAVG= 85.04   +17.83
   t= 35.04s   YAVG=102.67   + 6.23
   t= 41.84s   YAVG=125.45   +30.47
   t= 45.60s   YAVG= 90.78   + 2.13
   t= 49.00s   YAVG=102.89   + 4.90
   t= 53.64s   YAVG= 88.05   + 4.55
   t= 57.88s   YAVG= 74.27   + 1.52
   t= 60.96s   YAVG=101.98   + 8.49
   t= 62.92s   YAVG=117.90   +32.36
```

Ahora se cruza con lo declarado en `guion_visual.py`:

| Declarado | Medido en el render | Fuerza | Salto de luz |
|---|---|---|---|
| 6,88 s | **6,88** | 0,15 | +23,22 |
| 20,55 s | **20,56** | 0,22 | +31,97 |
| 33,02 s | **33,04** | 0,14 | +17,83 |
| 41,85 s | **41,84** | 0,18 | +30,47 |
| 62,93 s | **62,92** | 0,20 | +32,36 |

**Cinco de cinco, con una desviación máxima de 0,02 s.** Y la separación es limpísima: los efectos
declarados saltan **entre +17,8 y +32,4**; todo lo demás que detecta la prueba —cambios de plano, una
lámina más clara que la anterior— se queda **en +8,5 o menos**. No hace falta afinar el umbral: hay un
orden de magnitud de distancia entre un efecto y el ruido del contenido.

Eso convierte la prueba en binaria y en automatizable:

> **Si un destello declarado no aparece en la lista de picos, no está en el vídeo.** No es opinión, no
> hay que mirarlo, no hay que discutirlo. Se arregla y se vuelve a renderizar.

---

## 3. La segunda comprobación: que la fuerza se corresponda

Mira la última columna de la tabla otra vez. La fuerza más baja (0,14) da el salto más pequeño (+17,8) y
las tres altas dan los tres saltos grandes. No es perfectamente proporcional —el salto depende también
de lo clara que sea la imagen debajo— pero el orden se respeta. Si te sale al revés (un 0,22 que salta
menos que un 0,14), no es un fallo del efecto: **es que la imagen de debajo ya estaba quemada y el
destello no tiene recorrido**. Ese plano necesita otra cosa, no más fuerza.

---

## 4. Las comprobaciones que ya te da el auditor

Antes de renderizar, y por tanto mucho antes de esta pasada, el auditor del montaje ya reporta tres
cosas que descalifican un sitio para llevar efecto:

```
  ! 0.2 s con mas de 4 elementos a la vez (ruido)

--- cuadro PLANO: ningun elemento manda (2.3 s) ---
    29.80 -  30.90  (1.10 s)  nombre
    48.80 -  50.00  (1.20 s)  torre

--- elementos LAVADOS contra su fondo (4) ---
    46.76  torre_citroen_noche   luz  96.7 sobre fondo  97.8  ->   1.1 de diferencia
    39.41  bajo_la_torre         luz  72.5 sobre fondo  70.0  ->   2.5 de diferencia
```

Cruza esas listas con los segundos de tus efectos. **Un efecto que cae dentro de un tramo de ruido, de
cuadro plano o sobre un elemento lavado está tirado**, y lo sabes antes de renderizar.

---

## 5. La tabla de veredictos

Igual que en el `98`, se clasifica todo **antes** de tocar nada:

| Hallazgo | Veredicto |
|---|---|
| Efecto declarado que no aparece en los picos | 🔴 **Arreglar** — probablemente `eval=frame` o un ancla inexistente |
| Efecto con un salto menor que el de una fuerza inferior | 🟡 Mirar el plano: puede estar quemado |
| Efecto que cae en tramo de ruido / cuadro plano / elemento lavado | 🔴 **Mover o quitar** |
| Efecto cuya razón no cabe en una frase | 🔴 **Quitar** |
| Pico grande no declarado | 🟡 Mirar: o es un corte fuerte legítimo, o un efecto que no recuerdas |
| Más efectos que tu techo del `470` | 🔴 **Quitar hasta el techo** |

La cuarta fila es la del `29` aplicada solo a efectos, y sigue siendo la que más cosas quita:

> **Si te preguntan «¿por qué ese destello ahí?» y no tienes una frase, sale.** No «queda bien». Una
> frase que diga qué hace.

---

## 6. La pasada completa, en orden

```
1. Cuenta los efectos y comparalos con el techo (470).
2. Escribe, al lado de cada uno, su razon en UNA frase.
3. Corre la deteccion de picos sobre el render.
4. Cruza: declarados vs medidos. Cinco de cinco o se arregla.
5. Cruza con las listas del auditor: ruido, cuadro plano, lavados.
6. Clasifica todo en la tabla de veredictos.
7. Solo entonces, corre el 98 sobre el archivo final.
```

---

## Errores frecuentes

1. **Dar por hecho que el efecto está porque el render no falló.** El fallo silencioso produce un archivo
   perfectamente sano sin el efecto.
2. **Correr el `98` antes que esta pasada.** Si aquí quitas algo, hay que volver a renderizar y el `98`
   caduca.
3. **Buscar los efectos a ojo en la línea de tiempo.** Un destello de 0,2 s no se ve pasando el vídeo.
4. **Ajustar el umbral de detección de picos.** Hay un orden de magnitud entre efecto y contenido; si te
   hace falta afinarlo, tu efecto es demasiado suave para existir.
5. **Subir la fuerza cuando el salto sale corto.** Si la imagen está quemada, más fuerza no cabe.
6. **No cruzar con las listas del auditor.** Un efecto sobre un elemento lavado es trabajo tirado.
7. **Dejar un efecto sin frase que lo justifique** porque «ya está puesto».
8. **Ignorar un pico grande no declarado.** O es un corte legítimo o es algo que no controlas.
9. **Hacer esta pasada solo en el episodio final.** Se hace por tramo (`475`); a doce minutos, si no, no
   se hace nunca.
10. **Confundir esta pasada con la verificación del corte.** Son dos cosas y las dos hacen falta.

---

## Relacionado

- `98` — **verificación del corte**: la comprobación general, que va **después** de esta.
- `470` — el techo de efectos contra el que se cuenta.
- `471` — los sitios donde un efecto paga; aquí se comprueba que cayó en uno.
- `472` — la prueba A/B, para decidir si un efecto dudoso se queda.
- `473` — el sistema de marca: aquí se verifica que sus números no derivaron.
- `432` — **medir un destello**: el instrumento que esta pasada usa, con sus cuatro números y su trampa
  de nivel de log. `431` — la forma de la campana que produce la firma.
- `429` — cuándo quitar un efecto: los seis disparadores y el protocolo de retirada, para todo lo que
  esta pasada marque en rojo.
- `423` — el efecto que no se ve; `424` — el efecto que tapa un problema.
- `29` — el corte final: «si no cabe la razón en una frase, sale».
- `108` — análisis y medición con ffmpeg; de ahí sale `signalstats`. `421` — la magnitud que delata a
  cada familia de efecto, cuando el tuyo no es de luz.
- `133` — verificación automática dentro del pipeline.
- `canales/150-catalogo-del-fallo-silencioso`, `canales/159-cazar-un-fallo-que-no-avisa` — la familia
  completa de fallos que no dan error.
- `canales/168-reproducir-antes-de-afirmar`, `canales/169-el-informe-de-auditoria` — no afirmar sin
  haberlo comprobado, y cómo se reporta.
