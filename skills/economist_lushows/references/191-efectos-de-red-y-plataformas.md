# 191 — Efectos de red y plataformas

Cómo pensar negocios donde el valor crece con cada usuario (marketplaces, plataformas, apps sociales): cómo arrancar sin morir en el problema del huevo-gallina y cómo volverte difícil de copiar.

## Qué es un efecto de red (sin tecnicismos)
Un **efecto de red** existe cuando cada usuario nuevo hace que el producto valga MÁS para los demás usuarios. Un teléfono solo es inútil; el segundo teléfono crea valor; un millón de teléfonos crean una red imparable.

No confundir con "tener muchos clientes". Una panadería con mil clientes NO tiene efecto de red: el cliente 1001 no mejora la experiencia del cliente 1. En un marketplace de comida (tipo Rappi), cada restaurante nuevo SÍ mejora la app para todos los comensales, y cada comensal mejora el negocio para todos los restaurantes.

Tipos principales:
- **Directo (de un lado):** más usuarios = más valor para usuarios iguales. Ej.: WhatsApp, una red social.
- **Indirecto / cruzado (dos lados):** más de un lado atrae al otro. Ej.: marketplace (compradores ⇄ vendedores), app de transporte (pasajeros ⇄ conductores). Esto es lo más común en negocios reales.
- **De datos:** más uso = mejores recomendaciones = más uso. Ej.: motor de búsqueda, recomendador.

## El problema del huevo y la gallina
En una plataforma de dos lados nadie quiere ser el primero: los vendedores no entran si no hay compradores, y los compradores no entran si no hay vendedores. **Vacío + vacío = nada.** Es la causa #1 de muerte de marketplaces.

Cómo se rompe (tácticas probadas, elige según tu caso):
- **Subsidiar un lado** (ver abajo): regalar valor al lado más difícil de conseguir.
- **Arrancar de un solo lado primero** ("single-player mode"): que el producto sea útil para UN usuario aunque no haya red todavía. Ej.: una herramienta de agenda que sirve sola y luego se conecta.
- **Ciudad/nicho por ciudad/nicho** ("go narrow"): no lances en todo el país; domina una zona o un nicho hasta tener densidad, luego expande. La densidad local importa más que el total nacional.
- **Sembrar oferta a mano** ("do things that don't scale"): tú mismo cargas los primeros vendedores/productos/contenido para que el primer comprador ya encuentre algo.
- **Robar de otra plataforma:** importar oferta/usuarios de un lugar donde ya existen (con permiso y cuidando reglas).

## Qué lado subsidiar (la decisión clave)
En un mercado de dos lados, casi siempre subsidias (das gratis o barato) al lado **más difícil de atraer y más sensible al precio**, y cobras al lado que más valor recibe.

Pregúntate, lado por lado:
| Pregunta | Si responde "este lado" → considéralo el subsidiado |
|---|---|
| ¿Cuál es más escaso / difícil de conseguir? | Ese lado |
| ¿Cuál es más sensible al precio? | Ese lado |
| ¿Cuál atrae al otro con más fuerza? | Ese lado (su presencia es el imán) |
| ¿Cuál tiene más alternativas (más fácil que se vaya)? | Ese lado |

El lado que se queda y monetizas es el que obtiene valor claro y tiene menos alternativas. Regla práctica: **subsidia la oferta cuando la oferta es el cuello de botella; subsidia la demanda cuando ya tienes oferta esperando.**

## Ventaja defensiva (por qué no te copian fácil)
Un competidor puede copiar tu app en un mes. Lo que NO puede copiar es tu red. La defensa real viene de:
- **Densidad / liquidez:** suficiente oferta y demanda para que cada quien encuentre match rápido. Liquidez = probabilidad alta de que una búsqueda termine en transacción.
- **Costos de cambio:** historial, reputación, reseñas, saldos, integraciones que se pierden al irse.
- **Multi-homing difícil:** si a un usuario le cuesta usar dos plataformas a la vez, tiende a quedarse en la dominante. Si es fácil (como pedir en dos apps de delivery), tu foso es débil → necesitas otra defensa (marca, exclusividad, precio).

