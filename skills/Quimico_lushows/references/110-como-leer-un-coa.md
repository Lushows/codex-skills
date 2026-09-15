# 110 — Cómo leer un COA (anatomía completa, campo por campo)

Un **certificado de análisis (COA, certificate of analysis)** es el documento con el que se acepta una materia
prima, se libera un lote, se defiende un claim y se gana o se pierde un cliente B2B. También es, en el mercado
de suplementos, un documento **comercial**: quien te lo manda quiere que lo leas rápido y mires solo el número
grande. Este módulo te enseña a leerlo despacio, campo por campo, hasta poder decir qué afirma ese papel, qué
no afirma y qué decisión soporta. Es el módulo hermano de `213` —que hace lo mismo para cannabis—; aquí el
marco es general, con énfasis en hongos, donde el papel miente con más facilidad porque el analito no es
evidente.

Términos: **COA** = certificado de análisis. **lote (batch/lot)** = unidad de producción trazable.
**analito (analyte)** = lo que se mide. **matriz (matrix)** = el material en que se mide (polvo, extracto,
cápsula). **base (basis)** = con agua (tal cual, *as-is*) o sin agua (base seca, *dry weight*). **LOD / LOQ** =
límite de detección / de cuantificación (`73`). **incertidumbre expandida (expanded uncertainty, U)** = el ±
del resultado, normalmente con k=2 (`76`). **especificación (specification)** = el límite contra el que se
compara.

## La regla de lectura: tres preguntas antes del primer número

1. **¿Este COA es de mi lote?** Un COA "de la marca", "del producto" o "de referencia" no ampara ningún lote.
2. **¿Qué material exactamente se analizó?** Cuerpo fructífero, micelio sobre grano, extracto o producto
   terminado son cuatro cosas químicamente distintas (`217`, `218`).
3. **¿Qué decisión voy a tomar con esto?** Aceptar materia prima, liberar producto, sostener una etiqueta,
   exportar. Cada decisión exige un COA distinto de bueno.

## Anatomía de un COA: los once campos comentados

### 1. Encabezado del laboratorio y acreditación

Debe traer nombre legal completo, dirección, teléfono y **número de acreditación ISO/IEC 17025**. Se verifica
en el directorio del organismo acreditador (ONAC en Colombia; A2LA, ANAB en EE.UU.; ENAC en España), no en el
PDF. Y se verifica el **alcance**: ensayo + matriz + método (ver `107`). Un laboratorio acreditado para
metales en agua no lo está para metales en polvo de hongo. Si el ensayo se hizo fuera de alcance, un
laboratorio honesto lo declara con una nota — y eso no es malo, solo hay que saberlo.

### 2 y 3. Cliente, muestra, lote y cantidad del lote

El campo "cliente" dice quién pidió el análisis: si es un tercero ajeno a tu cadena de suministro, ese COA
pertenece a otra transacción y podría ser de otro lote o de otro material. Y deben aparecer **ambos** códigos,
el de muestra del laboratorio y el de lote del producto; sin el segundo el certificado no es trazable. El
tamaño del lote importa porque determina cuántas tomas debió tener el muestreo (`66`).

### 4. Quién tomó la muestra y bajo qué plan

El campo que casi ningún COA trae, y el que más cambia el significado del documento. Si el laboratorio hizo
el muestreo bajo su acreditación (cláusula 7.3 de ISO/IEC 17025), el COA describe el lote. Si la muestra la
mandó el proveedor, describe lo que el proveedor escogió mandar (ver `109`). Cuando el campo no aparece, la
pregunta es literal: *"¿quién tomó esta muestra y con qué plan?"*.

### 5. Fecha de muestreo, fecha de recepción y fecha de análisis

Tres fechas distintas y las tres importan. La secuencia lógica es: producción → muestreo → recepción →
análisis → emisión. Lo que rompa ese orden —análisis anterior a la producción del lote— es error de
transcripción o documento reciclado. También importa el **hueco**: una muestra de terpenos analizada 40 días
después de tomada ya perdió volátiles (`199`); una microbiológica a los 10 días no dice nada del lote (`100`).

### 6. Matriz y descripción de la muestra

"Polvo café claro, molido, empacado en bolsa sellada" es útil. "Suplemento" no lo es. La matriz define la
validación del método: uno validado en extracto no está validado en cápsula con excipientes.

### 7. Método por ensayo (una línea por analito, no una nota general)

Cada resultado debe traer su método con referencia verificable: kit comercial y versión (Megazyme K-YBGL
2025), método oficial (AOAC, USP) o SOP interno con código. "Método interno" a secas, o un solo "HPLC" al pie
para diez analitos, no permite auditar nada. En hongos este campo separa un certificado real de la publicidad:
**enzimático específico** vs **colorimétrico de polisacáridos totales** son dos universos distintos (`91`, `222`).

### 8. Resultado, unidad y base

