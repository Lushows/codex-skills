# 187 — Extracción con etanol (el caballo de batalla: barato, escalable y traicionero)

El etanol es el solvente que más kilos de cannabis procesa en el mundo, y con razón: es barato, se recupera,
es GRAS en alimentos, no exige sala antideflagrante de la misma categoría que los hidrocarburos y escala de
5 kg a 5 toneladas con la misma física. Su problema es que es **poco selectivo**: junto con los
cannabinoides arrastra clorofila, ceras, azúcares y agua. Todo lo que arrastres de más lo vas a tener que
quitar después, y cada paso de limpieza cuesta dinero y rendimiento. Este módulo te da la fisicoquímica, las
variables que de verdad mueven la aguja y cómo comprobar que hiciste bien el trabajo.

Términos:
- **etanol absoluto (absolute/anhydrous ethanol)** = etanol ≥ 99,5 % v/v, casi sin agua.
- **etanol desnaturalizado (denatured ethanol)** = etanol con un aditivo que lo hace no potable; su
  desnaturalizante puede quedarse en tu producto.
- **relación biomasa:solvente (biomass-to-solvent ratio)** = kg de material seco por litro de etanol.
- **maceración vs. percolación (maceration / percolation)** = dejar en remojo vs. hacer pasar solvente fresco
  a través del lecho.
- **crudo (crude)** = extracto sin refinar, después de evaporar el solvente.

## Por qué el etanol se lleva todo

El etanol tiene un parámetro de solubilidad de Hansen intermedio: disuelve compuestos apolares (los
cannabinoides, con logP alto, ver `30`) **y** compuestos polares (azúcares, clorofila, sales). Los
cannabinoides ácidos como el THCA, además, tienen un grupo carboxilo que los hace más solubles en etanol que
sus formas neutras. La palanca que tienes para hacerlo selectivo es una sola: **la temperatura**.

| Temperatura del etanol | Qué extrae | Qué NO extrae | Postproceso necesario |
|---|---|---|---|
| −40 °C (criogénico) | Cannabinoides y terpenos | Casi nada de clorofila y ceras | Poco; a veces ninguno |
| −20 °C | Cannabinoides, algo de ceras | Poca clorofila | Winterización ligera |
| Ambiente (20–25 °C) | Todo, incluida clorofila y ceras | — | Winterización obligatoria + decoloración |
| Caliente (reflujo) | Todo, máximo rendimiento en masa | — | Refinación pesada; crudo verde oscuro |

