# 282 — Especificación de producto terminado: la plantilla que define tu producto

Si de esta skill te llevas un documento, que sea este. La **especificación de producto terminado** es la
tabla que dice, para cada lote, qué parámetro se mide, con qué método, contra qué límite, cada cuánto y por
qué. Es lo único que convierte "extracto de reishi" en un producto definido. Sin ella no puedes reclamarle
al proveedor, no puedes sostener un claim, no puedes registrar ante INVIMA, no puedes exportar y no puedes
saber si el lote de hoy es igual al de hace seis meses. Con ella, todas esas conversaciones pasan a ser
técnicas en vez de emocionales. Este módulo trae la plantilla vacía y dos plantillas llenas —extracto de
hongos y aceite de cannabis— listas para adaptar.

Términos: **especificación (specification)** = conjunto de ensayos, métodos y criterios de aceptación que
un material debe cumplir para ser liberado. · **criterio de aceptación (acceptance criteria)** = el límite
numérico. · **liberación de lote (batch release)** = la decisión documentada de que el lote se puede
vender. · **skip-lot** = ensayar solo algunos lotes según un plan basado en riesgo. · **base seca (dry
basis, bs)** = resultado corregido por humedad (`07`).

## 1. Las cinco columnas y qué va en cada una

| Columna | Qué contiene | Error típico |
|---|---|---|
| **Parámetro** | Qué se mide, con el analito nombrado sin ambigüedad | "Polisacáridos" en vez de "beta-glucano" |
| **Método** | Código y año (AOAC/USP/Ph. Eur.) o método interno con su validación | "Método interno" a secas |
| **Límite** | Número, unidad y **base**. Con dirección: ≥, ≤ o rango | Poner un valor puntual sin rango |
| **Frecuencia** | Cada lote · skip-lot · anual · por proveedor · una vez en desarrollo | Ensayar todo siempre y quebrarse |
| **Justificación** | De dónde sale el límite: norma, farmacopea, capacidad de proceso, seguridad, claim | Copiar un límite sin saber de dónde salió |

Marco de referencia: para EE. UU., **21 CFR 111.70** exige establecer especificaciones (de componentes, en
proceso, de etiquetado y de producto terminado) y **111.75** exige verificarlas. Fuente: `ecfr.gov`,
consultado agosto de 2026; ver `274`. En Colombia el expediente del registro sanitario ante INVIMA pide la
especificación técnica del producto y sus métodos (`269`, `286`). Para la lógica farmacéutica de cómo se
justifica una especificación, la referencia conceptual es **ICH Q6A**.

## 2. Cómo se justifica un límite (esto es lo que casi nadie hace)

Un límite tiene exactamente cuatro orígenes legítimos:

```
1. REGULATORIO   la norma lo fija       → metales pesados, THC total, microbiología
2. FARMACOPEICO  la monografía lo fija  → cuando existe monografía para tu material (280)
3. DE PROCESO    tu proceso lo alcanza  → mínimo 3 lotes de producción real, media ± 3 desviaciones
4. DE CLAIM      tu etiqueta lo exige   → si declaras 200 mg por porción, el límite inferior lo garantiza
```

Y una regla dura de este oficio: **un solo lote no es una especificación.** Con un lote tienes una
anécdota. Con tres o más tienes una distribución, y de ahí sale un rango honesto. El cálculo se ejecuta,
no se estima de cabeza: rutea a `Matematicas_lushows` o usa `lab-tools/`.

Otra regla que evita un problema legal: **el límite del activo se declara como mínimo (≥), y la etiqueta se
escribe contra ese mínimo, no contra el promedio.** Si el promedio de tus lotes es 32 % y el mínimo
histórico 26 %, declaras contra 26 % o subes el mínimo del proceso. Declarar contra el promedio garantiza
que la mitad de los lotes incumpla la etiqueta.

## 3. Plantilla vacía

