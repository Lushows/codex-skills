# 70 · Valor del dinero en el tiempo

> **Qué resuelve / cuándo usarlo** — Cuando hay que comparar cantidades de dinero en momentos distintos (hoy vs. dentro de meses o años): ¿conviene cobrar $1.000.000 hoy o $1.100.000 en un año? Es el cimiento de TODA la matemática financiera (interés, VPN, TIR, préstamos, valoración).

## Concepto (para no-experto)

**Idea central: un peso hoy vale MÁS que un peso mañana.** No por inflación únicamente, sino por tres razones que se suman:

1. **Oportunidad** — si tengo el peso hoy, puedo invertirlo y que produzca más pesos. Esa renta perdida tiene un costo.
2. **Riesgo** — un peso prometido para mañana puede no llegar (quien me lo debe quiebra, cambia de opinión). El peso en mano es seguro.
3. **Inflación** — con el tiempo el dinero pierde poder de compra (con $1.000 compro menos pan el año que viene).

**Analogía cotidiana:** un mango maduro hoy vale más que la *promesa* de un mango maduro el próximo mes. Hoy lo puedo comer, vender o sembrar (y tener un árbol). La promesa puede dañarse o no cumplirse.

Términos que definimos la primera vez que aparecen:

- **Tasa de descuento (`i`)** — el porcentaje, por período, que usamos para "encoger" un dinero futuro hasta su valor de hoy. Refleja oportunidad + riesgo + inflación. Si `i = 10%` anual, significa que para ti un peso dentro de un año vale como $0,9091 hoy.
- **Valor presente (VP)** — cuánto vale HOY una cantidad que recibirás en el futuro. También llamado *valor actual*.
- **Valor futuro (VF)** — en cuánto se convertirá HOY una cantidad después de `n` períodos creciendo a la tasa `i`.
- **Período** — la unidad de tiempo de la tasa (año, mes, día). La tasa y `n` deben estar en la MISMA unidad. Esto es la trampa #1.
- **Descontar** — traer un valor futuro al presente (dividir por crecimiento). **Capitalizar** — llevar un valor presente al futuro (multiplicar por crecimiento).

## Fórmulas / método

Con tasa por período `i` (decimal: 10% → 0,10) y `n` períodos:

```
Capitalizar (presente → futuro):   VF = VP · (1 + i)^n
Descontar    (futuro → presente):  VP = VF / (1 + i)^n  =  VF · (1 + i)^(-n)

Factor de descuento de un período:  FD = 1 / (1 + i)
```

- `VP`, `VF` — en unidades monetarias (COP, USD…). Siempre llevan moneda.
- `i` — adimensional (porcentaje por período), p. ej. 0,10 por año.
- `n` — número de períodos (adimensional), debe usar el MISMO período que `i`.

**Regla de oro de coherencia temporal:** si la tasa es mensual, `n` se cuenta en meses; si es anual, en años. Mezclar (tasa anual con `n` en meses) es el error que más dinero falso produce.

Dos cantidades en momentos distintos **solo se pueden comparar o sumar tras llevarlas al mismo momento** (normalmente, al presente). Sumar pesos de años distintos sin descontar es como sumar metros con litros.

## Verificación en código

```python
from decimal import Decimal, getcontext, ROUND_HALF_UP

# Dinero SIEMPRE con Decimal, NUNCA float (float introduce errores binarios:
# 0.1 + 0.2 != 0.3). Damos precisión amplia y redondeamos UNA vez al final.
getcontext().prec = 40

def valor_futuro(vp: Decimal, i: Decimal, n: int) -> Decimal:
    """VF = VP * (1+i)^n"""
    return vp * (Decimal(1) + i) ** n

def valor_presente(vf: Decimal, i: Decimal, n: int) -> Decimal:
    """VP = VF / (1+i)^n"""
    return vf / (Decimal(1) + i) ** n

def cop(x: Decimal) -> Decimal:
    """Redondea a peso entero (COP no usa centavos) — UNA sola vez, al final."""
    return x.quantize(Decimal("1"), rounding=ROUND_HALF_UP)

# --- Caso: ¿$1.000.000 hoy vs. $1.100.000 en 1 año, con i = 10% anual? ---
i  = Decimal("0.10")
vp_oferta_b = valor_presente(Decimal("1100000"), i, 1)
print("VP de la oferta B:", cop(vp_oferta_b))   # -> 1000000

# === VERIFICACIÓN POR SEGUNDA VÍA (operación inversa) ===
# Si descuento $1.100.000 y obtengo VP, al capitalizar VP de vuelta debo
# recuperar EXACTAMENTE $1.100.000.
reconstruido = valor_futuro(vp_oferta_b, i, 1)
assert cop(reconstruido) == Decimal("1100000"), "Inversa falló"
print("Inversa OK -> recupera:", cop(reconstruido))

# === SEGUNDA VERIFICACIÓN (estimación / sanity check de orden de magnitud) ===
# A i=10%, descontar 1 año debe quitar ~9% (factor 1/1.1 ≈ 0.909).
# 1.100.000 * 0.909 ≈ 999.900  -> consistente con 1.000.000. OK.
factor = Decimal(1) / (Decimal(1) + i)
print("Factor de descuento 1 año:", round(factor, 4))  # 0.9091
```

