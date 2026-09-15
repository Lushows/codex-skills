# 14 · Porcentajes sin errores

> **Qué resuelve / cuándo usarlo** — Cualquier cálculo con `%`: "saca el 19% de IVA", aumentos y descuentos, descuentos encadenados ("20% + 10% extra"), variación porcentual entre dos cifras, y revertir un precio para hallar el original. Es el tema que más decisiones de dinero arruina por errores triviales.

## Concepto (para no-experto)

Un **porcentaje** (símbolo `%`) es simplemente una **fracción cuyo denominador es 100**. "19%" quiere decir "19 de cada 100", o sea `19/100 = 0,19`. Nada más. La palabra viene del latín *per centum* = "por cada cien".

La regla de oro, la que evita el 90% de los errores: **un porcentaje SIEMPRE es porcentaje DE algo**. Ese "algo" se llama la **base** (el número de referencia, el 100%). Si no tienes clarísima cuál es la base, no calcules todavía.

Analogía cotidiana: si en un salón hay 25 estudiantes y el "20%" sacó beca, ese 20% es 20% **de 25** = 5 estudiantes. Pero si mañana entran 5 estudiantes nuevos y vuelves a hablar del "20%", ahora la base es 30, y 20% de 30 = 6. El mismo porcentaje da números distintos porque **cambió la base**. Confundir bases es el error #1.

Términos que usaremos:
- **Base (B)**: el número del que sacas el porcentaje (el 100% de referencia).
- **Tasa (r)**: el porcentaje, escrito como decimal. 19% → `r = 0,19`. Para convertir: divide entre 100.
- **Parte (P)**: el resultado, `P = B × r`.
- **Punto porcentual (p.p.)**: la diferencia *aritmética* entre dos porcentajes (de 10% a 12% hay 2 **p.p.**), distinta del *cambio porcentual relativo* entre ellos (de 10% a 12% hay +20% relativo). Confundir ambos es el error #2.

## Fórmulas / método

Con `B` = base, `r` = tasa en decimal (`r = porcentaje / 100`):

```
Parte:                 P = B · r
Porcentaje que es A de B:   r = A / B      (luego ·100 para %)
Aumento de p%:         B_final = B · (1 + r)
Descuento de d%:       B_final = B · (1 − r)
Cambio porcentual:     Δ% = (nuevo − viejo) / viejo · 100
Diferencia en puntos:  Δp.p. = porcentaje_nuevo − porcentaje_viejo
Revertir un aumento:   B_original = B_final / (1 + r)
Revertir un descuento: B_original = B_final / (1 − r)
Descuentos encadenados: factor = (1−d₁)·(1−d₂)·…   →   B_final = B · factor
```

Símbolos: `B`, `A`, `P`, `B_final`, `B_original` en la misma unidad (p. ej. COP). `r`, `d`, `factor` son adimensionales (puros números). `Δ%` se expresa en %; `Δp.p.` en puntos porcentuales.

**Clave para reversión:** un aumento del 20% NO se deshace con un descuento del 20%. Deshacer es **dividir** por el factor, no restar el mismo porcentaje (ver Errores comunes).

## Verificación en código

Todo dinero con `decimal` (NUNCA `float`, que arrastra errores como `0,1+0,2=0,30000000000000004`). Redondeamos **una sola vez al final** con redondeo bancario/normal explícito.

```python
from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")  # un centavo / un peso, ajusta la cuantía según la moneda
def money(x):  # redondea a 2 decimales, media-arriba, UNA sola vez
    return x.quantize(CENT, rounding=ROUND_HALF_UP)

# --- 1) Parte: 19% de IVA sobre 100.000 COP ---
base = Decimal("100000")
r    = Decimal("19") / Decimal("100")     # 0.19 exacto en Decimal
iva  = base * r
print("IVA:", money(iva))                  # 19000.00

# --- 2) Precio con IVA (aumento) ---
precio_con_iva = base * (Decimal("1") + r)
print("Con IVA:", money(precio_con_iva))   # 119000.00

# --- 3) Descuentos encadenados: 20% y luego 10% sobre 50.000 ---
p0 = Decimal("50000")
factor = (Decimal("1") - Decimal("0.20")) * (Decimal("1") - Decimal("0.10"))
final = p0 * factor
print("Factor encadenado:", factor)        # 0.7200
print("Final:", money(final))              # 36000.00

# --- 4) Revertir: el cliente pagó 119.000 con IVA del 19%, ¿base? ---
pagado = Decimal("119000")
base_rec = pagado / (Decimal("1") + r)
print("Base recuperada:", money(base_rec)) # 100000.00

# --- 5) Cambio porcentual vs puntos porcentuales ---
viejo, nuevo = Decimal("10"), Decimal("12")  # tasa de conversión 10% -> 12%
cambio_rel = (nuevo - viejo) / viejo * Decimal("100")
puntos     = nuevo - viejo
print("Cambio relativo:", cambio_rel, "%")   # 20 %
print("Puntos porc.:", puntos, "p.p.")        # 2 p.p.
```

