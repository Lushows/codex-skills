# 414 · Subtítulos quemados o cerrados: la geometría, no la decisión

**Qué resuelve:** cuál de los dos usar ya está decidido en `95` —quemados en vertical corto, cerrados
en YouTube largo, y casi siempre **los dos**— y no se repite aquí. Lo que `95` no cubre es el problema
geométrico, que es el que de verdad rompe piezas: **el subtítulo quemado y el subtítulo automático de
la plataforma se pelean por la misma franja**, y esa franja es justo la que ninguna de las dos zonas
seguras te deja usar.

---

## Las tres capas de texto que acaban apiladas abajo

| Capa | Quién la pinta | Se puede mover |
|---|---|---|
| Tu subtítulo quemado | Tú, dentro de los píxeles | Sí, es lo único que controlas |
| El subtítulo automático de la red | La plataforma, si el espectador lo activa | No |
| El caption / descripción | La plataforma, siempre | No, y **crece** con el texto |

Las tres viven en el tercio inferior. La consecuencia práctica: **tu subtítulo tiene que estar por
encima de las otras dos**, no «abajo pero un poco más arriba». En 1080×1920 eso significa la línea base
entre el 55% y el 70% de la altura (`95`), es decir, entre **380 y 500 px del borde inferior** —y con
caption largo o en pauta, más cerca de 500 que de 380.

---

## La trampa que se come la mitad de los subtítulos quemados

El filtro `subtitles=` de ffmpeg **no trabaja en píxeles de tu lienzo**. Un `.srt` no declara
resolución, así que libass usa un lienzo virtual y escala. Todo lo que pongas en `force_style` —
`FontSize`, `MarginV`, `Outline`— está en unidades de ese lienzo virtual, no en las tuyas.

Medido el **11-sep-2026**, quemando sobre un lienzo de 1080×1920 y leyendo con PIL la fila más baja de
píxeles del texto:

```
por defecto      y 1658-1851  (0.864-0.964)  base a  68 px del borde
MarginV= 20  ->  base  134 px del borde · alto de línea 48 px
MarginV= 30  ->  base  200 px del borde · alto de línea 48 px
MarginV= 90  ->  base  600 px del borde · alto de línea 48 px
factor medido: 6.657 px de lienzo por unidad de MarginV   (1920/288 = 6.667)
MarginV=440  ->  NADA EN PANTALLA
```

Tres cosas, todas graves:

1. **Por defecto el subtítulo cae en y 0,864–0,964**, es decir, de lleno bajo el caption y los botones.
   El comportamiento por defecto de ffmpeg es el peor sitio posible.
2. `MarginV=440` —el valor que uno escribiría pensando en píxeles, y que aparece tal cual en los
   ejemplos de `95`— **manda el texto fuera de pantalla y no da ningún error**. El render sale bien,
   el archivo pesa, y no hay subtítulo.
3. El factor es `alto_del_vídeo / 288`. Para una base a 440 px reales sobre 1920: `MarginV = 66`.

```bash
# base a 440 px reales, cuerpo ~54 px reales, sobre lienzo de 1080x1920
ffmpeg -i video.mp4 -vf "subtitles=subs.srt:force_style=\
'FontSize=8,Outline=1,Alignment=2,MarginV=66'" -c:a copy salida.mp4
```

Si prefieres pensar en píxeles de verdad, el camino limpio es un `.ass` con `PlayResX: 1080` y
`PlayResY: 1920` declarados: ahí `MarginV: 520` sí son 520 px (`45`, y ojo a la trampa de reescalado
que ese módulo describe).

### Calibrar en vez de deducir

El factor teórico y el medido no coincidían exactamente (6,657 contra 6,667: el descuento del
descendente). No se deduce, se calibra con dos puntos:

```python
k = (base_2 - base_1) / (margin_2 - margin_1)
margin = (objetivo - base_1) / k + margin_1
```

Dos renders de un fotograma y ya sabes el valor exacto para tu combinación de lienzo y fuente.

---

## El caso de 16:9 (Paper Empires, vídeos de la calculadora)

En horizontal el enemigo no es el caption: es la **barra de progreso del reproductor** (`416`). El
subtítulo quemado de un 1920×1080 debe tener su línea base **por encima de `H·0,72` = 778 px**, no en
los 60-80 px del borde inferior que usa la convención de cine. Con cuerpo de 44 px eso da una base
razonable en `y ≈ 720`, unos **360 px del borde inferior**.

Y aquí el subtítulo **cerrado** gana por geometría, no por accesibilidad: YouTube coloca sus CC por
encima de sus propios controles, esquivando la barra solo. Si el vídeo va a YouTube largo, quemar el
subtítulo es asumir a mano un problema que la plataforma ya resuelve. Quemado en los cortes verticales,
cerrado en el episodio horizontal.

---

## Verificar dónde cayó de verdad

No se mira: se mide, sobre el fotograma renderizado.

```python
a = np.array(Image.open("frame.png").convert("L"))
filas = np.where(a.max(axis=1) > 80)[0]
print(f"texto y {filas.min()}-{filas.max()} ({filas.min()/H:.3f}-{filas.max()/H:.3f})")
print(f"base a {H-1-filas.max()} px del borde inferior")
```

Sobre un fondo plano es exacto; sobre imagen real se hace con la diferencia entre el fotograma con
subtítulo y el mismo sin él. Es la única forma de saber que el bloque de dos líneas más largo del
`.srt` —no el primero— sigue estando donde debe.

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Escribir `MarginV=440` pensando en píxeles sobre un `.srt` | El subtítulo se va fuera de pantalla sin un solo aviso |
| Dejar el `MarginV` por defecto | Cae en 0,864–0,964: bajo el caption y los botones |
| Deducir el factor de escala en vez de calibrarlo | Falla por el descendente y por la fuente |
| Quemar subtítulos en un 16:9 para YouTube | Chocan con la barra; los CC de la plataforma ya la esquivan |
| Verificar con el primer bloque del `.srt` | El problema está en el bloque de dos líneas más largo |
| Quemar y además dejar activo el automático de la red | Dos subtítulos apilados, ilegibles los dos |
| Subir el subtítulo tanto que tape la cara | Se cambia un intocable por otro (`411`) |
| Comprobar mirando en vez de midiendo filas de píxeles | «Se ve bien» no distingue 380 de 500 px |

## Relacionado

`95` quemados contra cerrados, `.srt`, indexación y velocidad de lectura · `45` `MarginV` y la trampa
de `PlayResX/Y` · `416` la barra del reproductor en 16:9 · `412` el suelo de cuerpo ·
`376` contorno contra sombra · `410` el mapa de intocables
