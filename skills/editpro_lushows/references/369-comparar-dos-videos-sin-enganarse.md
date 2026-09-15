# 369 — Medir de verdad: comparar dos videos sin engañarse

> `300` te dio qué mirar y qué ignorar. `304` te dio el método de experimentar. Este módulo es lo más
> difícil de las dos cosas: **decir si el video B fue mejor que el video A**. Suena trivial y no lo es.
> La mayoría de las conclusiones que saca la gente de sus propios números son falsas, y las saca con toda
> convicción.

---

## El problema de fondo

Un video no es una medición: es **una tirada**. La plataforma decide a quién se lo muestra, en qué
momento, dentro de qué mezcla de contenido, y esa decisión mueve los números mucho más que tu gancho.

Dos videos idénticos publicados en días distintos pueden dar resultados muy diferentes. Por lo tanto:

> **Una diferencia entre dos videos no es una señal. Es una diferencia entre dos videos.**

Todo el método que sigue existe para convertir diferencias en señales.

---

## La trampa número uno: la métrica que se invirtió

Instagram **reemplazó la "tasa de visualización" por la "tasa de salto"**:

- Anunciado el **24 de agosto de 2025** (Social Media Today), junto con el gráfico de retención por reel.
- Desplegado del todo, incluida la API de Insights, en **abril de 2026**.
- **Tasa de salto** = porcentaje de vistas de gente que se fue **durante los primeros 3 segundos**.
- La vieja **tasa de visualización** medía lo contrario: quién se quedó **más allá** de los 3 segundos.

Lo que esto significa para ti, en concreto:

1. **Sube = malo.** Al revés que casi todo lo demás del panel. El cerebro se equivoca con esto durante
   semanas.
2. **No puedes comparar contra tu histórico** de antes del cambio. Un "40%" de antes y un "40%" de ahora
   no son la misma realidad, y ni siquiera son exactamente complementarios (no son necesariamente
   `100 − x`, porque la base de qué cuenta como vista también ha cambiado con el tiempo).
3. **Tu línea base se reinició.** Lo honesto es empezar un historial nuevo desde tu primer video medido
   con tasa de salto, y no mezclarlo con el anterior.

Y una advertencia general que vale para las dos plataformas: **los nombres y las definiciones cambian sin
avisar**. Por eso lo que se guarda en el diario no es solo el número: es **el nombre exacto de la métrica
y la fecha**. Sin eso, en seis meses tu historial es basura.

> **No existe un umbral oficial publicado por Meta ni por TikTok** que diga cuál es una tasa de salto
> "buena". Los números que circulan en blogs de herramientas son estimaciones comerciales sin metodología
> publicada. El único punto de comparación válido es **tu propia mediana**.

---

## Las métricas, ordenadas por cuánto significan

### Nivel 1 — Significan mucho (miden tu montaje)

| Métrica | Dónde | Qué decisión mueve |
|---|---|---|
| **Tasa de salto** | Instagram | El fotograma 0 y el primer segundo |
| **Gráfico de retención** | Instagram y TikTok | Dónde cortar, dónde meter eventos |
| **Tiempo promedio de visualización** | TikTok | El montaje completo |
| **% que vio completo** | TikTok | El final y la duración |
| **Reenvíos** | Ambas | El remate y el motivo de compartir |

### Nivel 2 — Significan a medias

- **Guardados:** miden utilidad, no calidad de montaje. Suben en videos de método y receta.
- **Comentarios:** miden fricción o polémica. Un video excelente puede tener cero.
- **Nuevos seguidores por video:** dependen tanto del perfil como del video.

### Nivel 3 — Ruido para decidir montaje

- **Vistas, alcance, impresiones, me gusta.** Son consecuencia de la distribución. Sirven para saber si
  algo explotó, no para saber **por qué**.

**La prueba rápida:** si al ver el número no sabes qué cambiarías en la línea de tiempo mañana, es de
nivel 3.

---

## Los siete confusores que arruinan una comparación

Antes de comparar dos videos, verifica que estos siete estén iguales o anotados:

1. **Hora y día de publicación.** Cambia la mezcla de público de golpe.
2. **Seguidores vs no seguidores.** Un video que salió mucho a extraños siempre retiene peor. No es peor
   video: es público más frío.
