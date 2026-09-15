# 159 — Campaña multipieza: un rodaje, diez piezas

> Grabar es lo caro. Montar es lo barato. El error económico más común de un negocio que hace video es
> hacer **un rodaje para una pieza**: gastas la mañana entera, sacas un video, lo pones en pauta, y si
> no funciona no tienes nada más. La forma correcta es planear el rodaje para que salgan **diez a
> quince piezas distintas**, y dejar que la pauta decida cuál es buena. Este módulo es ese sistema.

---

## El principio: la pauta no premia el video bueno, premia el video que ganó la prueba

Nadie sabe de antemano cuál ángulo va a funcionar. Ni tú, ni yo, ni una agencia. Lo que sí se sabe es
que **la variación de creativo produce más resultado que la optimización de campaña**. Meta y TikTok
en 2026 reparten el presupuesto solo si hay varias piezas compitiendo: con un creativo único, el
algoritmo no tiene nada que optimizar y el CPM sube por fatiga en 5–10 días.

La consecuencia práctica: necesitas **caudal de creativos**, no perfección. Y el caudal solo es
sostenible si sale de un mismo rodaje.

---

## Los cuatro ejes de variación

Cada pieza nueva sale de cambiar **uno** de estos cuatro ejes, dejando los otros tres iguales. Así
puedes leer el resultado: si cambias tres cosas a la vez, no sabes qué funcionó.

### Eje 1 — El gancho (primeros 3 segundos)

El de mayor impacto por mucho. El mismo cuerpo con seis aperturas distintas son seis piezas.

Tipos de gancho para producir en el mismo rodaje:
- **Pregunta directa:** "¿Sabes cuánto te deja tu plato estrella?"
- **Afirmación incómoda:** "Tu plato más vendido te está quebrando."
- **Visual puro sin palabras:** el chorro, el corte, el número cambiando.
- **Cifra:** "El 70% de los restaurantes cobra mal."
- **Negación:** "Esto no es para ti si ya sabes tus costos."
- **Contexto personal:** "Llevo tres años con un bar y esto me habría ahorrado…"

**Graba los seis el mismo día.** Toman 10 minutos y multiplican tu campaña por seis.

### Eje 2 — El ángulo (qué problema atacas)

El mismo producto vendido por razones distintas. Ejemplos para una calculadora de costos:
- Ángulo dinero: "no sabes cuánto ganas"
- Ángulo tiempo: "dejas de hacer cuentas a mano"
- Ángulo miedo: "estás vendiendo a pérdida sin saberlo"
- Ángulo facilidad: "no necesitas saber Excel"
- Ángulo prueba social: "lo usa gente como tú"
- Ángulo precio: "cuesta menos que un almuerzo"

Cada ángulo es una pieza. Y aquí está la mina: **el ángulo ganador te dice cómo debe hablar todo tu
negocio**, no solo el anuncio. Ese hallazgo vale más que la campaña.

### Eje 3 — El formato

El mismo contenido en otro molde:
- Demo (`156`)
- Testimonio (`154`)
- Antes/después (`155`)
- UGC hablando a cámara (`158`)
- Comercial puro sin voz, solo imagen y música (`150`)
- Carrusel de capturas de WhatsApp

### Eje 4 — La duración y el corte

De la misma pieza: 6 s, 15 s, 30 s. No son recortes automáticos: cada duración se monta aparte, pero
sale del mismo material.

---

## La matriz: cómo se planea el rodaje

Antes de grabar, llenas esta tabla. Es el documento más rentable del proceso.

| # | Ángulo | Formato | Gancho | Material que necesito |
|---|---|---|---|---|
| 1 | Dinero | Demo | Cifra | Pantalla + macro del número |
| 2 | Dinero | UGC | Afirmación incómoda | Yo a cámara frontal |
| 3 | Facilidad | Demo | Pregunta | Pantalla lenta + manos |
| 4 | Miedo | Antes/después | Visual | Libreta + pantalla, mismo encuadre |
| 5 | Prueba social | Testimonio | Frase del cliente | Entrevista cliente |
| … | | | | |

De la columna derecha sale la **lista de tomas del rodaje**. Ese es el truco: no planeas videos,
planeas material, y compruebas que un solo día de rodaje cubre las 12 filas.

---

## La regla del bloque intercambiable

Para que un rodaje produzca 12 piezas, el material tiene que estar **grabado por bloques que se puedan
recombinar**. Eso impone cuatro reglas de rodaje:

1. **Todo con la misma luz y el mismo balance de blancos.** Si el bloque 3 se grabó con otra luz, no
   se puede pegar con el bloque 7. Esta sola regla es la que salva o hunde el sistema.
