# 123 · Música anclada a palabra

**Qué resuelve:** que un acorde caiga exactamente sobre una palabra. Es el recurso más
caro del episodio en atención del montador y el que más se nota cuando está bien: la
música deja de acompañar y empieza a subrayar.

---

## De dónde sale el segundo exacto

De `tiempos.json`, que guarda cada palabra de la locución con su inicio, duración y fin:

```json
{"w": "consta.", "limpia": "consta", "t": 62.981, "d": 0.473, "fin": 63.454}
```

Y de la función que lo consulta. Está en `acabar.py` y es la misma de `tiempos.py`:

```python
def cuando(palabra, defecto=0.0):
    """Segundo de una palabra del guion, para colgar de ella un efecto."""
    anc = re.sub(r"[^\wáéíóúüñÁÉÍÓÚÜÑ]", "", palabra).lower()
    for p in tiempos["palabras"]:
        if p["limpia"] == anc:
            return p["t"]
    print(f"  ! ancla de sonido sin coincidencia: '{palabra}' -> {defecto:.2f} s")
    return defecto
```

## 🔴 Las dos trampas de `cuando()`, las dos comprobadas

**1 · Devuelve la PRIMERA aparición.** En el episodio 01 hay **155 palabras y 23 de las
98 distintas se repiten**. `"años"` sale dos veces: en **31,20** y en **38,49**.
`acabar.py` ancla ahí el reloj con `cuando("años", 38.49)` — el valor por defecto delata
que se buscaba la segunda — pero `cuando()` devuelve la primera y **el reloj entra 7,3 s
antes de lo previsto**. Es un fallo real, en producción, y en el vídeo se oye como un
efecto que no viene a cuento.

El arreglo es pedir la ocurrencia:

```python
def cuando(palabra, defecto=0.0, n=1):
    """n=1 la primera aparición, n=2 la segunda... n=-1 la última."""
    anc = re.sub(r"[^\wáéíóúüñÁÉÍÓÚÜÑ]", "", palabra).lower()
    hits = [p["t"] for p in tiempos["palabras"] if p["limpia"] == anc]
    if not hits or abs(n) > len(hits):
        print(f"  ! ancla sin coincidencia: '{palabra}'[{n}] -> {defecto:.2f} s")
        return defecto
    return hits[n - 1 if n > 0 else n]
```

**2 · Falla en silencio.** Un ancla con puntuación (`"consta."`) o con una tilde distinta
no casa nunca y el efecto cae en el defecto **sin romper nada**. El aviso se imprime, pero
si nadie mira la consola el episodio sale con el acorde en el sitio equivocado. Por eso
todo ancla lleva un defecto **que es el valor correcto conocido**: si el `print` aparece,
la mezcla sigue siendo válida.

## La tabla de desfases: dónde vive la energía del sonido

Un sonido no se ancla en su segundo 0: se ancla donde el oyente percibe su **golpe**.

| Sonido | Dónde está su energía | Desfase | Valor real en `acabar.py` |
|---|---|---|---|
| **Acorde de piano** | Al principio (ataque de 8 ms) | **−0,03 a 0,00 s** | — |
| Impacto | Al principio | −0,10 a −0,15 s | `dr_impacto` −0,12 · `dr_golpe` −0,10 |
| Revelación | Al principio, con cola | −0,15 s | `dr_revela` −0,15 |
| Papel, obturador | Al principio | −0,20 / −0,30 s | `ob_papel` −0,20 · `ob_obturador` −0,30 |
| Destello | Casi instantáneo | **−0,06 s** | `tr_flash` −0,06 |
| **Riser** | **Al FINAL: crece hacia la palabra** | **−2,2 s** | `dr_riser` −2,2 |

La regla que resume la tabla: **un sonido de impulso se ancla en `t − 0,1`; un sonido que
construye se ancla en `t − su_duración`**. El riser de 2,3 s empieza 2,2 s antes de
"aprendiz" precisamente para llegar arriba justo en la sílaba.

## Un acorde de piano sobre una palabra

Se genera con `piano.py` y entra en `PISTAS` como una pista más. El ataque de 8 ms hace
que no necesite prácticamente desfase.

```python
import piano

# re menor con séptima: los 12 ms entre notas son el arpegio de una mano real
acorde = [(0.000, "D2", 3.0, 0.95), (0.012, "F3", 2.6, 0.45),
          (0.024, "A3", 2.6, 0.45), (0.036, "C4", 2.4, 0.38)]
piano.tocar(acorde, os.path.join(SON, "ac_consta.wav"), cola=2.0)   # → 3,94 s

PISTAS += [("ac_consta", cuando("consta", 62.98) - 0.03, 3.9, 0.30, False)]
```

Los **12 ms de separación entre notas** no son decorativos: un acorde con las notas
exactamente simultáneas suena a sintetizador. Una mano real nunca es simultánea.

## Cuándo merece la pena

| Merece | No merece |
|---|---|
| La palabra que da nombre al episodio | Cualquier sustantivo llamativo |
| La cifra que lo cambia todo | Todas las cifras |
| El verbo del giro (`consta`, `separar`) | Adjetivos |
| El remate de la última frase | El final de cada bloque |

**Tope: 2 o 3 acordes anclados por episodio.** Anclado a todo, nada está anclado — y
además cada acorde nuevo compite con el colchón que ya suena (`120`).

Antes de anclar, dos preguntas: ¿la palabra está **sola**, con aire alrededor? Si cae en
medio de una enumeración rápida, el acorde se pierde. ¿Hay ya un destello ahí? Entonces el
acorde va con él, no aparte (`125`).

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Anclar a una palabra repetida sin decir cuál | El efecto cae 7 s antes (bug real del piloto con `"años"`) |
| Ancla con puntuación o tilde distinta | Cae en el defecto **en silencio** |
| Defecto puesto a `0.0` | Cuando falla, el efecto se va al segundo 0 del episodio |
| Anclar un riser en `t − 0,1` | El riser revienta DESPUÉS de la palabra: suena a error |
| Acorde con las notas simultáneas | Suena a sintetizador, no a piano |
| Cinco o seis acordes anclados | Ninguno significa nada; el episodio suena a videojuego |
| Anclar sin comprobar que hay aire | La palabra va en una enumeración y el acorde se pierde |

## Relacionado

`125` música y destello · `84` picos dramáticos · `39` sincronizar gesto y palabra ·
`120` intensidad · `82` componer por código
