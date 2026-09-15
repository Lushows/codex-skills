# 40 — Grupos funcionales (por qué una molécula se comporta como se comporta)

Un grupo funcional es el pedacito de la molécula que manda: define si se disuelve en agua o en aceite, si
se oxida al aire, si se rompe con calor, a qué longitud de onda se ve en el detector y si el laboratorio
puede medirlo directo o le toca derivatizarlo. Si aprendes a mirar los grupos funcionales de tus activos
—cannabinoides, terpenos, glucanos, triterpenos, alcaloides fúngicos— puedes predecir estabilidad,
solvente de extracción y método analítico **sin buscar un solo paper**. Es el ahorro más grande del oficio:
evita comprar el equipo equivocado, elegir el solvente equivocado y perder un lote por oxidación.

Términos: **grupo funcional (functional group)** = átomo o conjunto de átomos que le da a la molécula su
reactividad característica. **Fenol (phenol)** = OH pegado directo a un anillo aromático. **Ácido
carboxílico (carboxylic acid)** = -COOH. **Éster (ester)** = -COO-R. **Cromóforo (chromophore)** = parte de
la molécula que absorbe luz UV-visible; es lo que ve el detector DAD.

## Tabla maestra: grupo, polaridad, qué le pasa y cómo se detecta

| Grupo funcional | Fórmula | Polaridad | Debilidad típica | Detección directa |
|---|---|---|---|---|
| Alcano / cadena alquílica | R-CH₂-CH₃ | Muy apolar | Casi inerte | No absorbe UV; GC-FID/MS |
| Alqueno (doble enlace) | C=C | Apolar | Oxidación, isomerización | UV débil (<200 nm); GC-MS |
| Alcohol | R-OH | Media-polar | Oxidación a cetona | Baja UV; sililar para GC (`64`) |
| Fenol | Ar-OH | Polar, ácido débil | Oxidación a quinona | UV fuerte 270–280 nm |
| Ácido carboxílico | R-COOH | Polar, ácido | Descarboxilación con calor | UV según resto; LC-MS modo negativo |
| Éster | R-COO-R' | Media | Hidrólisis (ácido/base) | Según cromóforo; FTIR ~1735 cm⁻¹ |
| Éter | R-O-R' | Media-apolar | Peróxidos con el tiempo | Débil |
| Cetona / aldehído | C=O | Media-polar | Maillard, oxidación (`62`) | UV 270 nm débil; FTIR ~1700 cm⁻¹ |
| Amina (1ª, 2ª, 3ª) | R-NH₂ / R₂NH / R₃N | Polar, básica | Oxidación, pardeamiento | LC-MS modo positivo, excelente |
| Amida | R-CO-NH-R' | Polar | Hidrólisis lenta | UV ~210 nm |
| Fosfato éster | R-O-PO₃H₂ | Muy polar, ácido | Hidrólisis enzimática | LC-MS negativo; mala retención en C18 |
| Glicósido / acetal | azúcar-O-R | Muy polar | Hidrólisis ácida | Sin cromóforo: RID, ELSD o enzimático |

## Los grupos funcionales de tus dos negocios

**Cannabis.** Un cannabinoide como el Δ9-THC tiene tres cosas que explican casi todo su comportamiento:
un **fenol** (por eso da UV fuerte a ~208 y ~230 nm y por eso se oxida), una **cadena pentilo** apolar (por
eso es prácticamente insoluble en agua y sí en etanol, hexano y aceites) y un **anillo pirano** con un doble
enlace en posición 9. La forma ácida, el **THCA**, agrega un **-COOH** que se pierde como CO₂ con calor:
eso es la descarboxilación (`174`). El grupo -COOH cambia la polaridad, cambia el tiempo de retención en
HPLC y cambia la masa: por eso THCA y THC son picos distintos y el factor 0,877 existe (`175`).

**Hongos.** Los β-glucanos son polímeros de glucosa unidos por enlaces **glicosídicos** —acetales— sin
ningún cromóforo. Consecuencia directa y carísima de ignorar: **no se pueden ver con un detector UV**. Por
eso los β-glucanos no se miden por HPLC-UV sino por hidrólisis + medición enzimática de glucosa (`221`).
Los ácidos ganodéricos, en cambio, son triterpenos con **cetonas, hidroxilos y un -COOH**: sí se ven en UV
(~245–255 nm por la cetona conjugada) y sí se hacen por HPLC-DAD (`224`). La psilocibina tiene un **éster
de fosfato** y una **amina terciaria**: por eso es muy polar, retiene mal en C18 clásico y se hidroliza a
psilocina (`251`).

