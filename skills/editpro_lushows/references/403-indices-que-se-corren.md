# 403 — Índices que se corren

**Qué resuelve:** en un filtergraph generado por código hay **dos numeraciones distintas que parecen la
misma**: la posición del elemento en la tabla del guion y el índice de su entrada `-i` en ffmpeg. Mientras
ningún elemento se salte, coinciden. El día que uno se salta, se separan para siempre y **la escena entera
se cae** — o, peor, el vídeo sale corto y nadie se entera.

> **Frontera.** `canales_lushows/153` cuenta este fallo desde el motor del canal: por qué ocurre, la
> guardia que hoy vive en `motor.py` y el aborto del episodio. **Este módulo es la parte medida:** cuándo
> muerde exactamente, qué dice ffmpeg palabra por palabra, cómo se detecta antes de gastar un render y en
> qué otros filtros aparece el mismo bicho. No se repite nada de allí.

---

## 1. Las dos numeraciones

```python
for i, ele in enumerate(esc["elementos"]):      # ← posición en la TABLA
    ...
    if e1 <= e0:
        continue                                # el ancla cayó fuera: no se añade nada
    entradas += ["-i", escalado(buscar(ele["r"]), anchura)]
    filtros.append(f"[{i+1}:v]scale=...")       # ← índice de ENTRADA en ffmpeg
```

`continue` no detiene a `enumerate()`. Se descarta el elemento 2, el 3 se añade como entrada real número 2
y el filtro lo pide como `[3:v]`. **La entrada `[3:v]` no existe.**

El arreglo vivo en `motor.py:193` es un contador que avanza solo cuando la entrada se añade de verdad:

```python
n = 0
for ele in esc.get("elementos", []):
    ...
    if e1 <= e0:
        continue
    n += 1                                      # ← solo aquí
    entradas += ["-loop","1","-framerate",str(FPS),"-t",f"{dur:.3f}",
                 "-i", escalado(buscar(ele["r"]), anchura)]
    filtros.append(f"[{n}:v]scale={anchura}:-1,...[e{n}]")
    filtros.append(f"[{ultimo}][e{n}]overlay=...[v{n}]")
    ultimo = f"v{n}"
```

---

## 2. Qué dice ffmpeg, literalmente

Reproducido hoy con ffmpeg 8.1.2 sobre tres elementos de los que se descarta el segundo:

```
entradas -i : ['bg.png', 'e0.png', 'e2.png']
filtros     : ...[1:v]scale=160:-1[e1];[bg][e1]overlay=60:100[v1];
              [3:v]scale=160:-1[e3];[v1][e3]overlay=420:100[v3];...

[fc#0 @ …] Invalid file index 3 in filtergraph description …
Error binding filtergraph inputs/outputs: Invalid argument
returncode = 4294967274          # -22 (EINVAL) leído como sin signo
```

Dos cosas de ese bloque importan más que el mensaje:

- Llega por **`stderr` de un subproceso**, no como excepción de Python. Un bucle que no mira
  `returncode` sigue como si nada.
- `4294967274` es `-22` en complemento a dos. Cualquier comprobación del tipo `if r.returncode < 0` no
  lo atrapa en Windows. **Se comprueba `!= 0`, siempre.**

---

## 3. Cuándo muerde y cuándo se esconde

Aquí está la razón de que este fallo sobreviva meses en un repo. Cuatro elementos, mismo código, variando
cuál se descarta:

| caso | `enumerate()` | contador propio |
|---|---|---|
| no se salta ninguno | ✅ OK | ✅ OK |
| se salta el **2.º** | ❌ `Invalid file index 4` | ✅ OK |
| se salta el **3.º** | ❌ `Invalid file index 4` | ✅ OK |
| se salta el **último** | ✅ OK | ✅ OK |
| se saltan los **dos últimos** | ✅ OK | ✅ OK |

**Si lo que se descarta está al final, los índices siguen siendo contiguos y no pasa nada.** El código con
el fallo funciona perfectamente durante semanas, hasta el día en que un ancla del medio de una escena
deja de encontrar su palabra. Entonces no falla el elemento descartado: falla el siguiente.

---

## 4. La aritmética del desastre silencioso

Fallar la escena es lo bueno. Lo malo es concatenar las demás. Sobre `ep01-lustig`:

| escena | ini | fin | dur |
|---|---|---|---|
| muerte | 0,00 | 16,15 | 16,15 |
| **oficio** | **16,15** | **22,88** | **6,73** |
| nombre | 22,88 | 34,41 | 11,53 |
| torre | 34,41 | 50,29 | 15,88 |
| metodo | 50,29 | 63,45 | 13,16 |

Si cae `oficio` y se concatena el resto, el mudo dura **56,72 s en vez de 63,45 s**. La voz no se ha
movido: desde el segundo 16,15 **toda la imagen va 6,73 s adelantada respecto a lo que se está
contando**, y el desfase se arrastra hasta el final. El MP4 existe, se abre, se ve bien en el primer
vistazo. Por eso `motor.py:272` aborta:

```python
if len(partes) != len(ESCENAS):
    raise SystemExit(f"\nABORTADO: {len(ESCENAS)-len(partes)} escena(s) fallaron. …")
```

La comprobación de un segundo que lo confirma sobre cualquier montaje ya hecho:

```bash
ffprobe -v error -show_entries format=duration -of csv=p=0 salida/_mudo.mp4
# 56.72   frente a  sum(e["fin"]-e["ini"] for e in ESCENAS) = 63.45  -> falta una escena
```

---

## 5. La familia entera: dónde más aparece el mismo bicho

Cualquier sitio donde un número se derive de la **posición en una lista de origen** en vez de la posición
en la lista que de verdad se construyó:

| Sitio | Cómo se manifiesta |
|---|---|
| `[{i}:v]` con `i` del bucle | `Invalid file index N` |
| Etiquetas `[e{i}]` / `[v{i}]` | Etiqueta consumida sin producir, o producida dos veces (`409`) |
| `hstack=inputs=N` / `xstack` / `amix=inputs=N` | `N` cuenta los declarados, no los añadidos: cuelga o falla |
| `-map 0:a?` con entradas variables | Se mapea el audio del elemento equivocado |
| Colores o posiciones «por turno» (`i % 3`) | No falla: sale el color equivocado, en silencio |

Las cuatro primeras avisan. **La quinta no**, y es la peor: el módulo `409` es para esa.

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| `enumerate()` sobre una lista con `continue` | El filtro pide una entrada que no existe |
| `capture_output=True` sin comprobar `returncode` | ffmpeg falla en silencio dentro del bucle |
| Comprobar `returncode < 0` | En Windows llega como 4294967274: hay que comprobar `!= 0` |
| Probar solo con el último elemento descartado | Pasa el test y el fallo sigue vivo |
| Concatenar las escenas que sí salieron | Episodio completo y desincronizado desde el fallo hasta el final |
| Fiarse de que el MP4 existe | Existe, dura menos y suena sobre la imagen equivocada |
| Usar `inputs=N` con la cuenta de la tabla | `hstack`/`xstack`/`amix` cuelgan esperando un flujo que no llega |

## Relacionado

`400` el orden de render es narrativo · `404` acumular o sustituir · `408` lo que cuesta cada capa ·
`409` depurar un apilado · `104` filter_complex · `109` trampas y errores de ffmpeg ·
`132` render reproducible · `133` verificación automática · `canales_lushows/153` índices corridos ·
`canales_lushows/150` el catálogo del fallo silencioso · `canales_lushows/159` cazar un fallo que no avisa
