# 137 · El sonido de archivo

**Qué resuelve:** el único audio ajeno que puede entrar a un episodio y bajo qué
condiciones. Una grabación histórica real —un discurso, una llamada, el ambiente de una
sala— tiene un peso documental que ninguna síntesis alcanza. También tiene reglas
propias, distintas de las de la imagen.

> ⚖️ **Esto no es asesoría legal.** Es el filtro de producción. Cuando el filtro no da
> una respuesta clara, la salida es no usar el audio, no usarlo «con cuidado».

---

## La regla de partida

**El sonido de archivo entra solo si es diegético y necesario.** Si lo que aporta es
ambiente, se sintetiza (§ 83, § 135). Si lo que aporta es **el documento en sí** —la voz
real de quien dijo aquella frase—, entonces merece pasar por el filtro.

Y el filtro es más duro que con la imagen, por una razón concreta: en audio hay que
comprobar **dos derechos** (la obra y el fonograma, § 130) y las fichas de archivo suelen
hablar solo del primero.

## Las tres familias, con reglas distintas

| Familia | Qué es | La trampa propia |
|---|---|---|
| **Grabación histórica** | un discurso, una emisión, una declaración | el fonograma tiene plazo propio, y casi nunca coincide con el de la obra |
| **Archivo público / CC** | Wikimedia Commons, archivos nacionales, repositorios de sonido | la licencia es **por archivo**, no por repositorio |
| **Obra del gobierno federal de EE. UU.** | material producido por empleados federales en el ejercicio de su cargo | **no cubre a los contratistas** ni al material ajeno que la agencia reproduce |

### Sobre la obra del gobierno federal
La norma estadounidense (17 U.S.C. § 105) excluye de protección «las obras del Gobierno
de los Estados Unidos», definidas como las preparadas por un funcionario o empleado
federal **como parte de sus funciones oficiales**
([uscode.house.gov](https://uscode.house.gov/view.xhtml?req=%28title%3A17+section%3A105+edition%3Aprelim%29)).

Dos límites que provocan casi todos los errores:

1. **Contratistas.** Una obra hecha por un contratista con fondos federales **puede
   estar protegida**: la agencia decide caso por caso si permite al contratista
   registrar el derecho. No es automático que sea libre.
2. **Material reproducido.** Que una agencia federal publique una foto o un audio en su
   web no lo convierte en suyo. Puede ser material de agencia con licencia. Es la
   confusión más común de todas (§ 96).

Y algo obvio que se olvida: esto es **derecho estadounidense**. No dice nada sobre las
obras de otros gobiernos.

## Cómo se verifica, paso a paso

```
1. FICHA DEL ÍTEM   abrir la página del archivo concreto, nunca la del
                    buscador ni la de la categoría.
2. LICENCIA LITERAL copiar el texto tal cual aparece. No resumirlo.
3. ¿OBRA O          buscar explícitamente quién es el titular de LA
   FONOGRAMA?       GRABACIÓN. Si la ficha solo habla de la obra,
                    falta la mitad del trabajo.
4. FECHA Y LUGAR    de la grabación, no de la digitalización.
5. ETIQUETAS        distinguir "dominio público" de fórmulas como
   AMBIGUAS         "sin restricciones de copyright conocidas": la
                    segunda dice que el archivo no encontró titular,
                    no que no lo haya.
6. CLÁUSULAS        NC (no comercial) es incompatible con un canal
   QUE MATAN        monetizado. ND (sin derivadas) es incompatible con
                    montarlo dentro de un episodio.
7. DESCARGAR        el archivo y la captura de la ficha. El enlace no
                    es prueba: la página cambia.
```

Si en el paso 3 no hay respuesta, se para ahí.

## Repositorios y lo que hay que saber de cada uno

- **Wikimedia Commons.** Estar en Commons **no** significa libre: cada archivo lleva su
  licencia y las hay incompatibles con uso comercial. La ficha manda.
- **LibriVox.** Las grabaciones se donan al dominio público por los propios lectores.
  Ojo con el texto leído: tiene que ser libre **también** (una traducción moderna de un
  clásico puede no serlo).
- **Bancos de efectos colaborativos.** Conviven CC0, CC BY y CC BY-NC en el mismo sitio.
  **NC descarta la pieza** para este canal. Y la atribución de CC BY hay que ponerla, en
  la descripción del episodio (§ 345).
- **Archivos nacionales y hemerotecas.** Condiciones propias por institución.

## Las tres trampas específicas del audio

1. **YouTube no es un archivo.** Un discurso subido por un tercero no acredita nada: hay
   que ir a la fuente institucional. Extraer audio de YouTube está en § 139.
2. **Las remasterizaciones.** Mucho «audio de época» que circula es una remasterización
   moderna. Si remasterizar genera un fonograma nuevo con plazo nuevo es discutible y
   varía por territorio ⚠️ **pendiente de verificar**; criterio del canal: **tratarla
   como protegida y no usarla**.
3. **La música de fondo del archivo.** Una grabación de noticiero libre puede llevar
   música protegida debajo. Si no se puede aislar la voz limpia, no entra.

## Cómo se registra

Toda pieza de archivo sonoro tiene entrada en el manifiesto (§ 138) con estos campos
además de los habituales:

```
alias ............ discurso_1971_nixon
tipo ............. archivo_sonoro
institución ...... <archivo o repositorio, con la URL del ÍTEM>
fecha_grabacion .. <la real, no la de digitalización>
titular_obra ..... <quién / dominio público / desconocido>
titular_fonograma  <quién / dominio público / desconocido>   ← el campo que falta siempre
licencia_literal . "<copiada tal cual>"
fecha_consulta ... <cuando se descargó, con captura guardada>
uso .............. <episodio y tramo>
```

Si `titular_fonograma` queda en `desconocido`, la pieza no pasa la compuerta.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Comprobar la obra y olvidar el fonograma | El error de § 130, en su versión de archivo |
| Tomar «sin restricciones conocidas» por dominio público | Se asume libre lo que solo está sin identificar |
| Usar material de una web `.gov` sin mirar de quién es | Foto o audio de agencia dentro de un vídeo monetizado |
| Dar por libre lo hecho por un contratista federal | Puede estar protegido: no es automático |
| Usar una pieza CC BY-NC | Incompatible con monetización, y se descubre tarde |
| Olvidar la atribución de una CC BY | La licencia deja de cubrirte |
| Bajar el audio de un vídeo de YouTube | Sin cadena de derechos y sin fuente citable |
| Guardar el enlace en vez del archivo y la captura | Cuando llega la reclamación no hay nada que enseñar |

## Relacionado

`83` sonido diegético · `96` verificación de datos · `130` la obra y la grabación ·
`131` dominio público por país · `138` registrar lo propio · `139` lo que nunca entra
