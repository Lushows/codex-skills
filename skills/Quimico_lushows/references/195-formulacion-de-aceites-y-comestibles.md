# 195 — Formulación de aceites y comestibles (que la etiqueta y el frasco digan lo mismo)

Formular un aceite sublingual o un comestible con cannabinoides es sencillo de hacer mal y difícil de hacer
bien. Lo fácil es mezclar extracto con aceite hasta que "más o menos dé". Lo correcto es partir del
**miligramo por porción que quieres declarar**, calcular hacia atrás cuánto extracto se necesita según la
potencia real del lote, y luego **comprobar por análisis** que el producto terminado cumple. La mayoría de
los productos que reprueban en inspección no fallan por contaminación: fallan por **discrepancia de
etiqueta**, es decir, el frasco no tiene lo que dice.

Términos: **potencia declarada (label claim)** = el mg por porción que promete la etiqueta.
**Sobrecarga (overage)** = extra de activo que se añade para compensar la pérdida durante la vida útil.
**Homogeneidad de contenido (content uniformity)** = que cada unidad tenga lo mismo que las demás.
**Vehículo (carrier oil)** = el aceite que disuelve el cannabinoide. **Emulsión (emulsion)** = sistema para
meter un activo aceitoso en una matriz de agua.

## Aceites sublinguales: los tres elementos

| Elemento | Opciones frecuentes | Qué gobierna |
|---|---|---|
| Vehículo | MCT (triglicéridos de cadena media), oliva, girasol alto oleico, cáñamo | Sabor, oxidación, viscosidad, absorción |
| Activo | Destilado, aislado, extracto de espectro amplio o completo | Potencia, perfil, color, sabor |
| Estabilizantes | Tocoferoles, romero (extracto), envase ámbar | Vida útil frente a oxígeno y luz |

El MCT es el vehículo más usado porque es líquido en frío, casi insaboro y resiste bien la oxidación (no
tiene dobles enlaces que oxidar). El aceite de oliva aporta polifenoles antioxidantes pero sabor fuerte y
mayor viscosidad en frío.

### El cálculo de formulación, hecho al derecho

```
Objetivo:  10 mg de CBD por porción de 1,0 mL, frasco de 30 mL
Potencia del destilado (COA del lote): 82,4 % p/p de CBD por HPLC-DAD

CBD total requerido por frasco = 10 mg/mL × 30 mL          = 300 mg
Masa de destilado requerida    = 300 mg / 0,824            = 364 mg
Masa de vehículo               = masa objetivo del frasco − 364 mg

Verificación: 364 mg × 0,824 / 30 mL = 10,0 mg/mL
```

Y ahora la parte que casi nadie hace: **decidir la sobrecarga con datos, no con miedo**. Si tu estudio de
estabilidad muestra 6 % de pérdida de CBD a los 24 meses, formulas a 10,6 mg/mL para que a fin de vida útil
sigas por encima del 90 % del claim. Sin estudio de estabilidad, la sobrecarga es adivinanza (ver `164`).

Toda esta aritmética se ejecuta, no se estima: `lab-tools/potencia_formula.py` o `Matematicas_lushows`.

## Comestibles: el problema no es el sabor, es la homogeneidad

Un aceite es una solución: si se agita, es homogéneo. Un comestible es una matriz sólida o semisólida donde
el activo puede **migrar, separarse o degradarse**. Los tres puntos de fallo:

1. **Dispersión.** Añadir destilado directamente a una masa de gomita da puntos calientes: unas unidades con
   18 mg y otras con 4 mg. La solución técnica es **premezcla** (diluir el activo en una fracción del
   vehículo o del jarabe antes de incorporarlo) o **emulsión**.
2. **Emulsificación para matrices acuosas.** Bebidas y gomitas necesitan que el cannabinoide, que es
   lipofílico, se comporte como si fuera soluble en agua. Se usan nanoemulsiones (tamaño de gota típico
   reportado en el rango de decenas a ~200 nm) con tensioactivos de grado alimentario. Ver `157`.
3. **Pérdida por proceso.** El calor del depositado de gomitas y el pH ácido de las gomitas de fruta
   degradan cannabinoides. Hay que medir **antes y después** del proceso, no solo la premezcla.

### Homogeneidad: cómo se demuestra

