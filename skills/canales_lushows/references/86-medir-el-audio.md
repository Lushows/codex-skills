# 86 · Medir el audio

**Qué resuelve:** dejar de opinar sobre el sonido. Poner ganancias a ojo sobre WAV ya
atenuados dejó **44 saltos audibles** en un episodio de 90 s. La mezcla se mide, se
corrige por número y se vuelve a medir.

---

## Lo que se mide y contra qué

| Métrica | Qué es | Objetivo | Se corrige con |
|---|---|---|---|
| **I** integrado | Volumen percibido del archivo entero | **−14,0 LUFS** ±1 | `loudnorm=I=-14` |
| **TP** pico real | Cresta reconstruida, la que ve el códec | **≤ −1,5 dBFS** | `loudnorm=TP=-1.5` |
| **LRA** recorrido | Distancia entre lo flojo y lo fuerte | **4 a 9 LU** | Compresión del maestro |
| **S** corto plazo (3 s) | La estructura del nivel | recorrido **≤ 8 LU** | Nivel del colchón (`80`) |
| **M** momentáneo (400 ms) | El detalle: pausas y golpes | *serie* | — |

**6 LU es el umbral en que el oído deja de oír "cambio" y empieza a oír "corte".**
## 🔴 Los saltos se cuentan sobre S, no sobre M

Es el error de método que invalida la auditoría. El momentáneo (400 ms) sube y baja con
**cada sílaba**: medido así, el episodio ya terminado da 42 "saltos" que en realidad son
habla normal. El corto plazo (3 s) promedia el habla y deja ver lo único que importa:
**si el suelo se cae**.

Medición real de `episodio01.mp4` (80 s, mezcla terminada):

```
  integrado      -14.1 LUFS  objetivo -14,0 ±1     OK
  pico real       -1.4 dBFS  objetivo <= -1,5      OK
  recorrido LRA    2.0 LU    objetivo 4-9          CORREGIR
  corto plazo    -17.9 a -12.7 LUFS (5.2 LU)       OK
  suelo de pausa -28.9 LUFS  (momentáneo mínimo)
  saltos >= 6 LU en 2 s:   0   objetivo <= 2       OK
```

Cero saltos estructurales: el colchón sostiene. El **LRA de 2,0 LU** sí es un defecto
real y pendiente — el compresor del maestro está aplastando el relieve que construyen
los picos (`84`).

## El script de auditoría (real y ejecutable)

```python
#!/usr/bin/env python
# auditar_audio.py — mide la mezcla y dice qué corregir, con el segundo exacto.
import re, subprocess, sys

LINEA = re.compile(r"t:\s*([\d.]+).*?\sM:\s*(-?[\d.]+)\s+S:\s*(-?[\d.]+)")
FINAL = {"I":   re.compile(r"\bI:\s*(-?[\d.]+)\s*LUFS"),
         "LRA": re.compile(r"\bLRA:\s*(-?[\d.]+)\s*LU"),
         "TP":  re.compile(r"\bPeak:\s*(-?[\d.]+)\s*dBFS")}

SUELO, UMBRAL, VENTANA = -70.0, 6.0, 2.0   # LUFS sin señal · LU de salto · s


def medir(ruta):
    """(serie [t, momentáneo, corto], resumen {I, LRA, TP}) de ebur128."""
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", ruta,
                        "-filter_complex", "ebur128=peak=true", "-f", "null", "-"],
                       capture_output=True, text=True, errors="replace")
    serie, res = [], {}
    for ln in r.stderr.splitlines():
        m = LINEA.search(ln)
        if m:                                     # línea de serie temporal
            t, mom, cor = (float(m.group(i)) for i in (1, 2, 3))
            if cor > SUELO:                       # -120.7 = silencio, no cuenta
                serie.append((t, mom, cor))
            continue
        for k, rx in FINAL.items():               # bloque de resumen final
            mm = rx.search(ln)
            if mm and k not in res:
                res[k] = float(mm.group(1))
    return serie, res


def saltos(serie, col=2, umbral=UMBRAL, ventana=VENTANA):
    """Cada medida contra la de hace `ventana` s. Máximo un aviso por segundo."""
    fuera, ultimo = [], -9.0
    for i, fila in enumerate(serie):
        t, v = fila[0], fila[col]
        k = i
        while k > 0 and serie[k][0] > t - ventana:
            k -= 1
        if k == i:
            continue
        d = v - serie[k][col]
        if abs(d) >= umbral and t - ultimo >= 1.0:
            fuera.append((t, d))
            ultimo = t
    return fuera


def ok(c):
    return "OK      " if c else "CORREGIR"


def informe(ruta):
    serie, res = medir(ruta)
    if not serie:
        print(f"{ruta}: sin audio medible")
        return 1
    I, LRA, TP = res.get("I", 0.0), res.get("LRA", 0.0), res.get("TP", 0.0)
    cortos = [c for _, _, c in serie]
    moment = [m for _, m, _ in serie]
    est = saltos(serie, col=2)                    # estructurales, sobre S (3 s)
    rec = max(cortos) - min(cortos)

    print(f"\n{ruta}")
    print(f"  integrado     {I:>6.1f} LUFS  objetivo -14,0 ±1     {ok(abs(I + 14) <= 1)}")
    print(f"  pico real     {TP:>6.1f} dBFS  objetivo <= -1,5     {ok(TP <= -1.4)}")
    print(f"  recorrido LRA {LRA:>6.1f} LU    objetivo 4-9         {ok(4 <= LRA <= 9)}")
    print(f"  corto plazo   {min(cortos):>6.1f} a {max(cortos):.1f} LUFS "
          f"({rec:.1f} LU)   {ok(rec <= 8)}")
    print(f"  suelo de pausa{min(moment):>6.1f} LUFS  (momentáneo mínimo)")
    print(f"  saltos >= {UMBRAL:.0f} LU en {VENTANA:.0f} s: {len(est):>3}   "
          f"objetivo <= 2          {ok(len(est) <= 2)}")
    for t, d in est[:20]:
        print(f"        {int(t)//60}:{t % 60:05.2f}   {d:+5.1f} LU")
    return 0 if (abs(I + 14) <= 1 and TP <= -1.4 and len(est) <= 2) else 1


if __name__ == "__main__":
    sys.exit(max([informe(r) for r in sys.argv[1:]] or [1]))
```

