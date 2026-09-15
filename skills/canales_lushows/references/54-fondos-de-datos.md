# 54 · Fondos de datos

**Qué resuelve:** las escenas explicativas —la cifra, el esquema, la ruta, la red del
fraude— necesitan un fondo que **signifique análisis**. Aquí están los cinco que se usan,
con su código.

---

## Cuándo se usa uno de estos

Cuando lo que va encima es información, no una persona. Un retrato sobre papel milimetrado
se lee como error; una cifra sobre papel milimetrado se lee como prueba.

| Fondo | Para |
|---|---|
| Plano técnico | Cómo funcionaba el montaje, la máquina, la ruta del dinero |
| Papel milimetrado | Una cifra sola, una curva, una comparación de magnitudes |
| Mapa | Movimiento geográfico, países, fronteras |
| Tablero de investigación | Relaciones entre personas, la red |
| Libro contable | Cuentas, transferencias, el documento que lo destapó |

**Regla común:** estos fondos tienen más detalle que los demás, así que su viñeta sube al
rango alto (`.62-.66`) y la luz baja al bajo (`.10-.16`). El detalle vive en el centro; los
bordes se apagan.

## Plano técnico (blueprint)

```html
<div class="esc" style="background:linear-gradient(150deg,#152232 0%,#0D1520 60%,#070B10 100%)">
  <div class="l" style="inset:0;opacity:.24;background:
    repeating-linear-gradient(0deg,transparent 0 38px,rgba(96,150,200,.42) 38px 39px),
    repeating-linear-gradient(90deg,transparent 0 38px,rgba(96,150,200,.28) 38px 39px)"></div>
  <div class="l" style="left:4%;top:6%;right:4%;bottom:6%;border:2px solid rgba(110,170,220,.22)"></div>
  <div class="l" style="right:4%;bottom:6%;width:420px;height:150px;
    border:2px solid rgba(110,170,220,.28);background:rgba(20,40,64,.35)"></div>
  <div class="l" style="right:4%;bottom:6%;width:420px;height:150px;background:
    repeating-linear-gradient(0deg,transparent 0 49px,rgba(110,170,220,.28) 49px 51px)"></div>
  <div class="l" style="left:16%;top:14%;width:34%;height:2px;background:rgba(140,195,240,.30)"></div>
  <div class="l" style="left:16%;top:12%;width:2px;height:6%;background:rgba(140,195,240,.30)"></div>
  <div class="l" style="left:50%;top:12%;width:2px;height:6%;background:rgba(140,195,240,.30)"></div>
</div>
```

El **cajetín** abajo a la derecha y las **cotas** con remate en T son lo que lo convierten
en plano. Sin ellos es una cuadrícula azul.

## Papel milimetrado

Tres rejillas —1 mm, 5 mm y 1 cm—. Sin las tres no se lee milimetrado.

```html
<div class="esc" style="background:linear-gradient(165deg,#1D2A2C 0%,#131C1E 58%,#090E0F 100%)">
  <div class="l" style="inset:0;opacity:.16;background:
    repeating-linear-gradient(0deg,transparent 0 15px,rgba(120,190,175,.40) 15px 16px),
    repeating-linear-gradient(90deg,transparent 0 15px,rgba(120,190,175,.40) 15px 16px)"></div>
  <div class="l" style="inset:0;opacity:.26;background:
    repeating-linear-gradient(0deg,transparent 0 75px,rgba(140,215,195,.55) 75px 77px),
    repeating-linear-gradient(90deg,transparent 0 75px,rgba(140,215,195,.55) 75px 77px)"></div>
  <div class="l" style="inset:0;opacity:.34;background:
    repeating-linear-gradient(0deg,transparent 0 150px,rgba(160,235,210,.60) 150px 153px),
    repeating-linear-gradient(90deg,transparent 0 150px,rgba(160,235,210,.60) 150px 153px)"></div>
  <div class="l" style="left:12%;bottom:18%;width:76%;height:3px;background:rgba(232,197,71,.45)"></div>
  <div class="l" style="left:12%;top:14%;width:3px;height:68%;background:rgba(232,197,71,.45)"></div>
</div>
```

Los dos ejes amarillos existen para que la curva o la barra que va encima tenga de dónde
salir. Una gráfica flotando sin eje se lee como adorno.

## Mapa

El mapa no se dibuja: se **sugiere** con paralelos, meridianos y una rosa. Lo geográfico
concreto va encima como recorte (`64`).

