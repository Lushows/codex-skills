# 31 · Curvas de aceleración

**Qué resuelve:** el movimiento lineal es la marca de agua del video hecho a mano. Nada
en el mundo físico arranca y se detiene a velocidad constante — ni una cámara, ni un
brazo, ni un papel que cae. El ojo lo sabe aunque el espectador no sepa nombrarlo.

---

## Por qué el lineal se ve barato

Un movimiento lineal tiene aceleración cero en el medio e **infinita en los extremos**:
el primer fotograma pasa de 0 px/f a 4 px/f de golpe. Ese salto es lo que se lee como
"animación de plantilla". La corrección es siempre la misma: repartir la aceleración.

**La excepción honesta:** un empuje de fondo que ocupa el plano entero y se corta por
ambos lados **puede** ser lineal, porque el espectador nunca ve su arranque ni su
frenada — los tapa el corte. Todo lo que empieza o termina en pantalla, no.

---

## La variable normalizada

Todas las curvas se escriben sobre `u`, el avance de 0 a 1:

```
u = clip((t - T0) / D, 0, 1)
```

En `zoompan` no hay `t` fiable con imagen en bucle. Se usa `on/25`:

```
u = clip((on/25 - T0) / D, 0, 1)
```

## Las cuatro curvas del canal

| Curva | Fórmula sobre `u` | Cuándo |
|---|---|---|
| **easeOut cúbica** | `1-pow(1-u,3)` | Por defecto. Todo lo que **aterriza**: entradas, cifras, frenadas narrativas |
| **easeIn cuadrática** | `pow(u,2)` | Lo que **arranca y se va**: salidas, empuje que acelera hacia el corte |
| **smoothstep** | `u*u*(3-2*u)` | Gestos de cámara que empiezan y terminan en pantalla: travelling, grúa |
| **smootherstep** | `u*u*u*(u*(u*6-15)+10)` | Igual pero más suave. Movimientos largos (más de 4 s) |

Aplicar a un valor: `valor = A + (B-A) * curva(u)`.

## Escrito en ffmpeg

Empuje de 12% en 3,4 s que **frena** (easeOut):

```
zoompan=z='1+0.12*(1-pow(1-clip((on/25)/3.4,0,1),3))':d=1:
        x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080:fps=25
```

Deslizamiento de 90 px por la izquierda, en 0,32 s, con easeOut:

```
[bg][el]overlay=x='1080-90*pow(1-clip((t-1.40)/0.32,0,1),3)':y='412':
                enable='gte(t,1.40)'
```

Fíjate: con `clip` no hace falta ningún `if(lt(t,T0+d),…)`. Pasado `T0+D`, `u` vale 1,
`pow(0,3)` vale 0 y `x` queda exactamente en su posición final. Una sola expresión,
sin ramas, sin riesgo de que el elemento quede a un píxel de su sitio.

Travelling con smoothstep (arranca y para dentro del plano):

```
zoompan=z='1.18':d=1:
        x='(iw-iw/zoom)*(0.20+0.60*(clip((on/25)/4.0,0,1)*clip((on/25)/4.0,0,1)*(3-2*clip((on/25)/4.0,0,1))))':
        y='(ih-ih/zoom)*0.55':s=1920x1080:fps=25
```

## Sigmoide, cuándo sí

La sigmoide real (`1/(1+exp(-k*(u-0.5)))`) tiene un problema: no vale 0 en `u=0` ni 1 en
`u=1`, así que hay que normalizarla y el resultado es indistinguible de `smootherstep`
a simple vista. **No la uses en producción.** Solo tiene sentido cuando quieres una
frenada muy larga con arranque muy corto, y para eso es más limpio subir el exponente:

```
easeOut fuerte:  1-pow(1-u,5)     ← el 80% del recorrido en el primer 30% del tiempo
```

## El generador en Python

El motor arma las expresiones; no se escriben a mano:

```python
def u(t0, d, var="t"):
    return f"clip(({var}-{t0})/{d},0,1)"

def ease_out(t0, d, a, b, var="t", p=3):
    return f"({a}+({b}-{a})*(1-pow(1-{u(t0,d,var)},{p})))"

def smoothstep(t0, d, a, b, var="t"):
    e = u(t0, d, var)
    return f"({a}+({b}-{a})*({e}*{e}*(3-2*{e})))"

# zoompan: var="(on/25)" y t0=0, porque el reloj del plano arranca en 0
z = ease_out(0, 3.4, 1.0, 1.12, var="(on/25)")
```

Sí, `u` se repite tres veces en `smoothstep`. El evaluador de ffmpeg tiene `st()`/`ld()`
para guardar variables, pero exigen un `;` dentro de la expresión y el `;` es el
separador de cadenas del `filter_complex`: se cuela un fallo de parseo cada dos por tres.
Repetir la expresión desde Python no cuesta nada y no falla nunca.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Curva sin `clip` | Pasado `D` el valor sigue creciendo y el elemento se va del cuadro |
| `easeIn` en una entrada | El elemento aparece lento y aterriza de golpe: al revés |
| `smoothstep` en todo | Un episodio entero blando, sin acentos |
| Usar `t` dentro de `zoompan` | Con imagen en bucle no es fiable; va `on/25` |
| Curva sobre el zoom pero lineal en `x`/`y` | La cámara acelera y se desplaza a la vez a ritmos distintos: se nota |
| `st()`/`ld()` dentro de `filter_complex` | El `;` rompe el grafo de filtros |

## Relacionado

`30` catálogo de movimientos · `32` entradas y salidas · `36` contadores ·
`37` cámara simulada · `39` sincronizar gesto y palabra
