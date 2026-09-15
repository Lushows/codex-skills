# 144 — YouTube largo: estructura, retención, miniatura y título

> Verificado a **agosto de 2026**. Las horquillas de retención y CTR son referencias de industria; YouTube
> no publica benchmarks oficiales. Tu propio historial en YouTube Studio es mejor referencia que cualquier
> tabla de este módulo.

## Antes de nada: ¿tú necesitas video largo?

Respuesta honesta para un bar en Tocancipá: **casi nunca, y cuando sí, no es para vender cerveza.**

El video largo tiene sentido cuando:

- Hay una **historia** que no cabe en 40 segundos: cómo se montó el bar, quién cocina, el proceso de algo.
- Quieres **posicionarte como referencia local**: "los 7 sitios para comer en la sabana".
- Estás **vendiendo algo caro o complejo** (eventos privados, alquiler del lugar, franquicia).
- Estás **documentando** para tener material que después se corta en 20 verticales.

No tiene sentido para promocionar el jueves de trivia. Para eso hay un Short de 15 segundos.

**La jugada más rentable del video largo es que es una fábrica de cortos.** Grabas 20 minutos de contenido
bueno una vez, sacas un video de 8 minutos y de ahí salen 12 verticales para tres plataformas.

---

## Especificaciones

| Qué | Valor |
|---|---|
| Resolución | **1920x1080** mínimo. **3840x2160 (4K) si puedes** |
| Por qué 4K aunque nadie vea en 4K | YouTube le da **más bitrate** al 4K. Se ve mejor incluso en 1080p |
| Formato | 16:9 |
| Fotogramas por segundo | 24, 25 o 30. Constante. Si grabaste a 60, decide y sé consistente |
| Códec | H.264 (o H.265/AV1 si tu editor lo saca bien) |
| Audio | AAC **384 kbps**, 48 kHz, estéreo |
| Bitrate video 1080p30 | 12–20 Mbps |
| Bitrate video 2160p30 | 45–70 Mbps |

```bash
# 1080p de subida limpia
ffmpeg -i master.mov \
  -c:v libx264 -profile:v high -level 4.2 -pix_fmt yuv420p \
  -b:v 18M -maxrate 22M -bufsize 36M -r 30 \
  -c:a aac -b:a 384k -ar 48000 -ac 2 \
  -movflags +faststart -y youtube_1080.mp4
```

El truco del **4K aunque tu material sea 1080p**: subir escalado a 2160p hace que YouTube use su
codificación de mayor bitrate. Es real y funciona, pero **el archivo pesa 4 veces más y sube 4 veces más
lento**, y la mejora es visible sobre todo en planos con mucho movimiento o mucho grano. Si tu bar tiene
poca luz y grano, vale la pena. Si es material limpio, no te mates.

---

## La estructura que aguanta

### Los primeros 15 segundos son casi todo

Hay un dato de industria que se repite: los videos que enganchan en los primeros 15 segundos retienen
mucho más al llegar al minuto 3. La cifra exacta varía según quién la cite; la dirección es sólida y
coincide con lo que muestra cualquier curva de retención.

Lo que va en esos 15 segundos:

```
0:00–0:03   La promesa o el conflicto. Sin saludo, sin logo, sin "hola qué más".
0:03–0:08   Por qué te tienen que creer a ti (una frase, no un currículum).
0:08–0:15   Qué van a ver (el mapa del video), en una frase.
```

Lo que **no** va: presentación del canal, animación de intro, "antes de empezar suscríbete", agradecimiento
a los patrocinadores.

> El "no olvides suscribirte" al principio es la forma más eficiente de perder gente. Va al minuto 60–70 %
> del video, cuando ya demostraste que vales la pena.

### El cuerpo: bloques, no un río

Divide el video en bloques de 60–120 segundos, cada uno con su propio mini-gancho al inicio. Entre bloque
y bloque, un cambio claro: un plano distinto, un texto en pantalla, un cambio de lugar.

**La curva de retención se cae en las transiciones flojas.** Cuando un bloque termina y el siguiente
arranca con "bueno, entonces…", ahí pierdes gente. Arranca el bloque nuevo con su propia frase fuerte.

### El pico al 70 %

Hay una recomendación repetida que funciona: **guarda el mejor momento para alrededor del 70 % del
video**. Si el mejor momento está al principio, la gente se va después. Si está al final, no llegan.
El 70 % es el punto donde el que llegó hasta ahí, termina.

