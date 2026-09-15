# 181 — A/B testing y experimentos

Probar cambios con rigor en vez de "cambiar y ver qué pasa". Un experimento te dice si una idea
realmente mejora el negocio o si solo lo creíste. Sirve para precio, copy, oferta, página, flujo.

## Por qué importa (la trampa de "me parece que sí")
Sin experimento, atribuyes a tu cambio cosas que pasaron por azar, estacionalidad o suerte. El A/B
testing separa la señal del ruido: **mismo período, mismo público, dos versiones**, y comparas.

- **Grupo control (A):** la versión actual (lo que ya tienes). Es tu referencia.
- **Grupo tratamiento (B):** la versión nueva (el cambio que quieres probar).
- **Aleatorización:** cada persona cae en A o B al azar (par/impar, mitad y mitad). Esto neutraliza
  diferencias entre grupos.
- **Variable única:** cambia UNA cosa por test. Si cambias precio Y foto Y texto a la vez, no sabrás
  cuál movió la aguja.

## El método en 6 pasos
1. **Hipótesis clara** (formato): "Si [cambio], entonces [métrica] subirá de X% a Y%, porque [razón]".
2. **Una métrica primaria** (la que decide): conversión, ticket promedio, tasa de respuesta. Define
   también 1-2 "métricas guardrail" que NO deben empeorar (ej. devoluciones, quejas).
3. **Tamaño mínimo de muestra y duración:** cuántas personas y cuántos días (ver fórmula abajo).
4. **Correr A vs B en paralelo**, sin tocar nada más, hasta llegar al tamaño/tiempo planeado.
5. **Medir y decidir** con un mínimo de rigor (significancia, ver abajo).
6. **Iterar:** gana el mejor, ese pasa a ser el nuevo control, y pruebas la siguiente idea.

## Qué testear (de mayor a menor impacto típico)
| Palanca | Ejemplos de variante B |
|---|---|
| **Oferta** | combo vs. unidad, envío gratis vs. descuento, garantía 30 días |
| **Precio / anclaje** | $120k vs $129.900; mostrar 3 planes vs 2 (ver 57) |
| **Copy / titular** | "Mejora tu enfoque" vs "Concentración sin café a las 3pm" |
| **Llamado a la acción** | "Comprar" vs "Pedir por WhatsApp" |
| **Imagen / prueba social** | foto producto vs persona usándolo; testimonio visible |
| **Flujo** | 1 paso de checkout vs 3 pasos; pedir menos datos |

Prioriza por **alcance × impacto esperado ÷ esfuerzo**. Lo que ve más gente y es barato de cambiar, primero.

## Significancia básica para no técnicos
"Significativo" = la diferencia es lo bastante grande para que no sea casualidad. Tres reglas prácticas:

- **No decidas con números chicos.** Con 20 visitas por lado, casi nada es confiable. Regla burda:
  apunta a **al menos ~100 conversiones sumadas** entre A y B antes de concluir (mejor más).
- **Regla del traslape:** estima un margen de error aproximado por grupo con
  `margen ≈ 1 / √(conversiones del grupo)`. Si los rangos A y B se traslapan, **no hay ganador aún**.
- **Una sola decisión, un solo test.** No mires el resultado cada hora y pares cuando "va ganando B":
  eso infla los falsos positivos. Fija duración mínima (p. ej. 1-2 semanas completas para cubrir el
  ciclo semanal) y respétala.

Herramientas que calculan significancia gratis: buscadores de "A/B test significance calculator".
Para el dato bueno de tu tasa actual y volumen, mídelo en tu propio negocio (ver 21).

## Ejemplo numérico (cifras ilustrativas)
Tienda de hongos funcionales. Hipótesis: "Si ofrezco **combo 3x2** en la página de Melena, la
conversión sube de 4% a 6% porque baja la fricción de elegir cantidad".

| | A (control: unidad) | B (tratamiento: combo) |
|---|---|---|
| Visitas | 1.000 | 1.000 |
| Compras | 40 | 58 |
| Conversión | 4,0% | 5,8% |
| Ticket promedio | $120.000 | $300.000 (3 unidades) |

Chequeo de traslape (aprox):
- A: margen ≈ 1/√40 ≈ 0,16 → 4,0% ± ~0,6 pts → rango ~3,4%–4,6%
- B: margen ≈ 1/√58 ≈ 0,13 → 5,8% ± ~0,8 pts → rango ~5,0%–6,6%

Los rangos **no se traslapan** → B gana en conversión. Y como el ticket también sube, el ingreso por
1.000 visitas pasa de `40 × $120k = $4,8M` a `58 × $300k = $17,4M`.

**Pero revisa el guardrail:** ¿el margen del combo aguanta el descuento? Si el combo 3x2 implica
regalar una unidad de costo $40k, tu margen por venta cae; calcula la utilidad, no solo el ingreso
(ver 53, 144). Un test que sube ingreso pero hunde margen NO es una victoria.

## Cuando no tienes tráfico para un A/B clásico
Negocios chicos / B2B / pocos clientes:
- **Test secuencial:** semana 1 versión A, semana 2 versión B (ojo con estacionalidad; evita fechas raras).
- **Pre/post con sentido común:** mide 2 semanas antes y 2 después del cambio, y pregunta "¿pasó algo
  más?" (campaña, festivo, clima).
- **Tests cualitativos:** muestra A y B a 5-8 clientes y pregunta cuál y por qué. No es estadístico,
  pero detecta confusiones rápido.
- **WhatsApp / mensajes:** alterna 2 plantillas de mensaje (par/impar del número) y compara tasa de
  respuesta o de compra (ver 127 para growth y canales).

## Errores comunes
- **Cambiar varias cosas a la vez** → no sabes qué funcionó.
- **Parar el test cuando "va ganando"** (peeking) → falso positivo casi garantizado.
- **Muestra diminuta** → ruido disfrazado de hallazgo.
- **Optimizar la métrica equivocada** (clics en vez de ventas, ventas en vez de margen).
- **Ignorar guardrails** → subes conversión y disparas devoluciones o quemas margen.
- **No documentar:** sin bitácora de qué probaste y qué pasó, repites tests y olvidas aprendizajes.
- **Generalizar de un test único:** un resultado en un público/temporada no aplica a todos para siempre.

## Bitácora de experimentos (plantilla mínima)
| Fecha | Hipótesis | Métrica primaria | A | B | Tamaño | Ganador | Decisión |
|---|---|---|---|---|---|---|---|

Guárdala. En 6 meses vale oro: te dice qué mueve de verdad a TU cliente y deja de ser opinión.

## Siguiente paso típico
Escribe UNA hipótesis con el formato "Si… entonces… porque…", define la métrica primaria y un
guardrail, y lanza tu primer A/B de la palanca de mayor impacto (precio u oferta, ver 57 y 144). No
decidas hasta sumar suficiente volumen y revisar el margen, no solo el ingreso.
