# 52 · Texturas de fondo

**Qué resuelve:** un degradado limpio se lee como plantilla de presentación. La textura
es lo que convierte el color en **una superficie**: papel, billete, plano, hormigón. Y es
lo que hace que dos escenas del mismo tono no se confundan.

---

## Cómo se usa una textura

Capa 2 del esqueleto (`50`): un `<div class="l">` con `inset:0` y opacidad **baja**, entre
`.08` y `.26`. Si la textura se lee antes que el recorte que va encima, está mal calibrada.

| Familia | Opacidad | Sensación | Escenas típicas |
|---|---|---|---|
| Papel | .10-.18 | documento, archivo | citas, expediente |
| Guilloché | .12-.18 | dinero, valor | gancho, cifras |
| Rejilla técnica | .18-.26 | plano, sistema | cómo funcionaba |
| Tela | .08-.14 | despacho, traje | retrato, entrevista |
| Hormigón | .10-.16 | institución, muro | juzgado, cárcel |
| Metal | .06-.12 | industria, máquina | planta, oficina |
| Cartón | .12-.20 | mercancía, caja | almacén, decomiso |

---

## Papel — fibra irregular
```html
<div class="l" style="inset:0;opacity:.14;background:
  repeating-linear-gradient(94deg,rgba(230,220,196,.30) 0 2px,transparent 2px 7px),
  repeating-linear-gradient(2deg,rgba(230,220,196,.16) 0 1px,transparent 1px 5px)"></div>
<svg class="l" style="inset:0;opacity:.30;mix-blend-mode:overlay" viewBox="0 0 1920 1080">
  <filter id="fibra"><feTurbulence type="fractalNoise" baseFrequency="0.9 0.02" numOctaves="3"
    seed="7"/><feColorMatrix type="saturate" values="0"/></filter>
  <rect width="1920" height="1080" filter="url(#fibra)"/></svg>
```

Dos ángulos casi paralelos (94° y 2°): con uno solo se lee como rayas.

## Guilloché de billete

La textura firma del canal: dos tramas opuestas con periodos primos entre sí (9 y 13),
que es lo que evita el muaré.
```html
<div class="l" style="inset:0;opacity:.16;background:
  repeating-linear-gradient(38deg,rgba(200,230,205,.5) 0 1px,transparent 1px 9px),
  repeating-linear-gradient(-38deg,rgba(200,230,205,.35) 0 1px,transparent 1px 13px)"></div>
<div class="l" style="left:50%;top:44%;transform:translate(-50%,-50%);width:940px;height:940px;
  border-radius:50%;border:2px solid rgba(190,225,196,.14)"></div>
<div class="l" style="left:50%;top:44%;transform:translate(-50%,-50%);width:660px;height:660px;
  border-radius:50%;border:2px solid rgba(190,225,196,.10)"></div>
```

Los dos anillos concéntricos son la roseta del billete. Sin ellos es solo una trama.

## Rejilla técnica — plano de ingeniería
```html
<div class="l" style="inset:0;opacity:.24;background:
  repeating-linear-gradient(0deg,transparent 0 38px,rgba(96,150,200,.42) 38px 39px),
  repeating-linear-gradient(90deg,transparent 0 38px,rgba(96,150,200,.28) 38px 39px)"></div>
<div class="l" style="inset:0;opacity:.34;background:
  repeating-linear-gradient(0deg,transparent 0 190px,rgba(120,175,225,.55) 190px 192px),
  repeating-linear-gradient(90deg,transparent 0 190px,rgba(120,175,225,.40) 190px 192px)"></div>
<div class="l" style="left:4%;top:6%;right:4%;bottom:6%;border:2px solid rgba(110,170,220,.22)"></div>
```

Fina + gruesa cada 5 casillas: eso la hace leer como plano y no como hoja de cálculo.
El marco interior es el cajetín.

## Tela — lino / paño de traje
```html
<div class="l" style="inset:0;opacity:.12;background:
  repeating-linear-gradient(0deg,rgba(255,255,255,.22) 0 1px,transparent 1px 3px),
  repeating-linear-gradient(90deg,rgba(0,0,0,.28) 0 1px,transparent 1px 3px)"></div>
<div class="l" style="inset:0;opacity:.10;mix-blend-mode:overlay;background:
  repeating-linear-gradient(45deg,rgba(255,255,255,.35) 0 2px,transparent 2px 6px)"></div>
```

Trama de 3 px en cruz + espiga diagonal. A 2,25× son casi 7 px reales: se ve el tejido.

## Hormigón — muro colado
```html
<svg class="l" style="inset:0;opacity:.22;mix-blend-mode:overlay" viewBox="0 0 1920 1080">
  <filter id="horm"><feTurbulence type="fractalNoise" baseFrequency="0.006" numOctaves="5"
    seed="19"/><feColorMatrix type="saturate" values="0"/>
    <feComponentTransfer><feFuncA type="gamma" exponent="1.8"/></feComponentTransfer></filter>
  <rect width="1920" height="1080" filter="url(#horm)"/></svg>
<div class="l" style="inset:0;opacity:.18;background:
  repeating-linear-gradient(90deg,transparent 0 318px,rgba(0,0,0,.55) 318px 322px),
  repeating-linear-gradient(0deg,transparent 0 262px,rgba(0,0,0,.42) 262px 266px)"></div>
```

`baseFrequency` 0.006 da manchas grandes de colada; las juntas de encofrado dan la escala.

## Metal — chapa cepillada
```html
<div class="l" style="inset:0;opacity:.10;background:
  repeating-linear-gradient(90deg,
    rgba(255,255,255,.30) 0 1px,transparent 1px 2px,rgba(0,0,0,.22) 2px 3px,transparent 3px 6px)"></div>
<div class="l" style="inset:0;opacity:.28;background:
  linear-gradient(100deg,transparent 18%,rgba(220,238,246,.30) 34%,
    transparent 46%,transparent 62%,rgba(220,238,246,.18) 74%,transparent 86%)"></div>
```

El cepillado solo se lee metal con las **bandas de reflejo** en diagonal. Sin ellas es persiana.

## Cartón — caja de mercancía
```html
<div class="l" style="inset:0;opacity:.16;background:
  repeating-linear-gradient(0deg,
    rgba(120,86,48,.55) 0 3px,rgba(190,150,100,.30) 3px 8px,rgba(120,86,48,.35) 8px 11px,
    transparent 11px 22px)"></div>
<div class="l" style="inset:0;opacity:.20;mix-blend-mode:multiply;background:
  repeating-linear-gradient(90deg,transparent 0 470px,rgba(0,0,0,.40) 470px 476px)"></div>
```

Onda del corrugado (periodo 22 px) más las juntas verticales de las cajas apiladas.

## Combinarlas

Máximo **dos familias por fondo** y de escalas distintas: una gruesa que dé estructura
(juntas, suelo, cajetín) y una fina que dé materia. Dos finas juntas dan muaré; dos
gruesas, un tablero de ajedrez.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Opacidad por encima de .30 | La textura compite con el collage y cansa |
| Periodos iguales o múltiplos (10 y 20) | Muaré: bandas fantasma al mover el fondo |
| Una sola escala de textura | El fondo no tiene tamaño; parece papel pintado |
| Textura sin relación con la escena | Rejilla técnica en una escena de almacén: ruido |
| Repetir la misma familia en las seis escenas | El episodio se ve plano aunque el color cambie |

## Relacionado

`50` · `51` · `53` · `54` · `59` · `66` grano y textura
