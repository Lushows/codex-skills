# 199 — Changelog normativo (fuente de verdad de "qué cambió y cuándo")

La normativa contable y tributaria de Colombia **cambia todos los años**: el valor de la UVT, las tarifas, los plazos del calendario tributario, los topes de exógena, la estructura de formatos como el 2516. Este módulo es el **registro fechado** de esos cambios. Es la única "memoria viva" de la skill: cuando algo cambia, se anota AQUÍ con su fecha, y todos los demás módulos remiten aquí en vez de quemar un valor que quedará viejo.

> **Regla permanente**: ningún módulo escribe un valor de UVT, tarifa, tope o fecha como si fuera eterno. Dicen "verifica el valor del año" y apuntan a este changelog. Aquí —y solo aquí— se registra el dato vigente con su fecha de cambio.

## Cómo se lee una entrada

Cada entrada tiene: **fecha** del cambio o de la verificación → **qué cambió** → **módulos afectados** → **acción** (qué revisar). Lo más reciente va arriba.

## Cómo mantener este changelog vivo

1. **Antes de cualquier cálculo tributario o cierre**, revisa la fuente oficial (DIAN, decretos, resoluciones) y compara con la última entrada.
2. Si cambió algo, **agrega una entrada nueva arriba** con la fecha, qué cambió y los módulos afectados. No borres las viejas: el historial es valioso.
3. Al inicio de cada año fiscal, registra **una entrada de "verificación de inicio de año"** confirmando UVT, calendario y topes vigentes.
4. Si un módulo quemó un valor por error, corrígelo para que apunte aquí.
5. Cuando un cliente pregunte "¿esto sigue igual?", la respuesta sale de aquí, no de la memoria.

## Qué vigilar cada año (lista permanente)

- **Valor de la UVT** (afecta casi todo: topes, sanciones, tablas) — módulos 40, 42, 49, 68.
- **Calendario tributario** (fechas de renta, IVA, retención, exógena) — módulos 46, 47.
- **Tarifas** de renta, IVA, retención, ICA — Bloque 4.
- **Topes de exógena** y estructura de formatos — módulos 64, 192.
- **Formato 2516** (estructura, obligados) — módulo 191.
- **Régimen Simple (SIMPLE)**: tarifas y condiciones — módulo 63.
- **Nómina y seguridad social**: salario mínimo, auxilio de transporte, tarifas PILA — Bloque 5.
- **NIIF**: actualizaciones de los marcos por grupo — módulos 03, 62.
- **Reformas tributarias**: cualquier ley que cambie las reglas de juego.

## Entradas semilla (ILUSTRATIVAS / PLANTILLA — reemplazar con datos verificados del año)

> Las siguientes entradas son **ejemplos de formato**, no datos confirmados. Verifica cada cifra en la fuente oficial antes de usarla y reemplaza este bloque con entradas reales.

---

**[PLANTILLA] 2026-01-02 — Verificación de inicio de año fiscal 2026**
- Qué revisar: valor de la UVT 2026, salario mínimo y auxilio de transporte 2026, calendario tributario 2026.
- Módulos afectados: 40, 42, 46, 49, 50, 68.
- Acción: confirmar cada valor en DIAN/decreto y registrar el dato vigente. (Valores pendientes de verificar — NO usar de memoria.)

---

**[PLANTILLA / ILUSTRATIVA] 2026-XX-XX — Resolución anual de información exógena 2026**
- Qué cambió: nuevos topes y plazos para reportar exógena del año gravable.
- Módulos afectados: 64, 192.
- Acción: comparar topes con el año anterior y actualizar el módulo 192 si cambian las cuantías.

---

**[PLANTILLA / ILUSTRATIVA] 2026-XX-XX — Ajuste de plazos del calendario tributario 2026**
- Qué cambió: fechas de vencimiento de renta personas jurídicas/naturales, IVA y retención.
- Módulos afectados: 46, 47, 198.
- Acción: actualizar el calendario y el checklist de plazos.

---

## Errores comunes

- **Dejar el changelog sin actualizar** y seguir usando valores viejos: la causa #1 de declaraciones mal liquidadas.
- **Borrar entradas antiguas**: se pierde el historial de por qué algo cambió.
- **Confiar en las entradas plantilla** como si fueran datos reales (están rotuladas como ilustrativas a propósito).
- **Quemar un valor en otro módulo** en vez de apuntar aquí.

## Conexión con otros módulos

- **Módulo 40** — marco tributario que depende de la UVT vigente.
- **Módulo 46** — calendario tributario (fechas que cambian cada año).
- **Módulos 191, 192** — formatos 2516 y exógena cuya estructura/topes cambian.
- **Módulo 198** — el checklist de calidad confirma formatos y plazos contra este changelog.
- **economist_lushows** DECIDE con base en reglas vigentes; **contador** mantiene este registro al día.

## Siguiente paso típico

Cada vez que vayas a calcular un impuesto, liquidar nómina o cerrar el año, **empieza por aquí**: confirma que los valores estén vigentes y registra cualquier cambio. Esto NO reemplaza la verificación oficial ni al contador titulado.

- **22-jun-2026 (módulo 45):** añadida la **habilitación de factura electrónica paso a paso** (Solución Gratuita DIAN): portal `catalogo-vpfe-hab.dian.gov.co` (NO el menú de MUISCA, que da 500), modo "Software Gratuito DIAN", certificado gratis, SET de pruebas (2 FV + 1 NC + 1 ND), numeración en MUISCA, asociación en producción. Plazo Res. 000165/2023 (~2 meses desde registro RST / desde primera venta — confirmar con contador titulado).
