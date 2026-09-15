# 63 · Correlación vs causalidad

> **Qué resuelve / cuándo usarlo** — Para no tomar decisiones caras creyendo que "A mueve a B" cuando solo van juntos por azar o por una tercera variable. Úsalo siempre que veas dos cosas que suben/bajan a la vez y quieras concluir que una *causa* la otra.

## Concepto (para no-experto)

**Correlación** = dos variables (cosas que medimos con números, p. ej. gasto en publicidad y ventas) tienden a moverse juntas. Cuando una sube, la otra sube (correlación positiva) o baja (correlación negativa).

**Causalidad** = mover una variable *provoca* el cambio en la otra. Si bajo el precio y por eso vendo más, eso es causa.

La trampa más cara del análisis de datos es esta: **correlación NO implica causalidad**. Que dos cosas vayan juntas no prueba que una mande sobre la otra.

Analogía cotidiana: en una ciudad, las ventas de helados y los ahogamientos en piscina suben al mismo tiempo. ¿El helado ahoga gente? No. Hay una **tercera variable** que mueve a las dos: el **calor del verano**. Más calor → más helados Y más gente nadando. El helado y los ahogamientos están *correlacionados* pero ninguno *causa* al otro.

Esa tercera variable que explica la coincidencia se llama **variable confusora** (o *confounder*): una variable oculta que influye en las dos que estás comparando y te hace creer en una relación falsa.

Hay tres explicaciones posibles cada vez que ves correlación entre A y B:
1. **A causa B** (lo que normalmente quieres concluir).
2. **B causa A** (causalidad invertida — quizá las ventas hacen que inviertas más en ads, no al revés).
3. **C causa A y B** (variable confusora — como el calor).
4. **Pura casualidad** (correlación espuria — coincidencia numérica sin ninguna relación real).

Para una decisión con dinero, debes descartar las opciones 2, 3 y 4 antes de afirmar la 1.

## Fórmulas / método

El **coeficiente de correlación de Pearson** mide qué tan fuerte y en qué dirección dos variables se mueven *en línea recta* (relación lineal). Se llama **r** y va de −1 a +1.

$$
r = \frac{\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^{n}(x_i - \bar{x})^2}\;\sqrt{\sum_{i=1}^{n}(y_i - \bar{y})^2}}
$$

Símbolos:
- **x_i, y_i** = el dato i de cada variable (par de mediciones tomadas a la vez).
- **x̄, ȳ** ("equis barra", "ye barra") = la media (promedio) de cada variable.
- **n** = cantidad de pares de datos.
- **r** = coeficiente de correlación. Es **adimensional** (no tiene unidades; es un número puro).

Interpretación de r:
- **r = +1** → relación lineal positiva perfecta (los puntos caen exactos en una recta que sube).
- **r = −1** → relación lineal negativa perfecta (recta que baja).
- **r = 0** → no hay relación *lineal* (puede haber relación curva que r no detecta).
- Guía aproximada del valor absoluto |r|: 0–0.3 débil, 0.3–0.7 moderada, 0.7–1 fuerte.

**r² (r al cuadrado)** = fracción de la variación de una variable que la otra "explica" estadísticamente. Si r = 0.8, entonces r² = 0.64 → el 64 % de la variación va junta. **r² NO mide causa**, solo asociación.

Clave: **r mide correlación, jamás causalidad.** Ninguna fórmula prueba causa. La causa se establece con diseño experimental (ver Errores comunes).

## Verificación en código

```python
# Demostración: dos variables MUY correlacionadas que NO se causan,
# ambas movidas por una variable confusora (el "calor").
import numpy as np
from scipy import stats

rng = np.random.default_rng(42)  # semilla fija -> resultado reproducible
n = 200

# Variable confusora oculta: temperatura (grados C)
calor = rng.normal(25, 6, n)              # media 25 C, desv. 6 C

# Helados y ahogamientos: cada uno depende del CALOR + ruido propio.
# Ninguno depende del otro.
helados      = 50 + 8.0 * calor + rng.normal(0, 20, n)   # unidades vendidas
ahogamientos = 1  + 0.30 * calor + rng.normal(0, 1.5, n) # incidentes

# Correlación INGENUA helados vs ahogamientos (parecen relacionados)
r_ingenuo, p_ingenuo = stats.pearsonr(helados, ahogamientos)
print(f"r ingenuo (helados vs ahogamientos): {r_ingenuo:.4f}  (p={p_ingenuo:.2e})")

# Ahora CONTROLAMOS la confusora: correlacion PARCIAL quitando el efecto del calor.
# Truco: regresamos cada variable contra 'calor' y correlacionamos los RESIDUOS
# (lo que queda sin explicar por el calor).
def residuos(y, x):
    b1, b0, *_ = stats.linregress(x, y)   # pendiente, intercepto
    return y - (b0 + b1 * x)              # parte NO explicada por x

res_helados      = residuos(helados, calor)
res_ahogamientos = residuos(ahogamientos, calor)
r_parcial, p_parcial = stats.pearsonr(res_helados, res_ahogamientos)
print(f"r parcial (controlando calor):       {r_parcial:.4f}  (p={p_parcial:.2e})")
```

