# Métricas que importan y cuáles no

## La métrica madre: el ROAS de equilibrio

El ROAS a secas no dice nada. **ROAS 3,0 puede ser quiebra y ROAS 1,8 puede ser negocio**, según tu
margen. La única referencia válida es tu ROAS de equilibrio:

```
ROAS de equilibrio = Precio de venta ÷ (Precio − Costo del producto − Envío − Comisiones − Otros)
```

| Concepto | Modelo México dic-2026 |
|---|---|
| ROAS de equilibrio | **1,95** |
| CAC objetivo | USD 10,54 |
| Techo de CAC | USD 30,73 |
| Holgura | 2,92x |

Con ROAS de equilibrio 1,95: a 1,95 no ganas ni pierdes; a 2,5 ganas; a 1,6 estás pagando por
vender. Quien mira "ROAS 2,1, ¡vamos bien!" sin conocer su 1,95 está adivinando. Para calcular el
tuyo con exactitud, invoca `Matematicas_lushows`. Base conceptual en `11` y `42`.

## Qué mirar en cada etapa

| Etapa | Métrica principal | Secundarias | Ignorar |
|---|---|---|---|
| **Test de creativo (0-48 h)** | Retención a 3 s | CTR, CPM | ROAS, ventas |
| **Test de ángulo (2-5 días)** | CTR de enlace, CPC | Añadir al carrito | ROAS del día |
| **Validación (5-10 días)** | CPA | CVR, AOV | Alcance, impresiones |
| **Escala** | Margen por pedido | CPA, frecuencia | Likes, comentarios |
| **Negocio** | Margen neto mensual y caja | LTV, recompra, devoluciones | ROAS de un anuncio suelto |

## La tabla de umbrales

| Métrica | Malo | Aceptable | Bueno | Ganador |
|---|---|---|---|---|
| Retención a 3 s | < 15% | 15-25% | 25-35% | > 35% |
| CTR de enlace | < 1,0% | 1,0-1,5% | 1,5-2,2% | > 2,2% |
| CPC (México) | > 0,90 | 0,45-0,90 | 0,25-0,45 | < 0,25 |
| Visitas ÷ clics | < 70% | 70-80% | 80-90% | > 90% |
| Añadir al carrito ÷ visitas | < 4% | 4-7% | 7-12% | > 12% |
| CVR prepago | < 1,5% | 1,5-2,0% | 2,0-3,0% | > 3,0% |
| CVR contraentrega | < 3,5% | 3,5-4,5% | 4,5-6,5% | > 6,5% |
| Frecuencia (frío) | > 3,0 | 2,0-3,0 | 1,4-2,0 | < 1,4 |

Referencias de calidad creativa: conservador CTR 1,5% / CVR 2,0% prepago (4,5% COD) · bueno 2,2% /
3,0% (6,5%) · ganador real 3,0% / 4,0% (8,5%).

## Las métricas de vanidad (y por qué enamoran)

| Métrica | Por qué es engañosa | Qué mirar en su lugar |
|---|---|---|
| Alcance / impresiones | Mide gasto, no resultado | CPA |
| Likes y comentarios | Un video gracioso junta likes y no vende | CTR y CVR |
| Compartidos | Ayuda al CPM, no paga | CPM y CPA |
| CTR total (no de enlace) | Cuenta clics en el perfil, en "ver más" | CTR de enlace |
| ROAS sin contexto | Sin el de equilibrio no significa nada | ROAS vs ROAS de equilibrio |
| Ventas brutas | "Facturé 100.000" con margen negativo | Margen neto |
| Visitantes del sitio | Tráfico no es demanda | Añadir al carrito ÷ visitas |
| "Puntuación de calidad" | Diagnóstico de plataforma, no de negocio | Los números de arriba |

## El tablero de una hoja

Esto es todo lo que necesitas mirar cada mañana:

| # | Métrica | Ayer | Media 7 días | Umbral |
|---|---|---|---|---|
| 1 | Gasto | | | Presupuesto |
| 2 | Pedidos | | | — |
| 3 | CPA | | | < 10,54 |
| 4 | AOV | | | ≥ 1.099 MXN |
| 5 | Margen por pedido | | | > 0 |
| 6 | ROAS vs 1,95 | | | > 1,95 |
| 7 | CTR de enlace | | | > 1,5% |
| 8 | CVR | | | > 2,0% |
| 9 | Frecuencia del ganador | | | < 2,5 |
| 10 | Caja disponible | | | > 7 días de pauta |

Diez números. Si tu tablero tiene 40 columnas, no vas a mirarlo.

## Ventanas de tiempo: el error silencioso

| Ventana | Para qué sirve | Trampa |
|---|---|---|
| Hoy | Nada, es ruido | Decidir con el dato de las 11 a. m. |
| Últimos 3 días | Detectar caídas | Puede engañar en fin de semana |
| **Últimos 7 días** | **Decisiones normales** | — |
| Últimos 30 días | Tendencia y estacionalidad | Esconde caídas recientes |
| Desde el inicio | Contabilidad | Inútil para operar |

Regla: **decide con 7 días, alerta con 3, nunca con 1.**

## Atribución: por qué los números no cuadran

Tu plataforma dice 14 ventas. Tu pasarela dice 11. Ninguna miente del todo.

| Causa | Efecto |
|---|---|
| Atribución por vista | La plataforma se cuelga ventas que habrían ocurrido igual |
| Varias plataformas corriendo | Meta y TikTok se cuelgan la misma venta |
| Pérdida de señal (cookies, iOS) | La plataforma reporta de menos |
| Pedidos cancelados o devueltos | La plataforma no los resta |

La regla del operador: **la verdad es lo que dice tu banco**. Usa los números de la plataforma para
comparar creativos entre sí, y los del banco para saber si tienes negocio. La mecánica de atribución
y ventanas es de `facebook_ads_lushows`.

## Métricas de negocio que casi nadie mira y deciden todo

| Métrica | Por qué importa |
|---|---|
| Margen neto por pedido, después de devoluciones | Es lo que te queda de verdad |
| Tasa de devolución / cancelación | 15% de devoluciones convierte un buen ROAS en pérdida |
| Días de caja | Puedes ser rentable y quebrar (`244`) |
| Recompra a 60 días | Cada recompra es margen sin CAC (`272`) |
| Costo por pedido en atención al cliente | Tu tiempo también cuesta |

## Relacionados
`11` techo de CAC · `42` múltiplo de margen · `244` presupuestos · `263` iterar · `264` fatiga · `267` diagnóstico · `268` cuándo matar · `269` escalar
