# 30 — Onboarding & activación (llevar al usuario al valor rápido)

Para SaaS. **Léelo cuando diseñes signup, first-run, tours, checklists o empty states.** Pareja de 13 (app UI), 21 (forms) y 17 (copy).
**Filosofía núcleo (Wes Bush, "bowling alley"):** tu producto es la bola, el onboarding son las barandas. Las barandas mantienen el rumbo hacia el strike (el valor), pero NO tiran la bola. Error #1: tratar el onboarding como el mecanismo que entrega valor, en vez de rieles alrededor del producto que sí lo entrega.

## 1. Estrategia: activación, no onboarding

**Onboarding ≠ activación.** Onboarding = los flujos/guías (barandas). **Activación** = el usuario experimenta el valor central por primera vez (el "aha moment"). Completar un checklist NO es activación.
**Time-to-Value (TTV) = el rey.** Benchmark SaaS: 1 día 12h; <1h fuerte; <5min world-class. Aha en <5min → ~40% más retención a 30 días. Caso Athenic: 12→7 pasos + Google SSO → activación 42%→81%, trial-to-paid 8%→22%.
**Identificar el aha:** lista eventos candidatos → correlación/regresión vs retención a 8-12 semanas → verifica causalidad. "Magic numbers": Facebook *7 amigos en 10 días*, Slack *2.000 mensajes*, Dropbox *1 archivo en 1 dispositivo*.
**Principios:** **"do, don't tell"** (aprende haciendo, no leyendo) · **progressive > upfront** (revela la siguiente acción al completar; 30-40% de los pasos típicos son features avanzadas que van a "secondary onboarding") · **minimiza setup** (pre-rellena, defaults, sample data) · **3 fases:** Orient (0-60s) → Activate (1-5min, guiado al primer valor) → Reinforce (5min-7días) · **sweet spot 3-7 pasos** (>20 pasos baja completion 30-50%).

## 2. Patrones UX y cuándo

| Patrón | Funciona | Falla |
|---|---|---|
| Welcome screen | 1 frase/1 pantalla, setea expectativa | Párrafos (se descarta en <1s) |
| Product tour lineal | Solo para ya-convencidos | Bloquea features → mata exploradores |
| Tooltips/coach marks | Contextual, just-in-time | Todos de golpe = ruido |
| **Checklist/getting-started** | **El más potente para activación** | >7 ítems = homework |
| Progress bar | Siempre, junto al checklist (Zeigarnik) | — |
| Empty state como onboarding | Al aterrizar en lienzo en blanco | Vacío sin guía = parálisis |
| Sample/demo data + templates | Reduce barrera del lienzo en blanco | Si no se puede limpiar fácil |

**Checklist (receta):** 3-5 ítems (máx 7) · ancla cada uno a un **OUTCOME, no acción** (✅"Envía tu primer email de prueba" ❌"Configura SMTP") · incluye un ítem **ya completado** ("Crea tu cuenta ✓") para arranque · progress bar visible. (Completion promedio 19.2%, mediana 10.1% → la brevedad importa.)
**Interactivo > pasivo**, pero ofrece walkthrough opcional junto al checklist (sirve a ambos estilos). **Siempre da "Skip".**

## 3. Signup & first-run

**Reductores de fricción:** SSO/Google y magic link > formularios largos · **elimina sin piedad** campo de tarjeta, gate de verificación de email, formularios largos · **progressive profiling** (pregunta después, no upfront).
**La pregunta JTBD única** (segmentación que sí vale): Notion *"How do you want to use Notion?"* (Work/Personal/School) → dirige template + config + empty state. Una pregunta gana a un wizard de cinco; el resto se infiere por comportamiento. (Solo rol no basta: añade la capa jobs-to-be-done.)
**Demostrar valor ANTES del signup (frontera 2026):** Lovable (chatbox funcional pre-signup → 85% retención día-30), Gamma (*"What would you like to create?"* → el artefacto generado ES la activación). Si DEBES poner gate, entrega algo que el usuario se lleve en la 1ª sesión.
**Metas de la 1ª sesión:** UN momento de valor + UN artefacto producido/visto. Nada más.

