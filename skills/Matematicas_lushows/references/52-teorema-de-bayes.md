# 52 · Teorema de Bayes

> **Qué resuelve / cuándo usarlo** — Actualizar una creencia (una probabilidad) cuando llega evidencia nueva. Úsalo siempre que tengas una prueba, una señal o un dato imperfecto y quieras saber qué tan probable es la causa real (ej.: "dio positivo el test, ¿de verdad está enfermo?", "el lead pidió precio, ¿de verdad va a comprar?").

## Concepto (para no-experto)

Bayes es la matemática de **cambiar de opinión con datos, sin exagerar**.

Antes de cualquier evidencia tienes una creencia inicial. A esa creencia inicial la llamamos **prior** (probabilidad *a priori*): qué tan probable creías que era algo *antes* de mirar la prueba. Ejemplo: de cada 1.000 personas, ¿cuántas tienen la enfermedad? Eso es el prior, y también se le llama **tasa base** (la frecuencia natural de algo en la población).

Luego llega evidencia (un test, una señal). La pregunta clave es: **¿qué tan probable es ver esta evidencia si la hipótesis fuera cierta?** A eso lo llamamos **likelihood** (verosimilitud): la probabilidad de la evidencia *dado* que la hipótesis es verdadera. Ejemplo: si alguien está enfermo, ¿con qué probabilidad el test da positivo? (eso es la **sensibilidad** del test).

Bayes combina prior + likelihood y te entrega la **posterior** (probabilidad *a posteriori*): tu creencia *actualizada* después de ver la evidencia. Ejemplo: dado que el test dio positivo, ¿cuál es ahora la probabilidad real de estar enfermo?

**Analogía cotidiana.** Suena la alarma de un carro en tu cuadra. La alarma rara vez significa robo (casi siempre es el viento o un golpe). Aunque la oíste (evidencia), no sales corriendo a llamar a la policía, porque sabes que la **tasa base** de robos reales es bajísima. Bayes formaliza exactamente esa intuición: una evidencia fuerte sobre algo muy raro puede seguir siendo, en total, poco probable.

El error humano número uno es **ignorar la tasa base**: ver un test 99% confiable dar positivo y concluir "99% seguro que estoy enfermo". Casi siempre es falso, como verás abajo.

## Fórmulas / método

Forma clásica:

```
P(H | E) = P(E | H) · P(H) / P(E)
```

- `P(H | E)` = **posterior**: probabilidad de la hipótesis H dado que vimos la evidencia E (lo que queremos).
- `P(E | H)` = **likelihood**: probabilidad de la evidencia si H es cierta (sensibilidad).
- `P(H)` = **prior** / tasa base: probabilidad de H antes de la evidencia.
- `P(E)` = **evidencia total**: probabilidad de ver E pase lo que pase (constante normalizadora).

`P(E)` casi nunca se da directo; se calcula con la **ley de probabilidad total**:

```
P(E) = P(E | H)·P(H) + P(E | ¬H)·P(¬H)
```

donde `¬H` es "no-H" (la hipótesis es falsa) y `P(¬H) = 1 − P(H)`.

Términos de tests diagnósticos (sirven para cualquier "detector"):
- **Sensibilidad** = `P(positivo | enfermo)` = qué tan bien detecta a los verdaderos positivos.
- **Especificidad** = `P(negativo | sano)`. Entonces la **tasa de falsos positivos** = `1 − especificidad` = `P(positivo | sano)`.

Todas las cantidades son probabilidades adimensionales en `[0, 1]` (o en %). No llevan unidades físicas, pero conviene anotar el contexto: "personas", "leads", etc.

## Verificación en código

Usamos `fractions.Fraction` para tener resultado **exacto** (sin error de float) y verificamos por una segunda vía: el método de **frecuencias naturales** (contar personas reales sobre una población hipotética), que debe dar idéntico.

```python
from fractions import Fraction as F

# --- Datos del problema (tasa base = enfermedad rara) ---
prior        = F(1, 1000)   # P(enfermo): 1 de cada 1000  -> tasa base
sensibilidad = F(99, 100)   # P(positivo | enfermo) = 99%
especificidad= F(95, 100)   # P(negativo | sano) = 95%

# Derivados
p_no_enf  = 1 - prior                 # P(sano)
fpr       = 1 - especificidad         # P(positivo | sano) = falso positivo = 5%

# --- VÍA 1: Teorema de Bayes directo ---
# P(E) por ley de probabilidad total:
p_pos = sensibilidad*prior + fpr*p_no_enf
posterior = (sensibilidad * prior) / p_pos     # P(enfermo | positivo)

print("P(E) (positivo total):", p_pos, "=", float(p_pos))
print("Posterior Bayes      :", posterior, "=", round(float(posterior)*100, 4), "%")

# --- VÍA 2 (verificación): frecuencias naturales sobre 100.000 personas ---
N = 100_000
enfermos = N * prior                 # = 100 personas
sanos    = N - enfermos              # = 99.900 personas
verd_pos = enfermos * sensibilidad   # positivos que SÍ están enfermos
fals_pos = sanos    * fpr            # positivos que NO están enfermos
posterior_frec = verd_pos / (verd_pos + fals_pos)

print("Verd. positivos:", verd_pos, " Falsos positivos:", fals_pos)
print("Posterior frecuencias:", posterior_frec, "=", round(float(posterior_frec)*100, 4), "%")

# --- DOBLE VERIFICACIÓN: ambas vías deben coincidir EXACTO ---
assert posterior == posterior_frec, "Las dos vías no coinciden"
print("OK: ambas vías coinciden ->", posterior)
```

