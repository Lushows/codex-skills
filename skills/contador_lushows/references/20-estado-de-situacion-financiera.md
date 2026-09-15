# 20 — Estado de Situación Financiera (el "balance general")

El **Estado de Situación Financiera** (antes llamado "balance general") es la foto de tu negocio en un día exacto. Responde una sola pregunta: *¿qué tengo, qué debo y qué es realmente mío?* Por eso siempre se arma sobre una **fecha de corte** (por ejemplo, "al 31 de diciembre de 2025"), no sobre un período.

Bajo el marco colombiano (NIIF y NIIF para pymes) este estado es obligatorio dentro del juego completo de estados financieros. Aquí aprendes a leerlo y a verificar que **cuadre**. La promesa de la casa es innegociable: **Activo = Pasivo + Patrimonio**. Si no cuadra, hay un error, no una opinión.

## Los tres bloques

| Bloque | Pregunta que responde | Ejemplos |
|---|---|---|
| **Activo** | ¿Qué tengo / qué me deben? | Caja, bancos, cuentas por cobrar, inventario, equipos, local |
| **Pasivo** | ¿Qué debo a terceros? | Proveedores, préstamos, impuestos por pagar, nómina por pagar |
| **Patrimonio** | ¿Qué es de los dueños? | Capital aportado, utilidades acumuladas, utilidad del año |

> **Término clave:** *Patrimonio* es lo que quedaría para los dueños si vendieras todo el activo y pagaras todo el pasivo. Por eso se le llama también "valor en libros" del negocio.

## La ecuación que NUNCA falla

```
ACTIVO  =  PASIVO  +  PATRIMONIO
```

Todo lo que tienes (activo) salió de alguna parte: o lo financió un tercero (pasivo) o lo pusieron/ganaron los dueños (patrimonio). Si los dos lados no dan igual, el balance no cuadra.

## Corriente vs. no corriente

NIIF te pide separar lo que se mueve pronto de lo que es de largo plazo. La regla general es **12 meses**.

| Clasificación | Significa | Activo (ejemplo) | Pasivo (ejemplo) |
|---|---|---|---|
| **Corriente** | Se vuelve efectivo o se paga en ≤ 12 meses | Caja, inventario, clientes | Proveedores, IVA por pagar |
| **No corriente** | Más de 12 meses | Maquinaria, vehículos, local | Préstamo bancario a 5 años |

Esta separación es la base para medir liquidez (módulo 27): el activo corriente debe alcanzar para cubrir el pasivo corriente.

## Ejemplo rotulado — cifras ILUSTRATIVAS / inventadas

**Restaurante "La Sazón" — Estado de Situación Financiera al 31-dic-2025 (COP)**

| ACTIVO | | PASIVO Y PATRIMONIO | |
|---|---:|---|---:|
| **Activo corriente** | | **Pasivo corriente** | |
| Caja y bancos | 12.000.000 | Proveedores | 8.500.000 |
| Cuentas por cobrar | 3.500.000 | IVA por pagar | 1.200.000 |
| Inventario (insumos) | 6.000.000 | Nómina por pagar | 2.300.000 |
| *Subtotal corriente* | *21.500.000* | *Subtotal corriente* | *12.000.000* |
| **Activo no corriente** | | **Pasivo no corriente** | |
| Equipo de cocina | 18.000.000 | Préstamo bancario | 15.000.000 |
| (Depreciación acum.) | (4.000.000) | *Subtotal no corriente* | *15.000.000* |
| *Subtotal no corriente* | *14.000.000* | **TOTAL PASIVO** | **27.000.000** |
| | | **PATRIMONIO** | |
| | | Capital social | 5.000.000 |
| | | Utilidades acumuladas | 3.500.000 |
| | | **TOTAL PATRIMONIO** | **8.500.000** |
| **TOTAL ACTIVO** | **35.500.000** | **TOTAL PASIVO + PATRIMONIO** | **35.500.000** |

Verificación de cuadre: `35.500.000 = 27.000.000 + 8.500.000`. ✅ Cuadra. (Nota: la suma exacta de columnas, cuando hay decimales, se ejecuta y verifica en código vía Matematicas_lushows, nunca de cabeza.)

## Cómo leerlo en 30 segundos
1. ¿El total de activo iguala al total de pasivo + patrimonio? Si no, hay error.
2. ¿El activo corriente supera al pasivo corriente? Si sí, hay aire para pagar lo de corto plazo.
3. ¿El patrimonio es positivo? Si es negativo, el negocio "debe más de lo que vale".

## Errores comunes
- **Mezclar fechas:** un balance es de UN día. No sumes saldos de meses distintos.
- **Olvidar la depreciación acumulada:** los equipos van por su valor en libros (costo − depreciación), no por lo que costaron nuevos.
- **Meter gastos en el balance:** los gastos van al estado de resultados (módulo 21); aquí solo van saldos, no movimientos del período.
- **Clasificar mal corriente/no corriente:** un préstamo a 3 años NO es pasivo corriente.
- **Forzar el cuadre con una cuenta "ajustes":** si no cuadra, busca el asiento mal registrado, no tapes el hueco.

## Conexión con otros módulos
- **Módulo 21 (Estado de resultados):** la utilidad del año entra al patrimonio de este estado.
- **Módulo 22 (Flujos de efectivo):** explica por qué cambió la caja que ves aquí.
- **Módulo 23 (Cambios en patrimonio):** detalla cómo se movió el patrimonio entre dos balances.
- **Módulo 26 y 27 (Análisis y ratios):** este estado alimenta liquidez y endeudamiento.
- **Matematicas_lushows:** ejecuta toda suma, resta y ratio con `decimal` para evitar errores de centavos.

## Siguiente paso típico
Con el balance cuadrado, pasa al **módulo 21 (Estado de resultados)** para ver si el negocio ganó o perdió en el período, y luego conéctalo con el patrimonio de este estado.
