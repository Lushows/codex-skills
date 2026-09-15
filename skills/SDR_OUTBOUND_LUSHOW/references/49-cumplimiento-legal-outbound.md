# 49 — Cumplimiento legal del outbound

Este módulo cierra el Bloque 4 con la capa que casi nadie estudia hasta que le llega una multa o le suspenden la cuenta: **qué es legal en el outbound y qué no**, en las tres jurisdicciones que más te van a tocar — CAN-SPAM (USA), GDPR (Europa) y Habeas Data / Ley 1581 (Colombia y, con primos cercanos, el resto de LatAm). No es solo evitar sanciones: el cumplimiento **es deliverability y es marca**. Un opt-out (baja) fácil baja tus quejas de spam (ver `40`), y una base de datos conseguida legalmente rebota menos y convierte más. El outbound ético escala por años; el ilegal dura semanas y te explota en la cara (el principio del `00`). Aviso: esto es orientación práctica, no asesoría jurídica; para casos serios, un abogado.

## El principio: outbound legítimo ≠ spam

Las tres leyes, con sabores distintos, convergen en lo mismo: **puedes contactar a alguien si tienes una razón legítima, le dices quién eres, y le das una salida fácil.** Lo que se castiga es el engaño (remitente falso, asunto mentiroso), la falta de salida (no hay cómo darse de baja) y —en Europa y LatAm— tratar datos personales sin base legal. El B2B relevante y honesto casi siempre cabe dentro de la ley; el spam masivo y engañoso, no.

## CAN-SPAM (Estados Unidos)

La ley federal de correo comercial. Es la **más permisiva**: **no exige consentimiento previo** para el primer correo B2B en frío. Lo que sí exige:

| Regla | Qué significa |
|---|---|
| Remitente e "From" verdaderos | Nada de dominios/nombres falsos (ligado a autenticación; ver `42`) |
| Asunto no engañoso | El subject debe reflejar el contenido, sin clickbait mentiroso |
| Identificar que es publicidad | Que se entienda que es un mensaje comercial |
| Dirección física válida | Un domicilio postal real en el correo (o en la firma) |
| **Opt-out funcional** | Un mecanismo claro para darse de baja, **procesado en ≤10 días hábiles** |

Sanción: hasta ~$53.000 USD **por correo** infractor. La clave: identifícate de verdad y honra las bajas. El cold email B2B a USA es legal si cumples esto.

## GDPR (Unión Europea) — el más estricto

El Reglamento General de Protección de Datos regula el tratamiento de **datos personales** de residentes en la UE (un correo `nombre@empresa.com` es dato personal). Exige una **base legal** para procesar el dato. Para B2B en frío, la base usada normalmente es **interés legítimo** (legitimate interest), no consentimiento — pero solo si:

- El contacto es **relevante para su trabajo** (le escribes al rol adecuado sobre algo pertinente; aquí el ICP `10` te protege legalmente).
- Haces un **balance**: tu interés no aplasta los derechos de la persona.
- Ofreces **opt-out** y respetas el **derecho a ser olvidado** (borrar sus datos si lo pide).
- Dices de dónde sacaste el dato si lo preguntan (transparencia).

Ojo: para **marketing por email a personas físicas** algunos países UE aplican además la ePrivacy (que puede exigir opt-in). El B2B a roles corporativos suele ir por interés legítimo; el B2C, casi siempre requiere consentimiento. Sanciones GDPR: hasta €20 millones o 4% de la facturación global. **No inventes:** documenta tu base legal y borra a quien lo pida.

## Habeas Data / Ley 1581 de 2012 (Colombia)

La ley colombiana de protección de datos personales — la que más aplica a Lushows. Regula la recolección, uso y circulación de datos personales, vigilada por la **SIC** (Superintendencia de Industria y Comercio). Puntos clave para outbound:

