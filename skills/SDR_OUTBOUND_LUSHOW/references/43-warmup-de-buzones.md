# 43 — Warmup de buzones

**Warmup** (calentamiento) = simular actividad de correo real y creciente en un buzón nuevo para que los proveedores (Gmail, Outlook) construyan reputación positiva de él **antes** de que empiece a mandar outbound en frío. Importa porque un buzón recién creado y autenticado (ver `42`) todavía tiene reputación neutra-baja: si el día uno le mandas 40 correos fríos, Gmail ve "cuenta nueva disparando volumen a desconocidos" = patrón clásico de spam = te hunde antes de empezar. El warmup es la rampa que convierte un buzón nuevo y frágil en uno confiable. **No es opcional y no se puede saltar:** es la diferencia entre llegar a bandeja o a spam durante los próximos meses.

## La mecánica: cómo el warmup construye reputación

Los proveedores confían en cuentas que se comportan como humanos reales: mandan pocos correos, la gente los abre, los responde, los saca de spam, los marca como importantes. El warmup **fabrica ese comportamiento a escala** usando una red de buzones que se escriben entre sí automáticamente:

1. Tu buzón manda correos a otros buzones de la red del warmup.
2. Esos buzones **abren** tu correo, **responden**, y si tu correo cayó en spam, lo **sacan de spam y lo marcan "no es spam"** (la señal más poderosa).
3. Tu buzón también recibe y responde correos de la red.
4. Con el tiempo, Gmail/Outlook ven un buzón con alto engagement positivo y **suben su reputación**.

Esa última señal —sacar de spam y marcar "no es spam"— es oro: le enseña activamente al proveedor que tus correos son deseados. Ningún truco de copy reemplaza esto.

## Cuánto tiempo: 2 a 4 semanas

Un buzón nuevo necesita **mínimo 2 semanas, idealmente 3–4** de warmup antes de mandar outbound real. Y aquí está la clave que casi todos ignoran: **el warmup no se apaga cuando empiezas a enviar.** Lo dejas corriendo en paralelo, para siempre, a menor intensidad, como mantenimiento de reputación. Un buzón que envía outbound sin warmup de fondo se va degradando.

## La rampa: día por día

La regla es **empezar bajísimo y subir gradual**. No pases de 2 a 40 de golpe. Rampa típica de warmup (correos de warmup por buzón/día):

| Semana | Warmup/día | Outbound real/día | Nota |
|---|---|---|---|
| 1 | 5 → 15 (sube ~2/día) | 0 | Solo warmup. Ni un correo frío. |
| 2 | 15 → 25 | 0 | Sigue solo warmup. |
| 3 | 25 → 30 | empieza 5–10 | Introduces outbound de a poco |
| 4 | 30 (mantiene) | 10 → 20 | Sigues subiendo outbound |
| 5+ | 20–30 warmup de fondo (siempre) | 30–40 | Régimen normal (ver `44`) |

La suma warmup + outbound de un buzón sano se mantiene en un rango razonable (~40–70/día); no lo revientes.

## Cómo se hace: las herramientas

Nadie hace warmup a mano. Las plataformas de outbound modernas traen warmup automático integrado — enciendes un switch y la red hace todo. Comparativa 2026:

| Herramienta | Warmup | Precio aprox. | Nota |
|---|---|---|---|
| **Instantly** | Incluido, ilimitado en planes de pago | desde ~$37/mes | El más popular para arrancar; warmup + envío en una sola plataforma |
| **Smartlead** | Incluido, ilimitado | desde ~$39/mes | Muy fuerte en deliverability y rotación (ver `44`) |
| **Lemlist** | Incluido (lemwarm) | desde ~$55/mes | Bueno si ya usas Lemlist para cadencias |
| **Warmbox / Mailwarm / Warmup Inbox** | Solo warmup, standalone | ~$15–40/mes | Si tu plataforma de envío no trae warmup |

Recomendación práctica para Lushows: **Instantly o Smartlead** — hacen warmup Y envío en el mismo lugar, así no manejas dos herramientas. Conectas tus buzones (ver `41`), activas warmup, esperas 2–4 semanas, y recién ahí cargas tu primera campaña.

## Configuración recomendada del warmup

Dentro de la herramienta hay ajustes; estos son los sanos:

```
Correos de warmup por día:        empieza en 5, incremento diario +2, tope 30-40
Tasa de respuesta del warmup:     30-50% (la red responde ~1 de cada 3)
Rescate de spam:                  ACTIVADO (saca de spam y marca "no es spam")
Marcar como importante:           ACTIVADO
Días activos:                     lun-vie (los humanos no mandan masivo el domingo)
Warmup de fondo tras lanzar:      NO apagar nunca — dejar ~20-30/día
```

## Cómo saber si el buzón ya está listo

No adivines por el calendario; **mide**:

- La herramienta te muestra un **health score** / warmup score — apunta a **>90%** o "verde" antes de enviar real.
- Manda un correo de prueba a **Mail-Tester** (ver `42`): debe dar 9–10/10 y no caer en spam.
- Revisa que los correos de warmup estén llegando a **Primary/Principal**, no a Promociones.

Si a las 3 semanas el score sigue bajo o caes en spam, algo más está mal: revisa autenticación (ver `42`) o el dominio (ver `41`) antes de forzar volumen.

## Errores comunes (qué NO hacer)

- **Saltarse el warmup** "porque tengo prisa". Es la causa nº1 de campañas que nacen en spam. Las 2–4 semanas no se negocian.
- Empezar outbound real en semana 1. Mata el buzón nuevo.
- **Apagar el warmup** al lanzar campañas. Déjalo de fondo para siempre.
- Subir la rampa demasiado rápido (de 5 a 40 en tres días): parece spam y arruina el warmup.
- Calentar y luego mandar 100/día. El warmup te da derecho a ~40/día (ver `44`), no a volumen ilimitado.

## Siguiente paso

Con los buzones calientes (>90% health), pasa a `44`: cuántos correos por buzón puedes mandar sin quemarlo, y cómo rotar entre buzones para escalar volumen. Para verificar deliverability en marcha, `46`. Para técnicas avanzadas de warmup y recuperación de reputación de buzones quemados, ver `110`–`119`.
