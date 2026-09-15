# 140 — Retención y métricas: la única cifra que decide si tu video vive o muere

> Verificado a **agosto de 2026**. Las plataformas cambian los nombres de sus métricas más rápido que su
> comportamiento. Si un nombre no te cuadra con lo que ves en tu panel, quédate con la **idea** y busca el
> nombre nuevo. Los números de referencia vienen de reportes de agencias y de lo que Meta/YouTube publican;
> **no son garantías**, son horquillas para saber si estás cerca o lejos.

## La frase que resume todo

> **No importa cuánta gente empieza tu video. Importa qué porcentaje llega al final.**

En 2026 el criterio que reparte alcance dejó de ser "cuántos segundos vio la gente" y pasó a ser
**qué fracción del video vieron**. Esto castiga los videos largos y flojos, y premia los cortos y densos.

Ejemplo con tus números de Bendita Pola:

| Video | Duración | Gente que lo abrió | % promedio visto | Segundos vistos por persona |
|---|---|---|---|---|
| A — "el chorizo" | 12 s | 1.000 | 78 % | 9,4 s |
| B — "recorrido del bar" | 48 s | 8.000 | 14 % | 6,7 s |

El B tiene 8 veces más gente y **menos tiempo promedio**. En 2026, el A se sigue repartiendo y el B se
apaga. Cuando alguien te diga "pero mi video tuvo 8.000 vistas", pregúntale por el porcentaje.

---

## Las 4 métricas que de verdad importan (y en qué orden)

### 1. Gancho — cuánta gente pasa del segundo 3

Nombres según dónde estés:

| Dónde | Cómo se llama | Cómo se calcula |
|---|---|---|
| Meta Ads | *Hook rate* (no viene hecho: lo armas tú) | reproducciones de 3 s ÷ impresiones |
| Instagram orgánico | **Tasa de salto** (skip rate) — es el inverso | % que se va antes de tiempo |
| TikTok | Gráfico de retención, primer punto | % que sigue ahí a los 3 s |
| YouTube | Retención de audiencia, primeros segundos | % que sigue ahí |

**Es la métrica número uno porque es la primera puerta.** Si aquí pierdes al 80 %, nada de lo que hiciste
después existe. Editar el minuto 2 de un video que muere en el segundo 2 es tiempo tirado.

Referencia práctica en pauta de Meta (2026): por debajo del **15 %** de hook rate el anuncio está roto;
**25 %** es normal; por encima de **40 %** tienes un gancho realmente bueno. Estas cifras vienen de
agencias, no de Meta; úsalas como semáforo, no como ley.

### 2. Retención — el porcentaje promedio visto

Es lo que reparte alcance. La forma honesta de leerlo:

```
% visto  =  tiempo promedio de reproducción  ÷  duración del video
```

Si tu panel te da "tiempo promedio de visualización: 7 s" y tu video dura 20 s, tu retención es **35 %**.
Ese número es comparable entre videos de distinta duración. El de "7 segundos" no lo es.

Horquillas de referencia (video corto vertical, contenido de negocio, no de celebridad):

| Duración | Aceptable | Bueno | Muy bueno |
|---|---|---|---|
| menos de 15 s | 55–65 % | 70 % | +85 % |
| 15–30 s | 45–55 % | 65 % | +75 % |
| 30–60 s | 35–45 % | 55 % | +65 % |
| más de 60 s | 25–35 % | 45 % | +55 % |

Fíjate en el patrón: **subir la duración te baja el porcentaje casi automáticamente**. Por eso alargar un
video "para que dure más" suele ser un autogol.

### 3. Reenvíos — la métrica que abre público nuevo

En Instagram, los **envíos por DM** pesan mucho más que los "me gusta" para llegar a gente que no te sigue.
Mosseri lo ha dicho públicamente varias veces; las estimaciones de agencias hablan de 3 a 5 veces más peso
que un like. No puedo verificar el multiplicador exacto — nadie fuera de Meta puede — pero **la dirección
está confirmada por Instagram**: reenvío > guardado > comentario > like.

