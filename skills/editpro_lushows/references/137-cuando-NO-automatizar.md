# 137 — Cuándo NO automatizar

## Qué resuelve

El límite honesto del bloque 13. Los ocho módulos anteriores enseñan a construir tubería; este enseña a
saber cuándo la tubería sobra, y a no perder semanas construyendo algo que no se va a usar.

Dos frases que resumen todo:

> **Automatizar el gusto es imposible.**
> **Automatizar lo que se hace una sola vez es desperdicio.**

La automatización sirve para lo **repetitivo, medible y aburrido**. Todo lo demás es humano, y forzarlo
produce videos correctos y muertos, o scripts que nadie vuelve a correr.

---

## Las tres preguntas antes de escribir un script

| # | Pregunta | Si la respuesta es no |
|---|---|---|
| 1 | ¿Lo voy a hacer **muchas veces**? | no lo automatices: hazlo y guarda el comando en un archivo de texto |
| 2 | ¿Tiene un **resultado correcto medible**? | no se puede automatizar; como mucho, se asiste |
| 3 | ¿Lo hice **a mano al menos tres veces**? | primero hazlo, todavía no sabes qué automatizas |

Las tres tienen que dar sí. Con una sola que dé no, la automatización pierde.

---

## El cálculo, con números

La automatización se paga sola o no. El cálculo es sencillo y conviene hacerlo antes, no después:

```
ahorro total  =  (minutos que ahorra cada vez)  ×  (veces al año)
costo total   =  (horas de construirlo × 60)  +  (minutos de mantenerlo al año)

Vale la pena si:  ahorro total  >  costo total × 2
```

El factor 2 no es capricho: la mitad de las automatizaciones que construyes no funcionan como esperabas, o
cambian las condiciones. Si el margen es justo, pierdes.

### Ejemplos reales del caso maestro

| Tarea | Ahorro/vez | Veces al año | Ahorro anual | Costo de construir | ¿Vale? |
|---|---|---|---|---|---|
| `validar-cortes` | 40 min (evita 5 renders) | 30 | 1200 min | 4 h = 240 min | **sí, 5×** |
| `subtitulos` palabra a palabra | 110 min | 30 | 3300 min | 6 h = 360 min | **sí, 9×** |
| `limpiar-voz` (9 módulos) | 28 min | 30 | 840 min | 3 h = 180 min | **sí, 4,6×** |
| `analizar` | 24 min | 30 | 720 min | 2 h = 120 min | **sí, 6×** |
| Generar la portada del video | 4 min | 30 | 120 min | 3 h = 180 min | **no** |
| Escribir la descripción del post | 5 min | 30 | 150 min | 5 h = 300 min | **no** |
| Elegir la toma buena | — | — | no medible | — | **imposible** |

Las dos últimas del "no" son interesantes: son tareas repetitivas y aburridas, pero **el ahorro por vez es
tan chico que nunca alcanza**. Automatizar lo aburrido no basta; tiene que ser aburrido **y** costoso.

---

## Lo que no se puede automatizar: el gusto

Hay decisiones que no tienen respuesta correcta, tienen respuesta **buena**. Y "buena" no se mide.

| Decisión | Por qué no se automatiza | Lo máximo que puede hacer la máquina |
|---|---|---|
| **Cuál toma es la buena** | tres tomas correctas y una tiene vida | descartar las técnicamente malas y ordenarlas |
| **Si el gancho engancha** | depende de a quién, cuándo, en qué feed | medir la retención real después de publicar |
| **Qué música va** | "suena a nosotros" no es una métrica | filtrar por BPM, duración, licencia |
| **Si el chiste da risa** | ni leyendo la transcripción se sabe | nada |
| **Dónde respira el video** | el ritmo se siente | contar cambios por segundo y avisar de rachas |
| **Si el color se siente de la marca** | la paleta se mide, el sentimiento no | verificar que los colores estén dentro de la paleta |
| **Si la historia se entiende** | requiere ser humano y no saber el final | comprobar que no falten palabras |
| **Cuándo un blooper es el remate** | es una lectura de intención | marcarlo como excepción y preguntar |

**La trampa clásica:** intentar automatizar "elegir la mejor toma" pidiéndole a un modelo que puntúe las
tomas. Funciona lo justo para ser peligroso: te da un ranking con pinta de objetivo, y tú dejas de mirar.
El resultado es un video hecho de tomas correctas y sin ninguna que valga la pena.

