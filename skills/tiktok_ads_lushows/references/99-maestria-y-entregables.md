# 99 — Maestría y entregables

Lee este módulo cuando quieras saber qué separa a un media buyer de TikTok de élite del que solo "le da botones", o cuando necesites entregar algo profesional — un media plan, un brief de creativos o un reporte ejecutivo — en PDF, no en una captura de pantalla. La maestría es proceso; la presentación es respeto por tu cliente (o por ti mismo). Aquí están las dos.

## El camino del media buyer de élite

No se trata de saber dónde están los botones — eso lo aprende cualquiera en una semana. Lo que separa al de élite:

| Nivel | Qué hace | Mentalidad |
|---|---|---|
| **Principiante** | Configura campañas, mira el ROAS del panel | "¿Por qué no vende?" |
| **Intermedio** | Testea creativos, escala ganadores, lee fatiga | "¿Qué creativo gana y por qué?" |
| **Élite** | Piensa en sistema: creativo + señal + omnicanal + MER + economía del cliente | "¿El negocio entero es más rentable por lo que hago?" |

Los hábitos del de élite:

- **Vive en el creativo, no en la configuración.** Sabe que es el 80% (ver 92) y dedica el 80% de su tiempo a ángulos, hooks y producción (ver 30, 37, 38), no a mover pujas.
- **Es honesto con los números.** Usa MER global, no el ROAS inflado del panel (ver 97). Le dice al cliente "esto no es rentable" antes de que el cliente lo descubra.
- **Espía legal y sistemáticamente.** Entra a Creative Center cada semana (ver 94), tiene un banco de ángulos vivo (ver 38).
- **Cierra el círculo de datos.** Se asegura de que la conversión vuelva a TikTok (ver 96) y de que el lead no se enfríe (→ `ventas_lushows`).
- **Piensa omnicanal.** Sabe que TikTok siembra, Google cosecha, Meta puentea (ver 97). No defiende "su" canal; defiende el negocio.
- **Conoce la economía.** Antes de tomar un cliente valida que la unit economics da (→ `economist_lushows`). No promete lo imposible.
- **Respeta las políticas.** No arriesga la cuenta con claims prohibidos ni música robada (ver 08, 93).

El de élite no es el que sabe más trucos. Es el que sabe **qué importa** (creativo, señal, economía) y **qué es ruido** (vanity metrics, configuraciones marginales).

## Entregables profesionales: HTML → PDF con chrome headless

Cuando entregas a un cliente (o documentas para ti), no mandes capturas ni archivos sueltos. Genera un PDF limpio. El método: escribes un **HTML con CSS**, y lo conviertes a PDF con **Chrome en modo headless** (sin ventana). Es gratis, se ve profesional y lo controlas tú.

Los tres entregables que vas a generar:

| Entregable | Qué lleva | Cuándo |
|---|---|---|
| **Media plan** | Objetivo, presupuesto, mix de canales, calendario semanal, metas (CPA/MER) | Antes de lanzar / propuesta a cliente |
| **Brief de creativos** | Ángulos, hooks, guiones, referencias de Creative Center, qué graba el cliente | Para que el cliente/creator produzca (ver 38, 95) |
| **Reporte ejecutivo** | Spend, leads/ventas, CPA, MER, creativo ganador, plan próxima semana | Semanal/quincenal (ver 95) |

### Plantilla HTML (base con CSS para impresión)

Guarda esto como `entregable.html`, edita el contenido entre los comentarios, y conviértelo. La plantilla ya trae estilos pensados para PDF (márgenes, tipografía, tablas, color de marca):

