# 147 — Ultrasonido, microondas y enzimas (las asistencias que sí valen la pena)

Después de agua y etanol vienen las "asistencias": técnicas que no reemplazan el solvente sino que aceleran o
mejoran su trabajo. Ultrasonido (UAE), microondas (MAE) y enzimas (EAE) son las tres que una pyme puede
evaluar sin arruinarse. Cada una tiene un caso donde brilla y varios donde es puro gasto. El error caro que
evita este módulo: comprar un baño ultrasónico de 6 L creyendo que es un salto de producción, cuando lo que
resuelve es escala de laboratorio.

Términos: **UAE (ultrasound-assisted extraction)** = extracción asistida por ultrasonido; el mecanismo es la
**cavitación**: burbujas que colapsan y rompen paredes celulares. **MAE (microwave-assisted extraction)** =
calentamiento dieléctrico del solvente polar desde adentro. **EAE (enzyme-assisted extraction)** = usar enzimas
para digerir la pared celular y liberar el contenido. **Quitina (chitin)** = polímero estructural de la pared
fúngica, duro de romper (`216`).

## Las tres, comparadas

| Criterio | Ultrasonido (UAE) | Microondas (MAE) | Enzimas (EAE) |
|---|---|---|---|
| Mecanismo | Cavitación, ruptura mecánica | Calentamiento interno rápido | Hidrólisis específica de la pared |
| Reduce tiempo | Sí, típicamente de horas a 20–60 min | Sí, a minutos | No; suele tardar 1–4 h |
| Reduce solvente | Moderado | Sí | No |
| Riesgo al activo | Radicales por cavitación; calor local | Sobrecalentamiento, puntos calientes | Bajo, si controlas pH y T |
| Selectividad | Baja | Baja | **Alta** (eliges la enzima) |
| Costo de entrada pyme | Bajo (baño) a medio (sonda) | Medio | Bajo–medio (enzima por kg) |
| Escalable | Difícil (la energía no escala lineal) | Difícil fuera de equipo dedicado | **Sí, escala como cualquier reacción** |
| Veredicto para pyme | Útil en laboratorio y piloto | Casi siempre maquila o I+D | **La más práctica en producción** |

## Ultrasonido: qué hace y qué no

El ultrasonido genera burbujas que implosionan y rompen paredes celulares. En hongos esto importa porque la
pared de quitina y β-glucano es dura: si no la rompes, buena parte del glucano nunca llega al solvente.

```
Parámetros que se controlan (rangos típicos de trabajo, verificar con tu equipo):
  Frecuencia        20–40 kHz  (sonda de 20 kHz es más agresiva que baño de 40 kHz)
  Potencia          expresada como densidad, W/L o W/g de material
  Tiempo            10–60 min; pulsado (ej. 5 s ON / 5 s OFF) para controlar T
  Temperatura       el ultrasonido CALIENTA; sin camisa de enfriamiento sube 20–30 °C
  Relación S/L      1:10 a 1:30 p/v
```

Advertencia honesta: la cavitación genera radicales hidroxilo que **pueden degradar** el activo y despolimerizar
los β-glucanos. Un β-glucano despolimerizado sigue midiéndose como β-glucano en el ensayo enzimático, pero su
peso molecular cambió — y en la literatura de inmunomodulación el peso molecular y la ramificación importan
`[in vitro]` (`130`). Si vas a usar UAE, mide también algo de tamaño molecular (GPC/SEC) o al menos declara la
condición y mantenla fija.

Escala real: baños de 3–10 L sirven para desarrollo. Para producción se necesitan reactores sonoquímicos de
flujo, que ya son inversión de planta.

## Microondas: potente y traicionero

El microondas calienta el agua (y otros solventes polares) desde el interior de la matriz, generando presión
que revienta las células. Es rapidísimo — extracciones de 5–20 min — pero:

- El etanol de alto grado calienta mal por microondas; el agua y las mezclas hidroalcohólicas bajas, muy bien.
- Los **puntos calientes** (hot spots) queman zonas del material sin que el termómetro global lo note.
- Con solvente inflamable en cavidad de microondas hay riesgo real de ignición. **No improvises con un
  microondas doméstico.** Los equipos de MAE son cerrados, con control de presión y temperatura.

Veredicto para pyme colombiana: **MAE es I+D o maquila.** No es un camino de producción barato.

## Enzimas: la asistencia más práctica

Aquí sí hay una vía realista. Las enzimas digieren componentes específicos de la pared y liberan el activo, a
temperatura suave y sin solventes agresivos.

