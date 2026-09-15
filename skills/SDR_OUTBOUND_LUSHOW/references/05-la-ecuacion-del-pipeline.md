# 05 — La ecuación del pipeline

Este es el módulo más importante del Bloque 0. Es la **matemática que convierte el outbound de lotería a máquina**: la fórmula que conecta tu actividad (cuánta gente tocas) con tu revenue (cuánto vendes), pasando por respuestas, reuniones y oportunidades. Si conoces tu ecuación, puedes **predecir** cuánto pipeline vas a generar y **calcular hacia atrás** cuántos contactos necesitas para llegar a tu meta. Sin ella, estás adivinando.

## El principio: el embudo es una cadena de porcentajes

El outbound es un embudo. En cada etapa se cae un porcentaje de la gente, y lo que sobrevive pasa a la siguiente. La cadena es:

```
Contactos → Respuestas → Respuestas positivas → Reuniones agendadas
   → Reuniones realizadas → Oportunidades (SQL) → Clientes cerrados → Revenue
```

Cada flecha tiene una **tasa de conversión** (qué % pasa a la siguiente etapa). Multiplicas las tasas y sabes cuántos contactos necesitas para cerrar X. Como conoces cada tasa, sabes también **dónde se rompe** tu outbound cuando los números no dan (diagnóstico en `83`).

## Las etapas y sus tasas típicas 2026 (cold email B2B)

Números realistas y **defendibles** para outbound frío bien hecho (no spray-and-pray). Varían mucho por vertical y calidad de lista — úsalos como punto de partida, no como ley:

| Etapa | Métrica | Rango típico | Nota |
|---|---|---|---|
| Contacto → Respuesta | reply rate | 3%–8% | El total de respuestas (incluye negativas) |
| Respuesta → Positiva | positive reply rate | 20%–40% de las respuestas | Interés real, no "quítame de la lista" |
| Positiva → Reunión agendada | 40%–60% | Aquí entra tu manejo de respuesta (ver `64`, `69`) |
| Agendada → Realizada | show rate | 60%–80% | Los no-shows se recuperan (ver `75`) |
| Realizada → Oportunidad (SQL) | 40%–60% | Calificación del SDR (ver `70`) |
| Oportunidad → Cierre | win rate | 15%–30% | **Esto ya es trabajo del AE → `ventas_lushows`** |

Una regla gruesa de campo muy usada: **~1% de los contactos frío termina en reunión agendada** con una campaña decente. Es decir, ~100 contactos ≈ 1 reunión. Con lista y copy excelentes sube a 2–3%; con spam baja a ~0.

## La fórmula, hacia atrás desde tu meta

Lo útil es calcular **cuántos contactos necesitas** para tu meta de ventas. Se hace al revés del embudo, dividiendo:

```
Contactos necesarios =
  Clientes meta
  ÷ (win rate)
  ÷ (oportunidad → SQL)
  ÷ (show rate)
  ÷ (positiva → agendada)
  ÷ (respuesta → positiva)
  ÷ (reply rate)
```

## Ejemplo numérico completo (LatAm, agencia vendiendo servicio de $2M COP/mes)

Meta: **cerrar 4 clientes nuevos al mes.** Tasas asumidas (conservadoras):

```
Win rate (opp→cierre):        20%   (0.20)
Opp→SQL (realizada→opp):      50%   (0.50)
Show rate (agendada→hecha):   70%   (0.70)
Positiva→agendada:            50%   (0.50)
Respuesta→positiva:           30%   (0.30)
Reply rate (contacto→resp):    5%   (0.05)

Reuniones realizadas necesarias = 4 / 0.20 / 0.50 = 40 reuniones realizadas
Reuniones agendadas             = 40 / 0.70 ≈ 57 agendadas
Respuestas positivas            = 57 / 0.50 = 114 positivas
Respuestas totales              = 114 / 0.30 = 380 respuestas
CONTACTOS NECESARIOS            = 380 / 0.05 = 7.600 contactos/mes
```

**Resultado: ~7.600 contactos al mes (~380/día en 20 días hábiles) para cerrar 4 clientes.** Ese número te dice de inmediato si tu plan es realista: 380 contactos/día requiere varios buzones y automatización (ver `44`, `48`), o subir las tasas (mejor lista/copy) para necesitar menos volumen. Nota cómo un pequeño ojo en el reply rate —pasar de 5% a 8%— baja los contactos de 7.600 a ~4.750: **mejorar la tasa cuesta menos que subir el volumen** (por eso invertimos en lista y copy antes que en más buzones).

> ⚠️ Estos cálculos deben salir **exactos** cuando trabajes con los números reales del usuario. Ejecútalos/verifícalos con `Matematicas_lushows` — nunca de memoria.

## Las dos palancas: volumen y tasas

Solo hay dos formas de generar más pipeline:

1. **Subir el volumen** (más contactos): más buzones, más SDRs, más automatización. Escala lineal pero cuesta infra y gente, y tiene techo de deliverability (ver `44`).
2. **Subir las tasas de conversión**: mejor lista (ICP más afilado, `10`), mejor copy (`50`–`56`), mejor timing/señal (`14`, `37`), mejor manejo de respuestas (`64`). Escala sin costo marginal y es casi siempre la mejor inversión primero.

**Orden correcto:** primero exprime las tasas (lista + copy + señal), y solo cuando ya conviertes bien, sube el volumen. Subir volumen sobre una campaña que convierte mal solo multiplica el desperdicio.

## Errores comunes (qué NO hacer)

- **No medir las etapas intermedias.** Si solo miras "correos enviados" y "clientes cerrados", no sabes dónde se cae la gente y no puedes arreglar nada. Mide cada tasa (ver `80`, `81`).
- **Usar tasas optimistas.** Planear con 10% de reply rate cuando el real es 4% te deja a menos de la mitad de tu meta. Sé conservador.
- **Escalar volumen antes de arreglar tasas.** Multiplica el gasto sin multiplicar resultados.
- **Confundir el win rate con tu trabajo.** El cierre (opp→cliente) es del AE/`ventas_lushows`; el SDR es dueño de contacto→reunión. No te cuelgues un mal win rate que es del cierre.

## Siguiente paso

Toma tu meta real de clientes/mes y corre esta ecuación con tus tasas (o las típicas de arriba si aún no tienes datos). El número de contactos/mes que salga es el que dimensiona todo lo demás: cuántas cuentas necesitas en la lista (`17`), cuántos buzones (`44`), si necesitas equipo (`89`). Verifica el cálculo con `Matematicas_lushows` y lleva el embudo en un dashboard (`80`, `144`).
