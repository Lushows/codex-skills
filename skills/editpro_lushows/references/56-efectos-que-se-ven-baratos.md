# 56 — Efectos que se ven baratos: la lista negra honesta

> Este módulo existe porque la mayoría de los videos que "se ven amateur" no tienen un problema de
> cámara ni de luz. Tienen tres o cuatro efectos concretos que gritan "editado por alguien que apenas
> aprendió a usar el programa".

No es cuestión de gusto. Cada efecto de esta lista tiene una razón técnica o perceptual por la cual
se lee mal. Te doy la razón, no solo la prohibición — porque la razón te dice cuándo la excepción es
válida.

---

## La lista negra

### 1. El zoom con desenfoque (`zoomin`, "zoom blur transition")

**Qué es:** entre plano y plano, la imagen se acerca de golpe mientras se emborrona radialmente.

**Por qué se ve barato:**

- Es el efecto por defecto de todas las aplicaciones de edición para celular desde hace años. El
  espectador lo ha visto diez mil veces en contenido de bajo esfuerzo. **La asociación ya está hecha
  en su cabeza** y no la vas a deshacer.
- Dura demasiado. La versión de preset dura 0,4–0,6 s. Cualquier cosa vistosa que dure más de 0,3 s
  se lee como efecto, no como transición.
- No comunica nada. No hay paso de tiempo, ni cambio de lugar, ni cambio de tema. Solo hay zoom.
- Va sin sonido. Un movimiento fuerte sin apoyo sonoro siempre se siente hueco.

**La versión que sí funciona:** el golpe de escala del módulo `53` — 12–25% de aumento, 3 fotogramas,
con impacto de audio. Es el mismo principio ejecutado con criterio.

---

### 2. Las transiciones de "estrella", "corazón", "reloj de arena" y compañía

**Qué es:** el plano nuevo entra a través de una forma decorativa.

**Por qué se ve barato:**

- Son formas **sin relación con nada**. Una estrella que revela el plano de una hamburguesa no
  significa nada. El espectador lo lee como decoración, y la decoración gratuita es la firma del
  aficionado.
- Son el vocabulario de PowerPoint 2003 y de los editores gratuitos. Cargan esa asociación.
- Distraen del contenido justo en el momento del cambio, que es cuando el espectador está más
  atento.

**La excepción real:** si la forma **es de la marca**. Si el logo del cliente tiene un arco, un
revelado en forma de arco no es decoración: es identidad. Esa es exactamente la idea de `52`. La
diferencia entre "transición de corazón" y "transición de marca" es si la forma responde a algo.

---

### 3. El lens flare pegado encima

**Qué es:** un destello de lente sobreimpreso que atraviesa la pantalla.

**Por qué se ve barato:**

- Un flare real ocurre porque **hay una fuente de luz en el encuadre**. Si tu plano es una oficina
  con luz plana y le pones un flare, estás afirmando que hay un sol ahí. El ojo lo detecta como
  incoherente aunque el espectador no sepa explicarlo.
- Los flares de banco de recursos suelen venir en modo de fusión aditivo y a máxima opacidad. Lavan
  la imagen y se ven pegados, no integrados.
- Es un recurso de la estética de 2011. Cargó su época y se fue.

**Cuándo sí:** cuando **estabas filmando contra una luz** y el flare está en el material. Entonces no
lo estás poniendo: lo estás conservando. Eso sí es cine.

---

### 4. El glitch mal hecho

**Qué es:** la imagen se corta en franjas, se desplaza el color, aparece ruido digital.

**Por qué la mayoría se ve mal:**

- **Dura demasiado.** Un glitch real de transmisión dura 1 a 3 fotogramas. Los presets duran 15 a 30.
  Un fallo digital que dura medio segundo no es un fallo: es un adorno.
- **Es periódico y regular.** El preset repite el mismo patrón cada N fotogramas. Un error real es
  irregular. La regularidad delata la máquina.
- **No tiene sonido de error.** Un glitch visual sin distorsión de audio es una imagen rota en un
  mundo que suena perfecto. Incoherente.
- **Se aplica al video entero.** Un fallo de señal afecta la imagen completa por un instante, no un
  video de 40 segundos de forma continua.

**Cómo se hace bien:** 2–3 fotogramas, irregular, con corte de audio o distorsión en el mismo
fotograma, 1 o 2 veces en todo el video. Ver `57-glitch-y-textura.md` para los comandos.

