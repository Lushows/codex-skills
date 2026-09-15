# 246 · Desplegar modelos: canary / shadow / blue-green / rollback

> Cambiar el modelo de generación de avatares en producción "a lo bestia" (swap directo) es ruleta:
> si el nuevo checkpoint genera caras peores, lo descubres por las quejas. Las estrategias de despliegue
> progresivo te dejan probar el modelo nuevo con tráfico real **sin** arriesgar a todos los usuarios.

## Las cuatro estrategias
| Estrategia | Cómo | Impacto si falla | Para qué |
|---|---|---|---|
| **Shadow** | El modelo nuevo recibe **copia** del tráfico; su salida se **descarta** (solo se loguea) | **Cero** (usuario no la ve) | Cambios de alto riesgo: nueva arquitectura, schema de salida distinto |
| **Canary** | Enrutas un % creciente al nuevo: 1% → 5% → 20% → 50% → 100% | Limitado al % expuesto | Validación gradual con métricas reales |
| **Blue-Green** | Dos entornos idénticos; switch atómico del 100% del tráfico | Total, pero **rollback instantáneo** (revertir el LB/DNS) | Cuando no quieres splitting; rollback en segundos |
| **A/B** | Variantes en paralelo, medición de métrica de negocio | Según diseño | Decidir cuál modelo convierte/gusta más |

## El orden correcto para un modelo generativo
1. **Shadow primero**: el modelo nuevo procesa copia del tráfico de generación, guardas sus outputs y los
   comparas offline (FID/FVD/CLIP + revisión humana de samples). Cero usuarios afectados. Ideal cuando el
   nuevo modelo cambia el schema de salida o la arquitectura (el caso típico al cambiar de checkpoint base).
2. **Canary** después: si shadow se ve bien, enruta 1% → 5% → 20% → 50% → 100%, midiendo en cada escalón.
3. **Blue-green** si quieres switch atómico con rollback en segundos en vez de rampa.

Shadow valida **calidad** sin riesgo; canary valida **calidad + comportamiento bajo carga real** con riesgo
acotado. Para generativo, shadow es especialmente valioso porque la calidad visual no se ve en la loss.

## Rollback automático (no opcional)
Define umbrales explícitos y un controlador que enrute el 100% de vuelta al baseline **sin intervención
humana** si se cruzan. Para avatares/video, métricas-gatillo útiles:
- **p99 de latencia** sube > X% (ej. 40%) → el modelo nuevo es más lento/OOM intermitente.
- **Tasa de fallo/refusal** o de jobs que crashean sube > Y%.
- **Coste-por-request** excede el presupuesto (modelo nuevo más pesado = más segundos GPU).
- **Score de calidad** (eval automático sobre samples) cae bajo umbral (cruza con [[164-evals-calidad-avatar-video]]).

## Aplicado a GPU serverless (RunPod & co.)
- El "load balancer" suele ser **tu cola de jobs**: enruta un % de jobs al endpoint con el modelo nuevo
  (canary) y el resto al viejo. Dos endpoints/versiones de worker corriendo en paralelo.
- **Blue-green** = dos endpoints; el switch es cambiar a cuál apunta tu app. Mantén el viejo caliente hasta
  confirmar el nuevo → rollback = re-apuntar (segundos).
- **Shadow** = duplicas el job al endpoint nuevo en modo "descarta resultado, solo loguea sample+métricas".
  Cuesta GPU extra (corres dos modelos) → hazlo por una ventana acotada, no permanente.

## Detalles que muerden
- **Coste**: shadow y canary corren **dos modelos a la vez** → doble factura GPU durante la ventana. Acótala.
- **Cold-start sesga el canary**: el endpoint nuevo arranca frío y parece lento. Pre-caliéntalo (o
  pre-popula el volumen de pesos, [[113-network-volume-modelos-grandes]]) antes de medir latencia.
- **Versiona qué modelo sirve cada despliegue**: liga el worker a un checkpoint del registry
  ([[18-model-registry-versionado]]) para que el rollback sea "volver a la versión N", no adivinar.
- **El eval debe ser automático** para que el rollback dispare solo; revisión humana no escala como gatillo.

Cruza con [[16-cicd-modelos-workers]] y [[164-evals-calidad-avatar-video]].
