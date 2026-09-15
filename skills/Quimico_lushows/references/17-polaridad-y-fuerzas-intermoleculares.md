# 17 — Polaridad y fuerzas intermoleculares (la regla que decide agua o etanol)

Esta es, en la práctica, la física de tu extracción. Cuando alguien pregunta "¿por qué el agua saca los
beta-glucanos y el alcohol saca los triterpenos?", la respuesta no es tradición ni misticismo: es
polaridad. Cada molécula tiene una distribución de carga y una capacidad de hacer puentes de hidrógeno, y
el solvente que se le parece la disuelve. Entender esto te ahorra meses de ensayo y error, te permite
discutir de igual a igual con un maquilador y te evita el error caro más común del rubro: hacer una
tintura alcohólica y venderla diciendo que aporta beta-glucanos.

Términos: **momento dipolar (dipole moment)** = separación de carga dentro de una molécula, en debye (D).
**puente de hidrógeno (hydrogen bond)** = atracción fuerte entre un H unido a O/N/F y un par libre de otro
O/N/F. **fuerzas de dispersión de London (London dispersion forces)** = atracción entre dipolos
instantáneos; crecen con el tamaño y la superficie. **lipofilicidad (lipophilicity)** = afinidad por
grasas; se cuantifica como logP (`30`). **constante dieléctrica (dielectric constant, ε)** = cuánto apantalla
cargas un solvente; agua 80,1, etanol 24,5, hexano 1,9 a 20 °C.

## La escala de solventes que de verdad usas

| Solvente | ε (20 °C) | Índice de polaridad (Snyder) | Puentes H | Qué saca preferentemente |
|---|---|---|---|---|
| Agua | 80,1 | 10,2 | Dona y acepta | Polisacáridos, β-glucanos, sales, aminoácidos, ergotioneína |
| Etanol 96 % | 24,5 | 5,2 | Dona y acepta | Triterpenos, fenoles, alcaloides, algo de glucano bajo PM |
| Etanol 40–60 % (hidroalcohol) | ~50–60 | intermedio | Sí | Ventana amplia: fenoles + parte polar |
| Metanol | 32,7 | 5,1 | Dona y acepta | Analítico: psilocibina, cannabinoides ácidos |
| Acetonitrilo | 37,5 | 5,8 | Solo acepta | Fase móvil de HPLC (`81`) |
| Acetato de etilo | 6,0 | 4,4 | Solo acepta | Partición de terpenoides |
| Hexano | 1,9 | 0,1 | No | Ceras, lípidos, cannabinoides neutros |
| CO2 supercrítico | ~1,1–1,6 (ajustable) | variable con presión | No (sin cosolvente) | Aceites, cannabinoides, terpenos (`148`) |

Leer la tabla al revés también sirve: si tu activo no sale, no cambies de proveedor — cambia de solvente.

## Las cuatro fuerzas, de fuerte a débil

```
Ion–dipolo        40–600 kJ/mol   sal en agua; por qué el KCl se disuelve y el aceite no
Puente de H        10–40 kJ/mol   glucano–agua; celulosa–celulosa; por qué el azúcar es sólido a 25 °C
Dipolo–dipolo       5–25 kJ/mol   acetona, ésteres
Dispersión London    1–10 kJ/mol   cada contacto; en una molécula grande suman MUCHO
```

La dispersión es la fuerza olvidada. El Δ9-THC (C21H30O2, 314,5 g/mol) casi no tiene polaridad neta pero
tiene una superficie enorme de hidrocarburo: por eso se disuelve espectacularmente en aceite y casi nada
en agua (solubilidad acuosa reportada en el orden de µg/mL). Ahí nace toda la tecnología de emulsiones y
nanoemulsiones de CBD (`33`, `157`).

## El caso central: extracción dual de hongos

| Fracción | Molécula representativa | Rasgo estructural | Solvente que la saca |
|---|---|---|---|
| Polisacárida | β-1,3/1,6-glucano | Decenas de –OH por unidad; polímero grande | Agua caliente (decocción, 80–100 °C) |
| Triterpénica | Ácidos ganodéricos (reishi) | Esqueleto C30 lanostano, poco polar, con –COOH | Etanol 60–96 % |
| Aminoácido raro | Ergotioneína | Zwitterión (carga + y − a la vez) | Agua |
| Nucleósidos | Adenosina, cordicepina | Polares, con N | Agua o hidroalcohol suave |
| Esteroles | Ergosterol | Casi apolar | Etanol fuerte o hexano |

