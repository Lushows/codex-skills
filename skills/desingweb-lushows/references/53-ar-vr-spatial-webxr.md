# 53 — AR, VR, spatial computing & WebXR

La próxima plataforma (Vision Pro, Quest, WebXR) + el AR que **sí vende hoy** (AR try-on/commerce en el teléfono). **Léelo para experiencias inmersivas, AR de producto o cuando un cliente pregunte por "lo spatial".** Pareja de 08/38 (WebGL/3D). Verdad #1: **el headset NO es la plataforma de masas todavía, pero el AR en el teléfono SÍ vende.** No confundas las dos.

## 1. Panorama 2026 (hype vs realidad)

- **Apple Vision Pro 2** (chip M5, ~$2.499, feb-2026): más barato/rápido pero **experimental, no de masas** (~3.000 apps). Valor real: enterprise (arquitectura/médico), video inmersivo, pantalla-única gigante. Consumo masivo: aún no. `visionOS 26` empujó a colaboración + spatial scenes persistentes.
- **Meta Quest:** el headset más adoptado; **Quest 4 retrasado a ~2027** (rediseño por confort/peso). Gafas AR **Orion** también aplazadas (dev fines 2026, consumidor ~2027). **2026 = año tranquilo de hardware** (Samsung/Google Project Moohan/Android XR emergen).
- **El rol de la web:** **WebXR** ganó terreno (Safari visionOS 2+ soporta `immersive-vr` por defecto) PERO **el módulo AR de WebXR aún NO está en Safari/Vision Pro**. WebGPU es baseline (Three.js ya lo envía). **Conclusión de mercado: para el web designer en 2026, el dinero está en AR-on-phone (commerce), no en headsets.**

## 2. Principios de diseño spatial (visionOS HIG)

- **Windows / Volumes / Spaces:** *Windows* = planos 2D+ (apps tradicionales) · *Volumes* = contenedores 3D acotados (un objeto/modelo) · *Spaces* = Shared Space (apps coexisten) vs Full Space inmersivo (passthrough AR o VR total).
- **Zonas de confort:** *Manipulation Zone* (0-120cm, alcance de manos) · *Reading Zone* (120-700cm, ventanas). Contenido dentro del FOV, alineado a la cabeza (sin giros forzados).
- **Eyes + hands (gaze + pinch):** el **pinch es el nuevo click** (mira el target, junta dedos). Los elementos deben **brillar/crecer al recibir la mirada** (hover por gaze). Targets generosos y espaciados (el gaze es impreciso).
- **Estética glass/material:** translúcido, vibrancy, profundidad por sombras suaves; se mezcla con la luz real del passthrough. Sin fondos opacos pesados.
- **Spatial audio** (feedback direccional/presencia). **Passthrough/AR** preserva el espacio (menos mareo, más social) vs **inmersivo/VR** (exige más rigor de confort).

## 3. WebXR (la web inmersiva)

VR/AR en el navegador **sin instalar app** (WebXR Device API). Soporte 2026: Chrome/Edge/Firefox + Safari core; Quest Browser el caballo de batalla; Apple añadió `transient-pointer` para gaze-and-pinch.
**Stack (mayor→menor abstracción):** **A-Frame** (HTML declarativo, prototipar rápido) · **R3F + `@react-three/xr`** (la vía React, potente: hit testing, plane detection, anchors) · **Three.js** + WebXR (control total) · Babylon.js/PlayCanvas (engines pesados).
**Setup mínimo R3F:**
```jsx
import { Canvas } from '@react-three/fiber'; import { XR, createXRStore } from '@react-three/xr'
const store = createXRStore();
<>
  <button onClick={()=>store.enterAR()}>Entrar AR</button>
  <Canvas><XR store={store}>
    <mesh position={[0,1.5,-1]}><boxGeometry/><meshStandardMaterial color="orange"/></mesh>
    <ambientLight intensity={1}/>
  </XR></Canvas>
</>
```
**Cuándo WebXR vs native:** WebXR para alcance sin fricción de instalación (link/QR), iteración rápida, experiencias acotadas (visor inmersivo, tour, mini-juego). Native para máximo rendimiento/APIs del SO/distribución en store. **Limitación clave:** AR-WebXR flojo en Safari/Vision Pro → para AR de consumidor en iPhone NO uses WebXR puro (usa §4).

