# 74 — Exactitud, precisión y recuperación (dar en el blanco vs dar siempre en el mismo punto)

Un método puede darte el mismo número diez veces y estar diez veces equivocado. Otro puede oscilar y estar
centrado en el valor verdadero. Son dos propiedades distintas y se demuestran con experimentos distintos:
**exactitud** es qué tan cerca estás de la verdad, **precisión** es qué tan poco te dispersas. La
recuperación es la manera práctica de estimar la exactitud cuando no existe un material certificado de tu
matriz, que es casi siempre el caso en hongos y cannabis.

Términos:
- **Exactitud (accuracy / trueness)** = cercanía al valor verdadero. Su opuesto operativo es el **sesgo (bias)**.
- **Precisión (precision)** = dispersión entre medidas repetidas. Se expresa como **RSD** o **%CV**.
- **Repetibilidad (repeatability)** = misma muestra, mismo analista, mismo equipo, mismo día.
- **Precisión intermedia (intermediate precision)** = mismo laboratorio, distinto día/analista/equipo.
- **Reproducibilidad (reproducibility)** = entre laboratorios distintos.
- **Recuperación (recovery)** = fracción del analito añadido que el método vuelve a encontrar.

## La diana: las cuatro combinaciones

```
   Exacto y preciso        Preciso pero sesgado      Exacto pero impreciso     Ni lo uno ni lo otro
        o o                       o o                      o                          o
       o o                       o o                    o     o                   o        o
   (centro dado)          (agrupado, fuera del      (disperso, promedio         (disperso y fuera)
                            centro: sesgo)            en el centro)

El caso peligroso es el segundo: se ve profesional (RSD 1 %) y está mal.
Solo se detecta con un CRM, un spike o una comparación interlaboratorio.
```
La precisión sola no prueba nada sobre la verdad. Cuando un proveedor te muestra tres COA idénticos como
prueba de calidad, te está mostrando precisión, no exactitud.

## Cómo se demuestra cada una

| Propiedad | Experimento | Cálculo | Criterio típico (ILUSTRATIVO, defínelo tú) |
|---|---|---|---|
| Repetibilidad | 6 réplicas al 100 % o 3 niveles x 3 réplicas | RSD % | <= 2 % para analitos mayores; <= 15 % en trazas |
| Precisión intermedia | >= 2 días, >= 2 analistas | RSD % combinado | <= 3 % mayores; <= 20 % trazas |
| Exactitud vía CRM | Analizar el CRM como muestra | % del valor certificado | 97–103 % mayores |
| Exactitud vía spike | Fortificar matriz a 3 niveles, 3 réplicas | % recuperación | 95–105 % mayores; 70–120 % trazas |
| Exactitud vía comparación | Método nuevo vs método de referencia | prueba t pareada | Sin diferencia significativa (p > 0,05) |

Sobre los criterios: **ICH Q2(R2) deliberadamente no fija números.** Su exigencia es que el laboratorio
**predefina** el criterio de aceptación antes de validar, lo justifique según el uso previsto, y reporte el
estimado con su intervalo de confianza. Es una diferencia importante frente a la versión anterior: ya no
basta con "cumplió"; hay que decir cuál era el objetivo y con qué confianza se alcanzó. Verifica el texto
vigente en database.ich.org antes de escribir tu protocolo.

## Recuperación: la fórmula y sus trampas

```
% recuperación = (C_fortificada - C_muestra) / C_añadida x 100

Ejemplo (ILUSTRATIVO), cadmio en polvo de reishi:
  C_muestra      = 0,082 mg/kg
  C_añadida      = 0,100 mg/kg
  C_fortificada  = 0,171 mg/kg
  → (0,171 - 0,082) / 0,100 x 100 = 89,0 %
```
Trampas que hay que conocer:

1. **Fortificar al nivel equivocado.** Si añades 10 veces lo que hay, la recuperación sale bonita y no dice
   nada del nivel real de trabajo. Se fortifica cerca del LOQ, cerca del límite y en la parte alta del rango.
2. **Fortificar sobre el extracto en vez de sobre la matriz.** Solo mide el paso instrumental; no evalúa la
   extracción. El spike debe hacerse **sobre la muestra sólida** y dejarse equilibrar (30–60 min típicos).
3. **Corregir por recuperación sin declararlo.** Si el laboratorio multiplica los resultados por 1/0,89, debe
   decirlo en el COA. Los criterios difieren por sector; en residuos suele no corregirse y en cambio se exige
   que la recuperación esté en 70–120 %.
4. **Recuperación alta (>120 %).** Casi siempre es interferencia o contaminación, no "mejor método".

