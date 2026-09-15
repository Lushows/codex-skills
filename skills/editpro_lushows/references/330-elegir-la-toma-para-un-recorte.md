# 330 — Elegir la toma para un recorte de sujeto

**Qué resuelve:** el momento en que vas a quitarle el fondo a una persona y tienes que decidir **con cuál
de todas las tomas** lo haces. Esa decisión define el 80% del resultado. La técnica de recorte define el
20% restante.

---

## 1. El error que originó este bloque

Caso real, documentado, del material de Bendita Pola grabado el 4 de agosto.

Había que probar una técnica: recortar a la persona y componerla sobre una ilustración. En la carpeta
`videos/entrada` había **16 tomas**. Se abrió la carpeta, se tomó **el primer archivo de la lista** y se
trabajó con ese.

El primer archivo era `lv_0_20260804122837.mp4`: el plano de las escaleras. La persona sube desde la
puerta de la calle, **a contraluz**, recortada contra un vano de luz quemada, ocupando unos 60 píxeles de
ancho en un cuadro de 1080, entre barandas metálicas, neón rojo arriba y escalones con filos negros.

Es, sin discusión, **la peor toma de las 16 para un recorte**. Y no se eligió por mala suerte: se eligió
por orden alfabético. Nadie la comparó con nada. El dueño lo notó en el primer vistazo.

> ## La lección
> **Elegir el material es una decisión técnica con criterios medibles. No es un trámite previo al trabajo:
> es la primera parte del trabajo, y la que más pesa.**

Nadie que elija por orden de archivo puede decir que "la técnica no funcionó". La técnica no llegó a
probarse.

---

## 2. Los cinco factores que deciden si una toma se recorta

En orden de peso real. Los dos primeros valen más que los otros tres juntos.

### a) Contraste entre sujeto y fondo — el factor rey

El recorte, sea por IA o por croma, necesita **una diferencia** entre lo que está adelante y lo que está
atrás. Puede ser diferencia de **brillo** o de **color**. Si no hay ninguna de las dos, no hay recorte.

- Persona clara sobre pared oscura → fácil.
- Persona oscura sobre ventana quemada (contraluz) → **la silueta se traga la cara**. El algoritmo sí
  encuentra el contorno, pero adentro no hay nada que valga la pena mostrar.
- Persona con camiseta vino tinto sobre piso vino tinto → el recorte se come la camiseta.

### b) Complejidad del borde

No importa cuántos detalles tenga el fondo **en general**. Importa cuántos tiene **pegado al contorno del
sujeto**. Una baranda que cruza justo por el hombro es peor que una pared llena de cuadros a tres metros.

Enemigos clásicos, en orden de crueldad: rejas · persianas · escalones vistos de frente · plantas ·
sillas apiladas · gente al fondo.

### c) Pelo

El pelo suelto, con luz por detrás, es el borde más difícil que existe. Con pelo corto o recogido el
recorte es un problema resuelto; con pelo suelto y movimiento, es rotoscopia (`261`).

Barba: se comporta como pelo, pero como está pegada a la cara y no se mueve sola, casi siempre pasa.

### d) Movimiento

Dos movimientos distintos, dos problemas distintos:

| Movimiento | Efecto en el recorte |
|---|---|
| El sujeto camina despacio | manejable |
| El sujeto gesticula rápido | el brazo se vuelve un borrón sin borde → se corta en seco |
| La cámara está a pulso | el fondo se mueve; se pierde la placa limpia y el matte "hierve" |
| Todo quieto (trípode + persona sentada) | el mejor escenario posible |

### e) Ropa del color del fondo

Es el factor que más veces arruina una toma que parecía buena, y el más fácil de evitar **antes** de
grabar. Camiseta marrón + mesa de madera + luz cálida = tres cosas del mismo color. El recorte no las
distingue porque **en YUV literalmente son casi el mismo valor**.

---

## 3. Cómo se ven esos cinco factores en las 16 tomas reales

