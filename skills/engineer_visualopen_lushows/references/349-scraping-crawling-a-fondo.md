# 349 · Scraping / crawling a fondo (anti-bot, proxies, escala y lo legal)

> En 2026 el campo de batalla ya no es "qué librería" sino **reputación de IP y huella TLS**. El
> navegador es la variable que estandarizas; el stack de proxies debajo es donde se gana o se pierde.

## Scraping vs crawling
- **Crawling** = descubrir URLs (recorrer enlaces, sitemap, frontera de URLs). Output: lista de páginas.
- **Scraping** = extraer datos de una página concreta. Output: registros estructurados.
  Un pipeline real **crawlea para encontrar** y **scrapea para extraer**; sepáralos (cola de URLs → cola de parsing).

## La escalera: usa lo más barato que funcione
| Nivel | Herramienta | Cuándo |
|---|---|---|
| 1 | `httpx`/`requests` + `selectolax`/`lxml` | HTML estático, JSON oculto. **El 70% de los casos.** |
| 2 | API/endpoint interno (XHR/GraphQL) | la página llama a su propia API → pégale directo, ignora el HTML |
| 3 | Browser headless (Playwright) | el contenido se renderiza con JS y no hay endpoint usable |
| 4 | Browser + stealth + proxies residenciales | anti-bot serio (Cloudflare, DataDome, Akamai) |
| 5 | API de scraping gestionada (Scrapfly, Browserless, ZenRows) | cuando el nivel 4 te consume más que pagarlo |

**Regla de oro:** abrir un navegador es 10-100× más caro en CPU/RAM que un GET. Antes de Playwright,
abre DevTools → Network y busca el **JSON que la página ya consume**. Casi siempre está.

## Anti-bot: qué te delata (2026)
- **IP / ASN**: datacenter IPs (AWS, GCP) marcadas al instante. Residencial/móvil pasa mejor.
- **Huella TLS/JA3 + HTTP/2 fingerprint**: tu cliente debe parecer un navegador real a nivel de handshake, no solo de User-Agent.
- **Fingerprint del navegador**: canvas, WebGL, fuentes, `navigator.webdriver`, viewport vs UA coherentes.
- **Comportamiento**: timing máquina-perfecto, navegación en cadena rápida, mismos patrones repetidos. **La repetición es el mayor tell a escala.**

## Proxies (la pieza que decide)
| Tipo | Costo | Detección | Uso |
|---|---|---|---|
| Datacenter | $ | alta | sitios sin anti-bot |
| Residencial | $$$ (por GB) | baja | anti-bot medio/alto |
| Móvil (4G/5G) | $$$$ | mínima | lo más duro |
- **Rotación**: una IP por sesión lógica; rota en bloques, no por request (rotar cada hit rompe sesiones/cookies y huele a bot).
- **Sticky sessions** cuando necesitas mantener login/carrito.
- **Geo-targeting**: pide IPs del país del contenido (precios, disponibilidad cambian por región).

## Rate, cortesía y escala
- Respeta un **rate por dominio** (concurrencia limitada + delay con jitter). Mata el host y te banean a todos.
- **Backoff** ante 429/403; no martillees. Cachea respuestas (no re-bajes lo que ya tienes).
- Honra `robots.txt` salvo decisión consciente; identifícate con UA real si el sitio lo permite.
- **Arquitectura a escala**: frontera de URLs (Redis/cola) → workers de fetch → cola de parsing → store. Idempotencia por URL (no re-scrapees lo visto). Ver [[348-workflow-automation-patterns]].

## Parsing robusto
- Selectores **CSS/XPath estables** (atributos `data-*`, no clases generadas tipo `css-1a2b3c`).
- Prefiere **JSON-LD** / `__NEXT_DATA__` / estado embebido sobre raspar el DOM: más estable que el markup.
- **Valida el esquema** de salida (pydantic/zod). Si el sitio cambia, falla ruidoso, no guardes basura.
- Maneja **lazy-load/scroll infinito** y paginación por cursor.

## Legal / ético (no es opcional)
- Scrapear datos **públicos** suele ser defendible (*hiQ v. LinkedIn*), pero: **ToS**, **copyright**,
  y **datos personales (GDPR/CCPA)** son líneas rojas distintas. Datos personales → base legal + minimización.
- No saltes muros de pago/login para eludir acceso. No revendas contenido protegido.
- Consulta legal para uso comercial serio. [no verificado para tu jurisdicción]

## Gotchas
- Hardcodear el HTML de hoy → rompe mañana; centraliza selectores y monitoriza tasa de extracción.
- Proxies datacenter para Cloudflare → bloqueo inmediato; sube a residencial.
- Sin caché ni idempotencia → re-bajas todo en cada corrida, quemas proxies y tiempo.
- Un solo proceso headless para todo → OOM; aísla contextos y limita concurrencia.

Cruza con [[36-datasets-scraping-captioning]], [[350-browser-automation-playwright]] y [[348-workflow-automation-patterns]].

**Fuentes:** [browserless: stealth scraping at scale](https://www.browserless.io/blog/stealth-scraping-puppeteer-playwright) · [scrapfly: playwright stealth](https://scrapfly.io/blog/posts/playwright-stealth-bypass-bot-detection) · [proxyhorizon 2026](https://www.proxyhorizon.com/blog/playwright-vs-puppeteer-scraping).
