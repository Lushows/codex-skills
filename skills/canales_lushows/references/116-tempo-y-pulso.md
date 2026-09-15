# 116 · Tempo y pulso

**Qué resuelve:** a qué velocidad va la música del canal y por qué. El valor corto es
**60-70 ppm**, cerca del pulso humano en reposo. Este módulo dice qué parte de eso está
documentada, qué parte es tradición, y qué pasa exactamente por encima y por debajo.

---

## La conversión

```python
def compas(ppm, tiempos=4):
    """ppm -> segundos de compás. El ciclo T del ostinato (112)."""
    return tiempos * 60.0 / ppm
```

| ppm | Negra (s) | Compás 4/4 (s) | Uso |
|---|---|---|---|
| 50 | 1,200 | 4,800 | Demasiado lento: se oye como pieza detenida |
| **56** | 1,071 | **4,286** | El remate, apagándose |
| 60 | 1,000 | 4,000 | Un golpe por segundo. Cómodo y algo obvio |
| 62 | 0,968 | 3,871 | |
| **66** | 0,909 | **3,636** | El pulso de `_cierre` |
| **70** | 0,857 | **3,429** | El pulso de trabajo del canal |
| 75 | 0,800 | 3,200 | **Techo del motor** (ver abajo) |
| 90 | 0,667 | 2,667 | El motor se apila. Ya no es este canal |

## Qué está documentado

| Afirmación | Estado |
|---|---|
| El pulso en reposo de un adulto está entre 60 y 100 ppm | **Documentado.** Es el rango clínico estándar |
| Un tempo musical más rápido sube la activación percibida | **Documentado** y muy robusto, en estudios de autoinforme |
| La **respiración** del oyente se acopla al fraseo musical | **Documentado**, con efecto moderado |
| El **corazón** se sincroniza con el tempo de la música | **Débil y discutido.** Los efectos medidos son pequeños e inconsistentes |
| Por eso 60-70 ppm "baja la activación y sube la absorción" en un vídeo | **Nuestra hipótesis.** No la hemos medido |

La versión honesta: *elegimos 60-70 ppm porque está en el rango que la literatura asocia
a baja activación, y porque en la sala funciona.* No: *"el cerebro se sincroniza con el
latido"*.

## La razón que sí podemos defender: la rejilla

A 70 ppm el ciclo del ostinato es **3,43 s**, o sea **17,5 ciclos por minuto**. El
desarrollo de un episodio va a **40-48 eventos por minuto** (`93`): eso son
**2,3 - 2,7 eventos visuales por ciclo musical**.

Es el reparto que hace que imagen y sonido parezcan pensados juntos: cada ciclo lleva un
par de cosas y ninguna pisa a la otra. A 90 ppm hay 22,5 ciclos/min y los golpes del
bajo empiezan a caer entre eventos, sin coincidir con nada. A 50 ppm hay 12,5 y cada
ciclo tiene que aguantar cuatro eventos: el bajo deja de marcar.

## El techo real: 75 ppm, y lo pone el motor

Las duraciones del canal son **bajo 3,0 s** y **acorde 2,2 s entrando en `t0 + 1,10`**.
Para que el bajo no se solape consigo mismo hace falta `T ≥ 3,2 s`, y eso es exactamente
**4 · 60 / 3,2 = 75 ppm**.

Por encima, `amix=inputs=N:normalize=0` (`piano.py:106`) suma las notas solapadas. El
efecto sobre el nivel es **pequeño y está medido en `112`**: unos 2 dB de corrimiento
hacia el grave, no una saturación. Lo que se pierde es el **pulso**, que es justamente lo
único que aporta subir el tempo. Medido con cuatro compases idénticos:

```python
for ppm in (56, 66, 90):
    T = compas(ppm)
    ns = []
    for c in range(4):
        ns += bloque(c * T, "D2", ["D3","F3","A3"], [(0.45,"A4"), (round(T/2,2),"F4")])
    tocar(ns, f"116_{ppm}ppm.wav")
# 56 ppm -> 24 notas · 17,54 s   T=4,286  sobra 1,29 s: respira
# 66 ppm -> 24 notas · 15,27 s   T=3,636  sobra 0,64 s: el punto
# 90 ppm -> 24 notas · 12,27 s   T=2,667  🔴 el bajo se pisa 0,33 s y el acorde 0,63 s
```

**Si hace falta ir más rápido, se acortan las notas, no solo el ciclo:**

```python
def bloque_rapido(t0, raiz, acorde, T):
    d_bajo   = round(max(0.4, min(3.0, T - 0.2)), 1)   # 0,2 s de aire, y nunca <0,4
    d_acorde = round(max(0.4, min(2.2, T - 1.3)), 1)
    ns = [(t0, raiz, d_bajo, 0.95)]
    for k, a in enumerate(acorde):
        ns.append((t0 + 1.10 + k * 0.014, a, d_acorde, 0.38))
    return ns
```

⚠️ `muestra()` falla si la duración baja de **0,36 s**: monta un
`afade=t=out:st=dur-0.35` y con `dur=0,3` pide `st=-0,05`, que ffmpeg rechaza
(`Value -0.050000 for parameter 'st' out of range`). Verificado: 0,2 y 0,3 revientan;
0,4 funciona. **Nunca pasar duraciones por debajo de 0,4 s.**

## El comentario del piloto no cuadra

`piano.py:137` dice `T = 3.2   # el compás, a ~62 ppm`. No sale:

| Lectura de T = 3,2 s | ppm |
|---|---|
| Compás de 4 tiempos | **75,0** |
| Compás de 3 tiempos | **56,2** |
| Compás de 3,31 tiempos | 62,0 ← no existe |

`_cierre` usa T = 3,6 s → **66,7 ppm** en 4/4, que sí está en el rango bueno. Así que
**el colchón principal del canal va a 75 ppm, justo en el techo del motor**, y el
comentario dice 62. Ninguna de las dos cosas rompe nada hoy —el bajo de 3,0 s cabe por
0,2 s— pero está al borde: cualquiera que alargue el bajo a 3,4 s "para que suene más
lleno" lo apila sin darse cuenta. Lo limpio es dejar `T = 3.429` (70 ppm) y corregir el
comentario.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Subir el tempo por encima de 75 ppm sin acortar las notas | El bajo se apila y deja de articular: se pierde el pulso (`112`) |
| Duraciones por debajo de 0,4 s | `muestra()` falla con `afade ... st out of range` y devuelve `None` |
| Bajar de 50 ppm | La pieza se oye detenida; el bajo deja de marcar nada |
| Cambiar el tempo dentro del episodio | Se lee como fallo de reproducción, no como recurso |
| Montar los eventos sin mirar la rejilla `T` | 2-3 eventos por ciclo es lo que hace que parezca pensado junto |
| Confiar en el comentario `~62 ppm` | Es falso: T = 3,2 s son 75 ppm en 4/4 |
| Decir que el corazón se sincroniza con el tempo | Efecto pequeño y discutido. La respiración sí, el pulso apenas |

## Relacionado

`112` el ostinato · `115` progresiones por tramo · `117` dejarle sitio a la voz ·
`10` densidad de eventos · `93` estructura de episodio · `38` ritmo del movimiento
