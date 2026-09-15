# 198 — El sistema replicable completo (de 0 a máquina)

Este es el **mapa entero**: el módulo que conecta cada bloque de la biblioteca en una sola ruta, de no tener nada a tener una máquina de outbound que produce pipeline predecible mes a mes. El módulo `98` dio la versión de núcleo (los 8 subsistemas, las 4 fases); este es la versión **completa y exhaustiva**, que integra también la expansión (100–189) y el bloque de agencia (190–197) en el sistema. Importa porque es fácil perderse entre 200 módulos y no ver el bosque: aquí está el bosque. Es el módulo que lees cuando quieres saber **"¿por dónde voy y qué me falta?"**. Todo lo demás es detalle de una de estas piezas.

## El principio: outbound predecible es una ecuación con procesos detrás

La diferencia entre "a veces consigo clientes" y "un negocio que crece" no es talento: es **sistema** (ver `98`). Un sistema se puede medir, mejorar, delegar y escalar. La base matemática: el pipeline sale de una cadena de conversiones calculable (ver `05`, `82`) — si sabes tus ratios (contactos→respuesta→reunión→SQL→cierre), sabes exactamente cuánta actividad necesitas para tu meta. Eso convierte "ojalá caigan clientes" en "para N clientes/mes necesito X contactos/semana". Los números exactos de tu ecuación → `Matematicas_lushows`.

## El mapa completo: los 10 subsistemas

La máquina completa tiene diez piezas. Las primeras ocho son las del núcleo (ver `98`); las dos últimas aparecen cuando conviertes la máquina en negocio.

| # | Subsistema | Qué produce | Núcleo | Expansión |
|---|---|---|---|---|
| 1 | **Targeting / ICP** | A quién y por qué | `10`–`19` | `110`–`119` |
| 2 | **Sourcing de datos** | Listas verificadas | `20`–`29` | `100`, `120`–`129` |
| 3 | **Deliverability** | Llegar a la bandeja | `40`–`49` | `140`–`149` |
| 4 | **Stack / automatización** | Herramientas conectadas | `30`–`39` | `100`, `130`–`139` |
| 5 | **Mensajería / copy** | Correos que responden | `50`–`59` | `150`–`159` |
| 6 | **Cadencias** | Secuencia que corre sola | `60`–`69` | `160`–`169` |
| 7 | **Calificación / handoff** | Reuniones calificadas | `70`–`79` | — |
| 8 | **Métricas / mejora** | Los números que guían | `80`–`89` | `144` |
| 9 | **Verticalización** | Playbook por industria | `90`–`96` | `170`–`179` |
| 10 | **Negocio / agencia** | Vender la máquina | `95` | `190`–`197` |

Si una pieza falla, la cadena se rompe (ver `196`, `97`). El sistema es tan fuerte como su eslabón más débil — casi siempre deliverability (pieza 3) o targeting (pieza 1).

## La ruta de 0 a máquina: las cinco fases

Las cuatro fases del núcleo (ver `98`) más una quinta cuando lo vuelves negocio. Saltarse una rompe la siguiente.

**Fase 0 — Fundamentos (entiende el juego).** Antes de tocar una herramienta: entiende que outbound es sistema medible, no suerte; la ecuación del pipeline; la ética y la ley (ver `00`–`09`). Muchos fracasan aquí por arrancar a mandar correos sin entender la cadena.

**Fase 1 — Manual y probado (solista).** Todo a mano: buscas cuentas (ver `20`), escribes correos uno por uno (ver `50`), agendas. El objetivo NO es escalar: es **encontrar qué funciona** (qué ICP responde, qué mensaje convierte; ver `10`, `65`). Sal de aquí cuando tienes un ICP + mensaje que sí generan reuniones. **No automatices lo que aún no funciona** (ver `35`, `66`).

**Fase 2 — Documentado (playbook).** Escribes lo que funciona (ver `90`): el filtro exacto, la plantilla ganadora, la cadencia, la config de deliverability. El sistema ahora existe fuera de tu cabeza. **Este es el paso que casi todos se saltan y por eso nunca escalan.**