El resultado sin unidad no existe, y la unidad sin base no se compara. `% p/p base seca`, `mg/g`, `mg/kg`,
`µg/kg`, `mg/porción`, `UFC/g`. Si el COA reporta base tal cual, debe traer la **humedad** para poder
convertir (`07`, `98`). La conversión se ejecuta, no se estima:

```
Base seca (% p/p) = resultado base humeda / (1 - humedad/100)
Ejemplo: 27,6 % p/p tal cual con humedad 8,0 %  ->  27,6 / 0,92 = 30,0 % p/p base seca
```

### 9. LOD / LOQ y la trampa del "no detectado"

"ND" (*not detected*) significa "por debajo del límite de detección de **este** método", no "no hay". Un ND sin
LOD/LOQ declarado no es un resultado. Y hay un caso que invalida el certificado entero: **LOQ mayor que el
límite de especificación**. Si el límite de plomo es 0,5 mg/kg y el LOQ del método es 1,0 mg/kg, ese "cumple"
no significa nada.

### 10. Especificación, veredicto y regla de decisión

El COA debe decir contra qué límite se comparó, de dónde sale ese límite (farmacopea, norma nacional,
especificación interna) y —si declara "Cumple"— con qué **regla de decisión** se manejó la incertidumbre
(`107`). Un "Cumple" sin límite escrito ni incertidumbre es una opinión con membrete.

### 11. Incertidumbre, firma y responsable

El resultado ideal se reporta como `valor ± U (k=2)`. Y el documento debe ir **firmado por una persona con
nombre y cargo**, con página *n de N*. Un PDF sin firma, sin paginación y sin número de informe es un archivo,
no un certificado.

## COA de hongos comentado línea por línea (EJEMPLO — ILUSTRATIVO)

```
LABORATORIO ANALITICO XYZ S.A.S. — Bogota, Colombia            Informe No. LA-2026-04871
Acreditado ISO/IEC 17025:2017 — ONAC No. 20-LAB-XXX            Pagina 1 de 2
-----------------------------------------------------------------------------------------
Cliente ............. BIO-SETA S.A.S.                    <- (2) el cliente soy yo: correcto
Producto ............ Polvo de cuerpo fructifero de Ganoderma lucidum   <- (6) matriz explicita
Lote del cliente .... GL-2608-CF                         <- (3) coincide con el saco fisico
Tamano del lote ..... 240 kg (12 sacos de 20 kg)         <- (3) permite auditar el muestreo
Muestra tomada por .. Laboratorio XYZ, plan SOP-MU-04, 12 incrementos, compuesta 1,8 kg
                                                          <- (4) EL CAMPO DE ORO: no la tomo el proveedor
Fecha de produccion . 12-jun-2026
Fecha de muestreo ... 03-jul-2026                        <- (5) posterior a produccion: coherente
Fecha de recepcion .. 04-jul-2026
Fecha de analisis ... 07 a 11-jul-2026                   <- (5) 4 dias tras recepcion: razonable
Precinto ............ 004512, integro a la recepcion     <- cadena de custodia cerrada (109)
-----------------------------------------------------------------------------------------
ENSAYO                     RESULTADO      UNIDAD/BASE        LOQ      SPEC       METODO
Humedad                       5,0         % p/p tal cual     0,1      <= 8,0     Karl Fischer (98)
Actividad de agua            0,44         aW                  -       <= 0,60    Higrometro (35)
Glucano total                34,8 +- 1,4  % p/p base seca    0,5        -        Megazyme K-YBGL v2025
alfa-Glucano                  4,1 +- 0,3  % p/p base seca    0,3      <= 10,0    Megazyme K-YBGL v2025
beta-Glucano (por diferencia)30,7 +- 1,5  % p/p base seca      -       >= 25,0   Calculado: total - alfa
Ergosterol                    2,4         mg/g base seca     0,1        -        HPLC-UV 282 nm (238)
Plomo (Pb)                   0,082        mg/kg              0,010     <= 0,5    ICP-MS, digestion microondas
Cadmio (Cd)                  0,031        mg/kg              0,010     <= 0,2    ICP-MS
Arsenico (As)                0,044        mg/kg              0,010     <= 0,3    ICP-MS
Mercurio (Hg)                 ND          mg/kg              0,005     <= 0,1    ICP-MS
Aflatoxinas B1+B2+G1+G2       ND          ug/kg              1,0       <= 4,0    LC-MS/MS (101)
Ocratoxina A                  ND          ug/kg              0,5       <= 10,0   LC-MS/MS
Aerobios mesofilos          2,3 x 10^3    UFC/g              10        <= 10^5   Recuento en placa
Hongos y levaduras          1,1 x 10^2    UFC/g              10        <= 10^4   Recuento en placa
Salmonella spp.            Ausencia/25 g      -               -        Ausencia  ISO 6579
E. coli                     < 10          UFC/g              10        <= 10^2   ISO 16649
Identidad de especie   Ganoderma lucidum   % identidad ITS 99,6         -        Secuenciacion ITS (245)
-----------------------------------------------------------------------------------------
Regla de decision: aceptacion simple (riesgo compartido), U expandida con k=2, nivel ~95 %.
Incertidumbre declarada solo para ensayos cuantitativos con U establecida.
Resultados aplican unicamente a la muestra recibida y al lote descrito.
Firmado: Q.F. [Nombre], Director Tecnico, Reg. Prof. XXXXX — 12-jul-2026
```

