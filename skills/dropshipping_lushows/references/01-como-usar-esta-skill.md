# Cómo usar esta skill

## Para Claude

**Regla de oro: carga bajo demanda.** Nunca leas los 300 módulos. Lee el `SKILL.md` (que ya está en
contexto), identifica el modo, y carga **entre 1 y 5 módulos** relevantes a la pregunta concreta.

### Ruta rápida por tipo de pregunta

| El usuario dice... | Carga |
|---|---|
| "¿Qué vendo?" | `40`, `41`, `50`, `76` |
| "¿Sirve este producto?" | `41`, `42`, `76`, `61` |
| "¿A qué país le vendo?" | `10`, `11`, `12`, `13` + el playbook del país |
| "¿Cómo espío a la competencia?" | `81`, `82`, `96`, `105` |
| "No me convierte la página" | `204`, `180`, `183`, `203` |
| "No me da el margen" | `223`, `227`, `220`, `218` |
| "Mi campaña no vende" | `267`, `266`, `248` + invoca `facebook_ads_lushows` |
| "¿Dónde consigo el producto?" | `110`, `116`, `120` + el módulo del país |
| "¿Cuánto cobro?" | `216`, `42`, `226` |
| "Me llegó el pedido tarde / rechazado" | `159`, `163`, `171` |
| "¿Cuántos productos puedo probar con X plata?" | `233`, `232`, `79` |
| "¿Contraentrega o cobro en la página?" | `30`, `32`, `158` |

### Cuándo NO usar esta skill

- Venta B2B o prospección en frío → `SDR_OUTBOUND_LUSHOW`
- Producto propio fabricado, no revendido → `economist_lushows` + `directorcreativo_lushows`
- Servicios, software, infoproductos → `economist_lushows` + `ventas_lushows`
- La duda es sobre la mecánica de la plataforma de ads → la skill de ads correspondiente
- Contabilidad, declarar, facturar → `contador_lushows`

## Para el usuario (Lushows)

Esta skill está construida para **operar**, no para leer. La forma de usarla es hacerle una pregunta
concreta de negocio y dejar que cargue los módulos que hagan falta.

**Preguntas que funcionan bien:**
- "Tengo $500 y quiero vender en México en diciembre, ¿por dónde arranco?"
- "Encontré este producto, aquí está el link, ¿sirve?"
- "Mi página tiene 800 visitas y 2 ventas, ¿qué está roto?"
- "¿Me conviene contraentrega o cobrar en la página?"
- "Dame 10 ángulos para vender este producto en México."

**Preguntas que funcionan mal:**
- "Enséñame dropshipping" (demasiado amplio; te va a preguntar el modo)
- "¿Cuál es el mejor producto?" (no existe fuera de un país, un precio y un ángulo)

## Convención de los módulos

- Los que dicen **(código)** traen un script ejecutable. Se ejecuta, no se lee.
- Los `playbook-<país>` son autocontenidos: puedes operar solo con ese y el `SKILL.md`.
- Los números entre comillas invertidas (`42`) son referencias cruzadas a otros módulos.
- Todo dato con fecha de vigencia lleva la fecha explícita. **Si tiene más de 6 meses, verifícalo
  en web antes de recomendarlo** — este oficio cambia por decreto.

## Mantenimiento

Cuatro cosas envejecen rápido y hay que revisarlas cada trimestre:

1. **Aranceles y de minimis** (`13`-`19`) — cambian por decreto, sin aviso.
2. **CPM por país** (`33`) — se mueven con la temporada y el año.
3. **Herramientas de espionaje** (`89`-`91`) — aparecen y mueren.
4. **Estado del proyecto activo** (bloque en `SKILL.md`) — el mercado y el modelo elegidos.

## Cómo pedirle a esta skill que se corrija

Si un dato quedó viejo (un arancel cambió, una herramienta murió), díselo y pide que actualice el
módulo concreto. No reescribas la skill entera: el valor está en que cada módulo es reemplazable
sin tocar los otros.

## Relacionados
`00` el método · `05` diagnóstico inicial · `09` frontera con otras skills · `08` glosario
