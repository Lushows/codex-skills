# 54 — Lead generation (instant forms)

Lee este módulo cuando vendas algo que NO se compra de impulso (servicios, high-ticket, B2B, cursos, agendamiento), cuando no haya TikTok Shop en el país, o cuando un cliente diga "yo necesito que me dejen sus datos para llamarlos". Lead gen es el camino cuando la venta necesita conversación. Pero ojo: un formulario mal hecho te llena de basura. El arte no es **llenar** formularios — es **filtrar**. El frame manda: TikTok es **descubrimiento** (ver 00), el lead llega frío; tu trabajo es entregar uno tibio, calificado y rastreable, no un número cualquiera.

## Qué son los instant forms (y la trampa del lead barato)

Un **instant form** (formulario instantáneo, también *Lead Gen* / *Instant Form* en TikTok) es un formulario que se abre **dentro de TikTok**, sin salir de la app. El usuario toca el ad, se despliega el form con datos ya prellenados (nombre, teléfono que TikTok ya conoce), envía, y listo: tienes el lead sin que cargue ninguna web. TikTok ofrece dos tipos de plantilla:

| Tipo de form | Fricción | Resultado |
|---|---|---|
| **Instant Form (default)** | Baja: confirma datos prellenados | Mucho volumen, calidad baja |
| **"More info" / con preguntas** | Alta intencional: escribe, responde | Menos volumen, mejor calidad |

La trampa: como el instant es tan fácil de llenar, TikTok te trae **leads baratos pero curiosos**. Un CPL (Cost Per Lead, costo por lead) de $2.000 COP suena increíble hasta que llamas y nadie contesta o nadie tenía intención real. **Lead barato ≠ lead bueno.** Lo que importa no es el CPL — es el **costo por lead calificado** (CPLC): cuánto te cuesta un lead que de verdad puede y quiere comprar (ver 58).

| Métrica | Qué mide | Trampa |
|---|---|---|
| CPL | Costo por formulario enviado | Premia volumen basura |
| **CPLC** | Costo por lead **calificado** | Lo que de verdad importa |
| Tasa de contacto | % de leads con los que logras hablar | Cae si pides datos falsos o tardas |
| Tasa de cierre | % de leads que compran | El número final que paga las cuentas |
| CAC | Costo de adquirir un cliente | El que valida la unit economics |

## Cómo hacer un formulario que FILTRA, no solo llena

El objetivo es repeler al curioso y dejar pasar al comprador. Tácticas, de más a menos efectivas:

1. **Form tipo "More info" en vez de "Instant".** TikTok ofrece formularios de mayor fricción intencional — el usuario debe escribir, no solo confirmar. Filtra impulso.
2. **Pregunta de calificación.** Una pregunta que solo el lead bueno responde bien: presupuesto, urgencia, tipo de negocio, "¿ya tienes restaurante operando?". El curioso se cae ahí (ver 58).
3. **Expectativa clara en el creativo.** Si el video dice "agenda una asesoría de 30 min", el que llena ya sabe a qué va. El que no quiere asesoría, no llena (ver 48 congruencia).
4. **Campos mínimos pero suficientes.** Nombre, WhatsApp y 1 pregunta de calificación. Ni más (espanta) ni menos (basura).
5. **Pantalla de confirmación con próximo paso.** "Te escribimos por WhatsApp en minutos" — fija expectativa y reduce el lead que ya se olvidó.

### Plantilla de form que filtra (servicio / high-ticket)

```
Titular: Asesoría de costos para tu restaurante
Descripción: Solo si ya tienes el negocio operando. Cupos limitados.
Campos:
 - Nombre
 - WhatsApp
 - ¿Tu restaurante ya está operando?  [Sí / No, voy a abrir]
 - ¿Cuántas sedes tienes?              [1 / 2-3 / 4+]
Botón: Quiero mi asesoría
Confirmación: "Listo. Te escribimos por WhatsApp en los próximos minutos."
```

