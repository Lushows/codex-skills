# 71 — La curva de calibración (cómo un área de pico se vuelve un miligramo)

Todo número de un COA sale de una recta. El laboratorio inyecta patrones de concentración conocida, mide el
área de cada pico, dibuja área contra concentración y ajusta una recta; luego mete el área de tu muestra en
la ecuación y despeja. Suena trivial y ahí se esconden la mitad de los errores caros: extrapolar fuera del
rango, usar el R² como si fuera prueba de exactitud, y no entender que el punto más bajo de la curva es lo
que define ese "no detectado" del reporte. Este módulo te enseña a leer una curva aunque nunca toques el
equipo.

Términos:
- **Calibrante (calibrator / calibration standard)** = cada solución de concentración conocida de la curva.
- **Respuesta (response)** = lo que mide el detector; en cromatografía, el área del pico.
- **Regresión lineal por mínimos cuadrados (ordinary least squares, OLS)** = el ajuste estándar.
- **Ponderación (weighting, 1/x o 1/x²)** = corrección que evita que los puntos altos dominen el ajuste.
- **Residual (residual)** = diferencia entre el valor observado y el que predice la recta.
- **Rango de trabajo (working range)** = el intervalo donde el método está demostrado, ni un punto más allá.

## Cómo se construye

```
Modelo:   y = m·x + b
  y = área del pico (o área analito / área estándar interno)
  x = concentración del calibrante (mg/mL, µg/mL, ppm)
  m = pendiente (sensibilidad del método)
  b = intercepto (idealmente cercano a cero)

Despeje para la muestra:   x = (y - b) / m

Curva típica (ILUSTRATIVO), CBD por HPLC-DAD a 228 nm:
  conc (µg/mL) :   1,0     5,0     25,0    100,0   250,0   500,0
  área (mAU·s) :  12.410  62.900 314.100 1.251.000 3.140.000 6.270.000

  regresión: m = 12.548 ; b = 1.120 ; R² = 0,9998
  muestra: área 1.870.000  →  x = (1.870.000 - 1.120)/12.548 = 149,0 µg/mL
```
Cualquier cuenta de estas se ejecuta en código, nunca de memoria: usa `lab-tools/diluciones.py` o rutea a
`Matematicas_lushows`.

Buenas prácticas exigibles:
- **Mínimo 5 niveles** de concentración (6 es lo habitual en farmacopea), más el blanco analizado aparte.
- Los niveles deben **cubrir el rango real de tus muestras**, con la muestra cayendo idealmente en el tercio
  central de la curva.
- La curva se corre **el mismo día** que las muestras, o se verifica con controles si es curva histórica.
- Se intercalan **verificaciones de la curva (CCV, continuing calibration verification)** cada 10–20
  inyecciones; criterio típico ±5 % (analitos mayores) a ±15 % (trazas).

## R² no es lo que la gente cree

El coeficiente de determinación mide qué tan bien la recta explica la dispersión, **no** si el modelo es el
correcto ni si el método es exacto. Con puntos muy separados, una curva claramente torcida da R² = 0,999.

Lo que sí hay que mirar:

| Diagnóstico | Qué revela | Criterio práctico |
|---|---|---|
| **Gráfico de residuales** | Curvatura, saturación del detector | Residuales deben verse aleatorios, sin forma de "U" |
| **Desviación relativa por punto (%RE)** | Exactitud punto a punto | Habitual: ±15 % en todos los niveles, ±20 % en el más bajo (criterio de bioanálisis; adapta al tuyo) |
| **Intercepto b** | Contaminación, arrastre, línea base | b debe ser pequeño frente a la respuesta del nivel más bajo |
| **Ponderación** | Si el error crece con la concentración | Rangos de 2–3 órdenes de magnitud casi siempre piden 1/x o 1/x² |
| **Sensibilidad m** | Deriva del instrumento entre corridas | Se controla en carta de control (`77`) |

ICH Q2(R2) (vigente desde junio de 2024; verifica el texto en database.ich.org) reordenó esto: ya no exige
"linealidad" como un fin en sí, sino demostrar una **relación respuesta-concentración adecuada** en el rango
declarado, admitiendo modelos no lineales si se justifican y se validan. Es un cambio de mentalidad
importante: el criterio ya no es "R² > 0,999", es "el modelo predice bien en el rango que uso".

