# 362 · Error handling y patrones de resiliencia (que el fallo de uno no tumbe el sistema)

> Un endpoint GPU vive en un mundo hostil: HuggingFace 503, OOM mid-run, webhook que no responde, R2 lento.
> La resiliencia no es "que nada falle" — es **contener el fallo** para que degrade en vez de caer en cascada.

## El principio: fallar rápido, fallar acotado, NUNCA en silencio
El peor error es el que se traga: un `try/except: pass` que devuelve un video corrupto o un `200 OK` vacío.
El job queda "exitoso" pero el cliente recibe basura → debugging imposible. **Todo fallo se registra, se clasifica
(transitorio vs permanente) y se propaga con contexto** (job_id, stage, traceback). Si no sabes reintentar, no reintentes.

## Retries con backoff exponencial + jitter
Solo reintentar errores **transitorios** (5xx, timeout, connection reset, rate-limit 429). NUNCA reintentar
4xx de validación (input malo → reintentar 1000 veces da el mismo error y quema GPU).

```python
import random, time
TRANSIENT = (TimeoutError, ConnectionError)

def with_retry(fn, tries=4, base=2.0, cap=30.0):
    for i in range(tries):
        try:
            return fn()
        except TRANSIENT as e:
            if i == tries - 1:
                raise
            sleep = min(cap, base * 2**i) + random.uniform(0, 1)  # jitter mata el thundering herd
            time.sleep(sleep)
```

Jitter es obligatorio: sin él, 50 workers que fallan a la vez reintentan **al mismo instante** → re-tumban
el servicio que apenas se levantó. El cap evita esperas absurdas (2^10 = 17 min).

## Circuit breaker: deja de golpear lo que está caído
Si un dependiente (API premium de fallback, R2, webhook) falla N veces seguidas, **abre el circuito**: deja de
llamarlo por T segundos y falla rápido. Tras T, prueba con 1 request (half-open). Si pasa, cierra; si no, re-abre.

| Estado | Comportamiento |
|---|---|
| `closed` | Pasa todo. Cuenta fallos. ≥ umbral (ej. 5) → `open` |
| `open` | Rechaza inmediato sin llamar (ej. 30s). Protege al caído y libera tus workers |
| `half-open` | Deja pasar 1 sonda. Éxito → `closed`; fallo → `open` otra vez |

Sin breaker, un dependiente lento **consume todos tus slots GPU** esperando timeouts → tu servicio sano muere
por agotamiento de recursos. Esto es el fallo en cascada.

## Timeouts en TODA llamada de red
Un request sin timeout es una bomba: el default de muchos clientes es **infinito**. Un socket colgado retiene
un worker GPU (caro) para siempre. Regla: timeout de conexión (3-5s) + timeout de lectura acorde a la operación
(descarga de 44GB ≠ ping). El timeout del cliente debe ser **mayor** que el del servidor, nunca al revés.

## Bulkhead: aísla por compartimentos
Como los mamparos de un barco: una vía de agua inunda **un** compartimento, no el casco. En la práctica:
pools de conexiones separados por dependiente, límites de concurrencia por tipo de job. Si los jobs de "video largo"
saturan, que NO se lleven por delante los slots de "imagen rápida". Cuotas independientes = fallo contenido.

## Graceful degradation: algo es mejor que nada
Cuando el camino ideal falla, ofrece uno peor pero funcional. Ejemplos del stack visual:
- Modelo HQ OOM → reintenta a menor resolución/fps antes de rendirse.
- GPU serverless saturada → cae a API premium (Higgsfield/Runway) vía el breaker.
- R2 caído al subir → guarda en disco local y reintenta async, no pierdas el render ya pagado.

## Idempotencia: el reintento no debe duplicar
Si reintentas un job que **sí** se completó (pero perdiste la respuesta), no generes 2 videos ni cobres 2 veces.
Clave de idempotencia por job → si ya existe el resultado, devuélvelo en vez de recomputar. Esto hace que retries,
DLQ y at-least-once delivery sean seguros.

## Errores que muerden
- `except Exception` genérico que oculta OOM, KeyboardInterrupt y bugs de código juntos → captura clases específicas.
- Reintentar el job entero cuando solo falló el upload → desperdicias minutos de GPU ya gastados. Reintenta la **etapa**.
- Backoff sin cap ni límite de intentos → loop infinito que parece "colgado".
- Loggear el error pero devolver 200 igual → el monitoreo ve verde mientras los clientes sufren.

Cruza con [[160-disaster-recovery-cascada-fallback]] y [[141-webhooks-hmac-idempotencia-dlq-jobs-gpu]].
