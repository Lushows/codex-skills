# 158 · Procesos que se pisan

**Qué resuelve:** dos pasadas del pipeline vivas a la vez. El `rm` de temporales falla
con *Device or resource busy* y **aborta la cadena entera**; Chrome no escribe el PNG y
se calla.

---

## Cómo se manifiesta

**Caso 1 · el borrado que tumba la cadena.** Lanzar un render con otro todavía vivo:
`rm: cannot remove 'salida/_escalados': Device or resource busy`. El `rm` devuelve
distinto de cero, la cadena `rm … && python motor.py && python acabar.py` se corta ahí
y no se renderiza nada. Es el fallo **amable** de los tres: avisa.

**Caso 2 · Chrome no escribe el PNG y no lo dice.** `Failed to write file: Acceso
denegado`, ni excepción ni código distinto de cero. El fichero no se crea, o se queda el
de la pasada anterior. **De 17 piezas de texto, 5 se perdieron así** — y si lo que queda
en disco es la versión vieja, la verificación por peso la aprueba.

**Caso 3 · el MP4 a medias.** Dos `motor.py` escribiendo `salida/e03_maquina.mp4` a la
vez: el que concatena coge un archivo incompleto. `concat -c copy` no se queja, y el
episodio sale con un corte en negro.

## Por qué ocurre

Tres recursos globales que el pipeline comparte sin saberlo.

**1 · El perfil de Chrome.** Todos los scripts de render lo declaran igual:

```python
PERFIL = os.path.join(tempfile.gettempdir(), "chrome_render_paperempires")
```

`fondos.py`, `texto.py`, `fx.py`, `recursos.py`, `marca/piezas.py`, `marca/opciones.py`
y sus versiones por episodio: **siete scripts, un solo directorio de perfil**. Chrome lo
bloquea mientras lo usa; dos instancias a la vez y la segunda no escribe.

**2 · El directorio de salida.** `salida/` y `salida/_escalados` son por episodio, no
por ejecución: dos pasadas del mismo episodio pelean por los mismos archivos.

**3 · El sistema de archivos de Windows.** Un handle abierto impide borrar el archivo
*y su carpeta*. Por eso `rm -rf` da *busy*, y por eso **borrar el PNG antes de capturar
no es alternativa**: Chrome a veces lo mantiene abierto y Windows niega el borrado.

En una máquina lenta —un i7 de 2009— la tentación de solapar pasadas es constante: el
render tarda minutos y la segunda ventana está ahí.

## Cómo se caza

```bash
tasklist | grep -Ei "chrome|ffmpeg|python" | head    # ¿algo del pipeline vivo?
handle64 -nobanner "salida\_escalados"              # ¿quién tiene cogida la carpeta?
```

Y el síntoma que lo confirma sin herramientas: **relanzar solo, sin nada más abierto,
funciona**. Si el fallo desaparece con la máquina tranquila, es esto.

## La guardia automática

**Uno · un cerrojo por pipeline.** Barato, y corta el caso de raíz:

```python
import atexit, os, tempfile

def cerrojo(nombre="paperempires"):
    """Un único pipeline vivo. Si hay otro, se aborta ANTES de tocar nada."""
    ruta = os.path.join(tempfile.gettempdir(), nombre + ".lock")
    try:
        fd = os.open(ruta, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError:
        raise SystemExit(f"ABORTADO: ya hay un render vivo (pid {open(ruta).read()}). "
                         f"Si murió: del \"{ruta}\"")
    os.write(fd, str(os.getpid()).encode())
    os.close(fd)
    atexit.register(lambda: os.path.exists(ruta) and os.remove(ruta))
```

**Dos · un perfil de Chrome por proceso.** Elimina la pelea sin coordinar nada:
`PERFIL = os.path.join(tempfile.gettempdir(), f"chrome_render_paperempires_{os.getpid()}")`.
Cuesta disco temporal y ahorra el fallo silencioso más caro del bloque.

**Tres · no borrar: escribir donde no haga falta borrar.** Si cada pasada usa su propia
carpeta (`DIRS["salida"] = os.path.join(DIR_EPI, "salida", time.strftime("%Y%m%d_%H%M%S"))`),
el `rm` desaparece del pipeline y con él el *Device or resource busy*. Y cuando haya que
limpiar de verdad, que el fallo no tumbe la cadena:

```bash
rm -rf salida/_escalados || echo "no se pudo limpiar; sigo"
python motor.py ep01-lustig
```

**Cuatro · verificar por fecha, no por presencia.** Es la guardia que ya corre en
`fx_lustig.py`, y es la que salva el caso 2 cuando el perfil compartido sigue ahí:

```python
# No basta con que el PNG exista: si Chrome falla, el de la pasada anterior sigue en
# disco, el reintento lo da por bueno y la verificación aprueba una pieza que no se ha
# vuelto a generar. Se compara la FECHA del archivo, no su presencia.
antes = os.path.getmtime(out) if os.path.exists(out) else 0
for intento in range(1, 4):
    subprocess.run([CHROME, ...], capture_output=True, timeout=120)
    if (os.path.exists(out) and os.path.getsize(out) > 5120
            and os.path.getmtime(out) > antes):
        break
    print(f"      reintento {intento}: {nombre} no se volvió a escribir")
    time.sleep(2.0)          # que la instancia anterior suelte perfil y handle
else:
    fallos.append(f"{nombre}: Chrome no lo regeneró en 3 intentos")
```

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Lanzar un render con otro vivo | `rm` da *busy* y la cadena entera se aborta |
| Un solo `--user-data-dir` para siete scripts | Chrome no escribe el PNG, en silencio |
| Borrar el PNG antes de capturar | Windows niega el borrado si Chrome lo tiene abierto |
| Reintentar sin comprobar `mtime` | El PNG de la pasada anterior aprueba el reintento |
| `rm -rf … && python motor.py` | Un borrado imposible impide renderizar |
| Dos pasadas del mismo episodio | MP4 de escena a medias; `concat -c copy` no se queja |

## Relacionado

`150` el catálogo del fallo silencioso · `151` capturas en blanco que pesan lo normal ·
`157` escapes rotos al parchear código · `159` cómo se caza un fallo que no avisa ·
`98` episodios largos
