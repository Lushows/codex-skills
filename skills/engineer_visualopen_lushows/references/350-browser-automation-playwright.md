# 350 · Browser automation (Playwright / Puppeteer: headless, stealth, CI, captchas)

> Cuando no hay endpoint que pegar, manejas un navegador real. Playwright es el default 2026 para
> ~80% de proyectos nuevos; pero el navegador es la variable fácil — la IP y la huella TLS deciden.

## Playwright vs Puppeteer (2026)
| Eje | Playwright | Puppeteer |
|---|---|---|
| Navegadores | Chromium + **Firefox + WebKit** | Chromium (Firefox parcial) |
| Lenguajes | JS/TS, **Python**, .NET, Java | JS/TS |
| Aislamiento | **10+ contextos/proceso** | ~1 proceso por sesión |
| Auto-wait | nativo (menos flaky) | manual |
| Intercepción red | API limpia (Shopify/Next GraphQL) | sí, más verbosa |
| Stealth maduro | `playwright-stealth` Python **mantenido (v2.x, 2026)** | `puppeteer-extra-stealth` **deprecado feb-2025** |

**Elige Playwright** para proyecto nuevo, pipeline en Python, multi-navegador, o menos flakiness.
**Quédate en Puppeteer** si tu prod ya es JS+Puppeteer y solo necesitas Chromium. Aviso clave: el
plugin stealth de Puppeteer (Node) **no recibe updates desde feb-2025** y `playwright-extra` (Node)
no se actualiza desde marzo-2023 → ambos los detectan Cloudflare Bot Fight y DataDome 2024+. En
**Python**, `playwright-stealth` sí está vivo y sirve contra checks básicos de fingerprint.

## Headless en 2026
Usa el **headless "nuevo"** de Chromium (`--headless=new`), que comparte binario y huella con el modo
visible; el viejo headless tenía señales propias detectables. Aun así, headless puro deja rastros
(WebGL, fuentes, `navigator.webdriver`); para anti-bot serio combina con stealth + proxies residenciales.

## Checklist de stealth (Playwright y Puppeteer)
- `navigator.webdriver = false` (lo hace stealth; verifícalo).
- **Coherencia total**: User-Agent ↔ `sec-ch-ua` (client hints) ↔ viewport ↔ plataforma ↔ idioma/zona horaria. Una incoherencia te marca.
- Fija **locale, timezone, geolocalización** por contexto y mantenlos estables en la sesión.
- No pidas permisos innecesarios; persiste cookies dentro de la sesión y caduca a propósito.
- **Timing humano**: delays con jitter, sin cadenas de navegación máquina-perfectas. La repetición de patrones es el delator real a escala.
- Reusa **`storageState`** (cookies+localStorage) para no re-loguear en cada corrida.

## Captchas
- **Primero evita**: mejor IP/huella/comportamiento reducen el captcha de raíz. El captcha es síntoma, no causa.
- **reCAPTCHA/hCaptcha/Turnstile**: servicios de resolución (2Captcha, CapSolver) o APIs de scraping que lo gestionan. Costo por resolución.
- **Cloudflare/DataDome challenge**: rara vez lo "resuelves" con un click; necesitas IP residencial + huella correcta + sesión persistente, o una scraping API gestionada.

## Performance y recursos
- Un proceso headless come ~100-300MB RAM; **aísla contextos** (`browser.newContext()`) en vez de abrir N navegadores. Mucho más barato.
- **Bloquea recursos inútiles** (imágenes, fuentes, analytics) con route interception → 2-5× más rápido y menos ancho de banda.
- **Limita concurrencia** (pool de páginas); demasiadas pestañas → OOM. Reusa el navegador entre jobs (warm).
- Cierra siempre páginas/contextos (`finally`) — las fugas tumban el worker en horas.

## CI / entornos efímeros
- Imagen oficial `mcr.microsoft.com/playwright` (trae navegadores + libs del sistema). En custom: `npx playwright install --with-deps`.
- En Docker/Lambda corre como usuario no-root o pasa `--no-sandbox` (con cuidado: solo en entornos confiables).
- **Trace viewer** (`--trace on`) para depurar fallos no reproducibles localmente; guarda el trace como artefacto de CI.
- Sé determinista: versión de navegador pineada, `storageState` semillado, retries con `expect`/auto-wait, no `sleep` fijos.

## Gotchas
- `waitForTimeout(3000)` fijo → flaky; usa `waitForSelector`/`expect` (auto-wait).
- Headless viejo o UA "HeadlessChrome" → detección instantánea.
- Stealth plugin de Node desactualizado → falsa sensación de invisibilidad contra anti-bot moderno.
- No cerrar contextos → fuga de memoria → caída del worker.
- Proxy datacenter + browser perfecto → igual te banean: la IP manda.

Cruza con [[349-scraping-crawling-a-fondo]] y [[281-testing-frontend-playwright-vitest]].

**Fuentes:** [scrapewise: playwright stealth 2026](https://scrapewise.ai/blogs/playwright-stealth-2026) · [scrapfly: puppeteer stealth](https://scrapfly.io/blog/posts/puppeteer-stealth-complete-guide) · [proxyhorizon: playwright vs puppeteer](https://www.proxyhorizon.com/blog/playwright-vs-puppeteer-scraping).
