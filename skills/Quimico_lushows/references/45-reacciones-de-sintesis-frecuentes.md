# 45 — Reacciones de síntesis frecuentes (las que sí vas a ver en un proceso real)

No vas a montar un laboratorio de síntesis total, pero sí vas a comprar materias primas hechas por síntesis,
vas a leer procesos de maquiladores, vas a decidir si un ingrediente "semisintético" te sirve, y vas a
necesitar entender qué subproductos trae. Este módulo cubre las reacciones que aparecen de verdad en el
mundo de productos naturales, ingredientes y análisis: descarboxilación, esterificación, reducción,
oxidación controlada, ciclación, glicosilación e hidrogenación. Es descripción química, no protocolo de
producción: para sustancias controladas la línea roja de la skill se mantiene (`SKILL.md`).

Términos: **rendimiento (yield)** = producto obtenido / producto teórico, en %. **Economía atómica (atom
economy)** = masa del producto deseado / masa total de reactivos, en %. **Selectividad (selectivity)** =
proporción del producto deseado frente a los demás. **Reactivo limitante (limiting reagent)** = el que se
acaba primero y fija el máximo teórico. **Work-up** = el trabajo de aislar el producto después de la reacción.

## Las tres cuentas que se hacen antes de tocar nada

```
1) Reactivo limitante:  n = m / M      (mol = gramos / masa molar en g/mol)
   El que tenga menos moles ajustados por la estequiometría manda (`06`).

2) Rendimiento teórico: m_teo = n_limitante × coef × M_producto
   Rendimiento real (%) = m_obtenida / m_teo × 100

3) Economía atómica (%) = M_producto_deseado / Σ M_reactivos × 100
   → Un rendimiento alto con economía atómica baja sigue generando montañas de residuo (`63`).

Ejecutar SIEMPRE en código (`lab-tools/`, o rutear a `Matematicas_lushows`). Aritmética mental: prohibida.
```

## Catálogo de reacciones que sí te vas a encontrar

| Reacción | Transformación | Condiciones típicas | Dónde aparece |
|---|---|---|---|
| **Descarboxilación** | R-COOH → R-H + CO₂ | Calor seco, 100–140 °C | THCA→THC, CBDA→CBD (`174`) |
| **Esterificación de Fischer** | Ácido + alcohol → éster + H₂O | H⁺ cat., reflujo, quitar agua | FAME para GC (`64`), aromas |
| **Transesterificación** | Éster + alcohol' → éster' + alcohol | Base o ácido cat. | Perfil de ácidos grasos (`53`) |
| **Saponificación** | Éster + OH⁻ → carboxilato + alcohol | NaOH/KOH acuoso o metanólico, calor | Liberar esteroles del aceite (`46`, `55`) |
| **Oxidación de alcohol** | R-CH₂OH → aldehído → ácido | Oxidante suave o fuerte | Degradación de activos (`47`) |
| **Reducción de carbonilo** | Cetona → alcohol | NaBH₄, LiAlH₄, H₂/cat. | Semisíntesis |
| **Hidrogenación de C=C** | Alqueno → alcano | H₂ + Pd/C o Pt | **THC → HHC** (`181`); grasas |
| **Adición electrofílica / ciclación** | C=C + H⁺ → carbocatión → anillo | Ácido de Lewis, solvente apolar | **CBD → Δ8-THC** (`180`) |
| **Sililación** | R-OH → R-O-Si(CH₃)₃ | BSTFA/MSTFA + TMCS, 60–70 °C | Derivatización para GC (`64`) |
| **Glicosilación / hidrólisis glicosídica** | Azúcar-O-R ⇄ azúcar + R-OH | Enzima o ácido, calor | Liberar agliconas de flavonoides (`51`) |
| **Aminación reductiva** | Cetona + amina → amina secundaria | NaBH₃CN | Química de triptaminas (solo contexto teórico) |

## Tres casos que importan de verdad a tu producto

**1. Hidrogenación: THC → HHC.** Adición de H₂ al doble enlace del anillo. Elimina el doble enlace, y con
él la fotolabilidad y el camino a CBN: el HHC es más estable al aire y a la luz. Pero el carbono 9 se
convierte en un centro estereogénico nuevo, y el proceso genera **una mezcla de epímeros 9*R* y 9*S*** con
potencias reportadas muy distintas [in vitro/animal]. Consecuencia comercial: un COA de HHC que solo diga
"HHC 92 %" sin la relación 9R:9S no describe el producto (`43`, `181`).

