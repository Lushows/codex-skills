# 140 — De la materia prima al producto (el mapa completo, sin saltarse pasos)

Este es el módulo-mapa del bloque de tecnología farmacéutica. Antes de comprar una marmita, antes de pedir
una cotización a un maquilador y antes de diseñar la etiqueta, necesitas ver el proceso completo: qué entra,
qué le pasa en cada paso, cuánta masa se pierde y en qué punto se decide el número que vas a declarar. El
error caro que evita es el más común de todos: montar el proceso al revés — primero el frasco bonito, después
preguntarse cuántos miligramos de activo hay adentro. En este oficio el número va primero y el frasco después.

Términos: **galénica (galenics / pharmaceutical technology)** = la ciencia de convertir un principio activo en
una forma que se pueda dosificar, conservar y consumir. **Materia prima (raw material)** = lo que entra:
biomasa, extracto comprado, excipientes. **Producto terminado (finished product)** = lo que sale envasado y
etiquetado. **Rendimiento (yield)** = masa que sale / masa que entra, en %. **Maquila (contract manufacturing,
CMO)** = fabricar en planta de un tercero bajo tu especificación.

## El mapa: nueve estaciones

```
[1] MATERIA PRIMA        biomasa fúngica o vegetal, o extracto comprado
        ↓                 especificación de entrada + COA         → 141
[2] ACONDICIONAMIENTO    secado, estabilización, almacenamiento    → 142
        ↓                 % humedad objetivo, actividad de agua
[3] REDUCCIÓN DE TAMAÑO  molienda, tamizado                        → 143
        ↓                 granulometría (malla / µm)
[4] EXTRACCIÓN           agua, hidroalcohólica, dual, CO2, asistida → 144–148
        ↓                 licor de extracción (extract liquor)
[5] SEPARACIÓN/CONCENT.  filtración, evaporación al vacío           → 149
        ↓                 concentrado (°Bx o % sólidos)
[6] SECADO               aspersión (spray dry) o liofilización      → 150
        ↓                 POLVO DE EXTRACTO ← aquí nace el "ratio"  → 151
[7] ESTANDARIZACIÓN      ajuste a % de activo medido                → 152
        ↓                 ESPECIFICACIÓN DEL EXTRACTO
[8] FORMULACIÓN          cápsula, tableta, gotero, emulsión         → 153–162
        ↓                 dosis por unidad                          → 161
[9] ENVASE + ESTABILIDAD envase primario, estudio ICH               → 163–165
        ↓
    LOTE LIBERADO        documentación, trazabilidad                → 167–169
```

Cada flecha pierde masa y puede perder activo. El activo no se conserva por buena voluntad: se conserva porque
elegiste temperatura, tiempo y solvente correctos, y porque lo mediste antes y después.

## Dónde se pierde la masa (balance típico)

Cifras **(ILUSTRATIVO)** para 100 kg de cuerpo fructífero (fruiting body) fresco de reishi:

```
Fresco                          100,0 kg   (humedad ~ 85–90 % p/p reportada en literatura)
→ Secado a 12 % humedad          ~ 12,0 kg   pérdida = agua, no activo (si la T es correcta) → 142
→ Molienda malla 40 (~420 µm)     ~ 11,8 kg   pérdida = polvo fino, limpieza de equipo      → 143
→ Extracción dual + filtrado      licor       el bagazo (marc) se descarta con activo residual
→ Concentrado + secado            ~ 1,2 kg   POLVO DE EXTRACTO
Rendimiento de extracción = 1,2 / 11,8 = 10,2 % p/p base seca  →  "ratio 10:1" nominal
```

Ese "10:1" es **aritmética de masa**, no una medida de potencia. Es exactamente el punto donde la industria
empieza a mentir. Ver `151` y `152`.

## Qué puedes hacer con equipo modesto y qué exige maquila