## Ácido, base y el pKa: el grupo que decide a qué pH trabajas

Un grupo ácido o básico cambia de carga con el pH, y la carga cambia solubilidad, extracción y retención.

```
Regla práctica (regla de las 2 unidades de pH):
  pH = pKa - 2  →  ~99 % de la forma NEUTRA (ácidos)  →  se extrae bien a solvente orgánico
  pH = pKa + 2  →  ~99 % de la forma IONIZADA (ácidos) →  se queda en agua

Órdenes de magnitud reportados en la literatura (verificar para tu compuesto):
  ácido carboxílico alifático   pKa ~ 4–5
  fenol                          pKa ~ 9–10
  amina terciaria alifática      pKa ~ 9–10 (del ácido conjugado)
  éster de fosfato (1ª ionización) pKa ~ 1–2
```

Esto es la base de la **extracción ácido-base** de alcaloides (`50`, `30`) y de por qué un método de HPLC
para THCA usa fase móvil ácida: para que el -COOH esté neutro y el pico no se abra.

## Cómo se comprueba qué grupos tiene una molécula

| Pregunta | Técnica | Qué te dice | Módulo |
|---|---|---|---|
| ¿Tiene OH, C=O, COOH? | FTIR | Bandas características de estiramiento | `92` |
| ¿Cuál es el esqueleto completo? | RMN ¹H y ¹³C | Conectividad, número de H, entorno | `94` |
| ¿Fórmula molecular exacta? | HRMS (Q-TOF/Orbitrap) | Masa exacta, error < 5 ppm | `84` |
| ¿Absorbe UV? ¿a qué λ? | DAD (barrido 190–400 nm) | Existencia y tipo de cromóforo | `80` |
| ¿Es ácido o básico? ¿pKa? | Titulación / predicción | A qué pH extraer y correr | `22` |

Bandas FTIR de referencia (números de onda, cm⁻¹): O-H ancho 3200–3600 · N-H 3300–3500 · C-H 2850–3000 ·
C=O de ácido 1700–1725 · C=O de éster 1735–1750 · C=C aromático 1450–1600 · C-O 1000–1300 · P=O 1250–1300.

## Ejemplo aplicado — decidir el detector antes de gastar

Producto: extracto dual de reishi *(Ganoderma lucidum)* que quieres declarar con dos números en la etiqueta.

```
Analito 1: β-glucano
  Grupos funcionales: acetal glicosídico + muchos OH. Cromóforo: NINGUNO.
  → HPLC-UV es IMPOSIBLE. Método correcto: enzimático Megazyme K-YBGL (`221`).
  Valor de ejemplo (ILUSTRATIVO): 28,4 % p/p base seca.

Analito 2: ácidos ganodéricos totales
  Grupos: cetona conjugada + OH + COOH. Cromóforo: SÍ, ~245–255 nm.
  → HPLC-DAD con patrón de ácido ganodérico A (`224`).
  Valor de ejemplo (ILUSTRATIVO): 2,1 % p/p base seca, expresado como ácido ganodérico A.
```

Un proveedor que te ofrezca "β-glucanos por HPLC-UV" o no sabe química o te está vendiendo humo. Ese solo
párrafo ya te pagó la lectura del módulo.

## Errores comunes

- Pedir un análisis por UV de un compuesto sin cromóforo (azúcares, glucanos, ácidos grasos). El laboratorio
  factura igual y el número no significa nada.
- Extraer un alcaloide a pH neutro y luego quejarse del rendimiento: estaba ionizado y se quedó en el agua.
- Confundir la forma ácida con la neutra en la etiqueta: THCA y THC son moléculas distintas, con masa
  distinta; declarar una por la otra puede sacar un producto de cumplimiento (`175`).
- Guardar un extracto rico en fenoles en frasco transparente y con cabeza de aire: fenol + luz + O₂ = quinona
  y color pardo (`47`, `61`).
- Suponer que "polar" es sinónimo de "soluble en agua". La polaridad es un continuo; el criterio útil es el
  logP y el parámetro de solubilidad (`20`, `30`).

## Conexión con otros módulos

→ `41-nomenclatura-organica.md` — cómo se llama cada cosa cuando le escribes al laboratorio.
→ `17-polaridad-y-fuerzas-intermoleculares.md` — por qué el grupo funcional define la solubilidad.
→ `22-acidos-bases-y-ph.md` — pKa y control de carga.
→ `64-derivatizacion-para-analisis.md` — qué hacer cuando el grupo funcional impide el análisis directo.
→ `80-deteccion-uv-dad-y-pureza-de-pico.md` — cromóforos y detección.