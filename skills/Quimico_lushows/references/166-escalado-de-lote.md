# 166 — Escalado de lote (por qué lo que funciona en 1 kg falla en 100 kg)

El escalado es el cementerio de los productos buenos. Una fórmula que sale perfecta en el laboratorio se
convierte en un lote irregular en planta, y el dueño no entiende qué cambió si "es la misma receta". Lo que
cambió es la física: la transferencia de calor, la de masa y el mezclado **no escalan proporcionalmente**. Este
módulo te da las reglas para que el salto de piloto a producción no te cueste el primer lote comercial, y para
que sepas qué exigirle al maquilador cuando el proceso deja de ser tuyo.

Términos: **escalado (scale-up)** = pasar de un tamaño de lote a otro mayor. **Lote piloto (pilot batch)** =
tamaño intermedio, típicamente ≥ 1/10 del comercial. **Relación superficie/volumen (S/V)** = superficie de
intercambio por unidad de volumen; cae al crecer el equipo. **Número de Reynolds (Re)** = régimen de flujo,
laminar o turbulento. **Punto final (endpoint)** = criterio que dice cuándo terminar una operación.
**Validación de proceso (process validation)** = demostrar que el proceso da resultados consistentes.

## Lo que NO escala linealmente

| Fenómeno | Qué pasa al crecer | Consecuencia práctica |
|---|---|---|
| Transferencia de calor | S/V cae: en un tanque grande hay menos pared por litro | Calentar y enfriar tardan mucho más |
| Mezclado | El tiempo de mezcla crece más que proporcional | Zonas muertas, mezcla no homogénea |
| Evaporación | Área de superficie libre no crece como el volumen | Concentrar tarda mucho más (`149`) |
| Filtración | La torta se compacta con más masa | Ciclos más largos, presiones mayores |
| Secado | El gradiente de humedad dentro del lecho | Secado desigual (`142`) |
| Molienda | Calor acumulado | Sube la temperatura del producto (`143`) |
| Sedimentación/segregación | Más masa, más camino | El polvo se segrega en el transporte |

La regla mental: **el volumen crece con el cubo de la dimensión, la superficie con el cuadrado.** Duplicas el
diámetro del tanque, el volumen se multiplica por 8 y el área de pared solo por 4. Por eso el tanque grande
calienta la mitad de eficiente por litro.

## Cómo se escala cada operación

```
EXTRACCIÓN (marmita)
  NO escales por "misma potencia de calentamiento".
  Escala por: misma temperatura del líquido, mismo tiempo A TEMPERATURA,
              misma relación S/L, misma velocidad de punta del agitador.
  velocidad de punta (tip speed) = π × D × N   [m/s]
    D = diámetro del impulsor (m), N = revoluciones por segundo
  Mantener la velocidad de punta constante es el criterio más usado para
  escalar mezclado con cizallamiento.
  OJO: el tiempo de CALENTAMIENTO no es tiempo de extracción. Cronometra desde
  que llega a temperatura, no desde que prendes.

MEZCLADO DE POLVOS
  Escala por: mismo grado de llenado del mezclador (típicamente 50–70 %),
              mismo número de revoluciones TOTALES (no mismo tiempo).
  Verifica siempre con muestreo en 8–10 puntos del mezclador (arriba, medio,
  abajo, centro, periferia) y análisis del marcador.
  Criterio de homogeneidad: RSD de las muestras ≤ 5 % (criterio de trabajo habitual).

SECADO POR ASPERSIÓN
  Escala por: misma temperatura de SALIDA (`150`), misma relación
              caudal de alimentación / caudal de aire.

ENCAPSULADO
  Escala por: mismo polvo (densidad, flujo, humedad). El equipo cambia el
              mecanismo de dosificación (dosificador vs disco), y eso
              cambia la masa de llenado. Reajusta y revalida.
```

## Las tres etapas de escala

| Etapa | Tamaño típico | Objetivo | Qué se define aquí |
|---|---|---|---|
| Laboratorio | 0,1–1 kg | ¿Funciona la química? | Solvente, tiempos, marcador, fórmula |
| **Piloto** | 5–50 kg (≥ 1/10 del comercial) | ¿Sobrevive a un equipo real? | Puntos finales, rendimientos, tiempos reales |
| Comercial | 100 kg+ | ¿Es reproducible? | Validación de 3 lotes consecutivos |

El **piloto no es opcional**. Saltar de laboratorio a comercial es apostar el lote más caro de tu historia. Si
el maquilador te propone hacerlo directo, esa es tu decisión de riesgo, no la suya.

## La regla del 1/10 y la validación

