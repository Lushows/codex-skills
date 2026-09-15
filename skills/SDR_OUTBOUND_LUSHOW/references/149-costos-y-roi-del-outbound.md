# 149 — Costos y ROI del outbound

Todo lo que montaste en este bloque —el stack, la automatización, el equipo— cuesta dinero, y este módulo cierra el círculo: **¿cuánto te cuesta conseguir un cliente por outbound (el CAC) y rinde de verdad tu stack?**. Sin este número, el outbound es un acto de fe: gastas en herramientas y tiempo sin saber si sales ganando. Con él, tomas decisiones frías —qué herramienta cortar, si contratar otro SDR, si el canal cierra o no—. Aquí ves cómo sumar todos los costos, cómo calcular el CAC y el ROI del outbound, y un ejemplo completo. **Todo número exacto se ejecuta en `Matematicas_lushows`; la decisión estratégica que sale de ahí es `economist_lushows`.**

## El principio: cuenta TODOS los costos, o el CAC te mentirá barato

El error universal es contar solo lo obvio (la suscripción de Apollo) y olvidar lo caro (tu tiempo, o el sueldo del SDR). Un CAC que ignora el costo humano parece hermoso y es falso —y te lleva a escalar algo que en realidad pierde plata. El CAC honesto suma **tres familias de costo**: herramientas, personas y datos/infraestructura. Si un costo existe para que el outbound ocurra, entra en la cuenta.

## Las tres familias de costo del outbound

```
① HERRAMIENTAS (stack)
   Sourcing (Apollo/Clay) · Sequencer (Instantly/Smartlead) · CRM (HubSpot)
   Verificación (NeverBounce) · Pegamento (Make/n8n) · Señales (opcional)
   → rango solista/agencia chica 2026: ~$200–600/mes todo junto

② PERSONAS (el más caro, el más olvidado)
   Sueldo del SDR + carga (o TU tiempo valorado por hora si eres solista)
   Comisión/bono por reunión o SQL (ver 84)
   → un SDR en LatAm: rango amplio según país; TU hora tiene precio también

③ DATOS E INFRAESTRUCTURA
   Dominios secundarios + buzones (ver 41, 44) · warmup (43)
   Números de teléfono/WhatsApp (47) · créditos de enriquecimiento
   → ~$50–200/mes según volumen de buzones y dominios
```

La familia ② casi siempre es **el 60–80% del costo total**. Un stack de $400/mes con un SDR detrás cuesta muchísimo más que $400. Ignorar el costo humano es cómo la gente cree que su outbound es rentable cuando no lo es.

## El cálculo: de costo total a CAC

```
CAC outbound = Costo total del outbound (periodo)  ÷  Clientes ganados por outbound (periodo)
```

Dos precisiones que separan el CAC serio del ingenuo:
- **Atribuye bien el denominador.** Solo cuentas los clientes que el outbound generó (usa `sql_source`, ver `143`). Si un cliente vino de un ad y tú solo lo tocaste, es CAC compartido, no todo tuyo.
- **Compara CAC contra LTV, no contra el precio.** El CAC solo tiene sentido frente a cuánto vale un cliente en el tiempo (LTV: valor de vida del cliente). La regla sana de referencia es **LTV:CAC ≥ 3:1**; por debajo, el motor no rinde. El análisis LTV:CAC completo es de negocio → `economist_lushows`.

## El ROI del stack: ¿cada herramienta se paga sola?

El ROI (retorno de la inversión) del outbound pregunta si el margen generado supera lo invertido:

```
ROI outbound = (Margen generado por outbound − Costo total outbound) ÷ Costo total outbound
```

Y a nivel de herramienta, la pregunta afilada: *"¿esta herramienta genera (o ahorra) más de lo que cuesta?"*. Clay a $150/mes que te ahorra 20 horas de investigación y sube el reply rate 1 punto, se paga solo; una herramienta de señales de $300/mes que no mueve ninguna métrica, se corta. Revisa el stack cada trimestre con esta lupa (ver `146` para el mapa).

