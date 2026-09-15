# 171 — KYC y AML: por qué el exchange te pide la cédula

## Definiciones primero

- **KYC** (*Know Your Customer*, "conoce a tu cliente"): el proceso donde el exchange verifica
  quién eres — cédula, selfie, a veces comprobante de domicilio.
- **AML** (*Anti-Money Laundering*, antilavado de dinero): las reglas globales para evitar que
  el dinero de delitos se "limpie" pasando por plataformas financieras.

No es capricho del exchange: es requisito para que ellos puedan operar con bancos y no ser
cerrados por reguladores. Un exchange que NO pide KYC es una bandera roja, no una ventaja.

## Niveles de verificación (patrón típico)

| Nivel | Qué piden | Qué desbloquea |
|---|---|---|
| Básico | Email + teléfono | Casi nada o límites mínimos |
| Intermedio | Cédula + selfie | Depósitos/retiros normales |
| Avanzado | Comprobante de domicilio, origen de fondos | Límites altos |

Los montos exactos de cada nivel cambian por exchange y por país — verificar en la
plataforma al día. Para un sistema de capital chico, el nivel intermedio suele bastar.

## Banderas rojas que CONGELAN cuentas

El sistema antilavado del exchange es automático y desconfiado. Disparadores típicos:

1. **Entradas y salidas rápidas** de dinero sin operar ("pass-through": entra plata, sale plata).
2. **Terceros**: recibir depósitos de cuentas bancarias que no están a tu nombre, o P2P con
   contrapartes sucias (si le compras cripto a alguien que lavaba dinero, tu cuenta hereda la sospecha).
3. **Incoherencia**: declaraste ingresos modestos y mueves montos grandes.
4. **VPN / país falso**: aparentar operar desde otro país.
5. **Muchas cuentas** de la misma persona para evadir límites.

Un congelamiento puede durar semanas o meses mientras "revisan". Sin apelación rápida.

## Cómo operar limpio (la lista de Luis)

- Una sola cuenta, a tu nombre, verificada completa desde el día 1.
- Depósitos SOLO desde tu propia cuenta bancaria. Nada de terceros, nada de P2P con desconocidos.
- Coherencia: el capital que entra debe cuadrar con lo que declaras (módulo 172).
- Guardar comprobantes de cada depósito/retiro (pantallazo + extracto bancario).
- No prestar la cuenta a nadie, jamás, ni a familia. La cuenta congelada es TU problema.

## Cómo aplica al AGENTE TRADING

- En paper trading no hay KYC (no hay dinero). En testnet tampoco.
- Antes del go-live: cuenta verificada nivel intermedio+, fondeada desde el banco de Luis,
  con papel de cada movimiento. El bot solo opera; el dinero entra y sale limpio y documentado.
- Regla del sistema: **poco capital en exchange** (módulo 178) — así un congelamiento
  inesperado duele poco.
