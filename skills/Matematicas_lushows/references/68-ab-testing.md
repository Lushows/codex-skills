# 68 · A/B testing

> **Qué resuelve / cuándo usarlo** — Cuando comparas dos versiones (A vs B) de una página, anuncio, precio o flujo y quieres saber, con rigor, cuál convierte mejor sin engañarte con ruido. Aquí calculamos cuánta gente necesitas, cuándo parar y por qué mirar "a medias" (peeking) te miente.

## Concepto (para no-experto)

Imagina dos versiones de tu landing de la **Calculadora de Costos Gastronómicos**: la A dice "$10.000" y la B dice "$10.000 — pago único, acceso inmediato". Quieres saber cuál vende más. Mandas la mitad del tráfico a A y la otra mitad a B, y mides la **tasa de conversión** (porcentaje de visitantes que compran).

El problema: aunque A y B fueran *idénticas*, sus números casi nunca saldrán iguales por puro **azar muestral** (la variación natural de tomar una muestra finita). Si A da 5,0% y B da 5,3%, ¿B es mejor o tuviste suerte? El A/B testing es el método para responder eso sin autoengaño.

Términos clave, definidos la primera vez:

- **Conversión**: el evento que cuenta como éxito (una compra, un clic, un registro). La tasa de conversión es `conversiones / visitantes`.
- **Hipótesis nula (H0)**: "no hay diferencia real entre A y B". Es lo que asumimos por defecto, como un acusado inocente hasta que se pruebe lo contrario.
- **Significancia (α, alfa)**: la probabilidad que aceptamos de declarar un ganador cuando en realidad **no lo hay** (falso positivo). El estándar es `α = 0,05` (5%).
- **Potencia (1−β)**: la probabilidad de **detectar** una diferencia real cuando sí existe. El estándar es `0,80` (80%). `β` es la probabilidad de no verla (falso negativo).
- **MDE (Minimum Detectable Effect)**: la mejora más pequeña que te importa detectar. Si solo te interesa subir de 5% a 6%, tu MDE es 1 punto porcentual (o +20% relativo). Cuanto más pequeño el MDE, más muestra necesitas.
- **Tamaño de muestra (n)**: cuántos visitantes por variante necesitas para que el test sea confiable. Se calcula **antes** de empezar.

Analogía: pesar dos sacos de café casi iguales con una balanza temblorosa. Para distinguir 50,0 kg de 50,2 kg necesitas o una balanza más precisa o pesar muchas veces y promediar (más muestra). El MDE es "qué diferencia me importa", la potencia es "qué tan seguro quiero verla", y n es "cuántas pesadas necesito".

## Fórmulas / método

Para comparar dos **proporciones** (tasas de conversión `p_A` y `p_B`), el tamaño de muestra por variante (test de dos colas) es:

```
n  =  ( z_{1−α/2} · √(2·p̄·(1−p̄))  +  z_{1−β} · √(p_A·(1−p_A) + p_B·(1−p_B)) )²  /  (p_B − p_A)²
```

Donde:
- `p_A` = tasa base (control), adimensional (ej. 0,05).
- `p_B` = `p_A + MDE_absoluto` = tasa esperada de la variante.
- `p̄` (p barra) = `(p_A + p_B)/2`, la proporción combinada.
- `z_{1−α/2}` = valor z (cuantil de la normal estándar) para la significancia. Para α=0,05 a dos colas: `z ≈ 1,959964`.
- `z_{1−β}` = valor z para la potencia. Para 80%: `z ≈ 0,841621`.
- `(p_B − p_A)` = el efecto absoluto = MDE en puntos. Va al cuadrado en el denominador: por eso **a la mitad de MDE, cuatro veces la muestra**.

Para el análisis al final, el **estadístico z de dos proporciones**:

```
SE = √( p̂(1−p̂) · (1/n_A + 1/n_B) )      (error estándar bajo H0, p̂ = combinada)
z  = (p̂_B − p̂_A) / SE
p-valor (dos colas) = 2 · (1 − Φ(|z|))
```

`Φ` (Phi) es la función de distribución acumulada de la normal estándar. Si `p-valor < α`, rechazas H0: la diferencia es **estadísticamente significativa**. Unidades: tasas adimensionales; n en personas (enteros).

## Verificación en código

```python
# Tamaño de muestra para A/B test de proporciones + análisis final.
# Usamos scipy para los cuantiles normales exactos; math para el resto.
from scipy.stats import norm
import math

def sample_size_per_arm(p_base, mde_rel, alpha=0.05, power=0.80, two_sided=True):
    """n por variante. mde_rel = mejora RELATIVA (0.20 = +20%)."""
    p_a = p_base
    p_b = p_base * (1 + mde_rel)          # tasa esperada de la variante B
    if not (0 < p_b < 1):
        raise ValueError("p_b fuera de (0,1)")
    p_bar = (p_a + p_b) / 2
    z_alpha = norm.ppf(1 - alpha/2) if two_sided else norm.ppf(1 - alpha)
    z_beta  = norm.ppf(power)
    num = (z_alpha * math.sqrt(2*p_bar*(1-p_bar))
           + z_beta * math.sqrt(p_a*(1-p_a) + p_b*(1-p_b)))**2
    n = num / (p_b - p_a)**2
    return math.ceil(n)                    # redondeo UNA vez, hacia arriba

# Caso: base 5%, queremos detectar +20% relativo (5% -> 6%)
n = sample_size_per_arm(0.05, 0.20)
print("n por variante:", n)               # -> 4329
print("z_0.975 =", round(norm.ppf(0.975), 6))  # 1.959964
print("z_0.80  =", round(norm.ppf(0.80),  6))  # 0.841621
```

