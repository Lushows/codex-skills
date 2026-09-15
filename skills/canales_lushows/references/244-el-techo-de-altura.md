# 244 · El techo de altura

**Qué resuelve:** el ancho por sí solo no describe el tamaño. Una imagen vertical a
900 px de ancho mide casi mil de alto y **no cabe en un lienzo de 1080**. Por eso el
retrato del protagonista se caía del gancho sin avisar y cinco elementos acababan
clavados en el borde inferior.

---

## La clase lleva su techo

```python
CLASES = {
    #            dura   ancho  alto_max  fade_out  banda
    "heroe":   (3.40,  1280,   0.72,     0.45,  "centro"),
    "objeto":  (2.60,   900,   0.56,     0.40,  "lado"),
    "dato":    (3.10,  1380,   0.30,     0.45,  "cifra"),
    "rotulo":  (2.10,   980,   0.20,     0.30,  "pie"),
    "micro":   (1.40,   680,   0.26,     0.25,  "esquina"),
}
```

`alto_max` va en tanto por uno del lienzo: `0.72` son 777 px, `0.30` son 324. Y el ancho
se recorta hasta respetarlo:

```python
pr = proporcion(recurso)
if pr:
    # se recorta el ancho hasta que la altura entre en su presupuesto
    ancho = int(min(ancho, H_LIENZO * alto_max / pr))
```

El techo no es una salvaguarda de emergencia: es **la definición real del tamaño de la
clase**. El ancho es el tope cuando la imagen es apaisada; el alto manda cuando es
vertical.

## Cuánto interviene

En `ep01-lustig`, de los 27 elementos que coloca la capa automática, **18 salen
recortados por el techo** — dos de cada tres. No es un caso raro: es el caso normal en
un canal que trabaja con documentos, retratos de ficha y postales verticales.

| Recurso | Clase | alto/ancho | Ancho pedido → real | Alto sin techo → con techo |
|---|---|---|---|---|
| `torre_postal` | heroe | 2,28 | 1280 → **341** | 2915 → 777 |
| `retrato_lustig` | heroe | 1,35 | 1280 → **576** | 1726 → 777 |
| `aviso_falsos` | objeto | 1,37 | 900 → **440** | 1236 → 604 |
| `reglamento_celda` | objeto | 1,35 | 900 → **446** | 1219 → 604 |
| `boveda_servicio` | objeto | 1,24 | 900 → **486** | 1118 → 604 |
| `telegrama_union` | objeto | 0,68 | 900 → **889** | 612 → 605 |
| `r_casilla` | rotulo | 0,22 | 980 → **968** | 219 → 216 |

`torre_postal` es el caso extremo: sin techo mediría **2915 px de alto sobre un lienzo
de 1080**, casi tres pantallas. Con techo mide 341 de ancho y cabe. Y fíjese en la
última fila: un rótulo con proporción 0,22 apenas se toca, porque para eso tiene la
clase `rotulo` un techo de 0,20 — el recorte es de 12 px.

## Un héroe con techo sigue siendo un héroe

La objeción obvia: recortar un héroe de 1280 a 341 px lo deja del tamaño de un rótulo.
Es verdad, y es correcto. Una torre vertical **no puede** ocupar el ancho de un héroe;
lo que la hace héroe es que dura 3,40 s y vive en la banda `centro`, no su ancho.
La jerarquía de tiempo es la jerarquía de información; el ancho es una consecuencia de
la geometría del PNG.

Cuando un héroe vertical se queda visualmente pequeño, la respuesta no es subirle el
techo: es **recortar el PNG** para acercarlo a 4:3 (`195`) o poner una lámina de fondo
debajo que sostenga la cobertura (`144`).

Dicho de otro modo: para un canal de documentos, **`alto_max` es el parámetro que de
verdad fija el tamaño y `ancho` es el que casi nunca se aplica**. Quien afine las clases
mirando solo la columna del ancho estará girando un mando desconectado en dos de cada
tres elementos.

## También para la capa escrita a mano

Los héroes escritos a mano no pasan por `CLASES`, así que el episodio les aplica su
propio techo antes de montar:

```python
for e in clave:
    pr = proporcion(e["r"])
    if pr and e.get("w", 400) * pr > 0.78 * 1080:
        e["w"] = int(0.78 * 1080 / pr)
```

0,78 y no 0,72: a mano se permite más porque quien escribe ha mirado el PNG. Pero el
techo existe igual, porque el fallo que se está evitando —un elemento clavado contra el
borde inferior— no distingue entre capas.

## El techo y la cobertura tiran en sentidos opuestos

Recortar por altura **baja la cobertura** (`144`): `torre_postal` a 341 px ocupa el
12,8 % del lienzo; a 1280 ocuparía el 180 %, que es otra forma de decir que no cabe.
Cuando el episodio va flojo de cobertura y tiene muchos verticales, el ascensor no es el ancho:
son las láminas de fondo y encadenar en vez de sustituir. Subir el techo solo empuja
elementos fuera del cuadro y el auditor lo cazará por otro lado (`245`).

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Declarar solo el ancho | Un vertical mide 2915 px de alto y se sale del lienzo |
| Aplicar el techo solo a la capa automática | Los héroes escritos a mano se clavan en el borde inferior |
| Subir `alto_max` para «que se vea más» | El elemento sale del cuadro y salta la alarma del 12 % |
| Recortar el alto en vez del ancho | Se deforma la imagen; hay que reescalar, no recortar |
| Confundir clase con tamaño | Un héroe vertical pequeño sigue siendo el héroe del plano |
| Medir la proporción sin caché | Se abre el PNG una vez por candidata: 672 aperturas por minuto |

## Relacionado

`21` peso visual y jerarquía · `49` zona segura y tamaños · `144` presencia no es
superficie · `195` silueta contra tijera · `242` colocación por rectángulo ·
`245` la sangría
