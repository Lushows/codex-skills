# 38 · Ritmo del movimiento

**Qué resuelve:** cada plano puede estar bien movido y el episodio seguir siendo
monótono. El ojo no juzga el plano: juzga la **secuencia**. Empujar en los ocho primeros
planos se detecta al tercero, y a partir de ahí el espectador deja de mirar el cuadro.

---

## Las cinco familias

| Código | Familia | Qué hace |
|---|---|---|
| **A** | Acercarse | Empuje, parallax hacia dentro |
| **B** | Alejarse | Pull-out |
| **C** | Lateral | Travelling, panorámica, deriva horizontal |
| **D** | Vertical | Grúa, deriva hacia arriba o hacia abajo |
| **E** | Cámara quieta, capas vivas | El fondo casi no se mueve; el evento son los elementos |

`E` no es un plano estático: el recorrido baja al 4-6% pero entran tres o cuatro
elementos. Es el plano de dato, de trámite, de lista. Debe ser el **15-25%** del episodio.

## Las tres reglas

1. **Nunca la misma familia en dos planos seguidos.** Es la regla dura
2. **Máximo dos de la misma familia en cualquier ventana de cinco planos**
3. **Nunca tres planos seguidos con el mismo sentido general.** `A`, parallax hacia
   dentro y grúa que se acerca son familias distintas pero los tres empujan: el ojo lee
   una sola cosa

## Los dos patrones que aburren

| Patrón | Por qué falla |
|---|---|
| `A A A A A` | Una sola emoción durante todo el episodio: avanzar |
| `A B A B A B` | Metrónomo. Alternar estrictamente es tan predecible como no alternar |

Lo que funciona es **variedad con restricción**, no alternancia:

```
A  C  B  A  D  C  E  B  A  C  E  D
```

Ninguna repetición contigua, ninguna familia más de dos veces en cinco, y aun así no hay
manera de adivinar la siguiente.

## La curva de intensidad del episodio

El recorrido no es constante: sigue la forma del guion.

| Bloque | Recorrido | Familias predominantes |
|---|---|---|
| Gancho (0-15 s) | 13-16% | `A`, `C` — energía inmediata |
| Planteamiento | 9-12% | Repartido |
| Explicativo / datos | 5-8% | `E`, `B` — el dato necesita quietud para leerse |
| Escalada | 11-14% | `A`, `D` |
| Remate | 12-16% y **freno** | `A` con easeOut fuerte, o `B` que revela |

## El corte va en pleno movimiento

Un plano que **termina su gesto y luego espera al corte** deja un agujero: 0,4-0,8 s de
imagen quieta que se leen como fallo. El gesto debe estar todavía vivo cuando entra el
plano siguiente.

Dos excepciones: el **freno narrativo** (`34`), donde la detención es el gesto, y el
último plano del episodio.

**Continuidad en el corte:** el plano nuevo o va claramente en contra del anterior, o va
en otra familia. Lo que no puede es ir en la misma dirección a velocidad parecida — eso
se lee como un salto de montaje, como si el mismo plano hubiera dado un tirón.

## Planificar la secuencia

En la tabla de eventos, cada plano lleva su familia y su recorrido:

```python
PLAN = [
    {"plano": 1, "fam": "A", "r": 0.15, "d": 3.2},
    {"plano": 2, "fam": "C", "r": 0.14, "d": 2.8},
    {"plano": 3, "fam": "B", "r": 0.11, "d": 3.6},
    {"plano": 4, "fam": "E", "r": 0.05, "d": 4.1},
]
```

Y se valida antes de renderizar, que es cuando cuesta barato:

```python
def validar(plan):
    fallos = []
    fam = [p["fam"] for p in plan]
    for i in range(1, len(fam)):
        if fam[i] == fam[i-1]:
            fallos.append(f"plano {i+1}: repite familia {fam[i]}")
    for i in range(len(fam) - 4):
        v = fam[i:i+5]
        for f in set(v):
            if v.count(f) > 2:
                fallos.append(f"planos {i+1}-{i+5}: {f} aparece {v.count(f)} veces")
    for i in range(2, len(fam)):
        if all(f in ("A", "D") for f in fam[i-2:i+1]):
            fallos.append(f"planos {i-1}-{i+1}: tres empujes seguidos")
    e = sum(1 for f in fam if f == "E") / len(fam)
    if not 0.15 <= e <= 0.25:
        fallos.append(f"planos E al {e:.0%} (banda 15-25%)")
    return fallos
```

Si `validar()` devuelve algo, se cambia el plan — **no** se renderiza para ver qué tal
queda. Un episodio son 40 minutos de render; la tabla se corrige en dos.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Empujar por defecto en todos los planos | Se detecta al tercer plano |
| Alternar A y B estrictamente | Metrónomo: igual de predecible |
| Tres gestos "hacia dentro" de familias distintas | El ojo lee un solo movimiento largo |
| El gesto termina antes que el plano | 0,4-0,8 s de imagen quieta antes del corte |
| Dos planos seguidos con la misma dirección y velocidad | Se lee como salto de montaje |
| Sin planos `E` | Los datos pasan sin que se lean |
| Solo planos `E` en la parte explicativa | Ese tramo se hunde de ritmo |
| Recorrido igual en todo el episodio | No hay gancho ni remate: todo suena igual |

## Relacionado

`15` rampa de ritmo · `18` densidad por tipo de bloque · `19` errores de ritmo ·
`34` movimiento que narra · `37` cámara simulada
