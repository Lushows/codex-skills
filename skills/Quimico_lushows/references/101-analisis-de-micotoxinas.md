# 101 — Análisis de micotoxinas (el veneno que el moho deja aunque el moho ya no esté)

Las micotoxinas son metabolitos tóxicos que producen ciertos mohos. Lo que las hace peligrosas para un
negocio es que **sobreviven al moho**: puedes esterilizar el producto, matar todo lo vivo, y las aflatoxinas
siguen ahí, estables al calor. Un lote con microbiología perfecta puede estar fuera de norma por micotoxinas.
Se miden en microgramos por kilo (µg/kg = ppb), lo que exige LC-MS/MS y un muestreo muy cuidadoso, porque
son el analito **peor distribuido** que existe: pueden estar concentradas en un puñado de granos dentro de
una tonelada.

Términos: **micotoxina (mycotoxin)** = metabolito secundario tóxico de un moho. **aflatoxinas (aflatoxins)**
= B1, B2, G1, G2, producidas por *Aspergillus flavus* y *A. parasiticus*; B1 es la más tóxica y está
clasificada como carcinógeno humano Grupo 1 por IARC. **OTA (ochratoxin A)** = de *Aspergillus* y
*Penicillium*, nefrotóxica. **ppb (parts per billion)** = µg/kg. **inmunoafinidad (immunoaffinity column,
IAC)** = columna con anticuerpos que limpia y concentra la micotoxina.

## Las que se buscan y dónde

| Micotoxina | Moho productor | Matriz típica | Relevancia para hongos/cannabis |
|---|---|---|---|
| Aflatoxinas B1, B2, G1, G2 | *A. flavus*, *A. parasiticus* | Maíz, maní, especias, granos | **Alta**: el sustrato de cultivo suele ser grano |
| Aflatoxina M1 | Metabolito en leche | Lácteos | Baja |
| **Ocratoxina A** | *A. ochraceus*, *P. verrucosum* | Café, cereales, uva pasa | **Alta** en material vegetal secado |
| Deoxinivalenol (DON) | *Fusarium* | Trigo, maíz | Media, según sustrato |
| Zearalenona | *Fusarium* | Cereales | Media |
| Fumonisinas B1, B2 | *Fusarium* | Maíz | Media |
| Patulina | *Penicillium* | Manzana | Baja |

En **cannabis**, los mercados regulados de EE. UU. exigen típicamente aflatoxinas totales (B1+B2+G1+G2) y
ocratoxina A, con límites del orden de **20 µg/kg** para aflatoxinas totales y **20 µg/kg** para OTA en varios
estados (a agosto de 2026 el límite exacto **varía por estado**; verifica la norma de tu jurisdicción, ver
`203`). En la Unión Europea los límites para alimentos están fijados por el Reglamento (UE) 2023/915 y
sucesivos; para aflatoxina B1 en muchos alimentos el límite es del orden de **2 µg/kg** y aflatoxinas totales
**4 µg/kg** — números mucho más exigentes que los de cannabis en EE. UU. En Colombia, los límites aplicables
a alimentos y suplementos salen de la reglamentación INVIMA y de las normas de alimentos vigentes; a agosto
de 2026 hay que consultar el texto actual antes de fijar especificación (ver `266`).

## Por qué el muestreo es el 90 % del error

En un lote de grano contaminado, la varianza del muestreo suele superar largamente la varianza del análisis.
Esa es la razón por la que los protocolos oficiales de micotoxinas (Codex, UE, FDA) especifican el **plan de
muestreo** con tanto detalle como el método: número de incrementos, masa total de la muestra agregada,
molienda completa y submuestreo.

```
Regla practica para micotoxinas:
  1. Muchos incrementos pequenos repartidos por TODO el lote (10-100 segun tamano).
  2. Muestra agregada grande (1-10 kg).
  3. Moler TODO lo agregado hasta polvo fino y homogeneo.
  4. Solo entonces tomar los 25-50 g que van al ensayo.

Saltarse el paso 3 es el error que produce falsos negativos.
```

Ver `66-plan-de-muestreo-y-representatividad.md` y `67-homogeneizacion-y-molienda-de-muestra.md`.

## Métodos

