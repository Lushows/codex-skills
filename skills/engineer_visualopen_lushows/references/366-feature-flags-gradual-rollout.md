# 366 · Feature flags y rollout gradual (desplegar ≠ liberar; apaga sin re-deployar)

> Una feature flag separa **deploy** (el código está en producción) de **release** (el usuario lo ve).
> El superpoder: encender una feature al 1%, ver si arde, y apagarla en segundos **sin un nuevo despliegue**.

## Los cuatro tipos de flag (no los mezcles: su ciclo de vida difiere)
| Tipo | Propósito | ¿Permanente? |
|---|---|---|
| **Release toggle** | Esconder código a medio hacer; rollout gradual | No — bórralo al 100% |
| **Ops / kill-switch** | Apagar una integración cara o frágil en crisis | **Sí, permanente** |
| **Permission / entitlement** | Gatear features por plan/tier (free vs pro) | Sí, vive con el producto |
| **Experiment** | A/B test, asignación por bucket | No — bórralo al concluir |

Mezclar un kill-switch (permanente, crítico) con un release toggle (temporal, a borrar) lleva a apagar lo que no debías.

## Kill-switch: el flag que todo servicio GPU necesita
Cada dependencia cara o frágil va detrás de un kill-switch: la **inferencia en el endpoint propio**, el **fallback a
API premium**, el **envío de webhooks**. Cuando RunPod arde o la factura se dispara, apagas con un click —
sin esperar un build de 10 min ni un rollback. El kill-switch es resiliencia operacional, no deuda: se queda para siempre.

## Rollout gradual: 1% → 5% → 25% → 50% → 100%
No liberes al 100% de golpe. Sube por escalones y **observa entre cada uno** error-rate, latencia p95 y coste.
Automatiza el freno: si los errores superan el umbral en un escalón, **auto-rollback** del flag (no esperes al humano).

```python
def flag_on(flag, user_id, percent):
    # bucketing estable: el mismo user cae siempre del mismo lado → experiencia consistente
    h = int(hashlib.sha1(f"{flag}:{user_id}".encode()).hexdigest(), 16)
    return (h % 100) < percent
```

El hash del `user_id` (no `random()`) asegura que un usuario no vea la feature parpadear entre requests.

## Targeting: a quién le enciendes, no solo a cuántos
Antes del %, suele ir **canary dirigido**: internos primero, luego beta opt-in, luego geografía/tier. Reglas por
atributo (plan, país, versión de app, allow-list de cuentas). Combina: "internos al 100% + 5% del resto". Esto
detecta fallos con usuarios tolerantes antes de tocar a los que pagan.

## Evalúa el flag en el sitio correcto
- **Server-side** para lógica sensible/cara (qué modelo GPU corre): el cliente no debe poder forzarla.
- **Edge/cliente** para UI. Cachea la evaluación pero con TTL corto: un kill-switch debe propagar en **segundos**,
  no en minutos. El SDK con streaming de cambios (LaunchDarkly/Unleash) propaga casi instantáneo.

## Deuda de flags: el coste oculto que nadie limpia
Cada flag es un `if` → 2^N caminos de código. 20 flags olvidados = combinatoria intestable y bugs fantasma. Disciplina:
- Cada release toggle nace con **dueño + fecha de expiración**. Sin eso, no se crea.
- **Archivado trimestral**: time-to-archive sano 90–120 días. Un flag "atascado en cleanup" es el síntoma #1 de deuda.
- Trata los flags como **inventario con coste de mantenimiento**: mantén bajo el número de activos, borra el código muerto.
- Alerta sobre flags al 100% durante > X días → es código que debió fundirse ya.

## Herramientas (2026)
- **PostHog / Statsig**: mejor relación valor/precio para startup; flags + analytics + experiments integrados, free tier generoso.
- **LaunchDarkly**: gobernanza y targeting enterprise, ciclo de vida de 6 estados, kill-switches de primera clase.
- **Unleash / GrowthBook**: open-source self-hosted; Unleash modela 5 estados y vigila los "stuck in cleanup".

## Errores que muerden
- Flag sin dueño ni fecha → vive para siempre, nadie se atreve a borrarlo "por si acaso".
- Liberar al 100% sin escalones ni métricas → descubres el bug con **todos** los usuarios a la vez.
- `random()` en vez de hash del user → la feature parpadea request a request, soporte se vuelve loco.
- Kill-switch que tarda minutos en propagar (cache largo) → inútil en la crisis donde lo necesitas en segundos.
- Lógica de negocio crítica detrás de un flag de cliente → manipulable; debe ser server-side.

Cruza con [[324-ab-testing-experiments]] y [[246-canary-shadow-bluegreen-models]].