3. **Duración.** Un video de 15 s y uno de 60 s no comparten escala de retención. Compara solo videos de
   duración parecida (±30%).
4. **Sonido usado.** Un audio de tendencia cambia la distribución completa.
5. **Tema.** Comida vs gente vs promoción no son comparables entre sí.
6. **Racha de la cuenta.** Después de un video que explotó, el siguiente arranca con impulso. Después de
   dos flojos, arranca frío.
7. **Calendario.** Quincena, festivo, partido, lluvia. En un bar esto pesa de verdad.

**Regla:** si cambian dos o más de los siete, la comparación no existe. Guárdala y repite el
experimento.

---

## El método: cómo se compara de verdad

### Paso 1 — Cambia UNA cosa
Una sola variable: el fotograma 0, o el tipo de gancho, o la duración, o la posición del pago. Si cambias
dos, no vas a saber cuál funcionó y vas a aprender algo falso.

### Paso 2 — Publica en la misma franja
Mismo día de la semana, misma hora ±1 h, con al menos una semana de separación (o usa reels de prueba,
más abajo).

### Paso 3 — Espera 72 horas antes de mirar
Los números de las primeras horas son ruido puro. Un video puede parecer muerto el primer día y repuntar
el tercero. **Mirar a las 2 horas y sacar conclusiones es el error más común de todos.**

### Paso 4 — Usa tasas, nunca conteos
Compara tasa de salto, tiempo promedio, % completado, reenvíos **por cada 1.000 vistas**. Los conteos
brutos solo miden cuánto te repartió la plataforma.

```
reenvíos por mil = (reenvíos / vistas) × 1000
```

### Paso 5 — Compáralo contra tu banda, no contra el otro video
Toma tus **últimos 10 videos** comparables. Calcula:

- La **mediana** de la métrica (no el promedio: un video viral te lo destroza).
- El **valor más alto y el más bajo** de esos 10. Esa es tu **banda de ruido normal**.

Ahora:

- Si el video nuevo cae **dentro** de la banda → no pasó nada. Es una tirada más.
- Si cae **fuera** de la banda → hay algo. Y todavía no es prueba.

### Paso 6 — Repítelo tres veces
Una diferencia fuera de banda una vez es una anécdota. **Tres veces seguidas en la misma dirección** ya
es un aprendizaje que puedes convertir en regla.

Sí, son tres semanas. Sí, vale la pena. Lo otro es adivinar con tabla de Excel.

---

## Reels de prueba: la herramienta que sí acorta el camino

Instagram permite publicar un reel **solo para no seguidores**: tus seguidores no lo ven, y a las ~72
horas te dice cómo respondió el público frío. Está disponible para cuentas profesionales.

Por qué sirve tanto para lo que hace este bloque:

- **Elimina el confusor #2** (seguidores vs extraños): todos los que lo ven son extraños.
- Te deja probar **dos versiones del mismo video con distinto gancho** sin gastar el público propio.
- Si falla, no le enseñaste a tu comunidad un video flojo.

**Cómo usarlo para comparar ganchos:** monta el mismo cuerpo con dos arranques distintos. Publica el A
como prueba un martes, el B como prueba el martes siguiente, misma hora. Mira tasa de salto y tiempo
promedio a las 72 h. Repite el ciclo tres veces alternando cuál va primero, para que el orden no
contamine.

Confirma en tu app cómo está la función y qué te reporta: Instagram le cambia cosas con frecuencia.

---

## La hoja de comparación (una por experimento)

Que quepa en media página. Si no cabe, no la vas a llenar.

```
EXPERIMENTO: ________________________________
VARIABLE QUE CAMBIA: ________________________
(todo lo demás igual: duración, tema, franja, sonido)

              VIDEO A            VIDEO B
fecha/hora    ____________       ____________
duración      ____ s             ____ s
público       segs / extraños    segs / extraños
--------------------------------------------------
tasa de salto ____ %             ____ %      (IG, sube=malo)
t. promedio   ____ s             ____ s      (TikTok)
% completo    ____ %             ____ %
reenvíos/mil  ____               ____
--------------------------------------------------
MI BANDA (mediana / mín / máx de los últimos 10):
tasa de salto ____ / ____ / ____
t. promedio   ____ / ____ / ____

¿ALGUNO SALE DE LA BANDA?   sí / no
REPETICIÓN Nº: 1 · 2 · 3
CONCLUSIÓN PROVISIONAL: ______________________
```

