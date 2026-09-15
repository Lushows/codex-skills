# 102 — Sales Navigator avanzado

LinkedIn Sales Navigator es la mejor **fuente viva de personas y empresas** que existe: los datos los actualizan los propios profesionales (cambian de trabajo, ascienden, publican) y tú los filtras con precisión quirúrgica. El `26` te presentó la herramienta; este módulo es el nivel experto — **búsquedas booleanas afiladas, spotlights (los filtros de señal), listas, alertas y cómo convertir todo eso en munición para tu stack** (Clay `31`/`101`, sequencer `33`). Bien usado, Sales Nav no solo te da nombres: te dice *a quién atacar hoy y por qué*.

## El principio: los datos los mantiene el prospecto, no un scraper

Una base como Apollo o ZoomInfo envejece: el email de hace 8 meses puede estar muerto. En LinkedIn, la persona **misma** actualiza su cargo el día que asciende. Por eso Sales Nav es insuperable para dos cosas: **(1) filtrar por señales frescas** (cambió de empleo, la empresa crece, publicó algo) y **(2) verificar que el decisor sigue en el puesto** antes de escribirle. La contra: **no te da el email**; te da el perfil. El email lo consigues cruzando el perfil con Apollo/Clay (ver `23`, `29`). El flujo pro es: *Sales Nav filtra → exportas la lista → Clay enriquece con el correo → sequencer envía*.

## Filtros que separan al experto (spotlights y booleanos)

Los **spotlights** son los filtros de señal, tu mayor ventaja (ver `14`, `37`):

| Spotlight / filtro | Qué señala | Por qué importa |
|---|---|---|
| **Changed jobs (últimos 90 días)** | Alguien nuevo en el puesto | Recién llegado = quiere dejar huella, más abierto a hablar |
| **Posted on LinkedIn (últimos 30d)** | Está activo en la red | Vas a llegar por LinkedIn (ver `57`) y sí lee |
| **Company headcount growth** | La empresa crece | Presupuesto y dolores nuevos |
| **Mentioned in news** | Evento reciente | Gancho perfecto para el opener |
| **Seniority level / Function** | Nivel y área | Aísla al decisor real (ver `22`) |
| **TeamLink / shared connections** | Conexión en común | Vía cálida para un intro |

Para cargos usa **lógica booleana** en el campo de título — así atrapas variantes sin ruido:

```
Title:  ("director de operaciones" OR "COO" OR "gerente general" OR "head of operations")
        AND NOT ("asistente" OR "practicante" OR "junior")
```

Reglas del booleano en Sales Nav:
- **Comillas** para frase exacta: `"gerente de compras"`.
- **AND / OR / NOT** en MAYÚSCULAS.
- **Paréntesis** para agrupar: `(A OR B) AND NOT C`.
- Combínalo con los filtros nativos (empresa, geografía, tamaño) en vez de meter todo en el booleano.

## Account search vs. Lead search (usa los dos, en orden)

El error del novato es ir directo a *Lead search* (personas). El pro trabaja en **dos pasos** (ver `21`, `22`):

1. **Account search** → filtra **empresas** por tamaño, industria, geografía, crecimiento, tecnología. Guárdalas en una **Account List** (ej.: "Restaurantes 20–100 empleados Bogotá").
2. **Lead search** → dentro de esas cuentas, filtra **personas** por cargo/seniority/función. Guárdalas en una **Lead List**.

Así separas "a qué empresas quiero entrar" de "a quién dentro de cada una", que es la base de un buen list-building y de ABM (ver `94`).

## Listas y alertas (convertir la búsqueda en un sistema vivo)

- **Guarda toda búsqueda** como Saved Search: Sales Nav te avisa cuando entran **leads nuevos** que cumplen el filtro. Lista viva (ver `21`).
- **Lead Lists y Account Lists** = tus cubetas de trabajo. Sales Nav te muestra en el feed las **novedades** de esas listas: quién cambió de trabajo, quién publicó, qué empresa salió en noticias → eso es tu cola de "a quién tocar hoy con un gancho fresco".
- **Alertas** por cuenta: cambios de personal clave, crecimiento, noticias. Cada alerta es un **trigger de outbound** (ver `14`).

El ritual diario del SDR (ver `67`): abrir las alertas de tus listas → 10–15 leads con señal fresca → mensaje personalizado con el gancho del día.

## Del perfil al email (cerrar el ciclo con el stack)

Sales Nav no da correos, así que el flujo es:

```
1. Sales Nav: Account List + Lead List filtradas (booleano + spotlights)
2. Exportar los leads  → vía integración/Clay (ver 31, 101) o herramienta de sourcing (ver 25)
3. Clay: waterfall de email + verificación (ver 23, 28, 29)
4. Sequencer (Instantly/Smartlead, ver 103/104) para el canal email
5. El propio LinkedIn para el canal social (conexión + mensaje, ver 57)
   → secuencia multicanal (ver 61)
```

Nota sobre scraping: exportar masivo desde Sales Nav con bots (PhantomBuster y similares) **viola los términos de LinkedIn** y arriesga tu cuenta; hazlo con cabeza y a bajo volumen (ver `27`, `109`). Sales Nav no es Recruiter ni Ads: es prospección 1-a-1.

## Ejemplo real: cuentas en crecimiento + decisor nuevo

```
Objetivo: SaaS de gestión para clínicas, LatAm.
Paso 1 — Account search:
   Industry: Hospital & Health Care
   Headcount: 51–200
   Headcount growth: > 10%
   Geography: Colombia, México, Chile
   → guardar como Account List "Clínicas en crecimiento"
Paso 2 — Lead search (dentro de esa lista):
   Title: ("director médico" OR "gerente administrativo" OR "CTO" OR "director de tecnología")
   Seniority: Director, VP, CXO
   Spotlight: Changed jobs in last 90 days   ← el gancho
   → Lead List "Decisores nuevos clínicas"
Opener (por LinkedIn o email):
   "Felicitaciones por el nuevo rol en {empresa}. Los primeros 90 días
    son para dejar huella; ayudamos a clínicas de su tamaño a {resultado}
    sin {dolor}. ¿Vale 10 min esta semana?"
```
La conversación que sigue (objeciones, agendar, cerrar) no es de este módulo → `ventas_lushows`. Aquí solo montas la lista y el gancho.

## Precio y planes

Sales Navigator **Core** (~$99/mes) sirve para la mayoría de SDRs solistas: búsqueda avanzada, listas, alertas, InMails limitados. **Advanced** (Team, más caro) suma TeamLink y funciones de equipo; **Advanced Plus** (Enterprise) integra con CRM. Confirma precios actuales en LinkedIn. Para un solista, Core basta.

## Errores comunes

- **Saltar Account search** y filtrar solo personas → listas sin lógica de cuenta.
- **Meter todo en el booleano** en vez de usar los filtros nativos → resultados sucios.
- **Ignorar los spotlights** → mandas mensajes fríos sin gancho cuando tenías la señal servida.
- **Scrapear masivo** → baneo de cuenta (ver `27`, `109`).
- **Tratar el InMail como spam.** Es caro y limitado; úsalo para cuentas Tier A con mensaje quirúrgico (ver `16`, `57`).

## Siguiente paso

Arma una Account List + Lead List con un booleano de cargo y un spotlight de señal, y móntate las alertas. Exporta 30 leads, enriquécelos con email en Clay (`31`, `101`), verifícalos (`28`) y lánzalos en secuencia multicanal (`61`). Para el copy del mensaje de LinkedIn → `57`; para el gancho por señal → `14`, `37`.
