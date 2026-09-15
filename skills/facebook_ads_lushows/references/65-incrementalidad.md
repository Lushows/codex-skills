# 65 — Incrementalidad: ¿esas ventas pasaban igual sin pauta?

La pregunta incómoda que separa al media buyer serio del que lee dashboards. **Incrementalidad** = las ventas que la pauta CAUSÓ, no las que se atribuyó. Meta (y toda plataforma) se acredita ventas que iban a ocurrir de todos modos: el cliente que ya tenía el producto en el carrito, el que te buscó por recomendación y de paso vio un ad. Lee este módulo cuando tu ROAS de plataforma se vea hermoso pero el banco no lo confirme (ver 61 capa 5, 64), o antes de escalar retargeting. Actualizado jun-2026.

## Por qué importa (con el caso típico)

El retargeting y las campañas de marca son los grandes auto-atribuidores: le muestran un ad a quien YA te conocía y estaba a un paso de comprar, y cuando compra, se anotan la venta. Resultado clásico: campaña de retargeting con "ROAS 12" que, al pausarla, no mueve las ventas totales — porque esa gente compraba igual. Cada peso ahí pudo ir a prospección (ventas nuevas de verdad). Lo mismo aplica a **Advantage+ Sales** cuando un % alto del gasto cae en clientes existentes — por eso en 2026 Meta agregó el **cap de clientes existentes** (mar-2026): puedes limitar el % de presupuesto que va a compradores actuales; **ponlo en 25–30%** para forzar adquisición nueva (ver `actualizacion-2026-06`).

**Contexto 2026 que ayuda:** Meta lanzó **atribución incremental** como ajuste en Ads Manager — usa ML contrafactual (entrenado con Conversion Lift) para optimizar por las conversiones que el anuncio causó, no last-touch. Reporta MENOS, y eso es bueno: acerca el ROAS de plataforma a la incrementalidad real. Pruébalo en cuentas con volumen. No reemplaza tus tests, pero reduce la brecha.

## Métodos, del más formal al más casero

### 1. Conversion Lift de Meta (formal)
Test científico: Meta divide tu audiencia en grupo expuesto y grupo de control (que NO ve tus ads) y compara ventas reales entre ambos. Es EL estándar y la base con la que se entrenó la atribución incremental. Disponible para cuentas con gasto grande (lo pides a tu representante o desde Experimentos si calificas). Si gastas pocos millones COP/mes, no es para ti todavía.

### 2. Geo-lift / geo-holdout casero (intermedio)
Apaga (o enciende) la pauta en una ciudad comparable y compara contra ciudades control. Es la herramienta que Meta misma recomienda validar el escalado en 2026 (con view-through fuera del API, los geo-holdouts ganaron peso). Receta:
1. Elige 2 ciudades con historial de ventas parecido y estable (ej.: Cali test, Bucaramanga control — NO Bogotá vs un pueblo).
2. Excluye Cali de la segmentación geográfica 2–4 semanas; todo lo demás igual.
3. Mide ventas reales (backend) por ciudad, antes vs durante, en ambas.
4. Incrementalidad ≈ caída en Cali − variación en Bucaramanga. Ej.: Cali cae 30%, Bucaramanga sube 2% → ~28% de tus ventas en Cali dependían de la pauta; el resto era orgánico/recurrente.
Precauciones: necesitas separar ventas por ciudad (dirección de envío sirve); evita semanas con festivos/quincena dispar; 2 semanas mínimo; una sola variable a la vez.

### 3. Test de pausa honesto (el más accesible para pyme)
Pausa SOLO el retargeting 2 semanas y observa ventas totales reales:
- Si Ads Manager decía que retargeting "generaba" COP 4M/mes y al pausarlo las ventas totales caen solo 1M → su incrementalidad real era ~25%; el resto era auto-atribución.
- Decisión: recorta retargeting a un presupuesto mínimo (frequency controlada, ver 39) y pasa la diferencia a prospección.
Hazlo en periodo estable (no en lanzamiento ni Q4) y avisa(te) que las 2 semanas pueden verse "peores" en plataforma aunque el negocio no lo sienta.

