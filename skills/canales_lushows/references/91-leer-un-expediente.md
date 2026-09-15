# 91 · Leer un expediente

**Qué resuelve:** un PDF de 90 páginas en jerga jurídica y en inglés da miedo. En
realidad sólo cuatro sitios del documento contienen lo que el episodio necesita.

---

## Los tres documentos que importan

| Documento | Qué es | Qué aporta al guion |
|---|---|---|
| **Acusación** (*indictment*) | Lo que el gran jurado imputa. Son **alegaciones** | La estructura del negocio contada por el fiscal, y la lista de delitos |
| **Acuerdo de culpabilidad** (*plea agreement*) | El acusado admite hechos por escrito | **Hechos admitidos**: la mejor cifra posible, ya no discutible |
| **Sentencia** (*judgment* y memorandos de sentencia) | La pena, la restitución y el decomiso | El total final: cuánto se le quitó y cuánto debe devolver |

Añadir cuando existan: **demanda civil de la SEC**, **informe del examinador o del
síndico** de la quiebra y **demanda civil de decomiso** contra los bienes.

## Anatomía de una acusación

1. **Encabezado** (*caption*) — tribunal, distrito, número de caso, nombres. De aquí
   sale la cita exacta y el número con el que se busca todo lo demás.
2. **Alegaciones generales** (*introduction / general allegations*) — el relato del
   fiscal: quién era quién, qué empresas usó, cómo movía el dinero. **Es la mejor
   sinopsis del caso que existe** y suele ocupar de 5 a 20 páginas.
3. **Los cargos** (*counts*) — cada cargo es un delito concreto con su ley citada
   (fraude electrónico, blanqueo, conspiración, falsedad contable, evasión). Contar
   cuántos cargos hay y **de qué tipo** describe el negocio mejor que un adjetivo:
   veinte cargos de blanqueo dicen que el problema era mover el dinero, no ganarlo.
4. **Decomiso** (*forfeiture allegation*) — al final, casi siempre. Es la **lista de
   bienes** y la cifra que el gobierno reclama. Aquí aparecen los apartamentos, los
   relojes, los coches, las cuentas y su saldo.
5. **Anexos y tablas** — transferencias con fecha e importe, cuentas, propiedades.
   El anexo es la mina; el cuerpo del documento sólo lo resume.

## Anatomía de un acuerdo de culpabilidad

- **Base fáctica** (*statement of facts / factual basis*) — el acusado **reconoce**
  estos hechos. Todo lo que esté aquí se puede afirmar sin condicionales.
- **Cargos a los que se declara culpable** — casi siempre menos que en la acusación.
  Si el episodio dice "condenado por 27 cargos" y el acuerdo redujo a 2, es un error.
- **Cálculo de la pena** — la aritmética de las directrices: el nivel sube según la
  **cuantía del perjuicio** y el **número de víctimas**. Ahí hay dos cifras utilizables.
- **Restitución y decomiso** — importe acordado, a veces como sentencia monetaria
  (*money judgment*) por una cifra fija.
- **Cooperación** — si coopera, la pena baja. Explica por qué alguien salió antes.

## Anatomía de una sentencia

- **Fallo** — pena de prisión, libertad supervisada, multa.
- **Orden de restitución** — a quién y cuánto. Suele venir con una **lista de víctimas
  y su pérdida individual**: material para una escena de datos.
- **Orden de decomiso preliminar y final** — el inventario definitivo.
- **Memorandos de sentencia** de fiscalía y defensa — no son neutrales, pero es donde
  cada parte pone **su mejor cifra** y la argumenta. Se citan con atribución.

## Cómo se extrae la cifra utilizable

1. Localizar el número **en el documento**, con página y párrafo.
2. Anotar **qué mide exactamente**: ¿ingreso bruto?, ¿perjuicio a las víctimas?,
   ¿saldo incautado?, ¿valor de mercado estimado?, ¿reclamado o adjudicado? Son cuatro
   cifras distintas para el mismo caso y confundirlas es el error clásico.
3. Anotar **el periodo**: "entre 2003 y 2011" no es lo mismo que "en 2011".
4. Anotar **si es alegación o hecho probado** y con qué palabra se dirá en la voz.
5. Guardar la cita: documento, página, párrafo → `archivo/fuentes.json`.
6. Si la cifra se transforma (conversión de moneda, ajuste, promedio por año), eso ya
   es cálculo propio y se marca como tal (§ `92`).

## El lenguaje: alegado vs probado

| Situación | Cómo se dice en la voz |
|---|---|
| Acusación presentada | "la fiscalía lo acusó de…", "según la acusación…" |
| Hecho admitido en el acuerdo | "él mismo reconoció que…", "admitió haber…" |
| Condena firme | "fue condenado por…" |
| Demanda civil de un regulador | "la SEC lo demandó por…" |
| Caso caído, absuelto o archivado | Se dice, aunque estropee el remate |

**Nunca** convertir una alegación en afirmación por comodidad de guion. Es el único
punto del canal donde hay riesgo legal real, y además destruye la credibilidad.

## Trabajar el PDF

- Documentos escaneados antiguos no tienen texto: pasar OCR antes de buscar.
- Buscar directamente los términos que llevan a las cifras: `$`, "approximately",
  "in excess of", "forfeiture", "restitution", "loss amount", "Exhibit".
- Los expedientes vienen sellados arriba con **número de documento y de página del
  tribunal**: esa numeración es la que se cita, no la del visor de PDF.
- Marcar en el PDF cada página usada; al verificar (§ `96`) se vuelve a ellas.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Confundir lo reclamado con lo incautado | La cifra estrella del episodio queda inflada y desmentible |
| Sumar cargos de la acusación como si fueran condenas | Afirmación falsa sobre una persona concreta |
| Usar el total del caso completo para un solo acusado | Se le atribuye a uno lo que hicieron veinte |
| Ignorar el periodo de la cifra | "Ganaba mil millones al año" cuando eran mil millones en ocho años |
| Citar la página del visor y no la del tribunal | Nadie puede comprobarlo; en la práctica es una cita rota |
| Dar por buena una traducción al vuelo de un término jurídico | *Indictment*, *complaint* y *conviction* no son lo mismo |

## Relacionado

`90` fuentes primarias · `92` el aporte original · `95` cifras que se entienden al oírlas ·
`96` verificación de datos
