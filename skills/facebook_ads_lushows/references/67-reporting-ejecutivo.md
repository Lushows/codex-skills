# 67 — Reporting ejecutivo: reportar para generar confianza

Un reporte no es un volcado de métricas: es el instrumento con el que un cliente (o tu jefe, o tú mismo) decide seguir confiándote presupuesto. Este módulo da el formato semanal de 1 página y el mensual, con las reglas que hacen que las semanas MALAS te fortalezcan en vez de hundirte. Úsalo desde la primera semana de pauta; prerequisito: tener los números reales triangulados (ver 64) y el Ads Manager exportable (ver 63). Actualizado jun-2026.

## Reglas de oro (antes del formato)

1. **Números del NEGOCIO primero**: gasto, ventas reales, MER/CPA. Jamás abras con impressions o alcance.
2. **Lo malo se reporta PRIMERO y con plan.** La confianza no se construye en las semanas buenas (cualquiera reporta un ROAS lindo); se construye cuando el CPA subió 40% y tú lo dices antes de que pregunten, con causa y plan. Cliente que descubre el problema solo = cliente perdido.
3. **Cero jerga sin traducir**: la primera vez que uses CPA escribe "CPA (lo que nos cuesta cada venta)". Siempre. (La habilidad de comunicar el número es de **ventas_lushows** — si el cliente es difícil, rutea ahí el guion de la conversación.)
4. **Anticipa el "¿y esto por qué?"**: cada número fuera de lo normal lleva su causa en la misma línea.
5. Mismo día, misma hora, todas las semanas. La puntualidad ES parte del mensaje.
6. **Reporta MER, no ROAS de plataforma** como cifra de resultado. Si muestras ROAS, acláralo: "ROAS de Meta 4.0; nuestro retorno real sobre toda la venta (MER) fue 2.8 — la diferencia es atribución, lo normal" (ver 64). Esto te blinda: el día que el cliente cruce con su banco, tus números cuadran.

## Plantilla — reporte semanal de 1 página (markdown, lista para llenar)

```markdown
# Reporte semanal — [Cliente] — Semana [8–14 jun 2026]

## 1. Números core
| Métrica | Esta semana | Semana anterior | Cambio |
|---|---|---|---|
| Inversión (COP) | 2.000.000 | 1.400.000 | +43% |
| Ventas reales (backend) | 5.200.000 | 3.900.000 | +33% |
| MER (retorno real sobre toda la venta) | 2.6 | 2.79 | −7% |
| Pedidos / CPA (costo por venta) | 33 / 60.600 | 26 / 53.800 | +13% CPA |
| Clientes nuevos / nCAC | 27 / 64.800 | 21 / 61.900 | +5% nCAC |
| Conversaciones WhatsApp | 210 | 150 | +40% |
**Lectura:** subimos inversión 43% y la eficiencia (MER) cayó solo 7% — escalamos sano.
El CPA subió por [causa concreta]; sigue debajo de nuestro máximo de $85.000.

## 2. Qué hicimos (y por qué)
- Subimos presupuesto de [campaña] +40% porque sostuvo 3 semanas bajo CPA objetivo.
- Pausamos 2 ads fatigados (frequency >4, CTR −35%) y subimos 3 hooks nuevos.

## 3. Qué aprendimos
- El ángulo "energía para entrenar" duplica el CTR del ángulo "salud general" → base creativa (ver 68).
- Test cerrado: la audiencia abierta rinde igual que la de intereses → simplificamos estructura.

## 4. Qué sigue (próxima semana)
- 3 variantes del ángulo ganador en formato video corto.
- Test de oferta: combo x2 con envío gratis vs descuento directo.

## 5. Semáforo
🟡 AMARILLO — Crecimiento sano pero CPA subiendo al escalar. Verde si los hooks
nuevos sostienen CPA <$70.000 con esta inversión; si no, estabilizamos en $1.7M/sem.
```

El semáforo es honesto o no sirve: verde = todo en rango; amarillo = señal que vigilar + qué la resolvería; rojo = problema real + plan correctivo YA en marcha (no "lo vamos a ver").

