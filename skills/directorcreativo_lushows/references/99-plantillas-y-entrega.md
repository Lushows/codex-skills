# 99 — Plantillas y entrega (HTML → PDF)

El entregable final no es un montón de archivos sueltos: es un **artefacto presentable** que el dueño puede abrir, leer y mostrar con orgullo. Lushows PREFIERE PDFs listos generados directo, no archivos MD/HTML para procesar. Este módulo enseña a generar un BRANDBOARD / MANUAL / ARTE DE ETIQUETA en HTML bien diseñado y convertirlo a PDF con chrome headless.

## La preferencia del usuario (regla firme)
Cuando algo es presentable (brandboard, manual de marca, arte de etiqueta, deck), **NO entregues HTML o MD esperando que él los procese.** Genera el HTML bien diseñado y conviértelo TÚ a PDF con chrome headless. Entrega el PDF final.

## Por qué HTML→PDF (y no InDesign)
- Claude puede *escribir* HTML/CSS directamente y controlarlo al 100%.
- Chrome headless lo convierte a PDF de alta calidad con un comando.
- No requiere software de diseño abierto ni licencias.
- Reutilizable: una plantilla, infinitas marcas cambiando variables.

## El patrón de conversión (comando reutilizable)

**Windows (la ruta típica de Chrome en el sistema de Lushows):**
```
& "C:\Program Files\Google\Chrome\Application\chrome.exe" --headless --disable-gpu --print-to-pdf="C:\ruta\brandboard.pdf" --no-pdf-header-footer "file:///C:/ruta/brandboard.html"
```

Notas clave:
- `--print-to-pdf="..."` define el archivo de salida.
- `--no-pdf-header-footer` quita los encabezados/fechas que Chrome mete por defecto (importante para que se vea limpio).
- La URL de entrada va como `file:///` con barras normales `/`.
- Si `chrome.exe` no está en esa ruta, buscar también en `C:\Program Files (x86)\...` o usar `msedge.exe` (Edge usa el mismo motor y acepta los mismos flags).
- El tamaño de página se controla desde el CSS con `@page` (ver plantilla).

## CSS imprescindible para PDF
En el `<style>` define el tamaño y márgenes de página, y respeta los colores de fondo:
```css
@page { size: A4; margin: 0; }
* { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
```
Sin `print-color-adjust: exact`, Chrome borra los fondos de color al imprimir. Es el error #1.

## Mini-plantilla de BRANDBOARD reutilizable
Cambia solo las variables (`--marca-*`), los textos y la paleta. Una página A4 limpia con logo, paleta con HEX, tipografías y un ejemplo de aplicación.

```html
<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<style>
  @page { size: A4; margin: 0; }
  * { margin:0; padding:0; box-sizing:border-box;
      -webkit-print-color-adjust:exact; print-color-adjust:exact; }
  :root{
    --tinta:#1A2E22;      /* color de texto principal */
    --acento:#2E7D5B;     /* color de marca */
    --suave:#F4F1EA;      /* fondo claro */
  }
  body{ font-family:'Georgia',serif; color:var(--tinta);
        width:210mm; height:297mm; padding:18mm; background:#fff; }
  .header{ border-bottom:2px solid var(--acento); padding-bottom:10mm; margin-bottom:10mm; }
  .marca{ font-size:34pt; font-weight:700; letter-spacing:1px; color:var(--acento); }
  .tagline{ font-size:11pt; color:var(--tinta); opacity:.7; margin-top:3mm; }
  h2{ font-size:10pt; letter-spacing:3px; text-transform:uppercase;
      color:var(--acento); margin-bottom:5mm; }
  .bloque{ margin-bottom:12mm; }
  /* Logo: si hay archivo, va <img>; si no, marca tipográfica */
  .logo-box{ height:45mm; background:var(--suave); border-radius:4px;
             display:flex; align-items:center; justify-content:center; }
  .logo-box .marca{ font-size:28pt; }
  /* Paleta */
  .paleta{ display:flex; gap:6mm; }
  .swatch{ flex:1; text-align:center; }
  .swatch .chip{ height:30mm; border-radius:4px; margin-bottom:3mm; border:1px solid #0001; }
  .swatch .hex{ font-family:monospace; font-size:9pt; }
  .swatch .nombre{ font-size:8pt; opacity:.6; }
  /* Tipografías */
  .tipo-ej{ font-size:24pt; margin-bottom:2mm; }
  .tipo-meta{ font-size:9pt; opacity:.6; letter-spacing:1px; }
  /* Aplicación */
  .aplicacion{ background:var(--acento); color:#fff; padding:12mm;
               border-radius:6px; display:flex; align-items:center; justify-content:center;
               font-size:20pt; letter-spacing:2px; }
</style>
</head>
<body>
  <div class="header">
    <div class="marca">BIO-SETA</div>
    <div class="tagline">Hongos funcionales · Bienestar de la naturaleza</div>
  </div>

  <div class="bloque">
    <h2>Logo</h2>
    <div class="logo-box">
      <!-- <img src="file:///C:/ruta/logo.svg" style="max-height:35mm"> -->
      <div class="marca">BIO-SETA</div>
    </div>
  </div>

  <div class="bloque">
    <h2>Paleta de color</h2>
    <div class="paleta">
      <div class="swatch"><div class="chip" style="background:#2E7D5B"></div>
        <div class="hex">#2E7D5B</div><div class="nombre">Verde seta</div></div>
      <div class="swatch"><div class="chip" style="background:#1A2E22"></div>
        <div class="hex">#1A2E22</div><div class="nombre">Bosque</div></div>
      <div class="swatch"><div class="chip" style="background:#F4F1EA"></div>
        <div class="hex">#F4F1EA</div><div class="nombre">Crema</div></div>
      <div class="swatch"><div class="chip" style="background:#C98A3B"></div>
        <div class="hex">#C98A3B</div><div class="nombre">Tierra</div></div>
    </div>
  </div>

  <div class="bloque">
    <h2>Tipografía</h2>
    <div class="tipo-ej" style="font-weight:700">Aa Bb Cc — Títulos</div>
    <div class="tipo-meta">SERIF DISPLAY · TÍTULOS Y MARCA</div>
    <div class="tipo-ej" style="font-family:Arial,sans-serif;font-size:14pt;margin-top:5mm">
      Aa Bb Cc — Texto de lectura cómodo y claro.</div>
    <div class="tipo-meta">SANS-SERIF · CUERPO DE TEXTO</div>
  </div>

  <div class="bloque">
    <h2>Aplicación</h2>
    <div class="aplicacion">BIO-SETA</div>
  </div>
</body>
</html>
```

