# 29 — Destilación y equilibrio líquido-vapor (separar por volatilidad, sin quemar lo que vale)

Destilar es separar aprovechando que unos componentes se van al vapor antes que otros. Es la operación que
recupera tu etanol para volver a usarlo, la que quita el agua de una decocción, y —el caso estrella— la que
convierte un extracto crudo de cannabis en un destilado de 85–95 % de cannabinoides. Entender el equilibrio
líquido-vapor te evita dos errores caros: comprar una columna de platos para algo que necesitaba una
película descendente, y creer que "destilado" es sinónimo de "puro" cuando lo que hiciste fue concentrar
también las impurezas de volatilidad parecida.

Términos: **equilibrio líquido-vapor (vapor-liquid equilibrium, VLE)** = reparto de cada componente entre
líquido y vapor a T y P dadas. **volatilidad relativa (relative volatility, α)** = cociente de facilidades
de evaporarse entre dos componentes; α cercano a 1 = separación difícil. **plato teórico (theoretical
plate)** = una etapa ideal de equilibrio; más platos = mejor separación. **reflujo (reflux)** = devolver
parte del destilado a la columna para mejorar la separación. **azeótropo (azeotrope)** = mezcla que hierve
sin cambiar de composición: la destilación simple ya no la separa. **camino libre medio (mean free path)**
= distancia que recorre una molécula de vapor antes de chocar; base de la destilación molecular.

## Los fundamentos, en tres líneas

```
Raoult (ideal):   P_i = x_i · P°_i          x_i = fracción molar en el líquido
Dalton:           y_i = P_i / P_total        y_i = fracción molar en el vapor
Volatilidad relativa:   α = (y_A/x_A) / (y_B/x_B) ≈ P°_A / P°_B   en mezclas casi ideales

α > 1,5   separación cómoda con pocos platos
α ≈ 1,1   necesitas muchos platos y reflujo alto
α = 1     azeótropo: no se separa por destilación simple
```

El azeótropo que te va a tocar es **etanol–agua a 95,6 % p/p de etanol (78,2 °C, 1 atm)**. Ahí se detiene
cualquier destilación convencional; por eso el etanol de comercio es 96 % y llegar a "absoluto" requiere
tamiz molecular o destilación azeotrópica. Si tu proceso pide etanol anhidro, ese es un costo distinto
(`145`, `187`).

## Los tipos de destilación y cuándo se usa cada uno

| Tipo | Presión típica | Qué separa | Uso en tu mundo |
|---|---|---|---|
| Simple / por lotes | 1 atm o vacío suave | Componentes con α grande | Recuperar etanol de tinturas (`145`) |
| Fraccionada (con columna) | 1 atm a vacío | α pequeño; varias fracciones | Separar terpenos entre sí (`182`) |
| Rotatoria (rotavapor) | 50–200 mbar | Solvente vs no volátil | Concentrar extractos en laboratorio y piloto (`149`) |
| Película descendente (falling film) | 20–100 mbar | Solvente vs extracto, en continuo | Escala industrial de recuperación de etanol (`187`) |
| Película raspada / de trayecto corto (short path, wiped film) | 0,001–0,1 mbar | Cannabinoides vs ceras, terpenos y pigmentos | **Destilado de cannabis** (`192`) |
| Molecular (de trayecto muy corto) | < 0,001 mbar | Igual, con menor tiempo de residencia | Aislados de mayor pureza (`192`) |
| Arrastre con vapor | 1 atm con vapor de agua | Volátiles inmiscibles con agua | Aceites esenciales; casi no se usa en cannabis (degrada) |

## Por qué los cannabinoides necesitan vacío extremo

Un cannabinoide tiene una presión de vapor del orden de 10⁻⁷ mbar a temperatura ambiente (`28`) y empieza
a degradarse térmicamente bastante antes de los 200 °C. La ecuación del negocio es: **hay que hacerlo
hervir por debajo de la temperatura a la que se destruye**. Eso solo se logra con vacío de 0,001 a
0,01 mbar y, además, con **tiempo de residencia corto**.

Ahí entra la destilación de trayecto corto: el vapor no tiene que atravesar una columna, solo salta unos
centímetros del evaporador al condensador. A esa presión, el camino libre medio de la molécula es del
orden de esa distancia, así que la molécula "vuela" directo sin chocar. Resultado: la separación deja de
depender del equilibrio clásico y pasa a depender de la velocidad de evaporación desde la superficie. Es
por eso que el equipo se llama *short path* y no "columna".

```
Secuencia industrial típica (`192`):
  Extracto crudo → winterización (quitar ceras y lípidos, `191`)
                 → descarboxilación controlada (`174`, `26`)
                 → 1ª pasada: "terpene strip" — se van terpenos y solventes residuales
                 → 2ª pasada: se recoge la fracción principal de cannabinoides (el destilado)
                 → colas: pigmentos, oligómeros, material degradado

Pureza típica alcanzable, reportada por la industria: 80–95 % de cannabinoides totales en el destilado,
según crudo de partida, número de pasadas y equipo. Verificar SIEMPRE por HPLC del destilado, no por
apariencia ni por el dato del fabricante del equipo (`198`).
```

