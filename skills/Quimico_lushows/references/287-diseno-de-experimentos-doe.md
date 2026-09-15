# 287 — Diseño de experimentos (DoE): dejar de probar "a ver qué pasa"

Cuando quieres optimizar una extracción, casi todo el mundo hace lo mismo: cambia una variable, mira el
resultado, cambia otra, mira otra vez. Eso se llama OFAT (*one factor at a time*) y tiene dos defectos
caros: gasta muchos ensayos y **no puede ver interacciones** — el caso en que la temperatura solo ayuda si
además subes el tiempo. El diseño de experimentos (DoE) resuelve las dos cosas: con menos corridas te dice
qué factores importan, cuánto, y dónde está el óptimo. Para una pyme esto no es lujo académico: es la
diferencia entre 30 extracciones y 11.

Términos: **factor (factor)** = variable que tú controlas (temperatura, tiempo, % de etanol). **nivel
(level)** = valor que le asignas a un factor (60 °C y 80 °C). **respuesta (response)** = lo que mides
(rendimiento, % de β-glucano, color). **interacción (interaction)** = cuando el efecto de un factor depende
del valor de otro. **replicado (replicate)** = repetición de una corrida para estimar el error experimental.
**punto central (center point)** = corrida en el punto medio de todos los factores; sirve para detectar
curvatura y estimar el error.

## Los tres tipos de diseño que de verdad vas a usar

| Tipo | Para qué sirve | Cuántas corridas | Cuándo usarlo |
|---|---|---|---|
| **Screening** (Plackett-Burman o factorial fraccionado) | Saber cuáles de muchos factores importan | 8–12 para 5–7 factores | Al inicio, cuando no sabes qué manda |
| **Factorial completo 2^k** | Efectos e interacciones de pocos factores | 2^k (+ centros) → 8 + 3 para k = 3 | Cuando ya tienes 2–4 factores candidatos |
| **Superficie de respuesta** (Box-Behnken, central compuesto) | Encontrar el óptimo, con curvatura | 15–20 para 3 factores | Al final, para afinar el punto de operación |

Secuencia recomendada: **screening → factorial → superficie**. No arranques por superficie de respuesta con
siete factores: se te va el presupuesto en el primer diseño.

## Paso a paso (el orden importa)

1. **Define la respuesta y cómo se mide.** Antes de tocar nada: ¿optimizas rendimiento en % p/p, o
   concentración del activo en mg/g, o los dos? Con qué método analítico y qué incertidumbre (`76`). Si el
   método tiene ±10 % de error, no vas a poder distinguir efectos del 5 %.
2. **Lista los factores y sus rangos realistas.** Rango que tu equipo pueda mantener de verdad. Anota los
   factores que **no** vas a variar (los mantienes fijos y los registras: son parte del resultado).
3. **Elige el diseño** según la tabla de arriba.
4. **Aleatoriza el orden de las corridas.** Si haces todas las de 60 °C el lunes y las de 80 °C el martes,
   confundes temperatura con día.
5. **Incluye puntos centrales** (mínimo 3). Te dan el error puro y te avisan si hay curvatura.
6. **Ejecuta y registra todo**, incluidas las corridas que salieron mal y por qué.
7. **Analiza** con regresión y gráfico de Pareto de efectos. Aquí se rutea a `Matematicas_lushows`: el
   ajuste, la significancia y los intervalos de confianza se **ejecutan en código**, nunca a ojo.
8. **Confirma.** Corre el óptimo predicho 2–3 veces y compara con la predicción. Si no coincide, el modelo
   no sirve fuera del rango estudiado.

## Ejemplo: factorial 2³ para una extracción acuosa de hongo

Factores y niveles **(ILUSTRATIVO)**: A = temperatura (70 / 95 °C), B = tiempo (60 / 180 min),
C = relación sólido:líquido (1:10 / 1:20 g/mL). Respuesta: β-glucano extraído en mg/g de materia prima
seca, medido por método enzimático (`221`).

