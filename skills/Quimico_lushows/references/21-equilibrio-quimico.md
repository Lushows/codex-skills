# 21 — Equilibrio químico (por qué una extracción se "cansa" y una reacción no termina)

El equilibrio explica por qué tu segunda extracción rinde menos que la primera aunque uses el mismo
solvente, por qué el THCA nunca se convierte 100 % a THC en la práctica, y por qué un ácido débil como el
CBDA está mitad ionizado y mitad neutro según el pH. Es el concepto que separa "esto no funcionó" de "esto
llegó a su límite termodinámico y hay que cambiar la condición, no insistir". Confundir cinética (qué tan
rápido) con equilibrio (hasta dónde) es el error conceptual más caro del desarrollo de procesos.

Términos: **equilibrio (equilibrium)** = estado donde las velocidades directa e inversa se igualan y las
concentraciones dejan de cambiar. **constante de equilibrio (K)** = relación de productos sobre reactivos
en el equilibrio, adimensional o con unidades según la reacción. **principio de Le Châtelier** = si
perturbas un sistema en equilibrio, se desplaza para contrarrestar la perturbación. **actividad
(activity)** = concentración "efectiva", corregida por interacciones; en soluciones diluidas ≈
concentración. **cociente de reacción (Q)** = misma expresión que K pero fuera del equilibrio; Q<K avanza
hacia productos.

## La expresión, sin misterio

Para `aA + bB ⇌ cC + dD`:

```
K = ( [C]^c · [D]^d ) / ( [A]^a · [B]^b )      concentraciones en el equilibrio, en mol/L

K >> 1   la reacción "va" casi hasta el final
K ≈ 1    mezcla apreciable de ambos lados
K << 1   apenas avanza; no insistas sin cambiar condiciones

ΔG° = −R·T·ln K       R = 8,314 J/(mol·K), T en K
```

Esa última línea es la bisagra con la termodinámica (`25`): K no es un número mágico, sale de la
diferencia de energía libre entre productos y reactivos.

## Los equilibrios que te tocan en el oficio

| Equilibrio | Forma | Dónde lo vives |
|---|---|---|
| Ácido–base | HA ⇌ H⁺ + A⁻ | THCA/CBDA ionizados según pH; psilocibina zwitteriónica (`22`) |
| Reparto entre fases | Soluto(agua) ⇌ Soluto(aceite) | Extracción líquido-líquido, logP (`30`) |
| Disolución | Sólido ⇌ Soluto(disuelto) | Saturación de una extracción (`19`) |
| Líquido–vapor | Líquido ⇌ Vapor | Presión de vapor, destilación (`28`, `29`) |
| Complejación | M + L ⇌ ML | Cd unido a tioles del hongo; ciclodextrinas (`158`) |
| Adsorción | Soluto ⇌ Soluto adsorbido | Toda la cromatografía (`31`) |
| Isomerización | Δ9-THC ⇌ Δ8-THC (ácido) | Conversión no deseada en aceites ácidos (`180`) |

Fíjate: solo dos de esos son "reacciones químicas" en el sentido escolar. La mayoría de tus equilibrios son
**físicos** — reparto, disolución, adsorción. Ahí es donde está el dinero.

## Le Châtelier aplicado a extracción: por qué la multietapa gana

Cuando extraes, el soluto se reparte entre la biomasa y el solvente hasta que Q = K. Sacar el solvente
cargado y poner solvente fresco baja Q por debajo de K y el sistema vuelve a extraer.

```
Modelo simple, coeficiente de reparto K = 4 entre solvente y sólido, 1:10, activo inicial 100 mg  (ILUSTRATIVO)

1 etapa con 200 mL   → recupera ~80 mg  (80 %)
2 etapas de 100 mL   → 1ª: 67 mg ; 2ª sobre los 33 restantes: 22 mg → total 89 mg (89 %)
3 etapas de 67 mL    → total ~92 mg (92 %)
```

