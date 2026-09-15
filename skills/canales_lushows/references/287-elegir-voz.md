# 287 · Elegir voz

**Qué resuelve:** la voz es el 70% de la calidad percibida del episodio y, a la vez,
**la decisión más cara del pipeline** — no por dinero, sino porque cambiarla obliga a
rehacer las fases 3 a 7 de todo lo que venga después. Y hay un motivo abierto para
tener que cambiarla: **no está claro que `edge-tts` pueda usarse comercialmente.**

> El marco de derechos —los dos frentes, motor y semejanza— está en § `136`. Este módulo
> es la **decisión operativa**: qué voz, con qué licencia, a qué coste y cómo se migra.

---

## 🔴 El riesgo abierto, dicho entero

`edge-tts` no es una API oficial de Microsoft. Es un cliente no oficial del servicio de
«Leer en voz alta» de Edge (el propio mantenedor precisa que **no va contra Azure sino
contra la Bing Speech Platform**). El paquete es libre; el servicio del otro lado, no.

**Lo que se ha encontrado, con fuente y fecha:**

| Fuente | Qué dice |
|---|---|
| Microsoft Q&A, respuesta de moderación del **22-jun-2026** | «*at present, there isn't any public documentation that explicitly addresses commercial usage rights for Edge Read Aloud voices or edge-tts*». Y remite a soporte y a Legal para obtener certeza |
| Mantenedor de `edge-tts`, discusión #261 | «*This library is absolutely not reliable and could stop working at any moment*» · «*You shouldn't have your business rely on something this risky*» · «*You're making profit from a service that isn't cheap to replicate*». Declara que es para uso personal y se plantea añadir un aviso contra el uso comercial |
| `LICENSE` del repositorio | GPL-3.0: cubre **el código**, no el servicio |
| `README` del repositorio (consultado hoy) | **No lleva aviso sobre uso comercial** |

**Conclusión honesta: ni autorización expresa ni prohibición expresa.** Un canal
monetizado es uso comercial desde el primer día, así que esto es una **deuda conocida**,
no un asunto cerrado. Y hay un segundo riesgo que no es legal sino de ingeniería, y lo
dice el propio autor: el servicio puede dejar de funcionar cualquier martes.

## Las alternativas, con su licencia

| Motor | Licencia / condiciones | Español | Coste | Veredicto |
|---|---|---|---|---|
| **`edge-tts`** | GPL-3.0 el código; **servicio sin autorización comercial documentada** | Sí, `es-MX-JorgeNeural` | $0 | 🔴 Deuda abierta |
| **Azure AI Speech** | Servicio oficial de pago, uso comercial contemplado en el contrato | **La misma voz `es-MX-JorgeNeural`** | 0,5 M caracteres/mes gratis; ≈16 USD/millón después | 🟢 **La salida limpia** |
| **Kokoro** (82 M parámetros) | **Apache-2.0**, auto-hospedable | Sí | $0 + tu máquina | 🟢 Si se acepta cambiar de timbre |
| **Chatterbox Multilingual** (Resemble AI) | **MIT**, auto-hospedable, marca de agua incrustada | Sí, 23 idiomas | $0 + GPU | 🟢 Clona voces: ojo con § `136` |
| **Piper** | El motor pasó de MIT (repo archivado) a **GPL-3.0**; **cada voz lleva licencia propia** | Sí | $0, corre en CPU | 🟡 Hay que leer la licencia de **cada** voz |
| **Coqui XTTS-v2** | **CPML: no comercial** | Sí | $0 | 🔴 Descartado para un canal monetizado |
| ElevenLabs · OpenAI · Google · Polly | De pago, uso comercial en los planes de pago | Sí | Variable | 🟡 Válido, pero es cambiar de voz y de factura |

⚠️ Las licencias cambian. Lo anterior es lo encontrado **hoy**; antes de apoyarse en
cualquiera de esas filas hay que abrir el `LICENSE` y guardarlo en PDF con fecha (§ `136`).

## La salida que no cuesta el timbre: Azure con la misma voz

`es-MX-JorgeNeural` **está en el catálogo oficial de Azure AI Speech**. Eso convierte lo
que parecía un cambio de voz en un cambio de transporte: mismo modelo, mismo timbre,
mismos `rate` y `pitch` por SSML. La cuenta:

| | |
|---|---|
| Guion de 10 min (≈1.470 palabras) | **≈8.400 caracteres** (medido: 5,6-6,1 car./palabra en el piloto) |
| Capa gratuita de Azure | 0,5 M caracteres/mes → **≈59 episodios/mes gratis** |
| Si se pasa de ahí | ≈**0,14 USD por episodio** a 16 USD/millón |

**La capa gratuita sola cubre el canal.** El «coste de producción $0» sigue en pie
después de migrar: lo que se pierde no es dinero, es el «sin API key».

> ⚠️ El precio por millón viene de fuentes secundarias: la página oficial muestra el
> importe sólo en la calculadora. Lo verificado directamente en Microsoft es **la capa
> gratuita de 0,5 M caracteres/mes** y que la voz está en el catálogo. Antes de
> presupuestar, confirmar el precio en la calculadora de la región.

## Cómo se decide, y cuándo

**La ventana para decidir esto es ahora, con un piloto.** El coste de migrar crece con el
catálogo: cada episodio publicado con una voz es un episodio que, si se cambia, suena
distinto del siguiente. Y como el motor nuevo no dará exactamente 147 ppm, **todo
episodio futuro se recalibra** (§ `281`) — los publicados se quedan como están.

| Situación | Qué hacer |
|---|---|
| Canal sin monetizar, en pruebas | `edge-tts` vale. Anotar la deuda con fecha |
| **Antes de activar la monetización** | Migrar a un motor con licencia clara. Es el punto de no retorno |
| Se quiere conservar el timbre exacto | Azure AI Speech con `es-MX-JorgeNeural` |
| Se quiere seguir sin depender de nadie | Kokoro (Apache-2.0) o Chatterbox (MIT), auto-hospedados |
| Se piensa clonar una voz humana | Parar y leer § `136`: es otro problema, y más serio |

Y una cosa que no se hace: **preguntarle a un modelo de lenguaje si esto es legal**. Se
lee el contrato y se guarda con fecha, o se escribe a Microsoft Legal — que es
exactamente lo que la propia respuesta de Microsoft recomienda.

## Si se cambia de motor: lo que hay que rehacer

| Fase | Qué pasa |
|---|---|
| 3 · Voz | Nuevo `rate`, calibrado a 145-150 ppm con el motor nuevo |
| 4 · Tiempos | `tiempos.py` sigue valiendo: mide silencios, no depende del motor |
| 5-7 | Todas las anclas del episodio, recalculadas |
| Mezcla | La cadena de § `286` se recalibra: otro motor entrega otro nivel y otro LRA |
| Idiomas | Las seis pistas de § `88`, otra vez |

Lo único que **no** cambia es el método: alineación por silencios y sílabas, relieve
construido, anclas por palabra. Eso es del canal, no del motor.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Dar por hecho que «gratis» significa «permitido» | Un canal monetizado es uso comercial desde el primer día |
| Confundir la licencia del paquete con los términos del servicio | GPL-3.0 cubre el código; no dice nada del servicio remoto |
| Aplazar la decisión hasta tener veinte episodios | El coste de migrar crece con el catálogo |
| Cambiar de motor sin recalibrar las ppm | Los huecos del guion dejan de cuadrar |
| Elegir un motor sin abrir su `LICENSE` | XTTS-v2 parece libre y es **no comercial** |
| Usar Piper asumiendo que las voces son libres | Cada voz lleva licencia propia |
| Clonar una voz humana «de referencia» | Es el frente 2 de § `136`, y no se resuelve con licencias de software |
| Confiar en un servicio que su autor llama poco fiable | Puede caerse el día del estreno |

## Relacionado

`136` voz generada y derechos · `281` ritmo en ppm · `284` una sola pasada ·
`286` la cadena de proceso · `88` sonido por idioma · `87` voz a fondo ·
`139` la lista de lo que nunca entra

**Fuentes:** [Microsoft Q&A · 22-jun-2026](https://learn.microsoft.com/en-au/answers/questions/5925556/commercial-use-of-edge-read-aloud-voices-via-edge) ·
[Microsoft Q&A · edge-tts y uso comercial](https://learn.microsoft.com/en-us/answers/questions/2088770/are-opensource-edge-tts-free-for-commercial-use) ·
[rany2/edge-tts · Discussion #261](https://github.com/rany2/edge-tts/discussions/261) ·
[Azure AI Speech · precios y capa gratuita](https://azure.microsoft.com/en-us/pricing/details/cognitive-services/speech-services/) ·
[Azure AI Speech · catálogo de voces](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts)
