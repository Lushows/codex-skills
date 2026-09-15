# 206 — Farmacología del CBD (una molécula promiscua con evidencia desigual)

El cannabidiol es el cannabinoide más vendido del mundo y, paradójicamente, el peor entendido. No es
"el cannabinoide que no pega" y ya: es una molécula que interactúa con decenas de dianas moleculares, que
tiene un medicamento aprobado con evidencia sólida para tres condiciones muy específicas, y que se vende en
cremas y gomitas con afirmaciones que la evidencia no sostiene. Distinguir esas tres capas —mecanismo,
evidencia clínica y claim comercial— es exactamente el trabajo de esta skill.

Términos: **agonista inverso (inverse agonist)** = se une al receptor y reduce su actividad basal.
**Modulador alostérico negativo (negative allosteric modulator, NAM)** = se une a un sitio distinto del sitio
activo y reduce la respuesta al agonista. **FAAH** = amida hidrolasa de ácidos grasos, la enzima que degrada
la anandamida. **TRPV1** = receptor de potencial transitorio vanilloide 1, canal implicado en dolor y
temperatura. **Efecto de primer paso** = ver `122`.

## Mecanismo: no es un agonista de CB1

Este es el error conceptual más extendido. El CBD tiene **muy baja afinidad por CB1 y CB2** como agonista
ortostérico. Lo que se ha descrito en la literatura preclínica:

| Diana | Acción descrita del CBD | Nivel de evidencia |
|---|---|---|
| CB1 | Modulador alostérico negativo; antagonismo funcional | `[in vitro]` |
| CB2 | Agonista inverso / afinidad baja | `[in vitro]` |
| 5-HT1A | Agonista | `[in vitro, animal]` |
| TRPV1, TRPV2, TRPA1 | Agonista / desensibilizador | `[in vitro]` |
| GPR55 | Antagonista | `[in vitro]` |
| PPARγ | Agonista | `[in vitro]` |
| FAAH / transporte de anandamida | Inhibición → sube anandamida | `[in vitro, animal]` |
| Adenosina | Inhibe recaptación → señalización adenosinérgica | `[in vitro, animal]` |
| Canales de sodio y calcio | Modulación | `[in vitro]` |

La honestidad obliga a decir dos cosas: (1) **la mayoría de estos hallazgos son in vitro y a concentraciones
que pueden no alcanzarse in vivo con dosis realistas**; (2) el mecanismo por el que el CBD funciona en
epilepsias refractarias —donde sí hay evidencia clínica de alta calidad— **no está completamente establecido**,
aunque GPR55 y los canales iónicos son las hipótesis más discutidas.

Un punto práctico y muy citado: el CBD **atenúa algunos efectos del THC** en estudios controlados
`[clínico, resultados mixtos]`. No es un antídoto y la magnitud depende de la proporción y del momento de
administración. Vender "CBD para bajarle al THC" como si fuera confiable va más allá de lo que la evidencia
soporta.

## Farmacocinética: el talón de Aquiles

| Parámetro | Dato reportado en la literatura | Implicación |
|---|---|---|
| Biodisponibilidad oral | Baja, del orden de 6–20 %, muy variable | Gran parte de la dosis no llega a sangre |
| Efecto de la comida | Aumenta marcadamente la exposición con comida grasa | El mismo producto rinde distinto en ayunas |
| Metabolismo | CYP3A4 y CYP2C19 principalmente; también UGT | Sustrato y a la vez inhibidor (ver abajo) |
| Metabolito | 7-OH-CBD (activo) → 7-COOH-CBD | Relevante para la respuesta |
| Vida media | Variable, reportada en rangos de horas a más de un día según dosis y vía | Dificulta comparar estudios |

El efecto del alimento es enorme y casi nadie lo dice en la etiqueta. Estudios con el producto farmacéutico
de CBD muestran aumentos de varias veces en la exposición cuando se toma con comida rica en grasa
`[clínico]`. Si tu producto se toma "cuando sea", la dosis efectiva varía día a día.

## El CBD como inhibidor enzimático: la parte que sí es un riesgo real

El CBD inhibe varias isoformas del citocromo P450, notablemente **CYP3A4, CYP2C19 y CYP2C9**, y también
UGT `[clínico e in vitro]`. Consecuencias documentadas:

- Aumento de las concentraciones de **clobazam** (a través de su metabolito N-desmetilclobazam) `[clínico]`.
- Interacción con **warfarina**, con aumento del INR reportado `[reportes de caso / clínico]`.
- Elevaciones de transaminasas hepáticas, sobre todo a dosis altas y en combinación con **valproato**
  `[clínico, ensayos registrados]`.

