# 77 — Control de calidad analítico y cartas de control: cómo sabes que el laboratorio sigue midiendo bien hoy

Un método validado te dice que el laboratorio midió bien **el día de la validación**. El control de calidad
analítico (analytical quality control, AQC) es lo que te dice que sigue midiendo bien **el día que corrió tu
lote**. Es la diferencia entre un resultado defendible y un número salido de un equipo que se desajustó hace
tres semanas y nadie se dio cuenta. Si contratas laboratorios, esto es lo que debes exigir ver: no la
validación de hace dos años, sino la evidencia de desempeño de la corrida donde iba tu muestra.

Términos:
- **Control de calidad (quality control, QC)** = muestras de concentración conocida que se corren junto con
  las tuyas para demostrar que el sistema estaba bajo control.
- **Aptitud del sistema (system suitability test, SST)** = chequeos que se hacen ANTES de inyectar muestras
  reales; si fallan, no se corre nada.
- **Carta de control (control chart)** = gráfico del valor del QC a lo largo del tiempo, con líneas de aviso
  y de acción.
- **Deriva (drift)** = cambio lento y sostenido de la respuesta del equipo (columna que envejece, lámpara
  que pierde intensidad, fuente de iones que se ensucia).
- **Sesgo (bias)** = error sistemático: todos los resultados corridos hacia arriba o hacia abajo.

## Las tres capas del control de calidad

| Capa | Qué es | Cuándo se corre | Si falla |
|---|---|---|---|
| **Aptitud del sistema (SST)** | Inyección de una solución de referencia para ver resolución, factor de cola, platos teóricos, RSD de área | Antes de cada secuencia, y a veces intercalada | No se inyecta la secuencia; se corrige el equipo |
| **QC de matriz (matrix QC / control sample)** | Muestra real de composición conocida (o fortificada) que atraviesa TODO el método, incluida la preparación | Al menos 1 cada 10–20 muestras | Se invalida el bloque de muestras entre dos QC buenos y se repite |
| **Blancos** (method blank, reagent blank) | Todo el procedimiento sin muestra | Al inicio y cada bloque | Se investiga contaminación; crítico en metales (`88`) y solventes (`87`) |

Regla que separa laboratorios serios de los demás: **el QC de matriz debe entrar por la misma puerta que tu
muestra**, o sea desde la molienda/extracción, no inyectarse ya listo en el vial. Un QC que solo prueba el
instrumento no dice nada sobre la preparación de muestra, que es donde ocurren la mayoría de los errores
(`68`, `69`).

## Aptitud del sistema: los números que se revisan

```
Criterios típicos de SST en HPLC (ILUSTRATIVO — el laboratorio los define en su método):

  Resolución (Rs) entre el par crítico ............ >= 1,5
  Factor de cola (tailing factor, T) .............. 0,8 - 2,0
  Eficiencia (platos teóricos, N) ................. >= 2000
  RSD del área en 5-6 inyecciones repetidas ....... <= 1,0 % (contenido)
                                                    <= 5 %   (trazas)
  Desviación del tiempo de retención .............. <= 2 % vs el método
  Respuesta del patrón de chequeo vs curva ........ 98 - 102 %

En LC-MS/MS se agregan (83):
  Razón de iones (ion ratio) cualificador/cuantificador dentro de ±20-30 % del patrón
  Señal del estándar interno dentro de ±50 % de la media de la corrida
```

Si el laboratorio no te puede decir cuál es su par crítico ni su criterio de resolución, no tiene método
escrito: tiene una costumbre.

## La carta de control: leer el equipo como se lee un electrocardiograma

Se grafica el valor medido del QC (o su % de recuperación) contra el número de corrida. Se calculan la media
(x̄) y la desviación estándar (s) con al menos 20 corridas históricas, y se trazan:

```
  Línea central .............. x̄
  Límites de aviso (warning)   x̄ ± 2s
  Límites de acción (action)   x̄ ± 3s
```

Reglas de Westgard (las que usan los laboratorios clínicos y cada vez más los de alimentos):

| Regla | Qué ve | Qué significa |
|---|---|---|
| **1₃ₛ** | Un punto fuera de ±3s | Rechazo. Error aleatorio grande o falla puntual |
| **2₂ₛ** | Dos puntos seguidos fuera del mismo ±2s | Rechazo. Sesgo sistemático apareciendo |
| **R₄ₛ** | Un punto en +2s y el siguiente en −2s | Rechazo. Imprecisión creciente |
| **4₁ₛ** | Cuatro seguidos fuera del mismo ±1s | Aviso. Deriva |
| **10x̄** | Diez seguidos del mismo lado de la media | Aviso. Sesgo instalado (columna nueva, patrón nuevo, calibrante mal preparado) |

La regla **1₂ₛ** (un punto fuera de ±2s) NO se usa como rechazo: estadísticamente ocurre en ~5 % de las
corridas normales. Un laboratorio que rechaza por 1₂ₛ está repitiendo trabajo sin razón.

## Ejemplo aplicado — carta de control de β-glucano en un extracto de reishi

