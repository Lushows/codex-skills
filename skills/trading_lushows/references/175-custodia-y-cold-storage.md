# 175 — Custodia y cold storage: dónde vive tu cripto

## La frase que gobierna este módulo

**"Not your keys, not your coins"** — si no tienes las llaves, las monedas no son tuyas.
Cuando tu cripto está en un exchange, técnicamente el exchange la custodia y tú tienes una
*promesa* de que te la devolverá. Casi siempre cumple. Hasta que no (módulo 188).

## Definiciones

- **Wallet (billetera):** software o aparato que guarda las **llaves privadas** — la contraseña
  criptográfica que controla tus monedas. Quien tiene la llave, tiene la plata.
- **Hot wallet (caliente):** conectada a internet (app, extensión, el propio exchange).
  Cómoda y rápida, pero hackeable.
- **Cold wallet (fría):** las llaves viven FUERA de internet. Máxima seguridad, menos comodidad.
- **Hardware wallet:** aparato físico (Ledger, Trezor) que firma transacciones sin exponer la
  llave. El estándar razonable de cold storage para una persona.
- **Frase semilla (seed phrase):** las 12-24 palabras que regeneran tu wallet. Es LA llave
  maestra: quien la lea, te vacía. Se escribe en papel/metal, jamás en foto, nube o chat.

## La escalera de custodia

| Dónde | Seguridad | Comodidad | Para qué |
|---|---|---|---|
| Exchange | La del exchange (ajena) | Máxima | Capital operativo del bot |
| Hot wallet propia | Media | Alta | Montos pequeños, movimientos |
| Hardware wallet | Alta | Media | Ahorros / ganancias retiradas |

## La regla práctica

**En el exchange solo lo que el bot necesita para operar.** Ganancias acumuladas y capital que
no está en juego → se retiran a hardware wallet (o al banco, en pesos). Es el mismo principio
del efectivo: en la billetera lo del día, en la caja fuerte el resto.

Costo de un hardware wallet: el equivalente a una cena — contra el riesgo de perderlo todo,
es el seguro más barato del mundo cripto. Comprarlo SIEMPRE nuevo y del fabricante oficial
(uno usado puede venir con la semilla pre-copiada por el vendedor: estafa clásica).

## El balance operación vs seguridad para un bot

El dilema: el bot necesita fondos EN el exchange para ejecutar (una cold wallet no puede
firmar órdenes automáticas). No hay forma de tener 100% seguridad y 100% operación. La
respuesta no es elegir un extremo sino **dosificar**: exposición al exchange = capital
operativo chico; todo excedente, fuera. Barrido periódico (ej. mensual) de ganancias.

## Cómo aplica al AGENTE TRADING

- Hoy (paper/testnet): no hay custodia real que proteger — pero es el momento de que Luis
  practique el flujo: comprar hardware wallet, generar semilla, guardarla bien, hacer un
  retiro de prueba con monto mínimo.
- En live: regla escrita en el runbook — exchange = solo capital operativo; barrido de
  ganancias a custodia fría o a pesos según decida Luis con contador_lushows.
