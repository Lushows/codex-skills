# 84 — Compensación y cuota del SDR

Cómo le pagas a un SDR determina qué hace. Si le pagas por correos enviados, vas a tener toneladas de correos basura. Si le pagas por reuniones agendadas sin más, vas a tener reuniones falsas con quien sea para hacer el número. Si le pagas por **reuniones calificadas** (que el vendedor acepta como oportunidades reales), alineas el incentivo con el negocio. Este módulo cubre cómo estructurar el paquete —base + variable, OTE, la cuota— y por qué la métrica que premias es la decisión más importante que tomas. Los cálculos exactos de nómina y la parte legal/prestacional son de `contador_lushows`; aquí va la lógica del diseño.

## El principio: pagas por el output correcto, no por el esfuerzo

El SDR está en una posición peligrosa: su actividad (correos, llamadas) es fácil de inflar, y su resultado final (revenue) no lo controla (lo cierra el AE, ver `81`). La compensación tiene que caer en el punto medio correcto:

- **Muy arriba en el embudo** (pagar por actividad) → el SDR optimiza volumen basura.
- **Muy abajo** (pagar por revenue cerrado) → castigas al SDR por algo que no controla; se desmotiva.
- **En el punto justo** → pagar por **reuniones realizadas y calificadas (SQL)**. Es lo más abajo que el SDR sí controla con su trabajo (a quién elige, cómo califica), y lo más cerca del dinero.

**Regla:** la métrica principal de comp del SDR es **SQL / oportunidades aceptadas por el AE**, no meetings booked. ¿Por qué? Porque "booked" premia agendar con cualquiera; "SQL" premia agendar con quien *encaja* (ver `78`, `73`). Esto obliga al SDR a calificar de verdad y protege al vendedor de perder tiempo.

## La estructura: base + variable = OTE

- **Base:** sueldo fijo, se paga siempre. Da estabilidad y permite exigir estándares de proceso (actividad, calidad).
- **Variable (comisión/bono):** ligada al desempeño (SQL, a veces con acelerador por deals cerrados que vinieron del SDR).
- **OTE (On-Target Earnings):** lo que gana en total **si cumple el 100% de su cuota**. Es la cifra que le prometes al contratar. OTE = base + variable a cuota.

El split típico en SDR es **~60/40 o 70/30** (base/variable). Más peso en base que un AE (que suele ser 50/50), porque el SDR controla menos del resultado final. Un split muy agresivo (50/50) en SDR genera ansiedad y rotación sin mejorar resultados.

```
Ejemplo de estructura (SDR):
  OTE:       100%
  Base:       70%  (fijo, siempre)
  Variable:   30%  (a cuota de SQL)
```

## La cuota (quota): cómo fijarla

La cuota es el número de SQL/mes que el SDR debe producir para ganar el 100% de su variable. Se fija **desde la capacidad y desde la necesidad del negocio**, y debe ser **alcanzable por un buen SDR con esfuerzo** (típicamente ~70–80% del equipo la alcanza; si nadie la alcanza, está mal fijada y quema gente).

Para fijarla, usa el embudo (ver `81`) y la capacidad diaria:

```
Capacidad:   ~80–120 toques de calidad/día → ~1.500–2.000 contactos/mes
Ratio a SQL: ~1–2% (81)
→ Cuota realista:  ~15–30 SQL/mes por SDR maduro (post-ramp)
```

Durante el ramp (los primeros 2–3 meses) la cuota es **rampada** (más baja), no la plena — un SDR nuevo no produce como uno maduro (ver `86`). Fijar la cuota plena desde el día 1 es la forma más rápida de quemar a alguien bueno.

## Ejemplos de paquete en LatAm (órdenes de magnitud 2026)

Rangos aproximados, varían mucho por país, industria y si es venta local o a mercado USA (vender a USA paga bastante más). Cifras en USD/mes de referencia; **para el cálculo neto con prestaciones y retenciones usa `contador_lushows`.**

| Perfil | Base/mes | Variable a cuota | OTE/mes | Comisión típica |
|---|---|---|---|---|
| **SDR junior, mercado local LatAm** | $500–800 | $200–350 | $700–1.150 | ~$15–25 por SQL |
| **SDR con experiencia, local** | $800–1.200 | $350–600 | $1.150–1.800 | ~$25–40 por SQL |
| **SDR vendiendo a USA/EU (inglés, remoto)** | $1.200–2.000 | $600–1.200 | $1.800–3.200 | ~$40–80 por SQL + acelerador |

Notas de diseño:
- **Comisión por SQL** (reunión calificada aceptada) es lo más común y limpio. A veces se paga la mitad al agendar y la otra mitad cuando el AE la califica —así el SDR cobra algo rápido pero solo cobra completo si era real.
- **Acelerador** (bono extra) cuando un SQL del SDR se convierte en cliente: alinea al SDR con calidad, no solo cantidad. Suele ser un bono fijo por cierre (ej. $50–200) más que un % del deal.
- **Clawback** (devolución): si una reunión se marca SQL y resulta basura o no-show recurrente, no cuenta. Evita el juego de inflar.

## Por qué pagar por reuniones CALIFICADAS (no solo agendadas)

Es la decisión de diseño más importante. Compara:

| Si pagas por... | El SDR aprende a... | Resultado |
|---|---|---|
| Correos enviados | Mandar más basura | Deliverability quemada, cero reuniones (ver `40`) |
| Reuniones agendadas | Agendar con cualquiera para hacer número | AE pierde tiempo, deja de confiar, forecast sucio |
| **Reuniones calificadas (SQL)** | **Elegir bien y calificar duro** | Menos reuniones pero reales; AE feliz; pipeline limpio |

El SDR siempre optimiza para lo que le pagas. Págale por calidad y tendrás calidad. La definición exacta de qué cuenta como SQL debe estar **escrita y acordada con el AE** (ver `78`), o vas a discutir cada reunión.

## Errores comunes

- **Pagar por actividad.** Genera basura garantizada.
- **Cuota plena desde el día 1.** Quema al nuevo antes del ramp (ver `86`).
- **SQL sin definición escrita.** Fuente eterna de conflicto SDR↔AE. Define y acuerda el criterio.
- **Variable muy agresivo (50/50) en SDR.** Ansiedad y rotación sin ganancia.
- **Sin clawback ni acelerador.** El primero evita inflar; el segundo premia calidad.
- **Ignorar lo legal/prestacional.** El "cuánto le pago" bruto no es lo que cuesta ni lo que recibe → `contador_lushows`.

## Siguiente paso

Define tu OTE objetivo, elige el split (empieza 70/30), fija la cuota desde tu embudo (`81`) con ramp los primeros meses (`86`), y **escribe la definición de SQL con el AE** (`78`). Para calcular el costo real del contrato con prestaciones y el neto del SDR → `contador_lushows`; para saber si ese costo cabe en tus unit economics → `economist_lushows` y el cost per meeting en `80`.
