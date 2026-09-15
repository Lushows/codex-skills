# 60 · Estadística descriptiva

> **Qué resuelve / cuándo usarlo** — Resumir un montón de números (ventas, edades, tiempos de entrega, tickets) en uno solo que represente "el centro". Úsalo cuando alguien pregunta "¿cuánto vendemos en promedio?", "¿cuál es el ticket típico?" — y necesitas dar un número que NO mienta.

## Concepto (para no-experto)

**Estadística descriptiva** = describir un conjunto de datos con pocos números, sin sacar conclusiones más allá de lo que ves. (Lo contrario es la *estadística inferencial*, que adivina sobre una población a partir de una muestra — eso lo ves en [[65-muestreo-y-sesgos]] y [[66-intervalos-de-confianza]].)

Las **medidas de tendencia central** son números que intentan responder "¿dónde está el centro de mis datos?". Hay tres:

- **Media (promedio aritmético):** sumas todos los valores y divides entre cuántos hay. Analogía: si repartieras todo el dinero del grupo en partes iguales, a cada uno le tocaría la media.
- **Mediana:** ordenas los valores de menor a mayor y tomas el del medio. Analogía: la fila del banco ordenada por estatura — la mediana es la persona parada exactamente en la mitad. Deja la mitad por debajo y la mitad por encima.
- **Moda:** el valor que más se repite. Analogía: la talla de camiseta que más vendes. Puede haber una moda, varias, o ninguna.

La trampa central de este módulo: **la media engaña cuando hay datos extremos** (llamados *outliers* o valores atípicos: un valor muy lejos del resto). Un solo cliente que compró $100 millones puede inflar tu "ticket promedio" y hacerte creer que el negocio va mejor de lo que es. En esos casos la **mediana** es más honesta.

## Fórmulas / método

Sea un conjunto de **n** datos: x₁, x₂, …, xₙ.

**Media aritmética** (símbolo: x̄, se lee "equis barra"):

```
x̄ = (x₁ + x₂ + … + xₙ) / n = (1/n) · Σ xᵢ
```
- Σ (sigma mayúscula) = "suma de todos". n = cantidad de datos (debe ser entero positivo).
- Unidad: la misma de los datos (si los datos están en COP, x̄ está en COP).

**Mediana** (símbolo: x̃ o Me): ordena los datos de menor a mayor.
- Si **n es impar**: la mediana es el valor en la posición (n+1)/2.
- Si **n es par**: es el promedio de los dos valores centrales, posiciones n/2 y n/2 + 1.

```
n impar:  x̃ = x_((n+1)/2)
n par:    x̃ = ( x_(n/2) + x_(n/2 + 1) ) / 2
```

**Moda** (símbolo: Mo): el (los) valor(es) con mayor frecuencia. Si todos aparecen una vez, no hay moda. Es la única que sirve para datos *categóricos* (color, ciudad, talla).

**Cuándo usar cada una:**

| Situación | Mejor medida | Por qué |
|---|---|---|
| Datos simétricos, sin extremos (estaturas) | Media | Usa toda la información |
| Datos con outliers o sesgados (ingresos, precios de casas) | Mediana | No la arrastra un valor enorme |
| Datos categóricos (color favorito, talla) | Moda | Media/mediana no tienen sentido |

## Verificación en código

```python
# Estadística descriptiva EXACTA. Para dinero usamos Fraction (exacto, sin error de float).
from fractions import Fraction
from statistics import median, multimode, mean as st_mean
import numpy as np

# Tickets de venta en COP (uno es un outlier: 5.000.000)
datos = [12000, 15000, 11000, 14000, 13000, 5000000]

# --- MEDIA exacta con Fraction (sin floats para el dinero) ---
fr = [Fraction(x) for x in datos]
media_exacta = sum(fr) / len(fr)          # Fraction exacto
print("Media (exacta):", media_exacta, "=", float(media_exacta), "COP")

# --- MEDIANA ---
med = median(datos)                        # statistics.median ordena internamente
print("Mediana:", med, "COP")

# --- MODA ---
print("Moda(s):", multimode(datos))        # lista; vacía-equivalente si todos únicos

# ================= VERIFICACIÓN POR SEGUNDA VÍA =================
# Vía 1: numpy debe coincidir con nuestra media exacta
assert np.isclose(np.mean(datos), float(media_exacta)), "media numpy != Fraction"
# Vía 2: la inversa de la media -> media * n debe reconstruir la suma total
assert media_exacta * len(fr) == sum(fr), "media*n no reconstruye la suma"
# Vía 3: la mediana debe coincidir ordenando a mano
ordenado = sorted(datos)                    # [11000,12000,13000,14000,15000,5000000]
n = len(ordenado)                           # n=6 (par)
med_mano = (ordenado[n//2 - 1] + ordenado[n//2]) / 2   # (13000+14000)/2
assert med == med_mano, "mediana statistics != cálculo a mano"
# Vía 4 (sanity / orden de magnitud): la media debe caer entre min y max
assert min(datos) <= float(media_exacta) <= max(datos)
print("OK — las 4 verificaciones pasaron")
```

