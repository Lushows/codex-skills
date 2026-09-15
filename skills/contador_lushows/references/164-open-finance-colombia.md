# 164 — Open finance en Colombia

**Open finance** ("finanzas abiertas") es el modelo en el que tú, dueño de tus datos financieros, **autorizas** a que un banco o una app comparta de forma segura tu información (saldos, movimientos) con otra entidad o herramienta. Para la contabilidad esto es enorme: en vez de bajar el extracto en PDF y leerlo con OCR, los movimientos del banco pueden llegar **conectados y en tiempo casi real** a tu software. Es la materia prima para conciliar y contabilizar sin digitar.

Una aclaración importante: en Colombia el open finance está **en construcción y evolución** (marco regulatorio y adopción de los bancos avanzando). Las reglas y qué bancos ya lo soportan **cambian rápido**: verifica el estado vigente antes de prometerle algo a un cliente.

## Qué cambia para la contabilidad

| Antes | Con open finance |
|---|---|
| Bajar extracto PDF cada mes | Movimientos llegan automáticamente |
| Leer con OCR (puede fallar) | Datos ya estructurados desde el banco |
| Conciliar al cierre | Conciliar continuamente (casi diario) |
| Cliente reenvía soportes | La conexión los trae (según permisos) |

## Cómo se conecta (sin tecnicismos)

1. El dueño de la cuenta **da su consentimiento** explícito (qué datos, por cuánto tiempo).
2. La herramienta se conecta vía **API** (la "tubería" que comunica dos sistemas — módulo 166).
3. Los movimientos fluyen a la contabilidad para conciliar y sugerir asientos.
4. El consentimiento se puede **revocar** cuando el dueño quiera.

El **consentimiento** es el corazón: sin permiso del titular, no hay conexión. Eso protege al cliente y a ti.

## Ejemplo (cifras ILUSTRATIVAS / inventadas)

Un café conecta su cuenta vía open finance. Cada noche, los $3.400.000 de ventas por datáfono y los $1.200.000 de transferencias entran solos al sistema; al día siguiente la conciliación ya está casi lista y el contador solo revisa 2 excepciones. Antes, esto tomaba medio día al cierre del mes. Cifras y tiempos inventados para ilustrar.

## Errores comunes

- **Conectar sin consentimiento claro del titular**: problema legal y de confianza.
- **Asumir que todos los bancos ya lo soportan**: en 2026 la cobertura es desigual; verifica.
- **No revisar qué datos se comparten**: comparte lo mínimo necesario.
- **Olvidar que la conexión puede caerse**: ten un plan B (volver a OCR del extracto).
- **Confundir "datos en tiempo real" con "contabilidad lista"**: siguen necesitando clasificación y aprobación humana.

## Conexión con otros módulos

- Los datos que llegan alimentan la **conciliación automática** (módulo **162**) y la **contabilización** (módulo **163**).
- La parte técnica de **APIs, sincronización y seguridad** está en el módulo **166**.
- Los **riesgos de datos sensibles y privacidad** (Habeas Data en Colombia): módulo **169**.
- *Decidir* si invertir en esto o qué herramienta: `economist_lushows`. *Construir* la integración: `engineer_visualopen_lushows`.

## Siguiente paso típico

Averigua si el banco de tu cliente y la herramienta contable que usan ya ofrecen conexión por open finance (estado 2026, verifica directo con ellos). Si sí, haz una prueba con **una sola cuenta** y consentimiento por escrito antes de extenderlo. Si no, sigue con OCR del extracto (módulo 161) mientras madura.
