# 199 — Maestría y entregables (nivel maestro + producción en PDF)

Este es el módulo que cierra la biblioteca entera (00–199). El `99` cerró el núcleo con el camino del principiante al maestro y cómo sacar un entregable en PDF; este es la **versión completa a escala de agencia**: qué distingue el nivel maestro cuando ya operas una máquina (o varias), y **cómo producir todos los entregables del oficio** —playbook completo, listas, secuencias, propuestas, dashboards— como documentos presentables en PDF, listos para usar, presentar o venderle a un cliente. Importa porque el valor de dominar el outbound no está en lo que sabes: está en lo que **produces**. Un consejo se olvida; un playbook en PDF se ejecuta, un dashboard se revisa cada semana, una propuesta cierra un cliente. La frontera del maestro también es clara: produce la máquina que agenda; el **cierre y la negociación** siguen siendo `ventas_lushows`.

## El principio: el maestro produce sistemas y artefactos, no consejos

El SDR promedio piensa en el correo de hoy. El maestro piensa en **la máquina que produce los correos de todos los días** (ver `98`, `198`) y en **los documentos que hacen que esa máquina exista sin él**. Las cinco marcas de la maestría a escala:

1. **Piensa en sistemas, no en tácticas.** No busca "el mejor asunto"; construye el proceso que testea asuntos solo (ver `65`, `90`).
2. **Respeta la deliverability como un artesano sus herramientas.** Sabe que la mitad del resultado es fontanería invisible (ver `40`, `197`).
3. **Es implacable con relevancia y calificación.** 30 cuentas correctas > 3.000 al azar; un "no" rápido > un "tal vez" eterno (ver `10`, `78`).
4. **Vive de los números y es honesto con ellos.** Mide, diagnostica, mejora; nada de vanity metrics (ver `80`, `83`). Cálculos exactos → `Matematicas_lushows`.
5. **Produce y delega.** Todo lo que sabe está en documentos que otro puede ejecutar. Puede montar una agencia porque su sistema existe fuera de su cabeza (ver `190`, `194`).

## Los entregables del oficio (el catálogo completo)

Cada fase de trabajo termina en un artefacto. Este es el catálogo que la skill produce, a escala de agencia:

| Entregable | Qué es | Módulos fuente | Para |
|---|---|---|---|
| **ICP escrito** | Perfil de cliente ideal con criterios exactos | `10`, `11`, `12` | Tú o el cliente |
| **Lista / segmento** | Cuentas + contactos + los filtros usados | `20`, `21`, `100` | Ejecución |
| **Config de deliverability** | Dominios, SPF/DKIM/DMARC, plan de warmup | `41`–`43` | Setup |
| **Plantillas de mensaje** | Cold email / LinkedIn / WhatsApp listos | `50`–`59` | Ejecución |
| **Secuencia multicanal** | Cadencia día-por-día, canal por canal | `60`, `61` | Ejecución |
| **Playbook completo** | El sistema entero documentado | `90`, `198` | Delegar / vender |
| **Dashboard de métricas** | Números por etapa + metas + diagnóstico | `80`, `81`, `144` | Revisión semanal |
| **Propuesta de servicio** | Para vender lead-gen como agencia | `95`, `191`, `193` | Cerrar clientes |
| **Caso de estudio** | Campaña con números reales | `195`, `192` | Vender (prueba) |
| **Reporte por cliente** | Resultados del mes para cada cuenta | `144`, `194` | Retener clientes |

**Regla de entrega (innegociable):** nunca dejes al usuario con teoría. Cada interacción cierra con **lo exacto** —el filtro, la plantilla, la secuencia, la config, los números— listo para copiar o ejecutar. "Deberías personalizar" no es un entregable; una plantilla con la personalización marcada, sí.

## Cómo generar un entregable en PDF (chrome headless)

Cuando el entregable es presentable —un playbook, una propuesta, un reporte para el cliente— no lo dejes en Markdown crudo. **Genera el PDF directo.** El método: escribe un HTML autocontenido (estilos inline, sin dependencias externas) y conviértelo con Chrome/Chromium en modo headless.

