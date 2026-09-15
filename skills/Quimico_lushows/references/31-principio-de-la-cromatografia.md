# 31 — Principio de la cromatografía (la puerta de entrada a todo el análisis)

Este módulo es la bisagra de la skill. Todo el bloque analítico —HPLC, GC, LC-MS/MS, HPTLC, cromatografía
preparativa— es una sola idea repetida: si un compuesto se reparte muchas veces entre dos fases, y otro se
reparte distinto, al final del camino salen separados. Nada más. Si entiendes este módulo, entiendes por
qué un pico se ensancha, por qué dos cannabinoides coeluyen, por qué "no detectado" no es "no hay", y por
qué el método que usó tu laboratorio explica el número que te entregó. Sin este concepto, un COA es un
papel con números; con él, es un documento que se puede auditar.

Términos: **fase móvil (mobile phase)** = lo que se mueve y arrastra la muestra (líquido en LC, gas en GC).
**fase estacionaria (stationary phase)** = lo que está fijo en la columna y retiene. **retención (retention
time, tR)** = tiempo que tarda un compuesto en salir, en minutos. **resolución (resolution, Rs)** = qué tan
separados están dos picos. **coelución (co-elution)** = dos compuestos que salen juntos y se confunden.
**gradiente (gradient)** = cambiar la composición de la fase móvil durante la corrida.

## La idea, en una figura mental

```
La columna es una escalera con miles de escalones. En cada escalón el compuesto decide:
  ¿me quedo con la fase estacionaria o me voy con la móvil?

Esa decisión es un equilibrio de reparto (`30`), con su constante K. Un compuesto con K grande
se queda más y sale tarde; uno con K pequeño se va rápido y sale temprano.

Miles de repartos sucesivos convierten una diferencia minúscula de afinidad en una separación limpia.
Eso es toda la cromatografía.
```

Por eso el módulo `30` (reparto) es el prerrequisito real, no el `19`. Y por eso cualquier cosa que cambie
el reparto —temperatura, pH, composición del solvente, la química de la superficie— cambia el
cromatograma.

## Las ecuaciones que aparecen en todo informe de laboratorio

```
Factor de retención:   k = (tR − t0) / t0        t0 = tiempo muerto. Ideal: k entre 2 y 10
Selectividad:          α = k2 / k1               α = 1 → NO se separan, punto
Eficiencia:            N = 16 · (tR / W)²        N = platos teóricos; W = ancho en la base
Resolución:            Rs = 2·(tR2 − tR1) / (W1 + W2)

Criterio de aceptación habitual:  Rs ≥ 1,5  (separación "a línea base")
Ecuación maestra:  Rs = (√N / 4) · ((α − 1)/α) · (k/(1+k))
```

La ecuación maestra dice algo muy práctico: **la selectividad (α) es la palanca más poderosa**. Duplicar N
(columna el doble de larga, el doble de tiempo y de presión) mejora la resolución solo en √2 ≈ 1,41. En
cambio, cambiar la química de la fase o el pH puede mover α y arreglar la separación en una tarde. Por eso
un buen desarrollador de métodos toca primero la fase móvil y la columna, no la longitud (`81`).

## Los modos de separación y qué separan

| Modo | Fase estacionaria | Separa por | Dónde lo usas |
|---|---|---|---|
| Fase reversa (RP) | C18, C8, fenil-hexilo (apolar) | Lipofilia (logP) | Cannabinoides, triterpenos, casi todo (`79`, `198`) |
| Fase normal (NP) | Sílice, alúmina (polar) | Polaridad | Fraccionamiento preparativo, HPTLC (`96`) |
| HILIC | Sílice o amida, móvil muy orgánica | Hidrofilia | Psilocibina y compuestos polares (`256`) |
| Intercambio iónico (IEX) | Grupos cargados | Carga neta | Péptidos, ácidos orgánicos, oxalato (`230`) |
| Exclusión por tamaño (SEC/GPC) | Poros calibrados | Tamaño molecular | Peso molecular de β-glucanos (`219`) |
| Gases (GC) | Película en columna capilar | Volatilidad + polaridad | Terpenos, solventes residuales (`85`, `86`, `87`) |
| Afinidad | Ligando específico | Reconocimiento biológico | Purificación de proteínas (`54`) |

Ojo con un caso que a la gente le sorprende: **el β-glucano no se cuantifica por cromatografía**. Es un
polímero heterogéneo; se mide por vía enzimática (K-YBGL) y su distribución de tamaño por SEC. Querer un
"HPLC de beta-glucanos" es pedir algo que no existe como método de rutina (`221`, `222`).

## Detección: la cromatografía separa, el detector cuenta

Separar no es medir. Después de la columna va un detector, y **el detector define qué puedes afirmar**:

