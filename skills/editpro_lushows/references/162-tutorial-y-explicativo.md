# 162 — Tutorial y explicativo

**Qué resuelve:** enseñar algo en video. Una receta, cómo se usa un Excel, cómo se arma un mueble, cómo
se hace un trámite. El éxito no se mide en retención sino en **si la persona logró hacerlo**. Eso cambia
todas las reglas: aquí ralentizar a veces es lo correcto y el corte rápido puede arruinar el video.

> **La regla que gobierna el formato:** el espectador de un tutorial está **haciendo algo mientras mira**,
> o va a intentarlo después. Si tiene que devolver el video, fallaste. Si tiene que pausarlo, quizá también.

---

## 1. Los dos canales tienen que ir a la vez

Un tutorial tiene voz e imagen, y la falla número uno es que van desfasadas: se explica primero y se
muestra después, o al revés.

```
MAL:   "Ahora agregas la harina."  ... 2 s ... (aparece la mano con la harina)
MAL:   (echa la harina)  ... 1,5 s después ... "eso que echó era harina"
BIEN:  la mano entra al cuadro y a los 0,2 s la voz dice "ahora la harina"
```

**La ley del 0,2:** la palabra clave cae entre 0,2 s antes y 0,3 s después del gesto que la ilustra. Fuera
de esa ventana, el cerebro procesa dos cosas separadas y se cansa.

### Cómo se logra en la práctica

Si grabaste la voz aparte (lo recomendable en tutorial), montas al revés de lo normal: **montas la imagen
primero** y después ajustas la voz encima, estirando o acortando los silencios entre frases.

```bash
# Alargar un silencio entre frases: cortar la voz en dos y meter aire
ffmpeg -i voz.wav -af "adelay=0|0" -f lavfi -t 0.6 -i anullsrc=r=48000:cl=stereo \
  -filter_complex "[0:a]atrim=0:8.4[a1];[0:a]atrim=8.4[a2];[a1][1:a][a2]concat=n=3:v=0:a=1[out]" \
  -map "[out]" voz_ajustada.wav
```

Y si la voz se quedó corta para la acción, **se estira la imagen**, no la voz:

```bash
# Ralentizar un tramo de imagen al 70% sin tocar el audio
ffmpeg -i paso3.mp4 -vf "setpts=PTS/0.7" -an paso3_lento.mp4
```

---

## 2. Ritmo de instrucción: el pulso es OTRO

En video corto el estándar es un cambio visual cada 1,5–2 s (`20-el-pulso-del-video.md`). **En tutorial no.**

| Tipo de momento | Duración en pantalla | Por qué |
|---|---|---|
| Gancho / resultado final | 0,8 – 1,5 s | Aquí sí manda el ritmo de red social |
| Materiales / ingredientes | 0,6 – 1,0 s cada uno | Es una lista, va rápido |
| Paso simple y conocido | 1,5 – 2,5 s | Ritmo normal |
| **Paso crítico (donde la gente falla)** | **3 – 6 s** | Necesita verse completo |
| Movimiento manual delicado | tiempo real, sin cortes | Cortarlo destruye la enseñanza |
| Espera (hornear, cargar, secar) | 0,5 – 1 s con elipsis | Nadie quiere ver esperar |
| Resultado / cierre | 2 – 3 s | Aterriza |

**La asimetría es el formato.** Un tutorial bien montado es rápido en lo obvio y lento en lo difícil. Un
tutorial mal montado tiene el mismo ritmo en todo.

### Cómo identificar el paso crítico

Es donde la gente pregunta en los comentarios. Si no tienes comentarios todavía: es el paso donde tú
mismo tuviste que devolver el video de referencia, o el que tiene una técnica que no se explica con
palabras (una muñeca, un ángulo, una presión).

---

## 3. Cuándo ralentizar y cómo

Ralentizar en tutorial es una decisión pedagógica, no estética.

### Se ralentiza cuando:

- El movimiento es más rápido que el ojo (un corte de cuchillo, un click doble)
- Hay una transformación que no se ve a velocidad normal (la masa que cambia)
- Es el momento exacto donde la gente falla

