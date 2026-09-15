# 210 — Cannabis medicinal en Colombia (qué permite el Decreto 811 y qué trámite toca)

Colombia tiene uno de los marcos de cannabis más completos de América Latina y, aun así, la mayoría de los
emprendedores que llegan a este tema no sabe si necesita una licencia, dos, o ninguna. Este módulo te da el
mapa: qué es cannabis no psicoactivo según la norma, qué licencias existen y quién las da, en qué se
diferencia una licencia de un registro sanitario, y qué se puede vender legalmente hoy. Todo lo que sigue
está fechado **a agosto de 2026** y con el artículo exacto, para que puedas verificarlo tú mismo.

Términos: **licencia (licence)** = autorización para una actividad con la planta o sus derivados.
**Registro sanitario** = autorización del producto terminado para comercializarse. **Cupo** = asignación de
cantidad de cannabis psicoactivo autorizada. **Componente vegetal** = partes de la planta distintas de las
sumidades floridas. **Sumidad florida (flowering top)** = la inflorescencia.

## La definición que lo ordena todo

El **Decreto 811 de 2021** (expedido el 23 de julio de 2021 por el Ministerio de Salud y Protección Social,
sustituye el Título 11 de la Parte 8 del Libro 2 del Decreto 780 de 2016) define en su **artículo
2.8.11.1.3, numeral 10**:

> **Cannabis no psicoactivo**: sumidades, floridas o con fruto, de la planta de cannabis —con excepción de
> las semillas y las hojas no unidas a las sumidades— de las cuales no se ha extraído la resina, **cuyo
> contenido de tetrahidrocannabinol (THC) es inferior al 1 % en peso seco, incluyendo sus isómeros, sales y
> formas ácidas**.

Tres cosas que casi todos leen mal:

1. **El umbral es 1 %, no 0,3 %.** Colombia no usa el límite estadounidense. Este es un dato competitivo
   real, no un detalle.
2. **La base es PESO SECO.** No "tal cual". Si tu COA está en base húmeda, tienes que corregir antes de
   comparar (ver `07`).
3. **Incluye formas ácidas.** Es decir, THCA cuenta. En la práctica eso se traduce en THC total, con el
   factor 0,877 (ver `175`). Reportar solo Δ9-THC subestima y te puede dejar por fuera de la definición sin
   saberlo.

## Las licencias y quién las expide

Según el **artículo 2.8.11.2.1.2**, el esquema de licencias es:

| Licencia | Autoridad | Para qué |
|---|---|---|
| Fabricación de derivados de cannabis | **INVIMA** | Transformar cannabis psicoactivo en derivados |
| Fabricación de derivados **no psicoactivos** | **INVIMA** | Transformar cannabis no psicoactivo y componente vegetal en derivados no psicoactivos |
| Uso de semillas para siembra | Ministerio de Justicia y del Derecho | Comercializar, adquirir, importar o exportar semilla |
| Cultivo de plantas de cannabis **psicoactivo** | Ministerio de Justicia y del Derecho | Cultivar con fines médicos y científicos |
| Cultivo de plantas de cannabis **no psicoactivo** | Ministerio de Justicia y del Derecho | Cultivar material con THC < 1 % en peso seco |
| Licencias extraordinarias | Ministerio de Justicia y del Derecho | Casos especiales |

El **artículo 2.8.11.1.4** confirma que el INVIMA es la autoridad competente para expedir las licencias de
fabricación de derivados, y el **artículo 2.8.11.1.5** le mantiene las competencias sanitarias de inspección,
vigilancia y control sobre esos derivados. El **ICA** interviene en lo relativo a semillas y material vegetal
de propagación (ver `271`).

La **Resolución 227 de 2022** (Ministerio de Justicia y del Derecho, con Ministerio de Salud) reglamenta el
Decreto 811: licencias, cupos, autorizaciones y condiciones operativas. Verifica su versión vigente en el
normograma del INVIMA (normograma.invima.gov.co), porque ha tenido modificaciones.

## Licencia ≠ registro sanitario (la confusión más cara)

Son dos permisos distintos y necesitas **ambos** si vas a vender un producto:

```
LICENCIA (INVIMA o MinJusticia)
  → te autoriza la ACTIVIDAD: cultivar, fabricar derivados
  → es sobre el proceso y el establecimiento

REGISTRO SANITARIO / NOTIFICACIÓN / PERMISO (INVIMA)
  → te autoriza el PRODUCTO TERMINADO específico
  → es sobre la fórmula, la etiqueta y el expediente técnico
  → la categoría depende de qué producto sea:
     · alimento o suplemento dietario
     · producto fitoterapéutico
     · medicamento
     · cosmético
```

Tener licencia de fabricación de derivados no psicoactivos y creer que ya puedes vender un aceite en tienda
es el error clásico. Falta el registro del producto, y la categoría en la que caiga determina todo lo demás
(ver `266`, `269`, `270`).

## Alimentos y suplementos con cannabis no psicoactivo

Lo que la **Resolución 227 de 2022** habilitó y que a agosto de 2026 sigue siendo la vía práctica:

- Los ingredientes usados para preparar suplementos dietarios pueden ser **componente vegetal, grano y
  derivados no psicoactivos** de la planta de cannabis.
