# 98 — Karl Fischer y humedad (el número que hace comparables todos los demás números)

La humedad parece un dato secundario y es exactamente lo contrario: **sin humedad no hay base seca, y sin
base seca dos resultados no se comparan**. Un extracto con 30 % de β-glucano y 12 % de humedad tiene menos
activo por kilo que otro con 30 % y 4 % de humedad, aunque el COA diga el mismo número. Además, la humedad
manda en la vida útil, en el crecimiento de mohos y en si el polvo se apelmaza en la cápsula. Es el ensayo
más barato del laboratorio y el que más decisiones sostiene.

Términos: **humedad (moisture)** = agua contenida, en % p/p. **pérdida por secado (LOD, Loss On Drying)** =
lo que la muestra pierde al calentarla; no es solo agua. **Karl Fischer (KF)** = titulación química
específica para agua. **actividad de agua (water activity, aw)** = agua *disponible* para microorganismos,
entre 0 y 1; no es lo mismo que humedad.

## Los tres métodos, y por qué no dan lo mismo

| Método | Qué mide realmente | Rango típico | Tiempo | Nota |
|---|---|---|---|---|
| **Pérdida por secado (LOD)** en estufa 105 °C | Agua **+ todo lo volátil** | > 0,5 % | 2–4 h | Barato, universal, sobreestima si hay terpenos o solventes |
| **Termobalanza / balanza halógena** | Igual que LOD, más rápido | > 0,5 % | 5–15 min | Buena para control de línea, calibrar contra LOD |
| **Karl Fischer volumétrico** | **Solo agua** | ~0,1 – 100 % | 2–5 min | El de rutina en sólidos y líquidos con bastante agua |
| **Karl Fischer coulométrico** | **Solo agua**, trazas | ~1 ppm – 5 % | 2–5 min | Para aceites, solventes, aislados |

La diferencia LOD − KF es información: si LOD da 9,0 % y KF da 6,2 %, esos 2,8 puntos son **volátiles que no
son agua** — terpenos, etanol residual, amoníaco. En cannabis eso importa doble: la pérdida por secado de una
flor incluye terpenos, y por eso los COA serios usan KF o declaran explícitamente el método.

## Cómo funciona Karl Fischer

La reacción consume agua estequiométricamente, con yodo, dióxido de azufre, una base y un alcohol:

```
H2O + I2 + SO2 + CH3OH + 3 RN  ->  2 RN·HI + RN·HSO4CH3

Un mol de agua consume un mol de yodo -> midiendo el yodo consumido, mides el agua.

Volumetrico  : el yodo viene de una bureta; se titula hasta el punto final electroquimico.
Coulometrico : el yodo se genera en la celda por electrolisis; se mide la carga.
               1 mg de agua = 10,71 culombios. Por eso llega a ppm.
```

Puntos críticos de operación:

- **La celda debe estar seca.** Se hace un pre-acondicionamiento hasta deriva estable (drift) antes de
  cualquier medición. Una deriva alta se resta o invalida el resultado.
- **Titulante estandarizado** contra un patrón de agua conocido (tartrato de sodio dihidrato, 15,66 % de
  agua teórica, o estándares comerciales de agua certificados).
- **Muestra insoluble**: se usa un **horno KF** (KF oven) que calienta la muestra y arrastra el agua con gas
  seco hasta la celda. Es lo correcto para polvos de hongo y materiales que no se disuelven en metanol.
- **Interferencias químicas**: aldehídos y cetonas reaccionan con metanol y dan agua falsa; para esas
  matrices se usan reactivos "K" específicos. Compuestos oxidantes/reductores fuertes también interfieren.

## De humedad a base seca

```
Resultado en base seca = Resultado en base humeda / (1 - humedad_fraccion)

Ejemplo: beta-glucano 28,0 % p/p base humeda, humedad 6,5 % p/p
         28,0 / (1 - 0,065) = 29,95 % p/p base seca

Y al reves:
Resultado base humeda = Resultado base seca x (1 - humedad_fraccion)
```