| Concepto | Qué exige |
|---|---|
| **Autorización** | Regla general: necesitas autorización del titular para tratar su dato. Debe ser previa, expresa e informada |
| **Datos de fuentes públicas** | Datos en fuentes públicas/públicamente disponibles tienen tratamiento más flexible, pero **igual debes informar** el uso y respetar los derechos |
| **Finalidad** | Solo usas el dato para el fin informado (contactarlo comercialmente, si eso se dijo) |
| **Derechos ARCO** | El titular puede conocer, actualizar, rectificar y **revocar/suprimir** su dato cuando quiera |
| **Opt-out** | Mecanismo claro para dejar de recibir y para pedir eliminación |
| **RNBD** | Registro Nacional de Bases de Datos ante la SIC (aplica según tamaño de la empresa) |
| **Aviso de privacidad** | Política de tratamiento de datos publicada (el proyecto GastroLatam ya tiene `/privacy`) |

Para WhatsApp en frío en Colombia (ver `47`), esto es especialmente sensible: contactar números sin base legal es la zona más riesgosa. Prioriza leads con relación o interés previo. Sanciones SIC: multas de hasta ~2.000 SMMLV.

## La regla práctica que te mantiene limpio (los 3 países)

```
[ ] Identifícate de verdad: nombre real, empresa real, dominio autenticado (ver 42)
[ ] Asunto honesto, sin engaño
[ ] Contacta a quien de verdad se beneficia (ICP relevante; ver 10) — es tu escudo legal
[ ] Opt-out en CADA mensaje, en cada canal, fácil y honrado rápido
[ ] Datos conseguidos legalmente (no bases robadas/compradas turbias; ver abajo)
[ ] Guarda de dónde sacaste cada dato y tu base legal
[ ] Borra a quien lo pida, de inmediato, de todos los canales
[ ] Ten publicada tu política de tratamiento de datos (aviso de privacidad)
```

## Listas legales vs ilegales

- **Legal:** datos que TÚ recolectas o enriqueces de **fuentes profesionales/públicas** con proveedores legítimos (Apollo, ZoomInfo, LinkedIn/Sales Navigator, Lusha, Hunter; ver `23`), verificados y usados con finalidad B2B relevante. Estos proveedores tienen sus propios términos de cumplimiento.
- **Ilegal / tóxico:** comprar "bases de datos de 100.000 correos" en mercados grises, listas robadas, scraping que viola términos, o datos personales sensibles sin base. Además de ilegal, están **sucias** (bounces altos → quema tu deliverability; ver `44`, `46`) y llenas de spam traps. Doble castigo: legal y técnico.

## Opt-out: cómo hacerlo bien (y por qué te conviene)

El opt-out no es solo obligación: es **higiene de deliverability**. Quien no quiere recibir y no puede salir, te marca spam (ver `40`). Dale la salida:
- Email frío: una línea al final, natural — *"Si no es para ti, respóndeme 'no' y no te escribo más."* (más humano que un botón de "unsubscribe" tipo newsletter, que además se ve a marketing; ver `45`). Y hónralo: sácalo de todas las secuencias.
- WhatsApp: *"Responde STOP para no recibir más mensajes."* Cúmplelo.
- Mantén una **lista de supresión** (suppression list) global: quien pide baja, nunca más lo tocas, en ningún canal.

## Errores comunes (qué NO hacer)

- Comprar bases masivas turbias. Ilegal + sucias + te queman. El peor "atajo".
- No poner opt-out "para no dar ideas". Ilegal, y te dispara las quejas de spam.
- Ignorar una solicitud de eliminación. En GDPR y Habeas Data es sanción directa.
- Usar el mismo dato para un fin distinto al informado (Colombia/EU).
- Creer que "es B2B, no aplica ninguna ley". Aplica: CAN-SPAM siempre, GDPR/Habeas Data por el dato personal.

## Siguiente paso

Con el cumplimiento claro cierras el Bloque 4 (deliverability e infraestructura completos). El siguiente bloque es el mensaje (`50`–`59`: qué decir para que respondan) y la cadencia (`60`–`69`: cómo secuenciar los toques). Para las fuentes legítimas de datos, ver `23`. Para el cumplimiento específico de un negocio colombiano (registros, RNBD ante la SIC, política de tratamiento) el detalle regulatorio vive en la skill de cumplimiento `AVIS_lushows`. Para deliverability legal avanzada a gran escala, ver `110`–`119`.
