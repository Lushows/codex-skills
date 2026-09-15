# 99 — Plantillas y generación de PDF

Este módulo es tu "kit de entrega final": cómo organizar un plan de negocio profesional, qué plantillas usar (Business Model Canvas, P&L, punto de equilibrio) y cómo convertir todo en un PDF limpio y presentable. Regla de oro de entrega: **nunca entregues Markdown crudo a un cliente, banco o inversionista. Siempre PDF.**

## Para qué sirve

Tienes ya el análisis (mercado, modelo, números). Aquí lo empaquetas para que se vea como lo que es: un documento de consultor, no un borrador. Un plan bien presentado no mejora el negocio, pero sí mejora cómo te perciben quien decide darte un crédito, un socio o un cliente grande.

## 1. Estructura completa de un plan de negocio

Orden estándar (cada sección = 1 a 2 páginas; el total ronda 15-25 páginas, anexos aparte):

| # | Sección | Qué responde | Apoyo en |
|---|---------|--------------|----------|
| 1 | Resumen ejecutivo | "¿Qué es y por qué funciona?" en 1 página | escribir al final |
| 2 | Problema / Solución | Dolor real + cómo lo resuelves | ver 13 (idea/validación) |
| 3 | Mercado | Tamaño (TAM/SAM/SOM) y tendencia | ver 20, ver 21 |
| 4 | Modelo de negocio | Cómo ganas dinero, precios | ver 40, ver 57 |
| 5 | Competencia | Quién más lo hace y tu diferencia | ver 22 |
| 6 | Marketing y ventas | Cómo consigues clientes (CAC, canales) | ver 47, ver 52 |
| 7 | Operación | Cómo produces/entregas día a día | — |
| 8 | Equipo | Quién ejecuta y por qué creerle | — |
| 9 | Finanzas | Break-even, P&L, proyección 12-36 meses | ver 53, 54, 56 |
| 10 | Riesgos | Qué puede salir mal y tu plan B | — |
| 11 | Hoja de ruta | Hitos por trimestre | — |

**Resumen ejecutivo (lo más importante):** se escribe al final, pero va primero. Debe incluir, en ~250 palabras: qué vendes, a quién, tamaño de oportunidad, cómo ganas dinero, tracción/avance, cuánto dinero necesitas (si aplica) y qué harás con él. Si solo leen esta página, deben querer reunirse contigo.

> Aviso de país: cualquier cifra legal/fiscal/laboral (impuestos, costo de nómina, trámites de constitución) **depende del país y ciudad**. Pregunta país/ciudad primero y verifica las reglas vigentes (ver 21 para cómo conseguir el dato real). Aquí solo damos el método.

## 2. Plantilla — Business Model Canvas

Una hoja, 9 bloques. Útil para pensar el negocio antes de escribir 20 páginas:

```
+----------------+----------------+----------------+----------------+
| Socios clave   | Actividades    | Propuesta de   | Relación con   |
|                | clave          | valor          | clientes       |
+----------------+----------------+  (el "por qué  +----------------+
|                | Recursos       |   te compran") | Canales        |
|                | clave          |                |                |
+----------------+----------------+----------------+----------------+
| Estructura de costos            | Fuentes de ingreso              |
+---------------------------------+---------------------------------+
```

Llénalo en una sola frase por bloque. Si un bloque te cuesta llenarlo, ahí está tu hueco real.

## 3. Plantilla — P&L (Estado de Resultados) simplificado

P&L = "Profit & Loss" = lo que entra menos lo que sale. Estructura mínima mensual:

```
(+)  Ingresos por ventas
(−)  Costo de lo vendido (COGS: materia prima, producto, comisión por venta)
(=)  MARGEN BRUTO
(−)  Gastos fijos (arriendo, sueldos, software, servicios)
(−)  Marketing
(=)  EBITDA / Utilidad operativa
(−)  Impuestos y depreciación   ← tasa según país (verificar)
(=)  UTILIDAD NETA
```

**Ejemplo NUMÉRICO ilustrativo** (cifras inventadas, solo para mostrar el cálculo — NO son datos de mercado):

| Concepto | Mes |
|---|---|
| Ingresos (100 ventas × $50.000) | $5.000.000 |
| (−) COGS (40% de la venta) | −$2.000.000 |
| **Margen bruto (60%)** | **$3.000.000** |
| (−) Gastos fijos | −$1.800.000 |
| (−) Marketing | −$600.000 |
| **Utilidad operativa** | **$600.000** |

Lectura: cada venta deja $30.000 de margen bruto ($50.000 − $20.000 de costo variable). Eso es lo que paga tus gastos fijos. Guarda ese número, lo usamos abajo.

## 4. Plantilla — Calculadora de punto de equilibrio (break-even)

Punto de equilibrio = cuántas ventas necesitas para no perder ni ganar (utilidad = 0).

