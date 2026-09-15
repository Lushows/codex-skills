# 209 · Errores del formato corto

**Qué resuelve:** el catálogo de lo que este canal **no hace** en vertical, con la razón
medida de cada punto. No es una lista de gustos: cada línea remite a un número que se
sacó del episodio real o de una pieza real, y ese número es lo que permite rechazar la
propuesta sin discutir.

Los errores generales del vídeo vertical están en `editpro 147` y `editpro 359`. Aquí
sólo los de **este motor y este canal**, que son otros.

---

## 1 · Recortar el 16:9 en vez de renderizar

La cabeza de la lista y la más cara. Recorte 9:16 centrado sobre los 59 elementos de
`ep01-lustig`:

```
sobreviven enteros        1
quedan cortados          50
quedan fuera del todo     8
fracción media de ancho conservada   0,287
```

47 de 59 elementos son más anchos que la ventana entera (608 px). El retrato del
protagonista conserva el **3 %**. Está entero en `200`.

## 2 · Trasponer el lienzo y ya

Cambiar `W_LIENZO, H_LIENZO` y no tocar nada más:

| | 16:9 | 9:16 traspuesto |
|---|---|---|
| Superficie media por elemento | 18,4 % | **5,8 %** |
| Cobertura | 36,1 % | **11,4 %** |

Por debajo del 14 % el auditor marca «cuadro casi vacío». Un episodio entero así. `203`.

## 3 · Mantener cuatro elementos a la vez

El episodio llega a 4 simultáneos y va a 3 o más el 30 % del tiempo. Apilados en la
columna útil de 1200 px, la pila **no cabe el 50 % del tiempo**; en el peor instante pide
2476 px. Con cuatro, cada elemento tendría 402 px de ancho. **Dos simultáneos es el tope.**

## 4 · Reusar las piezas de texto del episodio

5 de las 16 piezas de texto caen por debajo del suelo de legibilidad al pasar a vertical
con el mismo ancho relativo. `linea_00` necesita **948 px** sobre un lienzo cuya zona
segura de texto son **820**: no cabe a ningún ancho. Se redibuja o se parte. `204`.

## 5 · Reusar la pieza de dato sin tocarle el pie

La cifra sale con 3,3 veces el margen del suelo; su pie de fuente se queda en **16,9 px
contra un suelo de 22,3**. Un número enorme con una fuente invisible es una afirmación sin
respaldo. `207`.

## 6 · Empezar el corte donde empieza la escena

Fotograma 0 de `ep01-lustig`: **0 elementos, 0,0 % de cobertura**, tercio inferior con
desviación 8,3. El primer elemento cruza el umbral de opacidad en el fotograma 5 y el
cuadro no se llena hasta el 20. Esa es la miniatura. `205`.

## 7 · Subtitular de dos en dos palabras

81 bloques, duración mínima **0,20 s**. Parpadeo. De tres en tres: 57 bloques, mínimo
0,31 s, ninguno por debajo del suelo. `206`.

## 8 · Dejar que el subtítulo ocupe dos líneas de 24 caracteres

24 caracteres al tamaño mínimo legible son **1086 px** y la zona segura son 820. El tope
es **18 caracteres por línea**. Encogerlo para que quepa es sacarlo del suelo de
legibilidad, que es lo mismo que no ponerlo. `206`.

## 9 · Poner cifra y subtítulo los dos en el pie

El pie útil son 220 px (`y` 1180–1400). No caben. Si se apilan, el centro del cuadro —
donde iba la prueba — se queda desierto. El subtítulo se queda el pie; la cifra se va al
centro. `201`, `207`.

## 10 · Componer a izquierda y derecha

Con la zona útil de 1080 de ancho y un elemento de clase `objeto` de 800 px, el margen
lateral real es de **±140 px**. La banda `lado` del 16:9 —cuatro de las dieciséis
posiciones— desaparece. Lo que se mueve en vertical es la `y`. `201`.

