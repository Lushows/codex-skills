# 62 — Maillard y pardeamiento (por qué el hongo secado cambia de color, de olor y de composición)

Cuando secas hongos o tuestas chaga, no estás solamente quitando agua: estás corriendo una reacción química
masiva entre los azúcares y los aminoácidos del material. Eso es la reacción de Maillard, y es la
responsable del color café, del olor a "tostado" que a la gente le encanta, y también de que parte de los
aminoácidos esenciales dejen de estar disponibles. Este módulo te da el control de esa reacción: cuándo la
quieres (café de hongos, chaga tostado) y cuándo te está destruyendo el producto (extracto que debía ser
claro, aminograma que se cae, triterpenos que se degradan). El error caro que evita: secar a 70 °C "para ir
más rápido" y entregar un lote que no cumple la especificación de color ni la de activos.

Términos: **reacción de Maillard (Maillard reaction)** = pardeamiento no enzimático entre un azúcar reductor
y un grupo amino. **Azúcar reductor (reducing sugar)** = azúcar con carbonilo libre (glucosa, fructosa,
maltosa); la sacarosa no lo es hasta que se hidroliza. **Melanoidina (melanoidin)** = polímero pardo, de
estructura mal definida, producto final de Maillard. **Caramelización (caramelization)** = pardeamiento de
azúcares solos, sin amino, y a temperaturas más altas. **Pardeamiento enzimático (enzymatic browning)** =
oscurecimiento por polifenol oxidasa/tirosinasa, el que pone negro al champiñón cortado; **no es Maillard**.

## Los tres pardeamientos, que la gente confunde

| | Maillard | Caramelización | Enzimático |
|---|---|---|---|
| Reactivos | Azúcar reductor + amino (aminoácido, péptido, proteína) | Azúcar solo | Fenoles + O₂ + polifenol oxidasa (PPO) |
| Necesita enzima | No | No | **Sí** |
| Arranca a | Perceptible desde ~50–60 °C; rápida >120 °C | Típicamente >150 °C | Temperatura ambiente, en minutos |
| a_w óptima | **Intermedia, ~0,6–0,8** | Baja/nula | Alta |
| En hongos | Secado, tostado, extracción caliente prolongada | Solo en tostados fuertes | El champiñón cortado que se pone negro |
| Cómo se frena | Bajar T, bajar tiempo, salir rápido de la zona de a_w media, bajar pH | Bajar T | Escaldado (inactiva la PPO), ácido, frío, atmósfera sin O₂ |

Detalle que decide procesos: **Maillard tiene un máximo a actividad de agua intermedia**. Un material muy
húmedo diluye a los reactivos; uno muy seco no los deja moverse. La zona peligrosa es justo la que atraviesas
a mitad del secado — y ahí es donde el tiempo de residencia importa más que la temperatura pico (`35`).

## Las tres etapas, en cristiano

```
ETAPA INICIAL   Azúcar reductor + −NH₂ (lisina, arginina, N-terminal)
                        │  condensación → base de Schiff
                        ▼
                Producto de Amadori (o de Heyns)    ← sin color todavía, pero la lisina YA se perdió
ETAPA INTERMEDIA
                Deshidratación / fragmentación → HMF, furfural, dicarbonilos (glioxal, metilglioxal)
                Degradación de Strecker: aminoácido + dicarbonilo → aldehído + CO₂
                        ↑ AQUÍ nace el AROMA (pirazinas, furanos, tiofenos: notas a tostado, nuez, cacao)
ETAPA FINAL
                Polimerización → MELANOIDINAS (color pardo a negro, alto peso molecular)
```

Tres consecuencias prácticas de este esquema:

1. **La pérdida nutricional ocurre antes que el color.** Cuando ves el pardeamiento, la lisina disponible ya
   se comprometió hace rato. El color es un indicador tardío.
2. **El aroma nace en la etapa intermedia** (Strecker). Si quieres el perfil tostado, tienes que llegar ahí
   y parar; si sigues, entras en amargo y quemado.
3. **Las melanoidinas no son inertes**: tienen capacidad antioxidante medible por ensayos químicos
   (DPPH, ORAC, FRAP) [in vitro] (`133`). Eso explica por qué un extracto tostado "da mejor antioxidante"
   en un ensayo de tubo — sin que eso diga nada sobre lo que pasa en una persona. No es un claim.

## Qué se pierde, medido

| Cambio | Magnitud típica reportada en literatura de alimentos | Cómo se comprueba |
|---|---|---|
| Lisina disponible | Es el aminoácido más afectado, por su ε-amino libre | Furosina por HPLC (marcador de producto de Amadori); aminograma antes/después (`54`) |
| Arginina, cisteína, metionina | Afectadas en menor grado | Aminograma |
| Color | Aumento de a* y b*, caída de L* | Colorimetría CIELab y ΔE (ver abajo) |
| HMF (5-hidroximetilfurfural) | Sube con severidad térmica | HPLC-UV 284 nm — el termómetro químico del proceso |
| Acrilamida | Se forma desde **asparagina + azúcar reductor** por encima de ~120 °C, sobre todo en tostados fuertes | LC-MS/MS. Es un contaminante de proceso genotóxico: se evalúa por MOE, no por IDA (`135`) |
| Triterpenos y compuestos termolábiles | Se degradan en paralelo, por calor, no por Maillard | HPLC-DAD del perfil (`224`, `61`) |

