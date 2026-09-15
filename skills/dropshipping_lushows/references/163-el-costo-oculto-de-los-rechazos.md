# El costo oculto de los rechazos (código)

> El pedido que no se entrega no cuesta cero. Cuesta el flete de ida, el flete de vuelta, el
> empaque, el tiempo de confirmación y el CAC del anuncio que lo trajo. **Y todo eso se lo cobras a
> los pedidos que sí se entregaron**, porque no hay nadie más a quien cobrárselo.

## La fórmula del desperdicio

```
desperdicio = (1 − tasa de cobro) ÷ tasa de cobro
```

Es "cuántos fallidos pagas por cada pedido bueno".

| Tasa de cobro | Desperdicio | Lectura |
|---|---|---|
| 95% (prepago) | 0,053 | 5 fallidos por cada 100 buenos |
| **78%** | **0,282** | 28 por cada 100 |
| 70% | 0,429 | 43 por cada 100 |
| 65% | 0,538 | 54 por cada 100 |
| 60% | 0,667 | 67 por cada 100 |
| **52%** | **0,923** | **92 por cada 100: casi uno a uno** |
| 45% | 1,222 | Más fallidos que buenos |

La curva **no es lineal**. Bajar de 78% a 65% no te quita 13 puntos de costo: te **duplica** el
desperdicio. Por eso perder unos puntos de entrega duele mucho más de lo que parece.

## Qué se pierde en cada modelo

| Concepto | COD fallido | Prepago reembolsado |
|---|---|---|
| Producto | Vuelve, si vuelve bien (`164`) | **Se pierde** o vuelve dañado |
| Flete de ida | **Perdido** | Perdido |
| Flete de vuelta | **Perdido** | Según política |
| Empaque | Perdido | Perdido |
| Comisión de pasarela | No aplica | A veces no se devuelve |
| CAC | **Perdido** | **Perdido** |
| Tiempo de confirmación | Perdido | — |

> En COD el fallido cuesta **flete de ida Y de vuelta**. En prepago reembolsado se pierde
> **producto + flete**. Son heridas distintas: la del COD sangra en flujo de caja, la del prepago
> sangra en inventario.

## El costo real por entrega buena

```
costo_por_entrega = costo_directo_del_bueno
                  + costo_de_un_fallido × desperdicio
```

Con eso el margen deja de ser una ilusión.

## Script

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Costo real de los rechazos: desperdicio, costo por entrega buena y margen honesto."""
from decimal import Decimal as D, ROUND_HALF_UP, getcontext

getcontext().prec = 28


def m(x):
    return D(str(x)).quantize(D("0.01"), rounding=ROUND_HALF_UP)


def m4(x):
    return D(str(x)).quantize(D("0.0001"), rounding=ROUND_HALF_UP)


def desperdicio(tasa_cobro):
    t = D(str(tasa_cobro))
    if t <= 0:
        raise ValueError("La tasa de cobro debe ser mayor que cero.")
    return (D("1") - t) / t


def analizar(precio, costo_producto, flete_ida, flete_vuelta, empaque,
             cac, costo_confirmacion, tasa_cobro, modelo="cod",
             recuperacion_producto=D("0.80")):
    """modelo: 'cod' (producto vuelve) o 'prepago' (se pierde al reembolsar).

    recuperacion_producto: fracción del costo del producto que recuperas
    cuando vuelve del fallido y se puede revender (solo COD).
    """
    precio = D(str(precio)); cp = D(str(costo_producto))
    fi = D(str(flete_ida)); fv = D(str(flete_vuelta)); emp = D(str(empaque))
    cac = D(str(cac)); conf = D(str(costo_confirmacion))
    rec = D(str(recuperacion_producto))
    w = desperdicio(tasa_cobro)

    if modelo == "cod":
        # El producto regresa; pierdes la fracción no recuperable + ambos fletes.
        costo_fallido = fi + fv + emp + cac + conf + cp * (D("1") - rec)
    else:
        # Prepago reembolsado: pierdes producto y flete de ida.
        costo_fallido = fi + emp + cac + cp

    costo_bueno = cp + fi + emp + cac + conf
    costo_total_por_entrega = costo_bueno + costo_fallido * w
    margen = precio - costo_total_por_entrega

    return {
        "tasa_cobro": f"{m(D(str(tasa_cobro)) * 100)}%",
        "desperdicio": m4(w),
        "costo_de_un_fallido": m(costo_fallido),
        "costo_directo_del_bueno": m(costo_bueno),
        "carga_de_fallidos_por_entrega": m(costo_fallido * w),
        "costo_real_por_entrega": m(costo_total_por_entrega),
        "margen_por_entrega": m(margen),
        "margen_%": m(margen / precio * 100),
    }


if __name__ == "__main__":
    base = dict(precio="26.00", costo_producto="6.50", flete_ida="2.90",
                flete_vuelta="2.90", empaque="0.70", cac="7.00",
                costo_confirmacion="0.25")

    print("MODELO COD")
    print(f"{'tasa':>7} {'desperd':>9} {'carga':>9} {'costo real':>11} "
          f"{'margen':>9} {'margen %':>9}")
    for t in ["0.45", "0.52", "0.60", "0.65", "0.72", "0.78", "0.85"]:
        r = analizar(tasa_cobro=t, modelo="cod", **base)
        print(f"{r['tasa_cobro']:>7} {r['desperdicio']:>9} "
              f"{r['carga_de_fallidos_por_entrega']:>9} "
              f"{r['costo_real_por_entrega']:>11} "
              f"{r['margen_por_entrega']:>9} {r['margen_%']:>9}")

    print("\nMODELO PREPAGO")
    for t in ["0.93", "0.95", "0.97"]:
        r = analizar(tasa_cobro=t, modelo="prepago", **base)
        print(f"{r['tasa_cobro']:>7} {r['desperdicio']:>9} "
              f"{r['carga_de_fallidos_por_entrega']:>9} "
              f"{r['costo_real_por_entrega']:>11} "
              f"{r['margen_por_entrega']:>9} {r['margen_%']:>9}")
```

## Cómo se usa esto para decidir

1. Corre el script con **tus** números, no con los del ejemplo.
2. Mira el margen al 52% y al 78%. Esa diferencia es el presupuesto que tienes para confirmar
   pedidos (`160`, `161`).
3. Si el margen al 65% ya es negativo, tu producto no aguanta COD. O subes precio, o bajas costo,
   o te vas a prepago (`30`).
4. Recalcula por ciudad: la ciudad que entrega al 45% puede estar financiándose con la que entrega
   al 82%. Apágala.

## Los costos que nadie mete y hay que meter

| Costo | Por qué se olvida |
|---|---|
| CAC del pedido fallido | Se contabiliza como costo de marketing global, no por pedido |
| Producto que vuelve dañado | Se asume que vuelve perfecto. Vuelve al 70-90% (`164`) |
| Tiempo de gestión del fallido | Alguien reprograma, llama, reempaca |
| Almacenaje del producto devuelto | Ocupa espacio y capital |
| Efecto en la reputación | No se mide, pero sube el CPA |

## La conclusión incómoda

El dropshipper promedio calcula margen así: precio − producto − flete − CAC. Con 52% de entrega,
ese cálculo se equivoca por **casi el doble del costo variable**. Por eso hay tiendas que "venden
mucho" y no tienen plata: están vendiendo bien y entregando mal.

Para verificación aritmética exacta, invoca `Matematicas_lushows`.

## Relacionados
`159` tasa de entrega · `158` contraentrega · `164` devoluciones · `30` COD vs prepago ·
`152` costo puesto en destino · `11` techo de CAC · `174` tablero
