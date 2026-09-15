# 227 — Cordyceps: química de un nombre que cubre varias cosas

"Cordyceps" es una palabra comercial que agrupa al menos tres materiales distintos: el hongo silvestre del
altiplano tibetano, una especie cultivable de color naranja, y una biomasa de fermentación con nombre de
cepa. Tienen química distinta y precios que se diferencian en dos órdenes de magnitud. Aquí aprendes a
distinguirlos antes de comprar, y a saber qué marcador aplica a cada uno.

Términos: **estroma (stroma)** = la parte fúngica visible, análoga al cuerpo fructífero. **cordicepina
(cordycepin)** = 3'-desoxiadenosina, nucleósido característico de *Cordyceps militaris*. **adenosina
(adenosine)** = nucleósido común, usado como marcador en farmacopea china. **CS-4** = cepa de micelio
cultivada en fermentación, muy usada comercialmente. **anamorfo (anamorph)** = forma asexual de un hongo.

## Los tres materiales que se venden como "cordyceps"

| Material | Nombre científico | Cómo se produce | Marcador principal |
|---|---|---|---|
| Cordyceps silvestre ("yartsa gunbu") | *Ophiocordyceps sinensis* (antes *Cordyceps sinensis*) | Recolección en el Himalaya sobre larva de lepidóptero | Adenosina; cordicepina baja o ausente |
| Cordyceps militaris cultivado | *Cordyceps militaris* | Cultivo sobre arroz/sustrato en bandeja; estroma naranja | **Cordicepina** alta |
| Biomasa CS-4 | Cepa de micelio (*Paecilomyces hepiali* o similar según el productor) | Fermentación líquida | Adenosina; identidad discutida |

Hechos comerciales que hay que decir en voz alta:

- El silvestre auténtico está entre los productos naturales más caros del mundo y es prácticamente
  **imposible** que esté en un suplemento de precio normal. Reportes de autenticación por ADN indican que,
  de decenas de muestras enviadas como *C. sinensis* a lo largo de años, casi ninguna resultó auténtica
  (reportado por laboratorios de autenticación y recogido en análisis de mercado 2026; **verifica la fuente
  primaria antes de citarlo públicamente**).
- Casi todo lo que se vende como "cordyceps" es *C. militaris* cultivado o biomasa CS-4.
- *C. militaris* cultivado sobre arroz **también puede llegar con grano**: aplica la misma auditoría de
  α-glucano que a cualquier otro (ver `218`, `220`).

## Familias de compuestos

| Familia | Ejemplos | Solubilidad | Método |
|---|---|---|---|
| Nucleósidos | Cordicepina, adenosina, guanosina, uridina | Agua / metanol acuoso | HPLC-UV 260 nm, LC-MS/MS (`228`) |
| Polisacáridos / β-glucanos | β-(1→3)/(1→6) | Agua caliente | Megazyme K-YBGL (`221`) |
| Esteroles | Ergosterol y derivados | Alcohol | HPLC-UV 282 nm (`238`) |
| Pigmentos carotenoides | Cordyxantina y similares (color naranja) | Lipídica | HPLC-DAD |
| Manitol (cordicepínico) | Alcohol de azúcar; a veces se declara como marcador | Agua | HPLC-RID, GC |

Ojo con el manitol: algunas fichas declaran "ácido cordicepínico" y eso es simplemente D-manitol, un
azúcar-alcohol común. Es un marcador débil de calidad.

## Rangos reportados

- **Cordicepina: *C. militaris* ≫ *O. sinensis*.** Fuentes de la industria citan un estudio de 2008 en
  *Journal of Agricultural and Food Chemistry* según el cual *C. militaris* contiene hasta unas **90 veces**
  más cordicepina que el *C. sinensis* silvestre (citado por Real Mushrooms y otros distribuidores;
  verifica la fuente primaria antes de usarlo en material técnico).
- En cultivos optimizados de *C. militaris*, un trabajo con espectrometría de masas MALDI reportó
  cordicepina de **136 mg/g en micelio** y 148,39 mg/mL en caldo de fermentación al día 20 de cultivo
  (PMC8424359). Son valores de cultivo optimizado en laboratorio, **no** lo que esperas de un polvo
  comercial: no los uses como referencia de compra.
