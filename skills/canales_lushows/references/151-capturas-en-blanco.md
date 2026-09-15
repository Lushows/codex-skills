# 151 · Capturas en blanco que pesan lo normal

**Qué resuelve:** Chrome headless deja **bloques blancos planos** dentro del PNG sin dar
un solo error, y el peso del archivo no lo delata.

---

## Cómo se manifiesta

Encadenando seis páginas de **4320×2430** en una misma pasada, Chrome falla a veces al
rasterizar y escribe zonas planas de blanco puro. Medido en el episodio 01:

| fondo | % del cuadro en blanco |
|---|---|
| `f_gancho` | 0,33% |
| `f_pregunta` | 1,04% |
| `f_peso` | 2,36% |
| `f_maquina` | 0,71% |
| `f_piezas` | limpio |
| `f_remate` | 1,88% |

Cinco de seis. En el vídeo terminado se veían como **dos rectángulos grises pegados al
borde inferior**, y nadie los localizó hasta mirar la grilla de fotogramas.

**Y no es determinista:** el mismo fondo renderizado en solitario sale limpio. Por eso
no vale tocar parámetros y volver a mirar — hay que comprobar y reintentar.

Hay un segundo sabor, más traicionero: cuando Chrome **no escribe el PNG** (`Failed to
write file: Acceso denegado`, porque otra instancia todavía suelta el perfil o el
antivirus tiene el fichero cogido). No lanza excepción, no devuelve código distinto de
cero: se queda sin fichero, en silencio. De 17 piezas de texto, **5 se perdieron así**.

## Por qué ocurre

- **Filtros SVG a tamaño grande.** Los fondos llevaban dos `feTurbulence`. A 4320×2430
  Chrome no consigue rasterizar una superficie filtrada tan grande y abandona trozos.
  Se sustituyeron por degradados repetidos, que Chrome tesela sin problema, y el grano
  se aplica después en ffmpeg (`noise=alls=5:allf=t+u`), donde además es temporal en
  vez de congelado.
- **Alturas pequeñas.** Por debajo de ~200 px de alto, la captura sale en blanco con
  bastante frecuencia.
- **Perfil de usuario compartido** entre scripts de render (ver `158`).
- **Un script que muere a mitad** deja Chrome capturando HTML que no existe: PNG negros
  o vacíos, sin aviso.

## Cómo se caza

Contar píxeles. No hay otra: el peso no distingue un fondo bueno de uno con un 2% en
blanco, porque el PNG comprime bien las dos cosas.

```python
def blancos(ruta):
    """Cuenta píxeles casi blancos. Detecta el fallo de rasterizado de Chrome."""
    if not os.path.exists(ruta):
        return 999999
    from PIL import Image
    im = Image.open(ruta).convert("RGB").resize((960, 540))   # basta a 1/4
    px = im.load()
    return sum(1 for y in range(540) for x in range(960) if min(px[x, y]) > 235)
```

`min(px) > 235` es blanco en los tres canales: un cielo claro o una luz clave no lo
disparan, porque los fondos del canal nunca pasan de **YMAX 110-140** por diseño.

⚠️ **El filtro de peso no sirve solo.** Una captura fallida de Chrome produce un
rectángulo blanco **opaco** de unos 10 KB. Cualquier comprobación del tipo *«pesa más
de 5 KB, luego está bien»* lo aprueba. El peso es una precondición, no una prueba.

## La guardia automática

Las dos condiciones juntas, con reintento. Es el bucle que hoy corre en `fondos.py`:

```python
for nombre, r in rutas.items():
    out = os.path.join(REND, nombre + ".png")
    for intento in range(1, 4):
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                        "--no-sandbox", f"--user-data-dir={PERFIL}", "--no-first-run",
                        "--no-default-browser-check", "--virtual-time-budget=2600",
                        "--force-device-scale-factor=2.25", "--window-size=1920,1080",
                        "--screenshot=" + out, "file:///" + r.replace("\\", "/")],
                       capture_output=True, timeout=180)
        mb = os.path.getsize(out) / 1e6 if os.path.exists(out) else 0
        malo = blancos(out)
        if mb > 1.5 and malo == 0:
            break
        print(f"      reintento {intento}: {nombre} con {malo} px en blanco")
    estado = "OK   " if (mb > 1.5 and malo == 0) else "SUCIO"
    print(f"{estado} {nombre:<12} {mb:5.1f} MB   blancos: {malo}")
```

Y tres reglas de construcción que evitan la mitad de los casos:

```python
# 1 · PRIMERO todos los HTML, DESPUÉS el render. Un script que muere a mitad deja
#     a Chrome capturando páginas que no existen y los fondos salen en negro.
rutas = {nombre: escribir_html(nombre, cuerpo) for nombre, cuerpo in F.items()}

# 2 · altura mínima: por debajo de 200 px Chrome headless captura en blanco
assert h >= 200, f"{nombre} mide {h} px de alto"

# 3 · para piezas con transparencia, comparar la FECHA, no la presencia. Si Chrome
#     falla, el PNG de la pasada anterior sigue en disco y el reintento lo aprueba.
antes = os.path.getmtime(out) if os.path.exists(out) else 0
...
if os.path.exists(out) and os.path.getsize(out) > 5120 and os.path.getmtime(out) > antes:
    break
```

Borrar el PNG antes de renderizar **no** es alternativa: Chrome a veces mantiene el
fichero abierto y Windows niega el borrado.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Dar por bueno un PNG por su peso | El rectángulo blanco opaco de 10 KB pasa el filtro |
| Comprobar la existencia del archivo | El de la pasada anterior aprueba el reintento |
| Bajar la resolución «por si acaso» | Se pierde la medida y el fallo vuelve intermitente |
| Filtros SVG en superficies de 4320 px | Bloques blancos en 5 de cada 6 páginas |
| Renderizar sin haber escrito todos los HTML | Capturas negras si el script muere a mitad |
| Umbral de blanco bajo (>200) | Grita con las luces clave: comprobación que se ignora (`143`) |

## Relacionado

`150` el catálogo del fallo silencioso · `52` texturas de fondo · `59` biblioteca de
fondos · `158` procesos que se pisan · `160` la grilla de fotogramas · `161` auditar
sobre gris, nunca sobre negro
