# 82 — Forecasting desde el outbound

Forecasting es proyectar cuánto pipeline y cuánto revenue vas a generar en las próximas semanas/meses **a partir de tu actividad de outbound de hoy**. Es lo que convierte el outbound de "a ver qué cae" a un motor con panel de control: si conoces tus ratios (ver `81`) y tu actividad, puedes decir con confianza razonable "en 90 días esto genera X reuniones y ~$Y en negocio". Sirve para dos cosas: **planear** (¿cuánta actividad necesito para llegar a la meta?) y **detectar problemas temprano** (si la actividad de hoy no alcanza, lo sabes hoy, no en 3 meses). Este módulo te da los dos métodos —hacia adelante y hacia atrás— y cómo manejar el desfase temporal.

## El principio: el pipeline es actividad con retraso

Todo forecast de outbound se apoya en una idea: **la actividad de hoy se convierte en revenue dentro de N días**, donde N es la suma de tus tiempos de ciclo. La reunión que agendas hoy no es dinero hoy; es dinero cuando el AE la trabaje y cierre. Si ignoras ese retraso, tu forecast es fantasía.

```
Actividad (hoy) → Reunión (días) → SQL (días) → Cierre (semanas) = Revenue (mes+2, mes+3…)
```

Por eso el forecast de outbound tiene **dos velocidades**:
- **Lo que el SDR controla y predice rápido:** reuniones y SQL. Estas responden a la actividad en días/semanas.
- **Lo que depende del AE y tarda:** deals cerrados. Esto es más trabajo de `ventas_lushows` (gestión de pipeline y probabilidad de cierre por etapa).

Un SDR/solista responsable forecast-ea con seguridad hasta SQL, y **estima** el revenue aplicando la tasa de cierre histórica, dejando claro que esa última parte es del vendedor.

## Método 1 — Hacia adelante (desde la actividad)

Empiezas con la actividad que estás corriendo y multiplicas por tus ratios para ver qué sale.

```
Actividad planeada:   1.500 contactos tocados este mes
× 5%   reply           →   75 respuestas
× 32%  positivas       →   24 positivas
× 50%  agendan         →   12 reuniones agendadas
× 80%  se presentan    →  9.6 reuniones realizadas
× 65%  califican       →  6.2 SQL
× 30%  cierran (AE)    →  1.9 clientes
× $1.500 margen/cliente → ~$2.800 en margen proyectado
```

Úsalo para responder "si sigo a este ritmo, ¿a dónde llego?". Si el resultado no alcanza la meta, subes el input (más contactos, ver `29`) o mejoras un ratio (ver `83`).

## Método 2 — Hacia atrás (desde la meta)

Empiezas con la meta de revenue y divides por los ratios para ver cuánta actividad necesitas. Es el embudo invertido de `81`, llevado a plan de trabajo:

```
Meta:              $6.000 margen/mes
÷ $1.500/cliente   →  4 clientes
÷ 30% cierre       →  13.3 SQL
÷ 65% calif.       →  20.5 realizadas
÷ 80% show         →  25.6 agendadas
÷ 50% agenda       →  51.2 positivas
÷ 32% positiva     →  160 respuestas
÷ 5% reply         →  ~3.200 contactos/mes  ≈ 160/día hábil
```

Ahora sabes exactamente cuánta lista construir y cuántos buzones necesitas (a ~30 correos/buzón/día seguros → ~5–6 buzones activos si es solo email; ver `44`). **Corre estas divisiones en `Matematicas_lushows` para que el redondeo no te deje corto.**

## El desfase temporal: el forecast por cohorte

El error más común es esperar que el revenue del mes venga de la actividad *del mismo mes*. No: viene de la actividad de meses anteriores. Piénsalo por **cohortes** (grupos de contactos según cuándo entraron):

| Mes | Contactos tocados | Reuniones (mismo mes) | SQL (mes+0/+1) | Cierres (mes+1/+2) |
|---|---|---|---|---|
| Enero | 1.500 | 12 | 6 | — |
| Febrero | 1.500 | 12 | 6 | 2 (de enero) |
| Marzo | 1.500 | 12 | 6 | 2 (de febrero) |

Regla práctica: **si tu ciclo de venta es de ~45 días, el revenue de marzo lo determinaste en enero–febrero.** Por eso no puedes "apretar" el pipeline el último día del mes: la palanca es la actividad de hace 1–2 meses. Esto también significa que **una caída de actividad hoy es un hueco de revenue garantizado dentro de 60 días** — la razón #1 para no dejar que el pipeline se seque cuando estás ocupado cerrando (el clásico "feast and famine").

## Niveles de confianza (no todo el forecast pesa igual)

Reporta el forecast en tres capas, de más firme a más especulativo:

- **Comprometido:** reuniones ya agendadas en calendario. Casi seguro (descuenta ~20% no-show).
- **Probable:** SQL en el pipeline del AE con siguiente paso definido. Aplica tasa de cierre histórica.
- **Proyectado:** lo que la actividad *en curso* va a generar según ratios. El más blando; úsalo para planear, no para prometer.

Nunca sumes los tres como si fueran lo mismo. La gestión fina de probabilidad por etapa del deal (weighted pipeline) es trabajo de vendedor → `ventas_lushows`.

## Ejemplo de reporte de forecast (solista, LatAm)

```
FORECAST — cierre estimado próximos 60 días
  Comprometido (reuniones en calendario):   9 held esperadas → ~4 SQL
  Probable (SQL en pipeline del AE):         5 SQL × 30% →  1.5 cierres
  Proyectado (actividad en curso):           1.500 contactos → ~6 SQL → ~1.8 cierres
  ─────────────────────────────────────────
  Revenue estimado (margen):   ~$3.300–$5.000  (rango, no punto)
  Riesgo principal: bounce rate subió a 4% → menos entregas → menos reply (ver 83)
```

Siempre da **rango, no número mágico**, y nombra el riesgo principal. Un forecast honesto con rango vale más que uno preciso y falso.

## Errores comunes

- **Forecast-ear con ratios inventados.** Sin datos propios, usa los benchmarks de `81` pero márcalos como supuestos y corrígelos al mes 1.
- **Ignorar el desfase.** Prometer revenue este mes desde actividad de este mes.
- **Sumar comprometido + proyectado como si fueran iguales.** Infla el forecast y quemas tu credibilidad.
- **Olvidar el no-show.** Descuenta siempre held/booked (~80%).
- **Forecast-ear cierres como si el SDR los controlara.** El SDR forecast-ea hasta SQL; el cierre es del AE (`ventas_lushows`).

## Siguiente paso

Toma tus ratios reales (`81`) y arma tu forecast hacia atrás desde tu meta de revenue: sabrás cuánta actividad diaria necesitas. Si el número da imposible para una persona, es señal de que toca escalar el equipo (ver `89`). Para que los cálculos sean exactos → `Matematicas_lushows`; para conectar el forecast con el modelo financiero del negocio → `economist_lushows`.
