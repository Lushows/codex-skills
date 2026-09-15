# 05 — Cifras significativas e incertidumbre (cuántos decimales puedes defender)

Cuando un COA dice "β-glucano 24,63 %", esos dos decimales son una promesa: estás afirmando que si
repites el análisis vas a caer cerca de 24,63 y no de 23 o de 26. Casi siempre esa promesa es falsa,
porque el método no tiene esa resolución. Escribir más decimales de los que soporta el método es una
forma silenciosa de mentir, y funciona al revés también: te impide ver que dos lotes que parecen
distintos (24,6 vs 25,9) en realidad son el mismo dentro del error del método. Este módulo te enseña
a leer y a escribir números con la precisión que puedes sostener.

Términos: **cifras significativas (significant figures)** = dígitos de un número que llevan información
real. **precisión (precision)** = qué tanto se repiten los resultados entre sí. **exactitud (accuracy)**
= qué tan cerca están del valor verdadero. **desviación estándar (standard deviation, s)** = medida de
dispersión. **RSD o CV (relative standard deviation / coefficient of variation)** = s dividido por la
media, en porcentaje. **incertidumbre expandida (expanded uncertainty, U)** = intervalo dentro del cual
está razonablemente el valor verdadero, normalmente con factor de cobertura k = 2 (~95 %).

## Precisión y exactitud no son lo mismo

| Situación | Precisión | Exactitud | Qué está pasando |
|---|---|---|---|
| 24,6 / 24,7 / 24,6 y el real es 24,6 | Alta | Alta | Método bien |
| 18,1 / 18,2 / 18,1 y el real es 24,6 | Alta | Baja | Sesgo: calibración o recuperación mala |
| 20 / 27 / 25 y el real es 24,6 | Baja | Aceptable en promedio | Método ruidoso; un solo dato no sirve |
| 12 / 31 / 22 y el real es 24,6 | Baja | Baja | El resultado no significa nada |

Un laboratorio que solo te manda **un** número no te permite distinguir estos cuatro casos. Por eso se
piden réplicas y controles (ver `74`, `77`).

## Reglas de cifras significativas

```
Suma y resta:           el resultado tiene tantos DECIMALES como el dato con menos decimales.
                        12,4 + 0,065 = 12,5  (no 12,465)
Multiplicación/división: el resultado tiene tantas CIFRAS SIGNIFICATIVAS como el dato con menos.
                        450 mg × 0,246 = 111 mg  (3 cifras, no 110,7)
Redondear al FINAL:      nunca a mitad de la cadena de cálculo.
Ceros a la izquierda:    no cuentan (0,0034 tiene 2 cifras significativas).
Ceros a la derecha con coma: sí cuentan (24,60 tiene 4).
```

Regla de oficio para reportar: **el resultado se redondea al nivel de su incertidumbre**. Si
U = ±2,0 %, no escribas 24,63; escribe 24,6 ± 2,0 % p/p base seca.

## Cómo se calcula la incertidumbre en la práctica

Versión mínima y honesta, con réplicas:

```
media (x̄)        = suma de resultados / n
desviación (s)    = raíz de [ suma (xi − x̄)² / (n − 1) ]
RSD %             = 100 × s / x̄
IC 95 % (t)       = x̄ ± t(n−1, 0,975) × s / raíz(n)
                    t(2 gl) = 4,303 ; t(4 gl) = 2,776 ; t(9 gl) = 2,262
```

Ejemplo **(ILUSTRATIVO)**: tres réplicas de β-glucano dan 24,0 / 25,3 / 24,5 % p/p base seca.
Media = 24,6; s = 0,66; RSD = 2,7 %; IC 95 % = 24,6 ± 1,6 % p/p. Se reporta **24,6 % p/p base seca
(n = 3, RSD 2,7 %)**, no 24,60 ni 24,6000.

La incertidumbre completa de un método (`76`) suma más fuentes: pesada, pureza del patrón, volumen,
recuperación, homogeneidad de la muestra. Casi siempre el aporte dominante **no** es el instrumento:
es el muestreo (ver `66`).

## Órdenes de magnitud de RSD que se consideran normales

| Tipo de análisis | RSD típico esperable | Comentario |
|---|---|---|
| HPLC-UV de un activo mayoritario | 1–3 % | Bien controlado |
| Ensayo enzimático de β-glucano | 3–7 % | Depende mucho de molienda y homogeneidad |
| Metales pesados por ICP-MS cerca del LOQ | 10–25 % | Cerca del límite el ruido manda |
| Pesticidas multiresiduo a nivel traza | 15–30 % | Recuperaciones 70–120 % aceptadas |
| Muestreo de un lote heterogéneo | 10–40 % | La fuente de error más grande y la más ignorada |

Valores orientativos de literatura y criterios ICH/AOAC; **verifica los criterios exactos del método
que uses**, no los tomes de esta tabla como especificación.

## Cómo se comprueba si dos números son de verdad distintos

No basta con que uno sea mayor. Chequeo rápido: si los intervalos de confianza se traslapan, no puedes
afirmar diferencia. Prueba formal: t de Student para dos medias, o el criterio de la propia
especificación del método. Ejecuta la prueba, no la intuyas — ruteo a `Matematicas_lushows`.

Caso típico: lote A 24,6 % y lote B 25,9 %, ambos con U = ±2,0 %. Los intervalos (22,6–26,6) y
(23,9–27,9) se traslapan ampliamente: **son el mismo lote dentro del error**. Cambiar de proveedor por
esa diferencia sería una decisión tomada sobre ruido.

## Ejemplo aplicado (BIO-SETA)

Vas a declarar en etiqueta "mínimo 200 mg de β-glucanos por porción". Tienes tres lotes con media
221 mg y RSD 6 % **(ILUSTRATIVO)**. La desviación es 13,3 mg; a tres desviaciones por debajo estarías
en 181 mg, por debajo de lo declarado.

Conclusión práctica: o subes la carga de extracto, o declaras 180 mg, o aprietas el control de proceso.
Declarar el promedio como si fuera el mínimo es el error que un inspector encuentra el día que analiza
el lote más flojo. La especificación se fija sobre el **peor caso creíble**, no sobre el promedio
(ver `282`, `283`).

## Errores comunes

- **Copiar los decimales del instrumento.** El software escribe 24,6317; el método soporta 24,6.
- **Reportar un solo resultado sin réplicas** y tratarlo como verdad.
- **Redondear en cada paso** de una cadena de cálculo y acumular error.
- **Declarar en etiqueta el promedio** cuando la palabra es "mínimo".
- **Ignorar la incertidumbre al comparar contra un límite.** Un plomo de 2,1 ppm con U = ±0,4 contra un
  límite de 2,0 ppm no es un incumplimiento demostrado; es una zona gris que hay que resolver (ver `112`).
- **Creer que más réplicas del mismo pesado mejoran la exactitud.** Repetir la inyección mide el
  instrumento; repetir desde el muestreo mide el proceso.

## Conexión con otros módulos

→ `04-unidades-concentraciones-y-conversiones.md` — la unidad antes que el decimal.
→ `74-exactitud-precision-y-recuperacion.md` — cómo se demuestran ambas en validación.
→ `76-incertidumbre-de-medida.md` — el cálculo formal completo de U.
→ `78-estadistica-para-el-laboratorio.md` — pruebas para comparar lotes y métodos.
→ `66-plan-de-muestreo-y-representatividad.md` — la mayor fuente de error, casi siempre.
→ `282-especificacion-de-producto-terminado.md` — de la dispersión al número que firmas.
