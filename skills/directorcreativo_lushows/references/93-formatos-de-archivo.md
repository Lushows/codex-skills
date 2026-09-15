# 93 — Formatos de archivo

Entregar el formato equivocado es como dar las llaves de otro carro: técnicamente es una llave, pero no sirve. Esta es la guía para saber qué archivo entregar para cada uso.

## La gran división: vector vs mapa de bits
Toda imagen digital es una de dos cosas:

- **Vector:** la imagen está hecha de fórmulas matemáticas (puntos, líneas, curvas). **Se agranda infinitamente sin perder nitidez.** Ideal para logos e íconos. Formatos: SVG, AI, EPS, PDF (vectorial).
- **Mapa de bits (rasterizado / bitmap):** la imagen es una cuadrícula de pixeles. Al agrandarla, se pixela. Ideal para fotos. Formatos: PNG, JPG, WebP, TIFF.

**Regla mental:** ¿es un dibujo de líneas/formas (logo, ícono)? → **vector**. ¿Es una foto con muchos matices? → **mapa de bits**.

## Los formatos, uno por uno

### Vector
| Formato | Qué es | Cuándo entregarlo |
|---|---|---|
| **SVG** | Vector para web, ligero, editable, escalable | Logo/íconos para web y apps |
| **AI** | Archivo nativo de Illustrator (editable) | Archivo maestro del logo (para el diseñador) |
| **EPS** | Vector universal, lo piden imprentas y proveedores | Mandar logo a un tercero (bordador, serigrafía) |
| **PDF (vector)** | Universal, abre en todo, mantiene vector | Entrega general, manuales, print |

### Mapa de bits
| Formato | Qué es | Transparencia | Cuándo entregarlo |
|---|---|---|---|
| **JPG** | Foto comprimida, liviana, sin transparencia | No | Fotos, imágenes sin fondo transparente |
| **PNG** | Imagen con transparencia, sin pérdida | Sí | Logo sobre fondo, gráficos con bordes nítidos |
| **WebP** | Formato web moderno, pesa menos que JPG/PNG | Sí | Web: mejor velocidad de carga |
| **TIFF** | Máxima calidad, pesado, sin compresión | Sí | Impresión de fotos de alta calidad |

## Tabla de decisión rápida

| Necesito entregar... | Formato correcto |
|---|---|
| Logo para web | **SVG** (+ PNG de respaldo) |
| Logo maestro (editable) | **AI** + **PDF** |
| Logo para un proveedor externo | **EPS** o **PDF** |
| Logo para imprenta | **PDF vectorial** (CMYK, ver 92) |
| Foto de producto para web | **JPG** o **WebP** |
| Imagen con fondo transparente | **PNG** |
| Foto para imprimir en alta | **TIFF** o **PDF** a 300 dpi |
| Post de redes sociales | **PNG** o **JPG** |
| Web que cargue rápido | **WebP** (con fallback JPG/PNG) |

## Transparencia (el detalle que confunde)
- **JPG NO tiene transparencia.** Si guardas un logo sin fondo en JPG, aparece un **fondo blanco** (o el color que sea). Por eso un logo recortado va en **PNG** o **SVG**, nunca JPG.
- **PNG y SVG sí** mantienen el fondo transparente.

## Compresión (calidad vs peso)
- **JPG** comprime "con pérdida": cada vez que guardas, pierde un poco de calidad. No lo uses para guardar repetidas veces ni para gráficos con líneas duras (aparecen "fantasmas").
- **PNG** comprime "sin pérdida": mantiene calidad, pero pesa más. Ideal para gráficos, malo para fotos pesadas en web.
- **WebP** es el equilibrio moderno: buena calidad, peso bajo, con o sin transparencia.

## El paquete de entrega del logo (estándar profesional)
Cuando entregas un logo, no das un archivo: das un **kit**. Carpeta organizada:

```
LOGO-MARCA/
├── editable/
│   └── logo.ai           ← archivo maestro
├── vector/
│   ├── logo.svg          ← web
│   ├── logo.eps          ← proveedores
│   └── logo.pdf          ← universal/print
├── png/
│   ├── logo-color.png        (fondo transparente)
│   ├── logo-blanco.png       (para fondos oscuros)
│   └── logo-negro.png
└── jpg/
    └── logo-fondo-blanco.jpg  ← cuando se necesita con fondo
```

Esto es lo que separa una entrega amateur ("toma el PNG") de una profesional (ver 99 sobre entrega).

## Errores comunes de formato
- Logo en JPG → fondo blanco indeseado. **Usa PNG/SVG.**
- Logo solo en PNG, sin vector → no se puede ampliar para una valla. **Entrega vector.**
- Foto en PNG pesado para web → carga lenta. **Usa JPG/WebP.**
- Mandar el .AI a un cliente sin Illustrator → no lo puede abrir. **Incluye PDF.**

## Mini-checklist de formatos
- [ ] ¿Logo/ícono? → vector (SVG/AI/EPS/PDF).
- [ ] ¿Foto? → mapa de bits (JPG/WebP/TIFF).
- [ ] ¿Necesito transparencia? → PNG o SVG, nunca JPG.
- [ ] ¿Es para web? → optimizado (WebP/JPG, SVG para logos).
- [ ] ¿Es para imprenta? → PDF/TIFF, CMYK, 300 dpi (ver 92).
- [ ] ¿Entregué el kit completo, no un solo archivo? (ver 99)

**Siguiente paso:** con el formato claro, prepara la exportación según destino (92) y arma la entrega ordenada (99).
