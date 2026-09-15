# 50 · Fundamentos de probabilidad

> **Qué resuelve / cuándo usarlo** — Cuando necesitas medir qué tan probable es algo (que un cliente compre, que un pago falle, que salga cara) y traducir esa incertidumbre a un número exacto entre 0 y 1. Es la base de todo lo demás: Bayes, distribuciones, A/B testing, riesgo.

## Concepto (para no-experto)

La **probabilidad** es un número que mide *qué tan posible* es que ocurra algo, en una escala fija: **0 = imposible**, **1 = seguro** (también se escribe como porcentaje: 0% a 100%). Nada puede tener probabilidad mayor que 1 ni menor que 0. Si alguien te dice "tengo 120% de probabilidad de vender", está mal por definición.

Definamos los ladrillos básicos, cada uno con su nombre técnico:

- **Experimento aleatorio**: una acción cuyo resultado no podemos predecir con certeza antes de hacerla. Ejemplos: lanzar un dado, abrir el chat de un lead nuevo, ver si un pago con tarjeta es aprobado.
- **Espacio muestral** (símbolo Ω, la letra griega "omega"): el conjunto de **todos** los resultados posibles del experimento. Para un dado de 6 caras, Ω = {1, 2, 3, 4, 5, 6}. Es como la lista completa de lo que *puede* pasar.
- **Evento** (símbolo A, B, ...): cualquier subconjunto del espacio muestral, es decir, un grupo de resultados que nos interesa. "Sacar par" es el evento A = {2, 4, 6}. Un evento puede ser un solo resultado o varios.
- **Resultado favorable**: cada resultado del espacio muestral que cumple con el evento.

**Analogía cotidiana**: imagina una bolsa con 10 fichas, 3 rojas y 7 azules. El espacio muestral es "las 10 fichas que podrías sacar". El evento "sacar roja" tiene 3 resultados favorables. La probabilidad de sacar roja es 3 de 10 = 0,30 = 30%. Es literalmente *contar lo que te sirve y dividir entre todo lo posible*.

Hay **dos formas de asignar** ese número, y conviene no confundirlas:

1. **Probabilidad clásica** (teórica): cuando todos los resultados son *igualmente posibles*, se cuenta. P = casos favorables / casos totales. Sirve para dados, monedas, barajas, sorteos justos.
2. **Probabilidad frecuentista** (empírica): cuando NO sabemos si son igualmente posibles (¿un cliente compra o no?), la estimamos repitiendo y observando. P ≈ veces que ocurrió / veces que lo intentamos. Por ejemplo, si de 200 chats 30 terminaron en venta, estimamos P(venta) ≈ 30/200 = 0,15. Cuantas más repeticiones, más confiable es la estimación (esto es la **Ley de los Grandes Números**: la frecuencia observada se acerca a la probabilidad real a medida que repites).

## Fórmulas / método

**Probabilidad clásica** (resultados equiprobables):

```
P(A) = |A| / |Ω|
```

- `P(A)` = probabilidad del evento A (número sin unidades, entre 0 y 1).
- `|A|` = cantidad de resultados favorables (cuántos elementos tiene A).
- `|Ω|` = cantidad total de resultados posibles (tamaño del espacio muestral).

**Probabilidad frecuentista** (estimación empírica):

```
P(A) ≈ n_A / n
```

- `n_A` = número de veces que ocurrió A.
- `n` = número total de repeticiones del experimento.

**Axiomas (reglas que SIEMPRE deben cumplirse):**

```
1)  0 ≤ P(A) ≤ 1               (rango: nunca negativo, nunca mayor que 1)
2)  P(Ω) = 1                   (algo del espacio muestral seguro ocurre)
3)  P(∅) = 0                   (el evento imposible tiene probabilidad 0)
4)  Suma de P de todos los resultados de Ω = 1
```

**Evento complementario** (lo contrario de A, símbolo Aᶜ o "no A"):

```
P(Aᶜ) = 1 − P(A)
```

Truco práctico: a veces es más fácil calcular la probabilidad de que algo NO pase y restar de 1.

> Probabilidad es **adimensional** (no tiene unidades). Si te aparece con unidades, algo se mezcló mal.

## Verificación en código

Filosofía error cero: calculamos exacto con `fractions` (fracciones, sin redondeo flotante) y **verificamos por una segunda vía con una simulación** (Monte Carlo) que debe acercarse al valor teórico.

```python
from fractions import Fraction
import random

# --- VÍA 1: cálculo EXACTO (probabilidad clásica con fracciones, sin float) ---
# Experimento: lanzar un dado de 6 caras (equiprobable).
espacio = [1, 2, 3, 4, 5, 6]          # espacio muestral Omega
evento_par = [x for x in espacio if x % 2 == 0]   # evento A = sacar par = {2,4,6}

P_par = Fraction(len(evento_par), len(espacio))   # |A| / |Omega|
print("P(par) exacta =", P_par, "=", float(P_par))  # 1/2 = 0.5

# Comprobamos los AXIOMAS:
assert 0 <= P_par <= 1, "FALLO: probabilidad fuera de [0,1]"

# La suma de TODOS los resultados de Omega debe dar exactamente 1
suma_total = sum(Fraction(1, len(espacio)) for _ in espacio)
assert suma_total == 1, "FALLO: las probabilidades no suman 1"

# Complemento: P(impar) = 1 - P(par)
P_impar = 1 - P_par
print("P(impar) = 1 - P(par) =", P_impar)
assert P_par + P_impar == 1, "FALLO: A y su complemento no suman 1"
```

