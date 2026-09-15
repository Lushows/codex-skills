# 39 — Volumen y fatiga creativa

Todo creativo muere. Este módulo cubre cómo detectar la fatiga sin pánico, cuánto producir según tu gasto, y el sistema de refresh para que la cuenta nunca dependa de un solo ad moribundo. Léelo al armar tu calendario mensual y cada vez que "el ad que funcionaba ya no funciona". En 2026 la vida útil se acortó (2-4 semanas en cuentas con gasto medio-alto) → el pipeline de refresco es obligatorio, no opcional.

## Qué es la fatiga (y qué no)

**Fatiga creativa** = el creativo agotó a su audiencia eficiente: la gente que iba a responder ya lo vio (varias veces) y Meta tiene que mostrárselo a gente cada vez menos propensa. Señales — las TRES juntas, sostenidas:

1. **Frequency sube** (frecuencia = impresiones ÷ personas alcanzadas; en frío, >2.5-3 enciende alarma).
2. **CTR cae** respecto a sus propias primeras semanas.
3. **CPA sube sostenido 5-7 días** — no 1 día de ruido.

Un mal martes no es fatiga; una semana de deterioro con frequency alta sí. En creative analytics (ver 68), la firma clásica de fatiga es: **thumbstop estable pero CTR y conversión cayendo** mientras frequency sube → la gente ya lo vio y dejó de reaccionar.

No es fatiga:
- Caída de 1-2 días (subasta, festivo, quincena, día de pago en Colombia mueve la conversión).
- Caída con **frequency baja** → problema de oferta (ver 41) o landing (desingweb-lushows), no de creativo.
- Caída justo tras editar la campaña → reinicio de aprendizaje (no toques y espera).
- Ad que **nunca** funcionó → no está fatigado, nació muerto: revisa oferta y ángulo (ver 41, 38).

## Vida útil típica 2026

- **Cuentas grandes** (gasto alto): **2-4 semanas**, a veces días — queman audiencia rápido.
- **Pymes con poco gasto**: semanas a meses — **a menos gasto, más dura el creativo**, porque tardas más en agotar tu audiencia eficiente. Una pyme colombiana gastando $1M COP/mes puede vivir de un ganador 2-4 meses.
- Corolario: no copies el ritmo de refresh de los gurús de cuentas de US$100k/mes. **Tu ritmo lo dicta TU gasto y TU frequency**, no un benchmark ajeno.

## Pipeline mensual según gasto

| Gasto mensual (COP) | Creativos nuevos/mes (conceptualmente distintos, ver 30) |
|---|---|
| < $1M | 4-6 |
| $1-5M | 8-12 |
| $5-20M | 15-25 |
| > $20M | 25-40+ |

Distribución del lote: **60% iteraciones de ganadores / 30% ángulos nuevos / 10% apuestas** (ver 30). Recuerda: deben ser distintos entre sí (Entity ID, ver 30), no casi-duplicados.

**Calendario de producción** (para no producir en pánico):
- **Semana 1**: briefs — elegir ángulos del mapa (ver 38), escribir hooks (ver 37), enviar briefs a creators (ver 32).
- **Semanas 2-3**: producción — grabación, diseño de estáticas (ver 35), edición y subtítulos (ver 34).
- **Semana 4**: al aire — montar, QA con el checklist (ver 31), lanzar.

El lote de junio se brifea en mayo. **Siempre hay un lote en cada etapa** (uno brifeándose, uno produciéndose, uno al aire). Así nunca llegas al lunes sin creativo nuevo.

## Iterar ganadores ANTES de que mueran

No esperes el funeral: cuando un ad lleva **2+ semanas ganando, ya** debe estar en producción su siguiente versión. Qué refrescar primero (de más barato a más caro):

1. **HOOK — 80% del refresh es un hook nuevo sobre el cuerpo ganador** (ver 37). Costo mínimo, mantiene lo que funciona, crea un Entity ID nuevo.
2. **Otra cara/escenario**, mismo guion (otro creator o el founder, ver 32).
3. **Cambio de formato**: video ganador → estática con su frase clave, o → carrusel (ver 33, 35, 36).
4. **Solo si 1-3 se agotaron**: ángulo siguiente del mapa (ver 38).

