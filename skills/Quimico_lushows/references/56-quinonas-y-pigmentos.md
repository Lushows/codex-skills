# 56 — Quinonas y pigmentos (el color de la chaga, y cuándo el color es calidad o es daño)

El color es el primer dato analítico que ve un cliente y el que más rápido genera una queja. En hongos y
cannabis, el color viene de tres orígenes químicos distintos y hay que saber cuál es cuál: **pigmentos
propios** (melaninas de chaga, carotenoides), **quinonas** formadas por oxidación de fenoles (daño), y
**melanoidinas** de la reacción de Maillard (daño térmico o proceso, `62`). La chaga negra es el ejemplo
perfecto: su color oscuro es el atributo del producto, pero un extracto de reishi que se oscurece es
degradación. Distinguirlos con método —no con opinión— evita rechazar lotes buenos y aceptar lotes dañados.

Términos: **pigmento (pigment)** = compuesto que da color propio a un material. **Quinona (quinone)** =
producto de oxidación de un fenol; anillo con dos carbonilos. **Melanina (melanin)** = polímero pardo-negro
formado por acoplamiento oxidativo de fenoles/indoles. **Melanoidina (melanoidin)** = polímero pardo de
Maillard, con nitrógeno de aminoácidos. **Cromóforo (chromophore)** = grupo que absorbe luz visible.

## De dónde sale el color: las cuatro rutas

| Ruta | Química | Ejemplo | ¿Es calidad o daño? |
|---|---|---|---|
| Pigmento biosintético | Carotenoides, quinonas propias, melaninas | Melanina de chaga; carotenoides de *Cantharellus* | **Atributo** |
| Oxidación enzimática (PPO/lacasa) | Fenol → quinona → polímero | Hongo cortado que se oscurece; psilocina azul | **Daño** (o marcador de manipulación) |
| Oxidación química (autoxidación) | Radicales + O₂ | Extracto fenólico que se parda en el frasco | **Daño** (`47`) |
| Maillard (no enzimática) | Azúcar reductor + amina, con calor | Polvo tostado, extracto secado caliente | Depende: puede ser proceso o daño (`62`) |

## Química de las quinonas

```
Fenol (incoloro o amarillo pálido)  --[O₂, PPO/lacasa, o pH alto]-->  Semiquinona (radical)
   --> o-QUINONA (amarilla-naranja, MUY reactiva)
   --> acoplamiento con otra quinona, con aminas o con tioles
   --> OLIGÓMEROS y POLÍMEROS pardo-negros (melaninas)

Por qué importa más allá del color:
  · Las quinonas son ELECTRÓFILAS: reaccionan con -SH y -NH₂ de proteínas y aminoácidos.
    Efecto real: pérdida de aminoácidos disponibles y de actividad enzimática.
  · La reacción se AUTOACELERA: una vez inicia, es difícil pararla.
  · Es el mismo mecanismo que vuelve azul a la psilocina (`47`) y pardo al hongo cortado.
```

Cómo se corta, por punto de ataque:

| Punto del mecanismo | Control | Ejemplo práctico |
|---|---|---|
| Enzima (PPO/lacasa) | Inactivación térmica, secado rápido, pH ácido | Escaldado o secado a T controlada (`142`) |
| Oxígeno | Envasado con N₂, vacío, cabeza de aire mínima | Bolsa con barrera + purga |
| Metales catalizadores | Quelantes (ácido cítrico, EDTA) | Agua de proceso tratada |
| Radicales / quinonas | Antioxidantes reductores (ascórbico, sulfitos*) | *Sulfitos: alérgeno declarable (`137`) |
| Sustrato fenólico | No se puede quitar; es el producto | — |

## El caso chaga: cuando el negro es el producto

*Inonotus obliquus* forma un **esclerocio** negro sobre abedul. Su color viene de un complejo
**melanínico-polifenólico** de alto peso molecular, formado por acoplamiento oxidativo de precursores
fenólicos. Datos que hay que manejar con honestidad:

- El complejo melanínico **no es una sustancia definida**: es un polímero heterogéneo. No hay patrón
  certificado ni CAS útil. Por eso se cuantifica por métodos indirectos y comparativos, nunca como
  "melanina X mg/g" con pretensión de exactitud.
- Se reporta comúnmente como "contenido de melanina" por extracción alcalina y precipitación ácida, con
  gravimetría, o como absorbancia a una longitud de onda fija. Ambos son **operacionales**: el resultado
  depende del procedimiento, así que el procedimiento es parte del dato (`91`).
- La chaga trae además **betulina y ácido betulínico del abedul**: son marcadores del sustrato, no del hongo
  (`55`, `60`), y su presencia dice si el material es realmente chaga silvestre sobre abedul.
- Riesgos reales y documentados de la chaga: **oxalato** alto y posible **radiocesio** en material de ciertas
  regiones. Estos sí se miden y sí van en la especificación (`230`, `38`).
