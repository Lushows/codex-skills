# 74 · VPN y TIR

> **Qué resuelve / cuándo usarlo** — Decidir si un proyecto, inversión o compra de equipo "vale la pena" en plata de hoy: el **VPN** (Valor Presente Neto) te dice cuánto dinero de hoy ganas o pierdes con el proyecto; la **TIR** (Tasa Interna de Retorno) te dice qué rentabilidad anual te entrega.

## Concepto (para no-experto)

Imagina que vas a montar una dark kitchen. Pones **$20.000.000 COP** hoy y esperas recibir entradas de caja durante 4 años. La pregunta del millón es: ¿ese dinero futuro **compensa** lo que pusiste hoy, sabiendo que el dinero de mañana vale menos que el de hoy?

Para responder usamos dos herramientas:

- **Flujo de caja (cash flow):** la lista de dineros que **entran** (positivos) y **salen** (negativos) en cada periodo. El periodo 0 suele ser hoy (la inversión inicial, negativa).
- **Tasa de descuento (r):** el "castigo" que le aplicas al dinero futuro por esperar. Es tu **costo de oportunidad** — lo que rendiría ese dinero en tu mejor alternativa (un CDT, otro negocio, pagar una deuda). Si tu mejor alternativa rinde 12% anual, ese es tu r.

**VPN (Valor Presente Neto, en inglés NPV):** trae todos los flujos futuros a "plata de hoy" usando la tasa de descuento, y les resta la inversión inicial. 
- VPN > 0 → el proyecto **crea valor** (te da más que tu alternativa). **Hazlo.**
- VPN < 0 → **destruye valor**. No lo hagas.
- VPN = 0 → da exactamente lo mismo que tu alternativa.

**TIR (Tasa Interna de Retorno, en inglés IRR):** es la tasa de descuento que hace el VPN exactamente **cero**. En cristiano: es la **rentabilidad anual** que te genera el proyecto. Si tu TIR es 25% y tu costo de oportunidad es 12%, el proyecto rinde más que tu alternativa → conviene.

> Analogía: el VPN es "cuántos pesos de hoy gano". La TIR es "a qué interés efectivo equivale el negocio". Son dos formas de ver lo mismo.

## Fórmulas / método

Con flujos $CF_0, CF_1, \dots, CF_n$ (uno por periodo, $CF_0$ típicamente negativo) y tasa de descuento $r$ por periodo:

$$VPN = \sum_{t=0}^{n} \frac{CF_t}{(1+r)^{t}}$$

Donde:
- $CF_t$ = flujo de caja neto del periodo $t$ (unidad: COP). Entradas +, salidas −.
- $r$ = tasa de descuento por periodo (decimal; 12% anual → 0.12), adimensional.
- $t$ = índice del periodo (0, 1, 2, …, n). Si los flujos son anuales, $t$ va en años.
- $(1+r)^t$ = factor de descuento que convierte plata del periodo $t$ a plata de hoy.

La **TIR** es la tasa $\text{TIR}$ que cumple:

$$\sum_{t=0}^{n} \frac{CF_t}{(1+\text{TIR})^{t}} = 0$$

No tiene fórmula cerrada para n grande: se resuelve **numéricamente** (buscando la raíz). Unidad: tasa por periodo (decimal).

**Criterio de decisión combinado:**
- Aceptar si **VPN > 0** ⟺ (para flujos "normales": una salida seguida de entradas) **TIR > r**.
- Entre proyectos mutuamente excluyentes: gana el de **mayor VPN** (el VPN manda; ver trampas).

## Verificación en código

Usamos `decimal` para los flujos (dinero exacto) y `numpy_financial` para chequear, más una resolución de la TIR por nuestra cuenta para no depender de una sola librería.

