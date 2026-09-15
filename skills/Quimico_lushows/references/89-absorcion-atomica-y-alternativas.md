# 89 — Absorción atómica y alternativas: cuándo el laboratorio barato alcanza y cuándo te miente

No todos los laboratorios tienen ICP-MS. En Colombia, buena parte de los laboratorios pequeños y
universitarios trabaja con absorción atómica, y su cotización va a ser mucho más barata. La pregunta no es
si la técnica es "buena" —lo es, y lleva 70 años funcionando— sino si **su límite de cuantificación alcanza
tu límite regulatorio en tu matriz**. Ese es el criterio único. Un resultado de "< 1 mg/kg" no te sirve de
nada si tu especificación dice "≤ 0,3 mg/kg": no probaste nada y pagaste igual.

Términos:
- **AAS (atomic absorption spectroscopy)** = se atomiza la muestra y se mide cuánta luz de una lámpara
  específica del elemento absorbe.
- **FAAS (flame AAS)** = atomización en llama aire-acetileno. Rápida, barata, poco sensible.
- **GFAAS / ETAAS (graphite furnace / electrothermal)** = atomización en un tubo de grafito calentado.
  Mucho más sensible.
- **CVAAS (cold vapor)** = mercurio reducido a vapor atómico a temperatura ambiente.
- **HGAAS (hydride generation)** = As, Se, Sb convertidos en hidruros volátiles.
- **Lámpara de cátodo hueco (hollow cathode lamp, HCL)** = fuente de luz específica de cada elemento.
- **Corrección de fondo (background correction)** = Zeeman o lámpara de deuterio; sin ella, la matriz infla
  el resultado.

## Cómo funciona y por qué es de un elemento a la vez

```
   [ LAMPARA del elemento ] --> [ ATOMIZADOR ] --> [ MONOCROMADOR ] --> [ DETECTOR ]
     emite la linea exacta       llama o horno       aisla la linea       mide absorbancia
     del elemento (Pb 283,3 nm)  de grafito

La lampara es especifica: para plomo se usa lampara de plomo. Para medir
cadmio hay que CAMBIAR la lampara y volver a correr. De ahi la diferencia
economica y de tiempo con ICP-MS, que ve 60 elementos en una sola inyeccion
de 2 minutos.

Se aplica Beer-Lambert igual que en UV (80): A = e*b*c. Con las mismas
consecuencias: rango lineal corto (tipicamente 1-2 ordenes de magnitud) y
saturacion si la muestra esta concentrada.
```

## Comparativa honesta de técnicas elementales

| Técnica | LOQ típico en matriz vegetal (mg/kg, ILUSTRATIVO) | Elementos por corrida | Costo por muestra (ILUSTRATIVO) | Veredicto |
|---|---|---|---|---|
| **ICP-MS** | 0,003–0,02 | 20–60 | COP 200.000–600.000 (panel) | El estándar. Pide esto (`88`) |
| **ICP-OES** | 0,05–0,5 | 20–60 | COP 150.000–400.000 (panel) | Sirve para límites altos; **no** para Cd/Pb bajos |
| **GFAAS** | 0,005–0,05 | 1 | COP 80.000–200.000 **por elemento** | Muy sensible; lenta. 4 elementos = 4 corridas |
| **FAAS** | 0,5–5 | 1 | COP 50.000–120.000 por elemento | Solo para elementos mayores (Ca, Mg, Fe, Zn). **Insuficiente para los cuatro grandes** |
| **CVAAS / DMA** | 0,001–0,01 (Hg) | 1 | COP 100.000–250.000 | Excelente para mercurio |
| **HGAAS** | 0,005–0,02 (As, Se) | 1 | COP 100.000–250.000 | Buena para arsénico total |
| **XRF portátil** | 5–50 | Varios | Bajo, no destructivo | **Screening**, no cumplimiento. LOD demasiado alto |

Cómo se usa esta tabla en la vida real:

```
Tu especificacion (derivada de USP <232>, dosis 2 g/dia): Cd <= 2,5 mg/kg.
   -> GFAAS con LOQ 0,02 mg/kg: SIRVE de sobra.
   -> FAAS con LOQ 2 mg/kg: NO SIRVE. Tu limite y su LOQ son casi el mismo
      numero; no puedes demostrar cumplimiento con confianza.

Quieres exportar a la UE como alimento: Cd <= 0,050 mg/kg peso fresco en
setas cultivadas (a agosto de 2026, Reg. 2023/915 — verificar vigencia).
   -> ICP-OES con LOQ 0,1 mg/kg: NO SIRVE. El LOQ esta POR ENCIMA del limite.
   -> GFAAS (LOQ 0,01) o ICP-MS (LOQ 0,005): SIRVEN.

REGLA PRACTICA: el LOQ del metodo debe ser como maximo 1/5 del limite,
idealmente 1/10. Si el laboratorio te ofrece un LOQ que es la mitad de tu
limite, el resultado no aguanta una discusion (73, 76).
```

Ese cálculo de "¿el LOQ alcanza?" es la única pregunta técnica que necesitas hacer para elegir entre una
cotización de COP 150.000 y una de COP 500.000. Todo lo demás es ruido comercial.

## Las trampas específicas de AAS

| Interferencia | Qué pasa | Cómo se controla |
|---|---|---|
| **Química** | El analito forma compuestos refractarios (fosfatos con Ca) y no se atomiza | Agente liberador (La, Sr), llama más caliente (óxido nitroso-acetileno) |
| **Ionización** | El átomo se ioniza y deja de absorber (Na, K) | Supresor de ionización (Cs, K en exceso) |
| **De fondo (background)** | Humo y partículas de la matriz absorben/dispersan luz → **resultado inflado** | **Corrección Zeeman** (la buena) o lámpara de deuterio |
| **De matriz en horno** | El analito se pierde en la etapa de calcinación | **Modificador de matriz** (Pd/Mg(NO₃)₂ para Cd y Pb) |
| **Memoria (carryover)** | Mercurio adherido al sistema | Enjuagues con oro/HCl; blancos intercalados |

