# 35 — IA en outbound 2026

La IA cambió la economía del outbound: lo que antes era el cuello de botella —investigar cada cuenta y escribir un mensaje relevante para cada persona— ahora se hace a escala. Pero también democratizó el spam: cualquiera manda 10.000 correos "personalizados" genéricos, y las bandejas (y los filtros de Gmail/Outlook) se endurecieron en respuesta. Este módulo separa lo que la IA **sí** hace bien en 2026 de la fantasía, y dónde está el límite. Es el complemento del research automático de Clay (`31`, `120`) y de los agentes SDR emergentes.

## El principio: la IA escala la relevancia, no reemplaza el criterio

La ventaja real de la IA no es "escribir correos" —eso lo hace cualquier plantilla—. Es **investigar a escala**: leer el sitio web, el LinkedIn y las noticias de 500 empresas y sacar el dato específico que hace que un mensaje se sienta escrito a mano. La relevancia era cara (tiempo humano); la IA la abarató. Pero **la IA no decide a quién contactar, no juzga si el encaje es real, y no sostiene una conversación de venta.** Eso sigue siendo humano.

Frase que ordena todo: **la IA hace el research y el primer borrador; el humano elige el target y cierra la conversación.**

## Los 4 usos que sí funcionan

| Uso | Qué hace la IA | Herramienta | Ver |
|---|---|---|---|
| **Research a escala** | Lee web/LinkedIn/noticias y extrae el dato relevante | Claygent (Clay), agentes | `31`, `120`, `130` |
| **Primer borrador / opener** | Redacta la línea 1 y el cuerpo usando ese dato | Clay + IA, Lemlist AI | `53`, `120` |
| **Clasificar respuestas** | Etiqueta réplicas: interesado / no / fuera de oficina / baja | sequencer con IA, Make+IA | `64` |
| **Puntuar encaje** | Combina señales y firmographics en un score | Clay, lead scoring | `38`, `137` |

Estos cuatro comparten algo: la IA **procesa información a volumen** y entrega algo que un humano revisa o que dispara una regla. No están "hablando con el cliente".

## Los agentes SDR: qué son y qué no (2026)

Han aparecido "agentes SDR" (herramientas que prometen prospectar, escribir y responder solas de punta a punta). La realidad honesta 2026:

- **Sí sirven** para: enriquecer + escribir borradores + clasificar respuestas + agendar mecánicamente. La parte de **operación repetible**.
- **No sustituyen** el juicio de targeting ni la conversación de venta. Un "agente" que responde solo a un prospecto interesado suele sonar robótico y quema la oportunidad justo cuando más vale.
- **El patrón ganador es humano + IA:** la IA prepara (research, borrador, score, orden de prioridad), el humano aprueba el mensaje y **toma la conversación** en cuanto hay interés real. La respuesta positiva es demasiado valiosa para dejársela a un bot; ahí entra el vendedor (`ventas_lushows`).

## El límite duro: personalización falsa = confianza cero

El error mortal de 2026 es la **personalización a escala mal hecha**: correos que dicen "vi tu increíble trabajo en {company}" donde la IA no vio nada. Los compradores ya reconocen el patrón y lo castigan (marcan spam, lo cual **daña tu deliverability**, ver `40`). Reglas para no caer:

1. **Cada dato debe ser verificable.** El prompt debe devolver `SIN_DATO` cuando no hay evidencia real, y esas filas van a plantilla genérica, no a falsa personalización (ver el prompt de `31`).
2. **La IA propone, tú revisas** en muestra. Antes de escalar a 500, lee 20 correos generados. Si 3 suenan raros o inventados, arregla el prompt.
3. **Relevancia > halago.** "Vi que están contratando 3 meseros y abriendo sede" (dato real, señal) vale más que "amo su marca" (relleno). Ver `52`, `53`.
4. **Variabilidad para deliverability.** Correos idénticos generados en masa disparan filtros; usa spintax y estructura variable (ver `45`, `121`).

## Ejemplo: pipeline de IA para una campaña

```
1. Clay trae 300 cuentas del nicho
2. Claygent (IA) investiga cada una → dato específico + SIN_DATO si no hay
3. IA redacta opener usando el dato   → columna "linea_1"
4. Fórmula arma el correo completo (opener IA + pitch fijo + CTA fijo)
5. HUMANO revisa 20 muestras → ajusta prompt si hace falta
6. Filtra: solo filas con email verificado + dato real (no SIN_DATO)
7. Exporta a Smartlead → cadencia (ver 33, 60)
8. IA clasifica respuestas → interesados a un humano en Slack (ver 34)
9. HUMANO conversa y cierra → ventas_lushows
```
Fíjate: la IA hace 2, 3, 8. El humano hace 5, 9 (lo de mayor juicio). Todo lo demás es plomería automatizada.

## Costo: la IA a escala se paga en tokens

Correr research + redacción con IA sobre miles de filas consume llamadas a modelos (tokens), y eso cuesta. Un Claygent sobre 5.000 cuentas puede ser caro si no optimizas. Para **reducir ese costo sin perder calidad** —caching, batching, elegir el modelo correcto para cada tarea, comprimir prompts— **rutea a `optimizer_tokens_lushows`**. Esta skill decide *qué* investigar y escribir; optimizer decide *cómo pagarlo barato*.

## Errores comunes

- **Confiar en la IA sin revisar** → correos que inventan datos y matan tu reputación.
- **Dejar que un agente responda a los interesados** → pierdes la venta por sonar robot. La respuesta positiva es del humano.
- **Generar correos idénticos en masa** → filtros de spam (ver `121`).
- **Ignorar el costo de tokens** hasta que llega la factura → ver `optimizer_tokens_lushows`.
- **Creer que la IA elige el target.** El ICP y a quién contactar es criterio humano/estratégico (ver `10`, `economist_lushows`).

## Siguiente paso

Monta el pipeline de arriba con 50 filas y **lee las 50 salidas a mano** antes de escalar. Afina el prompt de research en `120` y la personalización en `52`/`53`. Para señales que disparan estos correos → `36`, `37`. Para bajar el costo de la IA → `optimizer_tokens_lushows`. Para el momento en que la IA entrega el interesado y empieza la venta real → `ventas_lushows`.
