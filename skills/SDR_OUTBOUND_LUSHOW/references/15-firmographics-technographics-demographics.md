# 15 — Firmographics, technographics, demographics (los filtros de targeting)

Tu ICP (`10`) es una idea; los **filtros de targeting** son cómo la conviertes en una lista real dentro de una herramienta. Hay tres familias de filtros: **firmographics** (datos de la empresa), **technographics** (la tecnología que usa) y **demographics** (datos de la persona). Dominar estos tres vocabularios es lo que separa una búsqueda que devuelve "10.000 empresas cualquiera" de una que devuelve "las 400 exactas que encajan". Todo Apollo, ZoomInfo, Sales Navigator y Clay se maneja con estos filtros.

## Las tres familias

| Familia | Describe | Ejemplos de filtro |
|---|---|---|
| **Firmographics** | La **empresa** (cuenta) | Industria, nº de empleados, facturación, geografía, antigüedad, tipo (B2B/B2C), pública/privada |
| **Technographics** | La **tecnología** que la empresa usa | Usa Shopify / HubSpot / AWS / cierto CRM / cierto lenguaje |
| **Demographics** (a veces "contact-level") | La **persona** dentro de la empresa | Cargo, seniority, departamento, antigüedad en el rol, ubicación de la persona |

Regla mental: **firmographics eligen la cuenta, demographics eligen al contacto, technographics afinan ambos.** Un buen filtro combina los tres: "empresas [firmo] que usan [techno], y dentro de ellas el contacto [demo]".

## Firmographics — los filtros de empresa

Los más usados y accionables:

- **Industria / sector:** el filtro raíz. Cuidado: las herramientas clasifican por códigos (SIC/NAICS) o por texto de LinkedIn; una misma empresa puede estar mal etiquetada. Usa varias categorías cercanas + palabras clave.
- **Tamaño (nº de empleados):** el más predictivo del ticket, ciclo y decisor. Define rangos (ej. 11–50, 51–200). Cambia todo: en 10 empleados el dueño decide; en 500 hay comité (ver `11`).
- **Geografía:** país, estado, ciudad. Clave en LatAm para concentrar prueba social local.
- **Facturación (revenue):** útil pero menos confiable en pyme LatAm (datos escasos). En SaaS/USA sí.
- **Antigüedad de la empresa / año de fundación:** una empresa de 1 año tiene dolores distintos a una de 20.
- **Crecimiento de plantilla:** headcount subiendo = señal de escala (cruza con `14`).

## Technographics — targetear por tecnología

Saber qué software usa una empresa es oro para ciertos productos: si vendes un complemento de Shopify, filtrar "usa Shopify" te da una lista pre-calificada. Herramientas que detectan tech: **BuiltWith, Wappalyzer, Clearbit, HG Insights, Datanyze** (a fondo en `134`). Dos jugadas:

- **Complemento:** "usan X, yo mejoro/complemento X" (ej. "usan HubSpot, yo les hago funcionar los correos").
- **Desplazamiento:** "usan [competidor], yo soy la alternativa" → conecta con `19` competitive displacement.

Limitación: los technographics detectan sobre todo tecnología **web pública** (lo que corre en su sitio). El software interno (su ERP, su CRM privado) muchas veces no se ve; ahí toca preguntar o inferir.

## Demographics — los filtros de persona

Una vez elegida la cuenta, filtras a la persona correcta (ver `11`, `22`):

- **Cargo (job title):** el filtro más directo. Ojo: los títulos varían ("Head of", "Director de", "Gerente"). Usa varios sinónimos y el filtro de **seniority** para no depender del texto exacto.
- **Seniority / nivel:** C-level, VP, Director, Manager, IC. Filtra por poder de decisión sin adivinar el título.
- **Departamento / función:** Ventas, Marketing, Finanzas, Operaciones, TI.
- **Antigüedad en el cargo:** menos de 6 meses = trigger de job change (ver `14`, `133`).
- **Ubicación de la persona:** a veces distinta de la sede de la empresa (remoto).

## Cómo construir el filtro (paso a paso)

1. Traduce cada criterio duro de tu ICP a un filtro concreto de la herramienta.
2. Empieza **amplio** y estrecha viendo el conteo de resultados (así calibras tu SAM, ver `13`).
3. Combina firmo + techno + demo en una sola búsqueda.
4. Guarda la búsqueda como lista dinámica (se actualiza sola cuando entran cuentas nuevas).
5. Añade las **exclusiones** de tu ICP como filtros negativos.

## Ejemplo real: de ICP a filtro (Apollo/Sales Nav)

```
ICP: agencias de marketing pequeñas en Colombia que usan HubSpot,
     hablar con el fundador/director.

FILTRO:
  Firmographics:
    Industria = Marketing & Advertising
    Empleados = 5 – 50
    País = Colombia (ciudades: Bogotá, Medellín)
  Technographics:
    Usa = HubSpot
  Demographics (contacto):
    Seniority = Owner, Founder, C-Suite, VP, Director
    Departamento = ejecutivo / marketing
    Excluir cargo = "intern", "assistant"

Resultado esperado: lista acotada de decisores en agencias que ya usan
HubSpot → mensaje: "veo que usan HubSpot; les ayudamos a que sus
secuencias lleguen a inbox y no a spam".
```

Fíjate cómo el technographic ("usan HubSpot") **le da el ángulo al mensaje** (ver `18`). Los filtros no solo arman la lista: te dictan el copy.

## Errores comunes

- **Confiar ciegamente en la etiqueta de industria:** clasificaciones erróneas meten ruido. Verifica una muestra a mano.
- **Filtro demasiado estrecho de golpe:** 12 resultados no alimentan una campaña; afloja un eje.
- **Solo firmographics, sin demographics:** consigues empresas pero no sabes a quién escribir dentro.
- **Ignorar sinónimos de cargo/seniority** y perder la mitad de los contactos válidos.
- **No guardar exclusiones**, y recontactar a los malos clientes que ya sabías descartar.

## Frontera y siguiente paso

Las **herramientas concretas** donde aplicas estos filtros están en `25` (sourcing), `26` (Sales Navigator), `31`/`101` (Clay) y `134` (technographics a fondo). Este módulo es el **vocabulario**; ahí está el **cómo operar cada herramienta**.

**Siguiente paso:** toma tu ICP escrito (`10`) y tradúcelo a un filtro firmo+techno+demo en Apollo o Sales Nav. Mira el conteo (= tu SAM, `13`), guárdalo como lista, y prioriza en `16`.
