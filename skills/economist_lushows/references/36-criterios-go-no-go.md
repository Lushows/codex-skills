# 36 — Criterios go/no-go

Sirve para decidir CON HONESTIDAD si una idea o experimento sigue, pivota o se mata. La clave: definir los umbrales (números mínimos) ANTES de ver los resultados, para no engañarte interpretando datos malos como "buenos".

## Por qué se define ANTES (y no después)

El cerebro humano racionaliza. Si lanzas un test y luego decides "qué número sería bueno", siempre encontrarás una excusa para seguir ("es que era poca gente", "el clima estaba malo"). Eso se llama **sesgo de confirmación**: ver solo lo que quieres ver.

Solución: escribe el umbral en papel/pantalla antes de testear y fírmalo con fecha. Después solo comparas: ¿pasó la línea o no? Sin debate emocional. Esto convierte una decisión de ego en una decisión de datos (ver 32 sobre cómo correr el experimento, y 03 sobre el sesgo del fundador enamorado de su idea).

## Los 3 veredictos posibles

| Veredicto | Qué significa | Qué haces |
|---|---|---|
| **GO (seguir)** | Pasó el umbral. Hay señal real. | Inviertes el siguiente nivel de tiempo/dinero. Subes la apuesta. |
| **PIVOT (girar)** | Algo funciona pero no como pensabas (otro cliente, otro problema, otro precio). | Cambias UNA variable grande y vuelves a testear. No empiezas de cero. |
| **NO-GO / KILL (matar)** | No pasó y no hay señal de rescate. | Cierras esa hipótesis. Liberas tu tiempo. Esto es una VICTORIA, no un fracaso. |

Matar rápido una mala idea es de las decisiones más rentables que existe: te ahorra meses y ahorros. El costo de seguir por terquedad casi siempre supera el costo de admitir el error (ver 37 sobre cuándo pivotar vs perseverar).

## Cómo se construye un criterio cuantitativo

Un buen criterio tiene 4 partes:

1. **Métrica** — qué mides exactamente (ej. % de gente que paga, no "interés").
2. **Umbral** — el número mínimo aceptable.
3. **Muestra mínima** — cuánta gente/datos necesitas para que cuente (10 personas no es evidencia).
4. **Plazo** — hasta qué fecha mides.

> Regla de oro: la métrica debe medir **comportamiento real con costo** (pagar, dejar tarjeta, agendar y asistir), no opiniones ("me encanta", "lo compraría"). La gente miente para no incomodarte; la billetera no miente.

## Ejemplo numérico (cifras 100% ilustrativas)

Imagina que vas a validar un servicio de meal-prep saludable. Antes de testear defines:

| Criterio | Umbral GO | Resultado del test | ¿Pasó? |
|---|---|---|---|
| Tasa de conversión (visitas → pago de reserva) | ≥ 5% | 6.2% | Sí |
| Pedidos pagados en 2 semanas | ≥ 20 | 24 | Sí |
| Ticket promedio | ≥ $40.000 | $31.000 | No |
| Costo de adquirir 1 cliente (CAC) | ≤ $15.000 | $9.500 | Sí |
| % que recompra a la semana | ≥ 30% | 12% | No |

Lectura honesta: la **demanda existe** (conversión y CAC pasan), pero **el ticket es bajo y casi nadie recompra**. Eso no es GO ni KILL: es un **PIVOT** claro. La hipótesis que falla es la económica (cada venta deja poco y no se repite). Acciones: subir ticket (combos/planes semanales) y atacar la recompra (suscripción) — y volver a medir SOLO esas dos. Si tras el pivote la recompra sigue bajo 15%, ahí sí es NO-GO.

(Las cifras de arriba son inventadas para ilustrar el método. Tus umbrales reales dependen de tu costo, tu margen y tu país/ciudad — pregunta y calcula con datos locales, ver 21 para conseguir números reales y 20 si necesitas tamaño de mercado.)

## De dónde sale cada umbral (no los inventes al azar)

- **Umbral de conversión / recompra** → de benchmarks de tu sector + tu propio break-even (ver 53). Si por debajo de X% pierdes plata, ese X% ES tu línea.
- **Umbral de CAC** → debe ser menor que el margen que deja un cliente en su vida (LTV). Regla común: LTV/CAC ≥ 3. Si no se cumple, el negocio "vende pero no gana".
- **Muestra mínima** → como mínimo decenas, no unidades. Con 8 personas cualquier resultado es casualidad.
- **Plazo** → corto y fijo (1-3 semanas en validación temprana). Un plazo abierto = nunca decides = sangrado lento.

## Tabla de decisión (úsala tal cual)

| Demanda (¿la gente quiere?) | Economía (¿deja plata?) | Veredicto |
|---|---|---|
| Sí | Sí | **GO** — escala el siguiente paso |
| Sí | No | **PIVOT** — cambia precio/modelo/costo |
| No | Sí | **PIVOT** — cambia cliente/canal/mensaje |
| No | No | **NO-GO** — mata y reinvierte tu tiempo |

Dos ejes simples: ¿lo quieren? y ¿gano dinero? Casi toda decisión cae en una de estas casillas.

## Errores comunes

- **Mover la portería:** definir el umbral después de ver el resultado. Trampa #1. Fírmalo con fecha antes.
- **Confundir cumplidos con tracción:** "a todos les gustó" no es un criterio. Mide pagos, no aplausos.
- **Muestra ridícula:** decidir con 5 amigos. Sesgado y minúsculo.
- **Un solo número:** si solo miras "ventas" ignoras costo y recompra; puedes escalar un negocio que pierde plata.
- **No tener umbral de KILL:** si solo defines cuándo seguir pero nunca cuándo parar, nunca paras. Define SIEMPRE la línea de muerte.
- **Plazo infinito:** "le doy un tiempito más" repetido 6 veces = 6 meses perdidos.
- **Ignorar el resultado por orgullo:** el criterio solo sirve si te comprometes a obedecerlo aunque duela.

## Plantilla rápida (cópiala antes de cualquier test)

```
HIPÓTESIS: ___________________________________
MÉTRICA PRINCIPAL: ___________________________
GO si: ______ (umbral)  con al menos ____ datos, antes del ___/___
PIVOT si: ____________________________________
NO-GO/KILL si: _______________________________
Firmado (yo) — fecha: ___/___/___
```

## Siguiente paso típico

Escribe tus umbrales GO / PIVOT / KILL con fecha ANTES de lanzar el experimento de demanda (ver 32). Cuando lleguen los datos, compara contra la tabla de decisión sin negociar contigo mismo; si el resultado es PIVOT, define qué única variable cambias y vuelve a testear (ver 37).
