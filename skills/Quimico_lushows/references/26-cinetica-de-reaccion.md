# 26 — Cinética de reacción (cuánto tiempo y a qué temperatura, sin quemar el lote)

La cinética es la disciplina que convierte "hornea hasta que esté listo" en un número defendible. Es lo que
te permite decir: *a 115 °C, el 95 % del THCA está convertido a los 45 min, y a partir del minuto 70 estoy
perdiendo THC como CBN más rápido de lo que gano*. Es también lo que explica por qué un polvo con
psilocibina guardado en un armario pierde potencia sin que nada visible pase. Dos reacciones compiten casi
siempre: la que quieres y la que te destruye el producto. Sin cinética estás adivinando cuál va ganando.

Términos: **velocidad de reacción (reaction rate)** = cambio de concentración por unidad de tiempo, en
mol/(L·s) o %/min. **orden de reacción (reaction order)** = cómo depende la velocidad de la concentración;
orden 0, 1 o 2. **constante de velocidad (rate constant, k)** = el factor de proporcionalidad; sus unidades
dependen del orden. **energía de activación (activation energy, Ea)** = barrera energética, en kJ/mol.
**vida media (half-life, t½)** = tiempo en que queda la mitad. **Q10** = factor por el cual se multiplica la
velocidad al subir 10 °C.

## Las leyes que vas a usar

```
Orden 0:  [A] = [A]0 − k·t                 k en mol/(L·s) o %/min      t½ = [A]0 / (2k)
Orden 1:  ln([A]/[A]0) = −k·t              k en 1/s o 1/min            t½ = ln 2 / k = 0,693 / k
Orden 2:  1/[A] − 1/[A]0 = k·t             k en L/(mol·s)              t½ = 1 / (k·[A]0)

Arrhenius:  k = A · e^(−Ea / (R·T))        T en kelvin, R = 8,314 J/(mol·K)
            ln k = ln A − (Ea/R)·(1/T)     → graficar ln k vs 1/T da una recta de pendiente −Ea/R

Q10 = k(T+10) / k(T)   ≈ 2–3 para muchas degradaciones en alimentos
```

La mayoría de degradaciones de activos en producto terminado se ajustan bien a **orden 1** (la velocidad
es proporcional a lo que queda). Eso es una bendición práctica: con un t½ tienes toda la curva, y con dos
temperaturas tienes Ea y puedes extrapolar (`165`).

## Cómo se determina el orden, en la vida real

| Paso | Qué se hace | Criterio |
|---|---|---|
| 1 | Muestreo en al menos 6 tiempos, por triplicado | Cubrir hasta 50–70 % de conversión |
| 2 | Cuantificar por método validado (HPLC-UV, LC-MS/MS) | Con estándar interno (`72`) |
| 3 | Graficar [A] vs t, ln[A] vs t, 1/[A] vs t | El que da recta define el orden |
| 4 | Sacar k de la pendiente, con su intervalo de confianza | R² ≥ 0,98 y residuos sin patrón (`78`) |
| 5 | Repetir a 3 temperaturas y armar el Arrhenius | Ea en kJ/mol con incertidumbre (`76`) |

Regla dura: un solo punto no es cinética. "Después de 30 min quedaba 80 %" no permite predecir nada; con
la curva completa sí.

## Caso 1 — Descarboxilación del THCA: la reacción que sí quieres

El THCA pierde CO₂ y se convierte en Δ9-THC. La reacción se describe bien como **pseudo-primer orden** en
THCA, y en paralelo corre la degradación oxidativa Δ9-THC → CBN, también de primer orden pero más lenta.
Dos reacciones consecutivas: hay un **máximo** de THC y pasarlo es perder producto.

```
Esquema:   THCA  --k1-->  Δ9-THC  --k2-->  CBN  (+ otras vías)
Con k1 >> k2, el THC pasa por un máximo en:   t_max = ln(k1/k2) / (k1 − k2)

Valores de Ea reportados en la literatura para descarboxilación de THCA: del orden de 80–120 kJ/mol
(varía mucho con matriz, humedad y si es flor, extracto o aislado — MÍDELO en tu material).
```

Lo que esto significa operativamente: la temperatura tiene efecto exponencial y el tiempo solo lineal. Subir
10 °C puede acortar el proceso a la mitad o menos; alargar el tiempo al doble no compensa 10 °C menos y sí
suma degradación. El cálculo puntual con tu k se ejecuta en `lab-tools/decarboxilacion.py`, nunca de
memoria, y el módulo dueño del tema con los factores másicos es `174`.

Además, la descarboxilación de la **flor** y la del **extracto** no son la misma cinética: cambia la
transferencia de calor, la humedad y la superficie expuesta. Un protocolo de horno no se traslada a un
reactor sin volver a levantar la curva (`166`).

## Caso 2 — Degradación de la psilocibina: la reacción que no quieres

