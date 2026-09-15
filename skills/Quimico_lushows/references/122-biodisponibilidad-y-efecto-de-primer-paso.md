# 122 — Biodisponibilidad y efecto de primer paso (por qué tragar no es lo mismo que absorber)

"Biodisponibilidad mejorada" es la etiqueta más usada y menos demostrada del mercado de suplementos. Este
módulo te da la definición exacta de biodisponibilidad (F), te explica el efecto de primer paso —el filtro
hepático e intestinal que destruye buena parte de lo que tragas— y te enseña qué estudio hay que hacer para
poder decir "mejor absorción" sin mentir. El error caro que evita: pagar sobreprecio por una tecnología de
entrega (liposomal, nanoemulsión, fitosoma) que nunca se comparó contra nada.

Términos: **biodisponibilidad absoluta (absolute bioavailability, F)** = fracción de la dosis administrada
que llega intacta a circulación sistémica, tomando la vía intravenosa como 100 %. **Biodisponibilidad
relativa** = comparación entre dos productos orales, sin necesidad de vía IV. **Efecto de primer paso
(first-pass effect)** = metabolismo que sufre la sustancia en pared intestinal e hígado antes de llegar a
la circulación general. **Circulación portal (portal circulation)** = la sangre del intestino va primero al
hígado, no directo al corazón.

## Por qué existe el primer paso

```
Boca → estómago → intestino delgado
                       │ absorción
                       ▼
                 VENA PORTA  ──►  HÍGADO  ──►  circulación sistémica
                                    │
                                    └─ CYP450 (fase I) + conjugación (fase II)
                                       destruyen o conjugan parte de la dosis
```

Todo lo que se absorbe en el intestino pasa **obligatoriamente** por el hígado antes de llegar al resto del
cuerpo. Además, la propia pared intestinal tiene CYP3A4 y transportadores de expulsión (P-gp), así que hay
un doble filtro.

Ejemplos con respaldo clínico:

| Sustancia | F oral aproximada | Motivo dominante |
|---|---|---|
| Δ9-THC oral | baja y muy variable (reportado ~6–20 % en la literatura) | Lipofilia + primer paso hepático |
| CBD oral | baja y variable, muy dependiente de comida grasa `[clínico]` | Primer paso + solubilidad |
| Curcumina libre | muy baja sin potenciador `[clínico]` | Conjugación fase II masiva |
| β-glucano de alto PM | prácticamente nula como molécula intacta | No se absorbe: es un polímero grande (`130`) |

Ese último caso es central para hongos: si la molécula no se absorbe, su mecanismo **tiene que ser local**
(intestino, células inmunes de la mucosa), no sistémico. Esa es una conclusión química, no una opinión.

## Cómo se calcula F

```
                AUC_oral / Dosis_oral
F_absoluta  =  ─────────────────────────
                AUC_IV   / Dosis_IV

                AUC_test / Dosis_test
F_relativa  =  ────────────────────────      (contra un producto de referencia)
                AUC_ref  / Dosis_ref
```

Para poder decir "3 veces más biodisponible" necesitas la segunda fórmula, con **el mismo analito, la misma
dosis molar, el mismo diseño cruzado y el mismo estado de ayuno**. Sin eso es publicidad.

Criterios de bioequivalencia (marco regulatorio de referencia, usado por FDA y EMA a agosto de 2026): el
intervalo de confianza del 90 % del cociente test/referencia para AUC y Cmax debe caer entre 80 % y 125 %.
Ese es el estándar contra el cual se mide qué tan seria es una afirmación comparativa.

## Las tecnologías de entrega, sin humo