## 4. Empty states (profundo)

3 tipos: **first-use** (onboarding, lienzo en blanco + CTA primario) · **user-cleared** (vació la lista — tono de logro, no error) · **error/no-results** (comunica estado del sistema).
**Anatomía:** ilustración/ícono (opcional, no interactivo) + **headline positivo** + 1 línea de descripción + **CTA primario** + (a veces) "Learn more"/demo data.
**3 usos (NN/g):** (1) comunicar estado ("No hay registros para el rango" — distingue vacío real de carga lenta); (2) **learning cues** (DataDog: *"Star your favorites to list them here"*); (3) ruta directa a la tarea (Loggly: "añadir log sources" o "explorar con demo data").
**Microcopy:** headline positivo (✅"Start by adding data assets" ❌"You don't have any") · Notion *"Let's create your first page!"* + botón `+` · tono humano (✅"Almost there, make sure your password has at least 8 characters").

## 5. Engagement & retention loops

**Secuencia de emails (5-8 en 10-21 días):** welcome → setup prompt → feature education → first-milestone celebration → trial-ending warning → upgrade CTA → post-trial nudge. **Behavior-triggered > time-based** ("acabas de hacer X" > "llevas una semana"). Celebra milestones ("You just sent your first campaign to 250 contacts").
**Hook model (Nir Eyal):** Trigger → Action → **Variable Reward** (resultado positivo impredecible) → Investment (el usuario mete datos/config → carga el siguiente trigger).
**Gamificación con gusto (progreso, NO manipulación):** progress bars, milestones, checklists; celebra logros reales; evita badges huecos/FOMO artificial. +40-60% retención a 7 días con progreso visible.
**Feature adoption:** monitorea milestones reales (primer flujo publicado, primer invitado), no "tour completado".

## 6. Medición & tendencias 2026

Benchmarks B2B SaaS: activation rate **37.5%** (avg; >50% excepcional) · TTV 1día 12h · checklist completion 19.2%/10.1% · retención mes 1 46.9% · NPS post-onboarding 35.7.
**Regla:** cada flujo necesita **métricas pareadas** (completion del flujo Y feature-adoption del cohort). Alto completion + adoption plana = **fricción decorativa → bórralo.**
**Diagnóstico:** Funnel (dónde caen) + Session replay (qué hacen) + encuesta in-app de 1 pregunta (por qué pararon). Confusión → arreglo de onboarding; "no resuelve mi necesidad" → arreglo de producto.
**Tendencias:** PLG en la era IA (el producto hace el onboarding) · onboarding AI-personalizado (1 pregunta JTBD + comportamiento) · herramientas de in-product guidance (Appcues/Userpilot/Pendo/Chameleon) · **two-stream** (checklist para todos + monitoreo proactivo de milestones para rezagados).

## Onboarding anti-patterns — blacklist
welcome modal con párrafos (se descarta en <1s) · tour lineal largo que bloquea features · pedir demasiado en signup (wizard de 5 preguntas) · gate de tarjeta/verificación de email antes del valor · personalización solo por rol sin JTBD · features avanzadas en el onboarding primario · container vacío sin guía (parálisis) · checklist anclado a acciones técnicas en vez de outcomes · medir "tour completion" como éxito (vanity metric) · tratar el onboarding como entrega de valor · tools separadas para flows y analytics · drips time-based en vez de behavior-triggered.

**Regla de oro:** reduce TTV a un momento de valor en la 1ª sesión. Define UNA métrica de activación que prediga retención. Checklist de 3-5 outcomes con progress bar. Que el producto entregue el valor; el onboarding solo evita salirse del carril. Mide completion Y adoption en pares.