**Fase 3 — Sistematizado (herramientas).** Ahora sí automatizas lo repetitivo: sourcing con Apollo/Clay (ver `100`, `31`), envío con Instantly/Smartlead (ver `33`), señales que disparan campañas (ver `37`), secuencias que corren solas (ver `39`). Tu tiempo se va a lo que solo un humano hace: relevancia y respuestas. La IA amplifica aquí (ver `35`, `197`).

**Fase 4 — Delegado / negocio (equipo o agencia).** Entregas el playbook + la máquina a un SDR (ver `85`, `86`, `89`), o la conviertes en agencia y se la vendes a otros (ver `190`–`195`). Produces pipeline sin tu tiempo. Aquí decides: ¿escalas a equipo interno o montas agencia?

```
Fase 0: entiende el juego     → fundamentos (00–09)
Fase 1: manual + probar       → ¿qué funciona? (10, 50)
Fase 2: documentar            → playbook (90)
Fase 3: automatizar           → stack + señales (39, 37)
Fase 4: delegar / vender      → equipo (89) o agencia (190)
```

## Cómo saber en qué fase estás (autodiagnóstico)

- **No entiendo por qué unos correos funcionan y otros no** → Fase 0. Estudia fundamentos (ver `05`, `40`).
- **No consigo reuniones consistentes** → Fase 1, aún sin ICP/mensaje ganador. Itera a mano, NO automatices (ver `10`, `65`).
- **Consigo reuniones pero solo yo puedo, todo vive en mi cabeza** → falta Fase 2. Documenta (ver `90`).
- **Tengo el playbook pero paso horas en tareas mecánicas** → falta Fase 3. Automatiza (ver `39`).
- **La máquina funciona y quiero más** → Fase 4: delega (ver `89`) o monta agencia (ver `190`).

## El sistema como diagrama de flujo

```
SEÑAL / ICP (1)  →  LISTA + DATOS (2)  →  [INFRA sana (3)]
      ↓                                         ↓
   COPY relevante (5)  →  CADENCIA multicanal (6)
      ↓
   RESPUESTA  →  CALIFICA (7)  →  REUNIÓN AGENDADA
      ↓                              ↓
   MÉTRICAS (8) ← miden todo    HANDOFF → CIERRE (ventas_lushows)
      ↓
   DIAGNÓSTICO (83) → mejora el eslabón débil → vuelve a empezar
```

Todo el sistema alimenta las métricas (8), que diagnostican el eslabón débil (ver `83`), que dispara la mejora, que reinicia el ciclo. Es un **loop de mejora continua**, no una línea recta. La frontera está marcada: el sistema entrega la **reunión agendada y calificada**; el cierre cruza a `ventas_lushows`.

## Errores comunes (qué NO hacer con el sistema)

- **Automatizar en Fase 1:** escalas lo que no funciona y quemas dominios (ver `98`, `196`).
- **Saltarte la documentación (Fase 2):** sin playbook no delegas ni diagnosticas; todo depende de ti.
- **Creer que comprar herramientas ES el sistema:** ejecutan el sistema, no lo reemplazan (ver `30`).
- **Optimizar un eslabón que no es el cuello de botella:** afinas el copy cuando el problema era deliverability (ver `83`).
- **Montar agencia (Fase 4) saltándote las fases 1–3:** vendes una máquina que no tienes probada (ver `190`, `192`).

## Siguiente paso

Ubícate en una fase con el autodiagnóstico y ataca lo único que te falta para pasar a la siguiente — no intentes todo a la vez. Si empiezas, tu tarea es Fase 1: un ICP y un mensaje que generen la primera reunión (ver `10`, `50`). Cuando funcione, documenta (ver `90`), luego automatiza (ver `39`), luego decide equipo o agencia (ver `89`, `190`). Para el nivel maestro y convertir cada fase en entregables presentables (PDF), `199`.