## 4. AR en la web (lo deployable HOY)

El AR que convierte en 2026 **no es WebXR** — es **`<model-viewer>`** apoyándose en los visores nativos del SO: **AR Quick Look (iOS/USDZ)** y **Scene Viewer (Android/GLB)**. Cero app, un QR/botón:
```html
<script type="module" src="https://ajax.googleapis.com/ajax/libs/model-viewer/4.0.0/model-viewer.min.js"></script>
<model-viewer src="silla.glb" ios-src="silla.usdz" ar ar-modes="webxr scene-viewer quick-look"
  ar-scale="fixed" ar-placement="floor" camera-controls poster="silla.jpg" alt="Silla en tu espacio">
  <button slot="ar-button">Verlo en tu espacio</button>
</model-viewer>
```
**Pipeline GLB/USDZ:** GLB cross-platform (Android/web) + USDZ (iOS nativo). Optimización (Apple): **<100k polígonos, texturas ≤2048², Draco/KTX2**. Requiere **HTTPS** + iframe `xr-spatial-tracking`.
**Try-on (cara/cuerpo/manos):** **8th Wall (Niantic) se apaga** (acceso hasta 28-feb-2026) → migra a **Banuba** (líder en glasses/jewelry/makeup/footwear, hand-tracking para anillos/relojes) o **Zappar**. Patrón **QR-to-AR** (QR en empaque/vitrina → AR markerless world tracking) = el flujo retail dominante.

## 5. 3D/immersive commerce — el ROI (qué presentas al cliente)

- **+94% conversión** promedio con 3D/AR vs sin (Shopify) · **−40% devoluciones** (alinea expectativa con realidad; Macy's muebles <2% devoluciones, +60% ticket) · Rebecca Minkoff +27% compra tras 3D, +65% tras AR · Web AR documentado **+112% conversión, 22× ROI**.
- **Dónde invertir (ROI claro):** muebles/decoración, footwear, gafas, joyería, relojes, cosmética. **Assets:** fotogrametría/3D-scan para catálogos grandes, modelado manual para hero products, siempre optimizar GLB. **Cuándo NO:** SKUs de bajo ticket/alta rotación (el coste del asset no se amortiza).

## 6. Spatial UX, accesibilidad & qué aprender hoy

**Confort (no negociable):** mareo (cybersickness) por movimiento de cámara no iniciado por el usuario → ofrece **teletransporte vs locomoción suave**, viñeta de confort, y **alternativa 2D** siempre. Texto en 3D fatiga → minimiza lectura larga en el espacio (texto en pantallas planas). Targets grandes para gaze; subtítulos no solo audio.
**Qué aprender HOY (orden):** (1) **`<model-viewer>` + pipeline GLB/USDZ + optimización** (ships y vende ya); (2) **Three.js/R3F** + WebGPU; (3) **`@react-three/xr`** cuando aparezca el caso; (4) principios visionOS (gaze+pinch, zonas de confort, glass) como vocabulario.
**Trayectoria:** corto plazo = **AR commerce en el teléfono, ahora** (el ganador); medio plazo = gafas AR ligeras (~2027+) hacia ambient/spatial computing. El headset de masas no llegó — no diseñes para él como si fuera mainstream.

## Spatial/AR anti-patterns — blacklist
VR para lo que debe ser 2D (menús/formularios/lectura larga → pantalla plana) · cámara/movimiento no iniciado por el usuario (mareo instantáneo) · ignorar zonas de confort (fuera del FOV, obliga a girar la cabeza) · **gimmick AR sin función** (si no reduce incertidumbre de compra "¿cabe?/¿me queda?", no va) · 3D pesado sin optimizar (>100k polys, 4K sin comprimir, sin Draco/KTX2) · targets diminutos para gaze+pinch · **WebXR-AR puro para iPhone masivo** (Safari no lo soporta bien → usa model-viewer + Quick Look) · texto largo flotando en el espacio · olvidar el fallback 2D y HTTPS · **asumir que "spatial = headset"** (el 95% del ROI 2026 vive en el teléfono).
