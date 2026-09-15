# 19 — Soluciones y solubilidad (por qué el agua saca beta-glucanos y el etanol saca triterpenos)

Aquí se decide tu proceso. Una extracción no es "hervir hierbas": es un experimento de solubilidad donde
eliges solvente, temperatura, relación sólido:líquido y tiempo, y cada elección mueve el perfil químico de
lo que sale. Si no dominas este módulo vas a comprar un extracto "de espectro completo" que no tiene lo
que dice, o vas a diseñar un proceso que bota el 60 % de tu activo por el filtro. Y sobre todo, vas a
entender de una vez por qué la tradición china hierve el reishi y la tradición occidental lo tinta con
alcohol: no compiten, sacan cosas distintas.

Términos: **soluto (solute)** = lo que se disuelve. **solvente (solvent)** = el que disuelve. **solubilidad
(solubility)** = masa máxima de soluto por volumen de solvente a una temperatura dada, en mg/mL o g/L.
**saturación (saturation)** = punto donde ya no se disuelve más. **coeficiente de reparto (partition
coefficient)** = cómo se reparte un soluto entre dos fases (`30`). **relación sólido:líquido (solid-to-
solvent ratio)** = g de biomasa por mL de solvente, escrito 1:10, 1:20.

## "Lo semejante disuelve a lo semejante", con números

| Soluto | Rasgo dominante | Solubilidad en agua | Solubilidad en EtOH 96 % | Solvente de elección |
|---|---|---|---|---|
| β-1,3/1,6-glucano | Cientos de –OH, polímero grande | Baja en frío, sube con agua caliente | Muy baja (precipita) | Agua 80–100 °C |
| Ácidos ganodéricos (triterpenos) | C30 lanostano + –COOH | Muy baja | Buena | EtOH 60–96 % |
| Ergotioneína | Zwitteriónica | Alta | Baja | Agua |
| Adenosina / cordicepina | Nucleósidos polares | Moderada | Moderada | Agua o EtOH 30–50 % |
| Δ9-THC / CBD | C21, casi sin polaridad neta | Orden de µg/mL | Alta | EtOH, aceite, hidrocarburo, CO2 |
| THCA / CBDA (formas ácidas) | Añaden –COOH | Mayor que la neutra, aún baja | Alta | EtOH frío |
| Psilocibina | Éster fosfato zwitteriónico | Alta | Baja/moderada | Agua o MeOH acuoso (uso analítico) |
| Ergosterol | Esterol apolar | Nula práctica | Buena en caliente | EtOH caliente o hexano |

Esa tabla es el argumento entero de la **extracción dual** (`146`): dos solventes porque hay dos familias
de activos con solubilidades opuestas. Vender "dual" y usar solo alcohol es una mentira medible.

## Las cinco variables que mueves (y cuánto pesan)

| Variable | Efecto típico | Cuidado |
|---|---|---|
| Solvente | El más grande: cambia qué familia sale | Cambia también la matriz del método analítico (`75`) |
| Temperatura | Sube difusión y solubilidad; rompe pared celular | Degrada termolábiles: psilocibina, algunos fenoles (`26`) |
| Tiempo | Se acerca al equilibrio; rendimiento asintótico | Después del plateau solo degradas y gastas energía |
| Relación S:L | 1:20 extrae más que 1:5 por gradiente | Más solvente = más costo de evaporación (`149`) |
| Agitación / tamaño de partícula | Reduce resistencia de transferencia de masa | Molienda excesiva dificulta el filtrado (`143`) |

Modelo mental útil: la extracción es transferencia de masa contra un gradiente. Mientras el solvente esté
lejos de saturarse, sigue sacando. Por eso dos extracciones de 1 h con solvente fresco rinden más que una
de 2 h con el mismo solvente — y eso se llama extracción multietapa.

## Por qué el agua caliente y no el agua fría (beta-glucanos)

El β-glucano fúngico está atrapado en la pared celular, entrecruzado con quitina. El agua fría no lo saca
aunque el polímero sea hidrofílico: el limitante no es la solubilidad, es la **liberación de la matriz**.
El agua a 80–100 °C hace tres cosas: hincha la pared, hidroliza parcialmente enlaces que sujetan el
glucano, y rompe los puentes de hidrógeno glucano–glucano que mantienen la hélice triple agregada. Por eso
la decocción tradicional funciona y por eso el "reishi en agua fría" rinde poco (`144`, `241`).