---

## La métrica que de verdad importa en un bar

Todo lo anterior mide el video. Ninguna de esas métricas paga la nómina.

Para Bendita Pola, la única métrica final es **cuánta gente entró**. Y se puede medir sin software:

- **La palabra clave.** En el video: *"dile a quien te atienda que vienes por el video del corte"*. Se
  cuenta con una raya en una hoja detrás de la barra.
- **La pregunta al pedir.** "¿Nos viste en Instagram o en TikTok?" Una raya. Dos semanas.
- **El pico del día siguiente.** Anota ventas por día en una hoja. Cuando publiques algo que funcionó,
  mira el día siguiente y el fin de semana.
- **Los mensajes.** Cuántos DM o WhatsApp llegaron preguntando por lo que salía en el video.

**Un video con retención mediocre que llenó el bar el sábado le gana a un video con retención espléndida
que no movió a nadie.** No lo olvides cuando estés mirando la curva.

---

## Cuatro formas honestas de saber que te estás engañando

1. **Miraste el número antes de definir qué ibas a mirar.** Buscar en el panel hasta encontrar algo que
   subió no es medir, es consolarse.
2. **Cambiaste la explicación después de ver el resultado.** Si el video B ganaba, era el gancho; si
   perdía, "es que fue festivo". Elige la explicación antes.
3. **Comparaste un video tuyo con uno ajeno.** Otra cuenta, otro público, otra historia. No comparable.
4. **Sacaste conclusión con una muestra chiquita.** Con pocas reproducciones, la curva es ruido con
   forma, y las tasas se mueven enteras por unas pocas personas.

---

## Errores comunes

1. Comparar tasa de salto con la vieja tasa de visualización. Están invertidas y las bases cambiaron.
2. Olvidar que en tasa de salto **subir es malo** y celebrar un número alto.
3. Mirar los resultados a las 2 horas de publicar y decidir algo.
4. Comparar conteos (vistas, likes) en vez de tasas.
5. Cambiar dos cosas a la vez y atribuir el resultado a la que te gusta.
6. Comparar un video de 15 s con uno de 60 s.
7. Comparar un video que salió a extraños con uno que vieron sobre todo tus seguidores.
8. Usar el promedio en vez de la mediana: un viral te deforma la referencia para meses.
9. Sacar una regla de un solo experimento, sin las tres repeticiones.
10. Guardar el número sin guardar el nombre de la métrica ni la fecha: en seis meses no sabrás qué medía.
11. Creerle a un "benchmark de la industria" de un blog de herramientas. No hay umbrales oficiales
    publicados.
12. Republicar el mismo video "arreglado" y compararlo con el original: el público ya lo vio y arranca en
    desventaja.
13. Optimizar retención y no medir nunca si alguien vino al bar — teniendo además los reels de prueba
    para medir ganchos con público frío sin quemar el propio.

---

## Checklist

- [ ] Sé que la tasa de salto es inversa y que subir es malo
- [ ] Empecé un historial nuevo desde el cambio de métrica, sin mezclarlo con el viejo
- [ ] Anoto siempre el nombre exacto de la métrica y la fecha
- [ ] En este experimento cambia **una** sola cosa
- [ ] Los siete confusores están iguales o anotados
- [ ] Publiqué en la misma franja horaria y día de la semana
- [ ] Esperé 72 horas antes de mirar
- [ ] Comparo tasas, no conteos
- [ ] Calculé mi banda (mediana, mín, máx) con los últimos 10 videos comparables
- [ ] Definí la explicación **antes** de ver el resultado
- [ ] Voy por la repetición 1, 2 o 3, y no concluyo antes de la tercera
- [ ] Usé reels de prueba si quería medir el gancho contra público frío
- [ ] Tengo la hoja de comparación llena y guardada
- [ ] Además de las métricas del video, estoy contando cuánta gente llegó al bar