La práctica establecida en industria farmacéutica —y aplicable como buena práctica a suplementos— es que el
lote piloto que sostiene el desarrollo sea de **al menos un décimo** del comercial, y que la validación del
proceso se haga con **3 lotes consecutivos** que cumplan todos los criterios. Ese es el paquete que un auditor
espera ver (`167`, `168`).

```
PROTOCOLO DE VALIDACIÓN DE PROCESO (estructura mínima)

  1. Descripción del proceso y de los equipos (marca, modelo, capacidad).
  2. Parámetros críticos de proceso (CPP) con su rango:
       ej. temperatura de extracción 92–98 °C; tiempo 110–130 min;
           velocidad de punta 1,8–2,2 m/s; humedad final del polvo ≤ 5,0 %.
  3. Atributos críticos de calidad (CQA) y sus criterios (`141`, `282`).
  4. Muestreo intensificado: más puntos que en producción de rutina.
  5. Criterios de aceptación explícitos.
  6. 3 lotes consecutivos conformes.
  7. Informe firmado y conclusión: proceso validado / no validado.
```

## Cómo se comprueba que el escalado salió bien

| Comprobación | Cómo | Criterio |
|---|---|---|
| Rendimiento de sólidos | Balance de masa por etapa | Dentro de ±10 % del piloto |
| Recuperación de activo | Balance de activo (`140`) | Dentro de ±10 % del piloto |
| Homogeneidad de mezcla | 8–10 puntos del mezclador | RSD ≤ 5 % |
| Uniformidad de unidades | Masa y contenido (`154`) | Farmacopea (`280`) |
| Perfil analítico | Cromatograma comparado con el piloto | Sin picos nuevos |
| Tiempos reales | Registro de proceso | Documentados y dentro de rango |
| Estabilidad | Al menos un lote comercial al estudio (`164`) | Igual o mejor que el piloto |

**El chequeo que revela casi todo:** comparar el cromatograma del lote comercial contra el del piloto. Si
aparece un pico nuevo, la escala cambió la química (más tiempo a temperatura, más oxígeno, más cizallamiento).

## Ejemplo aplicado — el lote que salió con menos potencia

```
Síntoma: el piloto de 10 kg dio extracto con β-glucano 34,2 %.
         El primer lote comercial de 100 kg dio 27,8 %. Misma "receta".

Investigación (`169`)
  Paso 1 — comparar registros:
     piloto:    llegó a 95 °C en 18 min, 2 h a temperatura, agitación 2,0 m/s
     comercial: llegó a 95 °C en 95 min, 2 h a temperatura, agitación 1,1 m/s
  Paso 2 — hipótesis:
     (a) 95 min de calentamiento = 95 min extra de exposición térmica no contabilizados
     (b) la velocidad de punta bajó casi a la mitad → transferencia de masa menor
  Paso 3 — verificar: analizar el BAGAZO del lote comercial.
     bagazo comercial 14,1 % de β-glucano vs bagazo piloto 8,9 %
     → NO se degradó: NO SE EXTRAJO. La causa es (b), la agitación.
  Paso 4 — acción correctiva: subir rpm hasta recuperar 2,0 m/s de velocidad de punta;
     reextraer el bagazo del lote afectado si el balance lo justifica.
  Paso 5 — CAPA documentada y actualización del parámetro crítico (`169`).
```

Cifras **(ILUSTRATIVAS)**. Lo importante es el método: **el bagazo es el testigo que distingue "se degradó" de
"no se extrajo"**, y son problemas opuestos con soluciones opuestas.

## Errores comunes

- Escalar por "mismo tiempo total" sin descontar el tiempo de calentamiento.
- Escalar la agitación por rpm en vez de por velocidad de punta.
- Mezclar polvos "el mismo tiempo" en un mezclador más grande: el número de revoluciones cambia.
- Saltarse el piloto para ahorrar tiempo y perder el primer lote comercial completo.
- No muestrear el mezclador en varios puntos y descubrir la falta de homogeneidad en el análisis de producto
  terminado.
- Cambiar de equipo (otro molino, otro secador) y llamarlo "el mismo proceso".
- No documentar los parámetros reales del piloto. Sin ese registro, no hay contra qué comparar.
- Entregarle el proceso al maquilador sin parámetros críticos definidos: fabricará como le funcione a él.

## Conexión con otros módulos

→ `140-de-la-materia-prima-al-producto.md` — el mapa de operaciones que se está escalando.
→ `168-documentacion-de-lote-y-trazabilidad.md` — dónde se registran los parámetros reales.
→ `169-control-de-cambios-y-desviaciones.md` — cómo se maneja el lote que se salió.
→ `287-diseno-de-experimentos-doe.md` — cómo definir los rangos de los parámetros críticos.
→ `292-negociar-con-laboratorios-y-maquiladores.md` — qué exigirle por contrato a quien fabrica.