# 166 — Integración bancaria y APIs

Cuando hablamos de que el banco "se conecta" a la contabilidad (open finance, módulo 164), por debajo lo que hay es una **API**. Una API (Interfaz de Programación de Aplicaciones) es, en cristiano, una **tubería con reglas** por la que dos programas se hablan: el banco expone unas "ventanillas" y tu software pide por ahí "dame los movimientos de esta cuenta". Este módulo explica, sin volverte ingeniero, cómo es esa conexión, cómo se mantiene al día (sincronización) y cómo se protege (seguridad). El contador no programa esto, pero **sí debe entenderlo para confiar y para auditar**.

## Cómo se conectan banco y contabilidad

| Pieza | Qué es | Por qué importa al contador |
|---|---|---|
| **API** | La tubería que comunica los sistemas | Por ahí viajan tus datos financieros |
| **Token / credencial** | La "llave" que autoriza la conexión | Si se filtra, alguien entra a tus datos |
| **Sincronización** | Traer los movimientos nuevos cada cierto tiempo | Define si tu info está al día |
| **Webhook** | Aviso automático cuando pasa algo (ej. nuevo pago) | Permite conciliar en el momento |

## Sincronización: que los datos estén al día

La conexión no es magia continua; trae datos cada cierto rato o cuando algo ocurre. Hay que entender:

- **Cada cuánto** se actualiza (¿cada hora? ¿al instante?).
- **Qué pasa si falla** una sincronización: ¿reintenta? ¿avisa? ¿se pierden movimientos?
- **Duplicados**: la integración debe evitar traer dos veces el mismo movimiento.
- **Plan B**: si la API se cae, volver a OCR del extracto (módulo 161).

## Seguridad: lo no negociable

Por la tubería viajan datos sensibles. Lo mínimo:

- **Cifrado** (los datos viajan codificados, ilegibles si los interceptan).
- **Llaves/tokens guardados con cuidado**, nunca en un correo o un Excel suelto.
- **Permisos mínimos**: la conexión solo accede a lo que necesita.
- **Registro de accesos**: quién y qué se consultó (auditabilidad, módulo 167).
- **Cumplir Habeas Data** (protección de datos personales en Colombia) — módulo 169.

## Ejemplo (cifras ILUSTRATIVAS / inventadas)

Una herramienta sincroniza la cuenta cada hora vía API. A las 2:00 p.m. entra una transferencia de $2.500.000; a las 3:00 p.m. ya está en el sistema y un webhook avisa para conciliarla. Si la API hubiera fallado, la herramienta reintenta y, si no, avisa al contador para bajar el extracto a mano. Cifras y tiempos inventados.

## Errores comunes

- **Guardar las llaves/tokens en lugares inseguros**: es como dejar la llave de la caja fuerte pegada.
- **No saber cada cuánto sincroniza**: crees que está al día y no lo está.
- **Ignorar los fallos de sincronización**: faltan movimientos y la conciliación no cuadra.
- **Dar permisos de más a la integración**: si se compromete, el daño es mayor.
- **No tener plan B** cuando la API se cae.

## Conexión con otros módulos

- El concepto de **open finance** y consentimiento: módulo **164**.
- Los datos que llegan alimentan **conciliación** (**162**) y **contabilización** (**163**); el plan B es el **OCR** (**161**).
- **Controles y registro de accesos**: módulo **167**. **Privacidad y datos sensibles**: módulo **169**.
- *Construir o evaluar técnicamente* la integración, APIs y seguridad: `engineer_visualopen_lushows`.

## Siguiente paso típico

Pídele a tu proveedor de software tres respuestas por escrito: cada cuánto sincroniza, qué pasa si la conexión falla, y cómo protege las llaves y los datos. Si no te las da claras, no es una herramienta para confiarle datos financieros.
