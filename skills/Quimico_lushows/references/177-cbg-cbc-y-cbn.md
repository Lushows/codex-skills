# 177 — CBG, CBC y CBN: los tres menores que sí vas a ver en tu COA

Estos tres aparecen en casi cualquier análisis de cannabis y se venden como "el próximo CBD". Dos de ellos
(CBG y CBC) son productos legítimos de la ruta biosintética; el tercero (CBN) **no lo es**: es lo que queda
cuando el THC se oxida. Confundirlos cuesta plata en dos direcciones: pagar caro por un CBG que en realidad
es aislado sintético indiferenciable, o vender como virtud un CBN que solo delata material viejo. Aquí está
la química, el análisis y qué se puede y no se puede afirmar.

Términos:
- **CBG (cannabigerol)** = C₂₁H₃₂O₂, **316,48 g/mol**; ácido CBGA, C₂₂H₃₂O₄, **360,49 g/mol**.
- **CBC (cannabichromene)** = C₂₁H₃₀O₂, **314,47 g/mol**; ácido CBCA.
- **CBN (cannabinol)** = C₂₁H₂₆O₂, **310,43 g/mol**; producto de oxidación del Δ9-THC.
- **oxidación aromatizante** = la pérdida de hidrógenos que aromatiza el anillo del THC y da CBN (`204`).

## CBG — el precursor que se vende como producto

CBGA es el nodo de la ruta (ver `172`). En una planta normal casi todo se consume hacia THCA/CBDA, así que
el CBG residual suele quedar por debajo del 1 % `% p/p base seca`. El CBG comercial viene de tres sitios:

1. **Quimiotipos IV** seleccionados con baja actividad de sintasas, que acumulan CBGA.
2. **Cosecha temprana** de quimiotipos normales, cuando el precursor aún no se ha consumido. Cuesta
   rendimiento total.
3. **Aislamiento cromatográfico** desde extractos, o síntesis. Indistinguible por HPLC del natural — por eso
   la trazabilidad documental es la única forma de sostener un claim de origen (`193`, `285`).

Farmacología, con nivel de evidencia marcado: el CBG se describe como ligando de baja afinidad en CB1/CB2,
agonista α2-adrenérgico y bloqueador de TRPV1 [in vitro]; hay trabajos en modelos animales. La evidencia
clínica controlada en humanos es **escasa** a agosto de 2026. No se afirma ningún beneficio terapéutico
aquí, ni se le atribuye acción sobre ninguna enfermedad.

## CBC — el que casi nadie mide bien

CBCA viene de la CBCA sintasa. El CBC neutro es lipofílico, sin actividad relevante en CB1 [in vitro], con
interés reportado en canales TRP (TRPA1) [in vitro]. Su problema es analítico: **coeluye con facilidad** con
otros picos en métodos cortos de HPLC y tiene absortividad UV distinta a la del THC, así que si el
laboratorio cuantifica CBC contra el patrón de CBD (mala práctica) el número está mal.

Además, el CBC es fotoquímicamente activo: puede formar CBL (cannabiciclol) con luz y tiempo. Un COA con CBL
detectable es otra bandera de material envejecido.

## CBN — no es un ingrediente, es un termómetro

El CBN **no está en la ruta biosintética**. Se forma así:

```
Δ9-THC  --(O2, luz, calor, tiempo)-->  CBN
C21H30O2  (314,47)                      C21H26O2  (310,43)
```

Esto lo convierte en el mejor **indicador de historial** que tiene un COA de cannabis:

| Relación CBN / THC total (base seca) | Lectura típica |
|---|---|
| < 1 % | Material fresco y bien manejado |
| 1–3 % | Envejecimiento normal o proceso térmico moderado |
| 3–10 % | Almacenamiento prolongado, luz, o descarboxilación excesiva (`174`) |
| > 10 % | Material viejo, mal envasado o recalentado; revisar todo el lote |

Los rangos son criterios de trabajo, no umbrales normativos; fíjalos en tu especificación interna (`282`).

Sobre la fama del CBN como "el cannabinoide del sueño": una revisión sistemática de los estudios en humanos
publicados concluyó que la evidencia clínica es **insuficiente** para sostener ese efecto. Se dice así
[clínico, insuficiente], y no se escribe en una etiqueta.

## Cómo se mide / cómo se comprueba

- **Técnica:** HPLC/UHPLC-DAD, gradiente lo bastante largo para resolver CBG, CBGA, CBC, CBN, CBDV y CBL.
  Los métodos "de 8 minutos" de potencia rápida suelen **no resolverlos** (`81`, `198`).
- **Patrones:** cada analito con su propio estándar de referencia certificado. Cuantificar un menor contra el
  patrón de otro cannabinoide es un error de método, no un atajo (`70`).
- **Longitud de onda:** el CBN absorbe distinto (máximo cercano a 220 y hombro a ~285 nm). Usa DAD y verifica
  pureza de pico (`80`).
- **Confirmación:** LC-MS/MS con transiciones específicas si el pico está en trazas o hay coelución (`83`).
- **LOQ:** exige que el COA reporte el LOQ de cada menor. "No detectado" sin LOQ no significa nada (`73`).
- **Conversión de ácidos:** `CBG total = CBG + 0,878 × CBGA`; `CBC total = CBC + 0,877 × CBCA`.
  El CBN no tiene forma ácida relevante en producto.

## Ejemplo aplicado

Dos lotes de destilado de "espectro amplio" ofrecidos al mismo precio (ILUSTRATIVO, HPLC-DAD, `% p/p`):

| Analito | Lote A | Lote B |
|---|---|---|
| CBD | 78,4 | 76,9 |
| CBG | 3,1 | 0,4 |
| CBC | 1,9 | 0,3 |
| CBN | 0,3 | 4,8 |
| Δ9-THC | < 0,3 | < 0,3 |
| CBN / cannabinoides totales | 0,4 % | 5,8 % |

Mismo precio, materiales distintos. El lote B tiene un CBN 16 veces mayor y menores casi ausentes: es
compatible con material sobreprocesado térmicamente o con biomasa vieja. Se rechaza o se renegocia, y se
pide el estudio de estabilidad del proveedor (`164`, `284`).

## Errores comunes

- Vender CBN como ingrediente funcional con claims de sueño. La evidencia clínica no lo sostiene y el claim
  puede ser sancionable (`267`, `276`).
- Comprar "CBG de espectro completo" sin trazabilidad: químicamente no puedes distinguir origen natural de
  aislado.
- Aceptar un COA que reporta CBG/CBC/CBN cuantificados con un solo patrón. Pide el método.
- Ignorar el CBN al leer un COA. Es la información gratis más valiosa del documento.
- Confundir el ácido con el neutro en los menores: `CBGA` y `CBG` no son intercambiables ni en masa ni en
  precio.
- No exigir LOQ. "ND" con un LOQ de 0,5 % no dice lo mismo que "ND" con un LOQ de 0,01 %.

## Conexión con otros módulos

→ `172-biosintesis-de-cannabinoides.md` — por qué CBG y CBC sí, y CBN no.
→ `173-formas-acidas-thca-y-cbda.md` — las formas ácidas y sus factores.
→ `204-estabilidad-y-degradacion-del-thc.md` — la reacción que fabrica el CBN.
→ `193-cromatografia-preparativa-y-aislados.md` — cómo se obtienen los menores puros.
→ `198-analisis-de-potencia-metodo.md` — el método que sí los resuelve.
→ `213-como-leer-un-coa-de-cannabis.md` — qué mirar primero en el documento.
→ `276-claims-estructura-funcion-y-ftc.md` — qué se puede decir sin meterse en problemas.
