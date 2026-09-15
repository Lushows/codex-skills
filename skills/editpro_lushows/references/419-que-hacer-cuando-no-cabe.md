# 419 · Qué hacer cuando no cabe

**Qué resuelve:** el mapa de intocables está hecho (`410`), las bandas están medidas (`415`, `416`,
`418`) y el contenido **no entra**. Este es el momento donde se toman las dos peores decisiones del
oficio: encoger la letra por debajo del suelo, o bajar el rótulo a la banda vetada «sólo un poco». Las
dos son invisibles en el monitor y las dos se ven en el teléfono. Aquí está la escalera que hay que
subir en su lugar, en orden, y el cálculo que dice si de verdad no cabe.

---

## Primero: demostrar que no cabe

«No cabe» suele ser una impresión. Es aritmética, y responde sola:

```python
util  = SUELO * H - ARRIBA                    # 0,72·H para 16:9 (416); ver 45 para 9:16
pila  = sum(w * ih/iw for n, w in PILA) + HUECO * (len(PILA) - 1)
```

Ejecutado el **11-sep-2026** sobre cuatro piezas reales del episodio piloto (1920×1080):

```
banda útil: y 96 a 778  =  682 px  (0.631 de la altura)
  d_fecha      mostrada a  1380 px -> alto   306 px  (0.284)
  m_consta     mostrada a   760 px -> alto   220 px  (0.203)
  r_casilla    mostrada a   968 px -> alto   216 px  (0.200)
  linea_06     mostrada a  1120 px -> alto   685 px  (0.634)
  huecos 3 x 24 px
pila = 1499 px · útil = 682 px · NO CABE, sobran 817 px
```

Y el dato que cambia la conversación: **`linea_06` mide ella sola 685 px, más que toda la banda útil**.
No hay reorganización posible; hay que rehacer esa pieza o sacarla del plano. Saberlo antes de mover
nada ahorra la media hora de empujar rótulos.

---

## La escalera, en orden

Se sube de arriba abajo. No se salta un peldaño porque el siguiente parezca más cómodo.

| # | Movimiento | Cuándo | Coste |
|---|---|---|---|
| **1** | **Acortar el texto** | Casi siempre. Tres palabras dicen lo que ocho | Gratis, y el resultado es mejor |
| **2** | **Subir el elemento** | Cuando hay sitio arriba y no hay cara | Gratis |
| **3** | **Repartir en el tiempo** | Dos datos seguidos en vez de dos datos a la vez | Unos segundos de duración |
| **4** | **Rehacer la pieza más estrecha o más baja** | Cuando una sola pieza se come la banda | Regenerar el PNG |
| **5** | **Cambiar el plano** | Cuando el problema es el fondo, no el texto | Un plano nuevo |
| **6** | **Cambiar de formato** | Cuando el contenido es ancho y el destino estrecho (`417`) | Una tabla de eventos aparte |
| **7** | **Renunciar al dato** | Cuando los seis anteriores fallan | El dato sobraba |

El 7 no es una derrota: es la conclusión correcta de `canales_lushows/49` — *si un dato no cabe a su
cuerpo mínimo, el dato sobra o el bloque está mal compuesto; nunca se resuelve reduciendo el cuerpo.*

### El 1 es el que resuelve el 80%
Acortar es el único peldaño que además **mejora** la pieza. «Certificado de defunción · casilla 20» son
36 caracteres; «casilla 20» son 10, y con la pieza al lado se entiende igual. En una pieza mono a 38 px
con interletra 0,14, cada carácter avanza ~26 px: veintiséis caracteres menos son **676 px de ancho**
que dejas de necesitar, y por tanto una pieza que se muestra más grande y se lee mejor.

---

## Los tres movimientos prohibidos

| Movimiento | Por qué está prohibido |
|---|---|
| **Bajar el cuerpo** por debajo del suelo (`412`) | Deja de ser texto y pasa a ser textura. Y no avisa |
| **Meterse en la banda vetada** «sólo un poco» | La barra no es semitransparente: tapa (`416`) |
| **Estrechar la pieza** para que quepa a lo ancho | Estrechar el PNG mostrado reduce el cuerpo en pantalla en la misma proporción: es bajar el cuerpo con otro nombre |

El tercero es el que se cuela, porque parece un cambio de tamaño y es un cambio de legibilidad. La
fórmula de `412` lo delata en una línea.

---

## Cuando no cabe por ancho

El mismo problema en el otro eje, y una salida que no existe en el vertical: **partir en dos líneas**.
Una pieza de dos líneas ocupa la mitad de ancho y el doble de alto, así que sólo sirve si el
presupuesto que sobra es de alto. Antes de partir, se comprueba con el mismo cálculo.

Y la regla dura del ancho: **el ancho de una pieza de texto se calcula, nunca se fija**. Un ancho fijo
corta la última letra sin dar error —le costó al motor del canal doce rótulos— y además obliga a
recortar el cuerpo cuando el texto crece.

---

## El caso de los cuatro formatos

Si la pieza no cabe en uno solo de los destinos, la respuesta casi nunca es rediseñarla para el peor:
es **aceptar dos versiones**. Un rótulo ancho para el 16:9 de Paper Empires y uno corto para el corte
vertical cuesta una línea en la tabla de eventos; forzar el ancho a caber en 608 px lo vuelve ilegible
en los dos. Ver `417` y el flujo de texto como capa suelta de `38`.

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Encoger la letra «un poco» | Se cruza el suelo y nadie se entera hasta el teléfono |
| Estrechar la pieza para que quepa | Es encoger la letra, disfrazado |
| Meter el rótulo en la banda vetada | La barra lo tapa entero, no a medias |
| Empezar a empujar elementos sin hacer la cuenta | Se descubre a los veinte minutos que una pieza sola no cabe |
| Saltarse el peldaño 1 | Se rehacen piezas para un texto que sobraba |
| Fijar el ancho de la pieza de texto | Se corta la última letra sin error |
| Diseñar para el peor formato | Ilegible en todos en vez de correcto en cada uno |
| Tratar la renuncia al dato como un fracaso | Es el resultado correcto de un plano sobrecargado |

## Relacionado

`410` el mapa de intocables · `412` el suelo de cuerpo y la fórmula · `416` la banda vetada del 16:9 ·
`417` cuando el problema es el formato · `376` legibilidad real en móvil ·
`canales_lushows/49` los mínimos por tipo de texto
