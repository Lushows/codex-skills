# 24 — Exclusiones y solapamiento

**Solapamiento** (overlap) es cuando dos audiencias contienen a la misma gente; **exclusión** es sacar explícitamente a un grupo de un ad set. Este módulo existe por una razón: no pagar dos veces por el mismo ojo, ni pagarle a Meta por mostrarle "¡compra ya!" a quien compró ayer. Léelo cuando tengas varios ad sets activos, cuando tu CPM suba sin explicación, o antes de lanzar cualquier retargeting (ver 23).

## La herramienta: Audience Overlap

En Ads Manager → **Audiences** → selecciona 2-5 audiencias guardadas (checkbox) → menú "..." → **Show audience overlap**. Te muestra qué % de una audiencia está contenido en la otra. Funciona con custom audiences y lookalikes guardados (no con el targeting "al vuelo" de un ad set — guarda la audiencia primero si quieres compararla).

## Cuándo el solapamiento IMPORTA y cuándo no

**Importa** cuando dos ad sets con el mismo objetivo le compiten a la misma gente al mismo tiempo: Meta no te subasta contra ti mismo directamente (deduplica la subasta puntual), pero la fragmentación hace que ninguno acumule conversiones, ambos quedan en aprendizaje eterno y el CPM efectivo sube. Síntoma clásico: dos ad sets "distintos" con resultados mediocres idénticos.

**NO importa** cuando es el mismo embudo en etapas distintas con mensajes distintos: que tu visitante de web esté también en tu broad de prospecting está bien SI el retargeting le dice otra cosa (ver 23 y 25). Ahí el solapamiento es diseño, no accidente — lo que controlas con exclusiones es la dirección (el comprador sale de todo lo de venta).

Regla 2026: con estructura consolidada (1-2 ad sets de prospecting, ver 10 y 20) y Advantage+ audience expandiéndose por default, el solapamiento entre ad sets casi desaparece como problema autoinfligido. Si tienes overlap del 50%+ entre ad sets activos, tu problema real es que sobran ad sets.

## Exclusiones esenciales (tabla de configuración)

| Excluir a | De dónde | Con qué público | Ventana |
|---|---|---|---|
| Compradores recientes | Prospecting Y retargeting | Evento Purchase del Dataset + customer list de clientes (cinturón y tirantes, ver 21/28) | 30-180d según ciclo de recompra |
| Leads ya captados | Campañas de lead gen | Lead form submitters + lista del CRM | 90d |
| Carrito activo | Prospecting (opcional) | AddToCart 7d | Para que solo les hable el retargeting con su mensaje específico |
| Empleados / competencia | Todo (si aplica y la lista es chica, opcional) | Customer list manual | Permanente |

Matiz importante — **productos de recompra**: si vendes consumibles (suplementos, comida, cosmética), NO excluyas compradores para siempre. Exclúyelos 30-60 días y deja que reentren, o monta mensaje de recompra aparte ("toca reponer"). Excluir 180d a un cliente de un producto que dura 30 días = regalarle la recompra a la competencia.

## Existing customers en Advantage+ Sales: el cap, no la exclusión

En **Advantage+ Sales** (el nuevo nombre de ASC desde 2025, ya no es un objeto separado tras el overhaul de feb-2026 — ver 12/90) NO excluyes clientes manualmente: defines tu **lista de clientes existentes** en la configuración y pones un **cap de clientes existentes** (% máximo del presupuesto que puede ir a quien ya te compró). El cap entró confirmado en **mar-2026**: arregla el viejo truco donde ASC inflaba el ROAS retargeteando a quien ya iba a comprar.

Recomendación práctica: **pon el cap en 25-30%** para forzar adquisición de gente NUEVA. Si no defines la lista de clientes existentes, la campaña les gasta lo que quiera y tu "ROAS de prospecting" es mentira (estás cosechando, no sembrando). Define la lista con tu customer list (ver 28) y manténla viva mensualmente.

## El anti-patrón clásico

Seis ad sets de intereses: "yoga", "vida sana", "fitness", "meditación", "bienestar", "nutrición". El Audience Overlap muestra 70-80% entre todos — es LA MISMA persona seis veces. Resultado: 6 ad sets en aprendizaje eterno repartiéndose las conversiones, CPMs inflados, y el reporte dice que "ningún interés funciona". Solución: consolidar en 1 ad set broad (o 1 con los intereses apilados como sugerencia Advantage+, ver 20), mismos creativos, y dejar que acumule señal (ver 10).

