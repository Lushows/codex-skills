# 116 — El flujo híbrido: qué hace la máquina y qué hace el humano

Este es el módulo que da sentido a todos los demás. Los anteriores explican *cómo* se escribe un
proyecto de CapCut desde afuera. Este explica *por qué vale la pena*, y cómo repartir el trabajo para
que el resultado sea mejor que el de cualquiera de los dos por separado.

Si vas a leer un solo módulo de este bloque, es este.

---

## El problema de fondo

Un modelo de IA **no ve el video corriendo y no oye el audio como lo oye una persona.**

Puede leer una transcripción. Puede analizar fotogramas sueltos. Puede medir niveles de audio. Puede
razonar sobre estructura, ritmo, gancho y guion con bastante criterio.

Pero no puede sentarse a mirar los ocho segundos y decir "acá me aburrí". Eso lo hace un humano en
tiempo real, casi sin pensar, y lo hace bien.

Y del otro lado: un humano **no puede** ver veinticinco tomas de la misma frase y recordar con
precisión en cuál el sujeto no parpadeó y dijo bien la palabra. No puede medir un corte al décimo de
segundo cincuenta veces sin cansarse. No puede escribir doscientos subtítulos sin errores.

### El ciclo viejo (y por qué es tan lento)

```
IA propone un montaje "a ciegas"
   ↓
Renderiza un MP4                          ← 3 a 15 minutos
   ↓
El humano lo mira
   ↓
"El segundo corte está tarde, el texto tapa la cara,
 la música está muy alta, y esa toma no me gusta"
   ↓
La IA interpreta esas notas en palabras
   ↓
Renderiza de nuevo                        ← otros 3 a 15 minutos
   ↓
"Ahora el tercero está mal"
   ↓ ... y así cinco veces
```

Cada vuelta cuesta entre diez y treinta minutos, la mayoría esperando un render que se va a tirar a la
basura. Y las notas se transmiten en el canal más pobre posible: **palabras sobre algo visual**.

Un video de 40 segundos puede costar toda una tarde así.

### El ciclo nuevo

```
IA escribe el proyecto directamente en la línea de tiempo   ← segundos
   ↓
El humano abre CapCut y VE el montaje completo
   ↓
Arrastra tres cosas con el mouse                            ← 90 segundos
   ↓
Listo
```

**El render desaparece del ciclo de iteración.** Solo se renderiza una vez, al final, cuando ya está
aprobado.

Y las notas dejan de ser palabras: el humano **corrige directamente** lo que no le gusta, en la
herramienta donde ve el resultado al instante.

Eso no es una optimización menor. Es un cambio de naturaleza del trabajo.

---

## La división correcta del trabajo

No es "la IA hace todo y el humano supervisa". Es más limpio y más honesto que eso: **cada uno hace lo
que solo él puede hacer bien.**

### Lo que la máquina hace mejor (y el humano odia)

| Tarea | Por qué la máquina gana |
|---|---|
| **Encontrar la toma buena entre veinticinco falsas** | Transcribe todo, compara texto contra guion, detecta silencios, ruidos, cortes de frase. No se cansa en la toma 14. |
| **Medir cortes al décimo de segundo** | Aritmética exacta, cincuenta veces, sin deriva. |
| **Alinear cortes al pulso de la música** | Lee los beats y hace la cuenta. |
| **Escribir doscientos subtítulos** | Transcribe, agrupa en frases, calcula tiempos, aplica estilo. |
| **Limpiar la voz** | `highpass` + `afftdn` + `loudnorm`, idéntico y correcto cada vez. |
| **Generar arte de marca** | Placas, fondos, cartelas con la tipografía y los colores exactos. |
| **Detectar problemas técnicos** | Clip sobreexpuesto, audio saturado, formato equivocado, plano desenfocado. |
| **Recordar la regla** | Zona segura, duración por plataforma, límite de LUFS, márgenes. |
| **Escribir la línea de tiempo** | Cincuenta segmentos con sus materiales y compañeros, en segundos. |
| **Hacerlo otra vez para el segundo idioma / el segundo formato** | Costo marginal casi cero. |

Todo eso es **preciso y aburrido**. Es exactamente el trabajo que un editor humano hace a regañadientes
y donde comete errores por cansancio.

### Lo que el humano hace mejor (y la máquina no puede)

