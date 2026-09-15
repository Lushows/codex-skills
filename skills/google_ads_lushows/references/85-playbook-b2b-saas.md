# 85 — Playbook B2B/SaaS

Lee este módulo cuando vendes **software, SaaS o un servicio B2B** — como FACTUM/AVISPA'O (asistente de cumplimiento para pymes vía WhatsApp). El B2B es otro animal: el ticket es alto, el ciclo de venta es **largo** (días o semanas, no minutos), decide más de una persona, y el "lead" no es la venta — es el comienzo. Google **captura** al decisor que tiene un dolor concreto y busca solución ("software de facturación electrónica DIAN", "cómo cumplir con SST mi empresa"). Aquí Search rinde porque la intención es altísima, pero hay que medir por **valor de lead que cierra**, no por volumen de formularios. El cierre largo y consultivo se trabaja en `ventas_lushows`; la viabilidad, el LTV y el CAC en `economist_lushows`. Para GENERAR demanda donde el decisor aún no busca, Meta/LinkedIn complementan (ver `facebook_ads_lushows`).

## Estructura: alta intención + lead magnet

En B2B no vendes en el primer clic. Capturas un lead calificado y lo nutres. La estructura, con presupuestos de referencia COP:

| Campaña | Tipo | Puja | Presupuesto arranque | Rol |
|---|---|---|---|---|
| Marca | Search | tCPA bajo | $8.000–18.000/día | Defiende; competidores pujan sobre tu nombre |
| Alta intención | Search | tCPA o Max. conv. (valor) | $30.000–70.000/día | "software cumplimiento pymes", "facturación electrónica DIAN" |
| Lead form | Search + lead form asset | tCPA | $15.000–35.000/día | Capturar lead sin que salga del buscador (ver 52) |
| Demand Gen (nutrir) | Demand Gen | tCPA | $15.000–30.000/día | Lead magnet a decisores que aún no buscan (ver 41) |

- **Keywords de altísima intención, presupuesto enfocado.** En B2B prefieres POCAS keywords muy intencionadas a muchas amplias. "Software facturación electrónica Colombia", "cómo cumplir RUT y cámara de comercio", "asistente cumplimiento pyme", "obligaciones tributarias pyme [año]". Cada una vale oro porque el que la busca es un decisor con dolor. Benchmark COP: el CPC de estas keywords B2B corre alto, **$2.000–10.000+**, porque la competencia es de empresas con bolsillo — pero un cliente de $200.000/mes con buen LTV lo justifica.
- **Lead magnet, no venta directa.** El B2B se gana ofreciendo valor primero: una guía ("Checklist de cumplimiento para tu pyme 2026"), una demo, una prueba gratis, una calculadora, un diagnóstico. El anuncio promete ESO, no "compra ya".
- **Lead form asset** para capturar sin fricción de landing, PERO ojo: el lead form trae más volumen y MENOS calidad. Para B2B de ticket alto, a veces una landing con un poco de fricción filtra mejor (ver abajo y 52).
- **Demand Gen** (reemplazó a Discovery, ver actualizacion-2026-06) es tu campaña visual dentro de Google — YouTube/Gmail/Discover — para poner el lead magnet frente a perfiles de decisor que todavía no buscan. Es la opción "tipo Meta" de Google.

## Filtrar al consumidor: exclusiones y negativas

El error más caro del B2B en Google: pagar por **consumidores finales** cuando vendes a empresas. Si vendes "facturación electrónica para empresas" y no filtras, te llega gente buscando "cómo hacer una factura para mi mamá", estudiantes, o personas naturales.

**Negativas y exclusiones B2B (ver 22):**
- Negativas: "gratis", "empleo", "trabajo", "curso", "cómo se hace una factura", "plantilla", "qué es" (informacional puro), "ejemplos de", "personal".
- **Excluir consumidor:** términos que delaten a alguien que no es empresa.
- Si tu producto es para cierto tamaño/sector de empresa, las negativas filtran el resto.
- Con **AI Max / broad + Smart Bidding** (lo moderno en 2026), Google expande tus términos: eso hace los **negativos a nivel cuenta MÁS importantes que nunca** o se va a consultas de consumidor (ver actualizacion, 22).

