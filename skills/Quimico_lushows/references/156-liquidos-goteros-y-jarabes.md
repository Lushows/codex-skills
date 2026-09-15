# 156 — Líquidos, goteros y jarabes (dosis flexible, problema microbiológico)

Los líquidos son el formato favorito de las marcas naturales: el gotero comunica "artesanal", permite titular
la dosis gota a gota y se produce con inversión mínima. También son el formato donde más productos se dañan en
la góndola, porque el agua es el medio donde crece todo. Si vas a vender líquidos, el trabajo de verdad no es
formular el sabor: es **decidir el sistema de conservación y demostrar que funciona**.

Términos: **solución (solution)** = todo disuelto, una sola fase. **Suspensión (suspension)** = sólido disperso
que sedimenta. **Jarabe (syrup)** = solución con alta concentración de azúcar. **Conservante (preservative)** =
sustancia que impide el crecimiento microbiano. **Prueba de reto / eficacia de conservantes (preservative
efficacy test, PET)** = se inoculan microorganismos y se mide si el sistema los controla. **Sinéresis** =
separación de líquido.

## Los cuatro sistemas de conservación

| Sistema | Mecanismo | Nivel típico | Nota |
|---|---|---|---|
| Alcohol | Desnaturaliza proteínas microbianas | ≥ 20–25 % v/v en el producto final | El de las tinturas (`145`) |
| Azúcar (jarabe) | Baja la actividad de agua | ~65 % p/p de sacarosa → a_w ≈ 0,85 | Sabor y calorías altas |
| Glicerina / propilenglicol | Baja a_w, cosolvente | 20–50 % | Apto sin alcohol, sabor dulce |
| Conservantes químicos | Antimicrobiano directo | Según sustancia y pH | Benzoato, sorbato, parabenos |

**El punto que casi todos ignoran:** el benzoato de sodio y el sorbato de potasio solo funcionan en su forma
**no disociada**, es decir a pH ácido.

```
pKa del ácido benzoico ≈ 4,2   |   pKa del ácido sórbico ≈ 4,8

Fracción activa (no disociada) = 1 / (1 + 10^(pH − pKa))

Benzoato a pH 3,0  → 94 % activo
Benzoato a pH 4,2  → 50 % activo
Benzoato a pH 5,5  → 5 % activo    ← prácticamente inútil
Benzoato a pH 7,0  → 0,2 % activo  ← el producto está desprotegido

Conclusión: si tu bebible está a pH 6, el benzoato que pusiste es decoración.
```

Ese cálculo se hace con `Matematicas_lushows` o con `lab-tools/`, no de memoria. Y la consecuencia de diseño es
que **el pH es una decisión de conservación, no solo de sabor**: la mayoría de líquidos conservados con
benzoato/sorbato se formulan a pH 3,0–4,0.

## Solubilidad: el problema real de los extractos

| Material | ¿Se disuelve en agua? | Solución práctica |
|---|---|---|
| Extracto acuoso de hongo (β-glucanos) | Sí, con agitación; puede dar viscosidad | Solución acuosa directa |
| Extracto alcohólico (triterpenos) | No en agua | Tintura hidroalcohólica (`145`) o cosolvente |
| Extracto dual completo | Parcialmente | Cosolvente glicerina/etanol; o suspensión |
| Cannabinoides | **No** (logP ~6–7) | Aceite (`195`), nanoemulsión (`157`) o ciclodextrina (`158`) |

Regla rápida: si el activo es lipofílico, el formato líquido acuoso **no es una opción sin tecnología de
solubilización**. Los "CBD water" que no declaran su sistema de emulsión o son emulsiones o son marketing.

## Los goteros y la mentira de la gota

```
LA GOTA NO ES UNA UNIDAD DE MEDIDA CONFIABLE

  Regla común: 1 mL ≈ 20 gotas.
  Realidad: el volumen de gota depende de la tensión superficial, la viscosidad,
  el diámetro de la punta, el ángulo y de quién aprieta.
  En productos hidroalcohólicos y aceites, se han observado desviaciones grandes
  frente a la regla de 20 gotas.

  QUÉ HACER:
  1. Mide TU gotero: pesa 20 gotas, 5 réplicas, calcula mL/gota con la densidad.
  2. Declara en la etiqueta la dosis en mL y, si quieres, "aprox. N gotas".
  3. Mejor todavía: usa gotero graduado o pipeta dosificadora de 0,5 / 1,0 mL.
```

Un producto que se dosifica en gotas y declara mg por gota sin haber medido su propio gotero está inventando la
dosis. Es corregible en una tarde y casi nadie lo hace.

## Formulación tipo de un bebible

