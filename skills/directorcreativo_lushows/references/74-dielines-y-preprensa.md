# 74 — Dielines y preprensa

Aquí es donde mueren los diseños bonitos: el arte se ve perfecto en pantalla y sale mal de imprenta porque faltó sangrado, el color cambió o el texto quedó cortado. Preprensa es preparar el arte para que la máquina lo reproduzca exacto. Domina esto y nunca tirarás dinero en una tirada arruinada.

## Dieline / troquel — la base de todo
> **Dieline (troquel):** el plano técnico que indica dónde se **corta** la imprenta, dónde se **pliega**, dónde va el **pegado** y dónde está el área segura. Es el "molde" del empaque desplegado.

- Líneas típicas, cada una en un color/capa distinta:
  - **Corte** (línea sólida) — por donde se troquela el contorno.
  - **Plegado / hendido** (línea punteada) — por donde dobla la cartulina.
  - **Pegado / cola** (zona sombreada) — solapas que se adhieren.
  - **No imprimir** — pestañas internas.
- El dieline lo provee el **proveedor de empaque** según el envase real. **Pídelo SIEMPRE antes de diseñar.** Diseñar primero y "ajustar después" = desastre.
- El arte se monta **sobre** el dieline, en su propia capa. El dieline NO se imprime: va marcado para que la troqueladora lo lea o se elimina al exportar.

## Sangrado (bleed) — el error más común
> **Sangrado:** extender el arte **más allá** de la línea de corte, normalmente **3 mm** por lado, para que al cortar no aparezcan franjas blancas si la máquina se desvía un pelo.

- Estándar: **3 mm** de sangrado (algunas imprentas piden 5 mm en empaque grande).
- Todo fondo o gráfico que llega al borde debe extenderse hasta el sangrado.
- No dejes elementos importantes en la zona de sangrado: se cortarán.

## Márgenes de seguridad (safe area)
> **Margen de seguridad:** zona interna donde DEBE quedar todo el texto e info crítica, lejos del corte (típico **3 mm hacia adentro** de la línea de corte).

- Texto legal, logo, código de barras, lote → dentro del área segura.
- En cajas, aléjate además de los **pliegues**: un texto sobre un doblez queda partido o ilegible.

## Marcas de corte y registro
- **Marcas de corte (crop marks):** indican a la imprenta dónde recortar el pliego.
- **Marcas de registro:** crucecitas que alinean las distintas planchas de color; si no coinciden, las imágenes salen "movidas/desenfocadas" (mal registro).
- En un PDF de empaque profesional normalmente se incluyen marcas de corte + sangrado; el dieline en capa aparte.

## Color: CMYK, Pantone y por qué tu rojo cambia
> **CMYK:** sistema de 4 tintas de impresión (Cian, Magenta, Amarillo, Negro). Tu pantalla usa **RGB** (luz), que tiene más colores. Por eso un verde neón vibrante en pantalla sale apagado impreso.

- **Diseña y entrega en CMYK** para impresión offset/digital estándar.
- Convierte de RGB a CMYK **tú** y revisa: no dejes que la imprenta lo haga "a ciegas".
- **Pantone (tinta plana):** color sólido pre-mezclado, idéntico en cada tirada. Úsalo cuando el color de marca debe ser EXACTO siempre (el verde de BIO-SETA, el rojo Coca-Cola). Cuesta más pero garantiza consistencia.
- **Negro de texto:** usa negro puro (K=100), NO un negro "rico" (CMYK mezclado) en texto pequeño, o saldrá borroso por mal registro.
- **Negro de fondos grandes:** sí usa negro rico (ej. C40 M30 Y30 K100) para que no se vea grisáceo.
- Pide siempre una **prueba de color física** (proof) antes de la tirada grande si el color es crítico.

## Resolución e imágenes
- **300 dpi** a tamaño real para fotos e ilustraciones rasterizadas. Menos = pixelado.
- **Vectores** (logo, tipografía) son resolución infinita: úsalos siempre que puedas para nitidez perfecta.
- **Tipografías:** convierte el texto a **curvas/contornos (outlines)** antes de enviar, o incrusta (embed) las fuentes, para que la imprenta no sustituya por otra.
- Tamaño mínimo de tipo: respeta el legible legal (a menudo ~1–1.5 mm de altura de x); en negativo (texto blanco sobre fondo) usa cuerpos un poco mayores.

## Tinta blanca, barnices y capas técnicas
En sustratos transparentes o metalizados, el blanco no existe "solo": se imprime como tinta.
- **Capa de blanco (white ink):** va debajo del arte en material transparente/metalizado para que los colores sean opacos.
- **Barniz/laminado o acabados especiales** (foil, UV selectivo, relieve) se entregan en **capas separadas** marcadas como spot, no como color visible (ver 76).
- Marca esas capas claramente y nómbralas ("WHITE", "UV_SPOT", "FOIL").

## Cómo entregar el arte listo (lista del empacador)
- [ ] Formato **PDF/X** (o el que pida la imprenta) de alta calidad
- [ ] Tamaño real 1:1, no escalado
- [ ] **Sangrado 3 mm** en todos los lados con fondo extendido
- [ ] Info crítica dentro del **margen de seguridad**
- [ ] **Dieline en capa aparte**, sin imprimir
- [ ] Color en **CMYK** (+ Pantones definidos si aplica)
- [ ] Imágenes a **300 dpi**, tamaño real
- [ ] Tipografías **en curvas** o incrustadas
- [ ] Capas técnicas (blanco, foil, UV) **separadas y nombradas**
- [ ] Negro de texto = K100; negro de fondo = negro rico
- [ ] Marcas de corte y registro incluidas

## Antes de la tirada grande
1. Pide un **proof físico** (impresión de prueba) o un **dummy** (maqueta del empaque armado).
2. Revísalo bajo luz neutra: color, legibilidad del lote, posición del código de barras.
3. **Escanea el código de barras** del proof para confirmar que lee.
4. Aprueba por escrito. Recién entonces, tira los miles.

> Regla de oro: la imprenta reproduce lo que le mandas, no lo que querías. El 90% de los desastres son archivos mal preparados, no fallas de máquina.

**Siguiente paso:** aplica las reglas específicas de tu categoría (alimentos, suplementos, cosmética) en 75.
