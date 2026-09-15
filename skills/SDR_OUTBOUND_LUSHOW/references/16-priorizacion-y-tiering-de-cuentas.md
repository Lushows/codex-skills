# 16 — Priorización y tiering de cuentas (dónde va tu mejor tiempo)

No todas las cuentas de tu lista merecen el mismo esfuerzo. Tu tiempo es finito y tu deliverability es un recurso escaso (ver `44`): gastarlo por igual en una cuenta soñada y en una mediocre es un error de asignación. **Tiering** es partir tu lista en niveles (A/B/C) según qué tanto encajan, y darle a cada nivel el nivel de esfuerzo que corresponde. La regla: **investigación profunda y multicanal para las Tier A; volumen eficiente y automatizado para las Tier C.** Así concentras tu mejor energía donde está el mayor retorno.

## El principio: encaje ≠ binario

El ICP (`10`) no es un "sí/no": es un **gradiente**. Unas cuentas cumplen todos tus criterios y activaron una señal (`14`); otras cumplen a medias. El **ICP fit score** convierte ese gradiente en un número (0–100) que ordena tu lista. Con ese orden, decides dónde poner el esfuerzo caro (personalización 1:1, llamada, LinkedIn, video) y dónde el barato (secuencia semi-personalizada a volumen). Sin tiering, o personalizas todo (no escala) o nada (no convierte); el tiering resuelve ese trade-off (ver `66`).

## Los tres tiers

| Tier | Qué es | Cuántas | Nivel de esfuerzo | Canales |
|---|---|---|---|---|
| **A** — cuentas soñadas | Encaje perfecto + señal activa + ticket alto | Pocas (10–50) | 1:1 profundo, research manual, video, multi-threading | Email + LinkedIn + llamada + WhatsApp |
| **B** — buen encaje | Cumplen ICP, sin señal fuerte todavía | Medias (cientos) | Semi-personalizado (1:few), 1 línea investigada | Email + LinkedIn |
| **C** — encaje aceptable | Cumplen filtros mínimos; volumen | Muchas (miles) | Automatizado a escala, personalización ligera con variables | Email (secuencia) |

En **ABM/enterprise** las Tier A son el juego entero (ver `160`–`165`). En **pyme LatAm de ticket bajo** el peso está en B/C con automatización eficiente (ver `93`). Tu mezcla depende de tu ticket: **entre más caro el cliente, más cuentas Tier A y más esfuerzo por cuenta se justifica.**

## Cómo calcular el ICP fit score (paso a paso)

1. **Elige 4–6 criterios** que predicen encaje (de tu ICP): sector exacto, tamaño ideal, tecnología, geografía, señal activa, prueba social en el nicho.
2. **Asigna peso** a cada uno (los que más predicen cierre, más peso).
3. **Puntúa cada cuenta** (herramientas como Clay, `31`/`101`, automatizan esto; a mano en una hoja también sirve).
4. **Ordena y corta:** define los umbrales A/B/C (ej. ≥80 = A, 50–79 = B, 30–49 = C, <30 = fuera).
5. **Suma la capa de intent:** una cuenta B que activó una señal (`14`) **sube a A temporalmente** mientras dure la ventana.

## Ejemplo de scoring (fit + intent)

```
Criterio (peso)              Cuenta X   Cuenta Y
Sector exacto (25)             25         25
Tamaño ideal 5–40 (20)         20          5   (Y tiene 200 empl.)
Ciudad objetivo (15)           15         15
Usa tecnología señal (15)      15          0
Tengo caso en su nicho (15)    15         15
Señal activa/trigger (10)      10          0
----------------------------------------------
FIT SCORE                     100         60
TIER                           A           B
Esfuerzo                    1:1 + call   secuencia semi-personal
```

⚠️ Si armas un modelo de scoring con pesos y muchos criterios y quieres que los cálculos y umbrales sean **exactos** (o ponderaciones normalizadas), ejecútalo/verifícalo con **`Matematicas_lushows`**. Aquí damos el método; el número fino se calcula.

## Cómo repartir tu tiempo (la regla operativa)

Una asignación sana para un SDR solista con lista mixta:

- **Tier A (~10% de cuentas):** ~40% de tu tiempo. Research real, mensaje único, multicanal, seguimiento tenaz. Aquí no automatizas casi nada.
- **Tier B (~30%):** ~40% del tiempo. Plantilla con una línea investigada por cuenta; secuencia email+LinkedIn.
- **Tier C (~60%):** ~20% del tiempo. Secuencia automatizada con variables (`{empresa}`, `{ciudad}`), personalización ligera. Es tu red de arrastre.

La lógica: las pocas Tier A justifican esfuerzo caro porque cada cierre vale mucho; las muchas Tier C se trabajan baratas porque el retorno por cuenta es bajo pero el volumen compensa.

## Dónde vive el tiering en tu operación

- **En el CRM/lista:** un campo `Tier` y un campo `fit_score` por cuenta (ver higiene en `77`, arquitectura CRM en `141`).
- **En las secuencias:** una secuencia por tier (la de A es multicanal manual; la de C es automatizada — ver `60`, `61`).
- **En tu día:** bloquea tiempo separado para A (research + toques manuales) y para C (batch de secuencia) — ver `67`.

## Errores comunes

- **Tratar todo como Tier A:** te ahogas personalizando y nunca alcanzas volumen.
- **Tratar todo como Tier C:** automatizas hasta tus cuentas soñadas y las quemas con un correo genérico.
- **Fit score sin intent:** ignoras el timing; una cuenta B con señal activa vale más hoy que una A dormida.
- **No re-priorizar:** el tier es dinámico; una cuenta sube o baja con nuevas señales.
- **Sobre-optimizar el modelo de scoring** en vez de empezar simple (4 criterios) y afinarlo con resultados (`79`).

## Frontera y siguiente paso

El **lead scoring automatizado y el routing** (puntuar y enrutar leads con reglas/herramientas) está en `38` y `137`. El **ABM puro** (cuando casi todo es Tier A) en `160`. Cálculos exactos → **`Matematicas_lushows`**.

**Siguiente paso:** toma tu lista, define 4–6 criterios de fit con pesos, puntúa y córtala en A/B/C. Asigna a cada tier su secuencia (`60`) y su presupuesto de tiempo. Antes, confirma que tu lista es del tamaño correcto en `17`.
