# 229 — Chaga (*Inonotus obliquus*): química de un material que no es una seta

El chaga rompe todas las reglas del bloque: no es un cuerpo fructífero, no se cultiva a escala, es silvestre
por definición, y su composición depende del árbol donde creció. Eso lo hace químicamente fascinante y
comercialmente riesgoso: es el hongo del catálogo con más problemas de autenticidad, de contaminantes y de
seguridad de uso (ver `230`). Este módulo cubre la química; los riesgos tienen módulo propio porque son
serios.

Términos: **esclerocio (sclerotium)** = masa compacta y endurecida de hifas con reservas; en chaga es el
"conk" negro sobre el abedul. **conk** = la excrecencia visible en el tronco. **betulina (betulin)** y
**ácido betulínico (betulinic acid)** = triterpenos que el hongo toma o transforma de la corteza del abedul.
**inotodiol** = triterpeno característico del chaga. **melanina (melanin)** = pigmento negro polimérico de
la capa externa.

## Qué es exactamente el material

El chaga que se vende es el **esclerocio**, la costra negra que crece sobre abedules (*Betula* spp.) vivos,
durante años. La parte interna es café-anaranjada (el "cork"), la externa es negra y rica en melanina. El
verdadero cuerpo fructífero del hongo aparece bajo la corteza cuando el árbol muere y prácticamente no se
comercializa.

Consecuencias:

- **No es cultivable a escala** en la forma que se vende. Lo que sí se cultiva es **micelio de
  *I. obliquus***, generalmente sobre grano, y ahí entra otra vez el problema de `218`. Un estudio
  comparativo de suplementos de chaga con técnicas analíticas complementarias encontró niveles de β-glucano
  **más bajos en productos de micelio sobre grano que en esclerocio auténtico** (*International Journal of
  Molecular Sciences* / MDPI, 2025; 26(7):2970).
- **La química depende del huésped.** Un trabajo comparó contenido químico y actividad citotóxica de chaga
  crecido sobre *Betula pendula* y *B. pubescens* y encontró diferencias (PMC11357148, 2024).
- **Acumula lo del ambiente**: potasio-40, cesio radiactivo, metales. Ver `230`.

## Familias de compuestos

| Familia | Ejemplos | Dónde | Solubilidad |
|---|---|---|---|
| Triterpenos | Betulina, ácido betulínico, inotodiol, lanosterol, trametenólico | Capa interna | Alcohol / lipídica |
| Melaninas | Complejos poliméricos oscuros | Costra externa | Álcali; parcialmente agua |
| Polisacáridos / β-glucanos | β-(1→3)/(1→6) | Todo el esclerocio | Agua caliente |
| Polifenoles | Ácidos fenólicos, complejos tipo "cromógeno" | Todo | Agua/alcohol |
| Ergosterol y derivados | Peróxido de ergosterol | Todo | Alcohol |
| **Oxalatos** | Ácido oxálico y oxalato de calcio | Todo | Agua | 

Ese último renglón es el que casi nadie pone en la ficha y el que puede hacerle daño a alguien. Va completo
en `230`.

Nota importante sobre la betulina: **viene del abedul**, no la fabrica el hongo desde cero. Un chaga con
mucho ácido betulínico refleja el árbol tanto como el hongo. Y hay chaga cultivado con distintas fuentes de
betulina en el medio precisamente para modular eso (estudio de transcriptoma de *I. obliquus* cultivado con
distintas fuentes de betulina, PMC6770048, 2019).

## Cómo se mide / cómo se comprueba

