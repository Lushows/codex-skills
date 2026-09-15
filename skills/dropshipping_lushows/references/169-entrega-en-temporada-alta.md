# Entrega en temporada alta

> En Q4 todo lo que funciona el resto del año se degrada: la paquetería se satura, el tránsito se
> alarga, el proveedor se llena y el cliente se vuelve intolerante porque **compró para una fecha**.
> Un retraso de tres días en marzo es una molestia; el 24 de diciembre es un reembolso.

## Qué se degrada y cuánto

| Variable | Resto del año | Q4 pico |
|---|---|---|
| Última milla urbana | 1-3 días | +1 a +3 días |
| Última milla rural | 3-6 días | +2 a +5 días |
| Tránsito aéreo China | Ver `146` | +2 a +5 días por saturación |
| Tarifa aérea | USD 6-8/kg | Sube; verificar semana a semana |
| Espacio en avión | Disponible | Escaso: tu carga puede quedar en tierra ("rolling") |
| Aduana | 3-10 días | Extremo alto del rango |
| Tolerancia del cliente | Media | **Cero** |
| CPA de los anuncios | Base | Sube fuerte |

## El calendario Q4-2026

| Fecha | Evento | Mercado |
|---|---|---|
| **13-17 nov** | **Buen Fin** | México |
| **27 nov** | Black Friday | Global |
| **30 nov** | Cyber Monday | Global |
| **20 dic** | Límite de aguinaldo (MX) y prima (CO) | MX, CO |
| **24 dic** | Navidad | Global |
| **26 dic** | Boxing Day | Reino Unido |
| **6 ene** | Reyes | ES, MX, CO |

El **20 de diciembre** es el dato menos conocido y más útil: es el límite legal para pagar aguinaldo
en México y prima en Colombia. Hay una inyección de liquidez masiva justo antes de Navidad. La gente
tiene dinero y quiere gastarlo rápido — pero solo sirve si tienes stock y puedes entregar.

## Fechas de corte para pedir desde China

Con tránsito de 15 días + 3 de holgura:

| Objetivo | Último día para pedir |
|---|---|
| **Black Friday (27 nov)** | **9-nov-2026** |
| **Navidad (24 dic)** | **6-dic-2026** |
| **Reyes (6 ene)** | **19-dic-2026** |

Tabla completa por mercado y modo en `170`.

## La regla de oro de la temporada

> **Compra el stock de temporada con 30-45 días de anticipación sobre lo que creas que necesitas, y
> nunca prometas una fecha que dependa de un embarque que todavía no salió.**

Quedarse sin stock en la semana del Buen Fin cuesta más que sobrar inventario en enero. El
inventario sobrante se liquida; la temporada perdida no vuelve hasta dentro de un año.

## Cómo se planifica el stock

1. Calcula tu venta diaria promedio de las últimas 4 semanas normales.
2. Multiplica por el factor de temporada: **2-4× en la semana pico**, 1,5-2× en el mes.
   *Verificar contra tus propios datos del año anterior si los tienes.*
3. Suma los días de reposición reales (`146`). Si no puedes reponer, todo el stock entra antes.
4. Resta lo que ya tienes.
5. Divide en dos pedidos: el grueso temprano por el modo barato, y un refuerzo aéreo con fecha de
   corte propia.
6. Define el punto en el que **apagas la pauta** por falta de stock, y respétalo.

## Ajustar la promesa de entrega

En temporada, el rango de entrega se recalcula con el **percentil 90 de la peor semana**, no del
promedio anual. Ver `157`.

| Antes | Durante el pico | Después del corte |
|---|---|---|
| "Llega en 2-5 días" | "Llega en 3-7 días" | "Llega después del 26 de diciembre" |

Cambiar el mensaje cuando pasa la fecha de corte es obligatorio. Seguir vendiendo "llega antes de
Navidad" el 22 de diciembre es publicidad engañosa y reembolso garantizado.

## El contador regresivo, bien usado

Publicar "Pide antes del {fecha} para recibir antes de Navidad" hace tres cosas a la vez:

1. Genera urgencia real (no inventada).
2. Te protege: después de esa fecha nadie puede reclamarte la entrega.
3. Concentra la demanda antes del colapso de la paquetería.

Es la única urgencia que puedes usar sin mentir. Úsala.

## Año Nuevo Chino 2027: el otro pico

| Dato | Valor |
|---|---|
| Fecha del día 1 | **6-feb-2027** |
| Feriado oficial | **4-12 feb 2027** |
| Desaceleración previa | **3-4 semanas antes** (empieza ~mediados de enero) |
| Recuperación | **6-8 semanas** después |

Esto significa: pedidos puestos después de mediados de enero de 2027 pueden no producirse hasta
marzo. Si tu plan incluye reponer en enero o febrero, **el pedido se hace en diciembre**. Es la
trampa que sorprende a todo el que arranca en Q4 y planea escalar en Q1.

## Lo que se prepara antes, no durante

| Preparativo | Cuándo |
|---|---|
| Plantillas de WhatsApp aprobadas en Meta | 2 semanas antes mínimo (`162`) |
| Segunda transportadora contratada | Antes de noviembre |
| Guiones de retraso escritos (`171`) | Antes |
| Fecha de corte publicada en la web | Antes de Black Friday |
| Stock de empaque e insertos | Con el lote |
| Quién empaca en el pico | Antes: contratar en diciembre es imposible |
| Tablero con alertas diarias (`174`) | Funcionando desde octubre |

## El error que se repite cada año

Escalar la pauta el día que el producto despega, sin verificar cuánto stock queda ni cuántos
pedidos puede empacar la operación. Resultado: vendes 300 y despachas 120, los otros 180 se
enfurecen, y el ahorro de la campaña se va en reembolsos. **Antes de subir presupuesto, mira el
inventario y la capacidad de empaque.**

## Relacionados
`170` fechas de corte Q4-2026 · `146` tiempos de tránsito · `157` comunicar la entrega ·
`171` cuando se atrasa · `174` tablero · invoca `facebook_ads_lushows` para la pauta de temporada
