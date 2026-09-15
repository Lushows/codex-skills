# 161 — Dosis y tamaño de porción (de la evidencia a los miligramos reales por cápsula)

Esta es la decisión que ordena todo el producto: cuántos miligramos del activo entrega una porción diaria. De
ahí salen el tamaño de cápsula, el precio, el costo por día y la posibilidad de sostener lo que dices. La
mayoría de las marcas la toman al revés: eligen "500 mg" porque suena bien, y luego inventan una justificación.
El camino correcto va de la evidencia al miligramo, pasando por una cuenta que hay que ejecutar en código y no
adivinar.

Términos: **porción / tamaño de porción (serving size)** = la cantidad que la etiqueta indica tomar por vez.
**Dosis diaria (daily dose)** = total en 24 h. **Dosis usada en estudios (studied dose)** = la que aparece en la
literatura, con su forma de material. **Margen de seguridad (safety margin)** = distancia entre tu dosis y el
NOAEL o el límite de exposición conocido (`135`). **Sobredosificación de formulación (overage)** = poner un poco
más para cubrir la pérdida durante la vida útil.

## Los seis pasos, en orden

```
1. ¿QUÉ ACTIVO?              El marcador que vas a declarar y medir (`152`).
2. ¿QUÉ DICE LA EVIDENCIA?   Dosis usada en estudios, con nivel de evidencia (`12`, `248`).
3. ¿SOBRE QUÉ MATERIAL?      ¿La dosis del estudio era de polvo entero, extracto o compuesto puro?
4. ¿MARGEN DE SEGURIDAD?     Toxicología y límites conocidos (`134`, `135`, `250`).
5. ¿CUÁNTOS mg POR UNIDAD?   Dosis diaria / número de unidades por día.
6. ¿CABE?                    Volumen de la cápsula vs densidad del polvo (`154`).
```

El paso 3 es donde se cae casi todo el mercado. Un estudio que usó "3 g/día de polvo de melena de león" **no**
respalda "1 g/día de extracto 10:1" ni al revés. Son materiales distintos con contenidos de activo distintos. Y
como el ratio no dice nada del activo (`151`), la única forma de traducir entre ellos es por el marcador medido.

## La traducción honesta entre materiales

```
REGLA DE ORO
  No traduzcas por ratio. Traduce por MILIGRAMOS DE MARCADOR.

  mg de marcador/día = masa de material (mg) × % de marcador / 100

Ejemplo (ILUSTRATIVO)
  Estudio: 3000 mg/día de polvo entero de cuerpo fructífero
           con β-glucano medido 22,0 % p/p b.s.
           → 660 mg de β-glucano/día

  Tu producto: extracto con β-glucano 32,0 % p/p b.s.
           masa necesaria = 660 / 0,320 = 2063 mg/día de extracto
           → NO son 300 mg, aunque el extracto sea "más concentrado"

  Si tu producto entrega 300 mg de extracto/día:
           300 × 0,320 = 96 mg de β-glucano/día
           = 14,5 % de la exposición del estudio.
```

Ese último renglón es la cuenta que ninguna marca publica y que cambia por completo la conversación. Ejecútala
en `lab-tools/betaglucano_dosis.py`, que hace exactamente esta conversión (COA → mg por cápsula → mg por porción
diaria), y verifica por segunda vía con `Matematicas_lushows`.

## Qué dosis usa la literatura (y cómo citarla sin mentir)

Los estudios clínicos de hongos funcionales usan rangos amplios, materiales heterogéneos y —crítico— **muchas
veces no reportan el contenido de β-glucano del material usado**. Eso no es un detalle: es la razón por la que
"la dosis clínica de reishi" no existe como número único.

| Qué se lee a menudo | Qué falta para poder usarlo |
|---|---|
| "1,5 g/día de extracto de reishi" | ¿Extracto acuoso, alcohólico o dual? ¿Qué % de β-glucano y de triterpenos? |
| "3 g/día de Hericium" | ¿Cuerpo fructífero o micelio? ¿Polvo entero o extracto? |
| "PSK 3 g/día" | Ese sí es un preparado definido; no se extrapola a "cola de pavo" genérica (`231`) |

Cómo se cita honestamente en un documento técnico:

> *"En estudios clínicos disponibles se han usado dosis del orden de X g/día de [material descrito como…]
> `[clínico, n pequeño]`. El contenido de β-glucano de ese material no siempre se reporta, por lo que la
> equivalencia con nuestro extracto se establece por miligramos de β-glucano medido, no por masa de material."*

Eso es defendible. "Nuestra dosis es la dosis clínica" no lo es.

## Cómo se define la porción en la práctica

