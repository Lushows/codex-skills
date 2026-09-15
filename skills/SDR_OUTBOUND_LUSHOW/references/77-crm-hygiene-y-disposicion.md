# 77 — CRM hygiene y disposición

El CRM (Customer Relationship Management = el sistema donde vive cada contacto y su historia) es la memoria de tu máquina de outbound. Si está sucio —estados inventados, contactos duplicados, notas a medias, leads sin próximo paso— pierdes tratos por olvido, no por falta de demanda. La higiene del CRM (mantenerlo limpio y consistente) y la disposición (registrar el resultado de CADA intento de contacto con un estado estándar) son lo que garantiza que *nada se pierda*: cada lead tiene un estado claro y un próximo paso. Este módulo te da los estados de lead limpios y las reglas de disposición. Es el registro donde aterrizan la calificación (`70`), el handoff (`73`), los no-shows (`75`) y el nurture (`76`).

## El principio: lo que no se registra, se pierde

Tu memoria no escala. A los 50 leads en juego ya no recuerdas quién dijo qué, ni a quién le prometiste llamar el martes. El CRM es tu segundo cerebro, pero solo funciona si lo alimentas con disciplina: **cada toque genera una disposición (resultado) y un próximo paso con fecha.** La regla de oro: *ningún lead activo puede quedar sin próximo paso agendado.* Un lead sin próximo paso es un lead muerto que todavía no sabes que perdiste.

La disposición además es lo que hace medible todo el sistema (ver `72`, `74`): sin estados consistentes no puedes calcular tasas de conversión ni saber dónde se cae el embudo.

## Los estados de lead (pipeline limpio)

Usa un set corto y estándar. Demasiados estados confunden; muy pocos no informan. Este set cubre outbound:

| Estado | Qué significa | Próximo paso típico |
|---|---|---|
| **Nuevo** | Entró a la lista, sin tocar | Iniciar cadencia (ver `74`) |
| **En cadencia** | Contactado, dentro de la secuencia | Siguiente toque agendado |
| **En conversación** | Respondió, calificando (ver `70`) | Agendar call / seguir calificando |
| **SQL / Reunión agendada** | Calificado, handoff hecho (ver `73`) | Que el AE la tome (ver `74`) |
| **No-show** | Faltó a la reunión | Secuencia de recuperación (ver `75`) |
| **Nurture** | Buen fit, "no ahora" (ver `76`) | Próximo toque con fecha |
| **Descalificado** | Fuera de ICP / sin dolor / dato muerto | Cerrado con motivo |
| **No contactar** | Pidió opt-out | Suprimir, no volver a escribir |
| **Ganado / Perdido** | (lo cierra el AE) | Feedback al SDR (ver `79`) |

## Las disposiciones de llamada/toque (resultado de cada intento)

Cada vez que llamas o escribes y no avanza a otro estado, registra la disposición:

```
DISPOSICIONES DE TOQUE (estándar):
  • Conectó – interesado        → mover a "En conversación"
  • Conectó – no ahora          → mover a "Nurture" (ver 76)
  • Conectó – no interesado     → "Descalificado" (motivo)
  • No contestó / buzón         → seguir cadencia, próximo toque
  • Correo rebotó               → verificar dato (ver 28); si muerto, descalificar
  • Pidió no ser contactado     → "No contactar" (opt-out, respétalo)
  • Persona equivocada          → buscar decisor correcto (ver 22)
```

Regla: **toda disposición lleva un motivo en una frase** ("no ahora — abre local en 2 meses", "fuera de ICP — es 1 solo food truck"). El motivo es oro para el feedback (ver `79`) y para el nurture (ver `76`).

## Higiene: las reglas que mantienen el CRM limpio

```
CHECKLIST DE HIGIENE (rutina):
  □ Sin duplicados: 1 persona = 1 registro (dedup por email/teléfono)
  □ Sin lead activo sin próximo paso con fecha
  □ Todo estado refleja la realidad (no "En cadencia" un lead de hace 2 meses)
  □ Datos normalizados: teléfono con formato país (+57...), email en minúscula
  □ Nombre/cargo/empresa completos (no "Andrea" a secas)
  □ Fuente registrada (de dónde salió — ver 20)
  □ Cada nota fechada; nada de "hablamos hace rato"
  □ Los "muertos" cerrados con motivo, no dejados en limbo
```

El duplicado es el enemigo silencioso: dos SDR le escriben a la misma persona, o el AE ve historia incompleta. Dedup siempre por email y teléfono normalizados (lección aprendida en otros proyectos: normaliza mayúsculas/espacios antes de comparar).

## Ejemplo de registro bien llevado (una fila viva)

```
Andrea Gómez · Grupo Sazón (3 locales, Bogotá) · andrea@gruposazon.co · +57 300...
Estado: SQL / Reunión agendada
Fuente: cold email 2-jul
Historial:
  2-jul  Email 1 enviado (ángulo: costo de plato)
  2-jul  Respondió: "cuéntame más"  [disposición: conectó-interesado]
  3-jul  Call de calificación 8min → SQL (dolor+fit+timing ✅, ver 70)
  3-jul  Handoff a Camilo (AE) — nota completa (ver 73)
Próximo paso: Reunión jue 10am (AE) — invite enviada
```

Cualquiera que abra esa ficha entiende todo en 20 segundos. Eso es higiene.

## Errores comunes

- **Dejar leads sin próximo paso.** Se enfrían en el olvido. Regla: cero leads activos huérfanos.
- **Estados que mienten.** "En cadencia" algo que abandonaste hace un mes ensucia tus métricas.
- **No registrar el motivo al descalificar.** Pierdes el aprendizaje (ver `79`) y a veces botas un futuro cliente que debía ir a nurture.
- **Duplicados.** Dos toques a la misma persona = quedas desordenado. Dedup normalizado.
- **Notas vagas.** "Buena llamada" no sirve al AE ni a ti en 3 semanas. Sé concreto y fecha todo.

## Siguiente paso

Con estados y disposiciones limpios, tus métricas de `72` y `74` se vuelven confiables. Los "no ahora" registrados alimentan `76`; los no-shows, `75`. El motivo de cada descalificado nutre el loop de calidad con el AE en `79` y el filtro anti-basura de `78`.
