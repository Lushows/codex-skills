# 234 — *Agaricus* y las otras especies del catálogo (incluida la que trae una hidrazina y la que trae una estatina)

Después de los cinco famosos —reishi, melena de león, cordyceps, chaga y cola de pavo— viene una segunda fila
de especies que se usan mucho y se auditan poco. Dos de ellas tienen sorpresas químicas que un formulador
serio necesita conocer antes de comprar: *Agaricus* trae **agaritina**, una hidrazina natural, y *Pleurotus*
puede traer **lovastatina**, que es literalmente una molécula de medicamento. Este módulo es el mapa rápido
de esa segunda fila, con lo que hay que medir en cada una.

Términos: **agaritina (agaritine)** = derivado hidrazínico natural del género *Agaricus*.
**hidrazina (hydrazine)** = grupo N–N; varias hidrazinas naturales son reactivas y se estudian como
genotóxicas. **lovastatina (lovastatin)** = estatina, principio activo de medicamentos hipolipemiantes,
producida naturalmente por algunos hongos. **peso fresco (fresh weight, FW)** vs **base seca (dry weight,
DW)** = la trampa de base más común de este módulo.

## El género *Agaricus*: el lío del nombre y la agaritina

| Nombre que verás | Situación a agosto de 2026 |
|---|---|
| *Agaricus blazei* Murrill | Nombre comercial dominante; taxonómicamente discutido |
| *Agaricus subrufescens* Peck | Nombre correcto según la revisión taxonómica moderna |
| *Agaricus brasiliensis* | Sinónimo usado en literatura brasileña y japonesa |
| *Agaricus bisporus* | El champiñón común. Otra especie, pero mismo problema de agaritina |

Un COA que diga *A. blazei* no es fraude: es la costumbre comercial. Si mandas ITS (`245`) y vuelve
*A. subrufescens*, es lo esperable.

### Agaritina: cuánta hay

| Material | Valor reportado | Base | Fuente |
|---|---|---|---|
| *A. bisporus* cultivado | 200–500 mg/kg | peso fresco | Literatura de composición de *Agaricus* |
| *A. bisporus* (estudio puntual) | 341 ± 32 µg/g ≈ 341 mg/kg | según el trabajo original | Trabajo de cuantificación de agaritina en especies de *Agaricus* |
| *A. blazei / subrufescens* (mismo trabajo) | 22–57 µg/g | según el trabajo original | Ídem |
| *A. bisporus* en conserva/procesado | 15–20 mg/kg | peso fresco | Estudio de agaritina en alimentos procesados, mercados nórdico y checo |

**Aquí hay que ser muy cuidadoso con la base.** Varios trabajos reportan que *A. blazei* contiene más
agaritina que *A. bisporus* **en base seca**, mientras que en peso fresco la comparación se invierte, porque
los materiales tienen humedades muy distintas. Si comparas un número sin convertir a la misma base, concluyes
lo contrario de lo real (`07`). Esta es la trampa de base número uno del módulo.

Dato útil de proceso: la agaritina es **termolábil e hidrosoluble**, y se degrada mucho con almacenamiento,
congelación, secado y cocción — el descenso reportado en procesados es de casi un orden de magnitud. También
se ha estudiado el fraccionamiento con etanol para removerla de extractos acuosos.

### Qué se sabe del riesgo, dicho con honestidad

La agaritina se metaboliza a especies reactivas (iones diazonio, radicales) y pertenece a la familia de las
hidrazinas naturales, emparentada con la girometrina. Hay estimaciones publicadas de un riesgo adicional
acumulado de cáncer a lo largo de la vida del orden de 10⁻⁵ en humanos, con la advertencia expresa de que
**no hay datos humanos directos**. Nivel de evidencia: `[in vitro]` + `[animal]` + modelado de riesgo.

Lectura práctica: comer champiñones no es el problema. El problema aparece cuando alguien concentra
*Agaricus* en un extracto seco, lo vende en gramos por día y nunca midió la agaritina.

Aparte, existen reportes de caso de disfunción hepática asociados al uso de extractos de *A. blazei* en
pacientes oncológicos (literatura japonesa). Verifica la fuente primaria antes de citarla en un documento,
pero tenlo presente como señal de que el material no es inocuo por definición.

## Otras especies del catálogo

| Especie | Parte usada | Marcador que se mide | Nota que cambia una decisión |
|---|---|---|---|
| *Pleurotus ostreatus* (orellana) | Cuerpo fructífero | β-glucano, ergotioneína, **lovastatina** | Ergotioneína alta: se reportó 2,22 mg/g base seca como la más alta entre varias especies. Y puede traer lovastatina medible — ver abajo |
| *Boletus edulis* (porcini) | Cuerpo fructífero | β-glucano | 57,9 % p/p base seca en **estípite** vs 16,88 % en **sombrero** (Sari et al., *Food Chemistry*, 2017; 216:45–51, método Megazyme). La parte importa más que la especie |
| *Auricularia auricula-judae* (oreja de Judas) | Cuerpo fructífero | Polisacáridos ácidos, β-glucano | Muy hidrosoluble, alta viscosidad; ojo en formulación líquida (`34`) |
| *Tremella fuciformis* | Cuerpo fructífero | Polisacárido con ácido glucurónico, alto peso molecular | Retención de agua; usado en cosmética. No es β-glucano clásico |
| *Wolfiporia extensa* (*Poria cocos*) | Esclerocio | Pachimano: β-(1→3)-glucano **insoluble** | Insoluble en agua: un extracto acuoso rinde poquísimo (`241`) |
| *Fomitopsis betulina* (birch polypore) | Cuerpo fructífero | β-glucano, triterpenos | β-glucano reportado alrededor de 50 % p/p base seca en el grupo de políporos |
| *Hericium erinaceus* | Cuerpo fructífero | β-glucano, hericenonas, erinacinas | Tiene módulo propio: `225`, `226` |

