# 42 — Isomería y estereoquímica (dos moléculas con la misma fórmula y distinto destino legal)

Dos sustancias pueden tener exactamente la misma fórmula molecular, la misma masa exacta y el mismo espectro
de masas de baja resolución, y sin embargo una ser legal y la otra controlada, una activa y la otra inerte,
una estable y la otra que se degrada en tres meses. Eso es la isomería, y en cannabis es el centro de un
mercado de miles de millones de dólares: Δ8-THC y Δ9-THC son isómeros de posición. Si tu método analítico no
los separa cromatográficamente, tu COA es una opinión. Este módulo te da el mapa de tipos de isomería y,
sobre todo, el criterio de qué exigirle al laboratorio para que la diferencia sea demostrable.

Términos: **isómeros (isomers)** = compuestos con la misma fórmula molecular y distinta estructura.
**Isómeros constitucionales (constitutional isomers)** = difieren en qué está unido con qué.
**Estereoisómeros (stereoisomers)** = misma conectividad, distinta disposición en el espacio.
**Resolución cromatográfica Rs (resolution)** = qué tan separados están dos picos; Rs ≥ 1,5 = separación a
línea base. **Coelución (coelution)** = dos compuestos que salen al mismo tiempo y se cuentan como uno.

## El árbol completo de la isomería

```
ISÓMEROS (misma fórmula molecular)
│
├── CONSTITUCIONALES (distinta conectividad)
│   ├── de cadena      → n-butano vs isobutano
│   ├── de posición    → Δ8-THC vs Δ9-THC   ← el caso del cannabis
│   └── de función     → etanol vs dimetil éter
│
└── ESTEREOISÓMEROS (misma conectividad, distinto espacio)
    ├── CONFIGURACIONALES (solo se cambian rompiendo enlaces)
    │   ├── enantiómeros  → imágenes especulares no superponibles  (ver `43`)
    │   └── diastereómeros → no especulares: cis/trans, E/Z, epímeros
    └── CONFORMACIONALES (giro libre; silla/bote, no son sustancias distintas)
```

| Tipo | ¿Misma masa exacta? | ¿Se separan por MS? | ¿Se separan por LC/GC? |
|---|---|---|---|
| De posición (Δ8 vs Δ9) | Sí | No, solo por fragmentación fina/HRMS con cuidado | **Sí**, es la única vía práctica |
| De función | Sí | A veces por fragmentación | Sí |
| Diastereómeros (cis/trans) | Sí | Casi nunca | Sí, columna normal |
| Enantiómeros | Sí | **No** | Solo con **columna quiral** (`43`) |

## Δ8 vs Δ9: el caso que hay que dominar

Ambos son **C₂₁H₃₀O₂**, masa monoisotópica **314,2246 Da**, masa molar **314,47 g/mol**. La única diferencia
es la posición del doble enlace en el anillo ciclohexeno: entre C9-C10 (Δ9) o entre C8-C9 (Δ8).

| Propiedad | Δ9-THC | Δ8-THC |
|---|---|---|
| Posición del doble enlace | C9=C10 (exocíclico al carbono terciario) | C8=C9 (endocíclico, más sustituido) |
| Estabilidad termodinámica | Menor | **Mayor** (alqueno más sustituido) |
| Origen | Biosintético (vía THCA, `172`) | Mayoritariamente por isomerización ácida de CBD (`180`) |
| Potencia relativa en CB1 | Referencia | Menor, reportado en literatura como fracción de Δ9 |
| Ion precursor en LC-MS/MS | m/z 315,2 [M+H]⁺ | m/z 315,2 [M+H]⁺ — **idéntico** |

La consecuencia analítica es brutal y hay que decirla sin rodeos: **en LC-MS/MS de triple cuadrupolo, Δ8 y
Δ9 dan el mismo precursor y transiciones muy parecidas.** Lo único que los distingue en la práctica es que
salgan a tiempos de retención distintos. Por eso, en un método de potencia, la exigencia de aceptación no es
"se detectó Δ9-THC", es:

```
Criterio de idoneidad del sistema (system suitability) — método de potencia de cannabis:
  Rs (Δ8-THC / Δ9-THC) ≥ 1,5    en la mezcla de patrones, en cada secuencia
  Rs (CBD / CBG)       ≥ 1,5
  Rs (THCA / CBDA)     ≥ 1,5
  Si no se cumple: la secuencia NO se reporta. Se reacondiciona la columna o se ajusta el gradiente.
```

Un laboratorio que no te muestre el cromatograma de la mezcla de patrones con esa resolución no puede
sostener el número de Δ9 que te reporta (`111`, `198`).

## Isomería en hongos: menos famosa, igual de cara

