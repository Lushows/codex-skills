# 216 — Biología fúngica y ciclo de vida (por qué la química cambia según la etapa)

No puedes discutir de calidad de hongos sin entender que "el hongo" son varias cosas a lo largo de su vida,
y cada una tiene composición distinta. Una espora, una red de hifas creciendo dentro de un tronco y una seta
madura son el mismo organismo en etapas diferentes, con paredes celulares distintas, metabolitos distintos y
rendimientos distintos. Quien vende suplementos suele confundir eso a propósito: te vende una etapa barata
diciendo el nombre de la otra. Este módulo es la base biológica que hace que `217` y `218` tengan sentido.

Términos: **hifa (hypha)** = filamento celular del hongo. **micelio (mycelium)** = conjunto de hifas.
**cuerpo fructífero (fruiting body / sporocarp)** = estructura reproductiva, la "seta". **esclerocio
(sclerotium)** = masa compacta y endurecida de hifas con reservas, como el chaga. **primordio (pin /
primordium)** = la seta bebé. **sustrato (substrate)** = el material sobre el que crece.

## El ciclo, en cristiano

```
espora  ->  hifa primaria  ->  micelio (colonización del sustrato)
                                  |
                                  |  senal ambiental: caida de temperatura, luz, CO2 bajo, humedad
                                  v
                            primordio  ->  cuerpo fructifero  ->  esporas
```

La transición clave para tu producto es la del medio: **el micelio no fructifica solo**. Necesita un cambio
ambiental (baja de CO₂, luz, choque térmico, aire fresco). En fermentación industrial —tanques líquidos o
bandejas de grano— ese cambio no se da: el productor se queda con micelio, que es mucho más rápido y barato
de producir. Ahí nace el problema comercial del bloque (ver `218`).

| Etapa | Tiempo típico | Qué se cosecha | Costo relativo |
|---|---|---|---|
| Micelio en fermentación líquida | 3–10 días | Biomasa + caldo | Muy bajo |
| Micelio sobre grano (arroz/avena) | 2–4 semanas | Grano colonizado, entero | Bajo |
| Cuerpo fructífero cultivado | 2–6 meses (reishi) | Solo la seta | Alto |
| Esclerocio silvestre (chaga) | 5–20 años | El conk del abedul | Muy alto, no cultivable a escala |

Los tiempos son órdenes de magnitud del cultivo comercial y varían mucho por especie, cepa y condiciones;
verifica con tu productor.

## Qué es la pared celular fúngica (y por qué es el activo)

La pared del hongo no es celulosa como en plantas: es **quitina (chitin)** —un polímero de
N-acetilglucosamina— más una matriz de **glucanos**, mayoritariamente β-(1→3) con ramas β-(1→6). Esa matriz
es lo que se vende como "beta-glucanos" y lo que reconoce el sistema inmune innato `[in vitro]` `[animal]`
a través de receptores como Dectin-1 (ver `130`).

Consecuencia práctica número uno: **el activo está encerrado en una pared rígida.** Por eso los hongos se
extraen con agua caliente o se muelen fino: sin romper la pared, el β-glucano no sale y la biodisponibilidad
es baja (ver `241`). Consecuencia número dos: el contenido de quitina sube la fibra insoluble y puede
inflar mediciones gravimétricas mal hechas.

## Genética, cepa y variabilidad

Dos lotes de la misma especie pueden diferir mucho porque:

- **Cepa (strain)**: dentro de *Ganoderma lucidum* hay cepas con rendimiento y perfil de triterpenos
  distintos. Un estudio sobre *G. lucidum* mostró que el contenido de β-glucano en cuerpo fructífero depende
  de la cepa y del sustrato de madera usado (Sánchez-Hernández et al., *Journal of Fungi*, 2020;
  PMC7587577).
- **Sustrato**: la madera, el grano o el suplemento nitrogenado cambian el metabolismo (ver `239`).
- **Etapa de cosecha**: antes o después de la esporulación cambia el peso y la composición.
- **Ambiente**: luz, temperatura y estrés oxidativo modifican metabolitos como la ergotioneína (ver `235`).

Por eso una especificación honesta se construye con **varios lotes y un rango**, no con un análisis suelto
(ver `282`).

## Cómo se mide / cómo se comprueba

| Pregunta biológica | Cómo se responde en laboratorio | Unidad |
|---|---|---|
| ¿Qué especie es? | Secuenciación ITS y comparación en base de datos | % de identidad |
| ¿Hay biomasa fúngica real o solo grano? | Ergosterol por HPLC-UV 282 nm | `mg/g base seca` |
| ¿Cuánto de la pared es β-glucano? | Megazyme K-YBGL (glucano total − α-glucano) | `% p/p base seca` |
| ¿Cuánta quitina hay? | Glucosamina tras hidrólisis ácida (CG o HPLC) | `% p/p base seca` |
| ¿El material está seco y comparable? | Karl Fischer o pérdida por secado | `% humedad` |

## Ejemplo aplicado

Un proveedor te ofrece "Cordyceps 10:1". Preguntas la etapa y responde: "biomasa de fermentación líquida,
cepa CS-4". Eso significa **micelio**, no cuerpo fructífero, y de una especie que muchas veces no es
*Ophiocordyceps sinensis* verdadera. La consecuencia química directa: puedes tener cordicepina baja o nula
y β-glucano bajo. **(ILUSTRATIVO)** un lote así podría dar β-glucano 6 % p/p base seca y cordicepina por
debajo del límite de cuantificación, mientras un cuerpo fructífero de *Cordyceps militaris* da cifras muy
superiores (ver `227`, `228`). No lo asumas: mídelo.

## Errores comunes

- Creer que "micelio = raíz del hongo, más potente". Es marketing; biológicamente no es una raíz y
  químicamente suele ser más pobre en β-glucanos (ver `217`).
- Comparar lotes cosechados en etapas distintas sin decirlo: antes o después de esporular no es lo mismo.
- Ignorar la cepa en la especificación. Cambiar de cepa es cambiar de materia prima.
- Asumir que el hongo silvestre es "más puro". El silvestre acumula lo que haya en el ambiente: metales,
  radionúclidos, contaminación (ver `243`, `230`).
- Moler grueso y luego extraer: la pared no se rompe y el rendimiento cae sin que nadie sepa por qué
  (ver `143`).

## Conexión con otros módulos

→ `217-micelio-vs-cuerpo-fructifero.md` — la comparación química, con números.
→ `239-sustrato-cultivo-y-quimica-resultante.md` — cómo el sustrato queda escrito en el análisis.
→ `238-ergosterol-como-marcador.md` — el marcador que dice si hay hongo de verdad.
→ `245-identidad-de-especie-por-its.md` — cómo se prueba la especie.
→ `130-inmunomodulacion-y-beta-glucanos.md` — qué hace la pared celular en el cuerpo, con nivel de evidencia.