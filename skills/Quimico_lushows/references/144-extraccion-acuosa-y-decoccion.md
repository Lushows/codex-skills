# 144 — Extracción acuosa y decocción (agua caliente: la mitad que saca los β-glucanos)

La extracción con agua caliente es el proceso más antiguo, más barato y —para hongos— el que saca la fracción
que sostiene casi toda la evidencia inmunomoduladora: los β-glucanos. También es el único paso de todo este
bloque que una pyme colombiana puede montar bien con equipo de cocina industrial. Entender por qué el agua
saca unas cosas y no otras evita el error caro de vender un "extracto de reishi" hidroalcohólico que casi no
tiene β-glucano, o un "extracto acuoso" al que le prometiste triterpenos que el agua nunca iba a sacar.

Términos: **decocción (decoction)** = hervir el material en agua un tiempo prolongado. **Infusión (infusion)**
= verter agua caliente y dejar reposar, sin hervir. **Relación sólido:líquido (solid-to-liquid ratio, S/L)** =
gramos de material por mL de agua, ej. 1:15 p/v. **Licor de extracción (extract liquor)** = el líquido cargado.
**Bagazo (marc)** = el sólido agotado. **Contracorriente (countercurrent)** = extraer en etapas donde el
solvente más limpio toca el sólido más agotado.

## Qué saca el agua caliente y qué no

| Fracción | ¿Sale en agua caliente? | Por qué |
|---|---|---|
| β-glucanos solubles | Sí, es su solvente | Polímero muy hidroxilado, forma puentes de hidrógeno (`219`) |
| β-glucanos insolubles de pared | Parcialmente | Requiere T alta, tiempo, a veces álcali (industrial) |
| Proteínas y proteoglicanos (PSK/PSP) | Sí | Solubles en agua (`231`) |
| Ergotioneína | Sí, muy soluble | Aminoácido modificado, polar (`235`) |
| Nucleósidos (adenosina, cordicepina) | Sí | Polares (`237`) |
| Triterpenos ganodéricos | **Muy poco** | Apolares, logP alto (`224`, `55`) |
| Esteroles (ergosterol) | **No** | Prácticamente insolubles en agua (`238`) |
| Hericenonas | **Poco** | Lipofílicas (`226`) |
| Cannabinoides | **No** | logP ~6–7; el agua no los toca (`176`) |
| Almidón / α-glucano | Sí, y gelatiniza | Por eso el micelio en grano da "polisacáridos" altos (`220`) |

Esa tabla es, en una página, la razón de existir de la **extracción dual** (`146`): con agua sola te quedas sin
la mitad lipofílica de la química del hongo.

## Las cinco variables que controlas

```
1. TEMPERATURA        80–100 °C típico. Más T = más rápido, más riesgo de degradar y de extraer
                      material indeseado. A presión (autoclave) se llega a 110–121 °C.
2. TIEMPO             1–4 h por etapa es el rango de trabajo habitual.
3. RELACIÓN S/L       1:10 a 1:20 p/v. Más líquido = más extracción, más evaporación después.
4. AGITACIÓN          sin agitación la difusión manda; con agitación el tiempo cae mucho.
5. NÚMERO DE ETAPAS   2–3 extracciones sucesivas del mismo bagazo sacan mucho más que una larga.
```

**El truco que más rendimiento da por peso barato: extraer tres veces cortito en vez de una vez larguísimo.**
Cada etapa arranca con un gradiente de concentración nuevo.

```
Ilustración del efecto de etapas (ILUSTRATIVO), rendimiento acumulado de sólidos:
  1 etapa de 4 h, 1:15      →  7,8 % p/p b.s.
  2 etapas de 2 h, 1:10 c/u →  9,9 % p/p b.s.
  3 etapas de 1,5 h, 1:8    → 11,3 % p/p b.s.   (y menos agua total que evaporar)
```

## Qué puede montar una pyme y qué exige maquila

| Elemento | Versión pyme | Versión industrial |
|---|---|---|
| Recipiente | Marmita de acero 316 con camisa de vapor o resistencia, 20–100 L | Reactor encamisado 500–5000 L |
| Agitación | Agitador de aspas con variador | Turbina + deflectores |
| Control de T | Termómetro con sonda + controlador PID | Automatización con registro |
| Presión | Olla a presión / autoclave de laboratorio | Extractor presurizado |
| Filtración | Filtro prensa pequeño, bolsa de nylon 25–50 µm, centrífuga de cesta | Filtro prensa, centrífuga decantadora |
| Concentración | Rotavapor 5–20 L (`149`) | Evaporador de película descendente |
| Secado del extracto | **No** — aquí se acaba lo casero | Spray dryer / liofilizador (`150`) |

