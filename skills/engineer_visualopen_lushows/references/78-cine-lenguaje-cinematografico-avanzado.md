# 78 — Cine y lenguaje cinematográfico avanzado

Un shot list dice *qué* filmas; el **lenguaje cinematográfico** dice *por qué la cámara está ahí*. Para guiar IA de
video (Runway/Kling/Veo/Higgsfield) y start-frames (FLUX/Nano Banana), encodea esta gramática en el prompt — el modelo solo respeta lo que nombras con vocabulario de oficio.

## Mise-en-scène
Todo lo que entra en cuadro: set, props, vestuario, blocking, profundidad (FG/MG/BG), paleta, textura. La composición
en capas (algo en primer término — *foreground dressing*) genera profundidad que la IA tiende a aplanar; pídela: `foreground bokeh foliage, subject in midground, deep background falloff`.

## Blocking, coverage, eje de acción
**Blocking** = coreografía de actor+cámara; el **moving master** (plano maestro que se reencuadra siguiendo el
movimiento, sin cortar) es el santo grial. **Coverage:** master + singles + inserts + OTS da opciones de montaje y
ritmo; el insert (manos, objeto) controla la atención — genera deliberadamente cada tamaño en planos separados.
**Línea de 180°:** el eje de acción mantiene la geografía (si A mira a la derecha y B a la izquierda, "se miran"); la IA NO respeta el eje entre clips → fíjalo nombrando direcciones de mirada y screen direction consistentes.

## Lenguaje de lentes (focal = psicología)
**18-24mm** (amplio, distorsión de proximidad) · **35mm** (testigo natural) · **50mm** (ojo humano) · **85mm**
(retrato, separación, intimidad) · **135mm** (compresión extrema, aplastado romántico). El tele acerca fondos; el
amplio los aleja. **Anamórfico vs esférico:** anamórfico = flares horizontales azules, bokeh ovalado, falloff de
bordes, 2.39:1 nativo — el look "cine". Cualidades fílmicas: fall-off, breathing (respiración de foco), flares.
Prompt: `shot on 85mm anamorphic, oval bokeh, horizontal flares, shallow falloff`.

## Aspect ratios
**2.39:1** (scope, épica/sci-fi) · **1.85:1** (estreno estándar, drama) · **1.66:1** (europeo) · **1.33/4:3** (revival intimista A24, o flashback) · **2.76:1** (Ultra Panavision, espectáculo). Elige por escala emocional.

## Iluminación de cine
Luz **motivada** (justificada por fuente diegética: ventana, lámpara). **Contrast ratio / key-to-fill:** 2:1 (suave,
comedia/comercial), 8:1+ (duro, noir/thriller). **Looks de género:** noir (cenital dura, sombras de persiana,
low-key) · 70s (cálido, flare, grano, Gordon Willis) · blockbuster teal-orange · A24 naturalism (luz disponible,
suave, desaturado) · music-video maximalism (saturado, practicals, neón).

## Cámara como narrador & referencias de DP
Altura (baja = poder; alta = vulnerabilidad). **Movimiento motivado vs inmotivado:** un push-in lento intensifica;
un movimiento sin motivo distrae — nombra el *por qué*. **DPs para anclar looks:** **Deakins** (limpio, motivado,
negative fill) · **Lubezki** (luz natural, planos secuencia, magic hour) · **Khondji** (texturizado, contrastado,
Se7en) · **Bradford Young** (subexpuesto, piel oscura rica). `lit like Deakins, motivated single source, deep shadows`.

## Gotchas
1. La IA promedia a "teal-orange genérico" — especifica paleta y ratio o tendrás el look AI por defecto.
2. No respeta la línea de 180° entre clips — fija dirección de mirada manualmente.
3. **Lente fantasma:** pides 85mm pero da gran angular — refuerza con `compressed background, shallow DOF`.
4. **Movimiento inmotivado:** los presets (crash zoom) son adictivos pero rompen el tono; con criterio.
5. **Iluminación plana:** pide negative fill / contrast ratio explícito o todo sale flat.
6. Aspect ratio inconsistente entre planos — define ratio y crop desde el start-frame.

**Fuentes:** runwayml.com/research (Gen-4 world consistency) · higgsfield.ai/create/motion-control · cinematography refs (Deakins/Lubezki/Khondji).