```html
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<style>
  @page { size: A4; margin: 18mm 16mm; }
  * { box-sizing: border-box; }
  body { font-family: -apple-system, "Segoe UI", Roboto, Arial, sans-serif;
         color: #1a1a1a; font-size: 13px; line-height: 1.5; }
  h1 { font-size: 24px; margin: 0 0 4px; color: #000; }
  h2 { font-size: 16px; margin: 22px 0 8px; padding-bottom: 4px;
       border-bottom: 2px solid #FE2C55; color: #000; } /* rojo TikTok */
  .sub { color: #666; font-size: 12px; margin-bottom: 20px; }
  table { width: 100%; border-collapse: collapse; margin: 8px 0 16px; }
  th { background: #111; color: #fff; text-align: left; padding: 8px 10px; font-size: 12px; }
  td { border-bottom: 1px solid #e3e3e3; padding: 7px 10px; }
  tr:nth-child(even) td { background: #fafafa; }
  .kpi { display: inline-block; margin: 6px 18px 6px 0; }
  .kpi b { display: block; font-size: 22px; color: #FE2C55; }
  .kpi span { font-size: 11px; color: #666; text-transform: uppercase; }
  footer { margin-top: 28px; color: #999; font-size: 10px;
           border-top: 1px solid #e3e3e3; padding-top: 8px; }
</style>
</head>
<body>
  <!-- ===== EDITA DESDE AQUÍ ===== -->
  <h1>Reporte de Pauta TikTok — [Cliente]</h1>
  <div class="sub">Periodo: [fecha] · Preparado por: [tu nombre]</div>

  <div class="kpi"><b>$2.4M</b><span>Inversión COP</span></div>
  <div class="kpi"><b>3.1</b><span>MER global</span></div>
  <div class="kpi"><b>$18.400</b><span>CPA</span></div>
  <div class="kpi"><b>41</b><span>Ventas</span></div>

  <h2>Resumen de la semana</h2>
  <p>[2–3 frases: qué pasó, qué creativo ganó, qué decisión tomas.]</p>

  <h2>Desempeño por creativo</h2>
  <table>
    <tr><th>Creativo / ángulo</th><th>Gasto</th><th>CPA</th><th>Estado</th></tr>
    <tr><td>Dolor — "tu caja no cuadra"</td><td>$900k</td><td>$15.200</td><td>Escalar</td></tr>
    <tr><td>Prueba social — testimonio</td><td>$700k</td><td>$19.800</td><td>Mantener</td></tr>
    <tr><td>Identidad — "chef ordenado"</td><td>$800k</td><td>$31.000</td><td>Apagar</td></tr>
  </table>

  <h2>Plan próxima semana</h2>
  <ul>
    <li>Escalar el ganador +25% (ver módulo 15).</li>
    <li>Producir 3 hooks nuevos del ángulo dolor (ver 37).</li>
    <li>Refrescar el creativo fatigado (ver 39).</li>
  </ul>
  <!-- ===== HASTA AQUÍ ===== -->

  <footer>Generado para [Cliente] · TikTok Ads · MER = ventas totales ÷ pauta total</footer>
</body>
</html>
```

### Comando para convertir a PDF

Con Chrome (o Edge, mismo motor) instalado, desde la terminal:

```bash
# Windows (PowerShell o cmd)
& "C:\Program Files\Google\Chrome\Application\chrome.exe" --headless --disable-gpu --print-to-pdf="reporte.pdf" --no-pdf-header-footer "entregable.html"

# Mac
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --print-to-pdf="reporte.pdf" --no-pdf-header-footer "entregable.html"

# Si no hay Chrome pero sí Edge (Windows):
& "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --headless --disable-gpu --print-to-pdf="reporte.pdf" --no-pdf-header-footer "entregable.html"
```

`--no-pdf-header-footer` quita la fecha/URL fea que Chrome mete por defecto. El PDF sale en la misma carpeta. Para los otros entregables, cambia el contenido del HTML (media plan: tabla de mix de canales + calendario; brief: tabla de ángulos/hooks/guiones) y reusa la misma plantilla y comando.

Para que un entregable de **marca** (no de pauta) se vea de diseño superior — colores, tipografía, identidad — esa dirección de arte es de `directorcreativo_lushows`. Aquí basta con limpio y profesional.

## Errores comunes — blacklist

- **Mandar capturas del panel** como "reporte". El cliente no técnico no las entiende; genera PDF limpio.
- **Reportar el ROAS inflado del panel** en vez del MER global del negocio (ver 97). Honestidad o pierdes el cliente.
- **Pasar el 80% del tiempo en configuración** y el 20% en creativo. Es al revés (ver 92).
- **Entregar el brief de creativos a medias** y esperar que el cliente "adivine" qué grabar (ver 38, 95).
- **No tener cadencia fija de reporte.** Sin consistencia, no hay confianza ni renovación (ver 95).
- **Dejar el header/footer de Chrome** en el PDF (sale URL y fecha feas) — usa `--no-pdf-header-footer`.
- **Prometer resultados sin validar la economía del cliente** (→ `economist_lushows`). El de élite es honesto con los números.
