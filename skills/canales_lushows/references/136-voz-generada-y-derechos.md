# 136 · Voz generada y derechos

**Qué resuelve:** la voz del canal es sintética, y eso abre **dos frentes distintos** que
casi todo el mundo mezcla: los **términos de uso del motor** que la genera, y el derecho
sobre la **semejanza** de una persona real. Son problemas separados, con soluciones
separadas.

> ⚖️ **Esto no es asesoría legal.** El terreno de la semejanza está cambiando ahora
> mismo, país por país y estado por estado. Lo que este módulo fija es una **regla de
> canal** deliberadamente más estricta que cualquier ley, para no depender de cómo
> acaben las leyes.

---

## Frente 1 · Los términos del motor

Cada motor de texto a voz tiene sus condiciones y **no son intercambiables**. Lo que hay
que leer y guardar, siempre con fecha:

| Qué comprobar | Por qué importa |
|---|---|
| ¿Permite **uso comercial**? ¿En el plan gratuito o solo de pago? | Un canal monetizado es uso comercial desde el primer día |
| ¿Exige **atribución** o aviso de que la voz es sintética? | Incumplirlo tumba la cobertura de la licencia |
| ¿Prohíbe hacer pasar la voz por la de una **persona real**? | Casi todos lo prohíben, y con razón |
| ¿Qué pasa con lo publicado si **cancelas** la cuenta? | Mismo problema que con los bancos (§ 134) |
| ¿Puede el proveedor **cambiar** los términos con efecto retroactivo? | Determina si hay que archivar el PDF con versión |

### El caso concreto de este canal: `edge-tts`

Hay que decirlo sin adornos. `edge-tts` **no es una API oficial de Microsoft**: es un
cliente no oficial del servicio de «Leer en voz alta» de Edge. El paquete en sí tiene
licencia libre, pero eso cubre el *código*, no el *servicio* que hay al otro lado.

En las consultas públicas de Microsoft Q&A, la respuesta es consistentemente que **no
hay documentación que autorice explícitamente el uso comercial** de esas voces por esa
vía, y se remite a Azure Speech para uso comercial
([Microsoft Q&A](https://learn.microsoft.com/en-us/answers/questions/2088770/are-opensource-edge-tts-free-for-commercial-use)).

⚠️ **Riesgo abierto, no resuelto.** No he encontrado ni una autorización expresa ni una
prohibición expresa dirigida a este uso. No voy a afirmar que sea seguro porque no lo
sé, y tampoco que sea ilegal. Lo que sí puedo decir es qué habría que hacer para cerrar
el frente:

1. Leer los términos del servicio de Edge vigentes y guardarlos con fecha.
2. Si no cubren el uso comercial, mover la locución a un motor con licencia comercial
   explícita —Azure Speech de pago es el camino directo— o a un motor local de código
   abierto cuya licencia se haya leído entera.
3. Anotar la decisión y la fecha en el cuaderno del canal.

Mientras eso no se haga, **es una deuda conocida del pipeline**, no un asunto cerrado.

## Frente 2 · La semejanza de una persona real

Aquí no se trata de derechos de autor sino de derechos sobre la **identidad**: la voz y
la imagen de alguien. El panorama, con lo que sé con certeza:

- **NO FAKES Act (EE. UU.):** crearía un derecho federal frente a réplicas digitales no
  autorizadas de voz e imagen, con un procedimiento de notificación y retirada.
  **Todavía no es ley.** La versión de 2026 (S. 4591 y H.R. 8915, 119.º Congreso) se
  reintrodujo el 20 de mayo de 2026 y fue informada en comisión el 18 de junio de 2026
  ([Congress.gov](https://www.congress.gov/bill/119th-congress/senate-bill/4591)). Es la
  cuarta vez que el texto aparece en unos tres años. **No des por hecho que se aprobará
  ni cuándo.**
- **Leyes estatales de EE. UU.:** existen derechos de imagen y publicidad estatales, y
  al menos un estado ha legislado específicamente sobre voz e IA. ⚠️ No conozco el mapa
  completo de los cincuenta estados y no lo voy a resumir de memoria.
- **Europa y América Latina:** la protección suele venir por derechos de la
  personalidad —imagen, voz, honor— y por protección de datos, no por derecho de autor.
  ⚠️ El detalle varía por país; **pendiente de verificar** donde haga falta.

### Lo que sí hace YouTube, hoy

YouTube tiene **detección de semejanza**: el creador se da de alta, la plataforma escanea
subidas nuevas buscando su rostro alterado o generado por IA, y puede pedir la retirada
por las Normas de privacidad. En 2025-2026 se amplió a más creadores mayores de edad y a
periodistas y cargos públicos
([YouTube Ayuda](https://support.google.com/youtube/answer/16440338) ·
[Blog de YouTube](https://blog.youtube/news-and-events/expanding-likeness-detection-civic-leaders-journalists/)).
Según la propia ayuda, **cubre el rostro, no la voz**.

Traducido a nuestro riesgo: un rostro real generado en un episodio es hoy detectable de
forma automática por la propia plataforma, y la retirada no depende de que exista o no
una ley nueva.

## La regla del canal, que no se discute

> **Nunca la voz ni la cara de una persona real, generadas.**

Sin matices y sin excepciones «por una vez»:

- Ni de personas vivas ni de fallecidas recientes.
- Ni «una voz parecida a», ni un acento que imite a alguien concreto.
- Ni rostros generados de personas reales, ni retoques que los animen.
- Las **citas textuales** de un personaje se leen con la voz del canal y se rotulan como
  lectura de un documento (§ 48, § 272). Nunca se interpretan como si el personaje
  hablara.
- Las reconstrucciones visuales van etiquetadas como tales (§ 276, § 384).

Esta regla no está aquí por miedo legal, aunque también. Está porque **un canal de
documentales vende una sola cosa: que lo que enseña es verdad**. El día que un
espectador descubre una voz falsificada, todo lo demás pasa a ser sospechoso.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Suponer que la voz sintética no tiene licencia detrás | Canal monetizado sobre un servicio que quizá no lo permite |
| Usar el plan gratuito de un motor para contenido monetizado | Uso fuera de ámbito desde el primer episodio |
| Clonar la voz del protagonista «para dar ambiente» | Riesgo de semejanza y pérdida total de credibilidad |
| Generar el rostro de una persona real | Detectable por la propia plataforma y retirable |
| Dar el NO FAKES Act por ley vigente | Se decide sobre una norma que aún no existe |
| Dar por hecho que si no hay ley, no hay riesgo | Los derechos de imagen ya existían mucho antes de la IA |
| No guardar los términos del motor con fecha | Cuando cambien, no habrá manera de saber qué aceptaste |

## Relacionado

`87` voz a fondo · `280` escribir para una voz sintética · `133` reclamaciones ·
`382` personas reales · `383` caras generadas: la línea · `384` reconstrucción y transparencia
