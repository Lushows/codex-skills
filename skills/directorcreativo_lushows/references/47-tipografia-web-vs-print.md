# 47 — Tipografía web vs. print

La misma fuente se comporta distinto en una pantalla que en papel. Una elección que brilla impresa puede verse rota en un celular. Este módulo te evita ese error y explica cómo viven las fuentes en la web.

## La diferencia fundamental
- **Print (papel)**: resolución altísima (300+ dpi), luz reflejada, posición fija. El papel aguanta detalles finos: serifas delgadas, alto contraste (Didot), tamaños pequeños. Lo que diseñas es lo que se imprime.
- **Web (pantalla)**: resolución variable, luz emitida (cansa más el ojo), tamaños y dispositivos infinitos, el render depende del navegador y del sistema. La pantalla CASTIGA los detalles finos: las serifas delgadas se rompen, el alto contraste parpadea.

## Qué fuentes funcionan mejor en pantalla
Reglas para texto en pantalla:
- **Altura-x alta** (la o, e, a se ven grandes) → más legible en chico.
- **Contraformas abiertas** (apertura amplia en c, e, s) → no se "tapan".
- **Contraste moderado o bajo** → no se rompe a tamaño pequeño.
- **Pensadas para pantalla**: **Inter, Source Sans, IBM Plex Sans, Public Sans, Söhne, Roboto, San Francisco, Segoe UI**. Para serif de pantalla: **Georgia, Newsreader, Tiempos Text, Source Serif**.

Evita en cuerpo de pantalla: didonas (Didot, Bodoni) y serifs de contraste muy alto a tamaños chicos — guárdalas para titulares grandes.

## Cómo llegan las fuentes a la web (4 formas)

### 1. Google Fonts (gratis, fácil)
Catálogo gratuito, se carga con un link/CSS. Cero costo, cero licencia que pagar. Calidad variable: hay joyas (Inter, Source Sans, Fraunces, Newsreader, IBM Plex, Space Grotesk) y mucho cliché (Montserrat, Poppins, Lato). Ventaja: rapidísimo de implementar.

### 2. Adobe Fonts (incluido en Creative Cloud)
Miles de fuentes de calidad activables por web. Si el cliente ya paga Adobe, es excelente. La licencia web está incluida mientras la suscripción esté activa (ojo: si se cancela, deja de servir).

### 3. Self-host (auto-hospedar) — recomendado para marca seria
Compras la licencia web a la fundidora, descargas los archivos (.woff2) y los sirves desde TU servidor con `@font-face` en CSS. Ventajas: control total, mejor rendimiento (sin pedir a terceros), privacidad. Es lo que hacen los estudios serios. Requiere la **licencia web** correcta (ver 49).

### 4. Fuentes de sistema (system stack)
No cargas nada: usas la fuente que ya tiene el dispositivo (San Francisco en Apple, Segoe en Windows, Roboto en Android). Máximo rendimiento, cero peso. Se ve nativo. Útil para apps y productos donde la velocidad manda más que el carácter de marca.

## Formato y rendimiento
- Usa **.woff2** (el formato web moderno, comprimido). Olvida .ttf/.eot para web.
- **Carga solo los pesos que usas** (cada peso pesa). 3 pesos, no 9.
- Define `font-display: swap` para que el texto se vea con la fuente de respaldo mientras carga la real (evita pantalla en blanco).
- Subconjunto (subsetting): incluye solo los caracteres latinos + acentos del español si no necesitas más; reduce el peso.

## Hinting y rendering (en simple)
- **Hinting**: instrucciones dentro de la fuente para que se vea nítida en tamaños pequeños alineándose a la grilla de píxeles. Las fuentes bien "hinteadas" (Inter, Source Sans, Georgia) se ven limpias en chico; otras se ven borrosas. Importa MUCHO en Windows y en pantallas de baja densidad.
- **Rendering**: cada sistema dibuja distinto. Una fuente puede verse perfecta en Mac (retina) y mediocre en un Windows viejo. Prueba siempre en ambos.

## px vs. rem (unidades web, en simple)
- **px** = píxeles fijos. 16px es 16px siempre.
- **rem** = relativo al tamaño base del navegador (por defecto 16px = 1rem). Si el usuario sube el tamaño base por accesibilidad, todo en rem escala con él; lo fijado en px no.
- **Recomendación**: define el cuerpo en **rem** (mejor accesibilidad) y bordes/detalles finos en px. Cuerpo cómodo en pantalla: **16–18px (1–1.125rem)**. Nunca menos de 14px en texto de lectura.

## Print: lo que cambia
- Trabaja en **CMYK** y a 300 dpi (no RGB ni 72 dpi de pantalla).
- Puedes usar fuentes más finas y de mayor contraste; el papel las soporta.
- El tamaño de cuerpo en print suele ser **9–11 pt** (el papel a 300 dpi rinde más que la pantalla).
- **Empaqueta o convierte a curvas** las fuentes antes de mandar a imprenta, y verifica la **licencia de impresión/desktop**.

## Checklist web
- [ ] ¿La fuente tiene altura-x alta y contraste moderado? (legible en chico)
- [ ] ¿La probé en Mac Y Windows, en celular Y desktop?
- [ ] ¿Uso .woff2 y solo los pesos necesarios?
- [ ] ¿Cuerpo a 16px+ y en rem?
- [ ] ¿Definí fallback en el `font-family`?
- [ ] ¿La licencia cubre web (o app)? (ver 49)

## Siguiente paso
Define la escala de tamaños y el interlineado correcto para lectura cómoda en cada medio (ver 48 sobre escalas y ritmo). Para elegir entre fuentes gratis de calidad o licenciadas, ver 49.
