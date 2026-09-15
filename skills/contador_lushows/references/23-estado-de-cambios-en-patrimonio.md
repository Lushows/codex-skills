# 23 — Estado de Cambios en el Patrimonio

El **patrimonio** es lo que de verdad es de los dueños (módulo 20). El **Estado de Cambios en el Patrimonio** cuenta una historia sencilla pero importante: *¿cómo cambió lo que es mío entre el inicio y el fin del período, y por qué?*

Si el balance de inicio decía que el patrimonio valía $8.500.000 y el de fin dice que vale $20.700.000, este estado explica esa diferencia partida por partida. Bajo el marco colombiano (NIIF y NIIF para pymes) es uno de los estados obligatorios del juego completo.

## Qué movimientos muestra

El patrimonio sube o baja por causas muy concretas:

| Movimiento | Efecto | Ejemplo |
|---|---|---|
| **Utilidad del período** | Sube | El negocio ganó plata (viene del módulo 21) |
| **Pérdida del período** | Baja | El negocio perdió plata |
| **Aportes de socios** | Sube | Los dueños metieron capital nuevo |
| **Dividendos / retiros** | Baja | Los dueños sacaron utilidades |
| **Reservas** | Reclasifica | Se aparta utilidad para un fin (legal, futura) |
| **Ajustes / correcciones** | Sube o baja | Corrección de errores de años anteriores |

> **Términos clave:**
> - *Capital social:* lo que los dueños aportaron para crear y financiar el negocio.
> - *Utilidades acumuladas (o retenidas):* ganancias de años anteriores que no se repartieron.
> - *Reserva legal:* en Colombia, las sociedades deben apartar parte de la utilidad como reserva (porcentaje según norma vigente — no se inventa).
> - *Dividendos:* la parte de la utilidad que se reparte a los dueños.

## La lógica del estado

```
   Patrimonio al inicio del período
 + Aportes de los socios
 + Utilidad del período
 − Dividendos / retiros
 ± Reservas y otros ajustes
 ─────────────────────────────────────
 = Patrimonio al final del período
```

Se presenta como una tabla con una columna por cada componente del patrimonio y filas por cada movimiento.

## Ejemplo rotulado — cifras ILUSTRATIVAS / inventadas

**Restaurante "La Sazón" — Cambios en el Patrimonio 2025 (COP)**

| Movimiento | Capital social | Reserva legal | Utilidades acum. | TOTAL |
|---|---:|---:|---:|---:|
| **Saldo al 1-ene-2025** | 5.000.000 | 0 | 3.500.000 | 8.500.000 |
| Aporte nuevo de socio | 3.000.000 | — | — | 3.000.000 |
| Utilidad del período | — | — | 14.700.000 | 14.700.000 |
| Traslado a reserva legal | — | 1.470.000 | (1.470.000) | 0 |
| Dividendos decretados | — | — | (5.500.000) | (5.500.000) |
| **Saldo al 31-dic-2025** | **8.000.000** | **1.470.000** | **11.230.000** | **20.700.000** |

Verificación de amarre: el total final (20.700.000) **debe igualar** el patrimonio del balance al 31-dic-2025 (módulo 20). El traslado a reserva mueve dinero entre columnas pero no cambia el total (suma 0). Las sumas y el cálculo de la reserva se ejecutan en código vía Matematicas_lushows con la tasa legal vigente.

## Cómo leerlo en 30 segundos
1. ¿Subió el patrimonio? Si sí, ¿fue por utilidad (sano) o solo por aportes nuevos (los dueños inyectaron plata)?
2. ¿Se repartieron muchos dividendos? Repartir está bien, pero descapitaliza si es excesivo.
3. ¿Hay correcciones de años anteriores? Una corrección grande puede indicar errores pasados.

## Errores comunes
- **No amarrar con el balance:** el total final debe coincidir exacto con el patrimonio del módulo 20.
- **Confundir dividendos con gasto:** los dividendos NO van al estado de resultados; salen del patrimonio.
- **Olvidar la reserva legal:** las sociedades colombianas deben constituirla; no apartarla es una falla de cumplimiento.
- **Meter aportes como ingreso:** un aporte de socio no es venta; no toca el estado de resultados.
- **Confundir retiro del dueño con sueldo:** en una persona natural, retirar plata no es gasto; reduce patrimonio.

## Conexión con otros módulos
- **Módulo 20:** el saldo final amarra con el patrimonio del balance.
- **Módulo 21:** la utilidad del período entra aquí.
- **Módulo 22:** aportes y dividendos también aparecen como financiación en el flujo de efectivo.
- **Módulo 24 (Notas):** la política de reservas y dividendos se revela en las notas.
- **economist_lushows:** cuánto repartir vs. reinvertir es una DECISIÓN de economist; aquí solo se registra.

## Siguiente paso típico
Pasa al **módulo 24 (Notas a los estados financieros)**: los cuatro estados necesitan notas que expliquen las cifras para estar completos bajo NIIF.
