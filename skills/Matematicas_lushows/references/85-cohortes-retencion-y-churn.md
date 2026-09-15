# 85 · Cohortes, retención y churn

> **Qué resuelve / cuándo usarlo** — Mide cuántos clientes se quedan vs. cuántos se van con el tiempo, agrupados por el momento en que entraron (cohorte), y traduce esa fuga en una "vida media" del cliente. Úsalo para saber si tu negocio retiene o tiene un balde con hueco.

## Concepto (para no-experto)

Imagina que cada mes entra un grupo de clientes nuevos a tu negocio. Ese grupo —todos los que llegaron en el mismo periodo— es una **cohorte** (palabra de origen militar: un grupo que avanza junto). En enero entran 100 personas: esa es "la cohorte de enero". En febrero entran otras 80: "la cohorte de febrero". Cada cohorte vive su propia historia.

La pregunta clave es: **de los que entraron, ¿cuántos siguen contigo después de 1 mes, 2 meses, 3 meses…?**

- **Retención** = el porcentaje de la cohorte que **sigue activo** después de cierto tiempo. Si de 100 clientes de enero, 70 siguen comprando en febrero, la retención al mes 1 es 70%.
- **Churn** (se pronuncia "chern", inglés para "abandono/fuga") = el porcentaje que **se fue**. Es el complemento de la retención: si retienes 70%, tu churn es 30%.

Analogía cotidiana: tu base de clientes es un balde con agua. Cada mes entra agua nueva (clientes nuevos) pero el balde tiene un **hueco** (churn) por donde se escapa agua. Si el hueco es grande, por más que eches agua, el balde nunca se llena. La retención mide qué tan tapado está el hueco.

La **curva de cohorte** es simplemente graficar la retención mes a mes: empieza en 100% (mes 0, todos están) y baja. Lo crítico no es solo qué tan rápido baja, sino **si se aplana** (clientes leales que ya no se van) o **llega a cero** (nadie se queda).

La **vida media del cliente** (en inglés *customer lifetime*, no confundir con LTV que es el valor en dinero) es cuántos periodos, en promedio, dura un cliente antes de irse. Si cada mes se va el 20%, en promedio un cliente dura 5 meses. Ese número alimenta el LTV (ver [[83-cac-ltv-y-payback]]).

## Fórmulas / método

Sea una cohorte que empieza con `N₀` clientes activos en el periodo 0.

**Retención al periodo `t`** (porcentaje, adimensional):
```
R(t) = activos_en_t / N₀
```
Por construcción `R(0) = 1` (100%).

**Churn del periodo `t`** (cuántos se fueron entre `t-1` y `t`, relativo a los que había en `t-1`):
```
churn(t) = (activos_en_(t-1) − activos_en_t) / activos_en_(t-1)
retención_periodo(t) = activos_en_t / activos_en_(t-1) = 1 − churn(t)
```

**Tasa de churn mensual promedio** `c` (cuando es razonablemente constante): la fracción que se va cada mes.

**Modelo geométrico de retención** (asume churn constante `c` por periodo):
```
R(t) = (1 − c)^t
```
Cada periodo sobrevive una fracción `(1−c)` de los que quedaban.

**Vida media del cliente** `L` (en periodos) bajo churn constante `c`:
```
L = 1 / c        [periodos]
```
Derivación: la vida esperada es la suma `Σ_{t=0}^{∞} R(t) = Σ (1−c)^t = 1/(1 − (1−c)) = 1/c` (serie geométrica, ver [[19-secuencias-y-series]]).

> ⚠️ Sutileza de unidades: `L = 1/c` cuenta el periodo de entrada como periodo 1 (suma desde t=0). Es la convención estándar para LTV. Si quieres "meses adicionales tras el primero", es `(1−c)/c`. Hay que ser explícito.

**Conversión entre churn de distintas frecuencias** (NO se multiplica, se compone — igual que el interés, ver [[71-interes-simple-y-compuesto]]):
```
churn_anual = 1 − (1 − churn_mensual)^12
churn_mensual = 1 − (1 − churn_anual)^(1/12)
```

