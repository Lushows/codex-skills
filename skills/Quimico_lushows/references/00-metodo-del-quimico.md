# 00 — El método del químico (cómo se piensa antes de creerle a un número)

Este es el módulo raíz de la skill. Aquí no hay fórmulas: hay una forma de pensar. Un químico no es
alguien que se sabe la tabla periódica de memoria; es alguien que, ante cualquier afirmación —"este
extracto tiene 30 % de beta-glucanos", "esta flor da 18 % de THC", "esto es 10:1"— hace siempre las
mismas cinco preguntas antes de aceptarla. Si aprendes a hacer esas cinco preguntas, ya puedes
defenderte de la mayoría de los proveedores que le venden humo a la gente que vende suplementos.
El error caro que esto evita es sencillo: pagar por un activo que no está, o poner en la etiqueta un
número que no puedes sostener si un laboratorio o el INVIMA lo va a verificar.

Términos: **analito (analyte)** = la sustancia específica que quieres medir. **matriz (matrix)** = todo
lo demás que la acompaña en la muestra y le estorba a la medición. **método analítico (analytical
method)** = el procedimiento completo, escrito, con el que se obtiene el número. **base (basis)** =
sobre qué masa se expresa el resultado (base húmeda, base seca, base "tal cual").

## Las cinco preguntas

| # | Pregunta | Qué destapa cuando falta |
|---|---|---|
| 1 | ¿**Qué** exactamente se midió? (analito) | "Polisacáridos" en vez de β-glucano; "cannabinoides totales" en vez de THC total |
| 2 | ¿**Sobre qué material**? (matriz) | Micelio en grano vendido como cuerpo fructífero; extracto vs materia prima |
| 3 | ¿**Con qué método**? | Colorimétrico barato vs enzimático específico; "método interno" sin referencia |
| 4 | ¿**En qué unidad y base**? | 30 % base seca vs 30 % "tal cual" con 12 % de humedad: no son el mismo número |
| 5 | ¿**Quién lo midió y cuándo**? | Laboratorio del propio proveedor, sin acreditación, sin lote, sin fecha |

Si una de las cinco no tiene respuesta, el número **no se afirma**. Se dice "hay que medirlo" y se
explica cómo. Esa es toda la disciplina.

## El arco de trabajo (siempre el mismo)

```
1. DECISIÓN     ¿Qué vas a decidir con este dato? (comprar, etiquetar, formular, defenderte)
2. PREGUNTA     Traducir la decisión a una pregunta medible, con analito, matriz, unidad y base.
3. MÉTODO       Elegir la técnica capaz de responderla (y descartar las que no pueden).
4. MUESTRA      Muestrear bien. Un mal muestreo arruina el mejor instrumento del mundo.
5. MEDIDA       Ejecutar o encargar el análisis, con patrón de referencia y control de calidad.
6. VERIFICACIÓN Revisar el dato: ¿tiene sentido físico? ¿cuadra el balance de masa? ¿otra vía lo confirma?
7. DECISIÓN     Volver al punto 1 y decidir, dejando por escrito el nivel de confianza.
```

El paso 6 es el que casi nadie hace y el que separa a un químico de un lector de PDF. Un resultado
que no se puede contrastar contra otra cosa (balance de masa, un segundo método, un rango esperado
de la literatura) es un rumor con membrete.

## Por qué el orden importa: la decisión manda sobre el método

No se mide "para saber". Se mide para decidir. Y la decisión define cuánta exactitud necesitas, lo
cual define cuánto vas a gastar.

| Decisión | Exactitud que necesitas | Método razonable | Costo relativo |
|---|---|---|---|
| Descartar un proveedor obviamente malo | Baja (orden de magnitud) | Colorimétrico o HPTLC | Bajo |
| Elegir entre dos lotes para comprar | Media (±10 % relativo) | Enzimático o HPLC-UV | Medio |
| Poner el número en la etiqueta | Alta (método validado) | HPLC-UV / LC-MS validado ICH Q2 | Alto |
| Sostener un expediente ante autoridad | Alta + trazable | Método oficial (AOAC/USP) en lab ISO 17025 | Muy alto |

