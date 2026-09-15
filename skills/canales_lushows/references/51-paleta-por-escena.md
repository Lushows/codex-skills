# 51 · Paleta por escena

**Qué resuelve:** el primer episodio salió entero marrón oscuro. Cada plano parecía
correcto por separado y el conjunto era una sola nota. Aquí se planifica el **recorrido
de color**: qué temperatura tiene cada escena y en qué orden se ponen.

---

## La paleta base del canal (no se negocia)

| Color | Hex | Uso |
|---|---|---|
| Negro tinta | `#12100C` | El suelo de todos los fondos. Ninguna escena baja de aquí |
| Papel | `#E6DCC4` | Márgenes de recorte, texto de documento |
| Rojo | `#E3120B` | **Acento único.** Sellos, tachados, la cifra que duele |
| Amarillo dato | `#E8C547` | Cifras, subrayados, luz cálida de escena |
| Verde mercado | `#0E8A5F` | Dinero, mercado, lo que crece |

El rojo y el amarillo **nunca** son el color de un fondo: son lo que va encima. Un fondo
rojo deja sin sitio al sello rojo.

## El principio: cada escena tiene temperatura y punto de luz

Dos parámetros por escena y con eso basta:

1. **Temperatura** — dónde cae el tono base: frío (azules/aceros), templado (verdes),
   cálido (ocres/ámbar).
2. **Punto de luz** — de dónde entra la luz y de qué color es (`53`).

## El recorrido: no seis fondos, una curva

La regla operativa es sencilla: **dos escenas seguidas nunca comparten temperatura.**
Se alterna frío/cálido para que el ojo note que ha cambiado de sitio.

Recorrido del episodio 01, que es el patrón por defecto:

| # | Escena | Temperatura | Base | Medio | Luz |
|---|---|---|---|---|---|
| 1 | Gancho | verde dinero | `#28402F` | `#12201A` | `#DFF0DA` cenital suave |
| 2 | La pregunta | azul expediente | `#1B2A38` | `#101A24` | `#7AB4DC` lateral fría |
| 3 | El peso | ocre almacén | `#3A3226` | `#2A2419` | `#FFE8B4` cálida arriba |
| 4 | La máquina | gris acero | `#39413F` | `#252B2A` | `#D6F0FF` cenital fría |
| 5 | Las piezas | azul plano | `#152232` | `#0D1520` | `#6E9CD4` plana, sin foco |
| 6 | El remate | verde industrial | `#2C3A31` | `#1B241E` | `#E2FFE8` + `#FFECC4` doble |

Todas caen a `#080D0B`–`#14110C` en la esquina inferior: **ese es el hilo que las une**
(`58`). Lo que cambia es el tercio alto de cada degradado.

## Cómo se planifica antes de escribir una línea de CSS

1. **Lista las escenas del guion** con su función narrativa (gancho, dato, giro, remate).
2. **Asigna temperatura por sentido**, no por gusto:

| Sentido de la escena | Temperatura | Por qué |
|---|---|---|
| Dinero, mercado, crecimiento | verde `#28402F` | El verde es el color del billete |
| Investigación, documento, duda | azul `#1B2A38` | Frío = distancia, expediente |
| Almacén, mercancía, volumen físico | ocre `#3A3226` | Cálido = materia, polvo, madera |
| Oficina, sistema, maquinaria | acero `#39413F` | Neutro frío = institución |
| Plano, esquema, cómo funcionaba | azul plano `#152232` | Blueprint |
| Caída, cierre, la verdad | verde industrial `#2C3A31` | Cierra el círculo del gancho |

3. **Comprueba la alternancia.** Si salen dos ocres seguidos, uno de los dos cambia.
4. **Reserva UN pico de color.** En un episodio hay una sola escena que puede permitirse
   saturación alta (el remate, casi siempre). Si todas suben, ninguna sube.

## La trampa del marrón

El fallo del episodio 01 tiene una causa concreta: **degradados con muy poca separación
de tono y viñeta muy fuerte**. Al oscurecer bordes al 70% y bajar el medio a un `#2A2419`
todo termina en el mismo lodo.

| Síntoma | Arreglo |
|---|---|
| Todo tira a marrón | Subir la saturación del tono base, no la luminosidad |
| Los seis fondos se parecen | Alternar frío/cálido y cambiar la FAMILIA de textura (`52`) |
| No hay blancos vivos | Añadir un punto de luz de `rgba(255,240,205,.22)` mínimo |
| Se ve apagado, no oscuro | Bajar la viñeta de `.70` a `.60` |

