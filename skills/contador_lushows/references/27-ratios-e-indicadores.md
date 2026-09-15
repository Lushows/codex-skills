# 27 — Ratios e Indicadores Financieros

Un **ratio** (o indicador) es una división entre dos cifras de los estados financieros que resume, en un solo número, algo difícil de ver a simple vista: si puedes pagar tus deudas, qué tan endeudado estás, qué tan rentable eres y qué tan rápido mueves tu plata. Son el "tablero de instrumentos" del negocio.

Importante para la promesa de la casa: aquí aprendes **qué significa cada ratio y cómo leerlo**. El **cálculo exacto se ejecuta y verifica en código vía Matematicas_lushows** (con `decimal`, nunca de cabeza). Y **decidir qué hacer** con un ratio malo es de economist_lushows.

## Las cuatro familias de ratios

| Familia | Pregunta que responde | Fuente |
|---|---|---|
| **Liquidez** | ¿Puedo pagar lo que debo pronto? | Balance (módulo 20) |
| **Endeudamiento** | ¿Cuánto del negocio es de terceros? | Balance |
| **Rentabilidad** | ¿Qué tanto gano sobre lo que vendo/invierto? | P&L + balance |
| **Actividad (eficiencia)** | ¿Qué tan rápido muevo cartera, inventario, pagos? | P&L + balance |

### Liquidez
| Indicador | Qué compara | Cómo leerlo |
|---|---|---|
| Razón corriente | Activo corriente ÷ pasivo corriente | >1 = el corto plazo está cubierto |
| Prueba ácida | (Activo corriente − inventario) ÷ pasivo corriente | Más exigente: ¿pago sin vender inventario? |
| Capital de trabajo | Activo corriente − pasivo corriente | Cuánta "holgura" tengo en pesos |

### Endeudamiento
| Indicador | Qué compara | Cómo leerlo |
|---|---|---|
| Nivel de endeudamiento | Pasivo total ÷ activo total | Qué % del negocio financian terceros |
| Apalancamiento | Pasivo total ÷ patrimonio | Cuánto debo por cada peso propio |

### Rentabilidad
| Indicador | Qué compara | Cómo leerlo |
|---|---|---|
| Margen neto | Utilidad neta ÷ ventas | Cuánto queda de cada peso vendido |
| ROA (retorno sobre activos) | Utilidad neta ÷ activo total | Qué tan bien uso lo que tengo |
| ROE (retorno sobre patrimonio) | Utilidad neta ÷ patrimonio | Qué ganan los dueños sobre lo suyo |

### Actividad
| Indicador | Qué compara | Cómo leerlo |
|---|---|---|
| Rotación de cartera | Ventas a crédito ÷ cuentas por cobrar | Qué tan rápido cobro |
| Rotación de inventario | Costo de ventas ÷ inventario | Qué tan rápido vendo lo que tengo |
| Días de pago a proveedores | (Proveedores ÷ compras) × 365 | En cuántos días pago |

## Ejemplo rotulado — cifras ILUSTRATIVAS / inventadas

Usando los estados de La Sazón S.A.S. (módulos 20 y 21):

| Indicador | Cifras usadas | Resultado | Lectura |
|---|---|---:|---|
| Razón corriente | 21.500.000 ÷ 12.000.000 | 1,79 | Por cada $1 que debo a corto plazo tengo $1,79. Sano. |
| Nivel de endeudamiento | 27.000.000 ÷ 35.500.000 | 76,1% | Terceros financian el 76% del negocio. Alto: vigilar. |
| Margen neto | 14.700.000 ÷ 120.000.000 | 12,3% | De cada $100 vendidos quedan $12,3. |
| ROE | 14.700.000 ÷ 8.500.000 | 172,9% | Muy alto, pero por un patrimonio bajo (poca base propia). |

**Lectura honesta:** la liquidez se ve bien, pero el endeudamiento del 76% es alto y el ROE altísimo es más síntoma de poco patrimonio que de gran rentabilidad. Un solo ratio nunca cuenta toda la historia: se leen en conjunto y contra el sector. Cada división se ejecuta en código vía Matematicas_lushows. Lo que se hace al respecto lo decide economist.

## Cómo leer ratios sin engañarte
1. **Compara contra ti mismo** (el año anterior) y contra **el sector**: un 12% de margen puede ser excelente o pésimo según el negocio.
2. **Léelos en grupo:** liquidez buena + endeudamiento alto puede convivir.
3. **Un número raro casi siempre tiene una causa concreta** en una cuenta del balance o P&L.

## Errores comunes
- **Calcular de cabeza:** la promesa es error cero; todo ratio va a Matematicas_lushows.
- **Comparar con denominadores distintos:** ventas a crédito ≠ ventas totales para rotación de cartera.
- **Tomar un ratio aislado como veredicto:** un ROE alto puede esconder un patrimonio diminuto.
- **Ignorar el sector:** los rangos "sanos" cambian por industria.
- **Saltar a la decisión:** interpretar es de aquí; decidir, de economist.

## Conexión con otros módulos
- **Módulos 20 y 21:** son la fuente de todos los ratios.
- **Módulo 22:** complementa la liquidez con generación real de caja.
- **Módulo 26:** vertical/horizontal y ratios se refuerzan mutuamente.
- **Matematicas_lushows:** EJECUTA cada cálculo de ratio y verifica el resultado.
- **economist_lushows:** toma los ratios y DECIDE (subir precios, reducir deuda, capitalizar).

## Siguiente paso típico
Si el negocio tiene varias empresas relacionadas, ve al **módulo 28 (Consolidación básica)**. Si ya quieres usar todo esto para decidir, salta al **módulo 29 (Leer estados para decidir)**.