### 4. Señales blandas (monitoreo continuo, gratis)
- **MER estable al subir gasto** = el gasto nuevo trae ventas nuevas → incremental (ver 64, tabla semanal). MER que se desploma al escalar = estabas cosechando demanda existente.
- **Branded search / menciones**: si las búsquedas de tu marca y los "los vi en Instagram" en el chat suben con la pauta, hay efecto causal.
- **Correlación temporal**: días sin entrega de ads (rechazos, saldo) con ventas iguales = mala señal de incrementalidad.

## Cómo leer un test de incrementalidad (la fórmula)

```
Incrementalidad % = (Ventas con pauta − Ventas que habrían pasado sin ella) ÷ Ventas con pauta
ROAS incremental = (Ventas incrementales) ÷ Gasto
```
La trampa es estimar "ventas que habrían pasado": para eso sirve el grupo control (geo o tiempo). Sin control, lo mejor que tienes es tu baseline histórico estable. Un ROAS de plataforma 12 con incrementalidad 25% significa **ROAS incremental real ≈ 3** — sigue pudiendo ser rentable, pero no a $12 por peso. La decisión nunca es "apagar", es "¿cuánto de este gasto causa ventas que no pasaban?".

## Ejemplo resuelto: test de pausa de retargeting

Tienda con COP 6M/mes de pauta: 4.5M prospección + 1.5M retargeting. Ads Manager dice que retargeting genera 9M (ROAS 6) y prospección 9M (ROAS 2).
1. Semana base (4 semanas promedio): ventas totales reales del backend = 16M/mes.
2. Pausa retargeting 2 semanas → ventas reales de la quincena: 7.4M (esperado sin efecto: 8M).
3. Caída real ≈ 0.6M/quincena ≈ 1.2M/mes, NO los 9M que la plataforma atribuía → incrementalidad ~13%; ROAS incremental del retargeting ≈ 1.2M ÷ 1.5M = **0.8** (¡perdía plata real!).
4. Decisión: retargeting baja a 0.5M/mes (solo carritos abandonados, frequency limitada); el 1M liberado va a prospección, que sí mueve el MER.
5. Verificación al mes siguiente: ventas totales 16.8M con el mismo gasto total → la reasignación fue correcta.

## ¿Cuándo obsesionarse y cuándo no?

| Situación | Veredicto |
|---|---|
| Cuenta chica creciendo, casi todo prospección | NO te obsesiones: el MER semanal te basta (ver 64) |
| Retargeting/marca se llevan >25–30% del gasto | SÍ: test de pausa ya |
| Advantage+ Sales con % alto de existing customers | SÍ: pon el cap de clientes existentes en 25–30% y revisa el desglose |
| Gasto grande (decenas de millones COP/mes) | SÍ: geo-lift o Conversion Lift formal; activa atribución incremental |
| Ventas por WhatsApp con mucha recompra | SÍ parcial: separa nuevos vs recurrentes en el CRM (ver 53); la recompra que llega sola no se la debes a la pauta |

Regla práctica de presupuesto: si no has hecho ningún test, asume que el retargeting es ~20–40% incremental (no 100%) y dimensiónalo como minoría del gasto (5–15%); la prospección abierta suele ser mucho más incremental por definición — le habla a gente que no te conocía.

## Frontera con economist_lushows

La incrementalidad alimenta el modelo de negocio: el ROAS/CAC **incremental** (no el de plataforma) es el que entra al unit economics real, a la decisión de cuánto presupuesto sostiene el margen, y al cálculo de LTV vs CAC. Cuando el test te dé el número causal, lleva ESE a economist_lushows para modelar viabilidad y techo de gasto — no el inflado.

## Errores comunes — blacklist
- Creer el ROAS de retargeting a valor nominal y "escalarlo" (solo pagas peaje sobre ventas que ya eran tuyas).
- Hacer test de pausa en temporada alta o durante un lanzamiento y concluir cualquier cosa.
- Geo-lift con ciudades no comparables o sin poder separar ventas por ciudad.
- Pausar TODO en vez de una pieza: no aprendes qué parte era incremental.
- Confundir correlación de un solo día con causalidad: mínimo 2 semanas por test.
- Usar la incrementalidad como excusa para no pautar: el punto es REASIGNAR plata hacia lo que sí causa ventas, no apagar el motor.
- Ignorar el cap de clientes existentes en Advantage+ Sales y dejar que la campaña retargetee gratis a quien ya compraba.
- Llevar el ROAS de plataforma (no el incremental) al modelo de negocio: infla el techo de gasto y te lleva a sobreinvertir.