**Regla de saturación:** el tono base de cada escena debe tener al menos **17 puntos de
diferencia** entre su canal más alto y el más bajo. `#2A2419` (42,36,25) tiene 17 — el
mínimo. `#2B2A28` (43,42,40) tiene 3: eso es gris sucio, no es una escena.

**Las dos palancas, medidas.** Sobre `f_peso` del episodio 01, cambiando una cosa cada vez:

| Cambio | `YMAX` | `SATAVG` |
|---|---|---|
| Original (luz `.20`, base `#3A3226`) | 82 | 5,6 |
| Subir la luz a `.48` | **120** | 6,0 |
| Subir la saturación de la base (`#3A3226`→`#4A3A1E`) | 86 | **10,8** |

La luz mueve el brillo máximo; la saturación de la base mueve el color. **Son palancas
distintas y el marrón necesita la segunda.** Las seis escenas del episodio 01 tenían
`SATAVG` entre 2,4 y 7,0: por eso todo se veía del mismo barro.

### La tercera palanca: la luz complementaria

Con una sola fuente de luz el fondo queda *teñido*, no *graduado*: todo el cuadro va
del mismo lado del círculo cromático y se lee plano. La solución es un **segundo foco
de la temperatura contraria en la esquina opuesta**, a la mitad de fuerza:

```css
/* clave cálida arriba a la izquierda */
radial-gradient(58% 62% at 50% 50%, rgba(255,238,186,.46), transparent 72%)
/* contra frío abajo a la derecha — la mitad de fuerza, nunca igual */
radial-gradient(58% 62% at 50% 50%, rgba(150,214,255,.20), transparent 72%)
```

Si los dos focos van a la misma fuerza se anulan y vuelve el gris. La proporción que
funciona es **clave `.42-.52` · contra `.18-.24`**.

### Resuelto: los seis fondos, antes y después

| Fondo | `YMAX` antes → después | `SATAVG` antes → después |
|---|---|---|
| `f_gancho` | 77 → **249** | 4,7 → **15,7** |
| `f_pregunta` | 55 → **146** | 6,9 → **13,2** |
| `f_peso` | 78 → **242** | 5,4 → **12,0** |
| `f_maquina` | 87 → **247** | 2,3 → **15,9** |
| `f_piezas` | 51 → **138** | 7,1 → **14,0** |
| `f_remate` | 69 → **158** | 3,4 → **14,7** |

Los tres cambios juntos: tono base más saturado, clave a `.42-.52` con contra
complementario, y la viñeta de `.62-.70` a `.46-.54`. Esa última importa más de lo que
parece: al `.70` se come el tercio exterior del cuadro, que es justo donde el reparto
por recuadros (`17`) decía que faltaba peso.

**Umbrales de aceptación:** `YMAX ≥ 110` y `SATAVG ≥ 12` en los seis. Se comprueba
antes de renderizar el episodio, sobre el PNG del fondo:

```bash
ffmpeg -i render/f_peso.png -vf "scale=480:-1,signalstats,metadata=print:file=-" \
  -f null - 2>/dev/null | grep -E "YAVG|YMAX|SATAVG"
```

## Verificar: la hoja de contactos

No se opina, se mira todo junto:

```bash
ffmpeg -y -i render/f_gancho.png -i render/f_pregunta.png -i render/f_peso.png \
       -i render/f_maquina.png -i render/f_piezas.png -i render/f_remate.png \
  -filter_complex "[0]scale=640:360[a];[1]scale=640:360[b];[2]scale=640:360[c];\
[3]scale=640:360[d];[4]scale=640:360[e];[5]scale=640:360[f];\
[a][b][c][d][e][f]xstack=inputs=6:layout=0_0|w0_0|w0+w1_0|0_h0|w0_h0|w0+w1_h0" \
  -frames:v 1 render/_paleta.png
```

Si en esa lámina de 3×2 no se distinguen seis escenas distintas a un metro de la
pantalla, el episodio es de una sola nota y hay que rehacer la curva.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Elegir el color "porque queda bonito" | La temperatura deja de significar algo |
| Fondo rojo o amarillo saturado | Mata el acento; el sello rojo ya no destaca |
| Subir luminosidad para arreglar el marrón | Sale gris lavado; hay que subir saturación |
| Todas las escenas con el mismo pico de color | No hay clímax visual |
| No mirar la hoja de contactos | El defecto solo se ve con los seis juntos |

## Relacionado

`50` · `52` · `53` · `57` · `58` · `23` empatar recorte y fondo
