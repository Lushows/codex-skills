# 112 — Playbook: transporte y logística

Cómo se gana (o se pierde) dinero moviendo cosas: carga, última milla y mensajería. Aquí domina la matemática del **costo por kilómetro** y la **utilización de la flota**: un camión parado o un mensajero a media carga te desangra aunque tengas clientes.

Aviso: capital, márgenes y KPIs de abajo son **rangos orientativos** para que ordenes el pensamiento, NO datos duros de tu país. El combustible, los peajes, los salarios y los impuestos al diésel cambian por país y ciudad. **Pregunta país/ciudad primero** y consigue tus números reales (ver 21).

## El negocio en una frase
No vendes "transporte": vendes **capacidad ociosa convertida en entregas**. Tu activo (vehículo + conductor) cuesta lo mismo esté lleno o vacío. La utilidad nace de llenarlo y enrutarlo bien. Por eso este es un negocio de **costos fijos altos + margen por unidad bajo**: vives o mueres por el volumen y la eficiencia, no por el precio por viaje.

## Los tres modelos (elige UNO para arrancar)
| Modelo | Qué mueves | Activo clave | Cómo cobras | Reto principal |
|---|---|---|---|---|
| **Carga / fletes** | Mercancía pesada entre ciudades/bodegas | Camión, tractomula | Por viaje, por tonelada o por km | Viaje de retorno vacío ("flete muerto") |
| **Última milla** | Paquetes del depósito a la puerta del cliente | Furgoneta, moto, bici-carga | Por entrega o tarifa mensual al e-commerce | Densidad de paradas; fallos de entrega |
| **Mensajería / domicilios** | Documentos, comida, compras locales | Moto, bici | Por servicio + propina | Tiempo ocioso entre pedidos |

Regla: no mezcles los tres al inicio. Cada uno tiene flota, ruteo y cliente distintos.

## Capital típico de arranque (orientativo)
- **Mensajería en moto (1-2 motos):** bajo. Puede arrancar con 1 moto propia y un celular con app de ruteo.
- **Última milla con furgoneta:** medio. Vehículo (propio, leasing o subcontratado) + estantería + sistema de ruteo.
- **Carga interurbana:** alto. El camión es el grueso del capital; muchos arrancan **sin comprar el camión**, subcontratando dueños-conductores y quedándose con la comisión por conseguir la carga (modelo "broker", capital muy bajo).
- En todos: deja **colchón de 2-3 meses** de combustible, salarios y mantenimiento. La cartera (clientes que pagan a 30-60 días) te puede ahogar aunque seas rentable (ver 92).

> Atajo de bajo capital: empieza como **broker/coordinador** (consigues la carga o el contrato de e-commerce y subcontratas vehículos). Aprendes el ruteo y los clientes sin inmovilizar capital en flota. Compras vehículos solo cuando una ruta tiene volumen estable.

## Estructura de costos (de dónde se va la plata)
Ordena tus costos en variables (suben con los km) y fijos (corren igual estés parado):
- **Variables:** combustible (el rey), llantas, mantenimiento por desgaste, peajes, comisiones de plataforma.
- **Fijos:** salario base del conductor, seguro/SOAT, impuestos del vehículo, depreciación, parqueadero, administración, ruteo/software.

Reparto **ilustrativo** de un peso de costo en última milla: combustible ~25-35%, mano de obra ~30-40%, vehículo (depreciación + seguro + impuestos) ~15-25%, mantenimiento/llantas ~8-12%, admin/software ~5-10%. **Verifica el tuyo**: el peso del combustible cambia muchísimo según el precio local del diésel/gasolina y si usas moto, furgoneta o camión.

## Márgenes típicos del sector (rango orientativo)
- **Mensajería/última milla:** margen operativo delgado, **~5-15%**. Se gana por volumen y densidad, no por viaje.
- **Carga interurbana propia:** **~8-18%** si llenas el retorno; puede ser negativo si vuelves vacío.
- **Broker de carga (sin flota):** márgenes sobre tu comisión pueden verse altos (%), pero los pesos absolutos por viaje son pequeños; es negocio de **volumen + rotación**.
No tomes estos números como tu realidad: son referencia para detectar si tu modelo cierra. Construye tu propio P&L (ver 53) y tu costo por km real.

## La métrica madre: costo por kilómetro
Casi todo se deriva de aquí. Cálculo simple:

**Costo por km = (costos fijos mensuales ÷ km recorridos al mes) + costo variable por km**

Si no sabes tu costo por km, no sabes si cada viaje gana o pierde. Calcúlalo **antes** de cotizar.

## KPIs clave del sector (mide estos 5)
1. **Costo por entrega (o por viaje):** todo lo que gastaste ÷ entregas completadas. Tu número del norte.
2. **Entregas por día por vehículo (productividad):** mide la densidad. Subirla de 25 a 35 baja el costo por entrega sin gastar más.
3. **Utilización de flota / capacidad:** % del vehículo realmente usado (km cargados vs. km totales, o % de capacidad llena). El **km vacío** es plata quemada.
4. **On-time / tasa de entrega exitosa:** % entregado a tiempo y al primer intento. Cada reintento duplica el costo de esa entrega.
5. **Consumo de combustible (km por litro / galón):** por vehículo y por conductor. Detecta desperdicio, robo de combustible y rutas malas.

