# 90 — Construir el playbook

El playbook de outbound es el documento único que convierte tu sistema de conseguir clientes en algo **repetible, enseñable y auditable**. Sin él, todo lo que sabes vive en tu cabeza: cuando contratas al primer SDR (ver `85`), cuando quieres delegar, o cuando una campaña deja de funcionar y no sabes qué cambió, no hay nada a qué volver. El playbook es la diferencia entre "yo consigo reuniones" y "tenemos una máquina que consigue reuniones". Este módulo te da la **estructura exacta del documento**: qué secciones lleva, qué va en cada una y cómo mantenerlo vivo. No es un manifiesto bonito que nadie lee; es el manual operativo que un SDR nuevo abre el lunes por la mañana para saber qué hacer.

## El principio: escribir el sistema lo obliga a ser un sistema

Documentar fuerza rigor. En el momento en que tienes que escribir "nuestro ICP es X", te das cuenta de si de verdad lo tienes claro (ver `10`). Un playbook cumple tres funciones: **onboarding** (un SDR nuevo llega a productividad en semanas, no meses; ver `86`), **consistencia** (todos mandan mensajes de la misma calidad, no cada quien improvisa) y **mejora** (cuando algo se rompe, comparas contra lo escrito y ves qué cambiar; ver `83`). La regla: **si no está en el playbook, no es un proceso — es una costumbre tuya que se pierde el día que no estés.**

## La estructura del documento (11 secciones)

Ordena el playbook de arriba (estrategia) hacia abajo (ejecución diaria). Un SDR nuevo lo lee completo una vez; después vive en las secciones 4–8.

| # | Sección | Qué contiene | Módulo fuente |
|---|---|---|---|
| 1 | **Contexto y oferta** | Qué vendemos, ticket, ciclo de venta, a quién ayuda y cómo | `18`, oferta real |
| 2 | **ICP y personas** | Perfil de cliente ideal escrito, buyer personas, quién NO es ICP | `10`, `11` |
| 3 | **Segmentos y tiers** | Nichos objetivo, criterios de tier A/B/C, dónde va el mejor tiempo | `12`, `16` |
| 4 | **Fuentes de lista y datos** | De dónde salen las cuentas y contactos, filtros exactos, herramientas | `21`–`27` |
| 5 | **Infraestructura de envío** | Dominios, buzones, límites por buzón/día, estado del warmup | `41`, `43`, `44` |
| 6 | **Mensajería** | Plantillas aprobadas de email/LinkedIn/WhatsApp, asuntos, variables | `50`–`59` |
| 7 | **Cadencias** | La secuencia día-por-día, canales, número de toques | `60`, `61` |
| 8 | **Manejo de respuestas** | Qué responder a positivas/neutras/objeciones; cuándo agendar | `64`, `68` |
| 9 | **Calificación y handoff** | Criterio SQL, qué se le pasa al vendedor y cómo | `70`, `72`, `73` |
| 10 | **Métricas y metas** | Números objetivo por etapa, cómo se reportan, cadencia de revisión | `80`, `81` |
| 11 | **Herramientas y accesos** | Stack completo, logins, quién administra qué | `30` |

## Cómo llenar cada sección (lo accionable)

- **Contexto/oferta:** una página. Producto, precio, para quién es, la promesa en una frase, los 3 casos de uso más comunes. Si el negocio/pricing todavía no está resuelto → `economist_lushows`.
- **ICP:** no una descripción vaga. Firmographics exactos (tamaño, sector, país), technographics si aplica, y una lista de "señales de que NO es ICP". Copia el formato de `10`.
- **Fuentes y datos:** aquí va el oro operativo. El **filtro literal** de Sales Navigator o Apollo, no "buscamos empresas de logística". Ejemplo abajo.
- **Mensajería:** cada plantilla con su nombre, cuándo se usa, y las variables que se personalizan. Marca cuáles están "aprobadas" (probadas) vs "en prueba" (A/B; ver `65`).
- **Cadencias:** una tabla día-por-día. Un SDR debe poder ejecutarla sin preguntar nada.
- **Métricas:** los números objetivo (reply rate meta, reuniones/mes por SDR) y dónde se ven. Que sean defendibles → verifícalos con `Matematicas_lushows` (ver `05`).

## Ejemplo: fragmento de la sección 4 (fuentes de lista)

```
FUENTE PRINCIPAL — cuentas
Herramienta: LinkedIn Sales Navigator + Apollo
Filtro Sales Nav (tier A):
  Industry: Logistics & Supply Chain, Transportation/Trucking/Railroad
  Headcount: 51–200
  Geography: Colombia
  Job title (decisor): "Gerente de Operaciones" OR "COO" OR "Director Logística"
Señal de priorización: publicó vacante de operaciones últimos 30 días (ver 14)
Cadencia de refresco: lista nueva cada lunes, 40 cuentas
Verificación de correo: NeverBounce antes de cargar a Instantly (ver 28)
Responsable: [SDR]
```

## Formato y mantenimiento

- **Un solo lugar, editable:** Google Doc, Notion o similar. No un PDF muerto. El PDF es para presentar/entregar (ver `99`); el vivo se edita.
- **Fecha de última revisión en cada sección.** Un playbook sin fechas miente.
- **Ritual de actualización:** revisión mensual. Lo que cambió en la campaña se refleja aquí ese mismo día, no "cuando haya tiempo".
- **Versiona las plantillas:** cuando un A/B gana, la nueva plantilla entra al playbook y la vieja se archiva con la fecha (ver `65`).

## Errores comunes (qué NO hacer)

- Escribir un playbook filosófico de 40 páginas que nadie abre. Es un manual operativo, no un ensayo.
- Dejarlo desactualizado: un playbook que miente es peor que ninguno, porque el SDR nuevo ejecuta lo viejo.
- Poner solo teoría ("personaliza tus correos") sin los artefactos exactos (el filtro, la plantilla, la cadencia).
- Meter el CIERRE y la negociación aquí. Eso es oficio de conversación → vive en `ventas_lushows`. El playbook llega hasta agendar y el handoff.

## Siguiente paso

Arma el esqueleto con las 11 secciones vacías hoy y llena primero las 2–4 (ICP, segmentos, fuentes): son las que más rápido pagan. Para adaptarlo a tu tipo de negocio ver `91` (SaaS), `92` (servicios) o `93` (pymes LatAm). Para convertirlo en entregable presentable en PDF ver `99`.