| Estación | Pyme colombiana con presupuesto | Necesita maquila / tercero |
|---|---|---|
| Secado (2) | Deshidratador de bandejas con control de T, horno de convección | Secado industrial de túnel |
| Molienda (3) | Molino de martillos/cuchillas de laboratorio + juego de tamices | Molienda criogénica |
| Extracción acuosa (4) | Marmita con agitación y control de T, olla a presión | Reactor encamisado, extractor a contracorriente |
| Hidroalcohólica (4) | Maceración en tanque cerrado, percolador de acero | Solventes clase 2, área clasificada |
| CO2 supercrítico (4) | **No** | Sí, siempre (`148`) |
| Concentración (5) | Rotavapor de 5–20 L | Evaporador de película descendente |
| Secado del extracto (6) | Nada barato funciona bien | Spray dryer o liofilizador (`150`) |
| Encapsulado (8) | Encapsuladora manual 100–400 huecos | Encapsuladora automática con BPM |
| Nanoemulsión (8) | **No** (requiere alta presión) | Microfluidizador / HPH (`157`) |
| Estudio de estabilidad (9) | Puedes diseñarlo tú | Cámara climática certificada + laboratorio |

Regla honesta: en Colombia, para vender legalmente un suplemento dietario necesitas que la planta esté
certificada en BPM, sea tuya o del maquilador (`167`). Casi siempre el camino de la pyme es: **yo controlo la
materia prima y la especificación, el maquilador controla la planta**.

## Cómo se comprueba que el proceso funcionó

No se comprueba "mirando el polvo". Se comprueba midiendo el mismo analito en tres puntos:

| Punto de muestreo | Qué se mide | Método | Para qué sirve |
|---|---|---|---|
| Materia prima seca | β-glucano, humedad, metales | Megazyme K-YBGL (`221`), Karl Fischer (`98`), ICP-MS (`88`) | ¿Vale la pena extraerla? |
| Polvo de extracto | mismo analito, % p/p base seca | mismo método | rendimiento real de activo |
| Producto terminado | mg por unidad | mismo método sobre cápsula | lo que dice la etiqueta |

**Balance de activo** (no de masa) — la cuenta que casi nadie hace:

```
Activo que entró (mg)  = masa MP (g) × % activo MP × 10
Activo que salió (mg)  = masa extracto (g) × % activo extracto × 10
Recuperación de activo = salió / entró × 100

Ejemplo (ILUSTRATIVO):
  11 800 g MP × 12,0 % β-glucano  = 1 416 000 mg entraron
   1 200 g extracto × 42,0 %      =   504 000 mg salieron
  Recuperación = 35,6 %   →  el 64 % del β-glucano se quedó en el bagazo o se degradó
```

Ese número (35,6 %) es el que decide si el proceso es negocio o no. Ejecuta la cuenta con
`lab-tools/rendimiento_extraccion.py`, nunca de memoria; si la decisión es grande, rutea a
`Matematicas_lushows`.

## Ejemplo aplicado — el orden correcto para BIO-SETA

1. Decidir el claim medible: "aporta X mg de β-glucano por porción diaria" (no un claim de enfermedad).
2. Fijar X con la evidencia disponible y el tamaño de porción realista (`161`, `249`).
3. Trabajar hacia atrás: mg por cápsula → % de β-glucano requerido en el extracto → tipo de extracción.
4. Recién ahí elegir proceso, equipo y proveedor.
5. Escribir la especificación del extracto **antes** de comprar (`152`, `247`).
6. Envase y estabilidad antes de imprimir vida útil en la etiqueta (`163`, `164`).

Hacerlo al revés cuesta un lote completo y, si ya imprimiste etiqueta, también cuesta la etiqueta.

## Errores comunes

- Comprar equipo antes de definir el analito y su método de medición. El equipo no negocia con la química.
- Confundir rendimiento de masa con recuperación de activo. Son dos números distintos y solo el segundo paga.
- Secar la biomasa a temperatura alta "para ir rápido" y perder termolábiles antes de extraer (`142`, `240`).
- Encargar la maquila sin especificación escrita: el maquilador cumple lo que está en el papel, no lo que
  imaginaste.
- Declarar en la etiqueta el número del proveedor sin verificarlo en tu producto terminado (`110`, `111`).
- Diseñar el envase al final, cuando ya no puedes cambiar la barrera a oxígeno y humedad que el producto pedía.

## Conexión con otros módulos

→ `141-especificacion-de-materia-prima.md` — la puerta de entrada; sin esto nada aguas abajo es controlable.
→ `146-extraccion-dual-y-por-que-importa.md` — el corazón químico del proceso de hongos.
→ `151-relacion-planta-extracto-y-ratios.md` — qué significa y qué no significa el "10:1".
→ `152-estandarizacion-de-extractos.md` — cómo se pasa de un ratio a una promesa medible.
→ `167-bpm-gmp-para-suplementos.md` — qué exige INVIMA para que este proceso sea legal.
