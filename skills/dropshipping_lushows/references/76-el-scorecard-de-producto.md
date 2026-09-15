# El scorecard de producto

La razón por la que la gente pierde dinero no es que elija mal: es que elige con emoción y sin criterio escrito. El scorecard te obliga a poner un número antes de gastar, y sobre todo te obliga a **descartar** — que es donde está el 90% del valor, porque solo 1 de cada 10 productos testeados gana.

## Los 10 criterios y sus pesos

| # | Criterio | Peso | Qué mide |
|---|---|---|---|
| 1 | Múltiplo disponible | 18 | Precio de mercado / tu costo puesto en bodega |
| 2 | Demostrabilidad visual | 15 | ¿Se entiende en 10 segundos sin voz? |
| 3 | Demanda verificada | 14 | Señales de `60` |
| 4 | Competencia (IC invertido) | 12 | Índice de `64`, invertido |
| 5 | Disponibilidad local | 10 | Stock en el país, con factura |
| 6 | Logística (peso, tamaño, fragilidad) | 8 | ¿Cabe en caja chica, no se rompe? |
| 7 | Riesgo regulatorio | 8 | Registro sanitario, NOM, claims |
| 8 | Riesgo de devolución (talla, compatibilidad) | 6 | SKUs y ajuste |
| 9 | Potencial de bundle | 5 | ¿Tiene complementos naturales? |
| 10 | Encaje de temporada | 4 | ¿Coincide con la ventana en la que vendes? |

Total: 100.

## Rúbrica de puntuación (0-10 por criterio)

| Criterio | 0-3 | 4-6 | 7-10 |
|---|---|---|---|
| Múltiplo | <2,7x | 2,7-3,3x | >3,3x |
| Demostrabilidad | Hay que explicarlo | Se entiende con texto | Obvio sin audio ni texto |
| Demanda | Solo vistas | Reseñas o anuncios recientes | Anuncios +60 días + reseñas del mes + comentarios de intención |
| Competencia (IC) | IC >20 | IC 9-20 | IC 3-8 |
| Disponibilidad local | Solo China | Proveedor nacional sin stock fijo | Proveedor nacional con stock y factura |
| Logística | Frágil, >3 kg, voluminoso | Mediano | <500 g, caja chica, resistente |
| Regulatorio | Registro sanitario o claim médico | NOM o certificación exigible | Ninguna exigencia |
| Devolución | Talla o compatibilidad crítica | Algún SKU | Universal, un solo SKU |
| Bundle | No tiene complementos | Uno forzado | 2-3 naturales del mismo momento |
| Temporada | Fuera de ventana | Neutro | Justo en la ventana |

## Umbrales de decisión

| Puntaje | Veredicto |
|---|---|
| ≥ 72 | 🟢 Testear con presupuesto completo (USD 200-300) |
| 62-71 | 🟡 Validación inicial barata (USD 50-100) y decidir |
| < 62 | 🔴 No testear |

**Vetos automáticos** (sin importar el puntaje total): múltiplo bajo 2,7x en México, registro sanitario que no tienes, producto sin proveedor local (regla del proyecto), o riesgo de daño a un niño (`72`).

## Script (código)

```python
from decimal import Decimal, ROUND_HALF_UP

PESOS = {
    "multiplo": 18, "demostrabilidad": 15, "demanda": 14, "competencia": 12,
    "disponibilidad_local": 10, "logistica": 8, "regulatorio": 8,
    "devolucion": 6, "bundle": 5, "temporada": 4,
}

MULTIPLO_MINIMO = {  # ganador real, Q4-2026
    "MX": Decimal("2.70"), "CO": Decimal("2.52"),
    "ES": Decimal("2.11"), "US": Decimal("5.31"),
}


def puntaje_multiplo(precio_mercado, costo_bodega, pais="MX"):
    """Convierte el múltiplo disponible en una nota 0-10."""
    precio = Decimal(str(precio_mercado))
    costo = Decimal(str(costo_bodega))
    if costo <= 0:
        raise ValueError("El costo debe ser mayor que cero")
    mult = (precio / costo).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    minimo = MULTIPLO_MINIMO[pais]
    if mult < minimo:
        return Decimal("0"), mult, True  # veto
    if mult < Decimal("2.70"):
        nota = Decimal("3")
    elif mult < Decimal("3.30"):
        nota = Decimal("6")
    elif mult < Decimal("4.00"):
        nota = Decimal("8")
    else:
        nota = Decimal("10")
    return nota, mult, False


def puntaje_competencia(ic):
    ic = Decimal(str(ic))
    if ic > 20:
        return Decimal("2")
    if ic >= 9:
        return Decimal("5")
    if ic >= 3:
        return Decimal("9")
    return Decimal("6")  # IC<3: o fase 1, o no hay mercado


def scorecard(notas, precio_mercado, costo_bodega, ic, pais="MX", vetos=()):
    """notas: dict con las 8 notas manuales 0-10.
    Devuelve (puntaje 0-100, veredicto, detalle)."""
    n_mult, mult, veto_mult = puntaje_multiplo(precio_mercado, costo_bodega, pais)
    completas = dict(notas)
    completas["multiplo"] = n_mult
    completas["competencia"] = puntaje_competencia(ic)

    faltan = set(PESOS) - set(completas)
    if faltan:
        raise ValueError(f"Faltan notas: {sorted(faltan)}")

    total = Decimal("0")
    detalle = {}
    for criterio, peso in PESOS.items():
        nota = Decimal(str(completas[criterio]))
        if not (Decimal("0") <= nota <= Decimal("10")):
            raise ValueError(f"{criterio}: nota fuera de 0-10")
        aporte = (nota * Decimal(peso) / Decimal("10")).quantize(Decimal("0.01"))
        detalle[criterio] = aporte
        total += aporte

    total = total.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)
    hay_veto = veto_mult or bool(vetos)

    if hay_veto:
        veredicto = "VETO: " + ("multiplo bajo minimo; " if veto_mult else "") + "; ".join(vetos)
    elif total >= 72:
        veredicto = "TESTEAR completo (USD 200-300)"
    elif total >= 62:
        veredicto = "VALIDACION barata (USD 50-100)"
    else:
        veredicto = "NO TESTEAR"

    return total, veredicto, {"multiplo_real": mult, "aportes": detalle}


if __name__ == "__main__":
    notas = {
        "demostrabilidad": 9, "demanda": 8, "disponibilidad_local": 9,
        "logistica": 8, "regulatorio": 10, "devolucion": 9,
        "bundle": 8, "temporada": 10,
    }
    total, veredicto, det = scorecard(
        notas, precio_mercado="1099", costo_bodega="260", ic=6, pais="MX"
    )
    print(f"Multiplo real: {det['multiplo_real']}x")
    print(f"Puntaje: {total}/100 -> {veredicto}")
```

## Cómo usarlo de verdad

1. Puntúa **10 candidatos a la vez**, no uno. El scorecard sirve para ordenar, no para bendecir.
2. Puntúa antes de enamorarte. Si ya compraste la muestra, tu nota va a estar sesgada.
3. Guarda el scorecard. Cuando el producto muera (`78`), compara la nota con el resultado real y recalibra tus pesos.
4. Los pesos son un punto de partida honesto, no una ley física. Si en tu operación la logística te ha matado dos veces, súbele el peso.

Para cálculos exactos de margen con envío, pasarela, devoluciones y comisión MSI, invoca `Matematicas_lushows`.

## Relacionados

`60` demanda real · `61` saturación · `64` medir competencia · `77` muestras · `78` matar a tiempo · `79` portafolio
