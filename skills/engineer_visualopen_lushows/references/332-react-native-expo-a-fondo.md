# 332 · React Native / Expo a fondo (New Arch, EAS, navegación, performance)

> [[71-mobile-react-native-expo]] dio el panorama; esto baja al detalle que decide si tu app de avatares/IA va fluida o se traba.
> En 2026 Expo es el camino oficial de RN, y la New Architecture ya no es opcional río arriba.

## Versiones y la cuenta regresiva de la Legacy Arch
SDK 54 (sep-2025) = RN 0.81 + React 19.1; **es el ÚLTIMO con soporte de Legacy Architecture**. SDK 55 y 56
(betas ya públicas en 2026) corren **solo New Arch** — migra antes de subir o quedas atascado. ~83% de los
builds EAS de SDK 54 ya usan New Arch [no verificado al 100% el número exacto]. SDK 54 trae **RN precompilado
para iOS** (XCFrameworks): builds de iOS mucho más rápidos sin compilar RN desde fuente.

## New Architecture, en concreto qué cambia para ti
- **JSI**: llamadas síncronas JS↔C++ sin el bridge JSON async → módulos nativos sin serializar, base de MMKV/Reanimated v4/Nitro.
- **Fabric**: renderer con layout concurrente; encaja con React 19 (Suspense, transitions). Algunas libs viejas con `findNodeHandle` o medición imperativa rompen.
- **TurboModules + Codegen**: módulos nativos lazy y tipados desde TS. Si una lib no migró a TurboModule, en New Arch corre por capa de interop (más lenta) o no carga.

## EAS — el triángulo Build / Submit / Update
| Servicio | Qué hace | Clave |
|---|---|---|
| **EAS Build** | compila iOS/Android en la nube | sin Mac para iOS; perfiles en `eas.json` |
| **EAS Submit** | sube a App/Play Store | usa credenciales/ASC API key |
| **EAS Update** | OTA de JS+assets sin revisión | **NO cambia código nativo**; ata a `runtimeVersion` |

EAS Update en SDK 54 hace **diffing de bytecode Hermes**: parches binarios en vez de bundle completo → ~75%
menos de descarga. Ver [[334-mobile-deploy-stores]] para reglas de tienda sobre OTA.

## Navegación — expo-router
File-based sobre react-navigation. `app/(tabs)/index.tsx`, `app/avatar/[id].tsx` (dinámica), `app/_layout.tsx`
(Stack/Tabs). Rutas **type-safe** y deep linking automático (`typedRoutes`). react-navigation crudo solo para
gestos/transiciones muy custom. Layouts anidados = un `_layout` por carpeta; el root suele montar providers
(query client, auth, theme).

## Módulos nativos — los tres caminos
1. **Config plugin**: modifica config nativa en `prebuild` (CNG) sin "eject". Para libs sin plugin propio.
2. **Development build** (`expo-dev-client`): reemplaza Expo Go cuando hay módulos nativos custom — Expo Go NO los carga.
3. **Expo Modules API** (Swift/Kotlin con `ModuleDefinition`): tu propio puente. Ver [[336-native-modules-mobile]].

## Performance — palancas reales
- **Hermes** (motor default): arranque rápido, bytecode precompilado. No uses JSC salvo razón fuerte.
- **FlashList v2** (`@shopify/flash-list`, reescrita para New Arch, sin `estimatedItemSize`) sobre `FlatList` en listas largas/feeds.
- **Reanimated v4 + Gesture Handler**: animaciones en UI thread vía JSI; nunca animes layout pesado desde JS thread.
- **MMKV v4** (Nitro, síncrono, ~30× AsyncStorage) para estado caliente; ver storage en [[335-offline-sync-mobile]].
- **Imágenes**: `expo-image` (cache disco/memoria, `recyclingKey` en listas). Para avatares/video generado, no metas base64 gigantes en estado React.
- Perfila con **Hermes profiler** + Flipper/React DevTools; el cuello casi siempre es re-render o listas, no "JS lento".

## Gotchas que muerden
1. SDK 55+ sin opción de Legacy Arch: **valida que TODAS tus libs soporten New Arch antes de actualizar**.
2. Edge-to-edge **obligatorio** en Android (RN 0.81): maneja `SafeAreaView`/insets o la UI se mete bajo barras.
3. `prebuild` regenera `ios/`+`android/` desde config: si editaste nativo a mano sin plugin, lo pierdes.
4. EAS Update no despacha nativo — lib nueva con código nativo = build+submit nuevos.
5. iOS 26 "Liquid Glass": íconos/UI nuevos; revisa assets si apuntas a ese look.

**Fuentes:** expo.dev/changelog/sdk-54 · docs.expo.dev/guides/new-architecture · docs.expo.dev/router.

Cruza con [[71-mobile-react-native-expo]], [[333-push-notifications]] y [[336-native-modules-mobile]].
