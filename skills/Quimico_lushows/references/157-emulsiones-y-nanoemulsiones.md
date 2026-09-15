# 157 — Emulsiones y nanoemulsiones (meter aceite en agua, y cuándo el "nano" es real)

Una emulsión es aceite disperso en agua (o al revés) estabilizado por un tensioactivo. Es la única forma de
poner un activo lipofílico —cannabinoides, triterpenos, aceites— en una bebida, un jarabe o una crema. La
nanoemulsión lleva el tamaño de gota a escala submicrónica, y con eso mejora estabilidad óptica, dispersión y,
en el caso de cannabinoides, absorción. También es el término más abusado del mercado: cualquier líquido turbio
se vende como "nano". Este módulo te da el criterio para saber si lo que compras (o produces) es realmente una
nanoemulsión, y por qué **esto es maquila para una pyme**.

Términos: **emulsión (emulsion)** = dispersión de dos líquidos inmiscibles. **Nanoemulsión (nanoemulsion)** =
emulsión con gotas típicamente por debajo de ~200 nm; translúcida. **Tensioactivo (surfactant)** = molécula con
parte polar y parte apolar que estabiliza la interfase. **HLB (hydrophilic-lipophilic balance)** = escala que
indica si un tensioactivo sirve para O/W o W/O (`33`). **Maduración de Ostwald (Ostwald ripening)** = las gotas
grandes crecen a costa de las pequeñas; la muerte lenta de toda nanoemulsión. **DLS (dynamic light
scattering)** = técnica que mide tamaño de gota. **PDI (polydispersity index)** = qué tan uniforme es la
distribución. **SNEDDS (self-nanoemulsifying drug delivery system)** = concentrado que se nanoemulsiona solo al
contacto con agua o fluidos digestivos.

## Escala de tamaño: qué significa cada término

| Tipo | Tamaño de gota | Aspecto | Estabilidad | Cómo se hace |
|---|---|---|---|---|
| Macroemulsión | > 1 µm (1000 nm) | Blanca opaca | Crema/separa en días–meses | Agitación de alto cizallamiento |
| Emulsión fina | 200–1000 nm | Blanca | Meses | Homogeneizador |
| Nanoemulsión | ~20–200 nm | Translúcida a transparente | Meses–años, limitada por Ostwald | **Alta energía**: HPH, microfluidización, ultrasonido |
| Microemulsión | 5–50 nm | Transparente | Termodinámicamente estable | Baja energía, mucho tensioactivo |
| SNEDDS | Forma nano al diluirse | Concentrado oleoso | Muy estable como concentrado | Formulación, sin equipo de alta energía |

Ojo con la trampa lingüística: **"microemulsión" tiene gotas más pequeñas que "nanoemulsión"**. Los nombres son
históricos y contraintuitivos. La microemulsión es termodinámicamente estable (se forma sola); la nanoemulsión
es cinéticamente estable (se forma con energía y con el tiempo se degrada).

## Cómo se fabrica de verdad

```
MÉTODOS DE ALTA ENERGÍA (los que dan nanoemulsión real)

  Homogeneización a alta presión (HPH)
    - se bombea la premezcla a través de una válvula estrecha a alta presión
    - literatura reporta que tras UN paso ya hay una fracción submicrónica grande,
      y que a los CUATRO pasos la distribución se vuelve monomodal en torno a ~400 nm
      (depende fuertemente de formulación y equipo)

  Microfluidización
    - dos corrientes chocan en una cámara de interacción
    - se ha reportado que a mayor presión de proceso baja el tamaño y la dispersidad,
      con condiciones óptimas descritas entre ~11 000 y ~15 000 psi para CBD
    - es el método que da los tamaños más finos y reproducibles

  Ultrasonido de alta intensidad
    - viable a escala piloto; el escalado es el problema (`147`)

MÉTODOS DE BAJA ENERGÍA
  Inversión de fase (PIT/PIC) y SNEDDS: no requieren equipo de alta presión,
  pero exigen MUCHO más tensioactivo. Tamaños reportados muy pequeños:
  un SNEDDS de CBD describe gotas de ~39 ± 8 nm al dispersarse.
```

Veredicto para una pyme colombiana: HPH y microfluidización son **equipos de planta**. Un SNEDDS, en cambio,
se puede desarrollar sin equipo de alta presión — es un concentrado de aceite + tensioactivos + cosolvente que
se nanoemulsiona en el tracto digestivo. Es la ruta técnicamente más accesible, y su costo se va en
tensioactivo y en desarrollo, no en maquinaria.

## Biodisponibilidad: qué dice la evidencia

El argumento comercial de la nanoemulsión es la absorción. Hay soporte, y conviene citarlo con nivel de
evidencia y sin exagerar:

- Un estudio cruzado en humanos comparó un SNEDDS de CBD contra una formulación oleosa comercial y reportó
  aumentos importantes de exposición `[clínico, crossover]`. En otro trabajo, un CBD-SNEDDS mostró Cmax ~22
  veces mayor y AUC ~7 veces mayor frente a **CBD en polvo puro** `[preclínico/comparativo]`.
- Ese "22×" se compara contra polvo puro, que es el peor comparador posible. Frente a un aceite bien formulado,
  las diferencias son mucho menores. **El comparador es la mitad del titular.**
- Revisiones de 2025–2026 sobre estrategias para mejorar la biodisponibilidad del CBD describen las
  nanoemulsiones orales como menos difundidas de lo esperado por **inestabilidad física** (separación,
  crecimiento de gota, Ostwald), **manufactura compleja y costosa** (alta energía), **preocupaciones de
  seguridad por los tensioactivos** y **retos regulatorios de reproducibilidad y escalado**.

Traducción honesta para tu etiqueta: puedes decir que tu formulación está diseñada para mejorar la absorción
**si lo mediste**, y no puedes atribuirle efectos de salud (`267`, `268`). "Nano" no es un claim de eficacia.

## Cómo se comprueba que una nanoemulsión es una nanoemulsión

| Atributo | Método | Criterio orientativo |
|---|---|---|
| Tamaño de gota (Z-average) | DLS (dynamic light scattering) | < 200 nm para llamarla nano |
| PDI | DLS | ≤ 0,25 indica distribución estrecha |
| Potencial ζ | Movilidad electroforética | \|ζ\| ≥ ~30 mV se asocia a buena estabilidad electrostática |
| Estabilidad acelerada | Centrifugación, ciclos térmicos, 40 °C | Sin separación ni crecimiento de gota |
| Crecimiento por Ostwald | DLS a 0/1/3/6 meses | El tamaño no debe crecer sostenidamente |
| Contenido de activo | HPLC-DAD (`198`) | Lo declarado |
| Tensioactivo residual | Cuantificación específica | Seguridad y etiqueta |

Un valor de referencia útil de la literatura: nanoemulsiones optimizadas de CBD se han descrito con diámetro
medio de ~120 nm y potencial ζ de ~−30 mV. Es un orden de magnitud razonable para especificar, no una constante.

**El ensayo que decide una compra:** pídele al proveedor el **informe de DLS del lote**, no un folleto. Si no
tiene DLS, no puede afirmar que es nanoemulsión.

## Ejemplo aplicado — evaluar una oferta de "CBD nano soluble en agua"

```
Oferta: "Polvo de CBD nanoemulsionado, 20 % CBD, soluble en agua, 100× más biodisponible"

Preguntas (y qué revela cada una):
  1. ¿Tamaño de gota por DLS al reconstituir? ¿Z-average y PDI?   → si no lo tiene, no es nano
  2. ¿Qué tensioactivos y en qué %?                               → seguridad, sabor y etiqueta
  3. ¿Método: HPH, microfluidización o SNEDDS?                    → define reproducibilidad
  4. ¿"100× más" contra qué comparador?                           → casi siempre contra polvo puro
  5. ¿Estabilidad del tamaño a 3 y 6 meses?                       → Ostwald
  6. ¿COA de potencia por HPLC de laboratorio tercero?            → (`108`, `213`)
  7. ¿Qué pasa con el tamaño de gota a pH 3,5 y con azúcar?       → tu bebida no es agua pura

Bandera roja mayor: cualquier multiplicador de biodisponibilidad SIN el comparador declarado.
```

## Errores comunes

- Llamar "nanoemulsión" a una emulsión turbia sin haber medido nunca el tamaño de gota.
- Comparar biodisponibilidad contra el peor comparador posible para inflar el múltiplo.
- Formular la nanoemulsión en agua pura y meterla en una bebida ácida y azucarada sin reevaluar: el medio
  cambia la estabilidad de la gota.
- Ignorar el tensioactivo: es el ingrediente más cuestionado en seguridad y el que más sabor aporta.
- Prometer estabilidad de años sin datos: la maduración de Ostwald es lenta pero inevitable.
- Creer que "nano" habilita claims de salud. No habilita nada; los claims dependen de la evidencia y de la
  norma (`276`, `293`).
- Intentar producir nanoemulsión con licuadora industrial. Eso es una macroemulsión con buena intención.

## Conexión con otros módulos

→ `32-coloides-emulsiones-y-espumas.md` — la fisicoquímica de por qué una emulsión se rompe.
→ `33-tensioactivos-y-hlb.md` — cómo se elige el tensioactivo y se calcula el HLB requerido.
→ `159-potenciadores-de-biodisponibilidad.md` — las otras rutas para el mismo objetivo.
→ `158-liposomas-y-ciclodextrinas.md` — alternativas al problema de solubilizar lo lipofílico.
→ `195-formulacion-de-aceites-y-comestibles.md` — la vía simple y barata en cannabis.