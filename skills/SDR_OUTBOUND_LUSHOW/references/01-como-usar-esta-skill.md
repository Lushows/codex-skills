# 01 — Cómo usar esta skill

Esta skill tiene 200 módulos. Nadie los usa todos de golpe. Este módulo es el mapa: cómo detectar en cuál de los **7 modos** está el usuario, qué módulos cargar para cada uno, y en qué orden recorre un proyecto de outbound de principio a fin. La regla de oro: **carga solo los 1–4 módulos que la pregunta concreta necesita, nunca los 200.**

## Los 7 modos

Todo proyecto de outbound cae en uno de estos siete momentos. Detecta la señal del usuario y entra por ahí.

| # | Modo | Señal del usuario | Carga primero |
|---|---|---|---|
| 1 | 🎯 **ICP & targeting** | "No sé a quién venderle", "defíneme el mercado", "¿qué nicho?" | Bloque 1 (`10`–`19`) |
| 2 | 🗂️ **Sourcing de datos** | "Necesito la lista", "los correos de empresas de X sector" | Bloque 2 (`20`–`29`) + `31` |
| 3 | 🛠️ **Stack & automatización** | "¿Qué herramienta uso?", "cómo automatizo" | Bloque 3 (`30`–`39`) + Bloque 10 (`100`–`109`) |
| 4 | 📬 **Deliverability** | "Mis correos caen en spam", "cómo configuro el envío" | Bloque 4 (`40`–`49`) + Bloque 11 (`110`–`119`) |
| 5 | ✍️ **Copy & cadencias** | "Escríbeme el cold email", "la secuencia" | Bloques 5 (`50`–`59`) + 6 (`60`–`69`) |
| 6 | 📊 **Métricas & equipo** | "Cómo mido", "contratar SDRs", "escalar" | Bloque 8 (`80`–`89`) + Bloque 15 (`150`–`159`) |
| 7 | 🏢 **Agencia lead-gen** | "Montar/vender outbound como servicio" | Bloque 19 (`190`–`199`) |

Si no está claro cuál, **pregunta en lenguaje simple** ("¿ya sabes a quién venderle, o empezamos por definir el cliente ideal?"). No adivines.

## Diagnóstico SIEMPRE antes de dar técnica

Antes de recomendar una herramienta o escribir un correo, entiende seis cosas. Una pregunta a la vez:

1. **Qué vende** — producto/servicio, ticket (precio), ciclo de venta.
2. **A quién** — ICP, B2B, vertical, país.
3. **Cuánto volumen necesita** — ¿cuántas reuniones/mes? (esto sale de la ecuación, `05`).
4. **Qué tiene hoy** — ¿lista? ¿herramientas? ¿dominios? ¿equipo?
5. **Dónde se traba** — no consigue datos / cae en spam / no le responden / no agenda / no califica.
6. **País, idioma y ley** — Colombia/LatAm cambia todo (WhatsApp-first, Habeas Data; ver `08`, `181`).

Recomendar sin diagnóstico es recetar sin examinar. El "dónde se traba" (punto 5) casi siempre te dice qué modo cargar.

## El recorrido completo de un proyecto

Casi todo proyecto de outbound recorre este orden. Cada flecha es un modo/bloque:

```
Definir ICP (Bloque 1)
  → Construir lista (Bloque 2)
    → Conseguir datos/correos (Bloque 2: 23, 24, 28, 29)
      → Configurar envío/deliverability (Bloque 4)
        → Escribir copy (Bloque 5)
          → Diseñar la cadencia (Bloque 6)
            → Ejecutar y manejar respuestas (Bloque 6)
              → Calificar (Bloque 7)
                → Agendar + handoff al vendedor (Bloque 7)
                  → [CIERRE → ventas_lushows]
                    → Medir y optimizar (Bloque 8)
```

El usuario puede entrar en cualquier punto (muchos ya tienen lista y solo necesitan copy, o ya envían pero caen en spam). Ubícalo en la etapa y trabaja desde ahí.

## Cómo se estructura la biblioteca

- **Núcleo `00`–`99`**: el sistema completo de outbound, 10 bloques de 10 módulos. Con esto haces todo.
- **Expansión `100`–`199`**: profundidad avanzada (herramientas a fondo, deliverability avanzada, RevOps, equipo, ABM, verticales, internacional, agencia). Se carga cuando el núcleo ya no alcanza.

Cada módulo del núcleo enlaza a su versión avanzada. Ej.: `40` (fundamentos de deliverability) apunta a `110`–`119` cuando necesitas escalar a miles de correos.

## Cómo cierra cada respuesta (formato de entrega)

Toda recomendación termina con tres cosas, siempre:
1. **Lo exacto** — el ICP escrito, el filtro de búsqueda, la plantilla de correo, la secuencia día-por-día, la config de deliverability o el número objetivo. Nunca "personaliza", sino *el texto*.
2. **Por qué funciona** — el principio, el número o la mecánica detrás.
3. **El siguiente paso concreto** — qué hacer ahora con una campaña real.

Si el entregable es presentable (un playbook, una propuesta de servicio de agencia), se genera PDF con chrome headless, no se deja en teoría.

## La frontera con las skills hermanas (rutea, no dupliques)

Esta skill es la **máquina que consigue y agenda**. Cuando la pregunta se sale de ahí, rutea:

- Convencer, rebatir a fondo, negociar, **cerrar** → **`ventas_lushows`**.
- Demanda pagada (anuncios) → **`facebook_ads`** (genera), **`google_ads`** (captura), **`tiktok_ads`** (descubre).
- ¿El negocio/CAC/pricing/GTM cierra? → **`economist_lushows`**.
- Cualquier número que deba ser exacto → **`Matematicas_lushows`**.
- Web/landing que convierte → **`desingweb-lushows`**. Marca → **`directorcreativo_lushows`**.

Detalle de cada frontera en el glosario `09` y en el `SKILL.md`.

## Siguiente paso

Identifica el modo del usuario con la tabla de arriba. Si es su primer contacto con outbound, arranca por `00` (método) → `05` (ecuación) → `10` (ICP). Si ya tiene algo andando, ve directo al "dónde se traba".
