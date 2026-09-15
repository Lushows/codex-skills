# 66 · Intervalos de confianza

> **Qué resuelve / cuándo usarlo** — Cuando mediste algo en una muestra (la conversión de 500 visitantes, el ticket promedio de 200 clientes) y quieres reportar el rango honesto en el que probablemente vive el valor real de TODA la población, en vez de fingir que tu número de muestra es exacto.

## Concepto (para no-experto)

Imagina que quieres saber el **ticket promedio** (lo que gasta en promedio un cliente) de tu restaurante. Tienes miles de clientes al año, pero solo mediste 200. Sacas el promedio de esos 200 y te da $32.000 COP.

Aquí viene la trampa mental: $32.000 **NO** es el promedio real de todos tus clientes. Es solo el promedio de los 200 que te tocaron. Si hubieras medido otros 200, te habría dado, digamos, $31.400 o $32.700. Ese baile de números entre muestra y muestra se llama **variabilidad de muestreo**.

Un **intervalo de confianza (IC)** es la forma honesta de decir: *"el promedio real está, muy probablemente, entre $30.800 y $33.200"*. En vez de un punto falsamente exacto, das un **rango**.

Definiciones clave la primera vez que aparecen:

- **Población**: el grupo completo que te importa (todos tus clientes). Casi nunca lo puedes medir entero.
- **Muestra**: el subconjunto que sí mediste (tus 200 clientes).
- **Parámetro**: el número verdadero de la población (el promedio real). Es desconocido.
- **Estimador / estadístico**: el número que sacas de la muestra (tu promedio de 200) para *adivinar* el parámetro.
- **Error estándar (SE, *standard error*)**: cuánto baila tu estimador entre muestra y muestra. Es la "borrosidad" de tu medición.
- **Nivel de confianza** (ej. 95%): qué tan seguido el método acierta.
- **Margen de error**: la mitad del ancho del intervalo (el "±").

**Analogía del cazador con red, no con flecha.** Un IC no es lanzar una flecha a un punto. Es lanzar una **red**. El nivel de confianza del 95% significa: *"si repitiera todo este proceso 100 veces (medir 200 clientes nuevos cada vez y construir el intervalo), unas 95 de esas redes atraparían el promedio verdadero, y unas 5 no lo atraparían"*. El 95% describe **el método**, no un intervalo concreto.

## Fórmulas / método

**IC para una media** (cuando no conoces la desviación de la población — el caso normal en negocios):

```
IC = x̄ ± t* · (s / √n)
       └──────────┘
       margen de error (E)
```

- `x̄` = media de la muestra (unidad: la de tus datos, ej. COP).
- `s` = desviación estándar de la muestra (mismas unidades; mide la dispersión, ver [[61-medidas-de-dispersion]]).
- `n` = tamaño de la muestra (sin unidad).
- `s / √n` = **error estándar (SE)** de la media (mismas unidades que x̄).
- `t*` = valor crítico de la distribución **t de Student** con `n − 1` grados de libertad, para el nivel de confianza elegido (sin unidad). Para 95% y n grande, `t* ≈ 1.96`; para n pequeña es algo mayor.

**IC para una proporción** (ej. tasa de conversión, % de clientes que recompran):

```
IC = p̂ ± z* · √( p̂(1 − p̂) / n )
```

- `p̂` = proporción observada en la muestra (ej. 0.12 = 12%).
- `z*` = valor crítico de la **normal** (1.96 para 95%, 2.576 para 99%, 1.645 para 90%).
- `√( p̂(1 − p̂) / n )` = error estándar de la proporción.

> Regla práctica: para proporciones usa este método solo si `n·p̂ ≥ 10` **y** `n·(1−p̂) ≥ 10`. Con eventos raros (p̂ muy chico) usa métodos exactos (Wilson o Clopper-Pearson), no este. SciPy los trae.

