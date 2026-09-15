# 188 — Extracción con hidrocarburos (por qué da el mejor extracto y por qué mata gente)

> **ADVERTENCIA DE SEGURIDAD — LÉELA ANTES QUE NADA.**
> La extracción con butano o propano es una operación con **riesgo real de explosión**. El butano es más
> denso que el aire: una fuga no sube, se acumula a nivel del piso y busca una fuente de ignición — un
> interruptor de luz, un motor de nevera, la chispa estática de una bolsa plástica. Las explosiones por
> "BHO casero" han causado quemaduras de tercer grado, amputaciones y muertes documentadas en Norteamérica y
> Europa desde 2013. **Esta operación exige instalación certificada Clase I División 1 (C1D1), clasificación
> de área, sistema cerrado peer-reviewed por ingeniero, detección de gas con enclavamiento, ventilación
> mecánica dedicada y personal entrenado.**
> Este módulo describe el proceso a **nivel técnico e industrial** para que puedas evaluar un maquilador,
> leer un COA o entender la química. **No es un protocolo replicable ni una guía para hacerlo en casa, en un
> garaje ni "con cuidado".** Si tu instalación no está clasificada y certificada, la respuesta correcta a
> "¿puedo hacerlo?" es **no**: maquila con quien sí lo esté.

Dicho eso: el hidrocarburo produce el extracto de mayor calidad organoléptica del mercado, y por eso existe.
Entender por qué es entender solubilidad selectiva.

Términos:
- **BHO (butane hash oil)** = extracto obtenido con butano como solvente; **PHO** si es propano.
- **sistema cerrado (closed-loop system)** = el solvente se condensa, se usa y se recupera sin contactar la
  atmósfera; es el mínimo legal e ingenieril, no un lujo.
- **C1D1 (Class 1, Division 1)** = clasificación eléctrica de área donde hay vapor inflamable en operación
  normal; todo el equipo eléctrico debe ser a prueba de explosión (OSHA 1910.307).
- **LEL (lower explosive limit)** = concentración mínima de vapor que ya puede explotar; para el butano está
  alrededor de 1,8 % v/v en aire.
- **live resin** = extracto de material congelado en fresco, sin secar, que conserva el perfil de terpenos.

## Por qué el hidrocarburo da mejor extracto

El butano (n-butano, punto de ebullición −0,5 °C) y el propano (−42 °C) son **apolares y muy selectivos**:
disuelven cannabinoides y terpenos, y prácticamente **no disuelven clorofila, azúcares ni sales**. Además se
evaporan a temperatura baja, así que los monoterpenos sobreviven al desolventizado.

| Solvente | Polaridad | Qué arrastra de más | Terpenos conservados | Postproceso típico |
|---|---|---|---|---|
| n-Butano | Muy baja | Ceras y lípidos (algo) | Alto | Winterización opcional |
| Propano | Aún más baja | Casi nada polar; menos ceras | Muy alto | Casi ninguno |
| Etanol frío | Media | Algo de clorofila y azúcar | Medio | Winterización frecuente |
| CO₂ supercrítico | Ajustable | Ceras | Medio (dos cortes) | Winterización habitual |

La consecuencia comercial es directa: los extractos de mayor precio por gramo del mercado legal
(*live resin*, *sauce*, *badder*) salen casi siempre de hidrocarburo o de solventless (`190`), no de etanol.

## El proceso a nivel de ingeniería (descriptivo, no operativo)

```
Material (fresco congelado o seco) → columna de extracción
        ↓  solvente líquido frío, presión de vapor propia del gas
Miscela (butano + extracto)
        ↓  filtración en línea / columnas de adsorbente (opcional)
Colector → recuperación del solvente por diferencial de presión y temperatura
        ↓  bomba de recuperación, condensador, tanque de solvente
Extracto crudo → horno de vacío (purga) → producto
```

