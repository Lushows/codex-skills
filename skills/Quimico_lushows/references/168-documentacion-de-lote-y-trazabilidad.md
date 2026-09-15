# 168 — Documentación de lote y trazabilidad (si no está escrito, no pasó)

La frase que gobierna todo este módulo es de las más repetidas en la industria farmacéutica y de las menos
practicadas en las pymes: **"si no está documentado, no ocurrió"**. Un lote sin registro no se puede defender
ante un reclamo, ni investigar cuando sale mal, ni retirar del mercado con precisión, ni presentar en una
auditoría. Y lo mejor: es lo más barato de todo el sistema de calidad. No requiere equipo, no requiere planta,
requiere disciplina y un formato. Este módulo te da los formatos.

Términos: **lote (batch / lot)** = cantidad de producto fabricada en un ciclo, homogénea y con identidad única.
**Registro de lote (batch record, BMR)** = el expediente completo de fabricación de ese lote. **Trazabilidad
(traceability)** = poder seguir un material hacia adelante y hacia atrás. **Muestra de retención (retention
sample)** = porción guardada del lote. **Liberación (release)** = decisión formal de que el lote se puede
vender. **Conciliación (reconciliation)** = que las cuentas de entrada, salida y desperdicio cierren.

## El sistema de codificación de lote

Antes de cualquier formato, define cómo se llama un lote. Un buen código dice qué es y cuándo se hizo sin
consultar nada:

```
FORMATO SUGERIDO:  PP-AAMMDD-NN
   PP     código de producto        (RE = reishi cápsulas, ML = melena de león polvo…)
   AAMMDD fecha de fabricación
   NN     consecutivo del día

Ejemplo: RE-260815-01  →  reishi cápsulas, 15 de agosto de 2026, primer lote del día

REGLAS
  - Cada lote de MATERIA PRIMA también tiene su código interno, distinto del del proveedor.
  - Un lote de producto terminado registra QUÉ lotes de materia prima consumió.
  - Nunca se reutiliza un código. Nunca.
  - El código va impreso en el envase primario o secundario, junto con el vencimiento.
```

## El registro de lote: las once secciones

```
REGISTRO DE LOTE — CONTENIDO MÍNIMO

  1. IDENTIFICACIÓN
     producto, código de lote, tamaño de lote, fecha de inicio y fin, versión de la fórmula

  2. FÓRMULA CUANTITATIVA
     cada componente con: nombre, código interno, lote del proveedor,
     cantidad teórica, cantidad real pesada, quién pesó, quién verificó

  3. MATERIAS PRIMAS
     COA de cada lote consumido, fecha de recepción, resultado de la inspección de entrada (`141`)

  4. ETAPAS DE PROCESO
     por cada operación: parámetros REALES (T, tiempo, rpm, presión, vacío),
     equipo usado (identificado), hora de inicio y fin, operario, firma

  5. CONTROLES EN PROCESO
     lo que se midió durante la fabricación, con hora y resultado (`154`, `155`)

  6. RENDIMIENTOS Y CONCILIACIÓN
     teórico, real, % de rendimiento, desperdicio, explicación si se sale del rango

  7. ENVASE Y ETIQUETADO
     lote de envase, lote de etiquetas, cantidad emitida, usada, dañada y destruida

  8. ANÁLISIS DE PRODUCTO TERMINADO
     COA con métodos, resultados, criterios y comparación contra especificación (`282`)

  9. DESVIACIONES
     cualquier cosa que no salió como el procedimiento decía, con su investigación (`169`)

 10. MUESTRA DE RETENCIÓN
     cantidad guardada, ubicación, hasta cuándo

 11. LIBERACIÓN
     nombre, cargo y firma de quien libera; fecha; decisión: LIBERADO / RECHAZADO / RETENIDO
```

La sección 7 —la conciliación de etiquetas— es la que más sorprende a los emprendedores y la que más miran los
auditores. Si emitiste 5 000 etiquetas y usaste 4 850, tienen que aparecer las 150 restantes: dañadas,
destruidas o devueltas al almacén. Etiquetas sueltas en circulación son producto falsificable.

## Trazabilidad: hacia atrás y hacia adelante

