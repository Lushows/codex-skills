# 99 — Checklist final go-live (antes del primer peso real)

> Esta lista se recorre COMPLETA el día antes de fondear la cuenta. Un solo ítem en rojo =
> no hay go-live ese día. No es burocracia: cada ítem existe porque su ausencia cuesta plata.

## A. Técnica (el sistema funciona)

- [ ] ≥2 semanas en testnet.binance.vision sin incidentes sin explicar (módulo 90)
- [ ] Órdenes MARKET/LIMIT ejecutan y se registran correctas (cantidad, precio, fees)
- [ ] OCO: stop + target quedan VIVOS en el exchange en cada posición, verificado consultando
      al exchange (no confiando en el log propio)
- [ ] Reconciliación probada: reiniciar el bot con posición abierta → la recupera exacta;
      matar el proceso a mitad de orden → no duplica ni pierde nada (módulo 93)
- [ ] Kill switch manual probado: botón → deja de operar, posiciones protegidas (módulo 94)
- [ ] Kill switch automático probado: límite −3% diario disparado a propósito en testnet
- [ ] Modo pánico probado: un comando cierra todo en testnet
- [ ] Servicio migrado a Render Frankfurt, latencia verificada, trading NO geo-bloqueado
- [ ] Reloj sincronizado (offset con el servidor de Binance manejado en el cliente firmado)

## B. Evidencia (la estrategia merece dinero)

- [ ] Tabla del módulo 08 EN VERDE: ≥3 meses paper, PF > 1.3, DD < 15%, ≥30 trades,
      costo API ≤ $15/mes, uptime sano
- [ ] Sin trampas: la portería no se movió, no se contaron "semanas buenas" como evidencia
- [ ] Si hubo PIVOT, el período extra de paper post-pivote también está en verde

## C. Operativa (la cuenta está blindada)

- [ ] Cuenta Binance de Luis con KYC completo y 2FA por app (no SMS)
- [ ] API keys: SOLO lectura + spot trading. Withdrawal APAGADO — verificado mirando la
      configuración, no de memoria (módulo 92)
- [ ] IP whitelist activa con la IP del servicio de Render EU
- [ ] Keys en variables de entorno de Render; cero rastros en repo, logs o chats
- [ ] Alertas funcionando: cada orden real notifica a Luis de inmediato
- [ ] Log estructurado de cada orden (request/response) activo — también es la base de
      impuestos (módulo 98)
- [ ] Capital fondeado: $200-500, ni un peso más (módulo 96)

## D. Humana (Luis sabe qué hacer si X)

Luis puede responder estas preguntas SIN buscar en ningún lado:

- [ ] ¿Cómo activo el kill switch desde el celular? ¿Y el modo pánico?
- [ ] Si veo una posición sin stop en Binance, ¿qué hago primero? (protegerla → avisar → investigar)
- [ ] Si sospecho que una key se filtró, ¿cuál es el orden de pasos? (módulo 92: borrar key primero)
- [ ] Si Render se cae un fin de semana, ¿qué protege mis posiciones? (los OCO en el exchange)
- [ ] ¿Qué apruebo y qué NO toco en modo híbrido? (módulo 95: sí/no, jamás editar órdenes)
- [ ] ¿Cuándo se escala capital y cuándo NO? (módulo 96: hitos, nunca tras racha ganadora)

## El último paso

Con todo en verde: fondear, activar **modo híbrido** (no auto), y agendar la revisión del
primer mes. El go-live no es un evento — es el inicio del período de prueba más importante.

> Si al recorrer esta lista aparece la tentación de "ese ítem lo hacemos después del
> lanzamiento", releer módulo 08: el costo de esperar una semana es ~$0.
