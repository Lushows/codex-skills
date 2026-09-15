# 417 · Del vertical al cuadrado: qué sobrevive al reencuadre

**Qué resuelve:** `38` da la estrategia —el cuadrado sagrado, los recortes con sus números, por qué el
16:9 no sale por recorte— y `147` da la composición vertical. Ninguno de los dos responde la pregunta
operativa: **antes de exportar, ¿cuántos de mis intocables sobreviven a cada recorte?** Aquí está la
medida, que se hace en dos segundos y evita la ronda de «exporta los cuatro y míralos».

---

## Las ventanas, en píxeles y en tanto por uno

Recorte **centrado**, que es el que aplican las plataformas cuando tú no decides.

**Desde un máster 1920×1080 (horizontal → vertical): se pierde ancho**

| Destino | Ventana x | Ancho | t/1 del ancho | Superficie conservada |
|---|---|---|---|---|
| 1:1 | 420 – 1500 | 1080 | 0,562 | 0,562 |
| 4:5 | 528 – 1392 | 864 | 0,450 | 0,450 |
| **9:16** | **656 – 1264** | **608** | **0,316** | **0,316** |

**Desde un máster 1080×1920 (vertical → cuadrado): se pierde alto**

| Destino | Ventana y | Alto | t/1 de la altura | Recorte |
|---|---|---|---|---|
| 4:5 | 285 – 1635 | 1350 | 0,703 | `crop=1080:1350:0:285` |
| 1:1 | 420 – 1500 | 1080 | 0,562 | `crop=1080:1080:0:420` |

Las dos direcciones pierden casi lo mismo en superficie, pero **no pierden lo mismo**: bajando de
horizontal a vertical se van los lados, donde vive el contexto; bajando de vertical a cuadrado se van
arriba y abajo, donde viven el rótulo y el remate.

---

## La medida: cuántos intocables sobreviven

Ejecutado el **11-sep-2026** sobre los 61 elementos del episodio piloto 16:9 del canal documental:

```python
def ventana(W, H, r):
    if W/H > r: w, h = H*r, H
    else:       w, h = W, W/r
    return ((W-w)/2, (H-h)/2, (W+w)/2, (H+h)/2)

for k, (a, b) in VENT.items():
    vis = max(0.0, min(x1, b) - max(x0, a))
    if vis > 0:            vivos[k] += 1          # asoma algo
    if vis >= anc * 0.98:  enteros[k] += 1        # cabe entero
```

```
1:1   ventana x  420-1500  ancho 1080 (0.562) · asoman 61/61 · enteros  6/61 (0.10)
4:5   ventana x  528-1392  ancho  864 (0.450) · asoman 60/61 · enteros  4/61 (0.07)
9:16  ventana x  656-1264  ancho  608 (0.316) · asoman 55/61 · enteros  1/61 (0.02)
```

**Uno de sesenta y uno.** Ésa es la respuesta honesta a «¿saco los cortes verticales recortando el
episodio?». No. Y fíjate en la trampa de la primera columna: **asoman 55 de 61**, así que un vistazo
rápido al vídeo recortado da la sensación de que «se ve todo». Se ve un trozo de todo, que no es lo
mismo. La medida que sirve es la de «cabe entero», y sólo para los intocables: al fondo y a la textura
les da igual quedarse a medias.

---

## Qué muere en cada dirección

| Dirección | Lo primero que se pierde | Se arregla |
|---|---|---|
| 16:9 → 9:16 | Todo lo ancho: líneas de tiempo, comparativas, mapas, rótulos largos | Rehacer la pieza estrecha, no recortarla |
| 16:9 → 9:16 | La firma de esquina (`413`): no hay esquina dentro de la ventana | Recolocar por formato |
| 9:16 → 1:1 | El rótulo superior y el remate inferior | Meterlos en el cuadrado sagrado (`38`) |
| 9:16 → 4:5 | Sólo el aire; es el recorte barato | Nada, si se compuso en 1080×1350 (`147`) |
| Cualquiera | La composición | Se asume: se encuadra con menos gracia para poder adaptar |

---

## Recortar decidiendo, no aceptando el centro

Cuando el recorte central mata el intocable, la ventana se mueve. Para una cara, se centra en los ojos
(`411`); para un documento, en la zona con texto:

```bash
# ventana vertical de 608 px puesta sobre el sujeto (x=400), no sobre el centro (x=656)
ffmpeg -v error -ss 28 -i ep01.mp4 -vf "crop=608:1080:400:0,scale=1080:1920:flags=lanczos" \
  -frames:v 1 -y rec_face.png
```

Y si el intocable no cabe ni moviendo la ventana, el recorte no es la herramienta: hay que **rehacer
el plano para el formato**, o aplicar la escalera de `419`. Para el canal documental eso significa una
tabla de eventos aparte para los cortes verticales, con piezas propias y menos elementos por plano.

---

## El orden que ahorra el trabajo

1. Decidir formatos **antes** de montar (`38`).
2. Declarar los intocables (`410`).
3. Correr la medida de supervivencia sobre la tabla de eventos, **antes de renderizar nada**.
4. Los que no sobreviven: recolocar, rehacer o renunciar (`419`).
5. Verificar la salida recortada con un fotograma, no con el máster.

El paso 3 cuesta dos segundos y sustituye a exportar cuatro versiones y revisarlas a ojo.

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Contar «asoma» en vez de «cabe entero» | 55 de 61 parecen bien y sólo 1 lo está |
| Sacar el vertical recortando un 16:9 ya montado | Sobrevive el 0,316 del ancho: es amputación, no adaptación |
| Aceptar el recorte centrado por defecto | El intocable acaba donde caiga |
| Heredar la firma de esquina | En 9:16 no hay ninguna esquina dentro de la ventana (`413`) |
| Revisar sólo el máster | Cada salida es un vídeo distinto y se verifica aparte |
| Medir después de renderizar | El cálculo se hace sobre la tabla, antes de gastar minutos de render |
| Estirar para llenar | Deforma caras y se nota siempre (`38`) |
| Olvidar que Instagram recorta el Reel a 4:5 en el feed | La mitad del público ve un recorte que tú no revisaste |

## Relacionado

`38` el cuadrado sagrado y los recortes · `147` componer en vertical y recortar con movimiento ·
`411` centrar en la cara · `413` la firma bajo recorte · `410` el mapa de intocables ·
`419` cuando no cabe en ningún formato
