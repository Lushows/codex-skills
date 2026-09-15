# 26 — Análisis Vertical y Horizontal

Tener los estados financieros bien armados (módulos 20–25) es como tener una radiografía. El **análisis vertical y horizontal** es leerla: convierte montos en pesos en **proporciones** y **tendencias** que te dicen qué está pasando. Son las dos lecturas más simples y poderosas, y no requieren más que dividir y restar — cálculos que, fieles a la promesa de la casa, se **ejecutan y verifican en código vía Matematicas_lushows**, nunca de cabeza.

Aquí aprendes **qué significan** los resultados. **Decidir qué hacer** con ellos es de economist_lushows.

## Análisis vertical: ¿cómo se reparte el todo?

Toma cada partida y la expresa como **porcentaje de un total** del mismo período. Responde: *¿qué tanto pesa cada cuenta?*

- En el **estado de resultados**, el total base son las **ventas** (= 100%).
- En el **balance**, el total base es el **total de activos** (= 100%).

Fórmula conceptual: `% vertical = partida ÷ total base × 100`.

| Para qué sirve | Ejemplo de hallazgo |
|---|---|
| Ver la estructura de costos | "El costo de ventas se come el 40% de cada peso vendido" |
| Detectar gastos inflados | "Los gastos de admón. son el 25%, mucho para el sector" |
| Comparar entre empresas de distinto tamaño | Dos negocios distintos se comparan en %, no en pesos |

## Análisis horizontal: ¿cómo cambió en el tiempo?

Compara la misma partida entre **dos períodos** y mide la **variación**. Responde: *¿esto subió o bajó, y cuánto?* Por eso NIIF exige comparativos (módulo 25): sin dos años, no hay análisis horizontal.

Fórmulas conceptuales:
- Variación absoluta: `año actual − año anterior`
- Variación relativa (%): `(año actual − año anterior) ÷ año anterior × 100`

| Para qué sirve | Ejemplo de hallazgo |
|---|---|
| Ver crecimiento o caída | "Las ventas crecieron 25% frente al año pasado" |
| Detectar alertas | "Los gastos crecieron 40% pero las ventas solo 25%: ojo" |
| Medir el ritmo | "La cartera crece más rápido que las ventas: ¿estamos cobrando mal?" |

## Ejemplo rotulado — cifras ILUSTRATIVAS / inventadas

**La Sazón S.A.S. — Análisis del Estado de Resultados (COP)**

| Concepto | 2025 | Vertical 2025 | 2024 | Horizontal (Δ%) |
|---|---:|---:|---:|---:|
| Ventas | 120.000.000 | 100,0% | 96.000.000 | +25,0% |
| Costo de ventas | 48.000.000 | 40,0% | 36.000.000 | +33,3% |
| **Utilidad bruta** | **72.000.000** | **60,0%** | **60.000.000** | **+20,0%** |
| Gastos de admón. | 30.000.000 | 25,0% | 24.000.000 | +25,0% |
| Gastos de ventas | 18.000.000 | 15,0% | 14.000.000 | +28,6% |
| **Utilidad operacional** | **24.000.000** | **20,0%** | **22.000.000** | **+9,1%** |

**Lectura honesta:** las ventas crecieron 25%, pero el costo creció 33,3% — más rápido. Eso explica por qué la utilidad operacional solo subió 9,1% pese a vender mucho más. El análisis señala el problema (el costo se está comiendo el crecimiento); decidir si renegociar proveedores o subir precios es de economist. Todos los % se ejecutan en código vía Matematicas_lushows.

## Cómo combinarlos
- **Vertical** te da la foto de la estructura de UN período.
- **Horizontal** te da la película de cómo cambió entre dos.
- Juntos: "los gastos pesan 40% de las ventas (vertical) Y vienen creciendo más rápido que las ventas (horizontal)" → señal fuerte.

## Errores comunes
- **Dividir por el total equivocado:** en el P&L se divide por ventas; en el balance, por total activos.
- **Comparar contra un año atípico:** si el año base fue malísimo, todo "crece" engañosamente.
- **Mirar solo el %:** un crecimiento de 200% sobre una base de $10.000 sigue siendo poca plata.
- **Calcular de memoria:** un error de centavos invalida la conclusión; siempre a Matematicas_lushows.
- **Confundir análisis con decisión:** este módulo describe; no concluye "hay que despedir gente".

## Conexión con otros módulos
- **Módulos 20 y 21:** estos estados son la materia prima del análisis.
- **Módulo 25:** los comparativos NIIF habilitan el horizontal.
- **Módulo 27 (Ratios):** los ratios profundizan lo que vertical/horizontal insinúan.
- **Matematicas_lushows:** ejecuta toda división, porcentaje y variación con `decimal`.
- **economist_lushows:** convierte los hallazgos en decisiones (precios, costos, inversión).

## Siguiente paso típico
Pasa al **módulo 27 (Ratios e indicadores)** para medir liquidez, endeudamiento y rentabilidad con precisión, más allá de la proporción simple.