```
DECISIÓN DE PORCIÓN — hoja de trabajo

  A. Objetivo de marcador por día:        ______ mg   ← de la evidencia y del posicionamiento
  B. Unidades por día (1, 2, 3):          ______      ← adherencia: 2 es el óptimo comercial habitual
  C. Marcador por unidad = A / B:         ______ mg
  D. % de marcador en el extracto:        ______ %    ← del COA, base seca
  E. Masa de extracto por unidad = C/D×100: ____ mg
  F. + excipientes (1–2 %):               ______ mg
  G. Volumen = F / densidad compactada:   ______ mL
  H. Tamaño de cápsula que lo aloja:      ______      ← tabla de `154`
  I. ¿Cabe? Si no: subir % del extracto, subir unidades/día o cambiar formato (`153`)
```

Sobre B: la adherencia baja rápido con más de 2 unidades al día. Un producto de 4 cápsulas diarias vende peor y
se toma peor. Eso es un dato de comportamiento, no de química, pero condiciona la química.

## El overage: cuánto de más se pone

Si el activo pierde potencia durante la vida útil, la etiqueta se incumple al final del período aunque estuviera
bien al inicio. Se compensa con overage:

```
overage (%) = pérdida esperada durante la vida útil, obtenida del estudio de estabilidad (`164`)

Ejemplo (ILUSTRATIVO): si a 24 meses el marcador cae 8 %,
  se formula a 150 mg / 0,92 = 163 mg por cápsula
  y la etiqueta declara 150 mg como MÍNIMO garantizado hasta el vencimiento.

Regla: el overage se justifica con DATOS de estabilidad, no "por si acaso".
Poner overage sin datos es sobredosificar a ciegas.
```

Para β-glucanos el overage suele ser pequeño (son polímeros estables). Para triterpenos, hericenonas o
cannabinoides, es más relevante (`204`, `255`).

## Cómo se comprueba la dosis en el producto real

| Ensayo | Cuándo | Criterio |
|---|---|---|
| Contenido de marcador por unidad | Cada lote, sobre muestra compuesta de 10–20 unidades | ≥ lo declarado |
| Uniformidad de contenido | Al validar y en activos de baja dosis | Según farmacopea (`280`) |
| Uniformidad de masa | En proceso, cada 15–30 min | ±7,5 % (`154`) |
| Contenido al final de la vida útil | Estudio de estabilidad | ≥ lo declarado (`164`) |

La etiqueta se cumple **al final de la vida útil**, no el día que se fabricó. Ese es el punto donde el overage
deja de ser una idea y se vuelve una obligación aritmética.

## Ejemplo aplicado — la porción de BIO-SETA, completa

```
A. Objetivo: 300 mg de β-glucano/día     ← elegido como objetivo comercial defendible,
                                            declarado como aporte, SIN claim de enfermedad (`267`)
B. Unidades/día: 2
C. Por cápsula: 150 mg de β-glucano
D. Extracto: 32,0 % p/p b.s. (Megazyme K-YBGL, `221`)
E. Extracto/cápsula: 150 / 0,320 = 469 mg
F. + 1 % excipientes = 474 mg
G. Volumen: 0,474 / 0,62 = 0,765 mL
H. Cápsula 00 (0,91 mL) ✔
I. Cabe con holgura.

Texto de etiqueta posible:
  "Porción: 2 cápsulas. Cada porción aporta 300 mg de β-glucano de Ganoderma lucidum
   (método enzimático Megazyme K-YBGL, sobre base seca)."

Texto imposible (claim de enfermedad):  cualquier mención a curar, prevenir o tratar (`268`).
```

Todas las cifras son **(ILUSTRATIVAS)**. Lo que no es ilustrativo es la secuencia: A→I, en ese orden, con la
cuenta ejecutada.

## Errores comunes

- Elegir "500 mg" primero y buscar la justificación después.
- Traducir dosis entre materiales usando el ratio en vez del marcador medido.
- Citar una dosis clínica sin decir sobre qué material se usó.
- Declarar el promedio de los lotes en vez del mínimo garantizado (`152`).
- Poner overage sin estudio de estabilidad que lo respalde, o no ponerlo cuando hacía falta.
- Diseñar una porción de 4–6 cápsulas al día: se cumple en el papel y no en la vida del cliente.
- Ignorar el límite superior: más no siempre es mejor, y hay que revisar tolerancia y seguridad (`250`, `135`).
- Hacer la cuenta de cabeza. Cada paso de este módulo es una multiplicación donde un error del 10 % es un
  producto incumplidor.

## Conexión con otros módulos

→ `152-estandarizacion-de-extractos.md` — de dónde sale el % de marcador.
→ `154-capsulas-y-encapsulado.md` — el paso "¿cabe?".
→ `249-dosificacion-de-hongos-funcionales.md` — qué dosis se han usado por especie.
→ `164-estabilidad-ich-q1-y-vida-util.md` — por qué la etiqueta se cumple al vencimiento.
→ `267-decreto-3249-y-que-puedo-decir.md` — cómo se redacta el aporte sin claim de enfermedad.
