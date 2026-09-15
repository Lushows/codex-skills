# 73 — LOD, LOQ y rango lineal ("no detectado" nunca significa "cero")

Si te llevas una sola idea de todo el bloque analítico, que sea esta: **el laboratorio no mide ausencia, mide
por debajo de su propio límite**. Un COA que dice "plomo: no detectado" sin decir el límite de detección es
un papel decorativo. Y al revés: un COA que dice "< 0,010 mg/kg" está diciendo algo verificable y útil. Este
módulo te enseña qué son el LOD y el LOQ, cómo se calculan, por qué el LOQ tiene que ser mucho más bajo que
tu límite regulatorio, y cómo se usa esa asimetría para hacer trampa.

Términos:
- **LOD (limit of detection)** = concentración más baja que el método puede distinguir del ruido; se puede
  afirmar presencia, no cantidad.
- **LOQ / LLOQ (limit of quantitation / lower limit of quantitation)** = concentración más baja que se puede
  medir con exactitud y precisión aceptables.
- **Rango de trabajo (working range / range)** = del LOQ al punto más alto validado.
- **Ruido (noise)** = fluctuación de la línea base del detector.
- **ND / BDL** = *not detected / below detection limit*, ambos significan "por debajo del LOD".

## Las tres maneras de calcular LOD y LOQ

ICH Q2(R2) (finalizada en noviembre de 2023, en aplicación desde 2024; verificar el texto vigente en
database.ich.org) admite varios enfoques. Los tres usuales:

| Enfoque | Fórmula | Cuándo se usa |
|---|---|---|
| Relación señal/ruido (S/N) | LOD ≈ S/N = 3 ; LOQ ≈ S/N = 10 | Métodos con línea base visible (HPLC-UV, GC-FID) |
| Desviación estándar del blanco | LOD = 3,3·σ/m ; LOQ = 10·σ/m | σ = desviación del blanco o del intercepto; m = pendiente |
| Desde la curva de calibración | σ = error estándar de la regresión (Sy/x) | El más usado en validación formal |

```
Cálculo desde la curva (ILUSTRATIVO), cadmio por ICP-MS:
  Sy/x (error estándar residual) = 0,00042 (unidades de señal)
  pendiente m = 0,0138 señal por (µg/L)

  LOD = 3,3 x 0,00042 / 0,0138 = 0,100 µg/L
  LOQ = 10  x 0,00042 / 0,0138 = 0,304 µg/L

  Con dilución de 0,5 g de muestra en 25 mL de digestado (factor 50):
  LOQ en muestra = 0,304 µg/L x 25 mL / 0,5 g = 15,2 µg/kg = 0,0152 mg/kg
```
Toda esta aritmética va a código: `lab-tools/loq_lod.py` o `Matematicas_lushows`. Fíjate en el paso final:
**el LOD del instrumento no es el LOQ del método**. Lo que importa para tu decisión es el segundo, expresado
en la unidad de tu producto (mg/kg de polvo, % p/p de flor), y en tu matriz.

## Por qué el LOQ tiene que ser MUCHO menor que tu límite

Regla operativa aceptada en la práctica de residuos y contaminantes: el LOQ debe estar entre **1/3 y 1/10**
del límite que necesitas demostrar. Si tu límite es 0,10 mg/kg de plomo, un método con LOQ de 0,05 mg/kg te
deja sin margen: cualquier resultado cerca del límite tendrá una incertidumbre relativa enorme.

```
Escenario (ILUSTRATIVO):
  Límite regulatorio: 0,30 mg/kg de plomo

  Lab A: LOQ = 0,50 mg/kg → reporta "ND". No demuestra NADA: no puede ver
                            un incumplimiento de 0,40 mg/kg... espera, sí lo vería,
                            pero no puede demostrar conformidad en 0,29.
  Lab B: LOQ = 0,03 mg/kg → reporta "0,12 mg/kg". Demuestra conformidad con margen.

  Con el COA del lab A no puedes defender el lote ante una autoridad ni ante un cliente.
```
Por eso, cuando cotices, **no compares precios: compara LOQ**. Un panel barato con LOQ alto no es más barato,
es inútil para cumplir.

## Cómo se ve esto en un COA bien hecho

