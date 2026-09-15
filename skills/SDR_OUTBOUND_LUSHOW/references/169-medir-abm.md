# 169 — Medir ABM (engagement de cuenta, no leads sueltos)

Medir ABM con las métricas del outbound de volumen es el error que hace que los programas ABM parezcan un fracaso cuando en realidad van bien. En volumen mides **leads y reuniones sueltas** (ver funnel `81`, métricas `80`); en ABM la unidad es la **cuenta**, y lo que mides es cuánto se está **calentando la cuenta entera** hacia una decisión. Este módulo es el cuadro de mando de ABM: qué medir, cómo definir "engagement de cuenta", y por qué la paciencia con los números es parte del método (ABM tiene ciclos largos y pocas cuentas: los promedios pequeños engañan).

## El principio: pocas cuentas → la estadística de volumen miente

Con 30 cuentas Tier A no puedes razonar como con 5.000 correos. Un "reply rate del 4%" sobre 30 cuentas no dice nada útil. Lo que importa es el **movimiento de cada cuenta** por una escalera de compromiso: de fría → consciente → interesada → en conversación → en oportunidad. La métrica reina es el **account engagement**: la suma de señales (aperturas, respuestas, clics en ads, asistencia a eventos, consumo de contenido, personas del comité activadas) que indica que la cuenta se está acercando. Subes cuentas de escalón, no cuentas de correos.

## Las métricas que importan en ABM

| Nivel | Métrica | Qué te dice |
|---|---|---|
| **Cobertura** | % de cuentas objetivo con contacto abierto | ¿Estás trabajando la lista de verdad? |
| **Cobertura** | Contactos activados por cuenta (multi-thread) | ¿Estás single o multi-threading? (`162`) |
| **Engagement** | Account engagement score (señales sumadas) | ¿La cuenta se calienta? La métrica central |
| **Engagement** | % del comité involucrado | ¿Cubres los roles que deciden? (`165`) |
| **Progresión** | Cuentas que suben de etapa / mes | El verdadero "avance" en ABM |
| **Progresión** | Cuentas → oportunidad (SQL de cuenta) | El handoff que vale (`72`, `73`) |
| **Resultado** | Win rate y ACV de cuentas ABM vs no-ABM | ¿ABM gana más y más grande? |
| **Resultado** | Velocidad del ciclo en cuentas ABM | ¿El aire acelera el cierre? |
| **Eficiencia** | Costo por oportunidad de cuenta | Justifica el esfuerzo (`economist_lushows`) |

La estrella es el **account engagement score** + la **progresión de etapa de cuenta**. Las métricas de resultado (win rate, ACV, ciclo) se comparan **ABM vs no-ABM** para probar que el programa vale.

## Cómo construir un account engagement score (práctico)

No necesitas una plataforma cara; puedes armarlo con puntos por señal, sumados a nivel cuenta:

```
Señal                                   Puntos
Apertura de email                          1
Respuesta de un contacto                   5
Clic en ad / visita a landing              2
Interacción con contenido (167)            3
Registro a evento (166)                    4
Asistencia a evento                        8
Nuevo contacto del comité activado         5
Respuesta del decisor económico (165)     10
-------------------------------------------------
Suma por cuenta, ventana de 30 días → nivel de engagement:
  0–5   FRÍA        6–15  TIBIA
 16–30  CALIENTE   31+    EN JUEGO (prioridad máxima)
```

Herramientas: Clay (`31`) o el CRM (`141`) para sumar señales; plataformas ABM (6sense, Demandbase, HubSpot ABM) lo automatizan si el presupuesto da. Umbrales y ponderaciones exactas → **`Matematicas_lushows`** (aquí va el método; el número fino se calcula y se calibra con resultados, ver `79`).

## Etapas de cuenta (el "funnel" de ABM)

En vez del funnel de leads (`81`), ABM usa un funnel de **cuentas**:

```
Cuenta objetivo → Comprometida (engagement > umbral) → En conversación
   → Oportunidad de cuenta → Cerrada (ganada/perdida)
```

Reportas cuántas cuentas hay en cada etapa y cuántas **avanzaron** este mes. El movimiento entre etapas es tu señal de salud, mucho más que cualquier tasa de apertura.

## Paciencia y tamaño de muestra (no te engañes con pocos datos)

- ABM tiene **ciclos largos** (meses) y **pocas cuentas**: los primeros meses verás engagement subir mucho antes de ver deals cerrados. Es normal; el engagement es el **indicador adelantado**.
- No calcules "tasas" finas sobre 20–40 cuentas: los porcentajes saltan por azar. Mira **movimiento absoluto** (cuántas subieron de etapa) y tendencias, no decimales.
- Da al programa **al menos un ciclo de venta completo** antes de juzgar resultados de cierre. Mientras tanto, juzga por engagement y progresión.

## Ejemplo: tablero mensual de ABM (30 cuentas Tier A)

```
Cobertura:     28/30 cuentas con al menos 1 hilo abierto (93%)
               Multi-thread promedio: 3.4 contactos/cuenta
Engagement:    EN JUEGO 4 | CALIENTES 9 | TIBIAS 11 | FRÍAS 6
               Comité cubierto (decisor tocado): 19/30
Progresión:    Subieron de etapa este mes: 7 cuentas
               Nuevas oportunidades de cuenta: 3
Resultado:     Win rate ABM 28% vs 11% no-ABM | ACV 2.1x mayor
```

Ese tablero cuenta la historia real: no "mandé 400 correos", sino "de 30 cuentas soñadas, 13 están calientes o en juego y 3 pasaron a oportunidad".

## Errores comunes (qué NO hacer)

- **Medir ABM con métricas de volumen** (nº de correos, reply rate global): esconde el progreso real por cuenta.
- **Impaciencia:** matar el programa en 6 semanas porque "no hay ventas". El ciclo es largo; mira engagement primero.
- **Sacar tasas finas de 20 cuentas:** ruido estadístico. Usa absolutos y tendencia.
- **No comparar ABM vs no-ABM:** sin el contraste no pruebas que el esfuerzo extra vale (win rate/ACV/ciclo).
- **Contar aperturas como éxito:** apertura es señal débil; ponderá más respuesta del decisor y avance de etapa.

## Frontera y siguiente paso

Este módulo mide hasta la **oportunidad de cuenta**. El pipeline, el forecast y el cierre del deal → venta enterprise en **`ventas_lushows`** y forecasting en `82`. Cálculos y calibración del score exactos → **`Matematicas_lushows`**. El ROI del programa → `economist_lushows`.

**Siguiente paso:** define tu account engagement score con la tabla de arriba, monta las etapas de cuenta en el CRM (`141`) y arma el tablero mensual. Compara ABM vs no-ABM en win rate y ACV. Con esto cierras el Bloque 16 — vuelve a `160` para el mapa completo y a `98` para hacerlo un sistema replicable.
