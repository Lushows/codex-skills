# 404 · Medir si la historia le importa a alguien

**Qué resuelve:** el sexto criterio del banco de historias, que faltaba. Los cinco de §
`97` comprueban que el caso **se puede contar**. Ninguno comprueba que alguien lo esté
buscando.

---

## El agujero, con nombre y número

El episodio 1 se eligió por rigor: documentos públicos, arco con caída, archivo libre.
Todo correcto. Lo que nadie midió:

| Historia | Wikipedia EN, visitas/mes | vs Lustig |
|---|---|---|
| Bernie Madoff | 109.694 | 18× |
| Theranos | 59.918 | 10× |
| Enron | 44.143 | 7× |
| Charles Ponzi | 19.759 | 3× |
| FTX | 19.123 | 3× |
| Wirecard | 7.160 | 1,2× |
| **Victor Lustig** | **6.193** | — |
| Victor Lustig (ES) | **788** | — |

Elegimos una historia de nicho sin saberlo, y eso **no se arregla con montaje**: se paga
entero en la distribución. Un canal nuevo no tiene audiencia que arrastrar; depende de que
la gente ya esté buscando el tema.

## La medida, y por qué esta y no otra

```
https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/
  en.wikipedia/all-access/user/<Titulo>/monthly/<desde>/<hasta>
```

API pública: **sin llave, sin navegador y sin VPN** — las tres cosas que este canal no usa
(§ `140`). Devuelve visitas mensuales reales de los últimos doce meses.

No dice cuánta gente verá el vídeo. Dice **cuánta gente ya busca el tema por su cuenta**,
que es lo que separa un título que se descubre solo de uno que hay que empujar.

## Los suelos

```python
SUELO_EN, SUELO_ES = 20000, 2000       # sondeo.py
```

No son opinión: son donde caen las historias de dinero que la gente ya conoce (Ponzi
19.759, FTX 19.123) frente a la que elegimos a ciegas (6.193).

Por debajo del suelo una historia **puede hacerse igual** — pero sabiendo que se está
creando la demanda, no recogiéndola. Esa es una decisión de calendario: una historia de
nicho vale como episodio 7, cuando ya hay canal; no como episodio 1.

## Una trampa: falta de dato no es cero de demanda

Si el artículo no existe **con ese título exacto** en ese idioma, la función devuelve
`None`, no `0`. Confundirlos mataría historias buenas cuyo artículo se llama de otra forma
(«Escándalo de X», «Caso Y»). Por eso el título de Wikipedia se **declara** en `TITULOS`,
no se deduce del nombre de la carpeta.

## El criterio 6

> **6 · Alguien la está buscando.** ≥ 20.000 visitas/mes en la Wikipedia inglesa y ≥ 2.000
> en la española. Se comprueba con `python sondeo.py <caso>`, en la misma media hora en la
> que se comprueba el archivo.

Y una consecuencia que conviene tener escrita: **popularidad y documentación no van del
brazo**. Los casos recientes y famosos (FTX, Theranos, Wirecard) tienen mucha demanda y
mucha información, pero su archivo visual es **moderno y con derechos** — agencias, no
dominio público. Los casos antiguos tienen archivo libre y poca demanda. El punto dulce
son los casos **famosos y viejos**: Ponzi, el crack del 29, las burbujas clásicas, los
grandes fraudes anteriores a 1960, donde hay a la vez nombre reconocible y archivo libre.

## Relacionado

§ `97` (banco de historias) · § `403` (cuántas piezas pide un episodio) · § `90` (fuentes
primarias) · § `99` (título, miniatura, descripción) · § `130`-`133` (derechos)
