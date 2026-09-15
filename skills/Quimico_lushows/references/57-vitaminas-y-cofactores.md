# 57 — Vitaminas y cofactores (qué puedes declarar de verdad y qué se te destruye en el proceso)

Las vitaminas son la única familia de "activos" que tiene un marco regulatorio claro para declarar en
etiqueta: hay valores de referencia, hay métodos oficiales y hay umbrales para decir "fuente de" o "alto en".
Eso las vuelve tentadoras y peligrosas a la vez: son las más fáciles de declarar y las más fáciles de
perder en el proceso. El caso estrella en hongos es la **vitamina D2**, que se genera al irradiar el
ergosterol con UV. Es real, es medible y es declarable — pero solo si se hace el tratamiento, se mide y se
demuestra que sobrevive hasta el final de la vida útil.

Términos: **vitamina (vitamin)** = compuesto orgánico esencial que el cuerpo no sintetiza en cantidad
suficiente. **Cofactor (cofactor)** = molécula que una enzima necesita para funcionar. **Coenzima
(coenzyme)** = cofactor orgánico (NAD⁺, FAD, CoA). **VRN / VDR (valor de referencia de nutrientes / daily
value)** = cantidad de referencia para calcular el % en la etiqueta. **UI (IU, international unit)** =
unidad de actividad; para vitamina D, 1 µg = 40 UI.

## Clasificación y estabilidad: la tabla que decide el proceso

| Vitamina | Tipo | Sensible a | Estabilidad en proceso |
|---|---|---|---|
| A (retinol) / carotenoides | Liposoluble | Luz, O₂, calor | Baja-media |
| **D2 (ergocalciferol)** | Liposoluble | **Luz UV, O₂** | Media; se degrada a taquisterol/lumisterol |
| D3 (colecalciferol) | Liposoluble | Luz, O₂ | Media |
| E (tocoferoles) | Liposoluble | O₂ (se sacrifica) | Actúa como antioxidante (`133`) |
| K | Liposoluble | Luz | Media |
| B1 (tiamina) | Hidrosoluble | **Calor, pH alcalino, sulfitos** | **Baja** |
| B2 (riboflavina) | Hidrosoluble | **Luz** (muy fotolábil) | Media |
| B3 (niacina) | Hidrosoluble | — | **Alta** (la más robusta) |
| B5, B6 | Hidrosoluble | Calor, luz (B6) | Media |
| B9 (folato) | Hidrosoluble | Calor, O₂, luz | Baja |
| B12 (cobalamina) | Hidrosoluble | Luz, agentes reductores | Media |
| **C (ácido ascórbico)** | Hidrosoluble | **O₂, calor, metales, pH** | **La más lábil** |

Regla de formulación: si una vitamina lábil está en el claim, hay que **sobredosificar (overage)** de forma
calculada y demostrada por estabilidad, no a ojo. Y el overage se justifica con datos ante el regulador,
porque lo que se declara debe cumplirse **al final de la vida útil**, no solo al fabricar (`164`, `282`).

## Vitamina D2 en hongos: el caso que sí vale la pena

```
Ergosterol (C₂₈H₄₄O, 396,65 g/mol)
   --[UV-B, ~280–315 nm]-->  Previtamina D2   --[isomerización TÉRMICA]-->  Vitamina D2 (ergocalciferol)
                                                                             C₂₈H₄₄O, 396,65 g/mol
   Reacciones competidoras con sobreexposición: taquisterol y lumisterol (productos NO deseados).
   → Más UV NO es mejor: hay un óptimo de dosis (mJ/cm²) que se determina experimentalmente (`287`).
```

Lo que hay que controlar y registrar para poder declarar:

| Variable | Unidad | Por qué |
|---|---|---|
| Contenido inicial de ergosterol | mg/g base seca | Es la materia prima de la reacción (`238`) |
| Dosis UV aplicada | mJ/cm² (o W/m² × s) | Define la conversión y los subproductos |
| Longitud de onda de la lámpara | nm (UV-B ~280–315) | UV-A no sirve; UV-C daña |
| Espesor / exposición del material | mm, geometría | El UV no penetra: solo actúa en superficie |
| Vitamina D2 final | µg/g y UI/porción | El dato de etiqueta |
| Estabilidad de D2 en el producto | % a 0, 3, 6, 12 meses | Lo que se declara debe durar |