- **Psilocibina vs baeocistina.** No son isómeros (difieren en un CH₂: 284,25 vs 270,22 g/mol), pero eluyen
  muy cerca y se confunden en métodos mal desarrollados. Sí hay que resolverlas (`256`).
- **Isómeros de posición del hidroxilo en triptaminas.** 4-hidroxi (psilocina) y 5-hidroxi (bufotenina) son
  isómeros de posición con la misma fórmula C₁₂H₁₆N₂O (204,27 g/mol) y farmacología distinta. Otra vez: los
  separa la cromatografía, no la masa.
- **Ergosterol y sus isómeros de posición del doble enlace** (ergosta-5,7,22-trienol vs 7,22-dienol):
  importan porque el ergosterol se usa como marcador de biomasa fúngica (`238`).
- **Enlaces glicosídicos.** β-(1→3) y β-(1→6) y β-(1→4) generan polímeros de la misma unidad —glucosa— con
  propiedades radicalmente distintas. Formalmente es isomería de posición del enlace, y es la base de por qué
  el glucano de hongo no es el de avena ni el almidón (`52`).

## Cómo se comprueba cuál isómero tienes

| Pregunta | Técnica | Criterio de aceptación |
|---|---|---|
| ¿Δ8 o Δ9? | HPLC-DAD o LC-MS con patrones de ambos | Rs ≥ 1,5; tiempo de retención ± 2 % del patrón |
| ¿Cis o trans / E o Z? | RMN (NOE, constantes de acoplamiento *J*) | *J* trans-diaxial típicamente mayor que gauche |
| ¿Qué enantiómero? | HPLC quiral (fase estacionaria de polisacárido) | Ver `43` |
| ¿Isómero desconocido nuevo? | HRMS + RMN 2D (COSY, HSQC, HMBC) | Fórmula con error < 5 ppm + conectividad |
| ¿Coeluye algo con mi pico? | DAD, pureza de pico espectral | Índice de pureza dentro del umbral (`80`) |

## Ejemplo aplicado — auditar un COA de "Δ9-THC no detectado"

Te llega un COA de un aceite importado (ILUSTRATIVO):

```
Δ9-THC: <LOQ (LOQ = 0,05 % p/p)   |   Δ8-THC: 4,2 % p/p   |   CBD: 1,1 % p/p
Método: "HPLC-UV, in-house"       |   Columna: no declarada
Cromatograma: no adjunto          |   Mezcla de patrones: no adjunta
```

Preguntas que hay que hacer, en ese orden:
1. ¿Corrieron un patrón de Δ9-THC en esa misma secuencia y a qué tiempo de retención salió?
2. ¿Cuál fue la Rs entre Δ8 y Δ9 en la mezcla de patrones? Si no la midieron, el "no detectado" puede ser
   simplemente Δ9 escondido bajo el pico gigante de Δ8.
3. ¿El LOQ de 0,05 % p/p se validó en **esta matriz** (aceite) o en solución (`73`, `74`)?
4. Con 4,2 % de Δ8 y 1,1 % de CBD residual, el perfil es coherente con isomerización de CBD (`180`): habría
   que pedir también los subproductos de esa reacción, que casi nadie mide.

Sin esas cuatro respuestas, ese COA no soporta ninguna decisión de compra ni ninguna declaración legal.

## Errores comunes

- Creer que un LC-MS/MS "es más específico" y por eso no hace falta separar isómeros. Es al revés: la MS te
  da la misma respuesta para ambos, así que la separación es más crítica, no menos.
- Comparar tiempos de retención entre laboratorios o entre columnas distintas. Solo valen dentro de la misma
  corrida, contra el patrón de esa corrida.
- Reportar "cannabinoides totales" sumando isómeros que no se resolvieron: se cuenta dos veces o se cuenta mal.
- Suponer que un isómero minoritario es irrelevante. En regulación de cannabis lo relevante suele ser un
  umbral (0,3 % p/p de THC total), y un isómero mal asignado te cruza el umbral (`175`).
- Olvidar que la isomerización puede ocurrir **dentro del producto** con el tiempo, no solo en el proceso: el
  medio ácido y el calor la promueven (`61`, `204`).

## Conexión con otros módulos

→ `43-quiralidad-y-enantiomeros.md` — el caso especial de las imágenes especulares y el (−)-trans-Δ9-THC.
→ `41-nomenclatura-organica.md` — cómo se escribe cada isómero sin ambigüedad.
→ `180-delta8-delta10-e-isomerizacion.md` — el mercado, la reacción y el riesgo regulatorio.
→ `81-columnas-fases-y-desarrollo-de-metodo-lc.md` — cómo se logra la Rs ≥ 1,5.
→ `52-polisacaridos-y-glucanos.md` — isomería de enlace glicosídico, el caso de los hongos.
