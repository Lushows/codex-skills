# 58 — Rutas biosintéticas: mevalonato y MEP (de dónde salen los terpenos y los cannabinoides)

Entender la biosíntesis no es lujo académico: es lo que te dice **por qué** el perfil químico cambia con el
cultivo, qué se puede aumentar y qué no, por qué los hongos no hacen los mismos terpenos que las plantas, y
por qué un cannabinoide es en realidad un híbrido de dos rutas distintas. Con este mapa puedes leer un
resultado de laboratorio y saber si tiene sentido biológico o si alguien mezcló material. Es la base de la
quimiotaxonomía (`60`) y de cualquier discusión seria con un químico de universidad.

Términos: **biosíntesis (biosynthesis)** = fabricación de una molécula por un organismo vivo, paso a paso
con enzimas. **Precursor (precursor)** = molécula de partida. **IPP / DMAPP** = isopentenil difosfato y su
isómero dimetilalil difosfato; las dos piezas C₅ universales. **Prenilación (prenylation)** = pegar una
cadena isoprenoide a otra molécula. **Ruta convergente (convergent pathway)** = cuando dos rutas distintas
aportan piezas al mismo producto final.

## Las dos fábricas de la unidad C₅

Todos los terpenos del planeta se construyen con IPP y DMAPP. Pero hay **dos rutas** para fabricarlos, y
quién tiene cuál define la química del organismo.

| | Ruta del mevalonato (MVA) | Ruta MEP / DOXP |
|---|---|---|
| Precursor | Acetil-CoA (×3) | Piruvato + gliceraldehído-3-fosfato |
| Localización celular | Citosol / retículo | **Plástido** (cloroplasto) |
| Enzima clave | HMG-CoA reductasa | DXS y DXR |
| Quién la tiene | **Hongos**, animales, levaduras, citosol vegetal | Plantas (plástido), la mayoría de bacterias, algas |
| Productos típicos | **Sesquiterpenos (C15), triterpenos (C30), esteroles** | **Monoterpenos (C10), diterpenos (C20), carotenoides** |
| Relevancia | Ergosterol y ácidos ganodéricos vienen de aquí | Mirceno, limoneno y el GPP de los cannabinoides |

**Consecuencia número uno para hongos:** los hongos **solo tienen MVA**. Por eso su química de terpenos es
de sesquiterpenos y triterpenos —ergosterol (`238`), ácidos ganodéricos (`55`), erinacinas diterpénicas
(`226`)— y no de monoterpenos volátiles tipo limoneno. Si un "extracto de hongo" reporta un perfil rico en
monoterpenos, hay algo añadido: es un aroma, no el hongo.

**Consecuencia número uno para cannabis:** en la planta conviven las dos rutas. Los **monoterpenos** del
aroma (mirceno, limoneno, pineno) se hacen mayoritariamente por **MEP en el plástido**; los
**sesquiterpenos** (β-cariofileno, humuleno) por **MVA en el citosol** (`49`). Por eso responden distinto al
ambiente y por eso se pierden distinto en el proceso.

## El ensamblaje: de C₅ a lo que te importa

```
Acetil-CoA ×3 ──MVA──┐
                     ├──►  IPP  ⇄  DMAPP     (isomerasa)
Piruvato + G3P ─MEP──┘        │
                              ▼
        DMAPP + IPP  →  GPP  (C10, geranil-PP)      → MONOTERPENOS (mirceno, limoneno, pineno)
        GPP   + IPP  →  FPP  (C15, farnesil-PP)     → SESQUITERPENOS (β-cariofileno, humuleno)
        FPP   + FPP  →  escualeno (C30)             → LANOSTEROL → ERGOSTEROL, ÁCIDOS GANODÉRICOS
        FPP   + IPP  →  GGPP (C20)                  → DITERPENOS (erinacinas)
        GGPP ×2      →  fitoeno (C40)               → CAROTENOIDES
```

Este esquema explica una cosa práctica: los precursores compiten. Si el organismo desvía FPP hacia
esteroles, hay menos para sesquiterpenos. Por eso no se puede "subir todo" a la vez con cultivo (`185`).

## La biosíntesis de cannabinoides: dos rutas que se encuentran

Este es el punto que hay que saber explicar de memoria, porque desmonta la idea de que los cannabinoides son
"solo terpenos".

```
RAMA 1 — POLICÉTIDA (ver `59`)
  Ácido hexanoico → hexanoil-CoA
  hexanoil-CoA + 3 × malonil-CoA  --[TKS, tetracétido sintasa]-->  tetracétido
  tetracétido  --[OAC, olivetolic acid cyclase]-->  ÁCIDO OLIVETÓLICO  (el anillo aromático con el COOH)
     · Sin OAC, el intermediario cicla solo a olivetol (sin COOH): por eso hacen falta las dos enzimas.
     · Con ácido butírico en vez de hexanoico → ácido divarínico → línea de las VARINAS (THCV, CBDV) (`178`)

RAMA 2 — TERPÉNICA (MEP, plástido)
  → GPP (geranil difosfato, C10)

CONVERGENCIA — PRENILACIÓN
  Ácido olivetólico + GPP  --[prenil transferasa / CBGA sintasa]-->  CBGA (ácido cannabigerólico)
     ← CBGA es la MADRE de todos los cannabinoides

RAMIFICACIÓN FINAL — oxidociclasas dependientes de FAD
  CBGA --[THCA sintasa]--> THCA        ← estereoespecífica: da (−)-trans (`43`)
  CBGA --[CBDA sintasa]--> CBDA
  CBGA --[CBCA sintasa]--> CBCA
  CBGA que no se convierte queda como CBGA residual

POST-COSECHA (ya no es biosíntesis, es química, `44`)
  THCA --calor--> Δ9-THC + CO₂        (descarboxilación, `174`)
  Δ9-THC --O₂/luz--> CBN              (oxidación, `47`)
```

