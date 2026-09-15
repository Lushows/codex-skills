# 271 · Las dos columnas en pantalla

**Qué resuelve:** que la separación entre lo probado y lo contado **se vea**. Si vive
solo en la voz, el método no existe: el espectador que mira sin escuchar —que son
muchos— recibe la leyenda como si fuera un hecho. Este módulo es el diseño del árbitro.

---

## La regla

> Todo lo que entra en pantalla declara en qué columna vive.

Está escrita en la cabecera de `fx_lustig.py`, no en una nota: *lo que consta va en papel
`#EDE6D6` con línea continua; lo que se cuenta va en gris `#B3A891` con línea punteada.
Nunca se mezclan los dos tratamientos sin rótulo que los distinga.*

## Las dos marcas no comparten nada

`m_consta` y `m_cuenta` son dos tarjetas de 900×260 px y están construidas para que no
puedan confundirse ni de reojo. No se diferencian en un rasgo: se diferencian en todos.

| | `m_consta` | `m_cuenta` |
|---|---|---|
| **Tipografía** | monoespaciada, `.16em` de espaciado | serif de revista |
| **Papel** | limpio, degradado corto | amarillento, tres radiales de mancha |
| **Geometría** | escuadra perfecta, cero curvas | borde gastado por `clip-path`, 19 vértices |
| **Ángulo** | +2,2° | −1,7°, ladeado |
| **Filo** | borde de tinta de 3 px | sin borde: papel arrancado |
| **Detalle** | lomo rojo de archivador y dos perforaciones | doble filete de cabecera |
| **Remate** | sello de archivo, doble aro, **sin palabras** | filete rojo corto |
| **Temperatura** | fría | cálida |

Dos decisiones que parecen menores y no lo son:

- **El sello no lleva texto.** Un sello que dijera algo estaría inventando un dato que el
  documento no tiene. Dice «esto pasó por un archivo», y nada más.
- **Las perforaciones.** Son la marca de que ese papel estuvo dentro de un expediente. Un
  detalle de tres píxeles que hace todo el trabajo semántico de la tarjeta.

El resto del sistema repite la misma oposición sin volver a usar las tarjetas: los sellos
`sello_consta` (**VERIFICADO**, oro) y `sello_falta` (**SIN FUENTE**, rojo), y el fondo
del bloque final `f_metodo`, que es tinta **partida en dos por una línea roja de 5 px**:
mitad izquierda fría, mitad derecha ámbar. El fondo enuncia el método antes de que la voz
lo nombre.

## Son motivos declarados, no repetición

Las marcas vuelven cada vez que se cambia de terreno, y esa vuelta es lo que enseña al
espectador a leerlas. Por eso están en `MOTIVOS` y el auditor **no las cuenta como
contenido repetido**:

```python
MOTIVOS = {"m_consta", "m_cuenta", "linea"}
```

La mecánica —declarar por familia, no por nombre; por qué mirar solo el nombre completo
haría que la línea de tiempo se bloquease a sí misma— está en § `254` y no se repite
aquí. Lo que importa en este módulo es el criterio: **una marca de columna cumple las
tres pruebas del motivo** (significa lo mismo cada vez, vuelve en un sitio elegido, el
espectador aprende con la vuelta). Es el caso de manual.

## La línea de tiempo: la columna hecha cronología

`linea_00 … linea_06` son siete estados acumulativos del mismo gráfico. Cada hito se
dibuja según su columna:

| | Hito que **consta** | Hito que **se cuenta** |
|---|---|---|
| Punto sobre el eje | relleno de oro, borde sólido | hueco, borde punteado |
| Tallo y tarjeta | línea continua, papel al 10% | punteada, papel al 4% |
| Chapa | `CONSTA` en oro | `SE CUENTA` en gris |
| Año | 56 px | 36 px si dice `SIN FECHA` |

De los cinco hitos, tres constan y dos no. Y el segundo de ellos es la mejor decisión del
episodio: **la condena federal por falsificación va sin año**. El certificado prueba el
oficio —casilla 10— pero no dice cuándo lo condenaron; 1935 no lo respalda ningún
documento nuestro. Poner esa fecha sería cometer exactamente lo que el episodio denuncia.
El estado `linea_06` no añade hito: marca en rojo, con el rótulo `SIN FUENTE PRIMARIA`,
los dos que no tienen papel detrás.

La balanza `balanza_00 … balanza_05` hace lo mismo en una sola imagen: dos platos —`LO QUE
CONSTA` con documento, `LO QUE SE CUENTA` con bloques— y un contador al pie que cambia de
gris a rojo: **AFIRMACIONES SIN FUENTE PRIMARIA · n DE 5**.

## Dónde caen, medido

Sobre la tabla de eventos del minuto 1 resuelta contra la locución (63,45 s, 59 elementos):

```
CONSTA     4 marcas ·  9.37 s en pantalla (14.8%) · en 0.60 · 17.94 · 58.15 · 60.68
SE CUENTA  3 marcas ·  7.32 s en pantalla (11.5%) · en 34.58 · 48.74 · 60.68
```

Se lee la estructura entera del tramo: el episodio abre en la columna del papel a los
0,6 s, sella el gancho en 17,94, cruza a la leyenda en 34,58 —**antes** de que la torre
entre en pantalla—, remata la leyenda con el rótulo rojo `r_sinfuente` en 48,74, y en
60,68 las dos marcas entran **a la vez y una a cada lado del cuadro** sobre el fondo
partido: ese plano es la tesis del episodio.

## Las cuatro reglas de colocación

1. **La marca entra antes que la pieza que califica.** `m_cuenta` cae en «versión»
   (34,58 s) y la torre llega después. Al revés, el espectador ya ha creído la imagen.
2. **La marca no se cruza con otra pieza de marca.** `m_consta` del bloque 1 se movió de
   `H*0.72` a `H*0.10` porque abajo tapaba un 19% de la línea de tiempo durante 2,2 s —y
   además rozaba la banda donde la plataforma pinta su barra—. Las dos eran de mano, así
   que nadie las había comprobado una contra otra.
3. **La marca no se apaga sola.** Vale 3 s en pantalla, pero el estado que declara dura
   hasta la siguiente marca. El espectador asume continuidad (§ `273`).
4. **Las dos juntas solo en el plano del método.** Fuera de ahí, verlas a la vez es
   exactamente lo que el episodio promete no hacer.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Marcas que comparten tipografía o papel | A 1920 px en un collage se leen igual: el método desaparece |
| Meter texto en el sello de archivo | Se inventa un dato que el documento no dice |
| Poner la marca después de la imagen de la leyenda | La imagen ya afirmó; la marca llega de descargo |
| Dibujar un hito con una fecha que no consta | El episodio comete lo que denuncia |
| Tratar las marcas como repetición | El auditor da alarma en falso y se aprende a ignorar la lista (§ `143`) |
| Sacar las dos marcas juntas «porque queda bonito» | Se pierde el único plano donde significan juntas |
| Colocar una marca sin comprobarla contra las otras piezas de mano | 19% tapado durante 2,2 s y nadie lo ve hasta la grilla |

## Relacionado

`270` el método · `273` marcar sin aburrir · `275` el hueco rotulado ·
`254` motivos · `126` el tema del episodio · `43` rótulos y etiquetas ·
`44` la cifra en pantalla · `50` sistema de fondos · `160` la grilla de fotogramas