```
ESPECIFICACIÓN DE PRODUCTO TERMINADO
Producto: ______________________  Código: ________  Versión: ____  Fecha: __________
Presentación: ____________________  Elaborado por: ______  Aprobado por: ______

| Parámetro | Método (código y año) | Límite (con unidad y base) | Frecuencia | Justificación |
|-----------|----------------------|----------------------------|------------|---------------|
| ORGANOLÉPTICO Y FÍSICO
| IDENTIDAD
| CONTENIDO / POTENCIA
| PUREZA
| CONTAMINANTES QUÍMICOS
| CONTAMINANTES BIOLÓGICOS
| ENVASE Y VIDA ÚTIL

Control de cambios: toda modificación de límite o método exige nueva versión y justificación (169).
```

## 4. Plantilla llena — extracto de hongos (cápsulas de reishi, BIO-SETA)

Todos los límites marcados **(ILUSTRATIVO)** son valores de ejemplo con forma correcta, **no valores
regulatorios verificados**. Los de contaminantes hay que tomarlos de la norma vigente del país de destino y
de la farmacopea aplicable. **Verificar con la autoridad sanitaria y con abogado sanitario antes de fijar.**

| Parámetro | Método | Límite | Frecuencia | Justificación |
|---|---|---|---|---|
| Aspecto y color | Visual, contra estándar de referencia interno | Polvo fino, pardo claro a pardo oscuro | Cada lote | Detecta cambio de materia prima o degradación |
| Olor y sabor | Organoléptico | Característico, sin olor extraño | Cada lote | Indicador temprano de rancidez o contaminación |
| **Identidad de especie** | Secuenciación **ITS** (`103`, `245`) | *Ganoderma lucidum* confirmado | Cada lote nuevo de materia prima | La adulteración de especie es el fraude #1 (`246`) |
| **Identidad química** | HPTLC comparativa contra material de referencia (`96`) | Perfil coincidente con el estándar | Cada lote | Confirma que el extracto es de ese material |
| Parte usada | Documental + microscopía | Cuerpo fructífero, sin micelio ni sustrato | Cada lote | En la UE define el estatus Novel Food (`278`) |
| Humedad | Pérdida por desecación o Karl Fischer (`98`) | ≤ 8,0 % p/p **(ILUSTRATIVO)** | Cada lote | Estabilidad microbiológica y base de cálculo (`35`, `07`) |
| Cenizas totales | Gravimétrico, farmacopea | ≤ 5,0 % p/p bs **(ILUSTRATIVO)** | Skip-lot | Detecta tierra o carga mineral |
| **Beta-glucano** | Enzimático, glucano total − α-glucano (McCleary, J AOAC Int 2016;99(2):364; kit K-YBGL) | **≥ 25,0 % p/p bs** **(ILUSTRATIVO)** | **Cada lote** | Es el activo declarado: sostiene la etiqueta (`221`) |
| **Alfa-glucano** | Mismo ensayo, reporte separado | ≤ 10,0 % p/p bs **(ILUSTRATIVO)** | Cada lote | Un α-glucano alto delata micelio sobre grano (`218`, `220`) |
| Glucano total | Mismo ensayo, reporte separado | Informar | Cada lote | Permite auditar la resta del beta-glucano |
| Triterpenos ganodéricos | HPLC-DAD (`224`) | Informar (o ≥ límite si se declara) | Skip-lot | Marcador de extracción alcohólica en reishi |
| Ratio planta:extracto | Documental, balance de masa (`151`) | Declarado y trazable | Cada lote | El ratio se declara, no se promete potencia (`242`) |
| Granulometría | Tamizado (`143`) | ≥ 95 % pasa malla declarada | Skip-lot | Uniformidad de llenado de cápsula |
| **Plomo (Pb)** | ICP-MS, AOAC 2015.01 (`88`) | Según norma del país de destino **(verificar)** | Cada lote | Los hongos son acumuladores (`243`) |
| **Cadmio (Cd)** | ICP-MS, AOAC 2015.01 | Según norma **(verificar)** | Cada lote | Idem |
| **Arsénico inorgánico** | HPLC-ICP-MS (especiación) | Según norma **(verificar)** | Cada lote | El límite moderno es de inorgánico, no de total (`281`) |
| **Mercurio (Hg)** | ICP-MS | Según norma **(verificar)** | Cada lote | Idem |
| Aflatoxinas B1 y totales | HPLC-FLD con columna de inmunoafinidad (`101`) | Según norma **(verificar)** | Cada lote | Riesgo real en material secado mal (`244`) |
| Ocratoxina A | HPLC-FLD o LC-MS/MS | Según norma **(verificar)** | Skip-lot | Idem |
| Plaguicidas multirresiduo | QuEChERS + LC-MS/MS y GC-MS/MS (`102`) | Según norma **(verificar)** | Anual o por proveedor | Depende del sustrato y del origen |
| Solventes residuales | GC-headspace (`87`) | Etanol ≤ límite de farmacopea **(verificar)** | Cada lote si hay extracción alcohólica | No aplica a extracto acuoso puro |
| Recuento total de aerobios | Farmacopea / método oficial (`100`) | ≤ 10⁴ UFC/g **(ILUSTRATIVO)** | Cada lote | Producto de consumo oral |
| Levaduras y mohos | Farmacopea | ≤ 10³ UFC/g **(ILUSTRATIVO)** | Cada lote | Idem |
| *Escherichia coli* | Farmacopea | Ausencia en 1 g **(ILUSTRATIVO)** | Cada lote | Patógeno |
| *Salmonella* spp. | Farmacopea | Ausencia en 25 g **(ILUSTRATIVO)** | Cada lote | Patógeno |
| *Staphylococcus aureus* | Farmacopea | Ausencia en 1 g **(ILUSTRATIVO)** | Skip-lot | Contaminación por manipulación |
| Peso promedio de cápsula | Gravimétrico | Declarado ± 7,5 % **(ILUSTRATIVO)** | Cada lote | Uniformidad de dosis (`154`, `161`) |
| Vida útil | Estudio ICH Q1 (`164`) | 24 meses **(ILUSTRATIVO, a confirmar con datos)** | Estudio, no lote | Se demuestra, no se declara (`165`) |

