# 165 — Agentes contables de IA

Un **agente** de IA es un escalón por encima de un asistente que solo responde: el agente **ejecuta tareas** por su cuenta, paso a paso. No solo te dice cómo conciliar, sino que entra al sistema, descarga el extracto, empareja, prepara los asientos y te deja todo listo para aprobar. En 2026 los agentes contables empiezan a hacer flujos completos. Por eso mismo hay que ser muy claro con su **alcance, sus límites y su gobierno**: un agente que ejecuta solo puede hacer daño rápido si no tiene barreras.

La promesa de la casa aplica con fuerza aquí: **CUADRE + CUMPLIMIENTO + AUDITABLE**. Un agente acelera, pero **no firma ni responde** — el contador titulado sí.

## Qué puede hacer un agente contable hoy

| Tarea del agente | Nivel de autonomía recomendado |
|---|---|
| Descargar extractos y facturas | Alta (es solo recolectar) |
| Emparejar en conciliación | Media (humano revisa excepciones) |
| Preparar asientos sugeridos | Media (humano aprueba) |
| Generar borradores de reportes | Media (humano valida cifras) |
| Presentar declaraciones / firmar | **Nunca solo** — humano obligatorio |
| Pagar o mover dinero | **Nunca solo** sin doble aprobación |

## Gobierno: las barreras del agente

Un agente sin reglas es peligroso. El **gobierno** (las reglas de cómo opera) debe definir:

- **Hasta dónde llega**: qué puede hacer y qué tiene prohibido (nunca firmar, nunca pagar solo).
- **Aprobaciones**: qué acciones requieren clic humano antes de ejecutarse.
- **Trazabilidad**: registro de cada acción (qué hizo, cuándo, con qué dato) — auditabilidad (módulo 167).
- **Botón de parada**: poder detenerlo en cualquier momento.
- **Límites de monto**: por encima de cierto valor, siempre humano.

## Ejemplo (cifras ILUSTRATIVAS / inventadas)

Un agente concilia solo hasta movimientos de $500.000; por encima, frena y pide aprobación. Una noche empareja 180 movimientos, deja 7 excepciones y se detiene ante una transferencia de $4.000.000 marcándola "requiere humano". El contador revisa en la mañana: aprueba 6, corrige 1, investiga la grande. El agente trabajó toda la noche, pero **nadie firmó nada sin un humano**. Cifras inventadas.

## Errores comunes

- **Darle autonomía total "para que ahorre tiempo"**: un error se propaga sin freno.
- **No registrar lo que hace**: sin bitácora no hay auditoría ni se puede deshacer.
- **Dejar que pague o presente sin aprobación**: jamás.
- **Confiar en sus números sin verificarlos**: pasa por `Matematicas_lushows`.
- **No tener botón de parada**: si se descarrila, hay que poder cortarlo.

## Conexión con otros módulos

- Las tareas que el agente automatiza están en **161** (leer), **162** (conciliar) y **163** (asientos).
- Los **controles, trazabilidad y aprobaciones**: módulo **167**.
- Los **riesgos** (alucinación, datos, responsabilidad de por qué firma el humano): módulo **169**.
- El agente **conversacional** que captura facturas por WhatsApp (AVIS/GASTROWHATS) vive en `AVIS_lushows`; *construir* agentes: `engineer_visualopen_lushows`.

## Siguiente paso típico

Antes de soltar un agente, escribe en una hoja sus **reglas de gobierno**: qué puede hacer solo, qué requiere aprobación, su límite de monto y cómo se detiene. Empieza con la tarea más segura (descargar documentos) y ve ampliando solo cuando los controles demuestren que funciona.
