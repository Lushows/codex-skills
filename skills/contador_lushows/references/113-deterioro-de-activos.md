# 113 — Deterioro de activos (NIC 36 / Sección 27)

Tienes una máquina en libros por $50.000.000, pero se dañó parcialmente o el mercado cayó y hoy no la venderías ni la usarías para recuperar tanto. **Deterioro** es reconocer que un activo "ya no vale lo que dice en libros" y bajar su valor para no mentir en el balance. La regla de oro de la norma: **un activo nunca puede aparecer por más de lo que puedes recuperar de él**.

En **NIIF plenas** esto es la **NIC 36 — Deterioro del valor de los activos**. En **NIIF para pymes** es la **Sección 27**, con la misma idea de fondo pero menos requisitos de revelación. Aplica a propiedades, planta y equipo, intangibles, inversiones, inventarios (con su propia regla) — no a los activos financieros, que tienen su modelo propio (módulo 112).

Términos: **importe en libros** = el valor por el que está registrado el activo (costo − depreciación acumulada). **Valor recuperable** = el MAYOR entre lo que obtendrías al venderlo (valor razonable menos costos de venta) y lo que obtendrías usándolo (valor en uso = valor presente de los flujos que genera).

## La regla, en una línea

> Si **importe en libros > valor recuperable**, hay deterioro. La pérdida = la diferencia.

## El proceso

| Paso | Qué haces |
|---|---|
| 1. ¿Hay indicios? | Caída de mercado, obsolescencia, daño físico, planes de descontinuar |
| 2. Calcular valor recuperable | El mayor entre valor de venta neto y valor en uso |
| 3. Comparar | ¿Libros supera el recuperable? |
| 4. Registrar la pérdida | Llevarla al estado de resultados |
| 5. Reversión | Si después mejora, se puede revertir (salvo plusvalía/goodwill) |

## Ejemplo (cifras ILUSTRATIVAS / inventadas)

GastroLatam tiene un equipo de cómputo en libros por **$8.000.000**. Quedó parcialmente obsoleto. Estiman:
- Valor de venta neto: $3.000.000.
- Valor en uso (lo que generará usándolo, traído a valor presente): $5.000.000. (Ese valor presente lo calcula `Matematicas_lushows`.)

Valor recuperable = el MAYOR de ambos = **$5.000.000**. Como libros ($8.000.000) supera el recuperable ($5.000.000), hay deterioro de **$3.000.000**.

| Cuenta | Débito | Crédito |
|---|---|---|
| Gasto por deterioro (5299) | 3.000.000 | |
| Deterioro acumulado del equipo (1599) | | 3.000.000 |

Después del asiento, el activo neto queda en $5.000.000, justo lo recuperable. Cuadra.

## Reversión del deterioro

Si en un periodo siguiente el activo se recupera (ej. el valor en uso sube a $6.000.000), puedes **revertir** la pérdida, pero solo hasta el valor que habría tenido si nunca se hubiera deteriorado (considerando la depreciación que igual habría corrido). La **plusvalía (goodwill) NO se revierte nunca**.

## Errores comunes

- **No buscar indicios de deterioro al cierre**: la norma exige evaluarlos cada periodo.
- **Usar el menor en vez del mayor** entre valor de venta y valor en uso: es el MAYOR.
- **Confundir deterioro con depreciación**: la depreciación es el desgaste planificado; el deterioro es una caída adicional, no esperada.
- **Revertir la plusvalía**: prohibido.
- **Mezclar con inventarios**: los inventarios se ajustan a valor neto realizable con su propia regla (ver módulos 30-39), no por NIC 36.

## Conexión con otros módulos

- **30-39** (PP&E, depreciación, inventarios): el deterioro se aplica sobre estos activos ya registrados.
- **112 — NIIF 9**: el deterioro de activos financieros (cartera) usa el modelo de pérdida esperada, NO la NIC 36.
- **Matematicas_lushows**: valor en uso = valor presente de flujos futuros; cálculo del importe recuperable.
- **114 — Impuesto diferido**: el deterioro contable rara vez es deducible fiscalmente de inmediato, generando diferencia temporaria.

## Siguiente paso típico

Al cierre de cada periodo, recorre tus activos importantes y pregunta "¿hay indicios de que valga menos?". Si los hay, pide a `Matematicas_lushows` el valor en uso y compara. Luego revisa el efecto fiscal en **114 — Impuesto diferido**.
