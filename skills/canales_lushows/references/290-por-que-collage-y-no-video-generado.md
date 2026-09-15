# 290 · Por qué collage y no vídeo generado

**Qué resuelve:** la pregunta que aparece cada vez que alguien ve el canal: «con lo que
hay hoy, ¿por qué no generas los planos?». La respuesta no es estética. Son tres
argumentos independientes —dinero, derechos y verdad— y cada uno solo bastaría.

---

## 1. El dinero, medido hoy

`pipeline/costo.mjs` calcula una pieza de 600 s con 80 planos y 8.250 caracteres de voz.
Voz (0,13 $) y guion (0,35 $) van en todas las filas, así que la diferencia es **solo la
imagen**. Ejecutado hoy:

| Arquitectura | Coste/pieza | Veces el piso | Break-even a RPM 15 $ |
|---|---|---|---|
| **planos + Ken Burns por ffmpeg** | **1,52 $** | **1×** | **102 vistas** |
| híbrido: planos + gancho generativo de 8 s | 2,34 $ | 2× | 157 vistas |
| generativo · wan-2.6-1080p (el más barato) | 30,48 $ | **20×** | 2.033 vistas |
| generativo · veo-3.1-standard | 240,48 $ | 158× | 16.033 vistas |
| generativo · seedance-2.5-720p (fal) | 284,28 $ | 187× | 18.953 vistas |
| generativo · seedance-2.5-1080p (fal) | **698,88 $** | **459×** | 46.593 vistas |

**Entre 20 y 459 veces.** Y la columna que decide no es el coste: es el break-even. Un
episodio de este canal es rentable con **102 vistas**; el mismo episodio en Seedance
1080p necesita **46.593**. Con un canal nuevo, esa diferencia no es un margen: es la
diferencia entre publicar y no publicar.

Y el piso real es todavía más bajo, porque este canal **ni siquiera genera las imágenes**.
Los 1,52 $ suponen 80 planos generados con un modelo de imagen. Aquí los planos son
recortes de archivo descargados de Commons y fondos dibujados en Chrome: el coste de
imagen del `ep01-lustig` es **cero**, y la pieza entera son los 0,48 $ de voz y guion.

Tres matices que evitan discusiones:

- **Los agregadores cobran el doble.** El mismo Seedance 2.5 480p: 0,2205 $/s en fal,
  0,1028 $/s en BytePlus, que es el fabricante. 2,1× por el intermediario.
- **Auto-hospedar no gana.** Se paga la GPU por hora encendida, no por segundo útil.
  Empata solo con utilización alta y sostenida, que un canal de un episodio por semana
  no tiene.
- **El vídeo largo profesional nunca fue vídeo continuo.** Son 60–90 planos de 5–10 s. El
  gancho (0–8 s) sí merece generativo porque decide el CTR; los otros 592 s no.

> Re-verificar esta tabla cada mes: el mercado se mueve semanalmente. `node
> pipeline/costo.mjs --rpm 15`.

## 2. Los derechos: lo que se puede defender

El `ep01-lustig` se monta sobre **80 fuentes**, y el manifiesto (`199`) las tiene todas
con licencia, autor y URL:

| Licencia | Piezas |
|---|---|
| Public domain | 66 |
| CC0 | 14 |
| **Total, todas de Wikimedia Commons** | **80** |

Eso se defiende en veinte minutos (`189`): se abre el manifiesto, se copia la URL, se
responde. Un plano generado no tiene esa columna. No es que esté prohibido: es que **no
hay nada que enseñar**. Si el modelo devolvió algo que se parece demasiado a una foto con
dueño, la reclamación llega igual y la respuesta es «lo hizo un modelo», que no es una
respuesta. Se cambia un riesgo documentado por uno opaco.

## 3. La verdad: la línea que no se cruza

