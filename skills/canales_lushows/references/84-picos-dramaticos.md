# 84 · Picos dramáticos

**Qué resuelve:** cómo se construye el momento en que entra la cifra. Un pico no es
subir el volumen: es **relieve**. El oído no percibe niveles absolutos, percibe
diferencias — y lo que hace pesar un golpe es el vacío que viene después.

---

## Un golpe son tres piezas y un hueco

| Pieza | Qué aporta | De la biblioteca |
|---|---|---|
| **Riser** | Expectativa. Sube 2-2,4 s y muere en el golpe | `dr_riser` |
| **Transitorio** | El chasquido que da pegada al ataque | `dr_golpe` |
| **Cuerpo** | El grave que se siente en el pecho | `dr_impacto` |
| **Silencio** | Lo que hace que la cifra pese | *(ducking del ambiente)* |

Quitar cualquiera de las cuatro estropea el efecto, pero la que más se olvida es la
cuarta, que además es gratis.

## La línea de tiempo exacta

Con **t = 0** en el fotograma donde entra la cifra:

| Momento | Qué ocurre | Parámetro |
|---|---|---|
| **−2,30 s** | Arranca el riser desde cero | `dr_riser`, ganancia 0,40 |
| −0,60 s | El riser ya se oye claramente | `pow(t/2.4, 3.4)` |
| **−0,10 s** | Transitorio seco | `dr_golpe`, ganancia 0,52 |
| **0,00 s** | Impacto grave + la cifra en pantalla | `dr_impacto`, ganancia 0,62 |
| **+0,30 s** | El ambiente empieza a caer | inicio de la rampa |
| +0,75 s | Ambiente al **14%** — esto es el silencio | `1-0.86*rampa(...)` |
| **+2,60 s** | El ambiente vuelve en 0,45 s | fin de la rampa |

Los tres números que no se tocan: **2,3 s de riser**, **0,10 s de adelanto del
transitorio** y **2,3 s de silencio posterior**. Con menos de 2 s el riser no construye
expectativa; con más de 3 s el espectador se aburre antes del golpe.

## El código

```python
GOLPE  = cifra["inicio"]              # el fotograma donde entra la cifra
RISER0 = max(0.0, GOLPE - 2.3)        # el riser arranca 2,3 s antes
S0, S1 = GOLPE + 0.30, GOLPE + 2.60   # el silencio va DESPUÉS del impacto

def rampa(a, b, f=0.30):
    """Trapecio: sube en f, se mantiene, baja en f. `between(t,a,b)` sería un clic."""
    return f"min(1,max(0,min((t-{a:.2f})/{f},({b:.2f}-t)/{f})))"

FC = (
    # RISER — ruido que crece exponencialmente y muere justo en el golpe
    f"anoisesrc=d=2.3:c=white,highpass=f=700,"
    f"volume='0.30*pow(t/2.3,3.4)':eval=frame,"
    f"adelay={int(RISER0*1000)}|{int(RISER0*1000)}[riser];"

    # IMPACTO — 47 Hz, se siente más de lo que se oye
    f"sine=f=47:d=2.6,volume=0.85,afade=t=out:st=0:d=2.6,"
    f"adelay={int(GOLPE*1000)}|{int(GOLPE*1000)}[golpe];"

    f"[cama][riser][golpe]amix=inputs=3:normalize=0:duration=longest,"
    # EL SILENCIO: el ambiente cae al 14% durante 2,3 s. El vacío es lo que pesa.
    f"volume='1-0.86*{rampa(S0, S1, 0.45)}':eval=frame,"
    f"aformat=channel_layouts=stereo[amb];"
)
```

Con la biblioteca ya sintetizada (`89`) se declara en la tabla de pistas y basta:

```python
("dr_riser",   cuando("toneladas", 22.2) - 2.30, 2.4, 0.40, False),
("dr_golpe",   cuando("toneladas", 22.2) - 0.10, 1.2, 0.52, False),
("dr_impacto", cuando("millones",   1.11) - 0.12, 2.8, 0.62, False),
("dr_revela",  cuando("pescado",   71.9) - 0.15, 3.5, 0.50, False),
```

## `pow(t/D, 3.4)`: por qué el exponente

Una rampa lineal (`t/D`) se percibe como algo que sube y ya. El oído responde a la
energía de forma logarítmica, así que una subida lineal suena **plana al final**, justo
donde tiene que apretar.

| Exponente | Sensación |
|---|---|
| 1,0 | Plano. No construye nada |
| 2,0 | Sube, pero se anticipa demasiado pronto |
| **3,4** | El 70% del recorrido ocurre en el último tercio. Es el valor del canal |
| 6,0 | No hay riser: hay un golpe con cola por delante |

## El presupuesto de picos

| Duración | Picos grandes | Mínimo entre dos |
|---|---|---|
| 60-90 s | **2 a 3** | 12 s |
| 3-5 min | 4 a 6 | 25 s |
| 10-12 min | 8 a 10 | 45 s |

Un episodio con un pico cada 8 segundos no tiene picos: tiene un nivel alto constante y
el espectador deja de reaccionar a los 30 s. **El pico funciona porque es escaso.**

## Los tres tipos y cuándo va cada uno

| Tipo | Piezas | Cuándo |
|---|---|---|
| **Golpe de cifra** | riser + transitorio + impacto + silencio | La cantidad que sostiene el episodio |
| **Revelación** | riser + `dr_revela` (acorde que se abre) | Cuando algo se entiende, no cuando algo golpea |
| **Cierre de bloque** | `tr_cierre` (barrido descendente) | Fin de escena, sin drama |

La revelación **no lleva silencio detrás**: se entiende algo, y el ambiente tiene que
sostener ese momento, no dejarlo caer.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Impacto sin silencio detrás | El golpe pasa y no queda nada; la cifra no pesa |
| Silencio **encima** del impacto | Se apaga el propio golpe. Va a partir de +0,30 s |
| Riser de menos de 2 s | No da tiempo a construir expectativa |
| Riser lineal | Suena plano justo donde tiene que apretar |
| Impacto sin transitorio | Suena a "puf" grave, sin pegada |
| Un pico cada pocos segundos | El oído se adapta y deja de reaccionar |
| Subir la música en el clímax | Lo contrario de lo que funciona: el clímax se hace con vacío |
| Ambiente al 0% en el silencio | Se oye el corte del propio silencio; el suelo es 14%, no cero |

## Relacionado

`80` arquitectura · `82` música · `85` ducking · `89` biblioteca