La psilocibina se desfosforila a psilocina, y la psilocina —que tiene el fenol libre en C4— se oxida rápido
a productos coloreados. En la práctica del análisis y del almacenamiento se comporta como **primer orden**
en cada etapa, y la velocidad sube con temperatura, con oxígeno, con luz y con pH alcalino (`22`).

```
Esquema:   Psilocibina  --k1-->  Psilocina  --k2-->  oxidación (productos azules/oscuros)

Consecuencia analítica: si mides solo psilocibina, subestimas; si mides solo psilocina, te confundes.
Se cuantifican AMBAS y se reporta la suma molar como "psilocibina equivalente" (`256`).

Consecuencia de custodia: material seco, oscuro, frío y sin oxígeno; extracto analítico procesado el
mismo día o congelado a −20 °C protegido de la luz (`109`, `255`).
```

Este es el ejemplo perfecto de por qué la cinética importa para la **integridad del dato**: si tu muestra
se degrada entre la recolección y la inyección, el resultado que reportas no es el del material — es el de
tu logística. El módulo dueño de la estabilidad de psilocibios es `255`, y el analítico es `256`.

## Cómo se mide

| Pregunta | Método | Unidad |
|---|---|---|
| ¿Cuál es k a esta temperatura? | Serie temporal + regresión del modelo del orden correcto | 1/min o 1/día |
| ¿Cuál es Ea? | k a 3 o más temperaturas + gráfico de Arrhenius | kJ/mol (`165`) |
| ¿Cuánta vida útil tengo? | t½ y extrapolación desde estudio acelerado, confirmada en tiempo real | meses a T declarada (`164`) |
| ¿Se degrada durante la preparación de muestra? | Blanco enriquecido (spike) procesado como muestra | % de recuperación (`74`) |
| ¿Cuál es el punto óptimo de descarboxilación? | Curva de THCA, THC y CBN por HPLC en el tiempo | % p/p b.s. vs min (`198`) |
| ¿El balance cierra? | Suma molar de precursor + producto + degradado | % del inicial (`06`) |

## Ejemplo aplicado — encontrar el punto de horneado que no quema el lote

Extracto crudo de cannabis, descarboxilación a 120 °C, muestreo por HPLC-UV **(ILUSTRATIVO)**:

```
t (min)   THCA (% p/p)   Δ9-THC (% p/p)   CBN (% p/p)   THC total teórico conservado
   0         62,0             3,1            0,2                 100 %
  15         28,4            32,6            0,4                  99 %
  30          9,1            50,0            0,9                  98 %
  45          2,6            56,0            1,6                  97 %
  60          0,8            57,2            2,9                  96 %
  90          0,2            55,1            5,4                  93 %
 120          0,1            51,8            9,0                  90 %

THC total = Δ9-THC + THCA × 0,877  (`175`)
```

Decisión: el máximo real de Δ9-THC está entre 55 y 65 min; a los 90 min la conversión ya está completa
pero ya perdiste 3 puntos porcentuales por CBN, y a los 120 min perdiste 6. El punto de corte industrial
razonable es **55–60 min a 120 °C** con verificación de THCA residual < 1 % p/p. Nótese que la fila de
"THC total conservado" es el balance de masa que valida que la pérdida sea real y no un error de método.

## Errores comunes

- Confundir termodinámica con cinética: "debería reaccionar" no es "va a reaccionar hoy" (`25`).
- Fijar un tiempo de horneado copiado de internet, sin curva propia. Cada matriz y cada equipo cambian k.
- Alargar el tiempo en vez de subir la temperatura (o al revés) sin mirar la reacción competidora.
- Extrapolar Arrhenius fuera del rango medido o a través de un cambio de fase (si el material se funde,
  el mecanismo cambia y la recta ya no aplica) (`165`).
- No cerrar balance de masa. Si el precursor bajó 20 puntos y el producto solo subió 12, algo se está
  yendo por una vía que no estás midiendo (`06`).
- Guardar la muestra "un par de días" antes de inyectar en analitos lábiles. Estás midiendo tu bodega.
- Reportar un t½ sin decir la temperatura, la matriz y el envase. Un t½ solo no significa nada.

## Conexión con otros módulos

→ `174-descarboxilacion-cinetica-y-calculo.md` — el módulo dueño, con factores y calculadora.
→ `255-estabilidad-y-degradacion-de-psilocibina.md` — el módulo dueño de la estabilidad de psilocibios.
→ `25-termodinamica-quimica.md` — qué puede pasar, frente a qué tan rápido pasa.
→ `165-estudios-acelerados-y-arrhenius.md` — cómo se usa Ea para predecir vida útil.
→ `27-catalisis-y-enzimas.md` — cómo se baja Ea a propósito.
→ `204-estabilidad-y-degradacion-del-thc.md` — la ruta THC → CBN en detalle.
→ `116-enzimas-y-cinetica-de-michaelis-menten.md` — cinética cuando hay un catalizador biológico.
