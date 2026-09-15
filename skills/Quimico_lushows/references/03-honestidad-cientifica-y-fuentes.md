# 03 — Honestidad científica y fuentes (cómo citar, cómo dudar y cómo decir "no sé")

La honestidad científica no es una virtud moral abstracta: es una herramienta de gestión de riesgo.
Si dices un número que no puedes sostener, alguien tarde o temprano lo verifica —un competidor, un
cliente técnico, un laboratorio, una autoridad— y el costo no es la corrección, es la credibilidad de
todo lo demás que dijiste. Este módulo te enseña a distinguir los tipos de fuente, a citar de forma
que otro pueda verificar, y a marcar con claridad la frontera entre lo que sabes, lo que estimas y lo
que ignoras. Para una marca chica esa frontera bien marcada es una ventaja competitiva, porque casi
nadie en el sector la marca.

Términos: **fuente primaria (primary source)** = el estudio original donde se generó el dato.
**revisión por pares (peer review)** = filtro editorial en el que otros científicos evalúan el trabajo
antes de publicarlo. **preprint** = manuscrito publicado antes de pasar revisión por pares.
**conflicto de interés (conflict of interest)** = relación económica o personal que puede sesgar el
resultado. **DOI (digital object identifier)** = identificador permanente de un artículo.

## Jerarquía de fuentes (de más a menos confiable para un dato químico)

| Nivel | Fuente | Qué tan firme | Ojo con |
|---|---|---|---|
| 1 | Farmacopea (USP, EP, JP), método AOAC, norma ISO | Muy firme, consensuada | Versión y año; cambian |
| 2 | Metaanálisis y revisión sistemática con método declarado | Firme | Calidad de los estudios incluidos |
| 3 | Artículo primario en revista indexada con revisión por pares | Media-firme | n pequeño, financiación, matriz distinta |
| 4 | Tesis, capítulo de libro técnico, informe de agencia | Media | Sin revisión externa a veces |
| 5 | Preprint | Baja-media | Puede cambiar o no publicarse nunca |
| 6 | Nota técnica de fabricante de instrumento o kit | Útil pero interesada | Muestra el mejor caso posible |
| 7 | Blog, ficha comercial, IA sin fuente | No es fuente | Sirve para encontrar la fuente real, no para citar |

Regla práctica: **el nivel 7 nunca se cita; se usa para llegar al nivel 1–3 y se cita ese.**

## Cómo se cita para que sirva

Una cita útil permite que otra persona llegue al mismo documento sin preguntarte. Mínimo:

```
Autores (año). Título. Revista, volumen(número), páginas. DOI.
+ qué dice exactamente: página o tabla, y sobre qué matriz y método.
```

Y en el texto, siempre la traducción del alcance: no *"se demostró que…"* sino *"en 24 ratones, dosis
oral de 200 mg/kg durante 14 días, se observó…"*. El alcance es la mitad del dato. Un resultado
`[animal]` a 200 mg/kg no se convierte en una recomendación humana de 200 mg, ni de lejos (ver `134`).

## Las tres marcas obligatorias

En todo lo que escribas o entregues:

1. **(ILUSTRATIVO)** — cifra de ejemplo, inventada para explicar la cuenta, no medida. Nunca se usa en
   etiqueta, cotización ni expediente.
2. **Nivel de evidencia** — `[in vitro]`, `[animal]`, `[clínico fase N]`, `[tradicional/anecdótico]`
   (ver `12`).
3. **Fecha del dato regulatorio** — "a agosto de 2026…" más dónde verificar lo vigente. La norma cambia
   y el documento tiene que envejecer con honestidad.

## Cómo se dice "no sé" sin quedar mal

Decir "no sé" sin plan es debilidad; decirlo con plan es autoridad. La fórmula:

```
"No se sabe con tu material. Se sabe cómo averiguarlo:
 - se mide [analito] por [método] sobre [matriz], expresado en [unidad, base]
 - lo hace un laboratorio con [acreditación] en [tiempo estimado]
 - cuesta del orden de [rango] y decide [la decisión concreta]"
```

