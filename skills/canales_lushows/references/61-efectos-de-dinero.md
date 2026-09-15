# 61 · Efectos de dinero

**Qué resuelve:** el canal habla de cifras todo el rato. Estos son los objetos que
convierten una cifra dicha en una cifra vista: fajos, lluvia, contadores, barras y
balanzas. Todos salen a PNG con alfa y se montan como cualquier recorte.

**Color:** el dinero dibujado va en verde apagado (`#CFD8C4` sobre `#A8B598`); en verde
saturado se lee como icono de aplicación, no como papel.

---

## 1 · Lluvia de billetes en bucle (un solo PNG)

La lluvia **no se hace con 24 fotogramas**. Se dibuja una lámina de altura `2×H` cuya
mitad inferior es copia exacta de la superior y se desplaza con `overlay`: como el
patrón es periódico en `H`, el bucle cierra perfecto y pesa un archivo.

```python
# fx_lluvia.py -> fx/lluvia.png (1920x2160, alfa)
import math, random
from PIL import Image, ImageDraw

W, H, S = 1920, 1080, 2          # S: se dibuja a 2x y se reduce al final
random.seed(7)                    # semilla fija = resultado reproducible

def billete(dr, x, y, ang, l=124, h=54):
    c, s = math.cos(math.radians(ang)), math.sin(math.radians(ang))
    pts = [(x + dx*c - dy*s, y + dx*s + dy*c)
           for dx, dy in ((0, 0), (l, 0), (l, h), (0, h))]
    dr.polygon(pts, fill=(207, 216, 196, 255))
    dr.line(pts + [pts[0]], fill=(42, 38, 32, 255), width=2)

alto = H*S
lienzo = Image.new("RGBA", (W*S, alto*3), (0, 0, 0, 0))   # 3 bandas, todo positivo
dr = ImageDraw.Draw(lienzo)
for _ in range(90):
    x, y = random.uniform(-80, W*S), random.uniform(0, alto)
    a = random.uniform(-38, 38)
    for k in (0, 1, 2):
        billete(dr, x, y + k*alto, a)
chico = lienzo.resize((W, H*3), Image.LANCZOS)   # reducir ANTES de recortar
banda = chico.crop((0, H, W, H*2))              # la de en medio: sin bordes clampeados
im = Image.new("RGBA", (W, H*2), (0, 0, 0, 0))
im.paste(banda, (0, 0)); im.paste(banda, (0, H))          # dos mitades idénticas
im.save("fx/lluvia.png")
```

En el filtro de la escena:

```
[bg][llu]overlay=x=0:y='-mod((t-3.10)*260,1080)':enable='between(t,3.10,7.40)'
```

Las tres bandas y el recorte de la de en medio garantizan que las dos mitades queden
**idénticas byte a byte**; dibujar directo sobre un lienzo de `2H` deja bordes cortados
y el bucle salta en cada vuelta. `260` = píxeles por segundo. Por debajo de 180 parece papel
flotando; por encima de 420 son rayas. La coma de `mod(...)` no hay que escaparla: va
dentro de comillas simples.

**Dos capas, nunca una.** Una lámina al 60% de tamaño y velocidad 150 **detrás** del
recorte, otra al 100% y velocidad 300 delante. Una sola capa se lee plana.

---

## 2 · Contador genérico (serie de estados)

La subida **no es lineal**: a velocidad constante se lee como cronómetro; arrancando
rápido y frenando al llegar se lee como cifra que se revela.

```python
def rampa(v_final, n=12, p=2.2):
    """Valores con salida suave (ease-out). p más alto = frena más tarde."""
    return [round(v_final * (1 - (1 - i/(n-1))**p)) for i in range(n)]

def contador(nombre, valores, unidad="M USD", w=900, h=210):
    """Entradas listas para el diccionario F de fx.py."""
    salida = {}
    for i, v in enumerate(valores):
        cifra = format(v, ",").replace(",", ".")      # separador de miles español
        salida[nombre + "_%02d" % i] = (w, h, f"""
<div style="position:relative;width:{w}px;height:{h}px">
  <div class="l mono oro" style="left:0;top:0;width:{w}px;text-align:right;
       font-size:112px;font-weight:800;letter-spacing:-.02em;
       text-shadow:0 6px 26px rgba(0,0,0,.9)">{cifra}<span
       style="font-size:46px;margin-left:12px">{unidad}</span></div>
</div>""")
    return salida

F.update(contador("usd", rampa(12600)))     # así se generaron usd_00…usd_11
```

