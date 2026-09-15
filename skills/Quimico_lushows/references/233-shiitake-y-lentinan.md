# 233 — Shiitake (*Lentinula edodes*) y lentinan: un medicamento inyectable no es un polvo oral

El shiitake es el hongo más cultivado del mundo después del champiñón, es alimento en medio planeta y tiene
la fracción β-glucánica mejor caracterizada estructuralmente de todo el bloque: el **lentinan**. También es
donde más se abusa de la palabra: el lentinan es, en Japón, un medicamento **intravenoso** aprobado para uso
oncológico, y hay etiquetas de suplemento que lo citan como si fuera lo mismo que un polvo de sombrero seco.
No lo es, ni por molécula, ni por pureza, ni por vía de administración.

Términos: **lentinan** = β-(1→3)-glucano de alto peso molecular purificado de *L. edodes*, con estructura de
triple hélice. **triple hélice (triple helix)** = conformación en la que tres cadenas de glucano se enrollan
entre sí; se asocia al reconocimiento por receptores del sistema inmune. **modificador de la respuesta
biológica (biological response modifier, BRM)** = categoría regulatoria japonesa para agentes que actúan
sobre la respuesta del huésped. **estípite (stipe)** = el tallo del hongo.

## Identidad y material

| Dato | Valor |
|---|---|
| Nombre científico aceptado | *Lentinula edodes* (Berk.) Pegler |
| Sinónimo frecuente en literatura | *Lentinus edodes* |
| Parte usada | Cuerpo fructífero (fruiting body): sombrero + estípite |
| Sustrato de cultivo | Troncos de roble o bloques de aserrín suplementado (`239`) |
| Dato práctico | El **estípite** contiene más β-glucanos que el sombrero — y es lo que la cocina bota |

Ese último renglón vale plata: el tallo del shiitake es residuo gastronómico y materia prima rica. Si te
ofrecen "stem powder" barato, no es necesariamente peor materia prima para β-glucanos.

## Química del lentinan

| Característica | Valor reportado |
|---|---|
| Tipo | β-(1→3)-D-glucano con ramificaciones β-(1→6) |
| Patrón de ramificación | 2 ramificaciones β-(1→6) por cada 5 unidades β-(1→3) de la cadena lineal |
| Peso molecular | Del orden de **500 kDa** |
| Conformación | Triple hélice en solución acuosa; se considera clave para el reconocimiento celular |
| Composición | Solo glucosa (a diferencia de PSK, que trae proteína, manosa, galactosa y fucosa, `231`) |
| Solubilidad | Hidrosoluble; sale con **agua caliente**, no con alcohol (`241`) |

La triple hélice es termolábil y sensible al pH y a agentes caotrópicos: si la desnaturalizas (calor extremo,
álcali, urea), la molécula sigue ahí pero deja de tener la conformación asociada al reconocimiento. Por eso
en un extracto no basta con medir cuánto β-glucano hay; para caracterizar bien hace falta ver **conformación**
(ver "Cómo se mide").

Otros compuestos del shiitake que importan:

| Familia | Ejemplo | Relevancia |
|---|---|---|
| Aminoácidos azufrados | **Ergotioneína** | 0,2–0,8 mg/g base seca reportado en *L. edodes* (200–800 mg/kg); ver `235` |
| Derivados de purina | **Eritadenina** | Marcador característico del shiitake; efectos sobre lípidos en modelos `[animal]` |
| Esteroles | **Ergosterol** | Precursor de vitamina D2 bajo UV (`236`) y marcador de biomasa fúngica (`238`) |
| Azufrados volátiles | Lentionina | El olor característico; se forma al cortar y secar |

Sobre ergotioneína hay un dato interesante: en un estudio de manipulación de la luz de cultivo, el contenido
en *L. edodes* subió de 1,2 mg/g (control) a alrededor de 2,8 mg/g bajo exposición a luz azul. Es un ejemplo
de que la **química se puede modular desde el cultivo** (`239`), pero verifica la fuente primaria antes de
usar ese número como especificación.

## El hecho regulatorio, con su país y su fecha

A agosto de 2026:

- **El lentinan está aprobado en Japón desde 1985** como modificador de la respuesta biológica, para uso en
  cáncer gástrico, en combinación con quimioterapia (se ha usado junto a tegafur en enfermedad inoperable o
  recurrente).
- La vía de administración en ese uso es **intravenosa**, con dosis del orden de **2 a 10 mg por semana**.
- **No está aprobado en Estados Unidos ni en la Unión Europea** como medicamento con esa indicación.

Verifica el estatus vigente en la autoridad japonesa (PMDA) antes de escribirlo en un documento técnico.

### La línea que no se cruza

Ese hecho **se describe; no se traslada**. Un suplemento colombiano de shiitake:

- **no contiene lentinan purificado** (contiene β-glucanos de shiitake, mezcla, otro peso molecular),
- **no se administra por vía intravenosa**,
- y por tanto **no hereda ni un gramo de la evidencia del medicamento japonés**.