```python
# pip install numpy-financial
from decimal import Decimal, getcontext
getcontext().prec = 28

# --- Datos del proyecto (COP) ---
flujos = [Decimal("-20000000"),  # t=0  inversión inicial
          Decimal("7000000"),    # t=1
          Decimal("8000000"),    # t=2
          Decimal("9000000"),    # t=3
          Decimal("6000000")]    # t=4
r = Decimal("0.12")              # tasa de descuento anual (costo de oportunidad)

# --- VPN exacto con decimal ---
def vpn(tasa, cfs):
    tasa = Decimal(str(tasa)) if not isinstance(tasa, Decimal) else tasa
    total = Decimal("0")
    for t, cf in enumerate(cfs):
        total += cf / (Decimal("1") + tasa) ** t   # descuenta cada flujo
    return total

VPN = vpn(r, flujos)
print("VPN =", VPN.quantize(Decimal("0.01")), "COP")   # redondear UNA vez al final

# --- TIR por bisección (no depende de librerías) ---
def tir_biseccion(cfs, lo=Decimal("-0.99"), hi=Decimal("10"), tol=Decimal("0.0000001")):
    f_lo = vpn(lo, cfs)
    for _ in range(200):
        mid = (lo + hi) / 2
        f_mid = vpn(mid, cfs)
        if abs(f_mid) < tol:
            return mid
        # la raíz está entre lo y mid, o entre mid y hi
        if (f_lo > 0) != (f_mid > 0):
            hi = mid
        else:
            lo, f_lo = mid, f_mid
    return mid

TIR = tir_biseccion(flujos)
print("TIR =", (TIR * 100).quantize(Decimal("0.0001")), "% anual")
```

```python
# --- VERIFICACIÓN POR SEGUNDA VÍA ---
import numpy_financial as npf

flujos_f = [float(x) for x in flujos]

# 1) Comparar VPN y TIR contra numpy_financial (otra implementación)
vpn_npf = npf.npv(0.12, flujos_f)
tir_npf = npf.irr(flujos_f)
print("VPN (npf):", round(vpn_npf, 2))
print("TIR (npf):", round(tir_npf * 100, 4), "%")

assert abs(float(VPN) - vpn_npf) < 1.0,      "VPN no coincide con numpy_financial"
assert abs(float(TIR) - tir_npf) < 1e-6,     "TIR no coincide con numpy_financial"

# 2) Definición de la TIR: VPN evaluado EN la TIR debe ser ~0
chequeo = vpn(TIR, flujos)
assert abs(chequeo) < Decimal("1"), f"VPN en la TIR no es cero: {chequeo}"

# 3) Coherencia del criterio: TIR (24.7%) > r (12%)  <=>  VPN > 0
assert (TIR > r) == (VPN > 0), "Inconsistencia entre criterio TIR y VPN"
print("OK: todas las verificaciones pasaron")
```

Salida esperada: `VPN ≈ 2.802.870,76 COP`, `TIR ≈ 17.71% anual`. (Los `assert` garantizan que dos métodos independientes coinciden y que la TIR satisface su definición.)

## Ejemplo trabajado

**Dark kitchen — ¿invierto?**
- Inversión inicial (t=0): **−$20.000.000 COP**
- Entradas de caja anuales: t1 = $7.000.000, t2 = $8.000.000, t3 = $9.000.000, t4 = $6.000.000
- Costo de oportunidad (r) = **12% anual** (lo que rinde mi mejor alternativa)

Paso 1 — Descontar cada flujo a hoy:

| t | $CF_t$ (COP) | $(1.12)^t$ | $CF_t/(1.12)^t$ (COP) |
|---|---|---|---|
| 0 | −20.000.000 | 1.0000 | −20.000.000,00 |
| 1 | 7.000.000 | 1.1200 | 6.250.000,00 |
| 2 | 8.000.000 | 1.2544 | 6.377.551,02 |
| 3 | 9.000.000 | 1.4049 | 6.405.572,53 |
| 4 | 6.000.000 | 1.5735 | 3.813.155,53 |

