# 153 · Índices corridos

**Qué resuelve:** el índice del bucle de Python y el índice de entrada de ffmpeg son
dos cosas distintas. Cuando se separan, **la escena entera falla y el episodio queda
desincronizado de la voz desde ahí hasta el final.**

---

## Cómo se manifiesta

```
  FALLO maquina:
    Invalid file index 7 in filtergraph description.
```

Un mensaje de ffmpeg, sí — pero en `stderr` de un subproceso, no una excepción de
Python. Si no se comprueba `returncode`, el bucle sigue, la escena no se genera y al
concatenar faltan 16 segundos. **Todo lo que viene después suena sobre la imagen
equivocada**, y el desfase crece escena a escena.

En una tabla de 400 eventos, un elemento que se descarta a mitad de escena mueve todos
los índices posteriores en uno. El síntoma no aparece en el elemento descartado:
aparece en el siguiente.

## Por qué ocurre

`render_escena()` construye dos listas en paralelo:

- `entradas` — los `-i` que se le pasan a ffmpeg. El fondo es `0:v`, el primer elemento
  `1:v`, el segundo `2:v`…
- `esc["elementos"]` — la tabla del guion visual, que incluye elementos que **pueden no
  llegar a añadirse**.

Un elemento se descarta cuando su vida resuelta es nula:

```python
e0 = max(t0, base + ele.get("offset", 0)) - t0
e1 = min(dur, e0 + ele.get("dura", 2.0))
if e1 <= e0:
    continue          # el ancla cayó fuera de la escena, o dura 0
```

Con `for i, ele in enumerate(esc["elementos"])`, ese `continue` **no detiene el
contador**: el elemento 5 se descarta, el 6 se añade como entrada real nº 5 y el filtro
lo referencia como `[6:v]`. ffmpeg pide una entrada que no existe.

Lo mismo ocurre con cualquier índice derivado de la posición en la lista de origen:
etiquetas `[e6]`/`[v6]`, tiempos por posición, colores por turno.

## Cómo se caza

Comparar las dos cuentas antes de llamar a ffmpeg:

```python
declarados = len(esc.get("elementos", []))
reales = (len(entradas) - 8) // 8      # 8 tokens por entrada -loop..-i
usados = max(int(m) for m in re.findall(r"\[(\d+):v\]", ";".join(filtros)))
print(f"{esc['id']:<12} declarados {declarados}  entradas {reales}  "
      f"mayor índice usado {usados}   {'OK' if usados < reales + 1 else 'CORRIDO'}")
```

Y, sobre el episodio ya montado, la prueba que lo confirma en un minuto: **la duración
del mudo tiene que coincidir con la del guion visual.**

```bash
ffprobe -v error -show_entries format=duration -of csv=p=0 salida/_mudo.mp4
# 74.72   frente a  sum(e["fin"]-e["ini"] for e in ESCENAS) = 91.04  -> falta una escena
```

## La guardia automática

Dos piezas, y hacen falta las dos. La primera: **el índice lo lleva un contador propio
que sólo avanza cuando la entrada se añade de verdad.** Es lo que hoy hace `motor.py`:

```python
n = 0
for ele in esc.get("elementos", []):
    ...
    if e1 <= e0:
        continue
    # El índice lo manda la posición REAL en 'entradas', no el del bucle: si un
    # elemento se descarta arriba, enumerate() sigue contando y ffmpeg acaba
    # pidiendo una entrada que no existe.
    n += 1
    entradas += ["-loop", "1", "-framerate", str(FPS), "-t", f"{dur:.3f}",
                 "-i", escalado(buscar(ele["r"]), anchura)]
    filtros.append(f"[{n}:v]scale={anchura}:-1,format=rgba,...[e{n}]")
    filtros.append(f"[{ultimo}][e{n}]overlay=...[v{n}]")
    ultimo = f"v{n}"
```

La segunda: **no concatenar si falta una escena.** Un episodio corto pero sincronizado
es recuperable; uno completo y desfasado hay que verlo entero para descubrirlo.

```python
r = subprocess.run(cmd, capture_output=True, text=True)
if r.returncode != 0:
    print(f"  FALLO {esc['id']}:\n    " + r.stderr.strip().split("\n")[-1][:220])
    return None
...
if len(partes) != len(ESCENAS):
    raise SystemExit(
        f"\nABORTADO: {len(ESCENAS)-len(partes)} escena(s) fallaron. "
        f"Concatenar las demás dejaría el episodio desincronizado de la voz "
        f"desde ahí hasta el final.")
```

`capture_output=True` sin `returncode` es el peor de los dos mundos: se traga el error
y no lo comprueba. **Si se captura, se lee.**

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| `enumerate()` sobre una lista con `continue` | El filtro pide una entrada que no existe |
| `subprocess.run(capture_output=True)` sin mirar `returncode` | ffmpeg falla en silencio dentro de un bucle |
| Concatenar las escenas que sí salieron | Episodio entero desincronizado de la voz |
| Descartar elementos después de construir el filtro | Mismo problema, al revés: entradas huérfanas |
| Etiquetas `[e{i}]` con el índice del bucle | Colisión de etiquetas si dos escenas comparten nombre |
| Fiarse de que el MP4 existe | Existe, dura menos y suena sobre la imagen equivocada |

## Relacionado

`150` el catálogo del fallo silencioso · `17` medir el montaje · `29` plantillas de
escena · `79` `xfade` a fondo · `159` cómo se caza un fallo que no avisa ·
`98` episodios largos
