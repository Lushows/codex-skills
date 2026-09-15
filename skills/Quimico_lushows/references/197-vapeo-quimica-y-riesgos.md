# 197 — Vapeo: química y riesgos (lo que pasa cuando calientas un aceite)

El vapeo de cannabinoides es el formato donde la química se vuelve más peligrosa, porque el consumidor no
inhala lo que tú formulaste: inhala **lo que sale del dispositivo después de calentarlo**. Entre el líquido
del cartucho y el humo que llega al pulmón hay reacciones térmicas que crean compuestos que nunca estuvieron
en tu fórmula. Este módulo existe por una razón concreta: en 2019–2020 la crisis de EVALI en EE.UU. dejó
miles de hospitalizados y decenas de muertes, y el hilo conductor identificado por los CDC fue el
**acetato de tocoferol (vitamin E acetate)** usado como espesante en cartuchos ilícitos de THC. Un excipiente
comestible perfectamente seguro por vía oral resultó no serlo por vía inhalada.

Términos: **aerosol (aerosol)** = la mezcla de gotas y vapor que inhala el usuario. **Excipiente de corte
(cutting agent)** = sustancia que se agrega al aceite para diluirlo o espesarlo. **Emisión (emission)** = lo
que efectivamente sale del dispositivo, medido con máquina de vapeo. **EVALI** = e-cigarette or vaping
product use-associated lung injury, el cuadro descrito por los CDC en 2019.

## La regla de oro: seguro por boca ≠ seguro por pulmón

El pulmón no tiene la barrera del hígado ni el epitelio del intestino. No hay lista universal de "excipientes
aptos para inhalación" en el mundo del cannabis, y ese vacío es el problema. Un ingrediente con estatus GRAS
(generally recognized as safe) alimentario **no está evaluado para inhalación**.

| Excipiente | Estatus oral | Qué pasa al calentar | Veredicto para inhalación |
|---|---|---|---|
| Acetato de tocoferol | Seguro como alimento y cosmético | Asociado por CDC (2019–2020) a EVALI en cartuchos de THC | No usar |
| Propilenglicol (PG) | Aditivo alimentario permitido | Puede formar óxido de propileno y formaldehído a alta temperatura | Riesgo dependiente de temperatura |
| Glicerina vegetal (VG) | Aditivo alimentario permitido | Puede formar acroleína y formaldehído a alta temperatura | Riesgo dependiente de temperatura |
| MCT (triglicéridos de cadena media) | Seguro como alimento | Lípido inhalado; preocupación por neumonía lipoidea `[reportes de caso]` | Evitar |
| Terpenos botánicos | Seguros en alimentos a bajas dosis | Se degradan y pueden formar carbonilos e irritantes | Usar con moderación y datos |
| Destilado puro sin cortes | — | Menos variables térmicas | La opción más limpia |

La tendencia técnica en mercados regulados a agosto de 2026 es **eliminar los agentes de corte** y trabajar
con destilado o resina viva sola, ajustando viscosidad con temperatura y con el diseño del dispositivo, no
con aditivos.

## Los productos de degradación térmica que hay que buscar

Cuando calientas un aceite con terpenos y glicoles, el aerosol puede contener:

- **Carbonilos**: formaldehído, acetaldehído, acroleína. Provienen sobre todo de PG y VG.
- **Ceteno (ketene)**: descrito en la literatura como producto de la pirólisis de acetato de vitamina E; es
  un gas muy reactivo para el epitelio pulmonar `[in vitro / química de pirólisis]`.
- **Metales**: níquel, cromo, plomo y estaño que migran de la resistencia, las soldaduras y el cuerpo del
  cartucho al aceite y al aerosol. Este es un problema del **hardware**, no del aceite (ver `202`).
- **Isómeros de cannabinoides**: el calor y la acidez pueden convertir Δ9-THC en Δ8-THC y CBN durante el
  almacenamiento y el uso (ver `180`, `204`).
- **Pesticidas transformados**: algunos plaguicidas producen compuestos más tóxicos al pirolizarse; el caso
  más citado es el **miclobutanil**, que puede liberar cianuro de hidrógeno al quemarse `[química de
  combustión]`. Por eso los límites de pesticidas en producto inhalado son más estrictos que en producto
  comestible (ver `200`).

## Cómo se mide / cómo se comprueba

