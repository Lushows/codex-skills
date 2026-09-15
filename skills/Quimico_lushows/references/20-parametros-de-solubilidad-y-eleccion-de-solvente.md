# 20 — Parámetros de solubilidad y elección de solvente (dejar de adivinar con Hansen)

El módulo anterior te dijo qué pasa; este te dice cómo **elegir** sin quemar seis meses probando. Existe
una herramienta cuantitativa —los parámetros de solubilidad de Hansen— que convierte "lo semejante
disuelve a lo semejante" en tres números por sustancia y una distancia calculable. Con eso puedes predecir
qué mezcla etanol/agua va a sacar mejor los triterpenos del reishi, o por qué el hexano saca cannabinoides
pero también ceras. Es la diferencia entre un desarrollo de proceso de químico y uno de ensayo y error.

Términos: **parámetro de solubilidad de Hildebrand (δ)** = raíz de la densidad de energía cohesiva, en
MPa^0,5; una sola cifra por solvente. **parámetros de Hansen (HSP)** = tres componentes: δD dispersión,
δP polar, δH puentes de hidrógeno, todos en MPa^0,5. **distancia de Hansen (Ra)** = qué tan lejos está un
solvente del soluto en ese espacio 3D; menor Ra = mejor solvente. **radio de interacción (R0)** = radio de
la esfera de solubilidad del soluto. **RED (relative energy difference)** = Ra/R0; RED < 1 predice
disolución.

## La tabla de Hansen que vas a usar

Valores de la literatura de HSP, en MPa^0,5, a 25 °C. Verifica contra tu fuente antes de publicar.

| Solvente | δD | δP | δH | δ total | Nota de oficio |
|---|---|---|---|---|---|
| Agua | 15,5 | 16,0 | 42,3 | 47,8 | δH altísimo: por eso solvata glucanos |
| Etanol | 15,8 | 8,8 | 19,4 | 26,5 | El caballo de batalla, Clase 3 ICH (`87`) |
| Metanol | 15,1 | 12,3 | 22,3 | 29,6 | Analítico; Clase 2, no para producto |
| Isopropanol | 15,8 | 6,1 | 16,4 | 23,6 | Alternativa a etanol en algunos países |
| Acetona | 15,5 | 10,4 | 7,0 | 20,0 | Clase 3, sabor/olor residual |
| Acetato de etilo | 15,8 | 5,3 | 7,2 | 18,2 | Buen extractante de terpenoides |
| Hexano | 14,9 | 0,0 | 0,0 | 14,9 | Clase 2; saca ceras junto al activo |
| CO2 supercrítico | ~13–17 (ajustable) | ~0–6 | ~0–6 | variable | Se "sintoniza" con presión (`148`) |
| Aceite MCT | ~16 | ~3 | ~4 | ~17 | Solvente y vehículo a la vez |

Y los solutos aproximados que te interesan **(ILUSTRATIVO — HSP estimados por contribución de grupos, no
medidos)**:

| Soluto | δD | δP | δH | Lectura |
|---|---|---|---|---|
| CBD / Δ9-THC | ~17,5 | ~4 | ~6 | Cerca de acetato de etilo y etanol; lejísimos del agua |
| Ácido ganodérico A | ~17 | ~6 | ~10 | Etanol 60–80 % cae casi encima |
| β-glucano (unidad) | ~19 | ~13 | ~25 | Solo el agua se le acerca |
| Psilocibina | ~19 | ~14 | ~22 | Zona acuosa; por eso el agua/MeOH acuoso |

## Cómo se calcula la distancia (y por qué las mezclas funcionan)

```
Ra = sqrt( 4·(δD_solv − δD_soluto)² + (δP_solv − δP_soluto)² + (δH_solv − δH_soluto)² )
RED = Ra / R0        RED < 1 → disuelve ;  RED ≈ 1 → frontera ;  RED > 1 → no disuelve
```

El truco de las mezclas: los HSP de una mezcla son el **promedio ponderado por fracción volumétrica**.

```
δ_mezcla = Σ ( φ_i × δ_i )   para cada componente D, P y H

EtOH 70 % v/v en agua:
δD = 0,70(15,8) + 0,30(15,5) = 15,71
δP = 0,70(8,8)  + 0,30(16,0) = 10,96
δH = 0,70(19,4) + 0,30(42,3) = 26,27
```

