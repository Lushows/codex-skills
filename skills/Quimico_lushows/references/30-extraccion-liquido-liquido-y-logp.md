# 30 — Extracción líquido-líquido y logP (por qué los cannabinoides viven en la grasa)

El coeficiente de reparto es uno de los números más útiles de toda la química aplicada: predice en qué
fase se va a quedar tu molécula, cómo se comporta en una partición, si va a atravesar una membrana, si se
absorbe al tomarla y hasta cómo se va a comportar en una columna de cromatografía. Con un solo número
—logP— entiendes por qué el CBD necesita aceite y el β-glucano necesita agua, por qué una nanoemulsión de
CBD existe, y por qué la psilocibina se comporta al revés que todo lo demás de este oficio.

Términos: **coeficiente de reparto (partition coefficient, P)** = relación de concentraciones de un soluto
entre dos fases inmiscibles en equilibrio, clásicamente octanol/agua. **logP** = su logaritmo base 10; es
para la forma **neutra** de la molécula. **logD** = lo mismo pero a un pH dado, contando la fracción
ionizada. **lipofilia (lipophilicity)** = afinidad por la grasa. **inmiscible (immiscible)** = que no se
mezcla. **emulsión (emulsion)** = dispersión de una fase en otra; aquí suele ser el enemigo del embudo
(`32`).

## Las ecuaciones

```
P = C_octanol / C_agua              (forma neutra, en el equilibrio)
logP = log10(P)

logD(pH) = logP − log10( 1 + 10^(pH − pKa) )      para un ÁCIDO
logD(pH) = logP − log10( 1 + 10^(pKa − pH) )      para una BASE

Lectura:  logP < 0   hidrofílico      logP 1–3  equilibrado     logP > 5  muy lipofílico
```

La diferencia entre logP y logD es donde se pierde la gente: el logP del THCA (una molécula con –COOH) no
describe su comportamiento a pH 7, porque a pH 7 está ionizado. Ahí manda **logD**, y por eso el pH es una
palanca de separación (`22`).

## Los logP que te tocan

| Compuesto | logP reportado (aprox.) | Lectura práctica |
|---|---|---|
| Δ9-THC | ~6,8–7 | Extremadamente lipofílico: aceite, alcohol, hidrocarburo; agua ni de broma |
| CBD | ~6,3–6,5 | Igual; su solubilidad en agua es del orden de µg/mL (`19`) |
| CBN | ~6,3 | Igual familia |
| THCA / CBDA | ~5,5–6 (neutro) — mucho menor como anión | Por eso responden al pH (`22`) |
| Limoneno, mirceno | ~4,4–4,9 | Lipofílicos y volátiles a la vez (`28`) |
| Ácido ganodérico A | ~2–3 | Intermedio: sale con EtOH 60–96 %, no con agua fría (`224`) |
| Ergosterol | ~7–8 | Muy lipofílico; marcador de biomasa fúngica (`238`) |
| Psilocibina | ~ −1,5 a −2 (zwitterión) | Hidrofílica: agua sí, aceite no. Al revés de todo lo anterior |
| Psilocina | ~1,3 | Suficientemente lipofílica para cruzar membranas (`127`, `257`) |
| Ergotioneína | ~ −3 | Zwitteriónica, se queda en el agua siempre (`235`) |
| β-glucano (polímero) | no aplica | No es una molécula pequeña; su comportamiento es coloidal (`219`) |

Esa tabla contiene, en una sola columna, la explicación de por qué **la extracción dual existe** (`146`):
tus dos familias de activos están en extremos opuestos de la escala.

## Por qué el cannabinoide es tan lipofílico (la estructura manda)

Un cannabinoide es un resorcinol (dos –OH fenólicos) con una **cadena alquílica de 5 carbonos** y un
sistema terpénico C10 pegado. Contando: ~21 carbonos casi todos apolares, contra 2 grupos –OH. La relación
apolar/polar es abrumadora, y los dos –OH quedan además parcialmente impedidos. Resultado: logP ~6–7, que
es territorio de "prácticamente insoluble en agua".

Consecuencias en cadena, todas medibles:

1. **Formulación.** Solo se puede vehicular en grasa, en alcohol, o forzándolo a una fase acuosa con
   tensioactivos — es decir, nanoemulsión (`33`, `157`).
2. **Absorción oral.** Se absorbe con la grasa de la comida; el efecto de la comida es enorme y está
   documentado `[clínico]` (`122`, `159`).
3. **Distribución.** Se acumula en tejido graso, lo que alarga la eliminación aparente (`121`, `126`).
4. **Análisis.** Se adsorbe a plásticos y paredes; los estándares se manejan en vidrio silanizado y en
   solvente orgánico (`70`).
5. **Limpieza de equipos.** No sale con agua. La validación de limpieza se hace con solvente (`167`).

La psilocibina hace exactamente lo contrario: zwitteriónica, logP negativo, muy hidrosoluble, y por eso su
extracción para análisis se hace en metanol acuoso y su química de estabilidad es la de un compuesto polar
oxidable (`251`, `255`, `256`).

