# 76 — Incertidumbre de medida (el número que decide si tu lote cumple o no)

Todo resultado analítico es un intervalo disfrazado de número. "Plomo 0,28 mg/kg" en realidad significa
"0,28 ± 0,06 mg/kg con 95 % de confianza". Si tu límite es 0,30 mg/kg, la diferencia entre celebrar y retirar
el lote está en ese ±. Ignorar la incertidumbre es el error que hace que la gente rechace lotes buenos,
libere lotes malos y pierda discusiones con laboratorios que sí la calculan. La norma ISO/IEC 17025 obliga a
los laboratorios acreditados a estimarla; tú tienes derecho a pedirla.

Términos:
- **Incertidumbre estándar (standard uncertainty, u)** = una desviación estándar asociada al resultado.
- **Incertidumbre combinada (combined, uc)** = suma en cuadratura de todas las fuentes.
- **Incertidumbre expandida (expanded, U)** = `U = k · uc`, con **k = 2** para ~95 % de confianza.
- **Presupuesto de incertidumbre (uncertainty budget)** = la tabla de todas las contribuciones.
- **Regla de decisión (decision rule)** = cómo se declara conformidad frente al límite, dada la incertidumbre.

## De dónde viene la incertidumbre

```
uc = raíz( u²_masa + u²_volumen + u²_patrón + u²_curva + u²_recuperación + u²_repetibilidad + u²_homogeneidad )

Las fuentes se suman EN CUADRATURA: la más grande domina.
Perseguir la pequeña es perder el tiempo.
```

Presupuesto típico **(ILUSTRATIVO)** para cadmio en polvo de hongo por ICP-MS, resultado 0,28 mg/kg:

| Fuente | u relativa | u relativa² | % de la varianza |
|---|---|---|---|
| Homogeneidad de la muestra | 6,0 % | 36,0 | 62 % |
| Recuperación de la digestión | 4,0 % | 16,0 | 27 % |
| Curva de calibración | 2,0 % | 4,0 | 7 % |
| Patrón certificado | 1,0 % | 1,0 | 2 % |
| Pesada y volumen | 0,7 % | 0,5 | 1 % |
| Repetibilidad instrumental | 0,8 % | 0,6 | 1 % |
| **Combinada uc** | **10,3 %** | 58,1 | 100 % |
| **Expandida U (k = 2)** | **20,6 %** | | |

```
Resultado: 0,28 mg/kg ± 0,058 mg/kg  (k = 2, ~95 %)
Intervalo: 0,222 - 0,338 mg/kg
```
Lección de la tabla: **el 89 % de la incertidumbre vive en la muestra y en la preparación**, no en el
instrumento. Volvemos al mismo mensaje de `65` y `66`: pagar por instrumentación mejor no mejora un
resultado dominado por la heterogeneidad del lote.

## Reglas de decisión: qué significa "cumple" cerca del límite

Este es el corazón práctico del módulo. Con límite = 0,30 mg/kg y resultado 0,28 ± 0,058:

| Regla de decisión | Cómo declara | En este caso |
|---|---|---|
| **Aceptación simple (shared risk)** | Se compara solo el valor medido con el límite | Cumple (0,28 < 0,30) |
| **Banda de guarda estricta (guarded acceptance)** | Debe cumplir incluso en el peor caso: resultado + U <= límite | NO cumple (0,338 > 0,30) |
| **Rechazo estricto** | Solo se rechaza si resultado − U > límite | Cumple (0,222 < 0,30) |

Ninguna es "la correcta": es una decisión de riesgo que **tú** o el regulador definen. Lo grave es no tener
regla escrita y decidir según convenga. En residuos de alimentos y en control oficial es común aplicar la
incertidumbre a favor del operador (solo se declara incumplimiento si el resultado menos U supera el límite);
en liberación de lote propio conviene lo contrario, la banda de guarda estricta, porque tú asumes el riesgo.

Escribe tu regla en la especificación del producto (`282`) **antes** de que llegue el primer resultado
limítrofe. Después, cualquier decisión parece acomodada.

## Cómo la estima un laboratorio

