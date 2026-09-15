# 119 — Límites y riesgos: la letra chica del puente

Los ocho módulos anteriores te enseñaron a hacer algo que funciona muy bien. Este te dice **cuándo no
hacerlo, y qué hacer para que el día que falle no te cueste un cliente.**

Es el módulo menos divertido del bloque y el que más plata te va a ahorrar.

Empecemos por la frase que hay que tener presente todo el tiempo:

> **Estás escribiendo en un formato privado, sin documentar, de una app que se actualiza sola, que
> pertenece a una empresa que no te debe nada.**

Eso no significa que no lo hagas. Significa que lo hagas con red.

---

## Riesgo 1 — El formato no es oficial

ByteDance nunca publicó la especificación del `draft_content.json`. Todo lo que sabemos viene de gente
que abrió el archivo, comparó versiones y dedujo.

Consecuencias reales:

- **No hay contrato.** ByteDance no prometió que este formato siga existiendo, ni que las claves se
  llamen igual, ni que los valores signifiquen lo mismo.
- **No hay soporte.** Si algo no funciona, no hay a quién preguntarle. Solo foros y repositorios de
  terceros.
- **No hay avisos de cambio.** No existe un changelog que diga "en la 8.4 renombramos `masks` a
  `common_masks`". Te enterás porque se rompió.

Y eso ya pasó: en CapCut 9.6 `materials.masks[]` pasó a llamarse `materials.common_masks[]`. Un cambio
de nombre, y toda automatización que tocara máscaras dejó de funcionar de un día para otro.

**Mitigación:** tratá el formato como una dependencia externa frágil. Aislá el código que lo toca en un
solo lugar, así cuando cambie tenés un solo archivo que arreglar.

---

## Riesgo 2 — Una actualización te lo rompe

CapCut se actualiza solo y con frecuencia. Cualquier actualización puede:

- Cambiar el nombre de una clave
- Agregar un campo obligatorio nuevo
- Cambiar el valor por defecto de algo
- Migrar el proyecto a un esquema nuevo al abrirlo (**irreversible**)
- **Cifrar el archivo**

El último es el escenario del fin del mundo, y **ya ocurrió en la versión hermana**: JianYing, la
edición china del mismo producto, cifra el `draft_content.json` desde la versión 6. Una vez que una
versión nueva vuelve a guardar el proyecto, no hay vuelta atrás.

Que CapCut internacional no lo haya hecho hasta hoy (verificado en 8.3.0, agosto 2026) **no es una
garantía de mañana**. Es el mismo código base y la misma empresa.

**Mitigación:**

1. **Desactivá la actualización automática** en máquinas donde el puente es parte del trabajo.
2. **Guardá el instalador** de la versión que sabés que funciona.
3. **Verificá después de cada actualización**, antes de trabajar: abrí un `draft_content.json` y confirmá
   que sigue siendo texto plano.
4. **Tené un plan B escrito** (más abajo).

---

## Riesgo 3 — Perder trabajo

Este es el riesgo que se materializa más seguido y el más fácil de evitar.

Formas de perder trabajo con el puente:

| Cómo | Qué pasa |
|---|---|
| Escribir con CapCut abierto | La app reescribe encima al guardar. Tu trabajo desaparece sin aviso. |
| Escribir un JSON inválido sobre el original | El proyecto no abre y no hay copia |
| Dejar referencias huérfanas | El proyecto no abre |
| Abrir con una versión nueva | El proyecto se migra al esquema nuevo, irreversible |
| Borrar la carpeta equivocada | Se van todos los proyectos |
| Confiar en el `.bak` | Solo guarda **un** estado anterior. Dos escrituras malas y no queda nada. |

### El protocolo de respaldo (no es opcional)

**Antes de la primera línea de código, siempre:**

```powershell
# respaldo con fecha de TODOS los proyectos
$fecha = Get-Date -Format "yyyyMMdd-HHmm"
Compress-Archive `
  -Path "$env:LOCALAPPDATA\CapCut\User Data\Projects\com.lveditor.draft\*" `
  -DestinationPath "D:\respaldos\capcut-$fecha.zip"
```