El etanol hace lo contrario: al bajar la constante dieléctrica, el glucano deja de estar solvatado y
precipita. Eso es un defecto si querías extraerlo, y una herramienta si querías **recuperarlo**: la
precipitación etanólica (añadir 3–4 volúmenes de EtOH al extracto acuoso) es el paso clásico para
concentrar polisacáridos.

## Cómo se mide

| Pregunta | Método | Unidad |
|---|---|---|
| ¿Cuánto sólido saqué? | Gravimetría de extracto seco (estufa 105 °C o liofilizar y pesar) | % rendimiento p/p b.s. |
| ¿Cuánto activo saqué? | Ensayo específico sobre el extracto: K-YBGL (β-glucano), HPLC (triterpenos, cannabinoides) | mg/g extracto y mg/g biomasa |
| ¿Ya llegué al equilibrio? | Curva cinética: muestrear a 15, 30, 60, 120, 240 min | mg/g vs tiempo, buscar plateau |
| ¿Cuál es la solubilidad real de mi activo? | Shake-flask: saturar, filtrar 0,45 µm, cuantificar por HPLC | mg/mL a T dada |
| ¿Cuál solvente conviene? | DoE con mezclas EtOH/agua (0, 30, 50, 70, 96 %) | Superficie de respuesta (`287`) |

Regla dura: el rendimiento se debe reportar **sobre biomasa seca de entrada**, no sobre extracto. "30 % de
beta-glucano en el extracto" y "30 % de recuperación del beta-glucano de la biomasa" son números
diferentes y confundirlos infla tu etiqueta (`151`, `242`).

## Ejemplo aplicado

Screening sobre 100 g de cuerpo fructífero de reishi molido a 0,5 mm, 1:20, 2 h **(ILUSTRATIVO)**:

```
Solvente        Extracto seco   β-glucano en extracto   Triterpenos en extracto   Recuperación β-glucano
                (% p/p b.s.)    (% p/p b.s., K-YBGL)    (mg/g, HPLC-UV 252 nm)    (% del contenido inicial)
Agua 95 °C          18,4              24,1                     0,4                        61 %
Agua 60 °C           9,1              19,8                     0,3                        25 %
EtOH 70 %, 25 °C     8,7               2,3                    11,2                         6 %
EtOH 96 %, 60 °C     6,2               0,9                    16,8                         2 %
```

Conclusiones que se pueden defender: (1) si el claim es beta-glucanos, la ruta es agua caliente y hay que
subir de una a dos etapas para pasar del 61 %; (2) el alcohol solo entrega el 6 % del beta-glucano
disponible: no puede sostener un claim de beta-glucanos; (3) la combinación dual da un producto con ambos,
pero cada activo diluido — hay que declarar los dos números con su método. Los porcentajes de recuperación
se calculan contra el contenido de la biomasa medido aparte; sin ese dato base, el "61 %" no existe.

## Errores comunes

- Reportar potencia del extracto sin decir el ratio ni el rendimiento. "30 %" sin base es humo (`242`).
- Hervir 6 horas creyendo que "más es mejor". Después del plateau solo degradas y pagas gas.
- Usar alcohol para hongos porque "el alcohol extrae mejor". Extrae mejor lo apolar, no lo tuyo.
- Filtrar en caliente y perder el glucano que precipita al enfriar. Muestrea después de estabilizar.
- Olvidar que el agua caliente también extrae potasio, oxalatos y —si el material está contaminado—
  metales solubles. La extracción concentra lo malo igual que lo bueno (`243`).
- Escalar del laboratorio a 100 L sin repetir la curva cinética. La transferencia de masa cambia con la
  geometría del tanque (`166`).

## Conexión con otros módulos

→ `20-parametros-de-solubilidad-y-eleccion-de-solvente.md` — cómo elegir sin adivinar (Hansen).
→ `17-polaridad-y-fuerzas-intermoleculares.md` — la física detrás de esta tabla.
→ `144-extraccion-acuosa-y-decoccion.md` — el proceso acuoso, paso a paso.
→ `145-extraccion-hidroalcoholica-y-tinturas.md` — el proceso alcohólico.
→ `146-extraccion-dual-y-por-que-importa.md` — por qué se hacen las dos.
→ `241-extraccion-de-hongos-agua-vs-alcohol.md` — el caso completo con rendimientos por especie.