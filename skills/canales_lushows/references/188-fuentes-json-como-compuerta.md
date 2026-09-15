# 188 · `fuentes.json` como compuerta

**Qué resuelve:** el registro no es papeleo: es **lo que hace defendible un episodio**
(§ 189) y lo que permite escribir los créditos sin volver a buscar nada (§ 184). Aquí se
convierte en algo que el pipeline **obliga** a cumplir: si una pieza de archivo no tiene
licencia anotada, **el render no corre**.

> ⚠️ **Esto no es asesoría legal.** Es higiene mecánica de producción. Pasar la
> compuerta no significa que una pieza sea legal: significa que está anotada y que
> nadie se saltó el filtro.

---

## Por qué una compuerta y no buenas intenciones

Un episodio son 60–80 piezas y cuatro días. La que se cuela nunca es la primera: es la
número 63, buscada a mano el último día porque faltaba un plano. En ese momento nadie
abre `fuentes.json`; se arrastra el archivo a `archivo/` y se sigue. Una comprobación
que solo avisa se ignora a las tres semanas (§ 143); una que **detiene el render** se
arregla en el minuto. `recortar_lustig.py` ya aborta si un alias no está registrado — lo
que falta es que además mire **la licencia**, y que sea la última puerta.

## Lo que el registro contiene, por pieza

`alias` (clave estable del montaje, § 192) · `archivo` (nombre en `archivo/`, que tiene
que **existir en disco**) · `titulo`, `autor`, `fuente`, `url` (los cuatro campos de la
atribución, TASL, § 184) · `licencia` (texto **literal**, nunca resumido) · `escenario`
(curación y orden de los créditos) · `px` (detecta lo que no aguanta 1920, § 194).

Si no hay autor se escribe `autor no identificado`: un hueco parece un descuido, y en
una reclamación parece otra cosa. Las piezas propias también se registran, con
`fuente: "Paper Empires"` y `licencia: "obra propia"`.

## La compuerta

```python
# -*- coding: utf-8 -*-
# COMPUERTA DE LICENCIAS · ultima puerta antes de renderizar. No avisa: DETIENE.
import io, json, os, re

# Mismas familias que sondeo.py (§ 180). Si cambian alli, cambian aqui.
LIBRES = re.compile(
    r"public\s*domain|^cc0|cc[\s-]*by(?![\w-]*nc)|attribution[\s-]*share|"
    r"gfdl|no\s*restrictions|pd-us|pd-1996|obra\s*propia", re.I)
VETADAS = re.compile(
    r"fair\s*use|uso\s*legitimo|non[\s-]*free|\bnc\b|noncommercial|no\s*comercial|"
    r"no\s*deriv|\bnd\b|editorial\s*use|all\s*rights|todos\s*los\s*derechos", re.I)
OBLIGATORIOS = ("alias", "archivo", "titulo", "autor", "fuente", "url", "licencia")


def exigir_licencias(ruta_fuentes, dir_archivo, usados=None, propias=("Paper Empires",)):
    """Devuelve el indice alias->pieza. Lanza SystemExit si algo no cuadra."""
    if not os.path.exists(ruta_fuentes):
        raise SystemExit("COMPUERTA: no existe fuentes.json. El episodio no se rinde.")
    piezas = json.load(io.open(ruta_fuentes, encoding="utf-8"))
    fallos, idx, ficheros = [], {}, {}

    for n, p in enumerate(piezas, 1):
        alias = p.get("alias") or f"<sin alias #{n}>"

        # 1 · campos completos. Un hueco no es un descuido: es una pieza indefendible.
        vacios = [c for c in OBLIGATORIOS if not str(p.get(c, "")).strip()]
        if vacios:
            fallos.append(f"{alias}: faltan campos {vacios}")
            continue

        # 2 · familia usable EN VIDEO MONETIZADO
        lic = p["licencia"].strip()
        if VETADAS.search(lic):
            fallos.append(f"{alias}: licencia vetada -> '{lic}'")
        elif not LIBRES.search(lic):
            fallos.append(f"{alias}: licencia no reconocida -> '{lic}' (si hay que "
                          f"interpretarla, no tenemos licencia)")

        # 3 · la url tiene que llevar a la FICHA. OJO: la ficha de Commons TERMINA en
        #     .jpg (el titulo de la pagina es "File:....jpg"): filtrar por extension
        #     marcaba como malas las 80 piezas buenas. Al binario lo delata el host.
        url = p["url"]
        if not url.startswith("http"):
            fallos.append(f"{alias}: url invalida -> '{url}'")
        elif re.search(r"^https?://upload\.|/images/[0-9a-f]/|[?&]download", url, re.I):
            fallos.append(f"{alias}: la url apunta al binario, no a la ficha del item")
        elif re.search(r"google\.[a-z.]+/search|/search\?|pinterest\.", url, re.I):
            fallos.append(f"{alias}: la url es un buscador, no una ficha (§ 185)")

        # 4 · el fichero en disco: un registro sin imagen no prueba nada
        if p["fuente"] not in propias:
            if not os.path.exists(os.path.join(dir_archivo, p["archivo"])):
                fallos.append(f"{alias}: '{p['archivo']}' no esta en {dir_archivo}")

        # 5 · colisiones
        if alias in idx:
            fallos.append(f"{alias}: alias duplicado")
        idx[alias] = p
        ficheros.setdefault(p["archivo"], []).append(alias)

    for fichero, quienes in ficheros.items():
        if len(quienes) > 1:
            fallos.append(f"fichero '{fichero}' reclamado por {quienes}")

    # 6 · nada en el montaje que no este registrado
    for origen in sorted(usados or ()):
        if origen not in idx:
            fallos.append(f"el montaje usa '{origen}' y no esta en fuentes.json")

    if fallos:
        # sin simbolos raros: la consola de Windows es cp1252 y una "x" bonita
        # revienta el propio informe de errores con UnicodeEncodeError.
        print("\n" + "=" * 68)
        print(f"  COMPUERTA DE LICENCIAS - {len(fallos)} problema(s). NO SE RINDE.")
        print("=" * 68)
        for f in fallos:
            print(f"   x {f}")
        print("\n  Se arregla anotando la licencia real o quitando la pieza.\n")
        raise SystemExit(1)

    print(f"  compuerta: {len(idx)} piezas con licencia anotada - "
          f"{len(usados or ())} usadas en el montaje - OK")
    return idx
```