| Tarea | Por qué el humano gana |
|---|---|
| **Decir "esta toma tiene algo"** | Carisma, energía, verdad. No hay métrica para eso. |
| **Sentir que el video se cayó en el segundo 12** | Es una sensación en tiempo real. |
| **Juzgar si el gancho enganchó** | Ídem. Se sabe viéndolo, no analizándolo. |
| **Decidir por gusto** | Cuál de dos cortes buenos es *el* corte. |
| **Saber qué es apropiado para esta marca, hoy** | Contexto que no está en ningún archivo. |
| **Oír que la música pelea con la voz** | Percepción auditiva real. |
| **Notar que el chiste no da risa** | No hay forma de medirlo. |
| **Asumir la responsabilidad de publicar** | Alguien tiene que poner la cara. |

Todo eso es **rápido y subjetivo**. Un humano lo hace en el tiempo que dura el video, y lo hace bien.

### La frase que resume todo

> **La máquina hace lo preciso y aburrido. El humano hace lo que solo se puede hacer mirando y oyendo.
> El puente es lo que permite que se pasen el trabajo sin fricción.**

Un editor humano bueno ya trabajaba así consigo mismo: primero la parte mecánica (organizar, sincronizar,
transcribir), después la parte creativa. Lo que hace el puente es dejar que la parte mecánica la haga
otro, y que el editor llegue directo a lo que le gusta.

---

## El protocolo de entrega

Entregar "el proyecto está en CapCut, abrilo" no alcanza. Un entregable serio tiene tres partes.

### 1. El proyecto abierto y funcionando

- Abre sin errores.
- Todos los materiales enlazados (nada en gris).
- Las pistas nombradas o al menos ordenadas de forma legible.
- El audio ya normalizado y balanceado.
- Los textos ya con la tipografía y el color de la marca.

**No entregues un proyecto que "casi" abre.** Verificalo vos abriéndolo antes.

### 2. La hoja de decisiones

Un archivo de texto corto que responde: *¿qué decidí y por qué?* Es lo que convierte el entregable en
una conversación en vez de una caja negra.

```markdown
# Reel GastroLatam — corte 1
Duración: 38,4 s · 1080×1920 · 30 fps

## Qué armé
Estructura: gancho (0-3s) → problema (3-14s) → solución (14-30s) → CTA (30-38s)

## Decisiones
- Gancho: usé la toma 07, no la 03. La 03 tiene mejor luz pero él duda medio
  segundo antes de la primera palabra y eso mata el arranque.
- Corté 4 muletillas ("o sea", "digamos") entre 8s y 19s. Se nota el ritmo más
  seco; si suena artificial, en la pista 1 están los cortes marcados.
- La música entra en 2,8s, no en 0. El silencio inicial da peso al gancho.
- Subtítulos agrupados de a 4 palabras. Palabra por palabra generaba 190
  segmentos y CapCut se arrastraba.

## Lo que NO hice y quiero que decidas vos
- El plano de la cocina (22s-26s) está movido. Lo dejé porque tiene energía,
  pero si te molesta hay una alternativa quieta en broll_04.mp4 en 00:14.
- No metí la placa de precio. No sé si esta campaña la lleva.

## Sé que está flojo
- La transición de 30s a 31s es un corte duro y se siente. No encontré nada
  mejor con el material que hay.

## Descartes (por si querés revisarlos)
- tomas_descartadas.md tiene las 25 tomas con timecode y por qué cada una quedó
  afuera.
```

Fijate en las tres secciones que casi nadie escribe y que son las que más valen: **lo que dejé para
que decidas vos**, **lo que sé que está flojo**, y **los descartes con su razón**.

Eso es honestidad de oficio. El módulo 08 (presentar y defender un corte) desarrolla esto largo.

### 3. Los descartes accesibles

Nada frustra más a un revisor que "no me gusta esta toma" y que la respuesta sea "hay que volver a
buscar entre todo el bruto". Tené la lista lista:

```
tomas_descartadas.md
| # | archivo | in | out | dice | por qué se descartó |
|---|---------|-----|-----|------|---------------------|
| 03 | A001.mp4 | 00:12,4 | 00:15,1 | "3 errores..." | duda antes de arrancar |
| 07 | A001.mp4 | 01:22,0 | 01:24,8 | "3 errores..." | ✅ ELEGIDA |
| 11 | A001.mp4 | 02:05,3 | 02:08,0 | "3 errores..." | se come la palabra "plata" |
```

