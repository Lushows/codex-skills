# 191 · El cupo por escenario

**Qué resuelve:** de dónde sale el número que se le pone a cada escenario, y qué hacer
cuando un escenario **no lo llena**. Un cupo sin aviso es un cupo inútil: el agujero
aparece a mitad del montaje, cuando ya no hay tiempo de buscar.

---

## El cupo sale del guion, no del gusto

Se lee el guion y se cuenta **cuántos segundos de pantalla** pide cada escenario. Con la
densidad del canal (un elemento nuevo cada 1,6–2,5 s, ver `10`), el cupo es:

```
cupo ≈ segundos_del_escenario / 2,0   ×   1,4   (margen de descarte)
```

El `1,4` no es prudencia: es el descarte real medido. De 80 piezas descargadas en el
episodio 01, **69 llegaron a recorte** (86%); el resto cayó por anacronismo o por no
empatar (`198`). Con margen 1,0 el episodio se queda corto en todos los escenarios.

| Escenario (ep01) | Segundos en guion | Cupo | Descargadas | Piezas finales |
|---|---|---|---|---|
| el_hombre | ~9 | 6 | **2** | 8 |
| torre | ~20 | 14 | 14 | 12 |
| paris | ~17 | 12 | 12 | 12 |
| alcatraz | ~17 | 12 | 12 | 10 |
| falsificacion | ~17 | 12 | 12 | 7 |
| chatarra | ~14 | 10 | 10 | 5 |
| ley | ~14 | 10 | 10 | 7 |
| viaje | ~11 | 8 | 8 | 8 |
| **Total** | | **84** | **80** | **69** |

## El caso real: cupo 6, conseguidas 2

`el_hombre` es el escenario del protagonista. Pedía 6 piezas. El sondeo devolvió **3
candidatas** para los tres términos de ese escenario, y solo **2** pasaban los 1100 px:

```
candidatos el_hombre en sondeo: 3
  que pasan 1100px: 2
    1532x1358  File:Victor Lustig Death Certificate.png
    2746x1798  File:Victor Lustig Mugshot.jpeg
```

El episodio se quedó con **dos fotos del hombre del que trata**. No hay más: Lustig es
anterior a la fotografía de prensa masiva y su rastro visual son un certificado y una
ficha policial.

Y eso no se descubrió al curar, porque `curar.py` imprimía `2 elegidas` en una línea
entre otras siete. Se descubrió al montar.

## El aviso, que es lo que faltaba

```python
def avisar_cupos(plan, elegidas):
    """Un escenario que no llena su cupo es una DECISIÓN pendiente, no un dato."""
    por_esc = collections.Counter(x["escenario"] for x in elegidas)
    huecos = []
    for esc, (cupo, _terminos) in plan.items():
        hay = por_esc[esc]
        if hay < cupo:
            falta = cupo - hay
            nivel = "CRÍTICO" if hay < cupo * 0.5 else "corto"
            huecos.append((nivel, esc, hay, cupo, falta))
    if not huecos:
        print("cupos completos")
        return []
    print("\n" + "!" * 74)
    for nivel, esc, hay, cupo, falta in sorted(huecos):
        print(f"  {nivel:<8} {esc:<16} {hay}/{cupo}  faltan {falta}")
    print("!" * 74)
    print("  decidir AHORA: ampliar términos · bajar el umbral de px · despiezar · reescribir")
    return huecos
```

Umbral: **por debajo del 50% del cupo se para**. `2/6` es 33% → `CRÍTICO`. El resto de
escenarios del episodio 01 llenaron el cupo al 100%, así que el aviso habría salido
solo, una vez, y con el escenario correcto.

## Las cuatro salidas de un escenario corto

1. **Ampliar los términos del sondeo.** Lo primero siempre. Para `el_hombre` no había
   más: se probó «Victor Lustig», «Victor Lustig mugshot» y la categoría «Mugshots».
2. **Bajar el umbral de píxeles** solo para ese escenario. Una foto de 900 px del
   protagonista vale más que una de 3000 px de una calle. Se paga con `194`.
3. **Despiezar lo que hay.** Es lo que se hizo: las 2 fuentes dieron **8 piezas**. El
   certificado de defunción salió entero y además por casillas (hospital, nombre,
   oficio, fecha); la ficha policial dio la ficha completa, el retrato frontal y el
   perfil. Ocho elementos distintos de dos ficheros.

   ```python
   ("casilla_oficio", "victor_lustig_death_certificate_png", "revista",
    D(encuadre=(.038, .600, .535, .655), escala=1.75, virar=0, contraste=1.12,
      nitidez=0.7, grano=False, borde=12, semilla=109)),
   ```

   El `encuadre` es una caja relativa `(x0, y0, x1, y1)` en 0..1, así que sobrevive a
   cualquier cambio de resolución de la fuente.
4. **Reescribir el guion** para que el escenario pida menos pantalla. Es la salida
   honesta cuando las otras tres fallan, y es mejor que rellenar con genérico.

## La regla del despiece

Despiezar no es repetir. Dos recortes de la misma fuente **no pueden verse seguidos** ni
compartir encuadre: el retrato frontal y el perfil son caras distintas de la misma foto
y funcionan; el certificado entero y la casilla del nombre funcionan porque uno es el
objeto y el otro es el dato. Tres casillas contiguas seguidas, no.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Imprimir `2/6` sin destacarlo | El agujero se descubre montando, sin tiempo de reaccionar |
| Rellenar el cupo con piezas de otro escenario | El episodio pierde el sitio que importa dos veces |
| Despiezar una fuente en 8 y usarlas seguidas | Se lee como una sola foto repetida, no como ocho elementos |
| Cupo sin margen de descarte | Falta el 14% en todos los escenarios a la vez |
| Bajar el umbral de píxeles para todo el episodio | Se cuela material blando donde sí había bueno |

## Relacionado

`190` · `174` · `176` · `194` · `10` · `93`
