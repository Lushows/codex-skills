# 55 · Fondos atmosféricos

**Qué resuelve:** el aire. Un fondo con humo, polvo o profundidad deja de ser una lámina
plana y se convierte en un sitio con volumen — y de paso disimula que el recorte que va
encima viene de otra foto.

---

## Por qué importa aquí

El collage tiene un problema estructural: recortes de fotos distintas sobre un plano liso
se leen como pegatinas. **La atmósfera es la cola.** Un velo de humo entre el fondo y el
recorte, o unas partículas delante, hace que compartan aire y el ojo los acepte juntos.

| Recurso | Qué aporta | Coste |
|---|---|---|
| Humo | Volumen, drama, ocultar transiciones | Un filtro SVG |
| Polvo en suspensión | Antigüedad, almacén, archivo | Un bucle de divs |
| Partículas de luz | Riqueza, movimiento, foco | Un bucle de divs |
| Profundidad de campo | Separar planos, dirigir la mirada | `filter:blur()` |
| Niebla baja | Suelo, misterio, cerrar el pie del cuadro | Un degradado con blur |

## Humo — `feTurbulence` + `feDisplacementMap`

El humo bueno no es una nube borrosa: es una forma **deformada**. Se pinta un degradado y
se retuerce:

```html
<svg width="0" height="0" style="position:absolute">
  <filter id="humo" x="-20%" y="-20%" width="140%" height="140%">
    <feTurbulence type="fractalNoise" baseFrequency="0.004 0.010" numOctaves="5" seed="23"
      result="t"/>
    <feDisplacementMap in="SourceGraphic" in2="t" scale="260" xChannelSelector="R"
      yChannelSelector="G"/>
    <feGaussianBlur stdDeviation="14"/>
  </filter>
</svg>

<div class="l" style="left:-10%;bottom:-12%;width:80%;height:70%;opacity:.30;
  filter:url(#humo);background:radial-gradient(52% 60% at 40% 90%,
    rgba(228,238,232,.85) 0%,rgba(196,214,204,.35) 42%,transparent 76%)"></div>
```

| Parámetro | Efecto |
|---|---|
| `baseFrequency` 0.004-0.010 | Volutas grandes. Por encima de 0.03 sale espuma, no humo |
| `scale` 180-320 | Cuánto se retuerce. Menos de 100 no se nota |
| `opacity` .18-.34 | Por encima de .40 tapa el fondo y se pierde la escena |
| `stdDeviation` 10-18 | Suaviza el borde del desplazamiento |

**Dos capas de humo** con `seed` distinto (23 y 41) y opacidades .30 y .16 dan mucho más
volumen que una sola al .46.

## Polvo y partículas — generadas desde Python

No se escriben a mano: `fondos.py` es Python, así que se generan. Va **dentro** del archivo
de fondo, antes del bloque HTML:

```python
import random

def polvo(n=90, seed=7, color="rgba(232,222,196,", zona=(0, 0, 1920, 1080)):
    """Motas de polvo en suspensión. Tamaños y opacidades repartidos, no uniformes."""
    r = random.Random(seed)
    x0, y0, x1, y1 = zona
    out = []
    for _ in range(n):
        x, y = r.uniform(x0, x1), r.uniform(y0, y1)
        d = r.choice([2, 2, 3, 3, 4, 6, 9])          # muchas pequeñas, pocas grandes
        a = round(r.uniform(.10, .55), 2)
        b = 0 if d < 4 else round(d * 0.8, 1)        # solo las grandes brillan
        out.append(
            f'<div class="l" style="left:{x:.0f}px;top:{y:.0f}px;width:{d}px;height:{d}px;'
            f'border-radius:50%;background:{color}{a});'
            f'box-shadow:0 0 {b}px {color}{a});"></div>')
    return "\n".join(out)
```

Uso: `F["f_almacen"] = f'<div class="esc" ...>{polvo(90, seed=7)}{capas(".62")}</div>'`

Reglas del polvo:

- **90-140 motas** en un plano general; 40-60 si hay un recorte grande encima.
- La mayoría de 2-3 px: el polvo se intuye, no se cuenta.
- Concentrar en el haz de luz (`zona=(300,0,1100,700)`), no repartir por todo el cuadro.
  El polvo solo se ve donde le da la luz, y esa es la razón de que funcione.
- Para partículas de luz (brasas, destellos): mismo generador con
  `color="rgba(255,226,150,"` y `n=35`.

## Profundidad de campo simulada

Todo lo que en la escena está "lejos" se desenfoca; lo que está en el plano del recorte,
no. Se hace por capas del propio fondo:

```html
<!-- fondo lejano: desenfocado y desaturado -->
<div class="l" style="inset:0;filter:blur(9px) saturate(.72)">
  <div class="l" style="left:8%;top:22%;width:36%;height:56%;
    background:rgba(120,150,140,.10);border:2px solid rgba(180,210,195,.08)"></div>
</div>
<!-- plano medio: nítido, es donde va el recorte -->
<div class="l" style="left:36%;top:30%;width:30%;height:52%;
  border:2px solid rgba(200,225,210,.16)"></div>
<!-- primer plano: muy desenfocado, oscuro, en los bordes -->
<div class="l" style="left:-4%;top:-6%;width:26%;height:114%;filter:blur(26px);
  background:linear-gradient(90deg,rgba(6,10,8,.92),rgba(6,10,8,.30) 70%,transparent)"></div>
```

Las tres capas juntas dan una sensación de distancia que ningún degradado consigue. La de
primer plano **oscura y borrosa en un borde** es la más barata y la que más se nota.

> `backdrop-filter` es inestable en Chrome headless con `--disable-gpu`. Usar siempre
> `filter:blur()` sobre una capa propia, nunca `backdrop-filter`.

## Niebla baja

```html
<div class="l" style="left:-6%;right:-6%;bottom:-4%;height:34%;filter:blur(34px);opacity:.26;
  background:linear-gradient(0deg,rgba(214,228,220,.85) 0%,rgba(214,228,220,.25) 52%,transparent 100%)"></div>
```

Cierra el pie del cuadro sin recurrir a más viñeta, que es lo que ahoga la escena (`53`).

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Humo sin `feDisplacementMap` | Mancha borrosa; se lee como error de compresión |
| `baseFrequency` alta en el humo | Espuma de jabón |
| Partículas repartidas uniformemente | Se lee como ruido digital o suciedad de lente |
| Polvo fuera del haz de luz | No lo justifica nada; parece un defecto |
| Todas las motas del mismo tamaño | Delata el bucle |
| `backdrop-filter` | Sale sin aplicar en headless con `--disable-gpu` |
| Atmósfera en las seis escenas | Pierde su valor: es un recurso de énfasis |

## Relacionado

`50` · `53` · `56` · `22` profundidad por capas · `66` grano y textura · `67` luz y destellos
