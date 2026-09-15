# 273 — FDA y DSHEA: cómo funciona el mercado de suplementos en Estados Unidos

Estados Unidos es el mercado de suplementos más grande del mundo y funciona con una lógica opuesta a la
colombiana: **no hay registro previo del producto**. Puedes lanzar mañana. Lo que hay es una lista de
obligaciones que se te caen encima **después**, y una autoridad que actúa por inspección, carta de
advertencia y retiro. Entender esa diferencia evita dos errores caros: creer que "no hay registro" es
"no hay reglas", y creer que el modelo gringo aplica en Colombia.

Términos: **DSHEA** = *Dietary Supplement Health and Education Act* de 1994, la ley que creó la categoría.
· **FD&C Act** = *Federal Food, Drug, and Cosmetic Act*, la ley marco de alimentos y medicamentos. ·
**warning letter** = carta pública de advertencia de la FDA. · **adulterated / misbranded** = producto
adulterado (composición o proceso) o mal rotulado (etiqueta o claim). · **facility registration** =
registro del establecimiento, no del producto.

## Lo que DSHEA estableció (1994) y sigue rigiendo en agosto de 2026

| Punto | Cómo funciona |
|---|---|
| Categoría | El suplemento dietario es un **alimento**, no un medicamento |
| Aprobación previa del producto | **No existe** |
| Responsabilidad de seguridad | Es del fabricante/distribuidor, no de la FDA |
| Ingredientes nuevos | Requieren notificación NDI 75 días antes (ver `275`) |
| Claims | Structure/function permitidos con disclaimer; claims de enfermedad prohibidos |
| Fabricación | cGMP obligatorio bajo 21 CFR Part 111 (ver `274`) |
| Establecimiento | Registro de la instalación ante la FDA (Food Facility Registration) |
| Eventos adversos | Reporte obligatorio de eventos adversos serios |

Fuente: `fda.gov` → Information for Industry: Dietary Supplements; consultado agosto de 2026.

## El disclaimer de DSHEA: el texto y su regla

Cuando haces un claim de estructura-función, la sección 403(r)(6)(C) de la FD&C Act obliga a acompañarlo
del disclaimer, cuyo texto es:

> *"This statement has not been evaluated by the Food and Drug Administration. This product is not intended
> to diagnose, treat, cure, or prevent any disease."*

La regla de colocación está en **21 CFR 101.93(d)**: el disclaimer debe aparecer adyacente a la afirmación,
sin material intercalado, o vinculado con un símbolo (un asterisco) al final de cada afirmación.

**Novedad que hay que conocer (a agosto de 2026):** el **11 de diciembre de 2025** la FDA publicó una carta
a la industria informando que está considerando modificar 21 CFR 101.93(d) —el requisito de que el
disclaimer aparezca en **cada panel** de la etiqueta— y que, mientras tanto, ejercerá **enforcement
discretion** sobre ese punto específico. La FDA mantiene la exigencia de incluir el disclaimer y de
vincularlo correctamente a cada claim de estructura-función. Fuente: FDA, *Letter to Dietary Supplement
Industry: DSHEA Disclaimer*, `fda.gov`, diciembre de 2025; análisis de Hogan Lovells y del National Law
Review, diciembre de 2025. **Verifica si ya salió la regla final antes de rediseñar etiquetas.**

## Las tres cosas que sí te pueden cerrar

1. **Un claim de enfermedad.** Convierte tu suplemento en un "unapproved new drug". Es el motivo número uno
   de las warning letters. Ver `276`.
2. **Un ingrediente sin historial ni NDI.** El producto se considera adulterado. Ver `275`.
3. **Fabricar fuera de cGMP.** 21 CFR 111 es inspeccionable y las observaciones (Form 483) son públicas.
   Ver `274`.

## Cómo se comprueba lo que pasa en el mercado

Todo es público y gratis. Úsalo antes de lanzar:

| Base de datos | Para qué | Dónde |
|---|---|---|
| Warning Letters | Ver qué frases exactas sancionaron y a quién | `fda.gov/inspections-compliance-enforcement-and-criminal-investigations/warning-letters` |
| Lista de NDINs | Si tu ingrediente ya fue notificado y con qué respuesta | `fda.gov` → NDI notification process |
| Dietary Supplement Ingredient Advisory List | Ingredientes que la FDA marcó como problemáticos | `fda.gov` |
| Recalls | Retiros por contaminación o adulteración | `fda.gov` |
| DSLD (NIH) | Etiquetas reales de miles de productos | `dsld.od.nih.gov` |

Leer 20 warning letters del rubro enseña más sobre claims que cualquier curso: ahí está el lenguaje exacto
que la agencia considera claim de enfermedad.

## Ejemplo aplicado — BIO-SETA mirando el mercado de EE. UU.

Escenario **(ILUSTRATIVO)**: exportar cápsulas de reishi. Lo que hay que resolver, en orden:

```
1. ¿El ingrediente es "grandfathered"?  → ¿extracto de Ganoderma lucidum comercializado como suplemento
                                            en EE. UU. antes del 15-oct-1994? Si no puedes documentarlo → NDI (275)
2. ¿Quién fabrica y cumple 21 CFR 111?  → si maquilas allá, auditoría del maquilador (274, 284)
3. Registro de la instalación ante FDA  → Food Facility Registration + agente en EE. UU. si es importador
4. Etiqueta: Supplement Facts panel     → formato reglado, distinto al colombiano
5. Claims: structure/function + disclaimer → y sustanciación lista por si la FTC pregunta (276)
6. Contaminantes: metales pesados y microbiología dentro de límites; California Prop 65 aparte
```

Punto que nadie ve venir: **la Proposition 65 de California** exige advertencia por exposición a ciertas
sustancias, incluidos plomo y cadmio. Los hongos son acumuladores (`243`). Es una demanda civil frecuente
contra suplementos de botánicos. **Verificar límites y obligaciones vigentes con abogado en EE. UU.**

## Diferencia clave con Colombia, en una frase

En **Colombia** el Estado te revisa **antes** (registro sanitario y aprobación previa de publicidad). En
**Estados Unidos** el Estado te revisa **después** (inspección, warning letter, demanda). El trabajo
químico es el mismo en los dos casos; lo que cambia es cuándo te lo piden. Por eso la especificación de
producto terminado (`282`) es la pieza que sirve en ambos mundos.

## Errores comunes

- **Creer que "no hay registro" es "no hay reglas".** cGMP, NDI y claims son obligaciones duras.
- **Usar el disclaimer de DSHEA en la etiqueta colombiana.** No aplica ni protege en Colombia (`267`).
- **Confiar en que el maquilador cumple 21 CFR 111 porque lo dice.** Se audita (`284`).
- **Ignorar la FTC.** La FDA mira la etiqueta; la FTC mira el anuncio y exige sustanciación (`276`).
- **Olvidar Prop 65** en productos de botánicos y hongos.
- **Asumir que un ingrediente legal en Colombia es legal allá.** Las listas no coinciden.

## Conexión con otros módulos

→ `274-cgmp-21-cfr-111.md` — cómo hay que fabricar.
→ `275-ndi-e-ingredientes-nuevos-en-eeuu.md` — el permiso de entrada del ingrediente.
→ `276-claims-estructura-funcion-y-ftc.md` — qué se puede decir y quién lo vigila.
→ `265-mapa-regulatorio-global.md` — las tres jurisdicciones lado a lado.
→ `282-especificacion-de-producto-terminado.md` — el documento que sirve en cualquier país.
