# 76 — Mitos de Google Ads

Lee este módulo cuando alguien (un "experto" de YouTube, un cliente, tu propio instinto) te empuje a hacer algo "porque así se hace". Google Ads está lleno de supersticiones que eran ciertas en 2015 y hoy te cuestan dinero. Cada mito aquí se desmonta con lo que **sí** es real en la era de Smart Bidding, concordancia moderna y AI Max (jun-2026). Regla general: si una creencia te pide reaccionar rápido, tocar mucho, o tratar al algoritmo como tonto — desconfía.

Marco: Google captura demanda existente. Muchos mitos vienen de no entender eso (creer que "más keywords" o "más tipos" generan demanda que no existe) o de pelear con un algoritmo que hoy entiende intención mejor que tu lista literal.

## Mito por mito

### Mito 1: "Más keywords es mejor"
**Falso.** Una lista gigante de keywords no mejora nada; diluye datos y te hace gestionar ruido. Smart Bidding optimiza por **señales de conversión**, no por cantidad de términos. Lo que importa es la **intención** detrás de la keyword, no el conteo.
**Real:** pocas keywords con intención clara + concordancia bien elegida + negativas que filtran basura (ver 21-concordancia, 22-negativas) rinden más que 500 keywords mediocres. Calidad de intención > cantidad. En la era broad + Smart Bidding, una sola keyword broad bien alimentada cubre más variantes que 50 exact.

### Mito 2: "Exact siempre gana"
**Falso.** La concordancia exacta (exact: la búsqueda debe coincidir casi literal) ya no es la fortaleza intocable que era. Hoy Google interpreta intención, y exact restringe tanto que pierdes volumen de búsquedas válidas que se escriben distinto. Broad (amplia) **con Smart Bidding y buenas negativas** suele capturar intención que exact deja afuera.
**Real:** la concordancia es una herramienta según el contexto, no una jerarquía fija. Broad + Smart Bidding + negativas funciona muy bien hoy; exact sigue útil para control fino en términos clave y para proteger marca (ver 21-concordancia, 39-marca-generico). No hay "ganador" universal.

### Mito 3: "Pausa lo que no convirtió ayer"
**Falso y carísimo.** Un día no es una muestra estadística. El rendimiento diario oscila enormemente; lo que "no convirtió ayer" puede convertir mañana. Pausar por el dato de 24 horas te mantiene matando ganadores y reiniciando aprendizaje sin parar.
**Real:** juzga por **1 ciclo de conversión completo** y volumen suficiente (15–30 conversiones para decisiones de puja). Mata solo con la regla del múltiplo de CPA y descartando causas reparables (ver 71-kill, 70-reglas).

### Mito 4: "Duplica la campaña para resetear el aprendizaje"
**Falso.** Duplicar no "resetea limpio" — tiras todo el historial de aprendizaje que ya pagaste y la copia entra en fase de aprendizaje desde cero, gastando errático mientras junta datos de nuevo. Casi nunca es la solución.
**Real:** si una campaña tiene un problema, **diagnostícalo** (ver 75-troubleshoot) y arréglalo dentro de la campaña existente. Duplicar solo tiene sentido en reestructuraciones grandes y planificadas, no como botón mágico de reseteo.

### Mito 5: "Broad es basura"
**Falso (hoy).** Broad tenía mala fama porque sin Smart Bidding traía cualquier cosa. Con Smart Bidding moderno + Enhanced Conversions + negativas, broad le da al algoritmo el espacio para encontrar intención que tú no anticipaste. Es de las fuentes de crecimiento más infravaloradas.
**Real:** broad **mal manejado** (sin negativas, sin Smart Bidding, sin revisar términos de búsqueda) sí es basura. Bien manejado es una palanca de captura potente. La diferencia es el mantenimiento, no la concordancia en sí (ver 21-concordancia, 22-negativas).