- Si el ingrediente **no está** en las referencias definidas por el Gobierno nacional, debe someterse a
  evaluación de la **Sala Especializada de Productos Fitoterapéuticos y Suplementos Dietarios de la Comisión
  Revisora del INVIMA**. Este paso es el cuello de botella real y el que más tiempo consume.
- La etiqueta de los suplementos dietarios debe declarar el **porcentaje de THC**.
- Se exige implementación de **Buenas Prácticas de Manufactura (BPM)** para fabricación y comercialización de
  alimentos y suplementos dietarios.

El INVIMA emitió sus primeras autorizaciones para alimentos a base de cannabis en 2023. Es decir: **la vía
existe y se ha usado**, no es teórica. Lo que cambia caso a caso es el tiempo y el nivel de exigencia del
expediente.

## El plan analítico mínimo para un expediente colombiano

| Ensayo | Técnica | Unidad y base | Por qué el INVIMA lo va a pedir |
|---|---|---|---|
| Perfil de cannabinoides y THC total | HPLC-DAD | % p/p **base seca** | Demostrar que estás bajo el 1 % |
| Identidad de la materia prima | HPTLC, FTIR o ADN | — | Trazabilidad del origen vegetal |
| Metales pesados (Pb, Cd, As, Hg) | ICP-MS | µg/kg o mg/kg | Seguridad del alimento |
| Pesticidas multiresiduo | LC-MS/MS + GC-MS/MS | µg/kg | Seguridad; ver `200` |
| Solventes residuales | GC-MS headspace | ppm | Si hubo extracción con solvente; ver `201` |
| Microbiología | Según norma de alimentos | UFC/g, ausencia/25 g | Seguridad; ver `203` |
| Micotoxinas | LC-MS/MS | µg/kg | Materia prima vegetal; ver `203` |
| Estabilidad | ICH Q1, zona climática IVb | meses | Sustentar la vida útil declarada; ver `204` |

Colombia está en **zona climática IVb** para estudios de estabilidad (caliente y muy húmeda). Usar la
condición de 25 °C / 60 % HR para un producto que se distribuye en la costa es subestimar el estrés real.

## Ejemplo aplicado (ILUSTRATIVO)

Un emprendedor quiere vender un aceite de CBD en Colombia. Ruta realista:

1. **Definir la categoría** del producto. Si el claim es cosmético, va por cosméticos; si es de aporte
   nutricional, por suplemento dietario; si es terapéutico, es medicamento y el camino es otro (ver `270`).
2. **Asegurar materia prima con trazabilidad**: proveedor con licencia de cultivo no psicoactivo y COA de
   lote con THC total en base seca por HPLC-DAD.
3. **Decidir si fabrica o maquila.** Si fabrica derivados, necesita licencia de fabricación de derivados no
   psicoactivos ante INVIMA. Si maquila con un tercero licenciado, ese requisito lo cumple el maquilador
   (ver `292`).
4. **Armar el expediente técnico** del producto: fórmula cuali-cuantitativa, especificación de materia prima
   y producto terminado, métodos analíticos, estudio de estabilidad, etiqueta proyectada (ver `286`).
5. **Radicar ante INVIMA** la solicitud de la categoría correspondiente.
6. **Etiqueta**: declarar el porcentaje de THC y cumplir el etiquetado de la categoría, sin claims de
   enfermedad (ver `272`, `268`).

Tiempos y costos varían mucho y dependen de la categoría, del estado del expediente y de los tiempos del
INVIMA; para modelar el flujo de caja de esa espera, rutea a `economist_lushows` y `contador_lushows`.

## Errores comunes

- **Usar el límite de 0,3 % de EE.UU.** En Colombia el umbral de no psicoactivo es **< 1 % en peso seco**.
- **Reportar solo Δ9-THC.** La definición incluye formas ácidas; hay que reportar THC total.
- **Comparar COA en bases distintas.** Base seca contra base húmeda no se compara (ver `07`).
- **Creer que la licencia reemplaza el registro sanitario.** Son permisos distintos y se necesitan ambos.
- **Poner claims terapéuticos en un suplemento.** Convierte el producto en medicamento sin registro; es
  infracción sanitaria (ver `267`, `268`).
- **No verificar la norma vigente.** El marco de cannabis en Colombia ha tenido modificaciones desde 2021 y
  hay propuestas de cambio en discusión. Verifica en normograma.invima.gov.co, minsalud.gov.co y el Gestor
  Normativo de Función Pública antes de tomar cualquier decisión.

## Conexión con otros módulos

→ `266-invima-y-suplementos-dietarios.md` — la categoría de suplemento en detalle.
→ `269-registro-sanitario-paso-a-paso-colombia.md` — el trámite del producto.
→ `270-fitoterapeuticos-vs-suplementos.md` — en qué categoría cae tu producto.
→ `272-etiquetado-en-colombia.md` — qué va en la etiqueta, incluido el % de THC.
→ `175-thc-total-y-el-factor-0877.md` — cómo se calcula lo que la definición exige.
→ `214-montar-una-linea-de-producto-de-cannabis.md` — el plan completo de punta a punta.
