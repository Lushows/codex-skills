# 25 — Customer Match y first-party

Lee este módulo cuando ya tienes una base de clientes o leads (correos, teléfonos) y quieres usarla en Google — para reactivarlos, excluirlos, o encontrar gente parecida. **Customer Match** te deja subir tu lista de contactos a Google y mostrarles (o no) anuncios. En el mundo post-cookie de 2026, tus **datos propios (first-party)** son la ventaja competitiva más difícil de copiar: nadie más tiene tu lista de clientes. Google y Meta la usan distinto, pero en ambos es oro (ver `facebook_ads_lushows` para el lado Meta). Frame: Google captura intención de extraños; Customer Match te deja capturar el valor de los que YA confiaron en ti.

## Qué es y cómo se sube (sin miedo a la privacidad)

Customer Match = subes una lista de correos, teléfonos y/o direcciones de tus clientes, Google la **cruza** con sus usuarios y crea una audiencia con quienes coinciden.

**Lo importante para dormir tranquilo:** los datos se suben **hasheados** (cifrados con SHA-256). El hash convierte "luchoxd07@gmail.com" en una cadena ilegible irreversible antes de salir de tu equipo. Google no ve el correo real; solo compara hash contra hash. Aun así, debes tener **consentimiento** y cumplir Habeas Data en Colombia (ver 29) — no subas listas compradas ni de gente que no aceptó uso publicitario.

Cómo subir (Audience Manager → Tus segmentos de datos → Customer Match):
1. Exporta tu CRM/lista a CSV con columnas: Email, Phone, First name, Last name, Country, Zip. Mientras más campos, mejor cruce.
2. Normaliza antes: teléfonos en formato E.164 (`+573004183337`), correos en minúscula sin espacios. Google hashea al subir, pero si los datos están sucios el cruce baja.
3. Google hashea automáticamente al subir (o súbela ya hasheada si tu sistema lo hace).
4. Espera el cruce (horas, a veces hasta 24–48h). Verás cuántos "coincidieron".

**Tamaños mínimos:** Google exige cierto volumen para activar la lista (~1.000 usuarios coincidentes para muchos usos), y la tasa de cruce suele ser 40–80% de lo que subes — no todos tus contactos tienen cuenta Google activa o el mismo correo. Si subes 500 contactos puede que no se active. Junta volumen antes de esperar magia. Truco: sube email **y** teléfono del mismo cliente en la misma fila; Google intenta cruzar por ambos y sube la tasa de match.

## Los 3 usos que cambian tu cuenta

| Uso | Qué haces | Para qué sirve |
|---|---|---|
| **Exclusión** | Subes compradores y los EXCLUYES de campañas de adquisición | No pagar por gente que ya compró (ver 24) |
| **Retención / recompra** | Campaña dirigida SOLO a tu lista de clientes | Venderles un segundo producto, recompra, upsell (ver 97) |
| **Similar / semilla** | Google encuentra gente PARECIDA a tu lista | Adquisición de nuevos clientes con perfil probado |

El uso de **exclusión** es el más subestimado y el más rentable: en una cuenta de adquisición pura, excluir a tus clientes actuales evita gastar en quien ya tienes. El de **similar** (antes "Lookalike" en lenguaje Meta; en Google son señales para que el algoritmo amplíe) potencia PMax, Demand Gen y Smart Bidding: dales tu lista de MEJORES clientes (no todos — los de mayor LTV) como semilla y el algoritmo busca más como ellos (ver 12, 41). Una semilla de "mis 200 mejores clientes" rinde más que una de "todos mis 5.000 contactos" — calidad sobre cantidad.

Caso gastro concreto: subes los dueños de restaurante que compraron la calculadora y pagaron, los usas como semilla para PMax → Google busca más dueños de restaurante con perfil de compra parecido. Y subes a TODOS los compradores como exclusión en tu Search de adquisición para no re-pagar por ellos.

## Por qué es el activo post-cookie

Las cookies de terceros (las que rastreaban gente entre sitios ajenos) están muriendo. La medición y el targeting basados en seguir al usuario por la web se degradan. Lo que **sobrevive** es lo que el usuario te dio directamente a ti: su correo al comprar, su teléfono al registrarse. Eso es first-party.