Para un bar esto es muy concreto: un video que hace que alguien se lo mande a un amigo diciendo
"parcero, vamos" vale más que uno que junta 300 corazones.

### 4. Repeticiones

Cuando alguien vuelve a ver, el porcentaje visto puede pasar del 100 %. Es la señal más fuerte que existe.
Se consigue con videos cortos, con bucle bien cerrado (ver `31`) y con información densa que obliga a
volver ("¿qué dijo el precio?").

---

## Cómo se lee una curva de retención

La curva es un gráfico: eje X = segundo del video, eje Y = % de gente que sigue viendo. Empieza en 100 % y
baja. **Lo importante no es que baje, sino DÓNDE baja fuerte.**

### Caída en picado del segundo 0 al 3

```
100% ┤█
     │ ██
 60% ┤   ███
     │      ██████████
 20% ┤                ██████
     └────┬────┬────┬────┬────
          3    6    9    12 s
```

**Diagnóstico: el gancho falló.** No es el desarrollo, no es la música, no es el final. Es el primer
fotograma y la primera frase. Rehaz solo eso y vuelve a publicar el mismo material.

Esta caída existe siempre — es donde se pierde más gente en cualquier video del mundo. La pregunta no es
"¿hay caída?" sino "¿cuánta?". Si a los 3 segundos te queda menos del 40 %, hay problema.

### Meseta y luego derrumbe en un punto concreto

```
100% ┤███████
     │       ████████
 60% ┤               █
     │                ████████
 20% ┤                        ███
     └────┬────┬────┬────┬────┬──
          5   10   15   20   25 s
```

**Diagnóstico: hay un momento aburrido exacto.** Ve al segundo 15 del video y mira qué pasa ahí. Casi
siempre es una de estas tres: un plano que dura más de 3 segundos sin cambio, una frase de relleno
("bueno, entonces… eh…"), o el momento en que se nota que es publicidad.

Corta ese pedazo. Literalmente. El video queda de 22 s en vez de 25 y la curva se arregla sola.

### Bajada suave y constante

```
100% ┤████
     │    ████
 60% ┤        █████
     │             █████
 20% ┤                  ████
     └────┬────┬────┬────┬────
```

**Diagnóstico: el video está bien pero es largo.** No hay un error puntual, hay demasiado video. Recórtalo
un 30 % y el porcentaje visto sube sin que cambies nada más.

### Subida al final

```
100% ┤███
     │   ████████
 60% ┤           ████    ███
     │               ████
 20% ┤
     └────┬────┬────┬────┬────
```

Si la curva **sube** al final, es gente repitiendo. Eso es oro. Ese video merece que le metas plata en
pauta y que hagas tres más iguales.

---

## Métricas que te van a distraer

| Métrica | Por qué engaña |
|---|---|
| **Vistas / reproducciones** | Una "vista" hoy se cuenta casi al instante de aparecer. No mide interés, mide reparto. |
| **Me gusta** | Cuesta un toque. No indica intención de nada. |
| **Seguidores nuevos** | Importa para marca, no dice si vas a vender cerveza el viernes. |
| **Alcance** | Es consecuencia, no causa. Sube el porcentaje visto y el alcance sube solo. |
| **Comentarios de "🔥🔥🔥"** | Suelen venir de conocidos. Mide los comentarios que preguntan algo. |
| **Tiempo total de visualización** | En 2026 pesa menos que el porcentaje. Un video largo lo infla sin mérito. |

Y la trampa favorita: **comparar el porcentaje visto de un video de 8 s con uno de 45 s.** No son
comparables. Compara solo dentro de la misma horquilla de duración.

---

## La métrica que a ti sí te importa: conversaciones por video

Tú tienes bar y pauta a WhatsApp. Ninguna métrica de la plataforma mide lo que te paga la nómina. Arma
tu propia tabla, a mano, una vez por semana:

| Video | Fecha | Vistas | % visto | Reenvíos | **Mensajes de WhatsApp ese día** | **Reservas** |
|---|---|---|---|---|---|---|
| chorizo | 2 ago | 3.400 | 71 % | 88 | 14 | 4 |
| trivia jueves | 3 ago | 9.100 | 22 % | 6 | 2 | 0 |

