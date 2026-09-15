# 165 — Estudios acelerados y Arrhenius (estimar vida útil sin esperar dos años)

Nadie puede esperar 24 meses para lanzar. La salida es forzar la degradación con temperatura, medir qué tan
rápido pasa, y extrapolar a la condición real usando la ecuación de **Arrhenius**. Es una herramienta poderosa
y muy mal usada: funciona cuando el mecanismo de degradación es uno solo y no cambia con la temperatura, y
falla silenciosamente cuando no. Este módulo te da la matemática, el procedimiento y —sobre todo— los límites,
para que no declares una vida útil que la realidad va a desmentir.

Términos: **Arrhenius** = relación entre la constante de velocidad de una reacción y la temperatura.
**Energía de activación (Ea)** = cuánta energía necesita la reacción; se obtiene del ajuste, no se inventa.
**Q10** = cuántas veces se acelera la degradación al subir 10 °C. **Orden de reacción** = cómo depende la
velocidad de la concentración (`26`). **ASAP (accelerated stability assessment program)** = enfoque de
estabilidad predictiva que usa una forma de Arrhenius modificada por humedad.

## La matemática, sin misterio

```
ARRHENIUS
    k = A · e^(−Ea / (R·T))

    k  = constante de velocidad de degradación
    A  = factor pre-exponencial
    Ea = energía de activación (J/mol)
    R  = 8,314 J/(mol·K)
    T  = temperatura ABSOLUTA (K = °C + 273,15)   ← el error #1 es usar °C

Forma linealizada (la que se usa en la práctica):
    ln k = ln A − (Ea/R) · (1/T)

    Graficas ln k contra 1/T. Si da una recta, el mecanismo es consistente.
    Pendiente = −Ea/R   →   Ea = −pendiente × R

CINÉTICA DE ORDEN CERO (muchos sólidos y pérdidas de potencia se ajustan bien)
    C(t) = C0 − k·t          t_vida = (C0 − C_límite) / k

CINÉTICA DE PRIMER ORDEN (frecuente en solución)
    ln C(t) = ln C0 − k·t    t_vida = ln(C0/C_límite) / k
    t½ = 0,693 / k
```

## El procedimiento completo

```
ESTUDIO ACELERADO PARA ESTIMAR VIDA ÚTIL

1. Elige AL MENOS TRES temperaturas (necesitas 3 puntos para una recta creíble).
   Ejemplo: 40 °C, 50 °C y 60 °C, todas a HR controlada.
   Ojo: no subas tanto que cambies el mecanismo (fusión, transición vítrea, Maillard nueva).

2. En cada temperatura, mide el atributo en ≥ 4 tiempos.

3. Para cada temperatura, ajusta el orden de reacción y obtén k.
   (Compara R² de orden 0 y orden 1; quédate con el mejor ajuste.)

4. Grafica ln k vs 1/T. Verifica LINEALIDAD. Si no es lineal, PARA:
   hay más de un mecanismo y Arrhenius no aplica.

5. Obtén Ea de la pendiente.

6. Extrapola k a la temperatura real de almacenamiento (ej. 30 °C = 303,15 K).

7. Calcula el tiempo hasta el límite de especificación.

8. Aplica un FACTOR DE SEGURIDAD y declara menos de lo que el modelo dice.

9. CONFIRMA con el estudio de largo plazo real (`164`): la estimación es provisional.
```

Todos estos ajustes se ejecutan en código: `lab-tools/vida_util_arrhenius.py`. Regresiones a mano o en una hoja
sin verificar es lo que este oficio no permite; si la decisión importa, verifica con `Matematicas_lushows`.

## Ejemplo numérico completo

```
Producto: aceite con un marcador termolábil.  Cifras (ILUSTRATIVAS).
Límite de especificación: 90 % del valor inicial.

Datos obtenidos (orden cero ajustó mejor, R² > 0,98 en las tres):
   T = 60 °C = 333,15 K   k = 0,420 %/día    1/T = 3,0017e-3
   T = 50 °C = 323,15 K   k = 0,168 %/día    1/T = 3,0945e-3
   T = 40 °C = 313,15 K   k = 0,062 %/día    1/T = 3,1934e-3

Regresión ln k vs 1/T:
   ln k:  −0,8675 ; −1,7838 ; −2,7806
   pendiente ≈ −9 976 K       (ajuste lineal, R² ≈ 0,9997)
   Ea = 9 976 × 8,314 ≈ 82,9 kJ/mol      ← valor plausible para degradación química

Extrapolación a 30 °C = 303,15 K   (1/T = 3,2987e-3):
   ln k(30) = ln A − 9976 × 3,2987e-3
   con ln A ≈ 29,1 (del intercepto)  →  ln k(30) ≈ −3,80  →  k(30) ≈ 0,0224 %/día

Vida útil estimada = (100 − 90) / 0,0224 ≈ 446 días ≈ 14,7 meses

Declaración prudente: 12 meses, a confirmar con el estudio real de largo plazo.
```