## Cómo se ve una semana MALA bien reportada (el caso que te conserva el cliente)

Mala práctica: abrir con "alcanzamos 180.000 personas" y esconder que el CPA se duplicó. El cliente lo descubre solo en su banco y te despide.

Buena práctica, apertura literal:
> "Semana difícil y la cuento primero. El CPA subió de $55k a $98k (+78%). Causa: Meta desaprobó nuestro ad ganador el martes (apelado, reactivado el jueves) y mientras tanto el presupuesto cayó en ads más fríos. No es la oferta ni el mercado. Plan: ya repuse 3 variantes del ganador, bajé el gasto 30% hasta estabilizar, y el viernes el CPA ya iba en $71k. Estimo volver a <$60k esta semana. MER de la semana: 1.9 (debajo de nuestro 2.5 objetivo) — lo recuperamos."

Eso es lo que separa a un buyer de un proveedor reemplazable: causa + plan + número de recuperación, todo antes de que pregunten.

## El reporte mensual (agrega, no repite)

Estructura del PDF (genera el PDF directo con chrome headless, ver 99 — y la preferencia del proyecto: PDF presentable, no markdown crudo):
1. **Tendencia 3 meses**: gráfica simple de inversión, ventas reales y MER por semana (de tu hoja del 64/69). La tendencia importa más que cualquier semana.
2. **Creative learnings acumulados**: qué ángulos/hooks/formatos ganan y pierden, con números (de tu hoja de learnings, ver 68). Es el activo que justifica tu trabajo más allá del mes.
3. **Resumen de tests**: hipótesis → resultado → decisión (incluye tests de incrementalidad, ver 65).
4. **Plan del mes**: presupuesto propuesto y en qué, con criterio explícito ("si MER ≥2.5 al día 15, subimos a X").
5. **Riesgos**: temporada, fatiga creativa, dependencia de un solo ad ganador, cambios de Meta (cita los del `actualizacion-2026-06` que te afecten — p.ej. vida útil del ad bajó a 2–4 semanas → necesitas pipeline más rápido).

## Traducir las novedades 2026 al cliente sin asustarlo

- **"Meta reporta menos ventas que antes"**: es la atribución incremental — ahora solo cuenta lo que el anuncio causó de verdad, no lo que iba a pasar igual. Número más honesto, no peor desempeño (ver 65).
- **"Ya no vemos el view-through"**: Meta lo quitó del reporte en enero; medíamos casi todo por clic igual. No cambia nuestra decisión.
- **"El píxel ahora se llama Dataset"**: mismo motor, nombre nuevo. Nada que hacer.

## Frecuencia según tamaño de cliente (ver 95 para el modelo de servicio)

| Cliente | Cadencia |
|---|---|
| Pyme < pocos millones COP/mes | Semanal corto (la plantilla) + mensual con llamada de 30 min |
| Cuenta media | Semanal + mensual PDF + canal de WhatsApp para alertas (solo alertas reales) |
| Cuenta grande | Dashboard siempre disponible (ver 69) + semanal ejecutivo + mensual estratégico |

## Errores comunes — blacklist
- Abrir el reporte con alcance e impresiones para "inflar" una semana mala — el cliente aprende a desconfiar de todo el reporte.
- Reportar ROAS de plataforma como ventas reales (ver 64): la mentira se descubre contra el banco, siempre.
- Esconder la semana mala o mandarla tarde — el silencio comunica más que el número.
- 12 páginas de gráficas sin una sola decisión (anti-dashboard, ver 69).
- Jerga sin traducir a un cliente pyme: no te ve experto, te deja de leer.
- Prometer en "Qué sigue" cosas que no se mencionan nunca más: el reporte siguiente DEBE abrir cerrando lo prometido.
- Entregar markdown crudo cuando debió ser un PDF presentable (preferencia del proyecto).
- Reportar sin haber triangulado contra el backend: estás reportando la versión que Meta cuenta de sí misma (ver 64).
