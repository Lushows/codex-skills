# 80 — Detección UV-DAD y pureza de pico: cómo se demuestra que ese pico es lo que dicen que es

El detector UV es el que convierte una separación en un número. Es barato, estable y confiable, y por eso
casi toda la potencia que se reporta en el mundo de cannabis y productos naturales sale de un HPLC con
detector de arreglo de diodos. Pero tiene un límite duro que conviene entender antes de firmar una
especificación: **el UV no sabe qué compuesto es**; solo sabe cuánta luz se absorbió a cierta longitud de
onda en cierto momento. La "identidad" viene del tiempo de retención y del espectro, no de una huella
molecular. Ahí nace la mitad de los falsos positivos y de los sobre-reportes de potencia.

Términos:
- **UV-Vis (ultraviolet-visible detector)** = mide absorbancia a una o pocas longitudes de onda fijas.
- **DAD o PDA (diode array detector / photodiode array)** = mide **todo el espectro** (típicamente 190–400 o
  190–800 nm) en cada instante de la corrida. Es un UV que además guarda el espectro de cada pico.
- **λmax** = longitud de onda donde el compuesto absorbe más.
- **Ley de Beer-Lambert** = A = ε · b · c (absorbancia = absortividad molar × camino óptico × concentración).
- **Pureza de pico (peak purity)** = prueba de que bajo ese pico hay un solo compuesto.
- **Coelución (coelution)** = dos compuestos que salen al mismo tiempo y se ven como un solo pico.

## La ley que hace posible cuantificar

```
A = e * b * c

A = absorbancia (adimensional)
e = absortividad molar, L/(mol*cm) — propiedad del compuesto A ESA longitud de onda
b = camino optico de la celda, cm (tipicamente 1 cm; en UHPLC, 0,5-1 cm con volumen menor)
c = concentracion, mol/L

Consecuencia practica #1: la respuesta depende del COMPUESTO. THCA y D9-THC no
absorben igual a 228 nm. Por eso cada analito necesita su propio patron (70).
Consecuencia practica #2: la linealidad se acaba. Por encima de A ~ 1,5-2,0 UA
el detector se satura y la respuesta deja de crecer proporcionalmente ->
subestimacion de potencia en concentrados.
```

Cuando un laboratorio cuantifica un cannabinoide menor **usando la curva de otro** (por ejemplo, reportar
CBC contra el patrón de CBD porque no tiene patrón de CBC), está asumiendo que las absortividades son
iguales. No lo son. Eso se llama cuantificación por **respuesta relativa** y es aceptable solo si el factor
de respuesta relativa (relative response factor, RRF) está determinado y declarado. Si el COA no dice nada,
supón que no lo hicieron.

## Elegir la longitud de onda: dónde se cuantifica y por qué

| Familia | λ de cuantificación típica | λ de confirmación | Nota |
|---|---|---|---|
| Cannabinoides (THCA, THC, CBDA, CBD, CBG, CBN) | 220–228 nm | 270–280 nm | CBN absorbe fuerte a ~280 nm; los demás caen mucho ahí (`79`) |
| Psilocibina y psilocina | 267–270 nm | 220 nm | Núcleo indol; ver `256` |
| Triterpenos ganodéricos (reishi) | 243–252 nm | — | Absorben débil; por eso el método es poco sensible (`224`) |
| Cordicepina y adenosina | 254–260 nm | — | Núcleo purina (`228`) |
| Hericenonas / erinacinas | 220 nm y ~280 nm | — | Baja absortividad; muchos laboratorios usan LC-MS (`226`) |
| Flavonoides y polifenoles | 280 y 320–360 nm | — | Dos bandas características (`51`) |

Un detalle que cambia números: **la fase móvil también absorbe**. El acetonitrilo tiene corte UV
(UV cutoff) alrededor de 190 nm y es transparente a 220 nm; el metanol corta cerca de 205 nm; el acetato
absorbe por debajo de 230 nm; y el TFA (ácido trifluoroacético) sube la línea base a 220 nm. Por eso los
métodos de cannabinoides usan ácido fórmico al 0,1 %: es prácticamente transparente donde se cuantifica.

## Pureza de pico: la prueba que separa un método serio de uno bonito

Un DAD guarda el espectro completo a lo largo del pico. Si bajo el pico hay un solo compuesto, el espectro
en la subida, en el ápice y en la bajada es **el mismo**. Si hay dos, cambia.

```
Como lo evalua el software (nombres segun marca):

  Purity Angle vs Purity Threshold (Waters)
  Peak Purity Index / Similarity y Threshold curves (Agilent, Shimadzu)
  Match factor / similarity 0-1000

Criterio general: se acepta pureza cuando el angulo/indice de pureza queda
POR DEBAJO del umbral calculado a partir del ruido. Si el angulo supera el
umbral, hay coelucion o el pico esta contaminado.

LIMITE HONESTO: el DAD solo detecta coelucion si los dos compuestos tienen
espectros DIFERENTES. Dos cannabinoides isomeros (D8-THC y D9-THC, o CBD y CBG)
tienen espectros UV practicamente identicos. La pureza de pico por DAD NO los
distingue. Ahi la unica salida es cromatografia mejor (81) o masas (83, 84).
```

Este es el punto que hay que decirle en la cara a un proveedor: **"pureza de pico OK" no significa "no hay
Δ8-THC"**. Significa "no hay nada con espectro UV distinto escondido debajo". Con la ola de Δ8/Δ10/HHC
(`180`, `181`), un método UV mal resuelto puede sumar isómeros y reportarlos como Δ9-THC, o al revés.

## Qué ve y qué no ve un DAD

