# 110 — CapCut: panorama real, versiones, y dónde vive todo

CapCut es el editor de video de ByteDance (los mismos de TikTok). Es, con distancia, el editor más
usado del mundo para contenido de redes. Y para nosotros tiene una propiedad que ningún otro editor
popular tiene tan a la mano: **guarda el proyecto entero en un archivo de texto que se puede leer y
escribir desde afuera**.

Eso es lo que hace posible el puente que se explica en los módulos 111 a 119: una IA arma el montaje,
lo escribe en disco, y vos lo abrís en CapCut y lo ves ya cortado, con el texto puesto y la música
sincronizada. Ese es el negocio de este bloque.

Este módulo es el mapa: qué versiones hay, cuál sirve para el puente, qué te da el Pro, y dónde vive
exactamente cada cosa en tu computador.

---

## Las cuatro CapCut (no son la misma cosa)

| Versión | Dónde corre | ¿Sirve para el puente? |
|---|---|---|
| **Escritorio** (Windows / Mac) | App instalada | **Sí. Es la única que sirve.** |
| **Móvil** (iOS / Android) | Teléfono | No. Sin acceso al sistema de archivos. |
| **Web** (capcut.com) | Navegador | No. El proyecto vive en la nube de ByteDance. |
| **JianYing (剪映)** | China | Es la versión china. Ojo: **desde la v6 el proyecto va cifrado.** |

La diferencia importa mucho más de lo que parece. La app de escritorio guarda los proyectos como
carpetas en tu disco. La web y el móvil los guardan en servidores. **Si tu proyecto está en la nube,
no hay puente posible** — no hay archivo que tocar.

Y JianYing es la trampa silenciosa: es el mismo producto, el mismo código base, la misma estructura de
carpetas… pero desde la versión 6 el archivo de proyecto ya no es texto legible, sino un bloque
cifrado. Mucha documentación de internet mezcla las dos y te hace perder una tarde.

**Regla práctica: CapCut de escritorio, versión internacional. Punto.**

---

## Qué versión hay hoy y cómo verificar la tuya

En agosto de 2026, la referencia verificada en una máquina real (Windows) es **CapCut 8.3.0**, y en esa
versión el archivo de proyecto **no está cifrado**: es JSON plano y legible.

Pero esto no es una promesa. CapCut se actualiza solo y muy seguido. Antes de construir nada encima:

1. Abrí CapCut → menú de la cuenta → *Acerca de* → anotá el número de versión.
2. Andá a la carpeta de proyectos (ruta abajo), abrí `draft_content.json` con el Bloc de notas.
3. Si ves llaves, comillas y palabras como `"tracks"`, `"materials"` → **es texto plano, hay puente**.
4. Si ves caracteres raros, cuadritos o basura binaria → **está cifrado, no hay puente**. Pará ahí.

Ese chequeo de treinta segundos te ahorra un día entero. Hacelo **cada vez** que CapCut se actualice.

---

## Dónde vive todo

### Windows

```
%LOCALAPPDATA%\CapCut\User Data\Projects\com.lveditor.draft\<id-del-proyecto>\
```

Que expandido normalmente es:

```
C:\Users\<tu-usuario>\AppData\Local\CapCut\User Data\Projects\com.lveditor.draft\
```

Cada proyecto es **una carpeta** con un nombre feo tipo `2408041930123456`. Adentro está todo (ver
módulo 111).

Para llegar rápido: `Win + R` → pegá `%LOCALAPPDATA%\CapCut\User Data\Projects\com.lveditor.draft` →
Enter.

### Mac

```
~/Movies/CapCut/User Data/Projects/com.lveditor.draft/
```

Para llegar: Finder → *Ir* → *Ir a la carpeta…* → pegá `~/Movies/CapCut/User Data`.

**Ojo con Mac:** en versiones recientes el archivo principal del proyecto en Mac se llama
`draft_info.json`, no `draft_content.json`. Es el mismo tipo de contenido pero con otro nombre, y en
algunas versiones existen **los dos** y hay que mantenerlos sincronizados. Si trabajás en Mac,
verificá cuál de los dos abre CapCut realmente antes de escribir nada.

### Otras carpetas que vas a ver

