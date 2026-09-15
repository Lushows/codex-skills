# 154 — Comp plans avanzados

El módulo `84` establece lo básico: pagas por reuniones **calificadas** (SQL), con estructura base + variable = OTE, split ~60/40–70/30. Este módulo va a la mecánica fina que separa un comp plan que motiva de uno que rompe: aceleradores, desaceleradores, clawbacks, comisión escalonada, SPIFs, garantías de ramp, y comp de equipo. Un comp plan avanzado no es más complejo por gusto —cada pieza corrige un comportamiento específico. La parte legal, prestacional y de nómina es de `contador_lushows`; el cálculo exacto de cada escenario de pago → `Matematicas_lushows`. Aquí va la lógica de diseño.

## El principio: cada regla del comp corrige una conducta

El SDR optimiza para lo que le pagas (ver `84`). Un comp plan avanzado usa reglas para empujar conductas concretas:

| La regla... | ...corrige la conducta de... |
|---|---|
| Comisión por **SQL** (no por meeting) | agendar con cualquiera para hacer número |
| **Clawback** | inflar reuniones que resultan basura o no-show |
| **Acelerador** | frenar en cuota (el clásico "ya llegué, relajo") |
| **Desacelerador / piso** | ignorar la calidad por perseguir volumen |
| **Bono por deal cerrado** | agendar SQL que encajan de verdad (calidad) |
| **Garantía de ramp** | castigar al nuevo por no producir aún (ver `86`) |

Regla de oro: **el plan debe caber en una servilleta.** Si el SDR no puede calcular cuánto ganó esta semana, el plan no motiva —confunde. Complejidad sí, pero legible.

## Aceleradores: por qué son la pieza más rentable

Un **acelerador** aumenta la comisión por unidad *después* de cumplir la cuota. Es contraintuitivo pagar más por lo mismo, pero es lo más rentable que puedes hacer:

- Sin acelerador, el SDR que llega a cuota el día 20 del mes **para** —no gana igual por seguir—. Pierdes su mejor semana.
- Con acelerador, cada SQL por encima de la cuota paga más → el buen SDR sigue empujando y sobreproduce.

```
Ejemplo de comisión escalonada (SDR local LatAm, ver rangos base en 84):
  0–100% de cuota:     $25 por SQL
  101–130% de cuota:   $35 por SQL   (acelerador ×1.4)
  >130% de cuota:      $50 por SQL   (acelerador ×2.0)

El costo del acelerador SIEMPRE se paga con la sobreproducción que genera:
cada SQL extra ya te trajo pipeline; pagas más de un pastel más grande.
```

## Clawback y desacelerador: proteger la calidad

- **Clawback (devolución):** si una reunión marcada SQL resulta basura, no-show recurrente o el AE la rebota por no encajar, **no cuenta** (y si ya se pagó, se descuenta del siguiente periodo). Sin clawback, el SDR aprende a inflar. La definición de qué "no cuenta" debe estar escrita y acordada con el AE (ver `78`).
- **Pago partido:** una técnica limpia es pagar **50% al agendar y 50% cuando el AE acepta el SQL** como válido. El SDR cobra algo rápido (motiva) pero solo cobra completo si era real (protege calidad). Más simple que un clawback y menos conflictivo.
- **Piso de calidad (gate):** el variable solo se libera si la **tasa de aceptación del AE** (% de SQL que el AE acepta) supera un umbral (ej. 70%). Si el SDR agenda mucho pero el AE rechaza la mitad, no cobra pleno. Alinea cantidad con calidad de un solo golpe.

## Bono por conversión: alinear al SDR con el dinero real

El SDR no controla el cierre (lo hace el AE, ver `81`), así que no le pagues por revenue —lo desmotivas. Pero sí puedes premiar la **calidad** con un bono cuando su SQL se convierte en cliente:

