# 91 — El tablero financiero del dueño

Los estados financieros completos tienen decenas de líneas. Pero como dueño, **no necesitas mirar todo cada mes**. Necesitas un puñado de indicadores — un "tablero" — que en una mirada te diga si el negocio respira bien o está en problemas. Igual que el tablero de un carro: no ves cada pieza del motor, ves velocidad, gasolina y temperatura.

Este módulo define ese tablero: los pocos números que un dueño debe revisar cada mes, qué significan, y cuándo deben preocuparte. La meta es que en 5 minutos sepas cómo va el mes.

## Términos que debes conocer
- **Indicador (KPI):** un número clave que resume un aspecto del negocio.
- **Margen:** porcentaje de la venta que te queda después de un costo. "Margen bruto" tras el costo del producto; "margen neto" tras todos los gastos.
- **Tendencia:** hacia dónde va un número en el tiempo (sube, baja, estable). Importa más que el dato suelto.
- **Punto de equilibrio:** las ventas mínimas para no perder ni ganar.

## El tablero mínimo del dueño (los 8 esenciales)
| Indicador | Qué te dice | Cuándo preocuparte |
|---|---|---|
| Ventas del mes | Cuánto facturaste | Cae 2 meses seguidos |
| Margen bruto (%) | Cuánto deja cada venta tras su costo | Baja sin que subas precios |
| Utilidad neta del mes | Si ganaste o perdiste de verdad | Negativa, o cae mes a mes |
| Caja disponible hoy | Plata real para operar | Menos de 1 mes de gastos cubierto |
| Cuentas por cobrar | Lo que te deben los clientes | Crece más rápido que las ventas |
| Cuentas por pagar | Lo que debes a proveedores | No te alcanza la caja para cubrirlas |
| Punto de equilibrio | Ventas mínimas para no perder | Vendiste por debajo de él |
| Gastos fijos del mes | Cuánto cuesta tener el negocio abierto | Suben sin que suban las ventas |

> Regla del dueño: mira siempre la **tendencia**, no el dato suelto. Un mes malo puede ser azar; tres meses cayendo es un problema.

## Cómo armar el tablero en una hoja
1. Toma tu P&G y tu balance del mes (ver 90).
2. Anota los 8 indicadores en una fila.
3. Pon al lado la columna del mes anterior.
4. Marca con color: verde (mejora), amarillo (estable), rojo (empeora).
5. Repite cada mes. En 3 meses ya ves tendencias reales.

## Ejemplo (cifras ILUSTRATIVAS / inventadas)
Tablero de "Café del Parque", mayo vs abril:
| Indicador | Abril | Mayo | Señal |
|---|---|---|---|
| Ventas | $9.000.000 | $9.500.000 | 🟢 |
| Margen bruto | 58% | 54% | 🔴 (subió el costo del café) |
| Utilidad neta | $1.100.000 | $900.000 | 🔴 |
| Caja hoy | $3.000.000 | $2.400.000 | 🟡 |
| Por cobrar | $500.000 | $1.300.000 | 🔴 (clientes pagando tarde) |
| Punto de equilibrio | $7.800.000 | $8.200.000 | 🟡 |

Lectura del dueño: vendió más pero ganó menos, porque el costo del café subió (margen cayó) y porque más clientes le quedaron debiendo. Acción: revisar precio del producto y cobrar la cartera. *(Los porcentajes y variaciones se calculan en `Matematicas_lushows`, no de memoria.)*

## Errores comunes
- **Mirar 30 indicadores.** Te paralizas. Empieza con estos 8.
- **Solo mirar ventas.** Vender más y ganar menos es trampa frecuente (ver el ejemplo).
- **No comparar contra el mes anterior.** Un número solo no tiene sentido.
- **Ignorar la caja.** Puedes tener utilidad y quebrar por falta de plata (ver 90 y 96).
- **Calcular los porcentajes a ojo.** Manda los cálculos a `Matematicas_lushows`.

## Conexión con otros módulos
- **90 (Leer tus números)** — primero aprende a leer los estados; este tablero sale de ahí.
- **96 (Señales de alerta)** — los rojos del tablero suelen ser las alertas de ese módulo.
- **21 (Estado de Resultados)** — de aquí salen ventas, margen y utilidad.
- **economist_lushows** — qué HACER cuando un indicador se pone rojo (subir precio, recortar gasto) se decide allá; aquí solo lo medimos.
- **AVIS (bot)** — puede enviarte el tablero o una alerta por WhatsApp cada mes (ver 92).
- **Matematicas_lushows** — todo cálculo de margen, variación y punto de equilibrio.

## Siguiente paso típico
Arma tu tablero de este mes con los 8 indicadores y guárdalo. El próximo mes compara. Si algún indicador sale rojo, ve a **96** para entender qué puede estar pasando, y a `economist_lushows` para decidir qué hacer.