| Carpeta | Qué guarda |
|---|---|
| `User Data\Projects\com.lveditor.draft\` | Tus proyectos. **Esta es la que importa.** |
| `User Data\Cache\` | Previsualizaciones, proxies, basura temporal. Se puede borrar. |
| `User Data\Config\` | Preferencias de la app. |
| `Videos\CapCut\` (Windows) | Donde exporta por defecto los MP4 terminados. |

La carpeta de caché crece muchísimo (decenas de gigas en un mes de uso intenso). Si el disco se te
está llenando, ese es el culpable, y borrarla es seguro con CapCut cerrado.

---

## Gratis vs. Pro: la verdad sin adorno

Los planes cambiaron en 2026. Lo verificado a la fecha:

| Plan | Dónde funciona | Precio aproximado |
|---|---|---|
| **Gratis** | Todas las plataformas | $0 |
| **Standard** | Solo app móvil | ~12 €/mes · ~110 €/año |
| **Pro** | Web + escritorio + móvil | ~24 €/mes · ~200 €/año |

En 2026 ByteDance reforzó el Pro sin subir el precio: los créditos de IA mensuales pasaron de 550 a
1.200 y el almacenamiento en nube de 100 GB a 1 TB.

### Lo que de verdad cambia con Pro

- **Sin marca de agua.** La gratuita marca la exportación con ciertas plantillas y efectos. Para
  contenido comercial esto es descalificador.
- **Créditos de IA.** Todo lo "mágico" (quitar fondo, separar voz, doblar, mejorar a 4K, largo→shorts)
  consume créditos. Sin Pro se acaban rápido.
- **Escalado a 4K.**
- **Biblioteca completa** de música, efectos y plantillas.

### Lo que NO cambia

- La estructura del archivo de proyecto es **idéntica** en gratis y en Pro. **El puente funciona
  igual con la versión gratuita.** No pagues Pro por esto.
- La calidad de exportación base (1080p H.264) es la misma.
- El motor de render es el mismo.

**Recomendación honesta:** si vas a publicar comercialmente y usás efectos de IA, Pro se paga solo.
Si solo querés el puente y hacés el trabajo pesado con ffmpeg (bloque 100-105), la gratuita alcanza.

---

## Por qué CapCut y no otro

Un editor sirve para el puente si cumple tres cosas: guarda el proyecto local, en formato legible, y
lo recarga cuando lo abrís.

| Editor | Proyecto local | Legible | Puente |
|---|---|---|---|
| **CapCut escritorio** | Sí | Sí (JSON plano, v8.x) | **Sí, hoy** |
| DaVinci Resolve | Sí, pero en base de datos | No directo | Vía OTIO/XML (módulo 117) |
| Premiere Pro | Sí (`.prproj`) | Comprimido (gzip XML) | Vía XML/EDL (módulo 117) |
| Final Cut Pro | Sí (bundle) | Parcial | Vía FCPXML |
| Kdenlive / Shotcut | Sí (`.kdenlive`, `.mlt`) | Sí, XML limpio | Sí, y es el más limpio |
| CapCut web / móvil | No | — | No |

CapCut gana por una razón sola y muy práctica: **es el editor que ya tiene abierto la persona que va a
revisar el corte.** El puente no sirve de nada si el humano no puede abrir lo que le entregaste.

Si tu revisor es un editor profesional con Premiere o Resolve, no forcés CapCut: andá directo al
módulo 117.

---

## Lo que CapCut hace bien y lo que no

**Bien:**
- Cortar rápido y ver el resultado al instante.
- Subtítulos automáticos decentes (mejores que la media en español latino).
- Texto animado y plantillas listas que se ven bien en redes.
- Exportación con presets correctos para TikTok/Reels/Shorts.
- Separación de voz y música que funciona sorprendentemente bien.

**Mal o nada:**
- Color serio. No hay scopes decentes ni gradación por nodos. Para eso, Resolve.
- Audio serio. No hay mezclador real ni ecualizador paramétrico por pista.
- Proyectos largos. Con más de ~20 minutos y muchas capas se pone lento y a veces se corrompe.
- Colaboración de verdad. La "nube" es para vos mismo entre dispositivos, no para un equipo.
- Trazabilidad. No hay historial de versiones utilizable.

**Traducción:** CapCut es una **sala de revisión y montaje rápido**, no una suite de posproducción.
Usalo para lo que es. El bloque de ffmpeg (100-105) hace mejor el trabajo pesado y repetible; CapCut
hace mejor el "mirá cómo quedó, ¿te gusta?".

---

## Las advertencias que sí hay que decir

**1. Es ByteDance.** CapCut ha estado en el centro de líos regulatorios y de privacidad en varios
países. Los términos de servicio te dan a ellos licencias amplias sobre el contenido que subís a su
nube. Para material de cliente sensible o bajo NDA, **trabajá con proyectos locales y no uses la
sincronización en nube ni las funciones de IA que suben el archivo a sus servidores**.

**2. El formato no es público.** No existe documentación oficial del `draft_content.json`. Todo lo que
sabemos viene de gente que lo abrió y lo estudió. ByteDance no debe nada y puede cambiarlo mañana.
Esto se trata en serio en el módulo 119.

**3. Se actualiza solo.** Podés despertarte con una versión nueva que rompa tu automatización. Si
dependés del puente para trabajo con fecha de entrega, desactivá la actualización automática y
mantené instalada una versión que sabés que funciona.

**4. Nada de subida automática.** Automatizar la publicación desde CapCut hacia TikTok viola los
términos. El puente termina en "el proyecto está listo para revisar", no en "ya se publicó".

---

## Herramientas de la comunidad (estado a agosto 2026)

No estás solo en esto. Hay dos proyectos serios, ambos no oficiales:

- **`pyJianYingDraft` / `pyCapCut`** (GuanYixuan) — librerías de Python para generar drafts. `pyCapCut`
  es la versión para CapCut internacional, instalable con `pip install pycapcut`. Genera drafts en
  cualquier sistema operativo; la exportación automatizada solo funciona en Windows (maneja la
  interfaz de CapCut por automatización de UI). **No soporta drafts cifrados.**
- **`capcut-cli`** (renezander030) — CLI en Node (`npm install -g capcut-cli`, Node ≥18). Lee y
  escribe el draft directamente: recortar, cambiar velocidad y volumen, poner texto, importar/exportar
  SRT, cortar largo a shorts, detectar escenas, y exportar a OpenTimelineIO para pasarle el corte a
  Resolve. Es consciente de las diferencias entre versiones y, en las nuevas, sincroniza todos los
  archivos de línea de tiempo que encuentra, no solo `draft_content.json`.

Ninguna es oficial. Ninguna tiene garantía. Ambas te ahorran semanas. Elegí una y **fijá la versión**
(no dejes que se actualice sola en medio de un proyecto).

---

## Cómo encaja esto con el resto de la skill

```
Bruto en la carpeta
      ↓
