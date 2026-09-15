# Cómo poner precio

## El precio no sale del costo

El error universal: costo × 3 = precio. Eso era una regla de 2019 y **murió** (ver `42`). El precio
correcto se fija así:

```
1. ¿Cuál es el múltiplo MÍNIMO que exige mi país y mi escenario?   → piso duro
2. ¿Cuánto vale el cambio que prometo?                             → techo de percepción
3. ¿Qué precios ancla ya conoce el cliente?                        → marco de referencia
4. ¿Qué precio deja holgura ≥2,0x sobre mi CAC real?               → veredicto
```

El precio final vive entre el piso y el techo. Si el piso está por encima del techo, el producto
no sirve: mátalo (`231`).

## Paso 1 — el piso: múltiplo mínimo por país (Q4-2026, para 20% neto)

| País | Conservador | Creativo bueno | Ganador real |
|---|---|---|---|
| Perú | 3,19x | 2,62x | 2,39x |
| Colombia | 3,39x | 2,77x | 2,52x |
| Chile | 3,68x | 2,87x | 2,55x |
| México | 3,74x | 3,00x | 2,70x |
| España | 4,33x | 2,72x | 2,11x |
| EE. UU. | 14,98x | 7,94x | 5,31x |

Multiplica sobre el **costo puesto en bodega**, no sobre el precio de AliExpress. Ver `28`, `42`.

Regla de operador: **planea con la columna conservadora**. Si el negocio solo funciona asumiendo
que serás un ganador real desde el primer día, no es un negocio, es una apuesta.

## Paso 2 — el techo: cuánto vale el cambio

| Pregunta | Efecto |
|---|---|
| ¿Cuánto le cuesta hoy el problema? (dinero, tiempo, vergüenza) | fija el máximo racional |
| ¿Qué alternativa paga hoy? (servicio, otro producto, aguantarse) | fija la comparación |
| ¿Con qué frecuencia le duele? | diario sostiene más precio que anual |

Ejemplo: si el cliente paga USD 25 por sesión de adiestramiento, un arnés de USD 35 que promete lo
mismo es barato. Si lo compara con "una correa", es carísimo. **Tú eliges contra qué se compara.**
Eso se hace con la promesa (`215`) y el posicionamiento, no con descuentos.

## Paso 3 — anclas de precio

| Ancla | Uso |
|---|---|
| Precio del producto suelto en marketplace | evítala: te obliga a competir por precio |
| Precio de la alternativa cara (servicio, marca) | úsala: te hace ver barato |
| Precio tachado propio ("antes 1.599") | legítimo solo si ese precio existió |
| Precio por uso ("sale a 3 pesos al día") | útil en ticket alto |

## Paso 4 — el veredicto: holgura

```
TECHO DE CAC = TICKET − TODOS LOS COSTOS POR PEDIDO COBRADO
HOLGURA      = techo de CAC ÷ CAC real
```

| Holgura | Lectura |
|---|---|
| < 1,0 | pierdes dinero en cada venta |
| 1,0 - 1,3 | trabajas gratis |
| 1,3 - 2,0 | frágil ante temporada (Q4 sube CPM 20-50%) |
| **2,0 - 3,0** | **sano: aquí se opera** |
| > 3,0 | subinvirtiendo: sube presupuesto o sube volumen |

El precio correcto es el más bajo que **todavía** deja holgura ≥2,0x en tu escenario conservador.
Ni uno más bajo (regalas margen), ni uno más alto por gusto (regalas volumen).

## Tabla de decisión rápida

| Situación | Acción |
|---|---|
| Piso > techo de percepción | producto muerto, siguiente (`231`) |
| Holgura 1,3-2,0 con producto suelto | arma bundle antes de bajar precio (`218`) |
| Holgura > 3,0 | sube presupuesto, no bajes precio |
| CPM sube en Q4 y holgura cae bajo 1,3 | sube precio o pausa (`238`) |
| Competencia bajó precio | no la sigas: cambia la oferta (`210`) |

## Precio y forma de pago

En México, meses sin intereses (MSI) suben la CVR de ~2,2% a ~3,0% (+36%) a cambio de ~1,5 puntos
más de comisión. Traducido:

| | Sin MSI | Con MSI |
|---|---|---|
| CVR | 2,2% | 3,0% |
| Comisión extra | — | ~1,5 pp del ticket |
| Efecto neto en pedidos cobrados | base | +36% |

Un punto y medio de comisión sobre USD 60 son ~USD 0,90. A cambio de 36% más pedidos. Es de las
decisiones más fáciles del negocio — **si tu ticket cruza el mínimo para MSI** (verificar con tu
pasarela; suele haber un piso). Otra razón para el bundle (`218`).

## Lo que NO debe determinar tu precio

| No | Por qué |
|---|---|
| Lo que cobra el competidor | no conoces su costo ni su CAC |
| Lo que "se siente justo" | tu intuición no paga el flete |
| Un número redondo bonito | ver `217` |
| El precio del proveedor × 3 | la regla de 3x murió (`42`) |

## Verificación obligatoria

Todo precio debe pasar por el modelo de `228` antes de publicarse, y por `223` para entender cada
renglón. Si el número no cuadra en Python, no cuadra en la vida real. Para auditar la aritmética
de un caso concreto, invoca `Matematicas_lushows`.

## Aplicación México dic-2026

| Escenario | Precio | Ticket USD | Techo CAC | CAC | Utilidad | Holgura |
|---|---|---|---|---|---|---|
| Suelto | 699 MXN | 38,20 | 15,28 | 12,65 | 2,63 | 1,21x |
| **Bundle + MSI** | **1.099 MXN** | **60,05** | **30,73** | **10,54** | **20,18** | **2,92x** |

El precio de 699 deja holgura de 1,21x: **trabajas gratis**. El de 1.099 deja 2,92x: eso es un
negocio. Mismo producto, misma bodega.

## Relacionados
`11` · `28` · `42` · `210` · `215` · `217` · `218` · `220` · `223` · `226` · `228` · `231` · `238`
