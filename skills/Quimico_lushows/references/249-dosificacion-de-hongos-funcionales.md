# 249 — Dosificación de hongos funcionales (de qué depende de verdad la dosis, y por qué "1000 mg" no dice nada)

"1000 mg de reishi" es una frase vacía. Mil miligramos ¿de qué? ¿De polvo de cuerpo fructífero, de extracto
9:1, de micelio sobre grano con 5 % de beta-glucano? La dosis que importa no es la masa del polvo, es la
**masa del activo**. Este módulo enseña a calcular la dosis por el activo, a traducir de lo que dicen los
estudios a tu producto, y a decir honestamente lo que no se sabe: en hongos funcionales **no existe una
dosis eficaz establecida** para casi ninguna especie.

Términos: **porción diaria (daily serving)** = lo que el usuario toma en 24 h. **activo declarado (declared
active)** = el compuesto que estandarizas y mides. **DER** = ratio materia prima:extracto (`242`).
**equivalente a hongo seco (dried mushroom equivalent)** = masa de materia prima que representa la dosis.

## La verdad primero

A agosto de 2026 **no hay dosis eficaz establecida por autoridad sanitaria** para hongos funcionales como
suplemento. Lo que hay son:

- Dosis usadas en ensayos clínicos pequeños, distintas entre sí y con materiales no comparables (`248`).
- Uso tradicional, que es `[tradicional/anecdótico]` y no fija dosis técnica.
- Dosis "de mercado", que se copian entre marcas sin base.

Por eso la forma profesional de trabajar es: **declarar el activo, declarar la dosis del activo, y describir
el rango que se ha usado en estudios**, sin prometer un resultado.

## Rangos usados en la literatura clínica (orientativos, no recomendaciones)

| Especie | Material del estudio | Rango de dosis reportado | Nivel de evidencia |
|---|---|---|---|
| Melena de león | Extracto de cuerpo fructífero o polvo | ~ 0,5–3,0 g/día, 4–16 semanas | `[clínico ECA]` pequeños, mixtos |
| Reishi | Extracto o polvo de esporas | ~ 1,0–3,0 g/día, 4–12 semanas | `[clínico piloto]` / ECA pequeños |
| Cordyceps militaris | Extracto | ~ 1,0–4,0 g/día, 1–12 semanas | `[clínico ECA]` pequeños |
| Cola de pavo | Extracto (no el PSK farmacéutico) | ~ 1,0–3,0 g/día | `[clínico]` limitado como suplemento |
| Ergotioneína (aislada) | Compuesto puro | 5–30 mg/día en estudios de biomarcador | `[clínico]` incipiente |

Estos números vienen de los estudios citados en `248`; **verifica el paper de origen antes de usar
cualquiera de ellos**, y ten presente que la mayoría no caracterizó químicamente el material.

## Cómo se calcula la dosis de verdad

```
Paso 1 — Definir el activo y su objetivo por porción:
  Objetivo (ILUSTRATIVO): 250 mg de β-glucano por porción diaria

Paso 2 — Conocer el activo del insumo (COA propio, base seca, método declarado):
  Extracto A: β-glucano 28,4 % p/p base seca (Megazyme K-YBGL)

Paso 3 — Masa de extracto necesaria:
  masa = 250 mg / 0,284 = 880,3 mg de extracto por porción

Paso 4 — Repartir en unidades:
  2 cápsulas de 440 mg  ó  1 cápsula de 900 mg (tamaño 00) con ajuste

Paso 5 — Sobredosificar por decaimiento en vida útil (si el estudio de estabilidad lo justifica):
  Si a 24 meses queda el 92 % del β-glucano:  880,3 / 0,92 = 957 mg de extracto por porción

Verifica todo esto con lab-tools/potencia_formula.py y lab-tools/betaglucano_dosis.py.
Aritmética mental: prohibida.
```

Compara ahora el mismo objetivo con un insumo malo:

```
Extracto B (micelio sobre grano): β-glucano 5,2 % p/p b.s.
  masa = 250 / 0,052 = 4808 mg de extracto por porción  → ~5 gramos de polvo al día.
Es físicamente inviable en cápsulas: harían falta ~10 cápsulas de 500 mg.
Por eso los productos MOG nunca declaran β-glucano por porción: la cuenta los delata (218, 246).
```

## La otra conversión útil: equivalente a hongo seco

```
Producto: 900 mg de extracto con DER 9:1
  Equivalente a hongo seco = 900 mg × 9 = 8100 mg = 8,1 g de cuerpo fructífero seco
Solo es válido si el DER es real y está documentado en el registro de lote (242).
```

## Cómo se comprueba

| Qué verificar | Cómo | Frecuencia |
|---|---|---|
| Que el activo por porción sea el declarado | Analizar el producto terminado, no el insumo | Cada lote (`247`) |
| Que la cápsula pese lo que dice | Uniformidad de masa USP <905> | Cada lote |
| Que el activo aguante la vida útil | Estabilidad ICH Q1A, tiempo real + acelerado | Programa anual (`164`) |
| Que el usuario tome lo que se supone | Instrucciones de uso claras en etiqueta | Diseño de etiqueta (`272`) |

Y una verificación que casi nadie hace: **analiza tu propio producto terminado**, no solo el insumo. Entre
el insumo y la cápsula hay mezcla, excipientes y pérdidas; el número que el cliente recibe es el del
producto terminado.

## Ejemplo aplicado (ILUSTRATIVO) — ficha de dosificación defendible

```
Producto: Extracto de cuerpo fructífero de Hericium erinaceus
Porción diaria: 2 cápsulas
Contenido por porción:
  Extracto seco (DER 8:1, extracción dual)          1000 mg
  De los cuales β-glucano (Megazyme K-YBGL)         ≥ 250 mg
  Equivalente a hongo seco                          8,0 g
  α-glucano                                         ≤ 80 mg (≤ 8 % p/p b.s.)
Modo de uso: 2 cápsulas al día con alimento.
Nota de evidencia: extractos de esta especie se han evaluado en ensayos clínicos pequeños en dosis
del orden de 0,5 a 3 g/día; la evidencia es preliminar y los resultados son mixtos.
```

Ninguna línea de esa ficha promete curar, prevenir ni tratar nada — y toda línea es verificable con un
análisis. Ese es el estándar.

## Errores comunes

- **Declarar mg de polvo y llamarlo dosis.** Sin activo declarado, la dosis es decorativa.
- **Copiar la dosis de la competencia.** Estás copiando el error de alguien que copió a otro.
- **Usar la dosis de un estudio con material distinto al tuyo.** Un ECA con extracto acuoso no justifica tu
  tintura alcohólica.
- **No sobredosificar por vida útil** y quedar por debajo de la etiqueta al mes 20.
- **Subir la dosis para compensar un insumo malo.** Sale más caro y arrastra más almidón, metales y toxinas.
- **Prometer un tiempo de efecto.** "Resultados en 7 días" no tiene soporte en esta literatura.

## Conexión con otros módulos

→ `248-evidencia-clinica-de-hongos-funcionales-2026.md` — de dónde salen (y no salen) los rangos.
→ `161-dosis-y-tamano-de-porcion.md` — el módulo general de dosis por porción.
→ `242-ratios-de-extraccion-y-etiquetado-honesto.md` — DER y equivalentes.
→ `247-especificacion-de-producto-de-hongos.md` — el activo garantizado.
→ `250-seguridad-e-interacciones-de-hongos.md` — límites superiores y precauciones.
→ `164-estabilidad-ich-q1-y-vida-util.md` — por qué se sobredosifica.
