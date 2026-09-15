# 65 · Muestreo y sesgos

> **Qué resuelve / cuándo usarlo** — Cuando quieres concluir algo sobre TODOS (la población) pero solo mediste a UNOS POCOS (la muestra). Este módulo te dice cuándo esa muestra representa a todos y cuándo te miente.

## Concepto (para no-experto)

Imagina que quieres saber qué tan satisfechos están tus clientes de un restaurante. Preguntarle a los 10.000 que pasaron este año es carísimo y lento. En vez de eso, le preguntas a 200. Eso es **muestrear**.

Definamos los términos clave la primera vez que aparecen:

- **Población**: el grupo COMPLETO sobre el que quieres concluir. Ejemplo: *todos* los clientes del restaurante en 2026.
- **Muestra**: el subconjunto que realmente mides. Ejemplo: los 200 que respondieron la encuesta.
- **Parámetro**: el número verdadero de la población (lo que NO conoces). Ejemplo: la satisfacción promedio real de los 10.000.
- **Estadístico** (o estimador): el número que calculas con la muestra para *adivinar* el parámetro. Ejemplo: la satisfacción promedio de los 200.

La pregunta del millón: ¿la muestra de 200 se parece a los 10.000? Solo se parece si fue elegida **al azar de verdad**, donde cada cliente tenía la misma oportunidad de caer en la muestra. Eso es **muestreo aleatorio simple**.

**Analogía de la sopa**: para saber si la sopa de una olla está salada, no te tomas toda la olla: la **revuelves** y pruebas una cucharada. La cucharada (muestra) representa bien la olla (población) *solo si revolviste*. Si pruebas la cucharada de la superficie sin revolver, donde flota la sal, concluirás que está saladísima cuando no lo está. Ese "no revolver" es un **sesgo**: un error sistemático que empuja tu resultado siempre hacia el mismo lado equivocado.

Los tres sesgos que más dinero cuestan:

- **Sesgo de selección**: tu muestra se elige de forma que sobre-representa a un tipo de gente. Encuesta "en la puerta del restaurante a la hora del almuerzo" → nunca aparecen los que solo van de noche.
- **Sesgo de supervivencia**: solo ves a los que "sobrevivieron" y no a los que desaparecieron. Mides la satisfacción solo de clientes que SIGUEN viniendo → los que se fueron furiosos (¡los que más te importan!) no están.
- **Sesgo de no respuesta**: solo te contestan ciertos perfiles. Si una encuesta de 1.000 envíos la responden 50, y casualmente responden los muy contentos y los muy enojados, tu "promedio" no representa a nadie.

Un sesgo NO se arregla con una muestra más grande. Una olla mal revuelta probada con una cucharada enorme sigue mintiendo. Más datos sesgados = mentira más confiada.

## Fórmulas / método

**Error estándar de la media** (qué tanto baila el promedio de muestra en muestra, *suponiendo muestreo aleatorio*):

    EE = σ / √n

- `σ` (sigma) = desviación estándar de la población (dispersión real de los datos), en las mismas unidades que el dato.
- `n` = tamaño de la muestra (cantidad de elementos medidos), adimensional.
- `EE` = error estándar, mismas unidades que el dato. Más `n` → menor `EE` → promedio más estable.

Clave: el error de muestreo (aleatorio) baja como `√n`. Para reducir el error a la mitad, necesitas **4 veces** más datos.

**Corrección por población finita** (cuando la muestra es grande frente a la población N):

    EE_finito = (σ / √n) · √((N − n) / (N − 1))

Si `n` es pequeño frente a `N`, el factor ≈ 1 y se ignora.

**Lo que NINGUNA fórmula corrige — el sesgo:**

    valor_observado = valor_real + sesgo + error_aleatorio

- El **error aleatorio** baja con más `n` (se promedia y desaparece).
- El **sesgo** NO baja con `n`: es un término fijo. Solo se elimina cambiando *cómo* tomas la muestra.

**Tasa de respuesta** (alerta de sesgo de no respuesta):

    tasa_respuesta = respuestas / invitaciones_enviadas

Tasas bajas (< 30–40%) hacen sospechar fuerte sesgo de no respuesta.

## Verificación en código

Simulamos una población REAL conocida y comparamos un muestreo aleatorio (honesto) contra uno sesgado, para *ver* la diferencia entre error que se promedia y sesgo que no.

```python
import numpy as np

rng = np.random.default_rng(42)  # semilla fija => resultado reproducible

# --- Poblacion REAL (la conocemos porque es simulada) ---
# 10.000 clientes; satisfaccion de 1 a 10. Promedio real ("parametro") lo medimos directo.
N = 10_000
poblacion = np.clip(rng.normal(7.0, 1.5, N), 1, 10)  # centrada en ~7
mu_real = poblacion.mean()
print(f"Promedio REAL poblacion (parametro): {mu_real:.4f}")

# --- 1) Muestreo ALEATORIO (olla bien revuelta) ---
def media_muestra_aleatoria(n):
    idx = rng.choice(N, size=n, replace=False)  # cada cliente, misma probabilidad
    return poblacion[idx].mean()

# Repetimos 2000 veces para ver como se comporta el estimador
estim_aleatorio = np.array([media_muestra_aleatoria(200) for _ in range(2000)])
print(f"Aleatorio n=200 -> media de medias: {estim_aleatorio.mean():.4f} "
      f"(sesgo = {estim_aleatorio.mean() - mu_real:+.4f})")

# --- 2) Muestreo SESGADO por seleccion ---
# Solo encuestamos a clientes "muy felices" (satisfaccion >= 8): puerta del local
felices = poblacion[poblacion >= 8]
def media_muestra_sesgada(n):
    idx = rng.choice(len(felices), size=n, replace=False)
    return felices[idx].mean()

estim_sesgado = np.array([media_muestra_sesgada(200) for _ in range(2000)])
print(f"Sesgado  n=200 -> media de medias: {estim_sesgado.mean():.4f} "
      f"(sesgo = {estim_sesgado.mean() - mu_real:+.4f})")

# --- Demostracion: mas n NO arregla el sesgo ---
for n in (50, 200, 1000):
    s = np.mean([media_muestra_sesgada(n) for _ in range(1000)]) - mu_real
    print(f"  sesgo con n={n:>4}: {s:+.4f}  (no se acerca a 0)")
```

