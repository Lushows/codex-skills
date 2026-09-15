# 178 — THCV, CBDV y las varinas: la serie propílica y su propio factor de conversión

Las "varinas" son la familia de cannabinoides con cadena lateral de **tres carbonos (propilo)** en vez de
cinco (pentilo). No son THC ni CBD con otro nombre: son moléculas distintas, con masa molar distinta,
farmacología distinta y —el punto que casi nadie aplica— **un factor de descarboxilación distinto de 0,877**.
Si compras una variedad "alta en THCV" y calculas su conversión con el factor del THC, tu número está mal.
Y si vendes THCV, prepárate: el mercado está lleno de material que en realidad es THCV sintetizado o
mal identificado.

Términos:
- **varina (varin)** = cannabinoide con cadena propílica (C3).
- **THCV (tetrahydrocannabivarin)** = C₁₉H₂₆O₂, **286,41 g/mol**; ácido THCVA, C₂₀H₂₆O₄, **330,42 g/mol**.
- **CBDV (cannabidivarin)** = C₁₉H₂₆O₂, **286,41 g/mol**; ácido CBDVA, C₂₀H₂₆O₄, **330,42 g/mol**.
- **CBGV (cannabigerovarin)** = C₁₉H₂₈O₂, **288,43 g/mol**; ácido CBGVA, C₂₀H₂₈O₄, **332,44 g/mol**.
- **ácido divarínico (divarinic acid)** = el precursor policetídico con cadena C3 (ver `172`).

## De dónde salen: el precursor cambia, no la enzima

En la ruta, si el policétido de partida usa **butanoil-CoA (C4)** en vez de hexanoil-CoA (C6), se forma
ácido divarínico y de ahí **CBGVA**. Las mismas sintasas (THCAS, CBDAS, CBCAS) actúan sobre él y producen
THCVA, CBDVA y CBCVA. Es decir: **la cadena la decide el precursor, no la sintasa**.

Por eso el quimiotipo y el contenido de varinas se heredan por vías distintas. El trabajo de referencia
("Complex Patterns of Cannabinoid Alkyl Side-Chain Inheritance in Cannabis", *Scientific Reports*, 2019)
muestra que la herencia de la longitud de cadena **no es mendeliana simple**: hay patrones digénicos y
epistáticos, y las F2 no segregan como uno esperaría. Consecuencia: seleccionar una línea alta en THCV es
un programa de mejoramiento largo, no un cruce.

Poblaciones con varinas apreciables se han reportado sobre todo en germoplasma de origen africano y de Asia
central; en el material comercial habitual los niveles suelen ser trazas.

## Los factores de conversión — cada serie el suyo

Mismo principio que en `175`: se pierde una molécula de CO₂ (44,009 g/mol) y el factor es el cociente de
masas molares.

| Par ácido → neutro | M(ácido) | M(neutro) | Factor |
|---|---|---|---|
| THCA → Δ9-THC | 358,48 | 314,47 | **0,877** |
| CBDA → CBD | 358,48 | 314,47 | **0,877** |
| **THCVA → THCV** | 330,42 | 286,41 | **0,867** |
| **CBDVA → CBDV** | 330,42 | 286,41 | **0,867** |
| CBGVA → CBGV | 332,44 | 288,43 | **0,868** |

Comprobación de balance: `330,42 − 44,01 = 286,41` ✓

```
THCV total = THCV + 0,867 × THCVA        (NO 0,877)
CBDV total = CBDV + 0,867 × CBDVA
```

La diferencia entre 0,877 y 0,867 parece cosmética (1,1 % relativo) pero es un error sistemático: sesga
todos tus lotes en la misma dirección y aparece en cualquier auditoría de método.

## Farmacología, con nivel de evidencia

- **THCV:** descrito como antagonista/agonista inverso de CB1 a dosis bajas y agonista a dosis altas
  [in vitro / animal]. En humanos se ha reportado que a dosis altas (del orden de 100 mg) puede producir
  efectos subjetivos tipo THC [clínico, exploratorio]. Es un compuesto **dosis-dependiente en dirección
  opuesta**, lo que hace peligroso extrapolar.