De aquí caen tres conclusiones duras:

1. **El quimiotipo es genético.** Que una planta sea "tipo I" (THC dominante), "tipo II" (mixta) o "tipo III"
   (CBD dominante) depende de qué alelos de sintasas tenga. No se cambia con nutrición (`170`, `171`).
2. **En la planta viva casi todo está en forma ácida.** Un COA que reporte mucho Δ9-THC y poco THCA en
   material fresco delata calor en el proceso o un error de método (`173`).
3. **El CBN no es biosintético.** Es degradación. Su presencia alta habla de almacenamiento, no de genética.

## Biosíntesis en hongos: lo que sí y lo que no

- **Ergosterol** viene de escualeno → lanosterol → (varios pasos) → ergosterol. Es la misma rama que en
  animales produce colesterol; por eso los antifúngicos azólicos atacan esa ruta.
- **Ácidos ganodéricos**: derivan de lanosterol, con oxidaciones sucesivas mediadas por citocromos P450.
  Eso explica su alto grado de oxigenación y su enorme variabilidad entre cepas (`55`).
- **Erinacinas** (micelio de *Hericium*): diterpenos de tipo cyathano, vía GGPP. **Hericenonas** (cuerpo
  fructífero) son de origen **policétido** con una parte prenilada: rutas distintas, órganos distintos. Ese
  solo hecho justifica que micelio y cuerpo fructífero no sean intercambiables (`217`, `226`, `59`).
- **Psilocibina**: viene del **triptófano** (ruta del shikimato, `59`), no del mevalonato. La skill cubre la
  bioquímica descriptiva; no cubre producción (`253`).

## Cómo se comprueba una hipótesis biosintética

| Pregunta | Herramienta | Resultado esperado |
|---|---|---|
| ¿Este compuesto viene de esta ruta? | Marcaje isotópico (¹³C-acetato, ¹³C-glucosa) + RMN/HRMS | Patrón de enriquecimiento en posiciones específicas |
| ¿Está el gen? | PCR / secuenciación del genoma | Presencia de la sintasa (p. ej. THCAS) |
| ¿Se expresa? | RT-qPCR, transcriptómica | Nivel de ARN mensajero |
| ¿Se acumula el intermediario? | LC-MS del perfil completo | CBGA residual alto = cuello de botella |
| ¿El perfil es coherente? | Metabolómica no dirigida + quimiometría | Agrupamiento por quimiotipo (`104`, `105`) |

## Ejemplo aplicado — leer un COA y detectar incoherencia biosintética

```
COA de flor fresca, secada a temperatura ambiente (ILUSTRATIVO):
  THCA 14,2 %  ·  Δ9-THC 6,8 %  ·  CBGA 0,4 %  ·  CBN 0,9 %  ·  CBDA 0,1 %

Lectura biosintética:
  · Δ9-THC de 6,8 % en material que "no se calentó" es incoherente: en planta la forma dominante es la ácida.
  · CBN de 0,9 % indica oxidación avanzada, es decir tiempo + oxígeno + luz (`47`).
  → Hipótesis: el material se secó caliente o lleva mucho tiempo almacenado, no es "flor fresca".
Verificación: repetir el análisis con muestreo propio (`66`) y pedir el cromatograma, no solo la tabla.
Impacto: el THC total no cambia mucho por descarboxilación, pero el CBN alto sí baja el valor comercial
y la vida útil restante (`175`, `204`).
```

## Errores comunes

- Creer que se puede "subir el CBD" de una planta tipo I con fertilización. El quimiotipo es genético.
- Suponer que los hongos producen monoterpenos. No tienen la ruta MEP.
- Presentar el CBN como cannabinoide "producido por la planta". Es un degradante.
- Comprar micelio esperando hericenonas (son del cuerpo fructífero) o cuerpo fructífero esperando erinacinas
  (son del micelio). Rutas y órganos distintos (`226`).
- Ignorar el CBGA residual: es información de proceso y de genética que casi nadie lee.
- Confundir "biosíntesis" con "síntesis de laboratorio" en un expediente regulatorio: el origen cambia la
  categoría del ingrediente (`275`, `278`).

## Conexión con otros módulos

→ `59-ruta-del-shikimato-y-policetidos.md` — la otra mitad de la historia: aromáticos y policétidos.
→ `49-terpenos-y-terpenoides.md` — los productos de esta ruta y sus propiedades.
→ `172-biosintesis-de-cannabinoides.md` — el módulo dueño del detalle en cannabis.
→ `60-quimiotaxonomia-y-marcadores.md` — usar el perfil biosintético para identificar especie.
→ `55-esteroles-y-triterpenos.md` — ergosterol y ácidos ganodéricos como productos MVA.
