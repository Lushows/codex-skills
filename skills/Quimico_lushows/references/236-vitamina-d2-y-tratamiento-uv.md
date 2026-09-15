# 236 — Vitamina D2 y tratamiento UV: el único activo de hongo que puedes fabricar con una lámpara

Este es el caso más limpio de todo el bloque de hongos: hay un precursor abundante (ergosterol), una reacción
fotoquímica conocida, un producto medible con método estándar (vitamina D2) y, en varios marcos regulatorios,
un nutriente con declaración nutricional permitida. Es decir: **es el único "activo" del catálogo que puedes
generar a voluntad, medir con confianza y declarar legalmente como nutriente**. También es donde más gente
se equivoca por sobre-irradiar y por confundir bases de reporte.

Términos: **ergosterol (ergosterol)** = el esterol de membrana de los hongos, el precursor.
**previtamina D2 (previtamin D2)** = el intermediario que se forma al abrirse el anillo B por acción del UV.
**vitamina D2 / ergocalciferol (vitamin D2, ergocalciferol)** = el producto final.
**fotoisómeros (photoisomers)** = taquisterol, lumisterol y suprasteroles, los subproductos de la reacción.
**UI (unidad internacional, IU)** = 1 µg de vitamina D = **40 UI**.

## La reacción, en cristiano

```
Ergosterol  --UV-B (~280-315 nm)-->  Previtamina D2  --isomerizacion termica-->  Vitamina D2
     |                                     |
     |                                     +--> Taquisterol, Lumisterol (fotoisomeros)
     +--> (sobre-irradiacion) --> Suprasteroles: se PIERDE rendimiento
```

Tres cosas que se deducen del esquema y que cambian el proceso:

1. El paso UV es rápido; el paso previtamina → vitamina D2 es **térmico** y más lento. Si irradias y enfrías
   de inmediato, dejas previtamina sin convertir y subestimas el resultado si mides al momento.
2. **Más UV no es más vitamina.** Pasado el óptimo, la reacción sigue hacia lumisterol, taquisterol y
   suprasteroles, y el rendimiento cae. Hay que encontrar la dosis óptima, no maximizar la lámpara.
3. El UV solo alcanza donde llega la luz. En hongo entero es superficie; en polvo o en rodajas finas hay
   mucha más área expuesta.

## Números reportados en la literatura

| Material y tratamiento | Resultado | Base | Fuente |
|---|---|---|---|
| *Agaricus bisporus*, contenido de ergosterol de partida | **3–8 mg/g** | base seca | Estudio de conversión de ergosterol bajo irradiación UV-C en *A. bisporus* (ScienceDirect, 2022) |
| *A. bisporus* con UV-C, 0,31 mW/cm² durante 10 min | vitamina D2 **0,9–1 mg/g** | base seca | Ídem |
| Portobello sin tratar | **0,3 µg/100 g** | peso fresco | USDA/ARS, documento *Vitamin D in Mushrooms* |
| Portobello tratado con UV (un lote) | **11,2 µg/100 g** | peso fresco | Ídem |
| Portobello tratado con UV, promedio de dos productores | **3,5–18,8 µg/100 g** | peso fresco | Ídem |
| *A. bisporus*, UV-B **durante el crecimiento** | **24 µg/100 g** | peso fresco | Estudio de UV-B en fase de crecimiento (PubMed 22489222, 2012) |
| *A. bisporus*, UV-B **post-cosecha** | **32 µg/100 g** | peso fresco | Ídem |
| Producto comercial UV tratado, rango típico | **10–20 µg/100 g** | peso fresco | Recopilaciones de mercado |
| *L. edodes* y *P. ostreatus* en polvo, suspensión etanólica irradiada | Sube D2, baja ergosterol | según el trabajo | *ACS Omega*, 2020, estudio de irradiación UV en suspensión |

**Ojo con la mezcla de bases.** Arriba conviven `mg/g base seca` y `µg/100 g peso fresco`, y difieren por
factores de mil y por la humedad. Un hongo fresco tiene ~90 % de agua; su base seca concentra unas 10×
(`07`). Antes de comparar dos cifras de este cuadro, conviértelas.

```
Conversion (ILUSTRATIVO):
  Hongo fresco con 12 ug/100 g de vitamina D2 y 91 % de humedad
  base seca = 12 ug/100 g / (1 - 0,91) = 133,3 ug/100 g base seca = 1,33 ug/g b.s.

  Declaracion en UI para una porcion de 84 g de hongo fresco:
  12 ug/100 g x 0,84 = 10,08 ug -> x 40 = 403 UI por porcion

Este calculo se ejecuta y se verifica por segunda via (Matematicas_lushows),
no se estima de memoria: aqui se declara un nutriente en una etiqueta.
```

## Cómo se mide / cómo se comprueba

| Analito | Método | Unidad y base | Nota |
|---|---|---|---|
| Vitamina D2 (ergocalciferol) | **HPLC-UV a ~265 nm** tras saponificación y extracción; o **LC-MS/MS** | `µg/100 g` (declarar fresco o seco) y `UI/porción` | El AOAC tiene métodos oficiales para vitamina D en alimentos (`281`) |
| Confirmación e interferencias | LC-MS/MS con estándar interno deuterado | `µg/100 g` | Separar D2 de D3 y de fotoisómeros |
| Ergosterol residual | HPLC-UV 282 nm | `mg/g base seca` | Mide cuánto precursor te queda (`238`) |
| Previtamina D2 y fotoisómeros | HPLC con detección UV a varias longitudes, o LC-MS | `µg/100 g` | Útil para optimizar la dosis de UV |
| Humedad | Karl Fischer o pérdida por secado | `% p/p` | Sin esto no puedes convertir bases (`98`) |
| Dosis de UV aplicada | Radiómetro calibrado | `mJ/cm²` (irradiancia × tiempo) | **Este es tu parámetro de proceso**, documéntalo por lote (`168`) |