Salida esperada:
```
VP de la oferta B: 1000000
Inversa OK -> recupera: 1100000
Factor de descuento 1 año: 0.9091
```

## Ejemplo trabajado

**Situación (LatAm real):** Un proveedor de GastroLatam te ofrece dos formas de pagar una deuda que tiene contigo:

- **Opción A:** te paga **$5.000.000 COP hoy**.
- **Opción B:** te paga **$5.800.000 COP dentro de 18 meses**.

Tu costo de oportunidad (lo que rendiría ese dinero invertido) es **2% mensual**. ¿Cuál conviene?

**Paso 1 — fijar período coherente.** La tasa es mensual (`i = 0,02`), así que `n` va en meses: `n = 18`. (Trampa evitada: no usar n=1,5 años con tasa mensual.)

**Paso 2 — llevar todo a HOY (valor presente).** Opción A ya está hoy: VP_A = $5.000.000.
Para B descontamos 18 meses:

```
VP_B = 5.800.000 / (1 + 0,02)^18
```

**Paso 3 — calcular con código exacto:**

```python
from decimal import Decimal, ROUND_HALF_UP, getcontext
getcontext().prec = 40
i = Decimal("0.02"); n = 18
vp_b = Decimal("5800000") / (Decimal("1") + i) ** n
print(vp_b.quantize(Decimal("1"), rounding=ROUND_HALF_UP))  # -> 4060993
```

**Resultado:** VP_B ≈ **$4.060.993 COP** (en pesos de hoy).

**Paso 4 — comparar EN EL MISMO MOMENTO:**
- VP_A = **$5.000.000 COP**
- VP_B = **$4.060.993 COP**

**Conviene la Opción A** (cobrar hoy). La diferencia a favor de A es ≈ **$939.007 COP** de hoy. Aunque B da más pesos *nominales* ($5,8M > $5,0M), descontados a tu costo de oportunidad valen menos hoy.

**Verificación (segunda vía — capitalizar A):** ¿cuánto debería ofrecer B en 18 meses para empatar a A? VF = 5.000.000·(1,02)^18 = **$7.139.658 COP**. Como B solo ofrece $5.800.000 < $7.139.658, B se queda corta. Coincide con la conclusión. ✔

## Errores comunes / trampas

- **Mezclar unidades de tiempo:** tasa anual con `n` en meses (o al revés). Siempre alinear `i` y `n` al mismo período. → ver [[75-tasas-nominal-efectiva-y-real]].
- **Comparar montos nominales sin descontar:** "$5,8M es más que $5,0M" ignora el tiempo. Siempre traer al mismo momento antes de comparar o sumar.
- **Usar `float` para dinero:** `1.1 ** 18` en float arrastra error binario. Usa `Decimal` y redondea solo al final.
- **Redondear en cada paso intermedio:** acumula error. Redondea UNA vez, al presentar. → [[05-cifras-significativas-y-redondeo]].
- **Olvidar el signo del exponente:** descontar es `(1+i)^(-n)` o dividir; capitalizar es `(1+i)^(+n)`. Confundirlos invierte el resultado.
- **Tasa en porcentaje sin convertir:** usar `i = 10` en vez de `0,10`. Define el decimal y verifícalo con un sanity check.
- **Asumir que descontar = restar inflación:** la tasa de descuento incluye oportunidad y riesgo, no solo inflación. → [[79-moneda-inflacion-y-devaluacion]].

## Cruces

- [[71-interes-simple-y-compuesto]] — el motor `(1+i)^n` viene del interés compuesto.
- [[72-valor-presente-y-futuro]] — desarrollo a fondo de VP/VF con flujos múltiples.
- [[74-vpn-y-tir]] — aplicar descuento a una serie de flujos para decidir inversiones.
- [[75-tasas-nominal-efectiva-y-real]] — convertir correctamente entre tasas por período.
- [[79-moneda-inflacion-y-devaluacion]] — el componente inflación de la tasa de descuento.

---

**Mini-checklist de exactitud**
1. ¿`i` y `n` están en el MISMO período (ambos mensuales o ambos anuales)?
2. ¿Comparé/sumé solo después de llevar todos los montos al mismo momento?
3. ¿Usé `Decimal`, redondeé una sola vez al final, y verifiqué con la operación inversa?
