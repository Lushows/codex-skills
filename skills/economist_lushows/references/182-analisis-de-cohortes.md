# 182 — Análisis de cohortes

Para ver la VERDAD sobre tu retención: agrupas a tus clientes por el mes en que entraron y sigues a cada grupo en el tiempo. Así descubres si tu negocio mejora o empeora, algo que un promedio general te oculta.

## Qué es una cohorte (en cristiano)
Una **cohorte** es un grupo de clientes que comparten un mismo punto de partida. La cohorte más común es por **mes de primera compra/registro**: "todos los que entraron en enero", "todos los de febrero", etc.

La gracia es que sigues a cada cohorte mientras envejece. En vez de preguntar "¿cuántos clientes activos tengo hoy?" (un número que mezcla viejos y nuevos), preguntas "de los que entraron en enero, ¿cuántos seguían comprando 3 meses después?". Eso es retención real, no humo.

Por qué importa: tu **promedio general miente**. Si creces rápido, los clientes nuevos (que aún no se han ido) inflan tus métricas y esconden que los viejos te abandonan. La cohorte separa "estoy creciendo" de "estoy reteniendo" (ver 89 churn/retención).

## La métrica clave: retención por cohorte
Para cada cohorte mides, mes a mes, **qué % del grupo original sigue activo** (compró, ingresó, usó el producto — tú defines "activo"). El mes 0 es siempre 100%.

Dos sabores:
- **Retención por logo/cliente:** % de clientes que siguen comprando. Bueno para suscripción y recompra.
- **Retención de ingresos (revenue retention):** % del dinero del mes 0 que el grupo sigue generando. Puede pasar de 100% si los que quedan gastan MÁS (eso es oro: "net revenue retention > 100%").

Define "activo" antes de medir. En BIO-SETA, por ejemplo: "compró al menos una vez en el mes" o "compró en los últimos 60 días" (porque la recompra de cápsulas no es mensual sino cada 1-2 meses — ajusta la ventana a tu ciclo de consumo).

## Cómo se lee una tabla de cohortes
Filas = mes de entrada. Columnas = meses transcurridos desde la entrada (Mes 0, 1, 2...). La forma es un triángulo: las cohortes viejas tienen más columnas porque han vivido más.

### Ejemplo NUMÉRICO (cifras ilustrativas, no datos reales)
Tienda de suplementos. "Activo" = compró ese mes. Cada celda es % de la cohorte que seguía comprando.

| Cohorte (mes entrada) | Clientes | Mes 0 | Mes 1 | Mes 2 | Mes 3 | Mes 4 |
|---|---|---|---|---|---|---|
| Enero | 100 | 100% | 42% | 30% | 24% | 22% |
| Febrero | 120 | 100% | 45% | 33% | 27% | — |
| Marzo | 150 | 100% | 50% | 38% | — | — |
| Abril | 180 | 100% | 55% | — | — | — |

**Cómo leerlo (3 lecturas en 1 minuto):**
1. **Lee una fila →** cómo envejece UNA cohorte. Enero: de 100 clientes, al mes 1 vuelven 42, y la cosa se estabiliza cerca de 22% (tu núcleo de fieles).
2. **Lee una columna ↓** (¡la lectura más valiosa!): compara cohortes a la MISMA edad. Mira la columna "Mes 1": 42% → 45% → 50% → 55%. **La retención al primer mes está SUBIENDO.** Algo que hiciste (mejor onboarding, mejor producto, mejor cliente) está funcionando.
3. **La cola (Mes 4 ≈ 22%)** es tu retención de largo plazo: el % que se queda "para siempre". De ahí sale tu LTV real (ver 52).

Si la columna ↓ bajara (55% → 50% → 45%), sería una alarma roja: estás atrayendo clientes de peor calidad o el producto se degrada, aunque tus ventas totales sigan subiendo por volumen.

## Cómo armar tu primera tabla (sin herramientas caras)
1. Exporta tus pedidos/registros a una hoja (columnas: cliente, fecha). En este proyecto sale de `data/orders.json` / `data/customers/`.
2. A cada cliente asígnale su **cohorte** = mes de su PRIMERA compra.
3. Para cada cliente y cada mes posterior, marca 1 si compró, 0 si no.
4. Tabla dinámica: filas = cohorte, columnas = (mes de actividad − mes de entrada), valor = % que compró.
5. Empieza con 6-12 cohortes. No necesitas software; una hoja de cálculo basta.

Regla de oro: **mide siempre el mismo "activo" y la misma ventana**, o estarás comparando peras con manzanas.

## Qué decisiones salen de aquí
- **Retención plana y decente (la curva se aplana > 0):** tienes encaje producto-mercado; vale la pena meterle a adquisición (ver 52 CAC/LTV, 120 marketing).
- **Curva que cae a casi 0:** NO escales todavía. Cada cliente nuevo se va; gastar en publicidad es llenar un balde con hueco. Arregla retención primero (ver 89).
- **Columna ↓ mejorando:** documenta qué cambiaste y dóblale la apuesta.
- **Una cohorte rara (muy buena o muy mala):** investiga qué pasó ese mes (campaña, descuento, canal). A veces un canal trae clientes basura que nunca recompran.
- **Revenue retention > 100%:** puedes crecer sin adquirir tanto; prioriza expansión/upsell sobre captación.

## Cohortes por dimensión (nivel 2)
No solo por fecha. Separa cohortes por:
- **Canal de adquisición** (Instagram vs. referido vs. anuncio): revela qué canal trae clientes que SE QUEDAN, no solo que compran una vez. Cambia dónde inviertes.
- **Primer producto comprado** (entró por Melena vs. por combo): ¿cuál "puerta de entrada" retiene mejor?
- **Ticket inicial / descuento usado:** los que entran con cupón agresivo suelen retener peor. Compruébalo con datos.

## Errores comunes
- **Mirar solo el promedio global** y celebrar crecimiento que en realidad es solo volumen tapando fuga (el error #1).
- **Ventana de "activo" mal calibrada:** si tu recompra es cada 2 meses y mides actividad mensual, todo parece churn. Ajusta al ciclo real del producto.
- **Pocos datos por cohorte:** con 5 clientes por mes, los % son ruido. Agrupa por trimestre si tu volumen es bajo.
- **Comparar cohortes de distinta edad** (la de enero tiene 6 meses, la de junio 1): solo son comparables a la MISMA columna de edad.
- **Confundir retención de clientes con retención de ingresos:** puedes perder clientes pero ganar plata si los que quedan gastan más (y viceversa). Mira ambas.
- **No definir "activo" por escrito:** cada vez lo mides distinto y los números no cuadran entre meses.

## Recordatorio de país/contexto
El análisis es universal, pero la **ventana de recompra** depende de tu sector y país (hábitos de consumo, estacionalidad, poder adquisitivo). No copies "retención buena = X%" de un blog gringo: el benchmark sano varía por industria. Para sacar tu benchmark real y tu tamaño de muestra mínimo, ver cómo conseguir datos en 21.

## Siguiente paso típico
Exporta tus pedidos, asigna a cada cliente su mes de entrada y arma una tabla de cohortes de retención de los últimos 6-12 meses. Lee la columna "Mes 1" de arriba abajo: si sube, dobla esa apuesta; si baja, congela la inversión en adquisición y arregla retención antes de escalar (ver 89, 52, 120).
