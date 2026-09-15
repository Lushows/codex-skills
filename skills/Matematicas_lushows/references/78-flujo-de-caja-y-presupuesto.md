# 78 · Flujo de caja y presupuesto

> **Qué resuelve / cuándo usarlo** — Para construir, proyectar y auditar el **flujo de caja** (cuánta plata entra y sale mes a mes) y armar un **presupuesto** con saldos acumulados, separando la caja real del "papel" de la utilidad contable.

## Concepto (para no-experto)

**Flujo de caja (cash flow)** = el dinero *que de verdad entra y sale* de tu cuenta en un periodo. No es lo mismo que la *utilidad* (ganancia contable): puedes "ganar" una venta hoy y recibir la plata dentro de 60 días. La caja es lo que tienes en la mano; sin caja, un negocio rentable también quiebra.

Términos, definidos la primera vez que aparecen:

- **Entradas (inflows):** dinero que llega — cobros de ventas, aportes de socios, préstamos recibidos.
- **Salidas (outflows):** dinero que se va — pago a proveedores, nómina, arriendo, impuestos, compra de equipos.
- **Flujo neto del periodo:** Entradas − Salidas en ese mes. Puede ser **positivo** (sobró caja) o **negativo** (faltó).
- **Saldo acumulado (saldo de caja):** lo que llevas en el banco. Es como una cuenta de ahorros: el saldo de hoy = el saldo de ayer + lo que entró − lo que salió.
- **Flujo de caja libre (Free Cash Flow, FCF):** la caja que queda *después* de cubrir la operación y las inversiones necesarias para mantener el negocio (compra de equipos = **CapEx**). Es la plata realmente "libre" para pagar deuda, repartir utilidades o reinvertir.
- **Presupuesto:** el plan de entradas y salidas a futuro. Es el "mapa" contra el que luego comparas la realidad.

**Analogía:** tu flujo de caja es como tu cuenta bancaria personal. La utilidad es lo que *deberías* tener según tu sueldo; la caja es lo que el cajero te deja sacar hoy. Si te pagan el día 30 pero el arriendo vence el día 5, puedes tener buen sueldo y aun así no alcanzar a pagar: eso es un problema de **caja**, no de rentabilidad.

## Fórmulas / método

Para cada periodo *t* (mes 1, 2, 3, …):

```
Flujo neto_t      = Entradas_t − Salidas_t
Saldo acumulado_t = Saldo acumulado_(t−1) + Flujo neto_t
Saldo acumulado_0 = Caja inicial
```

Flujo de caja libre (versión simple para una pyme):

```
FCF_t = Flujo de caja operativo_t − CapEx_t
```

donde **Flujo de caja operativo** = caja generada solo por la operación (cobros − pagos operativos), y **CapEx** = inversión en activos (máquinas, equipos, remodelación).

Versión contable del flujo operativo (método indirecto), partiendo de la utilidad:

```
Flujo operativo = Utilidad neta + Depreciación − ΔWC
```

- **Depreciación:** gasto contable que NO sale de caja (ver [[77-depreciacion]]); por eso se suma de vuelta.
- **ΔWC (cambio en capital de trabajo):** plata "atrapada" en cuentas por cobrar e inventario menos lo que financian los proveedores. Si crece, *resta* caja.

**Unidades:** todo en la misma moneda (ej. COP) y la misma periodicidad (mensual). Nunca mezcles meses con años sin convertir.

**Regla de oro de exactitud:** el dinero se maneja con `decimal` o en **centavos enteros**, nunca con `float` (los flotantes dan errores como 0.1 + 0.2 = 0.30000000000000004 — ver [[12-fracciones-decimales-y-precision]]).

## Verificación en código

```python
from decimal import Decimal, getcontext, ROUND_HALF_UP

getcontext().prec = 28  # alta precisión interna

def D(x):  # helper: todo string -> Decimal (nunca float -> Decimal)
    return Decimal(str(x))

def peso(x):  # redondear UNA sola vez, al final, a peso entero (COP no usa centavos)
    return x.quantize(Decimal("1"), rounding=ROUND_HALF_UP)

# --- Datos: presupuesto mensual de un café (COP) ---
caja_inicial = D("2_000_000".replace("_", ""))  # = 2.000.000

# (entradas, salidas) por mes, 6 meses
movimientos = [
    (D("8000000"),  D("9500000")),   # mes 1: arranque, compra de equipo
    (D("9500000"),  D("8200000")),   # mes 2
    (D("11000000"), D("8800000")),   # mes 3
    (D("10500000"), D("9000000")),   # mes 4
    (D("12000000"), D("9300000")),   # mes 5
    (D("13500000"), D("9600000")),   # mes 6
]

saldo = caja_inicial
filas = []
total_in = D("0")
total_out = D("0")
for i, (ent, sal) in enumerate(movimientos, start=1):
    flujo_neto = ent - sal
    saldo = saldo + flujo_neto          # saldo acumulado_t
    total_in += ent
    total_out += sal
    filas.append((i, ent, sal, flujo_neto, saldo))

print("Mes | Entradas   | Salidas    | Flujo neto | Saldo acum.")
for m, ent, sal, fn, ac in filas:
    print(f" {m}  | {peso(ent):>10} | {peso(sal):>10} | {peso(fn):>10} | {peso(ac):>11}")

saldo_final = saldo
print("\nSaldo final:", peso(saldo_final))

# --- VERIFICACIÓN POR SEGUNDA VÍA ---
# Vía 1 (arriba): iterando mes a mes.
# Vía 2: identidad global  saldo_final = caja_inicial + ΣEntradas − ΣSalidas
saldo_final_2 = caja_inicial + total_in - total_out
assert saldo_final == saldo_final_2, "Las dos vías NO coinciden -> hay un error"
print("Verificación OK (dos vías coinciden):", peso(saldo_final_2))

# --- Flujo de caja libre del mes 1 (operativo − CapEx) ---
# El mes 1 incluyó compra de equipo (CapEx) de 3.000.000 dentro de 'salidas'.
capex_mes1 = D("3000000")
flujo_operativo_mes1 = movimientos[0][0] - (movimientos[0][1] - capex_mes1)
fcf_mes1 = flujo_operativo_mes1 - capex_mes1
print("FCF mes 1:", peso(fcf_mes1))
# Chequeo: FCF = entradas - salidas_totales (porque CapEx ya estaba en salidas)
assert fcf_mes1 == movimientos[0][0] - movimientos[0][1]
```

