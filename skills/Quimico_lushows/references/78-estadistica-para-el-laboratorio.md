# 78 — Estadística para el laboratorio: cuándo dos resultados son distintos de verdad

La pregunta que más plata mueve en este oficio es simple: *"el laboratorio A me dio 27,4 % y el B me dio
25,1 % — ¿me están robando?"*. La respuesta casi nunca es sí o no: es **"depende de la variabilidad del
método"**. Sin estadística, terminas cambiando de proveedor por una diferencia que es puro ruido, o
aceptando una diferencia real porque "no se ve tan grande". Este módulo te da las cuatro o cinco
herramientas que de verdad usas cuando negocias con un laboratorio o auditas un COA.

Términos:
- **Media (mean, x̄)** = promedio. **Mediana (median)** = valor del centro; resiste los datos raros.
- **Desviación estándar (standard deviation, s)** = cuánto se dispersan los datos alrededor de la media.
- **RSD o CV (relative standard deviation / coefficient of variation)** = s dividida por la media, en %. Es
  la forma correcta de comparar dispersión entre analitos de magnitudes distintas.
- **Intervalo de confianza (confidence interval, CI)** = rango donde razonablemente está el valor verdadero.
- **Valor p (p-value)** = probabilidad de ver una diferencia así de grande si en realidad no hay diferencia.
- **Atípico (outlier)** = dato que no parece venir de la misma población.

## Lo mínimo indispensable

```
x̄  = suma(xi) / n
s  = raiz( suma((xi - x̄)^2) / (n - 1) )        <- n-1, no n (muestra, no población)
RSD (%) = 100 * s / x̄
Error estandar de la media (SEM) = s / raiz(n)
Intervalo de confianza al 95 % de la media:
    x̄  ±  t(0,975; n-1) * s / raiz(n)

t para 95 % bilateral:  n=3 -> 4,303 | n=4 -> 3,182 | n=5 -> 2,776
                        n=6 -> 2,571 | n=10 -> 2,262 | n=20 -> 2,093 | inf -> 1,960
```

Nota que con n = 3 el multiplicador es 4,3, no 2. Por eso un triplicado da intervalos anchísimos, y por eso
un laboratorio que te reporta "27,4 %" a partir de tres réplicas te está escondiendo un rango grande.

**Todos estos cálculos van a código**, nunca a cabeza (regla 4 de la skill). Rutea a
`Matematicas_lushows` o usa `lab-tools/`.

## ¿Los dos resultados son distintos? La prueba t

Para comparar dos laboratorios o dos lotes con réplicas:

```
t de Student para dos medias independientes (varianzas iguales):

    t = (x̄1 - x̄2) / ( sp * raiz(1/n1 + 1/n2) )
    sp = raiz( ((n1-1)*s1^2 + (n2-1)*s2^2) / (n1+n2-2) )
    grados de libertad = n1 + n2 - 2

Si |t| > t_critico(0,975; gl)  ->  las medias difieren significativamente (p < 0,05).

Si las varianzas NO son iguales (probar antes con F o Levene), se usa la
version de Welch, que ajusta los grados de libertad. En la practica: usa Welch
por defecto; es mas seguro y casi no cuesta potencia.
```

Un matiz que casi nadie aplica y que te ahorra pleitos: **significativo no es lo mismo que importante**. Con
suficientes réplicas, una diferencia de 0,2 % p/p sale "significativa" y no cambia ninguna decisión. La
pregunta correcta es la del **criterio de aceptación**: ¿la diferencia supera lo que tu especificación
tolera? Eso es una comparación con la **incertidumbre** (`76`), no con un valor p.

## Comparación honesta de dos laboratorios

| Paso | Qué se hace | Por qué |
|---|---|---|
| 1 | Enviar submuestras del **mismo material homogeneizado** (`67`) | Si el material no es homogéneo, mides variabilidad de muestreo, no de laboratorio |
| 2 | Enviar **al menos 3 submuestras a cada uno**, con códigos ciegos | Réplica única no permite estimar dispersión |
| 3 | Pedir a ambos el **método exacto y su incertidumbre expandida (U)** | Dos métodos distintos pueden dar resultados legítimamente distintos |
| 4 | Comparar con el **criterio de En** | Es el criterio estándar de comparación entre laboratorios |

```
Numero En (criterio de comparabilidad entre laboratorios, ISO 13528):

    En = (x1 - x2) / raiz( U1^2 + U2^2 )

    |En| <= 1,0  -> resultados compatibles; la diferencia se explica por
                    la incertidumbre declarada. No hay pleito.
    |En| >  1,0  -> incompatibles; alguno subestima su incertidumbre
                    o tiene un sesgo real. Ahi si se investiga.
```

Ejemplo (ILUSTRATIVO): laboratorio A reporta 27,4 % p/p con U = 2,2 % p/p (k=2); laboratorio B reporta
25,1 % p/p con U = 2,0 % p/p. En = (27,4 − 25,1) / √(2,2² + 2,0²) = 2,3 / 2,97 = **0,77**. Compatibles. No
te están robando: estás pidiéndole al método una precisión que no tiene.