| Tecnología | Qué hace en teoría | Qué exigir |
|---|---|---|
| Nanoemulsión | Reduce tamaño de gota, aumenta superficie y solubilización | Tamaño de partícula (DLS), estabilidad, AUC comparativa `[clínico]` |
| Liposoma | Encapsula en vesícula lipídica | Eficiencia de encapsulación real, no solo "es liposomal" |
| Fitosoma / complejo con fosfolípido | Mejora permeabilidad | Caracterización del complejo + PK humana |
| Ciclodextrina | Aumenta solubilidad aparente | Constante de complejación, ensayo de disolución |
| Piperina como potenciador | Inhibe glucuronidación y P-gp `[clínico]` | Cuidado: **también inhibe el metabolismo de fármacos** (`139`) |
| Autoemulsificable (SEDDS) | Se emulsiona solo al contacto con fluido gástrico | Ensayo de dispersión + PK |

Regla dura: **"liposomal" en la etiqueta no es un dato analítico.** Pide tamaño de vesícula por DLS,
eficiencia de encapsulación y, sobre todo, la AUC comparativa. La mayoría de los productos "liposomales"
del mercado latinoamericano no tienen ninguno de los tres.

Y una advertencia que casi nadie da: **aumentar la biodisponibilidad aumenta también el riesgo de
interacción y de efecto adverso**. Si la piperina sube la exposición del activo, también sube la de
cualquier fármaco que la persona esté tomando.

## Cómo se mide

| Nivel | Ensayo | Costo/tiempo | Qué permite afirmar |
|---|---|---|---|
| Barato | Disolución in vitro (USP aparato 2) | días | Que el producto libera el activo, nada más |
| Medio | Permeabilidad Caco-2 o PAMPA | semanas | Permeabilidad aparente `[in vitro]` |
| Medio-alto | PK en roedor | meses | Tendencia `[animal]`, no traducible directo |
| Alto | PK cruzada en humanos, 12–24 sujetos | 6–12 meses | "Mayor biodisponibilidad" con evidencia real |

## Ejemplo aplicado — auditar un "extracto de reishi liposomal"

Ficha del proveedor **(ILUSTRATIVO)**: "Absorción hasta 10 veces superior. Tecnología liposomal."

Preguntas, en orden, y qué pasa normalmente:

1. ¿10 veces superior **frente a qué**? Casi siempre la respuesta es "frente al polvo crudo", sin estudio.
2. ¿Qué analito se midió en plasma? Si el activo declarado es β-glucano, la pregunta se vuelve absurda:
   un β-glucano de alto peso molecular no se cuantifica en plasma como tal. La afirmación es imposible de
   sostener con el analito que el propio producto declara.
3. ¿Hay tamaño de partícula por DLS y eficiencia de encapsulación? Si no, no hay liposoma demostrado.
4. Conclusión de auditoría: la afirmación no es verificable y expone a la marca. Se retira del material y
   se sustituye por lo que sí se puede medir (contenido de β-glucano por Megazyme, `221`).

## Errores comunes

- Decir "más biodisponible" sin producto de referencia, sin AUC y sin diseño cruzado.
- Reclamar absorción sistémica de una molécula que no se absorbe (β-glucanos, la mayoría de polisacáridos).
- Comparar un estudio en ayuno contra otro con comida y atribuir la diferencia a la tecnología.
- Usar disolución in vitro como prueba de biodisponibilidad. Mide liberación, no absorción.
- Olvidar que un potenciador de absorción es también un potenciador de interacciones (`124`, `139`).
- Confundir biodisponibilidad con bioaccesibilidad (lo que queda disponible en el lumen). Son distintas.

## Conexión con otros módulos

→ `121-farmacocinetica-adme.md` — el marco completo del que sale F.
→ `123-vias-de-administracion.md` — la vía que evita el primer paso.
→ `125-metabolismo-de-fase-ii.md` — la conjugación que destruye la curcumina y compañía.
→ `159-potenciadores-de-biodisponibilidad.md` — el catálogo con evidencia por tecnología.
→ `157-emulsiones-y-nanoemulsiones.md` — cómo se hace y cómo se caracteriza de verdad.
