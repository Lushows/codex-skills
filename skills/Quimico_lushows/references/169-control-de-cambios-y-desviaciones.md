# 169 — Control de cambios y desviaciones (cómo se cambia algo sin romper todo lo demás)

Todo producto cambia: se acaba un proveedor, sube el precio de un excipiente, el maquilador cambia de equipo,
alguien propone mejorar el proceso. El control de cambios es el procedimiento que garantiza que un cambio se
evalúe **antes** de hacerlo, y que se identifique qué otras cosas quedan invalidadas — la estabilidad, la
etiqueta, el registro sanitario. La desviación es lo contrario: algo que ya pasó y no debía. Manejar ambas
cosas por escrito es lo que separa una empresa que aprende de una que repite el mismo error tres veces al año.

Términos: **control de cambios (change control)** = proceso formal para evaluar, aprobar e implementar un
cambio. **Desviación (deviation)** = apartamiento de un procedimiento o especificación aprobado. **OOS (out of
specification)** = resultado fuera de especificación. **OOT (out of trend)** = dentro de especificación pero
fuera de la tendencia histórica. **CAPA (corrective and preventive action)** = acción correctiva (arregla lo
que pasó) y preventiva (impide que vuelva a pasar). **Causa raíz (root cause)** = el porqué real, no el
síntoma.

## Cambio vs desviación

| | Cambio | Desviación |
|---|---|---|
| Cuándo se documenta | **Antes** de hacerlo | **Cuando ocurre**, o al detectarlo |
| Quién lo inicia | Quien propone la mejora | Quien detecta el problema |
| Pregunta central | ¿Qué se invalida si hago esto? | ¿Por qué pasó y qué hago con el lote? |
| Resultado | Aprobado / rechazado / aprobado con condiciones | Lote liberado / rechazado / reprocesado + CAPA |
| Si no se hace | Se rompe la validación en silencio | Se repite el problema |

## Matriz de impacto: qué invalida cada cambio

Esta es la tabla que hay que tener a la mano. La columna que más duele es la última.

| Cambio | ¿Reanaliza? | ¿Nueva estabilidad? | ¿Cambia etiqueta? | ¿Afecta registro sanitario? |
|---|---|---|---|---|
| Proveedor de materia prima | Sí, lote completo | Recomendable | Si cambia origen/parte usada | Puede requerir aviso |
| Especie o parte usada del hongo | **Sí** | **Sí** | **Sí** | **Sí** |
| Solvente o proceso de extracción | Sí | **Sí** | Posible | **Probable** |
| % de marcador declarado | Sí | No necesariamente | **Sí** | **Sí** |
| Excipiente (nuevo o distinto grado) | Sí | **Sí** (`160`) | Sí, lista de ingredientes | Probable |
| Tipo de cápsula (gelatina ↔ HPMC) | Sí | **Sí** | Sí | Probable |
| Envase primario | Sí | **Sí** (`163`, `164`) | Posible | Posible |
| Tamaño de lote / escala | Sí, validación | Al menos un lote al estudio | No | Normalmente no |
| Equipo de fabricación | Sí, validación | Depende | No | Normalmente no |
| Maquilador / planta | Sí, validación completa | **Sí** | Sí (fabricante) | **Sí** |
| Vida útil declarada | — | Debe estar respaldada | Sí | Sí |
| Diseño gráfico sin cambio de contenido | No | No | Sí | Verificar |

A agosto de 2026, qué cambios exigen modificación del registro sanitario ante INVIMA se verifica caso a caso
contra el Decreto 3249 de 2006 y los trámites vigentes (`266`, `269`). La regla prudente: **si el cambio toca
composición, fabricante, marca o vida útil, asume que hay que notificarlo hasta comprobar lo contrario.**

## El formato de control de cambios

```
SOLICITUD DE CONTROL DE CAMBIOS  N° CC-2026-007

  1. Qué se propone cambiar (estado actual → estado propuesto)
  2. Por qué (costo, disponibilidad, calidad, obsolescencia)
  3. Clasificación:  menor / mayor / crítico
  4. EVALUACIÓN DE IMPACTO — marcar y justificar cada uno:
       [ ] Especificación de materia prima      [ ] Método analítico
       [ ] Proceso de fabricación               [ ] Validación de proceso
       [ ] Estabilidad y vida útil              [ ] Envase
       [ ] Etiqueta y arte                      [ ] Registro sanitario
       [ ] Costo unitario                       [ ] Documentación y POE
  5. Acciones requeridas antes de implementar (con responsable y fecha)
  6. Plan de verificación posterior (¿cómo sabremos que salió bien?)
  7. Aprobación: técnico + calidad + dirección. Firmas y fecha.
  8. Cierre: evidencia de que se hicieron las acciones. Fecha de cierre.
```

El paso 4 es todo el valor del formato. Cambiar de proveedor de maltodextrina parece trivial hasta que marcas
la casilla de "estabilidad" y te das cuenta de que tienes que repetir seis meses de estudio.

## El manejo de una desviación

