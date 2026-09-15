# 154 · Anclas que caen al valor por defecto

**Qué resuelve:** el ancla es una palabra del guion; si no casa, el efecto **no
desaparece: se va al valor por defecto** y suena o entra donde no toca, sin aviso.

---

## Cómo se manifiesta

Dos casos reales, los dos en el episodio 01, los dos sin una sola excepción.

**1 · El ancla con puntuación no casa nunca.** En la tabla de sonido:

```python
("ob_billetes", cuando("efectivo?", 15.5) - 0.3, 1.6, 0.42, False),
```

`tiempos.json` guarda las palabras **normalizadas** —sin signos y en minúscula—, así
que `"efectivo?"` no coincide con `efectivo` jamás. El efecto cae a `15.5`, que era un
número escrito a ojo tres versiones antes. Lo mismo con `"ganarla...."` o `"máquina,"`.

**2 · `cuando()` devuelve la PRIMERA aparición.** Un tictac colgado de una palabra que
sale dos veces entraba **7,3 s antes** de donde debía, sobre el plano equivocado.

Ambos suenan «raro» en la escucha, pero no se localizan: parece un problema de mezcla,
de ducking o de ritmo, y se pierden horas ahí.

## Por qué ocurre

Un valor por defecto es un **absorbedor de fallos**: se escribe para que el script no se
caiga si falta una palabra y, a cambio, convierte un error duro en un desajuste mudo.
Como el desajuste es de décimas o de segundos —no de minutos—, el oído lo registra como
«algo va mal» sin poder señalar qué.

La segunda causa es más sutil: **una palabra no identifica un instante**. «vendió»,
«millones», «pescado» salen varias veces. Coger la primera es una decisión implícita,
y en cuanto el guion crece deja de ser la correcta.

## Cómo se caza

La normalización tiene que ser **la misma en los tres sitios** que resuelven anclas —
`tiempos.py` (que escribe `limpia`), `motor.py`/`auditar.py` (imagen) y `acabar.py`
(sonido)—: `re.sub(r"[^\wáéíóúüñÁÉÍÓÚÜÑ]", "", palabra).lower()`, copiada literal.

Y una pasada que lista todas las anclas huérfanas antes de renderizar:

```python
for esc in ESCENAS:
    for ele in esc.get("elementos", []) + esc.get("destellos", []):
        if "ancla" not in ele:
            continue
        anc = re.sub(r"[^\wáéíóúüñÁÉÍÓÚÜÑ]", "", ele["ancla"]).lower()
        veces = sum(1 for p in tiempos["palabras"]
                    if p["limpia"] == anc and esc["ini"] - 0.6 <= p["t"] <= esc["fin"])
        if veces == 0:
            print(f"  HUÉRFANA  {esc['id']:<10} '{ele['ancla']}' -> cae al inicio")
        elif veces > 1 and "ancla_n" not in ele:
            print(f"  AMBIGUA   {esc['id']:<10} '{ele['ancla']}' sale {veces} veces "
                  f"y no se dice cuál")
```

⚠️ Si el ancla lleva puntuación, el aviso sale como HUÉRFANA aunque la palabra exista.
Es la pista: **el ancla se escribe siempre sin signos.**

## La guardia automática

**Uno · el aviso en el resolutor.** Es lo que hoy hacen `motor.py`, `auditar.py` y
`acabar.py`, y es el mínimo:

```python
def cuando(palabra, defecto=0.0):
    """Se normaliza igual que en tiempos.py: un ancla con puntuación no casa nunca
    y el efecto cae en el valor por defecto sin avisar."""
    anc = re.sub(r"[^\wáéíóúüñÁÉÍÓÚÜÑ]", "", palabra).lower()
    for p in tiempos["palabras"]:
        if p["limpia"] == anc:
            return p["t"]
    print(f"  ! ancla de sonido sin coincidencia: '{palabra}' -> {defecto:.2f} s")
    return defecto
```

**Dos · elegir la aparición.** `motor.py` y `auditar.py` ya lo llevan para los
elementos visuales, con la misma resolución en los dos archivos:

```python
# Una palabra puede salir varias veces en la misma escena. Sin decir cuál, se coge
# la PRIMERA y el elemento aterriza en el sitio equivocado: con "vendió" dos veces,
# el plano de la segunda venta se iba a la primera.
# 'ancla_n' elige la aparición (0 = la primera, 1 = la segunda...).
i = ele.get("ancla_n", 0)
base = cand[min(i, len(cand) - 1)]["t"] if cand else t0
```

**Pendiente, y es el mismo fallo:** `acabar.cuando()` sigue devolviendo la primera
coincidencia **de todo el episodio**, sin selector. La extensión es de dos líneas y
cierra el caso del tictac:

```python
def cuando(palabra, defecto=0.0, n=0, entre=None):
    anc = re.sub(r"[^\wáéíóúüñÁÉÍÓÚÜÑ]", "", palabra).lower()
    cand = [p["t"] for p in tiempos["palabras"] if p["limpia"] == anc
            and (entre is None or entre[0] <= p["t"] <= entre[1])]
    if not cand:
        print(f"  ! ancla de sonido sin coincidencia: '{palabra}' -> {defecto:.2f} s")
        return defecto
    if len(cand) > 1 and n == 0:
        print(f"  ? '{palabra}' sale {len(cand)} veces; se usa la primera")
    return cand[min(n, len(cand) - 1)]
```

El `entre=esc("celda")` acota el ancla a su escena y resuelve la ambigüedad sin contar
apariciones: es la forma preferida cuando la palabra es común.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Escribir el ancla con signos (`"efectivo?"`) | No casa nunca; el efecto cae al número escrito a ojo |
| Normalizar distinto en sonido y en imagen | El mismo ancla resuelve a dos instantes |
| Confiar en la primera aparición | El tictac entra 7,3 s antes, sobre otro plano |
| Defecto silencioso sin `print` | Fallo invisible; se busca en la mezcla durante horas |
| Cambiar la voz sin regenerar `tiempos.json` | Todas las anclas apuntan a otro segundo |
| Anclar a una palabra muy común | Ambigüedad garantizada; anclar a la rara de la frase |

## Relacionado

`150` el catálogo del fallo silencioso · `14` encadenar elementos · `39` sincronizar
gesto y palabra · `17` medir el montaje · `123` música anclada a palabra ·
`84` picos dramáticos
