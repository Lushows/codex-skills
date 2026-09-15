# Modelo financiero en código

## Qué hace

Recibe producto, país y escenario. Devuelve **techo de CAC, CAC (estimado u observado), holgura,
ROAS de equilibrio, punto de equilibrio, múltiplo sobre costo y utilidad por pedido**: es lo que
decide si un producto se lanza o se descarta. Guárdalo como `modelo.py` y corre `python modelo.py`.

```python
# modelo.py — modelo financiero por producto (dropshipping, Q4-2026)
from dataclasses import dataclass
from decimal import Decimal as D, ROUND_HALF_UP

def money(x) -> D:
    return D(str(x)).quantize(D("0.01"), rounding=ROUND_HALF_UP)

def ratio(x) -> D:
    return D(str(x)).quantize(D("0.001"), rounding=ROUND_HALF_UP)

CPM_BASE = {  # USD, referencia Q4-2026. VERIFICAR con tu cuenta.
    "peru": D("3.70"), "colombia": D("4.00"), "mexico": D("4.50"),
    "chile": D("5.20"), "espana": D("5.80"), "eeuu": D("23.00"),
}

# múltiplo mínimo ticket ÷ costo puesto en bodega para ~20% neto
MULTIPLO_MINIMO = {
    "espana":   {"conservador": D("4.33"), "creativo": D("2.72"), "ganador": D("2.11")},
    "peru":     {"conservador": D("3.19"), "creativo": D("2.62"), "ganador": D("2.39")},
    "colombia": {"conservador": D("3.39"), "creativo": D("2.77"), "ganador": D("2.52")},
    "chile":    {"conservador": D("3.68"), "creativo": D("2.87"), "ganador": D("2.55")},
    "mexico":   {"conservador": D("3.74"), "creativo": D("3.00"), "ganador": D("2.70")},
    "eeuu":     {"conservador": D("14.98"), "creativo": D("7.94"), "ganador": D("5.31")},
}

ESCENARIOS = {
    "conservador": {"ctr": D("0.015"), "cvr_prepago": D("0.020"), "cvr_cod": D("0.045")},
    "creativo":    {"ctr": D("0.022"), "cvr_prepago": D("0.030"), "cvr_cod": D("0.065")},
    "ganador":     {"ctr": D("0.030"), "cvr_prepago": D("0.040"), "cvr_cod": D("0.085")},
}

@dataclass
class Producto:
    nombre: str
    ticket: D                 # lo que paga el cliente, envío incluido
    costo_bodega: D           # producto + flete intl + arancel + empaque  (ver 28)
    flete_cliente: D          # última milla
    comision_pct: D           # pasarela + MSI, como fracción del ticket
    comision_fija: D = D("0")
    atencion: D = D("0")      # soporte por pedido
    tasa_cobro: D = D("0.97") # cobrados ÷ generados
    pago: str = "prepago"     # "prepago" | "cod"
    costo_confirmacion: D = D("0")   # call center / bot, solo COD
    costos_fijos_producto: D = D("0")  # creativos, muestras, fotos

def desperdicio(t: D) -> D: return (D("1") - t) / t

def costo_fallidos(p: Producto) -> D:
    w = desperdicio(p.tasa_cobro)
    if p.pago == "cod":
        return w * (p.flete_cliente * 2 + p.costo_confirmacion)
    return w * (p.costo_bodega + p.flete_cliente)

def cac_estimado(pais: str, escenario: str, pago: str, tasa_cobro: D,
                 factor_cpm: D = D("1")) -> D:
    e = ESCENARIOS[escenario]
    cvr = e["cvr_cod"] if pago == "cod" else e["cvr_prepago"]
    por_impresion = e["ctr"] * cvr * tasa_cobro          # pedidos cobrados / impresión
    return (CPM_BASE[pais] * factor_cpm / D("1000")) / por_impresion

def diagnostico_holgura(h: D) -> str:
    if h < D("1"):   return "PIERDES DINERO"
    if h < D("1.3"): return "trabajas gratis"
    if h < D("2"):   return "fragil ante temporada"
    return "SANO" if h <= D("3") else "subinvirtiendo: sube presupuesto"

def modelo(p: Producto, pais: str, escenario: str,
           cac_observado: D | None = None, factor_cpm: D = D("1")) -> dict:
    comision = p.ticket * p.comision_pct + p.comision_fija
    fallidos = costo_fallidos(p)
    costos = p.costo_bodega + p.flete_cliente + comision + p.atencion + fallidos
    techo = p.ticket - costos
    cac = cac_observado if cac_observado is not None else \
        cac_estimado(pais, escenario, p.pago, p.tasa_cobro, factor_cpm)
    utilidad = techo - cac
    holgura = techo / cac if cac > 0 else D("0")
    roas_eq = p.ticket / techo if techo > 0 else D("0")
    multiplo = p.ticket / p.costo_bodega
    minimo = MULTIPLO_MINIMO[pais][escenario]
    equilibrio = (p.costos_fijos_producto / utilidad) if utilidad > 0 else None
    return {
        "producto": p.nombre, "pais": pais, "escenario": escenario,
        "ticket": money(p.ticket), "costos_por_pedido": money(costos),
        "costo_fallidos": money(fallidos), "desperdicio": ratio(desperdicio(p.tasa_cobro)),
        "techo_cac": money(techo), "cac": money(cac), "utilidad": money(utilidad),
        "holgura": ratio(holgura), "diagnostico": diagnostico_holgura(holgura),
        "roas_equilibrio": ratio(roas_eq), "multiplo": ratio(multiplo),
        "multiplo_minimo": minimo, "pasa_multiplo": multiplo >= minimo,
        "pedidos_equilibrio": (None if equilibrio is None else int(equilibrio) + 1),
    }

def imprimir(r: dict) -> None:
    print(f"\n=== {r['producto']} | {r['pais']} | escenario {r['escenario']} ===")
    print(f"  Ticket                 USD {r['ticket']}")
    print(f"  Costos por pedido      USD {r['costos_por_pedido']}"
          f"  (fallidos: {r['costo_fallidos']}, desperdicio {r['desperdicio']})")
    print(f"  TECHO DE CAC           USD {r['techo_cac']}")
    print(f"  CAC                    USD {r['cac']}")
    print(f"  UTILIDAD POR PEDIDO    USD {r['utilidad']}")
    print(f"  Holgura                {r['holgura']}x  -> {r['diagnostico']}")
    print(f"  ROAS de equilibrio     {r['roas_equilibrio']}")
    print(f"  Multiplo {r['multiplo']}x vs minimo {r['multiplo_minimo']}x"
          f"  -> {'PASA' if r['pasa_multiplo'] else 'NO PASA'}")
    if r["pedidos_equilibrio"]:
        print(f"  Pedidos para equilibrio {r['pedidos_equilibrio']}")

if __name__ == "__main__":   # Mexico dic-2026
    bundle = Producto("Bundle 1.099 MXN + MSI", D("60.05"), D("16.22"), D("8.74"),
                      D("0.050"), D("0.30"), D("0.30"), D("0.97"), "prepago",
                      costos_fijos_producto=D("250"))
    suelto = Producto("Suelto 699 MXN", D("38.20"), D("11.61"), D("8.74"),
                      D("0.035"), D("0.30"), D("0.30"), D("0.97"), "prepago",
                      costos_fijos_producto=D("250"))
    imprimir(modelo(bundle, "mexico", "ganador", cac_observado=D("10.54")))
    imprimir(modelo(suelto, "mexico", "ganador", cac_observado=D("12.65")))
    imprimir(modelo(bundle, "mexico", "creativo", factor_cpm=D("1.65")))  # Buen Fin
```

