# 87 — Brand assets y design tokens

El mejor manual del mundo no sirve si el cliente no encuentra el archivo del logo. Los brand assets son todos los archivos de la marca (logos, fuentes, paletas, plantillas, fotos) organizados y nombrados para que cualquiera los use sin preguntarte. Los design tokens son el siguiente nivel: los valores reutilizables (color, tipo, espacio) definidos una vez y usados en todas partes.

## El problema invisible
Entregas una marca espectacular y a los dos meses el cliente te escribe: "¿me pasas el logo otra vez?", "¿cuál era el verde?". Eso es fallo de entrega, no de diseño. Un kit bien armado es servicio profesional; un ZIP caótico es trabajo a medias.

## Estructura de carpetas (estándar)
Una estructura que cualquiera entiende:

```
MARCA_Brand_Kit/
├── 00_LEEME.pdf              ← cómo usar esta carpeta (1 página)
├── 01_Logo/
│   ├── Principal/            (SVG, PNG, PDF, AI)
│   ├── Secundario/
│   ├── Isotipo/
│   ├── Monocromo/
│   └── Negativo_fondo_oscuro/
├── 02_Color/
│   └── paleta.pdf            (HEX, RGB, CMYK, Pantone)
├── 03_Tipografia/
│   ├── Fuentes/              (archivos + licencia)
│   └── jerarquia.pdf
├── 04_Plantillas/
│   ├── Papeleria/            (tarjeta, membrete, factura)
│   ├── Social/               (Canva o editables)
│   └── Presentacion/
├── 05_Imagen/                (estilo fotográfico, ejemplos)
├── 06_Manual/                (brand guidelines PDF)
└── 07_Motion/                (intro/outro, Lottie)
```

## Naming de archivos (la regla de oro)
Nombres consistentes, sin tildes ni espacios, con orden lógico:

```
marca_logo_principal_color_RGB.png
marca_logo_principal_negativo_RGB.png
marca_isotipo_monocromo.svg
marca_logo_principal_CMYK.pdf
```

Patrón: `marca_pieza_variante_modo-color.formato`. Sin "logo_FINAL_FINAL_v3_usar-este.png". Si tú no lo entiendes en 6 meses, el cliente menos.

## Qué formato para qué
| Formato | Para qué | Nota |
|---|---|---|
| SVG | Web, escalado infinito | Vectorial, peso mínimo |
| AI / EPS | Imprenta, proveedores | Editable vectorial original |
| PDF | Manual, impresión, compartir | Universal |
| PNG | Digital con transparencia | Da varios tamaños |
| JPG | Fotos | No para logos (sin transparencia) |

Regla: **siempre entrega el vectorial** (SVG/AI). El PNG es derivado; el vectorial es la fuente de verdad.

## Design tokens: el nivel pro
Un design token es un valor de diseño con nombre, definido una vez. En vez de "el verde es #1B5E20" repetido en 30 lugares, defines:

```
color-brand-primary   = #1B5E20
color-brand-accent    = #C5E1A5
color-text            = #1A1A1A
space-base            = 8px
radius-button         = 12px
font-heading          = "Familia", sans-serif
font-body             = "Familia", sans-serif
```

Ventaja: cambias el token en un lugar y se actualiza en web, app y plantillas. Es como tener variables en lugar de números mágicos. Lo usan **Material Design**, **Shopify Polaris**, **Adobe Spectrum**. Para web se implementan como variables CSS (`--color-brand-primary`) o JSON de tokens.

### Niveles de token (jerarquía)
1. **Globales / primitivos**: `green-700 = #1B5E20` (el color en bruto).
2. **Semánticos / alias**: `color-primary = green-700` (qué rol cumple).
3. **De componente**: `button-bg = color-primary` (dónde se usa).

Esto permite cambiar el verde primario sin tocar cada botón. Para una marca chica no necesitas los 3 niveles, pero entender la lógica evita el caos al escalar (ver 89 sobre design ops).

## Color: los 4 sistemas siempre juntos
Cada color de marca documentado en:
- **HEX** — web (`#1B5E20`)
- **RGB** — pantalla (`27, 94, 32`)
- **CMYK** — impresión (`75, 0, 100, 50` aprox)
- **Pantone** — tinta plana exacta (si hay presupuesto)

Sin esto, cada proveedor inventa su versión y la marca se desincroniza (ver 88).

## Fuentes y licencias (lo que se olvida y trae problemas)
- Incluye los archivos de fuente Y la licencia (¿permite uso comercial? ¿web? ¿incrustar?).
- Si la fuente es de pago/Adobe Fonts, documenta cómo obtenerla legalmente — no la pirateas en el kit.
- Define la fuente de respaldo (fallback) para web y correo donde la custom no carga.

## Para el cliente no técnico (Lushows)
- Carpeta en Google Drive / Dropbox compartida (no solo un ZIP que se pierde).
- `00_LEEME.pdf` de UNA página: "el logo está en 01, el verde es este, las plantillas en 04".
- Plantillas en Canva (editables) más que PSDs que no abre.
- La fuente de verdad debe ser localizable en 30 segundos.

## Errores comunes
- Solo PNG, sin vectorial.
- Nombres caóticos con "FINAL_v2".
- Color solo en HEX (falla en imprenta).
- Fuentes sin licencia.
- ZIP que se descarga una vez y se pierde.
- Sin instructivo de uso de la carpeta.

## Mini-checklist
- [ ] Estructura de carpetas numerada y clara
- [ ] Naming consistente (sin espacios/tildes/"FINAL")
- [ ] Vectorial (SVG/AI) además de PNG
- [ ] Color en HEX/RGB/CMYK (+Pantone)
- [ ] Fuentes con licencia + fallback documentado
- [ ] Tokens definidos (al menos color/tipo/espacio) si hay web/app
- [ ] 00_LEEME de 1 página
- [ ] Compartido en nube, no solo ZIP

**Siguiente paso**: con los assets ordenados, asegúrate de que la marca se vea igual en todos los puntos de contacto — auditoría de consistencia omnicanal (ver 88).
