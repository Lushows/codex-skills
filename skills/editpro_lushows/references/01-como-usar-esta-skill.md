# 01 — Cómo usar esta skill

Resuelve el problema de **qué cargar y en qué orden** cuando llega una petición de video. La biblioteca
tiene 200 módulos; cargarlos todos es imposible y cargar los equivocados es peor que no cargar nada.
Aquí está el ruteo.

---

## La regla base

> Detecta el modo → carga entre 1 y 4 módulos → ejecuta → cierra con `98-verificacion-del-corte.md`.

Tres cosas no se negocian:

1. **Nunca cargues más de 4 módulos de golpe.** Si necesitas más, es que no entendiste la petición.
2. **El bloque 1 (10–19, lectura del material) no se salta.** Ni con prisa.
3. **Toda entrega pasa por `98`.** Sin excepción, aunque el video dure 6 segundos.

---

## Los 10 modos

### Modo 1 — Montaje desde bruto

**Cómo llega:** "Te dejé unos clips en la carpeta, monta algo." · "Grabé el evento, hazme un reel." ·
"Tengo 40 minutos de entrevista, sácame 3 piezas."

**Qué es:** el modo completo. Hay material que nadie ha leído y no hay estructura decidida. Es el más
largo, y el que más se arruina por saltarse la lectura del material.

**Ruta:**

```
02 (brief)  →  10, 11, 12, 13 (leer el material)  →  14, 15, 16 (elegir y validar cortes)
            →  20, 21 (ritmo y tipo de corte)     →  30, 31, 33 (estructura)
            →  40 (texto)  →  70 (sonido)  →  90, 92 (entrega)  →  98 (verificar)
```

**Carga primero:** `02`, luego bloque 1 completo si el material es grande, o solo `11` + `13` si son
tres clips cortos.

**Trampa clásica:** empezar a cortar el clip 1 mientras todavía no has abierto el clip 7. Ahí está el
gancho.

---

### Modo 2 — Diagnóstico de ritmo

**Cómo llega:** "Este video se ve lento." · "No sé qué tiene pero aburre." · "Se cae la retención en
el segundo 8." · "No fluye."

**Qué es:** ya existe un video montado y el problema es de pulso, no de contenido. Es un modo de
**medición**, no de gusto.

**Ruta:**

```
27 (diagnóstico)  →  20 (medir cambios por segundo)  →  22 (punch-in como cura barata)
                  →  140 (leer la métrica de retención si la hay)
```

**Carga:** `20`, `27`, `22`, `140`.

**Primer movimiento siempre:** contar cortes. Antes de opinar, este comando te da la lista de cambios
de escena detectados:

```bash
ffmpeg -hide_banner -i video.mp4 -filter:v "select='gt(scene,0.25)',showinfo" -f null - 2>&1 | grep showinfo
```

Divide la cantidad de cambios entre la duración: si te da menos de 0,4 cambios por segundo en un
vertical, ahí está tu "lento". Ver `20`.

---

### Modo 3 — Comercial / publicidad

**Cómo llega:** "Hazlo un comercial." · "Que se vea de TV." · "Necesito el creativo para la pauta." ·
"Un video para vender la calculadora."

**Qué es:** el video tiene un objetivo de negocio explícito y un lugar donde va a correr pagado. Cambia
todo: el ritmo es más apretado, el producto tiene que ser protagonista, y el remate tiene que llevar a
una acción.

**Ruta:**

```
02 (brief con objetivo de negocio)  →  150 (anatomía del comercial)  →  151 (ritmo publicitario)
→  152 (producto protagonista)      →  145 (video para anuncios Meta)  →  98
```

**Carga:** bloque 15 (`150`–`159`) según el tipo, más `145`/`146` si es Meta o CTWA.

**Frontera con las hermanas:** *qué decir* para vender lo define `ventas_lushows`; *qué creativo testear
y con qué presupuesto* lo definen `facebook_ads_lushows` / `tiktok_ads_lushows`. Aquí se produce la
pieza; no decidas el CPA objetivo.

