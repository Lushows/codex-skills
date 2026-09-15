# 135 — Señales de crecimiento (funding, contratación, expansión)

Las **señales de crecimiento** son eventos públicos que indican que una empresa está creciendo y, por tanto, **gastando**: levantó una ronda de inversión (funding), está contratando (hiring), abrió una sede o entró a un país nuevo (expansion). El módulo `37` las nombró; este va a fondo en las **tres más accionables** — dónde detectarlas, cómo leerlas y cómo convertirlas en outbound con timing perfecto. Son señales de "le pasó algo bueno y ahora tiene dinero y necesidad", primas del cambio de cargo (`133`) y hermanas del intent (`131`).

## El principio: crecer crea necesidades y presupuesto a la vez

Una empresa que crece tiene dos cosas que un prospecto normal no: **dinero fresco** y **problemas nuevos** que resolver rápido. Ese combo abre una ventana de compra. La lógica por señal:

- **Funding (ronda):** entró capital con la expectativa explícita de **crecer rápido**. Van a comprar herramientas, contratar y escalar. La ronda casi siempre trae un mandato de "gasten para crecer".
- **Hiring (contratación):** una vacante es la empresa **diciéndote su plan** en voz alta. Si buscan 5 vendedores, van a necesitar todo lo que le sirve a un equipo de ventas. La descripción de la vacante es un mapa de sus prioridades y su stack.
- **Expansión (nueva sede/país):** operación nueva = necesidades nuevas (proveedores locales, sistemas, personal). Especialmente rica para PYMES LatAm.

Como toda señal, **caducan** y exigen velocidad (`37`). Una ronda tiene su ventana más caliente en los primeros 1–3 meses.

## Las tres señales, a fondo

| Señal | Qué leer | Dónde detectarla | Ángulo |
|---|---|---|---|
| **Funding** | Monto, etapa (seed/A/B), inversores, para qué dijeron que es | Crunchbase, PitchBook, TechCrunch/prensa, boletines (Contxto en LatAm), Clay | "Vi la ronda; suele venir con el reto de escalar {X} sin romper {Y}" |
| **Hiring** | Qué rol, cuántos, seniority, herramientas que piden en la vacante | LinkedIn Jobs, portales (Computrabajo/elempleo en LatAm), scraping (`27`), Clay | "Vi que buscan {rol}; normalmente eso significa {necesidad}" |
| **Expansión** | Ciudad/país nuevo, formato, tamaño | Prensa local, LinkedIn, Google Maps (nueva ficha), redes | "Felicitaciones por la sede en {ciudad}…" |

### Funding — leer más que el titular
No basta "levantó plata". Lee la **etapa** (seed vs Serie B cambia su madurez y presupuesto) y **para qué** lo dijeron (si dicen "para expandir el equipo comercial" y tú le vendes a equipos comerciales, es tu señal exacta). Crunchbase es la base; su API o Clay lo automatizan. En LatAm, boletines como Contxto y la prensa local cubren rondas que Crunchbase se pierde.

### Hiring — la vacante es un rayos X de su prioridad
La joya subestimada. Una oferta de empleo revela: **qué** están priorizando (contratan → van a invertir ahí), **qué herramientas** usan o quieren (las piden en requisitos → technographic gratis, `134`), y **qué dolor** tienen (por qué necesitan a esa persona). Si buscan "SDR con experiencia en Apollo", sabes su stack, su función y su plan de crecimiento, todo de una vacante. Se scrapea de LinkedIn Jobs y portales (`27`); Clay tiene columnas que lo hacen.

### Expansión — oro para PYMES LatAm
Una nueva ficha en Google Maps, un post de "abrimos en Medellín", una nota en prensa local. Para quien vende a negocios físicos (restaurantes, retail, servicios), la apertura de sede es una necesidad recién creada y muy accionable.

## Cómo montar la detección, paso a paso

1. **Elige la señal más ligada a lo que vendes.** Si vendes a equipos comerciales → hiring de vendedores. Si vendes herramientas de escalado → funding. No persigas las tres a la vez (`37`).
2. **Conecta la fuente:**
   - Funding: alerta de Crunchbase / columna en Clay / boletín del sector.
   - Hiring: búsqueda guardada en LinkedIn Jobs + scraping de portales, o Clay.
   - Expansión: alertas de Google, monitoreo de prensa local, LinkedIn.
3. **Filtra por fit** (`10`, `137`). Que crezcan no importa si no son tu ICP.
4. **Enriquece al decisor** disparado por la señal (`29`, waterfall `130`, verifica `28`).
5. **Dispara la cadencia que nombra la señal** como razón del contacto (`128`), rápido (`147`).

## Ejemplo: cadencia disparada por "está contratando vendedores"

```
Señal (LinkedIn Jobs + Clay): {Empresa} publicó 4 vacantes de "Ejecutivo
   Comercial" esta semana; la vacante pide experiencia en HubSpot.
Fit: es tu ICP → sí. Bonus: sabes que usan HubSpot (technographic, `134`).

Email 1 (día 0):
  Asunto: Las 4 vacantes comerciales de {Empresa}
  "Hola {nombre}, vi que están sumando 4 ejecutivos comerciales. Cuando
   un equipo de ventas crece así de rápido, el cuello de botella deja de
   ser cerrar y pasa a ser **llenar el pipeline** de cada nuevo vendedor.
   Justo en eso ayudamos a equipos que usan HubSpot. ¿Charlamos 12 min?"

Email 2 (día 4): caso de otra empresa que escaló su equipo comercial.
```

La vacante **es** el opener y de paso te reveló su CRM. La conversación de venta que sigue → `ventas_lushows`.

## Errores comunes

- **Quedarse en el titular del funding** → lee etapa y destino del dinero; ahí está el ángulo real.
- **Ignorar el hiring** → es la señal más rica y barata (las vacantes son públicas); casi nadie la explota.
- **Perseguir las tres señales** → elige una y hazla bien (`37`).
- **Lentitud** → la ronda de hace 6 meses ya no es noticia; contacta en semanas, no meses.
- **Señal sin fit** → una startup que levantó Serie A pero no es tu ICP no vale.
- **Felicitar de forma genérica** → "felicidades por la ronda" pegado a un correo plantilla se nota; conecta la señal con el valor (`128`).

## Frontera y siguiente paso

Estas señales te dan cuentas con **dinero y necesidad ahora**; convertirlas en reunión y cierre es `ventas_lushows`. Elige tu señal #1 y monta su detección esta semana (empieza por **hiring**: es gratis y riquísimo). Escribe la cadencia que la nombra (`128`), cruza con fit (`137`), y actúa rápido (`147`). Para la señal de cambio de cargo (otra familia) → `133`; para el intent "está investigando" → `131`; marco general de señales → `37`.
