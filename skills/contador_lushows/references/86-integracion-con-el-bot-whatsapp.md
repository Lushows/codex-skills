# 86 — Integración con el bot de WhatsApp: capturar gastos y facturas por chat

Muchos negocios pequeños en Colombia **viven en WhatsApp**. La idea de este módulo es aprovechar eso: que el dueño o el cajero, en vez de guardar facturas en una bolsa para "después", le **tomen una foto al bot de WhatsApp** apenas las reciben. El bot lee la factura (OCR), la organiza y la deja lista para alimentar la contabilidad. Lo que antes se acumulaba y se perdía, ahora entra el mismo día.

Existe un proyecto real con esta forma: **AGENTE GASTROWHATS** (un bot de WhatsApp con IA) y su primo **AVIS** (el agente de AVISPA'O, que cuida los papeles de cumplimiento y lee facturas de las pymes). Este módulo explica **cómo un bot así alimenta la contabilidad** y, muy importante, **dónde termina el bot y dónde empieza el contador**.

> **El bot captura; el contador registra y responde.** El bot extrae y organiza, pero la clasificación final, el cuadre y la firma son del contador (control humano). Auditable: cada foto queda como soporte. La conversación y la lógica del bot las define `AVIS_lushows`; aquí vemos la **frontera contable**.

## Términos que debes conocer
- **Bot de WhatsApp:** programa que conversa por WhatsApp y puede recibir fotos, audios y PDFs.
- **Webhook:** el "tubo" por donde el bot recibe el mensaje y dispara el procesamiento.
- **Buzón de facturas:** donde el bot va acumulando las facturas que le mandan, ordenadas.
- **Cruce foto↔electrónica:** comparar la foto de la factura con su versión electrónica (XML) ante la DIAN, para validar que sea real y no esté duplicada.

## Cómo el bot alimenta la contabilidad (flujo)
1. El usuario **manda una foto** de la factura (o un PDF) al WhatsApp del negocio.
2. El bot **lee la factura con OCR** (ver 85): saca NIT, fecha, valor, IVA.
3. El bot **valida y organiza**: la guarda en el buzón, marca posibles duplicados, cruza con la factura electrónica si existe.
4. El bot **entrega los datos** al sistema contable (export, API o un reporte que el contador importa).
5. El **contador revisa, clasifica en el PUC y registra** el asiento (ver 12).

## La frontera con AVIS (qué hace cada quien)
| Hace el bot (AVIS / GASTROWHATS) | Hace el contador (contador_lushows) |
|---|---|
| Recibir la foto/PDF por WhatsApp | Clasificar en la cuenta correcta del PUC |
| Leer con OCR y extraer campos | Verificar `base + IVA = total` |
| Organizar el buzón y marcar duplicados | Registrar el asiento en partida doble |
| Cruzar foto ↔ factura electrónica | Conciliar, cerrar el mes, declarar |
| Recordar papeles de cumplimiento | Firmar y responder ante la DIAN |

El bot es el **ayudante que recoge y ordena**; el contador es **quien decide y firma**. El bot nunca registra un asiento "por su cuenta" ni declara impuestos.

## Ejemplo (cifras ILUSTRATIVAS / inventadas)
"Tienda Doña Rosa" recibe 8 facturas de proveedores en la semana. Doña Rosa le manda foto de cada una al bot apenas llegan. El bot extrae los datos, detecta que dos eran la misma (duplicada) y arma un reporte con 7 facturas por $3.450.000. El contador, el viernes, **revisa el reporte, corrige una clasificación, descarta el duplicado y registra**. Doña Rosa no perdió ni una factura en la bolsa. (Cifras inventadas; los totales se verifican en `Matematicas_lushows`.)

## Buenas prácticas
- **Foto clara y plana** para que el OCR acierte (ver 85).
- El bot debe **guardar la imagen original** como soporte auditable (ver 87).
- Definir una **rutina**: el contador procesa el buzón cada semana, no a fin de mes.
- **Cuidar los datos personales** que pasan por el chat (NITs, nombres): Habeas Data (ver 87).
- El bot **no clasifica solo cuentas dudosas**: las deja marcadas para el humano.

## Errores comunes
- Creer que "el bot ya lo contabilizó": el bot **captura**, no contabiliza ni declara.
- No revisar duplicados que el bot marcó → gasto doble.
- Mandar fotos borrosas y confiar en el dato extraído.
- Acumular el buzón sin procesarlo → vuelve el problema de la "bolsa de facturas".

## Conexión con otros módulos
- **85 (OCR de facturas)** — el motor que lee la factura.
- **84 (IA en contabilidad)** y **160–169** — el marco de IA y la frontera 2026.
- **12 (asientos)** y **89 (plantillas)** — el registro que hace el contador.
- **87 (respaldos y seguridad)** — guardar soportes y proteger datos personales.
- **AVIS_lushows** — la persona, conversación, cumplimiento y arquitectura del bot.
- **Matematicas_lushows** — verificación de totales e IVA.

## Siguiente paso típico
Con facturas entrando por chat, asegurar que todo quede respaldado y protegido: abrir **87 (respaldos y seguridad de datos)**.
