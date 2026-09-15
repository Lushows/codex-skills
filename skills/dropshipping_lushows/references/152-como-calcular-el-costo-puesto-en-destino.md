# Cómo calcular el costo puesto en destino (código)

> El costo de tu producto **no es lo que te cobró el proveedor**. Es lo que te cuesta tenerlo en tu
> bodega, listo para despachar, con impuestos pagados y las mermas repartidas. Ese número —el
> *landed cost*— es el único que sirve para fijar precio. Todo lo demás es adivinar.

## La fórmula

```
Landed cost unitario =
    precio FOB unitario
  + flete internacional prorrateado
  + seguro prorrateado
  + arancel + IVA/impuesto local
  + despacho, agente y manejo prorrateados
  + transporte interno prorrateado
  + empaque de destino
  ───────────────────────────────────
  ÷ (1 − tasa de merma)      ← lo que se pierde se reparte entre lo que sí vendes
```

## Cómo se prorratea cada cosa

| Costo | Base de prorrateo correcta | Error común |
|---|---|---|
| Flete aéreo | **Peso cobrable** (real o volumétrico) | Repartirlo por unidades cuando hay SKUs de pesos distintos |
| Flete marítimo | **CBM** | Igual |
| Arancel e IVA | **Valor de cada línea** | Repartir plano |
| Agente, THC, desconsolidación | Por bulto o plano entre todas las unidades | — |
| Transporte interno | Por peso o plano | — |
| Merma / defectuosos | Se **divide**, no se suma | Sumarla subestima el impacto |

> Dos formas válidas de repartir el arancel: **proporcional al valor** (correcto cuando hay varios
> SKUs de precios distintos) o **plano por unidad** (aceptable con un solo SKU). El script hace las
> dos y muestra la diferencia.

## Lo que casi nadie mete y debería

| Concepto | Magnitud típica | Por qué importa |
|---|---|---|
| Merma de importación (rotos, faltantes) | 2-5% | Ver `165` |
| Defectuosos que descubres vendiendo | 3-8% | Ver `164` |
| Empaque de destino (caja, inserto, etiqueta) | Costo real por unidad | Ver `167`, `168` |
| Comisión de pasarela | 3-4% + fijo, verificar | No es landed cost, pero va al margen |
| Flete al cliente | Ver `153`-`155` | Tampoco es landed cost; va aparte |

El landed cost termina en tu bodega. El flete al cliente y la comisión de pago van después, en el
cálculo de margen (`06`, `42`).