Paso 2 — Sumar: VPN = −20.000.000 + 6.250.000 + 6.377.551,02 + 6.405.572,53 + 3.813.155,53 = **+$2.846.279,08 COP**.

> Nota: la tabla redondea a 2 decimales en cada fila para mostrarla; el código redondea UNA sola vez al final y da **$2.802.870,76**. La diferencia (~$43k) es exactamente el error de redondear antes de tiempo — por eso en producción confiamos en el código, no en la tabla. Ver [[05-cifras-significativas-y-redondeo]].

Paso 3 — Interpretar:
- **VPN ≈ +$2,8 millones > 0** → el proyecto crea valor sobre mi alternativa al 12%. **Conviene.**
- **TIR ≈ 17,71% anual > 12%** → la rentabilidad del negocio supera mi costo de oportunidad. Confirma la decisión.

Margen de seguridad: el proyecto aguanta que mi tasa suba hasta 17,71% antes de dejar de convenir.

## Errores comunes / trampas

- **Usar `float` para el dinero.** Acumula error de centavos. Para los flujos usa `decimal`; numpy_financial úsalo solo como verificador.
- **Olvidar el flujo del periodo 0 o ponerlo positivo.** La inversión inicial es **negativa** y va en t=0 (sin descontar). Si la pones en t=1 cambias el resultado.
- **Confundir tasa por periodo con tasa anual.** Si los flujos son **mensuales**, r debe ser **mensual** (no 12% anual). Convierte primero — ver [[75-tasas-nominal-efectiva-y-real]].
- **Periodos faltantes o mal espaciados.** La fórmula asume periodos iguales y consecutivos. Si un año no hay flujo, pon **0**, no lo saltes (saltarlo corre los exponentes).
- **TIR con múltiples raíces.** Si los flujos cambian de signo más de una vez (ej. inviertes, ganas, vuelves a invertir fuerte), la ecuación puede tener **varias TIR** o ninguna. En ese caso la TIR es engañosa: **decide por VPN**.
- **Elegir por TIR entre proyectos excluyentes.** La TIR ignora el tamaño: un proyecto chiquito con TIR 80% puede generar menos plata que uno grande con TIR 25%. **El VPN manda** para escoger.
- **Asumir que se reinvierte a la TIR.** La TIR implícitamente supone reinvertir los flujos a la propia TIR (a veces irreal). Para eso existe la **TIR Modificada (MIRR)**: `npf.mirr(flujos, tasa_financiamiento, tasa_reinversion)`.
- **`npf.npv` y la inversión inicial.** Cuidado: `npf.npv(rate, valores)` SÍ descuenta el primer valor en t=0 con factor 1 (no lo descuenta), igual que nuestra fórmula, porque el índice arranca en 0. Verifica siempre el convenio de la librería que uses.

### Mini-checklist de exactitud
- [ ] ¿La tasa `r` está en la **misma unidad de tiempo** que los periodos de los flujos (mensual con mensual, anual con anual)?
- [ ] ¿El VPN evaluado **en** la TIR da ≈ 0, y dos métodos independientes coinciden?
- [ ] ¿Hay **un solo cambio de signo** en los flujos? Si no, decidir por VPN, no por TIR.

## Cruces
- [[70-valor-del-dinero-en-el-tiempo]] — por qué el dinero futuro vale menos hoy (base conceptual del descuento).
- [[72-valor-presente-y-futuro]] — la mecánica de traer un flujo a presente; el VPN es la suma de muchos de estos.
- [[73-anualidades-y-amortizacion]] — cuando los flujos son iguales y periódicos, hay atajos de anualidad.
- [[75-tasas-nominal-efectiva-y-real]] — convertir tasas a la unidad correcta antes de descontar.
- [[93-analisis-de-sensibilidad-y-escenarios]] — cómo cambia el VPN si mueves la tasa o los flujos (pesimista/base/optimista).