```
FLUJO DE DESVIACIÓN

  1. DETECTAR y CONTENER
     Poner el lote en CUARENTENA. Nada sale hasta que se decida.
  2. DESCRIBIR
     Qué pasó, cuándo, quién lo detectó, qué lotes están afectados, evidencia objetiva.
  3. EVALUAR IMPACTO INMEDIATO
     ¿Hay riesgo para la seguridad del consumidor?  → si sí, escala de inmediato.
     ¿Hay producto ya distribuido?                  → activa trazabilidad (`168`).
  4. INVESTIGAR LA CAUSA RAÍZ
     Herramientas: 5 porqués, Ishikawa (personas, método, material, máquina, medio, medición).
     La causa raíz NUNCA es "error humano" a secas. Pregunta por qué el sistema lo permitió.
  5. DECIDIR EL DESTINO DEL LOTE
     liberar con justificación / reprocesar / reclasificar / rechazar y destruir.
  6. CAPA
     Correctiva: arregla este caso.
     Preventiva: impide la reincidencia (cambia el procedimiento, el formato, el control).
  7. VERIFICAR EFICACIA
     A los 3–6 meses: ¿volvió a pasar? Si volvió, la CAPA no era la correcta.
  8. CERRAR con firma.
```

## El resultado fuera de especificación (OOS)

Un OOS no se resuelve repitiendo el análisis hasta que dé bien. Ese es el pecado capital del laboratorio y es
un hallazgo de auditoría grave.

```
INVESTIGACIÓN DE UN OOS — FASE I (laboratorio, antes de tocar el producto)
  ¿Error de cálculo?  ¿Estándar vencido o mal preparado?  ¿Equipo descalibrado?
  ¿Muestra mal tomada o mal homogeneizada (`67`)?  ¿Método mal aplicado?
  → Si se encuentra un error de laboratorio DOCUMENTABLE, se invalida el resultado
    y se repite. Sin causa demostrada, el resultado ES VÁLIDO.

FASE II (producción)
  Revisar registro de lote: parámetros reales, materia prima, desviaciones previas.
  Analizar muestra de retención y contramuestra.
  Considerar reanálisis con nueva toma de muestra según protocolo PREDEFINIDO
  (número de réplicas y criterio de decisión escritos ANTES, no después).

REGLA DE ORO: nunca se descarta un resultado sin causa asignable documentada.
"Nos dio raro, lo repetimos y ya" no es una investigación (`112`, `113`).
```

## Ejemplo aplicado — el proveedor que sube el precio

```
Situación: el proveedor de extracto de reishi sube 40 %. Hay una alternativa más barata.

CC-2026-011 — Cambio de proveedor de extracto de reishi

  Estado actual:   Proveedor A, extracto dual, β-glucano 34,2 %, triterpenos 1,6 %
  Propuesto:       Proveedor B, extracto dual, β-glucano declarado 30 %, triterpenos no declara

  EVALUACIÓN DE IMPACTO
  [x] Especificación de MP    → B no declara triterpenos: ¿es dual de verdad? (`146`)
  [x] Fórmula unitaria        → con 30 % harían falta 500 mg/cáps en vez de 469 → ¿cabe? (`154`)
  [x] Estabilidad             → matriz distinta (¿otro soporte?) → repetir estudio (`164`)
  [x] Etiqueta                → si baja el aporte por cápsula, cambia el número declarado
  [x] Registro sanitario      → cambio de composición: verificar exigencia ante INVIMA
  [x] Costo                   → rutear el análisis a `economist_lushows`

  ACCIONES ANTES DE IMPLEMENTAR
   1. Pedir a B: COA de 3 lotes con β-glucano, α-glucano y triterpenos por método declarado.
   2. Analizar por cuenta propia 1 lote en laboratorio tercero (`108`).
   3. Lote piloto y verificación de llenado (`166`).
   4. Iniciar estabilidad acelerada 3 meses antes de decidir (`165`).

  DECISIÓN ILUSTRATIVA: no implementar hasta tener los 4 puntos.
  El ahorro del 40 % no compensa reprocesar etiqueta, estabilidad y registro.
```

Ese ejercicio de 20 minutos con un formato es lo que evita descubrir el problema con 10 000 frascos impresos.

## Errores comunes

- Cambiar primero y documentar después (o nunca).
- Considerar "menor" un cambio de proveedor de materia prima. Casi nunca lo es.
- Repetir un análisis hasta que dé conforme, sin causa asignable.
- Cerrar una desviación con "se capacitó al personal" como única acción. No es una CAPA: es un parche.
- Poner "error humano" como causa raíz. La pregunta siguiente siempre es: ¿por qué el sistema lo permitió?
- No verificar la eficacia de la CAPA a los meses.
- Cambiar el envase y no repetir estabilidad. El estudio es del sistema producto-envase (`163`).
- No avisar a INVIMA de un cambio que sí lo requería y descubrirlo en una inspección.
- No documentar desviaciones "para que el archivo se vea limpio". Un archivo sin desviaciones en dos años no
  es señal de excelencia: es señal de que no se registran.

## Conexión con otros módulos

→ `168-documentacion-de-lote-y-trazabilidad.md` — el registro donde vive la evidencia.
→ `167-bpm-gmp-para-suplementos.md` — el sistema del que esto es un procedimiento obligatorio.
→ `164-estabilidad-ich-q1-y-vida-util.md` — lo que más se invalida con un cambio.
→ `112-como-impugnar-un-resultado.md` — el lado analítico del OOS.
→ `284-auditoria-de-proveedor.md` — cómo se califica al proveedor nuevo antes de cambiarlo.