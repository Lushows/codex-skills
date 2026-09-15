# Velocidad de rotación de caja

> Con capital chico, **la caja pesa más que el margen**. Un negocio con 12% de utilidad que rota
> cada 3 días aplasta a uno con 30% que rota cada 12. La mayoría de los dropshippers optimizan el
> número equivocado.

## El concepto: poder de compra efectivo

Tu capital no es lo que tienes. Es **lo que tienes multiplicado por cuántas veces lo puedes usar
antes de que se acabe la temporada**.

```
Vueltas          =  días de la temporada  ÷  días del ciclo de caja
Poder de compra  =  capital  ×  vueltas
```

| Modelo | Ciclo | Temporada 75 días | Vueltas | Poder de compra con US$500 |
|---|---|---|---|---|
| **Prepago** | **3 días** | 13-nov a 26-ene | **25** | **US$12.500** |
| COD | **12 días** | idem | **6,2** | US$3.100 |

Mismo capital. **Cuatro veces el negocio.** Esa es la razón por la que el proyecto de México cierra
en prepago aunque el COD convierta el doble en la página. Ver `30`.

## Qué es el ciclo de caja, exactamente

Días desde que **sale** un peso de tu bolsillo hasta que **vuelve** ese peso más la utilidad.

| Etapa | Prepago | COD |
|---|---|---|
| Pagas la publicidad | Día 0 | Día 0 |
| Cliente ordena | Día 0 | Día 0 |
| Cobras | **Día 0** | Día 4-7 (cuando entrega) |
| La pasarela / transportadora te liquida | Día 2-3 | Día 10-18 |
| **Ciclo total** | **≈3 días** | **≈12 días** |

Detalles que alargan el ciclo sin que te des cuenta:

| Ladrón de caja | Días que agrega |
|---|---|
| Pasarela con retención de 7 o 14 días | +4 a +11 |
| Reserva de riesgo de la pasarela (rolling reserve) | Congela 5-10% permanente |
| Transportadora COD que liquida semanal, no diario | +3 a +7 |
| Proveedor que exige pago antes de despachar / festivos de Q4 | +2 a +5 |

**Antes de elegir pasarela, pregunta el plazo de liquidación.** Es más importante que la comisión:
medio punto de comisión cuesta centavos; siete días de retención te quitan dos vueltas de caja en
plena temporada. Ver `192`.

## La aritmética del interés compuesto operativo

Cada vuelta reinvierte utilidad. Con multiplicador por ciclo `m = ticket ÷ (costo + CAC)`:

```
Prepago MX:  60,05 ÷ (29,33 + 10,54) = 1,506 por ciclo
COD MX:      60,05 ÷ (33,63 +  6,56) = 1,494 por ciclo
```

Multiplicador casi idéntico. **La diferencia entera está en cuántas veces lo aplicas**: 25 contra
6,2. Esa es toda la historia.

> Ojo con la fantasía: 1,506 elevado a 25 es un número ridículo. En la práctica el techo lo pone la
> demanda, el inventario y la cuenta publicitaria, no la calculadora. Por eso el script de abajo
> pone dos frenos: cuánto puedes subir el desembolso por ciclo y cuánto puedes gastar por día.

## Script: simulador de rotación de caja

