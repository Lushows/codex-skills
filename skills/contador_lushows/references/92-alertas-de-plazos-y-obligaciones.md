# 92 — Alertas de plazos y obligaciones: cómo no perder un vencimiento

En Colombia, perder un vencimiento cuesta plata: sanciones, intereses, hasta el cierre del negocio. El problema es que las obligaciones son muchas y caen en fechas distintas (DIAN, municipio, Cámara de Comercio, nómina, parafiscales). Un dueño ocupado las olvida fácil. Este módulo arma tu **calendario de obligaciones** y explica cómo automatizar los recordatorios para que nunca se te pase ni uno.

Aquí no liquidamos impuestos (eso vive en el bloque 40-49). Aquí organizamos el CUÁNDO y cómo recordarlo.

## Términos que debes conocer
- **Vencimiento:** fecha límite para presentar o pagar una obligación.
- **Periodicidad:** cada cuánto se repite (mensual, bimestral, anual).
- **Sanción por extemporaneidad:** multa por presentar tarde.
- **Intereses de mora:** lo que cobra la DIAN por pagar tarde, día a día.
- **Calendario tributario:** documento que la DIAN publica CADA AÑO con las fechas exactas según el último dígito del NIT.

> Regla de oro: **las fechas exactas cambian todos los años** y dependen del último dígito de tu NIT y del calendario tributario que la DIAN publica en diciembre/enero. Aquí damos el MAPA de obligaciones; las fechas concretas **se verifican en el calendario tributario del año vigente**.

## Mapa de obligaciones típicas de un comerciante
| Obligación | Periodicidad típica | Quién | Verificar fecha en |
|---|---|---|---|
| IVA / Impuesto al consumo | Bimestral o cuatrimestral | DIAN | Calendario tributario DIAN |
| Retención en la fuente | Mensual | DIAN | Calendario tributario DIAN |
| ICA | Según municipio (bimestral/anual) | Municipio | Secretaría de Hacienda local |
| Declaración de renta | Anual | DIAN | Calendario tributario DIAN |
| Información exógena | Anual | DIAN | Resolución exógena del año |
| Nómina y aportes (PILA) | Mensual | Operador PILA | Según dígito del NIT |
| Renovación matrícula mercantil | Anual (primeros meses) | Cámara de Comercio | Cámara de Comercio local |
| Nómina electrónica | Mensual | DIAN | Calendario DIAN |

## Cómo no perder un vencimiento (sistema simple)
1. **Una vez al año** (enero): baja el calendario tributario, busca tu último dígito de NIT y anota tus fechas.
2. Pásalas a un calendario digital con **alarma 5 días antes**.
3. Agrega un **buffer**: prepara la declaración una semana antes, no el mismo día.
4. Marca como recurrentes las mensuales (retención, PILA, nómina electrónica).
5. Designa un responsable claro (tú o tu contador) por cada obligación.

## Frontera con AVIS (el bot de WhatsApp)
Recordar y avisar es trabajo de conversación, no de contabilidad. Por eso:
- **contador** define QUÉ obligaciones existen y CUÁNDO (este calendario).
- **AVIS** CONVERSA: envía el recordatorio por WhatsApp ("Don Luis, su retención vence en 3 días"), confirma con botones que ya se pagó, y vuelve a avisar si no.
- El contador entrega la lista de obligaciones + fechas; AVIS la convierte en alertas automáticas.

## Ejemplo (cifras ILUSTRATIVAS / inventadas)
"Ferretería El Tornillo" arma su calendario en enero:
- Retención mensual → alarma el día 8 de cada mes (su NIT vence el 13, según el calendario verificado).
- IVA bimestral → alarma cada 2 meses, 5 días antes.
- Renovación de matrícula → alarma en febrero (vence en marzo).
- AVIS le manda los 3 recordatorios por WhatsApp y registra cuando confirma el pago.

Resultado: cero sanciones por olvido ese año. *(El valor de cualquier sanción evitada se estima en `Matematicas_lushows`.)*

## Errores comunes
- **Asumir que la fecha es la misma del año pasado.** Cambia cada año; verifica el calendario.
- **No saber tu último dígito de NIT.** Define tu fecha exacta; búscalo en el RUT.
- **Preparar la declaración el último día.** Si falla la plataforma o el banco, te vence. Deja buffer.
- **Pensar que solo existe la DIAN.** El ICA municipal y la Cámara de Comercio también vencen.
- **No tener un responsable claro.** "Creí que lo hacías tú" es la causa #1 de mora.

## Conexión con otros módulos
- **40 (Marco tributario)** — qué impuestos te aplican (de ahí salen las obligaciones).
- **46 (Calendario tributario)** — el detalle de fechas y dígitos de NIT.
- **94 (Checklist anual)** — renta, exógena y renovación viven ahí.
- **AVIS (bot)** — convierte este calendario en alertas por WhatsApp.
- **AVIS_lushows skill** — para configurar los mensajes de recordatorio del bot.
- **Matematicas_lushows** — cálculo de sanciones e intereses de mora.

## Siguiente paso típico
Baja el calendario tributario del año, identifica tu dígito de NIT, y arma tu lista de fechas. Pásala a AVIS para que envíe los recordatorios. Para el cierre de cada mes, sigue el **93 (checklist mensual)**.
