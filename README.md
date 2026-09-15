# Skills de Lushows — para Codex CLI (y Claude Code)

18 skills propias, listas para instalar en cualquier equipo.

## Antes de empezar

En el equipo nuevo necesitas dos cosas ya instaladas:

1. **Codex CLI** (o Claude Code). Este repo solo copia archivos; no instala el programa.
2. **git** — para comprobar, abre una terminal y escribe `git --version`.
   Si dice "no se reconoce", bajalo de https://git-scm.com/downloads
   (o usa la via del ZIP, mas abajo).

Como el repo es **privado**, al clonar te va a pedir tu cuenta de GitHub (Lushows).

## Instalar

### Windows

```powershell
git clone https://github.com/Lushows/codex-skills.git
cd codex-skills
powershell -ExecutionPolicy Bypass -File .\instalar.ps1
```

### Mac / Linux

```bash
git clone https://github.com/Lushows/codex-skills.git
cd codex-skills
bash instalar.sh
```

Luego **cierra y vuelve a abrir Codex**. Las skills se activan solas cuando lo que
pides coincide con su descripcion (no hay que invocarlas a mano).

> El instalador **sobrescribe** una skill del mismo nombre que ya exista.
> Este repo es la fuente de verdad. Si cambiaste algo en el otro equipo, subelo aqui primero.

### Sin git: descargar el ZIP

1. Arriba en esta pagina: boton verde **Code** -> **Download ZIP**.
2. Descomprimelo completo (no ejecutes nada desde dentro del ZIP).
3. Entra a la carpeta y corre el instalador que te toque (`instalar.ps1` o `instalar.sh`).

## Como saber si funciono

Abre Codex y pide algo que dispare una skill, por ejemplo:

> "arma el modelo financiero de un negocio de X"  -> deberia entrar `economist_lushows`

Si no pasa nada, revisa que las carpetas esten donde van:

```bash
ls ~/.codex/skills        # Mac / Linux
dir $HOME\.codex\skills   # Windows PowerShell
```

Deberias ver 18 carpetas, cada una con su `SKILL.md` adentro.

### A mano (si prefieres)

Copia cada carpeta de `skills/` dentro de `~/.codex/skills/`.
Codex busca en este orden: `.codex/skills/` del proyecto, `.codex/skills/` de la raiz
del repo, `~/.codex/skills/` (personal), `/etc/codex/skills/` (sistema).

## Que hay adentro

| Skill | Para que |
|---|---|
| `AVIS_lushows` | Cerebro de AVIS, el agente de AVISPA'O (cumplimiento + facturas Colombia) |
| `Matematicas_lushows` | Matematico error-cero: todo calculo se ejecuta en codigo y se verifica |
| `Quimico_lushows` | Quimico-farmaceutico: analisis, COA, extractos, cannabis y hongos |
| `SDR_OUTBOUND_LUSHOW` | Outbound y lead-gen B2B: prospectar y agendar |
| `canales_lushows` | Canales de contenido: documentales, guion, pipeline de video |
| `contador_lushows` | Contador publico: libros que cuadran, NIIF, DIAN, nomina |
| `desingweb-lushows` | Diseno y construccion web nivel Awwwards |
| `directorcreativo_lushows` | Director creativo: marca, logo, identidad, packaging |
| `dropshipping_lushows` | Que vender y como: producto, paises, ecommerce |
| `economist_lushows` | Economista y estratega: viabilidad, modelo financiero, precios |
| `editpro_lushows` | Edicion de video: cortes, ritmo, color, subtitulos, ffmpeg |
| `engineer_visualopen_lushows` | Ingenieria full-stack + IA visual open-source en GPU serverless |
| `facebook_ads_lushows` | Media buyer Meta: campanas, pixel/CAPI, escalar |
| `google_ads_lushows` | Google Ads / paid search |
| `optimizer_tokens_lushows` | Bajar costo y latencia de apps LLM |
| `tiktok_ads_lushows` | Media buyer TikTok |
| `trading_lushows` | Trading: AGENTE TRADING, riesgo, analisis, paso a real |
| `ventas_lushows` | Ventas: prospeccion, cierre, negociacion |

## Tambien sirven en Claude Code

Mismo contenido, otra carpeta: copia `skills/*` dentro de `~/.claude/skills/`.
Los instaladores lo preguntan.
