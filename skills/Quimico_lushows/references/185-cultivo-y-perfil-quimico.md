# 185 — Cultivo y perfil químico: qué mueve de verdad los números de tu COA

La genética fija el quimiotipo; el cultivo fija los números. Entre dos ciclos de la misma variedad puede
haber 5 puntos de diferencia en cannabinoides totales y un perfil de terpenos irreconocible. Para un químico
esto no es agronomía ajena: es la **fuente de variabilidad** que después tienes que absorber en tu
especificación, en tu formulación y en tu cumplimiento. Este módulo separa lo que sí mueve el perfil químico
de lo que es folclore de cultivador, y te dice cómo demostrarlo con datos en vez de con anécdotas.

Términos:
- **fotoperiodo (photoperiod)** = horas de luz; dispara la floración en variedades fotodependientes.
- **DLI (daily light integral)** = luz total recibida por día, en `mol·m⁻²·día⁻¹`.
- **VPD (vapor pressure deficit)** = déficit de presión de vapor; gobierna la transpiración, en `kPa`.
- **estrés abiótico (abiotic stress)** = estrés no biológico: sequía, luz UV, temperatura, salinidad.
- **madurez de tricomas (trichome maturity)** = criterio visual (transparente/lechoso/ámbar) de cosecha.

## Lo que sí mueve el perfil, con qué peso

| Factor | Efecto sobre cannabinoides | Efecto sobre terpenos | Fuerza de la evidencia |
|---|---|---|---|
| **Genética / quimiotipo** | Define la relación THC:CBD | Define el perfil dominante | Muy sólida (`170`, `171`) |
| **Momento de cosecha** | Sube el total hasta un máximo, luego degrada | Cambia el perfil: pierde monoterpenos | Sólida |
| **DLI / intensidad de luz** | Correlación positiva con cannabinoides totales hasta saturación | Aumenta terpenos totales | Buena, con estudios controlados en interior |
| **Densidad de tricomas (genética + ambiente)** | Directa | Directa | Sólida |
| **Nutrición (N, P, K, S, Mg)** | Efecto claro en biomasa; efecto en % de cannabinoide más discutido | Variable | Media |
| **Temperatura y VPD** | Indirecto vía fisiología | Directo: pérdida de volátiles con calor | Media |
| **UV-B suplementario** | Hipótesis clásica de aumento de THC; los estudios controlados recientes son **inconsistentes** | Variable | **Débil** |
| **Sustrato / suelo vs hidroponía** | Poco efecto directo en el perfil | Discutido | Débil |
| **"Curar con azúcares / melaza"** | Ninguno demostrado | Ninguno demostrado | **Nula** |

Ese último grupo importa: mucho de lo que se vende como "potenciador de resina" no tiene ensayo controlado
detrás. Cuando alguien te afirme un efecto, pídele el diseño experimental (`287`).

## El factor que más cuesta ignorar: la fecha de cosecha

A medida que la flor madura, los cannabinoides totales suben, llegan a una meseta y luego el THC empieza a
oxidarse a CBN (`204`) mientras los monoterpenos se evaporan. Simultáneamente sube el THC total en términos
absolutos, lo cual es un **problema de cumplimiento** para cáñamo (ver la aritmética en `171`).

Práctica correcta: **muestreo seriado antes de cosechar.** Se toman muestras representativas cada 5–7 días
en la última fase, se analizan por HPLC y se decide con el dato, no con la lupa. El criterio visual de
tricomas ámbar es útil como apoyo, pero no mide THC total ni te defiende ante un regulador.

## Variables que hay que registrar para poder explicar tu COA

Sin bitácora, cada análisis es una sorpresa. Mínimo por lote de cultivo:

```
Genética / origen del material   |  fecha de trasplante  |  fotoperiodo y DLI acumulado
Fertilización (receta, EC, pH)   |  T° y HR promedio/máx |  VPD promedio
Riego (volumen, frecuencia)      |  tratamientos fitosanitarios aplicados y fecha
Fecha de cosecha                 |  peso fresco y peso seco  |  método de secado (ver 186)
```

