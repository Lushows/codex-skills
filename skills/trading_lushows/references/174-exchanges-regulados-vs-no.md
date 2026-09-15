# 174 — Exchanges confiables vs de riesgo: cómo elegir dónde opera el bot

## Por qué esto importa más que el "mejor indicador"

Puedes tener el mejor sistema del mundo y perderlo TODO porque el exchange quebró, congeló o
desapareció (FTX, Mt. Gox — módulo 188). Elegir plataforma es una decisión de riesgo tan
importante como el sizing.

## Criterios de confiabilidad (checklist)

| Criterio | Qué mirar | Por qué |
|---|---|---|
| **Licencias y registros** | Registrado ante reguladores serios (EE.UU., UE, etc.) y cumpliendo lo que Colombia exija al día | Un regulado tiene más que perder si roba |
| **Proof of reserves** | Publica pruebas auditables de que tiene las criptos de los usuarios | FTX "tenía" el dinero... prestado a sí mismo |
| **Historia** | Años operando, cómo manejó crisis pasadas (hackeos, caídas de mercado) | El comportamiento pasado bajo estrés predice |
| **Liquidez y volumen** | Volumen real alto en BTC/ETH | Volumen falso = precios falsos = ejecuciones malas |
| **Seguridad** | 2FA obligatorio, whitelist de retiros, fondo de seguro | Capas que frenan al ladrón |
| **API estable** | Documentada, con testnet | El bot vive de la API |

**Definición — proof of reserves:** demostración pública (idealmente auditada) de que el
exchange realmente custodia las criptos que dice tener de sus clientes, y no las prestó.

## Binance en Colombia

- A la fecha de este módulo, Binance opera con usuarios colombianos, con KYC completo, y es
  el exchange de mayor volumen global — buena liquidez para BTC/ETH y API madura (la que usa
  el AGENTE TRADING, incluida su testnet).
- No está exento de riesgo: ha tenido fricciones regulatorias en varios países y pagó multas
  grandes en EE.UU. Ser el más grande no lo hace infalible.
- Estado regulatorio en Colombia: **evoluciona — verificar al día** antes del go-live.

## Señales de alarma de un exchange (huir)

1. Promete **rendimientos garantizados** ("gana 2% diario") — eso no es un exchange, es un esquema.
2. **No pide KYC** ni tiene entidad legal identificable.
3. **Retiros lentos o con excusas** reportados por usuarios (buscar antes de depositar).
4. Token propio que sostiene su balance (el pecado de FTX).
5. Equipo anónimo, sede difusa, soporte inexistente.
6. Te llegó por **DM de un desconocido** o "asesor" que te lo recomienda con urgencia.

## Cómo aplica al AGENTE TRADING

- Etapa actual: **testnet de Binance** — tubería real, dinero falso, riesgo cero.
- Go-live: exchange elegido por esta checklist, y aún así, **solo el capital operativo del mes**
  en la plataforma (módulos 175 y 178). La confianza en un exchange nunca es total: se
  administra, no se regala.
