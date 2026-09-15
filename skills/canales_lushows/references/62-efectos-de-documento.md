# 62 · Efectos de documento

**Qué resuelve:** el canal se llama Paper Empires y su material es el expediente. Estos
son los gestos que convierten un texto plano en un papel que alguien manipuló: sellos,
tachados, subrayados, notas al margen, firmas y redactado.

**Regla:** el gesto se hace **encima** del documento, nunca dentro. El sello es un PNG
aparte que entra girado; no se dibuja en la misma capa que el texto. Así se anima solo
y se reutiliza en cualquier documento.

---

## 1 · Sellos (ya existen tres)

`sello_prueba`, `sello_clasif`, `sello_decomiso` en `fx.py`. El patrón, por si hace
falta otro: marco de 8 px, giro entre −9° y +7°, opacidad 0,90-0,92 y **nunca** recto.

**Entrada:** un sello no aparece con fade, **cae**. En la tabla del guion visual:

```python
{"r": "sello_prueba", "ancla": "condenado", "offset": -0.12, "dura": 2.2,
 "x": "W*0.46", "y": "H*0.34", "w": 520, "entrada": "abajo", "rot": -6.0}
```

El motor mueve la entrada 380 px en 0,36 s: eso ya es el golpe. Un sello que aparece
suave no es un sello, es una marca de agua.

---

## 2 · Redactado (los bloques negros)

Lo más característico de un documento desclasificado y lo que más rinde: **las barras
aparecen una a una** mientras la voz dice lo que no se puede decir.

```python
# Estados acumulativos: el estado k lleva las k primeras barras.
BARRAS = [(78, 214, 520), (78, 268, 660), (78, 322, 410),
          (78, 430, 700), (78, 484, 300)]      # (x, y, ancho) en px del PNG

def redactado(nombre, barras, w=980, h=620, alto=34):
    salida = {}
    for k in range(len(barras) + 1):
        cuerpo = "".join(
            f'<div class="l" style="left:{x}px;top:{y}px;width:{a}px;height:{alto}px;'
            f'background:#12100C"></div>' for x, y, a in barras[:k])
        salida[f"{nombre}_{k:02d}"] = (w, h, f"""
<div style="position:relative;width:{w}px;height:{h}px">{cuerpo}</div>""")
    return salida

F.update(redactado("redact", BARRAS))
```

Se encadenan con `cadena_serie` (`61`) usando `paso` **0,45-0,7 s**: cada barra cae
sobre una palabra concreta de la locución. Si caen todas de golpe no se lee como
censura, se lee como error de render.

**El PNG del redactado va sobre el documento, no lo sustituye.** El texto tiene que
verse debajo lo suficiente para entender que había algo escrito ahí.

---

## 3 · Tachado y subrayado (el trazo a mano)

Un trazo recto se ve de plantilla. Un trazo con curva se ve hecho a mano:

```html
<svg width="900" height="120" viewBox="0 0 900 120">
  <path d="M18 74 C 210 54, 430 92, 640 62 S 862 56, 884 70"
        stroke="#E3120B" stroke-width="14" fill="none" stroke-linecap="round"
        opacity=".92"/>
  <path d="M26 80 C 220 62, 440 98, 648 68 S 858 62, 876 76"
        stroke="#E3120B" stroke-width="5" fill="none" stroke-linecap="round"
        opacity=".38"/>
</svg>
```

El segundo trazo desplazado 6-8 px es lo que da el gesto de rotulador. Se **revela de
izquierda a derecha** con el `crop` que crece de `41`:

```
[1:v]format=rgba,
     crop=w='iw*min(1,max(0,(t-5.10)/0.42))':h=ih:x=0:y=0,
     pad=w=iw:h=ih:x=0:y=0:color=black@0[tach];
[bg][tach]overlay=x=380:y=520:enable='gte(t,5.10)'
```

**0,35-0,45 s** para tachar. Más lento parece que alguien duda; más rápido no se ve el
recorrido y vuelve a leerse como aparición.

El subrayado es lo mismo con `stroke-width:9` en amarillo dato y `opacity:.6`, y va
**debajo** de la línea de texto, no encima: si tapa la palabra que subraya, sobra.

---

## 4 · Anotación manuscrita

Windows trae `Segoe Script` instalada, así que Chrome headless la resuelve sin
descargar nada. Girada, en el margen, y **corta**: tres o cuatro palabras.

```html
<div style="position:relative;width:520px;height:180px">
  <div class="l" style="left:0;top:20px;width:520px;font-family:'Segoe Script',cursive;
       font-size:44px;color:#E3120B;transform:rotate(-4.2deg);line-height:1.15">
    ¿de dónde salió<br>este dinero?</div>
  <div class="l" style="left:-46px;top:34px;width:38px;height:38px;
       border-left:5px solid #E3120B;border-bottom:5px solid #E3120B;
       transform:rotate(-40deg)"></div>
</div>
```

La flecha construida con dos bordes girados es más fiel que una flecha tipográfica.

---

## 5 · Firma que se firma

Una firma se traza en 0,7-1,0 s. Como casi siempre avanza de izquierda a derecha, el
`crop` que crece basta y evita generar estados. Cuando la firma vuelve sobre sí misma
(rúbricas cerradas), el `crop` la revela en el orden equivocado: ahí toca la serie con
`stroke-dasharray`, documentada en `64`, que es el mismo problema del trazado de ruta.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Sello con entrada `fade` | Se lee como marca de agua, no como acto |
| Sello recto | Delata que es un `div`, no un tampón |
| Todas las barras del redactado a la vez | Parece un fallo de render, no censura |
| Redactado que tapa el documento entero | No se entiende que debajo había un texto |
| Tachado con trazo recto | Efecto de plantilla; el trazo tiene que curvarse |
| Tachar en menos de 0,25 s | No se ve el recorrido: vuelve a ser una aparición |
| Subrayado por encima de la palabra | Tapa justo lo que quiere destacar |
| Anotación larga | Nadie lee cursiva girada de más de cuatro palabras |
| Dibujar el sello dentro del HTML del documento | Deja de poder animarse y de reutilizarse |

## Relacionado

`48` citas y documentos · `25` el borde de papel · `41` revelado por `crop` · `64` `stroke-dasharray` · `77` el tachado como transición
