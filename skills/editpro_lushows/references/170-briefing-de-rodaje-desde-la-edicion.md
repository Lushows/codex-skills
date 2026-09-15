# 170 — Briefing de rodaje desde la edición

**Qué resuelve:** que el día de grabación produzca material que **se pueda montar**. Este módulo no lo
escribe un director de fotografía: lo escribe el editor que va a sufrir después. Es la lista de lo que
hay que pedir **antes** de que alguien saque el celular, ordenada por cuánto duele cada cosa si falta.

> **De dónde sale esto.** De un rodaje real en un bar-restaurante, agosto de 2026. 16 clips, 10 minutos
> de material, un presentador que no es actor. Al montar quedaron **6 tomas usables**. Unas 28 tomas
> falsas. Y tres problemas que no se pudieron arreglar en post porque **no se arreglan en post**.
> Este bloque completo existe para que eso no se repita.

---

## 1. La regla madre

> **Todo lo que se puede arreglar en edición, cuesta tiempo. Todo lo que NO se puede arreglar en
> edición, cuesta el video.**

Hay una frontera muy clara y casi nadie la conoce. Apréndetela antes que cualquier otra cosa:

| Problema en el rodaje | ¿Se arregla en edición? | Costo real |
|---|---|---|
| Toma falsa, se trabó | ✅ Sí | Se corta. Barato. |
| Encuadre un poco flojo | ✅ Sí | Punch-in (`22`). Barato. |
| Color raro | ✅ Sí | Corrección (`61`). Medio. |
| Ruido de fondo constante | 🟡 A medias | Limpieza (`71`). Caro y se nota. |
| Poca luz / imagen con grano | 🟡 A medias | Se ve peor. Caro. |
| **Audio saturado (pegado a 0 dB)** | ❌ **No** | **Se pierde la toma.** |
| **Foco perdido** | ❌ **No** | **Se pierde la toma.** |
| **No hay b-roll** | ❌ **No** | **El video queda plano. Punto.** |
| **Música del local sonando encima** | ❌ **No** | **Se pierde el video entero.** |
| Saltos de luz entre la misma frase | ❌ Casi no | Se pierde el montaje limpio. |

Las cinco filas rojas son las que hay que blindar en el briefing. Las demás las arregla el editor sin
quejarse.

---

## 2. Los cinco no-negociables

Si el briefing solo alcanza para cinco frases, que sean estas.

### 1) La música del local se apaga

No se baja: **se apaga**. En el rodaje real la música del bar quedó metida en todos los clips y el
resultado fue que el audio **nunca bajó de -34 dB**. Ese dato parece técnico y no lo es: significa que
**no se pudo usar detección automática de silencios** para encontrar dónde empieza y termina cada toma.
Todo el material hubo que revisarlo a oído, clip por clip. Horas.

Con la música apagada, un comando encuentra los cortes solo:

```bash
ffmpeg -hide_banner -i clip.mp4 -af "silencedetect=noise=-40dB:d=0.6" -f null - 2>&1 | grep silence_
```

Con música sonando, ese comando **no devuelve nada** y el trabajo se vuelve manual.

Y hay un problema peor: la música del local es de alguien. Si te queda pegada, YouTube e Instagram la
detectan (`78`) y te pueden tumbar o desmonetizar el video. No hay forma de sacarla del audio de la voz.

**Cómo se pide:** "Apaga el equipo de sonido. Se prende otra vez cuando terminemos." Sin negociación.

### 2) El audio se monitorea, no se supone

Audio pegado a 0 dB = distorsión permanente. En el rodaje real todo el material llegó saturado. Eso no
se quita con ningún filtro: la información ya no está en el archivo. Detalle completo en `172`.

**Cómo se pide:** "Grabamos 10 segundos de prueba, los revisamos, y ahí sí arrancamos."

### 3) Cada frase se graba en UN solo sitio

En el rodaje real la misma frase se grabó en el pasillo con neón morado, en la barra y en la terraza a
plena luz del día. Al montar, cada corte era un salto de luz brutal: morado → ámbar → azul de mediodía.
Ver `175`.

**Cómo se pide:** "Terminamos TODO lo del pasillo. Después nos movemos a la barra. No volvemos."

### 4) Hay lista de b-roll y alguien responsable de ella

En el rodaje real hubo **un solo clip de producto para todo el video**. Un video de 60 segundos necesita
entre 8 y 15 planos de recurso (`174`). Con uno solo, el editor no tiene con qué tapar los cortes y el
video queda siendo una cara hablando.