Ese "declarar 12 cuando el modelo dice 14,7" no es timidez: es reconocer que el modelo tiene incertidumbre y que
la etiqueta no admite errores.

## Q10: útil para conversar, malo para decidir

```
Q10 = k(T+10) / k(T)

Del ejemplo:  k(50)/k(40) = 0,168/0,062 = 2,71
              k(60)/k(50) = 0,420/0,168 = 2,50

Regla clásica: "Q10 ≈ 2–3" para degradación química.
```

Y aquí va la advertencia honesta: **el método Q10 no es preciso y, contra la creencia popular, no obedece la
ecuación de Arrhenius.** Para datos que sí siguen Arrhenius, Q10 **disminuye** a medida que sube la temperatura
—se ve arriba: 2,71 baja a 2,50—. Por eso Q10 sirve para conversar rápido ("bajar 10 °C te duplica o triplica la
vida útil") y no para sostener una fecha de vencimiento. Para eso se usa el ajuste completo.

## Cuándo Arrhenius NO aplica

Esta es la sección que salva de una vida útil falsa:

- **Más de un mecanismo.** Si a 60 °C domina la oxidación y a 30 °C domina la hidrólisis, la extrapolación es
  ficción. Se detecta porque el gráfico ln k vs 1/T **no da una recta**.
- **Cambios de estado.** Si el producto funde, se ablanda por encima de su transición vítrea o se apelmaza a
  50 °C, la temperatura alta creó una física distinta.
- **Degradación gobernada por humedad.** Muchos suplementos se degradan por agua, no por calor. Ahí hay que
  modelar T **y** HR juntos. El enfoque ASAP usa precisamente una forma de Arrhenius **modificada por humedad**.
- **Crecimiento microbiano** y **cambios físicos** (separación de emulsión, sedimentación, crecimiento de gota):
  no son cinética química, se observan y no se extrapolan con Ea.
- **Sistemas complejos.** El propio campo de ciencia de alimentos advierte que la vida útil acelerada es
  confiable solo para sistemas relativamente simples y con mecanismo conocido.

Caso concreto: la coenzima Q10 de fuente natural puede tener vida útil muy corta —del orden de meses— por
oxidación a temperatura ambiente, y las estimaciones aceleradas no siempre predicen bien lo que pasa en
anaquel. Recordatorio de que el modelo no reemplaza el dato real.

## Cómo se comprueba la estimación

| Chequeo | Qué buscar | Si falla |
|---|---|---|
| Linealidad de ln k vs 1/T | R² alto con 3+ temperaturas | Múltiples mecanismos → no extrapolar |
| Ea plausible | Típicamente 40–130 kJ/mol para degradación química | Fuera de rango: revisa el ajuste |
| Aspecto en la condición alta | Que el producto siga siendo el mismo físicamente | Cambio de estado → descartar esa T |
| Concordancia con largo plazo a 6 y 12 meses | Que el dato real caiga cerca de lo predicho | Recalcular y corregir la fecha (`169`) |
| Balance de masa del cromatograma | Que lo que se pierde aparezca como degradado | Si no aparece: sorción al envase (`163`) |

## Ejemplo aplicado — qué esperar en un extracto de hongos

Los β-glucanos son polímeros térmicamente robustos: en un estudio acelerado el contenido casi no se mueve, y lo
que reprueba es la **humedad, el aspecto y la microbiología** (`164`). Consecuencia práctica: en un polvo de
hongos, Arrhenius sobre el activo da una vida útil enorme y engañosa, porque el limitante no es el activo.

**La regla que se deriva:** modela con Arrhenius el atributo que **de verdad limita**, no el que te conviene. Si
lo que reprueba es la ganancia de humedad, el modelo correcto es el de permeación del envase (`163`), no el de
cinética química.

## Errores comunes

- Usar °C en vez de kelvin en la ecuación. Da resultados absurdos que a veces parecen razonables.
- Extrapolar con una sola temperatura acelerada. Sin 3 puntos no hay recta, y sin recta no hay Ea.
- Aplicar Arrhenius a degradación microbiana, a separación física, o ignorar la humedad en higroscópicos.
- Subir la temperatura tanto que el producto cambia de estado y creer que el resultado sigue siendo válido.
- Declarar directamente el número del modelo sin factor de seguridad ni confirmación real.
- Usar Q10 como si fuera un método riguroso de estimación de vida útil.
- No confirmar la estimación con el estudio de largo plazo y dejar la fecha provisional para siempre.

## Conexión con otros módulos

→ `164-estabilidad-ich-q1-y-vida-util.md` — el estudio real que esta estimación anticipa y que la confirma.
→ `26-cinetica-de-reaccion.md` — orden de reacción y constantes de velocidad.
→ `163-envase-primario-y-compatibilidad.md` — cuando el limitante es la permeación, no la química.
→ `78-estadistica-para-el-laboratorio.md` — regresión, R² e incertidumbre del ajuste.
→ `294-informe-tecnico-y-pdf.md` — cómo se presenta el racional de vida útil en el expediente.