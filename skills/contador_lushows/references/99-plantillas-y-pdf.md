# 99 — Plantillas y generación de PDF

Este es tu "kit de entrega final": cómo empaquetar el trabajo contable en documentos profesionales — estados financieros, informe mensual al dueño, certificados — y convertirlos en un **PDF limpio y presentable**. Regla de oro de entrega: **nunca entregues Markdown crudo ni un Excel desordenado a un dueño, un banco o la DIAN. Siempre PDF.** Un estado financiero bien presentado se ve como lo que es: un documento confiable y auditable, no un borrador.

Aquí no liquidamos nada: empaquetamos. Los números ya deben venir cuadrados (ver 93) y verificados en `Matematicas_lushows`.

## Para qué sirve
Ya tienes los números cerrados y cuadrados. Aquí los presentas para que el dueño los entienda en minutos (ver 90), para que un banco te dé crédito, o para que queden archivados de forma auditable (ver 97). Un buen empaque no cambia los números, pero cambia cómo te perciben quienes deciden.

## Entregables que se generan en PDF
| Entregable | Para quién | Contenido base |
|---|---|---|
| Estado de Situación Financiera (Balance) | Dueño, banco, DIAN | ver 20 |
| Estado de Resultados (P&G) | Dueño, banco | ver 21 |
| Flujo de Efectivo | Dueño | ver 90 |
| Informe mensual al dueño | Dueño | tablero (ver 91) + comentarios |
| Conciliación bancaria | Archivo / auditoría | ver 93 |
| Certificación de estados | Banco / trámites | estados + firma del contador |

## 1. Estructura del informe mensual al dueño
El entregable estrella. Que un dueño no contable lo entienda en 10 minutos (ver 90):
1. **Portada** — negocio, mes, fecha.
2. **Resumen en una página** — el tablero de 8 indicadores (ver 91) con colores verde/amarillo/rojo.
3. **Estado de Resultados** del mes vs. mes anterior.
4. **Balance** resumido.
5. **Flujo de efectivo** — de dónde entró y salió la plata.
6. **Comentarios del contador** — 3 a 5 frases simples: qué pasó y qué vigilar.
7. **Próximos vencimientos** (ver 92).

> Aviso de cumplimiento: cualquier cifra de impuestos, tarifa o UVT **depende del año y se verifica con la norma vigente**. El PDF reporta números ya verificados en `Matematicas_lushows`; nunca calcules de cabeza para el entregable.

## 2. Cómo generar el PDF profesional (flujo recomendado)
No conviertas Markdown directo: se ve a "documento técnico". El camino limpio es **redactar el contenido en un HTML bien diseñado e imprimirlo a PDF con Chrome headless**. Chrome ya está instalado en cualquier PC; no necesitas instalar nada extra.

**Paso a paso:**
1. Redacta el informe en un archivo `informe.html` con estilos de impresión (esqueleto abajo).
2. Revisa que se vea bien abriéndolo en el navegador (doble clic).
3. Conviértelo a PDF con Chrome en modo headless (sin abrir ventana).

**Comando (Windows PowerShell)** — ajusta la ruta de Chrome a la tuya:

```powershell
& "C:\Program Files\Google\Chrome\Application\chrome.exe" `
  --headless --disable-gpu `
  --print-to-pdf="informe.pdf" `
  --no-pdf-header-footer `
  "file:///C:/ruta/a/informe.html"
```

En Mac/Linux el equivalente es:

```bash
google-chrome --headless --print-to-pdf=informe.pdf --no-pdf-header-footer informe.html
```

Si la ruta de Chrome no existe, búscala en `C:\Program Files (x86)\Google\Chrome\...` o usa Edge (`msedge.exe`), que acepta los mismos parámetros.

## 3. Esqueleto de HTML imprimible (copia y pega)