Métodos de medición: HPLC-UV a ~265 nm con purificación previa (saponificación + SPE), o **LC-MS/MS**, que
es lo preferible por especificidad y sensibilidad. Métodos oficiales de referencia: AOAC y EN aplicables a
vitamina D en alimentos; pedir siempre el método usado y su LOQ (`281`).

```
Cálculo de la declaración (ILUSTRATIVO):
  Vitamina D2 medida        : 12,5 µg/g base seca (LC-MS/MS)
  Humedad del polvo         : 5,0 %  → en base tal cual: 12,5 × 0,95 = 11,875 µg/g
  Porción declarada         : 2,0 g  → 23,75 µg por porción
  En UI                     : 23,75 µg × 40 UI/µg = 950 UI por porción
  % del valor de referencia : se calcula contra el VRN vigente en Colombia a la fecha (`272`)
  ⚠ Ejecutar y verificar en código. Y no se declara nada que no se mida por lote (`283`).
```

## Cofactores y compuestos "tipo vitamina" que aparecen en hongos

| Compuesto | Qué es realmente | Cómo se mide | Advertencia |
|---|---|---|---|
| **Ergotioneína** | Aminoácido no proteinogénico con azufre, no una vitamina | HPLC-UV 254 nm o LC-MS/MS, mg/g | No llamarla vitamina (`235`) |
| Niacina (B3) | Vitamina real, presente en hongos | HPLC / microbiológico | Sí declarable si se mide |
| Riboflavina (B2) | Vitamina real | HPLC-fluorescencia | Muy fotolábil |
| Adenosina / cordicepina | Nucleósidos | HPLC-UV 260 nm | Marcadores, no vitaminas (`228`) |
| NAD⁺ / NADH, FAD | Coenzimas del metabolismo | LC-MS/MS | No se declaran como nutriente |
| Coenzima Q10 | Quinona isoprenoide | HPLC-UV 275 nm | No es vitamina; claim regulado |
| Colina, betaína | Nutrientes con marco propio | LC-MS/MS | Verificar el marco vigente |

## Ejemplo aplicado — decidir si vale la pena declarar vitamina D2

```
Escenario (ILUSTRATIVO): polvo de melena de león, porción 2 g, se evalúa añadir tratamiento UV.

Costos y variables a estimar (rutear a economist_lushows / contador_lushows para el número final):
  · Equipo UV-B y su validación de dosis
  · Análisis de ergosterol pre-tratamiento y vitamina D2 post-tratamiento, por lote (`291`)
  · Estabilidad de D2 a 0/3/6/12 meses (`164`)
  · Ajuste del expediente y de la etiqueta (`272`, `286`)

Beneficio: permite un descriptor nutricional respaldado, si el aporte por porción alcanza el umbral
  regulatorio vigente en Colombia a la fecha de la decisión (verificar, `272`).

Decisión honesta: si el producto NO va a medir vitamina D2 por lote, no se declara. Un claim nutricional
sin verificación por lote es un hallazgo de auditoría esperando pasar (`283`, `267`).
```

## Errores comunes

- Declarar vitamina D porque "los hongos tienen vitamina D". Sin irradiación UV, el contenido natural suele
  ser bajo y muy variable; hay que medirlo.
- Confundir ergosterol con vitamina D2. El ergosterol es el **precursor**: declararlo como vitamina D es falso.
- Sobreexponer a UV creyendo que más es mejor y generar taquisterol/lumisterol en vez de D2.
- Declarar vitamina C en un producto en polvo sin overage ni estudio de estabilidad: al sexto mes ya no está.
- Usar UI y µg indistintamente sin el factor (para vitamina D, 1 µg = 40 UI). Cada vitamina tiene su factor.
- Llamar "vitamina" a la ergotioneína o al CoQ10. No lo son, y el marco regulatorio es distinto.
- No proteger de la luz un producto con riboflavina o vitamina D2 y perder el claim en el anaquel.

## Conexión con otros módulos

→ `236-vitamina-d2-y-tratamiento-uv.md` — el módulo dueño del proceso UV.
→ `238-ergosterol-como-marcador.md` — el precursor y su medición.
→ `235-ergotioneina.md` — el compuesto que no es vitamina pero se vende como si.
→ `164-estabilidad-ich-q1-y-vida-util.md` — cómo se demuestra que el claim dura.
→ `272-etiquetado-en-colombia.md` — cómo se declara un nutriente y con qué umbrales.