# Paqueterías de Colombia

> Colombia es el país donde el contraentrega mejor funciona de la región y donde la cobertura rural
> decide si un producto escala o se queda en Bogotá. Cuatro transportadoras se reparten el mapa y
> cada una tiene una vocación distinta. **Flete típico USD 2,50-3,20** por pedido.

## Las cuatro

| Transportadora | Vocación | Dónde brilla | Dónde cuesta |
|---|---|---|---|
| **Interrapidísimo** | **Líder en cobertura nacional** | Municipios pequeños, todo el país | Tiempos más largos fuera de eje |
| **Servientrega** | Urbano premium | Ciudades principales, servicio y trazabilidad | Precio |
| **Coordinadora** | Urbano principal | Bogotá, Medellín, Cali, Barranquilla | Menor alcance rural |
| **Envía Colvanes** | **Rural amplia** | Zonas apartadas, intermunicipal | Velocidad |

Regla práctica: **Interrapidísimo o Envía para cobertura, Servientrega o Coordinadora para
velocidad urbana.** Casi nadie gana usando una sola; se enruta por destino.

## Tasas de entrega en Colombia

| Escenario | Tasa |
|---|---|
| COD **sin** confirmación previa | **50-60%** |
| COD **con** confirmación previa | **65-78%** |
| Urbano con confirmación por WhatsApp o voz IA | **70-85%** |
| Prepago | 95-98% |

La diferencia entre 52% y 75% no es marketing: es la diferencia entre un desperdicio de 0,923 y uno
de 0,333 por cada pedido bueno. Ver `163` y `159`.

## Costo real de un pedido COD

| Concepto | Cómo se cobra |
|---|---|
| Flete de ida | **USD 2,50-3,20** típico, verificar por destino y peso |
| Comisión de recaudo | % sobre el valor cobrado, verificar |
| **Flete de retorno** | Casi siempre se cobra |
| Reexpedición | Cargo adicional |
| Sobrepeso | Por escalón de peso |

## El enrutamiento: la palanca gratis

La mayoría despacha todo con la misma transportadora por comodidad. Enrutar por destino sube la
tasa de entrega sin costar un peso adicional.

| Destino | Transportadora primaria | Respaldo |
|---|---|---|
| Bogotá, Medellín, Cali, Barranquilla | Coordinadora o Servientrega | Interrapidísimo |
| Ciudades intermedias | Interrapidísimo | Servientrega |
| Municipios pequeños / rural | **Interrapidísimo o Envía** | — |
| Zonas de difícil acceso | Envía, y confirmar antes | Ver `173` |

Implementación mínima viable: una tabla en Excel con ciudad → transportadora, y la regla aplicada
al generar la guía. No necesitas software.

## Cómo se elige (procedimiento)

1. Exporta tus últimos 100 pedidos y agrupa por ciudad. Ahí está tu mapa real.
2. Pide cobertura por municipio, no por departamento.
3. Pregunta: ¿cuántos intentos de entrega? ¿avisan por SMS o llamada antes?
4. Pregunta el plazo de liquidación del recaudo COD en días hábiles.
5. Pide el % de devoluciones que registran en tu tipo de producto y zona.
6. Prueba dos transportadoras en paralelo, 30 pedidos cada una, misma semana. Compara **tasa de
   entrega real**, no promesa.

## Régimen de importación, lo que hay que saber

| Dato | Valor | Nota |
|---|---|---|
| Umbral simplificado | **US$200 FOB** | Ver `17` |
| Origen sin TLC | **IVA 19% + ~10% de courier** | Verificar vigencia |
| Aéreo China→Bogotá | **2-4 días** aeropuerto a aeropuerto, **3-10** puerta a puerta | Ver `146` |
| Marítimo China→Buenaventura | **30-45 días FCL / 35-50 LCL** | + aduana 3-10 |
| Tarifa aérea | USD 6-8/kg, Colombia hasta **9,10/kg** | Verificar |

Colombia tiene el tránsito aéreo más rápido de LatAm desde China. Eso hace viable reponer stock en
campaña sin perder la temporada — ventaja que México no tiene con sus 8-15 días.

## Plataformas

**Dropi** nació aquí y es el estándar de facto del COD colombiano: 12 países, comisión **5%**,
liquidación **2-7 días hábiles** tras entrega efectiva, transportadoras integradas y generación de
guía automática. Ver `132`.

La comisión del 5% **se suma** al flete y a la comisión de recaudo. Si no la metes en el margen,
tu número está mal.

## Errores típicos en Colombia

| Error | Consecuencia |
|---|---|
| Despachar todo con una sola transportadora | Pierdes 5-12 puntos de entrega en zonas donde no es fuerte |
| No confirmar pedidos rurales antes de despachar | Devolución con flete doble a 3 días de distancia |
| Prometer 24-48 h a todo el país | Fuera de eje son 3-6 días |
| Olvidar el flete de retorno en el modelo | El desperdicio real duplica el estimado |
| No pedir teléfono adicional en el checkout | Sin contacto, no hay entrega |
| Asumir que el 19% de IVA se puede ignorar | Ver `17` e invoca `contador_lushows` |

## Checklist de configuración

1. Dos transportadoras contratadas mínimo, con regla de enrutamiento por destino.
2. Confirmación previa obligatoria para **todo** COD (`160`), sin excepción rural.
3. Tracking automático al cliente el mismo día del despacho (`156`).
4. Cliente con dos teléfonos y referencia de dirección.
5. Tablero con tasa de entrega **por transportadora y por ciudad**, revisado semanal (`174`).
6. Plan de reposición aérea de 10-24 días para no quedarte sin stock en campaña.

## Relacionados
`153` paqueterías México · `155` España y UE · `158` contraentrega · `159` tasa de entrega ·
`160` confirmación WhatsApp · `173` zonas difíciles · `17` régimen Colombia · `21` playbook Colombia
