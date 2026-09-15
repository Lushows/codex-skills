# 69 · Construir un efecto nuevo

**Qué resuelve:** el camino completo de una idea a un PNG animable que el motor pueda
montar, con la verificación que impide que un archivo vacío llegue al render final.

---

## El método, en siete pasos

| # | Paso | Criterio de salida |
|---|---|---|
| 1 | **La frase** | Escribir la frase exacta de la locución que el efecto responde. Si no hay frase, no hay efecto (`60`) |
| 2 | **El rótulo** | Nombrarlo en cuatro palabras. Si no se puede, el espectador tampoco va a poder |
| 3 | **Estático o serie** | ¿Cambia por dentro? Serie. ¿Sólo se mueve? Estático: el movimiento lo pone el motor |
| 4 | **La caja** | Ancho y alto en píxeles, y en qué posición de la retícula va a caer (`20`) |
| 5 | **HTML o PIL** | HTML si hay texto, cajas o tipografía. PIL si hay muchas repeticiones con azar |
| 6 | **Generar** | Escribir TODOS los HTML primero, renderizar después |
| 7 | **Verificar** | Peso, alfa y prueba sobre gris. No se da por bueno antes |

**El paso 6 no es una manía.** Ya pasó: un script murió a la mitad, los últimos HTML no
existían, Chrome capturó páginas en blanco sin protestar y el render salió con huecos
negros. Escribir todo y renderizar después convierte ese fallo en un error visible.

## El generador

Cualquier efecto nuevo se declara igual que los de `fx.py`: una entrada en `F` con
`(ancho, alto, cuerpo)`. Para uno local de un episodio, un archivo aparte con el mismo
bucle:

```python
# episodio02/fx_local.py
import io, os, subprocess, tempfile
BASE   = os.path.dirname(os.path.abspath(__file__))
DEST   = os.path.join(BASE, "..", "fx")
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
PERFIL = os.path.join(tempfile.gettempdir(), "chrome_render_paperempires")
CSS    = """*{margin:0;padding:0;box-sizing:border-box}
html,body{background:transparent;overflow:hidden;font-family:'Archivo',Arial,sans-serif}
.l{position:absolute} .mono{font-family:ui-monospace,'Consolas',monospace}
.oro{color:#E8C547} .rojo{color:#E3120B} .papel{color:#EDE6D6}"""

F = {}
F["mi_efecto"] = (760, 420, """<div style="position:relative;width:760px;height:420px">
  ...
</div>""")

if __name__ == "__main__":
    os.makedirs(DEST, exist_ok=True)
    rutas = []
    for nom, (w, h, cuerpo) in F.items():          # 1) escribir TODOS los HTML
        r = os.path.join(DEST, "_" + nom + ".html")
        io.open(r, "w", encoding="utf-8").write(
            f"<!doctype html><meta charset='utf-8'><style>{CSS}"
            f"html,body{{width:{w}px;height:{h}px}}</style>{cuerpo}")
        rutas.append((nom, w, h, r))
    for nom, w, h, r in rutas:                      # 2) renderizar después
        out = os.path.join(DEST, nom + ".png")
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                        "--no-sandbox", f"--user-data-dir={PERFIL}", "--no-first-run",
                        "--no-default-browser-check",
                        "--default-background-color=00000000",
                        "--virtual-time-budget=1600", f"--window-size={w},{h}",
                        "--screenshot=" + out, "file:///" + r.replace("\\", "/")],
                       capture_output=True, timeout=120)
        print(f"{'OK ' if os.path.exists(out) else 'FALLO '}{nom:<18}{w}x{h}")
```

Tres banderas que no se quitan: `--default-background-color=00000000` (sin ella el PNG
sale con fondo blanco y tapa la escena), `--user-data-dir` aislado (matar Chrome
globalmente le cierra el navegador al usuario) y `--virtual-time-budget` (sin él los
degradados y los filtros SVG salen a medio pintar).

