# 180 — Δ8-THC, Δ10-THC e isomerización: química rigurosa y advertencia seria

El Δ8-THC es el ejemplo perfecto de un problema que parece regulatorio y en realidad es químico. La planta
produce Δ8-THC en trazas; todo el Δ8 del mercado se obtiene **isomerizando CBD** en medio ácido. Esa
reacción no genera un producto: genera una **mezcla** con isómeros de posición, subproductos y residuos del
catalizador. Este módulo explica la química para que puedas auditar un COA y entender el riesgo. **No
contiene protocolo de conversión** y no lo va a contener: la línea de esta skill es analizar y auditar, no
enseñar a producir.

Términos:
- **isómero de posición (positional isomer)** = misma fórmula molecular, doble enlace en distinto sitio.
- **Δ9-THC** = doble enlace entre C9 y C10 del anillo terpénico. C₂₁H₃₀O₂, 314,47 g/mol.
- **Δ8-THC** = doble enlace entre C8 y C9. **Misma fórmula, misma masa molar: 314,47 g/mol.**
- **isomerización (isomerization)** = reordenar la molécula sin cambiar su fórmula.
- **ácido de Lewis (Lewis acid)** = catalizador que acepta pares de electrones; usado en estas conversiones.

## Por qué Δ8 y Δ9 son un problema analítico, no solo legal

Δ8 y Δ9 tienen **la misma fórmula molecular y la misma masa exacta**. Consecuencias duras:

- **La espectrometría de masas por sí sola no los distingue.** Ni HRMS: la masa exacta es idéntica. Lo que
  los separa es el **tiempo de retención cromatográfico** frente a patrones certificados de cada uno, y en
  casos difíciles, RMN.
- Un método de potencia que no fue desarrollado para resolverlos **los suma**. Muchos COA antiguos reportan
  "THC" cuando en realidad integraron dos picos mal resueltos.
- Δ10-THC (y sus epímeros), exo-THC (Δ4(8)-iso-THC) y otros isómeros aparecen en las mismas mezclas y
  complican todavía más el cromatograma.

## Qué pasa realmente en una isomerización de CBD

Descripción a nivel de mecanismo, sin condiciones operativas:

```
CBD  --(medio ácido, catálisis)-->  Δ9-THC  ⇌  Δ8-THC  (+ Δ10, iso-THC, oligómeros, productos clorados si
                                                        el catalizador o el solvente aportan cloro)
```

El anillo abierto del CBD cicla y el doble enlace migra. **Δ8 es el isómero termodinámicamente más estable**,
así que a tiempos largos la mezcla se desplaza hacia Δ8. Pero el equilibrio no es limpio: se forman productos
de reacción secundarios que, en la literatura de caracterización de productos comerciales, incluyen isómeros
no identificados y compuestos que **no existen en la planta y no tienen historial toxicológico**.

Ese es el corazón del problema de seguridad: no es tanto el Δ8 en sí —cuya farmacología se describe como
agonista CB1 de menor potencia que el Δ9 [in vitro / animal]— sino **todo lo demás que viaja con él**.
Análisis de productos comerciales publicados en revistas de química analítica y trabajos de caracterización
de incautaciones europeas (por ejemplo, la caracterización extensa de cannabinoides semisintéticos incautados
en Alemania, publicada en 2025) han encontrado repetidamente compuestos no declarados en las etiquetas.

Añade el residuo del catalizador y del solvente: ácidos, metales, disolventes clorados. Todo eso se mide o
no se sabe (`201`, `202`).

## Estatus regulatorio — a agosto de 2026, y verifícalo

| Jurisdicción | Situación a agosto de 2026 | Dónde verificar |
|---|---|---|
| EE.UU. federal | La DEA sostiene que los cannabinoides **sintetizados** no son cáñamo. Ha sido explícita con los ésteres acetilados (Δ8-THCO y Δ9-THCO, declarados Schedule I en 2023) y con HHC. Sobre Δ8 obtenido por conversión hay litigio y guía en evolución. | DEA, textos judiciales, texto de la ley agrícola vigente |
| EE.UU. estatal | Docenas de estados lo han prohibido o restringido; el mapa cambia cada legislatura. | Norma estatal, a la fecha |
| Unión Europea | Más de 20 países han adoptado controles sobre semisintéticos; el detalle varía por país. | Autoridad nacional (p. ej. ANSM en Francia) |
| Colombia | El marco (Decreto 811 de 2021 y desarrollos posteriores) regula cannabis y derivados; los isómeros del THC entran en la definición de fiscalización. Un producto con Δ8 obtenido por conversión **no** es un derivado no psicoactivo. | Minsalud, FNE, Gestor Normativo |

