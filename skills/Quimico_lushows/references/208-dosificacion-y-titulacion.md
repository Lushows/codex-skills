# 208 — Dosificación y titulación (del miligramo del frasco al miligramo que llega)

Dosificar cannabinoides es donde se juntan la química analítica, la farmacocinética y el diseño de producto.
Si formulas un aceite, tienes que decidir cuántos miligramos van por gota y cuántas gotas caben en una
recomendación responsable. Si asesoras a alguien, tienes que entender por qué la misma dosis produce efectos
distintos en dos personas. Este módulo te da el marco de **titulación (titration)**: empezar bajo, subir
despacio, medir la respuesta. Es el único enfoque defendible cuando la variabilidad entre personas y entre
productos es tan grande.

Términos: **titulación (titration)** = ajustar la dosis gradualmente hasta el efecto buscado con los mínimos
efectos indeseados. **Dosis mínima eficaz (minimum effective dose)** = la más baja que produce el efecto.
**Tolerancia (tolerance)** = necesidad de más dosis para el mismo efecto tras uso repetido. **Porción
(serving)** = la cantidad de producto que la etiqueta define como una toma.

## Las tres variables que hay que fijar antes de hablar de dosis

1. **Cuánto hay** (química analítica): mg de cada cannabinoide por unidad, verificado por HPLC-DAD en el
   producto terminado, no en la premezcla (ver `198`).
2. **Cuánto llega** (farmacocinética): biodisponibilidad de la vía, que va de ~4 % oral a ~35 % inhalado, con
   variabilidad enorme (ver `205`, `206`).
3. **Cuánto necesita esa persona** (farmacodinamia): tolerancia previa, peso, genética de CYP, medicación
   concomitante, y el efecto buscado.

Si te falta cualquiera de las tres, no estás dosificando: estás adivinando con unidades.

## El principio de titulación: "start low, go slow"

Es el estándar en la literatura de cannabis medicinal y en las guías de práctica de varios países:

```
1. Empezar con la dosis más baja posible del producto.
2. Mantenerla al menos 2–3 días (más si la vía es oral y de acción lenta).
3. Registrar efecto y efectos indeseados en un diario, con hora y dosis.
4. Si no hay efecto y no hay efectos indeseados: subir un escalón pequeño.
5. Si aparecen efectos indeseados: bajar al escalón anterior y quedarse ahí.
6. La dosis correcta es la MENOR que produce el efecto buscado.
```

Con productos con THC, el escalón debe ser especialmente pequeño y el tiempo de espera especialmente largo,
porque el Tmax oral puede llegar a 2–3 horas. **La causa más común de intoxicación por comestibles es
redosificar antes de que la primera dosis haya hecho pico** (ver `205`).

Nada de esto es una recomendación médica: es el marco de titulación descrito en la literatura, y su uso en
personas corresponde a un profesional de la salud tratante.

## Diseño de producto: cómo se elige la porción

| Formato | Dosis por unidad que facilita titular | Por qué |
|---|---|---|
| Aceite en gotero | 0,5–1,0 mg por gota | Permite escalones finos; el gotero es el instrumento de titulación |
| Cápsula | Dosis fija baja, con presentación de dos potencias | No se puede partir; hay que ofrecer escalones |
| Gomita | Divisible o de dosis baja | Una gomita de 25 mg no permite titular |
| Bebida | Envase de dosis única baja | No se guarda medio envase |
| Inhalado | El usuario titula por bocanadas | Efecto rápido, autotitulación natural |

Regla de diseño: **si el producto no se puede dividir, la dosis por unidad tiene que ser el escalón, no el
objetivo**. Una gomita de 50 mg no es un producto para principiantes; es un producto que obliga a partirla
con un cuchillo, y ahí la uniformidad de contenido se va al piso (ver `195`).

## La aritmética del gotero

El gotero es donde más errores de etiqueta se cometen, porque **una gota no es un volumen fijo**: depende de
la viscosidad del aceite, del diámetro de la punta y de la técnica del usuario.

