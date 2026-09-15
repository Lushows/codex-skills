# 177 · Archivos federales de EE.UU.

**Qué resuelve:** la mayor reserva de imagen libre que existe para historias de dinero, y
cómo se entra en ella sin equivocarse.

---

## La regla que lo abre todo

Una obra creada por un empleado del gobierno **federal** de Estados Unidos en el ejercicio
de su cargo **no tiene derechos de autor**: es dominio público desde el primer día, sin
plazos y sin país de origen que discutir. Eso convierte a las agencias federales en la
fuente número uno del canal.

**Tres límites que se olvidan siempre:**

1. **Federal, no estatal ni municipal.** La policía de Houston o el estado de Texas **sí**
   tienen derechos. Solo lo federal es automático.
2. **Empleado, no contratista.** Una foto encargada a una agencia externa puede seguir
   siendo de la agencia.
3. **Publicado por, no propiedad de.** Un organismo federal puede publicar en su web una
   foto de agencia con licencia: publicarla no la libera.

## Lo que hay, medido

Todo esto se puede tocar a través de Commons, que es donde ya está el material con la
licencia comprobada por otros. Cifras reales del 11-sep-2026:

| Categoría de Commons | Archivos | Subcats |
|---|---|---|
| `PD US Government` | **685.626** | 83 |
| `Images from the Library of Congress` | **631.061** | 56 |
| `Images from the National Archives and Records Administration` | **468.078** | 25 |
| `United States Department of Justice` | 233 | 30 |
| `United States Congress` | 203 | 56 |
| `Mug shots` | 180 | 10 |
| `United States Marshals Service` | 80 | 15 |
| `Wanted posters of the Federal Bureau of Investigation` | **92** | 2 |

Y pasando el filtro de licencia y tamaño del sondeo:

```
Federal Bureau of Investigation ............ 206 crudo →  104 aceptadas
Drug Enforcement Administration ............ 120 crudo →   60 aceptadas
United States Secret Service ................ 76 crudo →   52 aceptadas
Supreme Court of the United States ........... 91 crudo →   25 aceptadas
Wanted posters of the FBI .................... 92 crudo →   48 aceptadas (100 % dominio público)
```

## El hallazgo: los carteles de busca y captura

`Category:Wanted posters of the Federal Bureau of Investigation` da **48 piezas, todas en
dominio público**, y algunas enormes:

```
9560x9600   File:John Dillinger FBI wanted poster.jpg
4902x4872   File:Kathy Boudin FBI wanted poster issued 1 May 1970.jpg
3225x5006   File:EdwardleehowardWantedPoster.jpg
3212x3224   File:Dutch Schultz Wanted Poster.jpg
```

Un cartel a 9560×9600 se puede recortar en ocho planos distintos —la foto, la firma, la
recompensa, el texto legal— y cada uno es un elemento de montaje nuevo. De las 48, **24
superan los 1100 px** de ancho, que es la barra de `curar.py`. Es el mejor rendimiento por
pieza de todo el archivo federal: documento real, gráficamente potente y libre del todo.

## Dónde está cada cosa

| Organismo | Qué aporta a una historia de dinero |
|---|---|
| **FBI** | Carteles de busca y captura, fotos de operativos, y el archivo desclasificado (*The Vault*), con expedientes escaneados completos |
| **U.S. Marshals Service** | Las fichas policiales federales. `File:Ken Lay.jpg` y `File:Jeffrey Skilling mug shot.jpg` son suyas |
| **DEA** | Incautaciones: dinero en efectivo apilado, laboratorios, aviones. El plano «montaña de billetes» real |
| **Departamento de Justicia** | Ruedas de prensa, retratos oficiales de fiscales, salas |
| **Congreso** | Audiencias e informes escaneados. Las de Enron están en Commons a 1275×1650 |
| **Tribunales federales** | Sedes, salas, retratos de jueces |
| **NARA** (Archivos Nacionales) | El fondo histórico: fotografía del siglo XX por cientos de miles |
| **Biblioteca del Congreso** | Fotografía de prensa antigua, colecciones enteras digitalizadas |
| **NASA** | Imagen de la Tierra, satélite, infraestructura; útil para escala y mapa |
| **Reserva Federal, Tesoro, SEC, GAO** | Gráficos, sedes, billetes, informes |

## La vía de trabajo

Se entra **por Commons**, no por la web del organismo. En Commons la licencia ya está
declarada en `extmetadata`, el archivo está en resolución máxima y la URL de descripción
es citable. La web del organismo sirve para **encontrar** el documento; la descarga y la
prueba de licencia salen de Commons.

Excepción: cuando el documento concreto no está en Commons —una acusación reciente, un
informe de la GAO— se descarga del organismo y se anota a mano en el `fuentes.json` con la
base legal («obra del gobierno federal de EE.UU.»), sin inventar un enlace que no se haya
comprobado.

## Cuidado con las categorías gigantes

`PD US Government` tiene 685.626 archivos. No se piden 500 de golpe: la API devuelve
`HTTP 504 Gateway Timeout` y el sondeo queda a medias **sin dar error**. Se baja al
subárbol concreto (`Drug Enforcement Administration`, no `PD US Government`) y se pide de
100 en 100 (`193`).

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Dar por federal lo estatal o municipal | Foto con derechos usada como si fuera libre |
| Suponer que todo lo publicado por una agencia es suyo | Foto de agencia colada en el episodio |
| Pedir 500 archivos de `PD US Government` | 504 silencioso y sondeo incompleto |
| Bajar la foto de la web del organismo sin anotar la base legal | El episodio deja de ser defendible |
| Ignorar los carteles de busca y captura | Se pierde el material más potente y más libre que hay |

## Relacionado

`90` · `170` · `171` · `178` · `182` · `188` · `193`