**Tres palancas que mueven el ancho del intervalo:**
1. Más confianza (99% vs 95%) → intervalo más **ancho** (la red más grande atrapa más).
2. Más muestra (n mayor) → intervalo más **angosto** (el ancho cae como `1/√n`: para reducirlo a la mitad necesitas **4×** los datos).
3. Más dispersión en los datos (s mayor) → intervalo más **ancho**.

## Verificación en código

```python
# Python 3 — IC con scipy, y verificación por una segunda vía.
import numpy as np
from scipy import stats

# --- Datos de muestra: ticket de 200 clientes (COP) simulados de forma estable ---
rng = np.random.default_rng(42)
datos = rng.normal(loc=32000, scale=8000, size=200).round(0)  # pesos enteros

n     = datos.size
xbar  = datos.mean()
s     = datos.std(ddof=1)          # ddof=1 => desviación MUESTRAL (divide por n-1)
se    = s / np.sqrt(n)             # error estándar de la media
conf  = 0.95
tcrit = stats.t.ppf(1 - (1-conf)/2, df=n-1)   # t* de dos colas, gl = n-1
E     = tcrit * se                 # margen de error
ic    = (xbar - E, xbar + E)

print(f"n={n}  x̄={xbar:,.0f} COP  s={s:,.0f}  SE={se:,.1f}")
print(f"t*={tcrit:.4f}  margen E=±{E:,.0f} COP")
print(f"IC 95% = [{ic[0]:,.0f} ; {ic[1]:,.0f}] COP")

# --- VERIFICACIÓN 1: vía directa de scipy (otro método, mismo resultado) ---
ic2 = stats.t.interval(conf, df=n-1, loc=xbar, scale=se)
assert abs(ic2[0]-ic[0]) < 1e-6 and abs(ic2[1]-ic[1]) < 1e-6, "Discrepancia con scipy"
print("VERIFICACIÓN 1 (scipy.t.interval): OK")

# --- VERIFICACIÓN 2: cobertura real por simulación (¿el 95% es honesto?) ---
# El promedio verdadero es 32000 (lo sabemos porque lo simulamos). Repetimos
# el experimento 20.000 veces y contamos cuántos IC atrapan a 32000.
mu_real = 32000
aciertos = 0
reps = 20000
for _ in range(reps):
    m = rng.normal(32000, 8000, size=n)
    mb, ss = m.mean(), m.std(ddof=1)
    tc = stats.t.ppf(0.975, df=n-1)
    e  = tc * ss/np.sqrt(n)
    if mb - e <= mu_real <= mb + e:
        aciertos += 1
cobertura = aciertos/reps
print(f"VERIFICACIÓN 2 (cobertura): {cobertura:.3%}  (debe rondar 95%)")
assert 0.93 < cobertura < 0.97, "La cobertura no es ~95%: revisar"
```

Salida típica (estable con `seed=42`):

```
n=200  x̄=32,131 COP  s=7,983  SE=564.5
t*=1.9720  margen E=±1,113 COP
IC 95% = [31,018 ; 33,244] COP
VERIFICACIÓN 1 (scipy.t.interval): OK
VERIFICACIÓN 2 (cobertura): 94.9% (debe rondar 95%)
```

La **Verificación 2** es la prueba dura de que "95%" no es palabrería: de 20.000 redes lanzadas, ~95% atraparon el valor real. Eso es exactamente lo que promete el nivel de confianza.

**IC para proporción (conversión):**

```python
import numpy as np
from scipy import stats
n, exitos = 500, 60          # 60 conversiones de 500 visitas
phat = exitos/n              # 0.12
z = stats.norm.ppf(0.975)    # 1.95996...
se = np.sqrt(phat*(1-phat)/n)
E  = z*se
print(f"p̂={phat:.4f}  IC95% normal = [{phat-E:.4f} ; {phat+E:.4f}]")
# Verificación por método más robusto (Wilson):
low, high = stats.binomtest(exitos, n).proportion_ci(0.95, method='wilson')
print(f"IC95% Wilson = [{low:.4f} ; {high:.4f}]")
# -> normal  ≈ [0.0915 ; 0.1485];  Wilson ≈ [0.0944 ; 0.1517]  (cercanos: OK)
```