Cada refresh debe ser conceptualmente distinto para no colapsar en el Entity ID del original (ver 30).

## Cómo escalar un ganador sin matarlo

Cuando encuentras un ganador, la tentación es subirle el presupuesto de golpe. Eso dispara la frequency y acelera la fatiga. Opciones:
- **Subir presupuesto 20-30% cada 2-3 días** (escalado vertical suave) para no reiniciar aprendizaje ni quemar audiencia de golpe.
- **Escalado horizontal**: duplica el ganador en más ad sets/campañas o ábrelo a más geografía/público broad (ver 20).
- **Refresca el hook en paralelo**: mientras escalas, ya está al aire la siguiente versión.

(La mecánica fina de escalado y presupuestos vive en los módulos de estructura/escalado; aquí lo relevante es: escalar acelera la fatiga → ten el reemplazo listo.)

## Revivir ganadores viejos

Un ganador retirado puede volver cuando:
- **Estacionalidad**: el ad de diciembre vuelve cada diciembre; el de "propósitos" cada enero; el del Día de la Madre, etc.
- **Audiencia renovada**: tras 2-3+ meses de descanso, parte de la audiencia es nueva o ya olvidó el ad.
- Relanza como **ad nuevo** (idealmente con hook refrescado) y trátalo como apuesta del 30%, no como ganador garantizado.

## Registro de creativos (la hoja)

Sin registro no hay sistema. Una hoja de cálculo basta, una fila por creativo:

| Campo | Ejemplo |
|---|---|
| ID | 2026-06-V03 |
| Ángulo (ver 38) | Contraste vs café |
| Nivel consciencia (ver 38) | Consciente del problema |
| Hook (ver 37) | "Dejé el tercer café del día..." |
| Formato | Video UGC 9:16, 28s |
| Fuente | Creator @____ / founder / Canva |
| Fecha al aire | 2026-06-10 |
| Resultado | CPA $8.500, thumbstop 32%, CTR 1.8%, freq 2.1 |
| Estado | GANADOR / activo / fatigado / retirado / revivir-en-diciembre |
| Siguiente iteración | Hook H2 grabándose |

Con 3 meses de hoja sabes qué **ángulos y hooks ganan en TU cuenta** — eso vale más que cualquier benchmark ajeno (ver 68). Es tu activo: si cambias de agencia o de plataforma, la hoja se queda contigo.

## Diagnóstico exprés: ¿es el creativo, la oferta o la landing?

Antes de producir un lote nuevo "porque bajó el rendimiento", aísla la causa:

| Síntoma | Probable causa | Acción |
|---|---|---|
| Thumbstop bajo | Hook débil (ver 37) | Nuevo hook, mismo cuerpo |
| Thumbstop OK, CTR bajo | Cuerpo/oferta floja (ver 31, 41) | Reescribe cuerpo o mejora oferta |
| CTR OK, conversión baja | Landing/WhatsApp no cierra | desingweb-lushows / ventas_lushows |
| Todo cae + frequency alta | Fatiga real | Refresh del lote |
| Todo cae + frequency baja | Oferta o mercado | Revisa oferta (ver 41), no produzcas creativo aún |

## Errores comunes — blacklist

- ❌ Diagnosticar fatiga con 1 día malo y apagar al ganador por pánico.
- ❌ Lo contrario: dejar morir al único ad de la cuenta sin reemplazo en producción.
- ❌ Refresh cosmético (color, música) y llamarlo creativo nuevo (colapsa en el mismo Entity ID, ver 30).
- ❌ Producir en pánico cuando el CPA ya explotó: el calendario existe para que nunca pase.
- ❌ Copiar ritmos de refresh de cuentas con 100x tu gasto.
- ❌ Escalar un ganador 5x de golpe: disparas frequency y lo matas en días.
- ❌ Borrar ads fatigados en vez de pausarlos: pierdes historial, datos y la opción de revivir.
- ❌ No registrar nada y "recordar" qué funcionó: en 3 meses no recordarás ni el hook.
- ❌ Confundir fatiga con problema de oferta: si nunca funcionó, no está fatigado — nació muerto (ver 41 y 38).
