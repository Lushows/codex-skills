# La tasa de entrega y cómo subirla (código)

> **Este es el módulo más importante del bloque logístico.** En contraentrega, la diferencia entre
> el 52% y el 78% de entrega no es una mejora operativa: es la diferencia entre perder dinero y
> ganarlo, con el mismo anuncio, el mismo producto y el mismo precio. La confirmación previa es
> la palanca que separa las dos cosas.

## Las tasas verificadas

| Escenario | Tasa de entrega |
|---|---|
| COD **sin** confirmación | **45-60%** |
| COD **con** confirmación previa | **65-78%** |
| Urbano con confirmación por **WhatsApp o voz IA** | **70-85%** |
| **CDMX / GDL / MTY con 99minutos**, confirmado | **78%** |
| México: sin confirmar / confirmado | **45-55% / 60-72%** |
| Colombia: sin confirmar / confirmado | **50-60% / 65-78%** |
| Prepago | 95-98% |

**Confirmar mueve la aguja entre 15 y 25 puntos.** Ninguna otra palanca de la operación se le
acerca.

## Por qué se cae un pedido (y qué palanca lo levanta)

| Causa | Peso típico | Palanca |
|---|---|---|
| Cliente se arrepintió / pedido impulsivo | Alto | Confirmación previa (`160`) |
| No estaba en casa | Alto | Avisar el día de entrega + ventana horaria |
| Teléfono apagado o falso | Medio | Verificar en la confirmación |
| Dirección incompleta o mal escrita | Medio | Referencias obligatorias en el checkout |
| "No recuerdo haber pedido eso" | Medio | Confirmación + mensaje de despacho |
| Zona sin cobertura real | Medio | Enrutamiento (`154`), exclusión (`173`) |
| No tenía el efectivo | Medio | Recordar el monto exacto en la confirmación |
| Un solo intento del repartidor | Bajo-medio | Elegir paquetería con 2-3 intentos |
| Pedido falso / sabotaje | Bajo | Filtro antifraude (`172`) |

## Las ocho palancas, por impacto

| # | Palanca | Impacto | Costo |
|---|---|---|---|
| 1 | **Confirmación previa** antes de despachar | **+15 a +25 pts** | Tiempo o bot (`162`) |
| 2 | Concentrar pauta en zona urbana | +8 a +15 pts | Menos alcance |
| 3 | Aviso el día de la entrega | +4 a +8 pts | Casi cero |
| 4 | Enrutar por destino | +3 a +8 pts | Cero |
| 5 | Dos teléfonos + referencia obligatorios | +3 a +6 pts | Un campo más en el checkout |
| 6 | Gestión activa del primer intento fallido | +3 a +6 pts | Tiempo |
| 7 | Anticipo del flete o descuento por prepago | +5 a +12 pts | Algo de conversión |
| 8 | Filtro antifraude antes de despachar | +1 a +3 pts | Cero |

> No las apliques todas de golpe. Aplica la 1, mide dos semanas limpias, y sigue. Cambiar cinco
> cosas a la vez significa no saber cuál funcionó.