| Componente | Función | % típico |
|---|---|---|
| Agua purificada | Vehículo | 50–85 % |
| Extracto | Activo | 1–15 % |
| Glicerina vegetal | Cosolvente, dulzor, a_w | 10–30 % |
| Etanol | Cosolvente y conservante | 0–25 % |
| Ácido cítrico / citrato | Ajuste y buffer de pH (`23`) | c.s. a pH 3,5 |
| Sorbato de potasio | Conservante (fungicida) | 0,05–0,20 % |
| Benzoato de sodio | Conservante (bactericida) | 0,05–0,20 % |
| Goma xantana | Suspensión / cuerpo | 0,05–0,30 % |
| Saborizante y edulcorante | Palatabilidad (`162`) | c.s. |

Los límites de uso de conservantes en alimentos y suplementos en Colombia, a agosto de 2026, se verifican
contra la normativa sanitaria vigente aplicable al producto (`266`, `272`). No los tomes de esta tabla como
límite legal: son rangos de formulación típicos.

## Cómo se comprueba un líquido

| Ensayo | Método | Por qué |
|---|---|---|
| pH | Potenciómetro calibrado (`22`) | Conservación y estabilidad |
| Densidad | Picnómetro / densímetro | Convertir mg/mL ↔ mg/g |
| Contenido de activo | HPLC / método del marcador | La etiqueta |
| Volumen entregado | Vaciado de N envases | Que el frasco traiga lo que dice |
| Recuento total y patógenos | Microbiología (`100`) | Seguridad |
| **Prueba de reto (PET)** | Inoculación con cepas tipo, seguimiento 28 días | **Demuestra que el conservante sirve** |
| Grado alcohólico | Densimetría corregida a 20 °C | Etiqueta y conservación |
| Aspecto y sedimento | Visual a 0 / 3 / 6 / 12 meses | Estabilidad física (`164`) |

La **prueba de reto** es el ensayo que separa un producto formulado de un producto improvisado. Se inoculan
microorganismos de referencia y se verifica la reducción logarítmica en el tiempo, según el capítulo
farmacopeico correspondiente (USP <51> / Ph. Eur. 5.1.3, `280`). Es un ensayo que se contrata; cuesta, y se
hace **una vez por fórmula**, no por lote.

## Ejemplo aplicado — bebible de melena de león sin alcohol

```
Fórmula (ILUSTRATIVA) para 1,000 L
  Agua purificada                   c.s.p. 1000 mL
  Extracto acuoso de Hericium        60,0 g   (β-glucano 30 % b.s. → 18,0 g de β-glucano/L)
  Glicerina vegetal USP             200,0 mL
  Ácido cítrico                     c.s. a pH 3,6
  Citrato de sodio                    2,0 g    (buffer)
  Sorbato de potasio                  1,5 g    (0,15 %)
  Benzoato de sodio                   1,0 g    (0,10 %)
  Goma xantana                        1,0 g
  Saborizante natural de maracuyá    c.s.

Dosis: 10 mL aportan 180 mg de β-glucano.
Frasco de 250 mL = 25 porciones.

Controles del primer lote:
  pH 3,6 ✔  |  benzoato ~79 % no disociado a pH 3,6 → activo ✔
  PET USP <51> contratada una vez sobre esta fórmula
  β-glucano medido en producto terminado: objetivo 18,0 g/L ± 10 %
  estabilidad: 0/3/6/12 meses a 30 °C/75 % HR (`164`)
```

## Errores comunes

- Poner conservante y no verificar el pH: fuera de rango ácido, no protege.
- Vender un bebible sin prueba de reto y descubrir el problema con producto en el mercado.
- Declarar mg por gota sin haber medido el gotero propio.
- Intentar disolver un extracto lipofílico en agua y entregar un producto que se separa en el anaquel.
- Usar agua de la llave. El agua es materia prima y se analiza (`106`).
- Envasar en caliente sin control y confiar en eso como "pasteurización".
- Olvidar que el azúcar alto y el alcohol conservan pero también son atributos de etiqueta y de mercado.
- No dejar espacio de cabeza ni considerar la expansión térmica en transporte por carretera caliente.

## Conexión con otros módulos

→ `145-extraccion-hidroalcoholica-y-tinturas.md` — el líquido más simple y autoconservado.
→ `23-buffers-y-control-de-ph.md` — cómo se fija y se sostiene el pH.
→ `100-microbiologia-de-producto.md` — qué se mide y qué límites aplican.
→ `157-emulsiones-y-nanoemulsiones.md` — cómo se mete un activo lipofílico en un líquido acuoso.
→ `163-envase-primario-y-compatibilidad.md` — goteros, sellos y compatibilidad del líquido con el plástico.