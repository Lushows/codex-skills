# 109 — Scraping tools a fondo

Cuando ninguna base de datos tiene la lista que necesitas —los 400 restaurantes de una zona, los asistentes de un evento, los miembros de un grupo de LinkedIn, los negocios en cierto directorio— la construyes tú con **scraping**: herramientas que extraen datos de páginas web de forma automatizada. Este módulo cubre **PhantomBuster, Apify y Bardeen** con recetas concretas, y traza con claridad los **límites legales y de riesgo** — porque scrapear mal te banea cuentas, viola términos de servicio y puede meterte en problemas de datos personales. Es el complemento accionable del `27` (scraping ético y legal); cuando puedas, prefiere una fuente estructurada como Sales Nav (`102`) o Apollo (`100`) antes de scrapear.

## El principio: extraer lo que no viene en una base

Scraping = un bot que "visita" páginas y copia datos estructurados (nombres, empresas, cargos, teléfonos públicos, reseñas). Sirve para **listas de nicho que ninguna base vende**: negocios locales por zona (Google Maps), perfiles de una búsqueda de LinkedIn/Sales Nav, seguidores o comentaristas de una cuenta, miembros de un grupo, expositores de una feria, listados de un directorio o marketplace. El scraping te da el **nombre y la pista**; el **email/teléfono** lo consigues después cruzando con enriquecimiento (Clay/Apollo, ver `23`, `29`), porque scrapear datos de contacto directamente es lo más riesgoso legalmente.

## Las herramientas

| Herramienta | Qué es | Fuerte en | Precio aprox 2026 |
|---|---|---|---|
| **PhantomBuster** | Catálogo de "phantoms" (extractores prehechos), muy orientado a LinkedIn | Recetas listas para LinkedIn, Sales Nav, Instagram | ~$56–128+/mes por horas de ejecución |
| **Apify** | Plataforma de "actors" (scrapers) para casi cualquier web; más técnica | Google Maps, sitios a medida, escala grande | Pago por uso/compute; free tier |
| **Bardeen** | Automatización no-code en el navegador (scrape + acciones) | Tareas rápidas 1-clic desde tu navegador | Free; pago desde ~$10–20/mes |

- **PhantomBuster** = velocidad en redes: eliges un phantom ("LinkedIn Search Export", "Instagram Followers"), lo conectas a tu cuenta y corre. El más usado para LinkedIn, y el más riesgoso por lo mismo.
- **Apify** = potencia general: miles de "actors" prehechos (el de **Google Maps** es oro para negocios locales LatAm) y puedes hacer scrapers a medida. Más técnico, mejor para volumen.
- **Bardeen** = comodidad: automatizas desde el navegador con clics, ideal para tareas puntuales sin montar infraestructura.

## Recetas concretas

**1) Negocios locales por zona (Apify — Google Maps Scraper)**
```
Actor: Google Maps Scraper
Input: búsqueda "restaurantes" + área "Chapinero, Bogotá" (o coordenadas/radio)
Salida: nombre, categoría, dirección, teléfono público, web, rating, # reseñas
Uso: filtras por rating/reseñas (señal de negocio activo) → tu lista de cuentas
Siguiente: cruzar el dominio con Clay para hallar al dueño y su email (ver 23, 101)
```
Esta es la receta estrella para outbound a pymes LatAm (ver `93`): Google Maps tiene los negocios que ninguna base B2B cubre.

**2) Perfiles de una búsqueda de LinkedIn/Sales Nav (PhantomBuster)**
```
Phantom: "LinkedIn Search Export" / "Sales Navigator Search Export"
Input: la URL de tu búsqueda booleana ya filtrada (ver 102)
Salida: nombre, cargo, empresa, URL de perfil  (NO el email)
⚠️ Riesgo alto: viola términos de LinkedIn; ver límites abajo
Siguiente: email vía waterfall en Clay/Apollo (ver 29), nunca scrapeado directo
```

