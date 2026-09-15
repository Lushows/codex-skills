# 128 — Ética y derechos de la IA en video: lo que puedes hacer, lo que no, y lo que tienes que declarar

## Aviso honesto

No soy abogado y esto no es asesoría legal. Es lo que un editor profesional necesita saber para no
meter a su cliente —ni a sí mismo— en un problema evitable. Las leyes de esta materia se están
escribiendo **ahora mismo** y este módulo tiene fecha: **4 de agosto de 2026**.

Cuando el dinero en juego sea serio, la respuesta correcta no es este módulo: es un abogado.

Pero la mayoría de los problemas reales no requieren abogado. Requieren no hacer tres o cuatro cosas
obvias que la gente hace igual porque nadie se las dijo.

---

## Lo que cambió el 2 de agosto de 2026

Dos días antes de la fecha de este módulo entró a aplicarse el **Artículo 50 del Reglamento Europeo
de IA (EU AI Act)**.

Qué exige, en cristiano, para contenido de video generado con IA que llegue a público europeo:

1. **Marca de agua legible por máquina** (C2PA o equivalente) incrustada en el archivo.
2. **Divulgación visible para humanos**: que el espectador pueda saber que eso es sintético.

Sanciones citadas: hasta **15 millones de euros o el 3% de la facturación global anual**.

### ¿Te aplica a ti, montando reels en Colombia?

Directamente, probablemente no. Pero:

- **Si el cliente vende a Europa, sí.** Y muchos venden sin saberlo: una tienda en línea con envíos,
  una marca que pauta con segmentación amplia, un producto turístico.
- **Las plataformas se están adelantando a la ley.** Meta, YouTube y TikTok ya tienen etiquetas de
  contenido generado por IA y políticas propias. Incumplir la política de la plataforma te cuesta
  alcance o la cuenta, sin necesidad de que ninguna ley te alcance.
- **La dirección del viento es clara.** Nueva York también legisló divulgación en 2026 y hay
  actividad en muchas jurisdicciones. Lo que hoy es europeo, en dos años es normal en todas partes.

**Recomendación práctica: declara siempre.** Cuesta nada y te quita el problema de encima para
siempre.

---

## C2PA y SynthID: qué son y en qué se diferencian

Se confunden constantemente. Son cosas distintas y complementarias.

| | **C2PA / Content Credentials** | **SynthID** |
|---|---|---|
| Qué es | Metadatos firmados criptográficamente | Marca invisible en los píxeles |
| Metáfora | Un **certificado de nacimiento** pegado al archivo | Una **filigrana** dentro del papel |
| Contiene | Quién lo creó, con qué herramienta, cuándo, qué ediciones tuvo | Solo la señal de "esto es sintético" |
| Sobrevive a... | Poco. Se pierde al recomprimir, al subir a redes, al recortar | Recorte, filtros, compresión, **capturas de pantalla** |
| Quién lo usa | Estándar de industria (Adobe, Microsoft, OpenAI, muchos más) | Google (Imagen, Veo, Lyria); adoptado también por otros actores en 2026 |

Traducción práctica para ti:

- **El material que generes con Veo, Imagen o Lyria ya sale con SynthID incrustado.** No lo puedes
  quitar y no deberías intentarlo. Está en los píxeles.
- **Los metadatos C2PA los destruye tu propio flujo de trabajo.** Cuando pasas el clip por ffmpeg,
  recomprimes y los metadatos se van. No es sabotaje, es cómo funciona.
- Por eso la divulgación visible importa: es la capa que sobrevive a todo, porque la pones tú.

### Cómo preservar C2PA (si te lo piden)

```bash
# copia todos los metadatos que ffmpeg pueda arrastrar
ffmpeg -i entrada.mp4 -map_metadata 0 -movflags use_metadata_tags -c copy salida.mp4
```

Advertencia honesta: eso arrastra metadatos genéricos, pero **la firma criptográfica C2PA
generalmente no sobrevive a una recodificación**, porque la firma cubre el contenido y el contenido
cambió. Si el cliente exige C2PA de extremo a extremo, necesitas herramientas específicas del
estándar (`c2patool` y similares) y un flujo diseñado para eso. No prometas lo que no puedes
verificar.

---

## Producto y marca ajena

La pregunta que llega todas las semanas: *"¿puedo generar un video con una Coca-Cola?"*

### El marco simple

Marcar la diferencia entre estas tres cosas te resuelve el 90% de los casos:

| Situación | ¿Se puede? |
|---|---|
| **Producto en el mundo, incidental.** Una lata de gaseosa en la mesa de un restaurante | Generalmente sí. Es como filmar la calle |
| **Producto como sujeto de tu anuncio, sin autorización.** Tu marca de café con una taza Starbucks protagonista | **No.** Sugiere una asociación comercial que no existe |
| **Producto de marca ajena mal representado.** Una Coca-Cola con el logo deformado, en un contexto negativo | **No, y es peor.** Suma dilución de marca y posible daño reputacional |