## 11 · Copiar una tabla de zona segura de otro sitio

Para el margen inferior de Instagram sobre 1080×1920 circulan **cinco cifras distintas
fechadas el mismo mes**: 400, 420, 480, 192 y un rango de 384–672. Añadir una sexta no
mejora nada. Se mide con carta fiducial y se firma con fecha y dispositivo, o se trabaja
declaradamente con la hipótesis conservadora de `49`. `202`.

## 12 · Juzgar el vertical con el umbral de cobertura del 16:9

El objetivo 22–38 % está calibrado para 1920×1080. En vertical el techo real con la tabla
de clases es **22,9 %**, porque `heroe` y `objeto` juntos ya son 1231 px de una columna de
1200. El umbral vertical es **20–30 %**. Se cambia el umbral, no el montaje. `141`, `203`.

## 13 · Cortar el tramo por densidad

La ventana de 45 s más densa del episodio es 16,0–61,0 s con 60 elementos/min, y empieza a
mitad de la muerte del protagonista. Se corta por **límite de bloque**, que es donde la
locución respira. `208`.

## 14 · Fundir a negro al final

Tres de las cuatro redes reproducen en bucle: el último fotograma y el primero se ven
seguidos. Medio segundo de negro es medio segundo de permiso para deslizar, y además rompe
el bucle. `208`.

## 15 · Reusar la banda musical del episodio

En 60 segundos no cabe una progresión de 24 s: el corte empieza a mitad de frase musical y
se corta a la mitad. La música del vertical se monta con otras reglas. `128`.

## 16 · Publicar sin verlo en un teléfono

Es el único error de la lista que no tiene número, y por eso está el último: no se puede
medir, sólo se puede hacer. Ninguna tabla de zona segura, ninguna auditoría y ningún
fotograma de control sustituyen a subir el corte sin publicar y mirarlo con el pulgar
encima. `166`, `168`, `202`.

---

## La lista corta, para pegar en la pared

```
NO recortar el 16:9            →  1 elemento entero de 59
NO trasponer y ya              →  cobertura 36,1% → 11,4%
NO 4 simultáneos               →  la pila pide 2476 px de 1200
NO reusar piezas de texto      →  5 de 16 por debajo del suelo
NO reusar el pie del dato      →  16,9 px contra 22,3
NO empezar donde empieza       →  fotograma 0 con 0 elementos
NO subtitular de 2 en 2        →  bloques de 0,20 s
NO más de 18 car por línea     →  24 car = 1086 px de 820
NO cifra y subtítulo en el pie →  220 px de pie útil
NO componer a los lados        →  ±140 px de margen real
NO copiar zonas seguras        →  5 cifras del mismo mes
NO el umbral del 16:9          →  el techo vertical es 22,9%
NO cortar por densidad         →  se corta por bloque
NO fundir a negro              →  se ve en bucle
NO reusar la música            →  progresión de 24 s en 60
NO publicar sin teléfono       →  no hay sustituto
```

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Tomar esta lista por preferencias | Cada línea tiene un número detrás; la discusión es sobre el número |
| Saltarse uno «sólo esta vez» | Los de arriba son los que se ven de lejos; los de abajo, los que se notan sin saber por qué |
| Añadir reglas sin medirlas | Una lista de veinte puntos sin números deja de leerse |
| Aplicarla al 16:9 | Está escrita para 1080×1920; en 16:9 la mitad son falsos positivos |

## Relacionado

`200` el vertical se renderiza · `201` la columna · `202` la zona segura real ·
`203` densidad en vertical · `204` el texto manda · `205` el primer fotograma ·
`206` subtítulos siempre · `207` la cifra en vertical · `208` el cierre ·
`128` música para el vertical · `150` catálogo del fallo silencioso ·
editpro `147` formato vertical a fondo · editpro `359` formatos quemados
