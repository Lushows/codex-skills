# 208 · El cierre que devuelve al largo

**Qué resuelve:** para qué existe el corte vertical. Si es para tener vistas, ya está: se
publica y se olvida. Si es para que el canal crezca, el corte tiene que **terminar
mandando a alguien a un sitio**, y el sitio es el episodio largo. Este módulo fija de
dónde se corta, cuánto dura el cierre y qué dice — con los números del episodio real.

---

## De dónde se corta

Un corte vertical de este canal no es «los primeros 45 segundos». Es un **tramo cerrado**:
tiene su propia pregunta y su propia respuesta, y deja fuera la siguiente. Los bloques del
episodio y su densidad de elementos:

| Bloque | Tramo | Duración | Elementos | Elementos/min | Palabras/min |
|---|---|---|---|---|---|
| `muerte` | 0,00 – 16,15 | 16,15 s | 13 | 48,3 | 141 |
| `oficio` | 16,15 – 22,88 | 6,73 s | 7 | **62,4** | 143 |
| `nombre` | 22,88 – 34,41 | 11,53 s | 9 | 46,8 | 141 |
| `torre` | 34,41 – 50,29 | 15,88 s | 18 | **68,0** | 155 |
| `metodo` | 50,29 – 63,45 | 13,16 s | 12 | 54,7 | 150 |

La ventana de 45 s más densa del episodio es **16,0 – 61,0 s**, con 45 elementos
(60,0/min). Y es exactamente la ventana que **no** sirve: empieza a mitad de la muerte del
protagonista y termina a mitad del método. Un corte que empieza en el segundo 16 de una
historia no tiene principio.

> **El corte se elige por límite de bloque, no por densidad.** Los bloques son los
> silencios medidos de la locución (`93`); cortar por ahí es cortar por donde la voz
> respira. `muerte` + `oficio` son 22,88 s con 20 elementos: un corte con planteamiento y
> golpe. `torre` solo son 15,88 s con 18 elementos: el tramo más denso del episodio y una
> historia entera.

## Cuánto puede costar el cierre

| Cierre | % de un corte de 45 s |
|---|---|
| 1,5 s | 3 % |
| **2,5 s** | **6 %** |
| 3,5 s | 8 % |

2,5 s es el ajuste: por debajo no da tiempo a leer dos líneas, por encima se come un
elemento entero del montaje. Y hay una consecuencia que conviene tener delante: **el
cierre se resta del contenido**. Un corte de 45 s con cierre de 2,5 es un corte de 42,5 s
de historia. Si la historia pedía 45, el corte es de 47,5 y no se recorta el final.

## Qué dice el cierre

Tres cosas, en este orden, y ninguna más:

| Elemento | Registro (`201`) | Contenido |
|---|---|---|
| La **pregunta abierta** | centro | Lo que el corte deja sin responder. Es el único gancho honesto |
| El **título del episodio** | centro-bajo | Para que se pueda buscar. No «link en la bio» |
| La **marca** | arriba | Pequeña. Quien va a volver ya sabe de quién es |

La pregunta abierta no es un cliffhanger inventado: es lo que el propio recorte deja
fuera. Si el corte es `muerte` + `oficio`, el episodio sigue contando **por qué a un
falsificador le llamaban aprendiz**, y eso ya está en el guion. Fabricar una intriga que
el episodio no resuelve es la forma más rápida de que quien haga clic no vuelva nunca
(`385`, `389`).

Y el título literal, no una alusión: quien quiera buscarlo tiene que poder teclearlo. En
tres de las cuatro redes el enlace no es clicable desde el vídeo, así que lo que viaja es
el texto.

## Lo que el cierre no hace

| No | Por qué |
|---|---|
| Pedir suscripción | El vídeo no ha demostrado todavía que merezca una; el episodio sí |
| Decir «link en la bio» | El texto escrito del título funciona en las cuatro redes; el enlace, en una |
| Poner una pantalla final con logo 3 s | 3,5 s son el 8 % del corte, y ese 8 % es un elemento del montaje |
| Repetir la cifra del gancho | Ya se ha dicho; repetirla dice que no había nada más |
| Fundir a negro | El negro es el sitio donde el pulgar decide deslizar |

Ese último punto es el que cuesta aceptar y el que más se nota: el corte **no funde a
negro**. El último fotograma es la composición del cierre, a plena opacidad, congelada. Un
negro de medio segundo al final es medio segundo de permiso para irse.

## El mismo argumento que el primer fotograma

`205` dice que el fotograma 0 es la miniatura y no puede estar vacío. El último fotograma
tiene el mismo problema por el otro extremo: **en tres de las cuatro redes el vídeo se
repite en bucle**, así que el último fotograma y el primero se ven **seguidos**. Componer
el cierre sin mirar el arranque produce un salto que el espectador registra como corte
mal hecho, aunque no sepa decir dónde.

La comprobación es de un comando:

```bash
ffmpeg -v error -i corte.mp4 -vf "select='eq(n\,0)+gte(t\,{DUR}-0.04)',tile=2x1" \
       -frames:v 1 -y bucle.png
```

Los dos fotogramas uno al lado del otro. Si el paso de uno a otro se lee como un tropiezo,
se arregla en el cierre, no en el arranque: el arranque manda (`205`).

## Errores frecuentes

| Error | Consecuencia medida |
|---|---|
| Cortar por densidad | La ventana más densa (16,0–61,0) empieza a mitad de historia |
| Cortar «los primeros 45 s» | Deja el golpe del bloque `oficio` a medias |
| Cierre de 3,5 s o más | El 8 % del corte: un elemento entero del montaje |
| Restar el cierre del contenido sin decirlo | Un corte de 45 s con 42,5 s de historia |
| Fabricar una intriga que el episodio no resuelve | Quien hace clic no vuelve |
| «Link en la bio» | Funciona en una red de cuatro; el título escrito, en las cuatro |
| Fundir a negro | Medio segundo de permiso para deslizar |
| No mirar el bucle | El último y el primer fotograma se ven seguidos |

## Relacionado

`205` el primer fotograma · `93` estructura de episodio · `94` el gancho de dinero ·
`99` título, miniatura y descripción · `128` música para el vertical · `385`
sensacionalismo contra rigor · `389` el contrato con quien mira · `209` errores del
formato corto
