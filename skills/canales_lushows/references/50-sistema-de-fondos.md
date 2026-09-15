# 50 · Sistema de fondos

**Qué resuelve:** el fondo no se busca, se construye. Un fondo por escena, hecho por
código, con una estructura de capas fija — para que el episodio no dependa de encontrar
una foto que "sirva de ambiente" y para que todo tenga la misma piel.

---

## La regla

> **Los fondos los hacemos nosotros. El archivo va ENCIMA, en modo revista.**

Nunca al revés. Una foto de archivo estirada a pantalla completa detrás de todo es lo
que hace que un canal se vea de plantilla: la foto trae su propio grano, su propia luz
y su propio color, y a los tres planos el episodio ya no tiene idioma visual.

| Por qué se construye | Consecuencia práctica |
|---|---|
| Control total de color | El episodio puede tener un recorrido de temperatura (`51`) |
| Control del punto de luz | La mirada se guía hacia donde va el recorte (`53`) |
| Resolución libre | Se renderiza a 4320 px y el `zoompan` tiene por dónde viajar |
| Cero licencias | El fondo es CSS; no hay atribución ni riesgo de reclamo |
| Autenticidad | Es material original, no un banco de imágenes reciclado |

## El lienzo: 1920 se escribe, 4320 sale

El HTML se maqueta en **1920×1080 px CSS** y Chrome lo captura con
`--force-device-scale-factor=2.25` → **4320×2430 px**. El vídeo sale a 1920×1080.

Ese margen de 2,25× es lo que permite que `motor.py` haga `scale=4320:-2,zoompan=...`
con un recorrido del 8-16% **sin que nada se vea blando**. Maquetar directo a 4320 es un
error: los tamaños dejan de coincidir con los del resto del proyecto (recortes, rótulos,
retícula) y hay que hacer cuentas en cada línea.

## Las cinco capas (siempre en este orden)

| # | Capa | Qué hace | z-index |
|---|---|---|---|
| 1 | **Base** | El degradado de color. Define la temperatura de la escena | — |
| 2 | **Textura** | Guilloché, rejilla, fibra, suelo. Da materia y escala | — |
| 3 | **Luz** | El punto de luz que dice dónde mirar | — |
| 4 | **Superficie + viñeta** | `feTurbulence` en `overlay` + oscurecido de bordes | 200 / 210 |
| 5 | **Grano** | Ruido fino que une todo bajo la misma piel | 220 |

Las capas 4 y 5 **no se tocan entre escenas**: son la firma del canal (`58`). Lo que
cambia de una escena a otra es 1, 2 y 3.

## El esqueleto (copiar tal cual)

```html
<!doctype html><meta charset='utf-8'><style>
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1920px;height:1080px;overflow:hidden;
  font-family:'Archivo','Helvetica Neue',Arial,sans-serif}
.esc{position:relative;width:1920px;height:1080px}
.l{position:absolute}
.tex{position:absolute;inset:0;z-index:200;pointer-events:none;
  mix-blend-mode:overlay;opacity:.26}
.vin{position:absolute;inset:0;z-index:210;pointer-events:none}
.gra{position:absolute;inset:0;z-index:220;pointer-events:none;
  opacity:.22;mix-blend-mode:overlay}
</style>
<svg width="0" height="0" style="position:absolute">
  <filter id="ruido">
    <feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="2" seed="5"/>
    <feColorMatrix type="saturate" values="0"/></filter>
  <filter id="sup">
    <feTurbulence type="fractalNoise" baseFrequency="0.013 0.042" numOctaves="4" seed="11"/>
    <feColorMatrix type="saturate" values="0"/></filter>
</svg>

<!-- 1 · BASE -->
<div class="esc" style="background:radial-gradient(78% 70% at 46% 40%,
     #28402F 0%,#12201A 46%,#080D0B 100%)">

  <!-- 2 · TEXTURA -->
  <div class="l" style="inset:0;opacity:.16;background:
    repeating-linear-gradient(38deg,rgba(200,230,205,.5) 0 1px,transparent 1px 9px),
    repeating-linear-gradient(-38deg,rgba(200,230,205,.35) 0 1px,transparent 1px 13px)"></div>

  <!-- 3 · LUZ -->
  <div class="l" style="left:50%;top:-6%;transform:translateX(-50%);width:62%;height:46%;
    background:radial-gradient(58% 80% at 50% 0%,rgba(255,240,205,.22),transparent 72%)"></div>

  <!-- 4 · SUPERFICIE + VIÑETA -->
  <svg class="tex" viewBox="0 0 1920 1080" preserveAspectRatio="none">
    <rect width="1920" height="1080" filter="url(#sup)"/></svg>
  <div class="vin" style="background:radial-gradient(76% 70% at 50% 48%,
    transparent 34%,rgba(0,0,0,.64) 100%)"></div>

  <!-- 5 · GRANO -->
  <svg class="gra" viewBox="0 0 1920 1080" preserveAspectRatio="none">
    <rect width="1920" height="1080" filter="url(#ruido)"/></svg>
</div>
```

## El render

Los fondos viven en `episodio<NN>/fondos.py` y salen a `render/f_<escena>.png`:

```bash
"C:\Program Files\Google\Chrome\Application\chrome.exe" --headless=new --disable-gpu \
  --hide-scrollbars --no-sandbox --no-first-run --no-default-browser-check \
  --virtual-time-budget=2200 --force-device-scale-factor=2.25 --window-size=1920,1080 \
  --screenshot=render/f_gancho.png "file:///.../_f_gancho.html"
```

`--virtual-time-budget=2200` es el tiempo virtual que Chrome deja correr antes de
disparar. Sin él, los degradados grandes y los filtros SVG salen a medio pintar.

## Nomenclatura

`f_<id-de-escena>` — el mismo id que usa la tabla del guion visual, para que
`esc["fondo"] = "f_peso"` resuelva solo. Un fondo por escena, seis por episodio de
80-90 s. Reutilizar el mismo fondo en dos escenas seguidas se lee como que el vídeo se
quedó pegado.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Foto de archivo estirada de fondo | El episodio pierde idioma propio y hereda el color de la foto |
| Maquetar el HTML a 4320 px | Los tamaños dejan de cuadrar con recortes y rótulos |
| Saltarse la viñeta o el grano | El fondo se ve digital y el recorte no empata con él |
| Fondo demasiado detallado | Compite con el collage: el fondo es cama, no plano |
| Reutilizar el mismo fondo en escenas contiguas | Se lee como imagen congelada |
| Olvidar `--virtual-time-budget` | Capturas con filtros SVG a medio pintar |

## Relacionado

`51` · `52` · `53` · `57` · `58` · `59` · `23` empatar recorte y fondo
