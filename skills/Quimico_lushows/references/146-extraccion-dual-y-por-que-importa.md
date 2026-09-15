# 146 — Extracción dual y por qué importa (un extracto de un solo solvente es medio producto)

Este es el módulo central del bloque. Un hongo no tiene "un" activo: tiene al menos dos familias químicas con
polaridades opuestas. Los **β-glucanos** son polímeros de glucosa, enormes y muy polares: los saca el agua
caliente y los **precipita** el etanol. Los **triterpenos** (ácidos ganodéricos), esteroles y hericenonas son
apolares: los saca el etanol y el agua casi ni los toca. Por eso un extracto solo-agua o solo-alcohol es,
literalmente, **medio producto** — y por eso la industria seria, a agosto de 2026, converge en la extracción
dual como el estándar para especies con química mixta, en particular reishi.

El error caro que evita: pagar por un "extracto premium de reishi 20:1" hidroalcohólico y venderlo hablando de
β-glucanos que ese extracto no puede tener. O al revés: extracto acuoso vendido como "espectro completo".

Términos: **extracción dual (dual extraction)** = proceso de dos etapas, una acuosa y una alcohólica, cuyos
productos se recombinan. **Espectro completo (full spectrum)** = término de marketing sin definición legal;
solo significa algo si dices qué mediste. **Fracción (fraction)** = cada corriente que sale del proceso.
**Recombinación (recombination)** = juntar las dos fracciones en una proporción declarada.

## La química, en una tabla

| Familia | Polaridad | Solvente que la saca | Solvente que la deja | Módulo |
|---|---|---|---|---|
| β-1,3/1,6-glucanos | Muy polar, alto PM | Agua caliente 80–100 °C | Etanol > 60 % (precipita) | `219` |
| Proteoglicanos (PSK, PSP) | Polar | Agua caliente | Etanol alto | `231` |
| Ergotioneína | Polar (zwitterión) | Agua | Etanol alto | `235` |
| Nucleósidos (adenosina, cordicepina) | Polar | Agua | — | `228` |
| Ácidos ganodéricos (triterpenos) | Apolar-ácido | Etanol 70–95 % | Agua | `224` |
| Ergosterol | Muy apolar | Etanol / hexano | Agua | `238` |
| Hericenonas | Lipofílica | Etanol / aceite | Agua | `226` |
| Erinacinas (del micelio) | Lipofílica | Etanol | Agua | `226` |
| Melaninas de chaga | Compleja, parcialmente polar | Agua alcalina y etanol (parcial) | — | `229` |

**La frase que resume el módulo:** el agua caliente rompe la pared celular de quitina y libera los glucanos
solubles; el etanol disuelve las resinas y los terpenoides que están en las membranas y en la cutícula. Ningún
solvente hace las dos cosas, porque la regla es *lo semejante disuelve a lo semejante* (`17`, `20`).

## Cómo se hace de verdad (proceso de dos etapas)

```
BIOMASA SECA Y MOLIDA (malla 40, `143`)
      │
      ├─ RUTA A: primero agua ────────────────────────────────────────────┐
      │   Decocción 90–98 °C, 2–3 etapas (`144`)                          │
      │   → licor acuoso  → filtrar → concentrar (`149`)  = FRACCIÓN A    │
      │   → BAGAZO HÚMEDO: secar antes de la etapa alcohólica              │
      │        (el agua residual diluye el etanol y cambia la perilla)     │
      │   Maceración/percolación en etanol 75–85 % (`145`)                 │
      │   → licor alcohólico → recuperar etanol al vacío = FRACCIÓN B      │
      │                                                                     │
      └─ RUTA B: primero etanol ───────────────────────────────────────────┤
          Ventaja: el bagazo alcohólico se seca solo (el etanol se va)      │
          Riesgo: el etanol "sella" la matriz resinosa y baja el            │
          rendimiento acuoso posterior en algunos materiales.               │
                                                                            │
      RECOMBINACIÓN  ←─────────────────────────────────────────────────────┘
      Se juntan A y B en una proporción DECLARADA (ej. 70:30 en masa seca),
      se ajusta con soporte si hace falta y se seca (`150`).
      → EXTRACTO DUAL, con DOS números en la especificación.
```

Cuál ruta es mejor depende del material: se decide con un experimento, no con opinión. Diseño mínimo: mismo
lote, ambas rutas en paralelo, medir β-glucano y triterpenos en cada fracción y en el bagazo final (`287`).

## Lo que se puede hacer con equipo modesto y lo que exige maquila

