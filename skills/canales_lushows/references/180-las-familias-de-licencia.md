# 180 · Las familias de licencia

**Qué resuelve:** saber, en diez segundos y sin interpretar nada, si una pieza de
archivo puede entrar en un vídeo que **monetiza**. Ese es nuestro caso y cambia el
resultado: dos de las familias quedan fuera por definición, no por prudencia.

> ⚠️ **Esto no es asesoría legal.** Es el criterio operativo con el que este canal
> acepta o descarta material. Cuando una pieza es importante y la licencia no es
> obvia, la respuesta correcta es descartarla, no razonarla.

---

## La pregunta que hay que hacerse

No es «¿es libre?». Es: **¿puedo usarla, modificarla y ganar dinero con el resultado,
sin arrastrar obligaciones al resto del episodio?** Paper Empires monetiza: eso es
«ventaja comercial» en el sentido del texto de las licencias.

## Las familias

| Familia | ¿Uso comercial? | ¿Modificar/recortar? | ¿Obliga al resto? | Veredicto |
|---|---|---|---|---|
| **Dominio público** (plazo cumplido) | Sí | Sí | No | ✅ preferida |
| **Dominio público por origen** (gobierno federal EE.UU., § 182) | Sí | Sí | No | ✅ preferida |
| **CC0** (renuncia) | Sí | Sí | No | ✅ preferida |
| **CC BY** | Sí | Sí | No, pero exige crédito | ✅ con atribución (§ 184) |
| **CC BY-SA** | Sí | Sí | **Puede** contagiar la licencia | ⚠️ solo con criterio (§ 183) |
| **CC BY-NC** (y NC-SA, NC-ND) | **No** | — | — | ❌ fuera |
| **CC BY-ND** | Sí | **No** | — | ❌ fuera |
| **Todos los derechos reservados** | No | No | — | ❌ fuera |
| **«Uso legítimo» / fair use** | No es una licencia | — | — | ❌ fuera |

Las seis combinaciones CC salen de cuatro elementos —BY, SA, NC, ND— y **todas
incluyen BY**: no existe una licencia CC sin atribución (CC0 no es una licencia, es una
renuncia). Fuente: [About CC Licenses](https://creativecommons.org/share-your-work/cclicenses/).

## Por qué NC y ND quedan fuera por definición

**NC (NonCommercial).** El texto legal define el uso no comercial como el que «no está
principalmente dirigido ni destinado a una ventaja comercial o a una compensación
monetaria». Y —esto es lo que casi todo el mundo entiende al revés— **la condición
depende del uso, no de quién lo hace**: una ONG puede incumplirla y una empresa puede
respetarla. Un episodio con anuncios y con enlaces de afiliación no pasa esa prueba en
ninguna lectura razonable. Fuente: [CC FAQ](https://creativecommons.org/faq/).

**ND (NoDerivatives).** Prohíbe compartir material adaptado. Nuestro montaje **recorta
en silueta, vira el color, añade grano, anima y superpone**. Eso es adaptar. No existe
una forma de usar una pieza ND en este canal que no sea una adaptación.

No es cobardía: es que ambas nos dejan sin la única forma en que trabajamos.

## Cómo se traduce esto al filtro real

`piloto/sondeo.py` implementa exactamente esta tabla con dos expresiones regulares: una
lista de lo aceptado y una de lo vetado, y **si el texto de la licencia dispara la
vetada, la pieza cae aunque también dispare la aceptada**.

```python
LIBRES  = r"public\s*domain|^cc0|cc[\s-]*by(?![\w-]*nc)|attribution[\s-]*share|" \
          r"gfdl|no\s*restrictions|pd-us|pd-1996"
VETADAS = r"fair\s*use|non[\s-]*free|\bnc\b|noncommercial|no\s*deriv|nd\b|" \
          r"copyright|all\s*rights"
```

Dos detalles que costaron material y hay que respetar al tocarlo:

- `cc[\s-]*by(?![\w-]*nc)` acepta `CC BY` y `CC BY-SA` pero **rechaza `CC BY-NC`** con
  una mirada hacia delante. Si se quita el paréntesis, entra todo el NC del mundo.
- `VETADAS` se evalúa **solo sobre `UsageTerms`**, no sobre el texto completo. El
  motivo: la etiqueta legítima *«No known copyright restrictions»* contiene la palabra
  «copyright» y, al comprobarla sobre todo el texto, **se tiraba el 25 % del archivo
  libre**. Un episodio llegó a declararse inviable por eso.

## La regla de oro

> **Una licencia que hay que interpretar es una licencia que no tenemos.**

Si hace falta un párrafo para justificar por qué una pieza se puede usar, la pieza no
entra. Hay 60 más en el sondeo y el coste de buscar otra es de minutos; el coste de
equivocarse es un episodio desmonetizado o retirado.

## Casos que parecen familia y no lo son

| Etiqueta que se ve | Qué es realmente |
|---|---|
| `No known copyright restrictions` | ✅ aceptada (archivos de museo/biblioteca sin restricción conocida) |
| `PD-US`, `PD-1996`, `PD-old-70` | ✅ dominio público, pero **por motivos distintos** (§ 181) |
| `GFDL` | ✅ aceptada; libre y comercial, aunque con obligaciones de licencia |
| `CC BY 2.0 FR`, `CC BY 3.0 ES` | ✅ CC BY; el sufijo es la adaptación nacional, no otra familia |
| `Attribution-ShareAlike` | ⚠️ es BY-SA escrito en largo: mismo aviso del § 183 |
| `Free for personal use` | ❌ no es libre: excluye lo comercial con otras palabras |
| `Royalty free` | ❌ no significa gratis ni libre: significa «sin regalías por uso», bajo contrato |
| `Uso editorial` | ❌ marca de agencia; ver § 186 |
| Sin etiqueta de licencia | ❌ la ausencia nunca es dominio público |

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Dar por buena una pieza porque «está en Commons» | Commons aloja también material no libre bajo excepciones; la licencia es del archivo, no del sitio |
| Leer «CC BY-NC» y quedarse en el «CC BY» | Pieza inutilizable en un canal monetizado |
| Usar ND «sin modificar» | Nuestro montaje siempre modifica: no existe ese caso |
| Tomar «royalty free» por «libre» | Es un contrato comercial, no una licencia abierta |
| Suavizar una duda con «seguro que no pasa nada» | Es exactamente la frase que precede a una reclamación |
| Cambiar el regex de `LIBRES` sin probarlo | Un paréntesis mal puesto abre la puerta al NC o mata el archivo entero |

## Relacionado

`181` dominio público por antigüedad · `182` obra del gobierno federal ·
`183` CC y sus cláusulas · `185` lo que parece libre y no lo es ·
`188` `fuentes.json` como compuerta
