# 02 · Mentalidad de exactitud (error cero)

> **Qué resuelve / cuándo usarlo** — Te explica *por qué* esta skill nunca calcula de memoria y *cómo* un solo decimal mal puesto puede arruinar una decisión con dinero real. Léelo antes de confiar en cualquier número que produzca un LLM (incluido yo).

## Concepto (para no-experto)

**Error cero** es una promesa, no un eslogan: cada número que entrego tiene que ser *exacto*, porque de cada número cuelga una decisión que mueve dinero, tiempo o reputación.

Definamos los términos clave la primera vez:

- **LLM** (*Large Language Model*, "modelo grande de lenguaje"): el tipo de IA que genera texto, como yo. Predice la siguiente palabra más probable. Eso lo hace excelente con el lenguaje y **poco confiable con la aritmética**: no "calcula", *adivina* el resultado que *suena* correcto. Por eso esta skill ejecuta el cálculo en **código real** (Python o Node), nunca "a ojo".
- **Cálculo de memoria** ("mental arithmetic"): resolver una cuenta sin herramienta, dentro de la cabeza (o, en mi caso, dentro del modelo de lenguaje). **Prohibido** para todo lo no trivial.
- **Verificación**: confirmar un resultado por una **segunda vía** independiente (la operación inversa, una estimación, otro método o un *test* automático). Si las dos vías coinciden, el número es creíble; si no, hay un error que cazar.

**Analogía cotidiana.** Imagina un carpintero con el lema *"mide dos veces, corta una vez"*. La tabla cortada no se puede "des-cortar": si midió mal, perdió la madera. Un número en una cotización, una factura o un préstamo es igual: una vez que el cliente lo ve, o el banco lo cobra, ya actuó sobre él. La verificación por segunda vía es *medir dos veces*. El código es *la cinta métrica* (no el ojo).

**Por qué un decimal cambia la decisión.** Un decimal o una coma mal puesta multiplica o divide por 10, 100 o 1.000. En un margen del 15 %, confundirlo con 1,5 % te hace creer que el negocio pierde plata cuando gana; al revés, te hace vender por debajo del costo. El error no es "pequeño": cambia el *signo* de la decisión.

## Fórmulas / método

No hay una fórmula del "error cero", pero sí dos magnitudes que conviene definir para hablar con precisión de cuánto te equivocaste.

**Error absoluto** (cuánto te alejaste, en las mismas unidades del dato):

```
E_abs = | valor_obtenido − valor_verdadero |     [unidades del dato]
```

**Error relativo** (qué fracción del verdadero representa ese error; sin unidades, suele expresarse en %):

```
E_rel = E_abs / | valor_verdadero |              [adimensional]
E_rel(%) = E_rel × 100                            [%]
```

Donde:
- `valor_obtenido` = el número que produjiste.
- `valor_verdadero` = el número correcto (de la vía verificada).
- `| · |` = valor absoluto (la distancia, siempre positiva).

**Regla de decisión (el método):** un resultado solo se entrega si `E_rel = 0` para cálculos exactos (aritmética, dinero en centavos enteros, fracciones), o si está dentro de la tolerancia declarada para cálculos numéricos aproximados (raíces, integrales). Si las dos vías no coinciden a la precisión exigida → **no se entrega**, se depura.

## Verificación en código

Ejemplo real y peligroso: calcular el **20 % de descuento sobre $19.990 COP**. Un LLM "de memoria" suele soltar $15.992 — que está mal. Veámoslo con dinero **exacto** usando `decimal` (nunca `float`, porque `float` arrastra basura binaria como 0.1 + 0.2 = 0.30000000000000004).

```python
from decimal import Decimal, ROUND_HALF_UP

# --- Vía 1: cálculo directo en centavos enteros / Decimal ---
precio   = Decimal("19990")        # COP, pago en pesos enteros
desc_pct = Decimal("20") / Decimal("100")   # 20% = 0.20 exacto en Decimal

descuento     = precio * desc_pct           # 19990 * 0.20
precio_final  = precio - descuento

# Redondeo UNA sola vez al final, al peso (COP no usa centavos en la práctica)
precio_final = precio_final.quantize(Decimal("1"), rounding=ROUND_HALF_UP)

print("Descuento:", descuento)        # 3998.00
print("Precio final:", precio_final)  # 15992

# --- Vía 2 (verificación inversa): si el final es 80% del precio,
#     entonces final / 0.80 debe devolver el precio original ---
reconstruido = (precio_final / (Decimal("1") - desc_pct)).quantize(
    Decimal("1"), rounding=ROUND_HALF_UP)
assert reconstruido == precio, f"FALLA: {reconstruido} != {precio}"

# --- Vía 3 (sanity check de orden de magnitud): el final debe estar
#     entre el 75% y el 85% del precio (20% off ⇒ ~80%) ---
assert precio * Decimal("0.75") < precio_final < precio * Decimal("0.85")

print("OK: verificado por 3 vías ->", precio_final, "COP")
```

