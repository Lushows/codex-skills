# 338 — Continuidad entre tomas grabadas en momentos distintos

**Qué resuelve:** el corte que se siente raro y nadie sabe por qué. Pasa cuando dos tomas que van seguidas
en el video se grabaron con horas —o días— de diferencia. `26` explica cómo tapar un salto; este módulo
explica **cómo elegir qué tomas pueden vivir juntas** antes de montar nada.

---

## 1. El problema, con datos reales

El material de Bendita Pola del 4 de agosto parece un rodaje. Es cuatro rodajes. Los nombres de archivo
traen la hora, y la hora explica los números:

| Bloque | Hora | Tomas | YAVG | UAVG | Qué luz es |
|---|---|---|---|---|---|
| A | 12:28 – 12:57 | 0 a 4 | 72 – 104 | 122 – 149 | mediodía, mezcla de puerta y neón |
| B | 13:55 – 13:56 | 5, 6 | **101** | **117** | terraza, luz de día pura |
| C | 14:29 – 14:36 | 7, 8, 9 | 75 – 85 | **163** | salón, neón morado a tope |
| D | 15:54 – 16:16 | 10 a 15 | 71 – 77 | 141 – 150 | barra, neón y luz de tarde |

Casi cuatro horas entre la primera y la última toma. **Un corte del bloque B al bloque C mueve el brillo
medio 20 puntos y el color 46 puntos.** No hay corrección de color que empareje eso sin que se note
(`259`): son luces distintas sobre la misma cara, no un ajuste de ganancia.

Los cortes seguros son los de **dentro** del bloque: entre la 11 y la 12 hay 0,1 de diferencia de brillo y
2,4 de color. Invisible.

---

## 2. Las tres continuidades que rompen un corte

En orden de cuánto se notan de verdad en video vertical:

### a) Luz — la que más se nota

El espectador no sabe describirla, pero la ve al instante porque la cara cambia de color. Y en un formato
donde la cara ocupa medio cuadro, cualquier cambio de luz es un cambio de personaje.

**Umbrales de trabajo, medidos sobre este material** (con el método de `331`):

| Diferencia entre las dos tomas del corte | Qué pasa |
|---|---|
| `YAVG` menos de 5 y `UAVG` menos de 5 | invisible |
| `YAVG` 5–15 o `UAVG` 5–10 | se empareja con corrección primaria (`62`) |
| `YAVG` más de 20 o `UAVG` más de 15 | **se nota siempre**; hay que poner un puente |
| `UAVG` más de 30 | son escenas distintas. Trátalas como tales |

### b) Mirada y eje

Si en una toma la persona mira ligeramente a la izquierda y en la siguiente a la derecha, se lee como que
cambió de sitio. Es el problema del eje (`26`). En vertical, con la cara centrada, es más perdonable que
en horizontal — pero un cambio de mirada **entre planos del mismo tamaño** siempre se siente.

Regla de elección: para cortar seguidas, las dos tomas tienen que compartir **dirección de mirada** o
tener **tamaños de plano claramente distintos**. Una de las dos cosas.

### c) Vestuario y aspecto

Lo que cambia en cuatro horas y nadie anotó:

- **El nivel del vaso.** Es el delator número uno en un bar. Corta de un vaso lleno a uno por la mitad y
  el espectador lo nota aunque no sepa qué notó.
- **El hielo, la espuma, la condensación.** Una cerveza recién servida tiene espuma; a los diez minutos,
  no.
- **La comida.** Un plato mordido no vuelve atrás.
- **El pelo.** Cuatro horas de bar despeinan.
- **Sudor, brillo en la frente**, camisa arrugada, mangas subidas o bajadas.
- **Objetos en la mesa**: la botella que estaba a la izquierda ahora está a la derecha.

---

## 3. El método: agrupar antes de montar

Sobre la hoja de contactos (`333`), y antes de tocar la línea de tiempo:

1. **Ordena las tomas por hora** (los nombres de archivo del celular ya la traen; si no, `ffprobe` la
   saca del contenedor).
2. **Mide `YAVG` y `UAVG`** de una toma por bloque (`331`).
3. **Traza las fronteras** donde el color salta más de 15 puntos.
4. **Escribe la letra del bloque en cada casilla.**

```bash
# Fecha y hora de grabación, si el contenedor la trae
ffprobe -v error -show_entries format_tags=creation_time -of default=nw=1:nk=1 toma.mp4
```

A partir de ahí la regla es simple:

> **Se corta libremente dentro del bloque. Se cambia de bloque solo con un puente.**

---

## 4. Los puentes (en orden de solidez)

Cuando el video necesita saltar de un bloque a otro:

1. **Inserto de por medio.** Un primer plano de la botella, de las manos, del producto: 0,8 a 1,5 s. El
   ojo se reinicia y el cambio de luz se acepta. Es el puente más barato y el más efectivo.
2. **Cambio de escenario declarado.** Si se ve que ahora estamos en la terraza y antes estábamos en la
   barra, no hay salto: hay narración.
