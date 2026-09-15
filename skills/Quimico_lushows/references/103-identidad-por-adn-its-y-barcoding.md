# 103 — Identidad por ADN: ITS y barcoding (por qué tu polvo de hongo puede no ser la especie de la etiqueta)

Un polvo café no tiene cara. Cuando un hongo se seca, se muele y se extrae, desaparecen todas las
características que un micólogo usaría para identificarlo: forma, color, esporas, himenio. A partir de ahí,
la única pregunta honesta es "¿cómo sabes que esto es *Hericium erinaceus* y no otra cosa?", y la única
respuesta técnica es el **ADN**. El barcoding por ITS es el método aceptado internacionalmente para
identificar hongos a nivel de especie, y los estudios publicados sobre suplementos del mercado son
incómodos: una fracción grande de los productos no contiene la especie que declara.

Términos: **ITS (Internal Transcribed Spacer)** = región del ADN ribosomal nuclear, entre los genes 18S,
5.8S y 28S; es el **código de barras oficial de los hongos**. **PCR (Polymerase Chain Reaction)** =
amplificación de un fragmento de ADN. **Sanger** = secuenciación clásica, una secuencia por reacción.
**metabarcoding** = secuenciación masiva que lista **todas** las especies presentes en una mezcla.
**BLAST** = búsqueda de la secuencia contra una base de datos (GenBank, UNITE).

## Por qué ITS y no otro gen

