# 135 · Sintetizar es la garantía

**Qué resuelve:** por qué el canal genera su propio sonido con ffmpeg en vez de
descargarlo. La razón no es el coste ni el gusto: es que **elimina una categoría entera
de riesgo** en lugar de administrarla.

> ⚖️ **Esto no es asesoría legal.** Es una decisión de producción basada en dónde está
> el riesgo real de este canal. Sintetizar reduce el riesgo casi a cero; este módulo
> también dice honestamente **lo que no resuelve**.

---

## Lo que desaparece

De las tres capas de derechos que tiene cualquier audio (§ 130), una pista sintetizada
por nosotros las tiene las tres del mismo lado:

| Capa | Con audio descargado | Con audio sintetizado |
|---|---|---|
| **Obra** | de un compositor ajeno | la progresión la escribimos nosotros (§ 110-119) |
| **Fonograma** | de un sello o de un banco | el archivo lo produce nuestro script |
| **Interpretación** | de un músico ajeno | no hay intérprete: hay osciladores |

No hay licencia que leer, no hay lista blanca que mantener, no hay suscripción que
caduque, no hay banco que pueda reclamarnos nuestro propio vídeo. **El problema no se
gestiona mejor: deja de existir.**

## La prueba es reproducible, y eso es lo importante

La diferencia entre «es mía» y **demostrar** que es mía es todo el módulo § 133. Una
pista sintetizada viene con su propia prueba:

```
script generador  →  comando de ffmpeg  →  archivo .wav
     (en git)          (en pistas.json)        (con hash)
```

Cualquiera puede volver a ejecutar el script y obtener la pista. Eso es lo que una
afirmación no puede hacer. Ante una disputa, adjuntar el código que genera el audio
reclamado es la respuesta más fuerte disponible, porque **es verificable por la otra
parte**.

⚠️ **Matiz honesto:** no doy por hecho que la reproducción sea idéntica bit a bit entre
versiones distintas de ffmpeg o entre máquinas. Por eso en el registro se anota la
**versión de ffmpeg** (§ 138): la prueba es «este código, con esta versión, produce este
sonido», no una promesa de determinismo universal.

## Lo que sintetizar NO resuelve

Aquí es donde la gente se relaja de más. Tres cosas siguen en pie:

### 1. La obra sigue existiendo aunque la grabación sea tuya
Sintetizar la melodía de una canción protegida **sigue siendo usar esa canción**. El
sintetizador no lava el derecho sobre la composición: solo cambia quién es el dueño del
fonograma. Tocar «Happy Birthday» con un oscilador no es más libre que ponerla de un
disco.

**Regla del canal:** no se reproducen melodías reconocibles. Ni de temas comerciales, ni
de sintonías, ni de jingles, ni «solo las cuatro primeras notas». Las progresiones del
canal se escriben desde el criterio narrativo del bloque 110-119, no desde una canción
de referencia.

⚠️ **Dónde está exactamente la frontera entre una progresión de acordes —que en general
no se considera protegible por sí sola— y una melodía reconocible, es materia de
jurisprudencia y varía.** No voy a trazar esa línea con precisión aquí. Para producción
basta un criterio más estricto que la ley: **si al tararearla alguien puede nombrar la
canción, no entra.**

### 2. Los falsos positivos siguen llegando
Content ID compara ondas (§ 132). Atmósferas, drones graves, ruido filtrado y *risers*
genéricos se parecen entre sí por construcción, y hay casos documentados de audio CC0
reclamado. Sintetizar no te hace invisible al sistema; te hace **capaz de ganar** cuando
el sistema se equivoca.

### 3. El sonido de archivo sigue siendo archivo
Si en un episodio entra una grabación histórica real, ese audio tiene sus propias reglas
(§ 137) y no se beneficia de nada de este módulo.

## Lo que sí hay que cuidar del lado técnico

- **El script vive en el repositorio**, con su historial. Un comando escrito a mano en
  una terminal y perdido no es prueba de nada.
- **Una pista, una entrada** en el manifiesto (§ 138). Las pistas «rápidas» sin
  registrar son justo las que aparecen en la reclamación.
- **Nada de bibliotecas de muestras de origen dudoso.** Un sintetizador que arranca de
  una muestra grabada por otro no es síntesis pura: es una muestra con licencia. Si
  entra, entra con su ficha.
- **Cuidado con los modelos generativos de música.** Generar no es sintetizar: hay
  términos de uso, hay dudas abiertas sobre el material de entrenamiento y la
  titularidad de la salida varía por país. ⚠️ **No lo doy por resuelto.** El canal no
  los usa; si algún día se plantea, es una decisión con abogado, no un atajo.

## El resumen operativo

| Pregunta | Respuesta del canal |
|---|---|
| ¿De dónde salió esta música? | De `audio/generar_<tema>.py`, commit `<sha>` |
| ¿Quién es el titular? | Paper Empires |
| ¿Qué licencia tiene? | Ninguna que administrar: es propia |
| ¿Puedes demostrarlo? | Sí: aquí está el código y aquí el hash del wav |
| ¿Y si llega una reclamación? | § 133, con el registro en la mano |

Cuatro de esas cinco respuestas son imposibles con audio descargado. Esa es toda la
justificación de la decisión.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Creer que sintetizar borra también el derecho sobre la melodía | Infracción de obra con fonograma propio: sigue siendo infracción |
| Recrear «de oído» un tema conocido para el gancho | El caso anterior, con agravante de intencionalidad |
| Generar una pista a mano en la terminal y no guardar el comando | Pista sin prueba, exactamente como si se hubiera descargado |
| Dar por hecho que no llegará ninguna reclamación | Los falsos positivos existen; lo que cambia es que se ganan |
| Usar muestras de un pack descargado dentro de la síntesis | Se reintroduce el riesgo que el módulo entero elimina |
| Confundir música generada por un modelo con música sintetizada | Otro régimen, otros términos, otras dudas abiertas |
| No anotar la versión de ffmpeg | La prueba pierde la parte que la hace reproducible |

## Relacionado

`81` sintetizar efectos · `82` música por código · `130` la obra y la grabación ·
`132` Content ID · `133` reclamaciones · `138` registrar lo propio
