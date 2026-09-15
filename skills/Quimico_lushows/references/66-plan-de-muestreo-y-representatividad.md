# 66 — Plan de muestreo y representatividad (el error más grande y el más barato de arreglar)

El análisis nunca mide tu lote: mide el gramo que entró al instrumento. Si ese gramo no representa las
200 000 gramos del lote, el resultado es exacto y falso al mismo tiempo. En materiales fúngicos y en flor de
cannabis el muestreo aporta más error que todo el laboratorio junto, y es la única etapa que tú controlas
sin comprar un equipo. Un plan de muestreo escrito de una página vale más que cambiar de laboratorio.

Términos:
- **Lote (batch / lot)** = cantidad de material producida en condiciones uniformes, con un identificador único.
- **Incremento (increment)** = cada porción individual tomada del lote.
- **Muestra compuesta (composite / primary sample)** = la suma de todos los incrementos.
- **Muestra de laboratorio (laboratory sample)** = lo que se envía tras reducir la compuesta.
- **Sesgo de muestreo (sampling bias)** = error sistemático que ninguna repetición del análisis corrige.
- **Segregación (segregation)** = separación espontánea de partículas por tamaño o densidad durante el transporte.

## La regla de oro: muchos incrementos pequeños, no un incremento grande

El error fundamental de muestreo baja con el **número de incrementos**, no con la masa de un solo puñado.
Tomar 1 kg de un solo punto es peor que tomar 20 porciones de 50 g repartidas en el lote, aunque la masa
final sea idéntica.

Reglas prácticas de la industria (a agosto de 2026; ninguna es ley universal, verifica la norma de tu
jurisdicción y de tu cliente):

| Regla | Enunciado | De dónde viene | Cuándo usarla |
|---|---|---|---|
| Raíz de n | Muestrear √n de n unidades (a veces √n+1) | Práctica de inspección agrícola, siglo XX; discutida estadísticamente | Bultos/tambores de material presuntamente homogéneo |
| Incrementos fijos | 20–30 incrementos mínimo por lote | Muestreo incremental (ISM) en suelos: 30–100 incrementos | Material heterogéneo, contaminantes |
| Regla del regulador | Lo que diga tu norma local | Programas estatales de cannabis, farmacopeas | Siempre manda esta |

Advertencia honesta: la regla √n es **conveniencia histórica, no teoría estadística**; funciona como piso, no
como justificación. Si la decisión es cara (liberar 200 kg, defender un registro sanitario), sube el número
de incrementos y documenta por qué.

## Ejemplo A — lote de polvo de hongos (BIO-SETA)

Lote: 120 kg de polvo de cuerpo fructífero de melena de león, en 6 bultos de 20 kg.

```
1. Unidades del lote: n = 6 bultos → √6 = 2,45. La regla mínima diría 3 bultos.
   Decisión: muestrear los 6, porque el polvo se segrega por finos y el costo extra es cero.

2. Incrementos: 3 por bulto (superior, medio, fondo) con lanza de muestreo (sampling spear)
   → 18 incrementos x 50 g = 900 g de muestra compuesta.

3. Homogeneizar la compuesta y reducir por cuarteo hasta ~200 g (ver 67).

4. Dividir: 100 g al laboratorio · 100 g de contramuestra sellada en la empresa.

5. Rotular cada frasco: producto, lote, fecha, hora, quién muestreó, número de incrementos.
```
La lanza es importante: sin ella solo alcanzas la capa superior, que en polvos casi siempre está
enriquecida en partícula gruesa y empobrecida en finos, y los finos son donde se concentran β-glucano y
también los metales.

## Ejemplo B — lote de flor de cannabis

La flor es peor que el polvo: la potencia varía entre plantas, entre posiciones de la planta (cogollo apical
vs bajero) y entre partes del mismo cogollo (los tricomas se desprenden y caen al fondo del recipiente).

