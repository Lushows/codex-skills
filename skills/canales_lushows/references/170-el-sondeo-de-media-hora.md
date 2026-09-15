# 170 · El sondeo de media hora

**Qué resuelve:** saber si un caso se puede ilustrar ANTES de escribir una sola frase del guion.

---

## Por qué es la fase 0

El banco de historias (`97`) filtra por cuatro criterios. Tres se comprueban leyendo:
que haya arco, que haya cifra y que haya documento público. El cuarto —**que el archivo
visual sea libre**— es el que más candidatos elimina y el único que no se puede
comprobar leyendo. Hay que preguntarle al archivo.

El coste de invertir el orden es brutal: se escribe el guion, se graba la voz, se
monta, y en el montaje aparece que no existe una sola foto libre del protagonista.
Media hora de sondeo evita tres días de trabajo.

**Regla:** ningún episodio pasa a guion sin `sondeo.json` escrito y por encima del umbral.

## Las tres preguntas del sondeo

| # | Pregunta | Cómo se contesta | Módulo |
|---|---|---|---|
| 1 | ¿Existe categoría en Commons para cada nombre propio? | `prop=categoryinfo`, una llamada | `172`, `173` |
| 2 | ¿Cuántas piezas libres y grandes salen en total? | `sondeo.py` completo | `174` |
| 3 | ¿Cuántas son **del caso** y no de contexto? | recuento por título | `175` |

## El sondeo rápido: existencia de categorías

Antes de lanzar el sondeo completo (que tarda minutos) se hace esta comprobación, que
tarda **un segundo** y ya mata la mitad de los casos. Una sola llamada, hasta 50
categorías.

```python
import json, urllib.request, urllib.parse
API = "https://commons.wikimedia.org/w/api.php"
UA  = "PaperEmpires-archivo/1.0 (documental; contacto: ...)"

def censo(cats):
    p = {"action": "query", "format": "json", "prop": "categoryinfo",
         "titles": "|".join("Category:" + c for c in cats)}
    req = urllib.request.Request(API + "?" + urllib.parse.urlencode(p),
                                 headers={"User-Agent": UA})
    d = json.load(urllib.request.urlopen(req, timeout=45))
    for pg in sorted(d["query"]["pages"].values(), key=lambda x: x.get("title", "")):
        ci = pg.get("categoryinfo")
        if "missing" in pg and not ci:
            print(f"{pg['title'][:58]:<58} NO EXISTE")
        else:
            print(f"{pg['title'][:58]:<58} files={ci.get('files',0):<7} "
                  f"subcats={ci.get('subcats',0)}")

censo(["Kenneth Lay", "Jeffrey Skilling", "Andrew Fastow", "Enron",
       "Wanted posters of the Federal Bureau of Investigation"])
```

**Salida real (ejecutado 11-sep-2026):**

```
Category:Andrew Fastow                                     NO EXISTE
Category:Enron                                             files=14      subcats=5
Category:Jeffrey Skilling                                  NO EXISTE
Category:Kenneth Lay                                       files=2       subcats=0
Category:Wanted posters of the Federal Bureau of Inves...  files=92      subcats=2
```

Eso son treinta segundos y ya se sabe que el episodio de Enron no va a poder mostrar
la cara de sus tres protagonistas. Ver `176`.

## El sondeo completo

```bash
python sondeo.py enron          # escribe ep01-enron/sondeo.json
python sondeo.py enron --descargar
```

`sondeo.py` recorre dos listas escritas a mano por episodio: `CATEGORIAS` (la vía buena
para nombres propios) y `TERMINOS` (la vía buena para lugares, objetos y documentos).
De cada archivo guarda título, licencia, autor, URL de descripción, URL de descarga y
resolución. **Ese JSON es la prueba del episodio**, no un subproducto: de él sale el
`fuentes.json` (`188`) y de él salen los créditos de la descripción.

## Qué se busca, en este orden

1. **El rostro.** Si el protagonista no tiene foto libre, el episodio cambia de forma
   (o de caso). Es la primera consulta siempre.
2. **El lugar.** Edificio, ciudad, sede, cárcel. Casi siempre hay, porque la gente
   fotografía edificios y los sube con CC.
3. **El objeto.** Billete, imprenta, chatarra, expediente, teletipo.
4. **El documento.** Audiencias del Congreso, acusaciones, informes: dominio público y
   suelen estar en Commons como escaneo.
5. **El contexto de época.** Calle, coche, ropa, oficina del año que toque.

Lo genérico ("dinero", "fraude") devuelve ruido y no se busca nunca.

## Cuándo se abandona un caso

| Señal | Qué significa | Decisión |
|---|---|---|
| Menos de 40 piezas útiles totales | No da para 10 minutos | Abandonar o acortar a corto |
| Sin rostro del protagonista | El episodio no tiene cara | Replantear forma (`176`) |
| Menos de 15 piezas **del caso** | Es un episodio de fotos de archivo genérico | Replantear o abandonar |
| Todo lo bueno pide atribución | Se puede, pero hay que rotularlo | Seguir, con coste de diseño |
| Todo por debajo de 1100 px | No aguanta 1920 en pantalla | Abandonar |

La decisión se toma **con el número delante**, se escribe en el banco de historias junto
al caso y no se vuelve a discutir. Un caso descartado por archivo queda marcado para no
volver a sondearlo dentro de seis meses.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Escribir el guion y sondear después | Tres días de trabajo con un episodio que no se puede ilustrar |
| Fiarse del número total de piezas | 379 piezas y solo 11 del caso: es un episodio de stock (`175`) |
| Sondear solo con búsqueda libre | Para nombres propios devuelve ruido casi puro (`173`) |
| Dar por hecho que "seguro que hay fotos" | Enron es de 2001 y no tiene retrato libre de ninguno de los tres |
| No guardar el JSON del sondeo | El episodio deja de ser defendible ante una reclamación (`189`) |

## Relacionado

`97` · `171` · `172` · `174` · `176` · `188`
