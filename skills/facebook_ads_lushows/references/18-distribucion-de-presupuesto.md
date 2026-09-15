# 18 — Distribución de presupuesto

Cuánta plata va a cada cosa. Lee este módulo cuando definas (o redefinas) tu presupuesto mensual de pauta, cuando no sepas si "te alcanza" para retargeting, o cuando tengas la plata regada en 8 campañas sin lógica.

## Regla base de reparto

```
PROSPECTING (gente nueva)         70-80%   ← el motor del crecimiento
RETARGETING (gente que ya te vio) 10-20%   ← el cierre
TESTING (creativos/ofertas nuevas) ~10%    ← el seguro de vida
```

Ajustes por madurez:
- **Cuenta nueva** (primeros 1-2 meses): testing sube a 20-30% — todavía no sabes qué funciona; tu "prospecting" ES el test.
- **E-com con tráfico web alto**: retargeting puede pesar más (hasta 25%)... con cuidado: el retargeting se auto-atribuye ventas de gente que iba a comprar igual (ver 24 y 16). Si retargeting es 40% de tu presupuesto, no estás escalando: estás cosechando el mismo huerto cada vez más chico.
- **Cuenta micro** (< ~$1.5M COP/mes): NO repartas. 100% a una sola campaña de prospecting broad; el testing pasa adentro rotando creativos (ver 10). Retargeting con 200 visitantes al mes no tiene audiencia que perseguir.

## Antes de repartir: ¿cuánto presupuesto necesitas siquiera?

El presupuesto no es un capricho, es una consecuencia del CPA. Para que UN ad set tenga oportunidad de aprender necesita acercarse a 50 conversiones/semana (ver 13). Cuenta mínima:

```
Presupuesto mínimo viable/mes ≈ CPA esperado × 50 conv × 4 semanas
Ej (CPA $30.000): 30.000 × 50 × 4 = $6.000.000/mes para que UN ad set salga de aprendizaje
```

Si no llegas a eso, **no significa que no pautes**: significa que vivirás en learning limited rentable (ver 13) y debes consolidar todo en un solo ad set. La plata define cuántas "cubetas" puedes alimentar, no si juegas o no.

## Diario vs lifetime

- **Presupuesto diario** (default y recomendado): gasta ~X cada día (Meta puede flexionar hasta +75% un día y compensar en la semana). Predecible, fácil de escalar.
- **Lifetime** (total para un rango de fechas): Meta decide el ritmo día a día. Útil SOLO para campañas con fecha de fin real — eventos, lanzamientos, fechas comerciales (ver 98 y 19). Permite además programar horarios (dayparting), que el diario no.

## Mínimos para que algo aprenda

- Por ad set: mínimo **2-3× tu CPA esperado por día** para tener oportunidad de aprender; idealmente lo que te acerque a 50 conversiones/semana (ver 13). Con CPA de $30.000 COP, eso es ≥$60-90k/día por ad set.
- Si tu presupuesto no da para que DOS ad sets cumplan el mínimo, ten UNO. La matemática es brutal pero simple: mejor un ad set bien alimentado que tres anémicos.
- Por ad: dentro del ad set, Meta reparte solo. No hay mínimo por anuncio, pero con presupuesto chico no metas 10 ads (3-5 máximo o ninguno recibirá señal). Con presupuesto grande sí quieres 10-15 creativos distintos (ver 30).

## Mover plata sin romper nada

- **Dentro de una campaña CBO** (Advantage+ campaign budget): Meta ya mueve el presupuesto entre ad sets solo; no necesitas (ni debes) microgestionarlo.
- **Entre campañas**: mueve gradual — baja una 20%, sube la otra 20%, espera 72h (cambios >20% resetean aprendizaje, regla endurecida 2026, ver 13). No "apago esta y le paso toda la plata a aquella" en un día.
- **Escalar el total**: +20% cada 72h sobre la campaña ganadora (playbook completo en 72).

## Ejemplos numéricos (COP, mensual)

**$500.000 COP/mes (≈ $17k/día)** — micro:
```
1 campaña prospecting broad (CBO, 1 ad set, 4-5 ads) ... $17.000/día (100%)
Testing = rotación de creativos dentro de la misma campaña
Retargeting = $0 (no hay volumen; el "retargeting" es responder WhatsApp rápido, ver 50)
```

**$3.000.000 COP/mes (≈ $100k/día)** — media:
```
Prospecting (CBO, broad, 8-10 ads) ......... $70.000/día (70%)
Retargeting (ABO: web+IG 30d, 3 ads) ....... $15.000/día (15%)
Testing (ABO, 2-3 ads nuevos rotando) ...... $15.000/día (15%)
```

**$15.000.000 COP/mes (≈ $500k/día)** — grande:
```
Advantage+ Sales principal (15-20 creativos) ... $300.000/día (60%)
Prospecting manual broad (comparativa) ......... $75.000/día (15%)
Retargeting estructurado (ver 24) .............. $60.000/día (12%)
Testing dedicado (pipeline, ver 17) ............ $65.000/día (13%)
```
Los porcentajes son punto de partida, no ley: revisa CPA por capa cada semana contra backend (ver 16) y reasigna gradual.

## Reserva estacional: presupuesta el año, no el mes

En Colombia el costo de pautar sube fuerte en Q4 y en Día de la Madre (CPMs +30-80%, ver 19). Si presupuestas mes a mes plano, llegas a noviembre sin caja para el pico más rentable del año. Aparta desde mediados de año un **fondo de Q4** (un 20-30% extra sobre tu mensual base para oct-dic). Mismo principio para mayo (Madres) y septiembre (Amor y Amistad). El calendario completo está en 19; la viabilidad de cargar caja para esos picos: economist_lushows.

## No olvides el IVA y las comisiones (Colombia)

Tu "$3M de pauta" NO son $3M de caja. Si facturas con NIT, Meta carga **IVA 19%** → ~$3.57M reales. Súmale comisión de pasarela/tarjeta si pagas con crédito y la TRM si tu tope está en USD. Presupuesta sobre la caja real, no sobre el número de Ads Manager (detalles fiscales y de flujo de caja: economist_lushows).

## Errores comunes — blacklist

- Repartir $500k COP/mes entre 4 campañas "para diversificar": cuatro campañas muertas de hambre.
- Retargeting comiéndose 40%+ del presupuesto porque "su ROAS es mejor": es mejor porque cosecha lo que prospecting siembra; mata prospecting y en 4 semanas el retargeting no tiene a quién perseguir.
- Presupuesto lifetime en campañas evergreen (sin fecha fin): pierdes control del ritmo sin ganar nada.
- Duplicar el presupuesto un día bueno: reseteo de aprendizaje + resaca de CPA (ver 13).
- Sacar el testing del presupuesto "este mes que está apretado": en 6-8 semanas tus creativos fatigan y no hay reemplazo listo; el ahorro de hoy es la crisis de agosto (ver 39).
- No apartar fondo de Q4 desde mitad de año: ver pasar el pico desde la ventana.
- No apartar IVA y comisiones al presupuestar: presupuestas $3M y la caja te exige $3.57M.
