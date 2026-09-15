# 303 — Diagnosticar un video que funcionó: la autopsia que nadie hace

> Verificado a **agosto de 2026**. Todo el mundo analiza los fracasos. Casi nadie analiza los éxitos, y
> por eso casi nadie los repite. Este módulo es el procedimiento para desarmar un video que salió bien
> y separar **lo que es repetible** de **lo que fue suerte**. Es, con diferencia, el módulo que más
> dinero deja de todo el bloque.

## Por qué esto es más importante que analizar los fracasos

Un fracaso te dice qué **no** hacer. Hay infinitas maneras de hacerlo mal, así que esa información se
agota rápido: aprendes "no empieces con el logo", "no dejes planos de 5 segundos", y ya. Después de diez
fracasos analizados, los siguientes fracasos te enseñan lo mismo.

Un éxito te dice qué **sí** hacer, y eso es escaso. Si logras identificar por qué funcionó un video,
tienes una fórmula que puedes correr veinte veces.

Pero hay un problema: **el éxito es mucho más difícil de diagnosticar que el fracaso.** Cuando algo sale
bien, el cerebro fabrica una explicación en dos segundos y la da por cierta. "Funcionó porque salió el
perro." Puede ser. O puede ser que ese día publicaste a otra hora, o que el tema estaba en tendencia, o
que un cliente lo compartió en un grupo de 400 personas.

> **La pregunta no es "¿por qué funcionó?". Es "¿qué tendría que ser cierto para que vuelva a funcionar?".**

---

## Paso 0 — Antes de nada: ¿funcionó de verdad?

Tres filtros antes de emocionarse.

### Filtro 1 — Muestra

Si el video tiene menos de 1.000 reproducciones, no funcionó ni falló: no pasó nada. Un 82 % de retención
con 340 vistas puede evaporarse cuando llegue a 5.000.

### Filtro 2 — ¿Contra qué?

| Métrica | Este video | Mi promedio | ¿Es realmente mejor? |
|---|---|---|---|
| Tasa de salto | 26 % | 38 % | Sí, mucho |
| % visto | 61 % | 52 % | Sí |
| Reenvíos | 210 | 47 | Sí, muchísimo |
| Mensajes WhatsApp | 4 | 8 | **No. Peor** |

Este video "funcionó" en alcance y **falló en venta**. Si tu objetivo escrito era venta, no fue un éxito
— fue un video popular que no vendió. Es un caso real y frecuente, y confundirlo lleva a repetir un
formato que gusta y no factura.

### Filtro 3 — ¿En qué métrica funcionó?

Escríbelo explícitamente. "Funcionó" es vago. Estas son cosas distintas:

- Funcionó en **gancho** (poca gente se saltó el arranque).
- Funcionó en **retención** (los que entraron se quedaron).
- Funcionó en **reparto** (llegó a muchísima gente nueva).
- Funcionó en **conversión** (trajo mensajes/mesas).

Un video puede funcionar en una y fallar en otra. Y cada una se repite con técnicas distintas.

---

## Paso 1 — La autopsia técnica

Trata tu propio video como un video ajeno (el protocolo completo de eso está en `305`). Aplícate el mismo
rigor. Concretamente:

### 1.1 Congela el primer fotograma

```bash
ffmpeg -ss 0 -i reel_ganador.mp4 -frames:v 1 f0.png
ffmpeg -ss 0.5 -i reel_ganador.mp4 -frames:v 1 f05.png
ffmpeg -ss 1.0 -i reel_ganador.mp4 -frames:v 1 f10.png
```

Míralos y responde por escrito:
- ¿Qué se ve? (objeto / cara / texto / movimiento)
- ¿Se entiende sin contexto?
- ¿Hay movimiento entre f0 y f05? ¿Cuánto?
- ¿Hay texto? ¿Cuántas palabras?

### 1.2 Transcribe los primeros 3 segundos

Literalmente, con las muletillas incluidas. Esa frase es tu activo. Guárdala.

### 1.3 Cuenta los cortes y saca el ritmo

```bash
ffmpeg -i reel_ganador.mp4 -filter:v "select='gt(scene,0.3)',showinfo" -f null - 2>&1 | grep -c showinfo
```

```
cortes = 9
duración = 14,87 s
ritmo = 14,87 ÷ 9 = 1,65 s por plano   ← dentro del estándar 1,5–2 s de 2026
```

### 1.4 Dibuja la estructura en bloques con tiempos

```
0,0 – 1,7 s   gancho: chorizo en la parrilla, primerísimo plano, chisporroteo
1,7 – 4,2 s   corte a la mano cortándolo, sonido real
4,2 – 8,0 s   persona muerde, reacción, no habla
8,0 – 11,5 s  plano del plato completo + texto "$18.000"
11,5 – 14,9 s bucle: vuelve al chorizo en la parrilla
```

