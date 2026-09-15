# 44 — Límites, rotación y volumen

Este módulo responde la pregunta más práctica del outbound: **¿cuántos correos puedo mandar sin quemarme, y cómo escalo el volumen sin perder deliverability?** La respuesta corta y crítica: **~30–50 correos por buzón por día**, y para mandar más no subes ese número, sino que **agregas buzones y rotas entre ellos**. Confundir "quiero mandar 1.000 correos/día" con "voy a configurar un buzón para mandar 1.000" es el error que quema más operaciones. El volumen se construye con muchos buzones pequeños, no con pocos buzones grandes. Este módulo sostiene los dominios (ver `41`) y el warmup (ver `43`); sin respetar estos límites, todo lo anterior no sirve.

## El principio: por qué ~30–50/día por buzón

Un ser humano real, en su día, no manda 200 correos personales nuevos a desconocidos. Los proveedores lo saben. Cuando un buzón dispara alto volumen a gente que no le responde, el patrón grita "spam automatizado". El límite seguro de un buzón caliente y sano en 2026 es:

- **Conservador (recomendado para empezar):** 20–30/día.
- **Estándar sostenible:** 30–40/día.
- **Máximo agresivo (solo buzón muy maduro):** 50/día.

Por encima de ~50/día por buzón, el riesgo de reputación sube fuerte y el retorno baja. **La regla de oro: mejor 10 buzones a 30 que 3 buzones a 100.** Distribuir el volumen entre muchos buzones imita comportamiento humano y aísla el riesgo (si uno se degrada, no cae toda la operación).

## La matemática del volumen

El volumen total no depende de un número mágico, sino de esta ecuación simple (para números exactos, apóyate en `Matematicas_lushows`):

```
Correos/día = número de buzones × correos por buzón/día
```

| Meta correos/día | Buzones a ~40/día | Dominios (≈3 buzones c/u; ver 41) |
|---|---|---|
| 120 | 3 | 1 |
| 240 | 6 | 2 |
| 400 | 10 | 3–4 |
| 800 | 20 | 7 |
| 1.200 | 30 | 10 |

Y esto se traduce en prospectos por mes. Ejemplo real: 9 buzones × 35 correos/día × 22 días hábiles = **~6.900 primeros toques/mes**. Con un reply rate del 5% (ver `80`), son ~345 respuestas; si el 30% son positivas, ~100 conversaciones/mes para calificar (ver `70`) y agendar. Así se dimensiona una máquina de outbound hacia atrás desde la meta de reuniones (la ecuación completa está en `05`).

## Rotación de buzones: qué es y cómo se hace

**Rotación** (inbox rotation / sending rotation) = repartir automáticamente los envíos de una campaña entre varios buzones, para que cada uno se quede en su límite diario aunque la campaña sea grande. En vez de que `luis@` mande los 400 correos, la plataforma reparte: 40 desde `luis@dom1`, 40 desde `maria@dom1`, 40 desde `ventas@dom2`, etc.

Además, cuando un prospecto responde, la conversación **sigue por el mismo buzón** que lo contactó (para no confundirlo). Todo esto lo hacen automáticamente Instantly y Smartlead: conectas todos tus buzones a una campaña y activas "inbox rotation". Tú defines el límite por buzón; la herramienta reparte.

```
Config típica de rotación (Smartlead / Instantly):
  Buzones en la campaña:        9 (de 3 dominios)
  Límite diario por buzón:      35
  Capacidad total campaña:      315/día
  Rotación:                     activada (reparte parejo)
  Min. delay entre envíos:      60-180 seg (aleatorio, imita humano)
  Ventana de envío:             9am-5pm hora del prospecto, lun-vie
```

## Cómo escalar volumen sin quemarte

Escalar = **agregar más buzones/dominios y calentarlos**, no subir el límite de los que tienes. El proceso:

1. **Nunca cargues buzón nuevo a tope.** Todo buzón nuevo entra por warmup 2–4 semanas (ver `43`) y arranca a 5–10/día real.
2. **Sube el volumen de un buzón gradual:** semana 1 a 10/día, +5–10/día cada semana hasta ~35–40.
3. **Para duplicar volumen:** compra más dominios (ver `41`), crea buzones, caliéntalos. En ~4 semanas tienes el doble de capacidad sana.
4. **Distribuye la carga:** ningún dominio con más de 3–4 buzones enviando; reparte entre dominios.

## Señales de que estás quemando (frena de inmediato)

El volumen sano se autorregula por métricas, no por sensación. Detén o baja el volumen si ves (monitoreo en `46`):

| Señal | Umbral de alarma | Acción |
|---|---|---|
| **Bounce rate** (rebotes) | > 4% | Detén la campaña, limpia la lista (ver abajo) |
| **Spam complaint rate** | > 0.3% | Baja volumen, revisa lista y copy |
| **Reply rate** cae | < 1% | No es solo copy: puede que estés en spam |
| Correos de warmup caen a spam | cualquier caída | Pausa outbound, refuerza warmup |

**Limpia la lista SIEMPRE antes de enviar:** pasa los correos por un verificador (NeverBounce, ZeroBounce, MillionVerifier — ~$0.001–0.004 por correo) para quitar los inválidos. Una lista sucia con 10% de correos muertos te dispara el bounce rate y quema los buzones en un día. Esto es innegociable (ver `23` sobre calidad de datos).

## Errores comunes (qué NO hacer)

- Configurar un buzón para mandar 100–200/día "para ir rápido". Lo quemas en días.
- Subir volumen de golpe en vez de rampa semanal.
- No limpiar la lista → bounce alto → reputación destruida (el error más común y más caro).
- Meter 8 buzones en un solo dominio para ahorrar dominios: concentra riesgo (ver `41`, mejor 3 por dominio).
- Enviar 24/7 a cualquier hora. Ventana humana (horario laboral del prospecto, lun-vie) suma deliverability y respuestas.

## Siguiente paso

Ya sabes cuánto y cómo repartir; ahora asegúrate de que el **contenido** de cada correo no te delate como spam (ver `45`: palabras spam, texto plano, links, imágenes). Y monta el monitoreo para vigilar bounce/spam rate (ver `46`). Para estrategias de volumen a gran escala y arquitectura multi-dominio avanzada, ver `110`–`119`.