Filas adicionales **solo para chaga** (*Inonotus obliquus*): **oxalato** (cromatografía iónica o enzimático)
y **radiocesio Cs-137** (espectrometría gamma) — riesgos específicos documentados de esa especie, ver `230`.

## 5. Plantilla llena — aceite de cannabis (full spectrum, uso oral)

| Parámetro | Método | Límite | Frecuencia | Justificación |
|---|---|---|---|---|
| Aspecto | Visual | Líquido oleoso, sin separación de fases | Cada lote | Detecta emulsión rota o cristalización |
| Identidad del aceite portador | FTIR o perfil de ácidos grasos por GC-FID (`53`, `92`) | Coincide con estándar (p. ej., MCT) | Por proveedor | El portador cambia biodisponibilidad (`159`) |
| **CBD total** | HPLC-DAD, cannabinoides (base AOAC 2018.11 adaptada, `198`) | **90–110 % de lo declarado (mg/mL)**, incluyendo CBD + CBDA | **Cada lote** | Rango alineado con la monografía USP de inflorescencia (`280`) |
| **Δ9-THC total** | HPLC-DAD; total = Δ9-THC + (THCA × 0,877) (`175`) | ≤ límite legal del país de destino **(verificar; no es igual en Colombia, EE. UU. y la UE)** | **Cada lote** | Define si el producto es legal o ilegal |
| Perfil de cannabinoides menores | HPLC-DAD (CBG, CBC, CBN, THCV) | Informar | Cada lote | CBN alto delata degradación del THC (`204`) |
| Perfil de terpenos | GC-MS o GC-FID (`199`) | Informar, o rango si se declara "full spectrum" | Skip-lot | Sostiene el claim de espectro completo (`183`) |
| Contenido de agua | Karl Fischer (`98`) | ≤ 0,5 % p/p **(ILUSTRATIVO)** | Skip-lot | Estabilidad oxidativa |
| Índice de peróxidos | Farmacopea / AOCS | ≤ límite del aceite portador **(verificar)** | Skip-lot | Rancidez del portador (`47`, `61`) |
| **Solventes residuales** | GC-headspace (`87`, `201`) | Por clase, según farmacopea **(verificar)** | **Cada lote si hubo extracción con solvente** | Etanol, butano, hexano según el proceso (`187`, `188`) |
| **Metales pesados (Pb, Cd, As, Hg)** | ICP-MS, AOAC 2015.01 (`202`) | Según norma **(verificar)** | Cada lote | El cannabis es fitorremediador |
| Plaguicidas | QuEChERS + LC-MS/MS y GC-MS/MS (`200`) | Lista y límites del país de destino **(verificar)** | Cada lote | Las listas de cannabis suelen ser más largas que las de alimentos |
| Micotoxinas | HPLC-FLD o LC-MS/MS (`203`) | Según norma **(verificar)** | Cada lote | Riesgo del material vegetal de partida |
| Microbiología | Farmacopea (`100`, `203`) | Según norma **(verificar)** | Cada lote | Producto de consumo oral |
| Homogeneidad de contenido | Muestreo en 3 puntos del tanque, HPLC | RSD ≤ 5 % **(ILUSTRATIVO)** | Cada lote | Un aceite mal mezclado no dosifica (`66`) |
| Volumen de llenado | Gravimétrico | Declarado, con tolerancia legal **(verificar)** | Cada lote | Metrología legal |
| Estabilidad y vida útil | ICH Q1, acelerado + tiempo real (`164`, `165`) | Definida por el estudio | Estudio | El THC y el CBD se degradan a CBN (`204`) |