```html
<div class="esc" style="background:radial-gradient(70% 70% at 50% 42%,#1A2C3A 0%,#101C26 52%,#070C10 100%)">
  <div class="l" style="inset:0;opacity:.20;background:
    repeating-linear-gradient(0deg,transparent 0 118px,rgba(120,180,215,.45) 118px 119px),
    repeating-linear-gradient(90deg,transparent 0 118px,rgba(120,180,215,.30) 118px 119px)"></div>
  <div class="l" style="left:0;right:0;top:50%;height:3px;background:rgba(160,210,240,.34)"></div>
  <div class="l" style="left:0;right:0;top:34%;height:1px;background:rgba(160,210,240,.20)"></div>
  <div class="l" style="left:0;right:0;top:66%;height:1px;background:rgba(160,210,240,.20)"></div>
  <div class="l" style="right:6%;bottom:8%;width:180px;height:180px;border-radius:50%;
    border:2px solid rgba(160,210,240,.28)"></div>
  <div class="l" style="right:6%;bottom:8%;width:180px;height:180px;background:
    conic-gradient(from 0deg,rgba(232,197,71,.30) 0 2deg,transparent 2deg 90deg,
      rgba(160,210,240,.18) 90deg 92deg,transparent 92deg 180deg,
      rgba(160,210,240,.18) 180deg 182deg,transparent 182deg 270deg,
      rgba(160,210,240,.18) 270deg 272deg,transparent 272deg 360deg)"></div>
</div>
```

El ecuador grueso y los dos trópicos finos son lo que dice "mapa" en medio segundo.

## Tablero de investigación (corcho e hilos)

```html
<div class="esc" style="background:linear-gradient(170deg,#3B2E1E 0%,#2A2116 56%,#140F0A 100%)">
  <svg class="l" style="inset:0;opacity:.30;mix-blend-mode:overlay" viewBox="0 0 1920 1080">
    <filter id="corcho"><feTurbulence type="fractalNoise" baseFrequency="0.22" numOctaves="4"
      seed="3"/><feColorMatrix type="saturate" values="0"/></filter>
    <rect width="1920" height="1080" filter="url(#corcho)"/></svg>
  <div class="l" style="left:14%;top:24%;width:64%;height:2px;background:rgba(227,18,11,.42);
    transform:rotate(11deg);transform-origin:left center"></div>
  <div class="l" style="left:22%;top:70%;width:56%;height:2px;background:rgba(227,18,11,.34);
    transform:rotate(-17deg);transform-origin:left center"></div>
  <div class="l" style="left:60%;top:20%;width:44%;height:2px;background:rgba(227,18,11,.28);
    transform:rotate(58deg);transform-origin:left center"></div>
  <div class="l" style="left:14%;top:23%;width:16px;height:16px;border-radius:50%;
    background:#E3120B;box-shadow:0 3px 6px rgba(0,0,0,.6)"></div>
  <div class="l" style="left:60%;top:19%;width:16px;height:16px;border-radius:50%;
    background:#E8C547;box-shadow:0 3px 6px rgba(0,0,0,.6)"></div>
</div>
```

Los hilos van **detrás** de las fichas que se pegan encima y las chinchetas coinciden con
las esquinas de esas fichas. Si no coinciden, se ve que son dos cosas distintas.

## Libro contable

```html
<div class="esc" style="background:linear-gradient(180deg,#2E2A20 0%,#211E17 58%,#100E0A 100%)">
  <div class="l" style="inset:0;opacity:.22;background:
    repeating-linear-gradient(0deg,transparent 0 62px,rgba(224,210,178,.34) 62px 63px)"></div>
  <div class="l" style="left:12%;top:0;bottom:0;width:2px;background:rgba(227,18,11,.30)"></div>
  <div class="l" style="left:62%;top:0;bottom:0;width:2px;background:rgba(224,210,178,.24)"></div>
  <div class="l" style="left:80%;top:0;bottom:0;width:2px;background:rgba(224,210,178,.24)"></div>
</div>
```

Renglones más columnas de debe y haber. El filete rojo del margen izquierdo es el detalle
que lo hace libro y no cuaderno.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Rejilla de una sola escala | Se lee cuadrícula genérica, no plano ni milimetrado |
| Dibujar el mapa real en CSS | Horas perdidas y fronteras mal; va como recorte encima |
| Fondo de datos bajo un retrato | Choque de códigos: el dato no era la persona |
| Hilos y chinchetas que no coinciden con las fichas | Delata que el tablero es adorno |
| Luz fuerte sobre un fondo de datos | El detalle compite con la cifra que va encima |

## Relacionado

`50` · `52` · `27` composición de datos · `36` cifras animadas · `64` mapas · `65` diagramas
