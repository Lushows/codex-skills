# 184 · La atribución en la descripción

**Qué resuelve:** el bloque de créditos del episodio: qué campos lleva, en qué formato, y
por qué **se genera solo desde `fuentes.json`**. Escrito a mano, con 80 piezas, siempre
falta alguna — y la que falta es justo la que reclaman.

> ⚠️ **Esto no es asesoría legal.** Es el formato de crédito del canal, alineado con la
> práctica recomendada por Creative Commons.

---

## Los cuatro campos: TASL

Creative Commons recomienda que la atribución incluya **título, autor, fuente y
licencia**, con enlace siempre que se pueda, tanto si la obra se usa tal cual como si se
adapta ([Recommended practices for attribution](https://wiki.creativecommons.org/wiki/Recommended_practices_for_attribution)).
El orden es flexible; los cuatro elementos, no.

Y esos cuatro campos **ya están** en cada entrada de `fuentes.json`: `titulo` → T ·
`autor` → A · `url` + `fuente` → S · `licencia` → L. El registro se diseñó para esto:
**anotar una vez, acreditar sin volver a buscar.**

## El formato del bloque

Una línea por pieza, en la descripción del vídeo:

```
«Título» — Autor — Fuente — Licencia — URL
```

Reglas de escritura, todas nacidas de un fallo concreto:

- **Se quita el prefijo `File:` y la extensión.** El título de Commons es un nombre de
  archivo: `File:Victor Lustig Mugshot.jpeg` se acredita *«Victor Lustig Mugshot»*.
- **El autor va tal cual viene, aunque sea feo** (`inconnu`, `Agence Rol. Agence
  photographique (commanditaire)`). Reescribirlo corrompe el registro. Lo único que se
  limpia es la duplicación de la API (`Unknown authorUnknown author`). Si no hay autor:
  «autor no identificado», nunca un hueco.
- **`fuente` es el repositorio, nunca el autor.** Acreditar «Wikimedia Commons» como
  autor incumple BY (§ 183).
- **La licencia, con su versión exacta** (`CC BY 4.0`, no «Creative Commons»), y la
  **URL de la ficha**, no la de la imagen ni la del buscador.
- **Orden por escenario y luego alfabético**, para que el bloque sea estable entre
  versiones y comparable con su corrección.

## El generador

```python
# -*- coding: utf-8 -*-
# CREDITOS · genera el bloque de atribucion desde fuentes.json.
# Se ejecuta DESPUES del render y ANTES de subir. Si falla, no se sube.
import io, json, os, re, sys

def limpiar_titulo(t):
    t = re.sub(r"^File:", "", t or "").strip()
    return re.sub(r"\.(jpe?g|png|webp|tiff?|gif)$", "", t, flags=re.I)

def limpiar_autor(a):
    a = (a or "").strip()
    mitad = len(a) // 2                  # la API duplica: "Unknown authorUnknown author"
    if len(a) % 2 == 0 and a[:mitad] == a[mitad:]:
        a = a[:mitad]
    return a or "autor no identificado"

def creditos(ruta):
    piezas = json.load(io.open(ruta, encoding="utf-8"))
    vistos, lineas = set(), []
    for p in sorted(piezas, key=lambda x: (x.get("escenario", ""), x.get("titulo", ""))):
        clave = p.get("url") or p.get("titulo")
        if clave in vistos:              # la misma foto en dos escenarios: un credito
            continue
        vistos.add(clave)
        faltan = [c for c in ("titulo", "licencia", "url") if not p.get(c)]
        if faltan:                       # sin esto no hay credito posible
            raise SystemExit(f"CREDITOS: a '{p.get('alias')}' le falta {faltan}")
        lineas.append("«{t}» — {a} — {f} — {l} — {u}".format(
            t=limpiar_titulo(p["titulo"]), a=limpiar_autor(p.get("autor")),
            f=p.get("fuente", "origen no anotado"), l=p["licencia"], u=p["url"]))
    return lineas

if __name__ == "__main__":
    ruta = sys.argv[1] if len(sys.argv) > 1 else "fuentes.json"
    ls = creditos(ruta)
    cab = ("ARCHIVO Y LICENCIAS\nTodo el material de archivo de este episodio tiene "
           "licencia libre verificada.\nOrden: titulo - autor - fuente - licencia - "
           "enlace.\n")
    texto = cab + "\n" + "\n".join(ls) + "\n"
    io.open("creditos.txt", "w", encoding="utf-8").write(texto)
    print(f"{len(ls)} creditos - {len(texto)} caracteres -> creditos.txt")
```

## El problema que este generador destapó

Ejecutado sobre el `fuentes.json` real del piloto: **80 créditos, 18.493 caracteres.**
Eso no cabe en la descripción de un vídeo de YouTube ni de lejos.

🔴 **Pendiente de verificar:** el límite exacto vigente de la descripción (ronda los
5.000 caracteres; se comprueba en la ayuda de YouTube antes de dar por buena una
descripción larga). Lo que sí está medido es que **los créditos completos no caben**, y
eso obliga a decidir ahora, no el día de subir:

1. **En la descripción, el bloque abreviado**: título, autor y licencia por pieza, sin
   URL. Cabe en una fracción del espacio.
2. **El bloque completo con enlaces, en una página propia**, enlazada desde la
   descripción (un comentario fijado sirve de refuerzo, **nunca de único sitio**).
3. **Lo que se recorta es el texto narrativo, jamás los créditos.**

## Por qué generado y no a mano

A mano se olvidan piezas —las que entraron el último día—, el formato varía entre
episodios, y nadie detecta que a una entrada le falta la URL. Generado sale todo lo que
está en el registro, siempre igual, auditable, y **revienta** si falta un campo. Ese
`raise SystemExit` es la misma filosofía del § 188: un crédito imposible de escribir es
una pieza que no debió entrar.

En pantalla solo se acredita si la licencia lo pide de forma razonable o si el plano es
una obra identificable, con rótulo discreto (§ 43). Y **las piezas propias también se
anotan**, marcadas como «Paper Empires», para que el bloque distinga lo ajeno de lo
nuestro.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Acreditar «Wikimedia Commons» como autor | Incumple BY: Commons es el repositorio |
| Enlazar la imagen en vez de la ficha | El lector no puede comprobar la licencia |
| Escribir los créditos a mano el día de subir | Faltan piezas, y falta justo la que reclaman |
| «Limpiar» el nombre del autor para que quede bonito | Deja de coincidir con la fuente: la prueba se debilita |
| Recortar créditos para que quepa la descripción | Se sacrifica lo único que no es negociable |
| Dejar el bloque solo en un comentario fijado | Desaparece con el comentario |
| No acreditar lo propio | Nadie sabe qué plano es reconstrucción nuestra (§ 96) |

## Relacionado

`183` CC y sus cláusulas · `188` `fuentes.json` como compuerta ·
`189` defender un episodio · `99` título, miniatura y descripción ·
`43` rótulos y etiquetas
