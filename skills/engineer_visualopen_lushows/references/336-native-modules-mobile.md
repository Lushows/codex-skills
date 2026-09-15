# 336 · Native modules / Expo Modules API (puente JS↔nativo, cámara/audio, IA on-device)

> Cuando RN/JS no alcanza (cámara cruda, audio low-latency, CoreML), bajas a Swift/Kotlin con la Expo Modules API.
> Para apps de avatar/lip-sync esto es el corazón: captura, inferencia on-device y resultado de vuelta a JS sin saturar el thread.

## Expo Modules API vs TurboModules
- **Expo Modules API**: escribes Swift/Kotlin con `ModuleDefinition` declarativo, mínimo boilerplate, consistente entre plataformas. Rinde **comparable a TurboModules** y se **autolinkea**.
- **TurboModules (RN core)**: más bajo nivel, más Codegen/boilerplate. Úsalo si necesitas API RN pura sin dependencia de Expo.
- En 2026, dentro del ecosistema Expo, **Expo Modules API es el default**: menos código, mismo perfil de performance.

## Anatomía de un módulo
```swift
import ExpoModulesCore
public class AvatarModule: Module {
  public func definition() -> ModuleDefinition {
    Name("Avatar")
    Function("warmup") { /* cargar modelo en memoria */ }
    AsyncFunction("infer") { (uri: String) -> [String: Any] in
      // corre off-main-thread, devuelve a JS vía promesa
    }
    Events("onProgress")             // emite progreso a JS
    View(AvatarPreview.self) { /* vista nativa montable en RN */ }
  }
}
```
- **Function** (sync, cuidado: bloquea), **AsyncFunction** (promesa, para trabajo pesado), **Events** (push nativo→JS, ideal progreso de inferencia), **View** (componente nativo en el árbol RN).
- Tipos marshalled automáticamente (Records tipados). **Corre inferencia en cola de background**, nunca en main, o congelas la UI.

## El bridge: JSI bajo el capó
La New Arch usa **JSI** → las llamadas son síncronas JS↔C++ sin serializar JSON. Por eso un AsyncFunction puede
pasar buffers/objetos grandes sin el costo del viejo bridge. Para datos enormes (frames de video, tensores) pasa
**referencias/URIs**, no copies base64 a JS — devuelve un path de archivo y que JS lo lea con `expo-file-system`.

## Cámara / audio
- **Cámara**: `expo-camera` cubre foto/video/QR. Para frames crudos en tiempo real (feed a un modelo) necesitas módulo nativo (AVFoundation / CameraX) o **VisionCamera** + frame processors. Procesa el frame en nativo, emite solo el resultado a JS.
- **Audio low-latency**: `expo-audio` para play/record normal; para lip-sync/captura sincronizada baja a AVAudioEngine / Oboe (Android) en tu módulo. Declara permisos `NSMicrophoneUsageDescription` / `RECORD_AUDIO` o crashea (y Apple rebota — ver [[334-mobile-deploy-stores]]).

## IA on-device (lo nuestro)
- **iOS = CoreML/MLX**. Empaqueta el `.mlmodel`/`.mlpackage` como **resource del módulo** (config del module para que el build lo incluya). Hay precedentes: YOLOv8 (visión) y Stable Diffusion CoreML corriendo dentro de Expo/RN. Ver [[257-coreml-mlx-diffusion-on-device]].
- **Android = TFLite / NNAPI / ONNX Runtime Mobile**. Modelo en assets, delegado GPU/NNAPI para acelerar.
- **Patrón**: `warmup()` carga el modelo una vez (no por inferencia); `infer()` async devuelve resultado; `onProgress` para barras de progreso en generación. Cuantiza (int8) para caber en RAM móvil.
- **Cuándo on-device vs servidor**: on-device para latencia/privacidad/sin costo de GPU cloud; servidor (tu endpoint RunPod, [[261-browser-avatar-gen]]) cuando el modelo no cabe en el teléfono o quieres calidad full. Híbrido: preview on-device, render final en server.

## Distribución y flujo
- Módulo custom ⇒ **NO Expo Go**, sí **development build** (`expo-dev-client`). El módulo se autolinkea en `prebuild` (CNG).
- Puedes publicar el módulo como **package npm** reusable entre apps, o local en `modules/`.

## Gotchas
1. Inferencia en main thread = ANR/freeze; siempre cola de background.
2. base64 de imágenes/tensores entre nativo↔JS revienta memoria; pasa URIs.
3. Modelo cargado por cada llamada = lento; `warmup` una vez y mantén caliente.
4. Olvidar incluir el `.mlmodel` como resource → crash "model not found" solo en build de release.
5. Permisos cámara/micro sin descripción en Info.plist → rechazo de App Store.
6. `prebuild` regenera nativo: edita vía el módulo/config plugin, no a mano en `ios/`/`android/`.

**Fuentes:** docs.expo.dev/modules/overview · .../module-api · github expo-stable-diffusion (CoreML).

Cruza con [[257-coreml-mlx-diffusion-on-device]] y [[261-browser-avatar-gen]].
