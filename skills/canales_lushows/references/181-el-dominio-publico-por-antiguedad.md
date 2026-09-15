# 181 · El dominio público por antigüedad

**Qué resuelve:** la frase «es de 1925, ya es libre» es falsa como regla general y ha
metido material dudoso en más de un canal. Aquí está el mecanismo real y —sobre todo—
**qué es lo que hay que comprobar caso por caso**, porque el número exacto de años no
se puede escribir de memoria en un manual.

> ⚠️ **Esto no es asesoría legal.** Los plazos de protección los fija la ley de cada
> país y cambian. Este módulo enseña **dónde mirar**, no qué contestar.

---

## El mecanismo, sin números

En la mayoría de países la protección de una obra dura **la vida del autor más un
periodo posterior a su muerte**, y ese periodo **varía por país**. Cuando expira, la
obra entra en dominio público. Tres consecuencias que casi nadie tiene presentes:

1. **El reloj suele arrancar con la muerte del autor, no con la fecha de la foto.** Una
   fotografía de 1925 cuyo autor murió en 1985 puede seguir protegida hoy.
2. **El plazo es distinto en cada jurisdicción.** La misma foto puede ser libre en un
   país y no en otro, al mismo tiempo.
3. **Las obras anónimas y las corporativas** se rigen por reglas propias, normalmente
   contadas desde la publicación o la creación, no desde una muerte que no existe.

Además, EE.UU. tiene un régimen propio para lo **publicado** antes de cierta fecha, con
condiciones adicionales (formalidades, renovación, aviso de copyright) que no existen
en Europa. Por eso Wikimedia Commons **exige dos comprobaciones a la vez**: que la obra
sea libre en su **país de origen** y además en **EE.UU.**

## 🔴 Pendiente de verificar antes de afirmarlo en pantalla

No escribas en este manual ni en una descripción de YouTube ninguno de estos números de
memoria. Se comprueban **en cada episodio**, en la fuente, y se anota la comprobación:

- El número de años tras la muerte del autor en el país de origen de la pieza.
- La fecha frontera del dominio público por publicación en EE.UU. (**se mueve cada 1 de
  enero**: lo que era «un año más» deja de serlo).
- El plazo aplicable a obras **anónimas** y a obras **de encargo / corporativas**.
- Si a esa pieza le aplica la **restauración de derechos** de obras extranjeras (en
  Commons aparece como `PD-1996` / URAA): hay obras que **volvieron a estar protegidas
  en EE.UU.** aunque ya fueran libres en su país.

**Dónde se comprueba:** la ficha del archivo en Commons (la plantilla de licencia dice
el *motivo*), `Commons:Copyright rules by territory` para el país de la pieza, y la
tabla de dominio público de la Cornell Library («Copyright Term and the Public Domain
in the United States»), que se actualiza cada año.

## Leer la etiqueta, no la fecha

La ficha de Commons no dice «es libre»: dice **por qué** lo es. Esa palabra es el dato
que va a `fuentes.json`.

| Etiqueta | Qué está afirmando | Qué hay que mirar |
|---|---|---|
| `PD-old-70`, `PD-old-auto` | Expiró el plazo desde la muerte del autor | Que el **autor y su fecha de muerte** estén en la ficha |
| `PD-US`, `PD-US-expired` | Publicada en EE.UU. antes de la frontera vigente | Que conste **publicación**, no solo creación |
| `PD-1996` | Libre en origen antes de la fecha de restauración | Que el país de origen sea el que dice |
| `PD-anon-70` | Obra anónima, plazo desde publicación | Que de verdad no haya autor identificado |
| `PD-author` | El autor la liberó él mismo | Es una renuncia, no antigüedad |
| Solo `Public domain`, sin motivo | **Nada.** Es una afirmación sin respaldo | Tratar como dudosa |

En el `fuentes.json` real del piloto casi todo el archivo antiguo entra como
`Public domain` con autor identificado (`Louis-Emile Durandelle`, `Agence Rol`,
`The State Board of Health of Missouri`). Cuando el autor sale como `Unknown author`
la pieza no está mal, pero **se apoya en la regla de las anónimas**, que es más frágil:
si esa pieza va a ser un plano protagonista, conviene sustituirla por otra.

## Las trampas de la antigüedad

- **La foto es antigua; el escaneo es de ayer.** La antigüedad protege a la obra, no al
  archivo digital. Quien escanea a veces reclama derechos sobre el escaneo (§ 185).
- **Una obra antigua dentro de una foto nueva.** Fotografiar en 2019 un cartel de 1925
  crea una foto de 2019. El cartel puede ser libre y la foto no.
- **Restauraciones y coloreados.** Una versión coloreada o «mejorada con IA» de una foto
  libre es obra derivada con autor vivo. No entra sin su propia licencia.
- **El país de origen no es donde está el edificio.** Es donde se publicó por primera
  vez. Una foto de la Torre Eiffel publicada en un libro de Nueva York es
  estadounidense a estos efectos.
- **Derechos que no son de autor.** Aunque la obra sea libre, sobre las **personas
  reconocibles** pueden pesar derechos de imagen, y sobre edificios y esculturas
  modernas hay reglas propias por país. Dominio público del autor ≠ vía libre para todo
  uso.

## Qué hacemos en la práctica

1. **Preferimos la pieza cuya ficha explica el motivo** frente a la que solo afirma.
2. **Preferimos el origen federal de EE.UU.** (§ 182) cuando hay alternativa: ahí el
   motivo es el origen, no un plazo que se mueve cada año.
3. Si una pieza clave depende de un cálculo de años, **se busca sustituto antes de
   escribir el guion alrededor de ella**. Para eso existe el sondeo (§ 170).
4. En `fuentes.json` se anota **el texto literal de la licencia**, con autor y URL de la
   ficha. Nunca una interpretación nuestra.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| «Es de antes de 1930, es libre» | Falso fuera de EE.UU., y también dentro si no se publicó allí |
| Contar el plazo desde la fecha de la foto | El reloj suele contarse desde la muerte del autor |
| Copiar en el manual la frontera de dominio público de EE.UU. | Se mueve cada 1 de enero: el manual envejece y miente |
| Leer `Unknown author` como «sin derechos» | Es otra regla, más frágil, y también tiene plazo |
| Usar la versión coloreada de una foto libre | El coloreado es obra nueva con autor vivo |
| Anotar «dominio público» sin el motivo | En una reclamación no hay nada que enseñar (§ 189) |

## Relacionado

`180` las familias de licencia · `182` obra del gobierno federal ·
`185` lo que parece libre y no lo es · `188` `fuentes.json` como compuerta ·
`189` defender un episodio