**Cómo se pide:** con la lista impresa y una persona encargada de tacharla.

### 5) Se graba un ambiente puro de 5 segundos por locación

Cinco segundos de silencio absoluto, sin nadie hablando, en cada sitio donde se grabó. Es lo más barato
que existe y le salva la vida al editor (`172`, sección de ambiente). Nadie lo hace. Cuesta 15 segundos
en todo el día.

---

## 3. Qué le pide el editor a producción, en orden

Esta es la plantilla del briefing. Se manda **por escrito** el día antes.

### A. Del guion

- Guion cerrado y aprobado **antes** del rodaje. No se reescribe en el sitio.
- Frases divididas en **bloques de 8–12 palabras** (`177`). Las frases largas son la causa #1 de las
  tomas falsas.
- Marcado qué frase es el **gancho** (`30`) — esa se graba 6 veces, no 2.
- Marcado qué frase es el **remate/CTA** (`33`) — esa también.

### B. Del rodaje

- **Orden por locación**, no por orden del guion (`175`).
- **3 tomas buenas mínimo** por frase. No "una que quedó bien": tres. Cuestan 40 segundos y le dan al
  editor de dónde escoger (`14`).
- Después de cada toma buena: **2 segundos de quietud** antes de cortar la grabación. Ese colchón es lo
  que permite hacer un corte limpio.
- **Claqueta de pobre:** antes de cada toma, alguien dice en voz alta "bloque 3, toma 2". Queda en el
  audio y el editor lo encuentra en la transcripción (`13`) en segundos.

### C. Del material

- Nada de grabar en 4K si el celular se calienta y corta a los 3 minutos. 1080p a 30 fps estable es
  mejor que 4K entrecortado (`171`).
- **Espacio libre revisado** antes de empezar. Un rodaje que se cae a la mitad por memoria llena es un
  rodaje perdido.
- **Modo avión** puesto. Una llamada entrante corta la grabación y la toma buena se va.

### D. De la entrega al editor

- Los clips **sin editar, sin filtros, sin recortar**. Nada de mandar por WhatsApp: WhatsApp recomprime
  y baja la calidad (`92`). Se pasan por cable, Drive o AirDrop.
- Nombres que digan algo: `bloque3_terraza_toma2.mp4`, no `IMG_4471.MOV`.
- Un mensaje de voz de 1 minuto del director contando qué pasó: qué tomas cree que son buenas, qué se
  dañó, qué falta. Vale más que un documento.

---

## 4. La conversación de 10 minutos que ahorra 6 horas

Antes del rodaje, el editor se sienta con quien va a grabar y responde estas preguntas. En voz alta.

| Pregunta | Por qué la hace el editor |
|---|---|
| ¿Dónde se va a publicar? | Define el formato: vertical, cuánto dura, dónde va el texto (`176`) |
| ¿Cuánto dura el video final? | 30 s de video ≈ 12–20 planos. Con 6 clips no sale. |
| ¿Quién habla y cuánto habla? | Si es alguien que se traba, se cambia el método (`178`) |
| ¿En cuántos sitios se graba? | Cada sitio nuevo = un bloque de color distinto que hay que emparejar |
| ¿Hay producto? | Si sí, hay secuencia de producto obligatoria (`174`) |
| ¿Se puede volver a grabar si algo falla? | Si la respuesta es NO, se graba el doble de cobertura |
| ¿Hay logo, tipografía, colores de marca? | Si no, el video se monta y después no coincide con nada |

Esa última pregunta se la pasas a `directorcreativo_lushows`. Montar sobre una marca que no existe es
trabajo que se bota.

---

## 5. El presupuesto de tomas (cuentas reales)

Este es el cálculo que nadie hace y que explica por qué los rodajes se quedan cortos.

**Del rodaje real:**

- 16 clips, 10 minutos de material
- 6 tomas usables
- ~28 tomas falsas
- Tasa de aprovechamiento: **~19%**

Con alguien que no es presentador, un 20–30% de aprovechamiento es **normal**, no es un fracaso. El
error no fue trabarse: el error fue **planear como si el aprovechamiento fuera del 90%**.

**La fórmula del editor:**

