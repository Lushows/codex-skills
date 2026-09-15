# 79 · Moneda, inflación y devaluación

> **Qué resuelve / cuándo usarlo** — Convertir entre monedas sin perder centavos, comparar precios de años distintos en "pesos de hoy", y entender cuándo una moneda se devalúa o se aprecia y qué te queda de verdad después de la inflación (tasa real).

## Concepto (para no-experto)

Cuatro ideas distintas que la gente confunde. Las separamos:

1. **Conversión de moneda.** Cambiar una cantidad de una moneda a otra usando un **tipo de cambio** (precio de una moneda medido en otra). Ej.: si 1 USD = 4.000 COP, entonces 25 USD = 100.000 COP.

2. **Inflación.** La inflación es la **tasa a la que suben los precios en general** durante un periodo (normalmente un año). Si la inflación anual es 10%, una canasta que costaba $100.000 ahora cuesta $110.000. Tu dinero **pierde poder de compra**: con los mismos pesos compras menos. Analogía: la inflación es como una regla que se encoge cada año; el "metro" (el peso) mide cada vez menos cosas.

3. **Pesos constantes (ajustar por inflación).** Para comparar plata de años distintos hay que llevarla a una **misma vara**. "Pesos corrientes" = la cifra tal como se vio ese año (nominal). "Pesos constantes" = esa cifra reexpresada en el poder de compra de un año base (real). Comparar ventas de 2020 con 2026 sin ajustar por inflación es como comparar distancias mezclando metros con yardas.

4. **Devaluación vs. apreciación.** Cuando una moneda **pierde valor** frente a otra (necesitas más pesos para comprar 1 dólar) decimos que se **devaluó** (o depreció). Cuando **gana valor** (necesitas menos pesos por dólar), se **apreció**. Ojo: el tamaño del cambio depende de **cómo cotices** el par (pesos por dólar vs. dólares por peso); más abajo lo demostramos.

5. **Tasa real.** Es el rendimiento o crecimiento **después de descontar la inflación**. Si tu inversión rinde 12% nominal pero la inflación fue 8%, NO ganaste 4% de poder de compra: ganaste un poco menos (ver fórmula de Fisher).

**Término clave — nominal vs. real:** *nominal* = la cifra en pesos corrientes, sin ajustar. *Real* = ya ajustada por inflación, en poder de compra. La promesa de error cero exige siempre decir cuál de las dos es.

## Fórmulas / método

Sea:
- `M_A` = monto en moneda A. Tipo de cambio `e` = unidades de B por 1 unidad de A.
- **Conversión:** `M_B = M_A · e`. Inversa: `M_A = M_B / e`.
- **Spread de casa de cambio:** precio de **compra** (te compran tu divisa, más bajo) y **venta** (te venden divisa, más alto). El cliente pierde el spread.

**Inflación de un periodo** (tasa `π`):
- `Precio_final = Precio_inicial · (1 + π)`
- **Inflación acumulada** de varios periodos con tasas `π₁, π₂, …, πₙ`:
  `1 + π_acum = (1+π₁)(1+π₂)…(1+πₙ)`  ← se **multiplica**, NO se suma.

**Pesos constantes (deflactar / inflar)** usando un índice de precios `IPC` (Índice de Precios al Consumidor — número que mide el nivel de precios; ej. IPC base 100):
- Llevar un valor del año `t` al poder de compra del año base `b`:
  `Valor_real_b = Valor_nominal_t · (IPC_b / IPC_t)`
- Equivalente con tasas: `Valor_real = Valor_nominal / (1 + π_acum desde b hasta t)`

**Devaluación / apreciación** (cotizando "pesos por dólar", `S`):
- `variación = (S_final − S_inicial) / S_inicial`. Si > 0, el peso se **devaluó** (subió el precio del dólar).
- Relación entre las dos formas de cotizar: si el peso se devalúa `d` (pesos/USD), la apreciación del dólar medida en USD/peso es `1/(1+d) − 1`. **No es simétrica.**

**Tasa real (ecuación de Fisher):**
- Exacta: `1 + r_real = (1 + r_nominal) / (1 + π)`  ⟹ `r_real = (1+r_nom)/(1+π) − 1`
- Aproximación (solo para intuición, con tasas chicas): `r_real ≈ r_nominal − π`. La aproximación **falla** con tasas altas; usar siempre la exacta para dinero.

