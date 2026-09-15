# 303 · Grabado y técnicas de impresión de la lámina

> Cada look de lámina es en realidad **la huella de una máquina**. Entender qué máquina hizo
> esa marca es lo que permite reproducir el look a propósito en vez de por accidente.

---

## 1 · Las seis técnicas y su huella

| Técnica | Cómo se hace | Huella reconocible | Época |
|---|---|---|---|
| **Xilografía** | Se talla la madera y se imprime lo que queda alto | Línea **gruesa y uniforme**, esquinas romas, negro sólido. Sin medios tonos | s. XV–XVI |
| **Talla dulce (buril)** | Se abre el surco en cobre; la tinta queda **dentro** | Línea de **grosor variable**, punta afiladísima, trama que envuelve. Blanco absoluto | s. XVI–XIX |
| **Aguafuerte** | Se dibuja sobre barniz y el ácido muerde el cobre | Línea **más suelta y nerviosa** que el buril: es dibujo, no talla | s. XVII– |
| **Punteado / *stipple*** | Miles de puntos con punzón sobre cobre | Degradado **suavísimo, sin línea**. Es la técnica de Redouté | s. XVIII |
| **Litografía** | Dibujo graso sobre piedra; agua y grasa se repelen | Permite **lavado y medio tono continuo**. Se ve "dibujado", no "tallado" | s. XIX |
| **Semitono *(halftone)*** | Retícula de puntos de tamaño variable | **Roseta visible** al acercarse. Es la imprenta moderna | s. XX– |

---

## 2 · Por qué esto le importa a un director creativo

Cuando un cliente dice "que se vea antiguo", puede querer cosas opuestas:

- Xilografía → **tosco, popular, medieval**
- Talla dulce → **preciso, caro, institucional**
- Litografía → **suave, romántico, s. XIX**

Son tres marcas distintas. Nombrar la técnica cierra la ambigüedad de una.

---

## 3 · Cómo se falsifica cada huella hoy

| Para imitar… | Haz esto | Nunca hagas esto |
|---|---|---|
| **Talla dulce** | Trazo de ancho variable (polígono relleno, no `stroke-width`), trama que envuelve, blanco puro del papel | Línea de grosor constante |
| **Punteado** | Puntillismo denso, sin ninguna línea de trama | Mezclar puntos con rayado |
| **Xilografía** | Grosor uniforme, terminaciones romas, contraste absoluto | Degradados |
| **Litografía** | Manchas de valor con borde blando, textura de grano | Contornos duros |
| **Riso** | Semitono grueso visible, dos tintas planas **mal registradas a propósito** | Registro perfecto |

> Ver la implementación en código en [[301-ilustracion-generativa-por-codigo]].

---

## 4 · El registro: el detalle que da verdad

En impresión antigua a varias tintas, las planchas **nunca calzaban perfecto**. Ese desfase
mínimo —medio milímetro— es lo que hace que una pieza se lea como impresa y no como digital.

Reproducirlo: desplazar la segunda tinta 0.3–0.8 pt respecto a la primera. Un solo detalle,
efecto enorme. **Sistemático, no aleatorio**: siempre el mismo desfase, o se ve como error.

---

## 5 · La textura del papel

- **Verjurado** *(laid)*: líneas paralelas visibles al trasluz. Papel antiguo.
- **Vitela** *(wove)*: liso y parejo. Papel moderno, desde 1750.
- **Algodón**: fibra visible, borde deckle irregular.

En digital se simula con ruido fino de baja opacidad — **nunca** con una foto de papel arrugado,
que es el error más común y el que más abarata.

---

## 6 · Llevarlo a producción real

- Una lámina de una tinta se imprime en **tinta plana (Pantone)**, no en CMYK: el punto queda
  limpio y el color exacto.
- El puntillismo tiene un **límite físico**: por debajo de 0.3 pt el punto no imprime en offset.
  En serigrafía el límite es mucho mayor.
- Si la lámina va sobre color, considerar **sobreimpresión** *(overprint)* en vez de reserva:
  la tinta se mezcla y da riqueza.

Ver `171-sustratos-y-tecnicas-de-impresion` y `92-preparar-para-produccion`.
