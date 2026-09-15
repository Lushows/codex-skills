# 64 — Derivatización para análisis (cuando hay que disfrazar la molécula para poder medirla)

Hay moléculas que el instrumento simplemente no puede ver: son demasiado polares para volar en un
cromatógrafo de gases, no absorben luz UV, o se descomponen en el inyector antes de llegar a la columna.
La derivatización es modificarlas químicamente —de forma controlada y cuantitativa— para volverlas medibles.
Te importa porque casi todo análisis de esteroles (ergosterol), de ácidos grasos, de azúcares y de
aminoácidos en tu producto pasa por ahí, y porque **una derivatización mal validada es la fuente de error
más silenciosa de un COA**: el número sale, es reproducible, y está mal.

Términos: **derivatización (derivatization)** = reacción química previa al análisis para mejorar volatilidad,
estabilidad o detectabilidad. **Sililación (silylation)** = reemplazar el hidrógeno activo de −OH, −COOH,
−NH por un grupo trimetilsililo (TMS). **Reactivo derivatizante (derivatizing reagent)** = el que hace el
trabajo (BSTFA, MSTFA, dansil...). **Rendimiento de derivatización (derivatization yield)** = qué fracción
del analito se convirtió; si no es reproducible, no hay cuantificación. **Anhidro (anhydrous)** = sin agua;
en sililación, obligatorio.

## Por qué es necesaria

| Problema del analito | Qué pasa sin derivatizar | Qué resuelve la derivatización |
|---|---|---|
| Muy polar / no volátil (−OH, −COOH, −NH₂) | No eluye en GC o eluye con colas horribles | Baja la polaridad y el punto de ebullición |
| Termolábil | Se descompone en el inyector a 250 °C | La forma derivatizada aguanta |
| No tiene cromóforo | Invisible al detector UV | Se le pega un cromóforo o un fluoróforo |
| Ioniza mal en MS | Señal pobre en ESI | Se le añade un grupo que ioniza bien |
| Enantiómeros | Coeluyen en fase aquiral | Se forman diastereómeros separables (`43`) |

Caso concreto y muy nuestro: **los cannabinoides ácidos**. THCA y CBDA tienen −COOH; en un GC caliente
**descarboxilan en el inyector** y el instrumento reporta THC donde había THCA (`173`, `174`). Hay dos
salidas: (a) usar HPLC, que no calienta y por eso es el método de referencia para potencia (`198`); o
(b) sililar para medir la forma ácida por GC. La regla que se deriva: **si necesitas distinguir forma ácida
de neutra, GC sin derivatizar no es una opción.**

## Las tres familias de reacción

```
1) SILILACIÓN  (la reina en GC de productos naturales)
   R−OH  +  BSTFA/MSTFA  →  R−O−Si(CH₃)₃  +  subproducto
   Reactivos: BSTFA (+1 % TMCS como catalizador), MSTFA, TMSI, HMDS
   Condiciones típicas: piridina o acetonitrilo anhidro, 60–80 °C, 30–60 min
   Aplica a: esteroles (ergosterol), triterpenos, azúcares, ácidos orgánicos, fenoles, aminoácidos
   Talón de Aquiles: EL AGUA. Hidroliza el reactivo y arruina el rendimiento.

2) ACILACIÓN  (para aminas y alcoholes; añade halógenos que el ECD/NCI ve de maravilla)
   R−NH₂ + anhídrido trifluoroacético (TFAA) / heptafluorobutírico (HFBA) → amida perfluorada
   Ventaja: sensibilidad brutal con detección de captura de electrones o MS en NCI
   Aplica a: alcaloides, aminas biógenas, análisis forense

3) ALQUILACIÓN / ESTERIFICACIÓN  (para ácidos carboxílicos)
   R−COOH + BF₃/metanol, o TMSH, o diazometano (peligroso, evitar) → R−COOCH₃
   Aplica a: perfil de ácidos grasos como FAMEs (fatty acid methyl esters), el método clásico (`53`)
```

## Derivatización para HPLC — cuando el problema es el detector

En LC no se busca volatilidad sino **señal**. Se le pega al analito un grupo que absorbe UV o fluoresce:

| Reactivo | Reacciona con | Detección | Uso típico |
|---|---|---|---|
| Cloruro de dansilo | Aminas, fenoles | Fluorescencia | Aminas biógenas, aminoácidos |
| OPA (o-ftalaldehído) + tiol | Aminas primarias | Fluorescencia | Aminoácidos; derivado inestable → **pre-columna automatizada** |
| FMOC-Cl | Aminas primarias y secundarias | Fluorescencia | Aminoácidos (complementa OPA, que no ve prolina) |
| DNPH (2,4-dinitrofenilhidrazina) | Aldehídos y cetonas | UV 360 nm | Carbonilos, control de oxidación |
| PMP (1-fenil-3-metil-5-pirazolona) | Azúcares reductores | UV 245 nm | **Composición de monosacáridos** tras hidrólisis: el método para caracterizar un polisacárido (`52`) |
| 2-AB / APTS | Azúcares reductores | Fluorescencia | Perfil de glicanos, alta resolución |

**Pre-columna vs post-columna:** pre-columna es más simple y da mejor cromatografía, pero exige un derivado
estable el tiempo que dure la corrida; post-columna cuesta hardware pero sirve cuando el derivado se muere
en minutos (OPA es el ejemplo clásico).

## Lo que hay que validar (aquí es donde se cae la gente)

Una derivatización agrega una reacción química al método, así que la validación ICH Q2(R2) (`75`) tiene que
cubrirla explícitamente:

