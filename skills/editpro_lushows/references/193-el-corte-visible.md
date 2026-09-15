# 193 — El corte visible

Resuelve el problema contrario al de `192`. Ahí el objetivo era que el corte desapareciera. Aquí el
corte **es** el contenido: se ve, se siente, y esa sensación es parte de lo que el video comunica.

El video vertical vive casi entero en este territorio, y por eso está lleno de gente haciéndolo mal:
copian la apariencia (cortar rápido, saltar, poner glitches) sin la lógica. El corte visible bien
hecho no es "cortar más". Es **usar la ruptura como un signo de puntuación** que dice algo que el
contenido no dice.

---

## De dónde viene: la ruptura como decisión

### El jump cut y su acta de nacimiento

Un **jump cut** es cortar dentro del mismo plano quitando un pedazo del medio: la cámara no se
movió, el encuadre es casi igual, y la persona "salta". Durante cincuenta años se consideró un
error de principiante.

*À bout de souffle* (Jean-Luc Godard, 1960), montada por **Cécile Decugis** con **Lila Herman**, la
convirtió en lenguaje. Circulan varias versiones sobre el origen —la más repetida dice que la
película quedó larga y que en vez de sacar escenas enteras sacaron pedazos de adentro—, y no todas
las fuentes coinciden en el detalle. Lo que sí está documentado es el criterio, y es lo que
importa: **se quitó todo lo que no tenía energía, sin importar la continuidad.**

Ese es el permiso que la nouvelle vague le dio al oficio y que todavía usas todos los días: **la
continuidad no es sagrada; la energía sí.**

### Cómo llegó a tu teléfono

Tres saltos:

1. **1967, *Bonnie and Clyde*.** Dede Allen mete cortes bruscos y velocidades mezcladas en una
   película de estudio. La ruptura entra a Hollywood.
2. **1981–1995, MTV.** El videoclip normaliza el corte al golpe, el texto en pantalla, el plano que
   existe por impacto y no por información. Ver `190`.
3. **2005–2016, YouTube.** El jump cut deja de ser vanguardia y se vuelve **higiene**: quitar los
   "eh", las pausas, los arranques falsos. Nadie lo hizo por Godard; lo hicieron porque la retención
   caía.

Hoy el jump cut es tan normal que **lo raro es no cortar**. Eso invierte el significado: en 1960
cortar era ruptura; en 2026 **no cortar es la ruptura**. Vale la pena tenerlo presente cada vez que
alguien te diga "hazlo más dinámico".

---

## Las cinco familias del corte visible

### 1. Jump cut (compresión)

Quitar el aire dentro de un mismo plano.

**Para qué sirve de verdad:** densidad. Una persona hablando 90 segundos comprimida a 30 sin perder
una sola idea. Cada segundo que queda tiene contenido.

**Cómo se hace bien:**
- **Deja respirar el arranque.** No empieces con jump cut; que la primera frase corra completa para
  que el espectador se instale.
- **No cortes exactamente en el mismo encuadre.** Alterna con punch-in del 25–35%: el salto se
  siente intencional, no accidental. Es la diferencia entre "estilo" y "se le rompió el video".
- **Corta en el silencio entre palabras, no en la palabra.** Busca el valle de la onda.
- **No hagas más de tres o cuatro seguidos sin un plano de otra cosa.** El ojo se fatiga.

```bash
# Quitar automáticamente los silencios largos de un talking head (aproximación rápida
# para el corte bruto; después se afina a mano).
ffmpeg -i habla.mp4 -af silencedetect=noise=-30dB:d=0.35 -f null - 2>&1 | grep silence_
# Con las marcas que salen, se construyen los trim/atrim del corte definitivo.
```

**Cuándo NO usarlo:** testimonios donde la credibilidad manda, demostraciones de resultado, y
cualquier contenido donde alguien podría acusarte de haber sacado algo de contexto. Ahí el jump cut
se lee como "le quitaron algo". Ver `192` y `197`.

### 2. Montaje rítmico (el corte como percusión)

Los cortes caen con la música y la duración de los planos construye un pulso.

**La trampa:** sincronizar todo al beat produce lo que Eisenstein llamaba **montaje métrico**, el más
pobre de los cinco (`191`). Es lo que hace el botón de "beat sync" de CapCut, y es exactamente lo
que el público ya reconoce como plantilla.

**Cómo se sale de la plantilla, en concreto:**
- **No cortes en todos los golpes.** Corta en uno de cada dos, o de cada cuatro. Los golpes vacíos
  crean expectativa; los golpes llenos la resuelven.