Tu trabajo estratégico, más allá de la pauta: **capturar datos propios sin parar.** Cada venta, cada lead, cada descarga debería dejar un correo/teléfono en tu base con su consentimiento. Mientras más grande y limpia tu lista:
- Mejor Customer Match (más cruce).
- Mejores señales para Smart Bidding y PMax.
- Mejor Enhanced Conversions (ver 28, 53) — porque ata tus conversiones a datos reales.
- Menos dependes de cookies que se mueren.

Quien tenga la mejor base first-party gana la década. Es lo único que el competidor no te puede copiar ni Google quitarte. Higieniza la lista mensual desde tu CRM: agrega nuevos compradores, quita bajas y rebotes. Una lista viva de 3.000 contactos vale más que una muerta de 10.000.

## Segmentar tu lista — no toda vale lo mismo

Subir "todos mis contactos" en una sola lista es desaprovechar Customer Match. Segmenta y dale a cada segmento un uso distinto:

| Segmento | Quién está | Uso |
|---|---|---|
| Compradores activos (LTV alto) | Pagaron y recompraron | Semilla para similar + recompra/upsell |
| Compradores 1 sola vez | Pagaron una vez, no volvieron | Campaña de recompra con oferta de regreso |
| Leads no cerrados | Dejaron datos, no compraron | Remarketing con mensaje de objeción resuelta (ver `ventas_lushows`) |
| Carrito/checkout abandonado | Casi compran | Exclusión de prospección + remarketing agresivo |
| Bajas / pidieron borrado | Se dieron de baja | EXCLUIR de todo (legal y de respeto, ver 29) |

Refresco automatizado: lo ideal es conectar tu CRM o e-commerce a Google Ads vía API o un conector (Zapier, n8n, o la API de Google Ads directa — ver `engineer_visualopen_lushows`) para que las listas se actualicen solas a diario. Subir CSV a mano cada mes funciona para empezar, pero se queda viejo rápido; la lista que se sincroniza sola mantiene el cruce alto y le da al Smart Bidding señal fresca. Para la calculadora gastro: cada vez que entra una venta nueva en `data/orders.json`, ese correo debería terminar en la lista de "compradores" automáticamente — eso es first-party haciendo trabajo mientras duermes.

Caso de exclusión bien hecho: tienes $600.000 COP/mes en Search de adquisición. Subes tus 2.000 compradores como Customer Match y los excluyes de esa campaña. Resultado: dejas de pagar clics de gente que ya te compró la calculadora y no la va a recomprar — ese presupuesto ahora caza clientes nuevos. Es plata recuperada sin tocar pujas ni anuncios.

## Errores comunes — blacklist

1. **Subir listas sin consentimiento.** Ilegal bajo Habeas Data (ver 29) y Google puede sancionarte. Solo contactos que aceptaron uso publicitario. Nada de listas compradas.
2. **Esperar que coincida el 100%.** La tasa de cruce es 40–80%. Si subes 1.000, pueden coincidir 600. Normal. No es error tuyo — sube email + teléfono para mejorarla.
3. **Subir muy pocos contactos.** Bajo el mínimo (~1.000 coincidentes) la lista no se activa. Junta volumen primero.
4. **No usar la exclusión.** Pagar por reanunciar a clientes existentes en campañas de adquisición es de los desperdicios más comunes. Súbelos y exclúyelos.
5. **No actualizar la lista.** Una lista de hace un año está vieja y el cruce cae. Refréscala mensual desde tu CRM.
6. **Usar "todos los contactos" como semilla en vez de los mejores.** El algoritmo busca parecidos a lo que le das; si le das mediocres, trae mediocres. Semilla = top LTV.
7. **Creer que el hash te exime de la ley.** El hash protege el dato técnicamente, pero igual necesitas base legal y consentimiento (ver 29). Cumplir no es opcional.
8. **No capturar datos propios en cada venta.** Si no estás construyendo tu base first-party hoy, estás regalando tu única ventaja del futuro post-cookie. Pon un campo de email/teléfono con casilla de consentimiento en cada punto de contacto.