Esto se conecta con foso competitivo (ver 44) y con cómo defender el negocio a largo plazo. Mide la liquidez como KPI, no la "sensación de tracción".

## Ejemplo numérico (cifras ilustrativas)
Marketplace local de clases particulares: un lado son **profesores** (oferta), otro son **estudiantes** (demanda). Decides subsidiar la oferta porque sin profesores no hay nada que buscar.

Supuestos de ejemplo (inventados para ilustrar el cálculo, no datos de mercado):
- Lanzas en UNA ciudad. Siembras a mano 40 profesores el mes 0 (los reclutas tú, comisión 0% los primeros 3 meses = subsidio).
- Cada estudiante que llega y encuentra ≥3 profesores de su materia → "match" → reserva. Sin densidad, no reserva.
- Comisión que cobras al cerrar: 15% sobre clase de $50.000 = **$7.500 por transacción** (cobrada al estudiante vía precio, el lado que recibe valor).

Mes 3, con densidad lograda:
- 40 profesores activos, 300 estudiantes, 600 clases/mes.
- Ingreso = 600 × $7.500 = **$4.500.000/mes**.
- Liquidez (KPI): 70% de búsquedas terminan en reserva. Si bajara a 30%, la red "no cuaja" y debes meter más oferta, no más publicidad.

Lección del ejemplo: el dinero NO entró el mes 0. Primero pagaste densidad (subsidio + trabajo manual); la monetización llega cuando la liquidez es alta. Modela esto en tu flujo de caja (ver 53) o te quedas sin efectivo antes de que la red despegue.

## KPIs clave de una plataforma
- **Liquidez:** % de búsquedas/intentos que terminan en transacción. El número más importante.
- **Ratio entre lados:** ej. estudiantes por profesor; si se desbalancea, un lado se frustra y se va.
- **Densidad geográfica/nicho:** oferta disponible dentro del radio/categoría útil para el usuario.
- **Repeat rate / frecuencia:** % que vuelve. Sin recompra, la red no se sostiene (ver 128).
- **Take rate:** % que te quedas por transacción (tu comisión). Súbelo solo cuando el valor sea innegable.
- **GMV** (valor total transado) vs. **ingreso real** (GMV × take rate). No confundas: GMV no es tu dinero.

## Cómo arrancar mínimo viable
1. Elige UN nicho o UNA ciudad pequeña y defínelo estrecho (ver 102 sobre nicho).
2. Decide el lado a subsidiar con la tabla de arriba.
3. Siembra a mano la oferta (carga los primeros 20–50 vendedores/profesores/listados tú mismo).
4. Trae demanda muy enfocada a ese nicho; mide LIQUIDEZ, no descargas.
5. Solo cuando la liquidez sea alta y haya recompra, sube comisión y expande a otra zona/nicho.

## Errores comunes
- **Lanzar nacional desde el día 1:** dispersas la densidad y nadie encuentra match. Empieza concentrado.
- **Medir descargas/registros en vez de liquidez:** miles de registros sin transacciones = red muerta.
- **Subsidiar al lado equivocado:** quemas caja atrayendo demanda cuando el cuello de botella era la oferta.
- **Cobrar take rate alto demasiado pronto:** ahogas la transacción antes de tener costos de cambio que retengan.
- **Ignorar el multi-homing:** si es trivial usar a tu competidor en paralelo, no tienes foso real (ver 44).
- **Confundir GMV con ingreso:** presumes "$X millones transados" pero tu negocio vive del take rate.
- **Creer que tienes efecto de red cuando solo tienes muchos clientes:** revisa si el usuario N+1 mejora la experiencia del usuario N. Si no, es un negocio normal, no una plataforma.

> Recordatorio de país: comisiones, IVA sobre la comisión, retención a vendedores, reglas de pasarela de pago y responsabilidad de plataforma varían por país/ciudad. Antes de fijar take rate o estructura, pregunta país/ciudad y verifica reglas fiscales y legales vigentes (ver 21 para conseguir datos reales).

## Siguiente paso típico
Define en una frase tu efecto de red ("cada ___ que entra hace que ___ valga más para ___"), elige el lado a subsidiar con la tabla, y fija TU liquidez objetivo para UNA ciudad/nicho antes de gastar un peso en publicidad masiva.