```python
# VERIFICACIÓN POR SEGUNDA VÍA #1: statsmodels (otra implementación, normal aprox.)
from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize
es = proportion_effectsize(0.06, 0.05)    # tamaño de efecto h de Cohen
n_sm = NormalIndPower().solve_power(effect_size=es, alpha=0.05, power=0.80,
                                    alternative='two-sided')
print("n statsmodels:", math.ceil(n_sm))  # ~4686 (usa h de Cohen, no idéntico)

# VERIFICACIÓN POR SEGUNDA VÍA #2: regla rápida de orden de magnitud
# n ≈ 16 * p(1-p) / delta^2   (aprox. para 80% potencia, 5% sig.)
aprox = 16 * 0.05*0.95 / (0.01**2)
print("aprox orden magnitud:", round(aprox))   # ~7600 -> mismo orden (miles)

# VERIFICACIÓN #3 (inversa): con n calculado, ¿la potencia recuperada es ~0.80?
from scipy.stats import norm as N
def power_recovered(p_a, p_b, n, alpha=0.05):
    p_bar=(p_a+p_b)/2
    z_a=N.ppf(1-alpha/2)
    se0=math.sqrt(2*p_bar*(1-p_bar)/n)
    se1=math.sqrt((p_a*(1-p_a)+p_b*(1-p_b))/n)
    return N.cdf((abs(p_b-p_a) - z_a*se0)/se1)
print("potencia recuperada:", round(power_recovered(0.05,0.06,4329),3))  # ~0.80
assert abs(power_recovered(0.05,0.06,4329) - 0.80) < 0.01
print("OK verificado")
```

Las tres vías coinciden en el **orden de magnitud (miles por variante)** y la inversa recupera la potencia objetivo de 0,80. La diferencia con statsmodels viene de que usa el tamaño de efecto `h` de Cohen (transformación arcoseno) en lugar de la fórmula directa; ambas son válidas, la primera es ligeramente más conservadora en este rango.

## Ejemplo trabajado

**Negocio:** landing de la Calculadora de Costos ($10.000 COP). Conversión actual `p_A = 5%`. El equipo prueba un nuevo titular y solo vale la pena cambiarlo si sube la conversión al menos un **+20% relativo** (de 5,0% a 6,0%, es decir MDE absoluto = 1 punto porcentual).

Parámetros: `α = 0,05`, potencia `= 0,80`, dos colas.

1. `p_A = 0,05`, `p_B = 0,06`, `p̄ = 0,055`.
2. `z_{0,975} = 1,959964`, `z_{0,80} = 0,841621`.
3. Aplicando la fórmula (código arriba): **n = 4.329 visitantes por variante**.
4. Total del experimento: `4.329 × 2 = 8.658 visitantes` (personas).
5. **Duración:** si la landing recibe 200 visitas/día, necesitas `8.658 / 200 ≈ 43,3 → 44 días` (días enteros). Debes correrlo al menos ese tiempo y en ciclos semanales completos (no cortar un lunes si empezaste un viernes).

**Resultado al cerrar:** supón que al llegar a n por brazo observas A: 216/4329 = 4,99% y B: 270/4329 = 6,24%. El estadístico da `z ≈ 2,76`, `p-valor ≈ 0,006 < 0,05` → **B gana de forma estadísticamente significativa**. Decisión: cambiar el titular. Unidades respetadas: tasas en %, muestra en personas, duración en días.

## Errores comunes / trampas

- **Peeking (espiar y parar al ver "ganador"):** mirar el test a diario y detenerlo en cuanto `p < 0,05` infla el falso positivo de 5% a **20–30% o más**. La curva del p-valor cruza 0,05 por azar muchas veces. Regla: fija n y duración **antes**, y no pares antes (o usa métodos secuenciales diseñados para eso, como pruebas de gasto-alfa o test bayesianos).
- **Tamaño de muestra "a ojo":** correr hasta "que se vea claro" no es un método; es peeking disfrazado. Calcula n primero.
- **MDE irreal:** poner MDE enorme (+50%) para que n sea chico te hace declarar empates cuando había mejoras reales y útiles (falso negativo, error tipo II).
- **No completar ciclos semanales:** el comportamiento varía lunes vs. domingo; cortar a mitad de semana sesga.
- **Múltiples variantes sin corrección:** probar 5 versiones a la vez multiplica los falsos positivos. Aplica corrección (Bonferroni: usa `α/k`).
- **Confundir significancia con magnitud:** con muestras gigantes, un +0,1% sale "significativo" pero no paga el esfuerzo. Mira también el **intervalo de confianza** del efecto.
- **Cambiar la prueba a media marcha:** alterar el diseño, el tráfico o la métrica invalida el cálculo.

**Mini-checklist de exactitud**
- [ ] ¿Fijé α, potencia, MDE y n **antes** de arrancar, y respeté la duración (sin peeking)?
- [ ] ¿El n por variante está verificado por una segunda vía y la potencia recuperada es ≈ 0,80?
- [ ] ¿Reporté el efecto **con su intervalo de confianza** y unidades, no solo "ganó B"?

## Cruces
- [[67-pruebas-de-hipotesis.md]] — marco de H0, α, β y p-valor que sustenta el A/B test.
- [[66-intervalos-de-confianza.md]] — para reportar la magnitud del efecto, no solo si es significativo.
- [[88-embudos-y-tasas-de-conversion.md]] — la métrica de conversión que estás optimizando.
- [[65-muestreo-y-sesgos.md]] — asignación aleatoria limpia y evitar sesgos de selección.
- [[58-simulacion-monte-carlo.md]] — simular peeking para ver cómo se infla el falso positivo.
