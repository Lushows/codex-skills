# 118 · Checklist pre-lanzamiento de un render GPU (para no quemar dinero)

> Cada render fallido SE COBRA. Antes de mandar un job largo, corre esta lista. Nace de perder ~$1-2
> por job en fallos evitables (timeout, imagen vieja, audio mal medido).

## Antes de enviar
- [ ] **Imagen/tag correctos**: ¿el endpoint corre el build que crees? Confirma en **Releases** el tag.
      Si pinaste un SHA, ¿el build de GHCR ya está VERDE? (IMAGE_NOT_FOUND = timing).
- [ ] **Execution Timeout** ≥ `cold_start + N·t_segmento + margen`. Para 1 min LongCat: **≥2400s**.
      Ver [[112-execution-timeout-cold-start-economics]].
- [ ] **num_segments esperado**: calcula `3.72 + (N-1)·3.2` y compáralo con la duración del audio.
      ¿El **cap** (`LIPSYNC_MAX_SEGMENTS`) cubre tu audio? Ver [[114-video-segmentado-largo-clip]].
- [ ] **Inputs frescos y correctos**: la imagen y el audio son los ACTUALES (no reusados de un job
      previo en worker caliente). El worker debe descargar fresco y limpiar IN/OUT por job.
- [ ] **Audio normalizado** a 16kHz mono (si no, num_segments se rompe y el sync sufre).
- [ ] **¿Cold o warm?** Sin Network Volume, asume frío (~40 min, re-baja 44GB). Avisa al usuario.
- [ ] **Estima el costo**: `exec_time_seg · RUNPOD_RATE_PER_SEC`. Usa una tarifa REAL (A100/H100 ≈
      0.0008-0.0012/s), no el placeholder 0.00019. Ver [[30-finops-gpu]].
- [ ] **El resultado es durable**: ¿hay poller de servidor que guarde el video aunque cierres el
      navegador? Ver [[115-async-render-largo-poller-durable]].

## Durante el render (cómo leer que va bien)
- [ ] **Logs avanzan**: los timestamps cambian y el segmento sube (`Generating segment 8...`, `9...`).
      Congelado en un segmento intermedio = probable kill por timeout.
- [ ] Ignora el header "0 running workers" (lag de UI). Cree a **Logs** y **Requests**.

## Si falló
- [ ] **Requests**: `Failed` + `Execution time`. Si ≈ tu timeout → era el timeout (súbelo). Si << timeout
      con traceback → OOM/modelo/input (otra cascada de debug, ver SKILL.md).
- [ ] **¿Se produjo algo en R2?** Si el job llegó al upload antes de morir, el MP4 puede estar en la
      nube aunque la app no lo guardara → recupéralo desde el bucket.

## Validar barato antes de ir a producción
- [ ] Primer test con audio **corto** (~30s, 8-10 segmentos, ~15-18 min, ~$0.50) para confirmar el
      pipeline end-to-end. Solo cuando pase, lanza el largo. **Nunca debugees con el render de 40 min.**

Cruza con [[111-longcat-avatar-runpod-produccion]] y [[19-load-testing-capacity-planning]].
