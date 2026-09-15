# 102 — Pesticidas multiresiduo (medir 200 venenos a la vez, en partes por billón)

El análisis multiresiduo de plaguicidas es el ensayo más técnico y más caro de una batería de calidad, y el
que más gente contrata sin entender qué está pidiendo. "Análisis de pesticidas" no significa nada: significa
**qué lista de compuestos**, con **qué límite de cuantificación** para cada uno, y **en qué matriz**. Un
laboratorio puede reportar "no detectado" en 60 pesticidas y tu producto seguir contaminado con el que no
estaba en la lista. En cannabis este ensayo es el que más lotes rechaza y el que más pleitos genera.

Términos: **multiresiduo (multiresidue)** = un solo método para decenas o cientos de analitos.
**LMR (MRL, Maximum Residue Limit)** = límite legal de residuo para un plaguicida en un alimento.
**QuEChERS** = preparación de muestra rápida y barata (Quick, Easy, Cheap, Effective, Rugged, Safe).
**efecto matriz (matrix effect)** = la muestra suprime o realza la señal del analito en el detector.
**acción/no acción (action limit)** = el valor que dispara el rechazo del lote.

## La arquitectura del método

```
Muestra molida (5-15 g)
   -> Extraccion QuEChERS: acetonitrilo + sales (MgSO4, NaCl, citratos), agitar, centrifugar
   -> Limpieza dSPE: PSA (quita acidos organicos), C18 (quita grasas), GCB (quita clorofila)
      OJO: GCB retiene pesticidas planares -> se pierde recuperacion de algunos
   -> Division del extracto:
        rama LC-MS/MS  -> pesticidas polares, termolabiles (~80 % de la lista)
        rama GC-MS/MS  -> organoclorados, piretroides, volatiles (~20 %)
   -> Cuantificacion con calibracion EN MATRIZ + estandares internos marcados
```

QuEChERS está descrito en el método oficial **AOAC 2007.01** y en la norma europea **EN 15662**. Para
matrices grasas o muy pigmentadas —aceites de cannabis, extractos de hongo— hay que modificarlo, y ahí es
donde los laboratorios se diferencian de verdad.

## Por qué "no detectado" puede ser mentira sin que nadie mienta

Tres huecos, todos legítimos en el papel:

1. **El compuesto no estaba en la lista.** Si el panel tiene 66 analitos y el cultivador usó uno que no está,
   sale limpio. Pide siempre la **lista completa de analitos con su LOQ individual**.
2. **El LOQ es más alto que el límite.** Si el límite de acción es 0,05 mg/kg y el LOQ del laboratorio es
   0,1 mg/kg, "no detectado" no demuestra cumplimiento (ver `73`).
3. **La recuperación es mala en esa matriz.** Un pesticida que se recupera al 30 % en aceite de cannabis
   aparece tres veces más bajo de lo que está. La recuperación se demuestra por analito **y por matriz**.

Esos tres huecos son exactamente la base de `111-banderas-rojas-en-un-coa.md` y de
`113-lab-shopping-e-inflacion-de-potencia.md`.

## Listas y límites (a agosto de 2026)

| Marco | Lista | Nota |
|---|---|---|
| **Cannabis California** | 66 analitos (Categoría I con tolerancia cero práctica + Categoría II con límites) | Referencia de facto de la industria |
| Cannabis, otros estados EE. UU. | Entre ~10 y ~100 analitos | Varía por estado; no hay lista federal |
| **Unión Europea, alimentos** | LMR por par plaguicida-producto en la base de datos de la Comisión Europea | Por defecto 0,01 mg/kg cuando no hay LMR específico |
| **Codex Alimentarius** | LMR internacionales | Referencia cuando no hay norma local |
| **Colombia** | Resoluciones del ICA (registro de plaguicidas) y normas de alimentos; LMR frecuentemente armonizados con Codex | A agosto de 2026, verifica el texto vigente antes de fijar especificación (ver `271`) |

Regla de oro comercial: **la lista se define por el mercado de destino, no por lo que ofrezca el
laboratorio.** Si vas a exportar a la UE, el panel de 66 de California no te sirve.