**Fórmula:**

```
Margen de contribución por unidad = Precio − Costo variable por unidad
Punto de equilibrio (unidades)    = Gastos fijos totales ÷ Margen de contribución
Punto de equilibrio (en dinero)   = Unidades de equilibrio × Precio
```

**Ejemplo NUMÉRICO ilustrativo** (mismas cifras inventadas de arriba):

```
Precio                        = $50.000
Costo variable por unidad     = $20.000
Margen de contribución        = $30.000
Gastos fijos + marketing      = $1.800.000 + $600.000 = $2.400.000

Punto de equilibrio (uds)     = 2.400.000 ÷ 30.000 = 80 ventas/mes
Punto de equilibrio (dinero)  = 80 × 50.000 = $4.000.000/mes
```

Interpretación accionable: por debajo de 80 ventas pierdes; venta 81 en adelante es ganancia. Si crees que vender 80/mes es duro, el problema es el modelo o el precio (ver 40, 57), no la presentación.

## 5. Cómo generar el PDF profesional (flujo recomendado)

No conviertas Markdown directo: se ve a "documento técnico". El camino limpio es **redactar el contenido en un HTML bien diseñado e imprimirlo a PDF con Chrome headless**. Chrome ya está instalado en cualquier PC, no necesitas instalar nada extra.

**Paso a paso:**

1. Redacta el plan en un archivo `plan.html` con estilos de impresión (esqueleto abajo).
2. Revisa que se vea bien abriéndolo en el navegador (doble clic).
3. Conviértelo a PDF con Chrome en modo headless (sin abrir ventana).

**Comando (Windows PowerShell)** — ajusta la ruta de Chrome a la tuya:

```powershell
& "C:\Program Files\Google\Chrome\Application\chrome.exe" `
  --headless --disable-gpu `
  --print-to-pdf="plan.pdf" `
  --no-pdf-header-footer `
  "file:///C:/ruta/a/plan.html"
```

En Mac/Linux el equivalente es:

```bash
google-chrome --headless --print-to-pdf=plan.pdf --no-pdf-header-footer plan.html
```

Si la ruta de Chrome no existe, búscala en `C:\Program Files (x86)\Google\Chrome\...` o usa Edge (`msedge.exe`), que acepta los mismos parámetros.

## 6. Esqueleto de HTML imprimible (copia y pega)

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
  th, td { border: 1px solid #ccc; padding: 6px 8px; text-align: left; }
  th { background: #0b3d2e; color: #fff; }
  .kpi { display:inline-block; background:#f1f7f4; border:1px solid #0b3d2e;
         border-radius:8px; padding:10px 16px; margin:4px; }
  @media print { a { color: inherit; text-decoration: none; } }
</style>
</head>
<body>
  <div class="portada">
    <h1 style="border:none;">Plan de Negocio</h1>
    <p>[Nombre del negocio] — [Ciudad, País] — [Fecha]</p>
  </div>

  <div class="seccion">
    <h2>1. Resumen ejecutivo</h2>
    <p>...</p>
  </div>

  <div class="seccion">
    <h2>9. Finanzas</h2>
    <span class="kpi">Punto de equilibrio: 80 ventas/mes</span>
    <span class="kpi">Margen bruto: 60%</span>
    <table>
      <tr><th>Concepto</th><th>Mes 1</th></tr>
      <tr><td>Ingresos</td><td>$5.000.000</td></tr>
    </table>
  </div>
</body>
</html>
```

Claves de impresión: `@page` fija tamaño y márgenes; `page-break-inside: avoid` impide que una tabla se parta entre páginas; `page-break-after: always` en la portada la deja sola. Usa una sola tipografía y un solo color de acento (aquí verde esmeralda).

## Errores comunes

- **Entregar Markdown o un .docx improvisado.** Se ve a borrador. PDF siempre.
- **Resumen ejecutivo escrito primero y a las prisas.** Es la página que más se lee; escríbela al final.
- **Inventar el tamaño de mercado.** No pongas "el mercado es de X millones" si no lo verificaste (ver 21). Da rango orientativo y cita la fuente.
- **Tablas que se cortan entre páginas.** Falta `page-break-inside: avoid`.
- **Afirmar tasas de impuestos o trámites como verdad.** Depende del país/ciudad y cambia; deja una nota de "sujeto a verificación".
- **Demasiados colores y tipografías.** Un acento, una serif para texto. Sobrio = serio.
- **Olvidar la ruta correcta de Chrome.** Si el comando falla, lo primero a revisar es la ruta del ejecutable.

## Siguiente paso típico

Arma primero el Canvas (1 hoja), valida el punto de equilibrio con tus números reales (ver 53), y solo entonces redacta el `plan.html` e imprímelo a PDF. Si el break-even te asusta, vuelve a precio/modelo (ver 40, 57) antes de presentar nada.
