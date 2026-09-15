# 72 — Estándar interno y adición de estándar (los dos trucos contra el efecto de matriz)

Hay dos problemas que la curva de calibración normal no resuelve: que la muestra pierda analito durante la
preparación, y que la matriz distorsione la señal del detector. Las dos soluciones clásicas son el
**estándar interno** y la **adición de estándar**. Saber cuál usó el laboratorio te dice más sobre la
calidad del resultado que la marca del equipo. En LC-MS/MS aplicado a cannabis, hongos, pesticidas y
micotoxinas, un método sin una de estas dos herramientas es un método frágil.

Términos:
- **Calibración externa (external calibration)** = la de siempre: curva de patrones en solvente, muestra aparte.
- **Estándar interno, IS (internal standard)** = compuesto que NO está en la muestra y se agrega en cantidad
  fija a todo: patrones, muestras y controles.
- **SIL-IS (stable isotope labeled internal standard)** = el mismo analito con átomos pesados (D, ¹³C, ¹⁵N);
  el mejor IS que existe.
- **Adición de estándar (standard addition)** = calibrar dentro de la propia muestra, añadiéndole analito.
- **Efecto de matriz (matrix effect)** = supresión o aumento de señal causado por la matriz (`69`).

## Estándar interno: la relación que sobrevive a los errores

En vez de usar el área del analito, se usa la **relación** área del analito / área del IS. Si algo afecta a
los dos por igual (se perdió volumen, la inyección fue menor, la fuente del MS suprimió señal), la relación
no cambia y el resultado se salva.

```
Sin IS:    y = Área_analito                  → sensible a todo lo que pase en el camino
Con IS:    y = Área_analito / Área_IS        → los errores comunes se cancelan

Ejemplo (ILUSTRATIVO), pérdida de 10 % de volumen en la preparación:
  Área analito : 100.000 → 90.000   (error de -10 %)
  Área IS      :  50.000 → 45.000
  Relación     :    2,00 →   2,00   (error 0 %)
```

Qué debe cumplir un buen IS:
1. No estar presente en la muestra.
2. Comportarse **químicamente igual** que el analito (extracción, retención, ionización).
3. Estar bien resuelto o distinguible (por masa) del analito.
4. Ser estable y disponible con pureza conocida.
5. Agregarse **al inicio**, antes de la extracción; si se agrega antes de inyectar, solo corrige inyección,
   no recuperación.

| Tipo de IS | Ejemplo | Corrige | Limitación |
|---|---|---|---|
| SIL-IS | THC-d3, psilocina-d10, ¹³C-aflatoxina B1 | Recuperación + efecto de matriz + inyección | Costo alto; no existe para todo |
| Análogo estructural | Un cannabinoide ausente en la muestra; antraceno en GC | Inyección y parte de la recuperación | No sigue perfectamente al analito |
| Homólogo | Alcano vecino en GC de solventes | Inyección | Poco selectivo |

En LC-MS/MS de residuos, los métodos serios usan SIL-IS para los analitos críticos y análogos para el resto.
Pregunta cuántos de los analitos de tu panel tienen SIL-IS: si son 5 de 80, ya sabes dónde está la
incertidumbre.

## Adición de estándar: cuando no hay matriz blanca

Se usa cuando la matriz es tan particular que no se consigue un blanco equivalente (extractos de hongo,
resinas, aguas complejas) y el efecto de matriz es fuerte.

```
Procedimiento:
  Se divide la muestra en 4 alícuotas iguales.
  A cada una se le añade 0, 1, 2 y 3 veces una cantidad conocida del analito.
  Se analiza todo y se grafica respuesta vs cantidad añadida.
  La concentración original es el valor absoluto del intercepto en el eje x.

Ejemplo (ILUSTRATIVO):
  añadido (µg/mL):   0     2,0    4,0    6,0
  respuesta (área): 41.200 82.100 122.900 164.300
  regresión: m = 20.510 ; b = 41.150
  x0 = -b/m = -41.150/20.510 = -2,006  →  concentración original = 2,01 µg/mL
```
Ventaja: la calibración ocurre **dentro de tu matriz**, así que el efecto de matriz queda incluido.
Desventaja: cuesta 4 veces más análisis por muestra y no corrige interferencias espectrales (si otra cosa
coeluye y también responde, la adición de estándar no la ve).

## Calibración con matriz emparejada: la opción intermedia