1. **Enfoque bottom-up (GUM)**: identificar cada fuente, cuantificarla, combinarlas. Riguroso y laborioso.
2. **Enfoque top-down**: usar los datos de validación, de cartas de control y de ensayos de aptitud
   (proficiency testing) para estimar la incertidumbre global. Es el más usado en laboratorios de rutina y
   suele ser más realista, porque captura fuentes que el bottom-up olvida.
3. **Reproducibilidad interlaboratorio** como estimador directo cuando existe un estudio colaborativo.

Un laboratorio acreditado debe poder mostrarte su procedimiento de estimación y el valor de U por ensayo y
por matriz. Si te dicen "no la reportamos porque el cliente no la pide", pídela igual: existe.

## Ejemplo aplicado — THC total al filo del 1,0 %

Colombia, cannabis no psicoactivo: a agosto de 2026 el umbral de THC que separa las categorías está definido
en la normativa vigente (Decreto 811 de 2021 y sus resoluciones reglamentarias; **verifica el valor y la
base exacta en el texto vigente del Ministerio de Justicia / INVIMA / ICA antes de decidir nada**, porque el
umbral y la base — flor seca, base seca — cambian por norma y por jurisdicción).

```
Escenario (ILUSTRATIVO), umbral hipotético 1,00 % p/p base seca:
  Resultado: 0,96 % p/p base seca
  U (k=2) declarada por el laboratorio: 8 % relativo → ± 0,077
  Intervalo: 0,883 - 1,037 %

  Con aceptación simple      → cumple
  Con banda de guarda estricta → NO se puede afirmar cumplimiento
  Con rechazo estricto        → no se puede declarar incumplimiento

Decisión de negocio: si el destino del lote es exportación con muestreo oficial en
destino, la banda de guarda estricta es la única postura defendible. Un lote a 0,96
con U de 8 % es una apuesta, no un cumplimiento.
```
Aquí es donde química, plata y riesgo legal se tocan. La conversación correcta con tu químico no es "¿cumple?"
sino "¿con qué margen respecto a la incertidumbre?".

## Qué preguntarle al laboratorio

1. ¿Cuál es la incertidumbre expandida U (k = 2) de este ensayo en mi matriz y a este nivel?
2. ¿Cómo la estimaron: bottom-up, top-down o desde ensayos de aptitud?
3. ¿La U incluye el muestreo, o empieza en la recepción de la muestra? (Casi siempre empieza en recepción:
   tu muestreo queda **fuera** de esa U.)
4. ¿Qué regla de decisión aplican al declarar conformidad, si la declaran?
5. ¿Pueden reportarme el resultado como valor ± U en el COA?
6. Para valores cercanos al límite, ¿repiten el análisis o reportan la primera lectura?

## Errores comunes

- **Tratar el resultado como exacto.** Es la raíz de casi todas las peleas evitables con laboratorios.
- **Comparar dos laboratorios sin considerar U.** Si U es 10 % en cada uno, una diferencia de 12 % puede ser
  perfectamente compatible (`74`, `112`).
- **Olvidar que la U del laboratorio no incluye tu muestreo.** La incertidumbre real de "mi lote" es mayor
  que la del COA, a veces el doble.
- **No definir la regla de decisión antes.** Invita a acomodar el criterio al resultado.
- **Reportar más cifras significativas que las que la U permite.** Si U es ±0,06, escribir 0,2813 es ruido
  disfrazado de precisión (`05`).
- **Exigir U pequeña en trazas.** A nivel de ppb, U de 20–30 % es normal y no significa mal trabajo.

## Conexión con otros módulos

→ `05-cifras-significativas-e-incertidumbre.md` — cómo se redondea y se escribe.
→ `74-exactitud-precision-y-recuperacion.md` — de dónde salen los insumos.
→ `78-estadistica-para-el-laboratorio.md` — combinación de varianzas y pruebas.
→ `107-iso-17025-y-acreditacion.md` — la obligación normativa de estimarla.
→ `112-como-impugnar-un-resultado.md` — cómo se usa U en una disputa.
→ `282-especificacion-de-producto-terminado.md` — dónde se escribe la regla de decisión.