- Para producto comercial no hay un rango de consenso publicado que sirva de especificación universal.
  Construye la tuya con tus propios lotes (ver `282`).

## Cómo se mide / cómo se comprueba

| Marcador | Método | Unidad y base |
|---|---|---|
| Cordicepina y adenosina | HPLC-UV a 260 nm; LC-MS/MS para confirmar | `mg/g base seca` (`228`) |
| β-glucano / α-glucano | Megazyme K-YBGL | `% p/p base seca` |
| Identidad de especie | Secuenciación ITS | % de identidad (`245`) |
| Biomasa fúngica | Ergosterol HPLC-UV 282 nm | `mg/g base seca` |
| Metales pesados | ICP-MS | `mg/kg base seca` |
| Humedad | Karl Fischer | `% p/p` |

La combinación **ITS + cordicepina + α-glucano** resuelve el 90 % de las dudas sobre un cordyceps
comercial: qué especie es, si tiene el nucleósido característico y cuánto grano trae.

## Ejemplo aplicado — auditar una oferta

**(ILUSTRATIVO)**

```
Ficha del proveedor: "Cordyceps sinensis extract 10:1, 0,3 % cordycepin"

Preguntas obligatorias:
 1. Especie: si es "sinensis" y hay cordicepina medible, algo no cuadra.
    -> pedir ITS. Casi siempre vuelve C. militaris o una cepa de fermentacion.
 2. Metodo de la cordicepina: HPLC-UV con patron? cual patron? LOQ?
 3. Material: estroma o micelio? con grano o sin grano?
 4. alfa-glucano: si viene >30 % p/p b.s., el "10:1" no significa nada.

Resultado tipico del ensayo independiente (ilustrativo):
    ITS -> Cordyceps militaris (99,4 %)
    cordicepina 2,8 mg/g base seca (HPLC-UV 260 nm, patron certificado)
    beta-glucano 14,2 % / alfa-glucano 21,7 % p/p b.s. -> hay grano
Decision: renegociar precio o cambiar de material.
```

## Qué se puede y qué no se puede afirmar

- Se puede declarar: "cordicepina 2,8 mg/g base seca (HPLC-UV, patrón certificado)" y la dosis por porción.
- Se puede decir la especie real y el material real. Si es *C. militaris*, dilo: es un buen producto, no
  necesita disfrazarse de silvestre.
- Se puede mencionar uso tradicional marcándolo `[tradicional]`.
- **No se puede** afirmar que mejora el rendimiento deportivo como hecho establecido: la evidencia clínica
  es limitada, con estudios pequeños y resultados heterogéneos, muchas veces con mezclas de varios hongos
  (ver `248`). Y **nunca** claims de enfermedad (ver `268`).
- No traslades resultados `[animal]` de cordicepina purificada a un polvo con miligramos por gramo: no es
  la misma dosis ni la misma molécula aislada (ver `249`).

## Errores comunes

- Pagar precio de silvestre por producto cultivado. Casi nunca hay silvestre real.
- Comprar "CS-4" creyendo que es *C. sinensis*: es una cepa de fermentación con identidad propia.
- Aceptar cordicepina declarada sin método ni LOQ; en muchos productos está por debajo del límite de
  cuantificación (ver `73`).
- Olvidar el α-glucano: el *C. militaris* se cultiva sobre arroz y el grano puede venirse en el polvo.
- Confundir manitol ("ácido cordicepínico") con cordicepina. No tienen nada que ver.

## Conexión con otros módulos

→ `228-cordicepina-y-adenosina-analisis.md` — el método del marcador, en detalle.
→ `237-nucleosidos-y-nucleotidos-fungicos.md` — la familia química completa.
→ `245-identidad-de-especie-por-its.md` — cómo se prueba qué especie compraste.
→ `218-el-fraude-del-micelio-en-grano.md` — la auditoría del grano, que aquí también aplica.
→ `249-dosificacion-de-hongos-funcionales.md` — cómo se traduce un mg/g a una porción.