Salida: `Descuento: 3998.00`, `Precio final: 15992`, y los `assert` pasan. El resultado correcto **sí** es $15.992 — pero solo lo afirmamos *después* de que la inversa y el sanity check lo confirman. Si el LLM hubiera dicho $15.892 (un dígito cambiado), el `assert reconstruido == precio` habría reventado de inmediato.

## Ejemplo trabajado

**Situación real (GastroLatam).** Vendes la Calculadora de Costos a **$10.000 COP**. Lanzas una promo de **3 unidades por $25.000** (regalo para equipo de cocina) y quieres saber el descuento por unidad y el margen si tu costo digital marginal es ~$0.

Paso a paso:

1. Precio normal por 3 = 3 × $10.000 = **$30.000 COP**.
2. Precio promo = **$25.000 COP**.
3. Descuento absoluto = 30.000 − 25.000 = **$5.000 COP** (unidades: COP).
4. Descuento relativo = 5.000 / 30.000 = 0,1666… = **16,67 %** (redondeado a 2 decimales, una sola vez).
5. Precio por unidad en promo = 25.000 / 3 = **$8.333,33 COP/unidad**.

Verificación por segunda vía (inversa): 8.333,33 × 3 = 24.999,99 ≈ 25.000 ✔ (la diferencia de 1 centavo es por mostrar el unitario redondeado; el cálculo interno usa el valor exacto 25000/3). Sanity check: 16,67 % está entre 0 % y 100 %, y "un poco menos de 1/6" cuadra con "regalas casi una de cada seis". 

**Resultado:** descuento de **$5.000 COP (16,67 %)**; precio efectivo **$8.333,33 COP/unidad**. Como el costo marginal digital es ≈ $0, el margen de contribución sigue siendo ≈ 100 % aun con la promo — la promo no destruye rentabilidad, solo reduce ingreso por unidad. (Para el detalle de márgenes ver el cruce correspondiente.)

## Errores comunes / trampas

- **Calcular de memoria "porque es fácil".** El 80 % de los errores caros vienen de cuentas que *parecían* triviales. Regla dura: si tiene más de un paso o involucra dinero, va a código.
- **Usar `float` para dinero.** `0.1 + 0.2 != 0.3` en binario. Usa `Decimal` o centavos enteros. (Detalle en [[12-fracciones-decimales-y-precision]].)
- **Redondear en cada paso.** Cada redondeo intermedio inyecta error que se acumula. Redondea **una sola vez, al final**.
- **Confiar en una sola vía.** Un número "que se ve bien" no está verificado. Sin segunda vía, no se entrega.
- **Perder las unidades.** "5.000" no significa nada; "$5.000 COP" o "5.000 unidades" sí. Un número sin unidad es una trampa esperando a confundir pesos con dólares.
- **El error de la coma decimal.** En LatAm la coma es decimal y el punto es miles ($1.234,56). Confundirlos cambia el número por 100. Declara siempre el formato.
- **Aceptar el primer número del LLM (incluido el mío).** Si yo doy una cifra sin mostrar el código que la calculó, trátala como sospechosa hasta verla verificada.

### Mini-checklist de exactitud
- [ ] ¿El cálculo se ejecutó en **código real**, no de memoria?
- [ ] ¿Está **verificado por una segunda vía** (inversa / estimación / otro método)?
- [ ] ¿El resultado lleva **unidades** y se redondeó **una sola vez al final**?

## Cruces
- [[00-metodo-del-matematico-exacto]] — el protocolo completo del que esta mentalidad es el "por qué".
- [[03-protocolo-de-verificacion-por-codigo]] — el "cómo" técnico de ejecutar y comprobar.
- [[06-estimacion-y-sanity-checks]] — la segunda vía rápida por orden de magnitud.
- [[07-falacias-y-errores-numericos-comunes]] — catálogo de trampas que producen números falsos.
- [[99-protocolo-final-de-verificacion]] — la lista de chequeo antes de entregar cualquier número.
