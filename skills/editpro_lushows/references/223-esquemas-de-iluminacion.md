# 223 — Esquemas de iluminación

**Qué resuelve:** `173` te enseñó a no arruinar la luz. Este te enseña a **dibujar con ella**. La
diferencia entre "se ve bien" y "se ve como una película" casi nunca es la cámara: es que alguien
decidió de dónde venía la luz, qué tan dura era y qué tan oscuro dejaba el otro lado de la cara.

Todo lo de aquí se hace con lo que ya hay en tu bar: **una ventana, las lámparas del salón, el neón y
un cartón blanco**. Al final hay una sección con lo que cambia si algún día compras una luz LED de
$200.000 (`229`). Nada de softboxes, trípodes de luz ni equipo de rodaje.

---

## 1. Los tres papeles de la luz

Toda la iluminación del mundo, desde una película de Hollywood hasta un reel de bar, se explica con
tres papeles. No son tres aparatos: son tres **funciones**. Una sola ventana puede hacer dos.

> **Luz principal (key):** la luz que manda. Es la que decide de dónde parece que viene la luz de la
> escena y la que dibuja las sombras de la cara. Si solo tienes una, es esta.

> **Relleno (fill):** luz suave del lado contrario que **aclara la sombra** que dejó la principal. No
> crea sombras nuevas; solo hace que las que hay sean menos negras. Un cartón blanco hace este trabajo
> perfectamente.

> **Contra o luz de borde (back / rim):** una luz **detrás** de la persona, apuntando a su nuca y
> hombros. No ilumina la cara: le dibuja un filo brillante en el pelo y el hombro que la **despega del
> fondo**. Es la que hace que un plano se sienta con volumen.

**Lo importante:** el 90% del efecto viene de la **principal** y del **contra**. Si tienes que elegir
dos, elige esos.

---

## 2. La relación de contraste: el número que define el estilo

Aquí está el concepto que convierte la iluminación en decisión y no en suerte.

> **Relación de contraste (ratio):** cuántas veces más luz recibe el lado iluminado de la cara respecto
> al lado en sombra. Se escribe 2:1, 4:1, 8:1. Cada duplicación es **un paso** (`222`).

| Relación | Diferencia | Cómo se ve | Para qué |
|---|---|---|---|
| **1:1** | 0 pasos | Cara plana, sin sombra. Videollamada. | ❌ Casi nunca |
| **2:1** | 1 paso | Sombra suave, amable | Publicidad, comida, testimonio simpático |
| **4:1** | 2 pasos | Sombra clara, con volumen | **El punto dulce para un bar** |
| **8:1** | 3 pasos | Sombra oscura, dramático | Noche, misterio, "historias de cerveza" |
| **16:1+** | 4 pasos | Media cara negra | Muy dramático, arriesgado en redes |

**Cómo se cambia sin comprar nada:** moviendo el cartón blanco. Cerca de la cara = más relleno = ratio
bajo. Lejos o quitado = ratio alto. **Ese cartón es tu perilla de contraste.**

**Cómo se mide de verdad**, con ffmpeg: recorta el lado iluminado de la cara y luego el lado en
sombra, y divide el primer número entre el segundo. Si da ~2, tienes 2:1; si da ~4, tienes 4:1.

```bash
# Cambia el 420 por el 560 para medir el otro lado de la cara.
# Ajusta las coordenadas a TU encuadre vertical.
ffmpeg -hide_banner -i clip.mp4 -vf "crop=120:120:420:640,signalstats,metadata=print:key=lavfi.signalstats.YAVG" -frames:v 10 -f null - 2>&1 | grep -o 'YAVG=[0-9.]*' | tail -1
```

---

## 3. La ley que explica el 80% de lo que pasa con la luz

> **Ley del inverso del cuadrado:** si alejas una luz al doble de distancia, llega **la cuarta parte**
> de luz. No la mitad: la cuarta parte.

```
Lampara a 1 m de la cara  -> 100 % de luz
Lampara a 2 m             ->  25 %
Lampara a 3 m             ->  11 %
Lampara a 4 m             ->   6 %
```

Tres consecuencias que usas todos los días. **Con la luz cerca, un paso atrás de la persona apaga
muchísimo**: si la lámpara está a 1 m de la cara, la pared a 3 m recibe casi nada, o sea **fondo oscuro
gratis** y separación gratis (`221`). **Con la luz lejos, todo recibe casi lo mismo**: a 5 m, cara y
pared quedan parecidas y el plano sale plano —por eso las luces de techo del bar aplanan todo. Y **es
la forma más barata de bajar la intensidad de algo**: ¿el neón te tiñe la cara? Camina un metro y su
efecto se cae a una cuarta parte (`224`).