Esta estructura con tiempos **es la plantilla que vas a reutilizar**. No el video: la estructura.

### 1.5 Mira la curva

Un video que funcionó también tiene una curva, y esa curva te dice **cuánto margen te queda**. Si la
retención es del 61 % pero hay un escaloncito en el segundo 8, arreglar ese escalón puede llevarte al
70 %. El techo de un video bueno casi siempre está más arriba de lo que crees.

---

## Paso 2 — Separar lo repetible de la suerte

Aquí está el corazón del módulo. Haz dos columnas para cada elemento del video.

| Elemento | ¿Repetible? | Por qué |
|---|---|---|
| Gancho: primer plano de comida con movimiento y sonido real | **SÍ** | Es una decisión de edición. Puedo tomarla siempre |
| Ritmo de 1,65 s por plano | **SÍ** | Decisión de montaje |
| Precio en pantalla en el segundo 8 | **SÍ** | Decisión |
| Bucle que vuelve al inicio | **SÍ** | Decisión |
| Que ese día haya sido festivo | NO | No controlo el calendario |
| Que un influencer local lo compartiera | NO | No controlo eso |
| Que el audio de tendencia estuviera de moda esa semana | **Parcialmente** | Puedo vigilar tendencias, no puedo crearlas |
| Que el mesero saliera espontáneamente riendo | **Parcialmente** | Puedo crear condiciones para que pase, no puedo garantizarlo |
| Que la plataforma lo empujara | NO | Suerte de reparto |

**Solo lo de la columna "SÍ" es aprendizaje.** El resto es contexto.

### La prueba de fuego de la repetibilidad

Para cada elemento marcado como repetible, pregúntate:

> *Si mañana grabo otra cosa completamente distinta, ¿puedo aplicar este elemento?*

- "Empezar con primerísimo plano de comida en movimiento" → sí, siempre que haya comida. **Repetible.**
- "El chorizo" → no. Es un producto, no una técnica. **No repetible como tal.**
- "Un producto específico, en primer plano, con su sonido real" → sí. **Repetible, y es la versión
  correcta de la lección anterior.**

Fíjate en el ejercicio: la lección buena está en **subir un nivel de abstracción** desde lo concreto,
pero no dos. "El chorizo" es demasiado concreto. "Contenido de calidad" es demasiado abstracto y no
significa nada. El nivel útil está en el medio: **una instrucción de edición que puedas ejecutar mañana.**

---

## Paso 3 — La escalera de abstracción

Practica esto con cada éxito. Es el músculo más importante del bloque.

```
Demasiado concreto  →  "El video del chorizo funcionó"
                       (no sirve: no puedo volver a hacer ese video)

NIVEL ÚTIL          →  "Un primerísimo plano de un producto en movimiento,
                        con su sonido real y sin voz en los primeros 2 s,
                        baja mi tasa de salto"
                       (sirve: es una instrucción ejecutable)

Demasiado abstracto →  "El contenido auténtico conecta con la audiencia"
                       (no sirve: no cambia nada de lo que hago el martes)
```

Escribe siempre en el nivel del medio. La prueba: **si un aprendizaje no se puede convertir en una
instrucción para el montaje, está mal escrito.**

---

## Paso 4 — Formular la hipótesis y ponerle número

Un éxito sin hipótesis no es aprendizaje, es anécdota.

```
HIPÓTESIS: si arranco con primerísimo plano del producto en movimiento
           y sonido real, sin voz, mi tasa de salto baja al menos 8 puntos
           respecto a mi promedio (38 %).

PRUEBA:    3 videos con ese arranque, temas distintos, misma semana.

CONFIRMA SI: los 3 quedan por debajo de 32 % de salto.
DESCARTA SI: 2 o más quedan por encima de 35 %.
```

Fíjate que se define **de antemano** qué contaría como confirmación. Si defines el criterio después de ver
los resultados, siempre vas a encontrar la manera de darte la razón. Eso es lo que hace la gente que lleva
tres años "aprendiendo" y no ha aprendido nada.

---

## Paso 5 — Explotar el éxito antes de que se enfríe

Un video que funciona es una ventana que se cierra. Qué hacer, en orden y rápido:

### En las primeras 48 horas

1. **Responde todos los comentarios.** El video sigue repartiéndose; la actividad ayuda.
2. **Mira qué preguntan.** Cada pregunta repetida es el guion de tu próximo video.
3. **Sube una historia con el video** y una llamada directa.

### En la primera semana

4. **Haz dos videos más con la misma estructura**, tema distinto. No copies el video: copia la plantilla
   de bloques del paso 1.4.
5. **Publícalo en la otra plataforma.** Si funcionó en TikTok, va a Instagram. Distintos públicos.
6. **Considera meterle pauta.** Este es el punto clave para ti: ya sabes que retiene. Un video con
   retención probada y poco alcance es el mejor candidato a anuncio que vas a tener, y te sale más barato
   que un creativo nuevo (ver `145`).