Para ti: si el video es "cómo montamos Bendita Pola", el momento de la primera noche llena va al 70 %,
no al principio.

### El final

Los últimos 20 segundos son para **una sola acción**. No tres. Una.

Para un negocio local: "escríbenos por WhatsApp, el enlace está abajo" o "estamos en la [dirección], jueves
a domingo". No "suscríbete, dale like, comenta, comparte y visita nuestra web".

**No pongas pantalla final de 20 segundos con videos recomendados si tu objetivo es que te escriban.**
Esa pantalla existe para retener gente dentro de YouTube, no para llevarla a tu bar.

---

## Capítulos

Los capítulos (marcadores de tiempo en la descripción) hacen tres cosas:

1. Le dan al espectador control → en vez de irse frustrado, salta a lo que le interesa. **Un salto sigue
   contando como tiempo de visualización; irse, no.**
2. YouTube los usa para entender de qué trata el video.
3. Aparecen en resultados de búsqueda como puntos de entrada.

### Cómo se escriben

En la descripción, en orden, **el primero tiene que ser 00:00**:

```
00:00 Por qué abrimos un bar en Tocancipá
01:12 El local que nadie quería
03:40 Lo que costó de verdad (con números)
06:05 El primer viernes: se llenó
08:20 Lo que haría distinto
```

Reglas:
- Mínimo **3 capítulos**.
- Cada uno de mínimo **10 segundos**.
- El primero **debe** ser `00:00` o YouTube no activa los capítulos.
- Títulos que digan algo. "Parte 2" no sirve. "Lo que costó de verdad" sí.

Si tu video dura menos de 4 minutos, los capítulos molestan más de lo que ayudan. Sáltalos.

---

## Miniatura y título: la pareja que decide si el video existe

**Nadie ve tu video por lo bueno que es. Lo ven por la miniatura y el título.** Después el video decide si
se quedan. Son dos trabajos distintos y hay que hacer los dos.

### La miniatura

| Regla | Por qué |
|---|---|
| **1280x720 px**, JPG o PNG, menos de 2 MB | Especificación de YouTube |
| **Máximo 3–4 palabras** de texto | Se ve del tamaño de una uña en celular |
| **Tipografía gruesa, alto contraste** | Lo mismo |
| **Una cara con emoción clara**, si hay persona | Funciona; es aburrido pero funciona |
| **No repitas el título en la miniatura** | Desperdicias espacio diciendo lo mismo dos veces |
| **Colores saturados y distintos a los del entorno de YouTube** | Rojo, amarillo, cian destacan sobre el fondo |

**La prueba real:** reduce tu miniatura a 320x180 px y mírala en el celular con el brillo bajo. Si no se
entiende, no sirve.

```bash
# Simular cómo se ve la miniatura en tamaño real de celular
ffmpeg -i miniatura.jpg -vf scale=320:180 -y miniatura_prueba.jpg
```

### El título

- **60 caracteres o menos** para que no se corte en móvil.
- Las **palabras importantes al principio**: en móvil se corta el final.
- Que contenga lo que alguien escribiría en el buscador.
- **Sin mentir.** Un título que promete lo que el video no da destruye la retención, y la retención es lo
  que YouTube mide.

Malo: `✨ Nuestro nuevo video sobre el bar ✨`
Bueno: `Cuánto cuesta abrir un bar en Colombia (números reales)`

### CTR: qué es un buen número

El **CTR** (porcentaje de clics) es cuánta gente que vio tu miniatura hizo clic. Referencia de industria:
**4 % a 10 %** es rango normal para canales establecidos. Por debajo de 2 % hay problema de miniatura o
título. Por encima de 10 % con retención baja significa que la miniatura promete más de lo que el video da.

**CTR y retención se leen juntos, nunca por separado:**

| CTR | Retención | Diagnóstico |
|---|---|---|
| Bajo | Alta | El video es bueno, la portada no vende. Rehaz miniatura y título. |
| Alto | Baja | Prometiste de más. El video no cumple. |
| Bajo | Baja | El tema no interesa. Cambia de tema. |
| Alto | Alta | YouTube va a empujarlo. No lo toques. |

---

## Retención en video largo: qué es un buen número

Referencias de industria (no oficiales):

| Duración del video | Retención aceptable | Buena |
|---|---|---|
| 3–8 min | 40–50 % | +60 % |
| 8–15 min | 35–45 % | +55 % |
| 15+ min | 30–40 % | +45 % |