---

### 5. El desenfoque de fondo falso (el "modo retrato" en video)

**Qué es:** emborronar todo menos al sujeto, con una máscara automática.

**Por qué se ve barato:** el borde. La separación entre sujeto enfocado y fondo borroso es demasiado
limpia y **cambia de forma en cada fotograma**. El pelo, los dedos y los objetos que el sujeto sostiene
parpadean entre enfocado y borroso. El ojo lo caza inmediatamente aunque no sepa qué está viendo.

**La alternativa real:** desenfoque óptico. Acercarse al sujeto y alejarlo del fondo produce
desenfoque de verdad, gratis, con cualquier cámara. Es una petición de rodaje (ver `171`).

---

### 6. La viñeta pesada

**Qué es:** oscurecer los bordes de la imagen.

**Por qué se ve barato cuando se abusa:** una viñeta sutil (que apenas se nota) es una herramienta
legítima de dirección de la mirada, y la usan los coloristas todos los días. Una viñeta que se ve
como un círculo oscuro **anuncia** que alguien puso una viñeta. Es la diferencia entre maquillaje y
disfraz.

**El número:** si puedes señalar dónde empieza la viñeta, es demasiada. Ver `66-viñeta-nitidez-y-textura.md`.

---

### 7. La saturación al máximo

**Qué es:** subirle el color a todo para que "se vea más vivo".

**Por qué se ve barato:**

- La piel es lo primero que se rompe. A saturación alta se pone naranja o roja. El ojo humano es
  extraordinariamente sensible a los tonos de piel: es lo único de la imagen de lo que todo el mundo
  tiene referencia perfecta. Ver `67-piel.md`.
- Se pierde detalle en los canales saturados. Un rojo al 100% deja de tener textura: se vuelve una
  mancha plana.
- La sensación de "vivo" en cine no viene de la saturación, sino del **contraste** y de la separación
  entre luces y sombras. Ver `63-look-cinematografico.md`.

---

### 8. Los subtítulos amarillos con contorno negro grueso, palabra por palabra

**Qué es:** el estilo de karaoke de TikTok.

**Por qué se ve barato en 2026:** porque es **la preset**. Es exactamente lo que sale por defecto en
todas las aplicaciones de subtítulos automáticos. En un video de marca, usar el estilo por defecto
comunica que no hubo decisión de diseño.

**Matiz honesto:** funciona. Retiene. Si el objetivo es puramente rendimiento y no hay marca que
sostener, no es un error grave. Pero para un cliente con identidad, es dejar la tipografía del cliente
en el cajón. Ver `44` y `49`.

---

### 9. El "beat sync" en cada golpe

**Qué es:** cortar exactamente en cada golpe de la música durante todo el video.

**Por qué se ve barato:** el ritmo se vuelve mecánico. Después de 15 segundos el espectador ya predice
cuándo va a cortar, y cuando el espectador predice, se aburre. Los buenos montajes musicales cortan
al beat el 60–70% de las veces y **rompen a propósito** el resto. Ver `24-ritmo-y-musica.md`.

---

### 10. El texto que entra con rebote elástico exagerado

**Qué es:** el título que llega, se pasa, vuelve, se pasa otra vez y se asienta.

**Por qué se ve barato:** el sobre-impulso (overshoot) es una herramienta real de animación, pero la
proporción correcta es **5–12% de exceso en 2–3 fotogramas**. Los presets hacen 40% en 15 fotogramas.
Eso ya no es peso: es un juguete. Ver `42-anatomia-del-golpe.md` y `84-keyframes-y-curvas.md`.

---

### 11. La música "corporate upbeat" de banco genérico

No es un efecto visual, pero pertenece a esta lista porque produce el mismo daño. El ukelele con
palmas dice "video de banco" antes de que empiece a hablar nadie. Ver `74-musica.md`.

---

### 12. La marca de agua gigante y opaca

Un logo al 100% de opacidad ocupando el 20% de la pantalla no protege nada y arruina cada plano. El
estándar profesional: 40–60% de opacidad, en una esquina, ocupando menos del 6% del ancho. Ver
`87-marca-de-agua-y-firma.md`.

---

## El patrón detrás de toda la lista

Si lees los doce, hay una estructura común. Todos los efectos baratos comparten al menos dos de estas
cuatro características:

| Característica | Por qué delata |
|---|---|
| **Duran demasiado** | Lo que es vistoso y dura, se lee como decoración |
| **Vienen sin sonido** | Un evento visual fuerte sin audio no existe en el mundo real |
| **No responden a nada** | No salen de la marca, ni de la historia, ni del material |
| **Son la opción por defecto** | Si es lo que sale al abrir el programa, todos lo han visto |

**El test rápido:** ¿este efecto lo elegí, o vino puesto? ¿Dura menos de 0,3 s? ¿Tiene sonido? ¿Puedo
explicar de dónde sale?

Si las cuatro respuestas están bien, el mismo efecto que está en esta lista puede funcionar. El
`zoomin` de `xfade` con 3 fotogramas, un impacto de audio y usado una vez en el video es el golpe de
`53`. El mismo filtro, otro resultado.

---

## Lo que hace que un video se vea CARO (el reverso)

Para no dejar solo la lista de lo que no:

1. **Contraste y separación de negros.** Un negro que es negro de verdad. Ver `63`.
2. **Audio limpio con presencia.** Es lo que más sube la percepción de calidad, más que la imagen.
   Ver `70`.
3. **Cortes duros bien elegidos.** Ver `54`.
4. **Tipografía de la marca, bien espaciada, en la zona segura.** Ver `44`, `45`.
5. **Sonido en cada evento visual.** Ver `76`.
6. **Consistencia de color entre planos.** Ver `62`.
7. **Menos efectos, mejor ejecutados.**

Cuesta más trabajo y menos filtros. Esa es toda la diferencia.

---

## Cómo se lo dices al cliente

Cuando un cliente pide un efecto de esta lista, no le digas "eso se ve barato". Te contrató, no le
pidas que sepa. Se dice así:

> "Ese efecto lo tienen todas las apps por defecto, entonces la gente ya lo asocia a contenido
> rápido. Como tu marca se está posicionando en [X], te propongo esto otro que hace lo mismo pero
> sale de tu identidad. Te muestro las dos versiones y decides."

Y muéstrale las dos. Un cliente que ve las dos versiones elige bien el 90% de las veces. La discusión
teórica no la gana nadie; la comparación la gana el trabajo.

---

## Errores comunes

- **Prohibir sin entender.** El problema no es el filtro: es la duración, el sonido, la frecuencia y
  la ausencia de motivo. Aprender la razón te deja usar el efecto bien.

- **Cambiar un efecto barato por otro efecto barato.** Sustituir `zoomin` por `pixelize` no arregla
  nada si sigue durando medio segundo, mudo y en cada corte.

- **Creer que quitar todos los efectos hace el video profesional.** Un video plano, sin ritmo, sin
  sonido diseñado y sin color, tampoco se ve caro. Se ve vacío.

- **Discutir con el cliente en abstracto.** Muéstrale las dos versiones renderizadas.

- **Aplicar la lista sin mirar el contexto.** Un video de nostalgia de los 90 puede querer glitch,
  VHS y flare. Ahí no son baratos: son el concepto. Ver `57`.

- **Dejar el estilo por defecto de subtítulos en una pieza de marca.** La tipografía del cliente
  existe. Úsala.

- **Subir saturación para "dar vida".** Rompe la piel primero. La vida viene del contraste.

- **Poner marca de agua enorme "para que no me roben".** Nadie roba el video; sí lo dejan de ver.

---

## Checklist

Antes de dejar cualquier efecto en el corte final:

- [ ] Puedo explicar de dónde sale: la marca, la historia o el material. No "venía puesto".
- [ ] Dura menos de 0,3 s si es una transición vistosa.
- [ ] Tiene un evento de audio acompañándolo.
- [ ] No es la opción por defecto del programa.
- [ ] No se repite en cada corte.
- [ ] Si hay glitch: dura 2–3 fotogramas, es irregular y hay distorsión de audio en el mismo cuadro.
- [ ] Si hay flare: había una fuente de luz real en el encuadre.
- [ ] Si hay viñeta: no puedo señalar dónde empieza.
- [ ] La piel no está naranja ni roja (`67`).
- [ ] Los subtítulos usan la tipografía de la marca, no la preset amarilla.
- [ ] El montaje musical rompe el beat a propósito en algún punto.
- [ ] Si el cliente pidió algo de esta lista, le preparé las dos versiones para comparar.