**2. Ciclación ácida: CBD → Δ8-THC.** Ya está el mecanismo en `44`. Lo que agrega este módulo es la parte
de proceso: si el ácido usado contiene cloruro (HCl, ácido *p*-toluensulfónico con trazas), pueden formarse
**cannabinoides clorados**, que no tienen datos toxicológicos y que ningún panel estándar busca. Exigencia
mínima al proveedor: identificación del catalizador usado y un barrido HRMS de impurezas (`84`, `180`).

**3. Saponificación previa al análisis de esteroles.** Para medir ergosterol en hongo hay que romper primero
los ésteres de esterol; si no, subestimas. Es una reacción de preparación de muestra, no de producción, y es
la diferencia entre un dato correcto y uno bajo por defecto (`46`, `238`).

## Cómo se comprueba que una reacción salió como debía

| Control | Técnica | Criterio |
|---|---|---|
| ¿Se consumió el reactivo? | TLC/HPTLC en el tiempo | Desaparece la mancha del reactivo (`96`) |
| ¿Se formó lo que quería? | HPLC-DAD / GC-MS con patrón | Tiempo de retención + espectro coinciden |
| ¿Cuál es la pureza? | HPLC área normalizada + qNMR | qNMR da % p/p absoluto sin patrón idéntico (`95`) |
| ¿Qué impurezas hay? | HRMS (barrido no dirigido) | Fórmulas con error < 5 ppm (`84`) |
| ¿Quedó solvente? | GC headspace | Contra límites ICH Q3C (`87`) |
| ¿Quedó catalizador metálico? | ICP-MS | Contra límites ICH Q3D (`88`) |
| ¿Estereoquímica? | HPLC quiral / RMN | ee o relación de epímeros (`43`) |

Regla: **una reacción no está "buena" porque el rendimiento sea alto. Está buena cuando el perfil de
impurezas está caracterizado y bajo especificación.**

## Ejemplo aplicado — evaluar una cotización de "distillate HHC 95 %"

```
Cotización (ILUSTRATIVO): HHC 95 % p/p, USD X/kg, "COA incluido".
COA recibido: un cromatograma HPLC-DAD, un pico grande, "HHC 95,3 %".

Lo que falta y hay que exigir antes de comprar:
  1. Relación 9R:9S            → HPLC con método que resuelva epímeros. Sin esto no sabes qué compras.
  2. Δ9-THC residual           → % p/p; define legalidad del producto final (`175`, `211`).
  3. Catalizador metálico      → Pd o Pt residual por ICP-MS, en ppm, contra ICH Q3D.
  4. Solventes residuales      → GC-headspace contra ICH Q3C clase 1/2/3 (`87`).
  5. Impurezas desconocidas    → barrido HRMS; ¿algún pico > 0,10 % sin identificar?
  6. Trazabilidad del patrón   → ¿con qué patrón cuantificaron el HHC? ¿existe uno certificado?

Sin los seis puntos, "95 %" es un número de folleto (`111`).
```

## Errores comunes

- Evaluar un proceso solo por rendimiento. El costo real está en el work-up, el residuo y las impurezas (`63`).
- Aceptar "grado técnico" cuando el destino es consumo humano: el grado define el perfil de impurezas.
- No pedir el análisis de catalizador metálico en productos hidrogenados. Pd y Pt son los que faltan siempre.
- Confundir pureza cromatográfica por área (%) con pureza másica (% p/p). El detector responde distinto a
  cada compuesto; solo qNMR o un patrón certificado dan masa real (`95`).
- Suponer que "semisintético" significa "natural". Regulatoriamente suele ser lo contrario (`181`, `275`).
- Escalar una reacción multiplicando todo por 10 sin revisar transferencia de calor: reacciones exotérmicas
  se comportan distinto en volumen (`166`).

## Conexión con otros módulos

→ `44-mecanismos-de-reaccion-basicos.md` — el porqué de cada transformación.
→ `46-hidrolisis-esterificacion-y-saponificacion.md` — la familia del carbonilo, en detalle.
→ `63-quimica-verde-y-solventes.md` — economía atómica, factor E y elección de solvente.
→ `181-hhc-thco-y-semisinteticos.md` — el caso completo de los semisintéticos.
→ `06-estequiometria-y-balance-de-masa.md` — cómo se hacen las cuentas sin equivocarse.