```
Lote: 15 kg de flor seca, 30 bolsas de 500 g, de 40 plantas.

1. Unidades: 30 bolsas → muestrear al menos 10 (regla mínima 6, se sube por heterogeneidad).
2. 2 incrementos por bolsa, uno de arriba y uno del fondo = 20 incrementos x 5 g = 100 g.
3. No sacudir el fondo aparte: el kief del fondo tiene 3-5x la potencia de la flor entera
   y sesga hacia arriba (ILUSTRATIVO). Se homogeneiza TODO junto.
4. Moler la compuesta completa (molienda criogénica si se van a medir terpenos, ver 67 y 199).
5. Reducir por cuarteo a 15 g: 5 g al lab, 10 g de contramuestra.
```
Muchos programas regulados exigen que el muestreo lo haga **el laboratorio o un muestreador certificado**, no
el productor, justamente porque el sesgo aquí es trivial de introducir a propósito. A agosto de 2026, Nueva
York publicó un estándar dedicado de sistema de calidad de muestreo de cannabis (Office of Cannabis
Management, documento de enero de 2026); verifica el estándar vigente en tu jurisdicción antes de escribir
tu SOP.

## Cuarteo: cómo se reduce una muestra sin sesgar

```
Cuarteo manual (coning and quartering):
  1. Verter la compuesta formando un cono sobre superficie limpia e inerte.
  2. Aplanar el cono en un disco parejo.
  3. Dividir en 4 cuadrantes con una espátula.
  4. Descartar 2 cuadrantes opuestos, unir los otros 2.
  5. Repetir hasta la masa objetivo.

  120 kg → compuesta 900 g → 450 → 225 → ~110 g (3 cuarteos)
```
Alternativa mejor cuando existe: **divisor rotatorio (riffle splitter / rotary divider)**, que hace la
división mecánicamente y elimina el criterio de la mano. Pregúntale al laboratorio si lo tiene.

## Qué preguntarle al laboratorio

1. ¿Quién muestrea: ustedes o yo? Si soy yo, ¿me dan el SOP y las bolsas?
2. ¿Cuántos incrementos exige su procedimiento para un lote de este tamaño y esta matriz?
3. ¿Cómo reducen la compuesta: cuarteo manual o divisor? ¿Queda registrado?
4. ¿Cuánta masa mínima necesitan por ensayo, y cuánta guardan como retención?
5. ¿El muestreo está dentro de su alcance acreditado ISO 17025 o solo el ensayo? (Casi siempre solo el ensayo.)
6. ¿Puedo enviar duplicados ciegos del mismo lote para estimar el error total?

Ese último punto es la mejor herramienta de auditoría que tienes: manda dos frascos del mismo material con
identificadores distintos y compara. Si difieren mucho más que la precisión declarada del método, el problema
está en tu muestreo, en su submuestreo, o en su laboratorio, y ya sabes por dónde empezar (`77`, `78`).

## Errores comunes

- **Muestrear solo lo que se ve bien.** El operario evita la parte mohosa o el bulto sucio; el lote sale
  aprobado y el problema llega al cliente.
- **Un solo incremento por lote.** Es lo más común y lo más caro: convierte un resultado en una anécdota.
- **Muestrear el fondo del tambor de flor.** Concentra tricomas: infla la potencia y hace fracasar la
  reproducibilidad en el siguiente lote.
- **No sellar ni rotular en el momento.** Un frasco sin lote ni fecha es basura analítica, aunque el número
  sea correcto.
- **No guardar contramuestra.** Sin ella no hay cómo impugnar (`112`).
- **Muestrear después de mezclar "a ojo".** Mezclar mal segrega más de lo que homogeneiza; en polvos finos
  la agitación separa por tamaño.

## Conexión con otros módulos

→ `67-homogeneizacion-y-molienda-de-muestra.md` — qué se hace con la compuesta.
→ `78-estadistica-para-el-laboratorio.md` — cómo cuantificar el error de muestreo con duplicados.
→ `109-cadena-de-custodia-y-envio-de-muestras.md` — sellado, rótulo, transporte.
→ `112-como-impugnar-un-resultado.md` — para qué sirve la contramuestra.
→ `283-plan-de-control-de-calidad-por-lote.md` — dónde vive el plan de muestreo en tu sistema de calidad.
