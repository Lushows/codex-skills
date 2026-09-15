# 182 · Obra del gobierno federal de EE.UU.

**Qué resuelve:** es la mejor cantera de archivo del canal —expedientes del FBI, fotos
de la DEA, vistas del Congreso, NASA, NARA, tribunales— y la que más se usa mal. La
regla es sólida **y estrecha**. Aquí está su borde exacto y cómo se comprueba sin
suponer nada.

> ⚠️ **Esto no es asesoría legal.** Es el criterio de producción del canal.

---

## La regla

La ley estadounidense de copyright establece que **la protección no está disponible para
ninguna obra del Gobierno de los Estados Unidos**
([17 U.S.C. § 105](https://www.law.cornell.edu/uscode/text/17/105)). Y «obra del
Gobierno de los Estados Unidos» está definida como la **preparada por un funcionario o
empleado del Gobierno de EE.UU. como parte de sus funciones oficiales** (definición del
§ 101, recogida en las notas del propio § 105).

Traducido al oficio: si la hizo un empleado federal haciendo su trabajo, **nace en
dominio público**. No por antigüedad: **por origen**. Por eso es la fuente preferida del
canal — no depende de una fecha que se mueve cada año (§ 181).

Eso cubre justo lo que piden las historias de dinero:

- Fichas policiales, carteles de búsqueda y fotografía del **FBI**.
- Imagen operativa de la **DEA**, aduanas y **Servicio Secreto**.
- **Vistas del Congreso** (las comparecencias: oro puro para un caso tipo Enron).
- Documentos y resoluciones de **tribunales federales**.
- **NARA** (Archivos Nacionales) y **DVIDS** (imagen militar), ya presentes en el
  `fuentes.json` del piloto.
- **NASA** y agencias científicas.

## Los cuatro bordes donde se rompe

Esta es la parte que casi nadie comprueba. La regla **no** cubre:

1. **Contratistas.** Un fotógrafo contratado no es empleado federal. Su obra puede tener
   copyright propio aunque esté publicada en una web `.gov` y aunque la haya pagado el
   Gobierno.
2. **Gobiernos estatales, de condado y municipales.** «Gobierno de EE.UU.» significa
   **federal**. La policía de un estado, un tribunal estatal o un ayuntamiento se rigen
   por reglas propias, y varían de un estado a otro.
3. **Otros países.** Los gobiernos de la mayoría de países **sí** tienen copyright sobre
   sus obras. Una foto de un ministerio europeo o de una policía latinoamericana no
   hereda nada de esta regla.
4. **Material ajeno alojado en una web federal.** Es la confusión más común y la más
   cara: las agencias publican **fotos de agencia** (§ 186), capturas de prensa y
   material cedido. Estar en `fbi.gov` no lo convierte en federal.

Dos matices más, para no exagerar la regla en la otra dirección:

- El Gobierno **sí puede recibir y ostentar copyrights** que le transfieran por cesión o
  legado. Que una obra sea «suya» no siempre equivale a que sea libre.
- La propia norma aclara que esta exclusión **no pretende afectar a la protección de
  esas obras en el extranjero**. Nuestro criterio operativo sigue siendo usarlas
  —Commons las acepta como dominio público— pero conviene conocer el matiz antes de
  afirmar en público que «son libres en todo el mundo».

## Cómo se verifica en la ficha de Commons

Nunca por el dominio de la URL. Siempre por la **plantilla de licencia del archivo**:

| Lo que aparece en la ficha | Lectura |
|---|---|
| `PD-USGov` | Obra federal genérica ✅ |
| `PD-USGov-DOJ`, `PD-USGov-FBI`, `PD-USGov-DEA` | Agencia concreta ✅ |
| `PD-USGov-NASA` | NASA ✅ (ojo: NASA aloja imágenes de socios que **no** lo son) |
| `PD-USGov-Military`, `PD-USGov-DOD` | Defensa / DVIDS ✅ |
| `PD-USGov-Congress` | Material del Congreso ✅ |
| `PD-US` / `PD-US-expired` a secas | **No es esta regla**: es antigüedad (§ 181) |
| `Attribution` con nombre y apellidos de un fotógrafo | Es CC, no federal: hay que atribuir (§ 184) |
| Sin plantilla, solo «source: fbi.gov» | ❌ no verificado: descartar |

Comprobación de treinta segundos, por pieza y por escrito:

1. Abrir la **ficha del archivo**, no el resultado de búsqueda.
2. Leer la plantilla de licencia: ¿dice `PD-USGov…`?
3. Leer el campo **autor**: ¿es una agencia federal, o un nombre propio y un estudio?
4. Leer el campo **fuente**: ¿es NARA / DVIDS / la agencia, o un periódico?
5. Copiar el texto de la licencia **tal cual** a `fuentes.json`. Sin resumir.

## La señal de alarma

Si en la ficha aparece un **nombre propio de fotógrafo sin mención de agencia federal**,
o palabras como *courtesy of*, *handout*, *pool photo*, *via*, la pieza se trata como no
federal hasta demostrar lo contrario. `handout` y `pool` son vocabulario de prensa, y la
prensa no regala copyright.

## Por qué esto manda en nuestro sondeo

El archivo federal es lo que hace ilustrable un caso: la estafa se prueba con **el
expediente**, y el expediente es federal. Por eso los términos del sondeo apuntan ahí a
propósito —`Wanted posters of the Federal Bureau of Investigation`,
`United States Secret Service`, `United States congressional hearings`— y por eso una
categoría federal rinde más piezas utilizables que diez búsquedas libres (§ 172).

Contrapartida real, vista en el piloto: el archivo federal es mayoritariamente
**actual**. Media docena de piezas de DVIDS se descartaron en el recorte por uniforme
militar de hoy imposible de empatar con una escena de 1925. Libre no es lo mismo que
utilizable (§ 198).

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| «Está en una web `.gov`, es libre» | La confusión nº 1: las agencias publican material ajeno |
| Tratar una foto de policía estatal como federal | Fuera de la regla; régimen distinto por estado |
| Aplicar la regla al gobierno de otro país | Falso: la mayoría sí tiene copyright |
| Dar por federal la obra de un contratista | Puede tener copyright propio pese a pagarla el Gobierno |
| Ignorar «courtesy of» / «handout» en el pie | Es material de prensa colado en un archivo público |
| Anotar «gobierno EE.UU.» sin la plantilla exacta | En una reclamación no hay prueba que enseñar (§ 189) |
| Confiar en que si es federal, encaja en la escena | La mayoría del archivo federal es de hoy: anacronismo garantizado |

## Relacionado

`177` archivos federales de EE.UU. · `180` las familias de licencia ·
`181` dominio público por antigüedad · `186` fotos de agencia ·
`188` `fuentes.json` como compuerta