Esto no es teórico: es la razón por la que la ficha técnica del medicamento de CBD aprobado exige monitoreo
hepático. Cualquier producto de CBD que se venda sin advertencia de interacciones a personas polimedicadas
está omitiendo información de seguridad relevante (ver `209`).

## Dosis: el abismo entre lo clínico y lo comercial

| Contexto | Dosis usada | Nivel de evidencia |
|---|---|---|
| Ensayos clínicos en epilepsias refractarias (Dravet, Lennox-Gastaut, esclerosis tuberosa) | 10–20 mg/kg/día | `[clínico fase 3]` |
| Ensayos en ansiedad experimental / hablar en público | 300–600 mg dosis única | `[clínico fase 2, muestras pequeñas]` |
| Producto de consumo típico | 10–50 mg/día | Muy por debajo de las dosis con evidencia |
| Nivel provisional de ingesta segura de EFSA (9 feb 2026) | 0,0275 mg/kg pc/día ≈ **2 mg/día** para 70 kg | Evaluación de seguridad, no de eficacia |

Ese último renglón es demoledor para la industria europea: **el nivel provisional que EFSA considera seguro
está uno o dos órdenes de magnitud por debajo de las dosis que la gente toma y de las que se estudian en
clínica**. Y aplica solo a complementos alimenticios con CBD de pureza ≥ 98 %, sin nanopartículas y con
genotoxicidad descartada. Dato de EFSA Journal, publicado el 9 de febrero de 2026; verifica el estado vigente
en efsa.europa.eu y en la lista de la Unión de nuevos alimentos (ver `212`).

## Cómo se mide / cómo se comprueba

- **En producto**: HPLC-DAD para CBD y CBDA, con THC total en el mismo corrido (ver `198`). Sin ese dato no
  hay cumplimiento posible.
- **En plasma**: LC-MS/MS para CBD, 7-OH-CBD y 7-COOH-CBD, en ng/mL, con método bioanalítico validado.
- **Para afirmar un efecto**: ensayo clínico controlado, aleatorizado y con comparador. Un estudio abierto
  con 20 personas y sin placebo no sostiene un claim (ver `12`, `288`).
- **Para afirmar seguridad**: datos de función hepática si las dosis son altas, y revisión de medicación
  concomitante.

## Ejemplo aplicado (ILUSTRATIVO)

Persona de 70 kg. Producto de 25 mg de CBD por porción.

```
Dosis por peso   = 25 mg / 70 kg = 0,36 mg/kg/día
Dosis de ensayos en epilepsia = 10–20 mg/kg/día
Relación         = la dosis del producto es ~3 % del extremo bajo del rango clínico
Nivel EFSA (2026) = 0,0275 mg/kg/día → 1,9 mg/día para 70 kg
Relación         = el producto entrega ~13 veces el nivel provisional de EFSA
```

Cifras **(ILUSTRATIVO)** salvo el valor de EFSA, que está citado y fechado. La lectura es incómoda y hay que
darla completa: ese producto está **muy por debajo** de las dosis con evidencia clínica de eficacia y **muy
por encima** del nivel de ingesta que EFSA considera provisionalmente seguro para complementos alimenticios.
Ejecuta la conversión con `Matematicas_lushows`; no la estimes.

## Errores comunes

- **Llamar al CBD "agonista de CB1".** No lo es; el mecanismo es otro y mucho más disperso.
- **Extrapolar resultados in vitro a dosis de consumo.** Las concentraciones de laboratorio rara vez se
  alcanzan in vivo.
- **Usar la evidencia de epilepsia refractaria para vender una gomita de 10 mg.** Ni la dosis ni la población
  ni la formulación coinciden.
- **No advertir sobre interacciones.** Es el riesgo real y documentado del CBD, y casi nadie lo comunica.
- **Ignorar el efecto de la comida.** Duplicar o triplicar la exposición según el desayuno no es un detalle.
- **Confundir un nivel de ingesta segura con una dosis eficaz.** Son preguntas distintas con métodos
  distintos.

## Conexión con otros módulos

→ `176-cbd-quimica-y-propiedades.md` — la molécula y sus propiedades fisicoquímicas.
→ `124-citocromo-p450-e-interacciones.md` — el mecanismo de las interacciones.
→ `207-evidencia-clinica-del-cannabis-2026.md` — qué sostiene la evidencia y con qué calidad.
→ `212-cannabis-y-cbd-en-europa.md` — el estado del CBD como nuevo alimento en la UE.
→ `208-dosificacion-y-titulacion.md` — cómo se construye un esquema de dosis.
→ `159-potenciadores-de-biodisponibilidad.md` — el intento de resolver la baja biodisponibilidad.