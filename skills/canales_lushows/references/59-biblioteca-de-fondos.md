# 59 · Biblioteca de fondos

**Qué resuelve:** no empezar de cero cada episodio. Quince fondos probados, con su nombre,
su uso y su código. Se pegan en `fondos.py` y se le cambia el tono base si hace falta.

---

## Cómo se usa esta biblioteca

Cada bloque es el contenido del `<div class="esc">`. El esqueleto, los filtros SVG y las
tres capas de acabado los pone `fondos.py` (`50`); aquí solo va **base + textura + luz**.
En todos, el cierre del generador es `{capas(".62")}` con el alfa que indique la ficha.

| Nombre | Uso | Temperatura | Viñeta |
|---|---|---|---|
| `f_billete` | Gancho de dinero, cifras grandes | verde `#28402F` | .66 |
| `f_expediente` | La pregunta, la investigación | azul `#1B2A38` | .62 |
| `f_almacen` | Mercancía, volumen, decomiso | ocre `#3A3226` | .62 |
| `f_acero` | Oficina, sistema, institución | acero `#39413F` | .60 |
| `f_plano` | Cómo funcionaba el montaje | azul plano `#152232` | .58 |
| `f_planta` | Fábrica, producción, remate | verde ind. `#2C3A31` | .62 |
| `f_juzgado` | Proceso, sentencia, condena | hormigón `#2B3033` | .64 |
| `f_celda` | La caída, el encierro | verde apagado `#242B26` | .68 |
| `f_despacho` | Retrato, entrevista, el hombre | caoba `#3A2A20` | .60 |
| `f_prensa` | La noticia, el titular, la fama | crema oscuro `#33301F` | .60 |
| `f_frontera` | Rutas, países, blanqueo | azul noche `#141F2B` | .62 |
| `f_bolsa` | Mercado, cotización, colapso | verde/rojo `#101C18` | .64 |
| `f_ciudad` | Escala, riqueza, la ciudad de noche | añil `#101724` | .66 |
| `f_madera` | Documento firmado, mesa, contrato | nogal `#2C2118` | .58 |
| `f_ruina` | El final, lo que quedó | ocre quemado `#38251C` | .66 |

---