```
tomas a grabar por frase = 3 ÷ tasa esperada

Presentador profesional      → tasa 0,7 → grabar 4 tomas por frase
Alguien con práctica         → tasa 0,4 → grabar 7 tomas por frase
Alguien que nunca ha grabado → tasa 0,2 → grabar 12 tomas por frase... o cambiar de método
```

Cuando el número te da 12, la respuesta correcta **no** es grabar 12 veces (la persona se agota y
empeora). La respuesta es **partir la frase en dos** (`177`) y grabar 5 de cada mitad. Módulo `178`.

**Cuánto material hace falta para un video de 60 segundos vertical:**

| Elemento | Material bruto necesario |
|---|---|
| Voz en cámara (40 s finales) | 4–6 minutos con las repeticiones |
| B-roll de producto | 2–3 minutos, mínimo 8 planos distintos |
| B-roll de ambiente/lugar | 1–2 minutos, mínimo 5 planos |
| Ambientes puros | 5 s por locación |
| **Total sano** | **8–12 minutos bien repartidos** |

Los 10 minutos del rodaje real **alcanzaban**. El problema no fue la cantidad: fue el **reparto**. Casi
todo era la misma cara diciendo la misma frase en tres sitios distintos, y un solo plano de producto.

---

## 6. Lo que SÍ salió bien y hay que repetir siempre

En medio de todo, alguien hizo algo brillante sin saberlo: **grabó la secuencia completa del producto en
un solo clip de 61 segundos**. La botella en la mesa, la mano que la destapa, el líquido que cae, la
copa que se llena, la copa llena en primer plano. Todo seguido, sin cortar.

Ese clip **salvó el video**. De ahí salieron cuatro planos distintos de b-roll (`22`: punch-in a
distintas zonas del cuadro), el plano de portada, y el remate.

**Por qué funciona tan bien:**

1. Es **una acción con principio y final**. El editor puede entrar y salir donde quiera.
2. Tiene **movimiento real** — líquido, manos, espuma. La imagen viva retiene (`06`).
3. Al ser un solo clip, **la luz y el color son idénticos** en todos los planos que saques de él.
4. Da **sonido real** aprovechable: el destape, el líquido cayendo (`77`).

**Regla que sale de ahí, y que va en todos los briefings:**

> **Toda acción de producto se graba completa, de una sola vez, sin cortar.** Aunque después solo se
> usen 3 segundos. Un clip largo de una acción vale más que diez clips cortos sueltos.

Ver `174` (cobertura) y `153` (comida y bebida en video).

---

## 7. Plantilla de briefing (copia y pega)

```
BRIEFING DE RODAJE — [nombre del video]
Fecha: [ ]   Lugar: [ ]   Duración final estimada: [ ] segundos
Publica en: [ ]   Formato: 9:16 vertical

QUIÉN HABLA: [ ]
Nivel: (  ) actor  (  ) con práctica  (  ) nunca ha grabado
→ Si es la tercera: frases de máximo 10 palabras y método del módulo 178.

ANTES DE EMPEZAR (obligatorio, 5 minutos)
[ ] Música del local APAGADA
[ ] Celular en modo avión, No molestar
[ ] Espacio libre revisado (mínimo 10 GB)
[ ] Batería > 60% o cargador conectado
[ ] Lente limpio
[ ] Prueba de audio de 10 s, revisada de verdad
[ ] Resolución 1080p / 30 fps confirmada

BLOQUES POR LOCACIÓN (no por orden del guion)
LOCACIÓN 1: [ ]
  - Frases: [ ]
  - Tomas por frase: 3 buenas
  - Ambiente puro 5 s: [ ]
  - B-roll aquí: [ ]
LOCACIÓN 2: [ ]
  ...

SECUENCIA DE PRODUCTO (un solo clip largo, sin cortar)
[ ] Producto en reposo
[ ] Manos que lo toman / abren
[ ] La acción (servir, cortar, montar)
[ ] Resultado final en primer plano
[ ] Alguien lo prueba / reacciona

B-ROLL OBLIGATORIO (tachar cada uno)
[ ] Fachada / entrada
[ ] Ambiente general del sitio
[ ] Detalle de barra / mesa
[ ] Manos trabajando
[ ] Producto llegando a la mesa
[ ] Reacción de alguien
[ ] Plano de portada (el frame de la miniatura, 94)

ENTREGA AL EDITOR
[ ] Clips originales, sin comprimir, sin filtros
[ ] Nombrados por bloque y locación
[ ] Nota de voz del director con qué pasó
```