Símbolos: `c` = tasa de churn por periodo (fracción 0–1); `R(t)` = retención (fracción); `L` = vida media (periodos); `N₀` = tamaño inicial de cohorte (clientes).

## Verificación en código

```python
# Análisis de cohortes: retención, churn y vida media. Exacto con Fraction.
from fractions import Fraction as F
from decimal import Decimal, ROUND_HALF_UP

# --- Datos reales: una cohorte seguida mes a mes (clientes activos) ---
activos = [200, 150, 120, 102, 90, 81]   # mes 0..5
N0 = activos[0]

# Retención R(t) = activos_t / N0  (fracción exacta)
retencion = [F(a, N0) for a in activos]
print("Retención por mes:")
for t, r in enumerate(retencion):
    print(f"  mes {t}: {r}  = {float(r)*100:.2f}%")

# Churn periodo a periodo: (prev - curr) / prev
churn_periodo = [F(activos[t-1]-activos[t], activos[t-1]) for t in range(1, len(activos))]
print("\nChurn por periodo:")
for t, c in enumerate(churn_periodo, start=1):
    print(f"  mes {t-1}->{t}: {c} = {float(c)*100:.2f}%")

# --- VERIFICACIÓN 1 (inversa): retención_periodo = 1 - churn, y el producto
#     acumulado de retenciones periodo a periodo debe dar R(t) total ---
acum = F(1)
for t in range(1, len(activos)):
    acum *= (1 - churn_periodo[t-1])          # (1 - churn) = retención del periodo
    assert acum == retencion[t], f"falla en mes {t}"
print("\n[OK] producto de (1-churn) reconstruye la retención acumulada")

# --- Vida media bajo churn constante. Tomamos c = churn promedio estable ---
# Usamos el churn medio de los últimos periodos (más estable): mes 3->4 y 4->5
c = (churn_periodo[3] + churn_periodo[4]) / 2   # promedio exacto
L = 1 / c                                        # vida media en meses
print(f"\nChurn estable c = {c} = {float(c)*100:.4f}%")
print(f"Vida media L = 1/c = {float(L):.2f} meses")

# --- VERIFICACIÓN 2 (segunda vía): sumar la serie geométrica truncada ---
# Σ (1-c)^t debe acercarse a 1/c. Sumamos muchos términos y comparamos.
suma = F(0)
uno_menos_c = 1 - c
term = F(1)
for _ in range(2000):       # suficientes términos para converger
    suma += term
    term *= uno_menos_c
print(f"Σ(1-c)^t (2000 términos) = {float(suma):.6f}  vs  1/c = {float(L):.6f}")
assert abs(suma - L) < F(1, 10**6), "la serie no converge a 1/c"
print("[OK] la serie geométrica confirma L = 1/c")

# --- Conversión churn mensual <-> anual (composición, no multiplicación) ---
c_mensual = Decimal("0.10")            # 10% mensual
c_anual = Decimal(1) - (Decimal(1) - c_mensual) ** 12
print(f"\nChurn 10% mensual -> anual = {(c_anual*100).quantize(Decimal('0.01'))}%")
# Verificación inversa: de anual de vuelta a mensual debe dar ~10%
vuelta = Decimal(1) - (Decimal(1) - c_anual) ** (Decimal(1)/Decimal(12))
print(f"  inversa anual->mensual = {(vuelta*100).quantize(Decimal('0.0001'))}%  (debe ~10%)")
```

Salida esperada (resumen): retención mes 5 = 81/200 = 40.50%; el producto de `(1−churn)` reconstruye exactamente cada retención (assert pasa); con `c` estable ≈ 10% la vida media `L ≈ 10 meses`, y la serie geométrica truncada converge al mismo número (segunda vía confirmada); 10% mensual ≈ **71.76% anual** (no 120%, que sería el error de multiplicar).

## Ejemplo trabajado