```html
<!-- f_billete · guilloché de billete con roseta -->
<div class="esc" style="background:radial-gradient(78% 70% at 46% 40%,#28402F 0%,#12201A 46%,#080D0B 100%)">
  <div class="l" style="inset:0;opacity:.16;background:
    repeating-linear-gradient(38deg,rgba(200,230,205,.5) 0 1px,transparent 1px 9px),
    repeating-linear-gradient(-38deg,rgba(200,230,205,.35) 0 1px,transparent 1px 13px)"></div>
  <div class="l" style="left:50%;top:44%;transform:translate(-50%,-50%);width:940px;height:940px;
    border-radius:50%;border:2px solid rgba(190,225,196,.14)"></div>
</div>

<!-- f_expediente · rejilla de formulario y dos marcos de ficha -->
<div class="esc" style="background:linear-gradient(155deg,#1B2A38 0%,#101A24 55%,#080D12 100%)">
  <div class="l" style="inset:0;opacity:.20;background:
    repeating-linear-gradient(0deg,transparent 0 52px,rgba(120,170,210,.5) 52px 53px),
    repeating-linear-gradient(90deg,transparent 0 52px,rgba(120,170,210,.32) 52px 53px)"></div>
  <div class="l" style="left:8%;top:12%;width:36%;height:76%;border:2px solid rgba(130,180,220,.18)"></div>
</div>

<!-- f_almacen · suelo de nave y luz cenital cálida -->
<div class="esc" style="background:linear-gradient(180deg,#3A3226 0%,#2A2419 52%,#14110C 100%)">
  <div class="l" style="left:0;right:0;bottom:0;height:44%;background:
    repeating-linear-gradient(90deg,rgba(210,190,150,.10) 0 118px,transparent 118px 124px),
    linear-gradient(180deg,rgba(0,0,0,0),rgba(0,0,0,.55))"></div>
  <div class="l" style="left:50%;top:0;transform:translateX(-50%);width:70%;height:52%;
    background:radial-gradient(60% 80% at 50% 0%,rgba(255,232,180,.20),transparent 72%)"></div>
</div>

<!-- f_acero · paneles de oficina, luz fría cenital -->
<div class="esc" style="background:linear-gradient(168deg,#39413F 0%,#252B2A 55%,#101413 100%)">
  <div class="l" style="left:0;right:0;top:0;height:56%;background:
    repeating-linear-gradient(90deg,rgba(220,228,226,.07) 0 210px,transparent 210px 216px)"></div>
  <div class="l" style="left:50%;top:-6%;transform:translateX(-50%);width:56%;height:44%;
    background:radial-gradient(58% 80% at 50% 0%,rgba(214,240,255,.24),transparent 70%)"></div>
</div>

<!-- f_plano · blueprint con cajetín -->
<div class="esc" style="background:linear-gradient(150deg,#152232 0%,#0D1520 60%,#070B10 100%)">
  <div class="l" style="inset:0;opacity:.24;background:
    repeating-linear-gradient(0deg,transparent 0 38px,rgba(96,150,200,.42) 38px 39px),
    repeating-linear-gradient(90deg,transparent 0 38px,rgba(96,150,200,.28) 38px 39px)"></div>
  <div class="l" style="left:4%;top:6%;right:4%;bottom:6%;border:2px solid rgba(110,170,220,.22)"></div>
  <div class="l" style="right:4%;bottom:6%;width:420px;height:150px;border:2px solid rgba(110,170,220,.28)"></div>
</div>

<!-- f_planta · verde industrial con dos focos -->
<div class="esc" style="background:linear-gradient(172deg,#2C3A31 0%,#1B241E 55%,#0B0F0D 100%)">
  <div class="l" style="left:0;right:0;bottom:0;height:50%;background:
    repeating-linear-gradient(90deg,rgba(180,210,185,.09) 0 96px,transparent 96px 100px)"></div>
  <div class="l" style="left:12%;top:-4%;width:34%;height:46%;
    background:radial-gradient(60% 80% at 50% 0%,rgba(226,255,232,.18),transparent 70%)"></div>
  <div class="l" style="right:14%;top:-4%;width:30%;height:40%;
    background:radial-gradient(60% 80% at 50% 0%,rgba(255,236,196,.14),transparent 70%)"></div>
</div>

<!-- f_juzgado · hormigón con juntas de encofrado -->
<div class="esc" style="background:linear-gradient(176deg,#2B3033 0%,#1C2022 58%,#0C0E0F 100%)">
  <div class="l" style="inset:0;opacity:.18;background:
    repeating-linear-gradient(90deg,transparent 0 318px,rgba(0,0,0,.55) 318px 322px),
    repeating-linear-gradient(0deg,transparent 0 262px,rgba(0,0,0,.42) 262px 266px)"></div>
  <div class="l" style="left:-8%;top:4%;width:52%;height:78%;
    background:radial-gradient(70% 60% at 0% 40%,rgba(226,240,255,.16),transparent 74%)"></div>
</div>

<!-- f_celda · sombra de barrotes proyectada -->
<div class="esc" style="background:linear-gradient(182deg,#242B26 0%,#171C19 56%,#090C0A 100%)">
  <div class="l" style="inset:0;opacity:.32;transform:skewX(-9deg);background:
    repeating-linear-gradient(90deg,transparent 0 96px,rgba(0,0,0,.72) 96px 132px)"></div>
  <div class="l" style="left:26%;top:-10%;width:44%;height:120%;filter:blur(46px);opacity:.16;
    background:linear-gradient(180deg,rgba(226,240,220,.85),transparent 72%)"></div>
</div>

<!-- f_despacho · paño de traje y lámpara cálida lateral -->
<div class="esc" style="background:radial-gradient(72% 66% at 34% 38%,#3A2A20 0%,#241A13 50%,#0E0A07 100%)">
  <div class="l" style="inset:0;opacity:.12;background:
    repeating-linear-gradient(0deg,rgba(255,255,255,.22) 0 1px,transparent 1px 3px),
    repeating-linear-gradient(90deg,rgba(0,0,0,.28) 0 1px,transparent 1px 3px)"></div>
  <div class="l" style="left:-6%;top:2%;width:50%;height:70%;
    background:radial-gradient(66% 58% at 0% 36%,rgba(255,214,140,.24),transparent 74%)"></div>
</div>

<!-- f_prensa · columnas de periódico -->
<div class="esc" style="background:linear-gradient(160deg,#33301F 0%,#232116 56%,#100F0A 100%)">
  <div class="l" style="inset:0;opacity:.20;background:
    repeating-linear-gradient(0deg,transparent 0 14px,rgba(228,218,186,.30) 14px 16px)"></div>
  <div class="l" style="inset:0;opacity:.30;background:
    repeating-linear-gradient(90deg,transparent 0 412px,rgba(228,218,186,.34) 412px 414px)"></div>
</div>

<!-- f_frontera · mapa nocturno con ecuador -->
<div class="esc" style="background:radial-gradient(70% 70% at 50% 42%,#141F2B 0%,#0D1620 52%,#060A0E 100%)">
  <div class="l" style="inset:0;opacity:.20;background:
    repeating-linear-gradient(0deg,transparent 0 118px,rgba(120,180,215,.45) 118px 119px),
    repeating-linear-gradient(90deg,transparent 0 118px,rgba(120,180,215,.30) 118px 119px)"></div>
  <div class="l" style="left:0;right:0;top:50%;height:3px;background:rgba(160,210,240,.34)"></div>
</div>

<!-- f_bolsa · pantallas de cotización -->
<div class="esc" style="background:linear-gradient(178deg,#101C18 0%,#0A1310 58%,#050807 100%)">
  <div class="l" style="inset:0;opacity:.14;background:
    repeating-linear-gradient(0deg,transparent 0 5px,rgba(14,138,95,.55) 5px 6px)"></div>
  <div class="l" style="left:0;right:0;top:22%;height:56px;background:rgba(14,138,95,.16);
    border-top:2px solid rgba(14,138,95,.42);border-bottom:2px solid rgba(14,138,95,.42)"></div>
  <div class="l" style="left:0;right:0;top:64%;height:38px;background:rgba(227,18,11,.14);
    border-top:2px solid rgba(227,18,11,.34)"></div>
</div>

<!-- f_ciudad · ventanas lejanas desenfocadas -->
<div class="esc" style="background:linear-gradient(184deg,#101724 0%,#0A0F18 60%,#04060A 100%)">
  <div class="l" style="inset:0;filter:blur(7px);opacity:.34;background:
    repeating-linear-gradient(90deg,transparent 0 34px,rgba(255,226,164,.30) 34px 46px,
      transparent 46px 96px),
    repeating-linear-gradient(0deg,transparent 0 58px,rgba(0,0,0,.85) 58px 92px)"></div>
  <div class="l" style="left:0;right:0;bottom:0;height:38%;filter:blur(30px);
    background:linear-gradient(0deg,rgba(255,214,150,.16),transparent 80%)"></div>
</div>

<!-- f_madera · veta de nogal, mesa de despacho -->
<div class="esc" style="background:linear-gradient(174deg,#2C2118 0%,#1D1610 58%,#0B0806 100%)">
  <div class="l" style="inset:0;opacity:.16;background:
    repeating-linear-gradient(88deg,rgba(196,150,96,.36) 0 2px,transparent 2px 9px),
    repeating-linear-gradient(92deg,rgba(120,80,44,.30) 0 1px,transparent 1px 23px)"></div>
  <div class="l" style="left:50%;top:-8%;transform:translateX(-50%);width:58%;height:46%;
    background:radial-gradient(58% 80% at 50% 0%,rgba(255,224,168,.22),transparent 70%)"></div>
</div>

<!-- f_ruina · ocre quemado, rescoldo rojo insinuado -->
<div class="esc" style="background:radial-gradient(76% 68% at 52% 56%,#38251C 0%,#20140F 48%,#0A0605 100%)">
  <svg class="l" style="inset:0;opacity:.24;mix-blend-mode:overlay" viewBox="0 0 1920 1080">
    <filter id="cen"><feTurbulence type="fractalNoise" baseFrequency="0.008" numOctaves="5"
      seed="31"/><feColorMatrix type="saturate" values="0"/></filter>
    <rect width="1920" height="1080" filter="url(#cen)"/></svg>
  <div class="l" style="left:24%;bottom:-14%;width:52%;height:40%;filter:blur(64px);opacity:.20;
    background:radial-gradient(60% 60% at 50% 100%,rgba(227,18,11,.9),transparent 72%)"></div>
</div>
```

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Usar el mismo fondo dos episodios seguidos en la misma posición | El canal se vuelve plantilla |
| Copiar el bloque sin ajustar la viñeta de la ficha | Rompe la continuidad de brillo |
| Mezclar `f_bolsa` con acentos rojos encima | El rojo del fondo mata el rojo del sello |
| Meter los tres acabados a mano en el bloque | Se pierde la piel común (`58`) |

## Relacionado

`50` · `51` · `52` · `53` · `54` · `57` · `58`