La forma correcta es **asistir, no decidir**:

```
La maquina hace:  descarta las tomas con audio saturado, fuera de foco o cortadas.
                  Ordena las que quedan por claridad de dicción y estabilidad.
                  Te muestra 4 en vez de 26.
El humano hace:   elige entre esas 4 en veinte segundos.
```

Eso sí ahorra tiempo, y no te roba la decisión.

---

## Lo que no se debe automatizar: lo que se hace una vez

Un documental de una pieza. El video institucional del año. La pieza única para un evento. En esos casos:

- No hay repetición que amortice la construcción.
- El material es irrepetible, así que las excepciones son casi todas las filas.
- Los criterios cambian a mitad del proyecto porque estás descubriendo el video mientras lo haces.

Ahí se edita a mano, con las herramientas que sean más rápidas, y se guarda **el registro** de los
comandos usados en un `COMANDOS.md`, no un pipeline.

La forma barata de que quede algo:

```markdown
# COMANDOS -- video institucional 2026

## Limpieza de voz de la entrevista principal
ffmpeg -i entrada/entrevista.mp4 -af "highpass=f=80,afftdn=nr=12,equalizer=f=3000:t=q:w=1:g=3,acompressor=threshold=-18dB:ratio=3" trabajo/voz.wav
-- nr=12 y no 20: con 20 la voz sonaba a telefono

## Exportar el master
ffmpeg -i trabajo/mezcla.mp4 -c:v libx264 -crf 18 -preset slow salida/master.mp4
```

Eso cuesta cinco minutos y sirve casi tanto como un pipeline, para un proyecto único.

---

## La zona intermedia: semi-automatizar

Casi todo lo interesante vive aquí. El patrón que funciona es siempre el mismo:

> **La máquina reduce las opciones. El humano decide entre pocas.**

| Fase | Máquina | Humano |
|---|---|---|
| Selección de tomas | descarta 22 de 26, ordena las 4 | elige 1 |
| Cortes | propone entrada y salida al décimo | aprueba o mueve 3 de 30 |
| Subtítulos | genera todos con timing | corrige 5 palabras mal transcritas |
| Ilustración con IA | genera 4 variantes con la paleta forzada | elige 1, o pide otra ronda |
| Música | trae 3 pistas del largo correcto | escucha y elige |
| Verificación | mide 12 defectos técnicos | mira el video una vez, entero |

La pregunta que define el punto de corte: **¿dónde deja de haber respuesta correcta?** Justo antes de ahí
termina la máquina.

---

## Las cinco señales de que estás automatizando de más

1. **El script tiene más excepciones que casos.** Si la mitad de las filas necesitan `intencional=si`, la
   regla no describe tu trabajo.
2. **Pasas más tiempo arreglando el script que haciendo el video.** El pipeline es un medio; si se come
   la semana, dejó de serlo.
3. **Automatizaste algo que todavía no sabes hacer bien a mano.** Sale un script que consagra tus errores
   y los repite a escala.
4. **Estás automatizando para no decidir.** "Que el script elija el gancho" no es eficiencia, es evasión.
   La decisión sigue siendo tuya, solo que ahora la toma un `sort()`.
5. **Nadie ha corrido el script desde que lo escribiste.** Señal definitiva. Bórralo.

---

## El costo oculto: el mantenimiento

Nadie lo suma y es la mitad de la factura. Un script vivo cuesta, todos los años:

| Costo | Cuánto, aproximado |
|---|---|
| Actualizar cuando cambia ffmpeg o Node | 1–2 h al año |
| Arreglar cuando el modelo de IA cambia de formato de respuesta | 2–4 h al año |
| Explicárselo a alguien más | 1 h por persona |
| Encontrar el fallo raro que sale una vez cada 20 corridas | 3 h, y llega siempre |

Un pipeline de doce pasos cuesta fácil **15 horas al año** solo en mantenerse vivo (módulo `139`). Si el
ahorro anual no supera eso con margen, no lo construyas.

---

## La regla de las tres veces, en detalle

| Vez | Qué pasa de verdad |
|---|---|
| **1ª** | descubres el problema. No sabes qué es esencial y qué es casualidad |
| **2ª** | ves lo que se repite. Todavía crees que tu proceso es más limpio de lo que es |
| **3ª** | aparecen las excepciones: el clip sin audio, el que viene a 24 fps, el vertical entre horizontales |
| **4ª** | ya puedes escribir un script que sobrevive al mundo real |

