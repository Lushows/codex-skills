# 294 — Informe técnico y PDF (cómo entregar el trabajo para que lo lea quien decide)

El trabajo químico solo vale lo que vale su entregable. Un análisis brillante contado en un chat se pierde;
el mismo análisis en un PDF de 6 páginas con estructura, tabla de resultados y firma es lo que abre una
puerta con un cliente B2B, con un inversionista, con un profesor o con el INVIMA. Este módulo define **la
estructura del informe técnico** y el **patrón técnico del ecosistema Lushows** para generar el PDF: HTML +
CSS, impreso con Chrome en modo headless. Nada de convertidores intermedios, nada de Word.

Términos: **informe técnico (technical report)** = documento que responde una pregunta con método, datos y
conclusión trazable. **resumen ejecutivo (executive summary)** = la conclusión en 5–10 líneas, arriba, para
quien no va a leer el resto. **headless** = ejecutar el navegador sin interfaz gráfica, desde la consola.
**@page** = regla CSS que controla tamaño y márgenes de la página impresa.

## Estructura del informe técnico (10 secciones)

```
PORTADA
  Título específico (no "Informe de análisis": "Determinación de β-glucano en extracto de reishi,
  lote LT-2608"), cliente, autor y su rol, fecha, código y versión del documento.

1. RESUMEN EJECUTIVO (media página, se escribe al final)
   Qué se preguntó · qué se hizo · el número clave con unidad y base · la decisión recomendada.
   Si alguien solo lee esto, tiene que poder decidir.

2. OBJETIVO Y ALCANCE
   La pregunta exacta y la decisión que depende de ella. Qué queda FUERA del alcance (importante).

3. MATERIAL Y MUESTRA
   Identificación completa: material, lote, fecha de fabricación, proveedor, cantidad, condiciones de
   almacenamiento, fecha y forma de muestreo, cadena de custodia (109).

4. MÉTODO
   Técnica, referencia normativa o del kit, equipo, patrón de referencia y su trazabilidad, preparación
   de muestra, curva de calibración, LOD/LOQ, controles de calidad de la corrida. Si el método es propio,
   estado de validación (75).

5. RESULTADOS
   Tabla con: parámetro | resultado | unidad | base | LOQ | incertidumbre expandida | criterio |
   conforme/no conforme. Cromatogramas o espectros como figuras numeradas. NADA de interpretación aquí.

6. CÁLCULOS
   Fórmulas explícitas y un ejemplo numérico completo. Se declara que se ejecutaron y verificaron
   (Matematicas_lushows / lab-tools). Cifras significativas coherentes (05).

7. DISCUSIÓN
   Qué significa el número, contra qué se compara, qué lo explica, qué NO se puede concluir.
   Nivel de evidencia marcado en toda afirmación de efecto (12).

8. CONCLUSIÓN Y RECOMENDACIÓN
   Frases numeradas, accionables: "1. El lote cumple. 2. Se recomienda liberar. 3. Repetir metales en
   el próximo lote por cambio de origen."

9. LIMITACIONES
   Lo que este informe no prueba. Es la sección que da credibilidad, no la que la quita.

10. ANEXOS
   COA originales, datos crudos, cadena de custodia, certificados de acreditación, bibliografía.

FIRMA
   Nombre, rol, fecha. Si hay conflicto de interés (el informe lo paga el fabricante), se declara.
```

Reglas de escritura: unidades en todas las cifras · base declarada · cero adjetivos comerciales · cada
afirmación de efecto con su nivel de evidencia · las cifras ilustrativas marcadas **(ILUSTRATIVO)**.

## El patrón de PDF del ecosistema: HTML → Chrome headless

Se escribe el informe en HTML con CSS de impresión y se imprime con Chrome. Es reproducible, versionable
en git y no depende de ninguna licencia.

```bash
# Windows (PowerShell) — patrón del ecosistema Lushows
& "C:\Program Files\Google\Chrome\Application\chrome.exe" `
  --headless --disable-gpu `
  --print-to-pdf="C:\ruta\informe-LT-2608.pdf" `
  --print-to-pdf-no-header `
  --no-pdf-header-footer `
  "file:///C:/ruta/informe.html"

# Linux / macOS
google-chrome --headless --disable-gpu \
  --print-to-pdf=/ruta/informe-LT-2608.pdf \
  --no-pdf-header-footer \
  file:///ruta/informe.html