---

## 8. Cómo se dice todo esto sin que suene a regaño

El briefing lo lee gente que está haciendo un favor, en su negocio, en su horario. Si suena a manual de
la NASA nadie lo cumple.

Tres traducciones que funcionan:

| En vez de decir | Di |
|---|---|
| "Necesito niveles entre -12 y -6 dBFS" | "Grabemos 10 segundos y los oímos. Si suena raspado, nos alejamos un paso." |
| "Hay que respetar la continuidad de iluminación" | "Terminamos todo lo de acá y después nos movemos. No volvemos." |
| "Requiero cobertura suficiente de b-roll" | "Necesito 10 planos cortos de cosas: el trago, las manos, la barra. 15 segundos cada uno." |
| "Tres tomas por línea de guion" | "Dilo tres veces seguidas. La tercera casi siempre es la buena." |

Y una frase que cierra cualquier discusión: **"Todo lo que grabemos de más hoy son horas que no
gastamos mañana."** Es literalmente cierto.

---

## Errores comunes

1. **Mandar el briefing el mismo día del rodaje.** Se manda el día antes, y se lee en voz alta 10
   minutos antes de grabar. Un documento que nadie leyó no existe.
2. **Confiar en que "eso lo arreglas en edición".** El audio saturado, el foco perdido y la música del
   local **no se arreglan**. Di exactamente cuáles son las cinco cosas que no tienen arreglo.
3. **Planear con tasa de aprovechamiento del 90%.** Con alguien que no es presentador la tasa real es
   20–30%. Planea con esa.
4. **No nombrar un responsable del b-roll.** Si es "de todos", no lo hace nadie, y sale un solo clip de
   producto para todo el video. Que sea una persona con la lista en la mano.
5. **Grabar en orden de guion.** Produce saltos de luz que no se arreglan. Se graba por locación (`175`).
6. **Pedir 4K porque "se ve mejor".** Se ve mejor hasta que el celular se calienta y corta la toma
   buena. 1080p/30 estable gana siempre (`171`).
7. **Dejar la música del local sonando "bajita".** "Bajita" sigue siendo -34 dB de piso de ruido: mata
   la detección de silencios, mete derechos de terceros y contamina cada corte.
8. **No grabar ambiente puro.** Son 5 segundos por sitio y es la herramienta que tapa todos los saltos
   de audio en el montaje. No hay excusa.
9. **Grabar la acción del producto en cinco clips cortos.** Una sola toma larga de la acción completa da
   más planos y con luz idéntica. Fue lo único que salvó el rodaje real.
10. **Enviar el material por WhatsApp.** Recomprime, baja resolución y a veces rota el video. Cable,
    Drive o AirDrop.
11. **No dejar colchón al final de la toma.** Cortar la grabación justo al terminar la frase deja al
    editor sin margen para un corte limpio. Dos segundos de quietud.
12. **Rodar sin saber dónde se publica.** El formato define el encuadre. Si se graba horizontal y se
    publica vertical, se pierde la mitad de la imagen (`176`).

---

## Checklist

- [ ] El briefing se **envió por escrito el día antes** y se leyó en voz alta antes de grabar.
- [ ] Está claro y por escrito **dónde se publica** y **cuánto dura** el video final.
- [ ] La **música del local se apaga** — quedó dicho, no insinuado.
- [ ] Hay **prueba de audio de 10 segundos** planeada antes de la primera toma real.
- [ ] El guion está dividido en **bloques de 8–12 palabras**.
- [ ] Se definió el **número de tomas por frase** según el nivel de quien habla (mínimo 3 buenas).
- [ ] El plan de rodaje está **ordenado por locación**, no por orden del guion.
- [ ] Hay **una persona responsable** del b-roll, con la lista impresa.
- [ ] La **secuencia de producto** está planeada como **un solo clip largo sin cortar**.
- [ ] Está agendado grabar **5 segundos de ambiente puro por locación**.
- [ ] Alguien dice en voz alta **"bloque X, toma Y"** antes de cada toma.
- [ ] Cada toma buena termina con **2 segundos de quietud**.
- [ ] Se revisó **espacio libre, batería, modo avión y lente limpio**.
- [ ] Está acordado **cómo se entrega el material** (nunca por WhatsApp) y **cómo se nombran** los clips.
- [ ] El editor sabe si **se puede volver a grabar**. Si no se puede, se dobló la cobertura.
