# 411 · Caras: lo único que no se tapa nunca

**Qué resuelve:** de todos los intocables, la cara es el que más se pierde y el que menos se mide,
porque «se ve» aunque esté mal. Aquí está el criterio exacto —**la línea de los ojos**, no la cara
entera— y cómo se comprueba con la caja del plano, sin detector y sin ojo.

El `45` ya dice que una cara medio tapada por el caption sigue funcionando y un texto no. Cierto, y es
la mitad de la historia. La otra mitad: **hay un pedazo de la cara que no aguanta nada**.

---

## La jerarquía dentro de la propia cara

| Parte | Tolerancia a oclusión | Qué pasa si se tapa |
|---|---|---|
| **Ojos** (banda de ~0,22 a ~0,32 del alto del rostro) | **0,00** | Deja de ser una persona y pasa a ser una forma |
| Frente y pelo | 0,50 | No se nota; el caption de Instagram lo hace todo el rato |
| Boca | 0,30 | Se pierde el gesto, se entiende igual (salvo si el vídeo depende del labio) |
| Mentón y cuello | 0,60 | Irrelevante |
| Cuerpo | 0,70 | Irrelevante |

De ahí la regla operativa, que es una sola línea: **la línea de los ojos no entra jamás en una banda de
interfaz, ni en la banda de la barra del reproductor (`416`), ni en el borde de la ventana de recorte.**

## Dónde cae la línea de los ojos

Medido a mano una vez sobre los retratos del banco del canal: en un retrato de archivo encuadrado a
medio cuerpo, los ojos caen entre el **0,22 y el 0,30 de la altura del propio recorte**. Eso convierte
la comprobación en aritmética sobre la caja del elemento, sin necesidad de detectar nada:

```
ojos_y = y_declarada + alto_del_elemento × 0,26
alto_del_elemento = ancho_mostrado × (alto_PNG / ancho_PNG)
```

Y la posición deseable, en el cuadro, en tanto por uno de la altura:

| Formato | Línea de ojos | En píxeles | Si se baja |
|---|---|---|---|
| 9:16 · 1080×1920 | **0,30 – 0,36** | 576 – 691 | El retrato se lee hundido y el caption le come el mentón |
| 16:9 · 1920×1080 | **0,33 – 0,42** | 356 – 454 | Por debajo de 0,55 el plano parece un descuido |
| 1:1 · 1080×1080 | 0,33 – 0,40 | 356 – 432 | — |

---

## La comprobación, ejecutada

`rostros.py`, corrido el **11-sep-2026** sobre `ep01-lustig` del canal documental:

```python
OJOS   = 0.26                  # línea de ojos, en tanto por uno del alto del recorte
VETADA = (0.78, 0.86)          # banda de la barra de YouTube (416)
CARAS  = {"retrato_lustig", "ficha_policial"}     # lista EXPLÍCITA, nunca por subcadena

for el in elementos:
    if el["r"] not in CARAS: continue
    iw, ih = Image.open(buscar(el["r"])).size
    alto = el["w"] * ih / iw
    ojos = coord(el["y"]) + alto * OJOS
    ...
```

```
elemento                   y  alto  ojos y  ojos t/1  estado
ficha_policial           108   726     297     0.275  ok
retrato_lustig           281   777     483     0.447  barbilla en la banda
```

El retrato principal del episodio tiene los ojos a 0,447 —demasiado bajo para 16:9— y el mentón
metido en la banda de la barra. Ninguna auditoría de cobertura lo veía, porque de superficie va
sobrado.

> **Trampa del arnés, no del vídeo:** la primera versión seleccionaba las caras por subcadena
> (`"preso" in nombre`) y metía `d_preso`, que es un dato, no un rostro. Lista explícita siempre.

---

## Recortar centrando en la cara, no en el cuadro

Al pasar de 16:9 a vertical, el recorte centrado deja la cara donde caiga. Se centra en los ojos:

```bash
# ventana vertical de 608 px centrada en la cara (x=400), no en el cuadro (x=656)
ffmpeg -v error -ss 28 -i ep01.mp4 -vf "crop=608:1080:400:0,scale=1080:1920:flags=lanczos" \
  -frames:v 1 -y rec_face.png
# el mismo instante con recorte central, para comparar
ffmpeg -v error -ss 28 -i ep01.mp4 -vf "crop=608:1080:656:0,scale=1080:1920:flags=lanczos" \
  -frames:v 1 -y rec_centro.png
```

El `x` de la ventana sale de la caja de la cara: `x = cara_cx − 304`, recortado a `[0, W−608]`. Los dos
PNG uno al lado del otro deciden en tres segundos lo que discutir no decide en diez minutos.

---

## Detectar caras: lo que hay hoy en esta máquina

Para material rodado (Bendita Pola, testimonios de GastroLatam) la caja no está declarada y hay que
detectarla. **Comprobado el 11-sep-2026: OpenCV 5.0.0 ya no expone `cv2.CascadeClassifier` ni el módulo
`cv2.objdetect`** — el código de tutorial que circula falla con `AttributeError`. Lo que queda es
`cv2.FaceDetectorYN`, que necesita el modelo ONNX de YuNet descargado aparte:

```python
det = cv2.FaceDetectorYN.create("face_detection_yunet_2023mar.onnx", "", (w, h))
_, caras = det.detect(img)      # caras[i] = [x, y, w, h, ojo_d_x, ojo_d_y, ...]
```

Ese detector **devuelve los ojos como puntos**, así que con él el 0,26 deja de ser una estimación y
pasa a ser una medida. Mientras no esté el modelo, la aritmética de la caja es suficiente y honesta.

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Proteger «la cara» en vez de la línea de los ojos | Se salva el pelo y se pierde la mirada |
| Centrar el retrato verticalmente | Ojos hacia 0,50: el plano se lee hundido y el caption muerde el mentón |
| Recortar a vertical por el centro del cuadro | La cara acaba donde caiga, a veces partida por el borde |
| Seleccionar las caras por subcadena del nombre | `d_preso` entra como si fuera un rostro |
| Copiar el `CascadeClassifier` de los tutoriales | En OpenCV 5 no existe: `AttributeError` sin más explicación |
| Descentrar el sujeto a la derecha en 9:16 | Debajo viven los iconos (`45`) |
| Dar por buena una cara porque «ocupa mucho» | La superficie no dice nada de dónde están los ojos |
| No comparar los dos recortes en PNG | Se decide discutiendo en vez de mirando |

## Relacionado

`410` el mapa de intocables · `416` la banda de la barra · `417` del vertical al cuadrado ·
`418` medir de verdad · `147` composición vertical y la regla del tercio superior ·
`45` qué sí puede ir en la zona muerta