- **Corta a veces medio tiempo antes del golpe.** El corte adelantado se siente urgente; el corte
  atrasado se siente pesado. Los dos son herramientas.
- **Que la duración de los planos varíe.** 8, 8, 8, 8 es cuadrícula. 8, 8, 4, 4, 2, 2, 16 es una
  frase.
- **Guarda el corte grande para el cambio de la canción,** no para un golpe cualquiera.

Ver `24` para la técnica completa.

### 3. Ruptura marcada (el corte que anuncia un cambio)

Es el signo de puntuación: le dice al espectador "hasta aquí una cosa, ahora otra".

Las formas útiles, de menos a más ruidosas:

- **Corte a negro de 2–4 cuadros.** Casi invisible pero se siente como punto y aparte. La más
  elegante que existe.
- **Corte a blanco (flash).** Más agresivo; funciona en contenido energético.
- **Silencio total de medio segundo.** La ruptura más fuerte de todas y no es visual. Cortar el
  sonido antes de una frase importante multiplica su peso. Casi nadie la usa.
- **Cambio de relación de aspecto o de tratamiento de color.** Todo lo del "antes" en desaturado y
  todo el "después" en color: la ruptura ya no es un corte, es un sistema.
- **Whip pan / barrido.** Un movimiento rápido que empasta dos planos. Requiere que los dos tengan
  movimiento; si lo fabricas con un desenfoque digital, se nota.
- **Speed ramp.** Acelerar y frenar de golpe. Muy usado, muy quemado; funciona cuando el frenazo
  cae sobre algo que importa (el producto, la cara, el número), no sobre cualquier cosa.
- **Glitch, RGB split, shake.** Los que más se usan y los que menos comunican. Regla dura: si el
  efecto podría estar en cualquier otro video sin cambiar nada, es relleno.

### 4. Corte de choque (Eisenstein en 20 segundos)

Dos planos juntos que producen una idea que ninguno tiene solo. Es el corte visible más valioso y el
que menos se usa.

Cuatro moldes que funcionan en video comercial:

| Molde | Ejemplo |
|---|---|
| **Contraste de escala** | La moneda → la caja llena |
| **Antes / después sin transición** | El corte duro golpea más que cualquier barrido |
| **Contradicción** | Lo que dice contra lo que se ve (arma de doble filo, ver `197`) |
| **Repetición con variación** | El mismo encuadre tres veces, algo cambió |

La regla de Anne V. Coates aplicada (`03`): **un corte de choque se puede resumir en una frase.** "De
la llama que él apaga al sol que nadie apaga." Si tu corte no se puede decir así, no es un choque:
es una transición.

### 5. Ruptura del sistema (romper la regla a propósito)

Cruzar el eje, cortar contra el movimiento, saltar de un tamaño de plano al mismo tamaño, meter un
plano que no pertenece. Todo lo que `192` y `26` prohíben, hecho **a sabiendas y una sola vez**.

Funciona por la misma razón por la que funciona una grosería en un texto formal: **porque el resto
está en orden**. Si rompes el sistema todo el tiempo, no hay sistema que romper y no hay efecto.
La ruptura cuesta y solo se paga una vez por video.

---

## La pregunta que separa el estilo del ruido

Antes de dejar cualquier corte visible en el montaje:

> **¿Qué dice este corte que el contenido no dice?**

Respuestas válidas: "dice que pasó tiempo", "dice que esto es otra cosa", "dice que se aceleró",
"dice que hay que poner atención aquí", "hace el chiste", "hace la comparación".

Respuestas inválidas: "se ve bacano", "porque así se usa", "para que no se vea quieto", "porque el
cliente pidió que fuera dinámico".

Si la respuesta es inválida, ese corte está gastando atención sin comprar nada. La atención es el
único recurso escaso del video corto (`06`), y las transiciones son caras.

---

## La economía de la ruptura

Piensa en el corte visible como en el picante: sube el plato o lo arruina, y la diferencia es la
cantidad.

Reglas de dosis que aguantan la prueba de la práctica:

- **Una ruptura fuerte por video corto.** Una. Si tu reel de 30 segundos tiene cuatro glitches, tres
  speed ramps y dos flashes, no tiene ninguno: tiene ruido de fondo.
- **El efecto más fuerte va donde está el momento más importante.** Si el frenazo cae sobre una
  imagen cualquiera, gastaste tu única bala.
