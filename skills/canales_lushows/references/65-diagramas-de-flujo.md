# 65 · Diagramas de flujo

**Qué resuelve:** explicar un mecanismo — cómo se lavaba el dinero, cómo entraba la
mercancía, cómo se movía el papel — sin que el espectador tenga que leer cinco cajas de
golpe. El diagrama **se construye ante la cámara**, un paso por vez, al ritmo de la voz.

---

## El problema del `flujo` actual

`fx.py` tiene `flujo`: los cinco pasos del lavado, ya completos, en un PNG. Funciona
como resumen, pero se lee en dos segundos y la voz tarda diez en explicarlo — así que
durante ocho segundos el espectador ya terminó y está esperando. Y peor: lee el paso 5
mientras oye el paso 1.

**La regla:** el espectador no debe poder leer un paso antes de que la voz lo diga.

## Estados acumulativos

El mismo patrón del redactado (`62`): el estado `k` contiene los `k` primeros pasos.
Se genera con una función y se encadena con `cadena_serie` (`61`).

```python
PASOS = ["EFECTIVO<br>A GRANEL", "CRUCE A<br>MÉXICO", "ASEGURADORAS<br>EE.UU.",
         "TARJETAS<br>RECARGABLES", "EMPRESAS<br>DE FACHADA"]

def flujo(nombre, pasos, titulo, w_c=216, h_c=132, sep=64, top=150):
    """Devuelve len(pasos)+1 estados: el estado k lleva los k primeros pasos."""
    w = 44 + len(pasos)*(w_c + sep)
    salida = {}
    for k in range(len(pasos) + 1):
        cajas = "".join(f"""
  <div class="l" style="left:{22+i*(w_c+sep)}px;top:{top}px;width:{w_c}px;height:{h_c}px;
       background:rgba(237,230,214,.96);border:3px solid #2A2620;border-radius:3px;
       box-shadow:0 8px 20px rgba(0,0,0,.5)">
    <div class="mono" style="padding:14px 12px 0;font-size:13px;letter-spacing:.16em;
         color:#7A7263">PASO {i+1}</div>
    <div style="padding:6px 12px 0;font-size:19px;font-weight:800;color:#17140F;
         line-height:1.14">{t}</div>
  </div>""" + ("" if i >= k-1 else f"""
  <div class="l rojo" style="left:{22+w_c+i*(w_c+sep)+10}px;top:{top+50}px;
       font-size:34px;font-weight:800">&rarr;</div>""")
            for i, t in enumerate(pasos[:k]))
        salida[f"{nombre}_{k:02d}"] = (w, h_c + top + 60, f"""
<div style="position:relative;width:{w}px;height:{h_c+top+60}px">{cajas}
  <div class="l mono papel" style="left:0;top:22px;width:{w}px;text-align:center;
       font-size:21px;letter-spacing:.3em;opacity:.78">{titulo}</div>
</div>""")
    return salida

F.update(flujo("lavado", PASOS, "LA MÁQUINA, SEGÚN EL JUICIO"))
```

La flecha pertenece al paso **anterior**: aparece con el paso que apunta, no antes. Una
flecha que señala a un hueco vacío anticipa que falta algo y rompe el suspense.

## El anclaje: un estado por palabra

Un diagrama por pasos no se monta con `paso` fijo. Cada estado se ancla a la palabra
de la locución que nombra ese paso:

```python
{"id": "maquina", "ini": 41.20, "fin": 53.60, "fondo": "rejilla", "mov": ("out", 0.09),
 "elementos": [
   {"r": "lavado_01", "ancla": "efectivo",     "offset": -0.15, "dura": 2.60,
    "x": "W*0.06", "y": "H*0.30", "w": 1500, "entrada": "fade", "fade_out": 0.0},
   {"r": "lavado_02", "ancla": "frontera",     "offset": -0.15, "dura": 2.40,
    "x": "W*0.06", "y": "H*0.30", "w": 1500, "entrada": "fade", "fade_out": 0.0},
   # … un elemento por estado, siempre la MISMA x, y, w
 ]},
```

**La posición y el ancho no cambian entre estados.** Si varían un píxel, el diagrama
salta en cada paso y se ve como cinco imágenes distintas en vez de una que crece.

`fade_out: 0.0` evita que el estado se apague antes de que entre el siguiente. La
entrada `fade` de 0,30 s del motor sí conviene aquí: entre pasos anclados a palabras
hay 2 segundos, así que el fundido se lee como aparición suave, no como retraso.

## Duración por paso

| Pasos | Duración total sana | Por qué |
|---|---|---|
| 3 | 5-7 s | Un mecanismo de tres pasos no da para más |
| 5 | 9-13 s | Es el máximo que se sostiene sin partir la escena |
| 7 o más | Se parte en dos diagramas | Siete cajas en 1920 px son ilegibles en móvil |

Con más de cinco pasos, la caja baja de 200 px de ancho y el texto de 19 px: en un
móvil eso no se lee (`49`). Se agrupa: dos diagramas de tres, no uno de seis.

## Cuándo NO es un diagrama

| Situación | Lo que toca |
|---|---|
| Los pasos no van en orden (es una red, no una cadena) | Un tablero de investigación con hilos (`54`) |
| Sólo hay dos elementos | Una comparación o una balanza (`63`, `61`) |
| El mecanismo es geográfico | Una ruta sobre mapa (`64`) |
| La voz no enumera | Nada: el diagrama exige que la voz lleve la cuenta |

## El remate

Cuando entra el último paso, el diagrama completo se queda **1,5-2,5 s** en pantalla sin
nada nuevo encima. Es una de las pocas excusas legítimas para un plano sin eventos
(`16`): el espectador necesita ver la cadena entera de una vez para que el mecanismo
haga clic. Después se cierra con el sello (`62`) o con el tachado de marca (`77`).

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Diagrama completo desde el primer fotograma | Se lee en 2 s y sobran 8 de espera |
| La `x` o la `w` cambian entre estados | Cinco imágenes distintas en vez de una que crece |
| Flecha que apunta a una caja aún vacía | Anticipa el paso siguiente y mata el suspense |
| Estados con `paso` fijo en vez de anclados | El diagrama se desincroniza de la voz |
| Seis o siete cajas en una fila | Ilegible en móvil |
| Sin `fade_out: 0.0` | El paso se apaga antes de que llegue el siguiente: parpadeo |
| No dejar el diagrama completo al final | El mecanismo nunca se ve entero |

## Relacionado

`61` `cadena_serie` · `62` estados acumulativos · `54` tablero de investigación · `16` el plano de descanso · `49` tamaños legibles