---

### Modo 4 — Texto y tipografía cinética

**Cómo llega:** "Ponle subtítulos." · "Que salga el texto animado." · "Necesito que se lea sin sonido."

**Qué es:** trabajo sobre el canal de texto. Ojo: **la mayoría del público ve sin sonido**, así que
este modo casi nunca es un accesorio — es el canal principal.

**Ruta:**

```
40 (texto como canal principal)  →  41 (¿subtitular todo o resaltar clave?)
→  43 (formato ASS/libass)       →  45 (zona segura de la plataforma)  →  46 (ritmo del texto)
```

**Carga:** `40`, `41`, `43`, `45`.

**Decisión bisagra que se toma de primero:** ¿subtítulo completo o palabra clave? Depende del formato
y del objetivo, no del gusto. Está en `41`.

---

### Modo 5 — Color

**Cómo llega:** "Se ve feo el color." · "Que se vea cinematográfico." · "Los clips no combinan entre
sí." · "Ponle los colores de la marca."

**Qué es:** dos trabajos distintos que la gente confunde. **Corregir** es dejar la imagen neutra y
correcta. **Gradar** es darle un look. Se hace en ese orden y nunca al revés.

**Ruta:**

```
61 (corrección vs gradación)  →  62 (emparejar planos)  →  67 (piel)
→  63 (look cine) o 64 (forzar paleta de marca)  →  69 (scopes para verificar)
```

**Carga:** `61`, `62`, `67` si hay gente en cuadro, y luego `63` o `64` según el objetivo.

**Regla:** si la petición es "que tenga los colores de la marca", el módulo es `64` (duotono y mapeo),
no `65` (LUTs). Un LUT no impone una paleta de marca; la tuerce.

---

### Modo 6 — Sonido y voz

**Cómo llega:** "El audio suena mal." · "Quita el ruido de fondo." · "Se oye lejos." · "La música tapa
la voz."

**Qué es:** el modo donde más se nota la diferencia entre amateur y profesional, y donde la gente hace
lo contrario de lo que debería (quitar ruido a lo bestia y dejar la voz muerta).

**Ruta:**

```
70 (cadena de voz completa, 9 módulos en orden)  →  71 (ruido)  →  72 (ecualización)
→  73 (compresión y LUFS)  →  75 (ducking si hay música)
```

**Carga:** `70` siempre primero. Los demás según el síntoma.

**Diagnóstico antes de tocar nada** — mira el espectrograma, que es la foto de las frecuencias en el
tiempo:

```bash
ffmpeg -hide_banner -i voz.wav -lavfi showspectrumpic=s=1600x900:legend=1 espectro.png
```

Si ves una franja continua abajo en todo el clip, es zumbido eléctrico o aire acondicionado. Si ves
manchas verticales sueltas, son golpes. Cada una se trata distinto.

---

### Modo 7 — Motion graphics y composición

**Cómo llega:** "Ponle animaciones." · "Que salga el logo moviéndose." · "Necesito un gráfico con los
números."

**Ruta:**

```
80 (pensar en capas)  →  84 (keyframes y curvas)  →  85 (los 12 principios)
→  81 (recortes sin fondo) o 86 (gráficos de datos) según el caso
```

**Carga:** `80`, `84`, más el específico.

**La causa #1 de que un motion se vea barato:** interpolación lineal. El movimiento uniforme no existe
en la naturaleza. Todo entra rápido y frena, o anticipa antes de salir. Está en `84`.

---

### Modo 8 — IA generativa

**Cómo llega:** "No tengo material de eso, genéralo." · "Hazme un video con Veo." · "Necesito una
imagen de fondo." · "Ponle una voz."

**Ruta:**