3. **Gráfico o cartela a pantalla completa.** Medio segundo de color plano con texto (`262`).
4. **Corte por acción.** Si el movimiento continúa, el cambio de luz se disimula bastante.
5. **Emparejar color.** Sirve solo dentro del rango medio de la tabla. Con 46 puntos de diferencia de
   `UAVG`, la corrección deja una cara enferma (`259`).
6. **Negro de 4 cuadros.** Funciona, pero en vertical se lee como "se acabó" y cuesta retención. Última
   opción.

---

## 5. La jerarquía honesta: qué importa de verdad

No todo lo de arriba pesa igual en un reel de 30 segundos que se ve en un celular:

| Rompe el video | Se nota pero se aguanta | Casi nadie lo ve |
|---|---|---|
| cambio fuerte de color de piel | mirada que cambia de lado | posición exacta de la botella |
| vaso lleno → vaso vacío | pelo distinto | arruga de la camisa |
| ropa distinta sin razón | brillo en la frente | altura de la silla |
| el mismo plano dos veces | tamaño de plano repetido | sombras del fondo |

Perseguir la columna de la derecha es perder la tarde. Ignorar la de la izquierda es publicar un video que
"se ve raro".

---

## 6. Lo que se anota en el rodaje para no llegar aquí

Cuesta cero pesos y lo puede hacer una persona sola con el celular:

- **Una foto del plato, del vaso y de la mesa** al empezar cada bloque. Es la referencia de continuidad.
- **Una foto de la persona de cuerpo entero** al empezar: ropa, mangas, pelo.
- **Anotar la hora de cada bloque** (el nombre del archivo ya lo hace).
- **Si el rodaje se parte en dos días**, repetir la foto antes de grabar el segundo día y compararlas.
- **Bloquear el balance de blancos** en la cámara. Con auto, la cámara cambia el color entre toma y toma
  aunque la luz sea la misma (`171`).
- **Grabar el material de un mismo bloque seguido**, sin ir a comer en la mitad.

Detalle completo en `175`.

---

## 7. El caso especial: dos días distintos

Si el segundo día no se puede igualar la luz (y casi nunca se puede), hay dos salidas honestas:

- **Convertir el cambio en estructura.** "Antes / después", "día 1 / día 7". El cambio de luz deja de ser
  un error y se vuelve el argumento (`155`).
- **Separar por escenario.** Todo lo del día 1 en un bloque del video, todo lo del día 2 en otro, con un
  puente claro entre ellos.

Lo que no funciona es intercalar cortes de un día y del otro esperando que la corrección de color los
una. No los une.

---

## Errores comunes

1. **Montar por orden de guion sin mirar la hora de grabación.** Se intercalan bloques de luz distintos
   sin darse cuenta.
2. **Creer que la corrección de color arregla un cambio de fuente de luz.** Arregla ganancia y
   temperatura, no el neón morado sobre la cara.
3. **Cortar de la terraza de día al salón morado sin puente.** 46 puntos de `UAVG`: se ve siempre.
4. **No mirar el nivel del vaso.** El delator número uno en un bar.
5. **Dejar el balance de blancos en automático.** Cada toma sale de un color distinto.
6. **No fotografiar la mesa antes de empezar.** Sin referencia, la continuidad es memoria, y la memoria
   miente.
7. **Perseguir la posición exacta de los objetos** mientras se ignora un salto de color enorme.
8. **Cortar entre dos planos del mismo tamaño y con la mirada cambiada.** Suma dos problemas.
9. **Usar negro para tapar un salto en vertical.** Se lee como final y la gente se va.
10. **Grabar un bloque, irse a comer y volver al mismo encuadre.** La luz cambió; ahora son dos bloques.
11. **Intercalar dos días esperando que nadie note.** Lo notan.
12. **Anotar nada.** Con dos fotos por bloque se resuelve casi todo.
13. **Descartar una toma por continuidad cuando bastaba un inserto de un segundo.**

---

## Checklist

- [ ] Ordené el material por **hora de grabación**.
- [ ] Medí `YAVG` y `UAVG` de **una toma por bloque**.
- [ ] Tracé las **fronteras de bloque** donde el color salta más de 15 puntos.
- [ ] Marqué la **letra de bloque** en cada casilla de la hoja de contactos.
- [ ] Los cortes seguidos son **dentro del mismo bloque**.
- [ ] Cada cambio de bloque tiene un **puente** (inserto, escenario, gráfico o acción).
- [ ] Revisé el **nivel del vaso, la espuma y el plato** entre tomas que van seguidas.
- [ ] Revisé **pelo, mangas y sudor** entre bloques lejanos.
- [ ] Las tomas que van seguidas comparten **dirección de mirada** o tienen **tamaños distintos**.
- [ ] No intenté emparejar por color una diferencia mayor a 20 puntos de `YAVG`.
- [ ] Si el rodaje fue en dos días, el cambio está **usado como estructura** o **separado con puente**.
- [ ] Para el próximo rodaje: foto de la mesa y de la persona al empezar cada bloque, y balance de blancos
      bloqueado.