Salida esperada (resumen): saldo final **= 2.000.000 + 64.500.000 − 54.400.000 = 12.100.000 COP**, confirmado por ambas vías; FCF mes 1 = **−1.500.000 COP**.

**Segunda vía adicional (sanity check de orden de magnitud):** 6 meses con ~+1,7 M de flujo neto promedio sobre 2 M iniciales → del orden de 12 M. Coincide con la magnitud (ver [[06-estimacion-y-sanity-checks]]).

## Ejemplo trabajado

Café "La Esquina", presupuesto a 6 meses, caja inicial **2.000.000 COP**.

1. **Flujo neto por mes** (Entradas − Salidas):
   - Mes 1: 8.000.000 − 9.500.000 = **−1.500.000 COP**
   - Mes 2: 9.500.000 − 8.200.000 = **+1.300.000 COP**
   - Mes 3: 11.000.000 − 8.800.000 = **+2.200.000 COP**
   - Mes 4: 10.500.000 − 9.000.000 = **+1.500.000 COP**
   - Mes 5: 12.000.000 − 9.300.000 = **+2.700.000 COP**
   - Mes 6: 13.500.000 − 9.600.000 = **+3.900.000 COP**

2. **Saldo acumulado** (arranca en 2.000.000):
   - Fin mes 1: 2.000.000 − 1.500.000 = **500.000 COP** ← punto más bajo, casi se queda sin caja.
   - Fin mes 2: 500.000 + 1.300.000 = **1.800.000 COP**
   - Fin mes 3: 1.800.000 + 2.200.000 = **4.000.000 COP**
   - Fin mes 4: 4.000.000 + 1.500.000 = **5.500.000 COP**
   - Fin mes 5: 5.500.000 + 2.700.000 = **8.200.000 COP**
   - Fin mes 6: 8.200.000 + 3.900.000 = **12.100.000 COP**

3. **Lectura de negocio:** el negocio nunca queda en saldo negativo, pero el **mes 1 lo deja en 500.000 COP**, un colchón peligrosamente fino. Recomendación: tener una **reserva de caja** (≈ 1 mes de salidas, ~9 M) o aplazar parte del CapEx del mes 1.

4. **FCF mes 1** = operativo − CapEx = (8.000.000 − 6.500.000) − 3.000.000 = **−1.500.000 COP**. El negocio "quemó" caja el primer mes por la inversión inicial; algo normal al arrancar.

Resultado final verificado: **saldo de caja al mes 6 = 12.100.000 COP**.

## Errores comunes / trampas

- **Confundir utilidad con caja.** Vender a crédito suma utilidad pero NO suma caja hasta que cobras. Un negocio "rentable" puede quebrar por falta de caja.
- **Olvidar el desfase de cobros/pagos.** Si cobras a 60 días y pagas a 30, hay un hueco que la caja debe aguantar (capital de trabajo).
- **Meter CapEx como gasto operativo (o no meterlo).** La compra de un horno es salida de caja real en su mes, aunque contablemente se deprecie en años. No la dupliques: o cuentas la salida de caja completa, o la depreciación contable, según el método — nunca ambas.
- **Sumar depreciación a la caja sin restarla del flujo operativo** cuando usas el método indirecto. La depreciación se suma porque no salió caja; no la trates como una entrada.
- **Float para dinero.** 0.1 + 0.2 ≠ 0.3 en float. Usa `decimal` o centavos enteros.
- **Redondear cada mes.** Redondea una sola vez al final; redondear acumulando arrastra centavos perdidos (ver [[05-cifras-significativas-y-redondeo]]).
- **No proyectar el escenario malo.** Un presupuesto con solo el caso optimista esconde el mes en que te quedas sin caja. Modela también pesimista (ver [[93-analisis-de-sensibilidad-y-escenarios]]).

## Cruces

- [[77-depreciacion]] — por qué la depreciación se suma de vuelta al flujo operativo (no sale caja).
- [[80-margenes-bruto-contribucion-neto]] — la utilidad de la que parte el flujo operativo.
- [[74-vpn-y-tir]] — descontar estos flujos de caja a valor presente para decidir inversiones.
- [[86-forecasting-y-proyeccion]] — proyectar entradas y salidas futuras del presupuesto.
- [[93-analisis-de-sensibilidad-y-escenarios]] — presupuestar el caso base, optimista y pesimista.

---

**Mini-checklist de exactitud**
- [ ] ¿Dinero en `decimal`/centavos (no float) y redondeo UNA vez al final?
- [ ] ¿Saldo final verificado por dos vías (iterativa y `caja_inicial + ΣEnt − ΣSal`)?
- [ ] ¿Revisé el mes de saldo MÍNIMO, no solo el final, para no quedar sin caja?
