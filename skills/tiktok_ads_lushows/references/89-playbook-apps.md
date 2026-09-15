# 89 — Playbook apps

Lee este módulo cuando promociones una app móvil: quieres instalaciones, usuarios activos, o eventos dentro de la app (compras, suscripciones, registros). Aquí va la verdad que pocos dicen: **TikTok es el canal #1 para apps virales hoy**. Las apps que explotan en 2026 lo hacen por TikTok — orgánico y pagado. Si tu negocio es una app, este es probablemente tu canal principal, no uno secundario. Pero apps tiene su propia mecánica de medición (SKAN, eventos in-app) que debes entender o pagas a ciegas.

## Por qué apps y TikTok encajan (y la estructura)

La audiencia de TikTok ES la audiencia de apps móviles: jóvenes, en el celular, descubriendo cosas nuevas. Y el formato vertical de TikTok lleva directo a la tienda de apps sin fricción. Por eso una app con buen creativo puede escalar rapidísimo. TikTok tiene un objetivo dedicado: **App Promotion** (instalaciones y eventos in-app). Estructura:

| Capa | Cuántas | Qué define |
|---|---|---|
| Campaign | 1 | **App Install** o **App Events** (optimiza a evento in-app, ver abajo) |
| Ad group | 1 broad | Público amplio; OS (iOS/Android van separados por medición) |
| Ad | 10–20 | UGC + demo de la app, muchos hooks (ver abajo) |

Decisión clave: ¿optimizas a **instalación** o a **evento in-app**? Instalar es barato pero engaña — mucha gente instala y nunca usa. Si tu app tiene suficientes datos, optimiza al **evento que importa** (registro completo, primera compra, suscripción), no a la instalación. TikTok aprende a traer usuarios que de verdad usan, no que solo descargan. Empieza optimizando a instalación si no tienes datos, y migra a evento in-app cuando juntes señal (ver 13, 14).

**iOS y Android van en ad groups separados** por la medición (ver SKAN abajo). No los mezcles.

## Medición de apps: SKAN, MMP y eventos in-app

Esta es la parte técnica que hace única a la pauta de apps — explicada simple. En apps no mides como en web; mides con tres piezas:

- **MMP (*Mobile Measurement Partner*)** — una herramienta tercera (AppsFlyer, Adjust, Singular) que atribuye qué instalación vino de qué ad. **Es obligatoria** para pautar apps en serio; sin MMP pautas a ciegas. Conéctala a TikTok.
- **SKAN (*SKAdNetwork*)** — el sistema de Apple que mide instalaciones de iOS **respetando la privacidad** (sin rastrear al usuario individual). Por SKAN, la medición en iOS es **agregada y con retraso** (no ves cada instalación al instante, ves datos en ventanas). Debes configurar tu **esquema de conversión** (qué eventos cuentan y cómo se codifican) — esto se hace en el MMP. Android no tiene esta restricción, por eso van separados.
- **Eventos in-app** — los momentos que importan dentro de la app (registro, nivel completado, compra, suscripción). Se los pasas a TikTok vía el MMP para optimizar a ellos.

Sin este setup, los números de tu pauta de apps son humo, sobre todo en iOS. La parte técnica de integración (SDK, MMP, esquema SKAN) la puede apoyar `engineer_visualopen_lushows` en su bloque de producto.

| Métrica | Qué significa | Trampa |
|---|---|---|
| CPI | Costo por instalación | Barato engaña: instala ≠ usa |
| **CPA evento in-app** | Costo por registro/compra real | La que importa |
| **Retención D1/D7** | ¿Vuelven al día 1 y 7? | Define si el usuario vale |
| **ROAS in-app** | Ingreso de compras/suscripción | El número final |

## El creativo: hooks y Smart+ App

Apps queman creativo aún más rápido que e-commerce porque el público es enorme y rota veloz. La estrategia es **volumen de creativos diferenciados por hook** (ver 37, 39):

- **Demo de la app** — la pantalla en uso, el "así funciona", el momento satisfactorio dentro de la app. Screen recording nativo.
- **UGC / "esta app me cambió X"** — persona real mostrando cómo la usa y qué resuelve (ver 32).
- **Problema→solución** — "¿cansado de X? esta app...". El dolor que la app resuelve.
- **Trend / formato nativo** — meter la app dentro de un trend o reto de TikTok (ver 36).
- **Muchos hooks sobre la misma demo** — la app es la misma, pero el primer segundo cambia para cada perfil. Aquí el banco de hooks rinde muchísimo (ver 37, 49).

**Smart+ App** (ver 12, 90) es la automatización de TikTok para apps: junta puja, público y entrega, y deja que el creativo y el evento manden. Para apps, Smart+ suele rendir bien una vez tienes señal de eventos in-app y un buen flujo de creativos. Empieza manual para juntar datos, migra a Smart+ App para escalar. La **viabilidad** (¿el LTV del usuario justifica el CPA?) → `economist_lushows`. La **landing/web de la app** (si aplica) → `desingweb-lushows`.

## Errores comunes — blacklist

- **Pautar apps sin MMP.** Sin AppsFlyer/Adjust/Singular pautas a ciegas; no sabes qué ad trae usuarios buenos.
- **Optimizar a instalación para siempre.** Instala ≠ usa; migra a evento in-app cuando tengas señal (ver 14).
- **No configurar el esquema SKAN.** En iOS la medición queda rota y optimizas sobre datos falsos.
- **Mezclar iOS y Android en un ad group.** Tienen medición distinta; van separados.
- **Pocos creativos.** Apps queman creativo rapidísimo por el público enorme; necesitas volumen y muchos hooks (ver 39, 37).
- **Mirar CPI y no retención/ROAS in-app.** Un CPI barato con retención D7 nula es plata quemada.
- **Saltar a Smart+ App sin señal de eventos.** Automatiza sobre ruido; primero junta datos in-app (ver 12).