## La verificación

```python
# verificar_fx.py — se ejecuta después de generar, siempre
import glob, os
from PIL import Image

MIN_KB = 4
for p in sorted(glob.glob("fx/*.png")):
    kb = os.path.getsize(p) / 1024
    im = Image.open(p).convert("RGBA")
    a  = im.getchannel("A")
    bb = a.getbbox()                                   # None = todo transparente
    h  = a.histogram()
    opaco = h[255] / (im.width * im.height)
    medio = sum(h[8:248]) / (im.width * im.height)     # alfa intermedio = halo
    fallos = []
    if kb < MIN_KB:            fallos.append(f"peso {kb:.1f} KB")
    if bb is None:             fallos.append("PNG VACÍO")
    elif (bb[2]-bb[0]) < im.width*0.25:  fallos.append("contenido en 1/4 del lienzo")
    if opaco < 0.002:          fallos.append("sin píxeles opacos")
    if medio > 0.28:           fallos.append(f"alfa sucio {medio:.0%}")
    print(("FALLO " if fallos else "OK    ") + os.path.basename(p) +
          ("  ·  " + "; ".join(fallos) if fallos else f"  {kb:6.1f} KB"))
```

Qué mira cada comprobación:

| Comprobación | Qué caza |
|---|---|
| **Peso mínimo** | La captura en blanco. Un PNG grande que pesa 3 KB está vacío |
| **`getbbox()` del alfa** | Todo transparente: el HTML no pintó nada |
| **Ancho del contenido** | El efecto se dibujó en una esquina porque la caja está mal |
| **Píxeles opacos** | Todo semitransparente: falta un `background` o sobra un `opacity` |
| **Alfa intermedio > 28%** | Halo o borde comido: se verá como figura fantasma sobre el fondo |

## La prueba sobre gris

**Nunca sobre negro.** El fondo del canal es oscuro y sobre oscuro los halos y los bordes
sucios se disimulan; el episodio final los enseña justo cuando el fondo se aclara.

```bash
# una hoja de contactos de todos los efectos sobre gris medio
ffmpeg -f lavfi -i color=c=0x808080:s=1920x1080 -pattern_type glob -i "fx/*.png" \
  -filter_complex "[1:v]scale=300:-1,tile=6x4:padding=8:color=0x808080[t];
                   [0:v][t]overlay=(W-w)/2:(H-h)/2" -frames:v 1 -y fx/_contactos.png
```

Sobre ese contacto se mira, en este orden: **borde** (¿hay un halo claro?), **relleno**
(¿se transparenta lo que debería ser opaco?), **legibilidad del rótulo** al 300 px de
ancho —que es más o menos lo que ocupa en pantalla— y **peso visual** contra los demás.

## Última puerta: en movimiento

Un efecto no está terminado hasta verlo montado. Se hace una escena de prueba de 4 s con
el fondo de la escena real, no con un color plano: el efecto empata o no empata con **su**
fondo (`23`), y sobre un gris plano eso no se puede juzgar.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Renderizar mientras se escriben los HTML | Chrome captura páginas en blanco sin dar error |
| Dar por bueno un PNG porque existe | Un 4320×2430 de 62 KB está vacío y el vídeo sale negro |
| Auditar sobre fondo negro | Los halos aparecen en el render final, cuando ya no hay tiempo |
| Sin `--default-background-color=00000000` | PNG con fondo blanco que tapa la escena |
| Matar Chrome globalmente | Se le cierra el navegador al usuario |
| Sin `--virtual-time-budget` | Degradados y filtros SVG a medio pintar |
| Probar el efecto sobre color plano | No se sabe si empata con el fondo de su escena |
| Empezar por el dibujo y no por la frase | Un efecto bonito que no responde a nada |

## Relacionado

`60` el criterio · `61` `62` `64` `65` ejemplos completos · `23` empatar con el fondo · `68` la lista negra
