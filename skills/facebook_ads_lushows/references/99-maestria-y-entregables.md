# 99 — Maestría y entregables: el camino del media buyer de élite

El módulo de cierre: cómo se crece en este oficio, cómo se mantiene actualizado, y QUÉ produce esta skill cuando trabaja (los entregables concretos, sus plantillas y cómo generarlos en PDF). Léelo para entender el mapa completo y cada vez que tengas que generar un entregable para el usuario o un cliente.

## La curva de maestría

- **Nivel 1 — Ejecuta checklists**: lanza con el playbook (ver 98), optimiza con reglas (ver 70/71), no improvisa. Ya está por encima del 80% del mercado.
- **Nivel 2 — Diagnostica por capas**: ante cualquier problema recorre medición → oferta → creativo → estructura → entrega en orden (ver 61); distingue ruido de señal; sabe qué NO tocar.
- **Nivel 3 — Estratega**: lee el negocio completo (margen, operación, demanda, canal) y decide dónde la pauta SÍ es la palanca — y dónde no lo es y hay que decirlo (precio roto, oferta débil, operación que no cierra: economist_lushows / ventas_lushows). El nivel 3 rechaza proyectos que el nivel 1 acepta y quema.

En la era Advantage+ (ver 90) el nivel 1 es exactamente lo que la automatización reemplaza: si solo operas botones, te sustituye un toggle. La defensa contra la commoditización es subir a nivel 2-3 — criterio, diagnóstico y estrategia de negocio (ver 95).

## Mantenerse actualizado (las fuentes que valen)

1. **Tus PROPIOS datos** > cualquier gurú: el experimento documentado (ver 17) es tu única verdad permanente. Una hoja con cada test, hipótesis, resultado y aprendizaje vale más que 100 horas de YouTube.
2. Anuncios y changelog oficiales de Meta Business (las features llegan ahí antes que a los gurús, sin el humo).
3. Comunidades de practicantes que muestran números reales, no vendedores de cursos con pantallazos.
4. El Ad Library mensual (ver 94): lo que el mercado hace con plata real.

**El meta-principio**: las tácticas caducan (cada año muere una "estructura ganadora", desapareció el manual, llegó GEM, llegó el Meta Business Agent), el sistema no. **Oferta → creativo → señal → disciplina estadística** sobrevive cada update del algoritmo, incluido el próximo que aún no existe. Cuando algo cambie en Meta, pregunta: ¿cambia el sistema o solo la táctica? Casi siempre es solo la táctica (y la jerga tipo "Lattice" casi siempre es humo, ver 92).

## Los entregables de esta skill (cuándo y cómo)

| Entregable | Cuándo | Secciones |
|---|---|---|
| **Media plan** | Antes de lanzar o al replanificar | Objetivo de negocio y CPA/MER meta (desde margen, ver 64) · estructura de campañas · presupuesto mensual y distribución (ver 18) · calendario de fases (ver 98) · creativos requeridos · **proyección honesta con rangos y supuestos explícitos, nunca promesa de ROAS** |
| **Brief creativo** (para creator/diseñador) | Cada producción de creativos | Ángulo y a quién le habla (ver 38) · hook exacto o variantes (ver 37) · formato y duración (ver 33) · specs (9:16, 1:1, safe zones) · oferta y CTA (ver 45) · referencias (links de Ad Library, ver 94) · qué NO hacer (claims prohibidos, ver 44) |
| **Batería de copys** | Con cada batería creativa | Organizada por temperatura del público (ver 42): fría/tibia/caliente, 3-5 variantes por pieza, con hook + cuerpo + CTA |
| **Checklist de auditoría** | Al tomar una cuenta o trimestral | Los 20 puntos: medición (píxel/CAPI/EMQ/eventos, ver 62) · estructura (consolidación, solapamiento, ver 10/24) · creativo (volumen, diversidad, Entity ID, fatiga, ver 39/92) · métricas vs margen real (ver 64) · cumplimiento, verificación y Account Quality (ver 93) |
| **Reporte ejecutivo** | Mensual | Formato de 67: números vs objetivo, qué se probó/aprendió, plan del mes siguiente — para dueños de negocio, no para media buyers |

## Cómo se genera un entregable: HTML → PDF con chrome headless

Todo presentable se entrega en **PDF** (preferencia del usuario: PDF, no MD ni HTML suelto). El flujo:

1. **Redacta el contenido** con la estructura del entregable (tabla de arriba).
2. **Maqueta en un HTML autónomo**: un solo archivo, CSS embebido (sin dependencias externas), tipografía y color de la marca (pídelos a directorcreativo_lushows si hay manual; si no, una paleta sobria). Incluye `@page { size: A4; margin: ... }` y `@media print` para que pagine bien; usa `page-break-inside: avoid` en tablas y tarjetas.
3. **Convierte a PDF con chrome headless** (ejemplo de comando):

   ```bash
   # Windows (ruta típica de Chrome)
   "C:\Program Files\Google\Chrome\Application\chrome.exe" \
     --headless --disable-gpu --no-pdf-header-footer \
     --print-to-pdf="media-plan.pdf" "media-plan.html"

   # Alternativa multiplataforma
   chrome --headless --print-to-pdf=salida.pdf entrada.html
   ```

   Si `--no-pdf-header-footer` no aplica en la versión instalada, omítelo. Verifica que el PDF abra y pagine bien antes de entregarlo.
4. **Entrega el PDF** (no el HTML ni el MD). Detalle técnico de generación HTML/print-CSS y troubleshooting de chrome headless: engineer_visualopen_lushows.

