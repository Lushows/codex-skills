# 01 — Cómo usar esta skill (qué pedirle y cómo pedirlo)

Esta skill tiene 300 módulos, pero nunca se cargan todos: se cargan de dos a seis según lo que estés
resolviendo. Este módulo te enseña a formular el pedido para que la respuesta te sirva de una vez, sin
tres rondas de "es que me faltaba decirte que era micelio". La diferencia entre una respuesta útil y
una respuesta genérica está casi siempre en cuatro datos que tú ya tienes y no diste: qué material,
qué lote, qué método y qué decisión depende del resultado. Si los das al inicio, la respuesta llega
con método, unidad, base y siguiente paso concreto.

Términos: **módulo (module)** = uno de los archivos de `references/`, con dueño único de su tema.
**modo (mode)** = el tipo de trabajo que estás pidiendo (auditar, diseñar, formular, cumplir, enseñar).
**ruteo (routing)** = mandar la parte que no es química a la skill que sí es dueña de ese tema.

## Los siete modos de trabajo

| Lo que dices | Modo | Lo que recibes |
|---|---|---|
| "Me llegó este certificado, ¿está bien?" | Auditar un análisis | Lectura línea por línea, banderas rojas, qué exigir |
| "¿Cómo mido X? ¿qué le pido al laboratorio?" | Diseñar el análisis | Técnica, método, unidad, LOQ esperado, costo y tiempo |
| "Quiero hacer/mejorar este producto" | Formular | Ruta de proceso, especificación, estabilidad, controles |
| "¿Qué puedo decir en la etiqueta?" | Cumplimiento y claims | Qué sostiene la evidencia, qué permite la norma, con fecha |
| "Explícame qué es esto" | Enseñar | Concepto con analogía, términos en inglés y ejemplo numérico |
| "¿Este proveedor me está estafando?" | Cazar fraude | Las preguntas que lo desnudan y el ensayo que lo confirma |
| "Voy a hablar con el químico de la UDCA" | Preparar la reunión | Agenda, preguntas, entregables y protocolo a acordar |

## La plantilla del buen pedido

Copia esto y llénalo. Cinco líneas te ahorran una semana:

```
MATERIAL:   qué es exactamente (cuerpo fructífero seco / micelio en grano / extracto / producto terminado)
LOTE:       identificación y fecha de producción; cuánta cantidad tienes
DATO:       qué dice el papel que tienes (número, unidad, base, método, laboratorio)
DECISIÓN:   qué vas a decidir con esto (comprar, etiquetar, formular, reclamar, registrar)
RESTRICCIÓN: presupuesto, tiempo, país donde se vende
```

Ejemplo real de pedido bien hecho: *"Material: extracto en polvo de melena de león, proveedor chino.
Lote MLE-2405. Dato: COA dice 'polysaccharides 30 %', método no especificado. Decisión: si lo compro
para 500 frascos y qué pongo en la etiqueta. Restricción: vendo en Colombia, presupuesto de análisis
hasta COP 1.500.000."* Con eso la respuesta puede ser específica y accionable.

## Qué esperar en cada respuesta

Toda respuesta técnica de esta skill trae, como mínimo:

1. **El dato con método, unidad y base** — o la declaración explícita de que no existe y hay que medirlo.
2. **El nivel de evidencia** cuando se habla de efectos: `[in vitro]`, `[animal]`, `[clínico fase N]`,
   `[tradicional/anecdótico]` (ver `12`).
3. **Qué falta por medir** y cuánto cuesta medirlo, en orden de magnitud.
4. **El siguiente paso concreto**, no una lista de posibilidades.

Y toda cifra que no venga de una fuente citada va marcada **(ILUSTRATIVO)**. Si ves un número sin
marca y sin fuente en una respuesta, exige la fuente: es exactamente el error que esta skill existe
para no cometer.

## Lo que esta skill no hace

- **No reemplaza al laboratorio.** Diseña el análisis, lo interpreta y lo audita; no produce el dato.
- **No reemplaza al químico que firma.** Un registro sanitario, un método validado o un expediente los
  respalda un profesional titulado con responsabilidad legal.
- **No da consejo médico ni claims de enfermedad.** Describe evidencia y traduce a lenguaje legal.
- **No da protocolos de producción de sustancias controladas** (ver la línea roja en `SKILL.md`).
- **No hace aritmética de memoria.** Todo cálculo que sostiene una decisión se ejecuta en código
  (`lab-tools/`) o se rutea a `Matematicas_lushows`.

## Cómo se comprueba que la respuesta sirvió

Antes de actuar sobre lo que te respondió, pásale este filtro:

| Chequeo | Si falla, qué pedir |
|---|---|
| ¿Cada número tiene método, unidad y base? | "Dime el método y la base de ese número" |
| ¿Los efectos tienen nivel de evidencia? | "¿Eso es in vitro, animal o clínico?" |
| ¿Los cálculos se ejecutaron? | "Corre esto en `lab-tools/` y muéstrame el resultado" |
| ¿Hay fecha en lo regulatorio? | "¿A qué fecha aplica y dónde verifico lo vigente?" |
| ¿Sé qué hacer mañana? | "Dame el siguiente paso concreto, uno solo" |

## Ejemplo aplicado (BIO-SETA)

Pedido flojo: *"¿Cuánto beta-glucano tiene el reishi?"* → respuesta necesariamente genérica, porque el
valor depende de especie, parte usada, sustrato, secado y método.

Pedido bueno: *"Tengo 20 kg de cuerpo fructífero seco de Ganoderma lucidum cultivado en tronco en
Colombia, cosecha marzo 2026. Quiero sacar un extracto acuoso y poner 'aporta X mg de β-glucanos por
porción' en la etiqueta. ¿Qué mido, en qué orden, y cuánto cuesta?"* → respuesta con secuencia:
(1) humedad por Karl Fischer o pérdida por secado; (2) β-glucano por enzimático Megazyme K-YBGL sobre
materia prima, base seca; (3) rendimiento de extracción medido en el lote piloto; (4) β-glucano del
extracto por el mismo método; (5) cálculo de mg/porción con `lab-tools/betaglucano_dosis.py`;
(6) tres lotes antes de fijar el número de la etiqueta (ver `282`).

## Errores comunes

- **Preguntar por el activo sin decir el material.** Micelio, cuerpo fructífero y extracto dan números
  distintos por diseño; la pregunta sin material no tiene respuesta.
- **Pedir "todo lo que se pueda medir".** Sale carísimo y no decide nada. Primero la decisión.
- **Traer el número sin el COA.** El PDF completo tiene el método, el lote y el LOQ; el WhatsApp del
  proveedor no.
- **Saltarse el modo de cumplimiento.** Formulas primero y descubres al final que el claim es ilegal
  en Colombia (ver `267`, `268`).
- **Usar la respuesta como si fuera el dato.** Una estimación explicada sigue siendo una estimación
  hasta que un laboratorio la confirma sobre tu lote.

## Conexión con otros módulos

→ `00-metodo-del-quimico.md` — la mentalidad que hay detrás de estos modos.
→ `02-ningun-dato-sin-metodo.md` — el formulario de preguntas que vuelve auditable cualquier dato.
→ `10-glosario-quimico-esencial.md` — para entender los términos que aparezcan.
→ `13-ruteo-a-otras-skills.md` — qué parte de tu problema no es química.
→ `14-como-trabajar-con-un-quimico-de-universidad.md` — cuando el siguiente paso es una reunión.
→ `110-como-leer-un-coa.md` — el modo "auditar" en detalle.