Analizar el líquido del cartucho **no es suficiente**. Hay dos niveles de análisis y son distintos:

| Nivel | Qué se analiza | Técnica | Unidad |
|---|---|---|---|
| Formulación | El aceite en el cartucho | HPLC-DAD (potencia), GC-MS (terpenos), GC-MS headspace (solventes), ICP-MS (metales) | % p/p, mg/g, ppm |
| Emisión | El aerosol capturado | Máquina de vapeo + trampa (filtro Cambridge o impinger) → LC-MS/MS, GC-MS, ICP-MS | µg por bocanada (puff), µg/g de aerosol |

El análisis de emisiones exige definir el **régimen de vapeo**: volumen de bocanada, duración, intervalo,
potencia del dispositivo. Sin ese régimen declarado, el resultado no es comparable con nada. En cigarrillo
electrónico de nicotina existen regímenes normalizados (por ejemplo CORESTA CRM No. 81); en cannabis no hay
un estándar internacional único a agosto de 2026, así que se debe **declarar el régimen usado** en el
informe.

Para metales, el ensayo revelador es la **prueba de migración**: llenar el cartucho, almacenarlo a
temperatura controlada por semanas y medir metales en el aceite al inicio y al final. Si el plomo sube,
el problema es el hardware, no tu extracto.

## Ejemplo aplicado (ILUSTRATIVO)

Cartucho de 1,0 mL, destilado de 85 % de cannabinoides totales, sin agentes de corte, 5 % de terpenos
reintroducidos. Ensayo de migración de metales, 90 días a 25 °C / 60 % HR:

| Metal | Día 0 (µg/kg) | Día 90 (µg/kg) | Comentario |
|---|---|---|---|
| Plomo (Pb) | 12 | 310 | Migración clara desde soldadura |
| Níquel (Ni) | 8 | 95 | Desde la resistencia |
| Cromo (Cr) | 5 | 41 | Desde la resistencia |
| Cobre (Cu) | 30 | 260 | Desde el cuerpo del cartucho |

Cifras **(ILUSTRATIVO)**. El aprendizaje es el que importa: el aceite entró limpio y salió contaminado. Si
tu COA es del día de llenado, no dice nada sobre lo que el consumidor va a inhalar seis meses después. El
control correcto es **cualificar el proveedor de hardware con ensayo de migración**, no analizar solo el
aceite a granel (ver `284`).

## Postura honesta sobre el riesgo

- No existe evidencia que permita llamar "seguro" a ningún producto de inhalación. Lo defendible es hablar de
  **riesgo relativo y de control de contaminantes**, no de seguridad.
- La evidencia sobre efectos a largo plazo del vapeo de cannabinoides es escasa `[epidemiológico, temprano]`.
- Cualquier afirmación de que vapear es "más sano" que fumar debe declararse como comparación de exposición a
  productos de combustión, no como beneficio de salud, y en muchos países esa comparación es un claim
  regulado. Ver `293`.

## Errores comunes

- **Usar excipientes alimentarios porque "son GRAS".** GRAS es para comer, no para inhalar. Es la lección
  exacta de EVALI.
- **Comprar hardware por precio y sin ensayo de migración de metales.** El plomo del cartucho arruina un
  extracto impecable.
- **Analizar solo el aceite y no la emisión.** Lo que se inhala se forma en la resistencia, no en el frasco.
- **Reintroducir terpenos al 10–15 % para "que sepa rico".** Además de irritar, altera la viscosidad y
  aumenta los productos de degradación térmica.
- **No declarar el régimen de vapeo** en los informes de emisiones, lo que vuelve el dato incomparable.
- **Ignorar que el pesticida cambia al calentarse.** El límite de un pesticida en flor para comer no sirve
  para flor o extracto que se va a inhalar.

## Conexión con otros módulos

→ `200-pesticidas-en-cannabis.md` — por qué el límite inhalado es más estricto.
→ `202-metales-pesados-en-cannabis.md` — la migración desde el hardware.
→ `180-delta8-delta10-e-isomerizacion.md` — cómo el calor te fabrica isómeros en el cartucho.
→ `204-estabilidad-y-degradacion-del-thc.md` — qué le pasa al producto guardado.
→ `123-vias-de-administracion.md` — cómo se compara la inhalación con las demás vías.
→ `163-envase-primario-y-compatibilidad.md` — el envase como fuente de contaminación.