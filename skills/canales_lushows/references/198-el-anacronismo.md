# 198 · El anacronismo

**Qué resuelve:** un uniforme militar actual, un cono de señalización de plástico o una
caravana presidencial de 2021 en un episodio ambientado en 1925. Quien lo ve no piensa
«esa foto está mal elegida»: piensa que el canal rellena con lo que encuentra, y a partir
de ahí duda de todo lo demás, incluidos los datos.

---

## Por qué uno solo rompe el episodio entero

El collage funciona porque el espectador acepta un pacto: **todo lo que aparece viene de
la época**. Ese pacto no se degrada, se rompe: con una pieza moderna colada, las otras 68
dejan de ser archivo y pasan a ser «imágenes de internet», y la historia con ellas. Es más
grave que un fallo de color (`197`) porque el color se arregla y el contenido no.

## El caso real: 17 descartes en el episodio 01

De las 80 piezas descargadas, **11 no llegaron al montaje por anacronismo** (las otras 6
cayeron por no ser legibles). Las razones, tal como quedaron anotadas:

| Pieza descartada | Razón |
|---|---|
| `210120_h_le976_022_50859991941.jpg` | caravana presidencial de **2021** contra 1925-1947 |
| `american_soldiers_watch_as_the_tricolor_flie` | liberación de París **1944**: uniformes y jeep que contradicen los años 20 |
| `class_on_counterfeit_money_dvids2744{48,49,50,52,53}` | clase militar actual, uniforme ACU: imposible de empatar |
| `437th_mxs_airmen_hard_at_work_120510_f_lr006` | uniforme militar actual; ni virado pasa por chatarrería vieja |
| `guantanamo_prayer_sign.jpg` | cono de señalización amarillo y cartel moderno |
| `fbi_honolulu_adopt_a_school_evidence_scene_s` | escritorio y regla de plástico modernos |

El patrón se repite: **el archivo federal de EE. UU. es dominio público y por eso es
irresistible**, pero está lleno de fotografía de los últimos veinte años. La búsqueda
«Counterfeit money» devuelve material perfecto de licencia y perfectamente inservible de
fecha.

## No hay detector automático. Lo comprobé.

La tentación es fechar el fichero y filtrar. Las dos señales baratas —el EXIF y el año en
el título— se pueden calcular en segundos:

```python
def fecha_exif(ruta):
    try:
        ex = Image.open(ruta).getexif() or {}
    except Exception:
        return None
    for k, v in ex.items():
        if ExifTags.TAGS.get(k) in ("DateTimeOriginal", "DateTime"):
            return int(str(v)[:4])

def ano_en_titulo(titulo):
    anos = [int(a) for a in re.findall(r"(1[6-9]\d\d|20[0-2]\d)", titulo)]
    return min(anos) if anos else None
```

Contra el archivo real del episodio 01 fallan las dos:

| Señal | Marca | Anacronismos reales | Precisión |
|---|---|---|---|
| EXIF posterior a 1958 | **39 de 80** | 11 | 28% |
| Año en el título posterior a 1958 | 4 de 80 | 2 | 50% |

**El EXIF fecha el escaneo, no la fotografía.** Del propio archivo:

```
2026:04:06   victor_lustig_mugshot.jpeg        ← la ficha policial de 1935
2013:10:22   us_funded_loan_of_1891_20_000.jpg ← un bono de 1891
2022:07:29   rms_arabia_october_1902.jpg       ← un transatlántico de 1902
```

Un filtro por EXIF habría tirado la foto del protagonista. El año del título tampoco
sirve: dos de sus cuatro marcas son `RP-F-2012-96-168`, un número de inventario del
Rijksmuseum sobre un negativo de 1925.

Las señales valen para **ordenar la revisión** —mirar primero las 39 marcadas— y para nada
más.

## La revisión que sí funciona

Se abre la hoja de contactos sobre gris medio (`161`) y se recorre esta lista, cuadro a
cuadro:

```
vehículos · uniformes · plástico · señalización · tipografía de carteles ·
cables y enchufes · gafas · ropa de calle · asfalto pintado · vallas metálicas
```

La pregunta no es «¿de qué año es la foto?», es **«¿hay algo en el cuadro que no pudiera
existir en la época?»**. Dos piezas con EXIF moderno **sí se usan**: la celda de Alcatraz
de 2009 y los enseres de un preso de 2007 — piedra y metal, sin nada que delate la
década, y con `virar=0.70` pasan por archivo sin mentir: la celda de 2009 es la de 1935.

No hay script para «el cono es de plástico». Son 69 piezas y quince minutos.

## Descartar deja constancia

El descarte no se borra: se anota con su razón, en el mismo fichero donde está la tabla
de piezas.

```python
DESCARTES = {
    "210120_h_le976_022_50859991941_jpg":
        "caravana presidencial de 2021: anacronismo evidente contra 1925-1947",
    "class_on_counterfeit_money_dvids274448_jpg":
        "clase militar actual (uniforme ACU): imposible de empatar con el fondo",
}
```

Sirve para que nadie vuelva a intentarlo en la revisión siguiente, para recalcular el
cupo del escenario con conocimiento (`191`) y para saber qué términos de sondeo devuelven
basura moderna.

## El anacronismo propio

Cuenta también el que fabrica el canal: una tipografía que no existía, un mapa con
fronteras posteriores, un billete de una serie emitida después de los hechos.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Aceptar una pieza porque la licencia es perfecta | El archivo federal es libre **y** moderno |
| Virar a sepia para «salvar» un anacronismo | Sigue siendo de 2021, y ahora parece falsificado |
| Filtrar por EXIF | Marca 39 de 80 con 28% de acierto, y tira la ficha del protagonista |
| Filtrar por el año del título | `RP-F-2012-96-168` es un número de inventario, no una fecha |
| Descartar todo lo que tenga fecha moderna | Se pierden interiores de piedra perfectamente válidos |
| Descartar sin anotar la razón | Se vuelve a bajar y a evaluar en la revisión siguiente |
| No repasar la hoja de contactos a ojo | El cono de plástico no lo detecta ningún script |

## Relacionado

`197` · `191` · `161` · `380` · `384` · `199`
