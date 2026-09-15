# 30 — El stack de outbound

El "stack" es el conjunto de herramientas con las que corres tu máquina de outbound. La trampa del principiante es empezar comprando herramientas ("me suscribo a Apollo y ya"). Al revés: primero defines el **flujo** (ICP → lista → datos → envío → cadencia → CRM → medición) y luego pones **una herramienta por cada etapa**, no cinco que hacen lo mismo. Este módulo es el mapa de las 6 categorías, qué hace cada una, y cómo armar tu stack según cuánto tengas para gastar. Es la puerta de entrada al Bloque 3.

## Las 6 categorías (todo stack de outbound cabe aquí)

| # | Categoría | Qué resuelve | Herramientas típicas | Módulo a fondo |
|---|---|---|---|---|
| 1 | **Datos / sourcing** | Encontrar cuentas y contactos, sus correos y teléfonos | Apollo, ZoomInfo, Cognism, Lusha, RocketReach, Hunter, Sales Navigator | ver `25`, `100`, `102` |
| 2 | **Enrichment / orquestación** | Enriquecer, cruzar fuentes, calcular, personalizar a escala | **Clay**, Clearbit, waterfalls | ver `29`, `31`, `130` |
| 3 | **Sending / sequencers** | Enviar cold email a volumen y correr cadencias | Instantly, Smartlead, Lemlist, Apollo, Outreach, Salesloft | ver `33`, `103`, `104` |
| 4 | **Deliverability** | Que el correo llegue a bandeja, no a spam | dominios+buzones (Google Workspace), warmup, Postmaster | ver `40`–`46`, `110`–`118` |
| 5 | **CRM** | La base de verdad: contactos, deals, estados, handoff | HubSpot, Pipedrive, Salesforce | ver `32`, `141` |
| 6 | **Señales / intent** | Contactar en el momento correcto (trigger) | Bombora, G2, RB2B, Warmly, LinkedIn | ver `36`, `37`, `131` |

A esto se suma el **pegamento** (integraciones: Zapier/Make/n8n/webhooks, ver `34`) que conecta las 6 y la **IA** que personaliza a escala (ver `35`). Un mapa visual de cómo encajan → `39`.

## El principio: una herramienta por trabajo, no por marca

Muchas herramientas se solapan (Apollo hace datos **y** sequencer **y** mini-CRM). Eso tienta a "hacerlo todo en Apollo". Regla práctica:

- **Al arrancar**, consolidar reduce fricción: Apollo solo (datos + envío ligero) + una hoja/CRM básico es un stack válido para las primeras 500–1.000 cuentas.
- **Al escalar volumen**, se **separa el envío del dato**: los datos en Apollo/Clay, pero el envío en una herramienta dedicada de deliverability (Instantly/Smartlead) con dominios y buzones propios. ¿Por qué? Porque enviar cold email a volumen desde la misma herramienta que todos usan quema la reputación compartida; los sequencers dedicados te dan buzones e IPs bajo tu control (ver `41`, `44`).

Regla de oro: **el dato y el envío son dos negocios distintos.** No los cases solo porque una herramienta ofrece ambos.

## Cómo elegir según presupuesto

Piensa en tres niveles. Los precios son órdenes de magnitud 2026 (USD/mes), varían por asientos y créditos.

| Etapa | Presupuesto/mes | Datos | Enrichment | Sending + deliverability | CRM | Señales |
|---|---|---|---|---|---|---|
| **Bootstrap** (validar, 1 persona) | ~$100–300 | Apollo Basic (~$49–99) | — (Apollo enriquece) | Instantly Growth (~$37) + 2–3 dominios (~$6/dominio) + warmup incluido | HubSpot Free / Pipedrive (~$15) | LinkedIn + alertas manuales |
| **En marcha** (buscando escala) | ~$500–1.500 | Apollo Pro + Sales Navigator (~$99) | **Clay Starter/Explorer** (~$149–349) | Smartlead/Instantly Hypergrowth (~$97) + 5–15 buzones | HubSpot Starter/Pro | Clay señales + RB2B free |
| **Escala / equipo** | $2.000+ | ZoomInfo/Cognism (contrato anual, $$$) | Clay Pro + waterfalls | Smartlead a volumen (decenas de buzones) o Outreach/Salesloft | HubSpot/Salesforce | Bombora/6sense/G2 |

Lógica de la escalera:
1. **No pagues ZoomInfo/Cognism hasta que Apollo no te alcance.** ZoomInfo cuesta miles al año y solo se justifica cuando necesitas cobertura/telefonía verificada a escala o mercados donde Apollo falla (ver `25`).
2. **Clay entra cuando la personalización manual ya no escala** — cuando pasas de "escribo 30 correos a mano" a "necesito 500 correos relevantes/semana" (ver `31`).
3. **La deliverability no es opcional en ningún nivel.** Aunque estés en bootstrap, los dominios secundarios + warmup son obligatorios desde el correo #1 (ver `41`). Es lo barato que evita lo caro (quemar tu marca).
4. **El CRM puede empezar gratis** (HubSpot Free) pero necesita existir desde el día 1: sin base de verdad, pierdes leads y no puedes hacer handoff al vendedor (ver `32`, `73`).

## Ejemplo: stack mínimo real para un negocio de servicios en LatAm

Meta: 10 reuniones/mes vendiendo un servicio B2B, presupuesto ~$250/mes.

```
Datos      → Apollo Basic ($49) — cuentas por nicho + correos verificados
Enrichment → dentro de Apollo (sin Clay todavía)
Sending    → Instantly ($37) + 3 dominios secundarios ($18) + 6 buzones Google Workspace ($36)
Warmup     → incluido en Instantly
CRM        → HubSpot Free ($0)
Señales    → Sales Navigator Core ($99) para triggers de cargo/empresa
WhatsApp   → outbound manual/API para LatAm (ver 47, 59)
                                              ───────────
                                       TOTAL ≈ $239/mes
```
Con esto envías ~120–180 correos/día seguros (6 buzones × 20–30), suficiente para llenar una agenda pequeña. Cuando el volumen te pida más relevancia, agregas Clay; cuando pidas más buzones, subes el plan de Instantly.

## Errores comunes

- **Comprar antes de definir el flujo.** Terminas pagando 5 tools que se solapan. Define el flujo (`39`) primero.
- **Enviar cold email desde el dominio principal de la empresa** por ahorrarte los dominios secundarios. Es el error más caro: quemas la reputación de tu correo real (ver `41`).
- **Saltar el CRM.** "Lo llevo en un Excel" funciona hasta el lead 50; después pierdes seguimientos y no hay handoff limpio (ver `77`).
- **Sobre-optimizar el stack antes de tener resultados.** Con 0 reuniones agendadas no necesitas ZoomInfo ni Clay Pro; necesitas mandar la primera campaña.

## Siguiente paso

Define en qué nivel estás (bootstrap / en marcha / escala) y arma la tabla de tu stack con **una herramienta por categoría**. Luego profundiza en la pieza central del outbound moderno: Clay (`31`), tu CRM (`32`) y tu sequencer (`33`). Para ver cómo se conecta todo de punta a punta → `39`. Para reducir el costo de la IA que uses en personalización → `optimizer_tokens_lushows`.