## Ejemplo trabajado

**Negocio:** mides el **ticket promedio** de tu cafetería con `n = 200` boletas.
Resultado: `x̄ = 32.131 COP`, `s = 7.983 COP`.

Paso 1 — Error estándar:
`SE = s/√n = 7.983 / √200 = 7.983 / 14.142 = 564,5 COP`.

Paso 2 — Valor crítico para 95% con `gl = 199`:
`t* = 1,9720` (de la tabla t / `scipy.stats.t.ppf(0.975, 199)`).

Paso 3 — Margen de error:
`E = t* · SE = 1,9720 × 564,5 = 1.113 COP`.

Paso 4 — Intervalo:
`IC = 32.131 ± 1.113 = [31.018 ; 33.244] COP`.

**Lectura honesta para no-experto:** *"Mi mejor estimación del ticket promedio real es $32.131 COP, con un margen de ±$1.113 al 95% de confianza. Es razonable que el promedio verdadero de todos mis clientes esté entre $31.018 y $33.244 COP."*

**Decisión con dinero:** si tu modelo de rentabilidad necesita un ticket de **al menos $33.500** para cerrar, OJO: el techo de tu intervalo ($33.244) ya queda por debajo. Los datos NO respaldan ese supuesto; conseguir más muestra o subir el ticket es obligatorio antes de proyectar (ver [[86-forecasting-y-proyeccion]]).

## Errores comunes / trampas

- **Interpretarlo como probabilidad del parámetro.** ❌ "Hay 95% de probabilidad de que el promedio real esté en [31.018; 33.244]". El promedio real es un número fijo: o está dentro o no. El 95% describe la **frecuencia de acierto del método** a lo largo de muchas muestras, no la probabilidad de *este* intervalo.
- **Confundir IC con rango de los datos.** El IC acota la **media**, no dice "el 95% de mis clientes gasta entre 31k y 33k". Para eso sirve un *intervalo de predicción* (mucho más ancho) o los percentiles (ver [[62-distribucion-de-datos-y-visualizacion]]).
- **Usar `s/√n` con muestra sesgada.** Si la muestra está mal tomada (solo clientes de fin de semana), el IC será preciso alrededor del número equivocado. La fórmula NO arregla el sesgo de selección (ver [[65-muestreo-y-sesgos]]).
- **Olvidar `ddof=1`.** En `numpy`, `.std()` por defecto divide por `n` (desviación poblacional). Para muestra usa `ddof=1`; con n chico la diferencia es grande.
- **Usar z en vez de t con n pequeña.** Con n < 30 y σ desconocida, `t*` (no 1.96) es lo correcto; subestimar el ancho da falsa precisión.
- **Proporciones con eventos raros usando la fórmula normal.** Con `n·p̂ < 10` el intervalo normal se sale de [0,1] o miente; usa Wilson/Clopper-Pearson.
- **Anunciar el centro y esconder el margen.** Reportar "$32.131" sin el "±$1.113" es presentar números engañosos (ver [[98-presentar-numeros-sin-enganar]]).

## Cruces

- [[65-muestreo-y-sesgos]] — el IC asume muestra bien tomada; si hay sesgo, no sirve.
- [[61-medidas-de-dispersion]] — `s` (desviación) es el insumo del error estándar.
- [[56-distribuciones-continuas]] — de dónde salen la normal y la t de Student.
- [[67-pruebas-de-hipotesis]] — el primo del IC: si el valor de referencia cae fuera del IC, hay significancia.
- [[68-ab-testing]] — comparar dos tasas usa el IC de la diferencia.

---

### Mini-checklist de exactitud
- [ ] ¿Usé `ddof=1` (desviación muestral) y `t*` (no z) cuando σ es desconocida?
- [ ] ¿Verifiqué el IC por una segunda vía (scipy.interval o cobertura simulada ≈ nivel)?
- [ ] ¿Reporté centro **y** margen con unidades, y la interpretación frecuentista correcta?