## Cómo adaptarla a cada entregable
- **Brandboard (1 página):** esta plantilla, tal cual. Resumen visual de la marca.
- **Manual de marca (multipágina):** repite secciones, una por "página" usando un contenedor con `height:297mm` y `page-break-after:always;` entre ellas. Agrega: usos correctos/incorrectos del logo, área de protección, tono de voz, ejemplos.
- **Arte de etiqueta:** cambia `@page { size: ... }` al tamaño real de la etiqueta, diseña dentro, y para imprenta exporta recordando CMYK/sangrado (ver 92 — para arte final de imprenta, el PDF de Chrome sirve para *presentar*, pero el archivo de producción debe prepararse con specs de imprenta).

## Flujo completo de entrega
```
1. Diseñar el HTML con la plantilla (cambiar variables, textos, paleta)
2. Guardar como brandboard.html
3. Convertir con chrome headless --print-to-pdf
4. Verificar el PDF (colores, saltos de página, nada cortado)
5. Entregar el PDF a Lushows  ← el artefacto final presentable
6. (Aparte) entregar el kit de archivos del logo (ver 93)
```

## Verificación antes de entregar el PDF
- [ ] ¿Los fondos de color salieron? (si no → falta `print-color-adjust:exact`)
- [ ] ¿El contenido no se corta entre páginas?
- [ ] ¿Sin encabezado/fecha de Chrome? (usar `--no-pdf-header-footer`)
- [ ] ¿Los HEX y datos son los correctos? (pasar por QA de 98)
- [ ] ¿El PDF se ve presentable, listo para mostrar a un cliente?

## La carpeta de entrega final ordenada
```
ENTREGA-BIO-SETA/
├── BIO-SETA-brandboard.pdf      ← artefacto principal (presentable)
├── BIO-SETA-manual.pdf          ← manual completo (si aplica)
├── logo/                        ← kit de archivos (ver 93)
│   ├── editable/ vector/ png/ jpg/
└── etiquetas/
    └── etiqueta-melena.pdf
```

## Mini-checklist de entrega
- [ ] ¿Generé un PDF presentable, NO entregué HTML/MD suelto?
- [ ] ¿Usé `--print-to-pdf` + `--no-pdf-header-footer`?
- [ ] ¿El CSS tiene `@page` y `print-color-adjust:exact`?
- [ ] ¿Verifiqué el PDF (colores, saltos, datos)?
- [ ] ¿Incluí el kit de archivos del logo por separado (93)?
- [ ] ¿La carpeta de entrega está ordenada?
- [ ] ¿Pasó el QA visual de 98?

**Siguiente paso:** este PDF es también material de portafolio — documenta el proyecto como caso de estudio (95). Cierra el círculo: concepto (01) → diseño → QA (98) → entrega presentable (este módulo).
