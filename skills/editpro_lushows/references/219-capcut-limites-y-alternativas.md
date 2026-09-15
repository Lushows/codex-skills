# 219 — Dónde CapCut se queda corto y qué usar entonces

Este módulo es el freno de mano. Los ocho anteriores te enseñaron a exprimir CapCut. Este te enseña a
**reconocer el momento en que seguir exprimiendo es tirar el tiempo**.

Y también lo contrario, que importa más: **cuándo el impulso de "voy a cambiar de herramienta" es una
mala idea disfrazada de profesionalismo.**

Cambiar de herramienta cuesta. Cuesta aprender, cuesta rehacer, cuesta descubrir que la herramienta
nueva tiene otros problemas. La mayoría de las veces, la respuesta correcta es quedarse.

---

## Las señales de que llegaste al techo

No son opiniones. Son síntomas concretos:

| Síntoma | Qué significa |
|---|---|
| Llevás **más de 30 minutos** en un solo movimiento con keyframes | Es trabajo de After Effects |
| Necesitás **más de una máscara** en un clip y ya duplicaste dos veces | Es trabajo de After Effects |
| El cliente pide **cambios de color específicos** y no tenés cómo medirlos | Es trabajo de DaVinci |
| La línea de tiempo pasa de **20 minutos** y CapCut se arrastra | Es trabajo de Premiere/Resolve |
| Tenés que **entregar el proyecto** a otro editor | CapCut no exporta a ningún formato de intercambio |
| Necesitás **exportar con fondo transparente** | CapCut no hace alfa |
| Estás haciendo **la misma operación 50 veces** a mano | Es trabajo de ffmpeg o del puente por código |
| Hay **varias cámaras** que hay que sincronizar | CapCut no tiene multicámara |
| El audio necesita **EQ, compresión o de-esser** de verdad | Es trabajo de un editor de audio |
| Tenés que **medir el loudness** del entregable | Es trabajo de ffmpeg |
| El material es **confidencial** y CapCut lo sube a la nube | Es un problema de política, no de herramienta |

Si marcaste una, evaluá. Si marcaste tres, ya está: no es CapCut.

---

## Las alternativas, con honestidad

### DaVinci Resolve — el reemplazo total gratis

**Qué es.** Un editor de nivel cine, gratis en su versión completa (la de pago, Studio, cuesta una
sola vez y no es suscripción). Trae edición, color de nivel Hollywood, efectos (Fusion), audio
profesional (Fairlight) y entrega, todo en un solo programa.

**Cuándo es la respuesta correcta:**
- El color importa de verdad. Resolve tiene los mejores scopes y el mejor motor de color que existe.
- Proyectos largos. Aguanta documentales sin despeinarse.
- Multicámara.
- Necesitás un editor de audio serio (Fairlight tiene EQ, compresión, de-esser, medidor de LUFS).
- Querés dejar de pagar suscripciones.

**El costo real:**
- **La curva de aprendizaje es empinada.** Contá dos o tres semanas para sentirte cómodo.
- **Pide máquina.** Con menos de 16 GB de RAM y sin tarjeta gráfica decente, sufrís.
- **Es más lento para contenido de redes.** Lo que en CapCut son 15 minutos, en Resolve son 40 —
  porque tenés que hacer a mano lo que CapCut te da hecho.
- **Los subtítulos automáticos existen (en Studio) pero no le llegan a los de CapCut** en velocidad
  y comodidad.

**Veredicto:** si querés una sola herramienta para toda la vida y estás dispuesto a invertir el mes
de aprendizaje, Resolve es la respuesta. Pero **no lo uses para reels si CapCut te los resuelve.**

### After Effects — el especialista en movimiento

**Qué es.** El programa de gráficos en movimiento y composición. No es un editor de video; es un
compositor.

**Cuándo es la respuesta correcta:**
- Motion graphics de verdad: logos animados, infografías, títulos complejos.
- Composición seria: varias máscaras, rotoscopia, tracking planar, capas anidadas.
- Expresiones (lógica programada en la animación).
- Cualquier cosa que requiera **motion blur** en movimientos rápidos.
- Exportar elementos con canal alfa para usarlos en otro lado.

**El costo real:**
- **Suscripción de Adobe.** No es barato y no hay versión gratis.
- **Curva empinada.** Es el programa más difícil de este módulo.
- **Es lento.** Todo se renderiza.
- **No es para editar.** Meter un video largo en AE es un error clásico.

**El flujo correcto es híbrido:** hacés el elemento en After Effects, lo exportás con alfa (formato
con canal, tipo ProRes 4444 o PNG en secuencia), y lo **importás a CapCut** como una capa más. Así
tenés motion graphics profesionales sin abandonar la velocidad de CapCut.

Ese flujo es el que más rendimiento da, y casi nadie lo hace.

