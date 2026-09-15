# 24 — Conseguir teléfono, WhatsApp y social del contacto

El correo (`23`) es un canal; en LatAm no es el que más convierte. Aquí consigues los **otros datos de contacto** del decisor: teléfono, **WhatsApp** y sus **perfiles sociales** (LinkedIn, Instagram). Esto habilita el outbound multicanal (`48`, `61`) —email + LinkedIn + llamada + WhatsApp entrelazados— que agenda mucho más que cualquier canal solo. Y en PYMES/negocios locales de LatAm, el WhatsApp del negocio suele ser la vía #1 de respuesta.

## El principio: multicanal gana, y en LatAm el canal es WhatsApp

Un decisor que ignora tu correo te responde en LinkedIn; el que no ve LinkedIn contesta un WhatsApp. Tener 3 datos de contacto por persona multiplica tus chances de tocarla en el canal donde sí mira. En LatAm el patrón es **WhatsApp-first** (ver `08`, `180`): el negocio local vive en WhatsApp Business, no en el email. Por eso el teléfono que sacaste de Google Maps (`21`) muchas veces **ES** el WhatsApp — dato de altísimo valor.

Cuidado de fondo: el canal WhatsApp es potente pero **frágil y regulado**. Los números se banean si spameas; hay reglas de infraestructura y de opt-in que NO son este módulo (van en `47` infraestructura WhatsApp, `119` no quemar números, `59` frameworks de mensaje). Aquí solo **consigues el dato**; cómo enviarlo sin quemar el número y qué escribir están en esos módulos.

## Dónde sacar cada dato — paso a paso

| Dato | Fuentes principales | Nota |
|---|---|---|
| **Teléfono directo** | Apollo, Lusha, Cognism, RocketReach, ZoomInfo (ver `25`) | Lusha/Cognism destacan en móviles; Cognism verifica ("Diamond Data") |
| **Teléfono del negocio (PYME)** | Google Maps, web (Contacto), directorios, redes | Suele ser el WhatsApp |
| **WhatsApp** | Teléfono de Maps/web + verificar si tiene WA; bio de Instagram; botón "WhatsApp" en la web | Ver validación abajo |
| **LinkedIn** | Sales Navigator, Apollo (traen el `linkedin_url`) | Canal de social selling (`57`) |
| **Instagram / Facebook** | Búsqueda por nombre de negocio; bio con WA y correo | Clave en PYMES LatAm |

### Teléfono y móvil (B2B, decisor nominal)
Las bases de contacto (`25`) traen teléfono. Para **móvil directo** (el que sí contesta), **Lusha** y **Cognism** son las más fuertes en cobertura y verificación; Apollo y RocketReach traen teléfono pero con más ruido. Cobertura de móvil en LatAm: menor que en USA/UK; espera datos parciales. Usa waterfall (`130`) para subir el hit rate.

### WhatsApp (el canal LatAm)
1. Consigue el teléfono (arriba). En PYMES, el de Google Maps/web ya es el de atención = casi siempre WhatsApp.
2. **Valida que el número tenga WhatsApp** antes de guardarlo como tal:
   - Manual: abre `https://wa.me/57XXXXXXXXXX` (código de país + número, sin `+` ni ceros) — si abre chat, tiene WA.
   - A escala: herramientas de validación de números WA (algunas plataformas de envío y APIs lo hacen). No abuses.
3. Guarda en formato internacional E.164: `+57 300 000 0000`.

### Perfiles sociales
- **LinkedIn:** ya lo trae Sales Nav/Apollo. Es el canal de connection request + mensaje suave (`57`).
- **Instagram/Facebook:** en negocios locales la **bio** trae WhatsApp, correo y a veces el nombre del dueño. Búscalo por el nombre del negocio. Instagram DM es un canal de outbound válido en LatAm (`59`).

## Ejemplo real: dossier de contacto de una PYME local

```
Empresa: Café La Terraza (Bogotá) — de Google Maps (`21`)
  Teléfono Maps: +57 310 555 1234  → wa.me/573105551234 abre → ES WhatsApp ✅
Decisor: Andrés López (dueño) — nombre visto en respuestas a reseñas + IG
  Instagram: @cafelaterraza  → bio: "Reservas 📲 310 555 1234 | andres@..."
  LinkedIn: no tiene (típico en PYME local)
  Email: andres@cafelaterraza.co → verificar (`23`, `28`)

Ficha final de contacto:
  wa=+573105551234 | ig=@cafelaterraza | email=andres@... | tel=3105551234
  Canal primario sugerido: WhatsApp (LatAm local) → framework en `59`
```

## Prioriza el canal según el tipo de cuenta

- **PYME / negocio local LatAm:** WhatsApp #1, Instagram #2, email #3, llamada #4.
- **Empresa B2B / SaaS mediana:** email #1, LinkedIn #2, llamada #3, WhatsApp solo si es muy cálido.
- **Enterprise:** email + LinkedIn + llamada; WhatsApp rara vez.

El diseño de cómo entrelazar los canales en el tiempo está en `61` (secuencias multicanal); las ventanas y horarios en `62`.

## Errores comunes (qué NO hacer)

- **Guardar un teléfono como WhatsApp sin validar** → mensajes que no llegan.
- **Spamear WhatsApp con números nuevos/personales** → baneo inmediato. Cómo hacerlo bien: `47`, `119`.
- **Mandar el mismo texto por los 4 canales** → parece bot. Coherente pero distinto por canal (`127`).
- **Formato de número inconsistente** → usa E.164 (`+57…`) en toda la lista.
- **Ignorar el opt-out / legalidad** — WhatsApp y llamadas también caen bajo Habeas Data/regulación (ver `49`, `181`).

## Frontera y siguiente paso

Conseguir el dato de contacto y elegir el canal = esta skill. **Qué decir** en WhatsApp/DM en frío → `59`; la **conversación de venta** que arranca cuando responden → `ventas_lushows` (ahí viven las objeciones profundas y el cierre). Con email + WhatsApp + social por contacto, limpia toda la lista en `28` y enriquécela en `29` para personalizar el primer mensaje.
