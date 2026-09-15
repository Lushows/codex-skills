# 196 · QR-art y códigos creativos con ControlNet (escaneable + bonito)

> Un QR que es también una imagen de marca (paisaje, logo, producto) y **sigue escaneando**. El truco es ControlNet
> usando el QR como guía estructural: el modelo estiliza todo menos los módulos que el lector necesita. Es un balance fino entre **arte** y **escaneabilidad**.

## Cómo funciona
ControlNet "controla" la composición de Stable Diffusion con una imagen-guía. Le pasas el **QR real** como condición → el modelo pinta una escena cuya luz/sombra/textura **coincide con el patrón** de módulos del QR. El código queda camuflado dentro del arte pero su estructura sobrevive.
- Modelo de referencia: **QR Code Monster v2** (ControlNet para SD 1.5), entrenado justo para esto.
- También sirve QR como **tile/brightness** ControlNet; Monster es el más fiable para que escanee.

## Parámetros que deciden escaneo vs creatividad
| Parámetro | Valor típico | Efecto |
|---|---|---|
| **Control weight** | ~**1.5-1.7** | más alto = escanea más, menos creativo |
| **Start step** | ~0.2 | deja que el arte nazca antes de imponer el QR |
| **End step** | ~0.8 | el QR se refuerza al final → módulos nítidos |
| **Control mode** | **balanced** | siempre |

Regla central: **cuanta más fuerza y más pasos** con el QR activo → más escaneable y menos arte. Buscas el punto justo iterando weight 1.3→1.8.

## Reglas de escaneabilidad (física del QR)
- Hasta **~30%** del código puede "dañarse" por el estilizado y aún escanear (ECC del QR). No abuses.
- **Contraste** entre módulos oscuros y claros = lo más crítico; si el arte funde claro/oscuro en una zona, muere ahí.
- Respeta los **3 finder patterns** (cuadros de esquina) y el **quiet zone** (margen): si el arte los traga, ningún lector lo encuentra.
- Genera el QR base con **alto nivel de corrección de error (ECC = H)** → tolera más estilizado.
- Prefiere **URLs cortas** (acortador): menos módulos = más espacio para el arte y más robustez.

## Pipeline
```
URL corta → QR con ECC=H → ControlNet (QR Code Monster) + prompt de marca → genera N → TEST de escaneo automático → filtra
```
- **Gate de escaneo OBLIGATORIO**: pasa cada salida por un decodificador (zxing/pyzbar) en pipeline; descarta las que no leen. Lo bonito que no escanea es basura.
- Itera weight/steps si la tasa de escaneo es baja; baja un poco el arte antes de subir mucho el weight.

## Casos de marca
- **Producto en el QR**: paisaje/escena del producto (frasco, prenda) integrando el patrón → ad/empaque con QR oculto.
- **Logo-friendly**: deja zonas planas para incrustar el logo real como overlay (no lo generes — ver [[195-text-typography-in-image]]).
- Imprime y **prueba en físico**: el escaneo en pantalla ≠ en papel (tinta, reflejo, tamaño). Valida a tamaño final.

## Sirviendo QR-art en producción
- QR Code Monster es **SD 1.5** → ligero (<8GB), barato de servir; no necesitas GPU grande. Carga el ControlNet warm.
- Pipeline como **job batch**: genera 8-16 variantes por URL, decodifica todas, devuelve solo las que escanean ordenadas por "menos QR visible" (más arte) entre las válidas.
- **Tasa de éxito** típica: con weight ~1.5 y ECC=H, ~40-70% de salidas escanean → por eso batcheas y filtras, no generas de a una.
- Cachea el QR base por URL; solo varía prompt/seed.

## Gotchas
1. **No escanea** — weight muy bajo o contraste fundido; sube weight/end-step o ECC=H.
2. **Feo y rígido** — weight muy alto; baja a ~1.4 y mueve start-step a 0.2.
3. **Finder patterns comidos** — el arte tapó las esquinas; protégelas o sube su contraste localmente.
4. **Quiet zone invadida** — sin margen no hay lectura; reserva el borde.
5. **Solo testeaste en una app** — distintos lectores varían; prueba varios + físico impreso.
6. **URL larga** — demasiados módulos, frágil; acorta la URL.

Cruza con [[139-controlnet-ipadapter-serving-consistencia]].

**Fuentes:** civitai.com/models/111006/qr-code-monster · qrcodekit.com/news/stable-diffusion-qr-codes · nextdiffusion.ai/tutorials/mastering-stunning-qr-codes-with-stable-diffusion-qrcode-monster · qrdiffusion.com/blog/controlnet-models-for-qr-codes · antfu.me/posts/ai-qrcode-101