Devuelve **código de salida 1** si algo falla: sirve como puerta antes de publicar.

## Calibrar una pieza: medir, luego calcular

Nunca a ojo. Se mide el WAV suelto y se resuelve la ganancia lineal:

```python
def ganancia_para(ruta, objetivo_lufs):
    """dB = objetivo - medido ; lineal = 10^(dB/20)"""
    return 10 ** ((objetivo_lufs - medir(ruta)[1]["I"]) / 20)
```

Ejemplo real: `amb_sala` medía **−48,6 LUFS** y su sitio en la mezcla es **−41,0 LUFS**.

```
dB     = -41,0 - (-48,6) = +7,6 dB
lineal = 10^(7,6/20)     = 2,40      →  volume=2.40
```

Ese 2,40 es exactamente la ganancia de la tabla de `89`. Ninguna cifra se puso a oído.

## El orden de la corrección

1. **Integrado** → `loudnorm`. Si no llega, la mezcla está floja: subir la voz, no el maestro.
2. **Pico real** → si pasa de −1,5, falta `alimiter` en alguna pieza (`81`).
3. **Saltos sobre S** → casi siempre es el colchón. Subirlo al rango de `80`.
4. **LRA** → bajo 4, aflojar el compresor del maestro (`ratio` 2,4 → 1,8); sobre 9,
   subir el suelo, nunca bajar los picos.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Contar saltos sobre M | 42 falsos positivos: eso es habla, no cortes |
| Calibrar de oído sobre WAV ya atenuados | 44 saltos audibles y piezas inaudibles |
| Medir solo el integrado | El archivo cumple la norma y aun así suena a cortes |
| Aceptar LRA < 4 | Mezcla plana: los picos dejan de existir |
| Corregir picos antes que el colchón | Se persigue el síntoma; la causa es el suelo |

## Relacionado

`80` arquitectura · `84` picos · `85` ducking · `89` biblioteca · `17` medir el montaje

---

## 🔴 La frecuencia de muestreo: el fallo que entrega vídeos mudos

Medido el 12-sep-2026, después de que Luis abriera el episodio y escribiera *«y no se
escucha»*. El máster tenía:

```
Integrated  -14.1 LUFS      ✅ a norma
True Peak    -1.2 dBTP      ✅ a norma
sample_rate  96000 Hz       🔴
```

**`loudnorm` trabaja internamente a 192 kHz.** Si no se le pone un `aresample` detrás,
ffmpeg elige la frecuencia más alta que admita el códec de salida — **AAC a 96 kHz** — y
muchos reproductores no la decodifican: dan silencio, sin error, sin aviso y sin una línea
en el log. Los dos primeros episodios del canal se entregaron así.

```
loudnorm=I=-14:TP=-1.5:LRA=9,aresample=44100[out]
                             ^^^^^^^^^^^^^^^^^ obligatorio
```

**La lección que vale para todo:** medir LUFS y picos no es medir el audio. Un fichero
puede estar perfecto en las dos medidas que miramos siempre y ser inservible por una
tercera que no miramos nunca. A la verificación (§ `140`) entra también:

```bash
ffprobe -v error -select_streams a   -show_entries stream=codec_name,sample_rate,channels -of default=nw=1 salida.mp4
# se espera: aac · 44100 · 2
```

## Y una trampa de diagnóstico, en la misma sesión

Al oírse bajo, la primera medida que hice comparó «una pausa» con «hablando» y dio 0,2 dB
de diferencia: la cama de sonido al mismo nivel que la voz. **Era falso.** El segundo de la
pausa lo saqué del reloj del minuto 3 y lo medí sobre el minuto 1 del episodio: estaba
midiendo voz contra voz. Con las pausas correctas:

```
pausas (sólo cama)  -30,8 a -32,6 dB
hablando            -17,1 dB          →  14-15 dB de separación, que es lo correcto
```

**Una medida sobre la ventana equivocada no es una medida floja: es una medida que miente
con autoridad.** Antes de acusar a la mezcla, comprobar que el segundo que se mide es el
segundo que se cree.

Lo que sí era cierto: −14 LUFS es lo que pide YouTube, pero un reproductor local no
normaliza y la mayoría de los ficheros del mundo están más altos. Para revisar, copia a
**−11 LUFS**; el máster se queda a norma.