| Detector | Qué mide | Especificidad | Nota |
|---|---|---|---|
| UV / DAD | Absorbancia | Baja–media; el DAD da espectro y pureza de pico | Necesita cromóforo; es el caballo de batalla (`80`) |
| Índice de refracción (RI) | Cambio de índice | Muy baja | Azúcares; no sirve con gradiente |
| Fluorescencia | Emisión | Alta si el analito fluoresce | Micotoxinas (`101`) |
| ELSD / CAD | Masa de no volátiles | Baja pero universal | Compuestos sin cromóforo |
| MS simple cuadrupolo | Relación m/z | Media | Confirmación básica (`82`) |
| MS/MS (triple cuadrupolo, MRM) | Transición precursor→fragmento | Muy alta | Pesticidas, psilocibina trazas (`83`) |
| HRMS (QTOF, Orbitrap) | m/z exacta | Muy alta + identificación de desconocidos | Adulterantes, metabolómica (`84`, `104`) |
| FID (en GC) | Carbono que quema | Baja, pero muy lineal | Solventes residuales (`87`) |

Regla dura: **un tiempo de retención no identifica nada por sí solo**. Identificar exige coincidencia de
tR con estándar **más** un criterio adicional (espectro UV, relación de iones MS/MS, masa exacta). Un COA
que dice "identificado por tR" está afirmando de más (`111`).

## Cómo se comprueba que la separación sirve

| Pregunta | Cómo se comprueba | Criterio típico |
|---|---|---|
| ¿Está resuelto de sus vecinos? | Rs entre el analito y el pico más cercano | Rs ≥ 1,5 (`75`) |
| ¿El pico es de un solo compuesto? | Pureza de pico por DAD o por MS | Índice de pureza dentro de umbral (`80`) |
| ¿La columna sigue buena? | N y factor de cola (tailing) del control | N dentro de especificación; T ≤ 2,0 |
| ¿El sistema está en control? | System suitability al inicio de cada secuencia | RSD de área ≤ 2 % en 5 inyecciones (`77`) |
| ¿La matriz me está afectando? | Comparar pendiente en solvente vs en matriz | Efecto matriz en % (`72`, `83`) |
| ¿Hasta dónde puedo detectar? | LOD y LOQ del método, en esa matriz | µg/g o mg/kg (`73`) |

## Ejemplo aplicado — por qué el mismo material dio dos potencias distintas

Flor de cannabis, mismo lote, dos laboratorios **(ILUSTRATIVO)**:

```
Lab A — HPLC C18, gradiente, DAD 228 nm, 12 min
   THCA 21,4 % · Δ9-THC 0,9 % · CBN 0,1 %  → THC total = 0,9 + 21,4×0,877 = 19,67 % p/p b.s.

Lab B — HPLC C18 corta, isocrático, UV fijo 220 nm, 6 min
   THCA 23,8 % · Δ9-THC 1,1 % · CBN n.d.   → THC total = 1,1 + 23,8×0,877 = 21,97 % p/p b.s.

Diferencia: 2,3 puntos porcentuales, 12 % relativo
```

Auditoría del caso: el método corto de Lab B no resuelve THCA de CBGA (Rs ≈ 0,9), así que el área del
THCA incluye parte del CBGA — sobrestimación. Además, a 220 nm hay más interferencia de matriz que a
228 nm, y el UV fijo no permite verificar pureza de pico. No hubo fraude: hubo un método con resolución
insuficiente. La forma de zanjarlo es pedir el cromatograma, la resolución reportada y el certificado del
estándar, no discutir el número (`111`, `112`, `198`).

## Errores comunes

- Aceptar un resultado sin ver el cromatograma. El número solo no es auditable.
- Identificar por tiempo de retención únicamente, sin espectro ni MS/MS.
- Comparar resultados de dos métodos distintos como si fueran el mismo dato.
- Creer que un pico grande y bonito significa pureza. Puede ser dos compuestos coeluyendo (`80`).
- Alargar la columna para resolver un par crítico en vez de cambiar la selectividad. Caro y poco efectivo.
- Pedir "HPLC de beta-glucanos". No existe como método de rutina; el método es enzimático (`221`).
- Confundir "no detectado" con "cero". Solo significa por debajo del LOD de ESE método (`73`).

## Conexión con otros módulos

→ `65-el-metodo-analitico-de-punta-a-punta.md` — entrada al bloque analítico completo (65–114).
→ `79-hplc-y-uhplc.md` — la técnica que más vas a ver.
→ `81-columnas-fases-y-desarrollo-de-metodo-lc.md` — cómo se mueve α en la práctica.
→ `82-espectrometria-de-masas-fundamentos.md` — el detector que identifica de verdad.
→ `30-extraccion-liquido-liquido-y-logp.md` — el reparto que la cromatografía repite miles de veces.
→ `110-como-leer-un-coa.md` — cómo se audita el resultado que sale de aquí.
→ `193-cromatografia-preparativa-y-aislados.md` — la misma física, a escala de kilos.