Optimiza la campaña por **lead** (o por **lead calificado** si subes esa conversión vía Events API — ver 57), no por clic (ver 14). En TikTok el objetivo de campaña es **Lead Generation**, con entrega del lead vía instant form nativo o sitio externo.

## Integración a CRM/WhatsApp y la regla de los 5 minutos

Un lead que no contactas rápido se enfría y se va con quien lo llame primero. La regla, comprobada en performance LatAm:

> **Contactar al lead en menos de 5 minutos** multiplica la tasa de conexión. Después de 30 min, el lead ya está frío o ya habló con otro.

Cómo lograrlo, en orden:

1. **Conecta el instant form a tu CRM o WhatsApp** vía integración nativa (TikTok Lead Center / CRM partners) o webhook (Zapier/Make/API). El lead entra a TikTok → cae en tu sistema en segundos. No descargues CSV a mano: para cuando lo abres, el lead ya está frío.
2. **Dispara un mensaje automático de WhatsApp** apenas llega el lead: "Hola [nombre], vi que te interesó la asesoría de costos, ¿hablamos ahora?". Esto compra tiempo mientras un humano responde. En GastroLatam, este primer toque lo puede dar el bot (Luis) automáticamente.
3. **Asigna a alguien que cierre rápido.** La velocidad es ventaja competitiva. El handoff y el cierre son `ventas_lushows` (módulo 82, WhatsApp).

| Palanca | Qué resuelve | Cómo |
|---|---|---|
| Webhook a CRM/WhatsApp | Lead que cae en el vacío | Integración nativa o Zapier/Make |
| Auto-mensaje <5 min | Lead que se enfría | Bot / autoresponder |
| Asignación clara | Lead que nadie atiende | Dueño del lead definido |

Sin integración rápida, el mejor formulario del mundo te deja leads muertos. La velocidad de contacto vale más que cualquier optimización de puja.

## Medir lead calificado, no solo lead

No basta con generar leads — hay que enseñarle al algoritmo cuál es bueno:

1. **Define el lead calificado** en tu CRM (respondió bien la pregunta + contactable + intención).
2. **Sube esa conversión "lead calificado" de vuelta a TikTok** vía Events API (loop cerrado — ver 57). Sube "lead calificado", no "lead".
3. **Optimiza por ese evento profundo**, no por el formulario llenado.

Así el CPL sube pero el costo por **cliente** baja — que es lo único que paga las cuentas. Detalle completo de high-ticket en 58; medición en 57.

## Rutas a skills hermanas

- Cierre y calificación por WhatsApp → `ventas_lushows` (módulo 82).
- High-ticket / fricción intencional / agendamiento → 58.
- Subir lead calificado de vuelta a TikTok → 57.
- Validar CAC vs ticket → `economist_lushows`.
- Lead ads equivalentes en Meta → `facebook_ads_lushows`; lead/call ads en Google → `google_ads_lushows`.

## Errores comunes — blacklist

- **Mirar el CPL en vez del costo por lead calificado.** El lead barato suele ser basura; mide CPLC (ver 58).
- **Form "Instant" sin pregunta de calificación.** Te llena de curiosos; agrega fricción intencional ("More info").
- **No conectar el form a WhatsApp/CRM.** Los leads se enfrían sin contacto; integra con webhook, no CSV a mano.
- **Contactar al lead horas después.** Después de 5 min cae la conexión; automatiza el primer toque.
- **Creativo vago que no dice a qué se llena.** Atrae a todos y filtra a nadie; sé claro (ver 48 congruencia).
- **Optimizar por clic en vez de por lead.** Pagas tráfico, no leads; cambia el evento (ver 14).
- **Optimizar por "lead" en vez de "lead calificado".** El algoritmo trae quien llena forms; sube el evento profundo (ver 57).
- **Pasar el lead a ventas sin contexto.** Manda nombre + respuesta de calificación + de dónde vino (ver 55).
