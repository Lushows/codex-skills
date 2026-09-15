# 99 — Maestría y entregables

Lee este módulo cuando quieras pasar de "saber poner anuncios" a ser un especialista de élite que cobra bien y manda entregables de nivel, o cuando Lushows te pida un **media plan, plan de keywords, brief o reporte ejecutivo** y necesites generarlo bonito en PDF (no entregar un MD crudo esperando que el usuario lo procese). Este es el módulo de cierre: el camino del oficio + cómo se ven los entregables profesionales y cómo producirlos. Marco que cierra la skill: Google **captura intención** — el élite es quien sabe medir esa captura sin engañarse (incrementalidad, MER) y entregar la verdad de forma presentable.

## El camino del especialista de élite

El que sabe de verdad no es el que conoce más botones; es el que **piensa en plata y en sistema**:

| Nivel | Qué domina | Cómo se nota |
|---|---|---|
| Operador | Crea campañas, lee paneles | Hace lo que le piden |
| Optimizador | Lee términos, negativos, ajusta pujas | La cuenta mejora semana a semana |
| Estratega | Conecta canal-funnel-economía-CRM | Decide QUÉ pautar y por qué (ver 97, 96) |
| **Élite** | Mide incrementalidad, gobierna por MER, cierra el loop con OCI, sabe cuándo NO pautar Google | Le dice al cliente "esto NO es para Google, ve a Meta" y acierta |

Los principios que separan al élite:
1. **La verdad está en la caja, no en el panel.** El ROAS de Google miente si no es incremental (ver 65). Mira el negocio (MER, ver 97), no la métrica que la plataforma se auto-atribuye — y en 2026 la IA (PMax/AI Max) se auto-atribuye más que nunca.
2. **Negativos > pujas.** La rentabilidad se gana podando lo que no compra, no afinando decimales de puja (ver 22).
3. **Honestidad con los números.** Si la cuenta no es rentable, dilo. Si Google no es el canal, dilo (ver 03). El que infla resultados pierde al cliente cuando se descubre.
4. **La medición es el cimiento.** Sin conversiones reales bien medidas, todo lo demás es ruido (ver 05, 06, 53).
5. **Suelta la IA con freno, no con fe.** AI Max y PMax suben alcance, pero sin negativos, brand exclusions y assets curados, optimizan hacia gasto (ver 90, 91).
6. **Rutea fuera cuando no es tu trabajo.** Cerrar → `ventas_lushows`; landing → `desingweb-lushows`; viabilidad → `economist_lushows`; generar demanda → `facebook_ads_lushows`; descubrimiento → `tiktok_ads_lushows`; marca → `directorcreativo_lushows`; costo de tu IA → `optimizer_tokens_lushows`. El élite sabe sus límites.

## Los 4 entregables y qué lleva cada uno

| Entregable | Cuándo | Qué contiene |
|---|---|---|
| **Media plan** | Antes de lanzar / propuesta a cliente | Objetivo, presupuesto/mes, canales y % de reparto, CPA/ROAS meta, fases, timeline (ver 98, 97) |
| **Plan de keywords** | Setup de Search | Keywords por grupo, concordancia, volumen estimado, CPC estimado en COP, negativos iniciales (ver 20, 21, 22) |
| **Brief creativo** | Para RSA/video | Propuesta de valor, ángulos, titulares/descripciones, objeciones a responder, do/don't (ver 30, 31; arte → `directorcreativo_lushows`) |
| **Reporte ejecutivo** | Mensual al cliente | Inversión, conversiones, CPA, MER, qué se hizo, qué sigue — 1 página, sin 40 métricas (ver 95, 60) |

Regla de entregable: **simple, honesto, accionable.** Un reporte de 1 página que el cliente entiende vale más que un dashboard de 30 métricas que no lee. Nunca infles; muestra el número real y qué vas a hacer con él.

## Cómo generar el entregable en PDF (HTML → chrome headless)

El flujo profesional: escribes el contenido en **HTML con estilo** (no MD), y lo conviertes a PDF con Chrome en modo headless. Sale un PDF limpio, con tu diseño, listo para mandar al cliente. Este es el flujo estándar de entregables de Lushows: no entregues MD ni HTML crudo, entrega el PDF.

**Paso 1 — Escribe un HTML con estilo.** Una plantilla base sobria (para diseño de élite, rutea a `desingweb-lushows`; para reportes simples basta esto). Reporte ejecutivo:

