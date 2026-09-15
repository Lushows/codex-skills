# 116 — Opciones en cripto (lo básico honesto)

## Qué es una opción

Una **opción** es un contrato que da el **derecho (no la obligación)** de comprar o vender
un activo a un precio fijado (**strike**) antes de una fecha (**vencimiento**), a cambio de
pagar una **prima** hoy.

| Tipo | Derecho que compras | La apuesta implícita |
|---|---|---|
| **Call** | Comprar al strike | "Va a subir por encima del strike antes del vencimiento" |
| **Put** | Vender al strike | "Va a caer por debajo del strike antes del vencimiento" |

Analogía: la prima de una opción es como un seguro. Un put es un seguro contra caídas:
pagas la prima; si no pasa nada, la pierdes; si el mercado se derrumba, el seguro paga.

**Comprar** opciones tiene pérdida máxima conocida (la prima). **Vender** opciones cobra
la prima pero asume pérdidas potencialmente enormes — es donde más retail se quiebra.

## Volatilidad implícita: el precio del miedo

El precio de una opción no depende solo de hacia dónde va el activo, sino de **cuánto se
espera que se mueva**: la **volatilidad implícita (IV)**. Es la volatilidad que el mercado
"cobra" en la prima.

- IV alta → opciones caras (seguro caro porque hay miedo/euforia).
- IV baja → opciones baratas (calma; a veces, calma antes de tormenta).

La trampa clásica: comprar calls en plena euforia. Aunque aciertes la dirección, pagaste
la IV inflada — el activo sube y la opción apenas gana (o pierde, si la IV se desinfla).
En opciones se puede **acertar la dirección y perder plata**. Eso las hace otro juego.

## Por qué NO para nosotros (aún)

1. **Complejidad real**: una posición de opciones vive en 3+ dimensiones (dirección, tiempo,
   volatilidad — las "griegas"). El sistema actual maneja una: dirección con riesgo fijo.
   Sumar dimensiones sin dominarlas es sumar formas de perder.
2. **Liquidez concentrada y flaca**: las opciones cripto líquidas son de BTC y ETH en pocas
   plataformas (Deribit ha concentrado históricamente el volumen; verificar al día). Fuera
   de strikes populares, los spreads son anchos y castigan cada entrada/salida.
3. **La decadencia del tiempo (theta)**: una opción comprada pierde valor cada día que pasa
   sin movimiento. El swing de días/semanas paga ese peaje constantemente.
4. **Sin datos propios**: el bot no tiene ni un trade de opciones en su memoria. Empezar en
   real sería violar el ciclo paper → testnet → live (ver `00`).

## Cómo aplica al AGENTE TRADING

- **No operamos opciones.** Punto, por ahora. El edge del bot está en swing spot y la
  prioridad del backlog (SHORT, tercer par) está antes en la fila.
- Uso legítimo futuro como **dato**: la IV de BTC/ETH es un termómetro de miedo del mercado
  que podría alimentar el análisis de régimen — leerla no exige operarla.
- Único caso que algún día podría justificarlas: comprar puts como **cobertura** de una
  posición spot grande (ver `117`). Eso sería con capital real, tamaño mínimo y tras
  estudiar el costo de la prima — nunca "para apalancar ganancias".
