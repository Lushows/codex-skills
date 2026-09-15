# Diagnosticar una campaña que no vende

## El principio del diagnóstico

Una campaña que no vende falla en **un** punto del embudo, no en todos. El trabajo es localizar el
punto exacto antes de tocar nada. Cambiar cinco cosas a la vez y que mejore no te enseña nada;
cambiar la correcta y que mejore te da el negocio.

```
Impresiones → [1] → Clics → [2] → Visitas → [3] → Carrito → [4] → Compra
```

| Fuga | Se ve en | Culpable |
|---|---|---|
| [1] | CTR bajo | **El creativo / el ángulo** |
| [2] | Visitas ÷ clics bajo | **Velocidad o técnica de la página** |
| [3] | Carrito ÷ visitas bajo | **La oferta, el precio, la página** |
| [4] | Compra ÷ carrito bajo | **Checkout, envío, pago, confianza** |

## El árbol completo

### Paso 1 — ¿Hay impresiones?

| Observación | Causa | Acción |
|---|---|---|
| Gasta 0 o casi nada | Anuncio rechazado, puja muy baja, audiencia diminuta | Mecánica: `facebook_ads_lushows` |
| Gasta pero CPM altísimo | Audiencia muy acotada, temporada (`270`), categoría sensible | Ampliar audiencia (`245`) |

### Paso 2 — ¿CTR de enlace bajo (< 1,0%)?

**Culpable: el creativo.** No la audiencia, no la puja.

| Sub-síntoma | Diagnóstico | Arreglo |
|---|---|---|
| Retención a 3 s < 15% | El hook no frena | 5 hooks nuevos (`249`) |
| Retención buena, CTR malo | Entretiene y no vende | Cierre y llamada a la acción (`251`) |
| CTR cayó con el tiempo | Fatiga | `264` |
| CTR nunca fue bueno | Ángulo equivocado | Otro ángulo de la matriz (`250`) |

### Paso 3 — ¿Visitas ÷ clics < 75%?

**Culpable: la técnica.** La gente hace clic y se va antes de ver nada.

| Causa | Verificación |
|---|---|
| Página lenta (> 3 s) | Mide en celular con datos móviles |
| Página rota en móvil | Ábrela en tu celular, no en la computadora |
| Link mal puesto | Haz clic en tu propio anuncio |
| Pop-up inmediato | Quítalo |

Ejecución y optimización de la página: invoca `desingweb-lushows`.

### Paso 4 — ¿Carrito ÷ visitas < 4%?

**Culpable: la oferta o la página.** El anuncio prometió algo que la página no sostiene.

| Causa | Señal | Arreglo |
|---|---|---|
| Desconexión anuncio-página | El anuncio habla de regalo y la página de "organizador modular" | Que la página repita el ángulo del anuncio |
| Precio sorpresa | El anuncio no decía el precio y es más alto de lo esperado | Ancla el precio en el anuncio (`260`) |
| Página sin prueba | Cero testimonios, cero fotos reales | `256` |
| Sin razón para comprar hoy | Ninguna urgencia | Fecha de entrega, stock real |
| Producto mal explicado arriba | Hay que bajar para entender | Beneficio en el primer pantallazo |

### Paso 5 — ¿Compra ÷ carrito < 25-35%?

**Culpable: el checkout.**

| Causa | Arreglo |
|---|---|
| Envío sorpresa al final | Muéstralo desde el principio o inclúyelo en el precio |
| Pocos medios de pago | En México: tarjeta, SPEI, OXXO, MSI en Buen Fin |
| Checkout de 4 pasos | Un paso |
| Pide crear cuenta | Compra de invitado |
| Sin señales de confianza | Devoluciones, contacto, dirección real |
| Pasarela rechazando | Revisa la tasa de aprobación con el proveedor |

### Paso 6 — Todo el embudo bien y el CPA sigue alto

| Causa | Arreglo |
|---|---|
| AOV demasiado bajo para el CPM del país | Subir el bundle o el precio (`42`) |
| CPM de temporada | `270` |
| Escalaste demasiado rápido | `243`, `269` |
| Producto sin margen suficiente | El negocio no existe a ese precio; ver `42` |

## La tabla de un vistazo

| CTR | CVR | Diagnóstico | Primera acción |
|---|---|---|---|
| Bajo | Bajo | Ángulo equivocado o producto sin demanda | Ángulo nuevo (`250`); si falla 3 veces, producto |
| Bajo | Alto | Hook malo, mensaje bueno | 5 hooks nuevos (`249`) |
| Alto | Bajo | Promesa del anuncio ≠ página/oferta | Alinear página y revisar precio |
| Alto | Alto, CPA alto | CPM caro o AOV bajo | Subir AOV o cambiar de país/temporada |
| Alto | Alto, CPA bien | No hay problema | Escalar (`243`) |

## Los cinco sospechosos que nadie revisa

1. **El píxel duplicado**: reporta el doble de ventas y tomas decisiones sobre datos falsos.
2. **El envío que no se ve hasta el final**: mata el 20-40% de los carritos.
3. **La página en escritorio mientras el 95% entra por celular.**
4. **El stock agotado** de la variante más pedida.
5. **Tu propio WhatsApp sin responder**: en LatAm, mucha gente pregunta antes de pagar. Sin respuesta
   en 10 minutos, se pierde (`272`, `ventas_lushows`).

## Cuándo el diagnóstico es "el producto"

Si después de 3 ángulos distintos, 2 hooks por ángulo, página revisada y USD 150-200 gastados sigues
sin un CPA bajo el techo de CAC, el problema ya no es el creativo. Es:

| Posibilidad | Verificación |
|---|---|
| El producto no tiene demanda real | `60` |
| Está saturado | `61` |
| El margen no aguanta el CPM del país | `42`, `11` |
| El público no compra en línea a ese precio | Comparables del mercado |

Aceptarlo rápido es lo que te deja capital para el siguiente producto. Ver `268`.

## Frontera

Lo técnico de la cuenta (entrega, aprendizaje, eventos, atribución) es de `facebook_ads_lushows` y
`tiktok_ads_lushows`. La página y su velocidad, de `desingweb-lushows`. El cálculo del ROAS de
equilibrio, de `Matematicas_lushows`. Aquí se localiza **dónde está la fuga y qué significa para el
producto**.

## Relacionados
`244` presupuestos · `250` ángulos · `256` testimonios · `264` fatiga · `265` testear · `266` métricas · `268` cuándo matar · `270` CPM