**Caso GastroLatam (Calculadora de Costos, $10.000 COP).** No hay recompra mensual de un producto de pago único, así que medimos *retención de uso/engagement*: de los que compraron, ¿cuántos siguen usándola y recomiendan? Para un caso de suscripción usamos un SaaS gastronómico ficticio a $30.000 COP/mes.

Cohorte de marzo: **N₀ = 200** suscriptores. Activos: mes1=150, mes2=120, mes3=102, mes4=90, mes5=81.

1. **Retención mes 1** = 150/200 = **75%** (unidad: % de la cohorte).
2. **Churn mes 0→1** = (200−150)/200 = 50/200 = **25%**.
3. **Churn estabilizado** (meses 3→4 y 4→5): (102−90)/102 ≈ 11.76% y (90−81)/90 = 10.00%. Promedio ≈ **10.88% mensual**. (Lo típico: el churn alto al inicio se calma cuando quedan los leales — por eso la curva se aplana.)
4. **Vida media** con c ≈ 0.1088: `L = 1/0.1088 ≈` **9.2 meses**.
5. **Traducción a dinero** (cruce con [[83-cac-ltv-y-payback]]): si el margen por cliente es $30.000/mes, LTV ≈ 9.2 meses × $30.000 = **$276.000 COP** por cliente. Si captarlo cuesta menos que eso, el negocio crece.

Resultado: la cohorte de marzo retiene **40.5% a los 5 meses** y cada cliente dura en promedio **≈ 9.2 meses**, lo que sostiene un LTV de **≈ $276.000 COP**.

## Errores comunes / trampas

- **Multiplicar churn en vez de componerlo.** 10% mensual NO es 120% anual. Es `1−(1−0.10)¹² ≈ 71.76%`. Componer, como el interés.
- **Confundir churn de periodo con churn acumulado.** "Perdí 25% el mes 1 y 20% el mes 2" no es 45% perdido; el 20% se aplica sobre los que *quedaban*, no sobre la cohorte original.
- **Mezclar cohortes (retención agregada).** Promediar toda la base oculta que las cohortes nuevas (que aún no han tenido tiempo de irse) inflan el número. Siempre separa por cohorte.
- **Usar churn temprano (alto) como si fuera constante.** El primer mes siempre fuga más. Para `L = 1/c` usa el churn *estabilizado*, no el del mes 0→1, o sobrestimarás la fuga y subestimarás el LTV.
- **Churn de clientes vs. churn de ingresos (revenue churn).** No son lo mismo: si se van clientes pequeños pero crecen los grandes, el revenue churn puede ser negativo (bueno) aunque el churn de clientes sea positivo. Define cuál mides.
- **`L = 1/c` solo vale con churn aproximadamente constante.** Si la curva no se aplana de forma geométrica, suma la curva real `Σ R(t)` en lugar de la fórmula cerrada.
- **Float para porcentajes que alimentan dinero.** Usa `Fraction`/`Decimal` cuando el número va a multiplicar pesos (ver [[12-fracciones-decimales-y-precision]]).

## Cruces

- [[83-cac-ltv-y-payback]] — la vida media `L` es el insumo directo del LTV.
- [[71-interes-simple-y-compuesto]] — composición de tasas: por qué churn mensual≠anual×12.
- [[19-secuencias-y-series]] — la serie geométrica que da `L = 1/c`.
- [[14-porcentajes-sin-errores]] — retención y churn son porcentajes; evitar el error base.
- [[88-embudos-y-tasas-de-conversion]] — el embudo trae al cliente; la cohorte mide si se queda.

---

**Mini-checklist de exactitud**
1. ¿Separé por cohorte (no promedié toda la base) y `R(0)=100%`?
2. ¿Compuse el churn entre frecuencias (no multipliqué) y usé el churn *estabilizado* para `L=1/c`?
3. ¿Verifiqué `L` por segunda vía (suma de la serie `Σ R(t)`) y mantuve unidades (periodos, %, COP)?