## Precisión: cómo se calcula y qué es aceptable

```
RSD % = (s / media) x 100

Ejemplo (ILUSTRATIVO), 6 réplicas de THC total en flor (% p/p base seca):
  18,7  19,1  18,9  19,3  18,8  19,0
  media = 18,97 ; s = 0,218 ; RSD = 1,15 %   → repetibilidad buena

Precisión intermedia, mismos 6 en otro día con otro analista:
  19,4  19,6  19,2  19,8  19,3  19,5  → media 19,47 ; s = 0,216
  Diferencia entre días: 19,47 - 18,97 = 0,50 (2,6 % relativo)
  RSD intermedia combinada ≈ 1,8 %  → aceptable para un método de potencia
```
Referencia útil para juzgar reproducibilidad entre laboratorios: la **ecuación de Horwitz**, que predice el
RSD esperado según la concentración del analito. Empíricamente, a menor concentración, mayor RSD; es normal
que un analito en ppb tenga RSD de 15–25 % entre laboratorios y eso no significa que alguien esté haciendo
las cosas mal.

| Nivel del analito | RSD entre laboratorios que se considera normal |
|---|---|
| ~10 % p/p (potencia) | 2–5 % |
| ~0,1 % p/p (1000 mg/kg) | 5–8 % |
| ~1 mg/kg (ppm) | 10–16 % |
| ~10 µg/kg (ppb) | 20–30 % |

Esta tabla es la respuesta cuando alguien dice "un laboratorio me dio 0,8 ppm y otro 1,0 ppm, uno miente".
No necesariamente: a ese nivel, 20 % de diferencia entre laboratorios es el estado del arte.

## Ejemplo aplicado — auditar un informe de validación de potencia de cannabis

```
Lo que debe estar y qué mirar:

  Exactitud   : spikes a 3 niveles x 3 réplicas → 96,8 % · 99,1 % · 101,4 %  (ILUSTRATIVO)
                Criterio predefinido: 95-105 %. Cumple.
  Repetibilidad: 6 réplicas al 100 % → RSD 1,2 %. Criterio <= 2 %. Cumple.
  Precisión intermedia: 2 días x 2 analistas → RSD 2,4 %. Criterio <= 3 %. Cumple.
  Recuperación de THCA cerca del LOQ: 78 %  ← BANDERA. Si el criterio era 95-105 %,
                                              el método NO está validado a ese nivel
                                              y no debería reportar valores bajos.
```
Ese último renglón es el tipo de hallazgo que solo aparece si pides el informe de validación, no solo el COA.

## Qué preguntarle al laboratorio

1. ¿Me pueden enviar el resumen de validación con exactitud, precisión y rango para **mi** matriz?
2. ¿Cuáles fueron los criterios de aceptación **predefinidos** y quién los aprobó?
3. ¿A qué niveles fortificaron y sobre qué (matriz sólida o extracto)?
4. ¿Corrigen los resultados por recuperación? Si sí, ¿aparece declarado en el COA?
5. ¿Cuál es su precisión intermedia real de rutina para este ensayo (dato de cartas de control)?
6. ¿Participan en ensayos de aptitud (proficiency testing) para este analito y cómo salieron?

Esa última pregunta es la más poderosa: el **ensayo de aptitud interlaboratorio** es la única evidencia
externa de exactitud que existe. Un laboratorio con buenos z-scores te lo muestra con gusto.

## Errores comunes

- **Confundir precisión con exactitud.** Tres resultados iguales no prueban que sean correctos.
- **Validar en matriz fácil y aplicar en matriz difícil.** Validado en aceite, usado en gomita: no vale.
- **Fortificar solo al nivel alto.** Deja el LOQ sin demostrar.
- **Aceptar un método sin datos de precisión intermedia.** La repetibilidad del mismo día siempre se ve bien.
- **Exigir 100 % de recuperación en trazas.** Irreal; 70–120 % es el estándar del sector.
- **Discutir con un laboratorio por diferencias dentro del error esperado.** Antes de reclamar, calcula si la
  diferencia es significativa (`78`, `112`).

## Conexión con otros módulos

→ `73-lod-loq-y-rango-lineal.md` — el nivel donde la recuperación se degrada.
→ `75-validacion-de-metodos-ich-q2-r2.md` — el marco formal completo.
→ `76-incertidumbre-de-medida.md` — cómo se junta todo en un solo número.
→ `77-control-de-calidad-analitico-y-cartas-control.md` — cómo se vigila en rutina.
→ `78-estadistica-para-el-laboratorio.md` — pruebas t, F y z-scores.
→ `112-como-impugnar-un-resultado.md` — cuándo una diferencia justifica reclamar.
