# 71 — Mobile con React Native / Expo

En 2026 **Expo es la forma recomendada** de construir React Native (lo dice el equipo RN oficial). Workflow gestionado con CNG (Continuous Native Generation: el dir nativo se regenera desde config).

## Versiones (2026)
Expo **SDK 54** trae RN **0.81** + React 19.1, Reanimated v4, Android API 36 / iOS 26. **New Architecture habilitada
por default desde SDK 53.** **SDK 54 es la última donde se puede DESACTIVAR; SDK 55+ corre solo en New Architecture.**

## New Architecture (Fabric / TurboModules / JSI)
- **JSI** — reemplaza el "bridge" async por llamadas síncronas directas JS↔C++.
- **Fabric** — nuevo renderer, layout concurrente, mejor con React 19.
- **TurboModules** — módulos nativos lazy, tipados con Codegen.

## EAS (Expo Application Services)
- **EAS Build** — compila iOS/Android en la nube (sin Mac para iOS). `eas build --profile production --platform all`.
- **EAS Submit** — sube a App/Play Store.
- **EAS Update** — **OTA: despachas cambios de JS/assets SIN revisión de tienda** (`eas update --branch production`). **NO puedes cambiar código nativo por OTA** (requiere build nuevo).

## Routing — expo-router (recomendado)
File-based sobre react-navigation. `app/(tabs)/index.tsx`, `app/perfil/[id].tsx` (dinámica), `app/_layout.tsx`. Deep linking + type-safe routes automáticos. react-navigation directo solo para control muy custom.

## Módulos nativos / push
**Config plugins** modifican la config nativa en `prebuild` sin "eject"; si una lib no tiene plugin, usa un
**development build** (`expo-dev-client`). **Push (`expo-notifications`):** Android = **FCM HTTP v1** (la legacy fue
deprecada — sube el JSON de service account de Firebase a EAS); iOS = **APNs** vía EAS. Flujo: permiso → Expo Push Token → backend lo envía al Expo Push Service.
```ts
import * as Notifications from 'expo-notifications';
const { status } = await Notifications.requestPermissionsAsync();
const token = (await Notifications.getExpoPushTokenAsync()).data;     // POST al backend
```

## Storage / performance
- **MMKV** (v4, Nitro Module, ~30× más rápido que AsyncStorage, síncrono vía JSI, cifrado) — reemplazo directo de AsyncStorage.
- **SQLite** (`expo-sqlite`) relacional · **WatermelonDB** ORM reactivo para apps con muchos datos y sync.
- **Hermes** (motor JS default, arranque rápido) · **FlashList v2** (`@shopify/flash-list`, reescrita para New Arch, sin `estimatedItemSize`) reemplaza `FlatList` en listas largas.
- **RN vs nativo vs PWA:** RN/Expo para multiplataforma con UI rica (~90% código compartido); nativo cuando exprimes hardware (AR, juegos, audio low-latency); PWA cuando alcanza con web (pero iOS limita push/PWA, sin App Store).

## Gotchas
1. EAS Update **no** despacha cambios nativos (nueva lib con código nativo = build nuevo).
2. Push Android falla si no subes el service account JSON de FCM v1 — la legacy ya no existe.
3. Expo Go no carga módulos nativos custom; necesitas development build.
4. SDK 55+ no permite desactivar New Architecture; valida que tus libs la soporten antes de actualizar.
5. Edge-to-edge obligatorio en Android (RN 0.81/SDK 54): maneja safe areas o la UI se mete bajo barras del sistema.
6. AsyncStorage es lento/async; migra a MMKV temprano o tendrás cuellos en arranque.

**Fuentes:** expo.dev/changelog/sdk-54 · docs.expo.dev/guides/new-architecture · docs.expo.dev/push-notifications.