Eso explica algo que en la práctica todos ven y pocos explican: **una mezcla puede ser mejor solvente que
cualquiera de sus componentes puros**, porque cae en una zona del espacio de Hansen que ningún solvente
puro ocupa. Es exactamente el caso del etanol 60–70 % para triterpenos y fenoles de hongos. Ejecuta estos
cálculos en código, nunca de memoria (`Matematicas_lushows`).

## El filtro que va antes de Hansen: se puede usar

Un solvente óptimo que no puedes usar no sirve. El orden real de decisión es:

1. **Legal y de clase ICH.** Clase 1 (benceno, tricloroetileno) prohibidos. Clase 2 (metanol, hexano,
   acetonitrilo) con límite estricto. Clase 3 (etanol, acetona, acetato de etilo) tolerables (`87`).
2. **Alimentario / GRAS** si el producto es ingerible. Etanol, agua, CO2, aceites.
3. **Seguridad de proceso.** Punto de inflamación, clasificación de área, permisos de bomberos.
4. **Costo y recuperación.** ¿Se puede evaporar y reusar? (`149`)
5. **Recién ahí, Hansen** para elegir entre los que quedaron.

## Cómo se comprueba

| Pregunta | Método | Unidad / criterio |
|---|---|---|
| ¿Los HSP de mi extracto? | Ensayo de solubilidad en 12–20 solventes + ajuste de esfera | δD, δP, δH y R0 en MPa^0,5 |
| ¿Cuál mezcla rinde más? | DoE de mezclas (simplex-lattice), respuesta = mg activo/g biomasa | Superficie de respuesta (`287`) |
| ¿Queda solvente en el producto? | GC headspace | ppm vs límite ICH Q3C (`87`) |
| ¿Se degradó el activo con ese solvente? | HPLC antes/después + balance de masa | % recuperación (`06`, `74`) |
| ¿Cambió el perfil, no solo el rendimiento? | HPLC-DAD comparativo de huella | Áreas relativas (`104`) |

## Ejemplo aplicado

BIO-SETA quiere maximizar triterpenos ganodéricos sin salirse de solventes Clase 3. DoE de mezclas
EtOH/agua sobre el mismo lote, 1:15, 60 °C, 2 h **(ILUSTRATIVO)**:

```
EtOH (% v/v)   δP mezcla   δH mezcla   Triterpenos (mg/g biomasa b.s.)   Extracto seco (%)
   0            16,00        42,30              0,08                       18,4
  30            13,84        35,43              3,10                       15,9
  50            12,40        30,85              9,60                       12,7
  70            10,96        26,27             12,40                        9,8
  96             9,09        20,32             10,10                        6,4
```

El máximo cae en ~70 % v/v, justo donde δP y δH de la mezcla se acercan más a los del ácido ganodérico.
Hansen predijo el óptimo antes de correr los 5 puntos; el DoE lo confirmó. Decisión: etanol 70 % para la
fracción alcohólica de la extracción dual, agua 95 °C para la acuosa, y declarar ambos activos con su
método en la especificación (`247`).

## Errores comunes

- Elegir solvente por lo que hace el vecino. El óptimo depende de tu activo, no del rubro.
- Optimizar rendimiento de **masa** en vez de rendimiento de **activo**. El agua saca más sólidos y casi
  ningún triterpeno; parece mejor y es peor.
- Usar metanol o hexano en producción porque funcionó en el laboratorio. Son Clase 2: te obligan a
  demostrar residuales y te complican el registro (`87`, `269`).
- Tratar los HSP calculados por contribución de grupos como si fueran medidos. Son estimación; márcalo.
- Olvidar la temperatura. Los HSP cambian con T y la solubilidad casi siempre sube con calor — pero
  también sube la degradación.
- No medir solvente residual porque "es solo etanol". Etanol también tiene límite y también se declara.

## Conexión con otros módulos

→ `19-soluciones-y-solubilidad.md` — el fenómeno que este módulo cuantifica.
→ `30-extraccion-liquido-liquido-y-logp.md` — repartir entre dos fases inmiscibles.
→ `63-quimica-verde-y-solventes.md` — criterios de sostenibilidad y sustitución.
→ `87-solventes-residuales.md` — clases ICH Q3C y cómo se miden.
→ `148-co2-supercritico.md` — el solvente cuya polaridad se ajusta con presión.
→ `287-diseno-de-experimentos-doe.md` — cómo correr el DoE de mezclas bien.