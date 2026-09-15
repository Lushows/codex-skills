# 212 — Animaciones en CapCut: entrada, salida, bucle y combo

Una animación en CapCut es un movimiento prehecho que le ponés a un clip, a un texto o a un sticker.
No la construís vos: la elegís de una lista, le decís cuánto dura, y CapCut la ejecuta.

Es la función más rentable de todo el editor. Con dos clics, un título estático pasa a tener presencia
profesional. Y es también donde más se nota la diferencia entre alguien que sabe y alguien que no —
porque la mitad del trabajo está en **la duración**, no en cuál elegiste.

---

## Los cuatro tipos

CapCut divide las animaciones en cuatro pestañas. Entender qué es cada una te ahorra el 90 % de los
problemas.

| Tipo | Cuándo ocurre | Para qué sirve | Duración típica |
|---|---|---|---|
| **Entrada** (`in`) | Al principio del clip | Que el elemento *llegue* | 0,3 – 0,8 s |
| **Salida** (`out`) | Al final del clip | Que el elemento *se vaya* | 0,2 – 0,5 s |
| **Combo** | Todo el clip | Entrada + salida en un solo paquete | Todo el clip |
| **Bucle** (`loop`) | Todo el clip, repitiendo | Que el elemento *viva* mientras está en pantalla | Todo el clip |

La regla que resuelve casi todo:

> **Entrada + salida para textos que aparecen y desaparecen.
> Bucle para textos que se quedan un rato.
> Combo solo cuando te da pereza (y casi siempre te va a quedar peor que hacerlo a mano).**

---

## Cómo se ve por dentro

En el archivo del proyecto, las animaciones viven agrupadas. Cada grupo es de tipo
`sticker_animation` y adentro trae un arreglo `animations`. Cada animación individual se ve así:

```json
{
  "type": "in",
  "name": "Aparición progresiva",
  "duration": 500000,
  "id": "6798320778182922760",
  "resource_id": "6798320778182922760",
  "material_type": "video",
  "panel": "video",
  "start": 0,
  "path": ".../Cache/effect/<id>/<hash>",
  "platform": "all"
}
```

Lo que importa de ahí, sin ponernos técnicos:

- **`type`** es `in`, `out` o `loop`. Es literalmente la pestaña que elegiste.
- **`duration`: 500000** son **microsegundos**. Medio segundo. CapCut cuenta todo el tiempo en
  millonésimas de segundo. Si ves un número que parece absurdo, dividilo por 1.000.000.
- **`start`: 0** para las de entrada; para las de salida, CapCut calcula el arranque desde el final.
- **`panel`: "video"** dice a qué le aplica: video, texto o sticker. Cada uno tiene su lista propia
  de animaciones — no son intercambiables.
- **`path`** apunta a la caché local, igual que los efectos (módulo 211). Se descarga la primera vez
  que la usás.

Nota importante: **un mismo clip puede llevar entrada y salida a la vez**, y aparecen como dos objetos
dentro del mismo arreglo `animations`. Pero **no puede llevar bucle y entrada al mismo tiempo** — al
elegir bucle, CapCut te quita las otras.

---

## Lo que se usa de verdad

Datos reales de 51 proyectos tuyos:

| Animación | Tipo | Veces |
|---|---|---|
| *(bucle, varias)* | `loop` | 69 |
| Aparición progresiva | entrada | 49 |
| *(animaciones de subtítulo)* | caption | 47 |
| Flash desactivado | salida | 18 |
| Balanceo hacia la derecha | bucle | 6 |
| Flash activado | entrada | 5 |

Traducción de esa tabla: **usás dos animaciones y media.** Y está perfecto. Es exactamente lo que hace
un editor con criterio.

Fijate en el patrón que ya tenés armado sin darte cuenta:

- **Aparición progresiva (entrada) + Flash desactivado (salida)** es tu par por defecto para texto. Es
  un par excelente: entra suave, sale seco. Suave-seco es una combinación que funciona porque la
  entrada no distrae y la salida no deja al espectador esperando.
- **Bucle** para lo que se queda en pantalla. 69 usos: es tu recurso más frecuente.
- **Balanceo hacia la derecha** como el bucle con personalidad, para lo que necesita más presencia.

Si esto ya funciona, no lo cambies por aburrimiento. Cambialo solo cuando el proyecto pida otra cosa.

---

## Animaciones de entrada: el catálogo útil

De las decenas que hay, estas son las que aguantan uso repetido:

