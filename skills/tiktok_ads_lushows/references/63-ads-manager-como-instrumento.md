# 63 — Ads Manager como instrumento

Lee este módulo cuando abras Ads Manager y te ahogues en columnas que no entiendes, cuando tardes diez minutos en saber cómo va una campaña, o cuando quieras dejar de "sentir" y empezar a leer tu cuenta en 30 segundos. Ads Manager por defecto te muestra lo que TikTok quiere venderte (impresiones, alcance), no lo que decide tu plata. Configurarlo bien es como afinar un instrumento: una vez está, abres y en un vistazo sabes qué matar, qué escalar y qué dejar quieto. Esto convierte el diagnóstico (ver 61) en algo rápido y mecánico, no en una expedición.

## Columnas custom: la vista que importa

El primer cambio: arma una **vista de columnas personalizada** y guárdala. Borra el ruido, deja solo lo que toma decisiones (ver 60). Tu vista de performance debería tener, en este orden (de izquierda a derecha sigue el embudo, como en 61):

| Columna | Por qué |
|---|---|
| Gasto | Cuánta plata corrió (contexto de todo) |
| CPM | Salud de la subasta/audiencia (capa 1) |
| **Thumbstop / hook rate** | El #1 del creativo (capa 2, ver 68) |
| 6s view / % visto | Retención (capa 3) |
| CTR | Ganas de actuar (capa 4) |
| Conversiones | Cuántas ventas/leads |
| **CPA** | El número que decide ganar/perder |
| ROAS / GMV | Rentabilidad (con asterisco, ver 64) |
| Frequency | Aviso de fatiga (ver 39) |

Guárdala como vista predeterminada. Ordenada así, **leerla de izquierda a derecha es bajar por las capas del módulo 61**: el primer número que se sale de rango es tu capa rota. Crea una segunda vista "creativo" centrada en thumbstop, hold, CTR y CPA por anuncio (ver 68). Cambias de vista según la pregunta que traes.

Quita de tu vista diaria: alcance, impresiones, likes, follows, "engagement". Son contexto, no decisión (vanidad, ver 60).

## Breakdowns: partir el dato para ver la verdad

Un **breakdown** (desglose) parte un número total en pedazos para ver dónde está la diferencia. El promedio miente; el desglose dice la verdad. Los que más sirven:

| Breakdown | Qué revela | Cuándo usarlo |
|---|---|---|
| **Por anuncio (creativo)** | Qué video gana y cuál quema plata | Siempre — es el 80% (ver 68) |
| **Por edad / género** | Si un segmento dispara el CPA | Si el CPA promedio engaña |
| **Por ubicación geográfica** | Qué ciudad/región convierte | Negocios locales / envíos / geo-lift (ver 65) |
| **Por hora / día** | Cuándo conviene gastar | Optimizar horario (ver 70) |
| **Por placement** | Dónde se muestra el ad | Diagnóstico fino |

El más importante por lejos es **por anuncio**: dos creativos en el mismo conjunto pueden tener CPA de $4.000 y $40.000. El promedio del conjunto ($12.000) no te dice nada — el desglose te dice cuál matar (ver 68). En 2026 con Smart+ y conjuntos automatizados, el breakdown por anuncio es **aún más crítico**, porque el sistema reparte gasto solo y tú necesitas ver a quién se lo está dando.

### La paradoja de Simpson (por qué el promedio te miente)

Cuidado con un truco estadístico que arruina decisiones: el promedio de los promedios puede contradecir la realidad. Ejemplo: el creativo A tiene mejor CVR que B **en mujeres** y mejor CVR que B **en hombres**, pero como A recibió más tráfico de un segmento que convierte peor, su CVR total se ve más baja. Si decides por el total, matas al mejor creativo. **Moraleja: siempre desglosa antes de juzgar.** Un número agregado puede esconder la verdad opuesta.

## Reglas automáticas: el piloto que vigila por ti

Las **reglas automáticas** son condiciones que TikTok ejecuta solo, sin que estés mirando. Sirven para no quemar plata mientras duermes y para no tener que revisar cada hora. Configúralas en Ads Manager → Tools → Automated Rules. Ejemplos sensatos para empezar:

| Regla | Condición | Acción |
|---|---|---|
| Cortar sangría | CPA > 2× objetivo **Y** gasto > 1,5× tu CPA objetivo | Pausar el anuncio |
| Frenar fatiga | Frequency > 3,5 (últimos 7 días) | Avisar (no pausar aún, ver 39) |
| Proteger presupuesto | Gasto diario > X sin 1 conversión | Pausar |
| Detectar ganador | CPA < objetivo con 3+ conversiones | Avisar para escalar (ver 72) |
| Píxel caído | 0 conversiones con gasto > umbral en 6h | Avisar urgente (ver 62) |

Clave de calibración: la regla de cortar pide **dos condiciones a la vez** (CPA alto **Y** gasto suficiente). Si solo miras CPA, matas un creativo que llevaba una venta y aún no tenía señal (ver 13). El umbral de gasto protege a los creativos jóvenes. Empieza con reglas que **avisan**, no que pausan, hasta confiar en ellas. Más sobre automatización avanzada y dashboards en 69.

## Cómo leer la cuenta en 30 segundos

Rutina diaria, en orden:

1. **Vista performance** → recorre de izquierda a derecha. ¿El primer número fuera de rango en qué capa está? (ver 61). ¿Algún CPA disparado? ¿Gasto corriendo sin conversiones? Marca para revisar.
2. **Breakdown por anuncio** en lo marcado → ¿es un creativo el culpable? (casi siempre sí).
3. **Frequency** → ¿algo arriba de 3,5? Aviso de fatiga (ver 39).
4. **Decisión**: matar (CPA caro confirmado), escalar (ganador estable, ver 72) o dejar quieto (en aprendizaje, ver 13).

Si tardas más de 30s, tu vista está mal armada. Vuelve a las columnas custom.

## Ventana de atribución del panel (configúrala antes de leer nada)

Antes de juzgar cualquier número, fija la **ventana de atribución** en la que estás mirando. TikTok por defecto usa 7d-click / 1d-view (ver 64). Eso significa que el CPA que ves incluye conversiones de gente que vio el ad hasta 7 días atrás. Para comparar creativos entre sí está bien (todos bajo la misma vara), pero para decidir presupuesto recuerda que ese número **infla** frente al backend (ver 64). Documenta qué ventana usas en tu reporte (ver 67) para no comparar peras con manzanas mes a mes.

## Errores comunes — blacklist

- **Trabajar con la vista por defecto.** Te muestra vanidad, no decisiones. Arma columnas custom (ver 60).
- **Mirar el promedio del conjunto sin desglosar por anuncio.** El promedio esconde al creativo que quema plata (ver 68) y puede invertir la verdad (Simpson).
- **Reglas que pausan desde el día 1 sin calibrar.** Matan creativos en aprendizaje. Empieza avisando (ver 13).
- **Tener 15 columnas "por si acaso".** Ruido. Deja solo las que deciden.
- **Revisar cada hora a mano.** Para eso están las reglas y los dashboards (ver 69, 70).
- **No usar el breakdown geográfico/horario en negocios locales.** Gastas donde no compran. Desglosa.
- **Confiar en el ROAS de la columna sin asterisco.** Infla; triangula con backend (ver 64).
- **No fijar la ventana de atribución.** Comparas un mes a 7 días con otro a 1 día y crees que mejoraste.
