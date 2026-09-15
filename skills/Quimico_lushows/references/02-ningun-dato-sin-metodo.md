# 02 — Ningún dato sin método (la promesa central de esta skill)

Esta es la regla que gobierna todo lo demás: **un número químico sin método, sin unidad y sin fuente
no es un dato, es publicidad**. En el mercado de suplementos y de cannabis, casi todo el fraude vive
en ese hueco. Nadie te miente diciendo "esto tiene 30 %" cuando no tiene nada; te dicen "30 %" de una
cosa que sí está, medida con un método que no distingue lo que a ti te importa, sobre un material que
no es el que crees. Es mentira por omisión, y es legal hasta que tú preguntas. Este módulo te da el
formulario de preguntas que convierte cualquier afirmación en algo auditable — o la desarma.

Términos: **método analítico (analytical method)** = procedimiento escrito completo: preparación de
muestra, técnica, calibración, cálculo y criterios de aceptación. **especificidad (specificity)** =
capacidad del método de medir el analito sin que otras cosas de la matriz se cuelen en la señal.
**trazabilidad (traceability)** = cadena documentada que une tu resultado con un patrón reconocido.
**COA (certificate of analysis)** = certificado de análisis; el papel que reporta el resultado.

## El formulario de seis campos

Ninguna afirmación numérica se acepta si le falta alguno:

| Campo | Pregunta | Ejemplo bueno |
|---|---|---|
| Analito | ¿Qué molécula o grupo exacto? | β-glucano (1,3;1,6) |
| Matriz | ¿Sobre qué material? | Extracto acuoso en polvo de cuerpo fructífero de *G. lucidum* |
| Método | ¿Con qué procedimiento? | Enzimático Megazyme K-YBGL (glucano total − α-glucano) |
| Valor + unidad | ¿Cuánto y en qué unidad? | 24,6 % p/p |
| Base | ¿Sobre qué masa? | Base seca (humedad 4,1 % por pérdida a 105 °C) |
| Fuente | ¿Quién, cuándo, qué lote? | Lab X acreditado ISO 17025, 2026-03-14, lote GL-2603 |

La forma corta que puedes memorizar: **analito, matriz, método, valor+unidad, base, fuente**. Es lo
mismo que exige una farmacopea; no te lo estás inventando tú.

## Por qué el método cambia el número (no es un detalle burocrático)

El mismo material analizado por dos métodos da dos números distintos y **ambos pueden ser correctos**,
porque miden cosas distintas. Ejemplos reales del oficio:

| Analito aparente | Método A | Método B | Por qué difieren |
|---|---|---|---|
| "Polisacáridos" en hongos | Fenol-sulfúrico (colorimétrico) | Enzimático β-glucano | A cuenta almidón y otros azúcares; B resta α-glucano |
| "THC" en cannabis | HPLC (no descarboxila) | GC-FID (descarboxila en el inyector) | GC convierte THCA en THC y reporta un solo pico |
| Proteína en biomasa | Kjeldahl (N × factor) | Aminoácidos por LC | Kjeldahl cuenta todo el nitrógeno, incluida quitina |
| "Antioxidantes" | ORAC / DPPH | Cuantificación del compuesto | Los primeros miden una reacción, no una sustancia |

Moraleja: **antes de comparar dos números, compara sus métodos.** Si los métodos difieren, los números
no se comparan; se comparan las conclusiones, con la incertidumbre encima.

## Los tres disfraces más frecuentes

1. **Sustituir el analito por un pariente barato.** "Polisacáridos totales" en vez de β-glucano;
   "cannabinoides totales" en vez de Δ9-THC + THCA×0,877 (ver `175`, `222`).
2. **Callar la base.** Un 30 % "tal cual" sobre material con 10 % de humedad es 33,3 % base seca; al
   revés, un 30 % base seca puede volverse 27 % en el frasco. La comparación sin base es humo (ver `07`).
3. **Callar el LOQ.** "No detectado" sin límite de cuantificación no dice nada: puede significar
   "por debajo de 0,01 ppm" o "por debajo de 5 ppm", que en metales pesados es la diferencia entre
   cumplir y no cumplir (ver `73`).

## Cómo se comprueba

Pide, por escrito, estas cinco cosas al proveedor o al laboratorio. Si alguna se niega, ya sabes algo:

```
1. Método completo (nombre, norma o SOP, y versión). Si dice "método interno", pedir el resumen del SOP.
2. Base del resultado y humedad del material analizado, con su método de humedad.
3. LOQ y LOD del método para ese analito en esa matriz.
4. Trazabilidad del patrón de referencia (proveedor, pureza, certificado).
5. Identificación del lote y fecha de muestreo, no solo fecha de emisión del certificado.
```

Verificación cruzada barata: pide **el mismo lote analizado por un segundo laboratorio**. Si los dos
números difieren más de lo que permite la incertidumbre del método, hay un problema y ahora es
demostrable (ver `112`).

## Ejemplo aplicado (BIO-SETA)

Afirmación recibida: *"Nuestro extracto de melena de león tiene 30 % de beta-glucanos."*

Aplicando el formulario, resulta: analito = "polisacáridos"; matriz = "mushroom extract" sin decir si
es micelio o cuerpo fructífero; método = no declarado; base = no declarada; fuente = laboratorio
interno del proveedor. Cinco de seis campos vacíos.

Reescritura honesta del claim, una vez medido de verdad **(ILUSTRATIVO)**:

> β-glucano total 21,3 % p/p en base seca (humedad 3,8 %, pérdida por secado a 105 °C), medido por
> ensayo enzimático Megazyme K-YBGL sobre extracto acuoso en polvo de cuerpo fructífero de *Hericium
> erinaceus*, lote HE-2604, laboratorio acreditado ISO 17025, informe del 2026-04-22. α-glucano
> 6,1 % p/p base seca.

Ese párrafo se puede defender ante un cliente, ante un competidor y ante una autoridad. El "30 %" del
principio no se puede defender ante nadie.

## Errores comunes

- **Tomar el número más alto de los COA que te mandaron.** Casi siempre el más alto es el del método
  menos específico.
- **Aceptar "método interno" sin más.** Puede ser excelente o puede ser un colorímetro sin calibrar;
  pide el resumen del procedimiento.
- **Poner en la etiqueta lo que dice el COA de la materia prima.** El activo cambia con el proceso; la
  etiqueta habla del producto terminado (ver `282`).
- **Creer que "acreditado" cubre todo.** Un laboratorio ISO 17025 lo está para un alcance específico:
  puede estar acreditado en metales y no en β-glucanos (ver `107`).
- **Perder la contramuestra.** Sin material reservado del mismo lote, no hay forma de impugnar.
- **Repetir el número del proveedor en tu marketing.** Si es falso, el que responde ante el cliente y
  ante la autoridad eres tú, no él.

## Conexión con otros módulos

→ `00-metodo-del-quimico.md` — la mentalidad de la que sale esta regla.
→ `03-honestidad-cientifica-y-fuentes.md` — cómo citar y cómo decir "no sé".
→ `04-unidades-concentraciones-y-conversiones.md` — la unidad, que es el tercio del formulario.
→ `07-base-seca-vs-humeda.md` — la base, el campo que más se calla.
→ `73-lod-loq-y-rango-lineal.md` — por qué "no detectado" no es "ausente".
→ `110-como-leer-un-coa.md` y `111-banderas-rojas-en-un-coa.md` — el formulario aplicado a un papel real.
→ `222-polisacaridos-totales-por-que-no-sirve.md` — el caso más caro de esta regla en hongos.