```
Analito     Resultado    Unidad     LOQ      Límite spec   Conclusión
--------------------------------------------------------------------
Plomo (Pb)  0,12         mg/kg      0,010    0,30          Conforme
Cadmio (Cd) < LOQ        mg/kg      0,005    0,10          Conforme
Mercurio    ND           mg/kg      0,003    0,10          Conforme (LOD 0,001)
Arsénico    0,38         mg/kg      0,010    0,30          NO CONFORME
```
Las tres columnas que casi nadie exige y que definen si el papel sirve: **unidad, LOQ y base**. Y para
"no conforme", hay que mirar además la incertidumbre expandida antes de declarar un incumplimiento (`76`).

## Rango lineal y rango de trabajo

El **rango lineal** es donde la respuesta es proporcional a la concentración. Por debajo se pierde en el
ruido; por encima, el detector se satura (en UV, cuando la absorbancia pasa de ~1,5–2,0 unidades; en MS,
cuando el detector se satura de iones).

```
                señal
                  |            ,-----------  saturación (respuesta se aplana)
                  |         ,-'
                  |      ,-'   ← rango lineal utilizable
                  |   ,-'
                  |,-'
                  +---------------------------- concentración
                 LOD  LOQ                 límite superior
```
El **rango de trabajo declarado** de un método siempre es un subconjunto documentado del rango lineal: es lo
que se validó, con exactitud y precisión demostradas en al menos los extremos y el centro (`75`).

## Ejemplo aplicado — "libre de pesticidas" en un polvo de hongos

Un proveedor te ofrece un COA que dice "pesticidas: no detectados" en 40 analitos.

```
Preguntas obligatorias:
 1. ¿Cuál es el LOQ de cada analito? Si es 0,10 mg/kg y el límite de referencia
    de varios activos es 0,01-0,05 mg/kg, el "ND" no demuestra conformidad.
 2. ¿Los 40 analitos son los exigidos por mi mercado? Si mi jurisdicción exige 80,
    el COA cubre la mitad.
 3. ¿El método fue validado EN polvo de hongo, o en fruta?
 4. ¿Cuál fue la recuperación de los fortificados de esa corrida?

Y el punto legal: "libre de pesticidas" NO es una afirmación defendible.
Lo defendible es "por debajo del LOQ de X mg/kg por el método Y, para los N analitos
del panel Z". Eso es lo que puedes escribir sin exponerte (293).
```

## Qué preguntarle al laboratorio

1. ¿Cuál es el LOD y el LOQ **del método completo en mi matriz**, no del instrumento?
2. ¿Cómo los determinaron: S/N, desviación del blanco, o desde la curva?
3. ¿Verificaron el LOQ analizando muestras fortificadas a ese nivel? ¿Con qué precisión y exactitud?
4. ¿Cuál es el rango de trabajo validado? ¿Mi muestra cayó dentro?
5. ¿Cómo reportan valores entre LOD y LOQ: "trazas", "< LOQ", o un número?
6. ¿Me pueden bajar el LOQ si pago más (mayor masa de muestra, menos dilución, otro instrumento)?

## Errores comunes

- **Leer "ND" como "cero".** El error conceptual más costoso del sector; ha causado retiros de producto.
- **Comparar dos COA con LOQ distintos.** No son comparables; parece que un lote está más limpio y solo está
  peor medido.
- **Escribir "libre de metales pesados" en la etiqueta.** No es demostrable; es un claim de riesgo (`268`, `293`).
- **Aceptar LOQ del instrumento en vez del método.** El factor de dilución de la preparación puede multiplicar
  el LOQ por 50 o por 100.
- **Reportar un número por debajo del LOQ.** Es tentador ("0,003 mg/kg") y no tiene soporte estadístico.
- **Usar un método con LOQ igual al límite.** No deja margen para la incertidumbre y toda decisión cerca del
  límite es una moneda al aire (`76`).

## Conexión con otros módulos

→ `71-curva-de-calibracion.md` — de dónde salen σ y la pendiente.
→ `74-exactitud-precision-y-recuperacion.md` — cómo se verifica el LOQ en la práctica.
→ `75-validacion-de-metodos-ich-q2-r2.md` — qué exige la guía.
→ `76-incertidumbre-de-medida.md` — por qué cerca del límite hay que decidir con la incertidumbre.
→ `110-como-leer-un-coa.md` y `111-banderas-rojas-en-un-coa.md` — cómo detectar el "ND" vacío.
→ `293-como-comunicar-ciencia-sin-mentir.md` — cómo se dice esto en la etiqueta sin exponerte.