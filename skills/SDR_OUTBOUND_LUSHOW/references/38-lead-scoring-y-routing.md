# 38 — Lead scoring y routing

Cuando el outbound funciona, te llegan más leads de los que puedes atender bien, y no todos valen lo mismo. El **lead scoring** (puntuar leads) es asignarle a cada uno un número que dice "qué tan bueno es"; el **routing** (enrutamiento) es mandarlo automáticamente a la persona o cola correcta. Juntos hacen que tu mejor tiempo vaya a los mejores leads y que nada se caiga entre sillas. Este módulo es la versión operativa/automatizable; el scoring fit+intent avanzado vive en `137` y el round-robin a fondo en `142`.

## El principio: no todos los leads merecen el mismo esfuerzo

Tu tiempo (o el de tus SDRs) es finito. Si tratas igual a un lead perfecto y a uno mediocre, desperdicias el bueno y sobre-inviertes en el malo. El scoring ordena la fila: **atiende primero y con más energía a los de score alto**. Y el routing garantiza velocidad —el lead correcto llega a la persona correcta en segundos, no cuando alguien revise la bandeja—. La velocidad de contacto es un multiplicador conocido: responder a un interesado en minutos vs. horas cambia la tasa de reunión.

## Los dos ejes del score: Fit e Intent

Todo scoring serio combina dos preguntas distintas:

| Eje | Pregunta | Datos | Ejemplo de puntos |
|---|---|---|---|
| **Fit (encaje)** | ¿Es la empresa/persona correcta? | firmographics, cargo, industria, tamaño | industria objetivo +20, cargo decisor +15, tamaño en rango +10 |
| **Intent (intención/comportamiento)** | ¿Muestra interés o timing? | señales, respuestas, visitas web, aperturas | respondió positivo +30, visitó precios +20, señal de cargo nuevo +15 |

- **Fit alto + Intent bajo** = buen prospecto, aún frío → nurture / secuencia paciente (ver `76`).
- **Fit bajo + Intent alto** = curioso pero no es tu cliente → cuidado, no le des tu mejor tiempo.
- **Fit alto + Intent alto** = prioridad #1, contáctalo YA.

Esta matriz es la base; el detalle de combinarlos → `137`. Los datos de fit → `15`; los de intent → `36`, `37`.

## El cómo, paso a paso

1. **Define qué es un lead "A".** Antes de puntos, describe en palabras tu lead ideal (ej.: "restaurante 20–80 empleados, en ciudad grande, dueño/gerente, que mostró alguna señal"). El score solo traduce eso a números.
2. **Asigna puntos a los atributos de fit.** Pocos y claros. Que sumen a ~60 máx.
3. **Asigna puntos a las señales de intent.** Que sumen a ~40 máx.
4. **Define umbrales de acción.** Ej.: 70+ = Tier A (SDR contacta ya); 40–69 = Tier B (secuencia normal); <40 = Tier C (nurture o descarte).
5. **Automatiza el cálculo.** En Clay al construir la lista (ver `31`) o en el CRM/HubSpot con scoring nativo (ver `105`). Guarda el score en el campo `icp_fit`/score del CRM (ver `32`).
6. **Enruta por score.** Reglas de routing: Tier A → mejor SDR / cola prioritaria; por territorio/idioma/vertical → al owner correcto; round-robin para repartir parejo (ver `142`).
7. **Recalibra con resultados.** Los leads que **sí** cerraron, ¿qué score tenían? Si cierran los de score 50, tu modelo está mal calibrado. El loop de feedback ajusta los pesos (ver `79`).

## Ejemplo: modelo de scoring simple (0–100)

```
FIT (máx 60)
  Industria = nicho objetivo ............ +20
  Cargo = decisor (dueño/director/gerente) +15
  Tamaño empresa en rango (20–80 emp) ... +15
  Ciudad/país objetivo .................. +10

INTENT (máx 40)
  Respondió positivo a un correo ........ +30
  Visitó página de precios (first-party)  +20   (ver 36)
  Señal de evento (cargo/ronda/hiring) .. +15   (ver 37)
  Abrió 2+ correos ...................... +5
  (se toma el intent más alto, no se apilan todos)

UMBRALES
  70–100 → Tier A  → SDR contacta HOY, canal directo
  40–69  → Tier B  → entra a secuencia estándar
  0–39   → Tier C  → nurture largo o descarte (ver 76)
```

Routing sobre ese score:
```
SI score ≥ 70 Y vertical = "gastronomía"  → SDR_Ana (owner del vertical)
SI score ≥ 70 Y otro vertical             → round-robin entre SDRs
SI 40–69                                   → cola general de secuencias
SI < 40                                    → lista nurture, revisar en 90 días
```
Todo esto corre automático vía CRM o Clay + Zapier/Make (ver `34`). El humano solo trabaja los Tier A y B.

## La precisión de los umbrales importa

Los pesos y umbrales son decisiones de negocio, pero conviene que los números tengan lógica (que la suma máxima cuadre, que los umbrales partan bien la población). Si vas a calibrar con datos reales —tasas de conversión por rango de score, significancia— para no ajustar "a ojo", **rutea el cálculo a `Matematicas_lushows`**. Y si la pregunta es más estratégica ("¿este segmento vale la pena económicamente?, ¿el CAC cierra?"), eso es `economist_lushows`.

## Errores comunes

- **Scoring solo por fit.** Un ICP perfecto que no da señales de vida no es prioridad hoy; te falta el eje intent.
- **Demasiados atributos.** 30 reglas que nadie entiende. Empieza con 6–8.
- **No recalibrar.** Un modelo que no aprende de quién cierra se desactualiza (ver `79`).
- **Routing lento o manual.** Si el Tier A espera horas a que alguien lo asigne, perdiste el multiplicador de velocidad.
- **Puntuar como si el score decidiera la venta.** El score prioriza el esfuerzo; convencer y cerrar sigue siendo `ventas_lushows`.

## Siguiente paso

Escribe tu lead "A" en palabras, tradúcelo al modelo de puntos de arriba y móntalo en Clay o tu CRM. Define 2–3 reglas de routing por score/vertical. Combina fit+intent a fondo en `137`; reparte con round-robin en `142`. Alimenta los ejes con datos de intent (`36`), señales (`37`) y calidad de datos (`139`). Calibra los números con `Matematicas_lushows`.