**La regla operativa:** para que la cara resalte y el fondo caiga, **la luz principal va cerca de la
persona y lejos del fondo**.

---

## 4. Dura o suave: lo decide el TAMAÑO, no la potencia

> **Luz dura:** sombras de borde nítido, marcadas. Viene de una fuente **pequeña respecto a la persona**
> (el sol, la linterna del celular, un bombillo desnudo).

> **Luz suave:** sombras de borde difuso, amables. Viene de una fuente **grande respecto a la persona**
> (una ventana entera, un cielo nublado, una pared blanca que rebota).

La clave está en **"respecto a"**: es el tamaño **aparente**, cuánto ocupa la fuente vista desde donde
está la persona.

```
Ventana de 1,5 m de ancho, con la persona a 1 m   -> enorme -> luz muy suave
La MISMA ventana, con la persona a 5 m            -> pequenia -> luz dura
```

**Traducción:** para suavizar cualquier luz, **acerca a la persona a la luz**. Gratis, instantáneo.

**Las tres formas de suavizar en tu bar, sin comprar nada:** (1) **acercar** a la persona a la
ventana; (2) **difundir** con una cortina blanca delgada, una sábana o un mantel claro delante de la
ventana o de la lámpara —ojo con el calor si es incandescente—; (3) **rebotar**, apuntando la lámpara
a una pared o techo blanco: la pared entera se vuelve la fuente, y una pared es enorme. Es el mejor
truco de interiores que existe.

**Cuándo quieres luz dura:** para textura y drama. Un plano de botellas, del hielo, del vaso sudado. En
caras, la dura marca poros y arrugas: úsala a propósito o no la uses.

---

## 5. Los esquemas clásicos, traducidos a "ventana + cartón"

Estos nombres los usa todo el mundo. Aquí está cada uno con la instrucción exacta de dónde poner a la
persona en tu bar; la cámara siempre está de frente. En los dibujos: `V` = ventana o lámpara principal
· `C` = cartón blanco (relleno) · `P` = persona · `CAM` = celular en el trípode.

### a) Frontal plana (la que hay que evitar)

Luz de frente y a la altura de la cara, o sea justo detrás del celular. No hay sombra, no hay volumen.
**Es como se ve una videollamada y es como se ve el 90% de los reels.** Evítala.

### b) **Loop** — la de todos los días

Ventana a **45° de lado** y un poco **por encima** de los ojos. Deja una sombrita de la nariz que baja
en diagonal hacia la comisura, sin tocarla.

```
         V
          \
           \  45 grados
            P        C   <- carton al otro lado, a 1-1,5 m
            |
           CAM
```

**Por qué es la que más se usa en el mundo:** favorece a casi todas las caras, es fácil de acertar y se
ve natural. **Si dudas, haz loop.** Relación 3:1 o 4:1.

### c) **Rembrandt** — la de "esto se ve caro"

Igual que loop, pero la ventana **un poco más de lado y más alta**. La sombra de la nariz baja hasta
tocar la sombra de la mejilla y deja un **triangulito de luz bajo el ojo del lado oscuro**.

```
           V
            \
             \  60 grados, mas alto
              P     C  (carton mas lejos o quitado)
              |
             CAM
```

Ese triángulo es la firma. Se ve pintado, con volumen, serio. Va perfecto para hablar de la historia
del bar o de una cerveza. Relación 4:1 u 8:1. **Cómo lo aciertas:** mueve a la persona en pasitos de
15° mirando la pantalla hasta que el triángulo aparezca. Veinte segundos.

### d) **Split** (partida) — la dramática

Luz a **90°, totalmente de lado**. Media cara iluminada, media en sombra.

```
      V ---- P     C
             |
            CAM
```

Fuerte, arriesgada, memorable. En un bar de noche con neón atrás, se ve espectacular. En un video de
"pedí a domicilio", se ve amenazante. Úsala cuando el tono lo pida.

### e) **Mariposa / Paramount** — la de belleza

Luz **de frente pero alta**, unos 45° apuntando hacia abajo. Deja una sombra de mariposa justo debajo
de la nariz.

Adelgaza la cara y marca los pómulos. Es la de las fotos de revista. En tu bar: una lámpara colgante
sobre la mesa hace esto sola. Cuidado: si la luz está **demasiado** alta, los ojos se hunden en sombra.
Un cartón blanco abajo, sobre la mesa, devuelve luz y arregla eso al instante.