**Calidad de lead > cantidad de lead.** En B2B, 5 leads buenos valen más que 50 basura. Configura tu puja y tus exclusiones para traer DECISORES, no curiosos. Mejor un costo por lead más alto pero que cierra.

**Lead form vs landing — la decisión que define la calidad.** El lead form asset captura dentro de Google (sin salir del buscador): trae más volumen, más barato, pero más curioso. Una landing propia con un poco de fricción (pide nombre de la empresa, NIT, tamaño, necesidad) trae menos leads pero más calificados. Para ticket bajo/medio, lead form; para ticket alto y ciclo largo (FACTUM/AVISPA'O con clientes que valen millones al año), la landing con fricción filtra mejor y te ahorra tiempo de ventas persiguiendo gente que no era. Puedes correr ambos y comparar costo por lead CERRADO, no por lead capturado (ver 52).

## OCI por valor de lead: cerrar el loop del ciclo largo

Esta es la pieza que separa al B2B que escala del que se estanca. El ciclo es largo: el lead entra hoy, conversa por WhatsApp/llamada, evalúa, y cierra en 2–4 semanas. Si Google solo ve "lead capturado", optimiza a volumen de leads — y te llena de leads que nunca cierran.

**OCI por valor de lead (ver 53 OCI, 58 high-ticket):**
1. Cuando el lead entra, guarda su **GCLID** (el identificador del clic que lo trajo).
2. Mueve el lead por tu pipeline: lead → calificado (MQL) → demo → propuesta → cliente.
3. Sube de vuelta a Google la conversión en cada etapa que importe, **con su valor real**. Un lead que se vuelve cliente de un plan de $200.000/mes vale muchísimo más que uno que pidió info y desapareció.
4. Optimiza a **valor**, no a cantidad. Así Google aprende a traerte los leads que se parecen a los que CIERRAN y pagan más. Activa **Enhanced Conversions for leads** (datos first-party hasheados) como base — es el piso 2026 para que OCI funcione bien (ver actualizacion).

Para AVISPA'O específicamente: el lead entra por el asistente de WhatsApp; el GCLID viaja en el link. Cuando ese lead se vuelve cliente que paga, esa conversión-valor sube a Google. Sin esto, Google optimiza a "inicié conversación" — que en B2B no es nada, porque medio mundo escribe "info" y desaparece.

**Presupuesto y paciencia:** el B2B tarda en mostrar ROAS porque el ciclo es largo. No mates una campaña a las 2 semanas porque "no ha vendido" — el lead de la semana 1 puede cerrar en la semana 4. Mide con ventana de conversión larga (ver 60, 64). Y calcula tu costo por lead máximo desde el LTV: si un cliente vale $2.400.000 al año y cierras 1 de cada 8 leads calificados, puedes pagar bastante por lead — ese número lo da `economist_lushows`, no la intuición.

## Errores comunes — blacklist

1. **No filtrar al consumidor final.** Pagas clics de gente que no es empresa. Negativas y exclusiones agresivas a nivel cuenta: "gratis", "curso", "qué es", "plantilla" (ver 22).
2. **Optimizar a volumen de leads.** Te llenas de formularios que nunca cierran. Optimiza a valor de lead con OCI (ver 53).
3. **Vender en el primer clic.** El B2B no compra de inmediato; ofrece lead magnet (guía, demo, prueba) y nutre. Venta directa espanta.
4. **Matar la campaña a las 2 semanas.** El ciclo es largo; el lead de hoy cierra en semanas. Usa ventana de conversión larga y paciencia (ver 64).
5. **Lead form sin filtro.** Trae volumen barato pero basura. Para ticket alto, a veces una landing con fricción filtra mejor (ver 52).
6. **No defender la marca.** En B2B los competidores pujan sobre tu nombre para robarte el decisor. Cubre marca (ver 39).
7. **No subir el valor real del lead a Google.** Si todos los leads "valen igual", Google no sabe a cuáles parecerse. Sube el valor por etapa (ver 53, `economist_lushows` para el LTV).
8. **Ignorar Enhanced Conversions.** Sin señal first-party, OCI y Smart Bidding optimizan a ciegas. Actívalo, es el piso 2026 (ver actualizacion).