BIO-SETA envía extractos a un laboratorio que cuantifica β-glucano por Megazyme K-YBGL (`221`). El
laboratorio guarda un lote de extracto homogeneizado como material de control interno (in-house QC material)
y lo corre en cada tanda.

```
Material de control: extracto de Ganoderma lucidum, lote QC-2025-03, homogeneizado y
                     alicuotado en 60 viales de 2 g, sellados, a -20 C.
Valor asignado (media de 20 corridas): 28,4 % p/p base seca de beta-glucano   (ILUSTRATIVO)
Desviación estándar (s):               0,9 % p/p                              (ILUSTRATIVO)

  Aviso  : 26,6 - 30,2 % p/p     (x̄ ± 2s)
  Acción : 25,7 - 31,1 % p/p     (x̄ ± 3s)

Corridas 41 a 46 (ILUSTRATIVO):
  41: 28,1   ok
  42: 27,9   ok
  43: 27,2   ok  (por debajo de la media)
  44: 27,0   ok  (4 seguidas por debajo → regla 4-1s: AVISO)
  45: 26,4   fuera de aviso
  46: 25,9   fuera de aviso, dos seguidas 2-2s → RECHAZO

Diagnóstico real más probable: el lote nuevo de enzima liquenasa perdió actividad,
o el bano de incubacion se corrió de 40 a 37 C. No es que tu extracto empeoró.
```

Sin carta de control, ese laboratorio te habría reportado 25,9 % y tú habrías culpado a tu proveedor de
materia prima. Con carta de control, se detecta que el problema es del método y se repite la tanda.

## Materiales que sirven como QC

| Tipo | Qué es | Cuándo usarlo | Costo aproximado (ILUSTRATIVO) |
|---|---|---|---|
| **CRM** (certified reference material) | Material con valor certificado y trazabilidad metrológica (NIST, ERM, LGC) | Lo mejor; obligatorio para metales y micotoxinas | USD 300–1.200 por unidad |
| **RM** (reference material) | Material caracterizado sin certificación completa | Cuando no existe CRM de tu matriz | USD 100–400 |
| **QC interno** | Lote propio homogeneizado y caracterizado por varias corridas | Matrices raras (extracto de hongo, gomita de CBD) | Costo del lote + caracterización |
| **Muestra fortificada** (spike) | Matriz blanco + adición conocida de patrón | Recuperación en cada tanda | Costo del patrón (`70`) |

Para hongos y cannabis casi nunca existe un CRM de tu matriz exacta. A agosto de 2026 hay CRM de hoja de
cannabis y de flor para cannabinoides (por ejemplo, materiales del NIST y de proveedores comerciales) y CRM
de setas para metales pesados; para β-glucanos en extracto de reishi, prácticamente no. Ahí el QC interno es
la única salida honesta, y hay que decirlo en el informe.

## Qué preguntarle al laboratorio

1. ¿Me pueden mandar el **resultado del QC de la corrida donde iba mi muestra**, no solo mi resultado?
2. ¿El QC pasa por la **preparación completa** o se inyecta ya listo?
3. ¿Usan **CRM**? ¿Cuál, de qué proveedor y de qué matriz?
4. ¿Tienen **carta de control** de este ensayo? ¿Me la muestran?
5. ¿Cuál fue la **recuperación del spike** en mi tanda y cuál es su criterio de aceptación?
6. ¿Qué hacen cuando el QC falla: repiten toda la tanda o solo la muestra?
7. ¿Participan en **ensayos de aptitud** (proficiency testing / round robin)? ¿Con quién y con qué resultado
   en el último ciclo? (En cannabis existen esquemas comerciales de PT; en hongos funcionales son escasos.)

## Errores comunes

- **Pedir la validación y no el QC de la corrida.** La validación es historia; el QC es el presente.
- **Aceptar un COA sin blanco de método** en metales pesados o solventes residuales: la contaminación de
  laboratorio es la causa #1 de falsos positivos en esos ensayos.
- **Creer que un CRM de una matriz sirve para otra.** Un CRM de harina de trigo no controla la extracción de
  un extracto oleoso de cannabis.
- **Rechazar por 1₂ₛ.** Genera repeticiones costosas y "resultados escogidos" (se repite hasta que dé bonito).
- **QC preparado por la misma persona, el mismo día, del mismo patrón que la curva.** Entonces el QC no es
  independiente y no detecta un error de preparación del calibrante. El QC debe venir de un **patrón de
  origen distinto** (second-source standard).
- **No archivar el material de QC.** Si el lote de QC se acaba y el nuevo no se solapa con el viejo, la carta
  de control se rompe y hay que reconstruirla desde cero.

## Conexión con otros módulos

→ `74-exactitud-precision-y-recuperacion.md` — de dónde salen la media y la s del control.
→ `75-validacion-de-metodos-ich-q2-r2.md` — la validación que este control mantiene viva.
→ `76-incertidumbre-de-medida.md` — el QC alimenta la estimación de incertidumbre.
→ `78-estadistica-para-el-laboratorio.md` — las pruebas que sostienen estas reglas.
→ `107-iso-17025-y-acreditacion.md` — el QC es requisito de la norma, no un lujo.
→ `111-banderas-rojas-en-un-coa.md` — un COA sin evidencia de QC es una bandera roja.