El estudio de referencia de esta comparación es Ramirez et al., *Molecules* 27(24):8780 (2022), *"Cold
Ethanol Extraction of Cannabinoids and Terpenes from Cannabis Using Response Surface Methodology"*
(https://doi.org/10.3390/molecules27248780). Con relación 1:15 (biomasa:etanol) y 10 minutos de contacto,
reportaron rendimientos de masa de **18,2 / 19,7 / 18,5 g por 100 g de materia seca** a −20 °C, −40 °C y
temperatura ambiente, y eficiencia de extracción de **THCA de 83,6 % / 97,7 % / 102,1 %** respectivamente.

Lee bien ese dato, porque es contraintuitivo: **el rendimiento en masa es parecido en las tres condiciones,
pero lo que compone esa masa es distinto**. A temperatura ambiente parte de tu "rendimiento" es clorofila y
cera que después vas a botar. El frío no te da más aceite: te da mejor aceite.

## Las variables del proceso, en orden de impacto

1. **Temperatura del solvente.** La única palanca de selectividad real. Frío = crudo limpio.
2. **Tiempo de contacto.** Corto (3–15 min) extrae los cannabinoides, que están en la superficie del
   tricoma. Alargarlo solo suma clorofila. Más tiempo NO es más rendimiento útil.
3. **Relación biomasa:solvente.** Típicamente entre 1:5 y 1:15 (kg:L). Más solvente extrae más pero luego
   hay que evaporarlo todo, y la evaporación es el costo dominante.
4. **Granulometría.** Moler ayuda al contacto, pero moler demasiado fino colapsa el lecho, tapa el filtro y
   arrastra material vegetal fino al crudo (ver `143`).
5. **Humedad de la biomasa.** El agua en el material diluye el etanol y lo vuelve más polar → más clorofila y
   más azúcares. Biomasa a ≤ 10 % de humedad (ver `186`).
6. **Descarboxilación previa o posterior.** Si descarboxilas antes, el crudo es más apolar y el proceso más
   limpio; si lo haces después, conservas THCA para productos de forma ácida (ver `173`, `174`).

## El proceso, paso a paso

```
Biomasa seca (≤10 % humedad, molida a 2–5 mm)
   ↓  etanol frío, contacto corto, agitación suave
Miscela (solución etanol + extracto)
   ↓  filtración: 25–40 µm de desbaste → 5 µm de pulido (a veces + tierra diatomea)
Miscela clarificada
   ↓  recuperación de etanol: evaporador de película, rotavapor o columna de destilación
Crudo (extracto sin refinar)
   ↓  winterización si hizo falta (ver 191) → descarboxilación → destilación (ver 192)
```

La recuperación de etanol es el corazón económico. En operación industrial se hace con evaporador de
película descendente (*falling film*) al vacío, con recuperación típica de 90–95 % del etanol para
reutilizarlo. **Cada punto de etanol que no recuperas es dinero quemado y es un renglón de costo que se
modela con `economist_lushows`, no a ojo.**

## Cálculo del rendimiento (que se hace en código, no de cabeza)

```
Rendimiento en masa (%)      = masa de crudo (g) / masa de biomasa seca (g) × 100
Recuperación de cannabinoide = (masa crudo × %activo crudo) / (masa biomasa × %activo biomasa) × 100
```

Las dos cosas son distintas y confundirlas es el error de contabilidad más común del rubro: puedes tener
25 % de rendimiento en masa y 70 % de recuperación de THC total, o 15 % de masa y 95 % de recuperación. La
segunda operación es mejor negocio. Ejecuta con `lab-tools/rendimiento_extraccion.py` y ambos porcentajes
en `% p/p base seca`.

## Cómo se mide / cómo se comprueba

El crudo de etanol no se acepta por color. Se acepta por análisis:

| Ensayo | Técnica | Unidad | Por qué en este proceso |
|---|---|---|---|
| Potencia y perfil de cannabinoides | HPLC-DAD (`198`) | % p/p | Calcular recuperación y valorar el crudo |
| Perfil de terpenos | GC-MS / GC-FID headspace (`199`) | mg/g | El frío se paga con terpenos conservados: demuéstralo |
| **Solventes residuales — etanol** | GC-MS headspace o GC-FID (`201`) | ppm (µg/g) | Es el ensayo crítico de esta ruta |
| Metales pesados | ICP-MS (`202`) | µg/kg | El etanol concentra lo que traía la planta |
| Humedad / agua | Karl Fischer (`98`) | % p/p | El etanol arrastra agua y afecta pasos siguientes |
| Pesticidas | LC-MS/MS y GC-MS/MS (`200`) | µg/kg | La extracción los concentra igual que a los activos |

El etanol es Clase 3 en USP <467> (solvente de baja toxicidad), con límite de **5.000 ppm** salvo que se
justifique otro. Es un límite generoso comparado con butano o hexano, pero **generoso no es "no medirlo"**:
un crudo mal desolventizado puede traer decenas de miles de ppm. Si usaste etanol **desnaturalizado**, el
laboratorio tiene que buscar también el desnaturalizante (heptano, metanol, isopropanol, bitrex según el
grado) — y el metanol es Clase 2, con límite mucho más bajo. **Verifica el grado exacto y su ficha técnica.**

## Ejemplo aplicado (ILUSTRATIVO)

50,0 kg de flor seca con 18,0 % p/p de THC total (HPLC-DAD, base seca). Etanol a −35 °C, relación 1:8,
contacto 8 min, filtración 25 µm + 5 µm, recuperación en evaporador de película.

- Crudo obtenido: 9,1 kg con 74,0 % p/p de cannabinoides totales.
- Rendimiento en masa = 9,1 / 50,0 = **18,2 %**.
- THC total que entró = 50,0 kg × 0,180 = 9,00 kg. THC total en el crudo ≈ 9,1 kg × 0,700 = 6,37 kg.
- Recuperación ≈ 6,37 / 9,00 = **70,8 %**.

Todas las cifras son **(ILUSTRATIVO)**. Lo que enseña el ejemplo es la pregunta que hay que hacerse:
¿dónde quedaron los 2,6 kg de THC total que faltan? Respuesta habitual: en la torta de biomasa agotada
(por eso se hace un segundo lavado) y en el filtro. Si no analizas la **biomasa agotada (spent biomass)**,
estás botando producto sin saberlo. Ese es el análisis que más plata devuelve por peso.

## Equipo modesto vs. maquila

| Actividad | Con equipo modesto | Exige maquila / planta |
|---|---|---|
| Extracción a escala de 1–20 kg | Sí: congelador −40 °C, tanque, bomba, filtro | — |
| Recuperación de etanol a escala | Rotavapor sirve hasta ~20 L/día | Falling film o columna para volumen real |
| Descarboxilación controlada | Sí: horno de convección con datalogger (`174`) | Reactor encamisado para lotes grandes |
| Winterización | Sí (ver `191`) | — |
| Destilación a distillate | No | Sí — wiped film (ver `192`) |
| Todos los análisis (potencia, terpenos, solventes, metales) | No | Sí — laboratorio acreditado (`107`, `108`) |
| Manejo y permiso de etanol a granel | Depende del municipio | Verificar bomberos y almacenamiento de inflamables |

**A agosto de 2026**, en Colombia el etanol a granel es un inflamable con requisitos de almacenamiento y
concepto de bomberos, y el cannabis con THC exige licencia del Ministerio de Justicia / Ministerio de Salud
según el uso (ver `210`). Verifica lo vigente antes de comprar un tanque: la regulación se mueve.

## Errores comunes

- **Confundir rendimiento en masa con recuperación de activo.** Son dos números distintos y el segundo es el
  que decide si ganas plata.
- **Extraer a temperatura ambiente "porque rinde más".** Rinde más masa de cosas que vas a botar, y te
  obliga a winterizar y decolorar.
- **Dejar la biomasa en remojo horas.** Después de los primeros minutos ya no sacas cannabinoides: sacas
  clorofila.
- **Usar etanol desnaturalizado sin leer qué lo desnaturaliza.** Puedes estar metiendo metanol a un producto
  de consumo humano.
- **No analizar la biomasa agotada.** Es el único modo de saber si tu extracción está dejando 10 % o 30 % en
  la torta.
- **No recuperar el etanol y comprarlo nuevo cada lote.** Es el renglón que hunde el costo por kilo.
- **Saltarse el ensayo de solventes residuales "porque el etanol es seguro".** Seguro no significa
  indetectable, y el COA es lo que el comprador audita (`110`, `111`).

## Conexión con otros módulos

→ `145-extraccion-hidroalcoholica-y-tinturas.md` — la versión galénica de este mismo solvente.
→ `20-parametros-de-solubilidad-y-eleccion-de-solvente.md` — por qué el etanol se lleva todo.
→ `191-winterizacion-y-desceramiento.md` — el paso que este método suele exigir.
→ `192-destilacion-de-cannabinoides.md` — a dónde va el crudo después.
→ `201-solventes-residuales-en-cannabis.md` — el ensayo crítico de esta ruta.
→ `198-analisis-de-potencia-metodo.md` y `199-analisis-de-perfil-de-terpenos.md` — cómo se valora el crudo.
→ `188-extraccion-con-hidrocarburos.md` y `190-solventless-rosin-y-hash.md` — las alternativas y su trade-off.
