# 58 — Leads high-ticket

Lee este módulo cuando vendes algo **caro y de decisión lenta**: consultoría, software a medida, cirugía estética, asesoría legal, maquinaria, inmuebles, servicios B2B de varios millones, formación premium. Aquí la lógica se invierte respecto al e-commerce barato: **no quieres muchos leads, quieres pocos leads MUY calificados**, porque cada uno lo trabaja una persona durante semanas. Un lead malo no solo cuesta el clic — cuesta el tiempo de tu vendedor, que es lo más caro que tienes. El cierre es un oficio largo (ventas_lushows, especialmente high-ticket); aquí montamos Google para que **no pagues por curiosos** y para que la máquina aprenda a traer compradores con OCI.

## La economía del high-ticket: el CPL alto está bien

En high-ticket el **CPL** (*Cost Per Lead* — costo por lead) **se ve carísimo** comparado con un negocio barato, y eso está perfecto. Lo que importa no es el costo del lead, es cuánto vale el cliente que cierras.

| | Producto barato | High-ticket |
|---|---|---|
| Valor del cliente | $10.000 – $100.000 | $5.000.000 – $50.000.000+ |
| CPL aceptable | $2.000 – $20.000 | $50.000 – $500.000+ |
| Leads/mes | Muchos | Pocos y buenos |
| Qué optimizas | Volumen de ventas | **Calidad del lead** |
| Ciclo | Minutos/días | Semanas/meses |

Si un cliente te deja $10.000.000 de margen, pagar $200.000 por un lead que cierra 1 de cada 5 = $1.000.000 de costo de adquisición por venta. Excelente: gastas un millón para ganar diez. **Deja de mirar el CPL aislado**; mira el costo por **venta** y el margen (viabilidad y unit economics → economist_lushows). El número que importa es **CAC vs LTV**, no el precio del clic. Un competidor que se asusta del CPL alto y "lo baja" termina llenando su CRM de basura barata; tú, mirando el costo por venta, le ganas el mercado.

## Fricción intencional: filtrar es ganar

En e-commerce quitas fricción para vender más. En high-ticket **agregas fricción a propósito** para que el curioso no entre y solo pase el que va en serio. Cada barrera que pones cuesta volumen pero sube calidad — y aquí la calidad es todo.

Cómo meter fricción útil:

- **Lead form "más calificado"** (ver 52) con preguntas que duelen al curioso: presupuesto, tamaño de empresa, urgencia, rol ("¿eres tú quien decide la compra?").
- **Preguntas de calificación duras:** "¿Cuál es tu presupuesto para esto?" con rangos reales. Quien no tiene presupuesto, no llena. Perfecto: no lo quieres ocupando a tu vendedor.
- **Agendamiento en vez de "te contacto":** que el lead **reserve una hora** en tu calendario (Calendly o similar). El que agenda una llamada está mucho más comprometido que el que solo deja su número; el no-show baja y la calidad sube. Manda el link de agenda en la pantalla final del lead form o en el primer mensaje de WhatsApp.
- **Landing que pre-vende y descalifica:** la página dice claro para quién ES y para quién NO es ("esto es para restaurantes que facturan más de X"). Espanta al que no calza (la arma → desingweb-lushows).

Resultado: menos leads, pero el vendedor habla solo con gente real (el cierre → ventas_lushows high-ticket). La velocidad también cuenta: un lead caro contactado al otro día se perdió igual que uno barato (ver 54).

## Valor por etapa con OCI: el corazón del high-ticket

El ciclo es largo: alguien deja datos hoy y compra en 6 semanas. Si solo le dices a Google "se generó un lead", optimiza por **cantidad de leads** — y te llena de curiosos baratos. La solución es **OCI con valor por etapa** (ver 53, 96 stack-OCI): a medida que el lead avanza, le subes a Google una conversión con un valor que crece.

```
Lead entra (gclid capturado)
  → Lead calificado (es decisor, tiene presupuesto)  → subes "valor 1" (ej. $50.000)
  → Agendó / asistió a la reunión                    → subes "valor 2" (ej. $150.000)
  → Propuesta enviada                                → subes "valor 3" (ej. $400.000)
  → CERRÓ                                            → subes el valor real (ej. $10.000.000)
```

Con esto, Smart Bidding (ver 15) deja de perseguir "muchos leads" y aprende a traer **los clics que se parecen a los que avanzan y cierran**. Es la diferencia entre una cuenta que llena el CRM de basura y una que **agenda reuniones con compradores**. Sin OCI, en high-ticket vuelas completamente ciego (ver 64 ROAS-real).

Detalle práctico para ciclos largos: Google necesita datos para aprender, y tus ventas tardan semanas. Por eso arrancas optimizando por la conversión **temprana** (lead calificado/reunión agendada — hay volumen) y vas dándole valor creciente a las etapas profundas a medida que cierran. Así el algoritmo tiene señal mientras maduran las ventas reales (ver 54, 15).

Requisito previo: **capturar el gclid** desde el primer formulario y pegarlo al lead en tu CRM (ver 53, 54). Sin gclid no hay OCI, y sin OCI el high-ticket en Google es una lotería cara.

## Plantilla de arranque (servicio B2B, ticket alto)

- Campaña Search, keywords de **intención de solución** ("software inventario restaurante", "asesoría food cost", "consultoría rentabilidad restaurante"), concordancia frase/exacta + negativos duros (`gratis`, `plantilla`, `curso`, `empleo` — ver 22).
- Destino: **landing que descalifica** (desingweb-lushows) con lead form calificado o agenda, gclid capturado.
- Conversión temprana ("reunión agendada") como objetivo inicial de Smart Bidding; OCI con valor por etapa en cuanto haya cierres.
- Handoff instantáneo a WhatsApp/llamada (ver 54), seguimiento disciplinado (ventas_lushows high-ticket), y registro del gclid+etapa en el CRM para subir con OCI.

## Errores comunes — blacklist

1. **Asustarte por el CPL alto y "optimizar para bajarlo".** Bajar el CPL suele significar atraer curiosos baratos que no cierran. Mira el costo por **venta** y el margen, no el precio del lead (economist_lushows).
2. **Quitar fricción para "tener más leads".** Más leads malos = más tiempo perdido de tu vendedor. En high-ticket, la fricción que filtra es tu amiga.
3. **No usar OCI con valor por etapa.** Optimizar por "lead generado" te entierra en curiosos. Sube conversiones con valor creciente para que Google traiga compradores (ver 53).
4. **No capturar el gclid.** Sin él no hay OCI y el high-ticket en Google es azar. Captúralo en el primer formulario (ver 54, desingweb-lushows).
5. **Pedir "te contacto" en vez de agendar.** El que agenda una llamada está mucho más comprometido. Usa calendario, no "deja tu número".
6. **Landing que le habla a todos.** Si no descalifica, atrae a todos y filtras a mano gastando tiempo. La página debe decir para quién NO es (desingweb-lushows).
7. **Contestar lento un lead caro.** Pagaste $200.000 por ese lead; si lo contactas al otro día, lo perdiste. La velocidad cierra incluso en high-ticket (ver 54, ventas_lushows).
