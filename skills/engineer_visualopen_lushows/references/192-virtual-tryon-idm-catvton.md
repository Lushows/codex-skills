# 192 · Virtual try-on: vestir un modelo con una prenda (IDM-VTON / CatVTON / Leffa)

> VTON = poner una prenda real sobre una persona real, preservando rostro/pose del modelo
> y textura/logo/forma de la prenda. El 80% de la calidad vive en el **preproceso** (máscara + DensePose), no en el modelo.

## Las tres entradas obligatorias
1. **Imagen de la persona** (modelo o cliente).
2. **Imagen de la prenda** (flat-lay o packshot frontal limpio).
3. **Agnostic + máscara**: se borra la región de ropa actual de la persona → "person-agnostic". La **máscara binaria** marca dónde inyectar la prenda nueva. La calidad del borde de esa máscara decide el resultado.
   Más una **DensePose** (mapa UV del cuerpo) que da pose/volumen para que la prenda se deforme (warp) sobre el torso real.

## Cómo nace la máscara (el paso que la gente arruina)
- **Parsing humano** (SCHP / ATR / LIP) segmenta cuerpo en clases (torso, brazos, pelo…). De ahí sale el agnostic.
- **DensePose** (detectron2) da correspondencia UV → la prenda se mapea a la geometría del cuerpo, no se pega plana.
- Para prendas/formas arbitrarias: **Grounded-SAM** (texto→máscara) genera la máscara sin depender del parser fijo. Indispensable si quieres vestir accesorios o prendas raras.
- Regla: máscara **un pelo más grande** que la prenda objetivo; si es chica, queda ropa vieja asomando; si es enorme, alucina cuello/manos.

## Los modelos (2026)
| Modelo | Arquitectura | VRAM | Fuerte en | Débil en |
|---|---|---|---|---|
| **CatVTON** (ICLR'25) | UNet único, **concat** persona+prenda; 899M tot / 49M entrenables | **<8GB** a 1024×768 (~35s) | barato, rápido, corre en consumer GPU | detalle fino vs parallel-UNet |
| **IDM-VTON** (ECCV'24) | **parallel UNet** (GarmentNet) + IP-Adapter para semántica de prenda | ~16-24GB | preserva textura/logo/estampado, robusto a pose | pesado, lento, más setup |
| **Leffa** | flow-field en atención (regulariza warp) | media | **menos artefactos**, mejor FID | ecosistema más nuevo |

**Calidad medida (DressCode FID, menor=mejor):** Leffa **2.06** < CatVTON **3.99** < IDM-VTON **6.82**. CatVTON casi siempre **empata o gana** a IDM-VTON pese a ser 1/10 del tamaño → arranca por CatVTON, sube a Leffa si ves artefactos de warp.

## Recomendación de stack
- **E-commerce de volumen / presupuesto**: CatVTON. Cabe en una L4/A10, batch grande, costo mínimo.
- **Detalle crítico (logo, estampado, encaje)**: IDM-VTON o Leffa; Leffa si los bordes/manga distorsionan.
- Sirve los preprocesadores (SCHP+DensePose+SAM) como nodos **warm** aparte: cargarlos por job mata el throughput.

## VRAM y disco (sizing serverless)
- **CatVTON**: cabe en <8GB → L4/A10 sobran; ideal para escalar a 0 con cold-start corto.
- **IDM-VTON**: SDXL base + GarmentNet + IP-Adapter → presupuesta **16-24GB** (A10/A100). Pesa más en disco; si lo sirves serverless, cachea pesos en network volume (ver [[113-network-volume-modelos-grandes]]).
- **Preprocesadores** (detectron2/DensePose, SCHP, SAM) suman ~varios GB de modelos: hornéalos en la imagen o en volumen, no los bajes por job.
- DensePose con detectron2 es frágil de instalar (ABI CUDA/torch): fija versiones y prueba en local antes de subir.

## Gotchas
1. **Máscara mala → todo mal.** El 90% de los fallos (ropa vieja visible, dedos fundidos) son de la máscara, no del modelo.
2. **Manos y cuello**: zona de colisión persona/prenda; mantén manos FUERA de la máscara o se derriten. Inpaint local después si hace falta.
3. **Identidad del modelo**: rostro/pelo deben quedar intactos → no los incluyas en la región editable. Para fijar identidad cruza con [[173-pulid-instantid-identity]].
4. **Logo/estampado alucinado**: IP-Adapter capta semántica pero inventa detalle; valida texto del estampado char-por-char.
5. **Pose extrema**: DensePose falla en escorzos fuertes → la prenda se tuerce. Filtra poses o usa Leffa.
6. **Resolución de prenda**: sube prenda ≥1024 nítida; si entra borrosa, sale borrosa.

## Dos modos de negocio
| Modo | Entrada persona | Caso |
|---|---|---|
| **Catálogo** (1 modelo × N prendas) | modelos fijos de marca | poblar tienda: cachea parsing+densepose del modelo, itera prendas |
| **"Pruébatelo"** (N clientes × 1 prenda) | foto del cliente final | demo/conversión: preproceso por usuario, prioriza velocidad (CatVTON) |

El catálogo amortiza el preproceso (se calcula una vez por modelo). El "pruébatelo" lo paga por cada cliente → modelo ligero y máscara robusta mandan.

## Pista de producción
Pipeline determinista: `parsing → agnostic → densepose → (CatVTON/IDM) → inpaint manos → upscale`. Cachea parsing+densepose por persona (no cambian entre prendas) → multiplicas catálogo (1 modelo × N prendas) gratis. Para consistencia de pose/escena entre tomas, ControlNet/IP-Adapter: ver [[139-controlnet-ipadapter-serving-consistencia]].

Cruza con [[173-pulid-instantid-identity]] y [[139-controlnet-ipadapter-serving-consistencia]].

**Fuentes:** github.com/yisol/IDM-VTON · github.com/Zheng-Chong/CatVTON · arxiv.org/pdf/2412.08486 (Leffa) · digitalocean.com/community/tutorials/grounded-segment-anything-idm-vton · fashn.ai/blog/comparing-the-top-4-open-source-virtual-try-on-viton-models