## Detectar un dato atípico sin hacer trampa

| Prueba | Cuándo | Cuidado |
|---|---|---|
| **Grubbs** | Un solo sospechoso, datos aproximadamente normales, n ≥ 3 | Solo se aplica **una vez**; no se repite hasta que quede bonito |
| **Dixon Q** | n pequeño (3–10) | Poca potencia; conservadora |
| **Cochran** | Compara varianzas entre grupos (estudios colaborativos) | Detecta el laboratorio con dispersión rara |

Regla ética dura: **un atípico solo se elimina si hay causa asignable documentada** (vial roto, inyección
fallida, error de pesada anotado en el cuaderno). Eliminar por estadística sola y no reportarlo es
manipulación de datos, y en una auditoría GMP es un hallazgo grave (`169`).

## Distribuciones: por qué muchos datos de laboratorio no son normales

- **Contaminantes trazas** (metales, micotoxinas, pesticidas) suelen distribuirse **log-normal**: pocos
  valores altos jalan la media. Se trabaja con la mediana y con logaritmos.
- **Datos censurados** ("< LOQ") no se pueden promediar como cero ni como el LOQ. Enfoque aceptado: reportar
  cota inferior (todos los < LOQ = 0) y cota superior (todos = LOQ), y decir ambas. Es lo que exige el
  enfoque *lower bound / upper bound* usado en contaminantes en alimentos.
- **Conteos microbiológicos** son de Poisson y se trabajan en log10 (`100`).

## Ejemplo aplicado — ¿mi lote de melena de león bajó de potencia?

```
Lote 2026-04 (n=5 submuestras, beta-glucano % p/p base seca):  22,1  21,4  22,8  21,9  22,3
Lote 2026-07 (n=5):                                            20,3  20,9  19,8  20,6  21,1

Lote abril: x̄ = 22,10 ; s = 0,517 ; RSD = 2,3 %      (ILUSTRATIVO)
Lote julio: x̄ = 20,54 ; s = 0,502 ; RSD = 2,4 %      (ILUSTRATIVO)

t de Welch = (22,10 - 20,54) / raiz(0,517^2/5 + 0,502^2/5) = 1,56 / 0,322 = 4,84
gl ~ 8   ->   t critico 2,306   ->   p < 0,01

Conclusion: la diferencia de 1,56 % p/p es real, no ruido. Y ademas es
relevante: si tu especificacion dice ">= 21 % p/p base seca" (282), el lote
de julio NO cumple.

Siguiente pregunta (la de verdad importante): que cambio? Sustrato (239),
tiempo de secado (240), proporcion de micelio en el lote (217), o el
laboratorio corrio con enzima vencida (77)?
```

## Cuántas réplicas necesitas

```
Numero de replicas para detectar una diferencia d con potencia 80 % y alfa 5 %:

    n por grupo  ~  16 * (s/d)^2       (aproximacion rapida, dos grupos)

Con s = 0,5 % p/p y querer detectar d = 1,0 % p/p:
    n ~ 16 * (0,5/1,0)^2 = 4 por grupo.

Con querer detectar d = 0,5 % p/p:
    n ~ 16 * (0,5/0,5)^2 = 16 por grupo.   <- se dispara el costo (114)
```

Traducción de negocio: **detectar diferencias pequeñas cuesta muchas réplicas**. Antes de pagar 16 análisis,
pregúntate si una diferencia de 0,5 % p/p cambia alguna decisión tuya. Si no, no la midas.

## Errores comunes

- **Comparar dos números sin réplicas** y sacar conclusiones de proveedor. Es el error #1.
- **Promediar valores "< LOQ" como cero** y reportar un promedio bonito de metales pesados.
- **Reportar más cifras significativas que las que soporta la s** (`05`). Si s = 0,5, reportar 22,137 es
  ficción.
- **Usar R² como prueba de que la curva sirve.** R² alto convive con curvatura y con sesgo en los extremos;
  se miran los **residuales** (`71`).
- **Eliminar atípicos hasta que el lote cumpla.** Además de deshonesto, deja rastro en los datos crudos.
- **Confundir precisión con exactitud.** Cinco réplicas idénticas y todas mal es un método preciso e
  inexacto; solo un CRM o un spike lo destapa (`74`).

## Conexión con otros módulos

→ `05-cifras-significativas-e-incertidumbre.md` — cuántos dígitos puedes escribir.
→ `71-curva-de-calibracion.md` — regresión, residuales y por qué R² no basta.
→ `74-exactitud-precision-y-recuperacion.md` — de dónde salen s y el sesgo.
→ `76-incertidumbre-de-medida.md` — el número U que alimenta el criterio En.
→ `77-control-de-calidad-analitico-y-cartas-control.md` — las reglas de control son estadística aplicada.
→ `112-como-impugnar-un-resultado.md` — cómo se usa todo esto en una discusión real con el laboratorio.
→ `287-diseno-de-experimentos-doe.md` — cuando en vez de comparar dos cosas quieres optimizar varias.
