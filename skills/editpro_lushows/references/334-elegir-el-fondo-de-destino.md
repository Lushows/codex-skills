# 334 — Elegir el fondo de destino: cuál acepta un sujeto y cuál se lo come

**Qué resuelve:** la otra mitad de la decisión. En `330` se elige la toma; aquí se elige **sobre qué** se
va a pegar. Un recorte impecable sobre un fondo equivocado se ve peor que no haber recortado nada.

---

## 1. El error simétrico

Cuando alguien prueba una técnica de recorte, dedica el 95% de la atención al sujeto — los bordes, el
pelo, el halo — y toma el fondo de lo primero que hay a mano: la ilustración que ya estaba hecha, la que
se generó para otra cosa, la que se veía linda sola.

Un fondo se ve lindo solo justamente porque **está completo**. Y un fondo completo no tiene sitio para
nadie más. Ponerle una persona encima es tapar el 40% de una composición que ya estaba resuelta.

> **Un fondo de destino no se elige por lo bonito que es. Se elige por el hueco que tiene.**

---

## 2. Las cuatro propiedades de un fondo que acepta sujeto

### a) Espacio negativo donde va la persona

Una zona grande, tranquila, sin nada importante, del tamaño que va a ocupar el sujeto. En vertical 9:16
casi siempre es el tercio inferior o una mitad lateral.

Si el elemento principal de la ilustración está justo donde va la cabeza, o cambias el fondo o cambias la
ilustración. Mover a la persona a una esquina para que quepa nunca se ve bien.

### b) Separación de brillo con el sujeto

La misma lógica de `330` pero al revés: el sujeto es fijo y ahora eliges el fondo. Sujeto oscuro pide
fondo claro. Sujeto claro pide fondo oscuro.

| Diferencia de `YAVG` entre sujeto y zona de fondo | Resultado |
|---|---|
| más de 80 | se lee de inmediato, incluso en miniatura |
| 40 a 80 | correcto |
| 20 a 40 | se "hunde": hay que agregar un contorno o una sombra |
| menos de 20 | el sujeto desaparece. Cambia el fondo |

### c) Poco detalle **en la zona de contacto**

Lo que importa no es cuánto detalle tiene el fondo, sino cuánto tiene **justo donde va el contorno del
sujeto**. Un borde de recorte imperfecto sobre un área lisa es invisible; el mismo borde sobre una trama
de líneas finas grita.

### d) Dirección de luz compatible

Si en la toma la luz viene de la izquierda y en la ilustración las sombras caen a la izquierda, el
espectador no sabe qué le molesta, pero le molesta. Es el problema 2 de `260` y es el que más delata un
montaje casero.

---

## 3. Medir el fondo antes de usarlo

Los mismos comandos de `331`, aplicados a la **zona donde va a ir el sujeto**.

```bash
# crop=ancho:alto:x:y sobre la zona candidata del fondo
ffprobe -v error -f lavfi "movie=fondo.png,crop=500:300:134:850,signalstats" \
  -show_entries "frame_tags=lavfi.signalstats.YAVG,lavfi.signalstats.SATAVG" -of default=nw=1:nk=1

ffprobe -v error -f lavfi "movie=fondo.png,crop=500:300:134:850,edgedetect=low=0.1:high=0.35,signalstats" \
  -show_entries "frame_tags=lavfi.signalstats.YAVG" -of default=nw=1:nk=1
```

Ejemplo real, ilustración `i3-fundadores-1.png` de Bendita Pola (768 × 1344, estilo azul marino sobre
crema, dos botellas personaje dándose la mano):

| Zona | YAVG | SATAVG | Bordes | Sirve como fondo |
|---|---|---|---|---|
| Franja crema inferior | 211,9 | 4,3 | **0,33%** | **sí, ideal** |
| Zona de los personajes | 187,8 | 6,6 | **8,21%** | no: hay dos caras compitiendo |
| Marco azul superior | 23,2 | 21,0 | **0,00%** | sí, para un sujeto claro |

Tres zonas de una misma imagen, tres veredictos distintos. Por eso la pregunta nunca es "¿sirve esta
ilustración?" sino **"¿qué zona de esta ilustración sirve?"**.

Umbrales prácticos para la zona de destino:

- **Bordes por debajo de 1%** → cualquier recorte se ve limpio ahí.
- **1% a 3%** → aceptable; revisa el contorno con lupa.
- **más de 5%** → el fondo se come el borde. Cambia de zona.

---

## 4. Fondos que devoran al sujeto

En orden de frecuencia:

1. **El fondo del mismo color que la ropa.** Camiseta vino tinto sobre fondo vino tinto: el torso
   desaparece y solo flota una cabeza.
2. **Ilustraciones con líneas del mismo grosor que el error del recorte.** Trama de puntos, rayas finas,
   texturas de medio tono: el borde imperfecto se camufla con el estilo y todo se vuelve ruido.
3. **Fondos con caras.** Personajes, retratos, dibujos con ojos. **El ojo humano solo puede atender a una
   cara a la vez.** Si el fondo tiene dos botellas con ojos y boca, tu presentador es el tercero en
   importancia.
4. **Fondos con texto.** Compiten por la lectura y además el sujeto casi siempre tapa una palabra, lo que
   se lee como error, no como profundidad (eso es otra cosa: `262`).
5. **Degradados que cruzan por el contorno.** El fondo pasa de claro a oscuro justo a la altura del
   hombro: media silueta se lee y la otra media no.