| Enzima | Sustrato que ataca | Para qué se usa en hongos/plantas |
|---|---|---|
| Celulasa | Celulosa | Material vegetal, residuo de sustrato |
| Quitinasa | Quitina | Pared fúngica — la clave en hongos (`216`) |
| β-glucanasa | β-glucano | **Cuidado: te destruye el activo.** Solo para análisis controlado |
| Proteasa | Proteínas | Libera proteoglicanos, reduce viscosidad |
| Pectinasa | Pectina | Material vegetal blando |
| α-amilasa / amiloglucosidasa | Almidón | Remover α-glucano del micelio en grano (`220`) |

Uso interesante y poco explotado: **usar amilasas para bajar el α-glucano** de un material con sustrato
residual, subiendo el % relativo de β-glucano. Es legítimo si lo declaras como parte del proceso. Lo que no es
legítimo es usarlo para disfrazar micelio en grano como cuerpo fructífero (`218`).

```
Condiciones típicas de trabajo enzimático (siempre confirmar con la ficha del proveedor):
  Temperatura   45–60 °C (óptimo de la enzima; sobre 70 °C se desnaturaliza)
  pH            4,5–6,5 según enzima → requiere buffer y pH-metro (`23`)
  Dosis         0,1–2,0 % p/p sobre materia prima seca
  Tiempo        1–4 h con agitación suave
  Inactivación  subir a 85–90 °C por 10 min al terminar  ← paso OBLIGATORIO
```

El paso de inactivación no es opcional: una enzima activa que sigue en el licor te sigue digiriendo el producto
en el tanque y en el frasco.

## Cómo se comprueba si la asistencia sirvió

Nunca se decide "porque salió más oscuro". Se decide con un diseño comparativo:

```
DISEÑO MÍNIMO (un factor a la vez, mismo lote, n = 3)

  Control     : agua 90 °C, 2 h, 1:15
  Brazo UAE   : agua 90 °C, 30 min, 1:15, sonda 20 kHz, 200 W/L, pulsado
  Brazo EAE   : quitinasa 0,5 % p/p, pH 5,5, 50 °C, 3 h → inactivar → decocción 1 h

Se mide en los tres:
  - rendimiento de sólidos (% p/p b.s.)
  - β-glucano en el extracto (% p/p b.s.)  → Megazyme (`221`)
  - RECUPERACIÓN de β-glucano (%)          ← la que decide
  - β-glucano remanente en bagazo
  - costo por gramo de β-glucano recuperado ← rutea a `economist_lushows`

Criterio: gana la condición con mejor costo por gramo de activo, no la de mayor rendimiento bruto.
```

## Ejemplo aplicado — ¿vale la pena el ultrasonido?

Cifras **(ILUSTRATIVAS)** para un piloto de 5 kg de cola de pavo:

```
Condición   Tiempo   Recuperación β-glucano   Energía   Costo relativo del lote
Control      2,0 h          31,9 %             baja            1,00
UAE          0,5 h          40,4 %             alta            1,35
EAE          4,0 h          46,1 %             baja            1,18  (+ costo enzima)

Lectura: UAE sube 8,5 puntos y cuesta 35 % más → el gramo de activo sale más caro
         que con EAE, que sube 14 puntos por 18 % más de costo.
Decisión ILUSTRATIVA: probar EAE a escala piloto; UAE queda para laboratorio.
```

Ese cuadro se llena con **tus** números, no con estos. El punto es la forma de decidir: costo por gramo de
activo recuperado, no titular de rendimiento.

## Errores comunes

- Comprar un baño ultrasónico esperando resolver producción. Resuelve laboratorio.
- Meter etanol en un microondas doméstico. Es un riesgo de incendio, no un experimento.
- Usar enzima sin controlar pH: fuera de su ventana la enzima simplemente no trabaja y pagaste igual.
- Olvidar inactivar la enzima y encontrarse el producto degradado semanas después.
- Usar β-glucanasa "para liberar β-glucanos": la destruye. El nombre engaña a mucha gente.
- Comparar condiciones midiendo solo rendimiento de sólidos: más sólidos puede ser más almidón y más sales.
- No documentar los parámetros exactos. Sin registro, ninguna mejora es reproducible ni transferible al
  maquilador (`166`, `168`).

## Conexión con otros módulos

→ `144-extraccion-acuosa-y-decoccion.md` — el proceso base al que estas técnicas asisten.
→ `27-catalisis-y-enzimas.md` — cómo funciona una enzima y por qué el pH manda.
→ `287-diseno-de-experimentos-doe.md` — cómo comparar varias variables sin gastar 30 lotes.
→ `216-biologia-fungica-y-ciclo-de-vida.md` — por qué la pared de quitina es el obstáculo.
→ `220-alfa-glucanos-y-almidon-el-confusor.md` — el uso legítimo (y el ilegítimo) de las amilasas.
