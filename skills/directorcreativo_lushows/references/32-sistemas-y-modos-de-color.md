# 32 — Sistemas y modos de color

Un mismo color "vive" en varios sistemas según dónde aparezca: pantalla, web o imprenta. Si no entiendes esto, tu rojo de marca se verá distinto en el celular, en la web y en la caja impresa. Aquí está cada sistema, cuándo usarlo y por qué un color cambia de un medio a otro.

## RGB — el color de la LUZ (pantallas)
RGB = Red, Green, Blue. Las pantallas EMITEN luz mezclando estos tres. Es **aditivo**: sumar los tres da blanco; sin luz, negro.
- Cada canal va de 0 a 255. Ej: rojo puro = `R255 G0 B0`.
- Úsalo para: pantallas, video, redes sociales, apps, presentaciones.
- Gama amplia y colores vibrantes que el papel NO puede reproducir (verdes y azules eléctricos).

## HEX — RGB escrito para web
HEX es la misma info de RGB pero en código hexadecimal de 6 dígitos: `#RRGGBB`. Es el formato estándar en diseño web y digital.
- `#FF0000` = rojo (FF=255, 00, 00). `#000000` = negro. `#FFFFFF` = blanco.
- Los primeros 2 = rojo, los del medio = verde, los últimos = azul.
- Úsalo para: CSS, especificar colores a un desarrollador, herramientas de diseño.
- Es RGB; por tanto comparte gama y limitaciones con RGB.

## HSB / HSL — RGB pensado para HUMANOS
Mismo color que RGB pero descrito por Matiz, Saturación y Brillo/Luminosidad (ver 30). No es un sistema de salida distinto: es una forma más **intuitiva de manipular** el color.
- **HSB/HSV** (Hue, Saturation, Brightness): el de la mayoría de apps de diseño.
- **HSL** (Hue, Saturation, Lightness): común en CSS; 50% lightness = color pleno.
- Úsalo para: crear escalas y variaciones (subir/bajar saturación o luz manteniendo el matiz), construir paletas coherentes.

## CMYK — el color de la TINTA (imprenta)
CMYK = Cyan, Magenta, Yellow, Key(negro). La imprenta REFLEJA luz: el papel es blanco y las tintas RESTAN luz. Es **sustractivo**: más tinta = más oscuro.
- Valores en porcentaje 0–100. Ej: un naranja podría ser `C0 M60 Y100 K0`.
- Úsalo para: cualquier cosa que se IMPRIME en offset/digital (tarjetas, empaques, folletos, etiquetas).
- Gama MÁS PEQUEÑA que RGB: no puede reproducir los neones de pantalla. Por eso un azul eléctrico vibrante en web sale "apagado" impreso.

## Pantone / PMS — TINTA EXACTA (color directo)
El Pantone Matching System es un catálogo de tintas premezcladas con un código fijo (ej: **Pantone 485 C** = el rojo de tantas marcas). En vez de mezclar CMYK, la imprenta usa UNA tinta exacta y predecible.
- Garantiza que tu color de marca sea IDÉNTICO en cualquier imprenta del mundo.
- Imprescindible para colores corporativos críticos: el **Tiffany Blue (1837)**, el púrpura de **Cadbury (2685 C)**, el rojo Coca-Cola.
- Sufijos: **C** = coated (papel brillante), **U** = uncoated (papel mate/poroso) — ¡el mismo número se ve distinto según el papel!
- Úsalo para: logos, identidad, empaques donde el color NO puede variar. Cuesta más (tinta extra) pero es la única garantía de fidelidad.

## ¿Por qué un color se ve DISTINTO en pantalla vs impreso?
1. **Aditivo vs sustractivo**: la pantalla emite luz; el papel la refleja. Físicas opuestas.
2. **Gama distinta**: RGB abarca más colores que CMYK. Lo que brilla en pantalla puede ser inalcanzable en tinta.
3. **El papel y la luz ambiental**: papel mate "apaga" el color; la luz de la sala cambia la percepción.
4. **Cada pantalla está calibrada distinto** (ver 39): tu rojo en tu monitor no es el rojo del celular del cliente.

**Por eso una marca seria define su color en VARIOS sistemas a la vez**, no solo en HEX.

## Cuándo usar cada uno (tabla de decisión)
| Necesito... | Sistema |
|---|---|
| Web, app, redes, video | RGB / HEX |
| Crear escalas y variantes | HSB / HSL |
| Imprimir folletos, tarjetas, empaque a todo color | CMYK |
| Garantizar el color EXACTO de marca impreso | Pantone (PMS) |
| Una tela, plástico, pintura de marca | Pantone (referencia base) |

## Cómo especificar UN color de marca (lo mínimo profesional)
Para cada color de tu paleta, define los 4 valores:
```
Verde BIO-SETA
HEX     #2E7D32
RGB     46, 125, 50
CMYK    78, 18, 100, 5   (aprox.)
Pantone 7740 C
```
Así el desarrollador, el diseñador y la imprenta usan el MISMO color. (Plantilla completa de paleta en 33.)

## Errores típicos
- [ ] Mandar a imprenta archivos en RGB → la imprenta convierte sola y el color cambia sin avisar.
- [ ] Elegir un color neón en pantalla y esperar que salga igual en papel.
- [ ] Dar solo el HEX a la imprenta (no entiende HEX; necesita CMYK o Pantone).
- [ ] Olvidar el sufijo C/U en Pantone y recibir un color "raro" en papel mate.
- [ ] Confiar en cómo se ve en TU monitor sin calibrar (ver 39).

## Mini-checklist
- [ ] Cada color de marca tiene HEX, RGB, CMYK y Pantone.
- [ ] Lo digital va en RGB/HEX; lo impreso en CMYK/Pantone.
- [ ] Para empaque/etiqueta crítica, defino un Pantone.
- [ ] Avisé a la imprenta del tipo de papel (coated/uncoated).

**Siguiente paso:** con los sistemas claros, arma la paleta completa con roles y los 4 valores por color en 33.
