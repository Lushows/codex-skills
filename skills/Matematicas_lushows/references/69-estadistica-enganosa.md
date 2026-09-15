# 69 · Estadística engañosa

> **Qué resuelve / cuándo usarlo** — Detectar y desarmar números que mienten sin mentir: gráficos con ejes truncados, promedios que esconden la realidad, datos elegidos a dedo (cherry-picking), porcentajes sin base y correlaciones disfrazadas de causa. Úsalo cada vez que alguien te presente una cifra "impactante" antes de tomar una decisión con dinero.

## Concepto (para no-experto)

La estadística engañosa no suele usar números falsos: usa números **verdaderos presentados de forma tramposa**. Es la diferencia entre mentir y "decir media verdad". Cada técnica que veremos es técnicamente correcta pero te empuja a una conclusión equivocada.

Definamos los términos que vamos a usar:

- **Eje truncado**: en un gráfico, el eje vertical (el de los valores, "eje Y") normalmente empieza en cero. **Truncar** significa empezarlo en otro número (ej. en 95 en vez de 0) para que una diferencia minúscula se vea como una montaña. Analogía: dos personas miden 1.80 m y 1.82 m; si te tapo desde los pies hasta el cuello y solo te muestro la cabeza, parece que una es el doble de alta.
- **Promedio (media aritmética)**: sumar todos los valores y dividir entre cuántos hay. Es engañoso cuando hay valores extremos (**outliers**, datos muy alejados del resto).
- **Mediana**: el valor que queda justo en el medio cuando ordenas los datos de menor a mayor. La mitad está por debajo, la mitad por encima. Resiste a los outliers.
- **Cherry-picking** ("recoger solo las cerezas buenas"): mostrar solo los datos que apoyan tu mensaje y esconder el resto.
- **Porcentaje sin base**: decir "subió 50%" sin decir 50% **de qué**. 50% de 2 ventas son 3 ventas; suena enorme, es ridículo.
- **Correlación**: dos cosas que se mueven juntas. **Causalidad**: una causa la otra. Que se muevan juntas NO prueba que una cause la otra (módulo 63).

Analogía cotidiana del restaurante: un proveedor te dice "nuestros clientes aumentaron sus ventas 200%". Suena espectacular. Pero ¿el promedio de cuántos clientes? ¿Eligieron solo los 3 que mejor les fue? ¿200% sobre una base de cuánto? Tu trabajo es preguntar esas tres cosas **antes** de firmar.

## Fórmulas / método

Las herramientas para desenmascarar cada truco:

**1. Eje truncado — factor de exageración visual.** Si un gráfico de barras tiene el eje Y desde `eje_min` hasta `eje_max`, y comparas dos valores `a` y `b`:

```
razón_real    = b / a
razón_visual  = (b - eje_min) / (a - eje_min)
factor_exageración = razón_visual / razón_real
```

Con `eje_min = 0` el factor es 1 (honesto). Cuanto más alto `eje_min`, mayor el engaño.

**2. Promedio vs mediana.** Para datos `x₁,…,xₙ`:

```
media    = (Σ xᵢ) / n
mediana  = valor central (n impar) o promedio de los dos centrales (n par)
sesgo    = media − mediana
```

Si `media` ≫ `mediana`, hay outliers altos tirando del promedio. Pide la mediana.

**3. Porcentaje con su base.** Un porcentaje **siempre** necesita el número absoluto:

```
cambio_% = (valor_nuevo − valor_viejo) / valor_viejo × 100
absoluto = valor_nuevo − valor_viejo
```

Reporta SIEMPRE los dos. Unidad del porcentaje: adimensional (%); del absoluto: las unidades reales (ventas, COP, clientes).

**4. Correlación ≠ causa.** El coeficiente de correlación `r` (entre −1 y +1) mide cuán juntas se mueven dos variables, pero NO si una causa la otra. Sospecha de **variable de confusión** (`z`): una tercera causa que mueve a ambas. Ver módulo 63.

## Verificación en código