Gastar en el nivel 4 para una decisión de nivel 1 es quemar plata; usar el nivel 1 para etiquetar es
exponerte a una sanción.

## Cómo se comprueba que estás usando el método

Chequeo rápido antes de aceptar cualquier dato que te manden:

- El documento nombra el **método** (norma, código, o descripción del procedimiento), no solo el resultado.
- Aparece **lote** e **identificación del material**, no solo el nombre comercial.
- Hay **unidad** y **base** explícitas.
- Hay **fecha** y **quién firma**.
- Hay **límite de cuantificación (LOQ)** cuando el resultado es "no detectado".
- Los números tienen **cifras significativas** coherentes (un "30,000 %" es señal de que alguien copió y pegó).

## Ejemplo aplicado (BIO-SETA)

Te ofrecen un extracto de reishi (*Ganoderma lucidum*) "40 % polisacáridos, 10:1". Aplicas las cinco
preguntas y el proveedor responde: analito = "polisacáridos totales"; matriz = "extracto de hongo";
método = "método interno colorimétrico fenol-sulfúrico"; base = no dice; laboratorio = propio.

Traducción honesta: **no sabes cuánto β-glucano hay**. El fenol-sulfúrico responde a azúcares en
general, incluido el almidón del grano del sustrato (α-glucano). El dato que te importa —β-glucano por
método enzimático, sobre base seca— no existe todavía. Costo de averiguarlo: un ensayo enzimático tipo
Megazyme K-YBGL en un laboratorio externo, orden de magnitud USD 120–250 por muestra **(ILUSTRATIVO,
verificar cotización vigente)**. Esa plata es barata comparada con comprar 50 kg de almidón caro.

Si tras medir el resultado fuera, por ejemplo, β-glucano 12,4 % p/p base seca y α-glucano 46 % p/p
base seca **(ILUSTRATIVO)**, el "40 % polisacáridos" era cierto y a la vez inútil: la mayor parte era
almidón. El proveedor no mintió; tú no preguntaste bien.

## Errores comunes

- **Aceptar el número y no el método.** El número es la conclusión; el método es el argumento. Sin
  argumento, no hay conclusión.
- **Comparar dos COA de laboratorios distintos como si fueran la misma regla.** Métodos distintos
  miden cosas distintas; solo son comparables si comparten método, matriz y base.
- **Medir lo que es barato en vez de lo que decide.** Muchos pagan microbiología (barata) y nunca miden
  el activo por el que cobran.
- **Pedir "un análisis completo"** sin decir qué vas a decidir: el laboratorio te vende lo que le sobra
  en agenda y te quedas sin el dato que necesitabas.
- **Confundir precisión con exactitud.** Tres réplicas que dan siempre lo mismo pueden estar siempre
  igual de equivocadas (ver `05` y `74`).
- **No guardar contramuestra.** Si no reservaste material del mismo lote, no puedes impugnar nada después.

## Conexión con otros módulos

→ `01-como-usar-esta-skill.md` — cómo pedirle a esta skill el trabajo concreto que necesitas.
→ `02-ningun-dato-sin-metodo.md` — la promesa central, con el formulario de las preguntas.
→ `04-unidades-concentraciones-y-conversiones.md` — para no perderte entre %, mg/g y ppm.
→ `07-base-seca-vs-humeda.md` — la base, que es donde se cae la mitad de las comparaciones.
→ `12-niveles-de-evidencia.md` — cuando el dato no es una cantidad sino un efecto.
→ `65-el-metodo-analitico-de-punta-a-punta.md` — la versión larga y técnica de este arco.
→ `110-como-leer-un-coa.md` — aplicar todo esto a un certificado real.