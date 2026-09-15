# 194 · Packshot y ghost-mannequin para e-commerce (specular control + specs Amazon)

> El packshot e-commerce es **quirúrgico**: fondo blanco puro, producto fiel, cero adornos. El ghost-mannequin
> (maniquí invisible) hace que la prenda flote en 3D mostrando forma e interior. Ambos viven o mueren por el **borde y el specular**.

## Specs Amazon (imagen principal — cúmplelas o suprimen el listado)
| Regla | Valor exacto |
|---|---|
| Fondo | **RGB 255,255,255 puro** (off-white/crema/gris → suspensión automática) |
| Producto ocupa | **≥85%** del cuadro |
| Resolución | ≥1000px lado largo (zoom); **2000+ recomendado** |
| Formato | JPEG/PNG/TIFF/GIF (sin GIF animado) |
| Prohibido | texto, logos, marcas de agua, props, insets |

Los detectores de Amazon ven el "blanco que no es 255" aunque a tu ojo parezca blanco. Genera el packshot con **fondo flat RGB(255,255,255)** y verifica el histograma; reserva escena/lifestyle para imágenes secundarias.

## Ghost-mannequin: qué es y cómo se arma
Efecto "maniquí invisible": la prenda se ve como si la llevara un cuerpo, pero el cuerpo no está → muestra **forma, caída e interior** (cuello, etiqueta interna). Reduce devoluciones porque el cliente lee fit y volumen.
- **Clásico**: foto en maniquí + foto del interior (cuello por dentro) → composición en Photoshop quitando el maniquí. $10-30/img, 15-30 min.
- **IA (2026)**: de una sola foto en maniquí/percha el modelo borra el soporte, reconstruye el interior y normaliza luz. ~$3-8/img, segundos. ~47% de retailers de moda planean adoptarlo (encuesta eMarketer 2025); -80/85% en costo de contenido.

## Pipeline IA del ghost-mannequin
```
foto en maniquí → segmentar prenda (BiRefNet/SAM) → borrar soporte → reconstruir cuello/interior (inpaint) → relight → fondo 255 → upscale
```
- El paso frágil es **el interior del cuello**: si no tienes la toma interior, el modelo lo alucina → revisa que la etiqueta/costura interna sea plausible.
- Para prendas con hueco (chaquetas abiertas) hace falta máscara de la zona "vacía" que mostraría fondo, no piel.
- **Dos tomas ideales**: prenda en maniquí (exterior) + foto del cuello por dentro → composición real del interior, no alucinada. La IA solo borra el soporte y une.
- Multi-ángulo: repite el pipeline por vista (frente, espalda, 3/4) reusando la misma máscara base de prenda cuando la pose lo permite.

## Material vs técnica de toma
| Material | Riesgo | Mitigación |
|---|---|---|
| Algodón mate | aplana, se ve "cartón" | luz suave + microcontraste en upscale |
| Satén/cuero | highlight quemado o muerto | fuente direccional definida, preserva specular real |
| Punto/tejido | textura se pierde al recortar | matting alta-res + no sobre-suavizar |
| Herrajes metálicos | reflejo plano | gradiente que reflejar, no clipping a 255 |

## Specular control (el oficio que la IA no improvisa)
- **Tela mate** (algodón): luz suave envolvente; el relight no debe inventar brillos duros.
- **Satén/seda/cuero**: highlights **direccionales largos** venden el material; relight con fuente clara definida. IC-Light afina dirección/dureza → ver [[193-product-photography-pipeline]].
- **Metal/herrajes/cremalleras**: necesitan algo que reflejar (gradiente, flag) o se ven muertos; specular **quemado** (clipping a 255) arruina la lectura de forma.
- **Vidrio/acrílico** (frascos, packaging): bright-field (objeto oscuro/fondo claro) o dark-field (objeto claro/fondo oscuro) para definir silueta con bordes.
- Regla de oro: **preserva los highlights reales como capa**; el relight que los aplana produce el "look plástico".

## Gotchas
1. **Blanco no-255** — el killer #1 de rechazos Amazon; fuerza y verifica RGB(255,255,255).
2. **Borde sucio/halo** — matting flojo deja franja gris en fondo blanco; BiRefMet alta-res + refine de borde.
3. **Interior alucinado** — cuello/etiqueta inventados sin toma interior; valida o dispara la interior real.
4. **Specular quemado** — highlights a 255 borran la forma; controla exposición del relight.
5. **Forma distorsionada** — la IA "infla" la prenda; bloquea con la silueta del cutout real.
6. **<85% del cuadro** — recorta/encuadra para cumplir cobertura mínima.

Cruza con [[193-product-photography-pipeline]].

**Fuentes:** sellerlabs.com/blog/amazon-product-image-requirements-2026 · listing-forge.com/blog/amazon-main-image-requirements · photta.app/resources/ghost-mannequin-photography · wearview.co/blog/best-ai-ghost-mannequin-tools · github.com/ZhengPeng7/BiRefNet
