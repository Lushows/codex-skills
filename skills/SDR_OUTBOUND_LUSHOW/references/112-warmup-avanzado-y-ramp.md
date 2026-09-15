# 112 — Warmup avanzado y rampa de volumen

El Bloque 4 te enseñó a calentar un buzón nuevo (ver `43`). Este módulo es el nivel de flota: **cómo calientas y subes el volumen de decenas de buzones a la vez sin quemar ninguno, cómo diseñas la rampa (ramp-up) por semanas, y cómo mantienes la reputación cuando ya estás enviando en serio.** A escala, el warmup deja de ser "enciendo un switch en un buzón" y se vuelve una operación continua: siempre hay buzones calentándose, otros en rampa, otros en régimen, y otros jubilándose. La diferencia entre una flota que crece sana y una que se cae en cadena es la disciplina de la rampa: **nunca pides a un buzón más de lo que su edad y reputación aguantan.**

## El principio: la reputación se construye lento y se destruye rápido

Los proveedores (Gmail, Outlook) miden un buzón por su **historial de comportamiento**. Un buzón nuevo que dispara volumen = patrón de spam = hundido. La rampa fabrica un historial creíble: volumen bajo que sube gradual, con engagement positivo (respuestas, rescate de spam; ver `43`). A nivel avanzado sumas dos ideas:

1. **El warmup nunca se apaga.** Cuando el buzón entra a producción, dejas warmup de fondo (~20–30/día) para siempre, como mantenimiento. Un buzón que envía outbound sin warmup de fondo se degrada solo.
2. **La rampa aplica a la flota, no a un buzón.** Escalas capacidad total metiendo buzones en oleadas, cada oleada en su propia rampa, con un colchón siempre calentándose.

## La rampa por buzón: calendario día a día

Regla base: empieza bajísimo, sube ~5–10% de volumen real por semana, nunca dobles de golpe. Rampa madura de un buzón (warmup + outbound real):

| Semana | Warmup/día | Outbound real/día | Total | Nota |
|---|---|---|---|---|
| 1 | 5 → 15 | 0 | ≤15 | Solo warmup. Ni un frío |
| 2 | 15 → 25 | 0 | ≤25 | Solo warmup |
| 3 | 25 → 30 | 5 → 10 | ~35–40 | Introduces outbound de a poco |
| 4 | 30 | 10 → 20 | ~40–50 | Subes outbound, warmup estable |
| 5 | 25 | 20 → 30 | ~50 | Casi en régimen |
| 6+ | 20–25 (fondo) | 30–40 | ~50–65 | Régimen normal (ver `44`) |

La suma warmup+outbound de un buzón sano se queda en ~50–65/día. **No lo revientes** porque "ya está caliente": el warmup te da derecho a ~40/día de outbound, no a volumen ilimitado.

## La rampa de la flota: oleadas y colchón

Para escalar de, digamos, 300 a 1.000 correos/día sin caída en cadena:

```
OLEADA 1 (hoy):        10 buzones → warmup 4 semanas → producción semana 5
OLEADA 2 (semana 3):   10 buzones → warmup 4 semanas → producción semana 7
OLEADA 3 (semana 5):   10 buzones → warmup 4 semanas → producción semana 9
COLCHÓN permanente:    ~15-20% de buzones extra siempre en warmup, listos para reemplazar caídos
```

Reglas de la rampa de flota:

- **Solapa las oleadas** (empieza la siguiente antes de que termine la anterior) para que la capacidad suba de forma continua, no a saltos.
- **Nunca metas toda la flota nueva a producción la misma semana:** si algo está mal (autenticación, dominio), lo descubres con 10 buzones, no con 40.
- **Mantén el colchón caliente.** Cuando un buzón se degrade (ver `113`), lo jubilas y activas uno del colchón — capacidad estable sin bajón.

## Warmup avanzado: ajustes que casi nadie toca

Dentro de Instantly/Smartlead (ver `43`, `33`) hay palancas finas que a escala importan:

```
Warmup/día por buzón:         5 → +2/día → tope 25-35 (no 40+; deja margen para outbound)
Tasa de respuesta warmup:     30-45% (más natural que 50%+; una red que responde el 60% se ve artificial)
Rescate de spam:              ACTIVADO (sacar de spam + "no es spam" = señal nº1)
Marcar importante / responder hilo: ACTIVADO
Días activos:                 lun-vie; simula pausa de fin de semana
Rampa de outbound:            +5-10/día por semana, NUNCA doblar de un día a otro
Warmup de fondo tras lanzar:  20-30/día, permanente
```

- **No uses la misma red de warmup para toda la flota masiva.** Redes de warmup saturadas (muchos usuarios mandándose entre sí los mismos patrones) pierden valor; algunos proveedores serios rotan pools. A gran volumen, complementa con **envíos reales a listas semilla propias** (buzones tuyos en Gmail/Outlook/Yahoo que abren y responden) — engagement 100% real.
- **Warmup ≠ permiso de volumen.** Un buzón con warmup score verde a 95% sigue limitado a ~40 fríos/día. El score dice "tu reputación está sana", no "manda lo que quieras".

## Cómo saber si la rampa va bien (mide, no adivines)

| Señal | Sano | Alarma → acción |
|---|---|---|
| Warmup / health score | > 90% verde | < 80% → pausa outbound, refuerza warmup |
| Mail-Tester (ver `116`) | 9–10/10 | < 8 → revisa autenticación (`42`) o dominio (`41`) |
| Warmup llegando a Primary | Sí | Cae a Promociones/Spam → problema; no subas volumen |
| Bounce rate al introducir outbound | < 2% | > 4% → lista sucia, detén (ver `114`) |
| Domain reputation en Postmaster | Media/Alta | Baja → frena rampa, diagnostica (ver `113`) |

Si a las 3–4 semanas el score no sube o caes en spam, **el problema no es tiempo**: es autenticación, dominio o red de warmup saturada. No fuerces volumen encima de un buzón que no calentó bien — lo entierras.

## Errores comunes (qué NO hacer)

- Meter toda la flota a producción la misma semana (sin oleadas). Un error se multiplica por 40.
- Subir volumen doblando de golpe ("de 10 a 40 en tres días"): patrón de spam, arruina el warmup.
- Apagar el warmup al lanzar campañas. Déjalo de fondo para siempre.
- No tener colchón: cuando un buzón cae, bajas capacidad y tardas 4 semanas en reponerla.
- Confundir warmup score verde con permiso de volumen. El límite por buzón (ver `44`) manda siempre.
- Redes de warmup saturadas como única fuente de engagement: complementa con listas semilla reales.

## Siguiente paso

Con la flota calentándose en oleadas, necesitas leer la reputación real que Google te devuelve para pilotar todo esto: ve a `113` (Google Postmaster y monitoreo a escala). Si un dominio ya cayó pese a la rampa, ve a `114` (blacklists) y `117` (recuperar dominio quemado). Los fundamentos del warmup están en `43`; los límites de volumen en `44`. Para proyectar cuántas semanas y buzones necesitas para llegar a tu meta, `Matematicas_lushows`.
