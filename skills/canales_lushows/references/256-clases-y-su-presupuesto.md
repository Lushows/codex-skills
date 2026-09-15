# 256 · Clases y su presupuesto

**Qué resuelve:** cuánto dura, cuánto mide y dónde vive cada elemento que el diccionario
coloca. Una palabra no dice solo **qué** se ve: dice de qué **categoría** es lo que se ve,
y la categoría es la que reparte tiempo, tamaño y sitio. La jerarquía de tiempo es la
jerarquía de información: lo que más importa, más dura.

---

## La tabla

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

| Clase | Qué es | Dura | Ancho | Alto máx. | Banda |
|---|---|---|---|---|---|
| heroe | lo que la historia mira de frente | 3,40 s | 1280 px | 72% | centro |
| objeto | la cosa del mundo que acompaña | 2,60 s | 900 px | 56% | lado |
| dato | la cifra compuesta | 3,10 s | 1380 px | 30% | cifra |
| rotulo | la etiqueta que nombra | 2,10 s | 980 px | 20% | pie |
| micro | sellos y marcas | 1,40 s | 680 px | 26% | esquina |

Las duraciones caen dentro del objetivo del canal (1,6–2,4 s de media por elemento, `13`)
porque la media la bajan los `micro` y la suben los `heroe`: en el minuto 1 la duración
media medida es **2,34 s**.

## El ancho solo no sirve: el techo de altura

Una imagen vertical a 900 px de ancho mide casi mil de alto y no cabe en el lienzo. Por
eso cada clase lleva su techo de altura en tanto por uno, y el ancho se recorta hasta
respetarlo:

```python
dura, ancho, alto_max, fout, banda = CLASES[clase]
pr = proporcion(recurso)                       # alto/ancho real del fichero
if pr:
    ancho = int(min(ancho, H_LIENZO * alto_max / pr))
```

Lo que eso hace de verdad, medido sobre los 27 elementos de la capa AUTO:

| Clase | Veces | Ancho pedido | Aplicado (mín · media · máx) |
|---|---|---|---|
| heroe | 3 | 1280 px | **341** · 732,3 · 1280 |
| objeto | 20 | 900 px | 440 · 758,5 · 900 |
| dato | 2 | 1380 px | 1380 · 1380 · 1380 |
| rotulo | 1 | 980 px | 968 · 968 · 968 |
| micro | 1 | 680 px | 680 · 680 · 680 |

El caso extremo es `torre_postal`: proporción 2,28 (una torre, claro), techo de héroe
0,72 → **341 px de ancho** para 776 de alto. Sin el techo entraría a 1280 × 2918 px, o
sea, casi tres lienzos de alto. Así se caía el retrato del protagonista sin avisar y así
acababan cinco elementos clavados en el borde inferior.

Los `dato` no se recortan nunca porque son piezas apaisadas fabricadas a medida: su
proporción está por debajo del techo de 0,30 por construcción.

## La banda, y que la banda no manda

Cada clase nace en una banda —nueve posiciones canónicas, centros y no esquinas— pero la
banda es solo el primer sitio donde se prueba:

```python
orden = BANDAS[banda] + [q for k, v in BANDAS.items() if k != banda for q in v]
```

Si su banda está ocupada se prueban las demás antes de rendirse: mejor moverlo de sitio
que perder el elemento. Y aun así, en el minuto 1 hay **15 candidatas que se caen porque
no cabe ninguna posición** — la cuarta parte de todo lo que el diccionario intenta. Ese
número es el mejor termómetro de saturación que tiene el sistema: si sube mucho, el
episodio está pidiendo más elementos de los que el cuadro aguanta (`12`).

## La clase también decide contra quién compite

```python
tope = 0.05 if (txt or es_texto(recurso)) else 0.42
```

Un recorte puede quedar tapado al 42% sin que nadie lo note; una cifra o un documento, no:
por encima del 5% deja de leerse. El mismo elemento, con la misma banda, entra o no entra
según con quién coincida. Por eso `es_texto()` mira la carpeta de origen y los prefijos
(`d_`, `r_`, `t_`, `sello_`, `m_consta`…) y no la clase declarada: un `objeto` que vive en
`texto/` es texto.

## La capa escrita a mano tiene su propio techo

```python
for e in clave:
    pr = proporcion(e["r"])
    if pr and e.get("w", 400) * pr > 0.78 * 1080:
        e["w"] = int(0.78 * 1080 / pr)
```

78%, algo más que el 72% del héroe generado, porque un plano escrito a mano es una
decisión: si alguien ha puesto ahí el certificado a 1180 px, se respeta mientras quepa.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Fijar solo el ancho | Las verticales se salen del cuadro por abajo |
| Declarar `heroe` lo que no lo es | 3,4 s de pantalla para algo que no los merece |
| Anclar posiciones por esquina | Un elemento ancho en banda estrecha se sale por la derecha |
| Mismo tope de solape para foto y para cifra | Cifras ilegibles que el sistema da por buenas |
| Ignorar los descartes por sitio | El episodio pide más elementos de los que el cuadro aguanta |
| Cambiar `CLASES` para arreglar un plano | Se toca el episodio entero por un fotograma |

## Relacionado

`250` · `251` · `12` · `13` · `21` · `28` · `49`