```python
# --- VERIFICACION POR SEGUNDA VIA ---
# (a) Inversa/teoria: el error estandar empirico del muestreo aleatorio
#     debe coincidir con la formula EE = sigma/sqrt(n) (con correccion finita).
sigma_pob = poblacion.std(ddof=0)
n = 200
ee_formula = (sigma_pob / np.sqrt(n)) * np.sqrt((N - n) / (N - 1))
ee_empirico = estim_aleatorio.std(ddof=1)
print(f"EE formula={ee_formula:.4f}  EE empirico={ee_empirico:.4f}")
assert abs(ee_formula - ee_empirico) < 0.02, "EE teorico y empirico no concuerdan"

# (b) Sanity check: el estimador aleatorio es insesgado (~0), el sesgado NO.
assert abs(estim_aleatorio.mean() - mu_real) < 0.05, "aleatorio deberia ser insesgado"
assert (estim_sesgado.mean() - mu_real) > 0.5, "el sesgado deberia inflar el promedio"
print("OK: aleatorio insesgado; sesgo de seleccion confirmado y NO corregible con n.")
```

Salida (con semilla 42): promedio real ≈ 7.00; aleatorio ≈ 7.00 (sesgo ≈ 0); sesgado ≈ 8.6 (sesgo ≈ +1.6 fijo en todos los `n`). El `assert` del error estándar confirma que la fórmula `σ/√n` describe el muestreo aleatorio.

## Ejemplo trabajado

**Caso (LatAm):** GastroLatam vende la Calculadora de Costos en COP. Quieren saber el **ticket promedio** de los 4.000 restaurantes que la compraron este año. Encuestan vía WhatsApp.

- **Población:** 4.000 compradores.
- **Plan A (sesgado):** publican un link de encuesta en su estado de WhatsApp; responden 60 dueños, casi todos clientes "fans" que ya recomiendan el producto. Promedio reportado: $1.250.000 COP/mes.
- **Plan B (aleatorio):** toman los 4.000 números, eligen 300 *al azar* y llaman uno por uno hasta lograr respuesta. Promedio: $820.000 COP/mes.

Diferencia: $1.250.000 − $820.000 = **$430.000 COP** de inflación por sesgo de selección + no respuesta (solo fans contestaron el link). Si basan su pricing en el Plan A, sobreestiman lo que el cliente típico factura y ponen el producto demasiado caro.

Error de muestreo del Plan B (suponiendo σ ≈ $450.000 COP):

    EE = 450.000 / √300 · √((4000−300)/(4000−1))
       = 450.000 / 17,3205 · √(3700/3999)
       = 25.980,8 · 0,96196
       = $24.993 COP

Verificación de orden de magnitud: `√300 ≈ 17,3`, y `450.000/17,3 ≈ 26.000`; el factor finito (0,96) lo baja un poco → ~$25.000. Coherente.

**Resultado:** el ticket promedio del Plan B es ≈ **$820.000 ± ~$25.000 COP/mes** (error *aleatorio*, no sesgo). El Plan A tiene un error pequeño pero un **sesgo enorme**: es preciso y falso a la vez.

## Errores comunes / trampas

- **Confundir muestra grande con muestra buena.** 1 millón de respuestas voluntarias online valen menos que 1.000 elegidas al azar. (El clásico: la encuesta del Literary Digest de 1936, 2,4 millones de respuestas, predijo mal la elección por sesgo de muestra.)
- **Muestreo por conveniencia disfrazado de aleatorio.** "Pregunté a los que pasaban" NO es aleatorio.
- **Ignorar a los que NO contestaron.** Una tasa de respuesta del 5% casi garantiza sesgo de no respuesta; reporta siempre la tasa.
- **Sesgo de supervivencia.** Analizar solo clientes activos / negocios que siguen abiertos / fondos que no quebraron infla cualquier métrica de éxito.
- **Creer que un intervalo de confianza arregla el sesgo.** El intervalo solo mide el error *aleatorio*; si hay sesgo, el intervalo está centrado en el lugar equivocado (ver [[66-intervalos-de-confianza]]).
- **Auto-selección.** Quien decide entrar a la muestra (reseñas, encuestas opt-in) ya está sesgado: los muy felices y los muy enojados sobre-responden.

### Mini-checklist de exactitud
- [ ] ¿La muestra fue elegida AL AZAR de toda la población, o solo de "los que aparecieron"?
- [ ] ¿Reporté el tamaño `n` Y la tasa de respuesta, y descarté sesgos de selección/supervivencia/no respuesta?
- [ ] ¿Separé el error aleatorio (`σ/√n`) del posible sesgo (que `n` NO corrige)?

## Cruces
- [[60-estadistica-descriptiva]] — cómo resumir la muestra (media, mediana) antes de inferir.
- [[66-intervalos-de-confianza]] — cuantifica el error aleatorio de un estimador muestral.
- [[67-pruebas-de-hipotesis]] — decidir si una diferencia entre muestras es real o azar.
- [[58-simulacion-monte-carlo]] — método usado arriba para ver el comportamiento de un estimador.
- [[69-estadistica-enganosa]] — cómo se manipulan muestras para mentir con datos.