### Plantilla mínima de HTML para entregables

```html
<!doctype html><html lang="es"><head><meta charset="utf-8">
<style>
  @page { size: A4; margin: 18mm 16mm; }
  body { font-family: system-ui, Arial, sans-serif; color:#1a1a1a; line-height:1.5; }
  h1 { font-size: 22pt; border-bottom: 3px solid #1877F2; padding-bottom:6px; }
  h2 { font-size: 14pt; margin-top: 20px; color:#1877F2; }
  table { width:100%; border-collapse: collapse; page-break-inside: avoid; }
  th,td { border:1px solid #ddd; padding:8px; text-align:left; font-size:10pt; }
  th { background:#f4f6f8; }
  .nota { font-size:9pt; color:#666; }
</style></head>
<body>
  <h1>Media Plan — [Cliente]</h1>
  <h2>Objetivo de negocio</h2>
  <p>CPA máximo: $X · MER meta: Y (derivado del margen, ver 64).</p>
  <!-- secciones según la tabla de entregables -->
  <p class="nota">Proyección con rangos y supuestos; no es promesa de ROAS.</p>
</body></html>
```

## Auditoría de cuenta ajena — el recorrido de 30 minutos

Cuando pidan "revisa mi cuenta", este es el orden (cada paso alimenta el siguiente):

1. **Account Quality** (2 min): restricciones, rechazos, feedback score, estado de verificación (ver 93). Una cuenta en riesgo invalida todo lo demás.
2. **Events Manager** (5 min): ¿píxel + CAPI vivos? ¿EMQ decente? ¿el evento de optimización es el correcto? (ver 62/14). Medición rota = nada de lo que sigue es confiable.
3. **Estructura** (5 min): # campañas/ad sets activos vs gasto total. ¿Fragmentación? ¿learning limited por todos lados? ¿solapamiento? ¿Advantage+ Sales bien configurado con cap de clientes existentes? (ver 10/13/24/90).
4. **Creativo** (8 min): # ads activos, diversidad real de ángulos (¿se colapsan en Entity ID?, ver 92), antigüedad (¿fatiga?, ver 39), ¿hay patrón de ganador identificado? (ver 68).
5. **Números contra margen** (8 min): CPA/ROAS de plataforma vs números reales del negocio (ver 64); ¿la cuenta es rentable de verdad o solo bonita en Ads Manager?
6. **Veredicto** (2 min) en formato fijo: 3 problemas priorizados por impacto + quick wins de la semana 1 + plan 30 días. Honesto: si el problema es la oferta o la operación, se dice (nivel 3).

## Las 10 reglas de oro de toda la skill

1. La oferta es el 50%: ningún creativo salva una oferta mala (ver 41).
2. El creativo es el targeting: el hook decide a quién le llega (ver 30/92).
3. La señal es el combustible: CAPI + evento correcto o estás ciego (ver 06/14).
4. Mide contra el banco, no contra la plataforma: MER y margen real mandan (ver 64).
5. Consolida: pocos ad sets con presupuesto real > muchos fragmentados (ver 10).
6. No toques por ansiedad: cambios con calendario y kill criteria, no con cortisol (ver 70/71).
7. Diversidad creativa constante: la fatiga es la única certeza; vida útil 2-4 semanas; el pipeline nunca para (ver 39/92).
8. Escala gradual: ≤20-30% cada pocos días; lo que sube de golpe se cae de golpe (ver 72).
9. Protege el activo: BM verificado, 2FA, policy limpia — sin cuenta no hay nada (ver 93).
10. La pauta amplifica, no arregla: si el negocio no da, decirlo es el trabajo (economist).

## Dónde rutea esta skill (mapa de hermanas)

- **Google** (capturar demanda, branded search, PMax, YouTube) → google_ads_lushows.
- **TikTok** (descubrimiento, Spark Ads, UGC nativo, TikTok Shop) → tiktok_ads_lushows.
- **Costo de IA/tokens** (pipelines creativos, bots, automatizaciones) → optimizer_tokens_lushows.
- **Construcción técnica** (bot WhatsApp, CAPI, webhooks, hosting, generación PDF) → engineer_visualopen_lushows.
- **Negocio** (margen, oferta, precio, viabilidad) → economist_lushows.
- **Cierre y guion de venta** (chat, objeciones, follow-up) → ventas_lushows.
- **Marca y dirección de arte** (paleta, tipografía, estilo de creativos) → directorcreativo_lushows.
- **Landing y web** (congruencia ad→landing, CRO) → desingweb-lushows.

## Errores comunes — blacklist

- Coleccionar tácticas de gurús sin sistema propio: cada update del algoritmo te deja huérfano.
- Prometer ROAS específico en un media plan: proyecta rangos con supuestos o no proyectes.
- Entregar reportes con pantallazos crudos de Ads Manager: el dueño de negocio necesita decisiones, no interfaces.
- Entregar el HTML o el MD esperando que el cliente lo procese: genera el PDF con chrome headless y entrega el PDF.
- Auditar empezando por el creativo: si la medición está rota, opinaste sobre datos falsos (el orden de los 30 min existe por algo).
- Brief creativo de una línea ("haz un video del producto"): el creator adivina y el resultado es genérico.
- Quedarse en nivel 1 para siempre: ejecutar checklists sin entender el porqué te vuelve reemplazable por el propio Advantage+.
- No documentar experimentos: sin memoria escrita, repites tests pagados y rediscutes decisiones ya tomadas (ver 17).