| Método | Qué da | Cuándo usarlo |
|---|---|---|
| **ELISA / tiras rápidas** | Semicuantitativo, 15–30 min | Tamiz en recepción de materia prima |
| **HPLC-FLD** con derivatización | Cuantitativo, económico | Aflatoxinas y OTA, método clásico de farmacopea |
| **LC-MS/MS multimicotoxina** | Cuantitativo, 10–60 toxinas a la vez | **El estándar actual**; lo que debe decir tu COA |
| HPTLC | Cualitativo | Histórico, hoy marginal |

Preparación típica para LC-MS/MS: extracción con acetonitrilo/agua (a veces con ácido), limpieza por
**columna de inmunoafinidad** o por dilución directa (dilute-and-shoot) con corrección de matriz. Como las
micotoxinas sufren fuerte **efecto matriz** (supresión o realce de la señal), el método serio usa
**estándares internos marcados isotópicamente** (¹³C-aflatoxina B1, ¹³C-OTA). Si el COA no menciona ni
estándar interno marcado ni calibración en matriz, desconfía del número.

## Cómo se comprueba

- **LOQ declarado por debajo del límite regulatorio**, con margen. Un LOQ de 20 µg/kg no sirve para
  demostrar cumplimiento contra un límite de 20 µg/kg (ver `73`).
- **Recuperación** demostrada en tu matriz, típicamente aceptable entre 70 % y 120 % (criterio orientativo;
  el rango exacto lo fija el método validado, ver `74`).
- **Muestra fortificada (spike)** en cada corrida.
- **Ensayo de aptitud (proficiency testing)** del laboratorio en micotoxinas, dentro de su alcance ISO 17025
  (ver `107`).
- **Estándar interno isotópico** para corregir efecto matriz.

## Ejemplo aplicado (ILUSTRATIVO)

Lote de 400 kg de polvo de cordyceps cultivado sobre sustrato de arroz.

```
Muestreo    : 40 incrementos de 50 g repartidos en todo el lote -> 2,0 kg agregados
Molienda    : todo el agregado a < 0,5 mm, homogeneizado, cuarteado hasta 50 g
Metodo      : LC-MS/MS multimicotoxina, estandar interno 13C-AFB1 y 13C-OTA
LOQ         : 0,5 ug/kg cada aflatoxina ; 0,5 ug/kg OTA
Recuperacion (spike a 5 ug/kg): AFB1 92 % ; OTA 88 %

Resultados (base seca, humedad 6,0 % p/p):
  Aflatoxina B1   : 1,8 ug/kg
  B2, G1, G2      : < LOQ
  Aflatoxinas tot.: 1,8 ug/kg
  Ocratoxina A    : 3,4 ug/kg

Lectura: conforme frente a un limite tipo cannabis EE.UU. (20 ug/kg), pero AFB1 casi en el
limite de la UE para alimentos (2 ug/kg). Si el destino es Europa, este lote esta al filo.
La decision de mercado cambia el veredicto sin que cambie el numero.
```

(Cifras ilustrativas.)

## Errores comunes

- **Muestrear poco** y creerle al "no detectado". Con micotoxinas, un negativo mal muestreado no prueba nada.
- **No moler todo el agregado** antes de submuestrear.
- **LOQ igual o mayor al límite legal.** El resultado no puede demostrar conformidad.
- **Usar ELISA como resultado de liberación.** Es tamiz; confirma por LC-MS/MS.
- **Ignorar el efecto matriz**: sin estándar interno marcado o calibración en matriz, el sesgo puede ser
  del 30–50 %.
- **Suponer que esterilizar el producto elimina las micotoxinas.** No lo hace: son termoestables.
- **Comprar materia prima cultivada sobre grano sin COA de micotoxinas.** El grano es su hábitat natural.

## Conexión con otros módulos

→ `100-microbiologia-de-producto.md` — el moho vivo; la micotoxina es su rastro.
→ `83-lc-ms-ms-y-mrm.md` — la técnica que hace el trabajo.
→ `66-plan-de-muestreo-y-representatividad.md` — donde está el 90 % del error.
→ `244-micotoxinas-y-contaminacion-en-hongos.md` — el caso de hongos funcionales.
→ `203-micotoxinas-y-microbiologia-en-cannabis.md` — límites y práctica en cannabis.
→ `239-sustrato-cultivo-y-quimica-resultante.md` — por qué el grano trae el riesgo.