La clave industrial: la vitamina D2 **es una variable de proceso**, no una propiedad del hongo. Si no
registras irradiancia, distancia, tiempo, espesor de capa y temperatura, no puedes reproducir el lote.

## Estabilidad

La vitamina D2 en hongo seco es razonablemente estable, pero es **sensible a luz y oxígeno**, como cualquier
secosteroide. Consecuencias de formulación:

- Envase opaco o con barrera a la luz (`163`).
- Considerar antioxidante en matrices grasas, o envasado con barrera al oxígeno.
- El estudio de estabilidad va con protocolo ICH Q1 y con el analito **medido**, no asumido (`164`).
- Si haces claim de contenido, la especificación debe contemplar el decaimiento a lo largo de la vida útil:
  se formula con sobredosificación controlada y se justifica (`152`, `164`).

## Regulación, a agosto de 2026

| Marco | Situación | Dónde verificar |
|---|---|---|
| Unión Europea | Los **hongos tratados con UV** figuran en la lista de la Unión de nuevos alimentos (Reglamento de Ejecución (UE) 2017/2470), con condiciones de uso y niveles máximos específicos por categoría | Lista de la Unión de novel foods, Comisión Europea (`278`) |
| Unión Europea, declaración | La vitamina D tiene declaraciones nutricionales y de propiedades saludables autorizadas en el Reglamento (CE) 1924/2006 y su lista de claims permitidos | Registro de health claims de la UE (`277`) |
| Estados Unidos | La vitamina D es un nutriente declarable en el Nutrition Facts; el estatus del hongo tratado con UV se maneja por la vía correspondiente (GRAS/NDI según el caso) | FDA (`273`, `275`) |
| Colombia | Si declaras vitamina D en el rótulo, aplica el reglamento de rotulado y etiquetado nutricional (Resolución 810 de 2021 y sus modificaciones, incluida la 2492 de 2022). El contenido declarado debe estar respaldado por análisis | INVIMA y Ministerio de Salud (`272`, `266`) |

**Verifica la vigencia antes de usar cualquiera de estas entradas.** Este cuadro es orientación fechada, no
norma certificada.

## Ejemplo aplicado — línea de hongo UV para BIO-SETA (ILUSTRATIVO)

```
Objetivo: polvo de orellana (Pleurotus ostreatus) con vitamina D2 declarable

Parametros de proceso a fijar y documentar por lote:
  fuente UV (UV-B o UV-C), longitud de onda dominante
  irradiancia medida con radiometro calibrado  [mW/cm2]
  tiempo de exposicion                         [s]  -> dosis = irradiancia x tiempo
  espesor de capa de polvo                     [mm]
  temperatura y tiempo post-UV                 -> conversion previtamina -> D2
  humedad del material al momento de irradiar  [% p/p]

Analitica por lote:
  vitamina D2 por HPLC-UV 265 nm   -> ug/100 g, base declarada
  ergosterol residual              -> mg/g b.s.  (238)
  humedad                          -> Karl Fischer

DOE recomendado (287): 3 niveles de dosis UV x 2 espesores de capa, medir D2.
El optimo NO es la dosis maxima: pasado el pico se forman suprasteroles.
```

## Qué se puede y qué no se puede afirmar

- **Se puede** declarar el contenido de vitamina D2 medido, en `µg/100 g` o `UI/porción`, con el método.
- **Se puede**, en marcos donde exista la declaración autorizada, usar los claims de vitamina D aprobados
  para ese marco, respetando la condición de uso (cantidad mínima por porción).
- **Se puede** decir "tratado con luz ultravioleta para elevar su contenido de vitamina D2", que es una
  descripción de proceso, verdadera y verificable.
- **No se puede** decir que el producto trata, previene o cura ninguna enfermedad, ni deficiencias
  diagnosticadas, ni "fortalece los huesos" si esa frase no es un claim autorizado en tu marco (`276`, `277`).
- **No se puede** declarar vitamina D2 sin haberla medido en tu producto terminado.

## Errores comunes

- **Sobre-irradiar.** Es el error #1: más lámpara, menos vitamina, más suprasteroles.
- **Medir inmediatamente después del UV** y reportar bajo, porque la previtamina aún no isomerizó.
- **Comparar µg/100 g peso fresco contra mg/g base seca** sin convertir (`07`).
- **Declarar D2 sin estudio de estabilidad**, y quedar por debajo del rótulo al final de la vida útil.
- **Irradiar hongo entero y esperar rendimiento de polvo.** El UV no penetra.
- **No calibrar el radiómetro.** Sin dosis medida, el proceso no es reproducible ni auditable (`168`).
- **Confundir D2 con D3.** Son moléculas distintas; el método debe separarlas.

## Conexión con otros módulos

→ `238-ergosterol-como-marcador.md` — el precursor, y cómo se mide.
→ `57-vitaminas-y-cofactores.md` — la química de fondo de los secosteroides.
→ `61-estabilidad-quimica-luz-calor-oxigeno.md` — por qué el envase importa.
→ `164-estabilidad-ich-q1-y-vida-util.md` — cómo se sostiene un claim de contenido en el tiempo.
→ `287-diseno-de-experimentos-doe.md` — cómo se encuentra la dosis óptima de UV sin quemar lotes.
→ `278-novel-food-hongos-y-cannabis.md` — el estatus europeo del hongo tratado con UV.