### En el mes

7. **Guárdalo en tu carpeta de referencias propias.** Tu mejor biblioteca de referencia es la tuya.
8. **Reedítalo.** Versión de 8 s, versión con otro gancho, versión con otro remate. Mismo material.

---

## El caso peligroso: el éxito por la razón equivocada

Un video explota. Tú concluyes "la gente ama nuestras hamburguesas". Miras los comentarios: 300 personas
discutiendo sobre si el mesero se parece a un futbolista.

Ese video **no validó tu hamburguesa**. Validó un accidente. Si construyes tres meses de contenido sobre
la conclusión equivocada, perdiste tres meses.

### Cómo detectarlo

| Señal | Lectura |
|---|---|
| Los comentarios hablan de algo que no era el tema | El video se viralizó por un detalle lateral |
| Muchísimo alcance, cero guardados y cero mensajes | Entretuvo, no interesó al público correcto |
| El público alcanzado es de otra ciudad | Para un bar local, alcance inútil |
| Retención buena pero espectadores nuevos que nunca vuelven | Público de paso |

**Para un negocio local esto es crítico:** 200.000 vistas en todo el país valen menos que 3.000 vistas en
tu barrio. Revisa siempre el desglose geográfico antes de celebrar (ver `307`).

---

## Comparar tu éxito con tu promedio, elemento por elemento

La tabla que más enseña de todo el módulo. Llénala con tus 3 mejores y tus 3 peores videos:

| Elemento | Los 3 mejores | Los 3 peores |
|---|---|---|
| Duración promedio | 13 s | 34 s |
| Cortes por segundo | 0,6 | 0,2 |
| ¿Hay cara humana en el primer segundo? | 2 de 3 | 0 de 3 |
| ¿Hay precio en pantalla? | 3 de 3 | 1 de 3 |
| ¿Empieza con voz? | 0 de 3 | 3 de 3 |
| ¿Sonido ambiente real? | 3 de 3 | 1 de 3 |
| ¿Bucle cerrado? | 2 de 3 | 0 de 3 |

Con seis videos ya tienes patrones visibles. No son prueba estadística — son **pistas para diseñar el
próximo experimento** (ver `304`). Pero mira lo que salta a la vista en este ejemplo: los buenos no
empiezan con voz y son la mitad de largos. Eso son dos hipótesis listas para probar.

---

## Errores comunes

- **No analizar los éxitos.** Es el error más caro del oficio y el más común.
- **Explicar el éxito en dos segundos y creerse la explicación.** El cerebro fabrica causas al instante.
- **Quedarse en lo concreto ("el chorizo funcionó").** No es una instrucción reutilizable.
- **Irse a lo abstracto ("hay que ser auténtico").** Tampoco cambia nada del martes.
- **Celebrar un éxito de alcance cuando el objetivo era venta.** Revisa contra el objetivo escrito.
- **No revisar los comentarios.** Ahí está la razón real del reparto, y a veces no es la que crees.
- **Ignorar el desglose geográfico.** Un bar no se llena con vistas de otra ciudad.
- **Copiar el video en vez de la estructura.** La plantilla de bloques es el activo, no el tema.
- **No definir de antemano qué contaría como confirmación.** Así siempre te das la razón.
- **Dejar enfriar el éxito.** La ventana de 48 h para responder, replicar y meter pauta es real.
- **No meterle pauta a un video con retención probada.** Es el creativo más barato que vas a tener.
- **Concluir con un solo éxito.** Un video que explota puede ser suerte pura. Tres son un patrón.

---

## Checklist

- [ ] El video tiene **más de 1.000 reproducciones** y **más de 72 horas**.
- [ ] Escribí **en qué métrica exactamente** funcionó, y la comparé contra mi promedio.
- [ ] Verifiqué que funcionó **en el objetivo que había escrito antes de grabar**.
- [ ] Extraje los **fotogramas 0 / 0,5 / 1,0 s** y describí qué se ve.
- [ ] **Transcribí los primeros 3 segundos** literalmente y los guardé.
- [ ] Conté los cortes y calculé el **ritmo en segundos por plano**.
- [ ] Escribí la **estructura de bloques con tiempos**.
- [ ] Hice la tabla de **repetible vs suerte** para cada elemento.
- [ ] Subí cada aprendizaje al **nivel útil de abstracción** (instrucción ejecutable).
- [ ] Formulé una **hipótesis con número** y definí de antemano qué la confirmaría.
- [ ] Leí los **comentarios** para verificar que funcionó por la razón que creo.
- [ ] Revisé el **desglose geográfico** (crítico para un negocio local).
- [ ] Programé **2 videos más con la misma estructura** esta semana.
- [ ] Lo publiqué también en **la otra plataforma**.
- [ ] Evalué si merece **pauta**.
- [ ] Lo guardé en mi **carpeta de referencias propias**.
