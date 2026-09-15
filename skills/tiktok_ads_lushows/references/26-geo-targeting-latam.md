# 26 — Geo-targeting LatAm

**Geo-targeting** = dónde, geográficamente, le muestras tus anuncios. Es una de las pocas cercas DURAS que el algoritmo de TikTok respeta de verdad (ver 20), no una sugerencia que ajusta a su antojo. Lee este módulo cuando solo despachas en ciertas ciudades, cuando trabajas con contraentrega/pago contra entrega, o cuando tu CPA se ve bien pero las ventas no cuadran porque media pauta cae donde no puedes vender. En LatAm, el geo mal puesto es una de las fugas de plata más silenciosas que existen.

## La regla madre: anuncia SOLO donde entregas

Si despachas únicamente en Bogotá, anunciar "Colombia" entero significa pagar impresiones a gente de Pasto, Quibdó y Leticia a la que **jamás** le vas a vender. El algoritmo, además, optimiza hacia el clic más barato — y los clics baratos suelen venir de zonas de bajo poder adquisitivo o de gente que nunca podrá recibir tu producto. Resultado: CPM bonito, CPA engañoso, cero ventas reales. El panel te miente con un costo por clic lindo mientras tu caja registradora no se mueve.

| Tu operación | Geo correcto |
|---|---|
| Despacho nacional con transportadora | País completo (o excluye zonas sin cobertura del courier) |
| Tienda física + domicilio local | Ciudad + radio de los barrios que cubres |
| Contraentrega por zona | SOLO las ciudades/zonas donde el courier hace contraentrega |
| Servicio presencial (restaurante, taller) | Ciudad + radio realista de desplazamiento del cliente |
| Producto digital (ej. Calculadora Gastro, ver CLAUDE.md) | Donde está tu mercado y tu pago funciona; puedes ir amplio |

## Contraentrega: el caso LatAm clásico

El **pago contra entrega** (contraentrega) sigue siendo enorme en LatAm en 2026 porque mucha gente aún no confía en pagar online, sobre todo fuera de las capitales. Pero solo funciona donde el transportador lo ofrece. Reglas:

- Anuncia SOLO las ciudades/zonas con cobertura de contraentrega de tu courier (verifica la lista REAL con ellos, no asumas; Coordinadora, Servientrega, Interrapidísimo y demás tienen mapas de cobertura distintos).
- Excluye zonas rurales o de difícil acceso donde el flete mata el margen — valida con `economist_lushows` si la contraentrega a zona X deja utilidad después de flete ida y, en caso de rechazo, vuelta.
- Si una ciudad tiene alta tasa de "rechazo en la puerta" (pedidos que nadie recibe), exclúyela: cada rechazo es **flete perdido ida y vuelta** más el producto inmovilizado. En contraentrega la tasa de rechazo, no el CPA, suele ser la métrica que decide si una ciudad es rentable.

Truco 2026: para zonas de rechazo alto, no las excluyas del todo — cámbialas a **prepago** (PSE, Nequi, Bold, Wompi). Así sigues vendiendo ahí sin asumir el flete de los que no reciben. Para integrar esos pagos, ver `engineer_visualopen_lushows` (pagos LatAm) o coordina con quien maneje tu checkout.

## Cómo se configura (acciones exactas)

1. Ad group → Location / Targeting → Location.
2. Elige **Include**: escribe las ciudades reales (Bogotá, Medellín, Cali...) o el país si entregas nacional. TikTok permite ciudad y, en algunos casos, regiones/DMA.
3. Usa **Exclude** para sacar zonas sin cobertura aunque estén dentro del país incluido.
4. Para servicio local, usa el radio/punto en el mapa alrededor de tu local (ej. 10-15 km de tu restaurante).
5. Idioma: español (ver 20) para no gastar en impresiones de otro idioma.
6. Nombra el ad group con el geo: `BROAD_Bogota_Medellin` — te ahorra confusiones al escalar y al leer reportes.

## Trampas del geo amplio

| Trampa | Síntoma | Arreglo |
|---|---|---|
| "Colombia" entero pero despachas en una ciudad | CPM bajo, CPA "bueno", ventas reales escasas | Acota a tus ciudades de entrega |
| Incluir ciudades sin contraentrega | Pedidos que no se pueden completar | Excluir o pasar a prepago en esas zonas |
| Geo nacional para servicio presencial | Leads de gente que vive a 8 horas del local | Radio alrededor del local |
| Mezclar países LatAm en un solo ad group | Imposible leer qué país rinde; moneda/envío distintos | Un ad group por país |
| No excluir zonas de alto rechazo | Flete quemado en contraentrega | Excluir tras ver la data de rechazos |
| Geo muy chico (un solo barrio) | El algoritmo no tiene a quién mostrar; no entrega | Amplía a ciudad o varios barrios |

## Escalar geo: ciudad por ciudad

Cuando una ciudad funciona y quieres más volumen:

1. **No abras el país de golpe.** Añade ciudades de a una o dos, cada una con su capacidad de entrega verificada con el courier.
2. Mira el CPA por ciudad (breakdown geográfico en el reporte) antes de subir presupuesto. TikTok te deja desglosar por ubicación: úsalo.
3. Las ciudades grandes (Bogotá, Medellín, Cali, Barranquilla) dan volumen; las chicas a veces dan CPA mejor pero poco volumen. Mézclalo según tu meta de escala.
4. Si vas a otro país LatAm, ábrelo en campaña/ad group aparte: moneda, envío, oferta, comportamiento de compra y festividades cambian. Lo que funciona en Colombia no se traslada idéntico a Perú o México.

### Plantilla: estructura geo para escalar

| AG | Geo | Modalidad | Métrica clave |
|---|---|---|---|
| AG-CO-Capitales | Bogotá, Medellín, Cali, B/quilla | Nacional courier | CPA + tasa rechazo |
| AG-CO-Intermedias | 5-8 ciudades medias verificadas | Contraentrega | Tasa de rechazo |
| AG-CO-Resto-prepago | Resto del país | Solo prepago (PSE/Nequi) | CPA |

El geo bien puesto no "optimiza" — **filtra basura antes de que el algoritmo la persiga**. Es la cerca que más protege tu margen, y la más fácil de arreglar hoy mismo.

## Errores comunes — blacklist

1. **Anunciar el país entero cuando solo entregas en una ciudad.** La fuga de plata más silenciosa: CPM lindo, CPA mentiroso, cero ventas reales.
2. **Incluir ciudades sin cobertura de contraentrega.** Pedidos imposibles de completar; flete y tiempo perdidos.
3. **No usar Exclude.** Dejas entrar zonas sin cobertura o de alto rechazo que arrastran tu CPA real.
4. **Geo nacional para un negocio presencial.** Leads de gente que nunca va a llegar a tu local.
5. **Mezclar varios países LatAm en un ad group.** No puedes leer qué país paga; moneda y envío distintos lo enredan todo.
6. **Abrir el país de golpe al escalar.** Pierdes el control del CPA por ciudad; crece de a poco con capacidad de entrega verificada.
7. **No revisar la lista REAL de cobertura del courier.** Asumir que "entregan en todo lado" y descubrirlo con pedidos rechazados y flete quemado.
8. **Geo demasiado chico (un barrio).** El pool queda tan pequeño que el algoritmo no entrega; amplía a ciudad o varios sectores.