Con eso, cambiar de toma es un cambio de dos números en el JSON, no una expedición.

---

## Cómo se reciben las notas

Este es el otro lado del puente, y donde se gana o se pierde la velocidad.

### El vocabulario de notas

Pedí las notas en este formato. Una línea por nota:

```
[timecode]  [qué]  [qué querés en su lugar]
```

Ejemplos buenos:

```
00:03,2  el corte llega tarde, entra medio segundo antes
00:07,5  el texto tapa la cara, subilo
00:12,0  esta toma no me gusta, probá otra
00:14,8  la música pisa la voz acá
00:22,0  este pedazo sobra entero, sacalo
final    la salida de música es muy abrupta
```

Ejemplos inútiles (y qué preguntar):

| Nota | Qué preguntar |
|---|---|
| "no me convence" | ¿En qué segundo dejaste de estar enganchado? |
| "está lento" | ¿Lento desde el principio o se cae en algún punto? |
| "falta algo" | ¿Falta información, falta energía, o falta cierre? |
| "hacelo más dinámico" | ¿Más cortes, más movimiento, o música más rápida? |

**El timecode es lo que convierte una opinión en una instrucción ejecutable.** Sin timecode, la nota
requiere una ronda de interpretación, y ahí vuelve la lentitud.

### Las tres clases de nota

| Clase | Ejemplo | Quién la ejecuta |
|---|---|---|
| **Mecánica** | "el corte llega tarde", "el texto tapa la cara" | La máquina, en segundos |
| **De criterio** | "esa toma no me gusta, probá otra" | La máquina propone, el humano elige |
| **Estructural** | "esto no arranca, hay que replantear el gancho" | Se vuelve al brief (módulo 02) |

Si te llegan tres notas estructurales, **no las parchees**. Significa que el brief estaba mal o que se
entendió mal. Volvé a hablar antes de tocar la línea de tiempo.

### La regla de la corrección directa

Muchas notas el humano las puede aplicar más rápido él mismo, arrastrando en CapCut, que
explicándotelas. **Dejalo.** No hay que canalizar todo por el puente.

Lo que sí conviene es que, después, el proyecto corregido vuelva y se lea:

```bash
# comparar el corte que entregué contra el que quedó después de la revisión
jq -S . entregado/draft_content.json > a.json
jq -S . revisado/draft_content.json  > b.json
diff a.json b.json
```

Eso te dice **exactamente qué cambió el humano**: qué cortes movió, cuánto, en qué dirección. Es la
mejor retroalimentación que existe, porque no es una opinión: es una corrección medida.

Si ves que siempre acorta el primer corte, tu criterio de gancho es lento. Si siempre baja la música,
tu nivel por defecto está alto. **Ajustá los valores por defecto y la próxima vez hay menos notas.**
Ese es el bucle de aprendizaje real de este flujo.

---

## Ejemplo completo, punta a punta

Un reel de 40 segundos para GastroLatam, a partir de 25 minutos de bruto.

**Fase 1 — máquina (8 minutos de reloj, cero atención humana)**

1. `ffprobe` sobre todos los archivos: formatos, duraciones, problemas técnicos.
2. Whisper transcribe todo con timecodes por palabra.
3. Se identifican las 25 tomas de la misma frase; se compara cada una contra el guion.
4. Se descartan las que tienen tropiezos, silencios largos o ruido.
5. Se eligen las 6 mejores y se arma una estructura gancho→problema→solución→CTA.
6. Se limpia el audio: `highpass` + `afftdn` + `loudnorm` a −16 LUFS.
7. Se calculan los cortes al fotograma y se alinean con los beats de la música.
8. Se generan los subtítulos agrupados de a 4 palabras con la tipografía de la marca.
9. Se escribe el `draft_content.json` desde la plantilla.
10. Se valida (`lint`), se copia a la carpeta de CapCut.
11. Se escribe la hoja de decisiones y la lista de descartes.

**Fase 2 — humano (4 minutos de atención plena)**

12. Abre CapCut. Ve el reel armado.
13. Lo mira una vez de corrido. Siente que el segundo 12 se cae.
14. Arrastra el corte del 12 medio segundo antes. Lo mira de nuevo. Mejor.
15. La toma del 22 no le gusta. Mira la lista de descartes, elige la alternativa, la cambia.
16. Baja la música dos rayitas.
17. Aprueba.