### El problema específico de la IA

Los modelos **no saben dibujar logos**. Van a producir un logo de Coca-Cola casi correcto, con la
tipografía casi bien y la curva casi bien. Eso es lo peor de los dos mundos: se reconoce la marca, y
se ve mal.

Los términos de servicio de la mayoría de los proveedores además te prohíben expresamente generar
marcas registradas de terceros. Es una violación de contrato antes de ser cualquier otra cosa.

### La regla operativa

> **Si la marca no es tuya y no tienes autorización escrita, prohíbela en el prompt.**

```
no brand logos, no trademarks, no recognizable product packaging, no visible brand names
```

Y si de verdad necesitas ese producto en el plano: **filma el producto real** o compón la foto real
del producto encima del fondo generado. Eso está en un terreno muy distinto y mucho más firme.

---

## Personas reales: el terreno peligroso

Aquí es donde un trabajo mal pensado deja de ser un error y pasa a ser un daño.

### Lo que está pasando legalmente

En Estados Unidos, el **NO FAKES Act** (S. 4591) avanzó por unanimidad en el Comité Judicial del
Senado el **18 de junio de 2026**. A la fecha de este módulo **no es ley todavía** —está en el pleno
del Senado— pero su dirección es inequívoca:

- crea un **derecho de propiedad intelectual sobre tu voz y tu imagen**;
- prohíbe distribuir réplicas digitales no autorizadas;
- y —esto es lo que te toca a ti— **la responsabilidad alcanza a quien encarga el trabajo y a la
  plataforma que lo publica**, no solo a quien construyó el modelo.

O sea: la marca que pide el anuncio y la agencia que lo hace pueden responder. Muchos estados de
EE.UU. ya tienen leyes propias de deepfakes y clonación de voz, y en Colombia aplican los derechos
de imagen y de datos personales que ya existían, más el Habeas Data.

### Las reglas que no se negocian

