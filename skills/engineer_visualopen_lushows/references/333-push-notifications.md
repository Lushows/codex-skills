# 333 · Push notifications (APNs / FCM v1 / Expo Push, permisos, deep-links, segmentación)

> El push en RN se rompe en dos puntos: credenciales de plataforma mal montadas y permisos pedidos en mal momento.
> Aquí el flujo completo de token → backend → entrega → tap → deep-link, con las trampas de 2026.

## Dos tipos de token — no los confundas
- **Expo Push Token** (`getExpoPushTokenAsync`) → lo envías al **Expo Push Service**, que reenvía a APNs/FCM por ti. Más simple, un solo endpoint.
- **Device Push Token** (`getDevicePushTokenAsync`) → token nativo crudo; lo usas si hablas **directo a FCM/APNs** desde tu backend (sin Expo en medio). El código cliente sigue siendo `expo-notifications`; cambia el server.

`expo-notifications` es **push-service agnóstico**: mismo cliente, eliges a quién mandas en el server.

## Credenciales de plataforma (donde más se cae)
- **Android = FCM HTTP v1**. La API legacy está **muerta**: sube el **JSON de service account** de Firebase a EAS (`eas credentials`). Sin esto, push Android falla silencioso.
- **iOS = APNs** vía EAS (push key `.p8` / APNs auth key). EAS la gestiona en build.
- El **Expo plugin** ya te deja listo para notifs con **imágenes y deep links** sin config extra.

## Flujo de registro (cliente)
```ts
import * as Notifications from 'expo-notifications';
const { status } = await Notifications.requestPermissionsAsync();
if (status !== 'granted') return;                       // respeta el "no"
const token = (await Notifications.getExpoPushTokenAsync({ projectId })).data;
await api.post('/devices', { token, platform: Platform.OS, userId });
```
- **Permiso = momento, no arranque**: pídelo tras un beneficio claro (ej. "te aviso cuando tu avatar esté listo"), no en el primer launch. Android 13+ exige permiso runtime `POST_NOTIFICATIONS`.
- **Token listener**: el push service puede **rotar** el token con la app viva → registra `addPushTokenListener` y re-sube el nuevo al backend, o pierdes entregas.

## Recepción, foreground y tap → deep-link
- **Handler** decide qué pasa en foreground (`setNotificationHandler` → mostrar banner/sonido o silenciar).
- **Listeners**: `addNotificationReceivedListener` (llegó) vs `addNotificationResponseReceivedListener` (el usuario **tocó**).
- **Deep-link al tap**: mete la ruta en `data` del push (`data: { url: '/avatar/abc' }`) y en el response listener navega con expo-router (`router.push(data.url)`). Cubre el caso **app cerrada**: lee `getLastNotificationResponseAsync()` al montar, o el tap en cold-start se pierde.

## Background tasks y entrega garantizada
- iOS no garantiza despertar la app por push; para sync confiable combina silent push con `expo-background-task` (BGTaskScheduler) — el SO decide cuándo correrlo, no tú.
- Si la entrega DEBE ocurrir (recordatorio crítico), usa **notificación local programada** (`scheduleNotificationAsync`) en el device como respaldo del push remoto; no dependas solo del server.
- **Priority**: FCM `high` y APNs `priority: 10` para alertas visibles inmediatas; `normal`/`5` para data que puede esperar (mejor batería, menos throttle).

## Segmentación / envío (server)
- Manda en **lotes** al Expo Push API (≤100 por request) y **lee los receipts** (`/getReceipts`) — ahí salen errores reales: `DeviceNotRegistered` (borra el token), `MessageRateExceeded` (backoff).
- **Canales Android** (`setNotificationChannelAsync`): obligatorios para sonido/prioridad/importancia por categoría (transaccional vs marketing).
- **Segmenta en tu backend** (no en el cliente): asocia token ↔ userId ↔ tags (idioma, plan, último uso) y resuelve audiencias al enviar. Útil para campañas tipo las de [[AGENTE GASTROWHATS]] pero en app nativa.
- **Silent push** (content-available iOS / data-only FCM) para refrescar datos en background; iOS lo throttlea agresivo, no lo uses como entrega garantizada.

## Gotchas
1. Sin service account JSON de FCM v1 → Android no entrega y no avisa.
2. Permiso pedido al arranque = denegación masiva; iOS solo deja pedir **una vez** "bonito" antes de mandar a Ajustes.
3. Tap en cold-start ignorado si no lees `getLastNotificationResponseAsync`.
4. Token rotado sin listener = entregas perdidas para ese device.
5. Expo Go tiene push limitado/sandbox; valida en **development/production build** real.
6. No mandes datos sensibles en el `body` (aparece en lockscreen) — manda un id y resuelve dentro de la app.

**Fuentes:** docs.expo.dev/push-notifications/push-notifications-setup · .../sending-notifications-custom · sdk/notifications.

Cruza con [[332-react-native-expo-a-fondo]] y [[334-mobile-deploy-stores]].
