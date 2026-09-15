# 261 — Psicometría: MEQ30, 5D-ASC y las escalas del campo (cómo se mide algo que es subjetivo)

Un químico puede medir psilocina en plasma con incertidumbre del 3 %. Medir "lo que la persona vivió" es
otro oficio: la **psicometría**. Y hay que tomárselo tan en serio como a un método analítico, porque en este
campo la variable subjetiva es la que más se usa para explicar los resultados clínicos. Este módulo explica
qué instrumentos existen, qué miden, qué tan validados están y cuáles son sus límites reales.

**Alcance:** metodología de investigación. Ninguna de estas escalas es una herramienta de autodiagnóstico ni
de uso fuera de un estudio.

Términos: **psicometría (psychometrics)** = ciencia de construir y validar instrumentos de medida de
constructos psicológicos. **validez de constructo (construct validity)** = que el instrumento mida lo que
dice medir. **fiabilidad (reliability)** = que mida consistentemente. **análisis factorial confirmatorio
(confirmatory factor analysis, CFA)** = técnica para verificar la estructura de un cuestionario.

## Los instrumentos principales

| Instrumento | Qué mide | Estructura | Momento de aplicación |
|---|---|---|---|
| **MEQ30** (Mystical Experience Questionnaire) | Experiencia "mística" | 30 ítems, 4 factores: mística, ánimo positivo, trascendencia de tiempo/espacio, inefabilidad | Retrospectivo, tras la sesión |
| **5D-ASC** (5 Dimensions of Altered States of Consciousness) | Estado alterado en general | 5 dimensiones; versión ampliada de 11 factores (11-ASC) | Retrospectivo, tras la sesión |
| **EDI** (Ego Dissolution Inventory) | Disolución del yo | 8 ítems | Tras la sesión |
| **CEQ** (Challenging Experience Questionnaire) | Experiencia difícil ("mal viaje") | 7 factores | Tras la sesión |
| **PES48 / MEQ40** | Espectro extendido: místico + visual + angustiante | Ampliación validada (Stocker et al., 2024) | Tras la sesión |
| **MADRS, BDI, HAM-D** | Síntomas depresivos | Clínicas, no de experiencia | Desenlace clínico |
| **PANAS, STAI** | Afecto y ansiedad | Generales | Antes y después |

## Qué tan validado está el MEQ30

Es el instrumento más usado del campo y sí tiene respaldo psicométrico real:

- La validación revisada (Barrett, Johnson y Griffiths, 2015) mostró mediante **análisis factorial
  confirmatorio** fiabilidad y validez interna de la estructura de 4 factores, y con modelos de ecuaciones
  estructurales mostró que las puntuaciones **predicen cambios persistentes** autorreportados en actitudes,
  conducta y bienestar atribuidos a la experiencia. `[psicométrico, validado]`
- La **convergencia con el 5D-ASC es alta**: se ha reportado r ≈ 0,87 entre las puntuaciones totales de
  ambos instrumentos. Es decir, miden en buena medida lo mismo; usar los dos no duplica información.
- Trabajos recientes (Stocker et al., 2024; validación inglesa de la Psychedelic Experience Scale, 2025)
  confirmaron los cuatro factores originales y añadieron factores no cubiertos: **paradojicalidad,
  conectividad, experiencia visual y experiencia angustiante**, lo que aumentó la varianza explicada frente
  al 5D-ASC.

## Las críticas que hay que conocer

Un módulo honesto no puede vender el MEQ30 como si fuera un termómetro:

1. **Carga conceptual religiosa.** El instrumento nace de la escala de Pahnke sobre experiencia mística; sus
   ítems usan lenguaje de "unidad", "sacralidad", "certeza de realidad". Eso condiciona qué se puede
   observar y sesga hacia un marco interpretativo particular.
2. **Es retrospectivo y autorreportado.** Se responde horas o días después, con la memoria ya reconstruida y
   posiblemente influida por la expectativa y por el equipo.
