# 171 — Genética y variedades: por qué la semilla promete y la flor decide

Todo el negocio del cannabis se vende con nombres de variedad, pero el laboratorio no reconoce nombres:
reconoce genotipos y perfiles medidos. Este módulo te da lo mínimo para no dejarte vender humo genético:
qué controla realmente el perfil de cannabinoides, por qué una semilla "certificada CBD" puede darte un
lote fuera de norma, y qué le puedes exigir por escrito a un banco de semillas. El error caro clásico es
sembrar 5 hectáreas con una variedad "0,2 % THC" y descubrir en cosecha que el THC total quedó en 0,55 %
`% p/p base seca`: no hay producto, hay pasivo.

Términos:
- **genotipo (genotype)** = la información genética de la planta.
- **fenotipo (phenotype)** = lo que expresa esa planta en un ambiente dado; lo que mides.
- **quimiotipo (chemotype)** = el fenotipo específicamente químico (ver `170`).
- **clon (clone / cutting)** = copia vegetativa de una planta madre; mismo genotipo, no necesariamente mismo
  fenotipo.
- **estabilidad (trueness-to-type)** = qué tan poco varía la descendencia respecto de lo declarado.

## Qué controla el perfil de cannabinoides

Tres capas, en orden de peso:

1. **Sintasas ácidas (THCAS / CBDAS / CBCAS).** Deciden a dónde va el precursor CBGA (ver `172`). Modelo
   clásico: locus **B** codominante, alelos `B_T` y `B_D`. Modelo actual: región compleja con
   reordenamientos y copias múltiples de las sintasas — Grassa et al., *Genome Research* 2019, mapa físico y
   genético de *C. sativa*; revisiones posteriores en *Genome* (2021) sobre variación genómica de las
   sintasas y su efecto en el contenido de cannabinoides.
2. **Longitud de la cadena alquílica.** Decide si sale la serie pentilo (THC, CBD) o la serie propilo
   (THCV, CBDV) — herencia no mendeliana simple, con patrones digénicos y epistáticos descritos en
   *Scientific Reports* 2019 ("Complex Patterns of Cannabinoid Alkyl Side-Chain Inheritance"). Ver `178`.
3. **Ambiente y manejo.** Nutrición, luz, estrés, momento de cosecha, secado. No cambia el quimiotipo, pero
   sí mueve las concentraciones absolutas y el perfil de terpenos varias décimas. Ver `185` y `186`.

## Por qué se "escapan" los tipo III

Un cáñamo tipo III bien seleccionado sigue produciendo algo de THCA, porque la CBDAS no es perfectamente
específica y porque en muchas poblaciones hay copias funcionales residuales de THCAS. Si la planta acumula
más cannabinoide total (planta grande, floración larga, cosecha tardía), **el THC total sube en proporción
aunque la relación THC:CBD no cambie**. Es aritmética, no mala suerte:

```
Si  THC_total / CBD_total = 1/25  (relación fija del quimiotipo)
y   CBD_total sube de  8 %  →  15 %  p/p base seca
entonces THC_total sube de 0,32 % → 0,60 % p/p base seca
```

Moraleja operativa: **la fecha de cosecha es una variable de cumplimiento**, no solo de rendimiento.
Se monitorea con muestreos seriados antes de la cosecha (`186`, `66`).

## Tipos de material de siembra

| Material | Uniformidad química | Riesgo | Cuándo tiene sentido |
|---|---|---|---|
| Semilla feminizada estabilizada | Media-alta | Segregación residual; machos ocasionales | Escala de campo |
| Semilla regular | Baja | Sexado manual, mucha varianza | Mejoramiento, no producción |
| Clon de madre seleccionada | Alta | Sanidad (virus, viroides), degeneración de la madre | Producción de flor premium |
| Micropropagación (tissue culture) | Muy alta | Costo, dependencia de proveedor | Bancos de germoplasma, escala |

Un dato que sí se puede exigir por contrato: **el porcentaje de plantas fuera de especificación** en un lote
de semilla, medido sobre una muestra representativa al final de floración, con COA por HPLC.

## Cómo se mide / cómo se comprueba

- **Identidad genética:** marcadores SNP o genotipado dirigido a THCAS/CBDAS. Te dice el genotipo esperado
  (`B_T B_T`, `B_T B_D`, `B_D B_D`), no la concentración final. Costo bajo por muestra, resultado en días.
- **Quimiotipo real:** HPLC-DAD sobre flor seca, `% p/p base seca`, formas ácidas y neutras separadas
  (ver `198`).
- **Identidad de especie / contaminación:** secuenciación de regiones marcadoras (ITS) cuando hay dudas de
  material vegetal mezclado (ver `103`).
- **Uniformidad:** muestrear N plantas individuales (no un pool) y reportar media, desviación y máximo. El
  máximo es el que te saca de norma, no la media.

Regla dura: un genotipado **no reemplaza** un análisis de potencia para efectos regulatorios en ninguna
jurisdicción que conozcamos a agosto de 2026. Sirve para seleccionar, no para certificar.

## Ejemplo aplicado

Compras semilla feminizada declarada "tipo III, THC total < 0,25 %". Siembras 1.000 plantas y muestreas 30
plantas individuales a los 55 días de floración (ILUSTRATIVO, HPLC-DAD, `% p/p base seca`):

| Estadístico | THC total | CBD total |
|---|---|---|
| Media | 0,26 % | 7,4 % |
| Desviación estándar | 0,07 % | 1,9 % |
| Máximo | 0,44 % | 11,2 % |
| Plantas > 0,30 % | 7 de 30 (23 %) |  |

La media cumple. **El lote no cumple**, porque el muestreo oficial no promedia tu campo entero: toma una
muestra y si sale alto, el lote se pierde. Decisión: cosechar antes, o descartar el 23 % identificable por
posición, o renegociar con el banco de semillas usando este dato. Cualquier cuenta de este tipo se ejecuta
en código (`Matematicas_lushows`), no de cabeza.

## Errores comunes

- Confundir "certificado de semilla" con "garantía de cumplimiento del lote cosechado".
- Reportar solo la media del campo cuando el riesgo regulatorio vive en la cola alta de la distribución.
- Traer un clon de otra finca sin test de virus/viroides y contaminar toda la madre.
- Usar nombres comerciales en el expediente técnico. Un regulador quiere quimiotipo medido, no "Gorilla Glue".
- Asumir que la variedad que cumplió en un clima cumplirá en otro. Trasplantar genética a otra altitud es un
  experimento, y se maneja como tal (ver `287`).
- Seleccionar solo por THC/CBD y perder el perfil de terpenos, que es lo que el consumidor percibe (`182`).

## Conexión con otros módulos

→ `170-cannabis-botanica-y-quimiotipos.md` — la clasificación que estás intentando cumplir.
→ `172-biosintesis-de-cannabinoides.md` — qué hacen exactamente esas sintasas.
→ `178-thcv-cbdv-y-varinas.md` — la herencia de la cadena alquílica.
→ `185-cultivo-y-perfil-quimico.md` — lo que el ambiente sí mueve.
→ `186-cosecha-secado-y-curado.md` — la fecha de cosecha como variable de cumplimiento.
→ `287-diseno-de-experimentos-doe.md` — cómo probar una genética nueva sin quemar un ciclo.