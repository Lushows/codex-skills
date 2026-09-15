# 15 — Átomo y tabla periódica (por qué el cadmio se pega al hongo y el potasio no)

Todo lo que discutes con un laboratorio —por qué el ICP-MS mide cadmio y no beta-glucanos, por qué el
carbono forma esqueletos y el mercurio se acumula, por qué el potasio-40 aparece en cualquier planta— se
explica desde la estructura del átomo. No necesitas resolver ecuaciones de orbitales: necesitas saber leer
la tabla periódica como un mapa de comportamiento. Ese mapa te dice qué elemento va a contaminar tu
producto, cuál va a ser tu analito y cuál va a ser tu interferencia en el instrumento. El error caro es
tratar "metales pesados" como una categoría única: Cd, Pb, As y Hg se comportan distinto en la planta, en
el hongo, en la digestión de muestra y en el plasma del ICP-MS.

Términos: **número atómico (atomic number, Z)** = cantidad de protones; define al elemento. **isótopo
(isotope)** = mismo Z, distinta cantidad de neutrones; misma química, distinta masa y a veces
radiactividad. **electronegatividad (electronegativity)** = cuánto jala un átomo los electrones del
enlace; base de la polaridad. **masa molar (molar mass)** = gramos por mol, en g/mol; es la que convierte
mg de analito en moles. **metal de transición (transition metal)** = bloque d, forma complejos con
azufre, nitrógeno y oxígeno — por eso se pega a proteínas y a la pared del hongo.

## El mapa: qué te dice cada zona de la tabla

| Zona | Elementos típicos | Qué significa para tu producto |
|---|---|---|
| Bloque s, grupos 1–2 | H, Na, K, Ca, Mg | Cationes de sales y buffers; K-40 aporta radiactividad natural |
| Bloque p, no metales | C, N, O, S, P | El esqueleto de todo compuesto orgánico que analizas |
| Halógenos | F, Cl, Br, I | Cl del HCl de digestión; interferencias poliatómicas en ICP-MS |
| Bloque d (transición) | Fe, Cu, Zn, Cd, Hg | Catalizan oxidación y se acumulan en biomasa fúngica |
| Bloque p pesado | Pb, As (metaloide), Sn | Contaminantes regulados; As pide especiación |
| Lantánidos | Ce, La | Trazadores de suelo y de adulteración con tierra |
| Gases nobles | He, Ar | Ar es el plasma del ICP-MS; He el gas portador de GC |

La periodicidad no es folclore: el cadmio está justo debajo del zinc, tiene química parecida, y por eso
los transportadores biológicos de Zn del micelio lo dejan entrar. Eso explica, en una línea, por qué los
hongos concentran Cd más que la mayoría de las plantas.

## Isótopos: lo que hace posible el LC-MS y lo que enciende alarmas

Cada elemento existe como mezcla de isótopos con abundancia natural conocida.

```
Cl natural  = 35Cl (75,8 %) + 37Cl (24,2 %)  → patrón M / M+2 característico en MS
C natural   = 12C (98,9 %) + 13C (1,1 %)     → base del pico M+1 proporcional al nº de carbonos
K natural   = 39K, 41K estables + 40K radiactivo (~0,012 %) → radiactividad natural de toda planta
Cs-137      = NO natural; solo de origen artificial (accidentes/ensayos nucleares)
```

Tres consecuencias prácticas:
1. El patrón isotópico confirma identidad en HRMS (ver `84`).
2. Los isótopos estables se usan como estándar interno (`72`): cafeína-d3, THC-d3, psilocina-d4.
3. La distinción K-40 (natural, inevitable) vs Cs-137 (artificial, señal de depósito) es toda la
   discusión de radiocesio en chaga (`38`).

## Enlaces y valencia — la regla que gobierna a los productos naturales

| Átomo | Enlaces típicos | Dónde lo ves |
|---|---|---|
| C | 4 | Esqueleto de cannabinoides, terpenos, glucanos |
| O | 2 | Hidroxilos, éteres, ácidos carboxílicos (THCA) |
| N | 3 | Alcaloides: psilocibina, cordicepina, ergotioneína |
| P | 5 | Éster fosfato de la psilocibina (el que la hace polar) |
| S | 2 | Ergotioneína (tiol/tiona), cisteína, metionina |

