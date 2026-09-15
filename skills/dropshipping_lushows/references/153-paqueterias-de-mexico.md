# Paqueterías de México

> En México la última milla no la decide el precio: la decide **quién entrega bien en la zona donde
> te compran**. Las cuatro grandes se reparten el país por vocación: una es urbana, una es nacional
> clásica, una es premium urgente y una es regional del norte. Elegir mal es regalar 15 puntos de
> tasa de entrega.

## Las cuatro integradas en Dropi MX

| Transportadora | Vocación | Dónde brilla | Dónde falla |
|---|---|---|---|
| **99minutos** | **Líder urbano** | CDMX, GDL, MTY, zonas metropolitanas | Cobertura rural limitada |
| **Estafeta** | Nacional clásica | Cobertura amplia, ciudades medias | Más lenta en metro |
| **FedEx** | Urgente premium | Urgencias, ticket alto, B2B | Precio |
| **Paquetexpress** | Regional norte | Noreste y norte, ciudades intermedias | Menos fuerte en el sur |

> **Flete típico MXN 120-200** por pedido en estas rutas. Verificar con tarifa vigente y con tu
> volumen: el precio baja con cuenta directa o vía plataforma que agrega volumen.

## La tasa de entrega, que es lo que de verdad pagas

Datos verificados para México:

| Escenario | Tasa de entrega |
|---|---|
| COD **sin** confirmación previa | **45-55%** |
| COD **con** confirmación previa | **60-72%** |
| Urbano con confirmación por WhatsApp o voz IA | **70-85%** |
| **CDMX / GDL / MTY con 99minutos, con confirmación** | **78%** |
| Prepago | 95-98% (el pedido ya está cobrado) |

Ese 78% de CDMX/GDL/MTY es el techo práctico del COD mexicano y explica por qué la gente que gana
en México concentra pauta en las tres metrópolis en lugar de repartirla por todo el país. Ver `159`
y `173`.

## Cómo se elige, en orden

1. **Mira tu mapa de ventas primero, no el tarifario.** Si el 70% de tus pedidos es zona metro,
   99minutos gana aunque no sea la más barata.
2. Pide cobertura por **código postal**, no por estado. México tiene municipios enteros que la
   paquetería dice cubrir y entrega en 7 días.
3. Pregunta explícitamente: **¿cuántos intentos de entrega hacen?** Uno solo mata tu tasa.
4. Pregunta el **plazo de liquidación del COD**: cuántos días hábiles desde entrega efectiva hasta
   que la plata está en tu cuenta. Es tu flujo de caja.
5. Pregunta la comisión de COD (suele ser un % del recaudo, aparte del flete).
6. Corre 20-30 pedidos de prueba con dos transportadoras a la vez y compara tasa real.

## Estructura de costo en COD

| Concepto | Cómo se cobra |
|---|---|
| Flete de ida | MXN 120-200, verificar |
| Comisión de recaudo COD | % sobre el monto cobrado, verificar |
| **Flete de retorno** | Se cobra igual o parcial cuando el cliente no recibe |
| Reexpedición por dirección mala | Cargo adicional |
| Sobrepeso / sobredimensión | Por encima del límite del tarifario |

El flete de retorno es el costo que todo el mundo olvida al modelar. Ver `163`.

## Prepago vs COD en México

| | COD | Prepago |
|---|---|---|
| Conversión en la página | Alta | Menor |
| Tasa de cobro | 45-72% (85% top urbano) | 95-98% |
| Días hasta tener la plata | 10-15 | ~3 |
| Capital necesario | Alto | Bajo |
| Curva del píxel | Sucia | Limpia |

Con **menos de USD 500 de capital**, COD no es viable: financias flete de ida y vuelta de la mitad
de tus pedidos. Por eso el proyecto de diciembre 2026 va **prepago cerrando en la web**. Ver `30`.

## Plataformas y agregadores

| Tipo | Qué te da | Cuidado |
|---|---|---|
| **Dropi MX** | 12 países, comisión **5%**, liquidación **2-7 días hábiles** tras entrega efectiva, transportadoras integradas | La comisión se suma al flete: métela en el margen |
| Agregadores de guías (varios) | Tarifas por volumen sin cuenta propia | Verifica quién responde por un paquete perdido |
| Cuenta directa con la paquetería | Mejor precio en volumen | Requiere facturación y volumen mínimo |

## Meses sin intereses: el detalle que sí mueve conversión

En México, MSI en prepago sube ticket promedio y conversión en bundles de 1.000+ MXN. No es
logística, pero decide si el prepago funciona. Ver `195` y `192`.

## Errores típicos en México

| Error | Consecuencia |
|---|---|
| Vender COD a todo el país desde el día 1 | Tasa de entrega de 45-50%, margen negativo |
| Prometer "entrega en 24 h" con paquetería nacional | Incumples fuera de metro |
| No pedir teléfono verificado en el checkout | La paquetería no puede coordinar → devolución |
| Direcciones sin referencias | Clave en zonas de colonias grandes; pide "entre calles" |
| Ignorar el retorno en el cálculo | El fallido cuesta el doble de lo que creías |
| No revisar límite de peso/dimensión del tarifario | Cargo de sobredimensión que come el margen |

## Configuración recomendada para diciembre 2026 (prepago, stock local, bundle ~1.099 MXN)

1. **Una** paquetería urbana fuerte + **una** nacional como respaldo.
2. Prepago: no necesitas comisión de recaudo, solo flete. Margen más limpio.
3. Envío gratis metido en el precio del bundle (`157`), no como línea aparte.
4. Guía generada el mismo día, tracking automático al cliente (`156`).
5. Corte de despacho diario a hora fija; publícala.
6. Ver `169` y `170` para el calendario de temporada: **Buen Fin 13-17 nov**, Black Friday 27 nov,
   aguinaldo hasta el 20 dic.

## Relacionados
`154` paqueterías Colombia · `155` España y UE · `156` tracking · `157` comunicar la entrega ·
`158` contraentrega · `159` tasa de entrega · `173` zonas difíciles · `20` playbook México