**Antes de cada escritura sobre un proyecto en particular:**

```powershell
$proy = "$env:LOCALAPPDATA\CapCut\User Data\Projects\com.lveditor.draft\reel001"
Copy-Item $proy "$proy.respaldo-$(Get-Date -Format 'HHmmss')" -Recurse
```

Cuesta un segundo. Te salva la tarde.

### Trabajá con Git

Los `draft_content.json` son texto. Meté la carpeta de proyectos (o al menos los JSON) en un
repositorio Git local:

```bash
cd "/c/Users/user/AppData/Local/CapCut/User Data/Projects/com.lveditor.draft"
git init
git add "*/draft_content.json" "*/draft_meta_info.json"
git commit -m "estado antes de automatizar"
```

Con eso tenés historial completo, podés volver a cualquier estado, y `git diff` te muestra exactamente
qué cambió entre dos versiones — que además es la mejor herramienta de aprendizaje del formato
(módulo 112).

**Advertencia:** no metas los videos al repositorio. Solo los JSON. Un repositorio con archivos de
video se vuelve inmanejable en dos días.

---

## Riesgo 4 — Silencio en vez de error

CapCut casi nunca te dice qué está mal. Los modos de falla son:

| Síntoma | Causa probable |
|---|---|
| El proyecto no aparece en la lista | `draft_meta_info.json` mal escrito |
| Abre con la línea de tiempo vacía | `duration` en 0, o `material_id` que no coincide |
| Abre con todo en gris | Rutas de medios rotas |
| No abre / la app se cierra | JSON inválido o referencias huérfanas |
| Abre pero falta un elemento | Falta un campo obligatorio que no sabías que existía |
| Abre y se ve bien pero al exportar falla | Estado inconsistente que solo se detecta al renderizar |

El último es el peor, porque llega tarde. **Exportá siempre una prueba corta antes de dar el proyecto
por bueno.**

**Mitigación:** validá en capas, siempre en el mismo orden:

```
1. ¿El JSON es sintácticamente válido?      →  jq . archivo.json
2. ¿Hay referencias huérfanas?               →  capcut-cli lint
3. ¿Los archivos de medios existen?          →  verificar cada path
4. ¿Las cuentas de tiempo cierran?           →  target == source/speed, duration global
5. ¿Abre en CapCut?                          →  abrirlo
6. ¿Exporta?                                 →  exportar 5 segundos de prueba
```

Nunca saltes del paso 1 al 5.

---

## Riesgo 5 — Las herramientas de la comunidad

`pyCapCut` y `capcut-cli` son excelentes y te ahorran semanas. También:

- **No son oficiales.** Nadie las garantiza.
- **Dependen del mismo formato frágil.** Si CapCut cambia, ellas se rompen igual.
- **Pueden dejar de mantenerse.** Son proyectos de personas, no de empresas.
- **Pueden tener bugs que corrompan tu proyecto.** Es software libre sin garantía, y así lo dicen sus
  propias licencias.

**Mitigación:**

- **Fijá la versión.** `pip install pycapcut==X.Y.Z`, `npm install -g capcut-cli@X.Y.Z`. Nunca dejes que
  se actualicen solas en medio de un proyecto con fecha.
- **Probá la versión nueva en el laboratorio** antes de usarla en trabajo real.
- **Guardá una copia del código** que estás usando, por si el repositorio desaparece.
- **Entendé lo que hacen.** Si dependés de una caja negra que no entendés, el día que falle no vas a
  poder arreglarla.

---

## Riesgo 6 — Términos de servicio y datos

Esto no es un riesgo técnico, es un riesgo de negocio.

- **CapCut es de ByteDance.** Sus términos les dan licencias amplias sobre el contenido que subís a su
  nube, y ha estado en el centro de discusiones regulatorias en varios países.
