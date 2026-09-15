# 178 — Contratos y términos de exchanges: qué firmaste sin leer

## El contrato que todos aceptan y nadie lee

Al crear la cuenta aceptaste los **Términos de Servicio**: un contrato real, redactado por los
abogados del exchange, para proteger al exchange. Conocer sus cláusulas típicas no es
paranoia — es saber en qué juego estás.

## Las cláusulas que importan (patrón general de la industria)

| Cláusula típica | Qué significa para ti |
|---|---|
| **Custodia** | Tus criptos las guarda el exchange; tienes un derecho de reclamo, no la llave (módulo 175) |
| **Congelamiento** | Pueden congelar tu cuenta por sospecha AML, orden de autoridad o revisión interna — a su criterio, sin plazo garantizado |
| **Suspensión de servicio** | Pueden pausar retiros o trading "por mantenimiento" o "condiciones de mercado" (pasa justo en los peores momentos) |
| **Cambios unilaterales** | Los términos cambian cuando ellos quieran; seguir usando la cuenta = aceptar |
| **Jurisdicción** | Un pleito se resuelve donde diga el contrato (a veces arbitraje en otra jurisdicción) — para un colombiano con capital chico, pelear es más caro que perder |
| **Sin seguro estatal** | No hay Fogafín ni FDIC; si quiebran, entras a la fila de acreedores |
| **Riesgo de mercado tuyo** | Fallas, liquidaciones raras, velas anómalas: el exchange se exime de casi todo |

**Definición — jurisdicción:** el país/tribunal donde legalmente se resuelven disputas. Si tu
contrato dice "arbitraje en Singapur", eso vale más que tu deseo de reclamar en Bogotá.

## Casos reales de fondos congelados (el patrón)

- **Quiebras** (FTX, Celsius, Mt. Gox): retiros pausados "temporalmente" → nunca reabrieron →
  años de proceso concursal para recuperar una fracción.
- **Congelamientos individuales** por revisión AML: usuarios legítimos con cuentas bloqueadas
  semanas/meses por P2P con contraparte sucia o incoherencias de origen de fondos (módulo 171).
- **Pausas de retiro en pánico de mercado**: cuando más quieres salir, la puerta se angosta.

La lección común: **el acceso a tu dinero en un exchange es un privilegio condicional**, no un
derecho absoluto e inmediato.

## La mitigación honesta (no hay cláusula que te salve, hay hábitos)

1. **Poco capital en exchange** — la mitigación #1, la única que depende 100% de ti. Un
   congelamiento del 10% de tu patrimonio es un susto; del 90% es una catástrofe.
2. Operar limpio y coherente (módulo 171) para no dar motivos.
3. Barrido periódico de excedentes a custodia propia o a pesos (módulo 175).
4. Exportar el historial de trades con frecuencia: si pierdes acceso, no pierdes tu contabilidad.
5. Leer al menos las secciones de retiros/congelamiento cuando cambien los términos.

## Cómo aplica al AGENTE TRADING

- El bot está diseñado para capital chico: eso convierte el peor caso contractual (cuenta
  congelada, exchange quebrado) en una pérdida acotada, no en ruina.
- Runbook del go-live: monto máximo en exchange definido por escrito + export automático o
  semanal del historial + revisión de términos antes de fondear.
