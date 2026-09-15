# 179 · Hemerotecas y sus muros

**Qué resuelve:** la prensa de época es donde vive la prueba de casi todos los casos, y es
también el archivo más cerrado. Qué se puede y qué se documenta como no verificable.

---

## Por qué importa tanto la prensa vieja

Un titular de portada del día de la quiebra es, a la vez, prueba y plano: dice la fecha,
dice la cifra y se ve bien en pantalla. Un recorte de periódico con la fecha visible hace
en tres segundos lo que la voz tardaría veinte en contar. Para historias anteriores a la
era digital suele ser **el único material gráfico del caso** que existe.

## El muro medido: la Biblioteca del Congreso

La Biblioteca del Congreso tiene el mayor fondo de prensa histórica digitalizada de
Estados Unidos, y **bloquea el acceso programático**. Probado el 11-sep-2026 con
User-Agent propio y contacto:

```
LoC · búsqueda JSON (www.loc.gov ... &fo=json) ...... HTTP 403 Forbidden
LoC · Chronicling America (…&format=json) ........... HTTP 403 Forbidden
LoC · la propia portada del sitio ................... HTTP 403 Forbidden
```

No es un problema de parámetros ni de cabeceras: devuelve 403 hasta la portada. El sitio
se puede consultar **a mano en un navegador**; lo que no se puede es sondearlo con un
script. Para el flujo de trabajo del canal eso significa que la LoC **no entra en el
sondeo automático**, y que su material se busca por otra puerta.

## La otra puerta: la LoC dentro de Commons

Buena parte del fondo de la Biblioteca del Congreso ya está volcado en Commons, donde sí
se puede sondear:

```
Category:Images from the Library of Congress ....... 631.061 archivos
Category:Bain News Service ..........................     85 archivos
Category:National Photo Company Collection ..........    500+ archivos
Category:Harris & Ewing .............................     10 archivos
```

Ahí está la fotografía de prensa estadounidense de principios del siglo XX, con la
licencia ya declarada.

## La trampa de licencia que vive justo aquí

El material de la LoC y de Flickr Commons no dice «dominio público». Dice **«No known
copyright restrictions»** — *no se conocen restricciones de derechos*. Es material
utilizable, y contiene la palabra `copyright`, así que **cualquier filtro que vete por esa
palabra suelta lo tira entero**. Medido sobre `Category:Bain News Service`:

```
total de la categoría ................................. 85
pasan el filtro de licencias libres ................... 85
vetados por la palabra "copyright" dentro de la frase .. 54
aceptados finalmente .................................. 26

se pierde el 64 % de lo libre
```

Cincuenta y cuatro fotografías de prensa de los años diez y veinte, utilizables, tiradas
por un `re.search("copyright", ...)`. El veto tiene que casar la frase completa
(`no known copyright restrictions` es **libre**; `all rights reserved` es **veto**), nunca
la palabra suelta. Ver `171` y `185`.

## Qué otras puertas sí responden

Probado el mismo día, sin clave:

```
Internet Archive · advancedsearch.php ..... HTTP 200
Gallica (BnF) · SRU ....................... HTTP 200 · dc:rights = "domaine public"
Commons · api.php ......................... HTTP 200
```

| Fuente | Qué aporta | Cómo se entra |
|---|---|---|
| **Commons** | Prensa ya volcada con licencia declarada | API, sin clave (`171`) |
| **Gallica (BnF)** | Prensa francesa desde el XIX, millones de páginas | API SRU, sin clave (`178`) |
| **Internet Archive** | Publicaciones escaneadas, boletines, informes | API de búsqueda, sin clave |
| **Biblioteca del Congreso** | El fondo estadounidense | Solo a mano; 403 a los scripts |
| **Hemerotecas de prensa privada** | El titular exacto que se busca | De pago y **con derechos**: se lee, no se usa |

## La línea roja de la prensa privada

Que un periódico digitalizado se vea en una hemeroteca de pago **no lo hace libre**. Se
puede leer para verificar un dato, y el dato se cita como fuente en la descripción. Lo que
no se puede es capturar la página y ponerla en pantalla. Un recorte de prensa solo entra
al montaje si:

1. Está en Commons o en un archivo con licencia declarada, **o**
2. Es dominio público por antigüedad y se ha comprobado el año y el país (`181`), **o**
3. Se **reconstruye**: se compone un recorte con la tipografía del canal, citando el medio
   y la fecha, y se rotula como reconstrucción. No se falsifica una portada real.

## Cómo se documenta lo que no se pudo verificar

Un episodio serio también dice lo que no pudo comprobar. En el `fuentes.json` o en la nota
del episodio se deja escrito, con fecha:

```
verificacion_pendiente:
  - dato: "portada de The Houston Chronicle del 3-dic-2001"
    estado: NO VERIFICADO
    motivo: "loc.gov devuelve HTTP 403 a peticiones programáticas (11-sep-2026);
             el ejemplar no está en Commons"
    accion: "no se muestra la portada; el titular se cita en voz, atribuido"
```

Eso hace dos cosas: evita que el dato entre en pantalla como si estuviera probado, y evita
que dentro de seis meses alguien repita la misma búsqueda fallida.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Vetar por la palabra `copyright` | Se tira el 64 % de la prensa libre de la LoC |
| Insistir contra el 403 de la LoC | Horas perdidas; el bloqueo es del sitio, no del script |
| Capturar una página de hemeroteca de pago | Reclamación de derechos y credibilidad del canal |
| Componer una portada falsa con aspecto real | Falsificación documental, aunque el dato sea cierto |
| No dejar constancia de lo no verificado | El dato se cuela en pantalla como probado |
| Sondear solo en inglés | Gallica tiene millones de páginas que nadie mira |

## Relacionado

`91` · `96` · `171` · `177` · `178` · `181` · `185` · `188`
