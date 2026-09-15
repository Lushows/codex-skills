# 129 — A/B testing de copy avanzado

El módulo `65` te dio los fundamentos: una variable a la vez, muestra suficiente, calcula significancia. Este módulo es la capa avanzada para cuando ya corres pruebas rutinariamente y quieres exprimirlas: **cómo pensar el tamaño de muestra con números reales, qué significa "significancia" de verdad, cómo priorizar qué variar cuando tienes 20 ideas, y las trampas estadísticas que hacen que "ganadores" desaparezcan al escalar.** Toda la matemática dura (calcular n exacto, correr la prueba de significancia, potencia estadística) se rutea a `Matematicas_lushows` — aquí armas el experimento bien para que ese cálculo signifique algo.

## El principio: el copy no se opina, se mide — pero medir mal es peor que no medir

Un A/B con muestra chica no es "una pista"; es una fuente de conclusiones falsas que te hacen tomar decisiones peores que lanzar una moneda, porque *crees* que aprendiste. El outbound tiene un enemigo estadístico particular: **tasas base bajísimas** (reply positivo de 1–4%). Con eventos tan raros, el ruido domina y hacen falta muestras grandes para distinguir señal de azar. Todo este módulo pelea contra ese enemigo.

## Qué variar: la jerarquía de impacto (y por qué el copy va casi al final)

La verdad incómoda del A/B de copy: **el copy es la palanca MÁS chica.** Optimizar el asunto cuando el problema es la lista es pulir la manija de la puerta equivocada (ver `65`). Orden real de impacto:

| Nivel | Palanca | Impacto relativo |
|---|---|---|
| 1 | **Lista / segmento / ICP** (ver `10`, `20`) | Enorme — el mismo copy a otro público cambia todo |
| 2 | **Oferta / ángulo** (qué problema, qué promesa) | Muy alto |
| 3 | **Trigger / timing** (ver `128`, `62`) | Alto |
| 4 | **Opener / personalización** (ver `52`, `53`) | Medio |
| 5 | **CTA** (ver `55`) | Medio-bajo |
| 6 | **Asunto** (ver `51`) | Bajo (y open rate es poco fiable, ver `65`) |
| 7 | **Palabras/spintax** (ver `121`) | Casi nulo para conversión |

Prueba de arriba hacia abajo. No optimices el asunto (nivel 6) mientras el nivel 1 está sin resolver. El "copy avanzado" empieza por aceptar que a veces el problema no es el copy.

## Tamaño de muestra: la matemática que casi nadie hace

La pregunta correcta no es "¿cuántos correos mando?" sino "**¿cuántos correos necesito para detectar la mejora que me importa, con confianza?**". Eso depende de tres cosas:

1. **Tasa base (p)** — tu reply positivo actual (ej. 3%).
2. **Efecto mínimo detectable (MDE)** — la mejora más pequeña que te interesaría accionar (ej. de 3% a 4% = mejora relativa del 33%).
3. **Confianza (95%) y potencia (80%)** — potencia = probabilidad de detectar el efecto si existe de verdad.

Cuanto más baja la tasa base y más pequeño el efecto que quieres detectar, **más gigante** la muestra. Un ejemplo del orden de magnitud (verifícalo siempre con `Matematicas_lushows`):

```
Detectar 3% → 4,5% en reply positivo (95% conf, 80% potencia):
  ≈ 1.500–2.000 envíos POR VARIANTE.

Detectar 3% → 3,3% (mejora chica):
  decenas de miles por variante — inviable para la mayoría.
```

Lección práctica: **con volumen de PYME, solo puedes detectar mejoras grandes.** Los ajustes finos de copy (3,0% vs 3,2%) son indetectables — no gastes ciclos ahí. Prueba cambios GRANDES (otro ángulo, otra oferta), donde el efecto es lo bastante grande para verse con tu muestra. Para calcular el n exacto de TU caso → dale a `Matematicas_lushows` tu tasa base, tu MDE y él te da el número.

## Significancia: qué significa el "95%" (y cómo no engañarte)

Significancia estadística al 95% = "si en realidad las dos versiones fueran iguales, vería una diferencia así de grande solo el 5% de las veces por puro azar". No significa "B es 95% mejor". Tres trampas avanzadas que arruinan pruebas técnicamente "correctas":