**Fase 3 — máquina (1 minuto)**

18. Exporta.

**Total: 13 minutos, de los cuales 4 son de atención humana.** El mismo trabajo a mano son dos horas,
la mayoría buscando entre tomas.

Y lo importante: **las decisiones creativas las tomó el humano**, todas. La máquina no eligió el ritmo
final ni la toma final. Solo hizo que llegar a esa decisión costara cuatro minutos en vez de dos horas.

---

## Los límites honestos de este flujo

**No sirve si el bruto es malo.** Ninguna cantidad de precisión arregla material sin energía, sin luz
o sin guion. El puente acelera el montaje, no salva la grabación.

**No sirve si nadie sabe qué quiere.** El brief sigue siendo el brief (módulo 02). Un montaje
automático de un objetivo confuso es un montaje confuso, más rápido.

**No reemplaza el criterio.** La IA puede elegir 6 tomas defendibles; cuál de las 6 es *la* toma sigue
siendo del humano. Si el humano no mira, el resultado va a ser correcto y olvidable.

**No es para producción crítica sin red.** El formato no es oficial y puede romperse con una
actualización. El módulo 119 trata esto en serio.

**El humano tiene que mirar de verdad.** El riesgo real de este flujo no es técnico: es que el humano
apruebe sin mirar porque "la máquina ya lo hizo". Ahí se pierde todo lo bueno del arreglo. **La única
tarea innegociable del humano es mirar el video completo, una vez, con atención.**

---

## Errores comunes

**Pedirle a la IA que "decida si quedó bueno".** No puede. Puede verificar que cumple el brief, la
duración, la zona segura y los niveles. El gusto es del humano.

**Renderizar para iterar.** Si estás exportando MP4 para ver si el corte quedó bien, estás en el ciclo
viejo. El punto del puente es que se mira en la línea de tiempo.

**Entregar el proyecto sin la hoja de decisiones.** El revisor no sabe qué mirar ni qué se descartó, y
las notas vuelven vagas.

**Ocultar lo que quedó flojo.** Se nota igual, y quema la confianza. Decilo vos primero.

**No tener los descartes a mano.** "Esa toma no me gusta" se vuelve media hora en vez de dos minutos.

**Aceptar notas sin timecode.** Cada nota vaga cuesta una ronda de interpretación. Pedí el segundo.

**Parchear notas estructurales.** Tres notas de estructura = el brief estaba mal. Volvé a hablar.

**Canalizar todo por el puente.** Si el humano lo arregla más rápido arrastrando, que lo arrastre.

**No leer el proyecto corregido.** Ahí está la mejor retroalimentación que vas a recibir en tu vida y
es gratis: un `diff` te dice exactamente cómo se equivocó tu criterio.

**Aprobar sin mirar.** El único error que arruina el flujo entero.

---

## Checklist

**Antes de armar**
- [ ] Hay un brief claro: para quién, para qué plataforma, qué tiene que lograr, cuánto dura
- [ ] El bruto está analizado: transcrito, con tomas identificadas y problemas técnicos detectados
- [ ] Está definido qué es trabajo de máquina y qué queda explícitamente para el humano

**Al armar**
- [ ] La máquina hizo lo preciso y aburrido: selección, medición, limpieza, subtítulos, escritura
- [ ] No tomé decisiones de gusto disfrazadas de decisiones técnicas
- [ ] El proyecto abre en CapCut sin errores y sin materiales en gris

**Al entregar**
- [ ] Hoja de decisiones escrita, con la sección "lo que dejo para que decidas vos"
- [ ] Está dicho, sin adornos, lo que sé que quedó flojo
- [ ] La lista de descartes está lista y con timecodes
- [ ] Verifiqué yo mismo que el proyecto abre antes de mandarlo

**Al recibir notas**
- [ ] Cada nota tiene timecode; las que no lo tienen, las pregunté
- [ ] Clasifiqué cada nota: mecánica, de criterio, o estructural
- [ ] Si hay varias estructurales, volví al brief en vez de parchear

**Al cerrar**
- [ ] El humano miró el video completo, de corrido, con atención, al menos una vez
- [ ] Comparé el proyecto entregado contra el revisado y saqué la lección
- [ ] Ajusté mis valores por defecto según lo que el humano corrigió
- [ ] Solo entonces se renderizó, una sola vez