## Script

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Costo puesto en destino (landed cost) por unidad.
Dinero con Decimal. Reparte arancel proporcional al valor o plano por unidad.
"""
from decimal import Decimal as D, ROUND_HALF_UP, getcontext

getcontext().prec = 28
CERO = D("0")


def m(x):
    """Redondea a 2 decimales de moneda."""
    return D(str(x)).quantize(D("0.01"), rounding=ROUND_HALF_UP)


class Linea:
    """Un SKU dentro del embarque."""

    def __init__(self, sku, unidades, fob_unitario, peso_kg_unitario,
                 cbm_unitario=D("0"), tasa_arancel=D("0"), tasa_iva=D("0"),
                 empaque_destino_unit=D("0"), merma=D("0")):
        self.sku = sku
        self.unidades = D(str(unidades))
        self.fob_unitario = D(str(fob_unitario))
        self.peso_unit = D(str(peso_kg_unitario))
        self.cbm_unit = D(str(cbm_unitario))
        self.tasa_arancel = D(str(tasa_arancel))
        self.tasa_iva = D(str(tasa_iva))
        self.empaque = D(str(empaque_destino_unit))
        self.merma = D(str(merma))

    @property
    def valor_fob(self):
        return self.fob_unitario * self.unidades

    @property
    def peso_total(self):
        return self.peso_unit * self.unidades

    @property
    def cbm_total(self):
        return self.cbm_unit * self.unidades


def landed_cost(lineas, flete_total, seguro_total, gastos_fijos_destino,
                base_flete="peso", reparto_arancel="valor"):
    """Devuelve dict por SKU con el costo unitario puesto en bodega.

    base_flete: 'peso' (aéreo) o 'cbm' (marítimo)
    reparto_arancel: 'valor' (proporcional) o 'plano' (por unidad)
    """
    flete_total = D(str(flete_total))
    seguro_total = D(str(seguro_total))
    gastos_fijos_destino = D(str(gastos_fijos_destino))

    total_valor = sum((l.valor_fob for l in lineas), CERO)
    total_peso = sum((l.peso_total for l in lineas), CERO)
    total_cbm = sum((l.cbm_total for l in lineas), CERO)
    total_unid = sum((l.unidades for l in lineas), CERO)

    base_total = total_peso if base_flete == "peso" else total_cbm
    if base_total == CERO:
        raise ValueError("La base de flete es cero: revisa pesos o CBM.")
    if total_valor == CERO:
        raise ValueError("El valor FOB total es cero.")

    # Impuesto total del embarque (para el reparto plano)
    imp_total = CERO
    for l in lineas:
        base_l = l.valor_fob + flete_total * (
            (l.peso_total if base_flete == "peso" else l.cbm_total) / base_total)
        ar = base_l * l.tasa_arancel
        imp_total += ar + (base_l + ar) * l.tasa_iva

    salida = {}
    for l in lineas:
        cuota_flete = flete_total * (
            (l.peso_total if base_flete == "peso" else l.cbm_total) / base_total)
        cuota_seguro = seguro_total * (l.valor_fob / total_valor)
        cuota_fijos = gastos_fijos_destino * (l.unidades / total_unid)

        base_imp = l.valor_fob + cuota_flete + cuota_seguro
        arancel = base_imp * l.tasa_arancel
        iva = (base_imp + arancel) * l.tasa_iva
        imp_linea = arancel + iva

        if reparto_arancel == "plano":
            imp_linea = imp_total * (l.unidades / total_unid)

        subtotal = (l.valor_fob + cuota_flete + cuota_seguro
                    + cuota_fijos + imp_linea + l.empaque * l.unidades)
        unit_bruto = subtotal / l.unidades
        if l.merma >= D("1"):
            raise ValueError("La merma no puede ser 100%.")
        unit_neto = unit_bruto / (D("1") - l.merma)

        salida[l.sku] = {
            "unidades": l.unidades,
            "fob_unit": m(l.fob_unitario),
            "flete_unit": m(cuota_flete / l.unidades),
            "seguro_unit": m(cuota_seguro / l.unidades),
            "fijos_unit": m(cuota_fijos / l.unidades),
            "impuesto_unit": m(imp_linea / l.unidades),
            "empaque_unit": m(l.empaque),
            "landed_sin_merma": m(unit_bruto),
            "landed_con_merma": m(unit_neto),
            "sobrecosto_%": m((unit_neto / l.fob_unitario - 1) * 100),
        }
    return salida


if __name__ == "__main__":
    # Ejemplo: lote México, aéreo, arancel 33,5% país sin TLC (1-ene-2026) + IVA 16%.
    # VERIFICAR tasas y flete reales antes de decidir.
    lote = [
        Linea("BUNDLE-A", 120, fob_unitario="4.20", peso_kg_unitario="0.45",
              tasa_arancel="0.335", tasa_iva="0.16",
              empaque_destino_unit="0.60", merma="0.05"),
    ]
    r = landed_cost(lote, flete_total="430.00", seguro_total="18.00",
                    gastos_fijos_destino="150.00",
                    base_flete="peso", reparto_arancel="valor")
    for sku, d in r.items():
        print(f"\n== {sku} ==")
        for k, v in d.items():
            print(f"  {k:<20} {v}")
```

## Cómo se lee el resultado

| Salida | Qué significa |
|---|---|
| `landed_sin_merma` | Costo real en bodega, si todo llega perfecto |
| `landed_con_merma` | **El que debes usar para fijar precio** |
| `sobrecosto_%` | Cuánto crece el precio del proveedor. 80-180% es normal en aéreo; por encima de ~200% el producto es **demasiado pesado o demasiado barato** para volar |

El ejemplo del script da **254%**: FOB 4,20 → landed 14,88. No es un error del código, es el
diagnóstico. Un producto de 0,45 kg que cuesta USD 4,20 paga USD 3,58 solo de flete aéreo. Ese
producto o viaja por barco, o se compra local, o se cambia (`41`).

Luego, precio de venta mínimo: `landed_con_merma × múltiplo mínimo` (`42`), y verifica contra el
techo de CAC (`11`).

## Errores que hacen quebrar

1. Fijar precio sobre el precio del proveedor. Faltan 60-140%.
2. Olvidar el IVA cuando no lo puedes acreditar.
3. No meter la merma: es la diferencia entre margen contable y margen real.
4. Repartir flete plano con SKUs de pesos muy distintos: subsidias el pesado con el liviano.
5. Meter el flete al cliente aquí. Va en el margen por pedido, no en el landed cost.

Para verificación aritmética exacta invoca `Matematicas_lushows`; para tratamiento contable del IVA
y del costo de inventario, `contador_lushows`.

## Relacionados
`149` DDP y DDU · `151` despacho de aduana · `147` modos de envío · `42` múltiplo mínimo · `11`
techo de CAC · `163` costo de los rechazos · `167` empaque