## Ejemplo de cálculo (solista/agencia chica, LatAm, cifras de muestra)

```
PERIODO: 1 mes
COSTOS
  ① Herramientas:  Apollo $99 + Instantly $97 + HubSpot $0(free) +
                   NeverBounce $50 + Make $16                    = $262
  ② Personas:      TU tiempo: 80 h × $15/h (costo de oportunidad) = $1.200
  ③ Datos/infra:   3 dominios+9 buzones ~$60 + warmup $30         = $90
  ─────────────────────────────────────────────────────────────
  COSTO TOTAL DEL MES                                            = $1.552

RESULTADO (atribuido a outbound, ver 143)
  Clientes ganados por outbound:  4
  Margen por cliente:             $1.500
  Margen total:                   $6.000

MÉTRICAS
  CAC outbound = $1.552 ÷ 4        = $388 por cliente
  ROI          = ($6.000 − $1.552) ÷ $1.552 = 2.87  → 287%
  LTV:CAC (si LTV = $1.500)        = 1.500 ÷ 388 ≈ 3.9 : 1   ✓ sano (>3)
```

Lectura: el outbound rinde (ROI 287%, LTV:CAC ~3.9). Pero fíjate cómo **tu tiempo ($1.200) es el 77% del costo** —si no lo contaras, el CAC parecería $88 y creerías que es magia. Estos números son de muestra: **corre TU cálculo real en `Matematicas_lushows`** (con decimal, sin float, para que el dinero cuadre exacto) antes de decidir nada.

## Qué decisiones desbloquea este número

- **CAC bajando el reply rate:** si el CAC sube, casi siempre es un ratio del funnel que cayó (ver `83`) —arréglalo antes de gastar más.
- **¿Escalar?** Si el CAC es sano y hay demanda, contratar otro SDR se justifica (ver `85`, `89`). Si el CAC ya aprieta, escalar solo lo empeora.
- **¿Cortar una herramienta?** La del ROI negativo se va.
- **¿Outbound vs. otro canal?** Comparar el CAC de outbound contra el de ads (`facebook_ads`, `google_ads`) es decisión de mezcla GTM → `economist_lushows`.

## Errores comunes

- **No contar el costo humano.** El error #1: un CAC que ignora tu tiempo o el sueldo del SDR miente barato.
- **Atribuir mal el denominador.** Contar como "outbound" clientes que vinieron de otro canal → CAC falsamente bajo (`143`).
- **CAC contra el precio, no contra el LTV.** Un CAC de $388 puede ser genial o terrible según cuánto valga el cliente en el tiempo.
- **Float en cálculos de dinero.** Redondeos que no cuadran; usa decimal → `Matematicas_lushows`.
- **Mirar el CAC una vez.** Es un número vivo; revísalo por periodo junto al dashboard (`144`).

## La frontera

Este módulo **define y estructura** los costos y el CAC/ROI del outbound. La **aritmética exacta** (con decimal, verificada) → `Matematicas_lushows`. La **decisión estratégica** que sale del número —LTV:CAC del negocio, mezcla de canales, si el modelo de negocio cierra, cuánto invertir— → `economist_lushows`. **Registrar contablemente** esos costos, clasificarlos y declararlos (no es lo mismo que calcular el CAC) → `contador_lushows`. Comparar contra el CAC de demanda pagada → las skills de ads.

## Siguiente paso

Suma tus tres familias de costo de este mes (sin olvidar tu tiempo), cuenta solo los clientes que el outbound realmente generó (`143`) y saca tu CAC y ROI con la plantilla del ejemplo —ejecutándolo en `Matematicas_lushows`. Lleva el resultado a `economist_lushows` para decidir si escalar, cortar o rebalancear canales. Vigílalo cada periodo junto a tu dashboard (`144`) y forecast (`145`).
