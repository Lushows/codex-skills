# 148 — Data-viz animada

La visualización de datos animada es contar una historia con números en movimiento: un gráfico que crece, una cifra que sube hasta su valor, un mapa que se ilumina. Bien hecha, hace que un dato abstracto se sienta y se entienda. Mal hecha, es el "race bar chart" hipnótico que no deja entender nada. La regla de oro de toda data-viz —animada o no— es **claridad sobre espectáculo**: si la animación dificulta leer el dato, sobra. Esto se apoya en los tipos de gráfico del núcleo (ver 25 simbolismo y los principios de composición, ver 50).

## Para qué animar datos (las funciones legítimas)

1. **Revelar / introducir**: un gráfico que se dibuja guía el ojo por el dato (la barra crece de 0 a su valor → el ojo entiende la escala).
2. **Comparar en el tiempo**: mostrar cómo cambió algo (antes/después, evolución).
3. **Dirigir la atención**: resaltar el dato clave (un punto que pulsa, una barra que se destaca).
4. **Contar una secuencia**: revelar capas de información paso a paso, no todo de golpe.
5. **Dar vida a una cifra**: un número que cuenta hasta su valor (count-up) hace sentir la magnitud.

Si la animación no cumple ninguna → es decoración que estorba la lectura.

## Tipos de animación de datos

| Tipo | Qué hace | Cuándo |
|---|---|---|
| **Grow-in (crecer)** | Barras/áreas crecen desde 0 | Entrada de un gráfico de barras/columnas |
| **Draw-on (trazar)** | La línea se dibuja de izq. a der. | Gráfico de líneas / tendencia |
| **Count-up** | Un número sube hasta su valor | KPIs, cifras destacadas |
| **Stagger de series** | Cada barra/segmento entra desfasado | Listas, rankings |
| **Transición de estado** | El gráfico cambia de un dato a otro fluido | Cambiar filtro/periodo |
| **Highlight** | Un elemento se destaca (color/pulso) | Señalar el dato clave |

Conecta con la elección del tipo de gráfico correcto (ver 25): primero eliges el chart adecuado al dato (barras para comparar, líneas para tendencia, etc.), **después** decides cómo se anima.

## Claridad sobre espectáculo: las reglas

- **El eje y las etiquetas deben estar legibles** durante y después de la animación. No animes los números mismos hasta hacerlos ilegibles.
- **Una idea por animación**: revela un mensaje, no diez datos compitiendo.
- **Duración corta**: 400–800 ms para una entrada de gráfico. Si tarda 4 s, aburre.
- **Easing suave** (ease-out): las barras frenan al llegar a su valor, no de golpe.
- **No mientas con el movimiento**: si el eje no empieza en 0, la animación de "crecer" exagera diferencias. Sé honesto con los números (el movimiento puede engañar más que un gráfico estático).

## El caso del "race bar chart"

Esos videos de barras que se adelantan unas a otras al ritmo del tiempo son virales pero **malos para entender**: el ojo persigue el movimiento, no procesa la magnitud. Úsalos solo como contenido de entretenimiento social (ver 146), nunca para que alguien tome una decisión con el dato. Para comprensión real: un gráfico claro y quieto, o una animación de revelado simple, gana.

## Data-viz animada para presentaciones y dashboards

- **Presentaciones**: revela el gráfico por partes (primero la barra del competidor, luego la tuya) para construir el argumento. El movimiento sirve al storytelling (ver 08 presentar la idea).
- **Dashboards / producto**: el dato cambia con interacción (filtros). La transición fluida entre estados ayuda a no perder el contexto (de dónde a dónde cambió). Aquí menos es más: animaciones de 200–300 ms, sin distraer del trabajo.
- **Redes sociales**: un KPI con count-up + una línea que se traza es un reel de "resultado" efectivo y rápido de producir.

## Herramientas reales

| Herramienta | Para qué |
|---|---|
| **After Effects** | Data-viz animada de alta calidad para video |
| **Flourish** | Gráficos animados sin código (incluye race charts) |
| **D3.js / Chart.js** | Gráficos animados en web/dashboards (con desarrollo) |
| **Recharts / visx + Framer Motion** | Gráficos animados en React (ver motion-framer) |
| **Canva / CapCut** | KPIs con count-up simple para reels |

Para implementar gráficos animados en web/React, la skill hermana **motion-framer** ayuda con las animaciones de Framer Motion sobre los componentes de gráfico.

## Errores comunes
- Animación que tapa o deforma las etiquetas/ejes.
- Race charts para decisiones (el ojo no procesa magnitud).
- Eje que no empieza en 0 + animación de "crecer" → engaño visual.
- Diez series animándose a la vez (caos).
- Duraciones largas que aburren.
- Animar "porque queda lindo" sin función.

## Mini-checklist
- [ ] Primero el tipo de gráfico correcto, después la animación (ver 25)
- [ ] La animación cumple una función (revelar/comparar/dirigir)
- [ ] Ejes y etiquetas legibles durante y después
- [ ] Duración corta (400–800 ms entrada; 200–300 ms en dashboard)
- [ ] Easing suave, sin engañar con el eje
- [ ] Una idea protagonista por animación

**Siguiente paso**: con todo el bloque de motion cubierto, conviene tener el mapa de qué herramienta usar para cada tarea y cómo exportar — el panorama de herramientas de motion 2026 (ver 149).
