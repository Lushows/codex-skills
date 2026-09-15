# 164 · Legibilidad por altura de mayúscula

**Qué resuelve:** el `font-size` **no mide lo que se lee**. Mide la caja em, que incluye
aire arriba y abajo. Lo que el ojo mide es la **caja de mayúscula**, y su proporción
cambia con la fuente: la de Arial es 0,718 em y la de Courier New 0,570. **Courier a
60 px se lee como Arial a 48.**

**Caso real:** tres gráficos con rótulos de 19 px dentro de un PNG de 760, mostrado a
656 px en el lienzo, quedaban en **16 px** de cuerpo en pantalla. Ilegibles, y las once
medidas del auditor los daban por buenos.

---

## Las dos reducciones que nadie ve

```
tamaño_en_pantalla = font_size × (ancho_mostrado / ancho_del_PNG)
caja_de_mayúscula  = tamaño_en_pantalla × ratio_de_la_fuente
```

El `ancho_mostrado` es el `w` que el elemento declara en `guion_visual.py`. **No es un
supuesto:** el proyecto lo tenía como constante (`ANCHO_MOSTRADO = 0.80 * 1920`,
`fx_lustig.py:33`) y una pieza colocada a 520 px se comprobaba como si midiera 1536. La
comprobación buena lee el `w` real de **cada uso**: la misma pieza a dos anchos distintos
da dos veredictos distintos.

## La tabla de cajas

Medida en esta máquina renderizando la `H` a 400 px con PIL y leyendo el `getbbox`:

| Fuente | Caja de mayúscula | `font-size` mínimo en pantalla |
|---|---|---|
| Impact | 0,790 em | 26 px |
| Verdana · Tahoma | 0,728 em | 28 px |
| **Arial · Arial Black · Trebuchet** | **0,718 em** | **28 px** |
| Archivo / Archivo Black *(la del canal)* | ≈ 0,715 em | 28 px |
| Georgia | 0,693 em | 29 px |
| Times New Roman | 0,662 em | 31 px |
| Consolas | 0,637 em | 32 px |
| **Courier New** *(la monoespaciada del canal)* | **0,570 em** | **35 px** |

**El suelo del canal son 20 px de caja de mayúscula** en el lienzo de 1920×1080; la
última columna es ese suelo traducido a cada fuente. Comprobación: Courier a 60 px da
`60 × 0,570 = 34,2` de caja; Arial a 48 da `48 × 0,718 = 34,5`. Se leen igual. Por eso el
bloque mecanografiado necesita entre un 20% y un 26% más de cuerpo que el de palo.

## El script

```python
#!/usr/bin/env python3
"""legible.py <proyecto> <episodio> - cuanto mide en PANTALLA la letra mas pequena."""
import glob, os, sys
from PIL import Image

CAJA = {"archivo": 0.715, "arial": 0.718, "georgia": 0.693, "times": 0.662,
        "courier": 0.570, "consolas": 0.637, "verdana": 0.728, "impact": 0.790}
MIN_CAJA = 20.0                    # px de caja de mayuscula en el lienzo de 1920

def main(proy, epi):
    sys.argv = ["x", epi]
    sys.path.insert(0, proy); sys.path.insert(0, os.path.join(proy, epi))
    import motor, diccionario
    from importlib import import_module
    diccionario.EPI_DIR = os.path.join(proy, epi)
    gv = import_module("guion_visual")

    FS, FAM = {}, {}                            # cuerpo minimo y familia, por pieza
    for ruta in (glob.glob(os.path.join(proy, epi, "fx_*.py")) +
                 glob.glob(os.path.join(proy, epi, "texto_*.py"))):
        m = import_module(os.path.splitext(os.path.basename(ruta))[0])
        FS.update(getattr(m, "FS", {})); FAM.update(getattr(m, "FAM", {}))

    anchos = {}
    for esc in gv.ESCENAS:
        for e in esc["elementos"]:
            anchos.setdefault(e["r"], []).append(e["w"])

    filas = []
    for nombre, fmin in FS.items():
        if nombre not in anchos: continue
        pw = Image.open(motor.buscar(nombre)).width
        ratio = CAJA.get(FAM.get(nombre, "archivo"), 0.715)
        for w in sorted(set(anchos[nombre])):        # un veredicto POR USO
            ep = fmin * w / float(pw)
            filas.append((ep * ratio, nombre, fmin, pw, w, ep))

    print(f"{'pieza':<18}{'fuente':>7}{'PNG':>6}{'mostr':>7}{'px pant':>9}{'caja':>7}")
    for caja, n, fmin, pw, w, ep in sorted(filas):
        print(f"{n:<18}{fmin:>7}{pw:>6}{w:>7}{ep:>9.1f}{caja:>7.1f}"
              f"{'   <-- ILEGIBLE' if caja < MIN_CAJA else ''}")

    sin = sorted(n for n in anchos if n not in FS and
                 os.path.basename(os.path.dirname(motor.buscar(n))) in ("texto", "fx"))
    for n in sin:
        print(f"{n:<18}   SIN REGISTRO de cuerpo minimo: nadie comprueba su legibilidad")

    mal = [f for f in filas if f[0] < MIN_CAJA]
    print(f"\n{len(filas)} usos · {len(mal)} por debajo de {MIN_CAJA:.0f} px de caja"
          f" · {len(sin)} sin registro")
    return 1 if (mal or sin) else 0

sys.exit(main(sys.argv[1], sys.argv[2]))
```