Los parámetros que gobiernan el resultado son la **temperatura de la columna** (más frío = más selectivo,
menos ceras), la **relación solvente:material**, el **tiempo de contacto** y la **rampa de purga en horno de
vacío**. El desolventizado final en horno de vacío es el paso que decide si pasas o repruebas solventes
residuales, y es un compromiso: purgar más quita butano pero también terpenos.

## Lo que hace que la instalación sea legal, no la habilidad del operario

A agosto de 2026 el consenso técnico en jurisdicciones legales (EE.UU., Canadá) exige, como mínimo:

| Requisito | Qué significa | Referencia habitual |
|---|---|---|
| Área clasificada C1D1 | Booth o sala con equipo eléctrico a prueba de explosión | OSHA 1910.307, NFPA 70 |
| Sistema cerrado peer-reviewed | Un ingeniero registrado firma que el equipo es apto a esa presión | Exigido por muchos AHJ locales |
| Materiales de presión | Acero inoxidable 304 o 316 con clasificación de presión | ASME |
| Almacenamiento de gas | Cantidades, distancias y ventilación del LPG | NFPA 58 |
| Detección de gas | Sensores con alarma y enclavamiento antes del 25 % del LEL | — |
| Ventilación mecánica | Extracción dedicada, con renovaciones/hora calculadas | NFPA 30 / código local |
| Personal | Entrenamiento documentado, EPP, permisos de trabajo | Programa de seguridad de la planta |

**En Colombia, a agosto de 2026**, no existe una norma específica de extracción con hidrocarburos para
cannabis; lo que aplica es el marco general de sustancias inflamables (concepto técnico de bomberos, RETIE
para instalación eléctrica en área clasificada, SG-SST) **más** la licencia de cannabis correspondiente ante
el Ministerio de Justicia / INVIMA según el uso (ver `210`). Verifica lo vigente con la autoridad local antes
de cualquier decisión: este párrafo envejece.

Si evalúas a un maquilador, pídele por escrito: certificado de clasificación de área, peer review del
sistema, concepto de bomberos vigente, registro de entrenamiento del personal y su histórico de solventes
residuales por lote. **Un maquilador que no puede mostrar eso no es barato: es un pasivo.**

## Cómo se mide / cómo se comprueba

Este es el proceso donde el análisis **no es opcional**, porque el riesgo que dejas en el producto es
químico, no estético.

| Ensayo | Técnica | Unidad | Criterio de referencia |
|---|---|---|---|
| **Solventes residuales** | GC-MS headspace o GC-FID (`201`) | ppm (µg/g) | Butano y propano son Clase 3 en USP <467>; muchos estados de EE.UU. fijan límites propios más estrictos (frecuentemente ~1.000–5.000 ppm butano según jurisdicción — verifica el tuyo) |
| Potencia y perfil | HPLC-DAD (`198`) | % p/p | Define el valor comercial |
| Terpenos | GC-MS / GC-FID headspace (`199`) | mg/g | Es la razón de ser de esta ruta: demuéstrala |
| Metales pesados | ICP-MS (`202`) | µg/kg | Ojo: el gas de mala calidad aporta contaminantes |
| Pesticidas | LC-MS/MS y GC-MS/MS (`200`) | µg/kg | Se concentran con el activo |
| **Calidad del solvente de entrada** | COA del proveedor del gas | ppm de aceites/mercaptanos | El butano de encendedor trae aceite de refinería y odorizantes |

Ese último renglón es el que más se descuida: **el butano de grado comercial no es grado de extracción**.
Los gases baratos traen residuos no volátiles que terminan en el extracto y aparecen como "sabor químico" o,
peor, en el ensayo de metales. Exige COA del lote de gas y guárdalo en el expediente (`286`).

## Ejemplo aplicado (ILUSTRATIVO)

Un procesador licenciado corre 20,0 kg de material fresco congelado (*fresh frozen*, ~72 % de humedad) con
n-butano/propano 70:30, columna a −20 °C. Cifras **(ILUSTRATIVO)**:

- Extracto crudo: 1,45 kg. Rendimiento sobre material fresco = **7,25 %**.
- Sobre base seca (5,6 kg de sólidos secos equivalentes) = **25,9 %**.
- Terpenos totales en el extracto: 6,8 % p/p (GC-MS) — contra 2,1 % típico de un crudo de etanol tibio.
- Solventes residuales tras 36 h de purga a vacío: butano 320 ppm, propano 45 ppm (GC-MS headspace).

La lección del ejemplo: **el mismo lote reportado sobre fresco o sobre seco cambia el "rendimiento" por un
factor de 3,5**. Cuando un maquilador te promete "25 % de rendimiento", la primera pregunta es *¿sobre qué
base?* (ver `07`). La segunda es *¿con qué solventes residuales?*, porque purgar poco infla el peso.

## Equipo modesto vs. maquila

| Actividad | Con equipo modesto | Exige maquila / planta certificada |
|---|---|---|
| Extracción con butano o propano | **NO. Nunca.** Sin C1D1 no se hace | **Sí, siempre** |
| Congelado del material fresco | Sí: congelador −20/−40 °C | — |
| Purga en horno de vacío | No como operación aislada; el material aún contiene solvente | Sí, dentro de la instalación clasificada |
| Winterización del extracto | Sí, si el extracto ya viene purgado y liberado (`191`) | — |
| Formulación y envasado | Sí, con extracto liberado por COA | — |
| Análisis de solventes residuales | No | Sí — laboratorio acreditado (`107`, `201`) |

La ruta razonable para un emprendedor pequeño es clara: **compra el extracto ya hecho y liberado, o maquila
con una planta certificada.** El capital de una instalación C1D1 real (booth, sistema peer-reviewed,
eléctrico clasificado, detección, ventilación, seguros) es de orden de decenas de miles de dólares antes de
producir el primer gramo; modélalo con `economist_lushows` antes de enamorarte de la idea.

## Errores comunes

- **Creer que "sistema cerrado" equivale a "seguro".** Un sistema cerrado en una sala no clasificada sigue
  siendo una bomba: las fugas ocurren en las conexiones, no en el diseño ideal.
- **Usar gas de encendedor o de camping.** Trae aceites de refinería y odorizantes que quedan en el producto.
- **Purgar poco para no perder peso ni terpenos.** El sobrepeso es solvente, y el COA lo delata.
- **Trabajar solo, sin detección de gas y sin permiso de trabajo.** El accidente típico ocurre en el
  mantenimiento, no en la extracción.
- **Comprar el extracto sin exigir el COA de solventes residuales del lote.** No del "producto", del **lote**.
- **Comparar rendimientos entre fresco congelado y material seco.** No son comparables sin corregir base.
- **Suponer que la regulación local ya lo permite.** A agosto de 2026 esto varía por municipio incluso dentro
  del mismo país.

## Conexión con otros módulos

→ `08-seguridad-de-laboratorio-y-epp.md` y `09-fichas-de-seguridad-sds-y-ghs.md` — el marco de seguridad.
→ `187-extraccion-con-etanol.md` — la alternativa escalable y menos peligrosa.
→ `190-solventless-rosin-y-hash.md` — cómo conseguir calidad premium **sin solvente inflamable**.
→ `201-solventes-residuales-en-cannabis.md` — el ensayo que decide si el lote se libera.
→ `199-analisis-de-perfil-de-terpenos.md` — el número que justifica esta ruta.
→ `191-winterizacion-y-desceramiento.md` y `192-destilacion-de-cannabinoides.md` — los pasos siguientes.
→ `210-cannabis-medicinal-en-colombia.md` — el marco de licencias vigente.
→ `284-auditoria-de-proveedor.md` — cómo auditar al maquilador antes de firmarle.