```
Volumen de gota típico: 0,03–0,05 mL (hay que MEDIRLO con tu gotero y tu aceite)

Ejemplo con frasco de 30 mL a 20 mg/mL de CBD:
    CBD total en el frasco      = 30 mL × 20 mg/mL = 600 mg
    Si 1 gota = 0,04 mL:
    Gotas por frasco            = 30 mL / 0,04 mL = 750 gotas
    CBD por gota                = 600 mg / 750 = 0,80 mg/gota
    Un mL completo (≈ 25 gotas) = 20 mg
```

Determinación experimental correcta: pesar 100 gotas en balanza analítica, dividir entre 100, convertir masa
a volumen con la densidad medida del aceite. Hazlo con el gotero real del producto, con al menos tres
frascos y tres operarios. Ejecuta el cálculo con `lab-tools/potencia_formula.py` o `Matematicas_lushows`.

## Cómo se mide / cómo se comprueba

| Qué se verifica | Cómo | Criterio |
|---|---|---|
| mg por porción declarados | HPLC-DAD sobre el producto terminado | Dentro del rango de la especificación (típicamente 90–110 % del claim) |
| Volumen real de gota | Gravimetría, 100 gotas, n ≥ 3 | %RSD bajo entre operarios |
| Uniformidad entre unidades | 10 unidades individuales | Ver `195` |
| Sostenibilidad durante la vida útil | Estudio de estabilidad | El claim se cumple hasta la fecha de vencimiento (ver `204`) |
| Respuesta del usuario | Diario de dosis y efectos | Instrumento de titulación, no de eficacia |

## Ejemplo aplicado (ILUSTRATIVO)

Producto: aceite de 30 mL, 300 mg de CBD y 15 mg de THC total. Gota medida = 0,042 mL.

```
Gotas por frasco = 30 / 0,042 = 714 gotas
CBD por gota     = 300 mg / 714  = 0,42 mg
THC por gota     = 15 mg / 714   = 0,021 mg

Esquema de titulación ILUSTRATIVO (no es una recomendación clínica):
  Días 1–3:  2 gotas   → 0,84 mg CBD + 0,042 mg THC
  Días 4–6:  4 gotas   → 1,68 mg CBD + 0,084 mg THC
  Días 7–9:  6 gotas   → 2,52 mg CBD + 0,126 mg THC
  ...
Y una comprobación regulatoria clave:
  THC total por envase = 15 mg → excede 0,4 mg/envase de la definición
  estadounidense nueva (ver 211) por un factor de 37,5.
```

Cifras **(ILUSTRATIVO)**. Dos lecciones: (1) la titulación fina exige gotas de fracción de miligramo, lo que
obliga a una concentración baja; (2) el mismo producto que es cómodo para titular puede ser ilegal en el
mercado de destino por su contenido total por envase. **Diseño de producto y cumplimiento se deciden juntos**.

## Errores comunes

- **Declarar "mg por gota" sin haber medido la gota.** Es el error de etiqueta más frecuente del sector.
- **Diseñar la porción por marketing** ("suena mejor 25 mg") y no por capacidad de titular.
- **Ignorar la comida.** La exposición a CBD aumenta marcadamente con comida grasa; si el esquema no dice
  con o sin alimento, la dosis efectiva cambia todos los días (ver `206`).
- **Extrapolar dosis de ensayos clínicos a productos de consumo.** Ni la dosis ni la pureza ni la población
  coinciden (ver `207`).
- **No advertir sobre el retraso de los comestibles.** Es el consejo de seguridad más importante que puede
  dar una etiqueta de producto oral con THC.
- **Olvidar que el producto envejece.** Si a los 12 meses queda el 88 % del claim, la dosis real bajó
  (ver `204`).

## Conexión con otros módulos

→ `161-dosis-y-tamano-de-porcion.md` — el marco general de porción.
→ `205-farmacologia-del-thc.md` y `206-farmacologia-del-cbd.md` — cuánto llega de lo que se toma.
→ `195-formulacion-de-aceites-y-comestibles.md` — cómo se construye la unidad de dosis.
→ `209-seguridad-interacciones-y-contraindicaciones.md` — cuándo no se debe dosificar.
→ `126-vida-media-y-regimen-de-dosis.md` — la lógica de los intervalos.
→ `211-hemp-y-cbd-en-estados-unidos-2026.md` — el límite por envase que restringe el diseño.