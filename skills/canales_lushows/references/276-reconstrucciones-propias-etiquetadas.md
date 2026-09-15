# 276 · Reconstrucciones propias, etiquetadas

**Qué resuelve:** el canal fabrica piezas —fichas, portadas, mapas, esquemas,
cronologías— porque el archivo no da para todo. Una pieza fabricada que parece un
documento **es un documento falso**, aunque se haya hecho con la mejor intención. Este
módulo es la línea entre reconstruir y falsificar, y la etiqueta que la sostiene.

---

## Qué es una reconstrucción aquí

Una pieza hecha por nosotros que representa algo real de lo que no tenemos imagen. En el
piloto son nueve de los cincuenta y nueve elementos del minuto 1: el esquema de la torre,
el marco de la ficha policial, la cronología, el mapa de ruta, el árbol genealógico, la
carpeta del expediente, las seis fichas de identidad, el documento a dos columnas y la
portada de prensa.

**No son reconstrucción** (y por tanto no llevan etiqueta de tal): los recortes de archivo
—esos llevan su crédito, § `184`—, los rótulos y las cifras animadas, los fondos del canal
y las figuras abstractas como la balanza.

## Los tres grados, y dónde está la raya

| Grado | Qué es | Etiqueta | ¿Se usa? |
|---|---|---|---|
| **1 · Diagrama** | Mapa, esquema, cronología, balanza. No se puede confundir con un documento | rótulo de contenido | Sí, libremente |
| **2 · Facsímil de formato** | Una ficha, una carpeta, un formulario **con nuestra tipografía y nuestro nombre** | etiqueta explícita de reconstrucción | Sí, con las cuatro reglas de abajo |
| **3 · Imitación de un documento real** | Un papel que pretende pasar por el original: membrete ajeno, sello de un organismo, fecha concreta, tipografía de época | — | **Nunca** |

El grado 3 no es una cuestión de grado estético. Es fabricar prueba. Da igual que lo que
diga sea cierto: si la pieza sale del vídeo recortada y circula como «el documento», el
canal ha puesto en el mundo un falso, y su única defensa —la credibilidad— era justamente
lo que vendía.

## El caso: la portada de prensa

La pieza más peligrosa del piloto es `titular_prensa`: una portada con el titular
*«VENDIDA LA TORRE EIFFEL COMO CHATARRA»*, que ilustra una afirmación que **no consta**.
Riesgo evidente: en cuanto sale de la pantalla, alguien la recorta y circula como «el
periódico de 1925».

Por eso **la pieza se delata a sí misma por cuatro sitios distintos**, de modo que ningún
recorte razonable pueda quitarlos todos:

| Aviso | Dónde | Qué dice |
|---|---|---|
| 1 | banda roja superior | `RECONSTRUCCIÓN · PAPER EMPIRES` · `NO ES UN DOCUMENTO DE ARCHIVO` |
| 2 | la cabecera | **PAPER EMPIRES**: nuestro nombre, no el de un diario inventado |
| 3 | sello cruzado sobre el cuerpo | `RECONSTRUCCIÓN`, a −10°, en rojo |
| 4 | el pie | `PIEZA RECONSTRUIDA POR PAPER EMPIRES` · `NO ES UN DOCUMENTO REAL` |

Y tres decisiones más, que son las que separan esta pieza de una falsificación bonita:

- **Ningún diario real implicado y ninguna fecha exacta.** El subtítulo dice `EDICIÓN
  FIGURADA · SIN FECHA COMPROBADA`. Inventar *Le Matin, 14 de mayo de 1925* sería atribuir
  a un periódico que existió una portada que no publicó.
- **Cero texto falso legible.** El cuerpo son **barras grises**, no párrafos inventados:
  *un párrafo inventado invita a leerlo y a creérselo; una barra gris se lee como lo que
  es, un hueco.*
- **El hueco de foto, aspado y rotulado** `SIN IMAGEN DE ARCHIVO`, y un pie en cursiva:
  *«Es la versión que ha llegado hasta hoy. Paper Empires no ha localizado prensa de 1925
  que la recoja.»* La pieza que ilustra la leyenda **es ella misma una declaración de que
  falta el papel**.