3. **Correlación no es mecanismo.** Que MEQ30 correlacione con el desenlace clínico no prueba que la
   experiencia mística **cause** la mejoría; podría ser un marcador de intensidad farmacológica.
4. **Techo y no linealidad.** En dosis altas muchos participantes saturan la escala, lo que reduce su
   capacidad de discriminar.
5. **Punto de corte arbitrario.** El criterio de "experiencia mística completa" (habitualmente ≥ 60 % del
   máximo en los cuatro factores) es una convención, no un umbral biológico.
6. **No mide lo negativo.** Para eso está el CEQ; usar solo MEQ30 sesga el retrato hacia lo positivo.

## Cómo se comprueba un instrumento (los "parámetros de validación" de la psicometría)

La analogía con ICH Q2 es casi exacta, y ayuda a un químico a entender el rigor exigible:

| Concepto analítico | Equivalente psicométrico |
|---|---|
| Especificidad | Validez de constructo y discriminante |
| Exactitud | Validez de criterio (contra un patrón externo) |
| Precisión / repetibilidad | Fiabilidad (alfa de Cronbach, omega, test-retest) |
| Linealidad | Funcionamiento del ítem (teoría de respuesta al ítem, IRT) |
| Robustez | Invarianza de medida entre grupos e idiomas |
| Transferencia de método | Validación de la traducción y adaptación cultural |

Ese último punto importa en Colombia: **una escala en inglés no es válida en español hasta que se adapta y
se valida**. Traducir no es validar.

## Ejemplo aplicado (ILUSTRATIVO) — reporte de un estudio

```
n = 30, dosis única supervisada, medición a las 7 h post-dosis

  MEQ30 total (0–100 normalizado):  media 62,4 (DE 21,8)
  "Experiencia mística completa" (≥ 60 % en los 4 factores): 17/30 = 56,7 %
  5D-ASC OBN (unidad oceánica):     media 58,1 (DE 24,0)
  CEQ total:                        media 19,7 (DE 15,2)   ← lo difícil también se reporta
  Correlación MEQ30 total con cambio en MADRS a semana 6: r = 0,41 (IC 95 % 0,06–0,67)

Lectura honesta: correlación moderada, con intervalo de confianza amplio y n pequeño.
No permite afirmar causalidad ni predecir el resultado de un individuo.
```

Fíjate en el detalle del intervalo de confianza: reportar solo "r = 0,41, p < 0,05" habría escondido cuánta
incertidumbre hay. Es el mismo principio de `05` y `76` aplicado a datos psicológicos.

## Errores comunes

- **Reportar MEQ30 y omitir CEQ.** Cuentas solo la mitad de lo que pasó.
- **Tratar el punto de corte como un hecho biológico.** Es una convención.
- **Usar la escala en español sin validación de la adaptación.** El instrumento deja de ser el instrumento.
- **Interpretar la correlación con el desenlace como mecanismo.** Es una de las preguntas abiertas del campo.
- **Aplicar MEQ30 en microdosis.** Está diseñada para experiencias intensas; en dosis bajas no discrimina
  (`264`).
- **Olvidar que el cegamiento condiciona la respuesta.** Si el participante sabe qué recibió, su reporte ya
  está influido (`262`).

## Conexión con otros módulos

→ `262-set-setting-y-diseno-de-estudio.md` — el contexto que moldea lo que se mide.
→ `257-farmacologia-de-la-psilocibina.md` — la discusión sobre si la experiencia es necesaria.
→ `259-dosis-en-investigacion-clinica.md` — dosis y respuesta subjetiva.
→ `288-como-disenar-un-estudio-piloto.md` — cómo elegir desenlaces.
→ `78-estadistica-para-el-laboratorio.md` — correlación, IC, tamaño de efecto.
→ `12-niveles-de-evidencia.md` — cómo pesar un autorreporte.
