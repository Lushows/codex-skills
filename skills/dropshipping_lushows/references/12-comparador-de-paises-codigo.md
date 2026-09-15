# Comparador de países (código ejecutable)

> **Ejecuta este script, no estimes de memoria.** Los aranceles y el CPM cambian; el modelo no.
> Guárdalo en el scratchpad y córrelo con los datos del producto concreto.

## Qué hace

Calcula, para cada país candidato: CAC real, techo de CAC, utilidad por venta cobrada, holgura,
múltiplo mínimo necesario, y cuántos tests permite tu capital. Ordena por holgura.

## El script

```python
# -*- coding: utf-8 -*-
"""Comparador de paises para dropshipping. Ajusta PRODUCTO, ESCENARIO y PAISES."""
from decimal import Decimal as D, getcontext
getcontext().prec = 28
def d(x): return D(str(x))

# ─── 1. TU PRODUCTO ────────────────────────────────────────────────
COSTO_PRODUCTO = d(8.00)    # USD, costo unitario al proveedor
FLETE_INTL     = d(5.50)    # USD por unidad, prorrateado (0 si compras local)
CAPITAL        = d(500)     # USD disponible para invertir
MARGEN_OBJETIVO= d(0.20)    # utilidad neta deseada sobre el ticket
TASA_GANADOR   = d(0.10)    # 1 de cada 10 productos testeados pega
SENAL          = d(3)       # ventas necesarias para leer la senal

# ─── 2. CALIDAD ESPERADA DEL CREATIVO ──────────────────────────────
ESCENARIOS = {
    "conservador":    dict(ctr=d(0.015), cvr_pre=d(0.020), cvr_cod=d(0.045)),
    "creativo bueno": dict(ctr=d(0.022), cvr_pre=d(0.030), cvr_cod=d(0.065)),
    "ganador real":   dict(ctr=d(0.030), cvr_pre=d(0.040), cvr_cod=d(0.085)),
}
ESC = ESCENARIOS["creativo bueno"]   # <-- cambia aqui

# ─── 3. PAISES CANDIDATOS ──────────────────────────────────────────
# cpm = CPM base en USD | q4 = multiplicador de temporada
# t_imp = arancel+IVA de importacion como fraccion del valor declarado
# imp_plano = impuesto fijo por pedido en USD (UE: 3 EUR por linea)
# cobro = tasa de entrega/cobro | local = flete ultima milla
# fee = comision de pasarela o plataforma | conf = costo de confirmacion
PAISES = [
 dict(pais="Mexico local",   cpm=d(4.50), q4=d(1.50), modelo="prepago", ticket=d(60.05),
      t_imp=d(0),     imp_plano=d(0), cobro=d(0.97), local=d(8.74), fee=d(0.055), conf=d(0),
      local_supply=True),
 dict(pais="Mexico COD",     cpm=d(4.50), q4=d(1.50), modelo="COD", ticket=d(60.05),
      t_imp=d(0),     imp_plano=d(0), cobro=d(0.78), local=d(8.74), fee=d(0.05), conf=d(0.35),
      local_supply=True),
 dict(pais="Mexico <-China", cpm=d(4.50), q4=d(1.50), modelo="COD", ticket=d(38.20),
      t_imp=d(0.335), imp_plano=d(0), cobro=d(0.50), local=d(8.74), fee=d(0.05), conf=d(0.35),
      local_supply=False),
 dict(pais="Espana <-China", cpm=d(5.80), q4=d(1.50), modelo="prepago", ticket=d(43.00),
      t_imp=d(0),     imp_plano=d(3.30), cobro=d(0.95), local=d(0), fee=d(0.035), conf=d(0),
      local_supply=False),
 dict(pais="Colombia COD",   cpm=d(4.00), q4=d(1.45), modelo="COD", ticket=d(30.00),
      t_imp=d(0),     imp_plano=d(0), cobro=d(0.78), local=d(2.80), fee=d(0.05), conf=d(0.35),
      local_supply=True),
 dict(pais="EEUU <-China",   cpm=d(23.00),q4=d(1.65), modelo="prepago", ticket=d(49.90),
      t_imp=d(0.54),  imp_plano=d(0), cobro=d(0.95), local=d(0), fee=d(0.035), conf=d(0),
      local_supply=False),
]

def analizar(p):
    cpm_q4 = p["cpm"] * p["q4"]
    cvr = ESC["cvr_pre"] if p["modelo"] == "prepago" else ESC["cvr_cod"]
    cobrados = d(1000) * ESC["ctr"] * cvr * p["cobro"]
    cac = cpm_q4 / cobrados

    flete_i = d(0) if p["local_supply"] else FLETE_INTL
    landed  = COSTO_PRODUCTO + flete_i
    impuesto = landed * p["t_imp"] + p["imp_plano"]

    desperdicio = (d(1) - p["cobro"]) / p["cobro"]
    if p["modelo"] == "COD":
        fallidos = desperdicio * (p["local"] * d(2) + p["conf"])
    else:
        fallidos = desperdicio * (landed + p["local"])

    costos = landed + impuesto + p["local"] + p["ticket"]*p["fee"] + p["conf"] + fallidos
    techo  = p["ticket"] - costos
    util   = techo - cac
    holgura= techo / cac if cac else d(0)
    multiplo_min = (costos - p["ticket"]*p["fee"] + cac) / (d(1) - p["fee"] - MARGEN_OBJETIVO) / landed
    costo_test = cac * SENAL
    tiros = int((CAPITAL - d(25)) / costo_test) if costo_test > 0 else 0
    p_exito = d(1) - (d(1) - TASA_GANADOR) ** tiros
    return dict(cpm_q4=cpm_q4, cac=cac, techo=techo, util=util, holgura=holgura,
                multiplo=multiplo_min, tiros=tiros, p=p_exito, roas_eq=p["ticket"]/techo if techo>0 else d(0))

print("="*116)
print(f"COMPARADOR DE PAISES  |  producto USD {COSTO_PRODUCTO} + flete {FLETE_INTL}  |  capital USD {CAPITAL}")
print("="*116)
print(f"{'Pais':<18}{'Ticket':>8}{'CAC':>8}{'Techo':>8}{'UTIL':>8}{'Holgura':>9}{'ROASeq':>8}{'Tiros':>7}{'P(gana)':>9}")
print("-"*116)
filas = [(p, analizar(p)) for p in PAISES]
for p, m in sorted(filas, key=lambda r: -r[1]["holgura"]):
    print(f"{p['pais']:<18}{float(p['ticket']):>8.2f}{float(m['cac']):>8.2f}{float(m['techo']):>8.2f}"
          f"{float(m['util']):>8.2f}{float(m['holgura']):>9.2f}{float(m['roas_eq']):>8.2f}"
          f"{m['tiros']:>7}{float(m['p'])*100:>8.0f}%")
print("-"*116)
print("\nLECTURA:")
print("  Holgura < 1.0  -> pierdes en cada venta, no hay negocio")
print("  Holgura 1.3-2.0-> real pero fragil ante el CPM de temporada")
print("  Holgura > 2.0  -> aguanta Black Friday, escala")
print("  ROASeq         -> el ROAS por debajo del cual pierdes plata")
```