Pregunta concreta que separa un GFAAS bien operado de uno que no: **¿tiene corrección de fondo Zeeman y usa
modificador de matriz?** En matrices vegetales y fúngicas, sin modificador el cadmio se volatiliza durante
la calcinación y el resultado sale bajo; sin corrección Zeeman, el humo de la matriz orgánica se lee como
metal y el resultado sale alto. Los dos errores existen y van en direcciones opuestas.

## Otras técnicas que te van a ofrecer

- **XRF portátil (handheld X-ray fluorescence)**: rápida, no destruye la muestra, sin digestión. Muy útil
  para **triaje** de materias primas y de sustrato (`239`): si el XRF ve plomo, seguro hay problema. Pero su
  LOD de decenas de mg/kg la descalifica para demostrar cumplimiento. Nunca la aceptes como COA.
- **Electroquímica (voltamperometría de redisolución anódica, ASV)**: barata y sorprendentemente sensible
  para Pb, Cd, Cu, Zn. Se usa en laboratorios de agua. Poco frecuente en suplementos y con más problemas de
  matriz.
- **Analizador directo de mercurio (DMA-80 y similares)**: descompone térmicamente la muestra sólida y
  amalgama el Hg en oro. **Sin digestión, sin ácidos, 5 minutos por muestra.** Si solo necesitas mercurio,
  es la mejor relación costo/calidad.
- **Kits colorimétricos de "metales pesados"**: no. No dan valores defendibles ni distinguen elementos.

## Ejemplo aplicado — elegir laboratorio para un lote de chaga

```
Contexto: chaga silvestre importada. Riesgos conocidos: metales, oxalato y
radiocesio (230). Producto: polvo, dosis declarada 3 g/dia.

Limites derivados de USP <232> (ILUSTRATIVO):
   Cd 5/3 = 1,67 mg/kg | Pb 5/3 = 1,67 | As 15/3 = 5,0 | Hg 30/3 = 10,0

Cotizaciones recibidas (ILUSTRATIVO):
  Lab A — ICP-MS, panel de 4, digestion microondas, ISO 17025 en alcance
          para producto vegetal.  LOQ: Cd 0,005 | Pb 0,01 | As 0,01 | Hg 0,005
          COP 420.000, 7 dias habiles.
  Lab B — FAAS para Cd y Pb + HGAAS para As + CVAAS para Hg.
          LOQ: Cd 1,0 | Pb 2,0 | As 0,05 | Hg 0,005
          COP 260.000, 12 dias habiles.

Decision: Lab A. El LOQ de plomo del Lab B (2,0 mg/kg) es MAYOR que tu
limite (1,67 mg/kg): matematicamente no puede demostrar cumplimiento.
Ahorrar COP 160.000 te deja sin evidencia utilizable. El precio no es el
criterio; el LOQ lo es.

Nota aparte: el radiocesio (Cs-137) NO se mide por ninguna de estas tecnicas.
Requiere espectrometria gamma (38, 230). Es un ensayo distinto y otro
proveedor.
```

## Qué preguntarle al laboratorio

1. ¿Qué **técnica exacta** por elemento (FAAS, GFAAS, CVAAS, HGAAS, ICP-OES, ICP-MS)?
2. ¿Cuál es el **LOQ en mi matriz** para cada elemento? (En matriz, no en agua.)
3. ¿Tienen **corrección de fondo Zeeman** y usan **modificador de matriz** en horno de grafito?
4. ¿La **digestión es por microondas** en vaso cerrado? (`88`)
5. ¿Corren **CRM** de matriz similar? ¿Qué recuperación obtuvieron?
6. ¿El ensayo está en su **alcance acreditado ISO 17025** para esta matriz y este elemento? (`107`)
7. Si necesito mercurio solamente: ¿tienen **analizador directo de mercurio**?

## Errores comunes

- **Elegir por precio sin mirar el LOQ.** Es el error que convierte un ahorro de COP 160.000 en un lote sin
  respaldo.
- **Aceptar "< LOQ" como cumplimiento cuando el LOQ está por encima del límite.** No demuestra nada.
- **Usar XRF como COA.** Sirve para tamizar proveedores, no para liberar lote.
- **Comparar resultados de FAAS con ICP-MS** y concluir que un laboratorio "mide mal": están midiendo con
  sensibilidades distintas.
- **Pedir "metales pesados" sin decir cuáles.** Cada elemento es una corrida y un costo en AAS.
- **Olvidar que radiocesio, oxalato y microbiología son ensayos aparte.** "Análisis completo" no existe: se
  arma con una lista (`283`).

## Conexión con otros módulos

→ `88-icp-ms-y-metales-pesados.md` — la técnica de referencia y la digestión.
→ `73-lod-loq-y-rango-lineal.md` — el concepto que decide todo este módulo.
→ `90-espectroscopia-uv-visible.md` — la ley de Beer-Lambert que comparten.
→ `36-quimica-inorganica-y-metales-relevantes.md` — química de los elementos medidos.
→ `38-radiactividad-en-alimentos-y-plantas.md` — el ensayo que ninguna de estas técnicas cubre.
→ `108-como-elegir-un-laboratorio.md` y `114-costos-y-tiempos-de-analisis.md` — el marco de decisión completo.
→ `230-chaga-riesgos-oxalato-y-radiocesio.md` — el caso que reúne varios ensayos distintos.
→ `243-metales-pesados-en-hongos.md` — por qué esto importa tanto en hongos.