```python
# --- VÍA 2: VERIFICACIÓN por simulación (frecuentista) ---
# Si la teoría dice 0.5, al lanzar el dado muchas veces la frecuencia debe acercarse.
random.seed(42)                 # semilla fija => resultado reproducible
N = 1_000_000                   # un millón de lanzamientos
pares = sum(1 for _ in range(N) if random.randint(1, 6) % 2 == 0)
P_par_sim = pares / N
print("P(par) simulada  =", P_par_sim)

# Deben coincidir dentro de un margen pequeño (la simulación tiene ruido estadístico).
assert abs(P_par_sim - float(P_par)) < 0.005, "FALLO: simulacion no concuerda con teoria"
print("OK: teoria y simulacion concuerdan.")
```

Salida esperada:

```
P(par) exacta = 1/2 = 0.5
P(impar) = 1 - P(par) = 1/2
P(par) simulada  = 0.499...
OK: teoria y simulacion concuerdan.
```

La doble vía es el corazón del método: la fracción `1/2` es la verdad exacta; la simulación de un millón de lanzamientos *confirma* que ese número describe la realidad.

## Ejemplo trabajado

**Contexto LatAm (GastroLatam):** El bot Luis recibió **240 conversaciones** en el mes. De esas, **36** terminaron en una compra de la Calculadora de Costos. ¿Cuál es la probabilidad estimada de que un chat nuevo termine en venta? ¿Y la de que NO termine en venta?

Paso 1 — Identificar el tipo. No sabemos si todos los chats son "igualmente compradores", así que usamos **probabilidad frecuentista** (estimación por observación).

Paso 2 — Definir el evento. A = "el chat termina en venta". n_A = 36, n = 240.

Paso 3 — Calcular exacto.

```python
from fractions import Fraction

n_A = 36
n   = 240
P_venta = Fraction(n_A, n)          # 36/240
print(P_venta, "=", float(P_venta)) # 3/20 = 0.15

# Complemento: probabilidad de NO vender
P_no_venta = 1 - P_venta
print(P_no_venta, "=", float(P_no_venta))  # 17/20 = 0.85

# Verificacion 1 (segunda via): deben sumar exactamente 1
assert P_venta + P_no_venta == 1
# Verificacion 2 (orden de magnitud): 36 es ~15% de 240; 0.15 tiene sentido
assert 0 <= P_venta <= 1
```

Paso 4 — Resultado **con su interpretación y "unidades"** (aquí la unidad natural es el porcentaje):

- **P(venta) = 3/20 = 0,15 = 15 %** de los chats nuevos.
- **P(no venta) = 17/20 = 0,85 = 85 %**.

Lectura de negocio: de cada 100 conversaciones nuevas, se espera **≈ 15 ventas** (15 chats × valor; con producto a $10.000 COP, eso es 15 × $10.000 = **$150.000 COP** por cada 100 chats, en promedio). Ojo: 36 casos es una muestra modesta — la estimación tiene incertidumbre (ver [[66-intervalos-de-confianza]]).

## Errores comunes / trampas

- **Probabilidad > 1 o negativa.** Si un cálculo da 1,3 o −0,2, hay un error seguro (sumaste mal, contaste favorables más de una vez, o usaste la fórmula equivocada). Los axiomas son un *sanity check* gratis.
- **Confundir "favorables/totales" cuando los casos NO son equiprobables.** La fórmula clásica P = |A|/|Ω| SOLO vale si cada resultado tiene la misma posibilidad. "Llueve o no llueve" no es 1/2 solo porque haya dos opciones.
- **Sumar probabilidades de eventos que se solapan** sin restar la intersección (eso se corrige en [[51-reglas-de-probabilidad]] con P(A∪B) = P(A)+P(B)−P(A∩B)).
- **Calcular con `float` y arrastrar error.** 0.1 + 0.2 no da exactamente 0.3 en flotante. Para exactitud usa `Fraction` (o `decimal` si es dinero); redondea UNA sola vez al final (ver [[12-fracciones-decimales-y-precision]]).
- **Estimar frecuentista con pocas repeticiones** y tratar el número como verdad absoluta. 1 de 2 chats = 50% es ruido, no una probabilidad confiable. Más datos → más confianza (Ley de los Grandes Números).
- **Olvidar que probabilidad ≠ frecuencia garantizada.** P(venta)=15% no significa "exactamente 15 de las próximas 100"; es el promedio a largo plazo.

## Cruces

- [[51-reglas-de-probabilidad]] — sumar, multiplicar, condicional e independencia (el paso siguiente natural).
- [[52-teorema-de-bayes]] — actualizar una probabilidad cuando llega nueva información.
- [[53-combinatoria]] — contar bien |A| y |Ω| cuando hay muchas combinaciones.
- [[58-simulacion-monte-carlo]] — el método de verificación por simulación, a fondo.
- [[59-falacias-de-probabilidad]] — los engaños mentales típicos (jugador, base rate, etc.).

---

**Mini-checklist de exactitud**
- [ ] El resultado está dentro de [0, 1] (o 0%–100%) y la suma sobre todo Ω da exactamente 1.
- [ ] Verifiqué por segunda vía (complemento que suma 1, y/o simulación que concuerda con la teoría).
- [ ] Usé `Fraction`/`decimal`, no `float`, y redondeé solo al final.