**Verificación por segunda vía (operación inversa + asserts):** si los cálculos son correctos, deshacerlos debe devolver el original, y un descuento encadenado equivalente único debe coincidir.

```python
# Inversa del IVA: quitar 19% del precio con IVA reconstruye la base
assert money(precio_con_iva / (Decimal("1") + r)) == money(base)

# Inversa de la base recuperada: al re-aplicar IVA vuelvo a 119.000
assert money(base_rec * (Decimal("1") + r)) == money(pagado)

# 20% + 10% encadenados == un único descuento del 28% (no del 30%)
desc_unico = Decimal("1") - factor          # 0.28
assert desc_unico == Decimal("0.28")
assert money(p0 * (Decimal("1") - desc_unico)) == money(final)

# Sanity / orden de magnitud: el final encadenado debe ser < cada paso intermedio
paso1 = p0 * Decimal("0.80")                 # 40000
assert final < paso1 < p0
print("OK: todas las verificaciones inversas pasaron")
```

## Ejemplo trabajado

**Problema (restaurante en Colombia).** Un plato cuesta **$50.000 COP**. Promoción: **20% de descuento** y, encima, **10% adicional** por pago en efectivo. Luego se suma **8% de propina** sugerida sobre el precio ya rebajado. ¿Cuánto paga el cliente y cuál fue el descuento real total?

Paso 1 — Encadenar descuentos (cada uno sobre la base que queda, no sobre la original):
- Factor = (1 − 0,20) × (1 − 0,10) = 0,80 × 0,90 = **0,72**
- Precio rebajado = 50.000 × 0,72 = **$36.000 COP**

Paso 2 — Descuento real total (¡no es 30%!):
- Descuento total = 1 − 0,72 = **0,28 = 28%**, es decir $14.000 COP menos. Restar 20%+10% como si fuera 30% habría dado $35.000: **$1.000 de error** por sumar porcentajes de bases distintas.

Paso 3 — Propina del 8% sobre el rebajado (base = 36.000):
- Propina = 36.000 × 0,08 = **$2.880 COP**
- Total a pagar = 36.000 + 2.880 = **$38.880 COP**

**Verificación (segunda vía).** Reviértelo: 38.880 ÷ 1,08 = 36.000 ✓; 36.000 ÷ 0,72 = 50.000 ✓ (recupero el precio de lista). Sanity check de orden de magnitud: un descuento "fuerte" del ~28% sobre 50k deja unos 36k, y +8% de propina sube poquito → ~39k. Coincide. **Resultado: el cliente paga $38.880 COP; descuento real 28% ($14.000).**

## Errores comunes / trampas

- **Sumar descuentos encadenados.** 20% + 10% **NO** es 30%, es 28% (factor 0,72). Siempre **multiplica factores**.
- **Deshacer un aumento restando el mismo %.** Subir 20% y luego bajar 20% **no** vuelve al inicio: 100 → 120 → 96 (pierdes 4%). Para revertir, **divide** por `(1+r)`, no restes `r`.
- **Confundir punto porcentual con cambio relativo.** "La conversión subió del 10% al 12%": son **+2 p.p.** (aritmético) y **+20% relativo**. Decir "subió 2%" es falso; decir "subió 20%" sin aclarar la base confunde.
- **Equivocar la base.** "% de aumento sobre el costo" ≠ "% de margen sobre el precio". Define siempre el 100% antes de dividir (ver pricing).
- **Usar `float` para dinero.** `0,1+0,2≠0,3`. Usa `decimal` o centavos enteros.
- **Redondear en cada paso.** Redondea **una sola vez al final**; redondeos intermedios acumulan centavos fantasma.
- **% de un %.** "El 50% de los que abren, el 30% compra" → 0,50×0,30 = 15% del total, no 80% ni 30%.

### Mini-checklist de exactitud
- [ ] ¿Identifiqué la **base** (el 100%) de cada porcentaje antes de calcular?
- [ ] ¿Encadené **multiplicando factores** (no sumando %) y revertí **dividiendo**?
- [ ] ¿Verifiqué por inversa (deshacer devuelve el original) y por orden de magnitud, con `decimal` y un solo redondeo final?

## Cruces
- [[13-razones-y-proporciones]] — un % es una razón con base 100; misma lógica de "parte sobre todo".
- [[12-fracciones-decimales-y-precision]] — convertir % ↔ fracción ↔ decimal sin perder exactitud.
- [[05-cifras-significativas-y-redondeo]] — cuándo y cómo redondear una sola vez al final.
- [[82-pricing-markup-margin-y-elasticidad]] — markup vs margin: el caso estrella de "% ¿sobre qué base?".
- [[80-margenes-bruto-contribucion-neto]] — márgenes son porcentajes sobre distintas bases; no confundirlos.