### El problema de la lovastatina en *Pleurotus*

Hay trabajos que identifican y cuantifican **lovastatina** en varias especies de hongos, junto con
ergotioneína, discutiendo las dificultades analíticas de hacerlo bien (*On the Identification and
Quantification of Ergothioneine and Lovastatin in Various Mushroom Species*, PMC8036957, 2021). La
consecuencia regulatoria es grande y casi nadie la ve:

- La lovastatina es **el principio activo de un medicamento**. Un suplemento que la contiene en cantidad
  medible entra en una zona gris regulatoria en cualquier marco (Colombia, `266` y `270`; EE.UU., `273`; UE,
  `278`), porque un producto con actividad farmacológica atribuible a una molécula de medicamento no es un
  alimento.
- Ya hubo un precedente internacional con el arroz de levadura roja (*Monascus purpureus*) y su monacolina K,
  que es químicamente idéntica a la lovastatina, y que terminó regulada.
- Si formulas con *Pleurotus* concentrado, **mídela**. Si sale por debajo del LOQ, lo documentas y sigues.

## Cómo se mide / cómo se comprueba

| Marcador | Método | Unidad y base |
|---|---|---|
| Agaritina | **LC-MS/MS validado** (existe método publicado y validado); alternativa HPLC-UV | `mg/kg`, declarando peso fresco o base seca |
| β-glucano y α-glucano | Megazyme K-YBGL | `% p/p base seca` (`221`) |
| Lovastatina | HPLC-UV 238 nm o LC-MS/MS con patrón | `mg/kg base seca` |
| Ergotioneína | LC-MS/MS o HPLC con par iónico | `mg/g base seca` (`235`) |
| Ergosterol | HPLC-UV 282 nm | `mg/g base seca` (`238`) |
| Identidad de especie | Secuenciación ITS | % identidad (`245`) |
| Metales pesados | ICP-MS | `mg/kg base seca` (`243`) — *Agaricus* es acumulador conocido de Cd |

Nota fuerte: **el género *Agaricus* está entre los acumuladores de cadmio**. Sumar eso a la agaritina hace de
*Agaricus* una materia prima que exige más analítica que la mayoría (`243`).

## Ejemplo aplicado — decidir si entra *Agaricus blazei* al catálogo (ILUSTRATIVO)

```
Propuesta: extracto acuoso de Agaricus blazei, DER 8:1, porcion 1,5 g/dia

Analitica minima antes de decidir:
  ITS -> Agaricus subrufescens                          (245)
  beta-glucano / alfa-glucano por Megazyme               (221, 220)
  agaritina por LC-MS/MS, EN BASE SECA del extracto
  cadmio por ICP-MS                                      (243)
  ergosterol                                             (238)

Cuenta que decide (ILUSTRATIVA):
  si agaritina en el extracto = 60 mg/kg base seca
  aporte diario = 1,5 g x 0,060 mg/g = 0,090 mg/dia = 90 ug/dia
  -> se documenta, se compara con la exposicion dietaria de fondo
     y se decide con criterio toxicologico (134, 135), no con corazonada.

Si el proveedor no puede entregar agaritina medida, el material no entra.
```

## Qué se puede y qué no se puede afirmar

- **Se puede** declarar composición medida (β-glucanos, ergotioneína) con método, unidad y base.
- **Se puede** decir "consumido tradicionalmente en Brasil y Japón" para *A. subrufescens* `[tradicional]`.
- **No se puede** afirmar acción sobre cáncer, colesterol, glicemia ni ninguna enfermedad. Ojo especial con
  el colesterol si hay *Pleurotus*: la tentación de insinuarlo por la lovastatina es exactamente el claim que
  convierte tu suplemento en un medicamento sin registro.
- **No se puede** ocultar la agaritina en la ficha técnica del producto cuando el comprador la pide.

## Errores comunes

- **Comparar agaritina en peso fresco contra base seca.** Concluyes lo contrario de lo real (`07`).
- **No medir cadmio en *Agaricus*.** Es el género que más problemas da.
- **Vender *Poria cocos* como extracto acuoso "rico en β-glucanos".** El pachimano es insoluble en agua.
- **Comprar porcini sin saber si es sombrero o estípite.** Hay una diferencia de más de 3× en β-glucano.
- **Ignorar la lovastatina en *Pleurotus* concentrado.** Es un riesgo regulatorio, no un bonus de marketing.
- **Usar "polisacáridos totales" para todo este grupo.** Con *Tremella* y *Auricularia*, además, ni siquiera
  estás midiendo β-glucano (`222`).

## Conexión con otros módulos

→ `215-panorama-de-hongos-funcionales.md` — el mapa general de especies.
→ `221-medir-beta-glucanos-metodo-megazyme.md` — el ensayo común a todas.
→ `235-ergotioneina.md` — el marcador donde *Pleurotus* y *Boletus* destacan.
→ `243-metales-pesados-en-hongos.md` — por qué *Agaricus* necesita ICP-MS sí o sí.
→ `270-fitoterapeuticos-vs-suplementos.md` — dónde cae un producto con una molécula de medicamento.
→ `245-identidad-de-especie-por-its.md` — cómo se resuelve el lío de nombres.