### f) **Corta vs larga** (el ajuste fino que casi nadie conoce)

Si la persona está de tres cuartos (no de frente): **luz corta** = la luz cae en el lado de la cara que
está **más lejos** de la cámara, el lado ancho queda en sombra y **adelgaza** (es la que quieres el 90%
de las veces). **Luz larga** = la luz cae en el lado **más cerca** de la cámara y **ensancha**; sirve
si la persona es muy delgada o si quieres un aire más comercial.

Cambiar de una a otra es **girar a la persona**, no mover la luz. Es el truco más barato para que
alguien se vea mejor en cámara.

---

## 6. El contra: la luz que de verdad separa

Si tuvieras que quedarte con un solo truco de este módulo, es este.

Una luz **detrás y arriba** de la persona, fuera de cuadro, apuntando a su nuca. Dibuja un filo
brillante en el pelo y el hombro. Efecto: la persona se **despega** del fondo, aunque el fondo esté
oscuro y nítido.

```
             (fuente de contra)
                 \
                  \
                   P
                   |
                  CAM
```

**En tu bar tienes al menos cuatro fuentes de contra, gratis:** el **neón de la pared** (persona de
espaldas a él, a 1,5–2 m: da un borde de color precioso), una **lámpara colgante** del salón (persona
justo debajo y un paso adelante), la **nevera de cervezas** con la puerta abierta, y la **linterna de
un segundo celular** apoyada en una repisa detrás, apuntando a la nuca.

**La regla de intensidad:** el contra debe ser igual o un poco más fuerte que la principal en esa zona
concreta. Si es muy tenue no se ve; si es exagerado, el pelo se quema en blanco.

**La combinación que te va a resolver los videos del bar de noche:**

```
Neon morado DETRAS a 2 m  ->  hace de contra (borde de color en el pelo)
Lampara del bar o LED     ->  hace de principal, a 45 grados, cerca de la cara
Carton blanco             ->  hace de relleno al otro lado
Fondo                     ->  el salon a 5 m, oscuro y desenfocado
```

Ese es el plano que se ve caro. Tres elementos, todos gratis salvo el cartón.

---

## 7. Luz motivada: la regla que hace que se vea real

> **Luz motivada:** la luz parece venir de algo que existe en la escena. Una ventana, una lámpara, el
> neón, una vela.

Si pones una luz que no se explica —una cara perfectamente iluminada en un rincón donde no hay nada que
ilumine—, el ojo del espectador no lo razona pero **lo siente falso**.

Cómo se aplica sin pensar mucho: mira dónde está la luz **real** de ese rincón del bar, pon a la
persona de forma que **esa** luz sea la principal, y si necesitas más luz, ponla **desde la misma
dirección** que la fuente real, nunca desde el lado contrario.

Es un truco de coherencia, y es también la razón por la que un video grabado en el bar con la luz del
bar puede verse mejor que uno con luces alquiladas mal puestas.

---

## 8. Tres recetas completas para tu bar

Cada una: dónde va la persona, dónde va la cámara, qué haces con el cartón. Todas se montan en menos de
5 minutos, tú solo.

**Receta 1 — "Terraza de día, mensaje comercial"** (el más amable)

```
Ventana o cielo abierto a 45 grados adelante de la persona, un poco por encima.
Persona a 3 m del fondo. Carton blanco al otro lado, a 1 m.
Celular en 2x, a 2,6 m, altura de los ojos.
Relacion objetivo 2:1 o 3:1. Todo claro, sin sombras duras.
```
Para qué: promociones, menú, "estamos abiertos", cualquier cosa que deba verse limpia y confiable.

**Receta 2 — "Barra de noche, historia del bar"** (el que se ve caro)

```
Lampara del bar o LED barato a 45 grados, CERCA de la cara (1 m).
Neon a 2 m DETRAS de la persona, haciendo de contra.
Carton al lado contrario, retirado (o sin carton) -> relacion 4:1 u 8:1.
Fondo del salon a 5 m, oscuro. Celular en 3x si el espacio da.
```
Para qué: historias, marca, "por qué abrimos este bar", contenido de identidad (`36`).

**Receta 3 — "Producto sobre la barra"** (el que vende)