### ffmpeg — el obrero invisible

**Qué es.** Una herramienta de línea de comandos. Sin interfaz, sin previsualización. Le escribís un
comando y hace la operación.

**Cuándo es la respuesta correcta:**
- **Trabajo por lotes.** Convertir 200 archivos, recortar 50 videos a 9:16, sacarle el audio a una
  carpeta entera. Lo que en CapCut son horas, acá es un comando.
- **Normalizar loudness.** `loudnorm` a -14 LUFS. Es la mejora de audio más rentable que existe y
  CapCut no la tiene.
- **Convertir formatos y códecs** que CapCut no lee.
- **Comprimir para entrega** con control real del bitrate.
- **Medir cosas:** duración, resolución, códec, niveles de audio.
- **Cualquier operación repetible y sin criterio artístico.**

**El costo real:**
- **No hay previsualización.** Trabajás a ciegas hasta que sale el archivo.
- **La sintaxis es hostil.** Ver módulos 100–109.
- **No sirve para decisiones creativas.** Es un obrero, no un editor.

**Veredicto:** ffmpeg no compite con CapCut, lo **complementa**. Todo editor que hace volumen debería
tener tres o cuatro comandos de ffmpeg guardados. Los módulos 100–109 de esta skill son exactamente
eso.

### Premiere Pro — el estándar de la industria

**Cuándo es la respuesta correcta:** cuando trabajás con otra gente que usa Premiere y tenés que
intercambiar proyectos. Ese es prácticamente el único argumento fuerte hoy.

**El costo real:** suscripción, y en 2026 Resolve le compite bien o le gana en casi todo. Si no hay
un requisito de compatibilidad con un equipo, Resolve es mejor decisión.

### Editores de audio (Audacity, Adobe Audition, Fairlight)

**Cuándo:** cuando el audio necesita más que subir y bajar volumen. Un podcast, una entrevista larga,
una locución que hay que dejar impecable.

**Lo mínimo útil:** Audacity es gratis y resuelve EQ, compresión y limpieza básica. Para un flujo de
redes, con Audacity + ffmpeg tenés cubierto el 90 %.

---

## Cuándo NO vale la pena cambiar de herramienta

Esta es la parte que casi nadie escribe, y es la más importante.

### 1. Si el problema es tuyo, no de la herramienta

"CapCut se queda corto" muchas veces significa "todavía no aprendí a usarlo". Si no usaste keyframes
con curvas, no exprimiste las máscaras duplicando clips, y no sabías que se pueden importar fuentes
propias — no llegaste al techo de CapCut, llegaste al techo de tu conocimiento.

Antes de cambiar: **releé los módulos 211 a 217 y verificá que exprimiste lo que hay.**

### 2. Si el problema es de una sola pieza

Cambiar de herramienta tiene un costo fijo alto (aprender, configurar, rehacer). Si el problema
aparece en un video de cincuenta, no cambies el flujo entero: **resolvé esa pieza aparte** y traela
de vuelta.

Ejemplo: necesitás un logo animado complejo. No migres a After Effects tu producción entera. Hacé el
logo en AE, exportalo con alfa, e importalo a CapCut. Media hora, no dos semanas.

### 3. Si el problema es de guion, no de edición

Un video que "se siente aburrido" no se arregla con una herramienta mejor. Se arregla con mejor
contenido. Cambiar de editor para arreglar un guion flojo es la forma más cara de no resolver nada.

### 4. Si tenés fecha de entrega

**Nunca cambies de herramienta con una entrega encima.** Nunca. Terminá con lo que sabés, entregá, y
después evaluá con calma.

### 5. Si el volumen no lo justifica

Aprender Resolve cuesta 40 o 60 horas. Si hacés 4 videos al mes, tardás dos años en recuperarlas. Si
hacés 4 videos por semana, las recuperás en dos meses. **Hacé la cuenta antes.**

### 6. Si la ventaja de CapCut es la que estás usando

Si tu producción vive de subtítulos automáticos, animaciones rápidas y ritmo por velocidad, estás
usando exactamente lo que CapCut hace mejor que nadie. Cambiar a Resolve por el color te va a costar
el triple de tiempo en todo lo demás.

---

## La trampa grande: no hay salida del proyecto

Esto merece su propia sección porque es la limitación estructural más seria y la que menos se sabe.

**CapCut no exporta a XML, ni AAF, ni EDL, ni OTIO. No hay ninguna vía oficial de llevar tu montaje a
otro editor.**

Consecuencias reales:

- Si un cliente te pide "los archivos del proyecto" para que otro editor haga cambios, no tenés cómo
  dárselos de forma útil.