## Salida esperada (resumen)

| Caso | Costos/pedido | Techo CAC | CAC | Utilidad | Holgura | ROAS eq. |
|---|---|---|---|---|---|---|
| Bundle, CAC observado | 29,33 | 30,72 | 10,54 | 20,18 | 2,914x SANO | 1,955 |
| Suelto, CAC observado | 22,92 | 15,28 | 12,65 | 2,63 | 1,208x trabajas gratis | 2,499 |
| Bundle, CPM Buen Fin (+65%) | 29,33 | 30,72 | 11,60 | 19,12 | 2,648x SANO | 1,955 |

(30,72 y no 30,73 es redondeo de centavos; irrelevante para decidir.)

## Cómo usarlo y regla de decisión

| Situación | Qué cambiar |
|---|---|
| Producto nuevo | crea otro `Producto` y corre los tres escenarios |
| COD | `pago="cod"`, `tasa_cobro` 0,52-0,78, agrega `costo_confirmacion` |
| Temporada | `factor_cpm` 1,2-1,5 (Q4) o 1,5-1,8 (Black Friday / Buen Fin) |
| Otro país | cambia el `pais`; las tablas ya traen CPM y múltiplo mínimo |
| Probar un descuento | baja el `ticket` y mira cómo cae el techo (`221`) |

```
Lanzar solo si, en escenario CONSERVADOR:  holgura ≥ 1,3x  y  multiplo ≥ minimo del pais
Escalar solo si, con CAC observado:        holgura ≥ 2,0x durante 3 dias seguidos
```

Si el producto solo funciona en escenario "ganador", no es un plan: es una esperanza.

**Advertencias:** los CPM y múltiplos mínimos son referencias de Q4-2026 — verifícalos con tus
datos apenas tengas 3-5 ventas. El `cac_estimado` sirve para planear; el observado, para decidir.
Para auditar un resultado invoca `Matematicas_lushows`; para impuestos y registro contable,
`236`, `237` y `contador_lushows`.

## Relacionados
`11` · `28` · `42` · `223` · `224` · `225` · `226` · `227` · `229` · `231` · `232` · `233` · `238` · `239`