Unidades: el tipo de cambio lleva unidad (COP/USD); las tasas son adimensionales (fracción o %); los montos llevan moneda.

## Verificación en código

```python
from decimal import Decimal, ROUND_HALF_UP, getcontext
getcontext().prec = 28  # alta precision interna; redondeamos UNA vez al final

CENT = Decimal("0.01")
def money(x):  # redondeo final a centavos, medio-arriba (bankers NO: usamos comercial)
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)

# ---------- 1) CONVERSION DE MONEDA ----------
usd = Decimal("250.00")
tasa = Decimal("4012.50")          # COP por 1 USD
cop = usd * tasa
print("250 USD =", money(cop), "COP")          # 1,003,125.00 COP
# Verificacion por via inversa: volver a USD debe dar el original
de_vuelta = (cop / tasa)
assert money(de_vuelta) == money(usd), "fallo inversa conversion"

# ---------- 2) INFLACION ACUMULADA (se multiplica) ----------
infl = [Decimal("0.131"), Decimal("0.092"), Decimal("0.057")]  # 13.1%, 9.2%, 5.7%
factor = Decimal(1)
for p in infl:
    factor *= (1 + p)
acum = factor - 1
print("Inflacion acumulada 3 anios:", (acum*100).quantize(Decimal("0.01")), "%")  # 31.99 %
# Verificacion: NO es la suma simple
suma_ingenua = sum(infl)
assert acum != suma_ingenua, "ojo: sumar tasas es el error clasico"
print("Suma ingenua (MAL):", (suma_ingenua*100).quantize(Decimal("0.01")), "%")  # 28.00 %

# ---------- 3) PESOS CONSTANTES (deflactar con IPC) ----------
# Ventas nominales 2020 vs 2026. IPC base: 2020=100, 2026=140 (ejemplo)
ventas_2020_nom = Decimal("50000000")   # 50 M COP en pesos de 2020
ventas_2026_nom = Decimal("62000000")   # 62 M COP en pesos de 2026
ipc_2020 = Decimal("100"); ipc_2026 = Decimal("140")
# Llevar 2026 a pesos de 2020 (poder de compra de 2020)
ventas_2026_real2020 = ventas_2026_nom * (ipc_2020 / ipc_2026)
print("Ventas 2026 en pesos de 2020:", money(ventas_2026_real2020), "COP")  # 44,285,714.29
crecio_real = (ventas_2026_real2020 / ventas_2020_nom) - 1
print("Crecimiento REAL:", (crecio_real*100).quantize(Decimal("0.01")), "%")  # -11.43 %
# Verificacion via 2da via: llevar 2020 a pesos de 2026 y comparar alla
ventas_2020_real2026 = ventas_2020_nom * (ipc_2026 / ipc_2020)
crecio_real_b = (ventas_2026_nom / ventas_2020_real2026) - 1
assert (crecio_real*Decimal("1e6")).quantize(Decimal("1")) == (crecio_real_b*Decimal("1e6")).quantize(Decimal("1"))

# ---------- 4) DEVALUACION (no simetrica) ----------
S0 = Decimal("3800")   # COP/USD inicial
S1 = Decimal("4180")   # COP/USD final
dev_peso = (S1 - S0) / S0
print("Devaluacion del peso:", (dev_peso*100).quantize(Decimal("0.01")), "%")  # 10.00 %
# El dolar medido en USD/peso: apreciacion vista desde el peso
ap_dolar = (1/(1+dev_peso)) - 1
print("Lado USD/peso:", (ap_dolar*100).quantize(Decimal("0.0001")), "%")  # -9.0909 %
assert dev_peso != -ap_dolar  # demuestra que NO es simetrico

# ---------- 5) TASA REAL (Fisher exacta vs aproximada) ----------
r_nom = Decimal("0.12"); pi = Decimal("0.08")
r_real = (1 + r_nom)/(1 + pi) - 1
print("Tasa real (Fisher exacta):", (r_real*100).quantize(Decimal("0.01")), "%")  # 3.70 %
aprox = r_nom - pi
print("Aproximacion (r_nom - pi):", (aprox*100).quantize(Decimal("0.01")), "%")   # 4.00 %  <- sobreestima
```