2. **Cada bloque se graba entero y aislado**, con dos segundos de aire antes y después.
3. **Nada de referencias cruzadas.** Que en el bloque A nadie diga "como les decía". Cada bloque tiene
   que poder ir en cualquier posición.
4. **Sonido consistente.** Mismo micrófono, misma distancia, mismo ambiente. Un bloque con eco arruina
   todas las combinaciones donde entra.

Los bloques típicos de un rodaje de un día:

- **6 aperturas** (3 s cada una)
- **4 cuerpos** de explicación / demostración (8–15 s)
- **3 cierres** con llamado a la acción distinto
- **20–30 planos de b-roll** (producto, manos, entorno, detalle)
- **2–3 testimonios** si hay clientes disponibles
- **Sonidos aparte** de cada acción (`153`)

Con eso: 6 × 4 × 3 = 72 combinaciones teóricas. En la práctica montas 10–15 que tengan sentido.

---

## Cómo se montan 12 piezas sin morir

### El video maestro

Montas **una sola pieza completa y buena**, la mejor que puedas. Esa es tu maestra. Después las
variantes salen de intercambiar bloques dentro de ella. Montar la maestra toma 3 horas; cada variante,
15–25 minutos.

### Estructura de proyecto

Organiza la línea de tiempo por bloques nombrados, no por planos sueltos. Una carpeta por bloque:

```
campana-agosto/
  bloques/
    apertura-01-pregunta.mp4
    apertura-02-cifra.mp4
    apertura-03-visual.mp4
    cuerpo-01-demo.mp4
    cuerpo-02-testimonio.mp4
    cierre-01-link.mp4
    cierre-02-precio.mp4
  piezas/
    P01_dinero_demo_cifra_9x16_30s.mp4
    P02_dinero_ugc_incomoda_9x16_15s.mp4
```

Y luego el ensamblaje es literalmente pegar archivos. Con ffmpeg (`101-ffmpeg-cortar-y-unir.md`):

```bash
# lista.txt
file 'bloques/apertura-02-cifra.mp4'
file 'bloques/cuerpo-01-demo.mp4'
file 'bloques/cierre-01-link.mp4'
```

```bash
ffmpeg -f concat -safe 0 -i lista.txt -c copy P01_dinero_demo_cifra_9x16_30s.mp4
```

Para que `-c copy` funcione, todos los bloques deben tener **el mismo códec, resolución, fps y
parámetros de audio**. Exporta todos los bloques igual desde el editor y este paso se vuelve
instantáneo. Es la diferencia entre 15 minutos por variante y 2 minutos.

Nomenclatura obligatoria (ver `96-versiones-y-nomenclatura.md`): el nombre del archivo tiene que
llevar **ángulo, formato, gancho, relación de aspecto y duración**. Cuando la pauta te diga "la P07
está ganando", tienes que poder saber en un segundo qué era la P07 sin abrirla.

---

## Cómo se lee el resultado

Con 12 piezas al aire, hay que saber leer.

**Primero: no toques nada 48–72 horas.** El algoritmo necesita repartir. Apagar piezas antes es el
error #1 y destruye la prueba.

**Segundo: mira la métrica correcta según lo que cambiaste.**

| Eje que variaste | Métrica que lo mide |
|---|---|
| Gancho | Retención a 3 s / *hook rate* |
| Ángulo | CTR y costo por resultado |
| Formato | Retención media y *hold rate* (25% del video) |
| Duración | Costo por resultado |
| Cierre | Conversión final (compras, no clics) |

Un error frecuente: leer el gancho por conversiones. Un gancho puede traer mucha gente equivocada.
El gancho se juzga por retención a 3 s; el ángulo, por conversión.

**Tercero: apaga por debajo, no por arriba.** Cuando una pieza lleva suficiente gasto y está claramente
peor que la mediana, se apaga. No se apaga "la que no me gusta".

**Cuarto: el ganador se reproduce, no se repite.** Cuando encuentras el ganador, el siguiente rodaje
hace **cinco variantes de ese ganador**, no diez cosas nuevas. Así se escala.

Más sobre métricas: `149-leer-analiticas-de-video.md` y `145-video-para-anuncios-meta.md`.

---

## Ritmo de producción sostenible

Realista para un negocio pequeño:

| Cadencia | Qué haces |
|---|---|
| **Un rodaje al mes** (medio día) | Sale material para 12–15 piezas |
| **Semana 1** | Montas y publicas 6 piezas |
| **Semana 2** | Lees resultados; montas 4 variantes del que va mejor |
| **Semana 3** | Montas las 5 piezas restantes del banco + 2 variantes nuevas |
| **Semana 4** | Preparas la matriz del próximo rodaje con lo aprendido |