Eso convierte una laguna en una tarea con precio. Es exactamente lo que un químico universitario
espera oír de un cliente serio (ver `14`).

## Sesgos que te van a morder

| Sesgo | Cómo aparece en este oficio | Antídoto |
|---|---|---|
| Sesgo de publicación | Solo se publican los estudios que dieron positivo | Buscar revisiones sistemáticas y registros de ensayos |
| Financiación | El estudio lo pagó quien vende el ingrediente | Leer la declaración de conflicto de interés |
| Extrapolación de dosis | Dosis de ratón usada como dosis humana | Ver `134`, `135`; nunca convertir de memoria |
| Del in vitro al cuerpo | Un efecto en célula a 100 µM que jamás se alcanza en sangre | Comparar con la Cmáx real (ver `121`) |
| Confirmación | Buscar solo lo que apoya tu producto | Buscar activamente el estudio que te contradice |
| Autoridad | "Lo dijo un doctor" | Pedir la fuente primaria, no el nombre |

## Cómo se comprueba una afirmación que te llega

1. Localiza la **fuente primaria**, no el post que la resume.
2. Revisa **matriz y dosis**: ¿es tu especie, tu parte, tu forma de extracto, una dosis alcanzable?
3. Revisa el **n** y el diseño: ¿hubo control? ¿fue ciego? ¿aleatorizado?
4. Revisa **conflicto de interés** y financiación.
5. Busca si hay **réplica** o si es un hallazgo único de un solo grupo.
6. Traduce a nivel de evidencia y escribe la frase con su alcance.

## Ejemplo aplicado (BIO-SETA)

Circula la frase: *"la melena de león regenera los nervios"*. Rastreada, la mayoría de referencias
llegan a estudios `[in vitro]` de hericenonas y erinacinas sobre síntesis de factor de crecimiento
nervioso (NGF) en cultivos celulares, y a algunos `[animal]`, más un puñado de ensayos humanos
pequeños. Además, los compuestos estudiados están en extractos específicos y su presencia en tu
producto **hay que medirla**, no asumirla (ver `226`).

Frase honesta y defendible: *"En estudios de laboratorio `[in vitro]` y en modelos animales `[animal]`
se ha observado que ciertos compuestos de Hericium erinaceus estimulan la producción de NGF en células
nerviosas. La evidencia en humanos es limitada. Nuestro extracto declara su contenido de X medido por
[método]."* Sin claim de enfermedad, sin promesa de efecto, con el alcance a la vista (ver `268`, `293`).

## Errores comunes

- **Citar el resumen del resumen.** El "telefonito roto" cambia dosis, especie y conclusión.
- **Usar el nombre de la revista como argumento.** Importa el diseño del estudio, no el logo.
- **Convertir `[in vitro]` en promesa de venta.** Es el atajo que más sanciones cuesta en Colombia.
- **Presentar cifras ilustrativas sin marcarlas** y que terminen en una cotización o una etiqueta.
- **No fechar lo regulatorio.** Un documento sin fecha se vuelve mentira por el simple paso del tiempo.
- **Esconder el dato que no te gusta.** Si tu lote dio bajo, decirlo te compra credibilidad; ocultarlo
  te compra un problema con fecha diferida.

## Conexión con otros módulos

→ `02-ningun-dato-sin-metodo.md` — el formulario que hace auditable cada número.
→ `11-como-leer-un-paper-cientifico.md` — cómo desarmar un artículo en 20 minutos.
→ `12-niveles-de-evidencia.md` — la escala que hay que marcar siempre.
→ `05-cifras-significativas-e-incertidumbre.md` — cuántos decimales puedes defender.
→ `268-claims-prohibidos-el-caso-bioseta.md` — qué pasa cuando esto no se respeta.
→ `293-como-comunicar-ciencia-sin-mentir.md` — la traducción a lenguaje de cliente.