Tablero mínimo: costo/entrega, entregas/día, % km vacío, % on-time, km por litro. Una hoja de cálculo semanal basta para empezar (ver 91).

## Ejemplo numérico (cifras ILUSTRATIVAS, no de tu país)
Operación de última milla, 1 furgoneta, mes de 26 días laborables.

**Costos fijos mensuales:**
- Salario conductor: 1.200
- Seguro + impuestos vehículo: 250
- Depreciación furgoneta: 400
- Parqueadero + admin + software ruteo: 250
- **Total fijo: 2.100**

**Costos variables del mes** (recorre 3.000 km):
- Combustible: 600
- Mantenimiento + llantas: 200
- **Total variable: 800**

**Costo total mensual = 2.100 + 800 = 2.900**

Escenario A — **flota mal usada:** entrega **25 paquetes/día** → 25 × 26 = **650 entregas/mes**.
- Costo por entrega = 2.900 ÷ 650 = **4,46 por entrega**.
- Si cobras 5,00 al e-commerce → margen 0,54 (≈11%). Frágil.

Escenario B — **misma furgoneta, mejor ruteo y densidad:** entrega **35 paquetes/día** → 910/mes. Casi no sube el combustible (mismas zonas, más paradas juntas), digamos +100 variable.
- Costo total = 3.000; costo por entrega = 3.000 ÷ 910 = **3,30**.
- A la misma tarifa de 5,00 → margen 1,70 (**34%**).

**Lección:** subir entregas/día de 25 a 35 (densidad) **triplicó el margen** sin comprar otro vehículo. En este negocio la utilidad está en la **utilización**, no en el precio. (Misma lógica de costos fijos y punto de equilibrio: ver 53.)

## Cómo arrancar mínimo viable
1. **Elige UN modelo y UNA zona/ruta densa.** La densidad lo es todo: muchas entregas en poco territorio.
2. **No compres flota al inicio.** Subcontrata o usa 1 vehículo propio. Compra solo cuando una ruta tenga volumen probado.
3. **Calcula tu costo por km y por entrega ANTES de cotizar.** Sin eso, cotizas a ciegas.
4. **Consigue 1-2 clientes ancla** (un e-commerce, una bodega) que te den volumen base y predecible.
5. **Mide on-time y entregas/día desde el día 1.** Una hoja de cálculo es suficiente.
6. **App de ruteo** (incluso gratis/barata) para ordenar paradas: ahorra combustible y tiempo de inmediato.
7. **Negocia el combustible y el mantenimiento** (estación fija, taller fijo): es tu mayor palanca de costo.

## Trampas que matan a este negocio
- **Flota ociosa / km vacío:** comprar vehículos antes de tener volumen. Cada vehículo parado o de retorno vacío drena los fijos. Asegura el **flete de retorno** antes de aceptar el de ida.
- **No conocer el costo por km:** cotizas, ganas el cliente y descubres que pierdes en cada viaje. Le pasa a casi todos los novatos.
- **Combustible fuera de control:** sin medir km/litro por vehículo, no detectas desperdicio ni robo de combustible (fuga clásica del sector).
- **Rutas ineficientes:** ordenar paradas "a ojo" infla km y horas. El ruteo es la diferencia entre 25 y 35 entregas/día.
- **Mantenimiento reactivo:** esperar a que el vehículo se dañe = días sin operar (costo fijo corriendo, cero ingreso) + reparación cara. El mantenimiento preventivo es más barato.
- **Cartera que te ahoga:** clientes corporativos pagan a 30-60 días pero tú pagas combustible y salarios cada semana. Puedes quebrar siendo rentable por falta de caja (ver 92).
- **Subcotizar para ganar el contrato:** en un negocio de margen delgado, un mal precio no se recupera con volumen; lo amplifica.
- **Depender de un solo cliente grande:** si se va, tu flota queda vacía. Diversifica.

## Errores comunes
- Confundir **vehículo lleno de km** con **vehículo productivo**: lo que paga es la entrega, no el kilómetro.
- Ignorar la **depreciación**: el vehículo se gasta aunque no veas el desembolso; si no la cargas al costo, tu margen es ficticio.
- Crecer comprando vehículos en vez de **subir densidad y utilización** de los que ya tienes.
- Olvidar peajes, impuestos al combustible y trámites locales del transporte: **pregunta país/ciudad primero** y consigue las reglas y tarifas vigentes (ver 21).
- Medir on-time pero no el **costo del reintento**: cada entrega fallida puede borrar el margen de varias exitosas.

## Siguiente paso típico
Define UN modelo y UNA zona densa, calcula tu **costo por km y por entrega real** con tus precios locales (ver 21), y arma el P&L con punto de equilibrio (ver 53). Solo entonces decide tarifa y si conviene comprar flota o subcontratar.
