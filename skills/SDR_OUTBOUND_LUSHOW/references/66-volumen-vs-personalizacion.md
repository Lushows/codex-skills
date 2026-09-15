# 66 — Volumen vs. personalización

Es el trade-off central del outbound y la decisión que define toda tu operación: ¿mando 2.000 correos casi iguales, o 100 escritos a mano uno por uno? Los dos extremos fracasan. Volumen sin relevancia es spam que quema tu dominio (ver `40`) y no agenda. Personalización total no escala: 100 correos artesanales al mes no llenan un pipeline. La respuesta no es elegir un lado — es un **modelo de tiers** que aplica el nivel de esfuerzo correcto a cada cuenta según lo que vale. Este módulo te da ese modelo.

## El principio: relevancia por dólar de esfuerzo

Tu recurso escaso es el tiempo. Cada minuto que gastas personalizando un correo es un minuto que no gastas en otro prospecto. La pregunta correcta no es "¿personalizo o no?" sino **"¿cuánta personalización merece ESTA cuenta según lo que puede pagarme?"**.

La lógica económica: si un cliente vale $50.000, invertir una hora en un correo 1:1 es obvio. Si vale $200, un correo artesanal te hace perder plata — necesitas escala. El ticket y el valor de vida del cliente (LTV, ver `economist_lushows`) deciden el nivel de esfuerzo. Personalizar barato a gran escala es el santo grial, y en 2026 la IA + herramientas como Clay lo acercan (ver más abajo).

## El modelo de tres tiers

| Tier | Qué es | Cuentas/mes | Esfuerzo por cuenta | Para qué ticket |
|---|---|---|---|---|
| **1:1** (uno a uno) | Correo escrito 100 % a mano, investigación profunda | 20–50 | 15–30 min | Alto ($10k+), cuentas tier A (ver `16`) |
| **1:few** (uno a pocos) | Plantilla + personalización real por micro-segmento | 200–600 | 2–5 min | Medio, el caballo de batalla |
| **1:many** (uno a muchos) | Plantilla con variables básicas, alto volumen | 1.000–3.000 | segundos | Bajo, o para validar mercado |

La mayoría de tu resultado vive en el **1:few**: suficiente relevancia para que responda, suficiente escala para llenar pipeline. Los extremos son casos especiales.

### 1:1 — artesanal, para cuentas grandes

Investigas a la persona y la empresa (LinkedIn, noticias, su web, un trigger real, ver `14`, `37`), y escribes un correo que **solo le sirve a ella**. Referencias algo que dijo, publicó o le pasó. Reservado para tus tier A: pocas cuentas que valen tanto que merecen la hora. Reply rates altos (a veces 15–30 %+), pero no escala.

### 1:few — plantilla + micro-segmento (el santo grial práctico)

Agrupas cuentas por un rasgo común (mismo cargo + mismo sector + mismo trigger) y escribes una plantilla cuyo **núcleo aplica a todo el grupo**, con 1–2 campos que sí personalizas. La clave: personalizar el **problema/contexto del segmento**, no solo el `{nombre}`. "Hola {nombre}" no es personalización (ver `52`).

```
Segmento: dueños de restaurante en Bogotá que abrieron sede nueva (trigger)

"Hola {nombre}, felicitaciones por la nueva sede de {restaurante} en {zona}.
Abrir un segundo local suele disparar el descontrol de costos entre cocinas —
lo que se gana en ventas se pierde en desperdicio si no cuadran los números.
A {cliente parecido} le ayudamos a {resultado}. ¿Te muestro en 12 min cómo?"
```

Lo que cambia por fila: `{nombre}`, `{restaurante}`, `{zona}`. Lo que es fijo: el problema (costos al abrir 2ª sede) es real para **todo el segmento**. Eso es 1:few: se siente 1:1, se ejecuta a escala.

### 1:many — volumen, para validar o ticket bajo

Plantilla con variables básicas (`{nombre}`, `{empresa}`), miles de envíos. Reply rate bajo (1–2 %) pero el volumen compensa si el ticket es chico. Úsalo también para **validar un mercado nuevo** rápido antes de invertir en personalización. Riesgo: es el que más rápido quema deliverability si la lista o el copy fallan (ver `40`, `20`).

## Cómo escalar la personalización sin morir (2026)

El avance real de estos años: acercar el 1:few al 1:1 con automatización.

| Herramienta | Qué hace | Rol |
|---|---|---|
| **Clay** | Enriquece cada fila (scraping, IA) y genera líneas personalizadas a escala | El puente 1:few → sensación 1:1 |
| **IA (Claude/GPT vía Clay o API)** | Escribe la primera línea desde un dato (su LinkedIn, su web) | Personalización a volumen |
| **Instantly / Smartlead** | Envío con variables `{spintax}` y rotación de buzones | Ejecución a escala |

Advertencia: la personalización con IA **mal supervisada es peor que ninguna** — genera líneas genéricas ("me encantó tu trabajo en {empresa}") que gritan "robot". Usa IA para el borrador, revisa por lote, y ancla siempre en un **dato verificable** (un trigger, un número, algo de su web). Ver `29` (enriquecimiento) y `52` (personalización que funciona).

## Cómo decidir tu mezcla (regla práctica)

1. Ordena tu lista en tiers A/B/C por valor de cuenta (ver `16`).
2. Tier A → 1:1. Tier B → 1:few. Tier C / mercado nuevo → 1:many.
3. Dimensiona el volumen desde tu meta de reuniones (ver `17`) y tu límite de envío (~30–50/buzón/día, ver `40`, `45`).
4. Mide reply positivo por tier (ver `65`). Si el 1:many no agenda, no es volumen lo que falta — es relevancia; súbelo a 1:few.

## Errores comunes (qué NO hacer)

- **Un solo modo para todo.** Tratar una cuenta de $50k igual que una de $200 desperdicia esfuerzo o deja plata en la mesa.
- **Creer que `{nombre}` es personalizar.** No lo es (ver `52`).
- **1:many con lista o copy flojos.** Quema el dominio a máxima velocidad (ver `40`).
- **1:1 para tickets bajos.** Pierdes plata: el correo cuesta más que el cliente.
- **IA sin supervisión.** Líneas genéricas que delatan el robot y bajan la respuesta.

## Siguiente paso

Segmenta tu lista en tiers (`16`), asigna modelo a cada tier, y arma la plantilla 1:few de tu segmento principal con `52`. El nivel de personalización que elijas define cuántos correos por variante juntas para un A/B válido (ver `65`). Y para orquestar los tres modos dentro de tu jornada sin ahogarte, ve a `67`.
