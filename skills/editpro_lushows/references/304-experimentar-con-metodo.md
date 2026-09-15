# 304 — Experimentar con método: una variable a la vez y cuánta muestra hace falta

> Verificado a **agosto de 2026**. Este es el módulo más incómodo del bloque, porque su conclusión
> honesta es: **con una cuenta pequeña, casi todo lo que crees haber "probado" es ruido.** No para que
> dejes de probar — para que pruebes las pocas cosas que sí se pueden probar, y dejes de tomar decisiones
> grandes con evidencia de servilleta.

## Qué es un experimento y qué no

Un experimento tiene cuatro partes. Si te falta una, no es experimento, es publicar.

```
1. HIPÓTESIS   una frase con una predicción y un número
2. VARIABLE    una sola cosa que cambia
3. MUESTRA     cuántos videos y cuántas reproducciones mínimo
4. CRITERIO    qué resultado confirmaría y cuál descartaría, escrito ANTES
```

Ejemplo malo:

> "Voy a probar si funcionan mejor los videos con música."

No hay número, no hay muestra, no hay criterio. Después de dos videos vas a decidir lo que ya querías
decidir.

Ejemplo bueno:

> **Hipótesis:** arrancar sin voz (solo sonido ambiente) baja mi tasa de salto al menos 8 puntos respecto
> a mi promedio de 38 %.
> **Variable:** solo el audio de los primeros 2 s. Todo lo demás igual.
> **Muestra:** 4 videos, mínimo 1.500 reproducciones cada uno.
> **Criterio:** confirmo si 3 de 4 quedan por debajo de 32 %. Descarto si 2 o más quedan por encima
> de 36 %. Si queda en medio, no concluyo y hago 4 más.

---

## La regla de la variable única

Si cambias el gancho **y** la música **y** la duración, y el video mejora, no aprendiste nada. Aprendiste
que esa combinación funcionó una vez.

### El problema real: no puedes aislar todo

Aquí hay que ser honesto. En video, "una variable" es una ficción parcial: si cambias el gancho, cambia
la duración; si cambias la duración, cambia el ritmo. **No busques pureza de laboratorio, busca que haya
una sola cosa que hayas cambiado a propósito.**

La forma práctica:

| Nivel de rigor | Cómo | Cuándo usarlo |
|---|---|---|
| **Máximo** | Mismo material, solo cambia el arranque | Probar ganchos. Es el mejor experimento posible |
| **Alto** | Misma estructura de bloques, tema distinto, un elemento cambiado | Probar formatos |
| **Medio** | Videos distintos pero todos comparten la variable | Probar temas o duraciones |
| **Bajo** | "Esta semana probé cosas nuevas" | No es un experimento |

### El experimento perfecto: mismo cuerpo, tres arranques

```bash
# Cuerpo común: del segundo 2 en adelante
ffmpeg -ss 2 -i original.mp4 -c copy cuerpo.mp4

# Tres arranques distintos de 2 s cada uno → tres videos
# arranque A: producto en movimiento
# arranque B: cara diciendo la frase
# arranque C: precio en pantalla
```

Todo lo demás es idéntico: música, color, remate, duración, día de la semana si los publicas espaciados.
La diferencia en tasa de salto es **atribuible al arranque**. Esto sí es un experimento.

---

## Cuánta muestra hace falta de verdad

Aquí viene la parte que duele.

### La intuición correcta, sin fórmulas

Cuando mides un porcentaje (retención, tasa de salto), el margen de error depende de cuántas
reproducciones tengas. La regla mental:

```
margen de error aproximado ≈ 50 ÷ raíz cuadrada de las reproducciones   (en puntos porcentuales)
```

| Reproducciones | Margen aproximado | Qué significa |
|---|---|---|
| 100 | ±5 puntos | Un 50 % podría ser realmente 45 % o 55 % |
| 400 | ±2,5 puntos | Empieza a servir |
| 1.000 | ±1,6 puntos | Aceptable para una métrica de un video |
| 5.000 | ±0,7 puntos | Bueno |

Parece que con 1.000 ya estás bien. **Pero ese es el margen de medir un solo video.** El problema real es
otro y es mucho peor: **la variación entre videos.**

### La variación entre videos es la que te mata

Dos videos exactamente del mismo tipo, publicados con dos días de diferencia, pueden dar 44 % y 58 % de
retención. Sin que hayas cambiado nada. Depende de a quién le tocó primero, del ánimo del reparto, del
día, de qué más había en el feed esa tarde.