```
120 (panorama a agosto 2026)  →  129 (lo que todavía hace mal — LÉELO ANTES DE PROMETER)
→  125 (la IA no respeta la marca)  →  126 (referencia visual vs descripción)
→  127 (costos) →  128 (ética y derechos)
```

**Carga:** `120`, `129`, `125`.

**Regla dura:** *real para lo tangible, ilustración para lo abstracto.* Nunca generes con IA lo que ya
está filmado. Un plato de comida generado se ve falso y mata la credibilidad; el plato real, aunque
esté peor iluminado, vende. Ver `82`, `153`.

---

### Modo 9 — Puente a CapCut

**Cómo llega:** "Déjame el proyecto para editarlo yo." · "Prepárame la base y yo la afino." · "Mándame
el archivo de CapCut."

**Qué es:** división de trabajo. Tú preparas lo aburrido y exacto (cortes medidos, subtítulos con
tiempos, audio limpio, orden de clips); el humano pone lo que requiere ojo y gusto.

**Ruta:**

```
110 (panorama CapCut)  →  111 (estructura del proyecto)  →  112 (generar un draft por código)
→  116 (flujo híbrido: qué hace cada uno)  →  119 (límites y riesgos)
```

**Carga:** `110`, `111`, `116`.

**Sé honesto con el riesgo:** los formatos de proyecto de CapCut cambian entre versiones y un draft
generado por código puede no abrir. `119` existe por eso. Siempre entrega también el render plano como
respaldo.

---

### Modo 10 — Pipeline / automatización

**Cómo llega:** "Esto lo voy a hacer todas las semanas." · "Automatiza el proceso." · "Necesito sacar
20 variantes del mismo anuncio."

**Ruta:**

```
130 (diseñar el pipeline)  →  131 (el montaje como tabla de datos, no como archivo)
→  133 (verificación automática)  →  134 (procesar por lotes)  →  137 (cuándo NO automatizar)
```

**Carga:** `130`, `131`, `137`.

**Lee `137` antes de prometer.** Automatizar tiene sentido cuando el formato es estable y el volumen
alto. Un video al mes con criterio distinto cada vez se hace a mano y sale más barato.

---

## Tabla rápida de ruteo

| Señal en el mensaje | Modo | Carga |
|---|---|---|
| "monta", "te dejé clips", "hazme un reel de esto" | 1 · Montaje | `02` → bloque 1 → `20` → `98` |
| "lento", "aburre", "no fluye", "se cae la retención" | 2 · Ritmo | `27`, `20`, `22`, `140` |
| "comercial", "de TV", "para la pauta", "vender" | 3 · Comercial | `150`, `151`, `152`, `145` |
| "subtítulos", "texto en pantalla", "sin sonido" | 4 · Texto | `40`, `41`, `43`, `45` |
| "color feo", "cinematográfico", "colores de marca" | 5 · Color | `61`, `62`, `67`, `63`/`64` |
| "audio malo", "ruido", "se oye lejos", "música tapa" | 6 · Sonido | `70`, `71`, `72`, `73` |
| "animación", "logo animado", "gráfico" | 7 · Motion | `80`, `84`, `85` |
| "genera", "IA", "no tengo material" | 8 · IA | `120`, `129`, `125` |
| "mándame el proyecto", "yo lo afino" | 9 · CapCut | `110`, `111`, `116` |
| "todas las semanas", "en lote", "20 variantes" | 10 · Pipeline | `130`, `131`, `137` |

---

## Cuando la petición mezcla varios modos

Es lo normal. "Monta esto, ponle subtítulos y que se vea de comercial" son los modos 1 + 4 + 3.

**No cargues los tres bloques.** Se resuelve por fases, y cada fase carga lo suyo:

1. Fase de lectura y estructura → modo 1.
2. Fase de acabado de texto → modo 4.
3. Fase de tratamiento publicitario → modo 3.
4. Verificación → `98`.

Trabajar por fases es además el orden correcto del proceso de montaje (ver `07`). Poner subtítulos
antes de tener el corte fino cerrado significa rehacerlos todos cuando muevas un corte.