## Cómo usarlo bien

1. **Pon TU costo de producto real**, no uno inventado. Si no lo tienes, pide cotización primero.
2. **Corre los tres escenarios.** Si el país solo funciona en "ganador real", estás apostando a que
   tu creativo sea excepcional. Es una apuesta, no un plan.
3. **Mira la holgura, no la utilidad.** Utilidad alta con holgura de 1,1 se evapora en temporada.
4. **Cruza `tiros` con tu fecha límite.** De nada sirven 28 tiros si no hay tiempo de dispararlos.

## Errores frecuentes al llenar los datos

| Error | Consecuencia |
|---|---|
| Poner `local_supply=True` con proveedor chino | Te ahorras el flete internacional que sí vas a pagar |
| Usar el CPM base en vez del de temporada | Subestimas el CAC entre 20% y 80% |
| Poner tasa de cobro de 95% en COD | El COD real va de 52% a 85%. Ver `159` |
| Olvidar el costo de confirmación | Pequeño por pedido, grande en volumen |
| Usar el ticket que **quieres** y no el que el mercado paga | Modelo bonito, negocio muerto. Ver `34` |

## Relacionados
`10` cómo se elige un país · `11` el techo de CAC · `13` mapa aduanero · `226` ROAS de equilibrio ·
`228` modelo financiero completo · `233` cuántos tiros da tu capital