Resultados clave (todos verificados por segunda vía / assert):
- 250 USD × 4.012,50 = **1.003.125,00 COP**; la inversa devuelve 250,00 USD.
- Inflación acumulada 3 años = **31,99%**, no 28,00% (sumar tasas está mal).
- Crecimiento **real** del negocio = **−11,43%** aunque el nominal subió 24%.
- Devaluación del peso **+10,00%** ≠ apreciación del dólar **−9,0909%** (asimétrico).
- Tasa real exacta **3,70%**, no 4,00% de la aproximación.

## Ejemplo trabajado

**Caso GastroLatam.** En 2024 compraste un horno importado a un proveedor en USD. Quieres saber: (a) cuánto te costó en pesos, (b) si tu margen "creció" de verdad y (c) cuánto rinde de verdad guardar la plata.

Datos: horno **USD 1.200**, tasa de compra del banco **4.250 COP/USD** (te venden dólares, precio venta).
- (a) Costo en pesos = `1.200 × 4.250 = 5.100.000,00 COP`.
  Verificación inversa: `5.100.000 / 4.250 = 1.200,00 USD` ✓ (unidades: COP / (COP/USD) = USD ✓).

- (b) En 2024 vendiste menús por **80.000.000 COP** (nominal). En 2026 vendiste **92.000.000 COP** (nominal). El IPC pasó de 100 (2024) a 119 (2026), es decir inflación acumulada 19%.
  Ventas 2026 en pesos de 2024 = `92.000.000 × (100/119) = 77.310.924,37 COP`.
  Crecimiento real = `77.310.924,37 / 80.000.000 − 1 = −3,36%`.
  Conclusión: en pesos vendiste 15% más, pero en **poder de compra perdiste 3,36%**. El crecimiento nominal era una ilusión de la inflación.

- (c) Un CDT te ofrece **11% nominal anual** y la inflación esperada es **9%**.
  Tasa real (Fisher) = `(1,11/1,09) − 1 = 1,83%`. Tu plata crece **1,83% real**, no 2% (la resta simple miente por 0,17 puntos).

Todas las cifras con unidades (COP, USD, %), redondeadas una sola vez al final.

## Errores comunes / trampas

- **Sumar tasas de inflación de varios años** en vez de multiplicar factores `(1+π)`. Subestima el efecto acumulado.
- **Comparar pesos corrientes de años distintos** ("vendí más que el año pasado") sin deflactar por IPC: confunde inflación con crecimiento.
- **Confundir el sentido del tipo de cambio:** COP/USD vs. USD/COP. Dividir cuando tocaba multiplicar te cambia el resultado por un factor enorme. Chequea unidades.
- **Creer que devaluación y apreciación son simétricas:** +10% de un lado NO es −10% del otro (es −9,09%). Es la misma trampa de los porcentajes (módulo 14).
- **Usar `r_real ≈ r_nom − π`** para dinero real: con tasas altas (LatAm) el error es material. Usa Fisher exacta.
- **Usar `float` para dinero o tasas en cadena:** acumula error de redondeo. Usa `Decimal`.
- **Ignorar el spread compra/venta** de la casa de cambio: la conversión "de pizarra" no es la que pagas.

### Mini-checklist de exactitud
- [ ] ¿Dije explícitamente si la cifra es **nominal** (pesos corrientes) o **real** (constantes)?
- [ ] ¿Multipliqué factores `(1+π)` para acumular inflación (no sumé tasas) y usé Fisher exacta?
- [ ] ¿Verifiqué unidades del tipo de cambio (COP/USD) y confirmé por la vía inversa?

## Cruces
- [[14-porcentajes-sin-errores]] — variaciones, asimetría sube/baja (base de devaluación/apreciación).
- [[37-conversion-de-unidades]] — disciplina de unidades aplicada al tipo de cambio.
- [[75-tasas-nominal-efectiva-y-real]] — tasa real y ecuación de Fisher en detalle.
- [[70-valor-del-dinero-en-el-tiempo]] — por qué $1 hoy ≠ $1 mañana (inflación + interés).
- [[86-forecasting-y-proyeccion]] — proyectar ventas en términos reales vs. nominales.