```html
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<style>
  @page { size: A4; margin: 18mm 16mm; }
  body { font-family: Georgia, "Times New Roman", serif; color: #1a1a1a;
         font-size: 11pt; line-height: 1.5; }
  h1 { font-size: 22pt; color: #0b3d2e; border-bottom: 3px solid #0b3d2e;
       padding-bottom: 6px; }
  h2 { font-size: 14pt; color: #0b3d2e; margin-top: 24px;
       page-break-after: avoid; }
  .portada { text-align: center; padding-top: 30vh; page-break-after: always; }
  .seccion { page-break-inside: avoid; }      /* evita cortar a la mitad */
  table { width: 100%; border-collapse: collapse; margin: 10px 0; font-size: 10pt; }
  th, td { border: 1px solid #ccc; padding: 6px 8px; text-align: right; }
  th { background: #0b3d2e; color: #fff; }
  td.concepto, th.concepto { text-align: left; }
  .total td { font-weight: bold; border-top: 2px solid #0b3d2e; }
  .kpi { display:inline-block; background:#f1f7f4; border:1px solid #0b3d2e;
         border-radius:8px; padding:10px 16px; margin:4px; }
  .verde{color:#0b7a3e;} .rojo{color:#b00020;} .amarillo{color:#a86b00;}
  @media print { a { color: inherit; text-decoration: none; } }
</style>
</head>
<body>
  <div class="portada">
    <h1 style="border:none;">Informe Financiero Mensual</h1>
    <p>[Negocio] — [Mes/Año] — Elaborado por [Contador]</p>
  </div>

  <div class="seccion">
    <h2>Resumen del mes</h2>
    <span class="kpi">Ventas: $9.500.000 <span class="verde">▲</span></span>
    <span class="kpi">Margen: 54% <span class="rojo">▼</span></span>
    <span class="kpi">Utilidad: $900.000 <span class="rojo">▼</span></span>
  </div>

  <div class="seccion">
    <h2>Estado de Resultados</h2>
    <table>
      <tr><th class="concepto">Concepto</th><th>Mes actual</th><th>Mes anterior</th></tr>
      <tr><td class="concepto">Ingresos</td><td>$9.500.000</td><td>$9.000.000</td></tr>
      <tr><td class="concepto">(−) Costo de ventas</td><td>$4.370.000</td><td>$3.780.000</td></tr>
      <tr class="total"><td class="concepto">Utilidad neta</td><td>$900.000</td><td>$1.100.000</td></tr>
    </table>
  </div>
</body>
</html>
```

Claves de impresión: `@page` fija tamaño y márgenes; `page-break-inside: avoid` impide que una tabla se parta entre páginas; `page-break-after: always` deja la portada sola. Números a la derecha, conceptos a la izquierda, una sola tipografía y un solo color de acento (verde esmeralda).

## Ejemplo (cifras ILUSTRATIVAS / inventadas)
El contador de "Café del Parque" cierra mayo (ver 93), arma el `informe.html` con el tablero (ver 91) y el P&G vs. abril, escribe 4 frases de comentario ("vendimos más pero el margen cayó por el costo del café; vigilar la cartera"), y lo imprime a `informe-mayo-2026.pdf`. Se lo manda al dueño por WhatsApp vía AVIS. El dueño lo entiende en 5 minutos. *(Todas las cifras vienen verificadas de `Matematicas_lushows`.)*

## Errores comunes
- **Entregar Markdown, Excel crudo o un .docx improvisado.** Se ve a borrador. PDF siempre.
- **Poner cifras sin verificar.** El PDF reporta números ya cuadrados (93) y verificados (Matematicas), nunca calculados a ojo.
- **Tablas que se cortan entre páginas.** Falta `page-break-inside: avoid`.
- **Números alineados a la izquierda.** El dinero va a la derecha para poder compararlo de un vistazo.
- **Demasiados colores y tipografías.** Un acento, una serif. Sobrio = confiable.
- **Olvidar la ruta correcta de Chrome.** Si el comando falla, lo primero a revisar es la ruta del ejecutable.
- **No archivar el PDF generado.** El entregable también es soporte (ver 97).

## Conexión con otros módulos
- **20 (Balance)** y **21 (Estado de Resultados)** — el contenido de los estados.
- **90 (Leer tus números)** y **91 (Tablero)** — el informe mensual nace de aquí.
- **93 (Checklist mensual)** — el PDF se genera tras cerrar y cuadrar el mes.
- **97 (Organizar soportes)** — el PDF generado se archiva como soporte.
- **AVIS (bot)** — entrega el PDF al dueño por WhatsApp.
- **Matematicas_lushows** — todas las cifras del PDF vienen verificadas de allá.

## Siguiente paso típico
Tras cerrar el mes (93), arma el `informe.html` con el tablero y el P&G, imprímelo a PDF con Chrome headless, archívalo (97) y entrégaselo al dueño. Nunca entregues el borrador en Markdown.
