# 46 — Hidrólisis, esterificación y saponificación (la familia de reacciones que decide tu vida útil)

Tres reacciones, un solo carbono: el del grupo carbonilo. La hidrólisis rompe un éster con agua; la
esterificación lo forma; la saponificación lo rompe con base y no da marcha atrás. Suena a laboratorio de
pregrado, pero es lo que explica por qué una tintura cambia de olor a los cuatro meses, por qué el
laboratorio te pide "saponificar" antes de medir ergosterol, por qué la psilocibina se convierte sola en
psilocina, y por qué el análisis de ácidos grasos por GC exige transformarlos en metilésteres. Dominar esta
familia te da control sobre la estabilidad de casi cualquier formulación líquida.

Términos: **hidrólisis (hydrolysis)** = ruptura de un enlace por adición de agua. **Esterificación
(esterification)** = ácido + alcohol → éster + agua. **Saponificación (saponification)** = hidrólisis de un
éster con base fuerte; da la sal del ácido (jabón). **Transesterificación (transesterification)** = cambiar
el alcohol de un éster por otro. **Índice de saponificación (saponification value)** = mg de KOH necesarios
para saponificar 1 g de grasa; mide el tamaño promedio de los ácidos grasos.

## El equilibrio y cómo se manipula

```
Esterificación de Fischer (REVERSIBLE, catálisis ácida):
  R-COOH + R'-OH   ⇄   R-COO-R' + H₂O          Keq típicamente ~ 1–10 → NO se completa sola

Para empujar hacia el éster (principio de Le Châtelier, `21`):
  · exceso grande de alcohol (usarlo como solvente)
  · retirar el agua (Dean-Stark, tamiz molecular 3 Å)

Hidrólisis ácida (la misma reacción al revés): exceso de agua.

Saponificación (IRREVERSIBLE, base fuerte):
  R-COO-R' + NaOH  →  R-COO⁻Na⁺ + R'-OH
  El carboxilato ya no es electrófilo → la reacción no vuelve. Por eso se usa para análisis: es cuantitativa.
```

## La curva en U: pH de máxima estabilidad

La velocidad de hidrólisis depende del pH porque hay tres caminos: catalizado por H⁺, catalizado por OH⁻ y
espontáneo con agua.

```
k_obs = k_H⁺·[H⁺] + k_H₂O + k_OH⁻·[OH⁻]

log k_obs
   |\                    /
   | \                  /        ← rama básica (suele ser MÁS rápida)
   |  \                /
   |   \____________ /           ← zona de mínima degradación = pH de máxima estabilidad
   +----------------------- pH
     2    4    6    8   10

Para la mayoría de ésteres de interés en formulación, el mínimo cae en la zona ligeramente ácida
(reportado en literatura de preformulación; hay que MEDIRLO para tu molécula, no asumirlo).
```

**Cómo se mide el pH de máxima estabilidad:** preparas la misma solución a pH 3, 4, 5, 6, 7 y 8 (con
buffers, `23`), la guardas a 50–60 °C, mides el activo por HPLC a 0, 7, 14 y 28 días, ajustas primer orden
en cada pH y graficas log k contra pH. El valle es tu pH objetivo. Cuesta un mes y salva un producto (`165`).

## Los cuatro casos que te importan

**1. Psilocibina → psilocina.** No es hidrólisis de éster de carboxilo sino de un **éster de fosfato**, y en
el hongo ocurre principalmente por vía **enzimática** (fosfatasas del propio hongo) además de la vía química
en medio ácido y calor. Efecto práctico: material mal secado o secado lento pierde psilocibina y gana
psilocina; y la psilocina es mucho más lábil a la oxidación, por lo que la potencia total cae. Un análisis
honesto reporta **ambas** y también la suma expresada como psilocibina equivalente (`251`, `255`, `256`).

**2. Ergosterol esterificado en hongos.** Buena parte del ergosterol del micelio está como **éster de
esterol** con ácidos grasos. Si extraes y mides directo, subestimas el total. El método correcto hace
**saponificación (hidrólisis alcalina) + extracción del insaponificable** y luego HPLC-UV a 282 nm o GC
después de sililar (`238`, `64`).

