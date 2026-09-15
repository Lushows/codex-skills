# 405 · El lienzo no es el marco (zona segura en 16:9)

**Qué resuelve:** dónde se puede poner un texto en el episodio horizontal. El módulo §
`202` trata el vertical y dice, con razón, que el canal todavía no ha medido sus propias
zonas. Este trata el **16:9**, que es donde vive el episodio y donde nadie miraba.

---

## El fallo, con sus números

12-sep-2026. Luis, viendo el episodio 1: *«veo textos títulos fuera del marco»*. Lo vio
él; las dieciséis medidas del auditor decían que no pasaba nada. Medido después:

| | |
|---|---|
| textos que pisaban el margen del 5% | **29** |
| textos que salían del lienzo de 1920×1080 | **11** |
| la línea de tiempo (`linea_00`, `02`, `06`) llegaba a | **y = 1104** — 24 px *por debajo* del borde |
| el rótulo del gancho (`t_aprendiz`) empezaba en | **x = −42** |

Los `−42` y los `+24` no eran casualidad: son **exactamente** `SANGRE = 0.022` sobre
1920 y 1080. El motor no se equivocaba — hacía lo que se le había dicho. Lo que estaba
mal era decírselo al texto igual que a una foto.

## La distinción que faltaba

> Un recorte que se sale por un borde se lee como una página pegada fuera de la hoja: es
> lenguaje de collage y suma (§ `291`). **Un texto que se sale es texto que no se lee.**

```python
# diccionario.py · rect()
if es_texto(recurso):
    sx0, sy0, sx1, sy1 = zona_segura()          # el texto NO sangra nunca
    x = min(max(x, sx0), max(sx0, sx1 - ancho))
    y = min(max(y, sy0), max(sy0, sy1 - alto))
else:
    mx, my = W_LIENZO * SANGRE, H_LIENZO * SANGRE   # el recorte sí
```

`es_texto()` ya existía para otra cosa (el texto no admite el mismo solape que una foto).
Aquí se reutiliza: **una sola definición de "esto lleva texto"**, no dos que se desalineen.

## Los márgenes, y por qué el de abajo es mayor

```python
SEGURO = {"izq": 0.05, "der": 0.05, "arriba": 0.05, "abajo": 0.08}
# sobre 1920×1080 -> la zona útil es (96, 54) a (1824, 994)
```

Qué pinta el reproductor encima del episodio, y por eso cada margen:

| Borde | Qué se le superpone |
|---|---|
| **abajo** | barra de progreso y controles; en móvil están casi siempre visibles. Es el único borde con interfaz permanente, por eso 8% y no 5% |
| arriba | el título del vídeo en móvil mientras se toca la pantalla |
| derecha | tarjetas y el icono de información, arriba a la derecha |
| todos | cualquier app que reencuadre, y el overscan de una tele |

**Honestidad sobre estas cifras:** el 5/5/5/8 es la práctica clásica de *title-safe*
(90% del cuadro) más un punto extra abajo por la barra. **No está medido sobre capturas
propias del canal**, igual que las del vertical (§ `202`). La diferencia es que aquí los
márgenes son conservadores por construcción: nadie pierde nada por dejar 96 px de aire, y
el defecto que corrigen era de 138 px. Cuando se haga la medición con la carta fiducial
de § `202`, se sustituyen aquí y en ningún otro sitio.

## La medida que ahora lo vigila

En `auditar.py`, junto a las otras dieciséis:

```
TEXTO fuera de zona segura        0   (objetivo 0 · margenes 5% lados, 8% abajo)
```

Reporta el elemento, los píxeles que se pasa y **por qué lado**, para poder arreglarlo
sin abrir el vídeo.

## La lección general

Este fallo llevaba dos episodios en pantalla y el auditor medía *fuera de cuadro* desde
el principio — pero medía contra **el lienzo**, y el lienzo no es el marco. Una medida
puede estar bien calculada, dar cero y no servir de nada porque compara contra la
frontera equivocada.

> Cuando el usuario ve un fallo que la auditoría no ve, la pregunta no es «¿falta una
> medida?» sino «¿contra qué está comparando la que ya hay?».

## Relacionado

§ `202` (la zona segura real de cada red · vertical) · § `200` (el vertical se renderiza,
no se recorta) · § `291` (el borde de papel) · § `140` (control de calidad) · § `86`
(medir el audio — el mismo tipo de fallo, en sonido) · § `242` (colocación por rectángulo)
