# El múltiplo mínimo de margen (la regla de 3x murió)

## Qué es el múltiplo

```
MÚLTIPLO = TICKET ÷ COSTO PUESTO EN BODEGA
```

**Costo puesto en bodega** = precio del producto + flete internacional prorrateado + arancel + IVA
de importación + manejo. NO es el precio que ves en AliExpress. Confundir los dos es el error #1.

## Por qué murió el 3x

La regla de 3x nació cuando el CPM en Meta estaba en USD 4-6 en EE.UU. y la competencia era una
décima parte. En 2026 el CPM de EE.UU. está en 23,00 USD base y sube 20-50% en Q4. El múltiplo
necesario no lo decide una tradición: lo decide la aritmética de tu CVR y tu CPM.

```
CPA = CPM ÷ (1.000 × CTR × CVR)
```

Con CPM 4,50 (México), CTR 2,2% y CVR 3,0% prepago:
CPA = 4,50 ÷ (1.000 × 0,022 × 0,030) = **USD 6,82 por venta**

Con CPM 23,00 (EE.UU.), CTR 1,5% y CVR 2,0%:
CPA = 23,00 ÷ (1.000 × 0,015 × 0,020) = **USD 76,67 por venta**

Ese salto de 11x es el que destruye la regla universal de 3x.

## Tabla de múltiplos mínimos para dejar 20% neto (Q4-2026)

| País | Conservador (CTR 1,5% / CVR 2,0%) | Creativo bueno (2,2% / 3,0%) | Ganador real (3,0% / 4,0%) |
|---|---|---|---|
| **Perú** | 3,19x | 2,62x | 2,39x |
| **Colombia** | 3,39x | 2,77x | 2,52x |
| **España** | 4,33x | 2,72x | 2,11x |
| **Chile** | 3,68x | 2,87x | 2,55x |
| **México** | 3,74x | 3,00x | 2,70x |
| **EE.UU.** | 14,98x | 7,94x | 5,31x |

Lectura correcta de esta tabla: **empieza siempre por la columna conservadora.** Tú no sabes si tu
creativo es bueno hasta que tienes datos. Planear con la columna del "ganador real" es planear con
un resultado que todavía no existe.

## Los escenarios de calidad de creativo

| Escenario | CTR | CVR prepago | CVR COD |
|---|---|---|---|
| Conservador | 1,5% | 2,0% | 4,5% |
| Creativo bueno | 2,2% | 3,0% | 6,5% |
| Ganador real | 3,0% | 4,0% | 8,5% |

El CVR de COD es 2-2,2x el de prepago porque no hay fricción de pago — pero después te come el
30-45% en pedidos no cobrados. El múltiplo COD debe calcularse sobre pedidos **cobrados**, no
generados. Ver `11`.

## Cómo calcular TU múltiplo (no el de la tabla)

Paso a paso, con números propios:

```
1. Techo de CAC = Ticket − costo bodega − envío − pasarela − fallidos − objetivo de utilidad
2. CPA estimado = CPM ÷ (1.000 × CTR × CVR)   ← usa el escenario conservador
3. ¿Techo de CAC ≥ CPA? → el producto pasa
4. Si no pasa: sube ticket, baja costo, o descarta
```

Ejemplo México, bundle del proyecto activo:

| Renglón | MXN |
|---|---|
| Ticket | 1.099 |
| Costo puesto en bodega (stock local) | 294 |
| Envío nacional | 120 |
| Pasarela 3,6% + IVA sobre comisión | 46 |
| Devoluciones/fallidos 5% | 55 |
| Utilidad objetivo 20% del ticket | 220 |
| **Techo de CAC** | **364 MXN ≈ USD 19** |

CPA conservador México = 4,50 ÷ (1.000 × 0,015 × 0,020) = USD 15,00 → **pasa con holgura de 21%**.
CPA conservador si el CPM sube 50% en Buen Fin = USD 22,50 → **NO pasa**. Ahí necesitas el bundle
más alto o el MSI para subir el ticket promedio. Ver `195` y `218`.

## Los tres botones para arreglar un múltiplo insuficiente

| Botón | Efecto | Riesgo |
|---|---|---|
| **Subir el ticket** (bundle, 2x1, upsell) | Directo y rápido | CVR cae si el precio pasa el umbral de impulso (`46`) |
| **Bajar el costo** (negociar, MOQ, stock local) | Sostenible | Requiere capital adelantado |
| **Subir el CVR** (página, prueba social, MSI) | El de mejor retorno | Toma semanas de iteración |

El botón que NO existe: "conseguir CPM barato". Eso no lo controlas tú; lo controla la subasta.

## Errores de cálculo frecuentes

| Error | Cuánto distorsiona |
|---|---|
| Usar precio AliExpress sin flete ni arancel | Infla el múltiplo 25-40% |
| Olvidar IVA sobre la comisión de pasarela | 0,5-0,8% del ticket |
| Ignorar el costo de los pedidos fallidos | En COD, 20-35% del margen |
| Calcular el múltiplo sobre ticket sin IVA en un país donde el IVA se cobra al cliente | Sobreestima el ticket real |
| Usar el CPM de julio para planear diciembre | Subestima el CPA 20-80% |

## EE.UU. y por qué casi nadie debería empezar ahí

Con de minimis eliminado y ~54% arancel a origen chino, más CPM de 23,00 USD, el múltiplo
conservador es **14,98x**. Eso significa que un producto de USD 4 puesto en bodega necesita
venderse a USD 60 para dejar 20%. Ese producto ya no es un producto: es una marca con una promesa.
Ver `14` y `23`.

## Regla práctica final

> Si tu múltiplo con costo puesto en bodega está por debajo de la columna **conservadora** de tu
> país, no testees. No es cuestión de creativo. Es aritmética.

Y si está justo en el límite, recuerda: en Q4 el CPM sube 20-50%; en Black Friday 50-80%. El límite
de septiembre es pérdida en noviembre.

## Relacionados
`11` techo de CAC · `12` comparador de países · `40` qué es un ganador · `41` criterios ·
`46` umbral de impulso · `48` peso y flete · `195` MSI · `218` bundle · `233` cuántos tiros
