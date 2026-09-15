# 185 · Lo que parece libre y no lo es

**Qué resuelve:** el catálogo de espejismos. Todos comparten la misma forma: **algo que
parece una autorización y no lo es** — un buscador, una frase en un blog, una web de
museo, una foto de un cuadro antiguo. Aquí están, uno por uno, con la pregunta que los
desmonta.

> ⚠️ **Esto no es asesoría legal.** Es el criterio de descarte del canal. Ante la duda,
> la pieza no entra.

---

## La regla que los explica todos

> **La licencia es una propiedad de la obra, no del sitio donde la encontraste.**

Un buscador, un repositorio o un blog son **dónde la viste**. La licencia la pone quien
tiene los derechos, y vive en la ficha del ítem. Todo lo que sigue es esa confusión con
distintos disfraces.

## El catálogo

| Espejismo | Qué es realmente | La pregunta que lo desmonta |
|---|---|---|
| Resultados de búsqueda de imágenes | Un índice de páginas ajenas. No otorga nada | ¿Cuál es la **ficha del ítem** y qué dice? |
| Filtro «licencias Creative Commons» del buscador | Una **pista** basada en metadatos que a menudo están mal | ¿Lo confirma la página original? |
| «Imagen sin copyright» en un blog | La opinión de alguien que tampoco lo comprobó | ¿De dónde la sacó **él**? |
| «Encontrada en internet» / «crédito al autor» | Confesión de que no hay licencia | ¿Quién es el autor y qué licencia puso? |
| Banco de imágenes «gratis» | Gratis ≠ libre: hay licencias propias con exclusiones | ¿Qué dice **su** licencia sobre uso comercial y redistribución? |
| «Royalty free» | Contrato de pago único, no licencia abierta | ¿Se compró? ¿A nombre de quién? |
| «Uso editorial» | Marca de agencia (§ 186) | — descarte directo |
| Foto sin marca de agua | La marca se quita recortando; el derecho no | ¿Aparece la misma foto en un banco de pago? |
| Web de museo o biblioteca | Puede publicar obra ajena y poner condiciones propias | ¿Hay una etiqueta de licencia **por ítem**? |
| Fotograma de película o TV | Protegido como la obra entera (§ 187) | — descarte directo |
| Portada de periódico o revista | Diseño, tipografía y fotos con derechos vigentes | ¿Existe el **documento** en un archivo público? |
| Captura de Google Maps / Street View | Producto con licencia propia y restringida | ¿Hay una foto libre del mismo lugar? |
| Imagen generada con IA por terceros | Régimen incierto y sin trazabilidad de lo que la entrenó | ¿Podemos probar su origen? No → fuera |

## Los dos casos que hay que entender de verdad

### 1. Capturas y descargas de webs de museo

Un museo puede ser dueño del cuadro y **no serlo de los derechos**, o al revés. Y casi
todos añaden **términos de uso propios** sobre sus imágenes de alta resolución, que son
un contrato con quien las descarga, no una declaración sobre el derecho de autor.

Lo que hacemos: si el museo publica el ítem con una etiqueta de licencia clara
(`CC0`, `Public Domain Mark`, `No known copyright restrictions`), se anota esa etiqueta
literal. Si solo hay unos «términos de uso» generales, la pieza **no entra**: se busca la
misma obra en Commons, donde la licencia está declarada por archivo.

### 2. La obra vs. la fotografía de la obra

Es la distinción más importante de este módulo. Una foto de un cuadro tiene **dos capas
posibles** de derechos: la del cuadro y la de la foto.

- **Objeto plano (cuadro, grabado, cartel, documento, billete).** Una reproducción
  fotográfica fiel de una obra bidimensional en dominio público se considera, en la
  política de Wikimedia Commons, sin copyright propio: es la etiqueta `PD-Art`, y exige
  que **la obra de base sea libre tanto en EE.UU. como en su país de origen**
  ([Commons: When to use the PD-Art tag](https://commons.wikimedia.org/wiki/Commons:When_to_use_the_PD-Art_tag)).
- **Objeto tridimensional (escultura, edificio, máquina, una imprenta, un lingote).**
  Cuando la fotografía tiene originalidad —encuadre, luz, punto de vista— **tiene
  copyright propio aunque el objeto fotografiado no lo tenga**. La regla que usa el
  propio Commons como atajo es: **«2D vale, 3D no»**.

Traducido a nuestro trabajo: el billete falsificado, el certificado de defunción y el
cartel de búsqueda suelen ser casos limpios. La foto de la Torre Eiffel, la de una
imprenta o la de un coche de época **son obras del fotógrafo**, y necesitan su propia
licencia por mucho que el objeto sea antiguo.

🔴 **Pendiente de verificar:** `PD-Art` es una **política de Commons** respaldada por su
posición institucional, no una regla idéntica en todas las jurisdicciones. Algunos países
reconocen protección a reproducciones fotográficas. Si una pieza `PD-Art` va a ser el
plano protagonista o la miniatura del episodio, se busca alternativa o se consulta.

## Cómo se descarta en la práctica

Tres preguntas, por escrito, antes de que la pieza toque el disco:

1. **¿Cuál es la ficha del ítem?** Si la respuesta es una búsqueda, un pin de Pinterest o
   un blog: no hay ficha, no hay pieza.
2. **¿Qué dice la licencia, literalmente?** Se copia el texto. Si hay que resumirlo o
   interpretarlo, cae (§ 180).
3. **¿La foto es de la obra, o es la obra?** Si es la foto de un objeto en 3D, necesita
   licencia propia.

El sondeo automatiza justo esto: `sondeo.py` solo consulta la API de Commons y solo
guarda piezas cuyo `LicenseShortName` / `UsageTerms` pasa el filtro. **Todo lo que entra
a mano, fuera del sondeo, es material de riesgo** y necesita las tres preguntas por
escrito antes de anotarse en `fuentes.json`.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Fiarse del filtro de licencias de un buscador | Metadatos erróneos: material no libre con apariencia de libre |
| Descargar de la web del museo «porque el cuadro es de 1700» | La obra es libre; la foto y los términos del museo, otra cosa |
| Tratar una foto de un objeto 3D como si fuera el objeto | Es obra del fotógrafo: hace falta su licencia |
| Quitar la marca de agua | Confirma que sabías que no era libre: agrava el problema |
| «Crédito al autor» como sustituto de licencia | El crédito no autoriza nada por sí solo |
| Meter una pieza a mano saltándose el sondeo | Entra sin filtro y sin registro; es por donde se cuela todo |
| Usar IA de terceros como archivo | Sin trazabilidad no hay defensa posible (§ 189) |

## Relacionado

`180` las familias de licencia · `181` dominio público por antigüedad ·
`186` fotos de agencia · `187` fotogramas de película ·
`188` `fuentes.json` como compuerta · `179` hemerotecas y sus muros
