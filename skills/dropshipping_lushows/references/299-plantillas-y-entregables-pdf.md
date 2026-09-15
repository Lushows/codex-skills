# Plantillas y entregables PDF

> Un análisis que vive en el chat se pierde. **El entregable de esta skill es un PDF**: se archiva, se
> compara mes a mes y se puede mandar a un socio, a un proveedor o al contador. Markdown crudo y HTML
> suelto no son entregables — son pasos intermedios.

## El pipeline: HTML → Chrome headless → PDF

Sin instalar nada. Chrome (o Edge) ya está en la máquina.

### Windows / PowerShell

```powershell
& "C:\Program Files\Google\Chrome\Application\chrome.exe" `
  --headless --disable-gpu `
  --print-to-pdf="C:\ruta\informe.pdf" `
  --print-to-pdf-no-header `
  --no-pdf-header-footer `
  "file:///C:/ruta/informe.html"
```

Si no hay Chrome, sirve Edge: `C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe`, mismos
parámetros.

### Bash (macOS / Linux / Git Bash)

```bash
chrome --headless --disable-gpu \
  --print-to-pdf="$PWD/informe.pdf" --no-pdf-header-footer \
  "file://$PWD/informe.html"
```

### Reglas que evitan los tres errores típicos

| Error | Causa | Solución |
|---|---|---|
| Sale en blanco | Ruta mal formada | `file:///C:/...` con tres barras y barras normales, nunca `\` |
| Salen encabezados y números de Chrome | Falta el flag | `--no-pdf-header-footer` |
| Tablas cortadas entre páginas | CSS | `tr, table { break-inside: avoid; }` |
| Fuentes raras | Fuente externa no cargó | Usar fuentes del sistema |
| Colores planos | Chrome no imprime fondos | `-webkit-print-color-adjust: exact;` |

### CSS base del entregable

```css
@page { size: A4; margin: 18mm 16mm; }
body { font-family: -apple-system, "Segoe UI", Roboto, sans-serif;
       font-size: 10.5pt; line-height: 1.45; color: #16181d;
       -webkit-print-color-adjust: exact; }
h1 { font-size: 20pt; margin: 0 0 2mm; letter-spacing: -.02em; }
h2 { font-size: 13pt; margin: 8mm 0 2mm; padding-bottom: 1.5mm;
     border-bottom: 1.5px solid #111; }
table { width: 100%; border-collapse: collapse; margin: 3mm 0; font-size: 9.5pt; }
th { background: #16181d; color: #fff; text-align: left; padding: 2mm; }
td { border-bottom: .5px solid #d6d9de; padding: 2mm; }
tr, table, .bloque { break-inside: avoid; }
.kpi { display: inline-block; min-width: 42mm; padding: 3mm; margin: 1mm;
       border: 1px solid #d6d9de; border-radius: 3px; }
.kpi b { display: block; font-size: 17pt; }
.rojo { color: #b3261e; } .verde { color: #1c6b3a; }
.nota { font-size: 8.5pt; color: #5b6069; }
```

**Números en tabla siempre alineados a la derecha, con separador de miles y la misma cantidad de
decimales.** Un PDF con números desalineados no lo lee nadie.

---

## Los 6 entregables de la skill

| # | Entregable | Cuándo | Módulos que lo alimentan |
|---|---|---|---|
| 1 | **Informe de investigación de producto** | Antes de testear | `50`, `76`, `81` |
| 2 | **Plan de lanzamiento a 90 días** | Al arrancar | `298` |
| 3 | **Modelo de economía unitaria** | Antes de gastar | `223`, `228`, `233` |
| 4 | **Informe semanal de operación** | Cada lunes | `276` |
| 5 | **Cierre mensual / de temporada** | Día 1-3 del mes; 7-ene | `276`, `295` |
| 6 | **Expediente de cierre de producto** | Al matar un producto | `296` |

---

## 1. Informe de investigación de producto

```
PORTADA         Producto · país · fecha · veredicto en una línea
1. EL PRODUCTO  Qué es, qué problema visible resuelve, demo
2. SCORECARD    Tabla con los criterios de `76` y puntaje
3. DEMANDA      Evidencia: anuncios activos, antigüedad, tendencias (`60`)
4. SATURACIÓN   Competidores, cuántos, desde cuándo (`61`)
5. NÚMEROS      Costo puesto en destino, precio, múltiplo, techo de CAC
6. RIESGOS      Regulatorio, PI, logística, devoluciones
7. VEREDICTO    TESTEAR / DESCARTAR / ESPERAR + presupuesto y criterio de corte
```

La línea que no puede faltar: **"se descarta si no hay 3-5 ventas con economía positiva al gastar
USD [X]"**.

