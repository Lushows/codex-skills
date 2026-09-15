# 15 · Rampa de ritmo

**Qué resuelve:** el episodio va a densidad constante. Aunque el número global sea
correcto, se siente plano: no hay aceleración hacia los remates ni aire en las
revelaciones, y el espectador deja de esperar nada.

---

## El principio

**El ritmo no es un número, es una curva.** La densidad media puede ser 46 eventos/min
y el episodio seguir siendo plano si todos los intervalos entre eventos miden lo mismo.
Lo que el espectador percibe como ritmo es la **derivada**: si el intervalo se acorta,
siente que algo viene; si se alarga de golpe, siente que algo acaba de pasar.

La unidad de trabajo no es "eventos por minuto" sino **el intervalo entre eventos**:

| Intervalo | Equivale a | Uso |
|---|---|---|
| 2,0-2,4 s | 25-30 ev/min | Frenada tras un pico. Máximo 2 s seguidos |
| 1,5-1,8 s | 33-40 ev/min | Explicativo: una comparación necesita entenderse |
| 1,2-1,4 s | 43-50 ev/min | Crucero |
| 0,8-1,0 s | 60-75 ev/min | Escalada hacia el remate |
| 0,45-0,6 s | 100-133 ev/min | Sólo los 2-3 últimos eventos antes del golpe |
| menos de 0,35 s | — | Parpadeo. No se usa nunca |

## La escalada

Antes de un remate se aceleran **3 o 4 eventos**, cada uno con el intervalo al 70% del
anterior. Menos de tres no se percibe; más de cinco cansa antes de llegar.

```python
def escalada(t_golpe, n=4, ultimo=0.45, k=0.70):
    """Segundos de entrada de los n eventos que preceden a un golpe en t_golpe.
    El intervalo se acorta un 30% en cada paso: el ojo lo lee como aceleración."""
    ts, t, hueco = [], t_golpe, ultimo
    for _ in range(n):
        t -= hueco
        ts.append(round(t, 2))
        hueco /= k
    return sorted(ts)

print(escalada(38.36))       # [35.04, 36.35, 37.27, 37.91]
```

Intervalos resultantes: 1,31 · 0,92 · 0,64 · 0,45 s. Cada elemento de la escalada es
corto (0,8-1,2 s) y **pequeño**: son acentos y datos, no principales. Un retrato en
mitad de una escalada la frena.

## La frenada

Justo después del golpe se corta la densidad de golpe: **un solo elemento, 1,2-2,0 s,
sin deriva**, sobre el fondo en movimiento. Es lo que hace que el golpe se oiga.

| Regla de la frenada | Valor |
|---|---|
| Duración | 1,2-2,0 s. Nunca más: pasado eso es un hueco |
| Elementos vivos | exactamente 1 (nunca 0: eso es un hueco, `11`) |
| Movimiento del elemento | ninguno |
| Movimiento del fondo | sí, y preferiblemente `out` — alejarse revela contexto |
| Cuántas por episodio | una por bloque grande; en un episodio de 8 min, 4 o 5 |

Una frenada sin golpe delante no es una frenada: es un bajón. **La frenada sólo existe
como consecuencia de una escalada.**

## La curva del episodio

```
ev/min
  60 |  ▁▇▇▆                                    ▇▇▆
  50 |  ▇   ▅▄                        ▄▅▆▇▇        ▆
  40 |         ▅▅▄▄▅▅▄▄▅▅▄▄▅▅▄▄▅▅  ▄▄▅               ▄▄
  30 |                                                  ▄▄▂
     +--------------------------------------------------------
      gancho    desarrollo         explicativo  remate   cierre
```

- **Gancho (0-15 s):** arranca alto y baja. Si arranca bajo, no hay episodio.
- **Desarrollo:** crucero con microondulaciones — cada bloque sube al terminar.
- **Explicativo:** baja de verdad. Una comparación de cifras no se entiende a 60 ev/min.
- **Remate:** escalada larga y la frenada más larga del episodio.
- **Cierre:** desciende hasta el final. No se remata acelerando.

Los valores concretos por tipo de bloque están en `18`.

## Cómo se acelera (y cómo no)

| Se acelera así | No se acelera así |
|---|---|
| Acortando el **intervalo entre entradas** | Acortando la vida de los elementos |
| Metiendo acentos cortos entre los principales | Metiendo principales más rápido |
| Troceando una cifra en estados (`13`) | Repitiendo el mismo recurso |
| Cortando de escena en mitad de la frase | Cortando de escena cada vez más rápido |

Acortar las vidas baja la duración media por debajo de 1,2 s y produce el síntoma de
parpadeo (`19`). La aceleración se hace **por separación, no por duración**.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Escalada de dos eventos | No se percibe como aceleración; sólo se ve prisa |
| Frenada de más de 2 s | Deja de ser aire y pasa a ser hueco |
| Frenada con 0 elementos | Es un hueco con otro nombre |
| Escalada con un retrato o un documento dentro | Frena la escalada justo donde debía apretar |
| Acelerar también el cierre | El episodio termina sin que nada aterrice |
| Rampa idéntica en todos los bloques | Se vuelve un tic: el espectador la anticipa |

## Relacionado

`10` densidad de eventos · `13` ciclo de vida del elemento · `14` encadenar elementos ·
`16` el plano de descanso · `18` densidad por tipo de bloque · `84` picos dramáticos