```html
<!doctype html><html lang="es"><head><meta charset="utf-8">
<style>
  @page { size: A4; margin: 18mm; }
  body { font-family: 'Segoe UI', Arial, sans-serif; color:#1a1a1a; font-size:12px; line-height:1.5; }
  h1 { color:#0b6b3a; border-bottom:3px solid #0b6b3a; padding-bottom:6px; }
  h2 { color:#0b6b3a; margin-top:22px; }
  table { width:100%; border-collapse:collapse; margin:12px 0; }
  th,td { border:1px solid #ddd; padding:8px; text-align:left; }
  th { background:#0b6b3a; color:#fff; }
  .kpi { display:inline-block; padding:10px 16px; background:#f2f7f4; border-radius:8px; margin:4px; }
  .kpi b { font-size:20px; color:#0b6b3a; display:block; }
  .muted { color:#666; font-size:11px; }
</style></head><body>
  <h1>Reporte Google Ads — [Cliente] — [Mes 2026]</h1>
  <div class="kpi"><b>$1.250.000</b>Inversión COP</div>
  <div class="kpi"><b>38</b>Conversiones (ventas)</div>
  <div class="kpi"><b>$32.895</b>CPA COP</div>
  <div class="kpi"><b>4.1</b>MER</div>
  <h2>Qué hicimos</h2>
  <ul><li>Revisión de términos: 14 negativos nuevos</li>
      <li>AI Max activado en campaña ganadora con blindaje</li>
      <li>OCI cargando ventas reales desde el CRM</li></ul>
  <h2>Qué sigue</h2>
  <ul><li>Subir presupuesto 15% en Search marca</li>
      <li>Cargar Customer Match para excluir compradores</li></ul>
  <p class="muted">CPA = costo por venta real (no por clic a WhatsApp). MER = ventas totales del negocio / inversión total en pauta.</p>
</body></html>
```

**Paso 2 — Convierte a PDF con Chrome headless.** En Windows (PowerShell), con Chrome o Edge instalado:

```powershell
& "C:\Program Files\Google\Chrome\Application\chrome.exe" `
  --headless --disable-gpu --no-pdf-header-footer `
  --print-to-pdf="C:\Users\user\Desktop\reporte.pdf" `
  "C:\Users\user\Desktop\reporte.html"
```

Si no hay Chrome, sirve Edge (mismo flag, otra ruta):

```powershell
& "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" `
  --headless --disable-gpu --no-pdf-header-footer `
  --print-to-pdf="C:\Users\user\Desktop\reporte.pdf" `
  "C:\Users\user\Desktop\reporte.html"
```

El flag `--no-pdf-header-footer` quita la URL y fecha que Chrome mete por defecto (detalle de amateur si lo olvidas). El `@page` del CSS controla tamaño A4 y márgenes. Si el HTML usa imágenes/fuentes locales, ponlas con ruta absoluta o el PDF sale sin ellas.

**Paso 3 — Entrega el PDF**, no el HTML ni el MD. El cliente recibe algo presentable; tú quedas como profesional.

## Plantilla de bloques reutilizables (para los 4 entregables)

| Bloque | Para qué entregable | Forma |
|---|---|---|
| Tabla de reparto de presupuesto por canal/% | Media plan | tabla 3 columnas (canal, $COP, %) |
| Tabla de keywords (keyword, match, volumen, CPC est., grupo) | Plan de keywords | tabla 5 columnas |
| Lista de negativos iniciales | Plan de keywords | lista o tabla |
| KPIs en tarjetas (`.kpi`) | Reporte ejecutivo | inversión, conversiones, CPA, MER |
| "Qué hicimos / qué sigue" | Reporte ejecutivo | dos listas cortas |
| Do / Don't | Brief creativo | dos columnas |

Notas de oficio:
- Usa la **paleta/tipografía de la marca del cliente** si la tiene (rutea a `directorcreativo_lushows` por el brand-kit; cambia el `#0b6b3a` por su color).
- Mantén **números reales en COP** y una sola idea por sección. Nada de relleno ni 40 métricas.
- Para gráficos simples, una tabla bien hecha gana a un chart mal hecho. Si necesitas algo visualmente fino de verdad (propuesta comercial, pitch deck), construye el HTML con `desingweb-lushows`.
- Si generas muchos reportes/briefs con IA y el costo de tokens se sube, baja ese costo con `optimizer_tokens_lushows` (caching, batch, plantillas).

## Errores comunes — blacklist

- **Entregar MD o HTML crudo esperando que el cliente lo procese.** Genera el PDF tú; el élite manda algo presentable (ver flujo chrome headless arriba).
- **Reporte de 40 métricas que nadie lee.** Una página: inversión, conversiones, CPA, MER, qué hiciste, qué sigue (ver 95).
- **Inflar los números en el reporte.** Se descubre y pierdes al cliente; muestra el real y el plan.
- **Juzgar la cuenta por el ROAS del panel** en vez de incrementalidad/MER. El élite mira la caja, no la auto-atribución (ver 65, 97).
- **Creer que más botones = más maestría.** El nivel se mide en decisiones de plata y en saber cuándo NO pautar Google (ver 00, 03).
- **No rutear fuera lo que no es Google Ads.** Cerrar, landing, viabilidad, marca, demanda, descubrimiento — cada cosa a su skill; querer hacerlo todo lo hace todo peor.
- **Olvidar `--no-pdf-header-footer`** y entregar un PDF con la URL y fecha de Chrome encima. Detalle de amateur; quítalo.
- **Soltar la IA (PMax/AI Max) sin freno y reportarlo como triunfo.** Sin negativos/brand exclusions/incrementalidad, ese ROAS es humo (ver 90, 65).
