# 30 — Velas japonesas y patrones

Una **vela** resume la pelea entre compradores y vendedores en un periodo (en nuestro caso, 1 hora).
Los patrones de velas son el alfabeto del gráfico — útiles para leer, peligrosos para "predecir".

## Anatomía de una vela

```
        │  ← mecha superior (hasta dónde subió el precio y lo rechazaron)
      ┌─┐
      │ │  ← cuerpo (distancia entre apertura y cierre)
      └─┘
        │  ← mecha inferior (hasta dónde bajó y lo compraron)
```

| Elemento | Qué cuenta |
|---|---|
| **Cuerpo grande** | Un bando dominó claramente (verde = compradores, rojo = vendedores) |
| **Cuerpo pequeño** | Indecisión: nadie ganó |
| **Mecha larga** | El precio fue hasta allá y lo devolvieron — rechazo de ese nivel |
| **Cierre** | El dato más importante: dónde quedó el precio al final de la hora |

## Patrones básicos (los tres que vale la pena conocer)

| Patrón | Cómo se ve | Qué sugiere |
|---|---|---|
| **Martillo** | Cuerpo pequeño arriba, mecha inferior larga | Vendedores empujaron, compradores recuperaron. Posible piso — *si aparece sobre un soporte* |
| **Envolvente alcista** | Vela verde cuyo cuerpo "traga" el de la roja anterior | Cambio de mando de vendedores a compradores |
| **Doji** | Cuerpo casi inexistente (apertura ≈ cierre) | Indecisión pura. Solo, no dice nada; tras un rally largo, posible agotamiento |

## La fiabilidad REAL (la parte honesta)

- Los estudios estadísticos serios sobre patrones de velas **aislados** encuentran tasas de acierto
  cercanas al azar. Un martillo en medio de la nada no significa nada.
- Lo que da valor es el **contexto**: un martillo *sobre un soporte* (`31`), *en régimen trending-up*
  (`03`), *con RSI saliendo de sobreventa* — ahí la vela es la confirmación, no la señal.
- Regla mental: la vela responde "¿quién ganó esta hora?", nunca "¿qué pasará la próxima?".
- Hay decenas de patrones con nombres exóticos (tres cuervos, bebé abandonado…). Memorizar el
  catálogo entero es coleccionismo, no trading. Con rechazo, dominio e indecisión se lee el 90%.

## Cómo aplica al AGENTE TRADING

- El bot no detecta patrones de velas en código, y está bien: son subjetivos y de baja fiabilidad
  aislada. Claude sí puede leerlos al interpretar las velas crudas que recibe.
- Uso correcto en el prompt de convicción: una mecha superior larga en la zona de resistencia
  debería BAJAR convicción de un LONG (rechazo visible) — es exactamente la lección FOMO de `10`:
  las 3 entradas perdedoras se hicieron comprando velas extendidas lejos de la SMA20.
- Si algún día se codifica algo, que sea lo objetivo: tamaño de mecha vs cuerpo, no "detectar
  hombro-cabeza-hombro" (ver crítica en `39`).