```
Ventana o LED a 90 grados de LADO respecto al vaso, un poco por DETRAS.
Es luz de contra lateral: hace brillar el liquido, la condensacion y el hielo.
Carton blanco al frente para que la etiqueta se lea.
Fondo oscuro. Celular en 2x a 45 cm.
```
Para qué: cerveza, cóctel, plato. La bebida se ilumina **desde atrás**, nunca de frente: el líquido se
enciende y se ve apetecible. De frente se ve opaco. Detalle en `153`.

---

## 9. Y si algún día compras una luz

Nada de lo anterior requiere comprar. Pero si compras un panel LED pequeño (`229` tiene precios reales
de Colombia, desde unos $200.000):

**va donde iba la ventana**, en el mismo sitio de los esquemas de la sección 5: a 45° y por encima de
la línea de los ojos, nunca de frente ni a la altura de la cara; **cerca** de la persona (1–1,5 m) para
que sea suave y para que el fondo caiga; con un pañuelo blanco o papel de cocina delante si la sombra
sale dura; y si es bicolor, **fíjala en un valor** y no la muevas en todo el rodaje (`228`).

**Lo que sigue siendo verdad:** una ventana grande es mejor luz que casi cualquier LED barato. El LED
gana solo cuando es de noche.

**Esto es si algún día contratas a alguien:** los softboxes, banderas negras, difusores en marco,
trípodes de luz y esquemas de cuatro puntos son de rodajes con equipo y con un tercero manejándolos.
Con tu celular, tú solo, en tu bar, no aportan nada que no consigas moviendo a la persona y un cartón.

---

## Errores comunes

1. **Luz de frente y a la altura de la cara.** Aplana los rasgos y se ve a videollamada. 45° y por
   encima de los ojos.
2. **No poner nada de relleno.** Con solo la principal, la sombra queda negra y con ruido. Un cartón a
   1 m arregla la mitad de los problemas de tu material.
3. **No usar contra.** Es la diferencia más grande entre "plano" y "con volumen", y en tu bar la fuente
   ya existe: el neón.
4. **Poner la luz principal lejos.** Lejos = dura, plana y encima ilumina el fondo. Cerca = suave y con
   caída de fondo gratis.
5. **Confundir potencia con suavidad.** La suavidad la da el **tamaño aparente**, no los vatios. Acerca
   la fuente o rebótala en la pared.
6. **Luz demasiado alta.** Los ojos se hunden en sombra y la persona se ve cansada. Un cartón abajo lo
   arregla.
7. **Iluminar el lado ancho de la cara (luz larga) sin querer.** Ensancha. Gira a la persona para que
   la luz caiga en el lado más lejano a la cámara.
8. **Luz que no se explica.** Una cara brillante donde no hay ninguna fuente visible se siente falsa.
   Motiva la luz con algo del bar.
9. **Cambiar el esquema entre tomas del mismo bloque.** Salto de luz en cada corte, imposible de
   emparejar (`173`).
10. **Iluminar la bebida de frente.** Se ve opaca. La bebida se ilumina de lado y por detrás.
11. **Creer que hace falta comprar luces.** Ventana + cartón + neón + lámpara del bar cubre el 95% de
    lo que necesitas para reels de 15 a 90 segundos.
12. **No mirar la sombra de la nariz.** Es el indicador gratis: sombra en diagonal sin tocar el labio =
    loop, bien. Sombra que llega hasta el labio o cruza la cara = mueve a la persona.

---

## Checklist

- [ ] Sé cuál es mi **luz principal** y está a **45° y por encima** de la línea de los ojos.
- [ ] Hay **relleno** (cartón blanco, mantel, pared clara) del lado contrario.
- [ ] Hay **contra**: neón, lámpara o linterna detrás dibujando el borde del pelo y el hombro.
- [ ] La **relación de contraste** es la que quiero (2:1 comercial, 4:1 general, 8:1 dramático) y la
      ajusté moviendo el cartón.
- [ ] La luz principal está **cerca** de la persona y **lejos** del fondo.
- [ ] La luz es **suave** (fuente grande respecto a la persona) salvo que quiera dureza a propósito.
- [ ] La luz está **motivada**: se explica con algo que existe en el bar.
- [ ] Si la persona está de tres cuartos, la luz cae en el **lado lejano** a la cámara (luz corta).
- [ ] La **sombra de la nariz** cae en diagonal y no toca el labio.
- [ ] Se ve un **brillo en los ojos** (catchlight); si no, la luz está muy alta o muy de lado.
- [ ] El **esquema no cambia** dentro del mismo bloque.
- [ ] Medí la relación con ffmpeg al menos una vez para calibrar mi ojo.