La psilocibina es un buen ejemplo del poder de un solo átomo: quítale el fosfato y tienes psilocina, mucho
menos polar y mucho menos estable en solución. Un átomo cambia la cromatografía, la estabilidad y la
farmacocinética (`251`, `255`).

## Cómo se mide

Elementos = espectrometría atómica; moléculas = cromatografía + detector.

| Pregunta | Técnica | Unidad típica | Orden de magnitud esperado |
|---|---|---|---|
| ¿Cuánto Cd/Pb/As/Hg hay? | ICP-MS tras digestión ácida | mg/kg (ppm) o µg/kg (ppb) | trazas; ver límites en `243` |
| ¿Qué elementos hay en general? | ICP-OES / barrido semicuantitativo | mg/kg | screening, no cuantificación fina |
| ¿Es As inorgánico o arsenobetaína? | HPLC-ICP-MS (especiación) | µg/kg por especie | la toxicidad depende de la especie |
| ¿Cuánta ceniza total (minerales)? | Gravimetría, mufla 550 °C | % p/p base seca | hongos: reportado alto por el K |
| ¿Hay radionucleidos? | Espectrometría gamma HPGe | Bq/kg | ver `38` |

Regla dura: sin digestión completa (microondas con HNO3/H2O2) el ICP-MS subestima. Si el COA no dice cómo
digirió la muestra, el número de metales no es auditable (`88`, `110`).

## Ejemplo aplicado

Un proveedor te ofrece polvo de *Ganoderma lucidum* y su COA dice "metales pesados: conforme". Tú pides el
detalle y llega esto **(ILUSTRATIVO)**:

```
Cd  0,42 mg/kg   ICP-MS, digestión microondas HNO3/H2O2, base seca
Pb  0,18 mg/kg   ICP-MS, mismo método
As  0,25 mg/kg   ICP-MS, total (sin especiación)
Hg  0,03 mg/kg   ICP-MS con oro como estabilizante
Humedad 8,1 %    Karl Fischer
```

Lectura de químico: (a) el Cd es el que manda, coherente con la afinidad Zn/Cd del bloque d; (b) el As
está reportado como total, así que no sabes cuánto es inorgánico — pídelo especiado si vas a exportar;
(c) todo está en base seca, así que es comparable con otro COA solo si el otro también lo está (`07`);
(d) el Hg necesita estabilizante en la solución o se pierde en el vial: si no lo dice, sospecha.

Cálculo de exposición: si una porción diaria es 2 g de polvo, el Cd aportado es
`0,42 mg/kg × 0,002 kg = 0,00084 mg/día = 0,84 µg/día` **(ILUSTRATIVO)**. Ese número, no el "conforme", es
lo que se compara contra el límite de ingesta (`135`, `136`). Ejecuta la cuenta en código, no de memoria
(`Matematicas_lushows`).

## Errores comunes

- Tratar "metales pesados" como un solo parámetro. Cd, Pb, As y Hg tienen fuentes, límites y métodos
  distintos; un "conforme" agregado esconde justo el que te va a rebotar en aduana.
- Comparar un metal en base húmeda contra un límite en base seca. Con 8 % de humedad el error es ~8 %; con
  hongo fresco, 10 veces.
- Creer que "arsénico total alto" es automáticamente peligroso sin pedir especiación.
- Pedir "análisis de minerales" cuando lo que necesitabas era ceniza total, o al revés: son preguntas
  distintas y cuestan distinto (`114`).
- Confundir radiactividad natural (K-40, en todo alimento) con contaminación (Cs-137). Es un error que
  arruina la comunicación de una marca (`38`, `293`).
- Suponer que el laboratorio digirió bien la muestra. Sin el método de digestión escrito, el número no es
  defendible ante INVIMA ni ante un cliente (`110`, `111`).

## Conexión con otros módulos

→ `16-enlace-quimico-y-geometria.md` — cómo esos átomos se unen y qué forma resulta.
→ `36-quimica-inorganica-y-metales-relevantes.md` — el capítulo completo de metales que importan.
→ `38-radiactividad-en-alimentos-y-plantas.md` — K-40 vs Cs-137, chaga y hongos silvestres.
→ `88-icp-ms-y-metales-pesados.md` — la técnica con la que se miden de verdad.
→ `243-metales-pesados-en-hongos.md` — por qué el hongo concentra Cd y qué límite aplica.
→ `04-unidades-concentraciones-y-conversiones.md` — mg/kg, ppm, ppb sin equivocarse.