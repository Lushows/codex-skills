# 245 — Identidad de especie por ITS (cómo se prueba que lo que compraste es lo que dice ser)

En polvo, todos los hongos se parecen. La morfología desaparece con la molienda y la química no siempre
distingue especies cercanas: un *Ganoderma* chino, uno colombiano y una especie hermana pueden dar perfiles
de triterpenos parecidos. La única prueba de identidad que aguanta una discusión es el **ADN**, y en hongos
el marcador aceptado internacionalmente es la región **ITS**. Este módulo explica qué es, qué prueba, qué
NO prueba y cómo se pide.

Términos: **ITS (internal transcribed spacer)** = región del ADN ribosomal, el código de barras oficial de
los hongos. **DNA barcoding** = identificar una especie comparando una secuencia con una base de datos.
**BLAST** = el algoritmo que compara tu secuencia contra GenBank. **amplicón (amplicon)** = el fragmento de
ADN copiado por PCR.

## Por qué ITS y no otro gen

En 2012 el consorcio internacional de código de barras adoptó formalmente ITS como marcador primario para
Fungi, porque tiene la mejor relación entre variación entre especies y facilidad de amplificación. Para
*Ganoderma*, un estudio publicado en PLOS ONE (2020) mostró que ITS más análisis filogenético identificó
correctamente *G. lingzhi* en siete suplementos comerciales, y demostró que un simple "mejor resultado de
BLAST" puede ser insuficiente sin el árbol filogenético que lo respalde. Esa es la lección práctica: pide
secuencia y análisis, no solo un porcentaje de coincidencia.

| Marcador | Uso | Nota |
|---|---|---|
| ITS1-5.8S-ITS2 | Estándar primario en hongos | Primers ITS1F/ITS4 los más usados |
| LSU (28S) | Complementario a nivel de género | Más conservado |
| TEF1-α, RPB2 | Resolución fina en géneros difíciles | Para *Ganoderma*, *Cordyceps*, *Trametes* |
| ADN de cloroplasto | No aplica | Los hongos no tienen cloroplasto — si el informe lo menciona, algo está mal |

## Qué prueba y qué no prueba

| ITS SÍ prueba | ITS NO prueba |
|---|---|
| Qué especie aportó el ADN de la muestra | **Qué parte del hongo** (micelio o cuerpo fructífero) |
| Presencia de una especie distinta a la declarada | Cuánto activo tiene |
| Presencia de un contaminante fúngico dominante | La proporción de cada especie en una mezcla |
| Que el material era biológico y tenía ADN íntegro | Si el extracto tiene maltodextrina |

Esa primera limitación es enorme y hay que decirla siempre: **ITS no distingue micelio de cuerpo fructífero**,
porque el ADN es el mismo organismo. La distinción micelio/fructífero se hace por química (α-glucano alto =
grano; ver `218`, `220`), no por ADN. Vender un análisis de ITS como prueba de "cuerpo fructífero" es un
truco comercial.

Segunda limitación: los **extractos muy procesados pueden no tener ADN amplificable**. Calor, alcohol y pH
extremos fragmentan el ADN. Un "no amplificó" no siempre significa fraude; puede significar que el método no
aplica a esa matriz. En esos casos se identifica la materia prima **antes** de extraer y se controla la
cadena de custodia (`109`).

## Cómo se mide / cómo se comprueba

```
Flujo del ensayo:
1. Muestra representativa (mínimo 1–5 g de polvo homogeneizado)
2. Extracción de ADN (kit CTAB o columna de sílice)
3. PCR de ITS con primers ITS1F / ITS4
4. Verificación del amplicón en gel o electroforesis capilar (~600–800 pb esperados)
5. Secuenciación Sanger bidireccional (o metabarcoding por NGS si hay mezcla)
6. Ensamblaje de la secuencia consenso y control de calidad (Phred, trazas limpias)
7. BLAST contra GenBank/UNITE + análisis filogenético con secuencias de referencia de tipo
8. Informe: secuencia depositada, % identidad, cobertura, árbol, conclusión
```

Lo que debes exigir en el informe, sin excepción:

- La **secuencia completa** en formato FASTA (para que otro laboratorio pueda repetir el análisis).
- **% de identidad y % de cobertura** contra la referencia, no solo "coincide".
- Que la referencia sea de una **secuencia de tipo o de voucher** confiable, no una entrada anónima.
- Si es mezcla: **metabarcoding (NGS)**, porque Sanger sobre una mezcla da una secuencia ilegible.
- Cadena de custodia de la muestra (`109`).

Costo y tiempo típicos: ITS por Sanger, del orden de USD 60–150 por muestra y 5–15 días hábiles según país
y laboratorio (ILUSTRATIVO — pide cotización; en Colombia hay laboratorios universitarios que lo hacen).

## Ejemplo aplicado (ILUSTRATIVO) — auditoría de tres proveedores de reishi

```
Muestra R-01: ITS 99,7 % identidad / 100 % cobertura con Ganoderma lingzhi (referencia de tipo). CONFORME.
Muestra R-02: ITS 99,1 % con Ganoderma applanatum. NO CONFORME — especie distinta a la declarada.
Muestra R-03: PCR sin amplificación (ADN degradado, extracto seco por aspersión a alta temperatura).
              → No concluyente. Se solicita muestra de la materia prima antes de extraer.

Química complementaria del mismo lote R-01:
  β-glucano 30,2 % / α-glucano 3,4 % p/p b.s. → coherente con cuerpo fructífero.
```

Conclusión operativa: identidad por ADN **más** perfil de glucanos. Ninguno de los dos solo alcanza.

## Errores comunes

- **Aceptar "identificado por ADN" sin la secuencia.** Sin FASTA no hay auditoría posible.
- **Usar ITS para probar "cuerpo fructífero".** No lo prueba. Es el error de interpretación más caro.
- **Correr Sanger sobre una mezcla de especies.** Da cromatogramas superpuestos e ilegibles; para mezclas,
  NGS.
- **Confiar en el mejor hit de BLAST.** Muchas entradas de GenBank están mal identificadas; el árbol
  filogenético es lo que da confianza.
- **Analizar el extracto en vez de la materia prima.** Si el ADN está degradado, pierdes tiempo y plata.
- **Hacerlo una sola vez.** Es un control de proveedor y de lote, no un trofeo de una sola auditoría.

## Conexión con otros módulos

→ `103-identidad-por-adn-its-y-barcoding.md` — la técnica en general.
→ `218-el-fraude-del-micelio-en-grano.md` y `220-alfa-glucanos-y-almidon-el-confusor.md` — lo que ITS NO
detecta y sí detecta la química.
→ `246-adulteracion-y-fraude-en-suplementos-de-hongos.md` — dónde encaja la sustitución de especie.
→ `60-quimiotaxonomia-y-marcadores.md` — identidad por química.
→ `284-auditoria-de-proveedor.md` — cómo se le exige al proveedor.
→ `109-cadena-de-custodia-y-envio-de-muestras.md` — para que el resultado tenga valor probatorio.