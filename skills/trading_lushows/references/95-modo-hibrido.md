# 95 — Modo híbrido (el primer mes con dinero real)

> Durante el primer mes live, el bot NO ejecuta solo: propone, notifica, y Luis confirma.
> Es la rueda de entrenamiento entre "todo simulado" y "todo automático".

## El flujo

```
Señal (convicción ≥8) → bot arma la orden completa (entrada, stop, target, tamaño)
  → notifica a Luis (WhatsApp/dashboard) con TODO el detalle
  → Luis responde: APROBAR o RECHAZAR (con ventana de tiempo)
  → si aprueba → orden real + OCO al exchange
  → si rechaza o expira → no se opera; se registra igual que un trade "fantasma"
```

Importante: el bot hace TODO el trabajo menos apretar el botón. Luis no calcula nada, no elige
precios, no ajusta tamaños. Si Luis tiene que pensar la orden, el híbrido está mal diseñado.

## ¿Qué aprueba o rechaza Luis? (y qué NO)

| Luis SÍ decide | Luis NO decide |
|---|---|
| "¿Ejecuto esta orden tal cual?" (sí/no) | Cambiar el stop, el target o el tamaño |
| Rechazar si ve algo raro (noticia enorme, número que no cuadra) | "Mejorar" la entrada esperando mejor precio |
| Activar kill switch si algo huele mal | Abrir trades que el bot no propuso |

La regla existe por una razón: si Luis edita las órdenes, el track record deja de ser del
sistema y pasa a ser de Luis — y entonces no medimos nada.

## Registrar TODO, incluso lo rechazado

Cada propuesta se guarda con su resultado hipotético (como si se hubiera ejecutado). Al final
del mes se compara:

- Trades aprobados: resultado real (con slippage y fees reales).
- Trades rechazados/expirados: resultado que HABRÍAN tenido.

Si los rechazados habrían ganado más que los aprobados, Luis está filtrando mal (miedo, sesgo)
y el híbrido lo demuestra con datos, no con opiniones.

## Medir la fricción

El híbrido tiene un costo: la demora entre señal y confirmación. Se mide en cada trade:
minutos entre notificación y aprobación, y diferencia entre el precio de la señal y el precio
de ejecución. En swing 1h una demora de minutos suele ser tolerable — pero se MIDE, no se asume.
Si la fricción come el edge (propuestas que expiran de madrugada, slippage por demora), es un
dato para la decisión de graduar.

## Cuándo graduar a auto-ejecución

Después de 1 mes híbrido se gradúa si TODO esto se cumple:

1. Cero incidentes técnicos (órdenes correctas, OCO siempre puestos, reconciliación limpia).
2. Tasa de aprobación alta (≈90%+): si Luis rechaza mucho, o el bot propone mal o Luis no
   confía — ambas cosas hay que resolverlas ANTES de soltar el control.
3. Los rechazos de Luis no mejoraron el resultado (ver arriba): la mano humana no agrega valor.
4. Luis declara explícitamente que puede NO mirar el teléfono y dormir tranquilo.

Si no se cumple, se extiende el híbrido otro mes. No es fracaso: es barato comparado con
descubrir un bug en modo auto.

## Cómo aplica al AGENTE TRADING

- Es condición #3 del go-live (módulo 08): auto-ejecución real SOLO tras 1 mes híbrido limpio.
- Requiere construir el flujo de notificar/confirmar (WhatsApp o dashboard) en Fase 8 y
  probarlo en testnet como todo lo demás (módulo 90).
- El umbral de convicción ≥8 no cambia en híbrido: el filtro es el mismo, solo se agrega la
  confirmación humana encima.