- **Peeking (mirar antes de tiempo).** Revisar el resultado cada día y parar cuando cruza 95% infla los falsos positivos brutalmente — porque con suficientes miradas, el ruido cruza el umbral solo. Regla: **fija el tamaño de muestra ANTES, y solo lees el resultado al alcanzarlo.** Nada de "ya va ganando, lo declaro".
- **Comparaciones múltiples.** Si pruebas 5 variantes a la vez, la probabilidad de que UNA cruce 95% por azar ya no es 5%, es ~23%. Con muchas variantes, sube el umbral o usa corrección (Bonferroni). Coméntalo con `Matematicas_lushows`.
- **Significancia estadística ≠ relevancia práctica.** Con muestras enormes, una mejora ridícula (3,00% vs 3,05%) puede dar "significativa" y no valer el esfuerzo de implementarla. Mira el **tamaño del efecto**, no solo el p-valor.

## El flujo de un A/B avanzado bien hecho

```
1. Hipótesis clara: "Cambiar el ángulo de 'ahorro de tiempo' a 'recuperar
   margen' subirá el reply positivo de ~3% a ~4,5%."   (cambio GRANDE)
2. Métrica primaria: reply positivo → reunión. (no open rate)
3. n por variante: calculado con Matematicas_lushows ANTES de lanzar.
4. Aleatorización limpia: mismo segmento, mismos días/horas (ver 62),
   mismos buzones repartidos — que la ÚNICA diferencia sea la variable.
5. Correr hasta n. Sin peeking. Sin parar antes.
6. Significancia: calcular con Matematicas_lushows al llegar a n.
7. Decisión: si pasa 95% Y el efecto vale → B es el nuevo control.
   Si no → empate, quédate con el más simple y prueba otra cosa de arriba.
8. Documentar: hipótesis, n, resultado, p-valor, decisión. Bitácora viva.
9. Meta-análisis: acumula aprendizajes entre campañas — qué ángulos
   ganan siempre en tu mercado se vuelve tu playbook (ver 90).
```

## Cuando el volumen no alcanza (la mayoría de los casos LatAm/PYME)

Si mandas 500/día no juntarás miles por variante en una semana. Opciones:
- **Acumula en el tiempo.** Corre la MISMA prueba 3–4 semanas hasta el n. Peor: no la corras si no vas a esperar.
- **Sube la métrica.** Es más fácil tener significancia en reply rate (5–10%) que en reply positivo (1–4%). Usa reply como proxy si el positivo es muy raro, sabiendo la limitación.
- **Prueba cambios grandes.** Efecto grande = menos muestra necesaria. Olvida los micro-ajustes.
- **Antes de A/B formal, usa el juicio.** Con muestra insuficiente, decidir por criterio experto (este módulo + `50`, `56`) es más honesto que fingir rigor sobre 40 correos.

## Errores comunes (qué NO hacer)

- **Peeking y parar al cruzar 95%.** La trampa #1. Fija n antes, lee al final.
- **Probar micro-cambios con volumen chico.** Indetectable. Prueba cambios grandes o no pruebes.
- **Declarar ganador sin calcular significancia.** "Se ve mejor" no es dato → `Matematicas_lushows`.
- **Optimizar open rate** (inflado en 2026, ver `65`) en vez de reply positivo → reuniones.
- **Ignorar comparaciones múltiples.** 5 variantes = 5 chances de falso positivo. Ajusta.
- **No documentar.** Sin bitácora repites pruebas y no construyes playbook (ver `90`).

## Siguiente paso

Formula UNA hipótesis de cambio GRANDE (otro ángulo u oferta, no otra palabra) y llévasela a `Matematicas_lushows` con tu tasa base y el efecto que quieres detectar para que calcule el n por variante ANTES de lanzar. Móntala en tu plataforma (ver `33`, `65`) con aleatorización limpia. Los fundamentos del A/B → `65`; qué palanca priorizar → esta jerarquía + `20` (lista) y `56` (frameworks de copy); acumular aprendizajes en tu sistema → `90`. Todo número que deba ser exacto → `Matematicas_lushows`.
