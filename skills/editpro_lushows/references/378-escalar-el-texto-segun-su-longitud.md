# 378 — Escalar el texto según su longitud: la fórmula que evita el desastre

Este módulo nace de un error real, cometido, publicado y corregido. Vale más que cualquier teoría: es la
razón por la que hoy existe una fórmula en el generador de proyectos.

---

## 1. El error, tal cual pasó

Se hizo a mano un texto que funcionaba perfecto: la palabra **`TÚ`**, dos letras, con escala **3.34**.
Enorme, centrada, contundente. Se veía muy bien.

Como se veía bien, esa configuración se **clonó** para las demás palabras del video. Entre ellas:
**`CERVEZA DORADA`** — catorce caracteres.

Resultado: una palabra que medía **siete veces** el ancho de la anterior, con la misma escala encima.
Salía del cuadro por los dos lados, o si el editor la ajustaba a la fuerza, quedaba ocupando la pantalla
entera como un cartel de carretera.

La lección no es "revisa antes de exportar". La lección es estructural:

> **La escala del texto no es una propiedad del estilo. Es una función de la longitud de la palabra.**
> Clonarla entre palabras distintas es tan incorrecto como clonar la duración de un clip entre clips de
> distinta duración.

---

## 2. Por qué un tamaño fijo tiene que reventar

Aritmética elemental que casi nadie hace:

```
ancho en pantalla ≈ número de caracteres × ancho medio del carácter × escala
```

Con escala fija, el ancho es **directamente proporcional al número de caracteres**. Y el ancho disponible
no crece: son 810 px de zona segura universal (`376`).

| Palabra | Caracteres | Ancho con escala fija 2.6 (relativo) |
|---|---|---|
| `TÚ` | 2 | 5,2 |
| `HOY` | 3 | 7,8 |
| `GRATIS` | 6 | 15,6 |
| `CERVEZA DORADA` | 14 | **36,4** ← siete veces la primera |

No hay ninguna escala fija que sirva para las dos puntas. Si eliges una que le quede bien a `TÚ`,
`CERVEZA DORADA` explota. Si eliges una que le quede bien a `CERVEZA DORADA`, `TÚ` queda diminuta y
pierde toda su fuerza.

**La solución no es un punto medio. Es una función.**

---

## 3. La fórmula

```js
function escalaPorLongitud(texto) {
  const largo = texto.length;
  return Math.max(0.85, Math.min(2.6, (2.6 * 5) / Math.max(largo, 5)));
}
```

Tres piezas, cada una con una razón:

| Pieza | Valor | Qué hace |
|---|---|---|
| **Escala de referencia** | `2.6` | La escala que le queda bien a una palabra de longitud de referencia |
| **Longitud de referencia** | `5` | Una palabra de 5 caracteres es la "unidad": recibe la escala 2.6 |
| **Techo** | `2.6` | Ninguna palabra crece más que la de referencia |
| **Piso** | `0.85` | Ninguna palabra se encoge por debajo de aquí |

### Qué hace realmente
Para palabras de **5 caracteres o más**, la fórmula mantiene el **ancho total constante**:

```
ancho ∝ largo × escala = largo × (13 / largo) = 13     ← constante
```

Es decir: todas las palabras largas ocupan el mismo ancho en pantalla, sin importar cuántas letras
tengan. Esa es exactamente la propiedad que quieres: una columna de cascada con bordes parejos.

Para palabras de **menos de 5 caracteres**, la escala se topa en 2.6 y el ancho **sí** baja. También
correcto: si no lo topara, `TÚ` recibiría escala 6.5 y ocuparía toda la pantalla de alto.

---

## 4. La tabla, para tenerla a mano