**1. Cara o voz de una persona real → autorización escrita. Siempre.**
No importa si es un empleado, un cliente feliz, tu socio o tu primo. Escrita, específica ("para uso
de IA en piezas de video"), y con alcance definido (qué piezas, qué plazo, qué medios).

**2. Persona pública sin autorización → no.**
Que sea famosa no la hace de dominio público. Al contrario: tiene más recursos para demandar.

**3. Voz clonada → autorización explícita para la clonación.**
Y con una advertencia: una autorización para "usar mi voz en el video" **no** es una autorización
para "entrenar un clon de mi voz y usarlo indefinidamente". Son dos cosas distintas y hay que
pedirlas por separado.

**4. Nunca poner palabras en la boca de alguien.**
Ni siquiera con autorización de imagen. Si vas a generar a alguien diciendo algo que nunca dijo,
necesitas autorización de **ese contenido específico**, no una autorización genérica.

**5. Menores: no. Punto.**
Ni con autorización de los padres, salvo un contexto extraordinariamente controlado y con asesoría
legal de verdad. No vale la pena. Nunca.

### La línea que no se cruza

Hay usos que no son un problema legal a resolver, sino algo que simplemente no se hace:

- material sexual de cualquier persona sin su consentimiento explícito,
- poner a alguien a decir algo que dañe su reputación,
- suplantar a una autoridad o a un medio para que la gente crea algo falso,
- material de campaña que muestre a un candidato haciendo o diciendo lo que no hizo,
- fraude: la voz clonada de un familiar pidiendo plata es un delito, no un caso creativo.

Si un cliente te pide algo de esta lista, la respuesta es no. Y no es una negociación de precio.

---

## Divulgación: cómo se hace bien

### Cuándo declarar

| Situación | ¿Declarar? |
|---|---|
| Aparece una persona sintética que parece real | **Sí, obligatorio** |
| Voz generada o clonada | **Sí, obligatorio** |
| El producto mostrado es una versión generada, no el real | **Sí** |
| Se recrea un evento o un lugar que existe | **Sí** |
| B-roll abstracto, fondos, texturas, transiciones | No hace falta |
| Corrección de color, estabilización, reducción de ruido con IA | No hace falta |
| Subtítulos generados, corte asistido por IA | No hace falta |

La línea que separa: **¿alguien podría creer que esto pasó de verdad y no pasó?** Si la respuesta es
sí, declaras.

### Cómo declarar sin arruinar la pieza

- **En el video**: una línea discreta, legible, unos segundos. "Imágenes generadas con IA" /
  "Contenido creado con inteligencia artificial". Abajo, en la tipografía de la marca, no en Arial
  amarillo.
- **En la publicación**: la etiqueta nativa de la plataforma (Meta, YouTube y TikTok la tienen).
  Úsala. Marcarla tú mismo es mucho mejor que la plataforma la detecte y te la ponga con una nota
  más fea.
- **En la descripción**: una frase al final.

Dato que la gente no espera: **declarar no penaliza el rendimiento.** El público de 2026 ya sabe qué
es la IA. Lo que sí penaliza es que te descubran ocultándolo.

---

## Datos del cliente y de terceros

Se olvida y es un problema serio:

- **No subas material sin permiso.** Si el cliente te dio grabaciones de una reunión, de una
  consulta, de un cliente suyo, tienes que saber si puedes subir eso a un servicio de un tercero.
- **Los servicios de nube guardan.** Lee la política de retención. Algunos guardan tus entradas
  para revisión de abuso durante un tiempo.
- **Datos personales en el video.** Caras de gente que no dio permiso, placas, direcciones, papeles
  con cédulas. Eso hay que desenfocarlo antes, no después.
- **Datos de salud, de menores, financieros.** Nivel de cuidado mucho más alto. Si el material los
  contiene, pregunta antes de subir.

---

## Derechos de lo que sale

La pregunta del cliente: *"¿el video es mío?"*

Honestamente, es un terreno con más incertidumbre de la que a la gente le gusta admitir:

- **Los términos del proveedor** normalmente te dan derechos de uso comercial de lo generado (Google
  y la mayoría de las plataformas grandes). **Léelos** para el proveedor que uses; no todos son
  iguales y cambian.
- **Registro de derechos de autor**: en varias jurisdicciones, incluido EE.UU., el contenido
  puramente generado por máquina no es registrable por falta de autoría humana. Lo que sí es
  registrable es **tu montaje**: la selección, la disposición, el corte y todo lo humano que le
  pusiste encima.
- **La exclusividad no existe.** Otro puede generar algo muy parecido. Eso no es un defecto del
  proveedor; es la naturaleza de la herramienta.
- **Hay litigios abiertos** en el sector sobre el material con el que se entrenaron los modelos,
  especialmente en música. No sé cómo terminan. Nadie lo sabe.

Lo que le dices al cliente: *"puedes usarlo comercialmente según los términos del proveedor; la
pieza como montaje es tuya; la exclusividad absoluta no te la puede garantizar nadie con esta
tecnología."* Eso es verdad y es defendible.

---

## Errores comunes

- **No declarar.** Cuesta nada, y que te descubran ocultándolo cuesta la confianza del público y
  posiblemente la cuenta.
- **Creer que el EU AI Act no te aplica porque estás en Colombia.** Si el cliente vende a Europa, le
  aplica. Y las plataformas ya lo exigen igual.
- **Confundir C2PA con SynthID.** Uno son metadatos frágiles, el otro está en los píxeles.
- **Prometer C2PA de extremo a extremo sin verificarlo.** Tu propia recodificación destruye la firma.
- **Intentar quitar la marca de agua.** Además de ser exactamente la señal equivocada, SynthID está
  en los píxeles y sobrevive a casi todo.
- **Generar productos de marca ajena.** Los modelos hacen logos casi correctos, que es lo peor
  posible, y suele violar los términos del proveedor.
- **Usar la cara de alguien sin autorización escrita.** Incluye empleados, clientes y familiares.
- **Confundir autorización de imagen con autorización para clonar la voz.** Son dos permisos
  distintos.
- **Poner palabras en la boca de alguien** amparado en una autorización genérica.
- **Trabajar con menores.** No.
- **Subir material del cliente sin saber si se puede.** Grabaciones de reuniones, consultas,
  historias clínicas.
- **No desenfocar caras, placas y documentos** antes de subir el bruto a un servicio.
- **Prometerle exclusividad al cliente.** No existe con esta tecnología.
- **Decirle al cliente que "la IA es legal, tranquilo".** El terreno se está escribiendo. Sé honesto
  sobre lo que no sabes.

---

## Checklist

- [ ] Sé si la pieza llega a **público europeo** (si sí: marca de máquina + divulgación visible)
- [ ] Marqué la etiqueta nativa de **contenido generado por IA** en la plataforma
- [ ] Si alguien podría creer que esto pasó de verdad, **hay divulgación visible** en la pieza
- [ ] La divulgación está en la tipografía de la marca y es legible, no escondida
- [ ] **Ninguna marca registrada ajena** aparece generada; el prompt la prohíbe explícitamente
- [ ] Si el producto de un tercero era necesario, se usó **material real**, no generado
- [ ] Toda persona real que aparece tiene **autorización escrita y específica** para uso de IA
- [ ] Si hay voz clonada, la autorización cubre **la clonación**, no solo el uso de la voz
- [ ] Nadie dice en la pieza algo que no dijo en la realidad
- [ ] **No hay menores**
- [ ] Verifiqué que puedo **subir el material del cliente** a servicios de terceros
- [ ] Desenfoqué caras de terceros, placas y documentos antes de subir
- [ ] Leí los **términos de uso comercial** del proveedor que estoy usando
- [ ] Le expliqué al cliente qué puede y qué **no** puede esperar en materia de derechos y
      exclusividad
- [ ] Si el riesgo es alto (campaña grande, persona pública, sector regulado), **hay un abogado**