### Mito 6: "Apretar el target da más volumen"
**Falso — al revés.** Apretar el tCPA (o subir el tROAS) baja el CPA pero **reduce** el volumen: Google deja de entrar a subastas. Aflojar el target es lo que abre volumen (a más CPA).
**Real:** si quieres crecer, aflojas en pasos del 10–15% con presupuesto que acompañe; si quieres proteger margen, aprietas (ver 74-tROAS-escalar). Es la confusión más cara del bidding.

### Mito 7: "PMax/AI Max sirve para cualquier cuenta"
**Falso para presupuestos chicos.** PMax y AI Max necesitan volumen de conversiones (≥30/mes) y buenos activos/feed para optimizar. Con poca plata reparten el presupuesto en baja intención y gastan a ciegas.
**Real:** con micro-presupuesto, solo Search de alta intención + marca (ver 79-micro). PMax/AI Max son para cuando Search ya está maduro y hay datos que alimentar (ver 73, 12-PMax, `actualizacion-2026-06`).

### Mito 8: "El Search de marca es puro crecimiento porque tiene ROAS altísimo"
**Falso a escala.** Mucha de esa gente te buscó por nombre y **te iba a comprar igual**; el ROAS espectacular esconde poca incrementalidad.
**Real:** la marca es defensa barata y casi obligatoria con poca plata, pero a escala mídela por incrementalidad, no por el ROAS reportado (ver 39-marca-generico, 65-incrementalidad, 78-grandes).

## Tabla resumen

| Mito | Realidad 2026 |
|---|---|
| Más keywords = mejor | Intención > cantidad; menos y mejores + negativas |
| Exact siempre gana | Broad + Smart Bidding + negativas suele capturar más intención |
| Pausa lo de ayer | Juzga por 1 ciclo de conversión y volumen, no por 24h |
| Duplica para resetear | Tiras el aprendizaje pagado; diagnostica y arregla |
| Broad es basura | Broad bien mantenido es palanca de crecimiento |
| Apretar = más volumen | Apretar = menos volumen; aflojar = más (a más CPA) |
| PMax sirve para todos | Necesita volumen+activos; no para micro-presupuesto |
| Marca = crecimiento | A escala es atribución regalada; mide incrementalidad |

El hilo común: los mitos vienen de tratar al sistema como si fuera 2015 (manual, exact, reacción diaria). El Google Ads de hoy premia **disciplina + señales de conversión limpias + paciencia con el aprendizaje** (ver 13-smart-bidding, 14-conversion). Y validar cualquier "hack" contra TUS datos, no contra un video.

## Errores comunes — blacklist

- **Inflar la lista de keywords creyendo que cubre más.** Diluye datos y multiplica el ruido a gestionar; la intención es lo que captura, no el conteo.
- **Forzar todo a exact "por control".** Pierdes volumen de búsquedas válidas que se escriben distinto; el algoritmo entiende intención mejor que tu lista literal.
- **Pausar por el rendimiento de ayer.** Un día es ruido; matas ganadores y reinicias aprendizaje sin parar (ver 71-kill).
- **Duplicar campañas para "resetear".** Tiras el aprendizaje ya pagado y empiezas de cero a ciegas (ver 75-troubleshoot).
- **Apagar broad por prejuicio.** Bien manejado captura intención que no anticipaste; el problema casi siempre es falta de negativas (ver 22-negativas).
- **Apretar el target esperando más volumen.** Es exactamente al revés (ver 74).
- **Prender PMax/AI Max con poca plata.** Sin volumen ni activos, gasta a ciegas (ver 79).
- **Creerle a cualquier "hack" sin probar contra TUS datos.** Lo que funcionó en otra cuenta/país/nicho puede no aplicar; valida con tu propia data (ver 65-incrementalidad).
- **Tratar al algoritmo como tonto.** Pelear contra Smart Bidding con micro-gestión manual constante casi siempre rinde peor que darle señales limpias y dejarlo aprender (ver 13-smart-bidding).
