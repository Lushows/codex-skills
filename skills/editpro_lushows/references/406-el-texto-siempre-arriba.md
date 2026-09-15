# 406 — El texto siempre arriba (y sus excepciones)

**Qué resuelve:** «el texto va arriba de todo» es la regla que todo el mundo repite y casi nadie sabe
justificar. Importa saberlo, porque **la razón verdadera no es la jerarquía: es que el texto se rompe con
mucho menos que una foto**, y esa asimetría se puede medir. Quien entiende la razón acierta también en los
tres casos en que el texto debe ir debajo.

`383` tiene el experimento del umbral doble. Aquí está por qué ese umbral tiene que existir.

---

## 1. La regla real, tal y como está escrita en el motor

En `diccionario.py:480`, dentro del bucle que busca sitio para cada elemento generado:

```python
# Sobre TEXTO el liston es otro: cualquier solape lo hace ilegible.
# Con el umbral unico del 42% entraban recortes encima de las cifras
# y el sistema los daba por buenos.
tope = 0.05 if (txt or es_texto(recurso)) else 0.42
```

**0,05 contra 0,42.** Un recorte puede quedar tapado un 42% y sigue valiendo; a un texto no se le tolera
ni un 5%. Y fíjate en que esto no es una regla de apilado: es una regla de **colocación**. El texto no se
protege poniéndolo encima, se protege **no dejando que nada aterrice sobre su rectángulo**.

---

## 2. Por qué el 5%: lo que se pierde al tapar una cifra

Rotulada `$ 20.000` en Arial Black a 110 px, midiendo la tinta que queda visible al taparla por la derecha
—que es el lado bueno, porque tapar el arranque la hace irrecuperable (`377` §3)—:

| tapado del ancho | tinta perdida | signos completos que quedan | qué se lee |
|---|---|---|---|
| 10 % | 14,0 % | 6 de 7 | `$ 20.00` |
| **20 %** | **24,4 %** | **5 de 7** | **`$ 20.0`** |
| 30 % | 34,2 % | 4 de 7 | `$ 20.` |
| 40 % | 48,5 % | 4 de 7 | `$ 20.` |

Tapar el 20% de una cifra no la deja «un poco tapada»: **la convierte en otra cifra**. Veinte mil pasa a
leerse veinte coma cero. Nadie protesta, nadie lo nota en la revisión, y la pieza dice un número que no es.
A una foto tapada un 20% no le pasa nada equivalente: pierde el 20% de su superficie y sigue siendo la
misma calle de París.

---

## 3. Ninguna métrica de píxel sabe esto

La tentación es automatizar el umbral con una medida de imagen. No funciona, y funciona **al revés**.
Recortando las dos piezas a su misma caja útil (418 × 160) y tapando la misma fracción:

| tapado | SSIM foto | SSIM cifra |
|---|---|---|
| 10 % | 0,904 | 0,954 |
| **20 %** | **0,798** | **0,912** |
| 30 % | 0,700 | 0,873 |
| 40 % | 0,598 | 0,822 |

SSIM dice que al 20% la **foto** está tocada (0,798) y la **cifra** está casi intacta (0,912). El
significado dice exactamente lo contrario. La razón es sencilla: una cifra es casi toda fondo vacío con
unos trazos finos encima, así que tapar un trozo mueve pocos píxeles; pero cada trazo es un símbolo cuyo
valor depende de estar completo.

> **Conclusión de oficio:** el umbral de pisada **no se puede derivar de la imagen. Sale del tipo de
> contenido.** Por eso `es_texto(recurso)` está en el código y no un `if ssim < 0.9`.

---

## 4. Las tres veces que el texto va debajo

Siendo el orden una decisión narrativa (`400`), hay tres casos legítimos en que el texto **no** va arriba:

| Caso | Dónde va | Por qué |
|---|---|---|
| **Sándwich** con el sujeto (`377`) | entre las dos copias del clip | El texto está en un plano espacial detrás de la persona |
| Texto que debe **pertenecer al plano** (`204` §2) | debajo de la pista de efectos | Un rótulo a color sobre un plano en blanco y negro se ve pegado |
| Texto que **es una imagen**: titular de periódico, ficha, telegrama | donde le toque como recorte | No es texto del montaje, es material de archivo; su umbral es 0,42 |

El tercero se cuela a menudo en la dirección contraria: alguien marca como texto un recorte de periódico
y el colocador automático empieza a rechazar posiciones perfectamente válidas porque le exige 0,05.

Y la excepción que nunca se negocia, en el otro sentido: **el texto de servicio** —precio, dirección,
horario, llamada a la acción— va arriba de todo y **limpio, sin efecto de imagen encima** (`204` §2). Un
precio bajo «Cassette defectuoso» no se lee, y ese texto existe exactamente para leerse.

---

## 5. Estar arriba no es ser legible

Lo último, y lo que más piezas arruina: el z solo protege de que te tapen. **No protege del fondo sobre el
que caes.** Un rótulo blanco encima de todo, aterrizando sobre un cielo blanco, es perfectamente visible en
el apilado y perfectamente ilegible en pantalla. Eso es contraste, y se mide aparte: `376` y `412` en esta
skill, `canales_lushows/163` para el contraste elemento-fondo y `canales_lushows/164` para la legibilidad
por altura.

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Justificar «el texto arriba» por jerarquía | Se aplica también donde el texto debe ir debajo |
| Un umbral de pisada único para todo | Con el 42%, entran recortes encima de las cifras y el sistema los aprueba |
| Derivar el umbral de una métrica de imagen | SSIM ordena al revés: la cifra rota puntúa mejor que la foto intacta |
| Aceptar un 20% de pisada sobre una cifra | La pieza publica un número distinto del real |
| Tapar el arranque de la palabra en vez del final | Deja de ser recuperable para el lector |
| Marcar un recorte de prensa como «texto» | El colocador rechaza posiciones válidas por exigirle 0,05 |
| Meter el texto de servicio dentro del efecto global | El precio no se lee |
| Dar por legible un texto porque está arriba | Arriba no es contraste (`376`, `412`) |

## Relacionado

`400` el orden de render es narrativo · `401` quién gana cuando dos coinciden · `402` el z dinámico ·
`377` texto detrás del sujeto · `379` números y cifras en pantalla · `376` legibilidad real en celular ·
`382` la zona protegida · `383` umbrales por tipo de contenido · `412` texto y cifras ·
`204` §2 el orden de render · `canales_lushows/163` contraste elemento-fondo ·
`canales_lushows/164` legibilidad por altura · `canales_lushows/44` la cifra en pantalla