```
Corrida   A(°C)   B(min)   S:L      Respuesta (mg/g, ILUSTRATIVO)
  1        70       60     1:10          41,2
  2        95       60     1:10          58,7
  3        70      180     1:10          49,5
  4        95      180     1:10          82,1
  5        70       60     1:20          46,0
  6        95       60     1:20          63,4
  7        70      180     1:20          52,8
  8        95      180     1:20          86,9
  9-11   82,5      120     1:15      64,1 / 62,8 / 65,0   (puntos centrales)

Efecto principal de un factor = (promedio nivel alto) − (promedio nivel bajo)
Efecto A = (58,7+82,1+63,4+86,9)/4 − (41,2+49,5+46,0+52,8)/4 = 72,78 − 47,38 = +25,4 mg/g
Efecto B = (49,5+82,1+52,8+86,9)/4 − (41,2+58,7+46,0+63,4)/4 = 67,83 − 52,33 = +15,5 mg/g
Efecto C = (46,0+63,4+52,8+86,9)/4 − (41,2+58,7+49,5+82,1)/4 = 62,28 − 57,88 =  +4,4 mg/g
Interacción AB = [(41,2+82,1+46,0+86,9) − (58,7+49,5+63,4+52,8)]/4 = (256,2 − 224,4)/4 = +7,95 mg/g
```

Lectura: la temperatura manda, el tiempo ayuda, la relación sólido:líquido casi no mueve la aguja en ese
rango — y existe una **interacción positiva A×B**: subir tiempo rinde mucho más si además subes temperatura.
Un OFAT nunca habría visto eso. La desviación de los tres puntos centrales (64,1 / 62,8 / 65,0) da el error
puro; efectos menores que ~2–3 veces esa desviación no se deben interpretar. Todos estos cálculos se
ejecutan y se verifican (`Matematicas_lushows`), incluida la significancia estadística.

## Qué NO puede decirte un DoE

- **Nada fuera del rango estudiado.** Si estudiaste 70–95 °C, no extrapoles a 120 °C.
- **Nada sobre factores que no incluiste.** Si el sustrato del hongo cambió a mitad del diseño, el modelo
  aprendió ruido.
- **Nada sobre calidad si tu respuesta solo mide cantidad.** Extraer más masa puede significar extraer más
  almidón (`220`). Mide siempre la respuesta que de verdad te importa, no la fácil.
- **Nada sobre estabilidad.** El óptimo de extracción puede ser el peor punto para la vida útil (`164`).

## Aplicaciones típicas en este oficio

| Problema | Factores típicos | Respuesta |
|---|---|---|
| Extracción hidroalcohólica (`145`) | % etanol, temperatura, tiempo, ratio | mg de marcador por g de planta |
| Extracción dual de hongos (`146`) | Tiempo de fase acuosa, tiempo de fase alcohólica, temperatura | β-glucano y triterpenos por separado |
| Secado por aspersión (`150`) | Temperatura de entrada, caudal, % de soporte | Rendimiento, humedad final, actividad de agua |
| Desarrollo de método LC (`81`) | % de fase orgánica, pH, temperatura de columna | Resolución, tiempo de análisis, simetría de pico |
| Formulación de emulsión (`157`) | HLB, % tensioactivo, energía de mezcla | Tamaño de gota, estabilidad a 30 días |

## Errores comunes

- **Cambiar dos cosas y no anotar la segunda.** El clásico: se cambió el lote de materia prima a mitad del
  experimento y nadie lo escribió.
- **No aleatorizar.** Convierte cualquier deriva del equipo o del día en un "efecto".
- **Sin réplicas ni puntos centrales**: no tienes con qué decidir si un efecto es real o ruido.
- **Optimizar una respuesta y arruinar otra.** Sube el rendimiento y se te va el color, el sabor o la
  estabilidad. Usa optimización multi-respuesta (función de deseabilidad).
- **Un DoE con un método analítico sin validar.** Estarás optimizando el error del método (`75`).
- **No hacer la corrida de confirmación.** El óptimo predicho es una predicción hasta que lo corres.

## Conexión con otros módulos

→ `78-estadistica-para-el-laboratorio.md` — la base estadística del análisis de efectos.
→ `76-incertidumbre-de-medida.md` — cuánto error trae tu respuesta antes de empezar.
→ `146-extraccion-dual-y-por-que-importa.md` — el caso donde el DoE paga solo.
→ `166-escalado-de-lote.md` — por qué el óptimo de laboratorio no es el óptimo de planta.
→ `288-como-disenar-un-estudio-piloto.md` — cuando el experimento es con personas, no con matraces.
→ `105-quimiometria-pca-y-modelos.md` — cuando las respuestas son espectros completos.