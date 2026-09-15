# 142 — Routing y round-robin

El **routing** (enrutamiento) es la regla que decide, en el instante en que un lead califica o responde, **a qué persona se le asigna**. El **round-robin** (repartir por turnos, como repartir cartas) es el método más común para hacerlo justo. `38` te dio el routing por score de forma introductoria; este módulo es el mecanismo a fondo: cómo repartir rápido y justo entre varios SDRs/AEs, cómo respetar territorios y verticales, y cómo evitar los dos pecados —el lead que espera horas a que alguien lo asigne, y el reparto injusto que quema al equipo.

## El principio: velocidad y justicia, en ese orden

Dos cosas rompen un equipo de outbound: **lentitud** (el lead caliente se enfría esperando dueño) y **injusticia** (un SDR recibe todos los buenos, otro todos los malos). El routing resuelve ambas: asigna en segundos (velocidad) y reparte parejo el volumen y la calidad (justicia). La velocidad de asignación es un multiplicador conocido —contactar a un interesado en minutos vs. horas cambia dramáticamente la tasa de reunión— así que el routing **manual** ("cuando alguien revise la cola") es una fuga directa de dinero.

## Los cuatro métodos de routing

| Método | Cómo reparte | Cuándo usarlo | Riesgo |
|---|---|---|---|
| **Round-robin puro** | Por turnos: 1→SDR-A, 2→SDR-B, 3→SDR-C, repite | Equipo parejo, leads homogéneos | Ignora carga y skill |
| **Round-robin ponderado** | Turnos con peso: el mejor/más rápido recibe más | Skills desiguales, ramp de novatos (`86`) | Requiere afinar pesos |
| **Por territorio/segmento** | Regla fija: vertical X → SDR dueño de X | Especialización por nicho/idioma/región | Desbalance si un territorio es más grande |
| **Por capacidad (load-based)** | Al que tiene menos leads activos ahora | Volumen alto y variable | Necesita datos de carga en vivo |

En la práctica se **combinan en cascada**: primero una regla fija (territorio/vertical), y dentro del grupo que califica, round-robin ponderado por capacidad. Nunca uses un solo método si tu equipo no es perfectamente homogéneo.

## La cascada de routing (el orden correcto)

```
Lead califica (SQL) o responde positivo
     │
     ▼
1. ¿Es lead A/B/C?  (score, ver 38)     → Tier A entra a cola prioritaria
     │
     ▼
2. ¿Territorio/vertical/idioma?         → si vertical=gastronomía → grupo {Ana, Luis}
     │                                     si es cuenta ABM nombrada → owner fijo (94)
     ▼
3. ¿Quién del grupo, este turno?        → round-robin ponderado por capacidad
     │                                     (salta a quien está de vacaciones/tope)
     ▼
4. Asigna owner + notifica en segundos   → Slack/WhatsApp al SDR: "tienes a X, contáctalo ya"
     │
     ▼
5. Registra la asignación (auditable)    → quién, cuándo, por qué regla (para revisar justicia)
```

El paso 4 es no negociable: **asignar sin avisar = lead que duerme**. El aviso instantáneo (vía webhook, ver `147`) es lo que convierte el routing en velocidad real.

## Reglas de un round-robin justo

Round-robin "puro" parece justo pero no lo es si no maneja los casos borde. Un reparto verdaderamente justo respeta:

- **Disponibilidad:** salta a quien está de vacaciones, enfermo o en su tope diario. Un lead asignado a alguien ausente es un lead perdido.
- **Tope de carga (cap):** nadie recibe más de X leads activos a la vez. Sobrepasar el cap = leads mal trabajados.
- **Balance de calidad, no solo de cantidad:** si repartes solo por número, uno puede terminar con todos los tier A y otro con los C. Reparte los tier A por su propio round-robin.
- **Reasignación por inactividad (el "safety net"):** si el owner no toca el lead en X horas, se reasigna automáticamente. Nada muere en la bandeja de alguien ocupado.
- **Auditabilidad:** guarda por qué cada lead fue a cada quien. Cuando alguien se queje de "me tocan los malos", los datos deciden, no la percepción.

## Ejemplo: reglas de routing en el CRM/automatización

```
# Cascada de asignación (corre en HubSpot workflows / Clay+Make, ver 147)

SI lead_status = "calificado/SQL":
   # Paso 1: cuentas nombradas ABM (prioridad absoluta)
   SI account.abm = true            → owner = owner_ABM_fijo    (ver 94)

   # Paso 2: por vertical
   SINO SI vertical = "gastronomía" → grupo = {SDR_Ana, SDR_Luis}
   SINO SI vertical = "retail"      → grupo = {SDR_Diego}
   SINO                             → grupo = {todos}

   # Paso 3: dentro del grupo, round-robin ponderado por capacidad
   asignar_a = miembro_del_grupo(
        disponible = true,
        leads_activos < cap (ej. 40),
        orden = round_robin_ponderado(peso_Ana=2, peso_Luis=1)  # Luis está en ramp
   )

   # Paso 4: notificar en <60s
   → Slack #sdr-leads: "🔥 {nombre} de {empresa} (tier {tier}) asignado a {owner}"

# Safety net: si owner no registra actividad en 4h laborales → reasignar al siguiente
```

Los pesos y caps son decisiones que conviene cuadrar con números (¿el cap de 40 es óptimo dado tu tiempo por lead?) → afínalos con `Matematicas_lushows`.

## Errores comunes

- **Routing manual.** "Cuando alguien revise la cola" mata el multiplicador de velocidad.
- **Round-robin ciego** que asigna a gente ausente o al tope → leads que duermen.
- **Repartir solo por cantidad**, no por calidad → resentimiento y datos torcidos (uno cierra más solo porque le tocan mejores).
- **Sin safety net.** Un lead atascado en la bandeja de alguien ocupado se pierde en silencio.
- **Sin auditoría.** Sin registro de por qué se asignó, no puedes defender la justicia del sistema ni depurarlo.

## La frontera

El routing decide **a quién** y **qué tan rápido**. Lo que ese SDR hace con el lead una vez asignado —la conversación, calificar, manejar la objeción, agendar— es oficio de venta: `64`/`68` para respuestas tempranas, `71` para el discovery, y el cierre → `ventas_lushows`. Los SLAs formales de tiempo de respuesta entre SDR y AE → `74`.

## Siguiente paso

Escribe tu cascada de routing (tier → territorio → round-robin) en palabras y móntala en tu CRM o en Clay+Make (`147`). Define el cap por persona y el safety net de reasignación. Alimenta el paso 1 con el scoring de `38`/`137`. Para cuentas ABM nombradas → `94`. Para cuadrar caps y pesos con números → `Matematicas_lushows`.