Salida (reproducible con la semilla 42):
```
r ingenuo (helados vs ahogamientos): 0.7837  (p=2.6e-42)
r parcial (controlando calor):       0.0461  (p=5.18e-01)
```

Lectura: el r ingenuo de **0.78** grita "fuerte relación", pero al **controlar la confusora** cae a **0.05** con p = 0.52 (no significativo). Conclusión correcta: helados y ahogamientos NO se causan; el calor los movía a los dos.

**Verificación por segunda vía** (cálculo manual de r con la fórmula, sin scipy, para confirmar que scipy no miente):

```python
# Recalculamos r ingenuo a mano desde la definicion y comprobamos que coincide.
x, y = helados, ahogamientos
mx, my = x.mean(), y.mean()
num = np.sum((x - mx) * (y - my))
den = np.sqrt(np.sum((x - mx)**2)) * np.sqrt(np.sum((y - my)**2))
r_manual = num / den
print(f"r manual: {r_manual:.4f}")
assert abs(r_manual - r_ingenuo) < 1e-9, "discrepancia: revisar"
print("OK: la formula a mano coincide con scipy.")

# Sanity check de rango: r SIEMPRE debe estar en [-1, 1]
assert -1.0 <= r_manual <= 1.0
```

## Ejemplo trabajado

**Caso GastroLatam (negocio real).** El dueño nota que los meses con más publicidad en redes son los meses con más ventas de la Calculadora de Costos. r = **0.82** entre *gasto en ads (COP)* y *ventas (unidades)* en 12 meses. Tentación: "cada peso en ads causa ventas, ¡subamos el presupuesto!".

Paso 1 — Calcular r y r²:
- r = 0.82 → relación fuerte y positiva.
- r² = 0.82² = **0.6724** → el 67.24 % de la variación de ventas va junta con el gasto en ads.

Paso 2 — Listar explicaciones rivales antes de creer en causa:
- ¿Causa invertida? Quizá en meses buenos (más ventas) el dueño *decide* invertir más en ads → ventas causarían el gasto, no al revés.
- ¿Confusora? La **temporada**: en enero (cierre fiscal de restaurantes) hay más demanda de la calculadora Y el dueño pauta más. La temporada movería ambas.
- ¿Espuria? Con solo n = 12 meses, una r alta puede salir por azar más fácilmente.

Paso 3 — Decisión honesta: r = 0.82 (adimensional) **no autoriza** afirmar "ads causa ventas". Antes de subir el presupuesto, hay que **probar la causa**: hacer un experimento controlado (apagar ads en una región o semana y comparar — ver módulo de A/B testing). Sin eso, el número es una correlación, no una palanca.

Resultado verificado: r = **0.82** (sin unidades), r² = **0.6724** (proporción, sin unidades). Acción correcta: experimentar, no asumir.

## Errores comunes / trampas

- **Concluir causa desde correlación.** El pecado capital. r alto solo dice "van juntas".
- **Ignorar la causa invertida.** Antes de "A→B", pregúntate si "B→A" explica igual de bien.
- **Olvidar la variable confusora.** Casi siempre hay una tercera variable; búscala activamente y contrólala (correlación parcial, segmentación, o experimento).
- **Correlaciones espurias por muestra chica o por minería de datos.** Si pruebas 100 pares de variables, varias darán r alto por puro azar. Con pocos datos, r baila mucho.
- **r = 0 ≠ "no hay relación".** r solo ve líneas rectas. Una relación en forma de U (ej. precio vs satisfacción) puede tener r ≈ 0 y aun así existir. Grafica siempre el diagrama de dispersión (scatter).
- **Outliers que inflan o invierten r.** Un solo dato extremo puede mover r de 0.1 a 0.9. Revisa el scatter.
- **Confundir r con r² o con la pendiente.** Son tres cosas distintas: dirección/fuerza (r), varianza explicada (r²) y cuánto cambia y por unidad de x (pendiente, ver regresión).

### Cómo comunicarlo (sin engañar)
- Di "**asociado con**" o "**correlacionado con**", nunca "causa" ni "provoca", salvo que tengas un experimento.
- Acompaña r con el **scatter plot**, el **n** y la **incertidumbre** (valor p / intervalo).
- Nombra explícitamente la confusora que controlaste (o admite que no pudiste).
- Para afirmar causa: experimento aleatorizado (A/B), o al menos control de confusoras y lógica temporal (la causa precede al efecto).

## Cruces

- [[64-regresion-lineal]] — pasa de "van juntas" a "cuánto cambia y por cada unidad de x".
- [[68-ab-testing]] — el experimento aleatorizado, la forma correcta de *probar* causa.
- [[60-estadistica-descriptiva]] — medias y bases para calcular r.
- [[69-estadistica-enganosa]] — cómo se abusa de la correlación para mentir con datos.
- [[65-muestreo-y-sesgos]] — muestras malas que fabrican correlaciones falsas.

---

**Mini-checklist de exactitud**
- [ ] ¿r está dentro de [−1, 1] y lo verifiqué con la fórmula a mano (assert)?
- [ ] ¿Listé y descarté causa invertida, confusora y azar antes de hablar de causa?
- [ ] ¿Comuniqué "asociado con" (no "causa") salvo que tenga un experimento?