## Las cuatro reglas del facsímil

1. **Que lleve nuestro nombre**, no el de nadie. Una cabecera inventada que suene a diario
   francés de los años veinte es peor que la nuestra: parece real y no se puede desmentir.
2. **Que la etiqueta sobreviva al recorte.** Un aviso solo abajo se va con la primera
   captura de pantalla. Cuatro, repartidos, no.
3. **Que ninguna cifra de la pieza carezca de fuente.** La chapa del marco de la ficha
   policial dice `ROBERT V. MILLER · 5954-H` y debajo, en pequeño, `CERTIFICADO DE
   DEFUNCIÓN, CASILLA 3(a)`. El dato y su procedencia viajan juntos dentro del PNG, no en
   un rótulo aparte que puede caerse del montaje.
4. **Que lo que no se sabe se quede vacío** y rotulado (§ `275`), nunca rellenado a ojo.

## La regla de las cifras: `NUNCA_AUTO`

Una reconstrucción con números propios **no puede colocarse por diccionario**. Si cuelga
de una palabra cualquiera, tarde o temprano contradice a la voz:

```python
NUNCA_AUTO = {"linea_00", "linea_01", "linea_02", "linea_04",
              "linea_05", "linea_06", "d_1890", "torre_esquema"}
```

El motivo está escrito en el propio vocabulario y viene de un episodio real: *un dibujo de
cotas decía «1,00 m» mientras la voz decía «trece mil setecientos metros»*. Nadie mintió
al escribirlo; lo colocó el generador. Estas piezas van **a mano, ancladas a su dato
exacto**, y por eso viven en la capa CLAVE (§ `250`).

## El marco sin cara

`marco_ficha` es una ficha policial **vacía**: dos ventanas rotuladas `FRENTE` y `PERFIL`,
y la foto de dominio público se pone encima desde la tabla de eventos. *Aquí no se dibuja
ninguna cara.* La rejilla de medición va sin números porque no sabemos su estatura y no se
inventa —y lleva rótulo, porque cada elemento se explica.

Si no hubiera foto libre, el marco se quedaría vacío y rotulado. Lo que **nunca** ocurre
es que se dibuje o se genere una cara: es regla roja del canal y su porqué doble está en
§ `277` y § `136`.

## La frontera con envejecer material

`197` explica cómo envejecer un recorte **real** para que empate con el fondo. No es lo
mismo:

| Se hace | No se hace |
|---|---|
| Envejecer una foto de archivo real para que case con el collage | Envejecer una pieza **nuestra** para que parezca de época |
| Dar textura de papel a nuestra ficha, con su etiqueta visible | Dar textura de papel a nuestra ficha **y quitarle la etiqueta** |
| Manchar y ladear la marca `m_cuenta`, que es un rótulo del canal | Manchar un facsímil hasta que parezca un escaneo de archivo |

Regla corta: **el desgaste es lenguaje visual mientras la pieza siga diciendo que es
nuestra.** En cuanto el desgaste sustituye a la etiqueta, es disfraz.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Inventar un nombre de periódico o un membrete de organismo | Se atribuye a un tercero algo que no publicó |
| Poner una fecha concreta en un facsímil | Convierte la pieza en documento datado: falso verificable |
| Texto de relleno legible en un documento reconstruido | Se cita como fuente el día que alguien lo recorta |
| Una sola etiqueta, y abajo | Desaparece en la primera captura |
| Cifra propia colocada por el diccionario | «1,00 m» mientras la voz dice trece mil setecientos |
| Dibujar lo que falta (huellas, caras, alias) | Se fabrica prueba: exactamente lo que el canal denuncia |
| Envejecer una pieza propia hasta que parezca archivo | Disfraz, no reconstrucción |

## Relacionado

`275` el hueco rotulado · `277` personas vivas · `271` las dos columnas en pantalla ·
`96` verificación de datos · `136` voz generada y derechos · `176` cuándo un caso no se
puede ilustrar · `184` la atribución en la descripción · `197` envejecer para que empate ·
`250` palabra a imagen · `43` rótulos y etiquetas
