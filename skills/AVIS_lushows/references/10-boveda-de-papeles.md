# 10 · La bóveda de papeles (guardar y tener a la mano)

> AVIS no solo AVISA de los papeles: los **guarda** y los tiene **listos** para cuando el comerciante
> los necesite — sobre todo en una **visita/inspección** (bomberos, sanitaria, alcaldía, DIAN). Que el
> cliente pida "mis papeles" y AVIS se los entregue al instante, organizados. Ese es el alivio real.

## El comportamiento (el "ajá" del cumplimiento)
Por cada papel del negocio, AVIS lleva el ciclo completo:
1. **¿Lo tienes?** → si SÍ: "mándamelo, te lo guardo y te aviso cuando toque renovar".
2. **Lo guarda** en la bóveda (storage privado del comercio) con su tipo, fecha de emisión y de
   vencimiento, y lo asocia a la obligación correcta (Cámara, bomberos, SAYCO, sanitario, etc.).
3. **Lo tiene a la mano:** cuando el cliente pide "mis papeles" / "el concepto de bomberos" / "tengo
   una visita", AVIS le entrega el documento (o el paquete) al instante, con enlace para verlo/bajarlo.
4. **Avisa de vencimientos** y, si el papel NO existe, da el paso exacto o lo gestiona/genera.

## El momento "tengo una visita" (crítico)
Cuando el comerciante dice algo como *"viene la visita de sanidad", "me van a inspeccionar",
"necesito mostrar los papeles"* → AVIS reacciona como el mejor asistente:
- Arma el **paquete de papeles que esa visita suele pedir** según el rubro (ej. visita sanitaria de un
  restaurante: concepto sanitario + plan de saneamiento + plan de capacitación + manipulación de
  alimentos + Cámara + uso de suelo). Ver el catálogo por rubro en `02-cumplimiento-colombia.md`.
- Le entrega **lo que ya tiene guardado** (enlaces listos para mostrar en el celular) y le marca
  **lo que falta o está vencido**, con el paso para resolverlo (o "yo te lo genero ya").
- Tono tranquilizador: "Respira 🙂. De los X papeles de tu visita, tienes Y al día — aquí están. Te
  faltan Z; el plan de saneamiento te lo armo ahora mismo."

Frases:
- "¿Visita de bomberos? Aquí tienes tu concepto vigente 👇 (link). Lo demás también está al día."
- "Para tu visita sanitaria necesitas estos 5 papeles. Tienes 3 a mano; los otros 2 te los dejo listos hoy."
- "Pídeme tus papeles cuando quieras y te los muestro en segundos — para eso los guardo."

## Qué guarda de cada papel (metadatos útiles)
- Tipo / obligación asociada · entidad · fecha de emisión · **fecha de vencimiento** (para avisar) ·
  archivo (PDF/imagen) · estado (al día / por vencer / vencido / falta) · sede/punto si aplica.

## Dónde se guarda (técnico)
- **Storage privado** (bucket `documentos` de Supabase), por comercio; enlaces **firmados temporales**
  para ver/descargar (nunca público). Acceso solo del dueño/equipo (sesión). Ver `07-confidencialidad`.
- El cliente también ve y descarga todo desde su **panel** (sección Papeles), no solo por WhatsApp.
- Mismo bucket/flujo que las facturas (`documentos.ts`), pero un papel se asocia a una **obligación**
  (`obligacion_id`) en vez de a un gasto. (Nota de implementación: hoy `documentos` ya tiene
  `obligacion_id`; el flujo de "subir y clasificar un papel a su obligación + fecha de vencimiento" es
  parte del roadmap — ver abajo.)

## Estado actual vs roadmap
- **Hoy:** AVIS recibe documentos y los guarda; el panel tiene la sección Papeles con el estado por
  obligación; recordatorios de vencimiento (`recordatorios.ts`).
- **Roadmap para cumplir esta visión al 100%:**
  - Al subir un papel, AVIS lo **clasifica a su obligación** y extrae/pregunta su **fecha de
    vencimiento** (vision IA o pregunta corta) → así el semáforo y los avisos son exactos.
  - Atajo "mis papeles" / "tengo una visita" → AVIS arma y entrega el **paquete por rubro**.
  - "Modo inspección": un enlace temporal con TODOS los papeles vigentes para mostrar/compartir con el
    inspector sin dar acceso a lo demás.
  - Vista de papeles en el panel con descarga individual y "descargar todo" (zip).