No basta con analizar una gomita. El criterio prestado de farmacia (USP <905>, uniformidad de unidades de
dosificación) es analizar **10 unidades individuales** y verificar que cada una esté dentro de un rango del
valor declarado, con un valor de aceptación calculado. En cannabis, muchos mercados exigen que la potencia
por unidad esté dentro de ±10 % o ±15 % del claim; el número exacto depende de la jurisdicción y hay que
verificarlo en la norma vigente del destino (a agosto de 2026 esto no está armonizado internacionalmente).

## Cómo se mide / cómo se comprueba

| Ensayo | Técnica | Unidad | Para qué |
|---|---|---|---|
| Potencia del producto terminado | HPLC-DAD, panel de cannabinoides | mg/mL o mg/unidad | Cumplir el claim de etiqueta |
| Uniformidad de unidades | HPLC-DAD sobre 10 unidades individuales | mg/unidad, %RSD | Demostrar que no hay puntos calientes |
| THC total | HPLC-DAD o LC-MS/MS | mg/envase y % p/p | Cumplimiento legal (ver `194`, `211`) |
| Actividad de agua (comestibles) | Higrómetro de punto de rocío | aW (adimensional) | Riesgo microbiológico (ver `35`, `203`) |
| Peróxidos / rancidez (aceites) | Índice de peróxidos, AOCS | meq O2/kg | Vida útil del vehículo |
| Tamaño de gota (emulsiones) | Dispersión dinámica de luz (DLS) | nm | Estabilidad física |

La muestra de potencia debe tomarse del **producto terminado en su envase**, no de la premezcla. Es la
diferencia entre saber qué formulaste y saber qué vendes.

## Ejemplo aplicado (ILUSTRATIVO)

Lote piloto de 500 gomitas, claim 10 mg de CBD por gomita.

- Premezcla analizada: 9,9 mg/g de CBD (HPLC-DAD).
- Gomitas terminadas, 10 unidades individuales: 8,4 · 9,1 · 9,6 · 9,8 · 10,1 · 10,2 · 10,4 · 10,9 · 11,3 ·
  12,0 mg/unidad. Promedio 10,2 mg; desviación estándar 1,05 mg; %RSD = 10,3 %.

Diagnóstico: el promedio cumple, pero la dispersión no. Hay unidades a 8,4 mg (−16 % del claim) y a 12,0 mg
(+20 %). Con un criterio de ±10 % por unidad, este lote **reprueba** aunque el promedio se vea perfecto.
Cifras **(ILUSTRATIVO)**. La causa habitual es dispersión insuficiente antes del depositado.

Moraleja operativa: **el promedio esconde el problema**. Si solo analizas una muestra compuesta, nunca vas a
ver esto — y el cliente sí lo va a sentir.

## Errores comunes

- **Formular sobre la potencia "nominal" del proveedor** en vez del COA del lote específico. Un destilado
  "80 %" que en realidad viene al 74 % te deja el producto 8 % por debajo del claim desde el día uno.
- **Poner sobrecarga a ojo.** 10 % "por si acaso" puede volverte el producto sobrepotente y sacarte del
  límite de THC por envase.
- **Analizar solo la premezcla.** El proceso destruye activo; el dato que importa es el del producto en su
  frasco.
- **Ignorar la actividad de agua en gomitas y chocolates.** Un aW alto es una invitación a mohos, y en
  cannabis eso arrastra el problema de micotoxinas (ver `203`).
- **Usar tensioactivos sin verificar su estatus alimentario en el país de venta.** Un emulsificante permitido
  en un mercado puede no estarlo en otro.
- **No declarar los terpenos reintroducidos ni el aceite portador.** Es información de alérgenos y de
  composición, no un secreto industrial.

## Conexión con otros módulos

→ `161-dosis-y-tamano-de-porcion.md` — cómo se define la porción antes de formular.
→ `157-emulsiones-y-nanoemulsiones.md` — la técnica para bebidas y matrices acuosas.
→ `164-estabilidad-ich-q1-y-vida-util.md` — de dónde sale la sobrecarga defendible.
→ `198-analisis-de-potencia-metodo.md` — el método con el que se comprueba el claim.
→ `204-estabilidad-y-degradacion-del-thc.md` — qué se pierde y hacia qué se convierte.
→ `213-como-leer-un-coa-de-cannabis.md` — cómo se lee el certificado del producto terminado.