## 2. Plan de lanzamiento a 90 días

Portada + tabla de 13 semanas con `Semana · Fechas · Entregable · Puerta · Estado`, tomada de `298`.
Al final: presupuesto por fase, fechas de corte de proveedor y la lista de las 6 puertas.

## 3. Modelo de economía unitaria

```
SUPUESTOS       Costo producto, flete, arancel, pasarela, devoluciones, ticket
UNIDAD          Ingreso · costo variable · margen de contribución
TECHO DE CAC    Cuánto puedes pagar por venta
ROAS EQUILIBRIO Y el ROAS objetivo con holgura
ESCENARIOS      Pesimista / base / optimista
CAJA            Días de rotación, vueltas por temporada (`32`)
SENSIBILIDAD    Qué pasa si el CPM sube 30% / si la entrega cae 10 puntos
```

> Los cálculos van ejecutados y verificados, no estimados a ojo. **Invoca `Matematicas_lushows`**
> para producir y auditar las cifras antes de meterlas al PDF.

## 4. Informe semanal de operación (el más usado)

```html
<h1>Informe semanal · [tienda]</h1>
<p class="nota">Semana [lun]-[dom] · generado [fecha]</p>

<div class="bloque">
  <span class="kpi"><b>$[ingreso]</b>Ingreso</span>
  <span class="kpi"><b>$[gasto]</b>Pauta</span>
  <span class="kpi"><b>$[margen]</b>Margen de contribución</span>
  <span class="kpi"><b>[n]</b>Pedidos</span>
  <span class="kpi"><b>$[cpa]</b>CPA real</span>
  <span class="kpi"><b>[roas]x</b>ROAS real</span>
</div>

<h2>Comparativo</h2>   <!-- esta semana vs las 2 anteriores, con % -->
<h2>Qué funcionó</h2>  <!-- 3 viñetas, con número cada una -->
<h2>Qué falló</h2>     <!-- 3 viñetas, con número cada una -->
<h2>Decisiones de la semana</h2>  <!-- escalar / matar / iterar -->
<h2>Alertas</h2>       <!-- stock, contracargos, entregas, caja -->
<h2>La semana entrante</h2>  <!-- 3 acciones, con responsable y fecha -->
```

Regla: **cada afirmación con un número al lado.** "El creativo 7 funcionó bien" no es informe;
"el creativo 7 cerró en CPA 143 vs 210 del promedio" sí.

## 5. Cierre mensual / de temporada

```
RESUMEN         Ingreso, utilidad real, margen neto %, caja disponible
P&L SIMPLE      Ingreso − devoluciones − contracargos − mercancía − envíos
                − pauta − comisiones − fijos = UTILIDAD
ADQUISICIÓN     CAC, ROAS, CPM, mezcla de canales
CLIENTES        Nuevos, recompra, LTV 90 días, tamaño de lista
OPERACIÓN       % entregado, tiempo de respuesta, devoluciones, contracargos + ratio
PROVISIONES     Contracargos y devoluciones pendientes (clave en enero)
DECISIONES      Qué se mantiene, qué se corta, qué se prueba
```

## 6. Expediente de cierre de producto

Las 10 líneas de `296`, más los creativos ganadores y el enlace a la carpeta de material. Una página.
Se relee antes del siguiente producto.

---

## Reglas de todos los entregables

| Regla | Por qué |
|---|---|
| Veredicto en la primera página | Nadie lee 8 páginas para encontrar la conclusión |
| Rangos con "verificar" cuando el dato no es tuyo | Nunca inventes precisión (`00`) |
| Fuente y fecha de cada dato externo | Los aranceles y las políticas cambian |
| Misma moneda en todo el documento, declarada | Mezclar USD y MXN sin decir cuál es cuál arruina el informe |
| Comparación contra ti mismo, no contra promedios de internet | Tus números son la única referencia válida |
| Nombre de archivo `AAAA-MM-DD_tipo_producto.pdf` | Se ordena solo |
| Guardar el HTML fuente junto al PDF | Para regenerar el mes siguiente |

## Flujo completo, resumido

```
datos del tablero (`276`)
  → cálculo verificado (invoca `Matematicas_lushows`)
  → HTML con el CSS base
  → chrome --headless --print-to-pdf --no-pdf-header-footer
  → PDF entregado + HTML archivado
```

## Relacionados
`01` cómo usar esta skill · `276` el tablero del operador · `228` modelo financiero ·
`296` expediente de cierre · `298` el plan de 90 días · `295` cierre de temporada · `109` el informe
semanal de inteligencia · invoca `Matematicas_lushows` para los cálculos