Salida esperada:
```
Media (exacta): 5065000/6 = 844166.6666666666 COP
Mediana: 13500.0 COP
Moda(s): [12000, 15000, 11000, 14000, 13000, 5000000]
OK — las 4 verificaciones pasaron
```

Lectura clave: la **media (≈ $844.167)** está disparada por el outlier de $5.000.000, mientras la **mediana ($13.500)** describe de verdad el ticket típico. Aquí la mediana NO miente; la media sí.

## Ejemplo trabajado

**Caso GastroLatam:** vendiste la Calculadora de Costos a 6 clientes esta semana. La mayoría pagó el precio normal ($10.000), pero un cliente compró un paquete corporativo de $5.000.000. ¿Cuál es el "ticket promedio"?

Datos (COP): 10.000, 10.000, 10.000, 10.000, 10.000, 5.000.000

Paso 1 — **Media:**
```
suma = 10000·5 + 5000000 = 50000 + 5000000 = 5.050.000 COP
media = 5.050.000 / 6 = 841.666,67 COP   (redondeo a 2 decimales, UNA sola vez al final)
```

Paso 2 — **Mediana** (n = 6, par). Ordenado: 10.000, 10.000, 10.000, 10.000, 10.000, 5.000.000.
Posiciones centrales 3 y 4 → ambas valen 10.000.
```
mediana = (10.000 + 10.000) / 2 = 10.000 COP
```

Paso 3 — **Moda:** el valor que más se repite = **10.000 COP** (aparece 5 veces).

**Resultado con unidades e interpretación:**
- Media = **$841.666,67 COP** ← engañosa: ningún cliente "normal" pagó cerca de eso.
- Mediana = **$10.000 COP** ← el ticket real de la mayoría.
- Moda = **$10.000 COP** ← lo que casi todos pagaron.

Conclusión honesta para el dueño: "El ticket típico es **$10.000** (mediana y moda). La media de $841.667 está inflada por una venta corporativa atípica; repórtala aparte, no la presentes como el promedio del negocio." Esto enlaza con [[98-presentar-numeros-sin-enganar]].

Verificación por inversa: media × n = 841.666,67 × 6 = 5.050.000,02 ≈ 5.050.000 (la diferencia de $0,02 es solo del redondeo mostrado; el cálculo interno usó el valor exacto 5.050.000/6).

## Errores comunes / trampas

- **Reportar la media con outliers presentes.** Un dato extremo la arrastra; usa mediana o reporta ambas. Mira los datos antes de elegir.
- **Confundir promedio con "lo normal".** Si el 90% paga $10.000, el promedio puede no parecerse a NADIE real. La media es un punto de equilibrio, no un valor típico.
- **Sacar la media de porcentajes o tasas como si fueran números planos.** Promediar "50% y 100%" para dos grupos de tamaños distintos da mal: necesitas media ponderada (ver [[96-scoring-indices-y-ponderaciones]]).
- **Olvidar ordenar antes de la mediana.** La mediana SIN ordenar es basura.
- **Usar la moda con datos continuos casi únicos** (precios con decimales): casi nunca se repiten, la moda no aporta. Agrupa en rangos primero.
- **Dinero con `float`.** `0.1 + 0.2 != 0.3` en float. Usa `decimal` o `Fraction` (ver [[12-fracciones-decimales-y-precision]]).
- **Redondear en pasos intermedios.** Redondea UNA vez al final ([[05-cifras-significativas-y-redondeo]]).

## Cruces

- [[61-medidas-de-dispersion]] — el centro no basta; mide qué tan dispersos están (desviación estándar, rango).
- [[62-distribucion-de-datos-y-visualizacion]] — ver la forma (histograma) revela si la media sirve o engaña.
- [[69-estadistica-enganosa]] — cómo se abusa del "promedio" para mentir con datos.
- [[98-presentar-numeros-sin-enganar]] — reportar media vs mediana con honestidad.
- [[06-estimacion-y-sanity-checks]] — el chequeo "min ≤ media ≤ max" y otras verificaciones rápidas.

---

### Mini-checklist de exactitud
- [ ] ¿Hay outliers? Si sí, reporté mediana (no solo media) y los señalé.
- [ ] ¿La media cae entre el mínimo y el máximo? (sanity check obligatorio).
- [ ] ¿Verifiqué por segunda vía (numpy vs Fraction, o media×n = suma)?