**3) Comentaristas / seguidores de un post o cuenta (PhantomBuster/Bardeen)**
```
Caso: gente que comentó un post relevante de tu industria = audiencia tibia con señal
Salida: perfiles → enriquecer → outbound con gancho "vi que te interesó {tema}"
```

**4) Expositores/directorio de un evento (Apify actor a medida o Bardeen)**
```
Fuente: página de expositores de una feria de tu sector
Salida: empresa + web → cuentas con intención (van a ese evento = invierten en el tema)
```

## Los límites legales y de riesgo (lee esto ANTES de scrapear)

Scraping vive en una zona gris; ignorarla te cuesta la cuenta o algo peor. Reglas duras (ver `27`, y para datos personales LatAm `08`):

- **LinkedIn prohíbe el scraping en sus términos.** Herramientas como PhantomBuster automatizan sobre tu cuenta y **LinkedIn detecta y banea** patrones de bot. Si scrapeas LinkedIn: **bajo volumen**, con límites conservadores, idealmente cuenta secundaria, y asumiendo el riesgo. No hay forma "100% segura".
- **Solo datos públicos y de contexto profesional.** Scrapear datos personales protegidos, correos personales masivos o info detrás de login que no es tuya = problema legal. Correos **corporativos** de contexto B2B es lo defendible; datos personales, no.
- **Respeta rate limits.** Corre despacio (delays entre acciones); a lo bestia te detectan y te bloquean la cuenta y la IP.
- **robots.txt y términos del sitio.** Muchos sitios prohíben scraping; Google Maps y directorios tienen sus reglas. Que Apify tenga un actor no te exime.
- **Datos personales = ley aplica.** En LatAm hay leyes de protección de datos (Habeas Data en Colombia, LFPDPPP en México, LGPD en Brasil). Guardar y usar datos personales tiene obligaciones. Para outbound B2B a correos corporativos hay más margen, pero **el consentimiento y el opt-out importan** (ver `07`, `08`, `45`). Esto no es asesoría legal; ante duda, consulta.
- **Prefiere la fuente estructurada.** Si Apollo o Sales Nav ya tienen el dato de forma legítima, **úsalos en vez de scrapear** — menos riesgo, mejor calidad (ver `100`, `102`, `25`).

Regla honesta: **scrapea negocios y datos públicos con moderación; nunca hagas del scraping de LinkedIn el pilar de tu operación** porque un baneo te tumba la cuenta. Es una táctica de relleno para listas de nicho, no la base de la máquina.

## Del scrape a la lista usable (cerrar el ciclo)

```
1. Scrape (Apify Google Maps / PhantomBuster)  → nombres + empresas + pistas
2. Limpiar y desduplicar (ver 28)
3. Enriquecer email/decisor en Clay o Apollo (ver 23, 29, 101)  ← NO scrapear el email
4. Verificar emails (NeverBounce/ZeroBounce, ver 28)
5. Cargar al sequencer solo los válidos (ver 103, 104)
```
El scrape es el **paso 1** de sourcing (ver `25`), no la lista final. Sin enriquecer y verificar, tienes nombres sin forma de contactarlos bien.

## Errores comunes

- **Scrapear LinkedIn a volumen** → baneo de cuenta. Bajo y con cuidado, o no lo hagas.
- **Usar el email scrapeado directo** sin verificar → rebotes y riesgo legal; enriquece y verifica aparte (ver `28`).
- **Ignorar rate limits** → bloqueo de IP/cuenta a mitad del trabajo.
- **Guardar datos personales sin base legal ni opt-out** → problema de Habeas Data/LGPD (ver `07`, `08`).
- **Scrapear lo que ya vende una base legítima** → riesgo gratis; usa Apollo/Sales Nav (ver `100`, `102`).

## Siguiente paso

Para pymes LatAm, tu mejor receta es **Apify + Google Maps Scraper** por zona → limpiar → enriquecer en Clay (`101`) → verificar (`28`) → secuencia (`103`). Reserva el scraping de LinkedIn para casos puntuales de bajo volumen. Marco legal y ético completo → `27` y `07`; sourcing general → `25`; datos LatAm → `08`.