**Matrix-matched calibration**: la curva se prepara en extracto de una matriz blanca (sin analito) del mismo
tipo. Es lo estándar en pesticidas y micotoxinas de alimentos. Su punto débil obvio: conseguir matriz blanca
real. En cannabis es difícil (¿flor sin cannabinoides?), por eso allí se privilegian los SIL-IS.

| Estrategia | Corrige recuperación | Corrige efecto de matriz | Costo | Cuándo |
|---|---|---|---|---|
| Externa en solvente | No | No | Bajo | Analitos mayores, matriz limpia, prep simple |
| Externa + IS análogo | Parcial | Parcial | Bajo-medio | Rutina de potencia |
| Externa + SIL-IS | Sí | Sí | Alto | LC-MS/MS de trazas, bioanálisis |
| Matriz emparejada | No (por sí sola) | Sí | Medio | Pesticidas, micotoxinas en alimentos |
| Adición de estándar | Sí | Sí | Muy alto por muestra | Matrices únicas, disputas, pocas muestras |

## Cómo se comprueba

- **Recuperación del IS (IS response check)**: en cada muestra, el área del IS debe caer dentro de una
  ventana (típicamente 50–150 % de la media de la corrida). Si en tu muestra el IS bajó al 30 %, hubo
  supresión severa y ese resultado debe marcarse, no reportarse liso.
- **Comparación de pendientes** solvente vs matriz para estimar el ME (`69`).
- **Muestra fortificada** analizada con el método completo; recuperación dentro de criterio (`74`).

Pídele al laboratorio que te muestre el área del IS de tu muestra. Es un dato de una línea y te dice si la
corrida fue sana.

## Ejemplo aplicado — psilocibina en material fúngico para un estudio autorizado

La psilocina es inestable y se oxida; la psilocibina es muy polar y se retiene mal en fase reversa. Ambos
factores hacen que sin IS los resultados bailen entre corridas.

```
Configuración típica (ILUSTRATIVO, basada en métodos publicados de LC-MS/MS):
  IS: psilocibina-d4 y psilocina-d10, agregados a la muestra ANTES de extraer
  Extracción en frío con metanol acuoso, protegida de la luz
  Columna biphenyl o HILIC (la fase reversa C18 retiene mal la psilocibina)
  Cuantificación por relación analito/SIL-IS

Sin IS: RSD entre días reportado como pobre por inestabilidad de psilocina
Con SIL-IS: la degradación afecta a analito e IS de forma parecida y la relación se sostiene
```
Nota de línea roja: este módulo trata cuantificación analítica en contextos legales (investigación
autorizada, control forense, control de calidad donde esté permitido), no producción.

## Qué preguntarle al laboratorio

1. ¿Usan estándar interno? ¿Marcado isotópicamente o análogo? ¿Para cuáles analitos?
2. ¿En qué momento agregan el IS: antes de extraer o antes de inyectar?
3. ¿Cuál fue el área del IS en mi muestra frente a la media de la corrida?
4. ¿Calibran en solvente, en matriz emparejada, o hacen adición de estándar?
5. Si mi matriz es rara (extracto, resina, gomita), ¿validaron el método **en esa** matriz?
6. ¿Cómo reportan una muestra con supresión fuera de criterio: la repiten, la diluyen, o la reportan igual?

## Errores comunes

- **Agregar el IS al final.** Corrige la inyección y nada más; la gente cree que está cubierta y no lo está.
- **Elegir como IS algo que sí está en la matriz.** Pasa con análogos "raros" que aparecen en extractos
  naturales; el resultado sale bajo.
- **Adición de estándar con un solo punto.** Sin la recta no hay extrapolación defendible.
- **Ignorar el área del IS fuera de ventana.** Es la alerta más barata que existe y casi nadie la mira.
- **Suponer que un SIL-IS elimina todo problema.** Puede haber coelución del isotopómero, contribución
  isotópica cruzada y efectos distintos si eluyen separados (los deuterados a veces eluyen un poco antes).
- **Usar matriz emparejada "parecida".** Extracto de shiitake no es matriz blanca para reishi.

## Conexión con otros módulos

→ `69-extraccion-para-analisis-spe-y-quechers.md` — de dónde sale el efecto de matriz.
→ `71-curva-de-calibracion.md` — la calibración base.
→ `74-exactitud-precision-y-recuperacion.md` — cómo se juzga si la corrección funcionó.
→ `83-lc-ms-ms-y-mrm.md` — donde el SIL-IS es prácticamente obligatorio.
→ `256-analisis-de-psilocibina-hplc-y-lc-ms.md` — el caso completo.