Medidas reales del material (procedimiento y comandos en `331`). Cada fila es un fotograma al 30% de la
toma, escalado a 540 px de ancho.

| # | Toma | Qué es | UAVG | Bordes | Veredicto |
|---|---|---|---|---|---|
| 1 | 122837 | escaleras, contraluz | 128,0 | 4,24% | **descartar** |
| 2 | 123726 | pasillo, sujeto lejos | 148,5 | 3,82% | fondo, no sujeto |
| 3 | 123910 | pasillo **sin nadie** | 149,3 | 3,95% | placa limpia (`261`) |
| 4 | 124427 | mano abriendo botella | 121,7 | **1,55%** | inserto excelente |
| 5 | 125739 | barra, plano medio | 146,6 | 4,00% | usable |
| 6 | 135553 | terraza, luz de día | **117,8** | 6,70% | **candidata** |
| 7 | 135656 | terraza, a cámara | **117,4** | 6,30% | **la buena** |
| 8 | 142916 | salón morado, lejos | 163,6 | 5,42% | color imposible |
| 9 | 143116 | salón morado, lejos | 162,5 | 4,99% | color imposible |
| 10 | 143641 | cuerpo entero, morado | 163,6 | 4,83% | color imposible |
| 11–15 | 1554–1614 | barra, plano medio | 141–143 | 3,0–3,1% | usables con trabajo |
| 16 | 161648 | barra **sin nadie** | 149,9 | 2,59% | placa limpia |

`UAVG` es la media del canal U. **La piel sana siempre tiene U por debajo de 128.** Las tomas 8, 9 y 10
están en 163: ahí no hay piel posible, hay neón morado sobre una persona. Las tomas 6 y 7 están en 117 —
luz de día en la terraza — y son las únicas con piel de verdad.

`Bordes` es el porcentaje de píxeles que `edgedetect` marca como borde: mide qué tan enredado está el
cuadro.

**La toma elegida a ciegas fue la 1.** La mejor era la 7. Están a nueve horas de distancia en la carpeta
y a un mundo de distancia en calidad.

---

## 4. El orden de descarte: tres preguntas, treinta segundos

No empieces puntuando. Empieza **matando** candidatas.

1. **¿Se le ve la cara con luz?** Si es una silueta, contraluz o está a diez metros → fuera. (Mata la 1,
   la 2, la 8 y la 9.)
2. **¿Hay algo pegado al contorno?** Baranda, marco de puerta, planta que le sale del hombro → fuera o a
   la cola. (Baja la 5.)
3. **¿La ropa se confunde con lo que tiene detrás?** Mismo color o mismo brillo → fuera.

Lo que quede, se mide (`331`). Lo que gane la medición, se prueba (`sección 6`).

---

## 5. Qué NO debe entrar en la decisión

- **"Es la que quedó primero."** El orden alfabético no es un criterio.
- **"Es la más bonita."** La toma más bonita del rodaje suele ser la peor para recortar, porque lo bonito
  casi siempre viene del fondo — y el fondo lo vas a botar.
- **"Es la que mejor habla."** Eso decide qué toma va al montaje hablado, no cuál se recorta. Se puede
  usar el audio de una y la imagen de otra.
- **"Es 4K."** La resolución no separa nada. Una toma 4K a contraluz se recorta peor que una toma HD con
  luz de frente.
- **"Es la más larga."** Del recorte casi siempre usas 1 a 2 segundos (`262`).

---

## 6. La prueba de los 8 segundos (hazla antes de comprometerte)

Antes de montar nada, con la toma finalista:

1. Corta 2 segundos del tramo exacto que piensas usar.
2. Métela a CapCut → **Quitar fondo**.
3. Ponle debajo un color plano **magenta** (`261`, sección 7). El magenta delata halos, agujeros y bordes
   sucios como ningún otro color.
4. Reproduce el tramo completo. No mires el primer fotograma: mira los 2 segundos.