```bash
# 1. Escribe el contenido como HTML autocontenido en el scratchpad (p. ej. playbook.html)
#    - Estilos en un <style> dentro del mismo archivo (nada externo que no cargue)
#    - Tipografía limpia, márgenes generosos, jerarquía clara
#    - Tablas para secuencias día-por-día y para los números
#    - Portada con nombre del cliente/proyecto y fecha si es propuesta o reporte

# 2. Conviértelo a PDF con Chrome headless (Windows):
"C:/Program Files/Google/Chrome/Application/chrome.exe" \
  --headless --disable-gpu \
  --print-to-pdf="playbook-outbound.pdf" \
  --no-pdf-header-footer \
  "file:///C:/ruta/al/playbook.html"

# Si Chrome no está ahí, usa Edge con las mismas banderas:
# "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe" --headless ...
```

Buenas prácticas para que el PDF se vea profesional:
- Estilos **inline** o en `<style>` en el mismo archivo (nada de CDNs ni fuentes externas que no carguen en headless).
- Jerarquía visual clara: títulos, subtítulos, tablas con bordes suaves, buen espaciado.
- **Tablas** para las secuencias (día-por-día) y los dashboards (métrica → valor → meta); se ven ordenadas en papel.
- **Portada** con nombre del cliente/proyecto y fecha cuando es propuesta o reporte de agencia.
- Para diseño de nivel (marca, color, tipografía fina, logo del cliente) → `directorcreativo_lushows`. Para una landing/web que reciba lo que agendas → `desingweb-lushows`.

## Entregables a escala de agencia (lo que 99 no cubre)

Cuando operas varios clientes (ver `194`), los entregables se **multiplican y estandarizan**:

- **Playbook maestro + variantes por cliente:** un sistema base (ver `90`, `198`) que adaptas por cliente/nicho (ver `170`–`179`). No reinventas cada vez.
- **Reporte mensual por cliente en PDF:** mismo template, datos de cada cuenta (ver `144`). La transparencia es lo que retiene clientes (ver `193`).
- **Propuesta de servicio como plantilla:** portada + caso + alcance + SLA + pricing (ver `191`, `193`, `195`), personalizable por prospecto. Es tu documento de venta; la conversación que la acompaña es `ventas_lushows`.
- **Dashboard consolidado:** todos los clientes en una vista para tu operación (ver `144`, `194`), más el dashboard individual que cada cliente ve.
- **Onboarding kit:** el checklist de alta de cliente (ver `194`) como documento repetible.

Los **números** de todos estos entregables deben ser exactos y defendibles → `Matematicas_lushows`. La **viabilidad y economía** de la agencia detrás de las propuestas → `economist_lushows`. La **facturación** de lo que vendes → `contador_lushows`.

## El camino del principiante al maestro (completo)

```
Principiante:  manda correos, espera, culpa al copy cuando cae en spam
Competente:    tiene ICP, deliverability sana, mide reply rate
Avanzado:      sistema documentado, multicanal, califica duro, diagnostica por número
Maestro:       máquina replicable + delegable + vendible; produce entregables
Agencia:       varias máquinas, infra separada, entregables estandarizados, negocio
```

El salto clave nunca es saber más tácticas: es pasar de **hacer outbound** a **construir el sistema que hace outbound** (ver `198`), **documentarlo** para que exista sin ti (ver `90`), y **empaquetarlo** como negocio (ver `190`).

## Errores comunes (qué NO hacer)

- Entregar teoría o Markdown crudo cuando el trabajo merecía un PDF presentable. Genera el artefacto.
- Confundir maestría con conocer más herramientas. El maestro domina el sistema, no la lista de apps (ver `30`).
- Producir entregables bonitos sin números defendibles detrás. Verifica todo con `Matematicas_lushows`.
- Reinventar cada entregable desde cero en vez de estandarizar plantillas por cliente (ver `194`).
- Creer que el cierre y la negociación son "el nivel más avanzado del SDR". Son otro oficio → `ventas_lushows`. Tu maestría es llenar el pipeline predeciblemente y producir el sistema que lo hace.

## Siguiente paso (y cierre de la biblioteca)

Cuando cierres cualquier fase de trabajo, pregúntate: **"¿qué artefacto se lleva el usuario?"** y prodúcelo — si es presentable, en PDF con el método de arriba. Este módulo cierra los 200: el mapa completo del sistema está en `198`, el negocio en `190`–`197`, el núcleo en `00`–`99` y la expansión en `100`–`189`. Todo apunta a lo mismo: una **máquina medible que consigue y agenda reuniones**, documentada y entregable. El cierre de esas reuniones, siempre, es `ventas_lushows`.