**La fatiga de creativo** llega a los 7–14 días con presupuesto medio. Por eso la campaña necesita
piezas nuevas entrando cada semana, no una tanda cada tres meses.

**El banco.** Todo lo que sobra de cada rodaje va a un banco de bloques etiquetados. A los tres meses
tienes suficiente material para montar piezas nuevas sin volver a grabar. El banco es el activo real
de este sistema.

---

## Adaptación de formatos

Cada pieza necesita salir en varias relaciones de aspecto. Reglas:

- **Monta en 9:16 primero** si la mayoría del gasto es reels/TikTok, y de ahí derivas.
- **1:1 y 4:5** se sacan reencuadrando, no recortando ciegamente. Revisa plano por plano que el sujeto
  siga en cuadro.
- **16:9** casi siempre necesita otro montaje: los textos cambian de lugar.
- **El texto se vuelve a colocar en cada formato.** Nunca escales el proyecto entero: las zonas seguras
  cambian (`45-zona-segura-por-plataforma.md`).
- **Exporta la versión sin texto** ("clean") de cada pieza. Te permite hacer versiones en otro idioma,
  con otro precio o con otra promoción sin volver a montar. Esto ahorra semanas.

---

## Errores comunes

1. **Un rodaje, un video.** Es el error económico de fondo. Planea 12 desde antes de grabar.
2. **No hacer la matriz antes de grabar.** Sin matriz sales del rodaje con material bonito que no se
   recombina.
3. **Cambiar la luz entre bloques.** Los bloques dejan de ser intercambiables y pierdes el sistema.
4. **Bloques con referencias cruzadas** ("como decía", "y lo tercero"). No se pueden reordenar.
5. **Cambiar tres ejes a la vez.** No puedes leer nada del resultado.
6. **Apagar piezas antes de 72 horas.** Destruyes la prueba y el algoritmo.
7. **Juzgar el gancho por conversiones.** El gancho se juzga por retención a 3 s.
8. **Apagar la que no te gusta.** La pauta decide, no el gusto. Casi siempre gana una que no
   esperabas.
9. **Nombres de archivo sin información.** "final_v3_bueno.mp4" hace imposible leer el reporte.
10. **Exportar los bloques con parámetros distintos.** Rompe el concat rápido y cada variante pasa de
    2 minutos a 20.
11. **No exportar la versión sin texto.** Después cambias el precio y hay que rehacer todo.
12. **Escalar el proyecto de 9:16 a 16:9 sin recolocar textos.** Todo queda fuera de zona segura.
13. **Cuando aparece un ganador, hacer diez cosas nuevas.** Se hacen cinco variantes del ganador.
14. **No guardar el banco de bloques.** Es el activo que hace barato el mes 3 y el mes 6.
15. **Publicar todas las piezas el mismo día y no volver a subir nada en un mes.** Fatiga garantizada.

---

## Checklist

Antes del rodaje:

- [ ] La **matriz está llena**: 12 filas con ángulo, formato, gancho y material necesario
- [ ] La lista de tomas sale de la matriz y cubre todas las filas
- [ ] Está definido: **6 aperturas, 4 cuerpos, 3 cierres**, b-roll y sonidos aparte

Durante el rodaje:

- [ ] Misma **luz y balance de blancos** en todos los bloques
- [ ] Mismo **micrófono, distancia y ambiente** en todos los bloques
- [ ] Cada bloque grabado **aislado**, con 2 s de aire antes y después
- [ ] Ningún bloque tiene **referencias cruzadas** a otro
- [ ] Se grabaron las **6 aperturas** aunque parezca repetitivo

En el montaje:

- [ ] Está montada **una pieza maestra** buena antes de hacer variantes
- [ ] Los bloques están exportados con **parámetros idénticos** (códec, resolución, fps, audio)
- [ ] Cada pieza tiene **un solo eje cambiado** respecto a su comparación
- [ ] Nomenclatura con **ángulo, formato, gancho, aspecto y duración** en el nombre del archivo
- [ ] Existe la versión **sin texto (clean)** de cada pieza
- [ ] Los textos fueron **recolocados** en cada relación de aspecto, no escalados

En pauta:

- [ ] Salieron **al menos 6 piezas** al aire a la vez
- [ ] **No se toca nada por 72 horas**
- [ ] Cada eje se lee con **su métrica** (gancho = retención a 3 s; ángulo = conversión)
- [ ] El **banco de bloques** quedó guardado y etiquetado
- [ ] Hay plan de **piezas nuevas cada semana** para evitar fatiga
- [ ] Cuando aparezca un ganador, el próximo lote son **variantes de ese ganador**