| Etapa | Pyme colombiana | Maquila |
|---|---|---|
| Decocción acuosa | Marmita 50–100 L con control de T | Reactor encamisado |
| Filtración | Bolsa 50 µm + filtro prensa pequeño | Filtro prensa / centrífuga |
| Secado del bagazo | Deshidratador de bandejas | Secador de lecho |
| Maceración etanólica | Tanque cerrado inox, área ventilada | Percolador / reactor con recuperación |
| Recuperación de etanol | Rotavapor 20 L (lento pero viable) | Evaporador + condensador con retorno |
| Concentración acuosa | Rotavapor al vacío | Película descendente |
| **Secado final del extracto** | **No viable en casa** | **Spray dryer o liofilizador (`150`)** |
| Análisis de las dos fracciones | Se contrata | Laboratorio acreditado (`107`, `108`) |

Arquitectura realista para una pyme: extraer las dos fracciones tú, concentrarlas, y **maquilar únicamente el
secado y el encapsulado en planta con BPM** (`167`). Es el punto donde el costo fijo del equipo se vuelve
imposible de justificar con volúmenes pequeños.

## Cómo se comprueba que el extracto dual es realmente dual

Un extracto dual honesto tiene **dos analitos declarados y medidos por dos métodos distintos**:

```
ESPECIFICACIÓN MÍNIMA DE UN EXTRACTO DUAL DE REISHI

Atributo 1: β-glucano       ≥ X % p/p base seca   método Megazyme K-YBGL (`221`)
Atributo 2: triterpenos     ≥ Y % p/p base seca   método HPLC-DAD ~252 nm,
                                                  expresado como ácido ganodérico A (`224`)
Atributo 3: α-glucano       ≤ Z % p/p base seca   (control anti-almidón, `220`)
Atributo 4: humedad         ≤ 6 % p/p             Karl Fischer (`98`)
Atributo 5: etanol residual ≤ límite clase 3      GC-headspace (`87`)
```

Si el COA solo trae un número, no es un extracto dual: es un extracto simple con nombre de marketing. Y si trae
"polisacáridos totales" en vez de β-glucano, el número incluye almidón y no prueba nada (`222`).

## Ejemplo aplicado — leer una etiqueta de reishi

Datos **(ILUSTRATIVOS)** de tres productos que dicen lo mismo en el frente del frasco:

```
Producto   Proceso declarado      β-glucano (Megazyme)   Triterpenos (HPLC)   Veredicto
A          "hot water extract"        31,2 % p/p b.s.        0,18 % p/p       honesto pero PARCIAL
B          "tintura 1:5, 80 % v/v"     < LOQ                 2,95 % p/p       honesto pero PARCIAL
C          "dual extract"             24,6 % p/p b.s.        1,42 % p/p       COMPLETO
D          "espectro completo 10:1"   "polisacáridos 40 %"   no reporta       BANDERA ROJA (`111`)
```

Fíjate en algo incómodo: C tiene **menos** β-glucano que A. Es esperable, porque la fracción alcohólica diluye
la acuosa. Un extracto dual no gana en cada número por separado; gana en cobertura química. Decir eso en la
etiqueta es más difícil de vender y más difícil de desmentir — y esa es exactamente la clase de honestidad que
sostiene una marca a cinco años (`293`).

## Cuándo la extracción dual NO se justifica

- **Cordyceps** cuando lo que te interesa son nucleósidos: son polares, el agua basta (`228`).
- **Cola de pavo** enfocado en la fracción proteoglicano: es acuosa (`231`).
- Productos donde el claim es solo β-glucano y el costo del segundo proceso no cambia la promesa.
- Cuando no vas a medir la segunda fracción. Un proceso que no se mide no se puede declarar: **es gasto, no
  valor**.

Regla de decisión: haz dual si tienes **un analito lipofílico que vas a medir y declarar**. Si no, es teatro.

## Errores comunes

- Recombinar A y B "a ojo" y sin declarar la proporción: cada lote sale distinto y la especificación no cierra.
- No secar el bagazo entre etapas y arruinar el grado alcohólico de la segunda extracción.
- Llamar "dual" a mezclar polvo de hongo con una tintura: eso es una mezcla, no una extracción dual.
- Medir solo "polisacáridos" y presentar el número como si fuera β-glucano (`222`).
- Prometer triterpenos en especies que casi no los tienen. La melena de león no es reishi (`225`).
- Ignorar el etanol residual del extracto seco: es un atributo de seguridad y de cumplimiento (`87`).
- Usar el término "espectro completo" como si fuera una especificación. No lo es en ninguna parte.

## Conexión con otros módulos

→ `144-extraccion-acuosa-y-decoccion.md` — la mitad polar, en detalle.
→ `145-extraccion-hidroalcoholica-y-tinturas.md` — la mitad apolar, en detalle.
→ `152-estandarizacion-de-extractos.md` — cómo convertir estas dos fracciones en una promesa medible.
→ `241-extraccion-de-hongos-agua-vs-alcohol.md` — comparación específica por especie.
→ `224-triterpenos-ganodericos-analisis.md` — cómo se mide la fracción alcohólica.
→ `221-medir-beta-glucanos-metodo-megazyme.md` — cómo se mide la fracción acuosa.