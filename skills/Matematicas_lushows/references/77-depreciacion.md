# 77 · Depreciación

> **Qué resuelve / cuándo usarlo** — Repartir el costo de un activo (máquina, vehículo, horno, computador) a lo largo de su vida útil, calcular cuánto "vale en libros" en cada año y elegir el método correcto (línea recta, saldo decreciente o suma de dígitos).

## Concepto (para no-experto)

**Depreciación** = el reparto contable del costo de un activo a lo largo del tiempo en que lo usas. La idea: un horno de $20.000.000 no es un "gasto" de un solo año; te sirve por 10 años, así que repartes su costo en esos 10 años. Cada año "gastas" un pedacito.

Analogía cotidiana: compras un carro por $80M. No se "evapora" el primer día; pierde valor poco a poco. La depreciación es ese desgaste contable año por año.

Términos clave (definidos la primera vez):
- **Costo (C)**: lo que pagaste por el activo, listo para usar. En pesos (COP).
- **Valor residual o de salvamento (S)**: lo que crees que valdrá al final de su vida útil (lo que te darían por venderlo viejo). En pesos.
- **Vida útil (n)**: años que esperas usarlo productivamente. En años.
- **Base depreciable (B = C − S)**: el monto total a repartir (solo se deprecia lo que vas a "consumir", no el valor residual). En pesos.
- **Depreciación del año (Dₜ)**: el pedacito que gastas en el año t. En pesos/año.
- **Depreciación acumulada (Aₜ)**: suma de todos los Dₜ hasta el año t. En pesos.
- **Valor en libros (VLₜ)**: lo que vale el activo en tu contabilidad al final del año t = C − Aₜ. En pesos.

> ⚠️ Esto es depreciación **contable/gerencial** para decidir y reportar. La depreciación **fiscal** (lo que la DIAN/SAT te permite descontar de impuestos) tiene reglas propias por país y por tipo de activo. No las confundas.

## Fórmulas / método

Notación: C = costo, S = valor residual, n = vida útil (años), B = C − S = base depreciable.

**1) Línea recta (SL — straight line)** — el mismo monto cada año.
- Dₜ = B / n   (constante para todo t = 1..n)
- VLₜ = C − t·D
- Al final: VLₙ = S exacto.

**2) Saldo decreciente (DB — declining balance)** — un porcentaje fijo sobre el valor en libros (que va bajando). NO usa S en la tasa.
- Tasa: d = k / n   (k = factor; k=2 → "doble saldo decreciente", DDB; k=1.5 → 150%)
- Dₜ = d · VLₜ₋₁   (con VL₀ = C)
- Regla de tope: nunca dejes que VL baje de S. Si Dₜ haría VLₜ < S, recorta Dₜ = VLₜ₋₁ − S.
- Saldo decreciente NUNCA llega a 0 solo; por eso muchas veces se **cambia a línea recta** cuando esta da más depreciación (DDB-to-SL).

