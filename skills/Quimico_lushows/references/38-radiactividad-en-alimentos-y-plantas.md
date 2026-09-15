# 38 — Radiactividad en alimentos y plantas (el análisis que nadie pide hasta que un cliente europeo lo pide)

Este módulo existe por una razón muy concreta: los hongos silvestres son de los productos alimenticios que
más acumulan **cesio-137**, un radionúclido artificial que sigue presente en los suelos de buena parte del
hemisferio norte cuarenta años después de Chernóbil. Si compras chaga silvestre de Rusia, Ucrania,
Bielorrusia, Finlandia o los Bálticos —que es de donde viene la mayoría de la chaga del mercado— este es un
riesgo real, medible y con límites regulatorios en la Unión Europea. Es también el tipo de análisis que
diferencia a un proveedor serio de uno que solo tiene un COA bonito de β-glucanos.

Términos: **radionúclido (radionuclide)** = isótopo inestable que emite radiación al decaer. **actividad
(activity)** = número de desintegraciones por segundo, en becquerel (Bq); 1 Bq = 1 desintegración/s.
**actividad específica (specific activity)** = Bq por kilogramo (Bq/kg), la unidad que verás en un COA.
**dosis efectiva (effective dose)** = energía absorbida ponderada por tipo de radiación y tejido, en
sievert (Sv) o milisievert (mSv). **vida media (half-life)** = tiempo en que decae la mitad. **radiación de
fondo (background radiation)** = la que existe naturalmente en todas partes.

## Los radionúclidos que importan en alimentos

| Radionúclido | Origen | Vida media | Comportamiento |
|---|---|---|---|
| Cesio-137 (¹³⁷Cs) | Artificial: ensayos nucleares, Chernóbil (1986), Fukushima (2011) | 30,2 años | Se comporta como el potasio: entra en la célula y se distribuye en tejido blando |
| Cesio-134 (¹³⁴Cs) | Artificial, contaminación reciente | 2,06 años | Su presencia indica contaminación reciente, no de 1986 |
| Estroncio-90 (⁹⁰Sr) | Artificial | 28,8 años | Se comporta como el calcio: va al hueso. Difícil de medir (emisor beta puro) |
| Potasio-40 (⁴⁰K) | **Natural**, en todo lo vivo | 1,25 × 10⁹ años | Está en tu cuerpo y en todos los alimentos. No es contaminación |
| Radio-226, Plomo-210, Polonio-210 | Naturales, serie del uranio | Variadas | Relevantes en algunos minerales y fertilizantes |

Punto de honestidad que hay que decir siempre: **todo alimento es radiactivo**. Un plátano tiene del orden
de 100–130 Bq/kg de ⁴⁰K natural; un cuerpo humano adulto contiene unos 4 000–5 000 Bq de ⁴⁰K. Cuando un
informe reporta actividad total sin separar isótopos, está mezclando lo natural con lo artificial y no
sirve para decidir nada. El análisis útil **identifica el isótopo**.

## Por qué los hongos concentran cesio

El ¹³⁷Cs es químicamente parecido al potasio (mismo grupo de la tabla periódica, mismo tamaño iónico
aproximado). El micelio de un hongo es una red que explora un volumen enorme de suelo buscando nutrientes,
y sus transportadores de potasio no distinguen entre K⁺ y Cs⁺: lo meten igual. Como además el micelio vive
en la capa orgánica superficial del suelo —justo donde quedó depositado el cesio— la exposición es máxima.

```
Consecuencias documentadas:

- Los hongos silvestres están entre los alimentos con mayor factor de transferencia de 137Cs desde el
  suelo, muy por encima de plantas cultivadas.
- Las especies MICORRÍCICAS (que viven asociadas a raíces de árboles) concentran más que las
  saprófitas de sustrato controlado.
- La CHAGA (Inonotus obliquus) crece sobre abedules vivos en bosques boreales del hemisferio norte,
  durante años o décadas. Es material silvestre, de larga vida, en la región más afectada. Es
  exactamente el peor caso posible (`229`, `230`).
- Un hongo CULTIVADO sobre sustrato controlado (aserrín y salvado de origen conocido) no tiene
  esta exposición. Esa es una ventaja competitiva real y verificable de la producción cultivada.
```

En la Unión Europea existen niveles máximos armonizados para ¹³⁴Cs + ¹³⁷Cs en alimentos, y desde el
accidente de Chernóbil ha habido controles específicos sobre hongos silvestres importados de terceros
países. **A agosto de 2026** los valores y el alcance vigentes deben verificarse en la legislación europea
actual antes de exportar o importar, porque el marco se ha ido consolidando y reformando; no se citan de
memoria (`277`, `278`, `285`).

## Cómo se mide