```python
# -*- coding: utf-8 -*-
"""Simulador de rotacion de caja. Compara modelos por VUELTAS, no por margen."""
from decimal import Decimal as D, getcontext, ROUND_HALF_UP
getcontext().prec = 28

def d(x): return D(str(x))
def money(x): return x.quantize(D("0.01"), rounding=ROUND_HALF_UP)

# ─── PARAMETROS ────────────────────────────────────────────────────
CAPITAL_INICIAL = d(500)     # USD disponibles
DIAS_TEMPORADA  = 75         # 13-nov a 26-ene
TOPE_ESCALADO   = d("1.35")  # cuanto puedes subir el desembolso por ciclo (realismo)
TOPE_DIARIO     = d(150)     # techo REAL de gasto publicitario por dia que puedes operar
RETIRO          = d("0.00")  # fraccion de la utilidad que sacas cada ciclo

# ticket, costo (todo menos publicidad) y CAC en USD por venta cobrada
MODELOS = [
    dict(nombre="Prepago MX 1.099 + MSI", ciclo=3,  ticket=d("60.05"), costo=d("29.33"), cac=d("10.54")),
    dict(nombre="Prepago MX 699",         ciclo=3,  ticket=d("38.20"), costo=d("22.91"), cac=d("12.65")),
    dict(nombre="COD MX 1.099 confirm.",  ciclo=12, ticket=d("60.05"), costo=d("33.63"), cac=d("6.56")),
    dict(nombre="COD MX 699 confirm.",    ciclo=12, ticket=d("38.20"), costo=d("28.03"), cac=d("6.05")),
    dict(nombre="COD lento (China 20d)",  ciclo=22, ticket=d("38.20"), costo=d("46.86"), cac=d("9.44")),
]

def simular(m):
    desembolso_u = m["costo"] + m["cac"]          # lo que sale por cada venta
    util_u       = m["ticket"] - desembolso_u     # lo que entra limpio por venta
    ciclos       = DIAS_TEMPORADA // m["ciclo"]
    capital      = CAPITAL_INICIAL
    gasto_prev   = None
    ventas_tot   = D(0); util_tot = D(0); retirado = D(0)

    for _ in range(ciclos):
        if capital <= 0:
            break
        techo = TOPE_DIARIO * d(m["ciclo"])           # no puedes gastar mas rapido que esto
        gasto = min(capital, techo) if gasto_prev is None else min(capital, techo, gasto_prev * TOPE_ESCALADO)
        ventas  = gasto / desembolso_u
        ingreso = ventas * m["ticket"]
        util    = ventas * util_u
        sacar   = util * RETIRO if util > 0 else D(0)
        capital = capital - gasto + ingreso - sacar
        ventas_tot += ventas; util_tot += util; retirado += sacar
        gasto_prev = gasto

    return dict(vueltas=d(DIAS_TEMPORADA)/d(m["ciclo"]), ventas=ventas_tot,
                util=util_tot + retirado, capital=capital + retirado, util_u=util_u)

print("=" * 104)
print(f"ROTACION DE CAJA  |  capital USD {CAPITAL_INICIAL}  |  {DIAS_TEMPORADA} dias  |  "
      f"escalado max {TOPE_ESCALADO}x/ciclo  |  tope USD {TOPE_DIARIO}/dia")
print("=" * 104)
print(f"{'Modelo':<26}{'Ciclo':>7}{'Vueltas':>9}{'Util/vta':>10}{'Ventas':>9}{'UTILIDAD':>12}{'Caja final':>12}")
print("-" * 104)
for m in MODELOS:
    r = simular(m)
    print(f"{m['nombre']:<26}{m['ciclo']:>6}d{float(r['vueltas']):>9.1f}"
          f"{float(money(r['util_u'])):>10.2f}{float(r['ventas']):>9.0f}"
          f"{float(money(r['util'])):>12.2f}{float(money(r['capital'])):>12.2f}")
print("-" * 104)
print("\nLECTURA:")
print("  - Util/vta parecida + vueltas distintas = gana el de ciclo corto.")
print("  - Utilidad negativa = el modelo quema capital mas rapido cuanto mas escalas.")
print("  - Los dos topes son el freno real: sube TOPE_DIARIO solo hasta lo que puedas despachar.")
```

## Cómo usar el resultado

| Pregunta | Dónde mirar |
|---|---|
| ¿Qué modelo elijo? | Utilidad total, no utilidad por venta |
| ¿Cuánto stock necesito? | Ventas totales ÷ ciclos, con margen de seguridad |
| ¿Me alcanza el capital? / ¿puedo sacar plata? | Caja final cerca de cero = te estrangula. Sube `RETIRO` y mira cuánto se frena |

## Reglas de caja para capital chico

1. **No retires nada durante la temporada.** Un dólar retirado en noviembre son cuatro que no trabajan.
2. **Negocia liquidación diaria** con la pasarela antes que un descuento en comisión.
3. **Nunca compres stock con más de 30 días de cobertura** en tu primera temporada: es caja muerta.
4. **Mide el ciclo real, no el prometido.** Días entre que pagas el anuncio y que el dinero está
   disponible en tu banco. Si pasa de 7 días en prepago, el problema es la pasarela, no el producto.

## La frontera

El cálculo exacto del modelo financiero completo del negocio (flujo, punto de equilibrio,
sensibilidad) es de `228`. La viabilidad del **negocio** como tal — no del producto — es de
**`economist_lushows`**. Si necesitas que los números queden verificados al centavo,
**invoca `Matematicas_lushows`**.

## Relacionados
`30` COD vs prepago · `31` COD y China son incompatibles · `20` playbook México · `192` pasarelas ·
`228` modelo financiero completo · `233` cuántos tiros da tu capital