- Sobre efectos: la evidencia disponible es mayoritariamente [in vitro] y [animal]. No se afirma efecto
  terapéutico ni preventivo (`268`).

## Pigmentos que sí se cuantifican bien

| Pigmento | Familia | Detección | Unidad |
|---|---|---|---|
| Carotenoides (β-caroteno, licopeno) | Tetraterpenos (`49`) | HPLC-DAD 450–475 nm | µg/g |
| Clorofila a/b | Tetrapirroles | HPLC-DAD 430/660 nm | mg/g |
| Antocianinas | Flavonoides (`51`) | HPLC-DAD 520 nm, pH diferencial | mg cianidina-3-glucósido eq/g |
| Riboflavina (B2) | Flavina | HPLC-fluorescencia | mg/kg |
| Melaninas / melanoidinas | Polímeros | **Solo métodos operacionales** | Absorbancia o % gravimétrico |

**Clorofila en extractos de cannabis:** el verde intenso de un extracto etanólico de flor viene de clorofila
y confiere sabor herbal amargo. Se reduce con etanol frío, tiempos cortos de contacto y filtración con
tierras (bentonita, carbón activado). Ojo: el carbón activado también **retira cannabinoides y terpenos**;
hay que medir antes y después para saber cuánto activo costó el color (`187`).

## Cómo se mide el color de forma objetiva

```
Colorimetría CIE L*a*b* (espectrofotómetro o colorímetro de mano):
  L* = luminosidad (0 negro – 100 blanco)
  a* = verde (−) a rojo (+)
  b* = azul (−) a amarillo (+)

  ΔE = raíz( (ΔL*)² + (Δa*)² + (Δb*)² )    ← diferencia total respecto a un patrón

  Interpretación práctica reportada en literatura de color:
    ΔE < 1     : diferencia no perceptible a simple vista
    ΔE 1–3     : perceptible por un ojo entrenado
    ΔE > 3–5   : perceptible por cualquiera → probable rechazo del cliente
  Verificar la cuenta de ΔE en código, no a mano.

Alternativa barata: absorbancia a 420 nm del extracto (índice de pardeamiento). Operacional pero útil
como carta de control interna (`77`).
```

El valor de esto: convierte "se ve más oscuro" —una discusión— en un número que entra al criterio de
aceptación del lote y al estudio de estabilidad (`164`).

## Ejemplo aplicado — rechazo de lote por color

```
Situación (ILUSTRATIVO): llega un lote de extracto de melena de león visiblemente más oscuro que el patrón.
Medición: L* 48,2 vs patrón 62,7 · a* 6,1 vs 3,0 · b* 21,4 vs 18,9
  ΔE = raíz(14,5² + 3,1² + 2,5²) = 15,1  → muy por encima de cualquier umbral de aceptación.
Diagnóstico diferencial:
  a) Oxidación enzimática/química → medir fenoles totales y comparar perfil HPLC contra el patrón.
  b) Maillard por secado caliente → buscar HMF (5-hidroximetilfurfural) por HPLC, marcador térmico (`62`).
  c) Sustrato contaminante o mezcla de especies → ITS (`245`) y α-glucano (`220`).
Resultado del ensayo: HMF elevado y fenoles sin cambio → causa térmica en el secado por aspersión.
Acción: bajar temperatura de entrada del secador y revalidar; añadir ΔE ≤ 3,0 al criterio de liberación
del lote (`283`). Sin la medición, esto habría sido una discusión de opiniones con el proveedor.
```

## Errores comunes

- Rechazar o aceptar por "se ve bien" sin colorimetría. No es auditable ni negociable con un proveedor.
- Interpretar todo oscurecimiento como oxidación: puede ser Maillard, y el control es distinto (`62`).
- Vender "alto en melanina" con un número de tres decimales. El método es operacional, no absoluto.
- Usar carbón activado para "limpiar" el color y no medir cuánto activo se llevó.
- Confundir el azul de un hongo psilocibio con potencia: es psilocina oxidada, o sea pérdida (`47`).
- Ignorar oxalato y radiocesio en chaga por concentrarse en el color (`230`).
- Poner sulfitos como antioxidante sin declararlos: son alérgeno de declaración obligatoria (`137`, `272`).

## Conexión con otros módulos

→ `47-oxidacion-y-degradacion-de-productos-naturales.md` — el mecanismo que genera quinonas.
→ `62-maillard-y-pardeamiento.md` — la otra ruta del color pardo.
→ `51-polifenoles-y-flavonoides.md` — los precursores fenólicos.
→ `229-chaga-inonotus-quimica.md` y `230-chaga-riesgos-oxalato-y-radiocesio.md` — el caso chaga completo.
→ `90-espectroscopia-uv-visible.md` — la técnica detrás de la medición de color.