| Pregunta | Método | Unidad / detalle |
|---|---|---|
| ¿Cuánto ¹³⁷Cs y ¹³⁴Cs tiene? | **Espectrometría gamma** con detector de germanio hiperpuro (HPGe) | Bq/kg de peso seco o fresco — **hay que declarar cuál** |
| ¿Cuánto tarda? | Conteo de 1 a 24 h según el LOD requerido | Más tiempo = menor LOD |
| ¿Cuánta muestra hace falta? | Geometría Marinelli de 0,5–1 L; típicamente 100–500 g | La geometría debe ser la calibrada |
| ¿Cuál es el LOD? | Se reporta como actividad mínima detectable (MDA) | Bq/kg; sin MDA, un "no detectado" no significa nada (`73`) |
| ¿Y el ⁹⁰Sr? | Separación radioquímica + conteo beta; caro y lento | Bq/kg; solo si el mercado lo exige |
| ¿Está el ⁴⁰K separado? | La espectrometría gamma lo identifica por su pico de 1 460 keV | Bq/kg; se reporta aparte, es natural |
| ¿El laboratorio está acreditado? | ISO 17025 con el alcance específico de espectrometría gamma | Verificar el alcance, no solo el sello (`107`) |

Regla dura: en radiactividad, la **base** importa tanto como en potencia. Un resultado en Bq/kg de peso
seco es mucho mayor que el mismo material en peso fresco (un hongo fresco es ~90 % agua). Comparar un
resultado en seco contra un límite expresado en producto listo para consumo, sin convertir, produce
rechazos falsos y aprobaciones falsas por igual (`07`).

## Ejemplo aplicado — calificar tres proveedores de chaga

Tres orígenes, misma especificación de β-glucano, espectrometría gamma HPGe, 12 h de conteo
**(ILUSTRATIVO)**:

```
Proveedor          Origen                    ¹³⁷Cs (Bq/kg b.s.)   ¹³⁴Cs   ⁴⁰K (Bq/kg b.s.)   MDA ¹³⁷Cs
A — silvestre      Bosque boreal, Europa E.        920            < MDA        1 150            4 Bq/kg
B — silvestre      Norteamérica (Canadá)            18            < MDA        1 080            4 Bq/kg
C — cultivado      Sustrato controlado, Asia       < 4            < MDA          890            4 Bq/kg

Dosis estimada del proveedor A a 3 g/día de chaga seca durante un año:
  920 Bq/kg × 0,003 kg/día × 365 días = 1 007 Bq ingeridos/año
  × coeficiente de dosis por ingestión de ¹³⁷Cs en adultos (1,3 × 10⁻⁸ Sv/Bq, ICRP)
  ≈ 1,3 × 10⁻⁵ Sv/año = 0,013 mSv/año
  Referencia de contexto: la dosis natural de fondo promedio ronda 2–3 mSv/año.
```

Cómo se lee esto con honestidad, sin alarmismo y sin negligencia: la dosis calculada para el proveedor A a
esa ingesta es **pequeña frente al fondo natural**, pero (1) el ¹³⁴Cs ausente confirma que es contaminación
antigua, no reciente; (2) el valor de 920 Bq/kg puede superar el límite de comercialización aplicable en
la UE y bloquear la importación, que es un problema comercial inmediato; (3) el consumidor no evalúa
dosis, evalúa titulares. La decisión práctica: proveedor B o C, y el análisis gamma entra a la
especificación de materia prima de chaga silvestre como parámetro obligatorio por lote (`141`, `284`).

El cálculo de dosis se ejecuta en código con los coeficientes vigentes de la ICRP, no de memoria
(`Matematicas_lushows`), y cualquier comunicación al consumidor sobre esto se hace sin claims de salud ni
de enfermedad, describiendo el control, no el efecto (`293`).

## Errores comunes

- No pedir espectrometría gamma para chaga u hongos silvestres del hemisferio norte. Es el análisis
  específico de este material.
- Aceptar "no detectado" sin la MDA. Con una MDA de 100 Bq/kg, un "no detectado" es inútil.
- Reportar actividad total sin identificar isótopos, mezclando el ⁴⁰K natural con el ¹³⁷Cs artificial.
- No declarar si el resultado es en base seca o fresca. Cambia el número por un factor de ~10.
- Suponer que "silvestre" es sinónimo de mejor. Para este parámetro, cultivado sobre sustrato controlado
  es objetivamente más seguro y más verificable (`239`).
- Alarmar al consumidor con becquereles sin contexto de dosis, o —al revés— esconder un resultado que
  bloquea una exportación.
- Confundir irradiación de alimentos (un tratamiento que no deja radiactividad residual) con
  contaminación radiactiva. Son cosas distintas y hay que saber explicarlo.

## Conexión con otros módulos

→ `230-chaga-riesgos-oxalato-y-radiocesio.md` — el módulo dueño del caso chaga, completo.
→ `229-chaga-inonotus-quimica.md` — qué es la chaga y qué contiene.
→ `36-quimica-inorganica-y-metales-relevantes.md` — el otro riesgo de acumulación.
→ `141-especificacion-de-materia-prima.md` — cómo entra este parámetro a la especificación.
→ `284-auditoria-de-proveedor.md` — qué se le exige al proveedor y cómo se verifica.
→ `285-importacion-y-documentos-tecnicos.md` — el papeleo de importación y exportación.
→ `107-iso-17025-y-acreditacion.md` — cómo verificar el alcance del laboratorio.
→ `135-noael-ida-y-limites-de-exposicion.md` — la lógica de exposición vs concentración.
