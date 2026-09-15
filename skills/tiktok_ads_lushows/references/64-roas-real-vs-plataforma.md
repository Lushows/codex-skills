# 64 — ROAS real vs plataforma

Lee este módulo cuando TikTok te muestre un ROAS de 5x pero tu cuenta de banco no lo sienta, cuando un cliente te diga "los números no me cuadran", o antes de decidir escalar basándote solo en lo que dice el panel. Esta es la verdad más cara de ignorar en todo el media buying: **el ROAS que reporta TikTok casi siempre infla**. No porque mienta a propósito, sino por cómo atribuye. Si escalas con el ROAS de plataforma como si fuera verdad, quemas presupuesto creyendo que ganas. La rentabilidad real se calcula triangulando tres fuentes y la decide el MER (rutea el modelo completo a `economist_lushows`).

## Por qué el ROAS de plataforma infla

TikTok cuenta como "suya" cualquier venta que toque su ventana de atribución, aunque la persona ya iba a comprar. Cuatro razones concretas:

| Causa | Qué hace |
|---|---|
| **Ventana de atribución generosa** | 7d-click / 1d-view: si alguien vio tu ad ayer y hoy compró buscándote en Google, TikTok se lo atribuye |
| **Robo de crédito** | Acredita ventas que también acreditan Meta y Google (todos suman la misma venta) |
| **No descuenta lo orgánico** | Clientes que ya te conocían y habrían comprado igual (incrementalidad, ver 65) |
| **Solo ve su pedacito** | No ve devoluciones, costos, comisiones ni el negocio completo |

Jerga: **7d-click/1d-view** = TikTok atribuye una venta si la persona hizo clic en los últimos 7 días o solo vio el ad en el último 1 día. Es una red ancha. Además, en iOS, **SKAN** (SKAdNetwork, el sistema de privacidad de Apple) entrega datos **agregados y con retraso**, así que parte del ROAS es estimado, no medido. Conclusión: el ROAS de plataforma es una **señal direccional**, no la verdad contable. Sirve para comparar creativos entre sí (todos bajo la misma vara inflada), no para decidir si el negocio gana.

## Triangular: las tres fuentes

Nunca decidas con una sola fuente. Cruza estas tres y la verdad vive en el medio:

| Fuente | Qué te da | Sesgo |
|---|---|---|
| **Plataforma (TikTok)** | ROAS por campaña/creativo, rápido | Infla (sobre-atribuye) |
| **Backend** (tu tienda/CRM/órdenes) | Ventas reales con su origen/UTM (ver 66) | Subcuenta (pierde los que no traen UTM) |
| **Banco / contabilidad** | La plata que de verdad entró | La verdad, pero sin desglose por canal |

Regla práctica: si TikTok dice ROAS 5x pero el backend (por UTM) solo atribuye 2x y el banco no muestra crecimiento de caja, **tu ROAS real está más cerca de 2x**. Decide con el conservador, no con el optimista.

### El factor de descuento (cómo calibrarlo)

No adivines cuánto infla TikTok — **mídelo** y conviértelo en un número que uses cada semana:

```
Factor de plataforma = ventas reales del backend (atribuidas a TikTok) ÷ conversiones que reporta TikTok
```

Ejemplo de un mes: TikTok reportó 120 compras; el backend (por `utm_source=tiktok`) registró 78 órdenes reales de TikTok. Factor = 78 ÷ 120 = **0,65**. A partir de ahí, cuando el panel diga "ROAS 4,0x", tu estimado realista es 4,0 × 0,65 ≈ **2,6x**. Recalcula el factor cada mes; cambia con la temporada y con la calidad del píxel (ver 62). Documéntalo en tu reporte (ver 67) para que el cliente entienda por qué el número del panel y el del banco no son el mismo.

## Los números que de verdad mandan

El ROAS está bien para comparar creativos entre sí, pero la rentabilidad del negocio se mide con estos. Aquí es donde se rutea a `economist_lushows` para el modelo completo:

| Métrica | Fórmula | Por qué importa |
|---|---|---|
| **MER** | Ingreso TOTAL ÷ gasto TOTAL en ads (todos los canales) | No se engaña con atribución; mide el negocio entero |
| **nCAC** | Gasto en ads ÷ clientes **nuevos** (no recompras) | El ROAS mezcla nuevos y recurrentes; el nCAC los separa |
| **Profit por pedido** | AOV − costo producto − comisiones − envío − devoluciones | Puedes tener ROAS 4x y perder plata si el margen es bajo |
| **CM (margen de contribución)** | Profit por pedido ÷ AOV | Cuánto de cada venta queda para pagar el CAC |
| **Payback** | nCAC ÷ profit por pedido | En cuántos pedidos recuperas lo que pagaste por el cliente |

El **MER** es el rey honesto: como divide ingreso total entre gasto total, no le importa qué canal se robó el crédito. Si subes gasto en TikTok y el MER global mejora, TikTok suma de verdad. Si subes gasto y el MER empeora aunque el ROAS de plataforma se vea bien, estás **canibalizando** ventas que ya eran tuyas (ver 65).

### Ejemplo numérico de triangulación completa

Tienda de producto digital, mes de junio:

| Dato | Valor |
|---|---|
| Gasto TikTok | $4.000.000 COP |
| Gasto total ads (TikTok + Meta) | $6.500.000 COP |
| ROAS que reporta TikTok | 4,2x → "ingreso $16,8M" |
| Ventas reales del backend atribuidas a TikTok (UTM) | $9.100.000 COP → ROAS real ≈ 2,3x |
| Ingreso TOTAL del negocio (banco) | $14.300.000 COP |
| **MER** | 14,3M ÷ 6,5M = **2,2x** |
| AOV | $38.000 · margen contribución 55% → $20.900/pedido |

Lectura: el panel grita "4,2x" pero el negocio entero gira a **MER 2,2x**. ¿Es rentable? Con margen de contribución del 55%, un MER de 2,2x deja caja positiva — pero muy lejos del 4,2x que celebraría un novato. **Decisión de escalar se toma con el 2,2x del MER, no con el 4,2x del panel.** Si al subir gasto el MER se mantiene o sube, escala (ver 72); si cae, estás pagando por ventas que ya tenías.

## Cómo usar esto sin volverte loco

1. Usa el **ROAS de plataforma** para comparar creativos entre sí (es consistente dentro de TikTok, ver 68).
2. Usa el **backend con UTMs** (ver 66) para calcular tu factor de descuento y saber qué atribuirle de verdad.
3. Usa el **MER y el banco** para decidir si escalas el presupuesto total (ver 72).
4. Para el modelo de CAC/LTV/viabilidad y cuánto puedes pagar por cliente → **rutea a `economist_lushows`**. Ese cálculo no se hace en Ads Manager. (Lo mismo aplica para Meta en `facebook_ads_lushows` y Google en `google_ads_lushows`: el MER suma todos los canales, no uno solo.)

## Errores comunes — blacklist

- **Escalar con el ROAS de plataforma como verdad.** Infla; quemas plata creyendo que ganas. Triangula y aplica tu factor.
- **No mirar el MER.** Es la única métrica que la atribución no engaña. Calcúlalo siempre (rutea `economist_lushows`).
- **Sumar el ROAS de TikTok + Meta + Google.** Cuentan la misma venta; el total es ficción. Usa MER.
- **Ignorar el profit por pedido.** ROAS 4x con margen flaco = pérdida. Mete costos reales.
- **Confundir cliente nuevo con recompra.** El nCAC separa lo que el ROAS mezcla.
- **Creer que SKAN/iOS te da el dato exacto.** Es agregado y con retraso; parte es estimación.
- **No calibrar tu factor de descuento.** Sin medir cuánto infla, "el ROAS real es ~2x" es una corazonada, no un dato.
- **Hacer el modelo financiero en Ads Manager.** No es su trabajo. Rutea a `economist_lushows`.