| Situación | ¿UV-DAD lo resuelve? | Alternativa |
|---|---|---|
| Cuantificar cannabinoides al 0,1–30 % p/p | Sí, es el estándar | — |
| Distinguir Δ8 de Δ9-THC | Solo si la cromatografía los separa; el espectro no ayuda | Columna adecuada (`81`) o MS (`83`) |
| Detectar pesticidas a µg/kg | No: insuficiente sensibilidad y selectividad | LC-MS/MS (`102`) |
| Detectar micotoxinas a µg/kg | Marginal (con fluorescencia sí, para algunas) | LC-MS/MS (`101`) |
| Cuantificar psilocibina en hongo (0,1–2 % p/p) | Sí, con buena preparación | HPLC-UV o LC-MS/MS (`256`) |
| Confirmar identidad de un compuesto desconocido | No | HRMS (`84`), RMN (`94`) |
| Compuestos sin cromóforo (azúcares, glucanos) | No absorben en UV útil | Índice de refracción, ELSD/CAD, o método enzimático (`91`, `221`) |

Esa última fila explica algo que confunde a mucha gente: **los β-glucanos no se miden por HPLC-UV**. No
tienen cromóforo. Se miden por método enzimático Megazyme (`221`). Si un COA te reporta β-glucano "por
HPLC", pregunta exactamente qué detectó y cómo — probablemente sea HPAEC-PAD o cromatografía de azúcares
tras hidrólisis, que es otra cosa y hay que declararla.

## Detectores alternativos cuando el UV no alcanza

| Detector | Qué mide | Cuándo se usa | Límite |
|---|---|---|---|
| **FLD** (fluorescence) | Emisión fluorescente | Aflatoxinas, algunas vitaminas | Solo compuestos fluorescentes o derivatizados |
| **RID** (refractive index) | Cambio de índice de refracción | Azúcares, polioles | Muy poco sensible; no admite gradiente |
| **ELSD / CAD** (evaporative light scattering / charged aerosol) | Partículas tras evaporar | Compuestos sin cromóforo, lípidos | Respuesta no lineal; menos precisión |
| **MS** | Relación masa/carga | Trazas y confirmación de identidad | Costo y efecto matriz (`83`) |

## Ejemplo aplicado — un COA de CBD con un pico sospechoso

```
Producto: aceite de CBD "full spectrum", declarado 1000 mg CBD por frasco de 30 mL.
COA reporta: CBD 3,4 % p/p ; D9-THC 0,28 % p/p ; "otros cannabinoides ND".

Lo que se pide y lo que aparece (ILUSTRATIVO):
  - Cromatograma a 228 nm: pico de THC ancho, con hombro en el flanco delantero.
  - Espectro DAD del apice vs el flanco: practicamente identicos (ambos cannabinoides).
  - Pureza de pico: "pasa".
  - Resolucion declarada del par critico: no reportada.

Interpretacion honesta: el DAD no puede descartar que ese hombro sea D8-THC
coeluyendo parcialmente con D9-THC. Si es D8, el D9 real es MENOR que 0,28 %
(bueno para cumplimiento) pero el producto contiene un isomero semisintetico
no declarado (mal para etiqueta y para regulacion — 180, 181).

Que se hace: pedir corrida con columna de mayor selectividad para isomeros o
confirmacion por LC-MS/MS con transiciones especificas, y exigir el valor de
resolucion Rs entre D8 y D9.  Costo adicional (ILUSTRATIVO): COP 250.000-600.000.
```

## Qué preguntarle al laboratorio

1. ¿A qué λ cuantifican cada analito y por qué esa?
2. ¿Evalúan **pureza de pico** con el DAD? ¿Cuál es el criterio y me lo reportan?
3. ¿Cuál es la **resolución (Rs)** entre el par crítico de mi matriz? (`75`)
4. ¿Cada analito tiene su **propio patrón**, o algunos se cuantifican por factor de respuesta relativa?
5. ¿Mi muestra quedó por debajo de la saturación del detector (A < ~1,5 UA)?
6. ¿Guardan el espectro DAD del pico para que un tercero lo pueda revisar?

## Errores comunes

- **Creer que "pureza de pico OK" = identidad confirmada.** Es lo contrario: descarta algunos problemas, no
  confirma la molécula.
- **Cuantificar cannabinoides menores contra el patrón de CBD** sin declarar el RRF, e inflar el "espectro
  completo" de la etiqueta.
- **Medir a 280 nm todo** porque "así se ve más limpio" y perder sensibilidad en THCA y CBDA.
- **Inyectar concentrados sin diluir** y reportar potencia con el detector saturado.
- **Pedir β-glucanos "por HPLC"** y aceptar un número que en realidad son polisacáridos totales (`222`).
- **Comparar áreas entre λ distintas** como si fueran comparables. No lo son.

## Conexión con otros módulos

→ `79-hplc-y-uhplc.md` — el equipo donde vive este detector.
→ `81-columnas-fases-y-desarrollo-de-metodo-lc.md` — cuando la solución al pico impuro es cromatográfica.
→ `83-lc-ms-ms-y-mrm.md` y `84-hrms-qtof-orbitrap-e-identificacion.md` — cuando hace falta identidad real.
→ `90-espectroscopia-uv-visible.md` — la técnica UV sin cromatografía y sus trampas.
→ `180-delta8-delta10-e-isomerizacion.md` — el problema práctico que el DAD no resuelve solo.
→ `221-medir-beta-glucanos-metodo-megazyme.md` — por qué ese analito no pasa por UV.
→ `111-banderas-rojas-en-un-coa.md` — qué falta en el COA que te acaban de mandar.