```python
from decimal import Decimal, getcontext
from statistics import mean, median
import numpy as np

getcontext().prec = 28  # alta precisión para dinero

# ---------- 1) EJE TRUNCADO: cuánto exagera un gráfico ----------
def factor_exageracion(a, b, eje_min):
    razon_real   = b / a
    razon_visual = (b - eje_min) / (a - eje_min)
    return razon_visual / razon_real

# Ventas mes pasado vs este mes: 102 vs 108 unidades
a, b = 102.0, 108.0
print("Eje desde 0   -> factor:", round(factor_exageracion(a, b, 0), 3))
print("Eje desde 100 -> factor:", round(factor_exageracion(a, b, 100), 3))

# ---------- 2) PROMEDIO ENGAÑOSO vs MEDIANA ----------
# Ticket de 10 mesas; una mesa es un evento corporativo gigante (outlier)
tickets = [18, 22, 25, 19, 30, 21, 24, 23, 20, 480]  # miles de COP
print("\nMedia  :", round(mean(tickets), 2), "(mil COP)")
print("Mediana:", round(median(tickets), 2), "(mil COP)")
print("Sesgo  :", round(mean(tickets) - median(tickets), 2))

# ---------- 3) PORCENTAJE SIN BASE (dinero con decimal) ----------
viejo = Decimal("2")   # 2 ventas
nuevo = Decimal("3")   # 3 ventas
cambio_pct = (nuevo - viejo) / viejo * Decimal("100")
print("\nCambio %:", cambio_pct, "%  | en absoluto:", nuevo - viejo, "ventas")

# ---------- 4) CORRELACIÓN FALSA (confusión por una 3a variable) ----------
np.random.seed(7)
calor = np.random.uniform(20, 35, 200)          # variable de confusión: temperatura
helados   = 5*calor + np.random.normal(0, 3, 200)   # el calor sube helados
ahogados  = 0.4*calor + np.random.normal(0, 1, 200) # el calor sube baños -> ahogados
r = np.corrcoef(helados, ahogados)[0, 1]
print("\nCorrelación helados~ahogados:", round(r, 3), "(¡pero NO causa!)")
```

```python
# ---------- VERIFICACIÓN POR SEGUNDA VÍA ----------
# (a) Eje truncado: recomputar a mano y comprobar con assert
#     razon_real = 108/102 = 1.0588 ; razon_visual(100) = 8/2 = 4 ; factor = 4/1.0588
assert abs(factor_exageracion(102.0,108.0,100) - (4/(108/102))) < 1e-9
assert abs(factor_exageracion(102.0,108.0,0) - 1.0) < 1e-12  # eje en 0 = honesto

# (b) Mediana por definición: ordenar y tomar promedio de los 2 centrales (n=10)
ordenado = sorted([18,22,25,19,30,21,24,23,20,480])
m = (ordenado[4] + ordenado[5]) / 2
assert m == median([18,22,25,19,30,21,24,23,20,480])  # 22.5

# (c) Porcentaje: la inversa debe devolver el valor nuevo
viejo, nuevo = Decimal("2"), Decimal("3")
pct = (nuevo - viejo)/viejo*Decimal("100")
reconstruido = viejo * (Decimal("1") + pct/Decimal("100"))
assert reconstruido == nuevo  # 2 * 1.5 = 3

# (d) Correlación falsa: al CONTROLAR el calor, la correlación residual ~ 0
#     (correlación parcial: quitamos el efecto del calor de ambas series)
import numpy as np
np.random.seed(7)
calor = np.random.uniform(20,35,200)
helados  = 5*calor + np.random.normal(0,3,200)
ahogados = 0.4*calor + np.random.normal(0,1,200)
def residual(y, x):
    b = np.polyfit(x, y, 1)
    return y - (b[0]*x + b[1])
r_parcial = np.corrcoef(residual(helados, calor), residual(ahogados, calor))[0,1]
assert abs(r_parcial) < 0.2   # sin el calor, casi no hay relación
print("Correlación parcial (controlando calor):", round(r_parcial, 3))
print("OK: todas las verificaciones pasaron")
```

