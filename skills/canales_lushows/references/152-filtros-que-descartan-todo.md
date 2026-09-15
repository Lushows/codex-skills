# 152 · Filtros que descartan todo

**Qué resuelve:** un filtro demasiado estricto no da error: devuelve **cero
resultados**, y cero resultados se lee como *«este caso no tiene archivo libre»*.

---

## Cómo se manifiesta

```
  LIB [ 1/24] Victor Lustig mugshot                    0 libres,   0 nuevos
  ...
  piezas con licencia libre verificada: 0
  umbral para 10 min: 40 piezas mínimo · INSUFICIENTE
```

El sondeo terminó con código 0 y el veredicto fue *«el caso no se puede ilustrar»*. El
caso tenía cientos de piezas libres. Dos filtros lo mataron:

**1 · La extensión del archivo.** El sondeo exigía que la URL terminara en `.jpg`, y
Commons las devuelve con la cadena de consulta detrás:

```python
>>> u = "https://upload.wikimedia.org/x/Foo.jpg?utm_source=a"
>>> bool(re.search(r"\.(jpg|jpeg|png|webp)$", u, re.I))
False                       # 24 búsquedas, 0 resultados
>>> bool(re.search(r"\.(jpg|jpeg|png|webp)$", u.split("?")[0], re.I))
True
```

**2 · La palabra dentro de otra palabra.** El filtro de licencias vetaba `copyright`
como subcadena. La licencia **«No known copyright restrictions»** —que es libre— la
contiene. Se tiraba el **25% del material libre** de las hemerotecas.

## Por qué ocurre

Un filtro de descarte es **lógica invertida**: cuanto mejor funciona, menos ves. Un `if`
que acepta de más te lo cuenta la salida; lo que un `if` rechaza de más desaparece antes
de llegar a la lista.

Y las dos formas concretas son siempre las mismas: **anclar al final (`$`) un dato que
lleva cola** —URLs con `?`, rutas con `#`— y **buscar subcadena donde había que buscar
palabra**. La segunda es la misma trampa que en el corrector de tildes de `auditar.py`,
y por eso ahí se escribió con `\b…\b`: buscando subcadena, «segun» salta dentro de
SEGUNDA, «aqui» dentro de CHECOSLOVAQUIA y «anos» dentro de ALGUNOS.

## Cómo se caza

Un filtro no se audita leyéndolo: se audita **pasándole los casos reales**.

```python
import re
LIBRES  = re.compile(r"public\s*domain|^cc0|cc[\s-]*by(?![\w-]*nc)|attribution[\s-]*share|"
                     r"gfdl|no\s*restrictions|pd-us|pd-1996", re.I)
VETADAS = re.compile(r"fair\s*use|non[\s-]*free|\bnc\b|noncommercial|no\s*deriv|nd\b|"
                     r"copyright|all\s*rights", re.I)

for c in ["No known copyright restrictions", "Public domain", "CC BY-SA 4.0",
          "CC BY-NC 2.0", "CC0", "Fair use", "PD-US"]:
    print(f"{c:<34} LIBRES={bool(LIBRES.search(' | ' + c))!s:<6} "
          f"VETADAS={bool(VETADAS.search(c))}")
```

```
No known copyright restrictions    LIBRES=False  VETADAS=True    <-- LIBRE, y se tira
Public domain                      LIBRES=True   VETADAS=False
CC BY-SA 4.0                       LIBRES=True   VETADAS=False
CC BY-NC 2.0                       LIBRES=False  VETADAS=True
CC0                                LIBRES=False  VETADAS=False   <-- ^ ancla al inicio
Fair use                           LIBRES=False  VETADAS=True
PD-US                              LIBRES=True   VETADAS=False
```

Dos hallazgos que siguen vivos en `sondeo.py`: `no\s*restrictions` **no** casa con «No
known **copyright** restrictions» (hay dos palabras en medio), y `^cc0` sólo casa si la
licencia corta viene primera en la cadena concatenada.

## La guardia automática

Recortar la cola antes de comparar, y una tabla de casos que se ejecuta con el módulo:

```python
# OJO: Commons devuelve la URL con parámetros detrás ("...jpg?utm_source=..."). Exigir
# que TERMINE en .jpg descartaba absolutamente todo y hacía parecer que el caso no
# tenía archivo libre. Se corta la cadena de consulta primero.
ruta_limpia = (ii.get("url", "") or "").split("?")[0]
if not re.search(r"\.(jpg|jpeg|png|webp)$", ruta_limpia, re.I):
    continue
```

```python
LIBRES = re.compile(
    r"public\s*domain|\bcc0\b|cc[\s-]*by(?![\w-]*nc)|attribution[\s-]*share|gfdl|"
    r"no\s*(known\s*copyright\s*)?restrictions|pd-us|pd-1996", re.I)

CASOS = {"No known copyright restrictions": True, "CC0": True, "Public domain": True,
         "CC BY-SA 4.0": True, "CC BY-NC 2.0": False, "Fair use": False}
for texto, esperado in CASOS.items():
    libre = bool(LIBRES.search(" | " + texto)) and not VETADAS.search(texto)
    assert libre is esperado, f"filtro de licencias roto en: {texto}"
```

⚠️ `VETADAS` sigue vetando por subcadena (`copyright`), así que la frase completa hay
que aceptarla **antes**: el orden es lista blanca explícita primero, veto después.

Y el contador de rendimiento, que delata al filtro en producción: el sondeo imprime
**cuántas devolvió la API y cuántas sobrevivieron**, término a término.

```
  CAT [ 3/17] Alcatraz Federal Penitentiary        86 crudas,  41 libres,  38 nuevos
```

Si una columna entera va a cero, el sospechoso es el filtro, no el archivo. **Regla:
un filtro que descarta más del 90% de lo que le llega se prueba antes de creérselo.**

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Anclar con `$` una URL con parámetros | 0 resultados en 24 búsquedas y el caso se declara inviable |
| Vetar por subcadena | «No known copyright restrictions» se lee como copyright: −25% |
| Leer «0 resultados» como «no hay material» | Tres días de trabajo perdidos en el caso equivocado |
| Aflojar el filtro para que salgan piezas | Una licencia que hay que interpretar es una licencia que no tenemos |
| Probarlo sólo con los casos buenos | Los falsos negativos no se ven nunca |

## Relacionado

`150` el catálogo del fallo silencioso · `170` el sondeo de media hora · `171` la API de
Commons · `174` el umbral de piezas útiles · `176` cuándo un caso no se puede ilustrar ·
`180` las cinco familias de licencia · `185` lo que parece libre y no lo es
