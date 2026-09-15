# 156 · Recursos que no existen y mejoran las notas

**Qué resuelve:** el auditor no encontraba un recurso y le asignaba **superficie 0 y
caja nula**. El recurso que iba a reventar el render **mejoraba las métricas**.

---

## Cómo se manifiesta

Un elemento de la tabla de eventos apunta a un alias que no está en ninguna carpeta —
porque se renombró, porque el PNG nunca se generó, porque la pieza se quedó en el
episodio anterior. El auditor lo procesa sin quejarse: `area()` devolvía `0.0` y
`caja()` un rectángulo nulo. Y entonces pasa lo contrario de lo que uno esperaría:

| Métrica | Qué le hace un recurso inexistente |
|---|---|
| huecos | **los tapa** — cuenta como elemento vivo |
| simultaneidad media · eventos/min | **los sube** |
| se sale del cuadro · oclusión | **nunca saltan** (`if c is None: continue`) |
| reparto 3×3 | no ocupa celda, pero tampoco la delata |

Cinco de las siete comprobaciones lo dan por bueno y dos lo premian. El veredicto sale
**APTO PARA RENDER**. Y al renderizar:

```
FileNotFoundError: recurso no encontrado: ficha_juicio
```

La auditoría no sirvió para nada: lo único que debía atrapar, lo escondió.

## Por qué ocurre

Por un `return 0.0` escrito para que el auditor no se cayera: el mismo patrón de `154`,
un valor por defecto que convierte un fallo duro en un dato falso.

Y por una asimetría de rutas que agrava el caso: el auditor buscaba en el **banco
común** mientras `motor.buscar()` mira **primero el episodio**. Un episodio con su
propia carpeta `texto/` pasaba comprobaciones que no encontraban nada y por eso
siempre salían limpias — así se colaron **4,9 s de titular sobre el fondo** sin que la
comprobación de «planos de sólo texto» dijera una palabra.

**La regla:** cuando un auditor replica la resolución de otro módulo, tiene que
replicarla *entera* — el mismo orden de carpetas, las mismas extensiones, la misma
normalización. Si no, mide un montaje distinto del que se renderiza.

## Cómo se caza

Comparar las dos resoluciones sobre la tabla completa. Si una encuentra y la otra no,
el auditor está midiendo otra cosa:

```python
import motor, auditar
for esc in ESCENAS:
    for ele in esc["elementos"]:
        try:
            m = motor.buscar(ele["r"])
        except FileNotFoundError:
            m = None
        a = auditar.hallar(auditar.BASE, ele["r"], auditar.EPI)
        if (m is None) != (a is None) or (m and a and os.path.abspath(m) != os.path.abspath(a)):
            print(f"  DISCREPA  {esc['id']:<10} {ele['r']:<24} motor={m}  auditor={a}")
```

## La guardia automática

**Uno · no puntuar lo que no se encontró: apartarlo.** Es lo que ya hace `auditar.py`:

```python
def _prop(recurso):
    """alto/ancho del PNG. Se cachea: se consulta miles de veces."""
    if recurso not in _CACHE:
        _CACHE[recurso] = None
        p = hallar(BASE, recurso, EPI)
        if p is None:
            SIN_RESOLVER.add(recurso)          # se reporta, no se puntúa como 0
        else:
            ...
    return _CACHE[recurso]
```

y `caja()` devuelve `None` —no un rectángulo de superficie cero— cuando la proporción
no se pudo leer, de modo que el elemento sale de las comprobaciones geométricas en vez
de aprobarlas por la puerta de atrás.

⚠️ **La guardia está a medias y hay que cerrarla.** `SIN_RESOLVER` se llena pero **no
se imprime en ninguna parte**: el auditor sabe que hay recursos fantasma y se lo calla.
Las líneas que faltan, al final de `main()`:

```python
if SIN_RESOLVER:
    print(f"\n  --- RECURSOS QUE NO EXISTEN ({len(SIN_RESOLVER)}) ---")
    for r in sorted(SIN_RESOLVER):
        dónde = [f"{e['id']}" for e in ESCENAS
                 for x in e["elementos"] if x["r"] == r]
        print(f"   {r:<26} en {', '.join(sorted(set(dónde)))}")
    raise SystemExit("  el render va a fallar: genera o renombra esas piezas")
```

**Dos · el auditor resuelve con el mismo orden que el motor.** `rutas_material()` lo
formaliza —*«mismo orden que `motor.buscar()`: primero el episodio, luego el banco»*— y
todas las comprobaciones lo usan, incluida la de planos de sólo texto, que antes miraba
sólo el banco común.

**Tres · el aviso tiene que ser un aborto.** Un recurso inexistente no es una
advertencia de estilo: es un render que va a fallar. Código de salida 1, y el
encadenado `python auditar.py && python motor.py` hace el resto.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| `return 0.0` cuando el recurso falta | El fantasma tapa huecos y sube la simultaneidad |
| Recoger el fallo en un `set` y no imprimirlo | Guardia escrita, guardia inútil |
| Auditar con un orden de carpetas distinto al del motor | Se mide un montaje que no es el que se renderiza |
| Saltar el elemento con `continue` en las pruebas geométricas sin marcarlo | Nunca salta «se sale del cuadro» ni «tapado» |
| Avisar sin abortar | Se renderiza igual y se descubre 8 minutos después |
| Renombrar el PNG y no la tabla | Exactamente este fallo, cada vez |

## Relacionado

`150` el catálogo del fallo silencioso · `144` presencia no es superficie · `146` medir
lo que se ve, no lo que existe · `155` cachés que sirven el archivo equivocado ·
`192` alias estables y colisiones · `199` el manifiesto del material