```
Esquema del método (ILUSTRATIVO, verificar contra la monografía o AOAC aplicable):
  1. Pesar 0,5 g de polvo seco y molido → base seca conocida (`07`)
  2. Saponificar: KOH metanólico ~1 M, 70–80 °C, 30–60 min, con antioxidante (BHT) y bajo N₂
  3. Extraer el insaponificable con hexano (3 × 10 mL)
  4. Evaporar, reconstituir en metanol, filtrar 0,22 µm
  5. HPLC-UV 282 nm, patrón de ergosterol (CAS 57-87-4), curva de 5 puntos (`71`)
  Resultado esperado, orden de magnitud reportado en literatura: décimas a unidades de mg/g base seca.
  ⚠ Trabajar bajo N₂ y con BHT: el ergosterol es fotolábil y oxidable (`47`).
```

**3. Ácidos grasos → FAME para GC.** Los ácidos grasos libres no cromatografían bien en GC: son polares y dan
picos con cola. Se convierten en **metilésteres (FAME, fatty acid methyl esters)** por transesterificación
(BF₃/metanol, o metóxido de sodio, o TMSH en el inyector). Es el estándar del oficio para perfil de
lípidos (`53`, `64`).

**4. Hidrólisis de glicósidos.** Los flavonoides suelen estar como glicósidos (con azúcar pegado). Para
comparar contra un patrón de la **aglicona** hay que hidrolizar (ácido diluido, calor, o enzima como
β-glucosidasa). Sin ese paso, comparas peras con manzanas y el número queda bajo (`51`).

## Cómo se comprueba y con qué unidades

| Parámetro | Método | Unidad | Nota |
|---|---|---|---|
| Índice de saponificación | Titulación con KOH (AOCS/USP) | mg KOH/g | Aceites y mantecas |
| Índice de acidez (ácidos libres) | Titulación con KOH | mg KOH/g | Sube con la hidrólisis: alarma temprana |
| Índice de peróxidos | Titulación yodométrica | meq O₂/kg | Es oxidación, no hidrólisis (`47`) |
| Grado de conversión | HPLC o GC del reactivo y del producto | % | Con patrones de ambos |
| Constante k de hidrólisis | Estabilidad forzada + ajuste cinético | día⁻¹ o h⁻¹ | Primer orden si linealiza ln C vs t (`26`) |
| Agua disponible | Karl Fischer / actividad de agua | % p/p / a_w | Sin agua no hay hidrólisis (`98`, `35`) |

## Ejemplo aplicado — por qué una tintura empezó a oler a vinagre

Caso (ILUSTRATIVO): tintura hidroalcohólica de reishi, 6 meses en bodega sin control de temperatura, huele
ácido y el pH bajó de 5,1 a 4,2.

```
Hipótesis 1 — hidrólisis de ésteres del extracto o del vehículo:
  Predicción: sube el índice de acidez, aparecen picos de ácidos libres, el pH baja. ✔ coherente
Hipótesis 2 — fermentación microbiana:
  Predicción: recuento microbiano alto, turbidez. → Con 40 % v/v de etanol es poco probable. Se descarta
  midiendo (`100`), no suponiendo.
Hipótesis 3 — oxidación:
  Predicción: color más oscuro, índice de peróxidos alto, olor rancio (no ácido acético). Parcial.

Ensayos a pedir: índice de acidez (mg KOH/g), pH, HPLC del perfil, recuento microbiano, índice de peróxidos.
Acción probable: fijar pH con buffer citrato, envase con menos cabeza de aire, temperatura ≤ 25 °C, y
repetir estabilidad acelerada (`164`).
```

## Errores comunes

- Ajustar el pH "para conservar" sin saber dónde está el mínimo de la curva en U: se puede empeorar.
- Medir esteroles sin saponificar y reportar un valor bajo como si fuera el contenido real.
- Inyectar ácidos grasos libres en GC sin derivatizar y culpar a la columna de los picos con cola (`64`).
- Reportar solo psilocibina en un material donde ya se convirtió a psilocina: la potencia real queda oculta.
- Olvidar que la saponificación destruye compuestos sensibles a base (algunos fenoles, lactonas): el método
  hay que validarlo con recuperación de patrón adicionado (`74`).
- Creer que "producto seco" no hidroliza. Con a_w > 0,6 hay agua suficiente para reacciones lentas (`35`).

## Conexión con otros módulos

→ `44-mecanismos-de-reaccion-basicos.md` — el mecanismo de adición-eliminación al carbonilo.
→ `53-lipidos-y-acidos-grasos.md` — FAME, índices y perfil lipídico.
→ `55-esteroles-y-triterpenos.md` — por qué el ergosterol necesita saponificación.
→ `64-derivatizacion-para-analisis.md` — esterificación y sililación como paso analítico.
→ `164-estabilidad-ich-q1-y-vida-util.md` — cómo se convierte todo esto en una fecha de vencimiento.