Punto honesto: el cuello de botella de la pyme no es extraer, es **secar el líquido**. Muchos proyectos
colombianos extraen en casa y mandan a maquilar solo el secado por aspersión; es una arquitectura sensata
siempre que la planta que seca tenga BPM (`167`).

## Cómo se comprueba que la extracción funcionó

Tres números, siempre en base seca:

```
1) RENDIMIENTO DE SÓLIDOS
   masa de extracto seco (g) / masa de materia prima seca (g) × 100  = % p/p b.s.

2) POTENCIA DEL EXTRACTO
   β-glucano en el extracto, % p/p b.s.  → Megazyme K-YBGL (`221`)

3) RECUPERACIÓN DE ACTIVO  ← el que decide si el negocio sirve
   (masa extracto × %activo extracto) / (masa MP × %activo MP) × 100

Ejemplo (ILUSTRATIVO):
   MP: 10,00 kg b.s. con β-glucano 22,0 % p/p  → 2 200 g de β-glucano entraron
   Extracto: 1,15 kg b.s. con β-glucano 61,0 % → 701,5 g salieron
   Rendimiento de sólidos = 11,5 %
   Recuperación de β-glucano = 31,9 %
   Ratio nominal planta:extracto = 8,7 : 1   (ver por qué esto no es una promesa, `151`)
```

Y un cuarto control que casi nadie hace: **analizar el bagazo**. Si el bagazo todavía tiene 15 % de β-glucano,
tu proceso está botando dinero y lo puedes cuantificar exactamente.

## Ejemplo aplicado — protocolo base para reishi en marmita de 50 L

```
Material: 3,0 kg de cuerpo fructífero seco, malla 40 (`143`), humedad 7,5 %
Etapa 1: 30 L de agua potable filtrada, 95 °C, 2 h, agitación 60 rpm
Etapa 2: filtrar en caliente (bolsa 50 µm); al bagazo, 24 L de agua, 95 °C, 1,5 h
Etapa 3: repetir con 18 L, 1 h
Combinar licores (~65 L) → filtrar a 5 µm → concentrar a ~6 L (`149`)
→ enviar a secado por aspersión con maltodextrina si aplica (`150`)

Controles del lote:
  - registro de T cada 15 min
  - sólidos solubles del licor por refractómetro (°Bx) al final de cada etapa
  - muestra de licor combinado y de bagazo, congeladas, para β-glucano
  - agua: potable, con análisis vigente (`106`)
```

Nota de honestidad: la fracción β-glucano que sale depende de la especie, del lote y de si la pared celular
está o no rota por la molienda previa. **No hay una constante universal.** Mide tu lote.

## Errores comunes

- Vender "extracto acuoso de reishi" prometiendo triterpenos. El agua no los saca (`146`).
- Hervir destapado 6 horas: pierdes volumen, subes la concentración de sales y no ganas activo proporcional.
- Usar una sola etapa larga en vez de varias cortas y quedarte con 30 % menos de rendimiento.
- Filtrar en frío después de haber gelatinizado almidón: se vuelve una gelatina imposible de filtrar.
- No medir el bagazo. Es el único dato que te dice cuánto estás botando.
- Agua no controlada: dureza, cloro y metales del agua entran a tu producto y aparecen en el análisis (`106`).
- Dejar el licor caliente sin refrigerar toda la noche: es un caldo de cultivo perfecto (`100`).

## Conexión con otros módulos

→ `146-extraccion-dual-y-por-que-importa.md` — por qué esto es solo la mitad del producto.
→ `145-extraccion-hidroalcoholica-y-tinturas.md` — la otra mitad, la lipofílica.
→ `149-concentracion-y-evaporacion.md` — qué hacer con 65 L de licor.
→ `219-beta-glucanos-quimica-y-estructura.md` — qué es exactamente lo que estás sacando.
→ `241-extraccion-de-hongos-agua-vs-alcohol.md` — la comparación específica por especie.