Advertencia honesta: **destilar no separa Δ9-THC de CBD** con eficiencia razonable — sus volatilidades son
demasiado parecidas (α cercano a 1) y ambos son cannabinoides C21. Para eso se usa cromatografía
preparativa (`193`). Quien te venda un "equipo de destilación que separa THC del CBD" está vendiendo humo
o está describiendo remediación por cromatografía con otro nombre (`194`).

## Cómo se mide y se controla

| Pregunta | Método | Unidad / criterio |
|---|---|---|
| ¿Qué pureza tiene el destilado? | HPLC-UV de cannabinoides sobre el destilado | % p/p de cada cannabinoide (`198`) |
| ¿Quedaron solventes? | GC headspace, USP <467> | ppm por solvente (`87`, `201`) |
| ¿Quedaron terpenos? | GC-MS del destilado | mg/g; en destilado suelen ser < 0,5 % (`199`) |
| ¿Cuál es el vacío real? | Vacuómetro Pirani/capacitivo en la cámara, no en la bomba | mbar absolutos (`28`) |
| ¿Cuánta pérdida hubo? | Balance de masa: crudo in = destilado + colas + trampa fría | % de recuperación (`06`) |
| ¿Se degradó el producto? | CBN y Δ8-THC en el destilado vs el crudo | % p/p; CBN creciente = exceso térmico (`204`, `180`) |
| ¿La temperatura del evaporador es la real? | Termopar en la superficie calefactora, calibrado | °C, registro continuo |

Regla dura: sin **balance de masa** no sabes si tu rendimiento bajo es separación mala o pérdida física en
trampas y paredes. Y sin CBN medido antes y después no sabes si "rindió poco" en realidad significa "se
quemó".

## Ejemplo aplicado — dos pasadas de short path sobre crudo de etanol

Crudo winterizado y descarboxilado, 1,00 kg, 68 % de cannabinoides totales por HPLC **(ILUSTRATIVO)**:

```
Fracción              Masa (g)   Cannabinoides (% p/p)   CBN (% p/p)   Comentario
Crudo de entrada       1 000            68,0                 1,2       Base del balance
Pasada 1 — cabezas        62             4,1                 0,1       Terpenos y solventes
Pasada 2 — destilado     690            89,4                 2,0       Producto
Colas / residuo          208            21,5                 6,8       Degradado y pigmentos
Trampa fría + pérdidas    40              —                    —        Se pesa, no se estima

Balance de masa: 62 + 690 + 208 + 40 = 1 000 g  → cierra al 100 %
Recuperación de cannabinoides: (690 × 0,894) / (1 000 × 0,680) = 90,7 %
CBN generado: pasó de 1,2 % a 2,0 % en el destilado → hubo estrés térmico, revisar T y residencia
```

Lo que se decide con esto: 90,7 % de recuperación es un buen número, pero el CBN que subió dice que la
temperatura del evaporador o el tiempo de residencia están altos. La siguiente corrida baja 5 °C y se
vuelve a medir. Ese es el ciclo — no se ajusta por color del destilado, se ajusta por HPLC.

## Errores comunes

- Creer que "destilado" significa "puro" o "limpio". Concentra cannabinoides **y** cualquier impureza de
  volatilidad similar, incluidos algunos pesticidas (`200`).
- Suponer que la destilación elimina pesticidas o metales. Los metales se quedan en las colas, sí; varios
  pesticidas destilan con el producto. Se mide, no se supone (`88`, `102`).
- Medir el vacío en la bomba. La cámara siempre está peor.
- Saltarse la winterización: las ceras ensucian el evaporador y bajan la transferencia de calor (`191`).
- No cerrar balance de masa y reportar "rendimiento" sobre lo que se recogió, ignorando lo que quedó pegado.
- Prometer separación THC/CBD por destilación. No se puede razonablemente: α ≈ 1 (`193`, `194`).
- Aplicar destilación a extractos de hongos esperando concentrar β-glucanos. Un polisacárido no destila:
  es no volátil. Ahí la operación correcta es evaporación o liofilización (`149`, `150`).

## Conexión con otros módulos

→ `28-gases-y-presion-de-vapor.md` — la presión de vapor que hace posible todo esto.
→ `192-destilacion-de-cannabinoides.md` — el módulo dueño del proceso en cannabis.
→ `191-winterizacion-y-desceramiento.md` — el paso previo obligatorio.
→ `193-cromatografia-preparativa-y-aislados.md` — cuando la destilación ya no separa.
→ `149-concentracion-y-evaporacion.md` — evaporar cuando no hay que separar.
→ `87-solventes-residuales.md` — verificar lo que quedó.
→ `25-termodinamica-quimica.md` — el costo energético de cada kilo evaporado.