Salida esperada (cifras clave): factor con eje en 100 ≈ **3.78×** de exageración; media tickets **68.2** vs mediana **22.5** (mil COP); cambio "50%" = **1 venta**; correlación falsa ≈ **0.9** que cae a ≈ **0** al controlar el calor.

## Ejemplo trabajado

**Situación (GastroLatam, junio 2026).** Un proveedor de delivery te muestra una diapositiva: *"Restaurantes en nuestra plataforma vendieron en promedio 68 mil COP por ticket — ¡40% más que el sector!"* y un gráfico de barras donde su barra parece el doble de alta que la competencia.

Paso 1 — **¿Promedio o mediana?** Pides los 10 tickets reales: nueve entre 18 y 30 mil, y uno corporativo de 480 mil.
- Media = **68.2 mil COP** (verificado en código).
- Mediana = **22.5 mil COP** (verificado).
- Sesgo = 68.2 − 22.5 = **45.7 mil COP**. El "promedio" está inflado por UN evento. El restaurante típico factura ~22.5 mil, no 68.

Paso 2 — **El gráfico.** Su barra usa eje Y desde 100 (truncado). Valores reales 102 vs 108. Factor de exageración con eje en 100 = **3.78×**: una diferencia real del 5.9% se ve casi 4 veces mayor. Pides el mismo gráfico con eje desde 0 → las barras quedan casi iguales.

Paso 3 — **El "40% más".** 40% sobre qué base. Si el sector vende 22 mil de mediana, 40% son **8.8 mil COP** por ticket. Útil saberlo en absoluto, no solo el porcentaje brillante.

**Conclusión con unidades:** el ticket típico real es **22.5 mil COP/ticket**, no 68.2 mil; la ventaja visual del gráfico es un artefacto del eje truncado (3.78× de exageración). Decisión: negociar la comisión usando la mediana, no caer en el promedio inflado.

## Errores comunes / trampas

- **Citar el promedio cuando hay outliers.** Sueldos, tickets, ingresos casi siempre están sesgados a la derecha: usa **mediana** (módulo 60).
- **Aceptar un porcentaje sin su número absoluto.** "+300%" puede ser +3 ventas. Pide siempre el valor base y el cambio absoluto (módulo 14).
- **Creer un gráfico sin mirar el origen del eje.** Si el eje Y no empieza en 0 en barras, sospecha. (En líneas a veces se justifica, pero exige verlo.)
- **Confundir correlación con causa.** Antes de actuar, busca la **variable de confusión** y, si puedes, controla por ella (correlación parcial) o haz un experimento (módulos 63, 68).
- **Cherry-picking temporal.** "Crecimos desde el mínimo de enero" elige a propósito el punto más bajo. Mira la serie completa, no el tramo conveniente.
- **Base que cambia.** Comparar % calculados sobre denominadores distintos (clientes vs sesiones vs pedidos) y sumarlos como si fueran lo mismo (módulo 89).
- **Dinero en float.** Para cualquier cifra monetaria usa `decimal`, nunca `float` (módulo 12).

### Mini-checklist de exactitud
- [ ] ¿Me dieron **mediana además del promedio** y el número de datos `n`?
- [ ] ¿Todo porcentaje viene con su **base y su valor absoluto**, y el eje del gráfico **empieza en 0**?
- [ ] ¿La relación entre dos variables se sostiene al **controlar la posible causa común** (no es solo correlación)?

## Cruces
- [[63-correlacion-vs-causalidad]] — el corazón del truco "correlación disfrazada de causa".
- [[60-estadistica-descriptiva]] — media, mediana y cuándo cada una miente o dice la verdad.
- [[14-porcentajes-sin-errores]] — porcentajes con base, puntos vs por ciento, cambios encadenados.
- [[62-distribucion-de-datos-y-visualizacion]] — cómo se construye (y se manipula) un gráfico honesto.
- [[98-presentar-numeros-sin-enganar]] — el lado constructivo: comunicar tus propios números sin caer en estas trampas.