Cómo consolidar sin perder lo aprendido: identifica el ad set con más conversiones históricas, muévele los mejores creativos de los demás, súbele el presupuesto gradual (20% cada 3-4 días), y apaga el resto. No los borres aún (por si necesitas el historial de referencia).

## El costo de la fragmentación, en plata

Ejemplo con números redondos (COP): generas 60 conversiones/semana con $8M COP/semana.
- **6 ad sets solapados**: ~10 conversiones c/u → ninguno llega a las ~50/semana de la fase de aprendizaje (ver 13) → todos pagan el "impuesto de aprendizaje" (CPAs típicamente 20-50% peores que un ad set estabilizado). Si tu CPA estable es $45k y el fragmentado $60k, sobre 60 ventas son **$900k COP/semana tirados** solo por estructura.
- **1 ad set consolidado**: 60 conversiones → sale de aprendizaje en días → mismo presupuesto, más ventas.
La fragmentación no es desorden estético: es un sobrecosto real y medible todas las semanas. (Si el CAC resultante no cierra con tu LTV, eso es matemática de **economist_lushows**.)

## Plantilla de exclusiones por tipo de negocio

Copia la fila que aplique a tu negocio y configúrala en cada ad set de venta:

| Negocio | Excluir | Ventana | Por qué |
|---|---|---|---|
| E-com compra única (electrónica, deco) | Purchase + lista clientes | 180d | no recompra pronto |
| E-com consumible (suplementos, café, cosmética) | Purchase + lista | 30-60d luego reentra | la recompra es tu venta más barata |
| Servicios local (gym, clínica, estética) | clientes activos (lista) | mientras sean clientes | no le vendas la membresía a quien ya la tiene |
| Lead-gen B2B (ver 27) | lead form 90d + CRM | 90d | no recapturar al mismo lead |
| WhatsApp-first sin web | lista de compradores del bot/CRM | según ciclo | el bot ya los atiende; el ad busca nuevos |

Para WhatsApp-first sin píxel: tu única fuente de exclusión es la **customer list de quien ya compró** (export del CRM/Sheet con +57, ver 28). Sin píxel no hay evento Purchase, así que esa lista ES tu exclusión — manténla viva mensual o le hablas "compra ya" a clientes felices.

## Checklist mensual de higiene (5 minutos)

1. ¿Cuántos ad sets de prospecting activos? Si > 2-3 sin razón estructural (ver 10): consolidar.
2. Audience Overlap entre los que queden: > 40-50% = fusionar.
3. ¿Exclusión de compradores presente en TODOS los ad sets de venta? (Se borra fácil al duplicar campañas — revisa).
4. ¿Cap de clientes existentes definido en Advantage+ Sales (25-30%) y con lista cargada?
5. ¿La customer list de exclusión tiene más de 30 días sin actualizar? Re-subir (ver 28).
6. Columna Frequency semanal en retargeting: > 6-8 = audiencia chica o presupuesto grande; ajustar (ver 23).

## Errores comunes — blacklist

- Duplicar una campaña y olvidar que las exclusiones no viajan como esperabas: verifica el ad set duplicado campo por campo.
- Excluir compradores con UNA sola fuente (solo Dataset): si el evento se pierde (iOS, ver 14), el cliente reentra. Dataset + customer list.
- Exclusiones infinitas "para no molestar a nadie": cada exclusión reduce la audiencia y encarece; excluye lo esencial, no a todo el que parpadeó.
- Pelear el overlap entre prospecting y retargeting: ese solapamiento es el embudo funcionando; lo que diferencias es el MENSAJE.
- Advantage+ Sales sin lista de clientes existentes ni cap: tu mejor campaña gastando en gente que ya te compró sin que lo sepas.
- Excluir compradores 180d vendiendo un consumible de 30 días: te amputas la recompra, que es tu venta más barata.
- Confiar en que "Meta deduplica y ya": deduplica la subasta puntual, no te salva de la fragmentación de aprendizaje entre tus propios ad sets.
- Comparar overlap entre una audiencia de 200 personas y una de 2 millones: el % es engañoso con tamaños muy dispares; mira números absolutos también.