```
Bono por deal cerrado originado por el SDR:  bono FIJO por cierre (ej. $50–200),
NO un % del deal.
Por qué fijo y no %:  el SDR no negoció el precio ni cerró; premias que ELIGIÓ
bien la cuenta, no el tamaño del deal (que no controla).
```

Esto hace que el SDR prefiera agendar 10 SQL que encajan sobre 20 que no. La conversación de cierre que convierte ese SQL en venta es del AE → `ventas_lushows`.

## Garantía de ramp: no castigues al nuevo

Durante el ramp (meses 1–3, ver `86`) el SDR no produce a cuota plena, así que no puedes exigir cuota plena y pagar solo por ella. Dos formas:

- **Variable garantizado decreciente:** mes 1 pagas ~80% del variable objetivo garantizado, mes 2 ~50%, mes 3 ya a resultados. Le da colchón mientras aprende.
- **Cuota rampada:** el 100% del variable se calcula contra la cuota *rampada* de ese mes (25% / 60% / 100%, ver `86`), no contra la plena.

La segunda es más limpia porque paga por resultado real desde el inicio, solo que contra una meta justa.

## Ejemplo completo (SDR con experiencia, mercado local LatAm)

Órdenes de magnitud 2026, en USD/mes de referencia. **El neto con prestaciones y retenciones → `contador_lushows`; cualquier escenario numérico exacto → `Matematicas_lushows`.**

```
OTE objetivo:        $1.500/mes
  Base (fija):       $1.000   (67%)
  Variable a cuota:  $500     (33%)  → a 20 SQL/mes de cuota = $25/SQL

Reglas:
  Pago partido:      $12.5 al agendar + $12.5 al aceptar el AE
  Acelerador:        SQL 21–26 → $35 c/u · SQL 27+ → $50 c/u
  Gate de calidad:   variable pleno solo si aceptación del AE ≥ 70%
  Bono conversión:   +$100 por cada SQL que cierra como cliente
  Ramp:              cuota rampada 25%/60%/100% en meses 1/2/3 (86)
  Referido:          +$300 si un SDR que refirió sigue a los 90 días (151, 159)
```

## SPIFs y comp de equipo (con cuidado)

- **SPIF (Sales Performance Incentive Fund):** un bono *temporal* por un empujón puntual ("esta semana, $10 extra por reunión con cuentas del sector salud"). Útil para desatascar un foco; peligroso si es permanente (se vuelve salario esperado). Úsalo corto y con objetivo claro (más en gamificación, ver `158`).
- **Componente de equipo:** un % pequeño del variable ligado a la meta del pod (ver `150`). Fomenta que se ayuden y compartan swipe (ver `157`). Manténlo chico (≤15% del variable): si es grande, el buen SDR carga al flojo y se desmotiva.

## Errores comunes

- **Plan que no cabe en una servilleta.** Si el SDR no puede calcular su pago, no lo motiva.
- **Sin acelerador.** El buen SDR frena al llegar a cuota; pierdes su mejor producción.
- **Sin clawback ni gate.** El SDR infla reuniones basura; el AE deja de confiar (ver `78`).
- **Pagar % del deal al SDR.** Premias algo que no controla (el tamaño) y no lo que sí (elegir bien).
- **Cuota plena en el ramp sin garantía.** Quema al nuevo bueno (ver `86`).
- **Componente de equipo grande.** El fuerte carga al débil y se va (ver `159`).
- **Cambiar el plan cada mes.** Mata la confianza; el SDR necesita estabilidad para planear.

## Siguiente paso

Diseña tu plan con base + variable (empieza 70/30), agrega **acelerador** y **gate de calidad o pago partido** desde el inicio, y garantía de ramp para los nuevos. Escribe la definición de SQL con el AE (`78`) o discutirás cada reunión. Fija la cuota que ancla todo esto → `155`. Para el costo real del contrato con prestaciones → `contador_lushows`; para simular cuánto paga el plan en cada escenario → `Matematicas_lushows`; para si el costo cabe en tus unit economics → `economist_lushows` y el cost-per-meeting en `80`.