```
HACIA ATRÁS (de una queja al origen)
  Cliente reclama  →  lote del envase  →  registro de lote  →  lotes de materia prima
  →  proveedor y fecha de compra  →  COA de origen
  Pregunta que debe responderse en MINUTOS: "¿qué materia prima llevaba ese frasco?"

HACIA ADELANTE (de un problema al mercado)
  Materia prima sospechosa  →  ¿qué lotes de producto la usaron?
  →  ¿a qué clientes/distribuidores fueron?  →  ¿cuánto queda en bodega?
  Pregunta que debe responderse en MINUTOS: "¿a quién le tengo que avisar?"

PRUEBA DE FUEGO (simulacro de retiro / mock recall)
  Elige un lote al azar. Cronometra cuánto tardas en:
    a) listar todas las materias primas que lo componen
    b) listar todos los clientes que lo recibieron
    c) calcular cuántas unidades quedan sin vender
  Objetivo de industria: menos de 4 horas. Hazlo una vez al año y documéntalo.
```

Un simulacro de retiro es gratis y es la mejor auditoría interna que existe. Si tardas dos días, no tienes
trazabilidad: tienes carpetas.

## Muestras de retención

| Pregunta | Respuesta de trabajo |
|---|---|
| ¿Cuánto se guarda? | Al menos el doble de lo necesario para repetir todos los ensayos de liberación |
| ¿De qué? | De cada lote de materia prima **y** de cada lote de producto terminado |
| ¿En qué envase? | En el envase primario real, cerrado |
| ¿Dónde? | En condiciones de almacenamiento declaradas, con registro de T/HR |
| ¿Cuánto tiempo? | Vida útil declarada + un margen (1 año es una práctica común) |
| ¿Para qué sirve? | Investigar reclamos, impugnar resultados (`112`), verificar estabilidad |

Sin muestra de retención, cuando llega un reclamo solo tienes la palabra del cliente contra la tuya.

## Cómo se comprueba que la documentación sirve

| Prueba | Qué se busca |
|---|---|
| Simulacro de retiro | Tiempo de respuesta y completitud |
| Revisión de registro por un tercero | ¿Se entiende sin explicaciones verbales? |
| Conciliación de rendimientos | ¿Cierran las cuentas dentro del rango? |
| Firmas | ¿Todas las etapas tienen quién ejecutó y quién verificó? |
| Correcciones | ¿Se tachó con una línea, se firmó y se fechó? (nunca corrector ni borrón) |
| Fechas | ¿Están en orden cronológico coherente? |
| Trazabilidad de etiquetas | ¿Cuadra emitidas = usadas + dañadas + destruidas? |

Reglas de buena práctica documental (ALCOA, el acrónimo que usan los auditores): los datos deben ser
**Atribuibles, Legibles, Contemporáneos, Originales y Exactos**. "Contemporáneo" significa que se anota cuando
pasa, no al final del día de memoria.

## Ejemplo aplicado — investigar un reclamo con el registro en la mano

```
Reclamo: "el frasco lote RE-260815-01 tiene el polvo apelmazado".

Con registro de lote (15 minutos):
  1. Registro de lote → humedad del polvo al envasar: 4,8 % ✔ conforme
  2. → HR ambiente registrada el día de encapsulado: 68 %   ← ALTA
  3. → lote de frascos: FR-2605, mismo proveedor de siempre
  4. → registro de envasado: NO se registró colocación de desecante  ← HALLAZGO
  5. Muestra de retención del mismo lote → humedad actual 7,9 %, a_w 0,61 → confirma
  6. Conclusión: falla en el paso de desecante + envasado con HR alta.
  7. Acción: revisar cuántos frascos del lote se distribuyeron; decidir alcance
     de la acción (aviso, reposición o retiro); corregir el procedimiento (`169`).

Sin registro de lote:
  "Puede ser la humedad de Barranquilla."  → no se sabe, no se corrige, se repite.
```

## Errores comunes

- Llenar los registros al final del día "de memoria". No es contemporáneo y se nota.
- Corregir con corrector o borrando. La corrección correcta es: una línea, el dato nuevo, firma y fecha.
- No conciliar etiquetas ni rendimientos.
- No guardar muestras de retención por ahorrar espacio.
- Confiar en que el maquilador guarda todo: pídele copia del registro de lote y guárdala tú (`167`).
- Reutilizar códigos de lote o improvisar la numeración.
- Tener los registros en un cuaderno personal en vez de en formatos versionados.
- Documentar solo lo que salió bien. Las desviaciones documentadas son señal de un sistema sano, no de un
  problema (`169`).

## Conexión con otros módulos

→ `167-bpm-gmp-para-suplementos.md` — el marco del que esto es el corazón.
→ `169-control-de-cambios-y-desviaciones.md` — qué se hace cuando el registro muestra que algo se salió.
→ `141-especificacion-de-materia-prima.md` — el registro de entrada.
→ `283-plan-de-control-de-calidad-por-lote.md` — qué se analiza en cada lote.
→ `112-como-impugnar-un-resultado.md` — donde la muestra de retención se vuelve decisiva.