El agua caliente hace dos cosas: rompe la pared celular por hidrólisis parcial y solvata los –OH del
glucano con puentes de hidrógeno. El etanol no puede solvatar un polímero con cientos de hidroxilos —de
hecho lo precipita, y eso es precisamente lo que se usa para recuperarlo (precipitación etanólica). Por eso
una tintura de reishi al 70 % de etanol tiene triterpenos y prácticamente no tiene beta-glucanos, y una
decocción tiene lo contrario. La extracción dual (`146`) existe porque ninguna sola sirve.

## Cómo se comprueba

No adivines la polaridad: mídela o infiérela con método.

| Pregunta | Cómo | Unidad / criterio |
|---|---|---|
| ¿Qué tan lipofílico es mi activo? | logP experimental (shake-flask) o calculado | logP adimensional; >3 = lipofílico (`30`) |
| ¿Mi extracto acuoso sí trae glucano? | Megazyme K-YBGL sobre el extracto seco | % p/p base seca (`221`) |
| ¿Mi tintura sí trae triterpenos? | HPLC-UV a ~245–252 nm vs patrón de ácido ganodérico A | mg/g de extracto (`224`) |
| ¿Cuál solvente rinde más? | Diseño de experimentos con 3–5 mezclas EtOH/agua | mg activo/g biomasa (`287`) |
| ¿Qué tan polar es mi mezcla? | Índice de polaridad ponderado por fracción volumétrica | Escala Snyder |

## Ejemplo aplicado

BIO-SETA quiere un solo producto de reishi que "traiga todo". Se corre una prueba de tres extracciones
sobre el mismo lote de cuerpo fructífero molido **(ILUSTRATIVO)**:

```
A) Agua 95 °C, 2 h, 1:20      → sólidos 18 % ; β-glucano 24,1 % p/p b.s. ; triterpenos 0,4 mg/g
B) EtOH 70 %, 25 °C, 24 h     → sólidos 9 %  ; β-glucano  2,3 % p/p b.s. ; triterpenos 11,2 mg/g
C) Dual: A + B, combinado seco → sólidos 27 % ; β-glucano 16,8 % p/p b.s. ; triterpenos 7,1 mg/g
```

Lectura: C no es la suma, es el promedio ponderado — al mezclar diluyes ambos activos. Si tu claim de
etiqueta es beta-glucanos, C te deja por debajo del 20 % y tendrás que subir la dosis por cápsula. Si tu
claim es "espectro completo", C es honesto pero debe declarar ambos números con su método. Decidir esto
sin medir es cómo nacen las etiquetas que no se pueden sostener (`242`, `268`).

## Errores comunes

- Vender una tintura alcohólica de hongo con claim de beta-glucanos. Físicamente el etanol los precipita:
  el número no va a estar ahí y un COA honesto te desmiente.
- Creer que "más alcohol = más fuerte". Más alcohol = más selectivo hacia lo apolar, y menos rendimiento
  total de masa.
- Usar "extracto 10:1" como si dijera algo de la polaridad o del activo. El ratio es masa (`151`, `242`).
- Formular CBD en una bebida acuosa sin tensioactivo y esperar que no se separe. Sin emulsión, la
  dispersión de London gana y el aceite sube (`33`, `157`).
- Ignorar que el agua caliente prolongada también degrada: la psilocibina y algunos fenoles no aguantan
  horas a 95 °C (`26`, `255`).
- Cambiar de solvente en producción sin repetir el análisis. Cambió la matriz: el método analítico puede
  necesitar revalidación (`75`).

## Conexión con otros módulos

→ `19-soluciones-y-solubilidad.md` — "lo semejante disuelve a lo semejante", con números.
→ `20-parametros-de-solubilidad-y-eleccion-de-solvente.md` — Hansen y cómo elegir sin adivinar.
→ `30-extraccion-liquido-liquido-y-logp.md` — partición y por qué los cannabinoides son lipofílicos.
→ `146-extraccion-dual-y-por-que-importa.md` — el proceso completo aplicado a hongos.
→ `241-extraccion-de-hongos-agua-vs-alcohol.md` — el caso específico, con rendimientos.
→ `33-tensioactivos-y-hlb.md` — cuando necesitas que lo apolar viva en agua.