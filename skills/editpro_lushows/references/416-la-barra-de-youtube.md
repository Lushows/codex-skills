# 416 · La barra de YouTube: la banda vetada del 16:9

**Qué resuelve:** todo el mundo protege el vertical y nadie protege el horizontal, porque el 16:9
«parece limpio». No lo es: el reproductor pinta encima, y lo hace justo donde la composición
documental quiere poner el rótulo, la cifra y el pie de fuente. Ésta es la banda, medida, y el techo
que hay que respetar en su lugar.

`45` ya dice «la barra de controles come ~90 px abajo; deja 120». Esa cifra es el caso mínimo. Lo que
el motor del canal documental tiene vetado, verificado el **11-sep-2026**, es bastante más ancho.

---

## La banda, en píxeles y en tanto por uno

Sobre un lienzo de **1920×1080**:

| Zona | Tanto por uno de la altura | Píxeles | Qué hay ahí |
|---|---|---|---|
| Margen superior de seguridad | 0,000 – 0,089 | 0 – 96 | Recorte en televisores, tarjetas de sugerencia |
| **Banda baja útil** | hasta **0,72** | hasta **778** | Aquí acaba todo lo que informa |
| Aire de cortesía | 0,72 – 0,78 | 778 – 842 | Nada crítico, pero puede haber imagen |
| **BANDA VETADA** | **0,78 – 0,86** | **842 – 928** | Barra de progreso, tiempo, controles |
| Resto inferior | 0,86 – 1,00 | 928 – 1080 | Título superpuesto, canal, sugerencias al pausar |

La banda vetada mide **86 px, el 0,08 de la altura**. Parece poco y no lo es: es exactamente la altura
de una línea de rótulo de 44 px con su aire.

**La regla operativa es una sola**: el borde **inferior** de cualquier elemento que informe —texto,
cifra, pie de fuente, marca de columna— queda por encima de `H · 0,72`. No su punto de anclaje: su
borde inferior.

```
y_max_declarada = 0,72 · H − alto_del_elemento
alto_del_elemento = ancho_mostrado × (alto_PNG / ancho_PNG)
```

Ese detalle mata episodios: en este motor la posición es el **ancla de la esquina superior izquierda**
(`diccionario.rect`), así que declarar `y = H*0,72` no deja el elemento encima de la barra: lo deja
empezando ahí y cayendo entero dentro.

---

## La comprobación, ejecutada

```python
for n in piezas_de_texto:
    iw, ih = Image.open(buscar(n)).size
    alto = w * ih / iw
    ymax = 0.72 * H - alto
    print(f"{n:<14}{w:>7}{alto:>7.0f}{ymax:>8.0f}{ymax/H:>11.3f}  {y_declarada}")
```

```
pieza           mostr   alto   y max  y max t/1  y declarada
d_1890           1340    232     546      0.506  604.8      <-- se pasa 59 px
d_preso          1380    267     511      0.473  730.5      <-- se pasa 220 px
m_consta          700    202     575      0.533  777.6      <-- se pasa 203 px
r_sinfuente       720    152     626      0.580  669.6      <-- se pasa 44 px
m_consta          760    220     558      0.517  172.8      ok
r_casilla         968    216     562      0.520  604.9      ok
```

**Cuatro de nueve colocaciones de texto del episodio piloto caen dentro de la barra.** El caso extremo
es `m_consta` declarada en `H*0,72` exacto: su borde inferior acaba en 980 px, o sea `0,907` — cruza la
banda vetada entera. Y ninguna auditoría de cobertura, densidad o huecos lo veía.

De los 61 elementos del episodio, **23 entran en la banda**. La mayoría son fotografías de archivo, y
ahí no hay problema: la banda vetada admite imagen, fondo y textura igual que las zonas muertas del
vertical (`45`). Lo que no admite es información.

---

## El fotograma de control

```bash
ffmpeg -v error -ss 55 -i episodio.mp4 -vf \
"drawbox=x=0:y=842:w=1920:h=87:color=red@0.45:t=fill,\
drawbox=x=0:y=0:w=1920:h=96:color=orange@0.35:t=fill,\
drawbox=x=96:y=96:w=1728:h=682:color=lime:t=5" \
  -frames:v 1 -y control_169.png
```

El verde es la zona de texto segura: **1728 × 682 px, el 0,568 del cuadro**. En el fotograma del
segundo 55 del piloto, el telegrama con texto legible entra de lleno en el rojo: la línea «cards to
follow» queda debajo de la barra de progreso.

---

## Lo que no se puede medir desde el escritorio

Tres cosas más del reproductor que **cambian** y que hay que medir, no recordar (`418`):

- **Los controles aparecen y desaparecen.** En tu reproductor local no salen nunca; en el móvil salen
  al tocar y en televisor se quedan. La medida se hace con los controles visibles, no sin ellos.
- **La pantalla final** (tarjetas de suscripción y vídeo siguiente) ocupa una superficie grande durante
  los últimos segundos. Su tamaño depende del diseño vigente: se mide publicando la carta de `415` como
  vídeo no listado y capturando el final, nunca de memoria.
- **Las tarjetas de sugerencia** viven arriba a la derecha y aparecen cuando tú las programas.

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Creer que el 16:9 no tiene interfaz | Es el formato donde menos se protege y el que tiene la banda más traicionera |
| Usar los «120 px» del caso mínimo | La banda real empieza en 842, no en 960 |
| Comprobar el ancla en vez del borde inferior | Un elemento declarado en 0,72 acaba en 0,907 |
| Vetar la banda también para imagen | Se desperdicia el 8% del cuadro; la banda admite fondo y archivo |
| Mirar el vídeo en el reproductor local | Ahí la barra no existe: es la ilusión de siempre |
| Olvidar la pantalla final | El remate del episodio queda debajo de la tarjeta de suscripción |
| Firmar abajo a la derecha | Ahí van el tiempo, la calidad y el botón de pantalla completa (`413`) |
| Dar por buena una banda sin fecha | Cambia; se vuelve a medir con la carta de `415` |

## Relacionado

`418` cómo se mide con captura real · `415` la carta de medida y la resta · `412` el suelo de cuerpo ·
`413` dónde sobrevive la firma · `410` el mapa de intocables · `419` cuando el rótulo no cabe encima
de 0,72 · `45` la fila de «YouTube largo» de la tabla por superficies
