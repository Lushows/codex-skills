# 63 · Comparaciones visuales

**Qué resuelve:** una cifra grande no se entiende, se acepta. "Doce mil millones" y
"ochenta mil millones" producen exactamente la misma sensación: *mucho*. La comparación
es lo que convierte una cifra en una imagen, y es el aporte original del canal — el
dato lo tiene cualquiera; la comparación la hicimos nosotros.

---

## El método: cuatro familias, y se elige una

| Familia | Convierte la cifra en | Sirve cuando |
|---|---|---|
| **Escala humana** | Un cuerpo al lado | Hay volumen, peso o altura físicos |
| **Objeto conocido** | Camiones, aviones, casas, campos de fútbol | El espectador ya sabe cuánto mide eso |
| **Superficie** | Cuántas manzanas de ciudad, cuánto terreno | La cifra es de área, o se puede convertir |
| **Tiempo** | Cuánto tardarías en contarlo / ganarlo | La cifra es dinero y el público cobra un sueldo |

**Se elige UNA por cifra.** Dos comparaciones seguidas de la misma cifra se anulan: el
espectador deja de calibrar y vuelve a "mucho".

## Cómo se elige la correcta

1. **¿Qué magnitud es en realidad?** Dinero en efectivo tiene peso y volumen; dinero en
   una cuenta no tiene ninguno. Comparar un saldo bancario con camiones es mentir.
2. **¿El referente lo conoce el espectador sin explicación?** Un campo de fútbol sí; una
   hectárea no. Si hay que explicar el referente, no es un referente.
3. **¿La proporción es legible?** Una comparación que da 0,7 o 1.400.000 no se ve.
   El rango que funciona en pantalla es **entre 3 y 60 unidades**. Fuera de ahí hay que
   cambiar de referente, no encoger el dibujo.
4. **¿El referente es del mundo de la historia?** Si el caso es de narcotráfico, los
   camiones y los aviones ya están en el relato. Un referente prestado de otro universo
   (elefantes, ballenas) rompe el tono.

## La cuenta se hace, se guarda y se cita

La comparación es un cálculo propio, así que **es responsabilidad nuestra**. Antes de
dibujar nada:

```python
# comparacion.py — se ejecuta y su salida se pega en fuentes.json
from decimal import Decimal as D

cifra   = D("12600000000")     # dato del expediente, con su fuente
unidad  = D("100")             # denominación del billete
peso_u  = D("...")             # gramos por billete — CONSTANTE CON FUENTE
grosor  = D("...")             # milímetros por billete — CONSTANTE CON FUENTE

n       = cifra / unidad
peso_kg = n * peso_u / 1000
alto_m  = n * grosor / 1000
print(f"billetes={n:,.0f}  peso={peso_kg/1000:,.1f} t  altura={alto_m:,.0f} m")
```

Las constantes (peso y grosor de un billete, capacidad de un camión, altura de un
edificio) **no se ponen de memoria**: se buscan en la fuente oficial del emisor o del
fabricante y se anotan en `archivo/fuentes.json` junto al resultado. Un error aquí es
un error factual en pantalla, y es el tipo de error que hunde un canal de documentales.

**Se redondea hacia abajo y se dice el redondeo.** "Más de 120 toneladas" es defendible;
"126,4 toneladas" obliga a defender el decimal.

## Cómo se dibuja

La estructura de una comparación tiene siempre tres partes, y ninguna es opcional:

```
[ LA COSA ]   [ EL REFERENTE ]   [ EL RÓTULO QUE DICE QUÉ ES CADA UNA ]
```

`camiones` y `altura` en `fx.py` son las dos plantillas ya construidas. El patrón:

```python
def comparacion(nombre, n, glifo, rotulo, titulo, w_u=300, h=420, sep=70):
    """n copias de un mismo objeto en fila, rotuladas, con titular arriba."""
    w = 40 + n*(w_u + sep)
    piezas = "".join(f"""
  <div class="l" style="left:{40+i*(w_u+sep)}px;top:150px;width:{w_u}px;height:150px">
    {glifo}
    <div class="l mono oro" style="left:0;top:178px;width:{w_u}px;text-align:center;
         font-size:19px;letter-spacing:.14em">{rotulo}</div>
  </div>""" for i in range(n))
    return (w, h, f"""
<div style="position:relative;width:{w}px;height:{h}px">{piezas}
  <div class="l mono papel" style="left:0;top:16px;width:{w}px;text-align:center;
       font-size:24px;letter-spacing:.28em;opacity:.8">{titulo}</div>
</div>""")
```

**La silueta humana es la que da la escala**, y va en el mismo PNG que el referente: si
entra como elemento aparte, el motor la escala por su cuenta y la proporción se pierde.

### Entrada: los referentes entran de uno en uno

Un dibujo con tres camiones que aparece completo se lee como ilustración. Tres estados
acumulativos (`cadena_serie`, `61`) con `paso` 0,35-0,5 s se leen como **cuenta**: uno,
dos, tres. Es el mismo recurso del redactado (`62`) y del diagrama por pasos (`65`).

## Comparación por tiempo

La única que no se dibuja con objetos. Se resuelve con texto grande y una unidad que el
espectador tenga en el cuerpo:

```
SI GANARAS  $50.000 AL DÍA
TARDARÍAS   690 AÑOS
```

Dos líneas, monoespaciada, alineadas por la izquierda en dos columnas. La segunda línea
entra **después** (`41`, máquina de escribir) porque el remate es la cifra de tiempo,
no la premisa. Cuidado: la premisa tiene que ser un número redondo e inventado a
propósito ("si ganaras X"), y decirse como hipótesis, nunca como dato.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Dos comparaciones seguidas de la misma cifra | Se anulan: el espectador deja de calibrar |
| Comparar un saldo bancario con peso o volumen | Es falso: ese dinero nunca fue papel |
| Referente que hay que explicar (hectárea, tonelada métrica) | Se gasta la frase en el referente y no en la historia |
| Proporciones fuera del rango 3-60 | O no se ve la diferencia, o no cabe |
| Constantes de memoria | Error factual con la voz confirmándolo |
| Decimales en la comparación | Obliga a defender una precisión que no se tiene |
| Silueta humana como elemento aparte | El motor la escala solo y la escala se pierde |
| Referente de otro universo (elefantes) | Rompe el tono del caso |
| El dibujo sin rótulo | Un camión sin "40 t" es un camión, no un dato |

## Relacionado

`61` efectos de dinero · `44` la cifra en pantalla · `92` el aporte original · `96` verificación de datos · `27` composición de datos