```
1. RENDIMIENTO Y REPRODUCIBILIDAD
   No hace falta que sea 100 %, pero sí que sea el MISMO para muestra y para patrón.
   Se comprueba: patrón derivatizado vs patrón ya derivatizado comercial, o curva de tiempo de reacción.

2. CINÉTICA — la curva de meseta
   Derivatizar 15, 30, 45, 60, 90 min y graficar área vs tiempo. Se trabaja EN LA MESETA,
   nunca en la pendiente: ahí, 5 minutos de diferencia cambian el resultado.

3. EXCESO DE REACTIVO
   Debe haber exceso suficiente para que la matriz (que también tiene −OH) no compita con tu analito.
   Matriz rica en azúcares = consumo brutal de reactivo. Se verifica con adición de estándar (`72`).

4. ESTABILIDAD DEL DERIVADO
   ¿Cuánto aguanta en el vial del automuestreador? Los TMS se hidrolizan con la humedad del ambiente.
   Se mide reinyectando el mismo vial a 0, 6, 12 y 24 h.

5. ESTÁNDAR INTERNO
   Debe agregarse ANTES de derivatizar y derivatizarse igual que el analito. Un estándar interno
   añadido después no corrige la variabilidad de la reacción, que es justo la que quieres corregir (`72`).

6. BLANCO DE REACTIVO
   Los reactivos de sililación dan picos propios y a veces contienen trazas del analito.
```

Punto 5 subrayado: **el estándar interno es lo que convierte una derivatización de artesanía en método.**
Para GC-MS de esteroles se usa típicamente un esterol que no esté en la muestra (colestano, betulina) o,
mejor, el análogo marcado isotópicamente si el presupuesto lo permite.

## Cuándo NO derivatizar

- Si LC-MS/MS resuelve el analito directo, **no derivatices**. Menos pasos, menos error (`83`).
- Si el analito es térmicamente sensible y el problema real era el GC, cambia de técnica, no de molécula.
- Si el método oficial de la farmacopea (`280`) o AOAC (`281`) no la usa, derivatizar te saca del método
  oficial y ahora tienes que validar equivalencia.
- Si la matriz es tan sucia que el rendimiento va a variar lote a lote: primero limpia con SPE (`69`).

## Ejemplo aplicado — ergosterol por GC-MS con sililación

Ergosterol es el marcador de material fúngico (`238`, `60`). Tiene un −OH en C3: es poco volátil y da colas.
Flujo típico **(ILUSTRATIVO en los números)**:

```
1. Saponificación: 0,50 g de polvo + KOH metanólico, 80 °C, 30 min   ← libera el ergosterol esterificado
2. Extracción del insaponificable con n-heptano; se lleva a sequedad bajo N₂   ← el agua debe irse TODA
3. Estándar interno: 5α-colestano, agregado en el paso 1
4. Derivatización: 100 µL de BSTFA + 1 % TMCS en piridina anhidra, 70 °C, 45 min (meseta verificada)
5. GC-MS, columna 5 % fenil, inyección splitless, SIM del TMS-ergosterol
6. Cuantificación por relación de áreas analito/estándar interno contra curva de 5 puntos (`71`)

Resultado ILUSTRATIVO de un lote de cuerpo fructífero de Ganoderma:
   Ergosterol = 1,84 mg/g base seca   (n=3, RSD 3,1 %)   LOQ del método 0,05 mg/g   (`73`)
Diagnóstico: coherente con material fúngico real. Un resultado < LOQ en un "extracto de hongo" es
una bandera roja de primer orden (`60`).
```

El mismo esqueleto sirve para triterpenos por GC-MS, para el perfil de ácidos grasos como FAMEs (`53`) y
para composición de monosacáridos de un polisacárido tras hidrólisis ácida (`52`).

## Errores comunes

- Derivatizar una muestra húmeda. El agua mata la sililación y el resultado sale bajo y errático. Secado
  bajo nitrógeno o con sulfato de sodio anhidro antes, siempre.
- Agregar el estándar interno después de derivatizar. Corrige la inyección, no la reacción: el error grande
  se queda.
- Trabajar en la pendiente de la curva de tiempo en vez de en la meseta. Método irreproducible entre analistas.
- Reinyectar viales del día anterior sin haber estudiado la estabilidad del derivado.
- Reactivo viejo o mal cerrado. BSTFA y MSTFA se hidrolizan con la humedad ambiente; se compran en ampolla
  y se usan frescos.
- Reportar formas ácidas de cannabinoides medidas por GC sin derivatizar. Ese número está sistemáticamente
  mal, aunque el cromatograma se vea hermoso (`173`, `198`).
- Olvidar que la piridina y los reactivos silanizantes son peligrosos: campana, guantes de nitrilo, SDS leída
  (`08`, `09`).
- No correr blanco de reactivo y atribuir a la muestra un pico que trae el frasco.

## Conexión con otros módulos

→ `85-cromatografia-de-gases.md` y `86-gc-ms-y-headspace.md` — la técnica que exige la derivatización.
→ `79-hplc-y-uhplc.md` y `83-lc-ms-ms-y-mrm.md` — la alternativa que suele evitarla.
→ `238-ergosterol-como-marcador.md` · `55-esteroles-y-triterpenos.md` — el analito del ejemplo.
→ `53-lipidos-y-acidos-grasos.md` — FAMEs, la derivatización más rutinaria del mundo.
→ `52-polisacaridos-y-glucanos.md` — composición de monosacáridos por marcaje con PMP.
→ `72-estandar-interno-y-adicion-de-estandar.md` — por qué el estándar interno va antes de la reacción.
→ `75-validacion-de-metodos-ich-q2-r2.md` — cómo se valida un método con paso de reacción.
→ `173-formas-acidas-thca-y-cbda.md` — el error clásico de medir ácidos por GC.