## Script: el impacto en el bolsillo

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Impacto de la tasa de entrega en el margen por pedido despachado (COD)."""
from decimal import Decimal as D, ROUND_HALF_UP, getcontext

getcontext().prec = 28


def m(x):
    return D(str(x)).quantize(D("0.01"), rounding=ROUND_HALF_UP)


def escenario(precio, costo_producto, flete_ida, flete_retorno,
              comision_recaudo_pct, costo_confirmacion, cac,
              tasa_entrega, despachados=D("100")):
    """Margen total y por pedido ENTREGADO, para una tasa de entrega dada."""
    precio = D(str(precio)); costo = D(str(costo_producto))
    f_ida = D(str(flete_ida)); f_ret = D(str(flete_retorno))
    com = D(str(comision_recaudo_pct)); conf = D(str(costo_confirmacion))
    cac = D(str(cac)); t = D(str(tasa_entrega)); n = D(str(despachados))

    entregados = n * t
    fallidos = n - entregados

    ingresos = entregados * precio
    # El producto vuelve del fallido y se reaprovecha, pero el flete no.
    egresos = (entregados * (costo + f_ida + precio * com)
               + fallidos * (f_ida + f_ret)
               + n * conf
               + n * cac)
    margen = ingresos - egresos
    desperdicio = (D("1") - t) / t if t > 0 else None

    return {
        "tasa": f"{m(t * 100)}%",
        "entregados": m(entregados),
        "fallidos": m(fallidos),
        "desperdicio": m(desperdicio) if desperdicio is not None else "-",
        "margen_total": m(margen),
        "margen_por_entregado": m(margen / entregados) if entregados else "-",
        "margen_por_despachado": m(margen / n),
    }


def tasa_de_equilibrio(paso=D("0.01"), **kw):
    """Tasa mínima de entrega con la que el margen deja de ser negativo."""
    t = D("0.20")
    while t <= D("1.00"):
        if escenario(tasa_entrega=t, **kw)["margen_total"] >= 0:
            return m(t * 100)
        t += paso
    return None


if __name__ == "__main__":
    # Ejemplo COD Colombia en USD. VERIFICAR con tus números reales.
    base = dict(precio="26.00", costo_producto="6.50", flete_ida="2.90",
                flete_retorno="2.90", comision_recaudo_pct="0.03",
                costo_confirmacion="0.25", cac="7.00")

    print(f"{'tasa':>6} {'entreg':>7} {'desperd':>8} "
          f"{'margen tot':>11} {'x entregado':>12} {'x despachado':>13}")
    for t in ["0.45", "0.52", "0.60", "0.65", "0.72", "0.78", "0.85"]:
        r = escenario(tasa_entrega=t, **base)
        print(f"{r['tasa']:>6} {r['entregados']:>7} {r['desperdicio']:>8} "
              f"{r['margen_total']:>11} {r['margen_por_entregado']:>12} "
              f"{r['margen_por_despachado']:>13}")

    eq = tasa_de_equilibrio(**base)
    print(f"\nTasa de entrega de equilibrio: {eq}%")

    # Cuánto vale confirmar: 52% -> 75%
    sin_c = escenario(tasa_entrega="0.52", **base)
    con_c = escenario(tasa_entrega="0.75", **base)
    delta = D(str(con_c["margen_total"])) - D(str(sin_c["margen_total"]))
    print(f"Ganancia de confirmar (52% -> 75%), por cada 100 despachados: {m(delta)}")
```

## Cómo se lee

- **Margen por despachado** es la métrica honesta: reparte el costo de los fallidos entre todos.
- La **tasa de equilibrio** es tu línea roja. Si tu operación está por debajo, cada pedido que
  despachas te empobrece. No lo arregla vender más.
- La última línea te dice, en dinero, cuánto vale montar la confirmación. Casi siempre paga el
  sueldo de quien la hace, varias veces.

## Cómo se mide de verdad

| Métrica | Definición |
|---|---|
| Tasa de entrega | entregados ÷ **despachados** |
| Tasa de confirmación | confirmados ÷ pedidos recibidos |
| Tasa efectiva | entregados ÷ **pedidos recibidos** |
| Desperdicio | (1 − tasa) ÷ tasa |

Mide **por transportadora, por ciudad y por semana**, no un promedio global. El promedio esconde
que una ciudad entrega al 82% y otra al 41%. Ver `174`.

## La regla del cambio único

Un cambio a la vez, tres días limpios de datos antes de juzgar, mínimo 30-50 pedidos por celda.
Con menos, estás mirando ruido.

## Relacionados
`158` cómo funciona el COD · `160` guion de confirmación WhatsApp · `161` confirmación por voz IA ·
`162` bot propio · `163` costo de los rechazos · `173` zonas difíciles · `174` tablero