**Este canal no genera caras de personas reales con IA. Nunca.** No como estilo: como
regla dura (`383`, del bloque de ética, aún por escribir; hasta entonces esta es la
formulación de referencia). Un canal que cuenta historias verificadas no puede fabricar
la imagen de alguien que existió y presentarla junto a un certificado de defunción real.
En el momento en que una cara es inventada, el espectador ya no sabe qué más lo es, y el
episodio entero pierde lo único que lo sostiene.

Cuando no hay foto de alguien, las salidas son tres, y ninguna es generarlo: se usa el
documento que sí existe, se rotula el hueco (`275`), o se ilustra el entorno y no la
persona. `176` explica cuándo un caso directamente no se puede ilustrar.

## 4. El límite que no es el coste

Aunque el vídeo generativo fuese gratis, seguiría sin usarse para el cuerpo del episodio.
En febrero de 2026 YouTube terminó 11 canales y vació 6 —35 M de suscriptores, 4.700 M de
vistas— por contenido no auténtico, y lo penalizado incluye literalmente «presentaciones
de imágenes IA con narración sintética». Que es la arquitectura barata.

Lo que separa este canal de eso no es la técnica —también hay imágenes fijas y voz
sintética— sino **el aporte original** (`92`): el archivo primario leído, las dos columnas
de lo que consta contra lo que se cuenta (`270`), y las piezas de datos construidas para
este caso. La técnica es idéntica; el criterio editorial es lo que se juzga.

## 5. El argumento que nadie pone en la hoja de cálculo: se puede corregir

Un plano generado es una caja negra de cinco segundos. Si al revisar el episodio resulta
que ese plano no se separa del fondo, o que el texto que salió dentro dice algo que no es,
o que hay que cambiarle la duración porque el guion se movió medio segundo, **no hay nada
que tocar**: se vuelve a generar, se vuelve a pagar, y sale otro plano distinto que a lo
mejor tiene otro problema.

Aquí cada plano es una tabla de eventos y un puñado de PNG:

| Qué cambia | Qué cuesta |
|---|---|
| Un recorte no se ve sobre su fondo | Una gamma y volver a componer (`292`) |
| El cuadro sale plano | Un ancho en el guion visual (`293`) |
| Un gráfico no se lee | Regenerar el HTML y recapturar (`297`) |
| El guion mueve media frase | Nada: los elementos van anclados a la palabra (`298`) |
| Hay que publicar una corrección | Se rehace el plano afectado, no el episodio |

Eso es lo que permite auditar antes de renderizar y arreglar en segundos lo que se
encuentra. Un canal que tiene que pagar cada iteración deja de iterar, y entonces lo que
publica es el primer intento.

## 6. Qué se hace con el presupuesto que se ahorra

No desaparece: se gasta en lo que sí se nota. Con la diferencia entre 1,52 $ y 284 $ se
pagan cuarenta horas de archivo, la verificación de datos y la locución en varios idiomas
—que multiplica las vistas de la misma pieza— antes que ocho segundos de cámara virtual
que nadie recuerda.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Comparar coste por segundo en vez de break-even | 30 $ suena barato hasta que son 2.033 vistas de umbral |
| Comprar el modelo a través de un agregador | 2,1× el precio de fábrica por el mismo modelo |
| Auto-hospedar «porque sale gratis» | Se paga la GPU encendida; empata solo con uso sostenido |
| Generar un plano «que se parezca» a una foto con dueño | Riesgo opaco: no hay licencia que enseñar |
| Generar la cara de alguien que existió | Se cruza `383`; el episodio pierde su única garantía |
| Creer que el coste era el límite | El límite es la política de contenido no auténtico |
| Dejar el gancho sin generativo por dogma | Los 8 s del gancho deciden el CTR y ahí sí paga |

## Relacionado

`92` el aporte original · `130` la obra es libre, la grabación no · `180` las familias de
licencia · `189` defender un episodio · `199` el manifiesto del material ·
`275` el hueco rotulado · `176` cuando un caso no se puede ilustrar ·
`270` papel contra leyenda · `383` caras generadas: la línea · `291` el borde de papel
