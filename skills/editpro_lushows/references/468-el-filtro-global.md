# 468 — El filtro global: el que no empareja nada

**Qué resuelve:** el gesto de poner un "look" —una LUT de moda, un preset de cámara antigua, un
`curves=preset=vintage` con saturación— **encima de todos los planos a la vez** y dar el color por
hecho. Es lo que hace que un montaje se vea a plantilla aunque los planos estén bien filmados, y es
medible: un filtro global **no acerca los planos entre sí**, que es justo lo único que tenía que hacer.

El módulo de oficio es `62-emparejar-planos.md`; el de referencia externa,
`255-emparejar-a-una-referencia.md`. Este mide la diferencia entre las dos cosas.

---

## 1. La confusión que hay debajo

Hay dos trabajos distintos y la gente hace el segundo creyendo que hace el primero:

| | Qué hace | Cuándo |
|---|---|---|
| **Corrección / emparejado** | lleva cada plano a un punto común: mismo negro, mismo blanco, misma piel | **antes**, plano a plano |
| **Gradación / look** | da carácter a la pieza entera, ya emparejada | **después**, una vez |

Un filtro global se salta el primero. Y como el segundo mueve todo en bloque, **las diferencias entre
planos siguen ahí, intactas, solo que ahora todas teñidas del mismo color**. Ver `61-correccion-vs-gradacion.md`.

---

## 2. La magnitud: dispersión entre planos

La cifra es la **desviación típica, entre planos, de tres estadísticos**: la luminancia media, el punto
de negro (percentil 1) y el punto de blanco (percentil 99). Emparejar significa exactamente **bajar esa
dispersión**. Si no baja, no emparejaste.

```python
def ficha(p):
    im = np.asarray(Image.open(p).convert("RGB")).astype(np.float32)
    y  = 0.299*im[...,0] + 0.587*im[...,1] + 0.114*im[...,2]
    return dict(med=y.mean(), neg=np.percentile(y,1), bla=np.percentile(y,99),
                rec0=(im<=1).mean()*100, rec255=(im>=254).mean()*100,
                niveles=len(np.unique(im.astype(np.uint8))))
fs = [ficha(p) for p in planos]
print("dispersión:", np.std([f['med'] for f in fs]))
```

---

## 3. Los números

Tres planos de archivo distintos (billetes con luz de estudio, pasillo institucional, avión contra el
cielo). Tres estados: crudos, con un filtro global típico, y emparejados plano a plano.

```bash
# el filtro global: un look encima de todo
ffmpeg -y -loglevel error -i plano.png -vf "curves=preset=vintage,eq=saturation=1.45:contrast=1.25" \
  -frames:v 1 filtrado.png
```

| Estado | media Y por plano | **σ de la media** | σ del negro | σ del blanco | recorte a 0 |
|---|---|---|---|---|---|
| **Crudos** | 125,2 · 104,9 · 127,4 | **10,11** | 7,90 | 17,76 | 0,09 · 0,11 · 0,00% |
| **Filtro global** | 127,0 · 102,5 · 127,8 | **11,71** | 5,49 | 19,62 | **6,81 · 2,33 · 4,59%** |
| **Emparejados** | 125,2 · 124,8 · 124,7 | **0,19** | 3,34 | 15,23 | 0,09 · 4,62 · 0,01% |

Las dos conclusiones están en la columna de en medio:

- **El filtro global empeoró la dispersión: de 10,11 a 11,71.** No es un matiz: aplicar el look subió
  la distancia entre planos, porque una curva no lineal separa más lo que ya estaba separado. El
  montaje sigue saltando en cada corte, ahora con color de época.
- **El emparejado la bajó de 10,11 a 0,19: 53 veces menos.** Eso es lo que hace que una secuencia se
  sienta rodada el mismo día.

Y la segunda factura, la que nadie mira: **el recorte**. Los planos crudos pegaban al negro entre el
0,00% y el 0,11% de sus píxeles. Con el filtro global, hasta el **6,81%**. Eso es detalle de sombra que
ya no existe y que ninguna corrección posterior recupera.

> **Umbral: si al aplicar tu look la σ de la media entre planos no baja, no estás emparejando, estás
> tiñendo.** Y si el recorte a 0 o a 255 pasa del 1% en algún plano, estás perdiendo material.

---

## 4. Cómo se hace bien (y la trampa del emparejado automático)

El orden correcto está en `62` y `61`: primero cada plano a un punto común, después el look una sola vez
sobre el corte terminado. El emparejado de la tabla se hizo llevando media y desviación de cada canal a
las del plano de referencia:

```python
for c in range(3):
    e[...,c] = (im[...,c]-im[...,c].mean())/im[...,c].std()*ref[...,c].std() + ref[...,c].mean()
```

🔴 **Y ahí está la trampa, visible en la tabla:** ese emparejado ingenuo funciona para la media (σ 0,19)
pero **provocó un 4,62% de recorte a negro y un 1,31% a blanco en el plano del pasillo**, porque estirar
la desviación típica empuja las colas fuera del rango. El emparejado profesional no iguala σ: iguala
**puntos** —negro, blanco y medios— con los scopes delante, y protege los extremos:

1. Fija el **negro** de cada plano en el mismo nivel (`lutyuv` o `curves`, punto `0/`).
2. Fija el **blanco** igual, sin que nada pase de 235 en rango limitado.
3. Ajusta los **medios** para que la piel caiga donde debe (`67-piel.md`, `254-la-piel-a-fondo.md`).
4. Solo entonces, el look: **una** LUT, sobre el corte, con intensidad regulable (`65-luts.md`).

Ver `252-leer-scopes-de-verdad.md` y `69-monitoreo-y-scopes.md` para hacer los tres primeros pasos
mirando, que es como se hacen.

---

## Errores frecuentes

1. **Aplicar la LUT a la secuencia entera antes de emparejar.** Es el error madre: el look amplifica las
   diferencias en vez de taparlas.
2. **Juzgar el emparejado a ojo saltando entre planos.** El ojo se adapta en dos segundos. Ponlos lado a
   lado (`62`) y mide.
3. **Emparejar igualando media y desviación típica sin mirar las colas.** Medido: 4,62% de recorte a
   negro. Iguala puntos, no momentos estadísticos.
4. **Subir contraste y saturación como sustituto del emparejado.** Es el punto 7 del `56`: rompe la piel
   primero.
5. **Dar por bueno un look porque "se ve bien" en el plano principal.** Mide los tres planos: el que
   sufre siempre es el más oscuro o el más plano.
6. **Poner la LUT al 100% sin control de intensidad.** Una LUT es un punto de partida, no un resultado.
7. **Confundir esto con el tinte de `462`.** Aquel mide *qué* color se impuso; este mide *si* los planos
   se acercaron. Son dos preguntas distintas y ambas se pueden fallar a la vez.

---

## Relacionado

- `62-emparejar-planos.md` — **el oficio: llevar varios planos a un punto común.**
- `61-correccion-vs-gradacion.md` — los dos trabajos y su orden.
- `255-emparejar-a-una-referencia.md` · `258-color-en-material-mixto.md`
- `252-leer-scopes-de-verdad.md` · `69-monitoreo-y-scopes.md` — hacerlo mirando.
- `65-luts.md` · `64-forzar-la-paleta-de-marca.md` — el look, después y una sola vez.
- `425-efectos-que-compiten.md` — qué pasa cuando dos efectos se pelean por el mismo bitrate.
- `462-el-degradado-morado.md` — la otra pregunta sobre el color de un fotograma montado.
