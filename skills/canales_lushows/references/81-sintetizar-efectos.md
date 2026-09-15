# 81 · Sintetizar efectos

**Qué resuelve:** cómo fabricar cualquier sonido con ffmpeg, sin descargar nada. Una
pista sintetizada **no puede recibir un reclamo de Content ID**, que es la causa nº1 de
muerte de estos canales. Además la duración es exacta, cosa que un banco no da.

---

## Las tres fuentes

```
sine=f=440:d=3                       tono puro — cuerpo, graves, acordes
anoisesrc=c=pink:a=0.06:d=30         ruido — aire, roce, papel, metal
aevalsrc='0.4*sin(2*PI*220*t)':d=2   expresión arbitraria — cuando las otras no llegan
```

Colores de `anoisesrc`: `white` (plano, agudo), `pink` (−3 dB/octava, natural),
`brown` (−6 dB/octava, grave), `blue`, `violet`.

> **🔴 `sine` y `anoisesrc` son FUENTES, no filtros.** Van en `filter_complex`, **nunca**
> en `-af`. Ponerlos en `-af` fue lo que hizo fallar los 22 efectos de golpe: `-af`
> espera una cadena que empieza por la entrada del archivo, y una fuente no tiene
> entrada. El error que devuelve ffmpeg no lo dice claro.

```bash
ffmpeg -filter_complex "sine=f=55:d=3,volume=0.3[a]" -map "[a]" -t 3 -y out.wav   # ✅
ffmpeg -af "sine=f=55:d=3" -y out.wav                                            # ❌ falla
```

## La envolvente: todo sonido es una curva de volumen

Un tono constante no es un efecto; es un zumbido. Lo que convierte una fuente en
sonido es la **envolvente**, escrita como expresión en `volume` con `eval=frame`.

| Forma | Expresión | Para qué |
|---|---|---|
| Golpe (ataque instantáneo, caída) | `pow(max(0,1-t/0.5),2.6)` | percusión, impacto |
| Crecimiento exponencial | `pow(t/2.4,3.4)` | riser |
| Campana (entra y sale) | `pow(max(0,1-abs(t-0.45)/0.42),2.4)` | whoosh |
| **Repetición** | `pow(max(0,1-mod(t,1.0)/0.035),4)` | tictac, goteo, latido |
| Trapecio (ventana sin clic) | `min(1,max(0,min((t-a)/f,(b-t)/f)))` | limitar a un tramo |

El exponente controla la dureza: **2 es blando, 3-4 es seco, 6+ es un clic**.
`mod(t,P)` es lo que hace que un solo filtro genere un tren infinito de pulsos con
período P — es la clave de reloj, goteo, latido y contadora.

> **`between(t,a,b)` sobre un volumen es un clic.** Es un interruptor: pasa de 0 a 1 en
> una muestra. Se usa siempre el trapecio de arriba con `f` entre 0,25 y 0,8 s.

## Los cinco filtros de forma

| Filtro | Qué hace | Uso típico |
|---|---|---|
| `highpass=f=1100` | quita graves | papel, roce, agudos |
| `lowpass=f=420` | quita agudos | motor, bóveda, encierro |
| `equalizer=f=240:width_type=q:w=1:g=2.5` | **formante**: resalta una resonancia | dar "cuerpo" o "materia" |
| `aecho=0.8:0.9:220|480|760:0.45|0.28|0.16` | espacio | túnel, celda, bóveda |

El **formante** es lo que separa un ruido de un objeto: un `anoisesrc` filtrado suena a
ruido; el mismo ruido con dos `equalizer` marcados a 900 Hz y 2,4 kHz ya suena a papel.

`tremolo=f=7.5:d=0.55` (amplitud) y `vibrato=f=5:d=0.4` (frecuencia) son la diferencia
entre un zumbido y un motor.

## El molde de fábrica

```python
def crear(nombre, dur, cadena, ganancia=1.0):
    """La cadena SIEMPRE empieza por una fuente."""
    out = os.path.join(DEST, nombre + ".wav")
    fc = (f"{cadena},volume={ganancia},alimiter=limit=0.94,"
          f"aformat=channel_layouts=stereo[a]")
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error",
                    "-filter_complex", fc, "-map", "[a]", "-t", str(dur),
                    "-c:a", "pcm_s16le", "-ar", "44100", "-y", out], check=True)
    return out
```

`alimiter=limit=0.94` de cola en cada pieza: evita que una envolvente exponencial
recorte al escribir el WAV.

## Recetas reales (salidas de la biblioteca)

```python
# ROCE DE PAPEL — ruido agudo con caída seca
"anoisesrc=c=pink:a=1:d=0.7,highpass=f=1100,"
"volume='pow(max(0,1-t/0.28),2.2)':eval=frame"

# FAJO DE BILLETES — el sin() a 24 Hz son las hojas pasando entre los dedos
"anoisesrc=c=white:a=1:d=1.6,highpass=f=2200,lowpass=f=9000,"
"volume='0.5*(0.5+0.5*sin(2*PI*24*t))*pow(max(0,1-t/1.5),1.4)':eval=frame"

# PUERTA DE BÓVEDA — tono grave + masa de ruido marrón, mezclados y frenados
"sine=f=68:d=2.2,volume=0.7[b1];"
"anoisesrc=c=brown:a=0.5:d=2.2,lowpass=f=900[b2];"
"[b1][b2]amix=inputs=2:normalize=0,"
"volume='pow(max(0,1-t/1.1),1.8)':eval=frame"

# ZUMBIDO DE FLUORESCENTE — 120 Hz es el armónico de la red eléctrica, no 50/60
"sine=f=120:d=30,volume=0.14[o1];"
"anoisesrc=c=pink:a=0.02:d=30,lowpass=f=3200[o2];"
"[o1][o2]amix=inputs=2:normalize=0"

# MOTOR — fundamental + 2º armónico + escape, y el tremolo son los pistones
"sine=f=58:d=12,volume=0.55,tremolo=f=7.5:d=0.55,lowpass=f=900"
```

## El método para inventar uno nuevo

1. **¿Tono o ruido?** Metal, cuerdas y motores → `sine`; papel, roce y aire →
   `anoisesrc`. Casi todo lo bueno es **los dos mezclados**.
2. **¿Qué banda ocupa?** Graves <300 Hz, cuerpo 300-2000, materia 2-8 kHz. Filtrar
   ANTES de la envolvente, o el filtro se come el ataque.
3. **¿Qué forma tiene en el tiempo?** De la tabla de envolventes. Si se repite,
   `mod(t,P)` con P = el período real del objeto.
4. **¿Dónde ocurre?** `aecho` si el espacio importa.
5. **Medir su LUFS** y calibrarlo (`86`, `89`). Nunca ponerlo a ojo.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| `sine`/`anoisesrc` dentro de `-af` | Falla toda la generación con un error poco claro |
| `between(t,a,b)` como ventana | Clic audible en los dos extremos |
| Filtrar después de la envolvente | El filtro suaviza el ataque y el golpe pierde pegada |
| Envolvente sin `:eval=frame` | La expresión se evalúa una vez: sale un volumen fijo |
| Exponente 6+ en la caída | Deja de ser ataque y se convierte en clic digital |
| Tono puro sin ruido encima | Suena a sintetizador de los 80, no a objeto |
| No poner `alimiter` de cola | Recortes en las crestas al escribir el WAV |

## Relacionado

`82` música · `83` diegético · `84` picos · `89` biblioteca
