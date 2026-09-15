# México: el arancel del 33,5% y el decreto de 2026

> Vigencia: septiembre 2026. Verifica en el DOF y en la ANAM antes de recomendar.

## Qué dice la norma

| Fecha | Qué ocurrió |
|---|---|
| **15-ago-2025** | Entran en vigor reglas y arancel del **33,5%** a paquetería de Temu, Shein, AliExpress y similares (venía del 19%) |
| **29-dic-2025** | Decreto con paquete arancelario para importaciones de **países sin TLC**: **1.463 fracciones**, tasas del **5% al 50%**. **Sin fecha de caducidad** |
| **1-ene-2026** | Entra en vigor |
| **23-abr-2026** | Ampliación con **185 fracciones** más, del 5% al 35% |

**Alcance:** aplica al régimen simplificado de mensajería y paquetería, a pedidos por debajo de
US$2.500 (~46.850 MXN) que entran sin intermediación comercial formal. China no tiene TLC con
México, así que entra de lleno.

## El impacto en el modelo, con números

Producto de US$8 FOB + US$5,50 de flete = US$13,50 puesto.

```
Valor declarado                    13,50
Arancel global 33,5%                4,52
Flete de última milla (Dropi MX)    8,74
Comisión de plataforma (5%)         1,91
                                  ──────
Costo por pedido                   28,67
```

Con ticket de 699 MXN (US$38,20) el margen bruto quedaría en **US$9,53**. Pero falta el golpe real:
**el tiempo de tránsito**.

## El problema que no es el arancel

Enviar desde China a México toma 8-15 días por aire. Con **contraentrega**, eso significa que el
cliente tiene dos semanas para arrepentirse **sin ningún costo** — simplemente no abre la puerta. La
tasa de entrega se derrumba del 78% (con stock local y confirmación) al ~50%.

Modelado completo:

| Variante | Ticket | Entrega | Costo | Margen bruto | CAC | **Utilidad** |
|---|---|---|---|---|---|---|
| MX stock local, confirmado | $38,20 | 78% | $28,03 | $10,16 | $6,05 | **+$4,11** |
| MX stock local + bundle | $60,05 | 78% | $33,63 | $26,43 | $6,05 | **+$20,38** |
| **MX ← China directo** | $38,20 | 50% | $46,86 | −$8,67 | $9,44 | **−$18,11** |

**El envío directo desde China a México pierde US$18 por venta.** No es un margen apretado: es un
negocio que paga por vender.

## Lo que sí funciona en México

1. **Stock local vía plataforma COD** (Dropi MX, Mastershop, Aliddy). Cero inventario, cero arancel
   para ti, entrega en 2-5 días. Ver `132`, `128`.
2. **Proveedor mayorista mexicano.** Margen mejor que la plataforma, exige encontrarlo y negociar.
3. **Importación en lote + 3PL mexicano.** Pagas el 33,5% una vez sobre un contenedor, no sobre cada
   paquete. Exige capital. Ver `136`.
4. **Prepago con stock local.** La combinación más rentable con capital chico: la plata vuelve en 3
   días en vez de 12. Ver `32`.

## El cálculo que decide

```
Si vendes 1 unidad por envío desde China:
    arancel pagado = 33,5% × 13,50 = 4,52 por unidad

Si importas 300 unidades en un lote:
    arancel pagado = 33,5% × (300 × 8,00 + flete consolidado)
    por unidad ≈ 33,5% × 9,50 = 3,18 por unidad
    + ahorras el flete internacional individual (5,50 → ~1,50)
```

Importar en lote no elimina el arancel: **elimina el flete individual y el tiempo de tránsito**, que
es lo que de verdad estaba matando el negocio.

## Errores frecuentes

| Error | Realidad |
|---|---|
| "El 33,5% vencía en abril de 2026" | Esa fecha correspondía a una medida anterior. El decreto de dic-2025 **no tiene caducidad** y en abr-2026 se **amplió** |
| "Mando por correo normal y no revisan" | El régimen simplificado aplica igual; el control es sobre el courier |
| "Hago dropshipping de AliExpress a México" | Pierdes ~$18 por venta. Los números están arriba |
| "Como es poco valor, no paga" | México no tiene un de minimis que te salve en este régimen |

## Lo bueno de México (que compensa el arancel)

- **77,2 millones de compradores digitales**, +19,2% anual, 8º del mundo en ecommerce.
- CPM barato: **US$4,50** base, US$6,75 en Q4.
- **La mejor temporada de LatAm**: Buen Fin, Black Friday, Cyber Monday, Guadalupe-Reyes, aguinaldo
  y Día de Reyes. 55 días seguidos de intención de compra. Ver `36`.
- Meses sin intereses: mecanismo de compra dominante, sube la conversión ~36%. Ver `195`.
- Infraestructura COD madura con 4 transportadoras integradas.

## Relacionados
`13` mapa aduanero · `20` playbook México · `128` proveedores en México · `132` Dropi ·
`153` paqueterías de México · `195` meses sin intereses · `36` calendario mexicano