Ejecuta esta cuenta con `lab-tools/base_seca.py`, nunca de memoria: rutea a `Matematicas_lushows` si de ella
depende un precio o un cumplimiento. Ver `07-base-seca-vs-humeda.md`.

## Humedad no es actividad de agua

Dos polvos con 8 % de humedad pueden tener aw de 0,45 y de 0,72. El que manda para el crecimiento de mohos y
bacterias es **aw**, no la humedad:

| aw | Qué crece |
|---|---|
| > 0,90 | Bacterias, incluidas las patógenas |
| 0,80 – 0,90 | La mayoría de levaduras y mohos |
| 0,60 – 0,80 | Mohos xerófilos, levaduras osmófilas |
| < 0,60 | Prácticamente nada crece |

Objetivo práctico para un polvo de hongo o de planta seca: **aw ≤ 0,60**, y humedad definida por
especificación. Ver `35-actividad-de-agua-y-humedad.md` y `100-microbiologia-de-producto.md`.

## Cómo se comprueba

- **Estándar de agua certificado** al inicio de cada serie; recuperación aceptable típicamente 98–102 %
  (criterio ILUSTRATIVO, fíjalo en tu método validado, ver `74`).
- **Deriva de la celda** registrada antes y después.
- **Duplicados** de cada muestra; la diferencia entre duplicados es tu control de homogeneidad (ver `67`).
- **Comparación periódica KF vs LOD** para conocer cuánto volátil no acuoso tiene tu matriz.

## Ejemplo aplicado (ILUSTRATIVO)

Lote de polvo de melena de león, HE-2604, especificación de humedad ≤ 8,0 % p/p.

```
Metodo               : Karl Fischer coulometrico con horno KF, 140 C, arrastre con N2 seco
Estandar de control  : 1,00 % agua, recuperacion 99,4 %  -> OK
Muestra, duplicado 1 : 6,18 % p/p
Muestra, duplicado 2 : 6,24 % p/p     Media: 6,21 % p/p
Perdida por secado   : 8,9 % p/p      Diferencia KF vs LOD: 2,7 puntos (volatiles no acuosos)
Actividad de agua    : 0,49 a 25 C
Veredicto            : humedad conforme; aw por debajo de 0,60; apto para envasar
Efecto en el activo  : beta-glucano 28,5 % base humeda -> 30,4 % base seca
```

(Cifras ilustrativas.)

## Errores comunes

- **Reportar un activo sin declarar la humedad y la base.** El error más frecuente de todos los COA.
- **Usar pérdida por secado en cannabis** y llamarlo humedad: te llevas los terpenos en el número.
- **Celda KF húmeda** o deriva alta ignorada: resultados inflados sin que nadie lo note.
- **Muestra insoluble metida directo a la celda** en vez de usar horno KF: solo mides el agua superficial.
- **Confundir humedad con aw** y creer que 8 % de humedad garantiza estabilidad microbiológica.
- **Muestra expuesta al ambiente** mientras se pesa: un polvo higroscópico gana humedad en minutos. Pesa en
  vial cerrado y por diferencia.

## Conexión con otros módulos

→ `07-base-seca-vs-humeda.md` — la regla que hace comparables los resultados.
→ `35-actividad-de-agua-y-humedad.md` — aw, el parámetro que gobierna el crecimiento microbiano.
→ `99-analisis-termico-dsc-y-tga.md` — TGA como otra vía para agua y volátiles.
→ `100-microbiologia-de-producto.md` — por qué la humedad decide el resultado microbiológico.
→ `142-secado-y-conservacion-de-biomasa.md` — cómo se llega a la humedad objetivo sin perder activo.
→ `164-estabilidad-ich-q1-y-vida-util.md` — humedad como variable crítica de vida útil.