## Cannabis: por qué este ensayo es tan difícil

- La flor tiene **mucha clorofila y muchos terpenos**: ensucian el sistema y compiten en la fuente de iones.
- Los concentrados **concentran también el pesticida**: un residuo indetectable en flor puede aparecer 5–10
  veces más alto en el extracto. Nunca supongas que el COA de la flor cubre al concentrado.
- Muchos límites son de **tolerancia cero práctica** (LOD/LOQ como criterio), lo que traslada toda la
  presión al desempeño analítico del laboratorio.
- Los residuos **no se distribuyen homogéneamente** en el material vegetal: el muestreo pesa muchísimo.

Ver `200-pesticidas-en-cannabis.md`.

## Cómo se comprueba

- **Calibración en matriz** (matrix-matched), no en solvente. Sin ella el efecto matriz sesga el resultado.
- **Estándares internos marcados isotópicamente** para los analitos críticos.
- **Muestras fortificadas (spikes)** en cada corrida, a nivel del límite de acción; recuperación típicamente
  aceptable entre 70 % y 120 % con RSD ≤ 20 % (criterio orientativo tipo SANTE; el rango exacto lo fija tu
  método validado, ver `74`).
- **Blanco de matriz** para descartar contaminación cruzada del propio laboratorio.
- **Confirmación por dos transiciones MRM** y relación de iones dentro de tolerancia (ver `83`).
- **Alcance ISO 17025**: que el ensayo y la matriz estén **dentro** del alcance acreditado, no solo que el
  laboratorio esté acreditado en algo (ver `107`).

## Ejemplo aplicado (ILUSTRATIVO)

Extracto de cannabis full spectrum destinado a un mercado con la lista de 66 analitos.

```
Metodo      : QuEChERS modificado para matriz grasa + LC-MS/MS y GC-MS/MS
Panel       : 66 analitos, LOQ individual entre 0,01 y 0,10 mg/kg
Spike a 0,05 mg/kg: recuperacion media 89 % (rango 74-112 %), RSD 9 %

Resultados:
  63 analitos      : < LOQ
  Miclobutanil     : 0,08 mg/kg     Limite de accion 0,00 (categoria I) -> NO CONFORME
  Piperonil butoxido: 0,9 mg/kg     Limite 2,0 mg/kg -> conforme
  Bifenazato       : 0,15 mg/kg     Limite 5,0 mg/kg -> conforme

Trazabilidad: el miclobutanil aparecio en el extracto y no en el COA de la flor.
Hipotesis: factor de concentracion del extracto ~6x sobre un residuo que en flor
estaba cerca del LOQ. Accion: analizar la flor con LOQ mas bajo y auditar al cultivador.
```

(Cifras ilustrativas.)

## Errores comunes

- **Pedir "análisis de pesticidas" sin lista.** Es como pedir "un examen médico".
- **Aceptar un LOQ por encima del límite** y creer que "no detectado" es conformidad.
- **Asumir que el COA de la materia prima cubre al concentrado.** El proceso concentra el residuo.
- **Calibrar en solvente** en vez de en matriz.
- **No pedir recuperaciones** por matriz. Sin recuperación demostrada, el número es una estimación.
- **Confiar en tamices portátiles** (SERS, tiras) como resultado reportable (ver `93`).
- **Cambiar de laboratorio hasta que salga limpio.** Eso es lab shopping y es fraude (ver `113`).

## Conexión con otros módulos

→ `69-extraccion-para-analisis-spe-y-quechers.md` — la preparación de muestra en detalle.
→ `83-lc-ms-ms-y-mrm.md` y `86-gc-ms-y-headspace.md` — los dos detectores del método.
→ `73-lod-loq-y-rango-lineal.md` — por qué el LOQ define lo que puedes afirmar.
→ `200-pesticidas-en-cannabis.md` — límites y práctica en cannabis.
→ `271-ica-y-materia-prima-vegetal.md` — el marco colombiano de plaguicidas.
→ `111-banderas-rojas-en-un-coa.md` — cómo se ve este ensayo cuando está mal hecho.