[10-18]  Ingesta, transcripción, selección de tomas  ← trabajo de análisis
      ↓
[100-105] ffmpeg: cortes, filtros, capas, audio      ← trabajo pesado y repetible
      ↓
[110-116] Puente CapCut: escribir el montaje         ← ESTE BLOQUE
      ↓
   El humano abre CapCut, mira, oye, decide
      ↓
[117-118] Si el revisor usa Premiere o Resolve       ← formatos de intercambio
```

El módulo **116** es el corazón conceptual de todo esto: por qué esta división del trabajo entre
máquina y humano es la correcta, y no un truco.

---

## Errores comunes

**Asumir que tu CapCut es como el del tutorial.** El 90% de las guías de internet están escritas sobre
JianYing (versión china) o sobre CapCut 5.x. Las rutas y las claves cambian. Verificá en TU máquina
antes de creerle a nadie, incluido este documento.

**Confundir CapCut con JianYing.** Se ven casi iguales. JianYing v6+ cifra el proyecto y ahí no hay
nada que hacer. Si el idioma de la interfaz es chino y el logo dice 剪映, es la otra.

**Intentar el puente con la versión web o móvil.** No hay archivos locales. No hay puente. Se pierde
tiempo buscando una carpeta que no existe.

**Pagar Pro creyendo que es necesario para automatizar.** No lo es. La estructura del proyecto es la
misma. Pagá Pro por la marca de agua y los créditos de IA, no por esto.

**Dejar la actualización automática activa en medio de un proyecto con fecha.** Una actualización
puede cambiar el formato y dejarte sin puente el día de la entrega.

**Buscar los proyectos en la carpeta de exportación.** `Videos\CapCut` tiene los MP4 terminados, no
los proyectos. Los proyectos están en `AppData\Local`, que además está oculta por defecto en Windows.

**Subir material de cliente confidencial a las funciones de IA en nube.** Eso sale del computador y
entra a servidores de ByteDance bajo sus términos. Para material bajo NDA, no.

**Borrar la carpeta `com.lveditor.draft` para "liberar espacio".** Ahí están todos tus proyectos. La
que se puede borrar es `Cache`.

---

## Checklist

- [ ] Confirmé que estoy en **CapCut de escritorio**, versión internacional (no JianYing, no web, no móvil)
- [ ] Anoté el número de versión exacto desde *Acerca de*
- [ ] Encontré la carpeta de proyectos y la tengo a mano (acceso directo o variable)
- [ ] Abrí un `draft_content.json` con el Bloc de notas y **confirmé que es texto legible**, no binario
- [ ] Si estoy en Mac, verifiqué si el archivo real es `draft_content.json` o `draft_info.json`
- [ ] Sé si el proyecto está local o sincronizado en la nube (si está en nube, no hay puente)
- [ ] Decidí gratis vs. Pro por razones reales (marca de agua, créditos IA), no por el puente
- [ ] Desactivé la actualización automática si hay una entrega con fecha de por medio
- [ ] Tengo claro que el material sensible no pasa por las funciones de IA en nube
- [ ] Sé que el revisor humano tiene CapCut instalado; si usa Premiere o Resolve, voy al módulo 117
- [ ] Hice una copia de seguridad de la carpeta de proyectos antes de tocar nada (módulo 119)