Esa variación en una cuenta pequeña ronda fácilmente **±10 puntos**. Consecuencia directa:

> **Una diferencia de menos de 10 puntos entre dos videos no significa absolutamente nada.**

Y si quieres detectar diferencias más pequeñas, necesitas más videos, no más vistas.

### Cuántos videos por variable

Regla práctica honesta para una cuenta pequeña:

| Diferencia que quieres detectar | Videos por grupo | ¿Realista? |
|---|---|---|
| Enorme (más de 20 puntos) | 3 por grupo | Sí. Hazlo |
| Grande (10–20 puntos) | 5 por grupo | Sí, con esfuerzo |
| Media (5–10 puntos) | 12+ por grupo | Difícil. Meses |
| Pequeña (menos de 5 puntos) | 30+ por grupo | **No lo intentes en orgánico** |

Traducción: **en orgánico solo puedes probar cosas que hagan una diferencia grande.** Y eso está bien,
porque las cosas que importan hacen diferencias grandes. El gancho hace diferencias de 15–25 puntos. La
duración hace diferencias de 15–20 puntos. El color de la tipografía no hace ninguna que puedas medir.

> **Corolario liberador: deja de discutir sobre cosas pequeñas.** No las puedes medir, así que decídelas
> por criterio estético y sigue.

---

## Dónde sí puedes comprar muestra: la pauta

Este es el atajo que casi nadie usa bien, y para ti es el más relevante porque ya inviertes en Meta.

En orgánico, la muestra te la regala la plataforma cuando quiere. **En pauta, la compras.**

```
Un conjunto de anuncios, 3 creativos que solo se diferencian en el gancho,
$30.000 COP/día durante 4 días.

Resultado: cada creativo recibe miles de impresiones en el MISMO público,
al MISMO tiempo, con el MISMO presupuesto.
```

Eso elimina de un golpe casi toda la variación que te arruina los experimentos orgánicos: mismo público,
mismo momento, mismo reparto. Lo que quede de diferencia **sí es del creativo**.

### Cómo montarlo bien

| Regla | Por qué |
|---|---|
| Los creativos van en **el mismo conjunto de anuncios** | Comparten público y presupuesto |
| **Mismo texto, mismo destino, mismo CTA** | Solo cambia el video |
| Deja correr **mínimo 3–4 días** | Los primeros días son fase de aprendizaje |
| No toques nada mientras corre | Cada edición reinicia el aprendizaje |
| Mira **hook rate y hold rate**, no solo el costo | El costo mezcla creativo con puja |

### La trampa de la pauta

Meta **no reparte parejo**. Si un creativo arranca bien las primeras horas, se lleva casi todo el
presupuesto y los otros mueren sin datos. Eso no es un test justo, es una carrera con ventaja.

Formas de manejarlo:
- Aceptarlo: si Meta escogió uno, es porque le está yendo mejor. Es información, aunque sea sucia.
- Usar un test A/B formal de la plataforma (divide el público de verdad).
- Correr los creativos en conjuntos separados con presupuesto propio. Más caro y menos limpio, pero cada
  uno recibe datos.

**Sé honesto contigo:** la mayoría de "tests" de pauta que hace la gente son del primer tipo. Sirven para
elegir un ganador, no para aprender un principio.

---

## Comparar bien: mediana, no promedio

Con 3–5 videos por grupo, **un solo video que explota destruye el promedio**.

```
Grupo A (gancho de producto):  48, 52, 55, 51, 210   ← ese 210 fue un video que se viralizó
promedio = 83   ← mentira
mediana  = 52   ← verdad

Grupo B (gancho de cara):      44, 49, 46, 50, 47
promedio = 47
mediana  = 47
```

Por promedio, A gana por goleada. Por mediana, A gana por 5 puntos — que está por debajo del umbral de
ruido, o sea, **empate**.

**Usa siempre la mediana** (el valor de la mitad cuando los ordenas). Y mira la lista completa de números,
no solo el resumen: si un grupo es 48-52-55-51 y el otro es 20-70-30-68, el segundo no tiene un promedio,
tiene un caos.

---

## Qué vale la pena probar y qué no

### Vale la pena (diferencias grandes, medibles)

| Experimento | Diferencia típica |
|---|---|
| Gancho: producto vs cara vs precio vs problema | 10–25 puntos de tasa de salto |
| Duración: 10 s vs 25 s vs 45 s | 15–25 puntos de % visto |
| Con voz vs sin voz en los primeros 2 s | 8–15 puntos |
| Con precio en pantalla vs sin precio | Grande en mensajes, pequeña en retención |
| Formato: documental (grabado del día) vs producido | Muy grande, en las dos direcciones |
| Un CTA vs tres CTA | Grande en clics y mensajes |
| Con bucle cerrado vs final abierto | Grande en repeticiones |