## Dónde se engancha y qué encontró

Al principio del render, **antes** de abrir el primer PNG. Devuelve el mismo índice
`alias → pieza` que `indice_fuentes()`, así que el resto del script no cambia:

```python
fuentes = exigir_licencias(FUENTES, ARCHIVO,
                           usados={origen for _, origen, _, _ in PIEZAS})
```

También se ejecuta en el generador de créditos (§ 184): **las dos salidas del episodio
—el vídeo y los créditos— pasan por la misma puerta.**

Ejecutada sobre las 80 piezas de `ep01-lustig/fuentes.json`, pasa 78 y levanta
exactamente **el defecto que ya existía**: dos entradas distintas de Commons con el mismo
nombre de fichero, de modo que en disco solo hay una imagen y la segunda entrada se queda
sin ella. Ese fallo estaba documentado en prosa dentro de `recortar_lustig.py` y nadie lo
había convertido en comprobación. Ahora detiene el render.

## Lo que la compuerta NO hace

No comprueba que la licencia sea **cierta**: si alguien escribe «Public domain» sobre una
foto de agencia, pasa — eso lo cazan el § 185 y el § 186, a mano. No comprueba el
**contenido**: que la imagen sea lo que dice la voz es otra verificación, igual de
obligatoria (§ 96). Y no sustituye a leer la ficha: es la red, no el trapecio.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Que la comprobación solo imprima un aviso | A las tres semanas nadie la lee (§ 143) |
| Validar la URL por su extensión | La ficha de Commons acaba en `.jpg`: se descarta el archivo bueno |
| Usar símbolos Unicode en el informe de fallos | `UnicodeEncodeError` en Windows: revienta justo el aviso que importaba |
| Anotar la licencia «al terminar» | Se pierde el origen de media docena de piezas |
| Resumir la licencia («CC» a secas) | El crédito queda incompleto y la prueba, débil |
| Relajar `VETADAS` para que pase «solo una» | En dos episodios la excepción es la norma |

## Relacionado

`180` las familias de licencia · `184` la atribución en la descripción ·
`189` defender un episodio · `192` alias estables y colisiones ·
`199` el manifiesto del material · `143` una comprobación que grita en falso se ignora
