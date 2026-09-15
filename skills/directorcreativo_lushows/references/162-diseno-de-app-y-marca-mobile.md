# 162 — Diseño de app y marca en mobile

El móvil es el entorno más íntimo y más exigente para una marca: la app vive en la pantalla de inicio del usuario, junto a Instagram y WhatsApp, y se usa con el pulgar, a veces de pie en el bus. Aquí la marca debe ser **reconocible en 24×24px** (el ícono) y al mismo tiempo **no estorbar** dentro de la interfaz. El error típico es tratar la app como un cartel: llenar todo de logo y color. La marca móvil bien hecha es como una buena anfitriona: se nota su mano en cada detalle sin gritar.

Términos en simple:
- **Ícono de app**: la imagen cuadrada que aparece en la pantalla de inicio. Es el "logo" más pequeño y más visto de la marca.
- **Splash screen**: la pantalla brevísima al abrir la app, mientras carga.
- **Onboarding**: las primeras pantallas que enseñan al usuario qué hace la app.
- **Safe area**: la zona segura de pantalla, evitando el notch y los bordes redondeados.

## El ícono de app: el logo más difícil

No es tu logo metido en un cuadrado. Es un **diseño propio para tamaño mínimo** (ver 26 simplicidad y memorabilidad).

| Regla | Por qué |
|---|---|
| Un solo concepto / símbolo, no el logo completo con texto | A 48px el texto es ilegible |
| Sin bordes, sombras ni "burbujas" propias | iOS/Android ya aplican su máscara y esquinas |
| Alto contraste con cualquier fondo (claro y oscuro) | Pantallas de inicio varían |
| Centro de masa equilibrado | Se ve torcido si no |
| Probarlo a 24, 48 y 120px | Si no se lee a 24, no sirve |

Tamaños fuente recomendados: **1024×1024px** master (App Store), el sistema genera el resto. Usa el isotipo o un fragmento icónico del logo (ver 20 anatomía del logo).

## Splash screen

- Mínima: logo centrado sobre el color de marca, o fondo neutro con el isotipo.
- **Corta**: no es una pantalla de bienvenida con texto; es un puente de < 1–2s.
- Debe encadenar visualmente con la primera pantalla real (mismo fondo evita "salto").
- Evita animaciones largas de logo aquí: aburren al 3.er uso (ver 143).

## Onboarding: marca + utilidad

3–4 pantallas máximo. Cada una: una idea, un beneficio, una imagen. No expliques features técnicas; muestra el valor.

| Pantalla | Contenido | Tono |
|---|---|---|
| 1 | La promesa principal | Cálido, claro (ver 161) |
| 2 | El beneficio diferencial | Concreto |
| 3 | Permiso o acción inicial | Honesto sobre por qué |

Permite **saltar** el onboarding. La voz aquí define la primera impresión de personalidad (ver 14).

## Marca dentro de la UI sin estorbar

La regla de oro: **la marca está en el sistema, no en cada esquina.**

- El **color de acento** de marca se reserva para acciones (botón principal, links), no para pintar todo.
- El **logo** vive en pocos lugares (header de inicio, perfil, splash), no en cada pantalla.
- La **personalidad** se siente en la tipografía, el espaciado, el movimiento (ver 140) y el microcopy (ver 161), no en estampar el logotipo.
- Los **componentes nativos** (iOS Human Interface, Android Material) se respetan en patrón; la marca los viste, no los reinventa de forma que confundan.

## Ergonomía del pulgar (lo que cambia vs. web)

- Zona alcanzable con el pulgar: tercio inferior de la pantalla → CTAs y navegación abajo.
- **Targets táctiles**: mínimo 44×44px (iOS) / 48×48dp (Android).
- Texto legible: cuerpo ≥ 16px; evita gris claro sobre blanco.
- Respeta la **safe area** (notch arriba, barra de gestos abajo).
- Diseña para pulgar con una mano y para uso a la luz del sol (contraste, ver 35).

## Coherencia con el resto de la marca

La app debe sentirse hermana del sitio (ver 160) y del feed (ver 165): mismo color de acento, misma familia tipográfica, mismo tono. Un usuario que pasó del Instagram a la app no debe sentir que cambió de empresa.

## Errores frecuentes

- Meter el logo completo (con texto) en el ícono → ilegible.
- Ícono con sombras/bordes propios que pelean con la máscara del sistema.
- Pintar toda la UI del color de marca → cansa y entierra las acciones.
- Onboarding de 7 pantallas sin opción de saltar.
- Ignorar la safe area → botones tapados por el notch.
- Reinventar patrones nativos de forma que el usuario no entienda.

## Mini-checklist

- [ ] Ícono legible a 24px, un solo concepto, sin bordes propios
- [ ] Splash corta que encadena con la primera pantalla
- [ ] Onboarding ≤ 4 pantallas, salteable, centrado en beneficio
- [ ] Color de marca reservado para acciones, no para todo
- [ ] Targets táctiles ≥ 44px, CTAs alcanzables con el pulgar
- [ ] Se siente la misma marca que el sitio y el feed

## Nota técnica

Para construir la UI de la app con calidad, apóyate en **ui-ux-pro-max** (patrones y sistemas de UI) y en **desingweb-lushows** si es web-app. Aquí defines la dirección de marca móvil.

**Siguiente paso**: si la marca vende, su mayor reto digital es el comercio — diseñar e-commerce que transmita marca Y convierta (ver 163 ecommerce, marca que vende).
