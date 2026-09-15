# 92 — Upsell, cross-sell y recompra: venderle más al que ya te compró

El cliente más fácil de venderle no es uno nuevo: es el que ya te compró y quedó contento. Ya confía en ti, ya conoce tu producto, ya superó el miedo de la primera compra. Venderle de nuevo cuesta una fracción de lo que cuesta conseguir uno nuevo, y suele cerrar más rápido. Sin embargo, la mayoría de los negocios pequeños dejan ese dinero en la mesa: venden una vez y se olvidan. Este módulo es cómo hacer crecer el valor de cada cliente sin volverte molesto.

## Los tres movimientos

Define bien la diferencia, porque se confunden:

| Movimiento | Qué es | Ejemplo BIO-SETA |
|---|---|---|
| **Upsell** | Venderle una versión mejor/mayor de lo que iba a llevar | Pasa de 1 frasco a la presentación de 3 con descuento |
| **Cross-sell** | Venderle un producto complementario | Compró Melena de León → le ofreces Cordyceps para energía |
| **Recompra** | Que vuelva a comprar lo mismo cuando se le acaba | Recordatorio de reorden cuando va a quedarse sin producto |

> La estrategia de pricing, bundles y modelo de ingresos recurrentes es de `economist_lushows`. Aquí vemos el **oficio**: cuándo ofrecer, cómo decirlo y con qué guion, sin quemar la confianza.

## El principio

> **Ofrece más solo cuando suma al resultado del cliente, no cuando tú necesitas vender.**

El upsell que ayuda al cliente a conseguir mejor su objetivo se siente a buen consejo. El upsell por meta de venta se siente a estafa. La diferencia la nota el cliente al instante. Vende el siguiente paso lógico para *él*, no el producto más caro para *ti*.

## El momento: cuándo ofrecer más

El timing lo es casi todo. Ofrecer en el momento equivocado mata la confianza.

- **Upsell:** justo después de que decidió comprar, antes de cerrar. "Ya que te llevas uno, la presentación de 3 te sale a [X] por unidad en vez de [Y], y te dura el ciclo completo de 3 meses que es lo que de verdad da resultado. ¿La prefieres?" El cliente ya está en modo "sí".
- **Cross-sell:** cuando ya obtuvo valor del primer producto (después del primer valor, ver 90). "Me alegra que la Melena te esté ayudando con el foco. Mucha gente la combina con Cordyceps para tener también más energía física. ¿Te cuento?"
- **Recompra:** justo antes de que se le acabe. Aquí el cálculo es clave: si un frasco dura ~30 días, el recordatorio ideal sale al día ~25, cuando aún tiene producto pero ya piensa en reordenar. Demasiado pronto se siente a presión; demasiado tarde, ya se quedó sin y perdió el hábito.

## La recompra programada (el sistema BIO-SETA)

Para productos de consumo (suplementos, consumibles) la recompra no debe depender de la memoria del cliente —ni de la tuya. Se programa. BIO-SETA usa un recordatorio automático de recompra (`src/repurchaseReminder.js`): el sistema sabe cuándo cada cliente compró y cuánto le dura, y dispara un mensaje antes de que se acabe.

El oficio detrás del sistema:
1. **Calcula la duración real** de cada presentación (ej. 120 cápsulas / 4 al día = 30 días).
2. **Define el día de aviso** unos días antes del agotamiento (ej. día 25).
3. **Escribe un mensaje que ayuda, no que cobra:** recuérdale el beneficio de la constancia, no solo "vuelve a comprar".
4. **Facilita el reorden:** que pedir de nuevo sea un "sí" de un toque, sin re-explicar nada.

> Plantilla de recordatorio de recompra:
> "Hola [nombre] 🙂 Calculo que tu [Melena de León] está por terminarse esta semana. Para no cortar el efecto justo cuando empieza a notarse, lo ideal es no quedar sin producto. ¿Te dejo listo el reorden y te llega antes de que se te acabe?"

## Plantilla — cross-sell tras primer valor

> "Qué bueno que la Melena te esté funcionando para el foco, [nombre]. Muchos clientes que buscan rendimiento completo la combinan con Cordyceps, que aporta la parte de energía física y resistencia. Si quieres, te armo el combo de los dos con un mejor precio que comprarlos por separado. ¿Te interesa?"

## Error común

El más caro: **no ofrecer nunca** por miedo a "ser pesado". Si tu oferta ayuda al cliente, callártela es hacerle un mal servicio. El segundo error: ofrecer *todo a todos*, sin relevancia —ofrecer Ganoderma para dormir a quien compró algo para energía. Eso enseña al cliente a ignorar tus ofertas. El tercero: el upsell agresivo que pone en riesgo la venta principal ya ganada; si dudas, asegura primero la venta y ofrece el extra después.

## Checklist de upsell / cross-sell / recompra

- [ ] ¿La oferta suma al *resultado del cliente*, no solo a mi venta?
- [ ] ¿Estoy ofreciendo en el momento correcto (no antes de tiempo)?
- [ ] ¿El cross-sell es relevante a lo que ya compró?
- [ ] ¿Tengo calculada la duración del producto para el recordatorio de recompra?
- [ ] ¿El mensaje de recompra habla de beneficio/constancia, no solo de comprar?
- [ ] ¿Reordenar es fácil (un "sí" de un toque)?

## Siguiente paso

Un cliente que recompra y confía es tu mejor fuente de nuevos clientes: pídele que te recomiende. Eso es el siguiente módulo (ver 93 referidos sistemáticos). Antes, define la duración de cada uno de tus productos y a qué día disparar el recordatorio de recompra.