## Por qué "no detectado" no es "cero"

Esta es la idea que más plata y más sustos ahorra.

```
La curva no baja hasta cero: baja hasta su punto más bajo validado, el LOQ.
Debajo del LOQ el método no puede dar un número confiable; debajo del LOD ni siquiera
puede afirmar presencia.

"No detectado" (ND)  = por debajo del LOD DE ESE MÉTODO
"< LOQ"              = se ve, pero no se puede cuantificar con exactitud
"< 0,01 mg/kg"       = correcto: dice el número por debajo del cual no puede afirmar

Ejemplo (ILUSTRATIVO):
  Lab A reporta "plomo: no detectado", LOQ del método = 0,50 mg/kg
  Lab B reporta "plomo: 0,12 mg/kg",  LOQ del método = 0,01 mg/kg
  No se contradicen. El lote SIEMPRE tuvo 0,12 mg/kg. El lab A simplemente
  no podía verlo. Si tu límite regulatorio fuera 0,10 mg/kg, el COA del lab A
  te habría dejado sacar al mercado un lote no conforme.
```
Regla que debes memorizar: **un COA sin LOQ no sirve para demostrar conformidad.** Y el LOQ del método debe
ser, como mínimo, del orden de 1/3 a 1/10 del límite que necesitas cumplir (ver `73`).

## Ejemplo aplicado — la muestra que se salió de la curva

```
Curva de THC total, rango 1-500 µg/mL. Extracto de resina inyectado sin diluir:
  área observada = 9.900.000  (fuera del punto más alto, 6.270.000)

Qué pasa si el laboratorio extrapola:
  x = (9.900.000 - 1.120)/12.548 = 788,9 µg/mL → "31,6 % p/p"  (ILUSTRATIVO)
Qué pasa en realidad: el detector ya está saturado, la respuesta dejó de ser proporcional,
y el valor verdadero es MAYOR que el reportado. El resultado va sesgado hacia abajo.

Lo correcto: diluir 1:5, reinyectar, caer en el tercio central de la curva y multiplicar
por el factor de dilución. Un COA que reporta valores fuera del rango de calibración,
sin nota de dilución, es una bandera roja (111).
```

## Qué preguntarle al laboratorio

1. ¿Cuántos niveles tiene la curva y cuál es el rango de trabajo validado?
2. ¿Mi muestra cayó dentro del rango o hubo dilución? ¿Cuál fue el factor?
3. ¿Usan ponderación? ¿1/x o 1/x²?
4. ¿Cuál es el LOD y el LOQ del método **para mi matriz**, no en solvente?
5. ¿Corren verificación de curva (CCV) durante la secuencia? ¿Cuál es el criterio de aceptación?
6. ¿Me pueden anexar la curva y los residuales al informe? (Un lab acreditado dice que sí sin dudar.)

## Errores comunes

- **Extrapolar por encima del último punto.** Subestima potencia; es error clásico en extractos y aceites.
- **Curva de 3 puntos.** Insuficiente para declarar rango; ICH pide típicamente 5 o más.
- **Presumir R² = 0,999 como prueba de exactitud.** No lo es; pide residuales y %RE.
- **Reportar "0" o "ausente".** Químicamente falso; lo correcto es "< LOQ" con el número del LOQ.
- **Curva en solvente para una matriz con efecto de matriz fuerte.** Sesga sin avisar (`69`, `72`).
- **No verificar la curva a mitad de secuencia.** Si el instrumento derivó a la inyección 40, las últimas 60
  muestras están mal y nadie se enteró.

## Conexión con otros módulos

→ `70-patrones-de-referencia-y-trazabilidad.md` — de dónde salen los calibrantes.
→ `72-estandar-interno-y-adicion-de-estandar.md` — cuando la calibración externa no basta.
→ `73-lod-loq-y-rango-lineal.md` — el fondo de la curva, en detalle.
→ `75-validacion-de-metodos-ich-q2-r2.md` — qué exige la guía sobre respuesta y rango.
→ `78-estadistica-para-el-laboratorio.md` — regresión, residuales y ponderación.
→ `111-banderas-rojas-en-un-coa.md` — cómo se ve una calibración mala desde el papel.