Esa bitácora es lo que convierte un resultado analítico en conocimiento reproducible, y es además requisito
de trazabilidad en cualquier esquema GMP o de exportación (`168`, `285`).

## Cómo se mide / cómo se comprueba

- **Muestreo representativo**, que es donde se gana o se pierde el estudio: muestras compuestas de N plantas
  y N posiciones de la planta (apical, medio, bajo), no "una cola bonita" (`66`).
- **Potencia por HPLC-DAD**, `% p/p base seca`, con humedad medida en la misma muestra (`198`, `07`).
- **Terpenos por GC-MS/headspace**, `mg/g`, muestra manipulada en frío (`199`).
- **Diseño para comparar tratamientos:** replicación real (no "una carpa contra otra"), aleatorización,
  control, y análisis estadístico con potencia calculada. Sin eso, lo que tienes es una anécdota (`78`, `287`).
- **Contaminantes:** el cultivo determina pesticidas (`200`) y buena parte de metales pesados, que entran por
  suelo, agua de riego y fertilizantes (`202`, `106`).

## Ejemplo aplicado

Ensayo de fecha de cosecha en una variedad tipo I, tres réplicas por fecha, muestra compuesta de 6 plantas
(ILUSTRATIVO, HPLC-DAD y GC-MS, base seca):

| Semana de floración | THC total (%) | CBN (%) | Terpenos totales (mg/g) | Peso seco por planta (g) |
|---|---|---|---|---|
| 7 | 15,8 | 0,03 | 18,1 | 82 |
| 8 | 19,4 | 0,05 | 16,4 | 96 |
| 9 | 21,1 | 0,09 | 14,2 | 104 |
| 10 | 21,3 | 0,21 | 11,7 | 107 |
| 11 | 20,4 | 0,48 | 9,3 | 108 |

Lectura honesta: el máximo de THC total está entre las semanas 9 y 10, pero **los terpenos ya cayeron 21 %**
entre la 9 y la 10, y el CBN se duplicó. Si tu producto compite por potencia, cosechas en 10; si compite por
aroma (flor premium, rosin), cosechas en 9 y aceptas 0,2 puntos menos de THC. **La decisión es de producto,
no de agronomía**, y ahora la puedes tomar con números.

Para un cáñamo tipo III el mismo gráfico se lee al revés: la semana que maximiza CBD puede ser la que te
saca del límite de THC total (`175`).

## Errores comunes

- Comparar dos ciclos sin haber medido humedad: media diferencia es agua (`07`).
- Cambiar tres variables a la vez (luz, nutrición y fecha) y atribuir el resultado a la que te gusta.
- Cosechar por color de tricomas cuando lo que decide tu cumplimiento es el THC total medido.
- Muestrear solo las colas superiores: sube el resultado y te engañas a ti mismo.
- Aplicar fitosanitarios sin verificar el periodo de carencia; el residuo aparece en el COA meses después
  (`200`).
- Regar con agua sin analizar: los metales pesados entran por ahí (`106`, `202`).
- Creer que la variabilidad se elimina. No se elimina: se **caracteriza** y se convierte en un rango de
  especificación (`282`).

## Conexión con otros módulos

→ `170-cannabis-botanica-y-quimiotipos.md` · `171-genetica-y-variedades.md` — lo que la genética fija.
→ `186-cosecha-secado-y-curado.md` — la etapa siguiente, donde se pierde lo ganado.
→ `182-terpenos-del-cannabis.md` — la fracción más sensible al manejo.
→ `66-plan-de-muestreo-y-representatividad.md` — el paso que decide si tus datos sirven.
→ `287-diseno-de-experimentos-doe.md` — cómo probar un tratamiento sin engañarte.
→ `200-pesticidas-en-cannabis.md` · `202-metales-pesados-en-cannabis.md` — lo que el cultivo deja.
→ `282-especificacion-de-producto-terminado.md` — cómo se absorbe la variabilidad.