ITS fue adoptado como barcode primario de hongos porque cumple tres condiciones prácticas: está presente en
**muchas copias** por genoma (del orden de ~250), lo que hace fácil amplificarlo incluso con ADN escaso o
parcialmente degradado; varía lo suficiente entre especies; y tiene una base de datos enorme —del orden de
cientos de miles de secuencias en GenBank— que permite comparar
([Raja et al., *Food Chemistry* 214:383-392, 2017, "DNA barcoding for identification of consumer-relevant
mushrooms"](https://pubmed.ncbi.nlm.nih.gov/27507489/)).

| Región | Uso | Nota |
|---|---|---|
| **ITS1-5.8S-ITS2** | Barcode primario de hongos | Primers universales ITS1/ITS4, ITS1F/ITS4B |
| LSU (28S, D1/D2) | Complemento a nivel de género | Menos resolución de especie |
| RPB2, TEF1-α | Barcode secundario | Cuando ITS no resuelve (algunos *Ganoderma*, *Cordyceps*) |
| COI | Barcode de animales | **No sirve bien en hongos**: intrones, amplificación difícil |

## Qué encontraron los estudios de mercado

Los datos publicados sobre productos comerciales de hongos son la razón por la que este módulo existe:

- Aproximadamente **30 %** de los polvos de hongo analizados coincidían en **género pero no en especie**, y
  **15 %** llevaban un nombre completamente incorrecto.
- Hasta **43 %** de las cápsulas de suplemento analizadas por ITS tenían la información de especie
  equivocada ([Raja et al., 2017](https://www.sciencedirect.com/science/article/pii/S0308814616310743)).
- La adulteración más común es **económicamente motivada (EMA)**: mezclar hongo caro con hongo barato para
  bajar el costo, revisado en la literatura reciente
  ([*Food Reviews International*, vol. 41 n.º 8, 2025, revisión sobre autenticación de hongos: barcoding,
  quimiometría e inteligencia artificial](https://www.tandfonline.com/doi/full/10.1080/87559129.2025.2480233)).

Traducido a negocio: si compras polvo de hongo sin verificación de ADN, la probabilidad de que no sea lo que
dice no es marginal.

## Cómo se hace (flujo real)

```
1. Muestreo: 3-5 tomas del lote, molidas y homogeneizadas (66, 67).
2. Extraccion de ADN: kit tipo CTAB o columna de silica. Aqui se cae todo si el ADN esta degradado.
3. Verificacion de calidad del ADN: concentracion (ng/uL) y relacion A260/A280 (~1,8 ideal).
4. PCR con primers ITS1/ITS4 (o ITS1F/ITS4B, mas especificos de hongo).
5. Gel o electroferograma: confirmar banda unica del tamano esperado (~600-750 pb en muchos hongos).
   Banda multiple = mezcla de especies -> Sanger no sirve, hay que ir a metabarcoding.
6. Secuenciacion Sanger en ambas direcciones (forward y reverse) y ensamblado del contig.
7. BLAST contra GenBank y contra UNITE (base curada de ITS fungico).
8. Criterio: identidad >= 97-99 % contra una secuencia de REFERENCIA de tipo o de voucher confiable,
   con cobertura >= 90 %. Un match de 99 % contra una secuencia mal anotada no vale nada.
```

## Los cuatro límites que hay que decir en voz alta

1. **El ADN no distingue micelio de cuerpo fructífero.** Son el mismo organismo, el mismo genoma. Un polvo de
   micelio sobre arroz puede dar *Hericium erinaceus* al 100 % y aun así ser mayormente almidón. La pregunta
   "¿cuerpo fructífero o micelio en grano?" se resuelve por **química**: β-glucano vs α-glucano por Megazyme
   K-YBGL (`91`, `221`) y ergosterol como marcador de biomasa fúngica (`238`). ITS y química son
   complementarios, no intercambiables.
2. **Los extractos suelen no tener ADN utilizable.** El calor, el etanol y la hidrólisis fragmentan el ADN.
   En un extracto acuoso concentrado o secado por aspersión, la PCR a menudo falla o amplifica basura. El
   barcoding se aplica **a la materia prima**, y para el extracto se usa huella química (`104`) o se
   confía en la trazabilidad documental del lote de entrada (`168`).
3. **Las bases de datos tienen errores.** Un porcentaje conocido de secuencias en GenBank está mal
   identificado. Por eso se compara también contra UNITE y se privilegian secuencias de material tipo.
4. **Una banda única puede esconder una mezcla.** Si hay dos especies con ITS de tamaño parecido, Sanger da
   una secuencia sucia y ambigua. Ante cualquier duda: **metabarcoding**, que lista todo lo que hay.

## Sanger vs metabarcoding

| | Sanger (ITS) | Metabarcoding (NGS) |
|---|---|---|
| Pregunta que responde | "¿Es esta especie?" | "¿Qué especies hay y en qué proporción relativa?" |
| Mezclas | No las resuelve | Sí |
| Costo relativo | Bajo | Alto (aunque baja cada año) |
| Tiempo | Días | 1–3 semanas |
| Uso | Verificación de lote de una sola especie | Blends, sospecha de adulteración, auditoría de proveedor |

Advertencia honesta: la proporción de lecturas en metabarcoding **no es** proporción de masa. El número de
copias de ITS varía entre especies. Sirve para decir "hay *Trametes* donde debía haber solo *Ganoderma*", no
para decir "hay 12 % de *Trametes* en peso".

## Ejemplo aplicado (ILUSTRATIVO)

Verificación de un proveedor nuevo de reishi, lote GL-2608.

```
ADN extraido      : 42 ng/uL, A260/A280 = 1,84   -> calidad adecuada
PCR ITS1/ITS4     : banda unica ~680 pb
Sanger bidireccional, contig de 664 pb, calidad Phred media > 40

BLAST GenBank : 99,4 % identidad con Ganoderma lingzhi (cobertura 98 %)
                97,1 % identidad con Ganoderma lucidum sensu stricto
UNITE         : asignado a Ganoderma lingzhi

Lectura: NO es G. lucidum europeo en sentido estricto, es G. lingzhi, el reishi asiatico.
Para la mayoria del mercado eso es exactamente lo que se espera y se vende como "reishi",
pero la ETIQUETA debe decir la verdad taxonomica y la ficha tecnica debe registrarlo.
Accion: alinear etiqueta, ficha tecnica y COA. Guardar la secuencia con el expediente del lote.
```

(Cifras ilustrativas. El complejo *G. lucidum / G. lingzhi* es un caso taxonómico real y frecuente.)

## Errores comunes

- **Creer que el ADN prueba que es cuerpo fructífero.** No lo prueba. Nunca.
- **Pedir barcoding sobre un extracto** y concluir "no se detectó la especie" cuando lo que pasó es que el
  ADN estaba destruido.
- **Aceptar un porcentaje de BLAST sin cobertura ni secuencia de referencia.** Pide el electroferograma, la
  secuencia FASTA y el reporte BLAST completo, no solo la conclusión.
- **Usar Sanger en un blend** de varias especies.
- **Confundir proporción de lecturas con proporción de masa** en metabarcoding.
- **Verificar una sola vez y nunca más.** El proveedor cambia de cosecha, de origen y a veces de especie.
  Verificación por lote, o al menos por proveedor y por campaña, con criterio escrito.

## Conexión con otros módulos

→ `245-identidad-de-especie-por-its.md` — el mismo tema desde el producto de hongos.
→ `91-metodos-colorimetricos-y-enzimaticos.md` y `221-medir-beta-glucanos-metodo-megazyme.md` — la pregunta
   que el ADN no responde: cuánto activo y cuánto grano.
→ `238-ergosterol-como-marcador.md` — marcador químico de biomasa fúngica real.
→ `104-metabolomica-y-huella-quimica.md` — autenticación cuando ya no hay ADN.
→ `246-adulteracion-y-fraude-en-suplementos-de-hongos.md` — el panorama del fraude.
→ `284-auditoria-de-proveedor.md` — dónde encaja el barcoding en el control de proveedores.