## Extracción líquido-líquido: cómo se hace bien

```
Regla de oro: n extracciones pequeñas rinden más que 1 grande con el mismo volumen total (`21`)

Fracción que queda sin extraer tras n etapas con volúmenes iguales:
    f_restante = [ V_ac / (V_ac + P · V_org) ]^n

Ejemplo: P = 10, V_ac = V_org = 100 mL
    1 etapa de 100 mL  → queda 1/(1+10) = 9,1 %   → extrae 90,9 %
    2 etapas de 50 mL  → queda [100/(100+500)]^2 = 2,8 % → extrae 97,2 %
```

Trucos de oficio: si se forma emulsión en el embudo, se rompe con sal (salting out), con centrifugación o
dejando reposar; nunca agitando más. Si el analito es ionizable, se ajusta el pH **antes** de particionar
para llevarlo a la forma neutra (`22`). Y siempre se verifica en qué fase quedó midiendo las dos, no
suponiendo.

## Cómo se mide

| Pregunta | Método | Unidad |
|---|---|---|
| ¿Cuál es el logP real de mi molécula? | Shake-flask octanol/agua + cuantificación en ambas fases (OECD 107) | logP adimensional, a T y pH declarados |
| ¿Y si es muy lipofílico? | Método cromatográfico (HPLC, OECD 117) contra patrones de logP conocido | logP estimado |
| ¿Cuál es el logD a mi pH? | Shake-flask con la fase acuosa bufferada al pH de interés (`23`) | logD a pH declarado |
| ¿Cuánto activo pasó a la fase orgánica? | HPLC de ambas fases + balance de masa | % de recuperación (`06`) |
| ¿Se quedó algo en la interfase? | Pesar y analizar la interfase; no ignorarla | mg y % del total |
| ¿Predicción rápida antes de gastar? | Cálculo in silico (XLogP3, cLogP) | Estimado — **se marca como calculado, no medido** (`39`) |

Regla dura: un logP calculado por software es una **predicción**, no un dato experimental. Se puede usar
para decidir el diseño; no se pone en un expediente técnico como valor medido (`286`, `02`).

## Ejemplo aplicado — limpiar clorofila de un extracto de cannabis con partición

Extracto etanólico crudo, verde oscuro, se quiere quitar clorofila conservando cannabinoides
**(ILUSTRATIVO)**:

```
Paso                                          Cannabinoides   Clorofila (A665)   Comentario
Crudo etanólico (base)                           100 %            1,00           Verde intenso
Partición hexano / metanol-agua 9:1, 3 etapas
  → fase hexano (se conserva)                     94 %            0,18           Cannabinoides, logP alto
  → fase metanólica (se descarta)                  6 %            0,82           Clorofila, más polar
Lavado adicional con MeOH:agua 8:2                 91 %            0,09           Se pierde 3 % más

Cannabinoides por HPLC-UV 228 nm; clorofila estimada por absorbancia a 665 nm (`90`)
```

Lectura: la partición cuesta 6–9 % del activo y quita 80–90 % del pigmento. Si el producto final es un
destilado, no vale la pena (la destilación deja el pigmento en las colas, `29`); si el producto es un
aceite full spectrum donde el color importa, sí. La decisión es económica y de posicionamiento, con
números medidos, no con "quedó más bonito". Ojo: hexano y metanol son solventes clase 2 con límites
estrictos de residuo; su uso obliga a análisis de solventes residuales del producto final (`87`, `63`).

## Errores comunes

- Usar logP cuando la molécula está ionizada al pH de trabajo. Ahí manda logD (`22`).
- Reportar un logP calculado como si fuera medido.
- Hacer una sola partición grande en vez de tres pequeñas. Se pierde recuperación gratis.
- Descartar la fase acuosa sin analizarla. La mitad de las "pérdidas inexplicables" están ahí.
- Ignorar la interfase cuando se forma emulsión: puede llevarse un porcentaje considerable del activo.
- Suponer que "polar" y "apolar" son categorías binarias. Es una escala continua y los intermedios
  (triterpenos, logP 2–3) son los que dan trabajo.
- Elegir solventes por costumbre sin mirar su clase toxicológica y su límite de residuo (`87`, `63`).

## Conexión con otros módulos

→ `19-soluciones-y-solubilidad.md` — la otra mitad de la decisión de solvente.
→ `20-parametros-de-solubilidad-y-eleccion-de-solvente.md` — Hansen, para elegir sin adivinar.
→ `22-acidos-bases-y-ph.md` — cómo el pH convierte logP en logD.
→ `31-principio-de-la-cromatografia.md` — el mismo reparto, repetido miles de veces.
→ `122-biodisponibilidad-y-efecto-de-primer-paso.md` — logP y absorción oral.
→ `157-emulsiones-y-nanoemulsiones.md` — cómo se mete un logP 7 en una bebida.
→ `251-psilocibina-y-psilocina-quimica.md` — el caso invertido: logP negativo.