```

Notas prácticas que ahorran una tarde:

- La ruta del HTML va como **URL `file:///`** con barras normales, incluso en Windows.
- Imágenes y logos: rutas relativas al HTML, o incrustadas como `data:` URI para que el PDF sea autónomo.
- Los saltos de página se controlan **en el CSS**, no moviendo texto.
- Si el PDF sale en blanco, casi siempre es que el HTML carga contenido por JavaScript: usa
  `--virtual-time-budget=5000` o genera el HTML ya renderizado.
- Verifica el PDF **abriéndolo**: número de páginas, que no se corten tablas, que las figuras se vean.

## Plantilla CSS mínima para que se vea profesional

```html
<style>
  @page { size: A4; margin: 20mm 18mm 18mm 18mm; }
  body { font: 10.5pt/1.5 "Georgia", serif; color: #1a1a1a; }
  h1 { font-size: 20pt; border-bottom: 2px solid #1a1a1a; padding-bottom: 6px; }
  h2 { font-size: 13pt; margin-top: 18pt; page-break-after: avoid; }
  table { width: 100%; border-collapse: collapse; font-size: 9.5pt; margin: 10pt 0; }
  th { background: #f0f0f0; text-align: left; }
  th, td { border: 1px solid #999; padding: 5px 7px; }
  tr, img, figure { page-break-inside: avoid; }
  .portada { page-break-after: always; text-align: center; padding-top: 60mm; }
  .meta { font-size: 9pt; color: #555; }
  .nota { border-left: 3px solid #999; padding-left: 10px; font-size: 9.5pt; }
  figcaption { font-size: 9pt; color: #555; }
  footer { position: fixed; bottom: 0; font-size: 8pt; color: #777; }
</style>
```

`page-break-inside: avoid` en `tr` es el detalle que separa un PDF profesional de uno con tablas partidas a
la mitad. Para el diseño visual más elaborado (portada, tipografía de marca), rutea a
`directorcreativo_lushows`; para informes que además son páginas web, a `desingweb-lushows`.

## Los cuatro entregables típicos de este oficio

| Entregable | Extensión | Quién lo lee | Lo que no puede faltar |
|---|---|---|---|
| Informe de análisis de un lote | 3–6 páginas | Calidad, dirección | Método, lote, LOQ, conformidad |
| Dictamen sobre un COA de proveedor | 2–4 páginas | Compras, dirección | Banderas rojas, recomendación de comprar o no (`111`) |
| Informe de desarrollo (extracción, formulación) | 10–25 páginas | Equipo técnico, socio inversionista | Diseño experimental, datos crudos, conclusión reproducible (`287`) |
| Expediente técnico | 90–150 páginas | INVIMA, cliente B2B | El índice completo de `286` |

## Ejemplo aplicado (BIO-SETA)

Informe "Determinación de β-glucano y α-glucano en extracto de *Ganoderma lucidum*, lote LT-2608".
Resumen ejecutivo **(ILUSTRATIVO)**: *"β-glucano 22,4 % p/p base seca y α-glucano 6,1 % p/p base seca por
método enzimático (Megazyme K-YBGL). El lote cumple la especificación (≥ 20 %). Se recomienda liberar. El
α-glucano bajo es consistente con material de cuerpo fructífero, no con micelio en grano."* Cuatro líneas
que contienen analito, valor, unidad, base, método, criterio, decisión y la interpretación clave. Todo lo
demás del informe existe para sostener esas cuatro líneas.

## Errores comunes

- **Enterrar la conclusión en la página 12.** Quien decide lee la primera media página.
- **Resultados sin base ni LOQ.** El informe hereda el defecto del COA (`110`).
- **Mezclar resultados con interpretación** en la misma sección: se pierde la trazabilidad del dato.
- **Sin sección de limitaciones.** Un informe que no admite límites parece publicidad.
- **PDF hecho de capturas de pantalla.** No se puede buscar, no se puede citar, no se puede auditar.
- **Sin versión ni fecha.** Dos versiones circulando y nadie sabe cuál manda.
- **No declarar el conflicto de interés** cuando el informe lo paga la parte interesada.

## Conexión con otros módulos

→ `286-expediente-tecnico-del-producto.md` — el entregable mayor que usa este mismo patrón.
→ `110-como-leer-un-coa.md` — la materia prima documental del informe.
→ `05-cifras-significativas-e-incertidumbre.md` — cómo se escriben los números en la tabla de resultados.
→ `76-incertidumbre-de-medida.md` — la columna que casi nadie incluye.
→ `295-checklist-de-calidad-quimica.md` — repásalo antes de firmar.
→ `298-plantillas-y-formatos.md` — los formatos que alimentan el informe.
