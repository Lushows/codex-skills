# Tiempos de tránsito reales

> Los números que te da el forwarder son **puerto a puerto**. El número que le importa al cliente es
> **fábrica a puerta**. Entre los dos hay entre 6 y 20 días que nadie te cuenta hasta que ya pagaste.

## Aéreo desde China — puerto a puerto y puerta a puerta

| Destino | Aeropuerto a aeropuerto | Puerta a puerta | Aduana incluida ahí |
|---|---|---|---|
| **Colombia** (BOG) | **2-4 días** | **3-10 días** | 3-10 días adicionales si hay revisión |
| **México** (MEX/NLU) | — | **8-15 días** | ya contemplada en el rango |
| **Chile** (SCL) | — | **12-20 días** | ya contemplada |
| **España** (MAD/BCN) | — | **10-18 días** | ya contemplada |

> El caso colombiano es la excepción de LatAm: 2-4 días de vuelo real. Lo que infla el reloj es
> tierra en China, consolidación y aduana en Bogotá. Verificar siempre con el forwarder del día.

## Marítimo desde China

| Destino / puerto | FCL (contenedor completo) | LCL (carga consolidada) |
|---|---|---|
| Colombia — Buenaventura | **30-45 días** | **35-50 días** |
| Chile — Valparaíso | **30-45 días** | 35-50 (verificar) |
| Perú — Callao | **30-35 días** | verificar |
| Perú — **Chancay** | **28-32 días** | verificar |
| México — Manzanillo / Lázaro Cárdenas | verificar con forwarder | verificar |
| España — Valencia / Barcelona | verificar con forwarder | verificar |

**Aduana suma 3-10 días** encima de cualquiera de estos números, en todos los destinos.
El LCL casi siempre suma 5-8 días extra sobre el FCL por la desconsolidación en destino.

## El tiempo que nadie cuenta

| Etapa invisible | Días | Cómo se reduce |
|---|---|---|
| Producción o reposición del proveedor | 1-5 (hasta 20 si fabrica) | Pedir stock confirmado por foto antes de pagar |
| Tierra de fábrica a bodega del forwarder | 1-3 | Fábrica cerca del puerto del forwarder |
| Espera a consolidar (solo LCL / líneas) | 1-7 | Salidas fijas semanales, no "cuando se llene" |
| Exportación China | 1-2 | Documentos completos desde el día 1 |
| Desconsolidación en destino | 1-3 | Nada, es estructural |
| **Aduana destino** | **3-10** | Ver `151` |
| Tierra puerto → tu bodega | 1-3 | — |

**Regla operativa:** al número puerto a puerto súmale **8-15 días** para tener el reloj real
fábrica→tu bodega. Luego suma la última milla al cliente (`153`, `154`, `155`).

## Cálculo del reloj total, con ejemplos

| Escenario | Producción | Tránsito | Aduana | Interno | **Total a tu bodega** |
|---|---|---|---|---|---|
| Aéreo China→México, proveedor con stock | 2 | 8-15 | incluida | 2 | **12-19 días** |
| Aéreo China→Colombia, proveedor con stock | 2 | 3-10 | 3-10 | 2 | **10-24 días** |
| Marítimo LCL China→Colombia | 4 | 35-50 | 3-10 | 3 | **45-67 días** |
| Marítimo FCL China→Perú vía Chancay | 4 | 28-32 | 3-10 | 3 | **38-49 días** |

Y luego, al cliente: +1 a 5 días de última milla.

## Lo que esto significa para el calendario

Para vender en diciembre 2026 con stock local tienes que pensar al revés:

1. Fija la fecha en que quieres **estar vendiendo** (ej. 20-nov-2026).
2. Resta la última milla y el margen de prueba: 5 días.
3. Resta el reloj total del modo elegido (arriba).
4. Resta **holgura del 30%** sobre el tránsito. No es pesimismo, es el número que evita el desastre.
5. Eso te da la fecha de pedido al proveedor.

Ver `170` para las fechas de corte ya calculadas de Q4-2026.

## Los tres momentos que rompen el reloj

| Evento | Ventana 2026-2027 | Efecto |
|---|---|---|
| **Año Nuevo Chino** | Feriado oficial **4-12 feb 2027** (día 1: 6-feb) | Desaceleración **3-4 semanas antes**, recuperación **6-8 semanas** después |
| Golden Week (octubre) | primera semana de octubre | Fábricas y puertos a media marcha ~1 semana |
| Pico Q4 de carga aérea | oct-nov | Tarifa sube, espacio escasea, "rolling" de carga |

Durante ANC no es que se tarde más: **no se produce**. Un pedido puesto el 25-ene-2027 puede no
moverse hasta marzo. Ver `169`.

## Cómo se verifica un tiempo, en vez de creerlo

1. Pide al forwarder **tres cotizaciones** con ETD (salida) y ETA (llegada) con fecha concreta,
   no "15 días aprox".
2. Pregunta explícitamente: **¿es puerto a puerto o puerta a puerta?** y **¿incluye despacho?**
3. Pide el historial de las últimas 4 salidas de esa ruta: cuántas llegaron en fecha.
4. Pregunta la frecuencia de salidas. Una salida semanal con 2 días de espera promedio es mejor
   que una "salida cuando se llene" que dice ser más rápida.
5. Todo por escrito, en WhatsApp o correo. Sirve para reclamar.

## Errores frecuentes

| Error | Qué pasa |
|---|---|
| Comparar aéreo puerta-a-puerta contra marítimo puerto-a-puerto | El marítimo parece mejor de lo que es |
| Prometer al cliente el número del forwarder | Incumples el 100% de las veces |
| Pedir marítimo en noviembre para Navidad | La mercancía llega en enero |
| No contar fines de semana ni festivos del destino | 2-4 días de error por envío |
| Confiar en "express 5 días" de un marketplace | Ese reloj empieza cuando ellos despachan, no cuando pagas |

## Relacionados
`145` cadena logística · `147` aéreo vs marítimo vs express · `148` líneas dedicadas · `151` aduana
· `157` comunicar la entrega · `169` temporada alta · `170` fechas de corte