6. **Fotografías reales muy detalladas.** Si el fondo es una foto, tu recorte tiene que estar perfecto
   porque no hay estilo que disimule. Con ilustración plana perdonas mucho más.
7. **Fondos con la misma temperatura de color que la piel.** Fondo naranja + piel = todo es la misma
   mancha. La piel manda sobre el fondo, no al revés (`254`).

---

## 5. Generar una ilustración pensada para recibir a alguien

Si el fondo lo vas a generar (`122`), pídelo con el hueco incluido. Lo que funciona:

- "**Composición vertical 9:16 con la mitad inferior vacía**, sin elementos, del color de fondo."
- "Estilo plano, de dos colores, sin texturas ni tramas finas."
- "Los elementos ocupan solo el tercio superior."
- "**Sin personajes con cara.**"
- "Luz que viene de la izquierda" (o de donde venga en tu toma).

Y lo que hay que verificar después, porque el modelo casi nunca obedece del todo: mide la zona vacía con
los comandos de arriba. Si trajo una textura sutil "para que no se vea plano", esa textura es exactamente
lo que va a delatar tu recorte.

Truco barato y confiable: pide la ilustración **sin el hueco** y agrega tú una banda de color plano por
debajo con `drawbox`, o baja la opacidad de esa zona. Un fondo hecho a medida vence a un fondo bonito.

```bash
# Aclarar u oscurecer la zona de destino para ganar separación
ffmpeg -i fondo.png -vf "drawbox=x=0:y=900:w=768:h=444:color=black@0.35:t=fill" -y fondo-listo.png
```

---

## 6. La prueba de la silueta negra

Antes de recortar nada: coge una **silueta plana negra** del tamaño y la posición que va a tener la
persona, ponla sobre el fondo candidato y mira a tamaño de celular.

- Si la silueta **se lee de inmediato** como una figura → el fondo sirve.
- Si hay que buscarla → el fondo no sirve, y ningún recorte perfecto lo va a arreglar.
- Si al ponerla tapa algo importante del fondo → el fondo no era para esto.

Cuesta un minuto y es la prueba más honesta que existe, porque elimina la variable "qué tan bien quedó el
recorte" y deja sola la que estás decidiendo.

---

## 7. Escala, altura y sombra: los tres remates

Aunque el fondo sea el correcto, tres cosas delatan el pegado:

- **Escala.** Si el fondo tiene objetos reconocibles (una mesa, una puerta), el tamaño de la persona
  tiene que ser coherente con ellos. Con ilustración abstracta esto no aplica y es una razón más para
  preferirla.
- **Altura de la línea de horizonte.** Si el fondo tiene una línea de piso, los pies van sobre ella, no
  flotando ni enterrados.
- **Sombra de contacto.** Una elipse oscura y desenfocada bajo los pies vale más que cualquier ajuste de
  borde. El matting recorta al sujeto, nunca su sombra (`263`).

---

## Errores comunes

1. **Usar el fondo que ya estaba hecho.** Es el mismo error de elegir la toma por orden alfabético, del
   otro lado del sándwich.
2. **Elegir el fondo por lo bonito que se ve solo.** Un fondo completo no tiene sitio para nadie.
3. **No mirar dónde queda el hueco.** El espacio negativo tiene que coincidir con el sitio de la persona.
4. **Fondo con caras.** El espectador atiende una cara a la vez y la tuya pierde.
5. **Fondo del color de la ropa.** El torso desaparece.
6. **Medir el fondo completo en vez de la zona de destino.** Mismo error que en `332`.
7. **Ignorar la dirección de la luz.** Nadie sabe qué está mal, pero todos lo notan.
8. **Texturas finas "para que no se vea plano".** Son las que delatan el borde del recorte.
9. **Olvidar la sombra de contacto.** Sin ella la persona flota, aunque el recorte sea perfecto.
10. **Poner al sujeto encima de texto del fondo.** Se lee como error de montaje.
11. **Escoger un fondo fotográfico teniendo uno ilustrado.** La ilustración plana perdona el borde
    imperfecto; la foto no perdona nada.
12. **No probar con silueta.** Un minuto de prueba evita una hora de recorte inútil.
13. **Cambiar de fondo después de haber ajustado el recorte a mano.** Decide el fondo primero; el borde
    se afina contra el fondo definitivo, no contra un provisional.

---

## Checklist

- [ ] El fondo tiene un **espacio negativo** del tamaño y en el sitio del sujeto.
- [ ] Medí `YAVG` de la **zona de destino** y del **sujeto**: la diferencia pasa de 40.
- [ ] Medí la **densidad de bordes** de la zona de destino: por debajo del 3%.
- [ ] El color del fondo **no coincide** con el de la ropa ni con el de la piel.
- [ ] El fondo **no tiene caras** ni texto donde va la persona.
- [ ] La **dirección de la luz** del fondo coincide con la de la toma.
- [ ] Hice la **prueba de la silueta negra** y se lee sola.
- [ ] La revisé **a tamaño de celular**, no a pantalla completa.
- [ ] La **escala** de la persona es coherente con lo que hay en el fondo.
- [ ] Los pies están sobre la línea de piso, no flotando.
- [ ] Agregué **sombra de contacto**.
- [ ] Si la zona no daba contraste, la modifiqué (`drawbox`) en vez de resignarme.
- [ ] Decidí el fondo **antes** de afinar el borde del recorte.
