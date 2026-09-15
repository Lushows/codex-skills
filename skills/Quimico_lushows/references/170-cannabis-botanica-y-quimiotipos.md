# 170 — Cannabis: botánica y quimiotipos (por qué "sativa/indica" no sirve para nada químico)

Si vas a desarrollar, comprar o analizar un producto de cannabis, lo primero es dejar de hablar como el
mercado y empezar a hablar como el laboratorio. El mercado dice "sativa" o "indica"; el laboratorio dice
**quimiotipo** y te da un número con método y unidad. La diferencia no es cosmética: el quimiotipo decide
si tu material es legal, cuánto vale, qué producto puedes hacer con él y qué análisis vas a tener que pagar.
El error caro típico es comprar biomasa "de CBD" que resulta ser quimiotipo II y te deja por encima del
límite de THC total, con un lote que ya no puedes vender ni exportar.

Términos:
- **quimiotipo (chemotype)** = el perfil químico dominante de la planta, definido por la relación
  THC:CBD medida, no por la forma de la hoja.
- **quimiovar (chemovar)** = una variedad definida por su química medida, no por su nombre comercial.
- **cannabinoide (cannabinoid)** = terpenofenol propio del cannabis; en la planta viva está casi todo en
  forma ácida (ver `173`).
- **tricoma glandular (glandular trichome)** = la glándula de la flor donde se acumulan cannabinoides y
  terpenos; es la fábrica y el objetivo de toda extracción.
- **base seca (dry basis)** = el resultado expresado descontando la humedad (ver `07`).

## Una sola especie, muchos nombres comerciales

A agosto de 2026 el consenso taxonómico de trabajo es tratar el cannabis cultivado como *Cannabis sativa* L.
en sentido amplio, con poblaciones diferenciadas. Los nombres "sativa", "indica" e "híbrida" que usa el
comercio no predicen la química: hay quimiovares vendidos como "indica" con perfiles de terpenos
indistinguibles de los "sativa". Para efectos químicos y regulatorios, **el nombre comercial no es un dato**.
Un dato es: `Δ9-THC 0,18 % p/p base seca, THCA 14,2 % p/p base seca, por HPLC-DAD, lote X, laboratorio Y`.

## Los quimiotipos clásicos

La clasificación de Small y Beutler, todavía vigente como marco operativo, se basa en la relación
THC total : CBD total (ambos calculados con el factor 0,877, ver `175`).

| Quimiotipo | Relación THC:CBD (aprox.) | Cannabinoide dominante | Uso típico |
|---|---|---|---|
| I | > 5 : 1 | THCA / Δ9-THC | Cannabis psicoactivo (uso adulto o medicinal con THC) |
| II | ~ 1 : 1 (0,5–3) | THCA y CBDA en proporciones comparables | Fórmulas balanceadas |
| III | < 1 : 5 (típicamente 15–25 a favor de CBD) | CBDA / CBD | Cáñamo para CBD |
| IV | CBGA/CBG dominante | CBGA | Materia prima para CBG (ver `177`) |
| V | Cannabinoides casi ausentes | — | Fibra y grano |

Las relaciones citadas son las que reporta la literatura de fitoquímica y genética del cannabis; el rango
exacto varía por publicación. **Verifica siempre con el análisis de tu lote**, no con la tabla.

## De dónde sale el quimiotipo: el locus B

El control genético clásico es un locus **B** con dos alelos codominantes: `B_T` (THCA sintasa, THCAS) y
`B_D` (CBDA sintasa, CBDAS). En ese modelo, quimiotipo I = `B_T B_T`, III = `B_D B_D`, y II = heterocigoto
`B_T B_D`, con segregación 1:2:1 en F2. Trabajos genómicos posteriores (mapa físico y genético de
*C. sativa*, Grassa et al., *Genome Research* 2019; y revisiones de genética de sintasas en *Genome* 2021)
mostraron que el locus es en realidad una **región con reordenamientos extensos y copias múltiples** de las
sintasas, lo que explica los "escapes": plantas etiquetadas tipo III que aparecen con THC total por encima
de lo esperado. Detalle en `171`.

Consecuencia práctica: **el genotipo predice, no garantiza**. La ley te va a pedir el fenotipo químico
medido en la flor, no el certificado de la semilla.

