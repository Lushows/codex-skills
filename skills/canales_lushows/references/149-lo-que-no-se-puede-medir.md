# 149 · Lo que NO se puede medir

**Qué resuelve:** creer que un episodio con las doce medidas en verde está terminado.
La auditoría mide la arquitectura del montaje; no mide si se ve bien ni si emociona.

---

## La frontera exacta

El auditor trabaja sobre `guion_visual.py` y `tiempos.json`: **geometría y tiempo**.
Todo lo que no sea una posición, una duración o una superficie está fuera de su alcance
por construcción, no por falta de código.

| El auditor sabe | El auditor no sabe |
|---|---|
| Que hay un recorte en `x=W*0.28`, 2,1 s | Si ese recorte se distingue del fondo |
| Que la cobertura es del 31 % | Si el cuadro se lee o es una sopa |
| Que el elemento entra en la palabra "quiebra" | Si el gesto subraya la palabra o la pisa |
| Que la escena tiene 48,3 ev/min | Si la escena engancha |
| Que la pieza de texto no tiene faltas | Si la frase suena a persona o a Wikipedia |
| Que suena música de 12,4 a 31,0 s | Si la música estorba a la voz |
| Que el episodio dura 63,45 s | Si alguien lo termina |

## Los cuatro juicios que siguen siendo humanos

**1. Empaste: si el recorte pega con el fondo.** Luz, ángulo, grano, temperatura de
color. Un retrato de estudio con luz frontal sobre un fondo de página amarillenta con
viñeta canta aunque esté colocado en el sitio perfecto y ocupe el 8 % del lienzo (`23`).
La tabla no tiene esa información: en la tabla sólo hay un nombre de fichero.

**2. Si la frase suena bien.** El texto se escribe para el oído (`95`). El corrector
caza `DEFUNCION` sin tilde; no caza una subordinada de tres niveles que el locutor no
puede decir de un tirón, ni una cifra leída como "cuatrocientos treinta y siete mil
doscientos" cuando bastaba "casi medio millón".

**3. Si el ritmo emociona.** Eventos/min mide **cuántos**, no **cuáles**. Una rampa de
densidad idéntica sobre dos guiones distintos da la misma cifra y un efecto opuesto
(`15`, `38`). El silencio bien puesto y el plano de descanso que respira (`16`) miden
exactamente igual que un bache.

**4. Si la historia importa.** El aporte original, el gancho de dinero, si el arco cierra
(`92`, `94`). Ninguna métrica del montaje toca esto, y es lo único que decide si el
episodio vale la pena.

## Qué se hace con eso

No se mide: **se mira**, y se mira barato. El sustituto del render completo es la
**rejilla de fotogramas**: un muestreo del episodio en una sola imagen (`_grid.png`).
Cuesta alrededor de un minuto frente a los 15–25 del render, y enseña justamente lo que
la tabla no sabe: color, empaste, legibilidad, densidad percibida.

```bash
# muestreo cada 2 s del vídeo mudo, en una rejilla de 6 columnas
ffmpeg -y -i salida/_mudo.mp4 -vf "fps=1/2,scale=480:-1,tile=6x8" salida/_grid.png
```

Sobre la rejilla se contestan, a ojo y en dos minutos, cuatro preguntas:

1. ¿Hay algún cuadro donde el recorte no se distinga del fondo?
2. ¿Hay algún cuadro que no se entienda sin oír la voz?
3. ¿Se repite un dibujo que la métrica no cazó?
4. ¿Se lee el texto al tamaño de un móvil?

Lo que aparezca y **pueda convertirse en geometría** se vuelve métrica nueva. La oclusión
nació así: la ficha del juicio enterrada bajo la foto del tribunal se vio en la rejilla,
y al día siguiente era una comprobación en el auditor. Lo que no pueda convertirse
—el empaste, el tono— se queda como criterio y se apunta en el guion de la próxima vez.

## El orden completo

```
auditar (1,4 s) → corregir la tabla → auditar → rejilla (1 min) → render (15-25 min)
                                                      ↑
                                          aquí se juzga lo que no se mide
```

Y una vez renderizado, **una pasada entera con sonido**. No con el guion delante: como
lo va a ver alguien. Es la única prueba que detecta que el episodio, estando todo bien,
no tira.

## La honestidad que hace falta

Dos afirmaciones opuestas, las dos ciertas:

- Un episodio con las doce medidas en verde **no está terminado**. Puede ser correcto y
  no valer nada.
- Un episodio que no pasa las medidas **está mal** de una forma concreta y arreglable,
  por muy bien que suene la historia.

La auditoría no es el criterio; es el **suelo**. Quita de la mesa los fallos que se
pueden objetivar para que el juicio humano se gaste donde hace falta: en si la historia
merece 63 segundos de la vida de alguien.

Y hay una tentación permanente que conviene nombrar: cuando algo se ve mal y no hay
métrica que lo explique, la salida fácil es declarar que "las métricas dicen que está
bien". Gana el ojo, siempre (`142`). La métrica se corrige después.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Dar por terminado lo que pasa la auditoría | Episodios correctos, planos y olvidables |
| Saltarse la rejilla por ir rápido | El empaste y la oclusión se descubren ya renderizados |
| Intentar medir lo inmedible | Métricas inventadas que se cumplen siempre (`147`) |
| Creer a la métrica contra el ojo | Se publica lo que se ve mal, con permiso por escrito |
| No ver el episodio entero con sonido | Nadie ha comprobado nunca si funciona |

## Relacionado

`16` el plano de descanso · `23` empatar recorte y fondo · `92` el aporte original ·
`95` escribir para el oído · `140` medir antes de renderizar · `148` el cuadro de mando