Escribir "shiitake, la fuente del lentinan aprobado contra el cáncer en Japón" en una etiqueta, una landing o
un mensaje de venta en Colombia es un claim de enfermedad (Decreto 3249 de 2006, ver `267`, `268`). Además,
en términos farmacocinéticos, comparar 2–10 mg intravenosos con un β-glucano oral de biodisponibilidad muy
baja no es exagerar: es cambiar de tema (`122`).

## Cómo se mide / cómo se comprueba

| Marcador | Método | Unidad y base |
|---|---|---|
| β-glucano y α-glucano | Megazyme K-YBGL, enzimático por diferencia | `% p/p base seca` (`221`) |
| Peso molecular y distribución | HPSEC-MALS | `kDa` + polidispersidad |
| Conformación de triple hélice | Ensayo de rojo Congo (desplazamiento del máximo de absorción) o dicroísmo circular | Cualitativo/semicuantitativo |
| Patrón de enlaces | Metilación y GC-MS, o RMN de ¹³C | Proporción molar (`94`) |
| Ergotioneína | LC-MS/MS o HPLC-UV con par iónico | `mg/g base seca` (`235`) |
| Ergosterol | HPLC-UV 282 nm | `mg/g base seca` (`238`) |
| Vitamina D2 (si hubo UV) | HPLC-UV 265 nm o LC-MS/MS | `µg/100 g` (`236`) |
| Identidad de especie | Secuenciación ITS | % identidad (`245`) |
| Metales pesados | ICP-MS | `mg/kg base seca` (`243`) |

Un COA que diga "lentinan: 20 %" sin decir cómo lo midió es humo: no hay un ensayo de rutina barato que
cuantifique lentinan como entidad química separada del resto del β-glucano. Lo honesto es declarar
β-glucano total con Megazyme, y si quieres hablar de lentinan, caracterizar peso molecular y conformación.

## Seguridad — el dato que casi nadie menciona

Existe la **dermatitis flagelada por shiitake** (shiitake dermatitis / flagellate dermatitis): una erupción
lineal característica asociada al consumo de shiitake crudo o poco cocido, atribuida en la literatura al
lentinan termolábil. Nivel de evidencia: `[reportes de caso clínicos]`, con series publicadas en varios
países. Consecuencias prácticas:

- El shiitake **se cocina**. Cocinar bien reduce el problema descrito.
- Si vendes shiitake deshidratado para consumo directo sin cocción, la advertencia corresponde.
- No es un efecto grave ni frecuente, pero es real y evitable; omitirlo por comodidad comercial es la misma
  actitud que produce los problemas del chaga (`230`).

## Ejemplo aplicado — porción de un producto de shiitake (ILUSTRATIVO)

```
Producto: capsulas de extracto acuoso de shiitake, cuerpo fructifero
COA del lote SH-2026-007:
  beta-glucano 28,4 % p/p base seca   (Megazyme K-YBGL)
  alfa-glucano  3,1 % p/p base seca
  humedad       4,2 % p/p             (Karl Fischer)

Capsula: 500 mg de extracto. Porcion: 2 capsulas/dia = 1.000 mg/dia

beta-glucano por capsula = 500 mg x 0,284 = 142 mg
beta-glucano por porcion = 284 mg/dia

Lo que SE PUEDE declarar: "aporta 284 mg de beta-glucanos por porcion diaria,
determinados por metodo enzimatico Megazyme, expresados en base seca".
Lo que NO: cualquier frase que mencione lentinan farmaceutico o enfermedades.
```

## Errores comunes

- **Citar el lentinan japonés en material de venta.** Es el error más caro del módulo.
- **Declarar "lentinan X %"** sin método que lo sostenga.
- **Extraer con alcohol y esperar β-glucanos.** El lentinan es hidrosoluble (`241`, `146`).
- **Sobrecalentar el extracto** y destruir la conformación que se supone que se está vendiendo.
- **Botar el estípite** creyendo que es descarte, cuando aporta más β-glucanos que el sombrero.
- **No advertir sobre el consumo crudo** en un producto de shiitake deshidratado.
- **Comparar un COA de sombrero con uno de tallo** como si fueran el mismo material (`07`, `66`).

## Conexión con otros módulos

→ `219-beta-glucanos-quimica-y-estructura.md` — la química de fondo, incluida la triple hélice.
→ `231-cola-de-pavo-trametes-psk-y-psp.md` — el otro caso de medicamento japonés que no se traslada.
→ `235-ergotioneina.md` — el otro marcador fuerte del shiitake.
→ `236-vitamina-d2-y-tratamiento-uv.md` — qué pasa si le pones UV a este hongo.
→ `250-seguridad-e-interacciones-de-hongos.md` — dermatitis, alergias y demás.
→ `267-decreto-3249-y-que-puedo-decir.md` — qué frase sí cabe en una etiqueta colombiana.