Mismo volumen total de solvente, más recuperación. Esa es toda la justificación industrial de la
extracción multietapa y a contracorriente. El cálculo exacto se hace en código, no de memoria
(`Matematicas_lushows`).

## Descarboxilación: un caso donde el equilibrio casi no manda

`THCA → Δ9-THC + CO2↑`. Como el CO2 escapa del sistema, el producto se retira permanentemente y la
reacción se vuelve prácticamente irreversible: K efectivo enorme. Por eso el límite de la descarboxilación
**no es termodinámico sino cinético y de degradación**: no llegas al 100 % porque el THC formado empieza a
convertirse en CBN antes de que el último THCA reaccione (`26`, `174`, `204`). Confundir esto lleva a
"hornear más tiempo" y a perder potencia.

## Cómo se comprueba

| Pregunta | Método | Unidad |
|---|---|---|
| ¿Llegué al equilibrio de extracción? | Curva de rendimiento vs tiempo hasta plateau | mg/g biomasa vs min |
| ¿Cuánto queda en el sólido agotado? | Extracción exhaustiva del residuo (Soxhlet o 3 etapas) + HPLC | % de balance de masa (`06`) |
| ¿Cuál es K de reparto? | Shake-flask: cuantificar en ambas fases | K adimensional (`30`) |
| ¿En qué forma está mi ácido débil? | pH del medio vs pKa; ecuación de Henderson-Hasselbalch | Fracción ionizada (`22`) |
| ¿Se está isomerizando el producto? | HPLC con resolución Δ8/Δ9 seguido en el tiempo | % de área relativa (`180`) |

Regla dura: sin **balance de masa** (lo que entró = lo extraído + lo que quedó en el sólido + pérdidas) no
sabes si tu proceso llegó al equilibrio o si simplemente perdiste producto en el filtro.

## Ejemplo aplicado

Proceso de reishi con agua 95 °C, 1:20, muestreo en el tiempo **(ILUSTRATIVO)**:

```
Tiempo (min)   β-glucano extraído (mg/g biomasa b.s.)
   15                 68
   30                112
   60                148
  120                161
  240                164
Contenido total en biomasa (K-YBGL sobre biomasa molida): 268 mg/g
```

Interpretación: a los 120 min ya estás en el plateau (61 % de recuperación). Las 2 h siguientes aportan
3 mg/g y cuestan gas. Si quieres pasar del 61 %, el camino no es más tiempo — es **segunda etapa con agua
fresca**, o pretratamiento (ultrasonido/enzimas) que libere más glucano de la pared (`147`). Ese es el
razonamiento de equilibrio aplicado a una decisión de planta.

## Errores comunes

- Alargar el tiempo cuando el sistema ya está en equilibrio. Gastas energía y degradas activo.
- No medir el residuo. Si no sabes cuánto quedó en el sólido, no puedes decir si el proceso es eficiente.
- Creer que la descarboxilación "se detiene sola" en el punto óptimo. No: el THC sigue degradando (`204`).
- Ignorar el pH en extracciones de compuestos ionizables. Un cambio de 2 unidades de pH puede mover la
  solubilidad de un ácido débil un orden de magnitud (`22`).
- Escalar sin repetir la curva. El equilibrio es el mismo, pero el tiempo para llegar cambia con la
  geometría y la agitación (`166`).
- Reportar "rendimiento" sin decir sobre qué base. Rendimiento de masa, de activo y recuperación son tres
  números distintos (`151`).

## Conexión con otros módulos

→ `22-acidos-bases-y-ph.md` — el equilibrio más importante de todos.
→ `25-termodinamica-quimica.md` — de dónde sale K.
→ `26-cinetica-de-reaccion.md` — qué tan rápido se llega, y qué se degrada en el camino.
→ `30-extraccion-liquido-liquido-y-logp.md` — el equilibrio de reparto, con números.
→ `06-estequiometria-y-balance-de-masa.md` — el balance que valida tu proceso.
→ `174-descarboxilacion-cinetica-y-calculo.md` — el caso donde el CO2 rompe el equilibrio.