### Nunca se ralentiza:

- Solo porque queda bonito
- Un movimiento que ya se entendía
- Más de 3 segundos seguidos (se vuelve tedioso)

```bash
# Cámara lenta al 40% con interpolación de fotogramas (más suave que setpts solo)
ffmpeg -i corte_cuchillo.mp4 -vf "minterpolate=fps=60:mi_mode=mci:mc_mode=aobmc,setpts=PTS/0.4" \
  -an corte_lento.mp4
```

> ⚠️ `minterpolate` es lento de procesar y puede generar artefactos raros en bordes rápidos. Pruébalo en 2
> segundos antes de mandarle un clip largo. Si deforma, usa `setpts` solo y acepta el ligero tirón.

**El acompañamiento:** cuando ralentizas, la voz debe decir por qué. "Míralo despacio: el cuchillo va
inclinado, no recto." Ralentizar sin explicar es solo un efecto.

---

## 4. Señalar en pantalla

El espectador no sabe dónde mirar. Señalar es la mitad del trabajo del formato.

### Los cinco recursos, en orden de sutileza

**1. Zoom hacia la zona (lo más natural)**

```bash
# Punch-in del 35% hacia la esquina superior izquierda donde está el botón
ffmpeg -i pantalla.mp4 -vf "scale=2592:1458,crop=1920:1080:200:120" -c:a copy zoom_boton.mp4
```

**2. Círculo o recuadro dibujado**

```bash
# Recuadro rojo de 4 px alrededor del botón, entre el segundo 5 y el 8
ffmpeg -i pantalla.mp4 -vf \
  "drawbox=x=640:y=380:w=260:h=64:color=red@0.9:t=4:enable='between(t,5,8)'" \
  -c:a copy señalado.mp4
```

**3. Oscurecer todo menos la zona (spotlight)** — el más claro de todos y el menos usado:

```bash
# Baja el brillo de todo el cuadro y deja la zona del botón normal
ffmpeg -i pantalla.mp4 -filter_complex \
 "[0:v]eq=brightness=-0.25:saturation=0.5[osc]; \
  [0:v]crop=260:64:640:380[zona]; \
  [osc][zona]overlay=640:380:enable='between(t,5,8)'[v]" \
  -map "[v]" -map 0:a -c:a copy spotlight.mp4
```

**4. Flecha o cursor grande.** El cursor real del sistema es demasiado pequeño para vertical. Si es
tutorial de pantalla, agranda el cursor en la configuración del sistema **antes de grabar**.

**5. Texto que nombra la cosa.** "Configuración → Cuentas". Obligatorio en tutoriales de software: los
menús no se leen a 1080p en un celular.

### Regla del señalamiento

**Un solo señalamiento a la vez.** Círculo + flecha + texto + zoom simultáneos convierten la pantalla en
un tablero de ajedrez. Escoge uno.

---

## 5. Capítulos y navegación

El tutorial es el único formato donde el espectador **quiere saltarse partes**. Ayúdalo.

### En video largo (YouTube)

Capítulos en la descripción con timecodes desde 00:00:

```
00:00 Qué vamos a hacer
00:38 Materiales
01:24 Paso 1 — preparar la base
03:10 Paso 2 — el ensamble (el difícil)
06:45 Errores comunes
08:02 Resultado
```

**Requisito de YouTube:** el primer capítulo tiene que arrancar en `00:00` y ninguno puede durar menos de
10 segundos, o no se activan.

Y también incrustados en el archivo:

```bash
# Crear archivo de capítulos y meterlo en el mp4
cat > capitulos.txt <<'EOF'
;FFMETADATA1
[CHAPTER]
TIMEBASE=1/1000
START=0
END=38000
title=Qué vamos a hacer
[CHAPTER]
TIMEBASE=1/1000
START=38000
END=84000
title=Materiales
EOF

ffmpeg -i tutorial.mp4 -i capitulos.txt -map_metadata 1 -c copy tutorial_cap.mp4
```