- **Las funciones de IA suben tu material a sus servidores.** Subtítulos automáticos, quitar fondo,
  separar voz, mejorar calidad: todo eso sale de tu computador.
- **Automatizar la publicación viola los términos.** El puente termina en "listo para revisar", no en
  "publicado".
- **La automatización de UI** (que usa `pyCapCut` para exportar) está en una zona gris. Funciona, pero
  no es un uso previsto.

**Mitigación:**

- Material de cliente bajo NDA: **proyectos locales, sin sincronización en nube, sin funciones de IA de
  la app**. Lo que necesites de IA, hacelo con tus propias herramientas.
- Si el cliente pregunta dónde vive su material, tenés que poder responder con precisión.
- Nada de publicación automática.

---

## Riesgo 7 — La dependencia de una sola herramienta

Si todo tu flujo de trabajo depende de que CapCut siga siendo como es hoy, tenés un punto único de
falla en un producto sobre el que no tenés ningún control.

**Mitigación arquitectónica — y es la más importante de todo el módulo:**

> **Guardá tu montaje en tu propio formato, no en el de CapCut.**

```
     TU MODELO DEL MONTAJE (JSON tuyo, simple, estable)
     { cortes: [...], textos: [...], audio: [...] }
                    │
        ┌───────────┼───────────┬─────────────┐
        ▼           ▼           ▼             ▼
   CapCut      OTIO/EDL/XML   ffmpeg      lo que venga
   (revisión)  (profesional)  (render)    mañana
```

Tu modelo es una lista de cortes con tiempos, una lista de textos con posiciones, una lista de pistas
de audio con volúmenes. Cincuenta líneas de JSON que vos controlás.

Los generadores hacia CapCut, hacia OTIO y hacia ffmpeg son **traductores** de ese modelo. Si CapCut
cambia el formato, reescribís **un traductor** y el resto del sistema no se entera. Si CapCut cifra el
archivo mañana, tu montaje sigue existiendo y podés renderizarlo con ffmpeg o entregarlo como XML.

**Sin esta separación, el día que CapCut cambie perdés todo el trabajo acumulado.**

---

## El plan B (escribilo antes de necesitarlo)

Si mañana el puente deja de funcionar:

1. **¿Podés seguir entregando?** Sí, si tenés el modelo propio: renderizás con ffmpeg (bloque 100-105)
   y entregás el MP4.
2. **¿Podés seguir iterando con el humano?** Sí, pero más lento: volvés al ciclo de render + notas. Peor,
   no fatal.
3. **¿Podés migrar a otro editor?** Kdenlive y Shotcut usan XML abierto y documentado. Son menos
   populares pero el formato es estable y público. Resolve importa OTIO nativo.
4. **¿Perdiste proyectos?** No, si tenés respaldos y Git.

Tener este plan escrito convierte una crisis en un mal día.

---

## Cuándo NO usar el puente

Sé honesto contigo mismo con esta lista:

| Situación | Por qué no |
|---|---|
| **Entrega crítica sin margen** | Si no hay tiempo para que falle, no metas una dependencia frágil. |
| **El cliente tiene que abrir el proyecto** | No controlás su versión de CapCut ni sus fuentes ni su caché. |
| **Material bajo NDA estricto** | ByteDance, nube, términos. |
| **Trabajo de archivo (5-10 años)** | Este formato no va a existir. Guardá máster + OTIO + hoja de montaje. |
| **Un video simple de un solo corte** | El puente es más trabajo que arrastrarlo a mano. |
| **Color o audio serios** | CapCut no es la herramienta. Resolve y Pro Tools sí. |
| **Proyectos largos (más de ~20 min)** | CapCut se pone lento y a veces corrompe. |
| **Nadie va a mirar el resultado** | Todo el flujo se apoya en que el humano mire. Si no mira, no lo hagas. |

Esa última fila es la más importante. **El puente sirve porque acelera el ciclo entre máquina y humano.
Si sacás al humano, no queda nada bueno: queda un video correcto y sin alma, hecho más rápido.**

