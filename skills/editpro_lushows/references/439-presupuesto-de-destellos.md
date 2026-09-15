# 439 — Presupuesto de destellos

> El cuarto destello de una pieza no puntúa: informa de que hay destellos. La luz como recurso de
> montaje se gasta, y se gasta rápido. Este módulo pone el número antes de empezar, que es la única
> forma de que no se dispare.

`269` explica el presupuesto del esfuerzo en general; esto es el presupuesto de **un solo recurso**,
con cifras medidas.

---

## 1. La regla: el número se decide antes, no después

Poner destellos y luego quitar los que sobran no funciona, porque cuando llegas a quitarlos ya te has
acostumbrado a verlos. **Se decide el cupo mirando la duración, se reparten los papeles (`430`, §3), y
ya no se añade ninguno más.** Si aparece un sitio mejor, se cambia uno de sitio; no se suma.

| Duración de la pieza | Cupo de destellos | Uno cada |
|---|---|---|
| Menos de 15 s | **0** | — |
| 15–30 s | **1** | — |
| 30–45 s | 1–2 | ≥ 15 s |
| 45–60 s | 2–3 | ≥ 12 s |
| 60–90 s | 4–6 | ≥ 12 s |
| 90 s – 3 min | 6–9 | ≥ 15 s |
| Más de 3 min | 9–12, **no más** | ≥ 20 s |

Los tramos de 60–90 s salen de material medido: **5 destellos en 62,98 s y 6 en 79,7 s** en las dos
piezas del piloto documental, con una separación mínima real de **7,67 s** (`430`). Por encima de los
tres minutos la densidad **baja**, no se mantiene: en una pieza larga el espectador ya aprendió el
recurso y hace falta menos.

**Lo de "0 destellos por debajo de 15 s" es en serio.** En un reel corto el ritmo lo llevan los cortes
(`20`) y un fogonazo compite con ellos. La excepción es el vídeo de anuncio, donde el flash suele ir
**en el corte** y entonces ya no es esto, es `53`.

---

## 2. Qué cuesta uno bien hecho

Separando tiempo de cabeza y tiempo de máquina, que es lo que engaña:

| Paso | Tiempo de persona | Tiempo de máquina |
|---|---|---|
| Elegir la palabra y el papel (`430`, `437`) | 2–3 min | — |
| Escribir la expresión con su `eval=frame` (`431`) | 1 min | — |
| Render de la escena a 1080p | — | minutos |
| Medir la curva y comprobar que ocurrió (`432`) | 2 min | ~10 s |
| Elegir y colocar el impacto sonoro (`433`) | 3 min | segundos |
| Verificar la sincronía sobre el archivo final | 3 min | ~20 s |
| **Total** | **≈ 11 min** | — |

Once minutos por destello. En una pieza de 90 s con seis, **una hora larga**. Ese es el número que hay
que tener en la cabeza cuando alguien dice "ponle unos flashes".

---

## 3. Qué rinde y qué no

| Recurso de luz | Coste | ¿Vale la pena? |
|---|---|---|
| **Un destello en el remate, con su sonido** | 11 min | **Siempre.** Es el que más rinde del bloque |
| Destello de apoyo en un cambio de bloque | 11 min | Sí, hasta el cupo |
| **Bloom en RGB sobre el plano principal** (`434`) | 5 min | **Sí.** Es el mejor negocio por minuto |
| Pulso de exposición por bloque (`436`) | 4 min | Sí en piezas de más de 60 s |
| Fuga de luz tapando una costura (`435`) | 8 min | Sí, cuando hay costura que tapar |
| Halación (`434`) | 10 min | Sólo si el look de película es la marca |
| Fuga "decorativa" sin costura debajo | 8 min | **No.** Es adorno |
| Destello nº 7 en una pieza de 60 s | 11 min | **No.** Resta |
| Afinar la fuerza de 0,14 a 0,15 | 15 min | **No.** El filtro ni se entera (`431`, §4) |