### En video vertical

No hay capítulos, pero sí **contadores en pantalla**: `PASO 2 DE 5` arriba, fijo, durante todo el bloque.
Le dice al espectador cuánto falta y sube el porcentaje de finalización de forma medible.

---

## 6. Estructura que funciona

```
0:00 – 0:04   EL RESULTADO. Se muestra terminado. Sin explicar nada.
0:04 – 0:10   Qué necesitas. Lista rápida, texto en pantalla, 0,8 s por ítem.
0:10 – …      Pasos numerados. Cada uno abre con su rótulo.
              └─ dentro de cada paso: el gesto + la voz + el detalle si es crítico
…             EL ERROR. "Aquí es donde todo el mundo se equivoca." ← el momento más visto
…             Resultado otra vez, ahora en detalle.
final         Qué hacer con eso / dónde está el archivo / CTA.
```

**El bloque del error es el que da vistas.** "Si te queda así, es porque…" — la gente que ya falló busca
exactamente eso. Nunca lo omitas por ahorrar segundos.

### Empezar por el resultado, siempre

Nadie sigue un tutorial cuyo resultado no ha visto. Los primeros 3 segundos son el plato terminado, el
mueble armado, la pantalla con el trámite aprobado. Sin voz explicando: **se muestra**.

---

## 7. La voz del tutorial

- **Segunda persona, imperativo suave.** "Agregas", "vas a", no "se agrega" ni "uno agregaría".
- **Nombra las cosas por su nombre completo la primera vez.** "El botón de Configuración, el del engranaje
  arriba a la derecha."
- **Anuncia el peligro antes, no después.** "Ojo con esto: si aprietas mucho, se parte."
- **Sin música durante los pasos críticos.** Compite con la instrucción.
- Música solo en: intro, transiciones entre pasos, montaje de resultado.

### Loudness

La voz de tutorial va **más presente** que en cualquier otro formato porque se oye en cocinas, talleres y
buses. Objetivo -14 LUFS con el pico de la voz consistente:

```bash
# Normalización en dos pasadas para voz de instrucción
ffmpeg -i voz.wav -af loudnorm=I=-14:TP=-1.5:LRA=7:print_format=summary -f null -
# (toma los valores measured_* y los metes en la segunda pasada)
ffmpeg -i voz.wav -af loudnorm=I=-14:TP=-1.5:LRA=7:measured_I=-19.4:measured_TP=-3.1:\
measured_LRA=9.2:measured_thresh=-30.1:linear=true -c:a aac -b:a 192k voz_ok.m4a
```

`LRA=7` (rango dinámico bajo) es a propósito: en tutorial queremos la voz pareja, no cinematográfica.
Detalle en `73-compresion-y-loudness.md`.

---

## 8. Elipsis: quitar la espera sin perder al espectador

Las esperas (30 min en el horno, la instalación que carga, la pintura que seca) se cortan, pero hay que
**marcar que se cortó** o el espectador cree que se saltó un paso.

Tres formas honestas:

| Recurso | Cómo se lee |
|---|---|
| Texto: `30 MINUTOS DESPUÉS` | Clarísimo. El estándar. |
| Timelapse de 1–2 s | Bonito y comunica duración |
| Fundido corto a blanco/negro (0,3 s) | Convención de "pasó tiempo" |

Nunca un corte duro seco: se lee como error de montaje o como truco.

```bash
# Timelapse: 20 minutos de grabación a 2 segundos
ffmpeg -i horneado.mp4 -vf "setpts=0.0017*PTS,scale=1080:1920" -an timelapse.mp4
```

---

## 9. Tutoriales de pantalla (software)

Lo específico:

- **Graba a 1920x1080 mínimo, aunque salga vertical.** Recortas después; ampliar no se puede.
- **Cursor grande** configurado antes de grabar. El cursor por defecto es invisible en celular.
- **Sube el zoom de la aplicación al 125–150%** antes de grabar. Es la diferencia entre legible e ilegible.
- **Limpia la pantalla**: cierra pestañas, notificaciones en silencio, fondo neutro, sin datos personales.
- **Movimientos de mouse lentos y deliberados.** Un mouse errático marea y no enseña.
- Cada click importante lleva **un pequeño zoom o un recuadro**.

