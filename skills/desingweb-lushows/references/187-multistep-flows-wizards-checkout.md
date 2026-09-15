# 187 — Multi-step flows, wizards & checkout choreography

**CRAFT + UX.** El nivel *flow* (distinto de field-level forms/21). Pareja de 21 (forms/inputs), 29 (pricing/checkout), 30 (onboarding), 180 (estados). Regla de oro: **multi-step convierte ~86% mejor que single-page para forms largos, + un progress indicator añade 20-25% — la choreography importa tanto como los campos; sweet spot 3-5 pasos.**

## 1. Cuándo partir en pasos (vs una sola página)

**Split cuando:** form largo (>6-7 campos), **chunks lógicos** naturales (contacto/envío/pago), branches condicionales, overwhelm. Mecanismo: **perceived effort management** (20 campos visibles se leen como "esto es enorme"; los mismos en 4 pasos de 5 se sienten triviales) + **sunk-cost/commitment** (quien completa el paso 1 ya invirtió). **Single-page cuando:** ≤5-6 campos, todo cabe, velocidad sobre handholding (login, newsletter). No fragmentes 3 campos en 3 pasos. **Sweet spot 3-5 pasos** (>6 hasta usuarios comprometidos abandonan; si tienes 9, recorta lo que pides).

## 2. Progress & orientación

El stepper responde **¿dónde estoy? ¿cuánto falta? ¿puedo volver?** **Numbered + named** (5+ pasos o dominio desconocido — el label reduce ansiedad). **% / progress bar** (flows cortos o de longitud variable). **Linear** (procesos secuenciales con dependencias — checkout) **vs non-linear clickeable** (pasos independientes — settings). **Back/edit-previous siempre** (corregir sin perder datos; en checkout los errores se cazan en el **review final** con **edit inline** sin re-navegar — Baymard). **"Review before submit"** explícito en flows con consecuencias. Tres estados del stepper (completado/actual/pendiente) visualmente distintos, no solo color.

## 3. Diseño del paso

**Un chunk lógico por paso** (agrupa por significado; no mezcles pago con dirección). **Carga cognitiva baja** (idealmente sin scroll en mobile — *one thing per screen*). **Autofocus** en el primer campo. **Una primary action: "Continuar"** (dominante; la secundaria "Atrás" subordinada; el CTA final específico "Pagar $120.000"). **Validation timing:** on-blur campo por campo + **bloquea el avance** validando todo el paso al pulsar Continuar (nunca dejes que llegue al paso 4 con un error del paso 1). **Optional vs required** (marca lo opcional explícitamente; permite skip). **"Don't lose my data"** (persiste estado entre pasos y sesiones — no-negociable en >3 pasos).

## 4. Checkout específico

**Pasos canónicos:** carrito → información → envío → pago → revisión → confirmación (el promedio tiene 14.88 campos; un guest óptimo logra 6-8). **Guest checkout obligatorio** (forzar cuenta = causa #1 de abandono corregible; ofrece "crear cuenta" *después*). **Express-pay arriba** (Apple/Google Pay, *antes* del form). **Patrón ganador 2026: accordion/one-page con secciones que colapsan al completarse** (ves progreso, editas inline, no recargas). **Trust at payment** (badges de seguridad **junto al campo de tarjeta**, no en footer). **LatAm checkout (cross-ref 21/42):** soporta **COD (contraentrega)**, **cuotas/MSI**, **PSE/Nequi**, y crucialmente **cierre por WhatsApp** (muchos flows terminan redirigiendo a WhatsApp con el pedido pre-armado — diseña el último paso como "Confirmar por WhatsApp" cuando COD/WhatsApp domina). **Mostrar costo total temprano** (el "cost shock" del envío en el último paso es razón top de abandono).

## 5. Onboarding wizards & setup flows

**Time-to-value es la métrica reina.** **Progressive onboarding > upfront tour** (introduce features cuando son relevantes — Calendly: primero creas *un* link <1min, valor inmediato, luego team/integraciones). **Checklist alternative** (cap 5-7 ítems; 15 = "me dieron tarea"). **Skip/"hacer después" siempre.** **Setup wizard mínimo** (cuenta → 1 config esencial → primer valor; pide datos solo cuando los necesitas).

## 6. Craft & a11y

**Transiciones** (slide horizontal o fade 150-250ms; `prefers-reduced-motion` → cambio instantáneo). **Focus management** (al cambiar de paso, **mueve el foco al heading** del nuevo paso o a un contenedor `tabindex="-1"` — sin esto el screen reader se queda en el botón anterior). **Step announcement** (`aria-live="polite"` "Paso 2 de 4: Envío"; `assertive` solo errores críticos). **Error recovery sin reiniciar** (lleva el foco al primer error, descríbelo en texto, corrige en sitio). **Save-and-resume**. **Keyboard** (Enter avanza, Tab en orden lógico; botones reales). **Completion celebration** (check animado/confetti sutil + next-step). **Medir step drop-off** (instrumenta cada transición; el paso con mayor caída es donde pides cuenta/tarjeta/dato sorpresa).

## Multi-step anti-patterns — blacklist
**paginar un form corto** (3 campos en 3 pasos) · **>6-7 pasos** sin recortar · **stepper sin "atrás"** o que pierde datos al recargar · **validar todo al final** (el error del paso 1 se descubre en el 5) · **forzar crear cuenta** antes de guest checkout · **express-pay enterrado** debajo del form · **costo de envío revelado en el último paso** · **review final que obliga a re-navegar** todos los pasos (en vez de edit inline) · **no mover el foco** al cambiar de paso · **`aria-live="assertive"` para todo** · **transiciones sin `prefers-reduced-motion`** · **tour de onboarding upfront** que vacía 12 features antes del primer valor · **checklist de 15 ítems** · **pantalla de éxito muda** sin next-step · **progress bar que miente** (salta de 30% a 90%).