Y la **duración media de reproducción** (AVD) por encima del 50 % de la duración total se considera fuerte.

Fíjate en lo mismo de siempre: **más duración, menos porcentaje**. Un video de 20 minutos con 45 % de
retención es un trabajo excelente; el mismo 45 % en 4 minutos es normal.

### Leer la curva

En YouTube Studio → tu video → **Participación → Retención de audiencia**. Ahí ves:

- **La caída de los primeros 30 segundos.** Siempre existe. Si a los 30 s te queda menos del 60 %, el
  arranque está roto.
- **Los picos hacia arriba.** Es gente rebobinando. Hay algo interesante o algo confuso. Ve a mirar.
- **Los valles.** El momento exacto donde aburres. Anótalo y no lo repitas en el próximo video.
- **La meseta final.** Si el último 20 % es plano, tu video podría haber durado más.

Ver `149` para el método completo de lectura.

---

## Cómo un video largo alimenta 12 cortos

Este es el flujo que le saca rendimiento real al esfuerzo:

1. Graba 25–40 minutos con buen audio y varias cámaras/ángulos si puedes.
2. Monta el video largo (8–12 min).
3. **Mientras montas, anota los momentos con timecode**: la frase buena, la reacción, el dato, el error
   gracioso.
4. Cada momento de 8–30 segundos se convierte en un vertical.
5. Reencuadra a 9:16 (ver `147` y `22`), pon texto, y ya tienes contenido para dos semanas.

```bash
# Extraer un momento marcado, sin recomprimir
ffmpeg -ss 00:04:12 -to 00:04:31 -i largo_master.mov -c copy -y momento_01.mov
```

Con `-c copy` el corte puede quedar unos fotogramas corrido (corta en el fotograma clave más cercano).
Para precisión al fotograma, recomprime:

```bash
ffmpeg -ss 00:04:12 -to 00:04:31 -i largo_master.mov \
  -c:v libx264 -crf 16 -preset slow -c:a aac -b:a 256k -y momento_01.mov
```

---

## Errores comunes

- **Hacer video largo para vender el jueves de trivia.** Eso es un Short.
- **Intro animada de 8 segundos.** La caída de retención más cara que existe.
- **"Suscríbete" al principio.** Va al 60–70 %, no al minuto cero.
- **Título bonito en vez de título buscable.** "Vibras del bar" no lo busca nadie.
- **Repetir el título en la miniatura.** Espacio desperdiciado.
- **Miniatura con 12 palabras.** A tamaño uña no se lee nada.
- **CTR alto con retención baja y celebrarlo.** Estás quemando la confianza del público.
- **Guardar el mejor momento para el final.** No llegan. Va al 70 %.
- **Video sin capítulos con más de 6 minutos.** Regalas los saltos que te habrían salvado tiempo de visto.
- **Poner el primer capítulo en 00:12 en vez de 00:00.** YouTube no activa capítulos y no te avisa.
- **Pantalla final de 20 segundos con recomendados cuando querías que te escribieran.**
- **Subir el largo y no sacarle los cortos.** Grabaste 40 minutos para usar 10. Ahí está la plata.
- **Comparar tu retención con la de un canal de entretenimiento.** No es tu categoría ni tu duración.

---

## Checklist

- [ ] Tengo claro **por qué este contenido es largo** y no un Short.
- [ ] Export **1080p (o 4K) 16:9, H.264, fps constantes, AAC 384 kbps**, `+faststart`.
- [ ] Los **primeros 15 segundos** tienen promesa, credibilidad y mapa. **Sin intro animada.**
- [ ] El video está partido en **bloques de 60–120 s**, cada uno con su propio arranque.
- [ ] El **mejor momento está alrededor del 70 %** del video.
- [ ] Los últimos 20 segundos piden **una sola acción**.
- [ ] Hay **mínimo 3 capítulos**, el primero en **00:00**, con títulos que dicen algo.
- [ ] La **miniatura** es 1280x720, con 3–4 palabras, y **la probé reducida a 320x180**.
- [ ] La miniatura **no repite** el título.
- [ ] El **título** tiene menos de 60 caracteres, palabras clave al principio, y no miente.
- [ ] La descripción tiene **dirección, horario y enlace de WhatsApp**.
- [ ] A los 7 días voy a mirar **CTR y retención juntos**, no por separado.
- [ ] Anoté los **timecodes de los momentos buenos** para sacar los verticales.
- [ ] Saqué al menos **6 cortos** de este video largo.