| Animación | Qué hace | Cuándo |
|---|---|---|
| **Aparición progresiva** | Fundido de opacidad | **El caballo de batalla.** Nunca estorba. Cuando dudás, esta. |
| **Deslizar** (arriba/abajo/izq/der) | Entra desde fuera del cuadro | Cuando querés dirección: texto que sube desde abajo se lee como "más info". |
| **Ampliar / Zoom** | Entra creciendo | Énfasis. Un dato, un precio. Cuidado: cansa rápido. |
| **Máquina de escribir** | Letra por letra | Solo para frases cortas y solo si el ritmo lo permite. Come tiempo. |
| **Flash activado** | Golpe de brillo | Para acentos duros, sincronizado al beat. |
| **Rebote** | Entra pasándose y vuelve | Energía juguetona. Se ve infantil si abusás. |

Duración recomendada para entradas: **0,3 a 0,8 segundos.** Menos de 0,3 y el ojo no la registra como
movimiento (se ve como un salto). Más de 1 segundo y el espectador está esperando a que termine para
poder leer — que es lo peor que le podés hacer a un texto.

**Cálculo que casi nadie hace:** si tu texto está en pantalla 1,5 segundos y le ponés una entrada de
0,8 s, el espectador tiene 0,7 segundos para leerlo. No alcanza. La animación se come el tiempo de
lectura. Regla: **la entrada no debe pasar del 25 % de la duración del clip.**

---

## Animaciones de salida: el catálogo útil

| Animación | Qué hace | Cuándo |
|---|---|---|
| **Desaparición progresiva** | Fundido | Neutro, siempre sirve. |
| **Flash desactivado** | Golpe y se va | **Tu favorita, y con razón.** Corta seco, no deja cola. |
| **Deslizar hacia fuera** | Sale del cuadro | Cuando la entrada también fue deslizando (simetría). |
| **Reducir / Zoom out** | Se encoge | Cierre de un bloque. |

Duración recomendada para salidas: **0,2 a 0,5 segundos.** Más cortas que las entradas, siempre.

**La razón de eso:** la entrada tiene que *invitar*, la salida solo tiene que *desocupar*. Una salida
larga hace que el espectador siga mirando algo que ya no le interesa. Es tiempo muerto.

---

## Bucles: la más incomprendida

Un bucle es un movimiento sutil que se repite mientras el elemento está en pantalla. Con 69 usos, es
tu herramienta más frecuente, así que vale la pena entenderla bien.

Para qué sirve realmente: **un elemento estático se vuelve invisible.** El ojo humano descarta lo que
no se mueve. Un título que respira ligeramente sigue siendo visto. Un título congelado se convierte en
parte del fondo a los dos segundos.

Los bucles que valen:

| Bucle | Qué hace | Cuándo |
|---|---|---|
| **Pulso / latido** | Crece y encoge apenas | Texto que se queda. El más discreto. |
| **Balanceo** (izq/der) | Se mece | Personalidad, algo juguetón. Tu elección para lo que necesita presencia. |
| **Flotar** | Sube y baja lento | Stickers, elementos gráficos. |
| **Vibrar / temblar** | Micro-sacudida | Alerta, urgencia. **Muy fácil de sobreusar.** |
| **Brillar** | Barrido de luz | Precios, ofertas. Chillón por naturaleza. |

Regla de bucles: **si lo notás conscientemente, está muy fuerte.** Un bucle bien puesto lo sentís pero
no lo ves. Bajale la intensidad hasta que casi dudes de si está activo — ahí está bien.

Y una regla más: **un bucle por pantalla.** Si tenés tres elementos meciéndose al tiempo, la pantalla
vibra y el espectador no sabe dónde mirar.

---

## Combos: por qué casi nunca los uso

Un combo es entrada + salida empaquetadas. Suena cómodo. Dos problemas:

1. **No controlás las duraciones por separado.** El combo reparte el tiempo como quiere, y casi
   siempre te da una salida demasiado larga.
2. **Entrada y salida suelen ser simétricas**, y la simetría es justamente lo que **no** querés
   (entrada suave 0,5 s + salida seca 0,25 s es la combinación que funciona).

Usá combos cuando estás haciendo 40 textos iguales y la velocidad importa más que la precisión. Para
lo que se ve en pantalla en el segundo 1, hacelo a mano.

---

## Animaciones de subtítulo (caption): categoría aparte

Cuando generás subtítulos automáticos, CapCut te ofrece animaciones específicas para ellos — con 47
usos en tus proyectos, claramente son parte de tu flujo.

Son distintas porque operan **palabra por palabra**, no sobre el bloque entero:

- **Resaltado / karaoke** — la palabra que se está diciendo se colorea. Es el estándar de TikTok.
- **Palabra por palabra** — cada palabra aparece cuando se pronuncia.
- **Escala por palabra** — la palabra hablada crece un poco.

Sirven muchísimo para retención: obligan al ojo a seguir el ritmo del habla. Pero:

- **Solo funcionan bien si la transcripción está bien sincronizada.** Si el timing está corrido, se ve
  peor que un subtítulo estático.
- **Consumen atención.** Si además tenés efectos y bucles, la pantalla se satura.
- **En textos largos son mareantes.** Bloques de 3 a 6 palabras, máximo.

Ver módulo 216 para el detalle de subtítulos.

---

## El sistema: dos pares y un bucle

Igual que con los efectos (módulo 211), lo que te da estilo no es la variedad, es la repetición
deliberada. Definí tres cosas y usalas siempre:

**Tu par estándar** — para el 80 % de los textos:
> Entrada: Aparición progresiva, 0,5 s · Salida: Flash desactivado, 0,3 s

**Tu par de énfasis** — para lo que tiene que golpear:
> Entrada: Flash activado / Ampliar, 0,3 s · Salida: Flash desactivado, 0,2 s

**Tu bucle** — para lo que se queda:
> Balanceo hacia la derecha o Pulso, intensidad baja

Con esos tres, resolvés cualquier pieza de redes. Y todas tus piezas se van a sentir de la misma
mano, que es lo que hace que una cuenta se vea profesional.

---

## Animaciones en clips de video (no solo texto)

Se puede, y casi nadie lo hace. Un clip de video con entrada *Ampliar* de 0,4 s le da un empujón al
corte. Es útil cuando:

- Abre una pieza (el primer plano entra creciendo).
- Después de un corte a negro.
- En un plano de recurso que aparece sobre la voz en off.

Advertencia: **si le ponés animación de entrada a cada clip de video, arruinaste el montaje.** El
corte duro es el recurso más poderoso que tenés. De hecho, tus 51 proyectos usan **una sola
transición en total** — todo lo demás es corte seco. Eso es criterio, no pereza. No lo pierdas
metiéndole animaciones a todo.

---

## Errores comunes

- **Entrada demasiado larga en texto corto.** Si el texto vive 1,5 s y la entrada dura 0,8 s, nadie
  alcanza a leer. La entrada no debe pasar del 25 % de la duración del clip.
- **Salida más larga que la entrada.** Se siente pesado. La salida siempre más corta.
- **Bucle demasiado fuerte.** Si lo notás, está mal. Bajale hasta que dudes de si está encendido.
- **Varios bucles al tiempo.** La pantalla tiembla y el espectador no sabe dónde mirar. Uno por
  pantalla.
- **Usar combo y después pelear con las duraciones.** Si vas a ajustar, hacelo a mano desde el
  principio.
- **Animación distinta en cada texto.** Es lo que más grita "amateur". Dos pares y un bucle, siempre
  los mismos.
- **Animar clips de video en cada corte.** Mata el ritmo. El corte duro es tu mejor herramienta.
- **Poner una animación de entrada al primer fotograma de un reel.** El espectador decide en 0,8
  segundos si se queda. Si en ese tiempo tu contenido todavía está "llegando", ya lo perdiste. El
  gancho arranca en pantalla, ya puesto.
- **Animación de subtítulo palabra por palabra con transcripción mal sincronizada.** Se ve peor que un
  subtítulo estático. Arreglá el timing primero.
- **Estirar el clip después de poner la animación.** A veces la animación no se re-escala y te queda
  una entrada de 0,5 s en un clip de 8 s, con 7,5 s de nada. Revisá.

---

## Checklist

- [ ] Definí mi par estándar (entrada + salida) y lo uso en el 80 % de los textos.
- [ ] Definí mi par de énfasis para lo que tiene que golpear.
- [ ] Definí un bucle y solo uno.
- [ ] Ninguna entrada pasa del 25 % de la duración de su clip.
- [ ] Todas mis salidas son más cortas que sus entradas.
- [ ] Hay un solo elemento con bucle activo por pantalla.
- [ ] El bucle está tan sutil que dudo si está encendido.
- [ ] El primer fotograma del video ya tiene el gancho puesto, sin animación de entrada.
- [ ] Los clips de video van a corte duro salvo excepciones justificadas.
- [ ] Si usé animación de subtítulo palabra por palabra, verifiqué que la sincronización esté bien.
- [ ] Revisé que ninguna animación quedó desproporcionada después de estirar o acortar su clip.
