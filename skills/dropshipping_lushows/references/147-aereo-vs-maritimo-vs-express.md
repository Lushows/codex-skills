# Aéreo vs marítimo vs express

> La decisión no es "rápido o barato". Es **cuánto vale un día de tu capital**. Si tienes USD 500 y
> una temporada que se cierra el 24 de diciembre, 30 días de barco no son ahorro: son la temporada
> perdida.

## Los cuatro modos

| Modo | Qué es | Tránsito | Costo | Mínimo práctico |
|---|---|---|---|---|
| **Courier express** (DHL/FedEx/UPS) | Paquete puerta a puerta, despacho simplificado | 5-12 días | El más caro por kg | 1 kg |
| **Aéreo consolidado / línea dedicada** | Tu carga viaja con la de otros, un agente despacha en lote | Ver `146` | **USD 6-8/kg** típico; Colombia hasta **9,10/kg** | 20-50 kg según agente |
| **Marítimo LCL** | Comparte contenedor | 35-50 días a Colombia | Bajo por kg, alto en fijos | ~0,5-1 CBM |
| **Marítimo FCL** | Contenedor completo (20'/40') | 30-45 días | El más bajo por unidad | Un contenedor |

## El punto de quiebre por peso

La pregunta correcta es **cuánto pesa tu lote**, no cuánto pesa una unidad.

| Peso del lote | Modo que casi siempre gana | Por qué |
|---|---|---|
| < 20 kg | Courier express o consolidado aéreo | Los fijos del marítimo (THC, documentación, desconsolidación, agente) aplastan el ahorro |
| 20-150 kg | **Aéreo consolidado** | El punto dulce del dropshipper que arranca |
| 150-500 kg | Aéreo si el producto tiene margen; LCL si es voluminoso | Depende del CBM |
| > 500 kg o > 2 CBM | LCL, y desde ~10 CBM evaluar FCL | El flete por unidad cae fuerte |

> El error clásico: comparar USD/kg entre aéreo y marítimo. El marítimo cobra por **volumen (CBM)**,
> no por peso. Un producto liviano y voluminoso (cojines, organizadores, peluches) puede salir más
> caro por barco de lo que parece.

## Peso volumétrico: el cobro que te sorprende

Aéreo cobra el **mayor** entre peso real y peso volumétrico.

```
Peso volumétrico aéreo (kg) = largo(cm) × ancho(cm) × alto(cm) / 6000
Courier express suele usar        /5000   (verificar con el operador)
Marítimo LCL cobra por CBM  = largo × ancho × alto / 1.000.000 (m³)
```

| Caja | Real | Volumétrico /6000 | Te cobran |
|---|---|---|---|
| 40×30×30 cm, 5 kg | 5 kg | 6,0 kg | **6,0 kg** |
| 40×30×30 cm, 12 kg | 12 kg | 6,0 kg | **12 kg** |
| 60×40×40 cm, 8 kg | 8 kg | 16,0 kg | **16 kg** |

Consecuencia práctica: pídele al proveedor que **quite la caja de retail individual** y meta todo
en bolsa compactada; tú le pones el empaque final en destino (`167`). Puede bajar 20-40% el
volumétrico. Verificar que el producto aguante el viaje sin esa caja.

## Cuadro de decisión

| Tu situación | Modo |
|---|---|
| Primer lote de prueba, 30-80 unidades livianas | **Aéreo consolidado** |
| Muestras (1-5 unidades) para foto y video | **Courier express**, y no llores por el costo |
| Reposición urgente en plena campaña que vende | Aéreo, aunque duela; ver `169` |
| Producto validado, 500+ unidades, sin urgencia | LCL o FCL |
| Producto voluminoso y de bajo precio | Marítimo o cámbialo de producto (`41`) |
| Temporada que cierra en < 25 días | Aéreo o **no pidas** |

## El costo real de esperar 30 días más

No es solo el flete. Es la caja parada.

| Concepto | Aéreo | Marítimo |
|---|---|---|
| Flete de 60 kg (ejemplo, verificar) | ~USD 420 a 7/kg | mucho menor, pero + fijos de USD 250-500 |
| Días hasta poder vender | ~15 | ~50 |
| Vueltas de caja en 100 días | ~5-6 | ~2 |
| Riesgo de que el producto se sature | Bajo | **Alto** (ver `62`) |
| Riesgo de perder la temporada | Bajo | Total |

Con USD 500 de capital, dos vueltas contra seis vueltas es la diferencia entre un negocio y un
experimento. **La velocidad de rotación manda por encima del flete unitario hasta que tengas
capital de sobra.** Ver `32`.

## Cuándo el marítimo sí es la decisión correcta

1. El producto ya está validado con al menos 100-200 ventas reales.
2. Sabes tu velocidad de venta semanal con dos semanas limpias de datos.
3. Tienes capital para tener **dos lotes vivos a la vez**: el que vendes y el que navega.
4. El producto no es de moda y no muere en 8 semanas.
5. No hay temporada en el medio.

Si falla cualquiera de las cinco, aéreo.

## El modelo híbrido (el que usan los que ganan)

```
Lote grande por barco  →  cubre el volumen base, costo bajo
Lote pequeño por aire  →  cubre el pico y evita quedarse sin stock
```

Pides el marítimo con 55-60 días de anticipación y, cuando la venta se acelera, mandas 40-60 kg por
aire para no romper la promesa de entrega. Requiere capital; no es para el primer lote.

## Qué preguntar antes de pagar un flete

1. ¿Es puerta a puerta o hasta el aeropuerto/puerto?
2. ¿Incluye despacho de aduana y arancel, o eso va aparte? (`149`)
3. ¿Cómo calculas el peso: /5000 o /6000? ¿Cobras volumétrico?
4. ¿Qué pasa si la aduana marca revisión física? ¿Quién paga el almacenaje?
5. ¿Cuál es tu frecuencia de salida y cuál fue la última demora real de esta ruta?
6. ¿Cubres seguro? ¿Por qué monto? (`166`)

Para importación formal, valoración y clasificación arancelaria, invoca `contador_lushows`.

## Relacionados
`146` tiempos de tránsito · `148` líneas dedicadas y consolidación · `149` DDP/DDU · `152` costo
puesto en destino · `166` seguros · `32` rotación de caja · `169` temporada alta