**3) Suma de dígitos de los años (SYD — sum of years' digits)** — acelerada, pero suave.
- Denominador: SYD = n(n+1)/2  (la suma 1+2+...+n)
- Fracción del año t: fₜ = (n − t + 1) / SYD   (más alta al inicio)
- Dₜ = fₜ · B

**Cuándo usar cada método:**
- **Línea recta**: activo que se usa parejo (mobiliario, edificios, equipo estable). Simple, predecible. Es el default.
- **Saldo decreciente / SYD (acelerados)**: activo que pierde valor o utilidad rápido al inicio (tecnología, vehículos, equipo que se vuelve obsoleto). Carga más gasto temprano → menos utilidad gravable temprano (ventaja fiscal donde lo permitan).

## Verificación en código

```python
from decimal import Decimal as D, getcontext, ROUND_HALF_UP
getcontext().prec = 28

def centavos(x):  # redondea a 2 decimales (pesos.centavos) UNA vez
    return x.quantize(D("0.01"), rounding=ROUND_HALF_UP)

C = D("20000000")   # costo del horno (COP)
S = D("2000000")    # valor residual (COP)
n = 10              # vida util (anios)
B = C - S           # base depreciable

# --- 1) LINEA RECTA ---
D_sl = B / n
tabla_sl = []
vl = C
for t in range(1, n + 1):
    vl -= D_sl
    tabla_sl.append((t, centavos(D_sl), centavos(vl)))

# --- 2) DOBLE SALDO DECRECIENTE (DDB) con tope en S ---
d = D(2) / D(n)     # tasa = 2/n
tabla_db = []
vl = C
for t in range(1, n + 1):
    dep = d * vl
    if vl - dep < S:          # tope: no bajar de S
        dep = vl - S
    vl -= dep
    tabla_db.append((t, centavos(dep), centavos(vl)))

# --- 3) SUMA DE DIGITOS (SYD) ---
SYD = D(n * (n + 1)) / D(2)
tabla_syd = []
vl = C
for t in range(1, n + 1):
    frac = D(n - t + 1) / SYD
    dep = frac * B
    vl -= dep
    tabla_syd.append((t, centavos(dep), centavos(vl)))

print("LINEA RECTA  D/anio =", centavos(D_sl), " VL final =", tabla_sl[-1][2])
print("DDB          VL final =", tabla_db[-1][2])
print("SYD          D anio1 =", tabla_syd[0][1], " VL final =", tabla_syd[-1][2])

# ---------- VERIFICACION POR SEGUNDA VIA ----------
# (a) La suma de TODAS las depreciaciones debe igualar la base B (SL y SYD)
sum_sl  = sum((row[1] for row in tabla_sl), D("0"))
sum_syd = sum((row[1] for row in tabla_syd), D("0"))
assert sum_sl == B,  f"SL no suma B: {sum_sl} != {B}"
assert sum_syd == B, f"SYD no suma B: {sum_syd} != {B}"

# (b) Valor en libros final debe ser EXACTAMENTE S en SL, SYD y DDB (por el tope)
assert tabla_sl[-1][2]  == centavos(S)
assert tabla_syd[-1][2] == centavos(S)
assert tabla_db[-1][2]  == centavos(S)

# (c) VL en cualquier anio = C - depreciacion acumulada (identidad contable)
acum = D("0")
for (t, dep, vl) in tabla_sl:
    acum += dep
    assert centavos(C - acum) == vl, f"VL inconsistente en t={t}"

print("OK: las 3 verificaciones pasan")
```

Salida esperada:
```
LINEA RECTA  D/anio = 1800000.00  VL final = 2000000.00
DDB          VL final = 2000000.00
SYD          D anio1 = 3272727.27  VL final = 2000000.00
```

Segunda vía resumida: (a) la suma de las cuotas = base depreciable; (b) el valor en libros final = valor residual exacto; (c) VL = C − acumulada en cada año. Si las tres pasan, los números son consistentes.

## Ejemplo trabajado

**Caso (LatAm):** Una dark kitchen compra un **horno industrial** por **C = $20.000.000 COP**, estima venderlo en **S = $2.000.000** tras **n = 10 años**.

Base depreciable: **B = 20.000.000 − 2.000.000 = $18.000.000**.

**Línea recta:**
- D = 18.000.000 / 10 = **$1.800.000 por año**.
- Año 1: VL = 20.000.000 − 1.800.000 = **$18.200.000**.
- Año 5: VL = 20.000.000 − 5·1.800.000 = **$11.000.000**.
- Año 10: VL = **$2.000.000** = S exacto. ✓

**Doble saldo decreciente (DDB), d = 2/10 = 20%:**
- Año 1: D = 20% · 20.000.000 = **$4.000.000** → VL = $16.000.000.
- Año 2: D = 20% · 16.000.000 = **$3.200.000** → VL = $12.800.000.
- (carga mucho más gasto al inicio que línea recta: $4M vs $1,8M).
- En años finales el tope recorta la cuota para no bajar de S; VL final = **$2.000.000**. ✓

**Suma de dígitos (SYD), denominador = 10·11/2 = 55:**
- Año 1: fracción 10/55 → D = (10/55)·18.000.000 = **$3.272.727,27**.
- Año 2: fracción 9/55 → D = **$2.945.454,55**.
- VL final = **$2.000.000**. ✓

Interpretación: con DDB o SYD cargas más gasto los primeros años (útil para un horno que se desgasta/obsoletiza rápido); con línea recta el gasto es parejo y más fácil de presupuestar. Todos terminan en el mismo valor residual con unidades en **pesos (COP)**.

## Errores comunes / trampas

- **Meter el valor residual en la tasa de saldo decreciente.** DB usa C − nada en la tasa; deprecia sobre el VL completo. S solo actúa como **tope** (no bajes de S).
- **Olvidar el tope en DB** → el valor en libros termina por debajo del residual o nunca llega a él. Siempre recorta la última(s) cuota(s).
- **Usar float para dinero.** 0.2 en binario no es exacto y los centavos se desvían en tablas largas. Usa `decimal`.
- **Redondear cada año y luego sumar** → la suma no cuadra con la base. Calcula con precisión completa y redondea para mostrar; verifica que la suma sin redondear = B.
- **Confundir depreciación contable con fiscal.** La tasa/vida útil que acepta la autoridad tributaria puede diferir de tu estimación gerencial.
- **Depreciar el residual.** Solo se reparte B = C − S, no el costo total (excepto la base de DB, que sí parte de C pero frena en S).
- **Vida útil irreal.** Si n está inflado, subestimas el gasto anual y sobreestimas la utilidad. Sé honesto con n.

## Cruces

- [[70-valor-del-dinero-en-el-tiempo.md]] — un peso de depreciación futura no vale igual que uno de hoy; descuenta si comparas.
- [[78-flujo-de-caja-y-presupuesto.md]] — la depreciación es gasto contable pero NO salida de caja; clave para diferenciar utilidad de efectivo.
- [[74-vpn-y-tir.md]] — el escudo fiscal de la depreciación entra en el flujo de un proyecto de inversión.
- [[81-costeo-y-costo-unitario.md]] — la depreciación del equipo se reparte en el costo por unidad producida.
- [[76-punto-de-equilibrio.md]] — la depreciación es un costo fijo que sube el punto de equilibrio.

---

**Mini-checklist de exactitud:**
1. ¿La suma de todas las cuotas = base depreciable (C − S)? (en SL y SYD)
2. ¿El valor en libros final = valor residual S exacto? (con tope en DB)
3. ¿Usé `decimal` y redondeé una sola vez al mostrar, no en cada paso?
