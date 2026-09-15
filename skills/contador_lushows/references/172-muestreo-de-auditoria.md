# 172 — Muestreo: revisar una parte para concluir del todo

Como no se puede revisar el universo entero, el auditor **toma una muestra**: revisa un subconjunto de operaciones y, a partir de él, concluye sobre el total. El arte está en que la muestra sea lo bastante grande y bien escogida como para que la conclusión sea válida. Escoger mal —pocas partidas, o las equivocadas— es como probar una sopa solo de la orilla: puede engañar.

Este módulo profundiza lo que el muestreo significa en auditoría (las NIA tienen una norma dedicada, la familia NIA 530). El módulo 71 ya introdujo la idea de "no revisar todo"; aquí está el método. **Todo cálculo de tamaño de muestra y de proyección de errores se rutea a `Matematicas_lushows`.**

> **Cumplimiento + auditable.** El método de muestreo, el tamaño, cómo se seleccionaron las partidas y cómo se proyectó el error deben quedar documentados (módulo 72). Un muestreo que no se puede reconstruir, no sirve como evidencia. Este texto explica el oficio; **no reemplaza al auditor habilitado**.

## Términos que debes conocer
- **Población:** el conjunto total de operaciones o saldos a examinar (todas las facturas del año, p. ej.).
- **Muestra:** el subconjunto que efectivamente se revisa.
- **Muestreo estadístico:** usa el azar y la probabilidad; permite cuantificar el riesgo y proyectar.
- **Muestreo no estadístico (a juicio):** el auditor escoge con criterio profesional; no se cuantifica matemáticamente.
- **Error de muestreo:** el riesgo de que la muestra no represente bien al total.
- **Proyección:** estimar el error total de la población a partir del error hallado en la muestra.

## Estadístico vs. no estadístico
| Aspecto | Estadístico | No estadístico (a juicio) |
|---|---|---|
| Selección | Aleatoria / sistemática | A criterio del auditor |
| Tamaño | Calculado con fórmulas | Estimado con experiencia |
| Proyección del error | Cuantificable | Cualitativa |
| Ventaja | Defendible, objetivo | Rápido, flexible |
| Cuándo | Poblaciones grandes y homogéneas | Poblaciones pequeñas o muy específicas |

## Qué define el tamaño de la muestra
A mayor riesgo y menor materialidad, **más** partidas. Influyen: el riesgo evaluado (módulo 171), la materialidad de desempeño, la tasa de error esperada y la variabilidad de la población. **Las fórmulas (atributos para pruebas de control, variables/MUS para saldos) se ejecutan en `Matematicas_lushows`** — nunca se estiman de cabeza.

| Si… | El tamaño de muestra… |
|---|---|
| Sube el riesgo | Aumenta |
| Baja la materialidad | Aumenta |
| Sube el error esperado | Aumenta |
| Población muy uniforme | Disminuye |

## Ejemplo (cifras ILUSTRATIVAS / inventadas)
"Comercial del Valle SAS" emitió 8.000 facturas en el año (inventado). El auditor quiere probar que cada venta tiene soporte. Define un muestreo de atributos; Matematicas calcula el tamaño: 60 facturas (cifra ilustrativa) dado el riesgo y la tasa de error tolerable. Revisa las 60, encuentra 2 sin soporte. Matematicas **proyecta**: si la tasa de error de la muestra y el límite superior superan lo tolerable, la conclusión es que el control falla y hay que ampliar pruebas sustantivas.

## Errores comunes
- Tomar "unas cuantas al azar" sin método ni tamaño calculado.
- No proyectar el error de la muestra al total (encontrar 2 errores y "ahí quedó").
- Escoger solo las partidas grandes y llamarlo muestra "representativa".
- Usar muestreo estadístico sin entender la fórmula → el número sale, pero mal. Va a Matematicas.
- Mezclar poblaciones distintas (ventas y compras) en una sola muestra.

## Conexión con otros módulos
- **171 (Riesgo y materialidad)** — definen el tamaño y la tolerancia.
- **173 (Evidencia y procedimientos)** — la muestra es el insumo de los procedimientos.
- **177 (Auditoría de sistemas y datos / CAATs)** — con datos masivos a veces se prueba el 100%, no se muestrea.
- **76 (Arqueo y toma física)** — un caso típico de muestreo de saldos.
- **`Matematicas_lushows`** — ejecuta tamaño de muestra y proyección del error.

## Siguiente paso típico
Con la muestra definida, **reunir la evidencia** aplicando los procedimientos de auditoría sobre las partidas seleccionadas (módulo 173). El tamaño y la proyección se ejecutan en `Matematicas_lushows`.