- Si a mitad de un proyecto grande decidís que CapCut no da, **rehacés desde cero**.
- Si CapCut cambia de política, de precio o cifra el archivo, tu biblioteca de proyectos queda
  atrapada.

**Cómo mitigarlo, sin paranoia:**

1. **Exportá siempre un archivo de video de cada corte aprobado.** Es tu única versión permanente.
2. **Guardá la transcripción / el `.srt`.** Es la estructura del contenido en texto, y sobrevive a
   cualquier herramienta.
3. **Guardá el material bruto organizado y con nombres claros** (módulo 135). Si tenés que rehacer,
   el bruto es lo que importa.
4. **Si el proyecto es grande y de cliente, considerá hacerlo en Resolve desde el día uno.** Es más
   lento al principio y te ahorra el desastre después.
5. **Copiá la carpeta del proyecto** (módulos 111 y 118). No es intercambiable con otros editores,
   pero al menos es tu respaldo dentro de CapCut.

---

## La matriz de decisión

Cuando dudes, buscá tu caso acá:

| Tu situación | La herramienta |
|---|---|
| Reel / TikTok / Short de menos de 3 min | **CapCut**, sin dudar |
| Video de YouTube de 10–20 min, hablado | CapCut aguanta; Resolve si te trabás |
| Documental, podcast en video, algo de más de 30 min | **Resolve** |
| El color es criterio de aceptación del cliente | Montaje en CapCut → color en **Resolve** |
| Logo animado, infografía, títulos complejos | **After Effects** → importar a CapCut |
| Composición con varias máscaras o rotoscopia | **After Effects** |
| Convertir / recortar / normalizar 50 archivos | **ffmpeg** |
| Normalizar el loudness antes de publicar | **ffmpeg** (`loudnorm`) |
| Podcast donde el audio tiene que estar impecable | Audio en **Audacity/Fairlight** → montaje en CapCut |
| Varias cámaras que sincronizar | **Resolve** |
| El mismo formato 50 veces con material distinto | **Puente por código** (módulos 112 y 218) |
| Material confidencial de cliente | **Resolve** (todo local, nada a la nube) |
| Tenés entrega mañana | **La que ya sabés usar** |

---

## Errores comunes

- **Cambiar de herramienta con una entrega encima.** Es la peor decisión posible. Terminá primero.
- **Confundir "no sé hacerlo" con "la herramienta no puede".** Verificá que exprimiste lo que hay
  antes de migrar.
- **Migrar todo el flujo por un problema puntual.** Resolvé esa pieza aparte y traela de vuelta.
- **Empezar un proyecto grande de cliente en CapCut** sin pensar que no hay forma de sacarlo. Si el
  proyecto puede necesitar otro editor después, no empieces acá.
- **Creer que Resolve va a hacer tus reels más rápido.** No. Va a hacerlos más lentos y con mejor
  color. Sabé qué estás comprando.
- **Meter un video de 40 minutos en After Effects.** No es un editor. Se va a arrastrar.
- **Aprender ffmpeg "por completo" antes de usarlo.** Aprendé los 4 comandos que necesitás y ya.
- **No exportar un archivo de video de cada corte aprobado.** Es tu única copia permanente del
  trabajo, porque el proyecto no es portable.
- **Pensar que una herramienta mejor arregla un guion flojo.** No lo hace, nunca lo hizo.
- **No hacer la cuenta del tiempo de aprendizaje contra tu volumen real de producción.**
- **Quedarse en CapCut por comodidad cuando ya se marcaron tres síntomas del techo.** El otro
  extremo también es un error: si llevás meses peleando con las mismas limitaciones, ya pagaste el
  costo de migrar varias veces sin migrar.

---

## Checklist

- [ ] Antes de decidir que CapCut no da, verifiqué que exprimí keyframes, máscaras duplicadas,
      fuentes propias y velocidad.
- [ ] Conté cuántos síntomas del techo marqué. Con uno, evalúo; con tres, migro.
- [ ] Si el problema es puntual, lo voy a resolver **fuera** de CapCut y traerlo de vuelta, sin
      migrar el flujo entero.
- [ ] No estoy cambiando de herramienta con una entrega encima.
- [ ] Hice la cuenta: horas de aprendizaje contra videos por mes.
- [ ] Si el proyecto es grande o de cliente y podría necesitar otro editor, no lo empecé en CapCut.
- [ ] Exporté un archivo de video de cada corte aprobado.
- [ ] Guardé la transcripción / `.srt` como estructura permanente del contenido.
- [ ] El material bruto está organizado y con nombres claros, por si toca rehacer.
- [ ] Sé exactamente qué me da la herramienta nueva y qué me quita.
- [ ] Tengo los 3 o 4 comandos de ffmpeg que necesito guardados y a mano.
- [ ] Si el material es confidencial, verifiqué qué funciones de CapCut lo suben a la nube.