Nota clave: varias definiciones legales de "THC" incluyen **"sus isómeros, sales y formas ácidas"**. Eso
cierra por completo el argumento de "es otro isómero, luego es legal".

## Cómo se mide / cómo se comprueba

1. **Cromatografía que resuelva Δ8 de Δ9.** HPLC con columna y gradiente validados para ese par, con
   patrones certificados **de ambos**. Se exige el cromatograma, no solo la tabla (`81`, `198`).
2. **Resolución mínima demostrada** entre los picos de Δ8 y Δ9 (criterio típico `Rs ≥ 1,5`, ver `79`).
3. **Barrido de compuestos no identificados.** Pide el cromatograma completo y pregunta por cada pico no
   asignado. En estos materiales suelen ser varios y suman área.
4. **HRMS para fórmulas de subproductos** y RMN cuando haya que asignar estructura (`84`, `94`).
5. **Solventes residuales y catalizador.** GC-headspace para solventes (`87`, `201`) e ICP-MS para metales
   si se usó un ácido de Lewis metálico (`88`, `202`).
6. **Perfil de impurezas como especificación.** Si alguien te vende esto, la especificación debe incluir un
   límite para "impurezas totales no identificadas", igual que en un API farmacéutico (`282`).

## Ejemplo aplicado

COA de un "destilado Δ8" ofrecido a un formulador (ILUSTRATIVO, HPLC-DAD, `% p/p`):

| Analito | Valor | Lectura |
|---|---|---|
| Δ8-THC | 68,4 | Lo que se vende |
| Δ9-THC | 4,1 | **Sobra**: en la mayoría de jurisdicciones te saca de norma solo |
| CBD | 2,3 | Reactivo sin convertir |
| Picos no identificados (suma de áreas) | ~18 | **El problema**: casi una quinta parte sin identidad |
| Solventes residuales | "No analizado" | Inaceptable |
| Metales pesados | "No analizado" | Inaceptable |

Decisión: **no comprar**. No porque el Δ8 sea intrínsecamente peor que el Δ9, sino porque el 18 % del
producto no tiene nombre, nadie sabe qué es y nadie ha medido su toxicidad. Ningún formulador serio pone en
un producto de consumo humano una fracción no identificada de ese tamaño.

## Errores comunes

- Creer que "Δ8 es legal porque viene de cáñamo". Las definiciones de THC suelen incluir isómeros.
- Aceptar un COA de potencia sin cromatograma cuando hay isómeros en juego.
- Confiar en LC-MS para separar Δ8 de Δ9. Misma masa exacta: la separación es cromatográfica.
- Ignorar los picos no identificados porque "el activo cumple". La suma de lo desconocido es el riesgo.
- Suponer que un producto de conversión no tiene residuos de catalizador porque el COA no los menciona.
  "No analizado" no es "no presente" (`73`, `111`).
- Comparar potencia Δ8 vs Δ9 sin decir el nivel de evidencia. La menor potencia relativa está descrita
  [in vitro / animal], no calibrada clínicamente en producto de consumo.

## Conexión con otros módulos

→ `42-isomeria-y-estereoquimica.md` — qué es un isómero de posición y por qué es difícil.
→ `176-cbd-quimica-y-propiedades.md` — la ciclación del CBD, desde el lado del formulador.
→ `181-hhc-thco-y-semisinteticos.md` — el resto de la familia semisintética.
→ `198-analisis-de-potencia-metodo.md` — el método que sí resuelve isómeros.
→ `201-solventes-residuales-en-cannabis.md` · `202-metales-pesados-en-cannabis.md` — lo que hay que medir.
→ `111-banderas-rojas-en-un-coa.md` — cómo se ve un COA que esconde cosas.
→ `265-mapa-regulatorio-global.md` — dónde verificar el estatus a la fecha.