```bash
# De grabación de pantalla 16:9 a vertical 9:16 con la zona útil ampliada
ffmpeg -i pantalla.mp4 -vf "crop=1080:1080:420:0,scale=1080:1080,pad=1080:1920:0:420:color=#101314" \
  -c:a copy vertical.mp4
```

Eso deja la zona activa cuadrada al centro y barras del color de marca arriba y abajo, donde después van
título y subtítulos.

---

## 10. Verificación específica del formato

Antes de dar por bueno un tutorial, la prueba real:

1. **Míralo sin sonido.** ¿Se puede hacer solo con la imagen y el texto? Si no, falta señalar.
2. **Óyelo sin imagen.** ¿Se entiende el orden? Si no, falta nombrar.
3. **Que alguien que no sabe lo intente.** Es la única prueba que cuenta. Donde pause, hay un corte mal
   hecho o un paso mal explicado.
4. **Cuenta los pasos.** Si dijiste "5 pasos" al inicio, tienen que ser 5 rótulos en pantalla.

---

## Errores comunes

1. **Voz e imagen desfasadas.** Se explica antes o después de mostrar. Es la falla #1 y arruina el video
   aunque todo lo demás esté bien.
2. **El mismo ritmo en todo.** Rápido en lo difícil y lento en lo obvio. Al revés.
3. **Cortar el movimiento crítico.** Justo la parte que la gente necesita ver es la que se cortó porque
   "era muy larga".
4. **No mostrar el resultado al inicio.** Nadie invierte 6 minutos en algo cuyo final no vio.
5. **Señalar con cuatro recursos a la vez.** Círculo, flecha, zoom y texto simultáneos. Uno basta.
6. **Texto de menús ilegible** en tutorial de software por no ampliar el zoom antes de grabar. No tiene
   arreglo en post.
7. **Música bajo el paso crítico.** Compite con la única cosa que el video tiene que transmitir.
8. **Elipsis sin marcar.** Corte duro después de "ahora lo dejas 30 minutos" — el espectador cree que se
   saltó algo.
9. **Omitir el bloque de errores comunes** por acortar. Es el bloque que más se busca.
10. **Numeración inconsistente.** Dijiste 5 pasos y en pantalla hay 4 rótulos y un bloque sin número.
11. **Cursor invisible** o movimientos de mouse erráticos.
12. **No incluir capítulos** en un tutorial largo de YouTube. Es el formato donde más se usan.
13. **Ralentizar por estética.** Cámara lenta bonita en un paso que ya se entendía; solo alarga el video.

---

## Checklist

- [ ] El resultado final se muestra en los primeros 4 segundos
- [ ] Cada palabra clave cae dentro de ±0,3 s del gesto que ilustra
- [ ] El ritmo es asimétrico: rápido en lo obvio, 3–6 s en los pasos críticos
- [ ] El movimiento delicado se ve completo, sin cortes internos
- [ ] Todo ralentizado tiene voz explicando por qué se ralentizó
- [ ] Un solo recurso de señalamiento a la vez
- [ ] Texto en pantalla para todo nombre de menú, botón, medida o cantidad
- [ ] Contador `PASO X DE Y` en vertical / capítulos con timecodes en largo
- [ ] Primer capítulo arranca en 00:00 y ninguno dura menos de 10 s
- [ ] Toda espera está marcada con texto, timelapse o fundido
- [ ] Bloque de "errores comunes" incluido
- [ ] Sin música durante los pasos críticos
- [ ] Voz a -14 LUFS con LRA bajo (pareja, no cinematográfica)
- [ ] Prueba sin sonido superada
- [ ] Prueba con alguien que no sabe hacerlo: no tuvo que devolver el video
- [ ] Pasó `98-verificacion-del-corte.md`
