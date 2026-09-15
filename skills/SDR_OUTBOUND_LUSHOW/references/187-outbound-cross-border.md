# 187 — Outbound cross-border (vender desde LatAm hacia USA/Europa)

Este es uno de los movimientos de negocio más potentes que puede hacer Lushows: **operar el outbound desde LatAm y venderle a USA o Europa.** La razón es puro arbitraje — pagas costos latinos y cobras precios de primer mundo. Un SDR o un servicio de outbound que en USA cuesta $5.000–7.000 USD/mes, desde Colombia o México se opera por una fracción, mientras el cliente gringo/europeo paga en dólares o euros por reuniones agendadas. Este módulo es sobre cómo montar esa operación cross-border sin que el prospecto note (ni le importe) que estás al sur, y cómo capturar el arbitraje limpio. Es la base económica de vender outbound-as-a-service internacional (ver `95`).

## El principio: arbitraje de costos, entrega de primer mundo

El arbitraje funciona porque **el outbound es 100% remoto y digital**: un email, una llamada por VoIP, un mensaje de LinkedIn no tienen nacionalidad si están bien hechos. El cliente en USA paga por reuniones calificadas en su pipeline; no le importa desde qué país se generaron mientras la calidad sea de su nivel. Tu ventaja es la estructura de costos (salarios, herramientas, vida en LatAm) contra ingresos en moneda dura. La trampa es creer que "barato" significa "descuidado": lo que rompe el arbitraje es que se note un acento no nativo, un inglés calcado, una zona horaria mal manejada o datos malos. La calidad es la condición para cobrar precio de primer mundo.

## Los números del arbitraje (por qué vale la pena)

| Concepto | En USA | Desde LatAm |
|---|---|---|
| Costo de un SDR full-time | $4.000–7.000 USD/mes | $800–2.000 USD/mes |
| Lo que cobras al cliente por reunión | $150–500+ USD/reunión | igual (cobras en USD/EUR) |
| Retainer de outbound-as-a-service | $2.000–8.000 USD/mes | igual (cobras precio USA) |
| Herramientas (Apollo, Instantly, Clay) | mismo costo global | mismo costo global |

El margen bruto de la operación cross-border bien montada es alto porque los ingresos son en dólares y buena parte de los costos en moneda local. Para modelar los números exactos de tu operación (márgenes, punto de equilibrio, cuánto cobrar) → `Matematicas_lushows` para el cálculo y `economist_lushows` para el modelo de negocio y pricing.

## Cómo montar la operación sin que se note (ni importe)

1. **Infraestructura con dominio del mercado destino.** Compra dominios `.com` (o `.co.uk`, `.es` según destino), no `.com.co`. Configura SPF/DKIM/DMARC (ver `42`) y warmup (ver `43`) exactamente como para USA/Europa. El correo debe verse local.
2. **Inglés/idioma nativo en el mensaje.** Aquí no hay atajo: las plantillas deben sonar escritas por un nativo (ver `183`, `185`). Contrata un redactor nativo o usa IA con revisión nativa para las plantillas maestras. Un solo "I write you to present…" y perdiste el arbitraje.
3. **VoIP con número local del destino.** Para llamadas, usa un número local (Aircall, JustCall, OpenPhone dan números USA/UK): el prospecto ve un número de su país, no una llamada internacional que nadie contesta. Para la voz en llamadas en vivo, quien llame debe tener inglés fluido y sin acento marcado — o enfócate en canales escritos (email/LinkedIn) donde el acento no aplica.
4. **Zona horaria alineada.** Colombia/Perú comparten huso con USA Este — enorme ventaja para responder en tiempo real (ver `186`). Para Europa, programa email en tu mañana temprano y agenda llamadas madrugando.
5. **Presencia legítima.** LinkedIn y web con presencia profesional coherente. No hace falta mentir sobre dónde estás — muchas empresas operan globalmente — pero sí verse serio y del nivel del mercado.
6. **Cumplimiento del mercado destino, no del tuyo.** Le vendes a USA → cumples CAN-SPAM (ver `183`, `49`); a Europa → GDPR con base legal (ver `184`). La ley que aplica es la del prospecto, no la tuya. Este es el punto que más gente ignora y el que más caro sale.

## El modelo de servicio cross-border

La forma clásica de capturar esto es **outbound-as-a-service**: agencias latinas que generan reuniones para empresas de USA/Europa (ver `95`). Modelos de cobro:
- **Retainer mensual** ($2.000–6.000 USD): corres la máquina de outbound del cliente.
- **Pago por reunión** ($150–500 USD/reunión calificada): cobras por resultado.
- **Híbrido**: retainer base + bono por reunión.

El cliente externaliza su generación de pipeline; tú aportas la máquina (listas, deliverability, cadencias, ops de esta skill). El **cierre de esas reuniones** lo hace el AE del cliente, o si tú también cierras, ese oficio de venta consultiva vive en `ventas_lushows`.

## Ejemplo: operación Colombia → USA (SaaS B2B)

```
- Dominios: outreach-{marca}.com (.com), calentados 3-4 semanas
- Sequencer: Instantly, envío por zona horaria del contacto (ET/PT)
- Listas: Apollo + Clay, ICP USA verificado con NeverBounce
- Mensaje: cold email en inglés nativo (revisado por redactor US)
- Llamadas: número US vía Aircall, en ventana ET (mismo huso que Bogotá)
- Cumplimiento: CAN-SPAM (dirección física + opt-out)
- Cobro al cliente: $3.500 USD/mes retainer + $200/reunión calificada
- Costo operación: ~$1.500 USD/mes (SDR + tools)
```

## Errores comunes (qué NO hacer)

- Inglés/idioma no nativo en el mensaje: destruye el arbitraje al primer correo (ver `185`).
- Dominios locales (.com.co) para vender a USA: se ven fuera de lugar, bajan confianza.
- Cumplir la ley de TU país en vez de la del destino: aplica la del prospecto (GDPR/CAN-SPAM; ver `49`).
- Llamar con número internacional: nadie contesta; usa VoIP local.
- Competir solo por barato descuidando calidad: rompe el arbitraje; el cliente paga precio USA por calidad USA.

## Siguiente paso

Elige un mercado destino (USA es el más accesible desde LatAm por huso e idioma comercial). Monta infra con dominio `.com` (ver `41`, `42`, `43`), escribe plantillas en idioma nativo (`183`/`184`/`185`), consigue VoIP con número local, y cumple la ley del destino (`49`). Modela los números con `Matematicas_lushows` y el pricing/negocio con `economist_lushows`. Para estructurar el servicio ver `95`; para armar el equipo distribuido ver `188`. La venta/cierre → `ventas_lushows`.