- **CBDV:** sin actividad relevante en CB1/CB2 [in vitro]; interés en canales TRP y en investigación clínica
  de neurodesarrollo [clínico fase 2, resultados mixtos].
- No se afirma aquí ningún efecto terapéutico ni se sugiere uso para ninguna enfermedad. Lo que existe es
  investigación, y así se comunica (`12`, `293`).

## Cómo se mide / cómo se comprueba

- **Método:** HPLC/UHPLC-DAD con patrones certificados **propios de cada varina**. THCV y Δ8-THC pueden
  eluir cerca en gradientes cortos; hay que demostrar resolución (`81`).
- **Confirmación estructural obligatoria** cuando el producto se vende por su contenido de THCV: HRMS para
  fórmula elemental (`286,41` vs `314,47` es una diferencia de 28 u, fácil de ver) y RMN si hay duda de
  isomería (`84`, `94`).
- **Reporte:** `% p/p base seca` o `mg/g`, con LOQ explícito. En flor real las varinas suelen estar cerca del
  LOQ, así que el LOQ **es** el dato.
- **Verificación de autenticidad:** un extracto "20 % THCV" de una planta cuyo COA de biomasa muestra
  THCVA < 0,5 % es aritméticamente imposible sin aislamiento o síntesis. Pide balance de masa del proceso
  (`06`, `284`).

Ejecuta las conversiones con `lab-tools/thc_total.py` indicando explícitamente el factor de la serie, o con
`lab-tools/unidades.py` para pasar a `mg/g` y `mg/porción`.

## Ejemplo aplicado

Flor declarada "rica en THCV" (ILUSTRATIVO, HPLC-DAD, `% p/p base seca`):

```
THCVA = 1,84 %      THCV = 0,11 %
THCA  = 12,60 %     Δ9-THC = 0,40 %

THCV total = 0,11 + 0,867 × 1,84 = 0,11 + 1,595 = 1,71 % p/p base seca
THC  total = 0,40 + 0,877 × 12,60 = 0,40 + 11,05 = 11,45 % p/p base seca
```

Dos lecturas honestas:

1. "Rica en THCV" significa **1,7 %**, no 15 %. Es alto para la especie y sigue siendo un componente menor.
2. El material es **cannabis psicoactivo** con 11,45 % de THC total. Cualquier discurso de "THCV sin efecto"
   ignora los 11,45 puntos que van al lado.

Si alguien hubiera usado 0,877: `0,11 + 1,614 = 1,72 %`. Diferencia pequeña, error sistemático real.

## Errores comunes

- Aplicar 0,877 a THCVA/CBDVA. El factor correcto es 0,867.
- Cuantificar THCV contra el patrón de Δ9-THC porque "eluyen parecido". Distinta absortividad, número mal.
- Vender "THCV" sin confirmación por masas: es el analito más falsificado del catálogo de menores.
- Prometer un efecto opuesto al THC sin decir que depende de la dosis y que la evidencia humana es
  exploratoria.
- Ignorar el THC total del mismo material cuando se promociona la varina.
- Creer que un cruce con una línea alta en THCV dará descendencia alta en THCV. La herencia no es simple.

## Conexión con otros módulos

→ `172-biosintesis-de-cannabinoides.md` — por qué la cadena cambia.
→ `171-genetica-y-variedades.md` — la herencia de la cadena alquílica.
→ `175-thc-total-y-el-factor-0877.md` — el método de cálculo, con la serie pentilo.
→ `179-thcp-cbdp-y-homologos.md` — el otro extremo: cadenas más largas.
→ `193-cromatografia-preparativa-y-aislados.md` — cómo se concentran menores de verdad.
→ `84-hrms-qtof-orbitrap-e-identificacion.md` — cómo confirmar que es lo que dice ser.