### No vale la pena (no lo vas a poder medir)

- El tono exacto del color.
- La fuente de los subtítulos (si ambas son legibles).
- Qué canción, entre dos canciones parecidas.
- Publicar a las 7:00 vs a las 7:30.
- Cuatro hashtags vs seis.
- El emoji del caption.

No significa que den igual. Significa que **no puedes saberlo con tu volumen**, así que decídelo por
criterio y deja de gastar energía ahí.

---

## El calendario de un experimento real

```
SEMANA 1
  Lunes    Defino hipótesis, variable, muestra y criterio. Lo escribo.
  Martes   Grabo material para 4 videos que comparten la variable.
  Miér.    Monto los 4.
  Jue–Dom  Publico uno por día.

SEMANA 2
  Lunes    NO miro nada todavía (el último tiene 24 h).
  Miér.    Los 4 tienen más de 72 h. Ahora sí: anoto las 4 cifras.
           Saco la mediana. Comparo contra el criterio escrito.
  Jue      Escribo la conclusión en el diario (ver 306).
           Defino el siguiente experimento.
```

**Un experimento por quincena.** Más rápido no se puede si quieres que signifique algo. Y en un año son
24 experimentos, que es muchísimo más de lo que hace el 99 % de la gente.

---

## Las tres conclusiones posibles (y la tercera es la más común)

| Conclusión | Qué haces |
|---|---|
| **Confirmada** | La variable pasa a ser tu estándar. La aplicas siempre desde ya |
| **Descartada** | La descartas y la escribes en el diario. Un "no funciona" bien probado vale oro |
| **No concluyente** | Ni una ni otra. **Es lo más frecuente.** Repites con más muestra, o la abandonas |

Aprende a decir "no concluyente" sin sentirte mal. La gente que aprende rápido no es la que siempre
encuentra respuesta: es la que sabe cuándo todavía no la tiene y no se inventa una.

---

## Errores comunes

- **Cambiar tres cosas y llamarlo experimento.** Una sola variable a propósito.
- **Decidir el criterio después de ver los resultados.** Ahí siempre te das la razón.
- **Concluir con dos videos.** Tres es el mínimo absoluto y solo para diferencias enormes.
- **Creer que una diferencia de 4 puntos significa algo.** Por debajo de 10 puntos es ruido.
- **Usar el promedio con muestras chicas.** Un viral destruye el promedio. Usa la mediana.
- **Probar cosas pequeñas.** No las puedes medir. Decídelas por criterio y sigue.
- **Comparar videos publicados con meses de diferencia.** La cuenta y la plataforma cambiaron.
- **Comparar entre plataformas.** Instagram y TikTok no son el mismo experimento.
- **Tocar los anuncios mientras corre el test.** Cada edición reinicia el aprendizaje.
- **Llamar test A/B a poner tres creativos y ver cuál gasta más.** Eso elige ganador, no enseña principio.
- **No aprovechar la pauta para comprar muestra.** Es tu única forma de tener datos limpios.
- **Abandonar un experimento a mitad porque "ya se ve" el resultado.** A las 24 h no se ve nada.
- **Sentirse mal con un "no concluyente".** Es el resultado más honesto y el más frecuente.

---

## Checklist

- [ ] Escribí la **hipótesis con un número** antes de grabar.
- [ ] Definí **una sola variable** que cambio a propósito.
- [ ] Definí **cuántos videos** y **cuántas reproducciones mínimo** por video.
- [ ] Escribí **el criterio de confirmación y el de descarte ANTES** de ver resultados.
- [ ] La diferencia que busco es **grande** (más de 10 puntos). Si no, no la voy a poder medir.
- [ ] Si es un test de gancho, usé **el mismo cuerpo de video** con arranques distintos.
- [ ] Todos los videos del experimento tienen **más de 72 horas** cuando los mido.
- [ ] Comparé usando la **mediana**, y miré también la lista completa de números.
- [ ] Si usé pauta: **mismo conjunto**, mismo texto, mismo destino, 3–4 días sin tocar nada.
- [ ] Anoté el resultado como **confirmado / descartado / no concluyente**, sin forzarlo.
- [ ] Lo escribí en el **diario de aprendizajes** (`306`), gane o pierda.
- [ ] Ya definí **cuál es el siguiente experimento**.
