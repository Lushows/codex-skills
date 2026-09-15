# 137 — Lead scoring: fit e intent

El **lead scoring** de outbound moderno combina dos preguntas en un solo número accionable: **¿esta cuenta es de las que me compran?** (fit / encaje) y **¿está en modo compra ahora?** (intent / intención). Todo el Bloque 13 alimenta este módulo: los datos (`130`), el intent (`131`, `132`), y las señales (`133`, `134`, `135`, `136`) solo valen si los **conviertes en una prioridad clara** de a quién contactar primero. Aquí armas esa fórmula. Es el cruce que `36` y `37` prometieron: **el oro está en la intersección de buen fit y alto intent**.

## El principio: fit e intent son ejes distintos, y multiplican

No los mezcles en una sola bolsa. Son dos preguntas independientes:

- **Fit (encaje):** ¿esta empresa **debería** comprarme? Es estructural y estable: tamaño, industria, tecnología, geografía (`10`, `15`, `16`). No cambia semana a semana.
- **Intent (intención):** ¿esta empresa está comprando **ahora**? Es temporal y volátil: visitó tu web (`132`), cambió de cargo (`133`), levantó ronda (`135`), postea dolores (`136`), consume tu categoría (`131`).

La clave: **no se suman, se combinan como ejes de una matriz.** Un lead con fit perfecto pero cero intent es "cultívalo/espera"; uno con intent altísimo pero mal fit es "no pierdas tiempo". El que tiene **ambos** es tu prioridad #1 absoluta.

## La matriz fit × intent (tu mapa de acción)

```
                 INTENT BAJO            INTENT ALTO
              (no busca ahora)        (busca ahora)
FIT ALTO   │  B — NUTRIR / ESPERAR │  A — CONTACTAR YA        │
(mi ICP)   │  outbound de goteo,   │  prioridad #1, cadencia  │
           │  contenido, espera    │  caliente, rápido (`147`)│
           ├───────────────────────┼──────────────────────────┤
FIT BAJO   │  D — IGNORAR          │  C — CUIDADO / DESCALIFICA│
(no ICP)   │  no gastes créditos   │  activo pero no te compra;│
           │  ni tiempo            │  revisa si tu ICP falla   │
```

- **A (fit alto + intent alto):** tu lista de oro. Todo el esfuerzo va aquí primero.
- **B (fit alto + intent bajo):** buena cuenta, mal momento. Cadencia lenta, nurture (`76`), y monitoreas señales (`133`, `135`) para que salte a A cuando aparezca el trigger.
- **C (fit bajo + intent alto):** tentador pero traicionero. Si muchos caen aquí, tu definición de ICP puede estar mal (`10`); revísalo antes de perseguirlos.
- **D (fit bajo + intent bajo):** ni los toques. Sacarlos ahorra créditos y protege tu deliverability (menos envíos a quien no responde, `45`).

## Cómo construir el score, paso a paso

1. **Puntúa el fit (0–100).** Asigna puntos por atributos de tu ICP:
   ```
   Industria objetivo ...... +30
   Tamaño en rango ......... +25
   Usa tecnología clave (`134`) +20
   Geografía objetivo ...... +15
   Cargo del contacto = decisor +10
   Atributo descalificador (ej. muy pequeño) → -50 o "fuera"
   ```
2. **Puntúa el intent (0–100) con decaimiento.** Cada señal suma, pero **pierde valor con el tiempo** (una visita web de hoy vale más que la de hace un mes):
   ```
   Visitó /precios esta semana (`132`) .... +40
   Cambio de cargo <30 días (`133`) ....... +35
   Funding <90 días (`135`) ............... +30
   Consume tu categoría / G2 (`131`) ...... +25
   Posteó dolor relevante (`136`) ......... +20
   → aplica decaimiento: -50% del valor pasados X días
   ```
3. **No los sumes en un total plano.** Ubica cada cuenta en el cuadrante (A/B/C/D) según umbrales (ej. fit ≥60 = alto, intent ≥40 = alto).
4. **Ordena la cola de trabajo por cuadrante:** A primero, luego B, C solo si sobra tiempo, D fuera.
5. **Automatiza el cálculo** donde vive tu data — Clay (`31`) o el CRM (`32`) — para que el score se recalcule solo cuando entra una señal nueva.

Para que los pesos y umbrales sean números defendibles (y no inventados), calíbralos con tus datos reales de conversión → `Matematicas_lushows`.

## Ejemplo: score en Clay para una campaña

```
Cuenta: Restaurante Brasa (Bogotá, 45 empleados, cadena)
  FIT:   industria +30, tamaño +25, geo +15, decisor identificado +10 = 80 (ALTO)
  INTENT: visitó /precios hace 3 días (`132`) +40
          gerente nuevo hace 20 días (`133`) +35, con decaimiento = 30
          → intent = 70 (ALTO)
  CUADRANTE: A → prioridad #1 → cadencia caliente + contacto en 48 h
```

## Fit e intent alimentan, pero no son el ruteo

Ojo con la frontera dentro de la skill: **este módulo arma el score** (la lógica fit × intent). **Qué se hace con el score operativamente** — a qué SDR se asigna, las reglas de routing, el reparto de la cola — es `38`. La priorización y el **tiering de cuentas** (A/B/C accounts para ABM) es `16`. La calificación conversacional (BANT/MEDDIC en la llamada) es `70`. Este módulo es el **cerebro que ordena la lista**; esos son el resto del cuerpo.

## Errores comunes

- **Sumar fit + intent en un solo total** → una cuenta con fit 90 / intent 0 y otra con fit 0 / intent 90 dan el mismo total plano, y son mundos opuestos. Usa la matriz.
- **Intent sin decaimiento** → una señal de hace 6 meses pesa igual que la de hoy y ensucia la prioridad. Aplica caducidad.
- **Perseguir el cuadrante C** → gastas en cuentas activas que no te compran; revisa tu ICP (`10`).
- **Pesos inventados** → si nunca calibraste con datos reales, el score es superstición. Ajústalo con conversión histórica (`Matematicas_lushows`).
- **Score que no se recalcula** → una cuenta que saltó de B a A por una señal nueva y tú no te enteras. Automatiza (`34`).

## Frontera y siguiente paso

El score te dice **a quién contactar primero**; la **conversación que convierte** ese contacto en venta es `ventas_lushows`. Arma tu primer scoring en Clay o tu CRM: define 4–5 atributos de fit con pesos y 3–4 señales de intent con decaimiento, y ubica cada cuenta en la matriz A/B/C/D. Trabaja A primero. Para el ruteo operativo del score → `38`; para el tiering de cuentas → `16`; para calificar en la conversación → `70`. Los datos que alimentan todo esto → `130`–`136`; mantenerlos limpios para que el score no mienta → `139`.