## Cómo se comprueba que la especificación sirve

```
1. ¿Cada fila tiene método CON código y año? Si dice solo "interno", exige la validación (75)
2. ¿Cada límite tiene unidad Y base? "30 %" no es un límite; "≥ 25,0 % p/p base seca" sí
3. ¿Puedo señalar de dónde salió cada límite? Si no, es un número copiado
4. ¿Tengo al menos 3 lotes que la cumplen? Si no, es una aspiración, no una especificación
5. ¿La etiqueta declara contra el LÍMITE INFERIOR y no contra el promedio?
6. ¿Existe una versión, una fecha y una firma de aprobación? Sin eso no es un documento controlado (168)
7. ¿Qué pasa si un lote sale fuera? Hay que tener el procedimiento de desviación escrito ANTES (169)
```

## Errores comunes

- **Copiar la especificación del proveedor y firmarla.** La suya protege al proveedor; la tuya te protege a ti.
- **Poner "cumple normativa vigente" en la columna de límite.** Es inejecutable: no se puede reclamar.
- **Fijar el límite con un solo lote.** Es una anécdota disfrazada de estándar.
- **Declarar la etiqueta contra el promedio.** Garantiza que la mitad de los lotes incumpla.
- **Olvidar la base seca en el activo.** Dos lotes con humedades distintas dejan de ser comparables (`07`).
- **Poner todo "cada lote" y luego no poder pagarlo.** Se diseña con riesgo: skip-lot donde el riesgo es bajo (`283`, `291`).
- **No versionar.** Si cambias un límite sin control de cambios, no sabrás qué cumplía el lote de hace un año.

## Conexión con otros módulos

→ `247-especificacion-de-producto-de-hongos.md` — la versión específica para materia prima fúngica.
→ `283-plan-de-control-de-calidad-por-lote.md` — cómo se ejecuta esta tabla lote a lote.
→ `286-expediente-tecnico-del-producto.md` — dónde vive este documento dentro del expediente.
→ `280-farmacopeas-usp-ep-y-monografias.md` y `281-metodos-oficiales-aoac.md` — de dónde salen los métodos.
→ `110-como-leer-un-coa.md` — cómo se verifica que el COA responde a esta especificación.
→ `164-estabilidad-ich-q1-y-vida-util.md` — cómo se demuestra la fila de vida útil.
→ `291-costos-de-analisis-y-presupuesto.md` — cuánto cuesta realmente cumplirla.
→ `Matematicas_lushows` — para calcular rangos, RSD y límites a partir de los lotes reales.