El dato del cuerpo mínimo lo pone el generador de piezas: `reg(nombre, w, h, fuente_min,
cuerpo)` guarda en `FS[nombre]` **la fuente más pequeña que aparece en esa pieza**. Desde
el PNG no hay forma de saberlo, así que **una pieza sin registrar aprueba por ausencia**.

## Lo que dice hoy del episodio

```
pieza              fuente   PNG  mostr  px pant   caja
titular_prensa         34  1280    520     13.8    9.9   <-- ILEGIBLE
columna_doble          34  1620    760     16.0   11.4   <-- ILEGIBLE
huella_expediente      34  1700    820     16.4   11.7   <-- ILEGIBLE
columna_doble          34  1620    820     17.2   12.3   <-- ILEGIBLE
balanza_02             34  1560    900     19.6   14.0   <-- ILEGIBLE
torre_esquema          34  1200    765     21.7   15.5   <-- ILEGIBLE
linea_02               36  1700   1080     22.9   16.4   <-- ILEGIBLE
lupa_casilla           36   980    760     27.9   20.0   <-- ILEGIBLE
sello_consta           60   760    680     53.7   38.4
d_1890               SIN REGISTRO de cuerpo minimo: nadie comprueba su legibilidad
...
17 usos · 15 por debajo de 20 px de caja · 7 sin registro
```

**`titular_prensa` a 9,9 px de caja es menos de la mitad del suelo**: en pantalla es una
mancha gris, y en móvil ni eso. `columna_doble` aparece **dos veces con veredicto
distinto según el ancho** —760 y 820 px—, que es justo lo que se pierde al comprobar
contra un ancho fijo. Y siete piezas de texto —`d_1890`, `d_fecha`, `d_preso`,
`m_consta`, `m_cuenta`, `r_casilla`, `r_sinfuente`— **no tienen registro**: nadie
comprueba su legibilidad. Las `balanza_*` coinciden además con las que `163` marca flojas
de contraste: una pieza pequeña *y* poco contrastada no está a medias, está fuera.

## Cómo se arregla, por orden de coste

1. **Subir el cuerpo en el HTML y regenerar el PNG.** Un rótulo de 34 px que se muestra a
   0,59 necesita **58 px**. Ojo: el texto ocupa más ancho, el navegador puede partirlo en
   dos líneas y se derrama por debajo de la caja.
2. **Mostrar la pieza más grande** subiendo su `w`. Es gratis, pero compite por sitio.
3. **Quitar texto.** Un gráfico con cuatro rótulos de 34 px y otro con dos de 58 dicen lo
   mismo; sólo el segundo se lee.
4. **Partirla en dos piezas** seguidas: cuesta un evento y arregla legibilidad y densidad.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Comprobar contra un ancho mostrado fijo | Una pieza a 520 px se aprueba como si midiera 1536 |
| Comparar `font-size` entre fuentes distintas | Courier a 60 px se lee como Arial a 48 |
| Medir la pieza una vez si se usa a dos anchos | El uso pequeño es el que falla y el que no se mira |
| Generar una pieza sin declarar su cuerpo mínimo | No se comprueba: aprueba por ausencia |
| Subir el cuerpo sin mirar si cabe | El navegador parte la línea y el texto se sale de la caja |
| Dar por bueno un rótulo porque «se lee en el monitor» | El monitor lo ve una persona: la que montó (`166`) |
| Usar la altura de x en vez de la caja de mayúscula | Los rótulos del canal van en mayúsculas |

## Relacionado

`163` contraste elemento-fondo · `166` la prueba del pulgar · `160` la grilla de
fotogramas · `42` tipografía del canal · `43` rótulos y etiquetas · `49` zona segura