| Palabra | Largo | Escala | Ancho relativo |
|---|---|---|---|
| `NO` | 2 | 2.60 | 5,2 |
| `TÚ` | 2 | 2.60 | 5,2 |
| `HOY` | 3 | 2.60 | 7,8 |
| `YA` | 2 | 2.60 | 5,2 |
| `NUNCA` | 5 | 2.60 | 13,0 |
| `GRATIS` | 6 | 2.17 | 13,0 |
| `NÓMINA` | 6 | 2.17 | 13,0 |
| `COMPRAS` | 7 | 1.86 | 13,0 |
| `ARRIENDO` | 8 | 1.63 | 13,0 |
| `SERVICIOS` | 9 | 1.44 | 13,0 |
| `$10.000` | 7 | 1.86 | 13,0 |
| `CERVEZA DORADA` | 14 | 0.93 | 13,0 |
| `Y AL FINAL NADA` | 15 | 0.87 | 13,0 |
| `CALCULADORA DE COSTOS` | 21 | **0.85** ← piso | 17,9 ⚠ |

Fíjate en la última fila: a partir de **~15 caracteres** entra el piso de 0.85, y de ahí en adelante el
ancho **vuelve a crecer**. El piso existe porque una escala menor sería ilegible en celular (`376`), pero
tiene una consecuencia:

> **Por encima de 15 caracteres, la fórmula ya no te protege.** Ahí no hay que escalar: hay que **partir
> la frase en dos líneas o en dos palabras de cascada.**

Ese es el límite real de la fórmula, y decirlo es más honesto que fingir que resuelve todo.

---

## 5. Cómo se calibra para tu estilo

Los números `2.6` y `5` no son universales: dependen de tu fuente y de tu tamaño base. Calibrarlos toma
diez minutos y se hace una sola vez:

1. Escribe una palabra de **5 caracteres** con tu estilo base (tamaño 15, tu fuente, tus mayúsculas).
2. Súbele la escala hasta que ocupe **el 80% del ancho seguro** (unos 650 px de los 810 disponibles).
3. Ese número es tu **escala de referencia**. Reemplaza el `2.6`.
4. El piso: baja la escala hasta que la altura de mayúscula quede en 67 px (el mínimo del `376`). Ese
   número es tu piso. Reemplaza el `0.85`.

Con fuentes muy condensadas la referencia sube (caben más letras); con fuentes anchas baja. Si cambias de
fuente, recalibra.

### Versión más fina: contar por ancho, no por caracteres
La `i` y la `M` no miden lo mismo. Si te sobra rigor, pesa los caracteres:

```js
const ANCHO = { default: 1, I:0.4, J:0.6, L:0.75, M:1.35, W:1.4, ' ':0.5, '.':0.4, '$':0.95 };
const anchoVisual = t => [...t.toUpperCase()].reduce((a,c)=> a + (ANCHO[c] ?? 1), 0);

function escala(texto, REF = 2.6, LARGO_REF = 5, PISO = 0.85) {
  const w = Math.max(anchoVisual(texto), LARGO_REF);
  return Math.max(PISO, Math.min(REF, (REF * LARGO_REF) / w));
}
```

Para el 95% de los casos la versión simple basta. La pesada vale la pena si trabajas con muchos números
(`379`) o con palabras llenas de `I` y `M`.

---

## 6. El orden de las operaciones (donde se rompe todo)

Cuando una palabra además lleva énfasis (`373`), **el orden importa**:

```js
const base  = escalaPorLongitud(palabra);        // primero longitud
const final = esPortadora ? base * 1.3 : base;   // después énfasis
```

Al revés —fijar 2.6 y multiplicar por 1.3— revienta el ancho con cualquier palabra larga.
Y una salvaguarda que conviene tener: después del énfasis, **vuelve a topar**.

```js
const TECHO_ABSOLUTO = 3.4;
const final = Math.min(base * factorEnfasis, TECHO_ABSOLUTO);
```

Ese 3.4 no es casualidad: es aproximadamente el 3.34 del error original. La escala que le quedaba bien a
`TÚ` **sí era correcta para `TÚ`**. El error nunca fue el número: fue clonarlo.

---

## 7. Validación automática antes de exportar

Si generas proyectos por código (`112`), esta comprobación cuesta cinco líneas y evita el 100% de los
textos desbordados:

```js
const ANCHO_SEGURO = 810;              // px, zona segura universal (376)
const PX_POR_UNIDAD = 50;              // calibra esto una vez con tu estilo

function validar(texto, escala) {
  const anchoEstimado = anchoVisual(texto) * escala * PX_POR_UNIDAD;
  if (anchoEstimado > ANCHO_SEGURO) {
    throw new Error(
      `"${texto}" se sale: ${Math.round(anchoEstimado)} px de ${ANCHO_SEGURO}. ` +
      `Pártela en dos o baja el énfasis.`
    );
  }
}
```