---

## Cuándo esta skill NO es la respuesta

Reconocer esto rápido ahorra trabajo botado:

| Petición | Va a |
|---|---|
| "Diséñame el logo / la paleta / la marca" | `directorcreativo_lushows` |
| "Hazme la landing donde va el video" | `desingweb-lushows` |
| "¿Qué le digo al cliente para que compre?" | `ventas_lushows` |
| "¿Cuánto invierto en la campaña? ¿Qué CPA es bueno?" | `facebook_ads_lushows` / `tiktok_ads_lushows` |
| "Móntame el modelo de video en una GPU" | `engineer_visualopen_lushows` |
| "¿Cuánto cobro por editar?" | `180` de aquí, pero los números al detalle → `economist_lushows` |

Si el proyecto no tiene identidad visual definida, **para y manda a `directorcreativo_lushows`**. Es
mejor perder media hora que montar 40 piezas que hay que rehacer.

---

## Cómo se cierra siempre

Tres cosas, en este orden, en toda respuesta que entregue video:

1. **Qué se hizo y por qué** — la decisión de montaje en una frase, sin nombrar herramientas.
2. **Qué se verificó y con qué medida** — números concretos.
3. **Qué no pudiste juzgar** — lo que le toca al humano.

Ejemplo de cierre correcto:

> Monté 38 s: gancho con la frase del segundo 112 del bruto (era el mejor momento y estaba enterrado),
> bucle abierto que cierra en el remate. Verifiqué: 1080x1920 a 30 fps, 38,4 s, -14,1 LUFS integrados,
> pico real -1,3 dBTP, ninguna palabra partida (transcribí el render final), texto dentro de la zona
> segura de Reels. **No puedo juzgar** si la música va con el tono de la marca ni si el chiste del
> segundo 22 funciona: eso lo decides tú.

---

## Errores comunes

- **Cargar 10 módulos "por si acaso".** Gasta contexto y diluye el criterio. Máximo 4.
- **Saltarse el brief (`02`) porque "ya sé lo que quiere".** Es la causa #1 de rehacer entero.
- **Saltarse la lectura del material porque hay prisa.** La prisa se paga doble.
- **Entrar por el módulo técnico y no por el modo.** Alguien pide "que se vea profesional" y arrancas
  en `102-ffmpeg-filtros-de-video`. Primero el modo, después la herramienta.
- **Confundir modo 5 con modo 8 de color:** "colores de marca" es `64` (duotono/mapeo), no `65` (LUTs).
- **Poner subtítulos antes de cerrar el corte fino.** Se rehacen todos.
- **Meterse a decidir presupuesto de pauta o copy de venta.** Eso es de las skills hermanas.
- **Entregar sin pasar por `98`.** Aunque sean 6 segundos.
- **Prometer algo de IA generativa sin haber leído `129`.** La lista de lo que todavía falla existe
  justo para no prometer de más.
- **Generar un draft de CapCut sin entregar también el render plano.** Si el draft no abre, quedaste sin nada.

---

## Checklist

Al recibir cualquier petición de video:

- [ ] Identifiqué el **modo** (1 al 10) antes de abrir cualquier módulo.
- [ ] Si mezcla modos, los ordené por fases en vez de cargarlos todos.
- [ ] Cargué **máximo 4** módulos.
- [ ] Si es montaje desde bruto: hice el brief (`02`) y leí **todo** el material antes de decidir.
- [ ] Verifiqué que la petición sea de esta skill y no de una hermana.
- [ ] Si no hay identidad de marca definida, lo dije y mandé a `directorcreativo_lushows`.
- [ ] Ejecuté midiendo, no adivinando.
- [ ] Pasé por `98-verificacion-del-corte.md` antes de entregar.
- [ ] Cerré con: qué se hizo y por qué · qué verifiqué con qué medida · qué no pude juzgar.