---

## La postura correcta

No es "esto es peligroso, no lo uses". Tampoco es "esto es magia, automatizá todo".

Es esta:

- **Es una herramienta poderosa apoyada en un cimiento inestable.**
- Usala donde el beneficio es grande y el costo de la falla es bajo: iteración rápida, borradores,
  volumen, subtítulos, montajes repetitivos.
- No la uses donde el costo de la falla es alto: entregas críticas, archivo, material sensible.
- **Respaldá siempre. Validá siempre. Verificá después de cada actualización. Tené plan B.**
- **Guardá tu montaje en tu propio formato**, no en el de nadie más.

Con esas cinco reglas, el peor escenario es un mal día. Sin ellas, el peor escenario es perder el
trabajo de una semana y la confianza de un cliente.

---

## Errores comunes

**Creer que el formato es estable porque hoy funciona.** No hay contrato. En JianYing ya se cifró. Y en
CapCut 9.6 ya se renombró una clave.

**Dejar la actualización automática activa en una máquina de trabajo.** Te podés despertar sin puente
el día de la entrega.

**Confiar en el `.bak` de CapCut.** Guarda un solo estado anterior. Dos escrituras malas y no queda
nada.

**No respaldar antes de la primera prueba.** El respaldo que sirve es el que hiciste **antes** del
error, no el que ibas a hacer después.

**Escribir con CapCut abierto.** Sigue siendo la causa número uno de trabajo perdido, y es la más
fácil de evitar.

**Saltarse la validación.** Los pasos 1 a 4 cuestan segundos. El paso 5 cuesta abrir la app y no
entender por qué no anda.

**No exportar una prueba.** Hay estados que solo fallan al renderizar, y te enterás cuando ya no hay
tiempo.

**Dejar que las librerías se actualicen solas.** Fijá versiones.

**Depender de una caja negra que no entendés.** El día que falle, no vas a poder arreglarla.

**Guardar el montaje solo en formato CapCut.** Es atarte a una empresa que no te debe nada. Modelo
propio + traductores.

**Subir material confidencial a las funciones de IA de la app.** Sale de tu computador bajo sus
términos.

**Automatizar la publicación.** Viola los términos y te puede costar la cuenta.

**Usar el puente para una entrega crítica sin margen.** El día que falle va a ser justo ese.

**Sacar al humano del flujo.** Ahí se pierde todo el sentido del arreglo.

---

## Checklist

**Antes de empezar (una vez)**
- [ ] Respaldé la carpeta completa de proyectos, con fecha, fuera del disco de trabajo
- [ ] Inicialicé un repositorio Git con los JSON (sin los videos)
- [ ] Desactivé la actualización automática de CapCut
- [ ] Guardé el instalador de la versión que sé que funciona
- [ ] Fijé la versión de las librerías que uso
- [ ] Escribí mi plan B en un archivo, no en mi cabeza

**Arquitectura**
- [ ] Mi montaje vive en **mi propio formato**, y CapCut es un destino, no la fuente de verdad
- [ ] El código que toca el formato de CapCut está aislado en un solo lugar
- [ ] Puedo renderizar con ffmpeg sin pasar por CapCut si hace falta

**Cada vez que trabajo**
- [ ] Copié el proyecto antes de escribirlo
- [ ] **CapCut está cerrado**
- [ ] Validé: JSON sintáctico → huérfanos → medios existen → cuentas de tiempo → abre → exporta prueba

**Después de cada actualización de CapCut**
- [ ] Verifiqué que `draft_content.json` sigue siendo texto plano
- [ ] Probé el flujo completo en el laboratorio antes de usarlo en trabajo real
- [ ] Revisé si alguna clave cambió de nombre

**Criterio**
- [ ] Este trabajo tiene margen para que el puente falle
- [ ] El material no es confidencial, o estoy trabajando 100% local sin funciones de nube
- [ ] No estoy automatizando publicación
- [ ] **Hay un humano que va a mirar el resultado completo antes de que salga**