Después de 8 o 10 filas vas a ver el patrón real de **tu** negocio, que no es el patrón de ningún blog.
Muchas veces el video de menos vistas es el que llena mesas.

---

## Cuánta gente hace falta antes de creerle a un número

Regla práctica: **por debajo de 1.000 reproducciones, no concluyas nada.** El reparto inicial es ruidoso;
un mismo video puede sacar 40 % o 60 % de retención según a quién le tocó primero.

Y por debajo de **3 publicaciones parecidas**, no digas "este formato no funciona". Un video es una
anécdota. Tres videos del mismo tipo son un dato.

---

## Cómo medir el porcentaje visto cuando la plataforma no te lo da

Algunas vistas del panel te dan tiempo promedio pero no porcentaje. Divide tú:

```
Tiempo promedio 6,2 s  ÷  duración 19 s  =  0,326  →  32,6 %
```

Y para saber tu duración exacta (no la que crees):

```bash
ffprobe -v error -show_entries format=duration -of csv=p=0 reel_chorizo.mp4
```

Un video que "dura 15 segundos" muchas veces dura 15,84. Al calcular porcentajes esa diferencia mueve la
cifra un par de puntos.

---

## El orden en que se arregla un video que rindió mal

No lo hagas al azar. Este es el orden por retorno:

1. **Gancho** (0–3 s). Si la caída inicial es fuerte, aquí está el 80 % de la ganancia.
2. **Duración.** Recorta. Casi ningún video de negocio necesita más de 25 s.
3. **El punto de derrumbe.** Elimina el pedazo exacto donde cae la curva.
4. **El remate.** Solo si la gente sí llega al final y aun así no pasa nada.
5. **Color, música, tipografía.** Sí, importan — pero mueven la aguja mucho menos que los cuatro anteriores.

Si estás retocando el color de un video con 18 % de retención, estás pintando una casa que se está cayendo.

---

## Errores comunes

- **Celebrar las vistas.** Vistas altas con retención baja es la plataforma probándote y decidiendo que no.
- **Comparar porcentajes entre duraciones distintas.** Un 40 % en 60 s es mejor trabajo que un 60 % en 8 s.
- **Sacar conclusiones con 200 reproducciones.** Ruido puro.
- **Editar el medio de un video que muere al principio.** Diagnostica antes de tocar nada.
- **Alargar el video "para que dure más y sume tiempo".** En 2026 eso te baja el porcentaje y te apaga.
- **Ignorar los reenvíos.** Es la métrica que te trae gente nueva, y casi nadie la mira.
- **Medir solo lo que la app te muestra.** Tu métrica real es mensajes de WhatsApp y mesas ocupadas.
- **Creer que un buen número en Instagram predice TikTok.** Son públicos y ritmos distintos. Mide aparte.
- **Publicar un video nuevo cada vez en vez de re-cortar el que falló.** El material ya está grabado; el
  gancho es lo barato de rehacer.
- **Tomar las horquillas de este módulo como verdad absoluta.** Son referencias de agencias y observación,
  no cifras oficiales. Tu propio historial es mejor referencia que cualquier tabla.

---

## Checklist

- [ ] Sé la **duración exacta** del video (con `ffprobe`), no la aproximada.
- [ ] Calculé el **porcentaje visto** = tiempo promedio ÷ duración.
- [ ] Miré la **curva de retención**, no solo el número resumen.
- [ ] Identifiqué si la caída es **inicial** (gancho), **puntual** (momento aburrido) o **constante** (largo).
- [ ] Tengo al menos **1.000 reproducciones** antes de concluir algo.
- [ ] Comparé este video solo contra videos de **duración parecida**.
- [ ] Anoté los **reenvíos**, no solo los me gusta.
- [ ] Registré en mi tabla los **mensajes de WhatsApp y reservas** del día de publicación.
- [ ] Si voy a corregir, ataco en orden: gancho → duración → punto de derrumbe → remate.
- [ ] Antes de decir "este formato no sirve", tengo **3 videos** del mismo tipo medidos.
