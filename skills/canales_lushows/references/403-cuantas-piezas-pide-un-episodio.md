# 403 · Cuántas piezas pide un episodio

**Qué resuelve:** el umbral de archivo del sondeo estaba mal por un factor de tres, y no
se supo hasta tener el episodio 1 montado entero. Este módulo lo corrige con la medida.

---

## El umbral viejo y por qué engañaba

`sondeo.py` decía: *«umbral para 10 min: 40 piezas mínimo»*. Con ese listón, Lustig pasó
holgado (988 piezas libres encontradas) y el episodio se hizo. **Y aun así se quedó corto
de material**, porque el umbral medía la cosa equivocada: contaba lo que hay en el
archivo, no lo que entra en pantalla.

## Lo que un episodio consume de verdad

Medido sobre los diez minutos del episodio 1:

```
cada minuto pone en pantalla entre 30 y 58 piezas DISTINTAS
el episodio tiene 119 piezas propias (71 recortes + 31 gráficos + 17 textos)
y aun así 8 de los 10 minutos pasan el tope de repetición (1,25 usos/recurso)
```

Lo que falta, minuto a minuto, para bajar de 1,25:

| Minuto | gestos | distintos | hacen falta | faltan |
|---|---|---|---|---|
| 2 | 51 | 37 | 41 | +4 |
| 3 | 45 | 26 | 36 | **+10** |
| 4 | 50 | 32 | 40 | **+8** |
| 5 | 37 | 26 | 30 | +4 |
| 7 | 45 | 31 | 36 | +5 |
| 8 | 39 | 28 | 31 | +3 |
| 9 | 41 | 27 | 33 | **+6** |

**Faltan unas 40 piezas.** Los minutos 1, 6 y 10 cumplen; los peores son los del acto II,
que es donde el relato se sostiene.

## La conversión: una de cada catorce

De las **988 piezas libres** que el sondeo encontró para Lustig, **71 acabaron siendo
recortes usables**. El resto se cae por resolución, por encuadre, por ser la misma foto
repetida en tres catálogos, o por no significar nada en la historia (§ `299`).

```
160 piezas usables / 0,07 de conversión  ≈  2.300 piezas libres en el sondeo
```

Ese 7% es **una medida, no una ley** — depende de cuánto se recorte y de qué archivo se
trate. Pero es la única que hay, y de ella sale el listón nuevo del sondeo.

## La regla

> Un episodio de diez minutos pide del orden de **160 piezas distintas** en pantalla. Si
> el sondeo no devuelve al menos **un par de miles de piezas libres**, el caso se puede
> escribir pero no se puede ilustrar sin repetirse, y la repetición se ve.

## Por qué los minutos CONSTA son los pobres

No es casualidad que falten piezas justo en el acto II. Los minutos que se apoyan en la
columna CONSTA (§ `92`) enseñan documentos, y de un documento hay **un** archivo: el
certificado es uno, la ficha es una. Los minutos de leyenda tienen la ciudad, la torre, el
barco, la época — material de sobra. **El rigor cuesta imágenes**, y hay que presupuestarlo
al elegir el caso, no descubrirlo montando.

## Relacionado

§ `97` (banco de historias) · § `404` (medir si la historia le importa a alguien) · §
`231` (el banco acumulativo) · § `296` (el recorte que no se usa) · § `299` (cuándo una
foto no aporta) · § `402` (el compás)