| Marcador | Método | Unidad y base |
|---|---|---|
| β-glucano / α-glucano | Megazyme K-YBGL | `% p/p base seca` (`221`) |
| Betulina, ácido betulínico, inotodiol | HPLC-DAD (baja longitud de onda, ~205–210 nm) o LC-MS/MS | `mg/g base seca` |
| Ergosterol | HPLC-UV 282 nm | `mg/g base seca` (`238`) |
| Polifenoles totales | Folin-Ciocalteu (inespecífico, decláralo así) | `mg GAE/g base seca` |
| Melanina | Extracción alcalina y gravimetría / absorbancia | `% p/p base seca`, semicuantitativo |
| **Oxalato total y soluble** | Enzimático (oxalato oxidasa) o cromatografía iónica | `mg/g base seca` (`230`) |
| Identidad de especie | Secuenciación ITS | % identidad (`245`) |
| Metales pesados | ICP-MS | `mg/kg base seca` (`243`) |
| Radionúclidos (si es silvestre importado) | Espectrometría gamma | `Bq/kg base seca` (`230`, `38`) |

Los triterpenos del chaga tienen cromóforo débil: absorben en UV bajo, donde la línea base es sucia. Por eso
la confirmación por masas vale la pena si el número va a sostener una etiqueta.

## Ejemplo aplicado — plan de compra de chaga para BIO-SETA

**(ILUSTRATIVO)**

```
Riesgo del material: silvestre, sin trazabilidad de origen, acumulador.

Requisitos minimos al proveedor:
  origen geografico y especie de abedul huesped, documentado
  identidad ITS: Inonotus obliquus
  beta-glucano y alfa-glucano (K-YBGL)  -> descarta micelio en grano
  ergosterol                            -> confirma biomasa fungica
  metales pesados por ICP-MS
  espectrometria gamma (Cs-137, K-40) si el origen es Europa del Este o Siberia
  oxalato total                         -> para poder definir la porcion (ver 230)

Sin esos seis renglones, el material no entra. El chaga es el unico del catalogo
donde la analitica de seguridad pesa mas que la de potencia.
```

## Qué se puede y qué no se puede afirmar

Aquí hay que ser especialmente severo, porque la literatura de chaga está llena de estudios oncológicos
`[in vitro]` que la gente convierte en publicidad:

- **Se puede** declarar composición medida (β-glucanos, triterpenos, polifenoles) con método, unidad y base.
- **Se puede** decir "usado tradicionalmente en Siberia y el norte de Europa" `[tradicional]`.
- **No se puede**, bajo ninguna circunstancia, sugerir acción sobre cáncer. Existen estudios de citotoxicidad
  en líneas celulares (por ejemplo, sobre A549 y BEAS-2B, PMC6142110, 2018) y trabajos sobre triterpenoides
  de chaga e inhibición de dihidrofolato reductasa (PMC11591880, 2024), todos `[in vitro]`. Convertir eso en
  un mensaje de venta es exactamente el claim que ya le costó caro a BIO-SETA (ver `268`).
- **No se puede** omitir la advertencia de oxalatos si vendes chaga (ver `230`).

## Errores comunes

- Comprar chaga sin origen documentado. Es un producto silvestre: el origen es parte de la especificación.
- Aceptar "chaga extract 30 % polysaccharides" de micelio en grano (ver `218`, `222`).
- Declarar ácido betulínico sin medirlo, asumiendo que "todo chaga lo tiene".
- No medir oxalatos y recomendar consumo diario alto. Hay reportes de daño renal documentados (`230`).
- Usar Folin-Ciocalteu ("polifenoles totales") como si fuera una medida de potencia específica.
- Ignorar la radiactividad en material del este de Europa o Siberia (`230`, `38`).

## Conexión con otros módulos

→ `230-chaga-riesgos-oxalato-y-radiocesio.md` — el módulo de seguridad, obligatorio si vendes chaga.
→ `238-ergosterol-como-marcador.md` — confirmar que hay hongo real.
→ `243-metales-pesados-en-hongos.md` — por qué los acumuladores necesitan ICP-MS.
→ `55-esteroles-y-triterpenos.md` — la química de la familia.
→ `268-claims-prohibidos-el-caso-bioseta.md` — las frases que no se escriben.