**Alineado a la derecha, siempre.** Centrado, la cifra se desplaza en cada estado y el
número parece temblar.

### Encadenar una serie

El motor aplica un `fade` de entrada de 0,30 s fijo: sobre estados de 0,09 s los deja
invisibles. Una serie se monta **sin fades**, con `enable` seco:

```python
def cadena_serie(base, estados, t0, paso, x, y, w, i0=1):
    """base: etiqueta de entrada ('bg'). estados: PNG ya añadidos como -i, en orden."""
    filtros, ultimo = [], base
    for k in range(len(estados)):
        a, b = t0 + k*paso, t0 + (k+1)*paso
        filtros.append(f"[{i0+k}:v]scale={w}:-1,format=rgba[s{k}]")
        filtros.append(f"[{ultimo}][s{k}]overlay=x='{x}':y='{y}':"
                       f"enable='between(t,{a:.3f},{b:.3f})'[c{k}]")
        ultimo = f"c{k}"
    return filtros, ultimo
```

`paso` entre **0,07 y 0,11 s**. Y el último estado se deja fijo **0,8-1,2 s**: la cifra
final tiene que descansar para poder leerse, que era todo el objetivo.

---

## 3 · Barra o pila que crece

Mismo patrón: `rampa()` sirve igual para alturas que para valores. Se generan 8-10
estados con la barra ya crecida y se encadenan con `cadena_serie`. El rótulo con la cifra
crece **en el mismo estado**: fijo mientras la barra sube, delata que son dos elementos.

---

## 4 · Balanza (dos platos, una viga)

5-7 estados interpolando el ángulo de la viga. El texto de los platos **no gira**.

```python
def balanza(ang, izq, der, w=1100, h=520):
    dy = int(380 * ang / -14)                 # ±14° = recorrido máximo
    plato = lambda x, y, col, txt: f"""
  <div class="l" style="left:{x}px;top:{110+y}px;width:300px;height:8px;background:{col}"></div>
  <div class="l mono papel" style="left:{x}px;top:{60+y}px;width:300px;text-align:center;
       font-size:26px;letter-spacing:.14em">{txt}</div>"""
    return (w, h, f"""
<div style="position:relative;width:{w}px;height:{h}px">
  <div class="l" style="left:{w//2-6}px;top:120px;width:12px;height:300px;background:#2A2620"></div>
  <div class="l" style="left:{w//2-380}px;top:110px;width:760px;height:10px;background:#2A2620;
       transform:rotate({ang}deg);transform-origin:50% 50%"></div>
  {plato(60, dy, "#E8C547", izq)}{plato(w-360, -dy, "#E3120B", der)}
</div>""")
```

La balanza sólo sirve para **dos cifras del mismo tipo** (lo que se llevó contra lo que
se recuperó). Para cifras de tipos distintos no es una balanza: es una comparación (`63`).

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Lluvia con 24 PNG de pantalla completa | Decenas de MB y un bucle que salta al reiniciar |
| Contador lineal | Se lee como cronómetro, no como revelación |
| Cifra centrada en el contador | El número tiembla al cambiar de dígitos |
| Serie montada con los fades del motor | Estados de 0,09 s con 0,30 s de fade: no se ve nada |
| No dejar descansar el último estado | La cifra final no se lee |
| Una sola capa de lluvia | Plano: sin dos velocidades no hay profundidad |

## Relacionado

`44` la cifra en pantalla · `63` comparaciones · `36` cifras animadas · `41` revelado por `crop` · `69`