## Dónde está la química: el tricoma

Casi toda la carga de cannabinoides y terpenos está en los tricomas glandulares capitados-tallados
(*capitate-stalked*) de las brácteas de la flor femenina. De ahí salen tres consecuencias que gobiernan todo
el bloque de extracción:

1. La **flor** vale mucho más que la hoja y el tallo — el tallo prácticamente no aporta cannabinoides.
2. El tricoma es **frágil**: se rompe con manipulación mecánica y calor. Por eso funcionan el hash y el rosin
   (`190`) sin ningún solvente.
3. Cualquier muestreo que mezcle flor y hoja **baja el resultado**, y cualquier muestreo que tome solo las
   colas lo sube. El plan de muestreo es parte del resultado (ver `66`).

## Cómo se mide / cómo se comprueba

El quimiotipo se declara sobre un **perfil de potencia** completo, no sobre un solo analito:

| Qué | Técnica de referencia | Unidad y base | Nota |
|---|---|---|---|
| Perfil de cannabinoides ácidos y neutros | HPLC/UHPLC-DAD (sin calor, conserva las formas ácidas) | `% p/p base seca` | Método de elección; ver `198` |
| Confirmación de identidad de picos | LC-MS/MS o HRMS | — | Para isómeros y trazas; ver `83`, `84` |
| Humedad (para pasar a base seca) | Pérdida por secado o Karl Fischer | `% p/p` | Sin esto no hay base seca; ver `98`, `07` |
| Perfil de terpenos | GC-MS o GC-FID con headspace | `mg/g` o `% p/p` | Ver `199` |

Nunca uses GC sin derivatizar para declarar el quimiotipo: el inyector caliente descarboxila las formas
ácidas y te borra la distinción THCA/THC (explicado en `173` y `198`).

## Ejemplo aplicado

Un productor colombiano ofrece "biomasa CBD 12 %". El COA que manda dice:
`CBD 11,8 %; THC 0,21 %`. Faltan tres cosas: la base, las formas ácidas y el método. Se le piden y llegan
(ILUSTRATIVO): `CBDA 12,4 % p/p base seca; CBD 0,9 %; THCA 0,62 %; Δ9-THC 0,05 %; humedad 9,1 %; HPLC-DAD`.

- CBD total = 0,9 + (12,4 × 0,877) = **11,8 % p/p base seca**
- THC total = 0,05 + (0,62 × 0,877) = **0,59 % p/p base seca**
- Relación THC:CBD ≈ 1:20 → quimiotipo **III**, correcto.

Pero 0,59 % de THC total supera el 0,3 % que usan varias jurisdicciones como umbral de cáñamo. El lote es
quimiotipo III legítimo **y aun así no es cáñamo conforme** bajo ese umbral. Ese es exactamente el error que
quiebra a un comprador. Ejecuta la cuenta con `lab-tools/thc_total.py`, no de memoria.

## Errores comunes

- Comprar por nombre de variedad ("Charlotte's Angel") en vez de por COA del lote que te van a entregar.
- Pedir "THC" y aceptar un número sin saber si es Δ9-THC solo o THC total (ver `175`).
- Comparar dos COA con humedades distintas sin llevar ambos a base seca (`07`).
- Muestrear solo las colas superiores: la ley y el comprador miden otra cosa.
- Asumir que si la semilla es certificada tipo III, la flor cumplirá — el ambiente y el estrés mueven el
  perfil (ver `185`).
- Declarar quimiotipo con un solo lote. Una especificación necesita varios lotes y un rango (`282`).

## Conexión con otros módulos

→ `171-genetica-y-variedades.md` — de dónde sale el quimiotipo y por qué se escapa.
→ `172-biosintesis-de-cannabinoides.md` — la ruta que fabrica THCA y CBDA.
→ `173-formas-acidas-thca-y-cbda.md` — por qué la planta viva casi no tiene THC.
→ `175-thc-total-y-el-factor-0877.md` — la cuenta que decide si tu lote es legal.
→ `185-cultivo-y-perfil-quimico.md` — cuánto mueve el ambiente al quimiotipo.
→ `198-analisis-de-potencia-metodo.md` — cómo se mide todo esto de verdad.
→ `210-cannabis-medicinal-en-colombia.md` — el marco colombiano a agosto de 2026.