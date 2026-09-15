# 99 — Maestría y entregables

Este módulo cierra el núcleo (00–99): el camino del SDR de élite y **cómo convertir el trabajo en entregables reales** que el usuario puede usar, presentar o vender. Importa porque una skill de outbound no vale por lo que sabe, sino por lo que **produce**: el ICP escrito, la lista con criterios, la secuencia día-por-día, el playbook, el dashboard. Un consejo se olvida; un entregable se ejecuta. Aquí está qué distingue al maestro del principiante, y el método concreto para generar los artefactos —incluido cómo sacarlos en **PDF presentable** con chrome headless cuando merecen verse profesionales.

## El principio: el maestro produce sistemas, no mensajes sueltos

El SDR promedio piensa en el correo de hoy. El maestro piensa en **la máquina que produce los correos de todos los días** (ver `98`). La maestría en outbound tiene cuatro marcas:

1. **Piensa en sistemas, no en tácticas.** No busca "el mejor asunto"; construye el proceso que testea asuntos y encuentra el mejor solo (ver `65`, `90`).
2. **Respeta la deliverability como un artesano respeta sus herramientas.** Sabe que el 50% del resultado es fontanería invisible y nunca la descuida (ver `40`).
3. **Es implacable con la relevancia y la calificación.** Prefiere 30 cuentas correctas a 3.000 al azar, y un "no" rápido a un "tal vez" eterno (ver `10`, `78`).
4. **Vive de los números y es honesto con ellos.** Mide, diagnostica y mejora; no se engaña con vanity metrics (ver `80`, `83`). Y conoce su frontera: **consigue y agenda; el cierre es de `ventas_lushows`.**

## Los entregables del oficio (qué produces)

Cada fase de trabajo termina en un artefacto concreto. Estos son los entregables que esta skill genera:

| Entregable | Qué es | Módulos fuente | Formato |
|---|---|---|---|
| **ICP escrito** | El perfil de cliente ideal con criterios exactos | `10`, `11` | Doc / PDF |
| **Lista / segmento** | Cuentas + contactos con los filtros usados | `20`, `21`, `26` | CSV + doc de criterios |
| **Plantillas de mensaje** | Cold email/LinkedIn/WhatsApp listos para copiar | `50`–`59` | Doc |
| **Secuencia multicanal** | La cadencia día-por-día, canal por canal | `60`, `61` | Tabla / PDF |
| **Config de deliverability** | Dominios, SPF/DKIM/DMARC, plan de warmup | `41`–`43` | Checklist / doc |
| **Playbook de outbound** | El sistema completo documentado | `90` | PDF |
| **Dashboard de métricas** | Los números por etapa y sus metas | `80`, `144` | Hoja / tabla |
| **Propuesta de servicio** | Para vender lead-gen como agencia | `95`, `191` | PDF |

**Regla de entrega:** nunca dejes al usuario con teoría. Cada interacción cierra con **lo exacto** (el filtro, la plantilla, la secuencia, la config), no con "deberías personalizar". Texto y tablas listos para usar.

## Cómo generar un entregable en PDF (chrome headless)

Cuando el entregable es presentable —un playbook, una propuesta de servicio, una secuencia para el cliente— no lo dejes en Markdown crudo esperando que el usuario lo procese. **Genera el PDF directo.** El método: escribe un HTML autocontenido y conviértelo con Chrome/Chromium en modo headless.

```bash
# 1. Escribe el contenido como HTML autocontenido (estilos inline, sin dependencias externas)
#    Guárdalo, por ejemplo, en el scratchpad como playbook.html

# 2. Conviértelo a PDF con Chrome headless (Windows):
"C:/Program Files/Google/Chrome/Application/chrome.exe" \
  --headless --disable-gpu \
  --print-to-pdf="playbook-outbound.pdf" \
  --no-pdf-header-footer \
  "file:///C:/ruta/al/playbook.html"
```

Buenas prácticas del HTML para que el PDF se vea profesional:
- Estilos **inline** o en un `<style>` en el mismo archivo (nada externo que no cargue).
- Tipografía limpia, márgenes generosos, jerarquía clara (títulos, tablas con bordes suaves).
- Tablas para las secuencias día-por-día y los números; se ven ordenadas en papel.
- Portada con el nombre del cliente/proyecto y la fecha si es una propuesta.
- Para diseño de nivel (marca, color, tipografía fina), apóyate en `directorcreativo_lushows`; para una landing/web que reciba lo que agendas, `desingweb-lushows`.

Si Chrome no está en esa ruta, busca el ejecutable o usa Edge (`msedge.exe`) con las mismas banderas. El objetivo: entregar un archivo que el usuario abre, lee y usa — o le manda a su cliente.

## El camino del principiante al maestro

```
Principiante:  manda correos, espera, culpa al copy cuando cae en spam
Competente:    tiene ICP, deliverability sana, mide reply rate
Avanzado:      sistema documentado, multicanal, califica duro, diagnostica por número
Maestro:       máquina replicable + delegable + vendible; produce entregables, no consejos
```

El salto clave no es saber más tácticas: es pasar de **hacer outbound** a **construir el sistema que hace outbound** (ver `98`) y **documentarlo** para que exista sin ti (ver `90`).

## Errores comunes (qué NO hacer)

- Entregar Markdown o teoría cuando el trabajo merecía un PDF presentable. Genera el artefacto.
- Confundir maestría con conocer más herramientas. El maestro domina el sistema, no la lista de apps.
- Meterte en el cierre y la negociación creyendo que es "nivel avanzado del SDR". Es otro oficio → `ventas_lushows`. Tu maestría es llenar el pipeline predeciblemente.
- Producir entregables bonitos sin números defendibles detrás. Verifica los cálculos con `Matematicas_lushows`.

## Siguiente paso

Cuando cierres una fase de trabajo con el usuario, pregúntate: "¿qué artefacto se lleva?" y prodúcelo. Si es presentable, sácalo en PDF con el método de arriba. Para el sistema completo que documentas ver `90` y `98`. Para el nivel maestro con toda la expansión (100–199) y los entregables avanzados —listas, secuencias y dashboards en PDF a escala de agencia— ver `199`.