El punto sobre acrilamida hay que decirlo con precisión y sin alarmismo: un secado suave de hongos
(típicamente 40–60 °C) no es un proceso de formación de acrilamida. Un **tostado** intenso de material
vegetal sí entra en el rango donde la reacción es posible, y si vas a vender "chaga tostado" o "café de
hongos", medirlo una vez cuesta poco y te deja dormir (`101` es micotoxinas; esto es contaminante de proceso,
mismo espíritu de control).

## Cómo se mide el pardeamiento

```
Color CIELab (colorímetro o escáner calibrado):
   L* = luminosidad (100 = blanco, 0 = negro)   a* = verde↔rojo   b* = azul↔amarillo
   ΔE = √[(ΔL*)² + (Δa*)² + (Δb*)²]

Interpretación práctica: ΔE ≈ 1 es el umbral aproximado de diferencia perceptible por el ojo entrenado;
ΔE > 3 es diferencia obvia para cualquiera. Es el criterio que se pone en la especificación de color (`247`).

Severidad térmica del proceso (para comparar dos secadores):
   Se registra el perfil T(t) real del producto, no la consigna del equipo. Dos secadores con la
   misma temperatura de aire pueden dar historias térmicas completamente distintas.
```

Batería mínima para controlar Maillard en un proceso propio: **CIELab + HMF + humedad/a_w**. Es barata,
rápida y correlaciona con lo que el cliente ve y huele.

## Ejemplo aplicado — chaga y reishi tostados

El chaga (*Inonotus obliquus*) ya llega oscuro de fábrica: su color viene de un complejo de **melanina
propia** del hongo, no de Maillard (`229`). Cuando además lo tuestas, agregas melanoidinas encima. Resultado
práctico, con niveles de evidencia marcados:

- El extracto acuoso sale más oscuro y con más sólidos solubles, porque el tratamiento térmico rompe pared
  celular y libera material [proceso, medible por sólidos totales y rendimiento, `144`].
- El perfil aromático cambia hacia notas tostadas por Strecker [proceso, medible por GC-MS headspace, `86`].
- La capacidad antioxidante *en ensayo químico* suele subir por las melanoidinas [in vitro] — y esto **no**
  se traduce automáticamente a nada en una persona (`133`).
- Los triterpenos y otros termolábiles **bajan** con el tostado severo [medible por HPLC-DAD, `224`].

Con reishi pasa lo mismo, y aquí está la trampa comercial: un reishi tostado puede dar mejor sabor y peor
perfil de triterpenos. Si tu marca vende "reishi estandarizado a X % de triterpenos", el tostado te pelea
contra tu propia especificación.

Datos **(ILUSTRATIVO)** de un ensayo de secado de reishi molido, mismo lote partido en tres:

```
Condición                 Humedad final   L*     ΔE vs control   HMF (mg/kg bs)   Triterpenos (% p/p bs)
40 °C, 18 h (control)     6,1 %           58,2   —               4                2,10
60 °C, 8 h                5,8 %           49,7   9,1             21               1,92
80 °C, 4 h                5,5 %           38,4   21,3            96               1,44

Lectura: el "atajo" de 80 °C ahorra 14 horas y cuesta 31 % de los triterpenos y un color fuera de spec.
Todos los valores son ILUSTRATIVOS: hay que medirlos en TU material, con TU secador.
```

## Errores comunes

- Llamar "Maillard" al champiñón que se pone negro al cortarlo. Eso es enzimático (PPO) y se frena con
  escaldado o frío, no bajando la temperatura del secador.
- Subir la temperatura para acortar el secado sin medir nada. El tiempo ahorrado se paga en activos y color.
- Medir solo la temperatura del aire y no la del producto. La historia térmica real es la del material.
- No especificar el color. Sin CIELab y un ΔE máximo, "café dorado" es una opinión y no se puede reclamar
  a un maquilador (`292`).
- Vender "más antioxidante" porque el tostado subió un ORAC. Es un ensayo químico [in vitro]; en Colombia
  ese tipo de traducción a beneficio es exactamente lo que te mete en problema (`267`, `268`, `293`).
- Olvidar que la zona de a_w intermedia es la peligrosa: un secado lento y tibio puede pardear **más** que
  uno corto y caliente.
- No revisar el aminograma cuando el producto se vende también como fuente de proteína. La lisina bloqueada
  no la ve un Kjeldahl (que además, en hongos, usa factor 4,38 y no 6,25 por la quitina, `48`).

## Conexión con otros módulos

→ `142-secado-y-conservacion-de-biomasa.md` — el módulo dueño del secado como operación unitaria.
→ `240-secado-y-perdida-de-activos.md` — cuánto activo se pierde y cómo se mide en hongos.
→ `35-actividad-de-agua-y-humedad.md` — por qué a_w manda sobre "% de humedad".
→ `229-chaga-inonotus-quimica.md` — melanina propia del chaga vs melanoidinas del tostado.
→ `223-reishi-ganoderma-quimica.md` y `224-triterpenos-ganodericos-analisis.md` — lo que el calor te cuesta.
→ `54-aminoacidos-peptidos-y-proteinas.md` — lisina, arginina y el aminograma.
→ `133-estres-oxidativo-y-antioxidantes.md` — qué significa (y qué no) un ensayo antioxidante in vitro.
→ `61-estabilidad-quimica-luz-calor-oxigeno.md` — el calor después de envasar sigue trabajando.