Que **falle ruidosamente** es la gracia. Un generador que exporta en silencio un texto desbordado te
cuesta una publicación; uno que se detiene te cuesta treinta segundos.

---

## 8. La regla de partir, no encoger

Cuando la validación falla, la respuesta correcta casi nunca es bajar la escala. Es **partir**:

| Frase original | Mal (encoger) | Bien (partir) |
|---|---|---|
| `CALCULADORA DE COSTOS` | escala 0.85, ilegible | `CALCULADORA` / `DE COSTOS` (cascada de 2) |
| `Y AL FINAL NO TE QUEDA NADA` | ilegible | `Y AL FINAL` / `NADA` |
| `PAGO ÚNICO DE $10.000` | ilegible | `$10.000` grande / `PAGO ÚNICO` pequeño debajo |

Fíjate en la tercera: partir no es solo cortar, es **jerarquizar**. Al partir, casi siempre descubres cuál
era la palabra portadora y cuál era andamio (`370`). La fórmula que te obliga a partir te está mejorando
la escritura.

---

## 9. Y en CapCut a mano, sin código

Sin generador, la disciplina es la misma en tres pasos:

1. Escribe todas las palabras del video **primero, sin ajustar tamaños**.
2. Ordénalas mentalmente de más corta a más larga.
3. Ajusta el tamaño **una por una**, de la más larga a la más corta: fija primero el ancho máximo con la
   palabra larga, y luego sube las cortas hasta ese mismo ancho.

Nunca al revés. Si empiezas por la más corta, te enamoras de una escala imposible —exactamente lo que
pasó con `TÚ`— y después todo lo demás pelea contra ella.

**Y nunca uses "copiar formato" entre palabras de longitudes distintas.** Ese botón es el que causó el
error original.

---

## Errores comunes

1. **Clonar la escala entre palabras de distinta longitud.** El error de origen, y el más caro.
2. **Usar "copiar formato" de CapCut** entre una palabra corta y una larga.
3. **Empezar a ajustar tamaños por la palabra más corta.** Fija un techo imposible.
4. **Aplicar el énfasis antes del cálculo por longitud.**
5. **No topar después del énfasis.** Una portadora larga con +30% se sale igual.
6. **Creer que la fórmula resuelve todo.** Por encima de 15 caracteres hay que partir, no escalar.
7. **Bajar la escala por debajo del piso** para que quepa. Cabe e ilegible es peor que no caber.
8. **No recalibrar al cambiar de fuente.** Una condensada y una ancha necesitan referencias distintas.
9. **Contar caracteres cuando el texto es casi todo `I` o `M`.** Ahí pesa los anchos.
10. **Exportar sin validar el ancho** cuando el proyecto se generó por código.
11. **Una validación que avisa pero no detiene.** Si no rompe, nadie lee el aviso.
12. **Partir la frase por donde cabe** en vez de por donde tiene sentido. Al partir, jerarquiza.
13. **Escalar solo en X para que quepa.** Deforma la letra y se nota inmediatamente en celular.

---

## Checklist

- [ ] Ninguna escala está clonada entre palabras de longitud distinta
- [ ] Calibré la escala de referencia y el piso con mi fuente y mi estilo base
- [ ] El cálculo por longitud se aplica antes que cualquier factor de énfasis
- [ ] Hay un techo absoluto después del énfasis
- [ ] Ninguna palabra queda por debajo del piso de legibilidad
- [ ] Toda frase de más de 15 caracteres está partida, no encogida
- [ ] Al partir, quedó claro cuál es la portadora y cuál el andamio
- [ ] Si ajusté a mano, empecé por la palabra más larga
- [ ] No usé "copiar formato" entre palabras de distinta longitud
- [ ] Si generé por código, hay validación de ancho que **detiene** la exportación
- [ ] La escala se aplicó igual en X y en Y
- [ ] Revisé la columna de cascada y los bordes derechos quedan parejos