Automatizar en la primera produce un script que solo funciona con el material de ese día. Es el motivo
número uno por el que los pipelines se abandonan.

---

## Tabla de decisión rápida

| Situación | Qué hacer |
|---|---|
| Tarea mecánica, 20+ veces al año, resultado verificable | **automatiza** |
| Tarea mecánica, 3 veces al año | guarda el comando en `COMANDOS.md` |
| Tarea que evita rehacer trabajo caro (compuertas) | **automatiza aunque sea poco frecuente** |
| Tarea de gusto | asiste: reduce opciones, no decidas |
| Proyecto único e irrepetible | a mano, con registro de comandos |
| Todavía no la has hecho tres veces | hazla |
| No sabes cómo se ve el resultado correcto | no automatices: primero define "correcto" |
| El cliente cambia el criterio en cada video | no automatices el criterio; automatiza el render |

Nota la tercera fila: **las compuertas se automatizan aunque no ahorren tiempo**, porque su valor no es
velocidad, es evitar publicar defectos. `validar-cortes` corre 10 veces por proyecto y su valor es que el
video no salga roto.

---

## Un caso concreto: los subtítulos

Vale la pena mirar dónde cae exactamente la frontera dentro de una sola tarea:

| Sub-tarea | ¿Automatizar? | Por qué |
|---|---|---|
| Sacar los tiempos de cada palabra | **sí** | medible, tedioso, 2 h a mano |
| Generar el `.ass` con la animación de golpe | **sí** | pura mecánica, 100% repetible |
| Elegir **qué** palabra se resalta | **no** | es énfasis, es interpretación |
| Corregir las palabras mal transcritas | **no** | requiere saber qué se dijo de verdad |
| Poner el texto en zona segura | **sí** | es geometría, está medida (módulo `45`) |
| Decidir si una frase entera va o no va | **no** | es guion |

Cuatro sí y tres no dentro de la misma tarea. Por eso "automatizar los subtítulos" no es una decisión: son
siete decisiones.

---

## Errores comunes

- **Automatizar la selección de tomas.** Sale un ranking con pinta de objetivo y dejas de mirar el
  material. Es el error más caro del bloque.
- **Construir el pipeline antes de haber editado tres videos a mano.** Automatizas lo que crees que haces.
- **No sumar el mantenimiento al costo.** Son 15 horas al año en un pipeline de doce pasos.
- **Automatizar lo aburrido aunque ahorre 4 minutos.** Aburrido no basta: tiene que ser aburrido y caro.
- **Automatizar para no decidir.** La decisión sigue siendo tuya, solo que ahora la toma un `sort()` que
  no entiende de qué va el video.
- **Insistir con un script que tiene más excepciones que casos.** La regla no describe tu trabajo; bórrala.
- **Construir pipeline para un proyecto único.** Ahí basta un `COMANDOS.md`.
- **Automatizar antes de saber qué es "correcto".** Sin criterio no hay compuerta, y sin compuerta el
  script solo produce defectos más rápido.
- **No borrar los scripts que nadie corre.** Ocupan atención, se rompen en silencio y engañan al siguiente.
- **Creer que un video montado por pipeline ya está bien.** Está *sin defectos*. Bueno es otra cosa, y esa
  la decides tú viéndolo.

---

## Checklist

- [ ] Hice la tarea a mano al menos tres veces antes de automatizarla
- [ ] Calculé ahorro anual contra costo de construir, y el margen es de al menos 2×
- [ ] Sumé el mantenimiento anual al costo, no solo la construcción
- [ ] La tarea tiene un resultado correcto que se puede verificar
- [ ] Ninguna decisión de gusto quedó dentro de un script
- [ ] Donde hay gusto, la máquina reduce opciones y el humano elige
- [ ] Las compuertas están automatizadas aunque no ahorren tiempo
- [ ] Para proyectos únicos escribí `COMANDOS.md` en vez de un pipeline
- [ ] Ningún script tiene más excepciones que casos normales
- [ ] No estoy automatizando algo para evitar tomar una decisión
- [ ] Borré los scripts que nadie ha corrido desde que se escribieron
- [ ] Tengo claro, por escrito, qué partes del proceso son humanas y por qué
- [ ] Después del pipeline, alguien ve el video completo y decide si es bueno