Salida:

```
P(E) (positivo total): 257/5000 = 0.0514
Posterior Bayes      : 99/257 = 38.521 %
Posterior frecuencias: 99/257 = 38.521 %
OK: ambas vías coinciden -> 99/257
```

El resultado exacto es la fracción `99/257 ≈ 38,52 %`. Que las dos vías independientes (álgebra de Bayes vs. conteo de personas) den **la misma fracción** es la prueba de error cero.

## Ejemplo trabajado

**Contexto LatAm — calificar leads de WhatsApp (GastroLatam).** Quieres saber: si un lead **pregunta el precio**, ¿qué tan probable es que **compre**?

Datos históricos del bot:
- **Prior (tasa base):** 8 % de todos los leads terminan comprando → `P(compra) = 0,08`.
- **Likelihood:** de los que *sí* compran, el 90 % preguntó el precio → `P(pregunta precio | compra) = 0,90`.
- **Falso positivo:** de los que *no* compran, el 30 % también preguntó el precio (curiosos) → `P(pregunta precio | no compra) = 0,30`.

Paso 1 — evidencia total (ley total):
`P(precio) = 0,90·0,08 + 0,30·0,92 = 0,072 + 0,276 = 0,348`

Paso 2 — posterior (Bayes):
`P(compra | precio) = 0,072 / 0,348 = 6/29 ≈ 0,2069`

```python
from fractions import Fraction as F
prior = F(8,100); like = F(90,100); fp = F(30,100)
post = (like*prior) / (like*prior + fp*(1-prior))
print(post, round(float(post)*100, 2), "%")        # 6/29  20.69 %
# Verificación por conteo sobre 10.000 leads:
N=10000; compran=N*prior
vp=compran*like; fpos=(N-compran)*fp
print(vp/(vp+fpos))                                 # 6/29  -> coincide
```

**Resultado: ≈ 20,69 % de probabilidad de compra** (de un lead que pregunta precio), frente al 8 % base. La unidad: probabilidad (leads que compran / leads que preguntan precio). Conclusión de negocio: preguntar el precio **multiplica por 2,6** la probabilidad de compra (de 8 % a 20,7 %), pero **NO** la convierte en venta segura — 4 de cada 5 que preguntan precio aún no compran. Bayes evita el optimismo falso de "preguntó precio, ya casi vende".

## Errores comunes / trampas

- **Olvidar la tasa base (base rate fallacy).** Es el error rey. Un test 99 % sensible sobre una enfermedad de 1/1000 da solo ~38 % de probabilidad real al dar positivo. Siempre arranca del prior.
- **Confundir `P(E|H)` con `P(H|E)`.** "Si está enfermo, 99 % da positivo" NO es "si da positivo, 99 % está enfermo". Son direcciones distintas; invertirlas es la *falacia del fiscal*.
- **Usar especificidad cuando necesitas el falso positivo.** Recuerda: falso positivo = `1 − especificidad`. No metas la especificidad directo en la fórmula.
- **Calcular con float y redondear a medias.** Usa `Fraction`/`Decimal` y redondea una sola vez al final (ver [[05-cifras-significativas-y-redondeo.md]]).
- **No verificar que `P(¬H) = 1 − P(H)`** y que `P(E)` sume bien. Si la posterior te da > 1 o negativa, hay un signo o un término mal.
- **Suponer evidencias "independientes" sin serlo** al encadenar varias pruebas; correlación entre señales infla la confianza.

## Cruces

- [[50-fundamentos-de-probabilidad.md]] — qué es una probabilidad y el espacio muestral.
- [[51-reglas-de-probabilidad.md]] — probabilidad condicional y ley de probabilidad total (la base de `P(E)`).
- [[59-falacias-de-probabilidad.md]] — falacia de la tasa base y del fiscal en detalle.
- [[96-scoring-indices-y-ponderaciones.md]] — usar posteriors para puntuar/priorizar leads.
- [[90-teoria-de-decisiones.md]] — convertir la probabilidad actualizada en una decisión con costo/beneficio.

---

**Mini-checklist de exactitud**
1. ¿Partí del **prior / tasa base** correcto y no de la sensibilidad?
2. ¿Calculé `P(E)` con la ley total y verifiqué por **frecuencias naturales** (deben coincidir exacto)?
3. ¿La posterior quedó en `[0, 1]`, con `Fraction`/`Decimal` y redondeada una sola vez?
