# 43 · Rótulos y etiquetas

**Qué resuelve:** la regla del canal dice *"cada elemento se explica"*, pero no dice
cómo. Sin una anatomía fija, cada rótulo sale de un tamaño y una posición distintos, y
la mitad acaba tapando justo lo que quería señalar.

Un rótulo es la respuesta a **"¿qué es eso?"**. Nada más. Si necesita una frase, no es
un rótulo: es un dato (`44`) o una cita (`48`).

---

## Anatomía

```
        ┌── etiqueta
        │
   TUNELADORA ────────●   ← punto de anclaje sobre el objeto
   Ø 2,4 m · 1989         ← línea secundaria (opcional)
        │
        └── línea guía horizontal
```

| Pieza | Especificación |
|---|---|
| **Etiqueta** | Familia Dato (Consolas), 40-52 px, MAYÚSCULAS, interletra `.18em`, papel `#E6DCC4` |
| **Línea secundaria** | Consolas 28-34 px, interletra `.12em`, oro `#E8C547` al 78% |
| **Línea guía** | 2 px, papel al 55%, **siempre horizontal**, 90-220 px de largo |
| **Punto** | círculo de 10 px relleno, o anillo de 14 px con borde de 2 px |
| **Separación** | 16 px entre el final del texto y el arranque de la línea |
| **Ancho total** | máximo 420 px. Si no cabe, se acorta el texto, no se reduce el cuerpo |

**La línea guía nunca es diagonal ni acodada.** Una diagonal es lenguaje de catálogo de
producto; una horizontal es lenguaje de archivo y se lee en el mismo gesto que el texto.

---

## Posición

El rótulo se coloca **fuera de la silueta del objeto**, en el lado con más aire.

| Situación | Dónde va |
|---|---|
| Objeto en la mitad izquierda | Etiqueta a la derecha, línea apuntando a la izquierda |
| Objeto en la mitad derecha | Etiqueta a la izquierda, línea apuntando a la derecha |
| Retrato / figura recortada | A la altura del **pecho**, nunca de la cara |
| Objeto que ocupa todo el cuadro | Esquina inferior izquierda, sin línea guía |

Dos rótulos simultáneos van **a alturas distintas** (mínimo 120 px de separación
vertical) y **a lados distintos** si es posible. Tres rótulos a la vez es ruido: se
encadenan (`14`).

---

## Duración

Un rótulo se lee más rápido de lo que se cree, pero necesita entrar y salir.

```
duración = 0,55 s (entrada) + nº de caracteres / 16 + 0,35 s (salida)
mínimo 1,6 s · máximo 4,0 s
```

`TUNELADORA` son 10 caracteres → 0,55 + 0,63 + 0,35 = **1,53 s → se eleva al mínimo,
1,6 s**. Con línea secundaria se suman sus caracteres al mismo cómputo.

**Entra 0,20 s antes** de que la voz nombre el objeto. Si la voz no lo nombra nunca —
un objeto de fondo que el espectador no sabría identificar — el rótulo entra al
segundo 0,4 de la vida del elemento y dura el mínimo.

**No sobrevive al plano.** Si el recorte sale, su rótulo salió antes o con él.

---

## Entrada y salida

La línea guía **se dibuja**, la etiqueta **aparece**. Ese desfase es lo que hace que se
lea como una anotación y no como una capa pegada.

| Fase | Qué pasa | Duración |
|---|---|---|
| 0,00 | aparece el punto (escala 0 → 1, con rebote) | 0,12 s |
| 0,10 | la línea crece del punto hacia la etiqueta | 0,22 s |
| 0,30 | la etiqueta entra con fundido y 14 px de deriva lateral | 0,25 s |
| final | todo sale junto, fundido de 0,35 s, sin movimiento | 0,35 s |

Sonido: `ob_obturador` en el fotograma del punto, a −22 LU respecto de la voz.

---

## Implementación

El rótulo es un PNG con transparencia hecho en Chrome, y la línea se anima con `crop`
progresivo como en `41`. Plantilla de la lámina:

```html
<!doctype html><meta charset='utf-8'><style>
*{margin:0;padding:0;box-sizing:border-box}
html,body{background:transparent;overflow:hidden;width:420px;height:120px}
.dat{font-family:'Consolas','Courier New',monospace}
</style>
<div style="position:relative;width:420px;height:120px">
  <div class="dat" style="position:absolute;left:0;top:14px;width:250px;text-align:right;
       font-size:46px;letter-spacing:.18em;color:#E6DCC4">TUNELADORA</div>
  <div class="dat" style="position:absolute;left:0;top:70px;width:250px;text-align:right;
       font-size:30px;letter-spacing:.12em;color:#E8C547;opacity:.78">2,4 m · 1989</div>
  <div style="position:absolute;left:266px;top:36px;width:130px;height:2px;
       background:rgba(230,220,196,.55)"></div>
  <div style="position:absolute;left:390px;top:29px;width:16px;height:16px;
       border:2px solid #E6DCC4;border-radius:50%"></div>
</div>
```

En la tabla de eventos, anclado a la palabra y con offset negativo:

```python
{"r": "rot_tuneladora", "ancla": "tuneladora", "offset": -0.20,
 "dura": 1.9, "x": "1180", "y": "612", "w": 420,
 "entrada": "der", "dur_entrada": 0.25, "fade_out": 0.35},
```

Para animar el crecimiento de la línea, la lámina se parte en dos PNG (`rot_linea` y
`rot_texto`) y la línea se revela con la máscara de alfa de `47`, con `D = 0,22`.
(No con un `crop` que crece: `crop` no puede animar su anchura con el tiempo.)

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Línea guía diagonal o acodada | Lenguaje de catálogo de producto, no de expediente |
| Rótulo a la altura de la cara | Tapa lo único que el espectador estaba mirando |
| Etiqueta en familia Titular | Compite con el titular real; el rótulo es información secundaria |
| Rótulo que dura lo que dura el plano | Se convierte en mobiliario y deja de leerse |
| Dos rótulos a la misma altura | Se leen como una sola frase partida |
| Frase entera dentro del rótulo | Un rótulo responde "qué es", no "qué pasó" |
| Rotular lo obvio (un billete, una cara conocida) | Gasta atención en lo que no la necesita |

## Relacionado

`40` el texto como canal principal · `42` tipografía del canal ·
`44` la cifra en pantalla · `26` superposición y oclusión · `28` respiración del cuadro