---

## 4. Cuando te pasas: qué se cae primero

Orden de recorte, de arriba abajo. Se quita hasta entrar en cupo:

1. **El que no lleva sonido.** Si no cabe el impacto, no cabe el destello (`433`).
2. **El que está a menos de 7 s del anterior.** Se lee como parpadeo, no como puntuación.
3. **El anclado a un verbo o a una palabra vacía.** Se ancla lo que se puede ver (`437`, §4).
4. **El que repite una idea ya marcada.** Una idea, un destello.
5. **El del último bloque, si no es el remate.** El cierre se apaga, no grita.
6. **El más débil de los que quedan.** Si tienes dos a 0,12, uno sobra.

Y la comprobación final, que es una resta: cuenta los picos de luminancia del render y compáralos con el
cupo que te habías puesto (`432`). Si no coinciden, alguien añadió uno sin decírtelo — o desapareció uno
por un ancla rota (`437`, §5).

---

## 5. El presupuesto también es de seguridad

El cupo de este módulo y el criterio de `438` no son lo mismo, pero se refuerzan: un destello cada 12 s
son **0,08 Hz**, 38 veces por debajo del límite de tres por segundo de WCAG 2.3.1. Mientras respetes el
cupo, la fotosensibilidad no es tu problema — **salvo que el riesgo venga de los cortes**, que no
cuentan en este presupuesto y sí en el de `438`.

Dicho al revés: si cumplir `438` te obliga a bajar el cupo, es que el montaje tiene un problema de
ritmo, no de luz.

---

## 6. La prueba del recuento, en dos líneas

Antes de entregar:

```bash
# cuántos picos de luminancia por encima de 15 niveles sobre la base hay en la pieza
ffmpeg -hide_banner -i final.mp4 -vf "signalstats,metadata=print:key=lavfi.signalstats.YAVG" \
  -f null - 2>&1 | grep -o "YAVG=[0-9.]*" | cut -d= -f2 > lum.txt
```

Y sobre `lum.txt`, contar los máximos locales que superen la mediana en más de 15. Ese número tiene que
ser **exactamente** el cupo que decidiste en el §1. Ni uno más, ni uno menos.

---

## Errores frecuentes

- **Decidir el número al final.** Cuando llegas a quitar ya te has acostumbrado y no quitas ninguno.
- **Escalar la densidad con la duración.** En una pieza larga la densidad baja, no se mantiene.
- **Poner destellos en piezas de menos de 15 s.** Compiten con los cortes y pierden los dos.
- **Contar el destello como "un minuto de trabajo".** Bien hecho son once, con la medición y el sonido.
- **Añadir uno más "porque ahí queda bien".** Si queda bien, cambia otro de sitio. El cupo no sube.
- **Quitar por gusto en vez de por orden.** El orden del §4 quita primero lo que no se puede defender.
- **Gastar el presupuesto en afinar y no en colocar.** Mover un destello a la palabra correcta vale diez
  veces más que subirle la fuerza dos centésimas.
- **No contar los picos del render final.** Es la única forma de saber que lo entregado es lo diseñado.

---

## Relacionado

- `430` — la jerarquía: cuál de los del cupo lleva el 0,22.
- `431`, `432` — la curva y la medición que sostienen el recuento del §6.
- `433` — el sonido, que es lo que hace que un destello cueste once minutos y no dos.
- `434`, `435`, `436` — los otros recursos de luz que compiten por el mismo presupuesto.
- `438` — el techo de seguridad, que va por encima de este cupo.
- `269` — el presupuesto del esfuerzo en general. `209` — cuándo el motion sobra, que es el mismo
  razonamiento aplicado al movimiento.
- `canales_lushows` `18-densidad-por-tipo-de-bloque.md` y `191-el-cupo-por-escenario.md` — cómo el motor
  del canal documental reparte cupos por bloque, que es esta misma idea generalizada a todos los
  recursos.