Si el contorno hierve, si desaparece medio brazo o si se ve un halo, **cambia de toma antes de invertir
tiempo**. Cambiar de toma cuesta un minuto. Arreglar un recorte malo cuesta la tarde y casi nunca queda.

Tres candidatas × 8 segundos = menos de un minuto para tomar la decisión más importante del montaje.

---

## 7. Si vas a volver a grabar

La forma más barata de ganar esta decisión es no tener que tomarla. Con el celular, en el bar, un domingo:

- Pared lisa detrás, **a metro y medio** de la persona.
- Luz de ventana **al frente**, nunca a la espalda.
- Ropa de color plano que **no** esté en la pared ni en la mesa.
- 60 fps, enfoque y exposición bloqueados, celular apoyado.
- **Graba 3 segundos de la escena vacía**: esa es la placa limpia, y vale oro (`261`). En el material real
  existen dos, las tomas 3 y 16, y salieron por accidente.

Detalle completo en `261`, sección 4.

---

## Errores comunes

1. **Elegir por orden de archivo.** El error que originó este bloque. El primer `.mp4` de la carpeta no
   tiene ninguna razón para ser el bueno.
2. **Elegir la toma más bonita.** Lo bonito suele venir del fondo, y el fondo se va a botar.
3. **Decidir sin abrir las demás.** Si hay 16 tomas y miraste 1, no elegiste: aceptaste.
4. **Recortar en contraluz.** El contorno sale perfecto y la cara sale negra. Se ve peor que no recortar.
5. **Confundir "fondo complejo" con "fondo complejo pegado al sujeto".** Lo segundo es lo que importa.
6. **No mirar la ropa contra el fondo.** Camiseta vino tinto sobre mesa vino tinto: el recorte se come el
   torso y nadie entiende por qué.
7. **Juzgar el recorte por un fotograma.** El recorte se rompe en el tiempo, no en la foto (`98`).
8. **Insistir con la toma mala porque ya se invirtió tiempo en ella.** El tiempo ya se perdió; seguir solo
   agrega pérdida.
9. **Creer que un modelo de IA mejor arregla una toma mala.** Mejora los bordes; no inventa la cara que
   el contraluz no registró.
10. **Recortar pelo suelto con viento.** No se puede. Ni con IA, ni con croma, ni con paciencia (`261`).
11. **Olvidar que existe una placa limpia.** Si en el material hay una toma del sitio vacío, tienes matte
    por diferencia gratis.
12. **No probar antes de montar.** Ocho segundos de prueba evitan tres horas de terquedad.
13. **Elegir la toma para el recorte y para el audio como si fueran la misma decisión.** No lo son.

---

## Checklist

Antes de aplicar un recorte a cualquier toma:

- [ ] **Miré las tomas disponibles**, todas, aunque sea en hoja de contactos (`333`).
- [ ] Descarté las que tienen la cara en **silueta o contraluz**.
- [ ] Descarté las donde el sujeto ocupa **menos de un quinto del ancho** del cuadro.
- [ ] Revisé qué hay **pegado al contorno** del sujeto, no solo el fondo en general.
- [ ] Comparé el **color de la ropa** con el color de lo que está detrás.
- [ ] Miré si hay **pelo suelto en movimiento** en el tramo que voy a usar.
- [ ] Medí las finalistas con ffmpeg (`331`), no solo a ojo.
- [ ] Verifiqué que la piel dé **U por debajo de 128** en la zona de la cara (`332`).
- [ ] Busqué si existe una **placa limpia** del mismo encuadre.
- [ ] Hice la **prueba de los 8 segundos sobre magenta** con la finalista.
- [ ] Reproduje el **tramo completo**, no un fotograma.
- [ ] Si el recorte sale sucio, **cambié de toma** en vez de pelear con el recorte.
- [ ] Anoté por qué elegí esa toma, en una línea, para no repetir la discusión mañana.