- **Cada transición decorativa que quites mejora el video.** Prueba a quitarlas todas y volver a
  meter solo las que extrañas. Casi nunca extrañas más de una.
- **Si el video funciona sin la ruptura, no la metas.** El corte visible es para cuando el corte
  duro no alcanza.

---

## Lo que caduca y lo que no

Los efectos de moda tienen fecha de vencimiento corta y visible. El zoom brusco con distorsión, el
glitch RGB, el "velvet" de transiciones descargadas, el efecto VHS: cada uno tuvo su año, y un video
con el efecto del año pasado se ve más viejo que un video sin ningún efecto.

Lo que no caduca:

- **El corte duro.**
- **El corte a negro corto.**
- **El silencio.**
- **El cambio de ritmo.**
- **El corte de choque.**

Todos son gratis, ninguno depende de un plugin, y todos siguen funcionando igual que en 1925. Si tu
estilo se construye con esos cinco, tus videos de hoy se van a ver bien en tres años. Si se
construye con los efectos de moda, se van a ver fechados en seis meses. Ver `196`.

---

## Corte visible y corte invisible en el mismo video

No son dos escuelas: son dos registros del mismo idioma, y los videos buenos usan los dos.

Un molde que funciona casi siempre en video comercial de 30–45 segundos:

| Sección | Registro | Por qué |
|---|---|---|
| **Gancho (0–3 s)** | Visible, agresivo | Hay que ganar la atención de alguien que no eligió esto |
| **Cuerpo / explicación** | Invisible, voz continua, imagen picada encima | Aquí hay que entender y creer |
| **Prueba / demostración** | Invisible extremo, sin cortar | Aquí hay que creer sobre todo (Bazin, `191`) |
| **Remate / cierre** | Visible, ruptura marcada | Hay que recordar y hay que actuar |

Cuando alguien dice "no me gustó, se siente amateur", nueve de cada diez veces el problema es que
usó el registro del gancho durante todo el video.

---

## Errores comunes

- **Confundir "dinámico" con "muchos cortes".** Dinámico es que cambie la energía. Un video de
  cuarenta cortes iguales es monótono a alta velocidad.
- **Jump cut en el mismo encuadre exacto.** Se lee como error de archivo. Alterna con punch-in.
- **Empezar con jump cuts desde el primer segundo.** El espectador no alcanzó a instalarse y siente
  ansiedad, no ritmo.
- **Sincronizar todos los cortes con todos los golpes.** Montaje métrico puro: plantilla.
- **Gastar la ruptura fuerte en un momento cualquiera.** El frenazo va donde está el producto, la
  cara o el número, no en el plano cinco.
- **Acumular efectos.** Glitch + shake + flash + speed ramp al tiempo = nada.
- **Jump cut en un testimonio.** Cuesta credibilidad y, en ciertos contenidos, cuesta más que eso
  (`197`).
- **Usar transiciones descargadas de un pack.** Están en diez mil videos y el público las reconoce
  como plantilla antes de leer una palabra tuya.
- **Creer que el efecto suple contenido flojo.** Nunca ha funcionado. Un corte visible sobre nada
  sigue siendo nada, pero más ruidoso.
- **No saber cuál registro estás usando.** El peor error de todos, porque no se puede corregir hasta
  que se nombra.

---

## Checklist

De reflexión, sobre un corte tuyo que ya esté armado.

- [ ] ¿Puedo decir en una frase qué dice cada corte visible de mi video? ¿Cuántos sobreviven la
      pregunta?
- [ ] ¿Cuántas rupturas fuertes tengo? Si son más de una en un video corto, ¿cuál me quedo?
- [ ] Mi ruptura más fuerte, ¿cae sobre el momento más importante del video?
- [ ] ¿Mi ritmo viene del contenido o de la canción? Si le quito la música, ¿sobrevive?
- [ ] ¿Los planos duran todos parecido? Si sí, tengo cuadrícula, no frase.
- [ ] ¿Usé algún efecto que podría estar en el video de cualquier otra persona sin cambiar nada?
- [ ] ¿Hay alguna sección del video que necesitaba el registro invisible y le puse el del gancho?
- [ ] Si quito todas las transiciones y dejo cortes duros, ¿qué extraño de verdad?
- [ ] Los efectos que usé, ¿van a verse bien dentro de dos años, o son del año pasado?
- [ ] ¿Estoy rompiendo una regla porque la conozco, o porque no la conocía?
