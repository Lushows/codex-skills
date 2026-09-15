# 13 — Fase de aprendizaje (learning phase)

Cuando lanzas o editas un ad set, Meta entra en modo exploración: prueba tu anuncio con distintos tipos de persona para descubrir quién convierte. Eso es la **fase de aprendizaje**. Durante ella el CPA (costo por adquisición: lo que pagas por cada conversión) es inestable y suele ser más caro. Lee este módulo antes de "optimizar" tocando botones — la mayoría de cuentas pequeñas se matan a sí mismas reseteando el aprendizaje cada dos días.

## La mecánica

- Necesita **~50 conversiones del evento de optimización en 7 días, por ad set**, para estabilizar. No 50 clics: 50 del evento que elegiste (Purchase, lead, conversación — ver 14).
- Por eso la consolidación (ver 10): 50 conversiones repartidas en 5 ad sets = 5 ad sets eternamente en aprendizaje.
- Cuenta rápida: si tu CPA es $40.000 COP, salir de aprendizaje cuesta ~$2M COP/semana por ad set. Si tu presupuesto es $500k/mes, NUNCA saldrás — y está bien (sigue leyendo).

> 🔁 **Refinamiento 2026 (ver `actualizacion-2026-06`):** Meta endureció las reglas de reseteo. Dos gatillos confirmados hoy: **cambios de presupuesto/puja > 20%** y **ediciones significativas con menos de 72h de vida del ad set** disparan re-aprendizaje. La ventana operativa práctica es clara: **cambios chicos (≤20%) y solo después de 72h**.

## Learning limited: cuándo preocuparte y cuándo aceptarlo

**"Learning limited"** (aprendizaje limitado) aparece cuando Meta proyecta que no llegarás a las ~50 conversiones semanales. Significa "no tengo señal suficiente para estabilizar", NO "tu campaña está rota".

- **Acéptalo si**: eres cuenta micro (< $1.5M COP/mes) o vendes ticket alto con pocas conversiones. Miles de cuentas viven en learning limited y son rentables. La pregunta correcta no es "¿salí de aprendizaje?" sino "¿mi CPA del backend es rentable?" (ver 16 y 64).
- **Preocúpate si**: tienes presupuesto de sobra y aún así no llegas → señal de evento mal elegido (optimiza un escalón arriba, ver 14), estructura fragmentada (consolida, ver 10), o cost cap demasiado agresivo que frena el gasto (ver 15).

Cómo salir de learning limited sin reventar nada (en orden):
1. **Consolida ad sets**: junta el volumen en menos cubetas (ver 10).
2. **Sube un escalón de evento**: de Purchase a InitiateCheckout, etc. (ver 14).
3. **Sube presupuesto del ad set** lo suficiente para acercarte a 50/sem — pero en pasos ≤20% / 72h.
4. **Amplía la audiencia** (más broad, más geo).
Lo que NO debes hacer: duplicar el ad set "para que haya más volumen" (terminas con dos en learning limited).

## Qué RESETEA el aprendizaje (ediciones significativas)

| Cambio | ¿Resetea? |
|---|---|
| Presupuesto o puja **±>20% de golpe** | SÍ |
| **Cualquier edición significativa con < 72h de vida** del ad set | SÍ (regla endurecida 2026) |
| Cambiar estrategia o monto de puja | SÍ |
| Cambiar targeting/audiencia del ad set | SÍ |
| Cambiar evento de optimización | SÍ |
| **Agregar o editar un creativo en el ad set** | SÍ (re-entra en aprendizaje) |
| Pausar varios días y reactivar (≈7+ días) | SÍ en la práctica |
| Presupuesto ±≤20% gradual y con >72h de vida | NO |
| Pausar/apagar UN anuncio dentro del ad set | NO (los demás siguen) |
| Editar copy de la página, UTMs, nombre de campaña/ad set | NO |
| Pausar unas horas / 1-2 días | NO significativo |

Nota: agregar un ad nuevo resetea, pero a veces TOCA (fatiga creativa, ver 39). El reseteo no es el demonio — el demonio es resetear sin razón cada 48 horas.

## Cómo editar sin dinamitar

1. **Agrupa cambios**: si vas a subir presupuesto, cambiar un creativo y ajustar algo más, hazlo TODO en una sola edición. Tres ediciones separadas = tres reseteos.
2. **Regla de las 72 horas**: después de tocar algo significativo, manos quietas 72h mínimo antes de evaluar o volver a tocar. Y nunca toques un ad set con menos de 72h de vida (lo resetea de una, regla 2026).
3. **Escala gradual**: presupuesto **+20% cada 72h**, no ×3 un viernes por la noche (receta completa de escalado en 72).
4. **Ventana de evaluación**: nunca juzgues un ad set por sus primeras 24-48h; mira ventanas de 7 días móviles. Con atribución 7d-click (ver 16) las conversiones se siguen "acomodando" a días previos.
5. Si necesitas refrescar creativos seguido, usa estructura donde el testing pasa en otro lado (ver 17) y a la campaña principal solo entran ganadores, 2-4 veces al mes.

## Mini-playbook: las 2 primeras semanas de un ad set nuevo

| Momento | Qué hacer | Qué NO hacer |
|---|---|---|
| Día 0-3 | Lanzar y NO tocar nada | Mirar a las 12h y entrar en pánico |
| Día 3-7 | Evaluar con ≥3× CPA de gasto; apagar ads sin tracción (no el ad set) | Subir presupuesto por un buen martes |
| Día 7-14 | Si CPA backend es rentable, escalar +20%/72h | Duplicar la campaña "para crecer" |
| Cualquier día | Anotar aprendizajes (ver 17) | Resetear por corazonada |

## La métrica de estabilidad real

Olvida el badge verde de "Activo". La estabilidad real es la **varianza del CPA semana a semana**: saca el CPA de las últimas 4 semanas (del backend si puedes, ver 16). Si oscila menos de ±20-25% alrededor del promedio, tu sistema está estable — diga lo que diga la columna de delivery. Si oscila ±60%, algo está mal: fragmentación, ediciones compulsivas, presupuesto insuficiente o fatiga creativa.

## Errores comunes — blacklist

- "Lleva 2 días y no vende, la apago": mataste el aprendizaje justo cuando estaba pagando la matrícula. Espera gasto de ≥3× CPA esperado antes de juzgar.
- Tocar un ad set con < 72h de vida: reseteo automático garantizado (regla 2026). Déjalo madurar.
- Subir presupuesto 100% porque ayer fue buen día: reseteo + CPA inestable + "Facebook me subió los costos".
- Tocar la campaña todos los días (cambiar copy, pausar, reactivar, mover plata): cada toque significativo reinicia el contador.
- Perseguir el badge "Activo" como objetivo: optimizas para una etiqueta de UI, no para plata.
- Duplicar el ad set "para salir de learning limited": ahora tienes DOS en learning limited.
- Pausar campañas el fin de semana "porque no atendemos WhatsApp": dos reseteos por semana, todas las semanas. Mejor: autoresponder o aceptar leads en cola (ver 50).
