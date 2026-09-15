# 101 — Clay avanzado

El `31` te enseñó a construir tu primera tabla en Clay (import → email → verify → Claygent → export). Este módulo es el nivel experto: **waterfalls de verdad, columnas con IA encadenadas, integraciones bidireccionales, agentes y patrones que la gente de outbound cobra caro por montar**. Aquí Clay deja de ser "un Excel con superpoderes" y se vuelve el **motor de datos que orquesta todo tu stack**: recibe señales, enriquece en cascada, decide, escribe y despacha a tu sequencer y CRM sin que toques nada.

## Waterfall de enrichment en serio (el diferenciador)

El waterfall (cascada: preguntar al proveedor 1, si falla al 2, al 3…) es *la* razón para usar Clay. Detalles que la mayoría no configura bien:

- **Ordena por costo/calidad, no al azar.** Pon primero los proveedores baratos y de alta precisión; deja los caros como último recurso. Clay solo paga por el que acierta.
- **Waterfalls por tipo de dato.** Uno para email de trabajo, otro para móvil, otro para email personal. No mezcles.
- **`Run if` en cada paso.** Solo busca móvil si NO hubo email; solo corre el proveedor caro si los baratos fallaron. Esto es lo que separa una factura de $200 de una de $2.000.
- **Cobertura esperada:** un proveedor solo cubre 40–70%; un waterfall bien armado llega a 80–90% (ver `29`). La cola que no encuentra ninguno → descártala o mándala por otro canal (LinkedIn, ver `57`).

```
Waterfall "Work Email":
  1. Proveedor barato/preciso (p.ej. datos nativos)   ── run always
  2. Segundo proveedor                                 ── run if [1] vacío
  3. Tercero                                           ── run if [1] y [2] vacíos
  4. Verificación (NeverBounce/ZeroBounce)             ── run if hay email
  → columna final: email_final (coalesce de 1/2/3, solo si "valid")
```

## Claygent encadenado y columnas de IA que deciden

Claygent (el mini-agente de IA que "navega" y responde) rinde 10x cuando encadenas columnas en lugar de pedirle todo en un prompt gigante:

1. **Columna A — recolectar:** "Visita {website}, devuelve en JSON: {especialidad, ciudad, tiene_ecommerce, ultima_noticia}."
2. **Columna B — razonar:** toma el JSON de A y clasifica: "¿encaja con nuestro ICP? Responde SI/NO/QUIZAS + razón en 6 palabras."
3. **Columna C — escribir:** solo si B = SI, redacta el opener usando el dato de A (ver `53`, `120`).

Ventajas: cada paso es barato, verificable y reutilizable; si algo falla ves *dónde*. Fuerza siempre salida estructurada y un `SIN_DATO` de escape para que la IA no alucine (ver `31`). Para bajar el costo de todos estos prompts a escala (que se multiplican por miles de filas) → `optimizer_tokens_lushows`; es donde vive la optimización de tokens, no aquí.

## Integraciones bidireccionales (Clay como hub, no como isla)

Clay puede **entrar** datos y **sacar** resultados a casi todo (ver `34`):

| Dirección | Mecanismo | Caso |
|---|---|---|
| Entrada | Import CSV, Apollo/Sales Nav, Google Maps, **webhook** | traer cuentas o recibir un lead de un form |
| Entrada | HTTP API / integración nativa | jalar de tu CRM las cuentas abiertas |
| Salida | Nativo a **Instantly/Smartlead/HubSpot/Salesforce** | mandar solo filas válidas + Tier A a la secuencia |
| Salida | **Webhook / HTTP** a n8n/Make | disparar cualquier automatización (ver `107`) |
| Ida y vuelta | Enriquecer inbound y **escribir de vuelta** al CRM | form → Clay enriquece/puntúa → CRM (ver `38`) |

El patrón pro: **Clay no reemplaza al CRM, lo alimenta.** El CRM (ver `32`) es la fuente de verdad; Clay es la fábrica que le entrega contactos limpios, enriquecidos y puntuados.

## Patrones avanzados que valen oro

- **Signal-based lists (outbound por señal).** Una tabla cuya fuente son señales: empresas que contratan cierto rol, que recaudaron ronda, que cambiaron de web. Clay las enriquece y las despacha en caliente (ver `14`, `37`). Ejemplo: "restaurantes que abrieron sede nueva este mes" → mensaje con timing perfecto.
- **Lookalike / clonar clientes buenos.** Tomas tus 20 mejores clientes, Clay extrae su patrón (firmographics + technographics) y busca gemelos (ver `15`, `19`).
- **Scoring compuesto.** Fórmula que combina firmographics + technographics + intent en un puntaje 0–100 y rutea Tier A/B/C (ver `16`, `38`).
- **De-dup contra CRM.** Antes de exportar, columna que consulta el CRM y descarta lo que ya existe → cero duplicados y cero pisar cuentas de un compañero (ver `77`).
- **Tablas encadenadas (table → table).** La salida "cuentas calificadas" de una tabla es la **fuente** de otra tabla de "contactos dentro de esas cuentas". Separa cuenta de contacto (ver `22`).

## Ejemplo real: máquina de inbound enriquecido

```
Trigger: alguien llena el form de la landing
  → Webhook a Clay (tabla "Inbound")
  → Waterfall: dominio del email corporativo → datos de empresa
  → Claygent: clasifica industria + tamaño + fit ICP
  → Fórmula: score 0–100 (ver 38)
  → Run if score ≥ 70: write-back a HubSpot como MQL + Slack al SDR
  → Run if score < 70: nurture / descartar (ver 76)
Resultado: el SDR solo ve leads calientes, ya enriquecidos, en segundos.
```

## Costo y control (Clay se dispara si no lo cuidas)

Clay cobra por **créditos** (cada enrichment/llamada de IA gasta). En avanzado el riesgo es multiplicar columnas caras por miles de filas.

- **Filtra ANTES de enriquecer.** Corre las columnas caras solo sobre las filas que ya pasaron un primer filtro barato.
- **`Run if` en todo lo que cuesta.** Es la palanca #1 de ahorro.
- **Prueba con 25 filas** cada nueva columna; mira el gasto; recién ahí escala.
- **Precio 2026 (aprox):** planes desde ~$149/mes hasta Pro/Enterprise de varios cientos; los créditos se agotan rápido en waterfalls agresivos. Estima tu volumen con `Matematicas_lushows`.

## Errores comunes

- **Waterfall sin orden ni `run if`** → factura enorme por datos que un proveedor barato ya tenía.
- **Un mega-prompt de Claygent** que hace 5 cosas → imposible de depurar y alucina. Encadena.
- **Exportar sin verificar** el email final (ver `28`) → rebotes que queman deliverability (ver `45`).
- **Usar Clay como CRM.** Es una fábrica de datos, no el sistema de registro. Escribe de vuelta al CRM (`32`).

## Siguiente paso

Reconstruye tu tabla del `31` con waterfall ordenado + `run if` + Claygent encadenado, y conéctala por integración/webhook (`34`, `107`) a tu sequencer (`33`, `103`, `104`) y CRM (`32`). Para señales que la alimenten → `37`; para el scoring → `38`; para no reventar el costo de IA → `optimizer_tokens_lushows`.
