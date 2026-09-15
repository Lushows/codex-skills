# 410 · El mapa de los intocables

**Qué resuelve:** «zona segura» suena a rectángulo, y un rectángulo no decide nada. Lo que hace falta
es un **inventario de objetos con prioridad** y las **tres amenazas distintas** que se los comen. El
módulo `45` da las cifras de cada red; éste da el mapa y la comprobación. Si sólo se lee uno, que sea
el `45` para saber cuánto, y éste para saber **qué** y **cómo se demuestra**.

---

## Las tres capas que todo el mundo confunde

Un elemento puede desaparecer por tres motivos incompatibles entre sí. Se diagnostican por separado
porque se arreglan de maneras opuestas.

| Capa | Quién se lo come | Dónde se ve | Se arregla |
|---|---|---|---|
| **1 · Interfaz** | La plataforma pinta encima: caption, iconos, barra de progreso, botón de suscribirse | Sólo en el reproductor real, nunca en el tuyo | Moviendo el objeto dentro del lienzo (`45`) |
| **2 · Recorte** | El feed, la cuadrícula o el corte vertical se llevan lo que está fuera de la ventana | Al exportar otro formato | Componiendo en la columna que sobrevive (`417`) |
| **3 · Propio** | Tu propio montaje: un rótulo encima de otro, un recorte encima de una cara | En tu monitor, si miras | Reordenando la tabla de eventos |

La capa 3 es la única que puedes ver sin salir de casa, y es justamente la que menos se revisa.

---

## El inventario: qué es intocable y cuánto aguanta

No todo pesa igual. Una cara medio tapada sigue funcionando; un precio medio tapado es un precio
perdido. Esta es la escala de tolerancia a la oclusión, en tanto por uno de la superficie del objeto:

| Objeto | Tolerancia | Por qué |
|---|---|---|
| Cifra, precio, número de teléfono | **0,00** | Un dígito tapado cambia el dato, no lo degrada |
| Texto en pantalla, CTA | **0,00** | Se lee entero o no se lee (`412`) |
| Ojos del sujeto | **0,00** | Con los ojos tapados la cara deja de ser una cara (`411`) |
| Subtítulo quemado | 0,00 | Además compite con el subtítulo automático de la red (`414`) |
| Marca o firma | 0,10 | Se reconoce por silueta; un mordisco no la mata (`413`) |
| Resto de la cara | 0,35 | Boca y mentón tapados: sigue leyéndose |
| Producto | 0,25 | Si se reconoce la forma, aguanta |
| Fondo, textura, ambiente | 1,00 | Para eso está la zona muerta |

Escríbelo por proyecto en un `intocables.json` con prioridad de 1 a 5. Sin archivo no hay auditoría:
lo que no está declarado, nadie lo comprueba, y aprueba por ausencia.

```json
{"retrato_lustig": 5, "d_fecha": 5, "d_preso": 4, "m_consta": 4,
 "r_sinfuente": 3, "sello_consta": 3, "ficha_policial": 2}
```

---

## Cruzar el inventario contra las tres capas

Sobre el motor del canal documental (`CANALES-LUSHOWS/piloto`), donde cada elemento declara recurso,
posición y anchura, el cruce es aritmética. Ejecutado el **11-sep-2026** sobre `ep01-lustig`:

```python
BARRA = (0.78*H, 0.86*H)                  # capa 1 · lo que pinta el reproductor
VENT9 = (W/2 - H*9/32, W/2 + H*9/32)      # capa 2 · lo que se lleva el corte vertical

def solapa(A, B):   # en ESPACIO y en TIEMPO: compartir escena no es coincidir
    return (min(A[4],B[4]) - max(A[2],B[2]) > 0 and min(A[5],B[5]) - max(A[3],B[3]) > 0
            and min(A[7],B[7]) - max(A[6],B[6]) > 0.2)

for nombre, prio in sorted(INT.items(), key=lambda kv: -kv[1]):
    for k in [c for c in cajas if c[0] == nombre]:
        c1 = k[5] > BARRA[0] and k[3] < BARRA[1]                  # entra en la barra
        c2 = not (k[2] >= VENT9[0] and k[4] <= VENT9[1])          # se sale al recortar
        c3 = [o[0] for o in cajas if o is not k and solapa(k, o)] # lo tapa lo mío
```

Salida real:

```
intocable            prio  capa 1 barra | capa 2 corte 9:16 | capa 3 propio
retrato_lustig          5  TAPA         | SE CORTA          | ok
d_fecha                 5   ok          | SE CORTA          | casilla_hospital, reloj_1947
d_preso                 4  TAPA         | SE CORTA          | ok
m_consta                4  TAPA         | SE CORTA          | linea_00
sello_consta            3  TAPA         | SE CORTA          | ok
```

Dos lecciones del propio arnés: **sin la condición de tiempo salían 9 colisiones de capa 3 y con ella
quedan 5** — compartir escena no es coincidir en pantalla. Y la segunda: la capa 2 marca «SE CORTA»
en todo, porque este episodio es 16:9 y la ventana vertical es el 0,316 del ancho. Eso no es un fallo
del episodio: es la respuesta correcta a «¿puedo sacar el vertical recortando?». No (`417`).

---

## El orden de trabajo

1. **Declarar** los intocables antes de montar, no después. Cinco líneas de JSON.
2. **Medir** la interfaz de las superficies a las que va (`415`, `418`), con fecha.
3. **Colocar** dentro del mapa resultante.
4. **Cruzar** el inventario contra las tres capas y arreglar por prioridad descendente.
5. **Verificar en el reproductor real**, que es lo único que no discute (`418`).

Y cuando el paso 3 no cabe, no se encoge el texto ni se baja a la banda vetada: se aplica la escalera
de `419`.

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Tratar la zona segura como un rectángulo y no como un inventario | Se protege el sitio y se pierde el objeto |
| Confundir la capa 1 con la capa 2 | Se mueve el elemento dentro del lienzo y sigue muriendo al recortar |
| No declarar los intocables | Lo que no está en la lista aprueba por ausencia |
| Comprobar el solape sólo en espacio | Colisiones falsas: dos elementos de la misma escena que nunca coinciden |
| Dar la misma tolerancia a una cara y a una cifra | Se sacrifica el dato para salvar el ambiente |
| Revisar sólo la capa 3, que es la que se ve en el monitor | Las dos que de verdad se comen el trabajo son invisibles en casa |
| Medir una vez y dar los números por eternos | Las interfaces crecen; sin fecha, la tabla es una trampa |
| Auditar por elemento en vez de por prioridad | Se arreglan cinco rótulos de relleno y se deja la cifra tapada |

## Relacionado

`45` cifras por plataforma · `411` caras · `412` texto y cifras · `413` marca · `415` medir la interfaz ·
`417` reencuadre entre formatos · `418` el protocolo de medida · `419` cuando no cabe ·
`376` legibilidad en milímetros