**Cómo se lee este COA, en orden:**

- **Trazabilidad primero (bloques 2–5).** Cliente correcto, lote que coincide con el saco, tamaño de lote
  declarado, muestreo hecho por el laboratorio con plan escrito, fechas en secuencia lógica y precinto íntegro.
  Con eso el documento ya vale como prueba; sin eso, todo lo de abajo es informativo.
- **La resta de glucanos.** β-glucano = 34,8 − 4,1 = 30,7 % p/p base seca. Rehacerla toma cinco segundos y
  detecta el error de transcripción más común del sector (`91`).
- **El α-glucano es el detector de fraude.** 4,1 % p/p en cuerpo fructífero es coherente. Un valor de 30–40 %
  gritaría "micelio sobre grano" (`218`, `220`).
- **La base.** Los glucanos van en base seca, con la humedad declarada aparte por Karl Fischer: comparable con
  otro COA. En base tal cual y sin humedad, no lo sería.
- **Los LOQ contra las especificaciones.** Pb: LOQ 0,010 vs spec 0,5 → 50 veces menor, excelente. Aflatoxinas:
  LOQ 1,0 vs spec 4,0 → 4 veces menor, justo. Ese cociente decide si un "ND" vale algo (`73`).
- **La identidad.** Sin ITS, no sabes de qué especie es el polvo, por mucho β-glucano que tenga (`245`).
- **La incertidumbre y la regla de decisión.** β-glucano 30,7 ± 1,5 contra spec ≥ 25,0 cumple bajo cualquier
  regla. Con 25,4 ± 1,5, la regla de decisión decidiría el destino del lote.
- **Lo que este COA NO dice**: no trae pesticidas, ni solventes residuales (no aplica a un polvo sin
  extracción), ni triterpenos ganodéricos (`224`) —que para reishi son parte del valor—, ni disolución o
  uniformidad, porque no es producto terminado. Un COA completo no es el que trae más ensayos: es el que trae
  **los que tu decisión necesita** y declara lo que no midió. Todas las cifras son **(ILUSTRATIVO)**.

## Del COA a la etiqueta: el puente que hay que hacer bien

Un COA de materia prima **no** respalda lo que dice tu etiqueta: entre uno y otro hay pérdidas por proceso,
dilución por excipientes y variación entre lotes.

```
Polvo con 30,7 % p/p beta-glucano base seca
Capsula con 500 mg de polvo -> 500 x 0,307 = 153,5 mg de beta-glucano por capsula
Porcion de 2 capsulas       -> 307 mg de beta-glucano por porcion
```

Lo que se declara en etiqueta debe sostenerse con el análisis del **producto terminado** (`282`, `283`). El
cálculo se ejecuta con `lab-tools/betaglucano_dosis.py` y se verifica con `Matematicas_lushows`.

## Errores comunes

- **Mirar solo el número grande.** El valor del COA está en los campos de trazabilidad, no en el porcentaje.
- **Aceptar el COA del proveedor como control de calidad propio.** Es el punto de partida (`106`, `284`).
- **No revisar la base ni la humedad** y comparar dos proveedores que no son comparables (`07`).
- **Leer el logo de acreditación en vez del anexo técnico del alcance** (`107`).
- **Aceptar "ND" sin LOD/LOQ**, o con un LOQ más alto que el límite legal (`73`).
- **No preguntar quién tomó la muestra.** Cambia por completo lo que el documento significa (`109`).
- **Confundir COA de materia prima con COA de producto terminado.** Solo el segundo sostiene la etiqueta, y
  el COA debe archivarse en el expediente del lote junto con la cadena de custodia, no en el correo (`168`).

## Conexión con otros módulos

→ `111-banderas-rojas-en-un-coa.md` — el catálogo de señales de alarma, una por una.
→ `112-como-impugnar-un-resultado.md` — qué hacer cuando el número no cuadra.
→ `213-como-leer-un-coa-de-cannabis.md` — el mismo ejercicio con las secciones propias del cannabis.
→ `107-iso-17025-y-acreditacion.md` — cómo verificar el sello del encabezado.
→ `91-metodos-colorimetricos-y-enzimaticos.md` y `221-medir-beta-glucanos-metodo-megazyme.md` — el método que
  hace verdadero el número de β-glucano.
→ `07-base-seca-vs-humeda.md` · `73-lod-loq-y-rango-lineal.md` · `76-incertidumbre-de-medida.md` — los tres
  campos que la gente ignora y que deciden todo.
→ `282-especificacion-de-producto-terminado.md` — contra qué se compara el resultado.
