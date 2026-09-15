# 21 — Encontrar cuentas por nicho

Aquí empieza el trabajo de verdad: sacar la **lista de empresas** (las "cuentas") que encajan con tu nicho. Este es el paso que la gente pide cuando dice "consígueme correos de empresas de tal sector". Pero primero van las **empresas**; la persona y el correo vienen después (`22`, `23`). Una cuenta bien elegida es una que cumple tu ICP (`10`): sector, tamaño, ciudad, madurez. Este módulo te da las fuentes reales, fuente por fuente, con el paso a paso para extraer un listado limpio de cada una.

## El principio: cruza fuentes, no dependas de una

Ninguna fuente tiene todo. LinkedIn es fuerte en empresas con presencia digital pero débil en la ferretería de barrio; Google Maps es oro para negocios locales con local físico pero flojo en SaaS; las Cámaras de Comercio tienen el universo formal de un país pero datos viejos. La jugada ganadora: **elige 2–3 fuentes según tu nicho, extrae de cada una, y cruza/deduplica** (ver `28`). Así cubres más mercado y validas: si una empresa aparece en LinkedIn y en la Cámara, existe de verdad.

Decide primero qué tipo de nicho tienes:

| Tu nicho es… | Fuentes primarias | Fuentes de apoyo |
|---|---|---|
| Negocios locales con local (restaurantes, clínicas, gimnasios, tiendas) | Google Maps, directorios locales, gremios | Cámaras de Comercio, Instagram |
| Empresas B2B/servicios/SaaS | LinkedIn Sales Navigator, Apollo, Crunchbase | directorios de industria, gremios |
| Formales de un país (cualquier sector) | Cámara de Comercio, RUES (Colombia) | LinkedIn, Maps |
| Vendedores/marcas de un producto | Marketplaces (Mercado Libre, Amazon), ferias | Instagram, gremios |
| Tech / startups | Crunchbase, LinkedIn, BuiltWith (technographics `134`) | Product Hunt, Y Combinator list |

## Fuente por fuente — paso a paso

### 1. LinkedIn / Sales Navigator (el motor B2B)
La mejor fuente para empresas con presencia profesional. Filtras por sector, tamaño (headcount), geografía y crecimiento. Búsqueda de *Companies* en Sales Navigator y guardas la lista de cuentas.
- Paso: Sales Nav → Account filters → Industry + Company headcount + Geography + (opcional) Headcount growth / Recent hires → guardar como Account List.
- El detalle de filtros booleanos y ejemplos reales de búsqueda están en `26` (y a fondo en `102`).
- Extraer las empresas a una hoja: Apollo (`25`) o un scraper (`27`, `109`) leen esa búsqueda.

### 2. Directorios de industria y asociaciones gremiales
Cada sector tiene su directorio o su gremio. En LatAm son mina de oro porque listan al universo formal del rubro con web y a veces teléfono. Ejemplos: cámaras sectoriales (gastronómica, hotelera, construcción), ACOPI, FENALCO, ANDI (Colombia), directorios como PáginasAmarillas, Guía local de proveedores, marketplaces B2B (Cylex, eInforma).
- Paso: busca "asociación/gremio/cámara de [tu sector] [país]" → entra al **directorio de afiliados** → normalmente hay un listado público con nombre + web. Extrae con scraper o a mano si son pocos (`27`).
- Ventaja: quien está afiliado a un gremio es un negocio serio y formal = mejor fit.

### 3. Cámaras de Comercio / registros mercantiles
El registro oficial de empresas de un país. En Colombia: **RUES** (rues.org.co) y el portal de cada Cámara permiten buscar por actividad económica (código CIIU), ciudad y estado (activa/renovada). Da razón social, NIT, a veces dirección.
- Paso (Colombia): RUES → búsqueda por CIIU + municipio → exporta lo que se pueda; complementa el correo/decisor con `22`–`23` porque el registro rara vez trae al decisor ni email.
- Cuidado legal: datos de registro público ≠ permiso para email masivo sin filtro. Respeta Habeas Data (ver `49`, `181`).

### 4. Google Maps (el rey del negocio local)
Insustituible para cualquier nicho con local físico. Cada ficha trae nombre, categoría, dirección, teléfono, web, horario, reseñas (proxy de tamaño).
- Paso manual: busca "[tipo de negocio] en [ciudad/zona]" → recorre resultados → copia nombre, web, teléfono.
- Paso a escala: scrapers de Maps (ver `27` y `109`) — Apify "Google Maps Scraper", PhantomBuster, Instant Data Scraper — extraen cientos de fichas con teléfono y web a CSV. **Es de las fuentes más legales y ricas para PYMES LatAm.**
- El teléfono de Maps suele ser el WhatsApp del negocio (ver `24`) — clave para outbound LatAm.

### 5. Crunchbase (startups, funding, empresas tech)
Para B2B tech/SaaS. Filtras por industria, ubicación, rondas de inversión, número de empleados. La señal de **funding** (levantaron plata) es un trigger de compra potentísimo (ver `14`, `135`): tienen presupuesto y están creciendo.
- Paso: Crunchbase → Search Companies → Industry + Location + Last funding date → exporta (plan Pro).
- Alternativas más baratas: Apollo también trae señal de funding; PitchBook es enterprise.

### 6. Marketplaces y plataformas
Si vendes a quien vende un producto, el marketplace ES tu directorio: Mercado Libre, Amazon, Falabella (vendedores), Airbnb (anfitriones), Rappi/DoorDash (restaurantes). Los perfiles de vendedor traen nombre de tienda y a veces contacto.
- Paso: filtra por categoría/ubicación en el marketplace → extrae vendedores con scraper (`27`).

### 7. Otras señales de dónde viven tus cuentas
- **Quién anuncia** en Google/Meta en tu nicho (usa la Meta Ad Library) = tienen presupuesto de marketing.
- **Quién asiste a ferias/eventos** del sector (listas de expositores públicas).
- **Competidores de un cliente tuyo actual** (busca "empresas como [cliente]" o similares en Crunchbase/LinkedIn).
- **Clientes de tu competencia** (displacement, ver `19`).

## Ejemplo real: 100 restaurantes medianos en Bogotá

```
Objetivo: restaurantes independientes, 2–10 sucursales, Bogotá.
1. Google Maps → "restaurantes en Chapinero / Usaquén / Zona T"
   → Apify Google Maps Scraper → CSV con nombre, web, teléfono, reseñas.
2. Filtro fit: >200 reseñas (proxy de tamaño), tiene web propia.
3. Cruza con Instagram (bio suele traer WhatsApp) y con RUES por CIIU 5611.
4. Decisor (dueño/gerente) → LinkedIn/`22`; correo → `23`; wa → `24`.
Resultado: ~100 cuentas con fit real + teléfono, en una tarde.
```

## Errores comunes (qué NO hacer)

- Quedarte con UNA fuente y creer que tienes el mercado.
- Copiar TODO sin filtrar por fit — el registro/Maps trae de todo, aplica tu ICP (`10`).
- Guardar la empresa pero no la web: sin dominio no puedes deducir el correo (`23`).
- Ignorar el estado (empresa "cancelada"/cerrada en RUES o Maps).

## Siguiente paso

Con 50–100 cuentas con fit y su `sitio_web`, pasa a `22` para dar con el decisor de cada una, y luego `23` para el correo. Si el nicho es local LatAm, prioriza Maps + WhatsApp (`24`, `59`).
