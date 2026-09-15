# 17 · Notación científica y magnitudes

> **Qué resuelve / cuándo usarlo** — Para manejar números enormes o diminutos (presupuestos de millones, tasas de 0.0003, datos de 10 millones de registros) sin perder ceros ni equivocarte de "tamaño". Te da el lenguaje de los órdenes de magnitud y los prefijos (k, M, G).

## Concepto (para no-experto)

**Notación científica** es una forma de escribir cualquier número como un número entre 1 y 10 multiplicado por una potencia de 10. La idea: en vez de contar ceros a ojo (donde es facilísimo equivocarse), separas el número en dos partes:

- La **mantisa** (también llamada *coeficiente* o *significando*): un número con un solo dígito antes del punto decimal, p. ej. `3.5`.
- El **exponente**: cuántas veces multiplicas o divides por 10, p. ej. `10^6` (un millón).

Ejemplo: la población de Colombia, ~52.000.000 personas, se escribe `5.2 × 10^7`. El `7` te dice de inmediato el "tamaño": estamos en las decenas de millones. Eso es el **orden de magnitud**: la potencia de 10 que domina el número (su exponente cuando lo escribes en notación científica).

**Analogía cotidiana.** Imagina describir distancias. En vez de decir "tengo 0.000002 km de pelusa en el bolsillo" y "manejé 0.000000000000... hasta una estrella", usas reglas de medida distintas (mm, km, años luz). Los **prefijos** (k = mil, M = millón, G = mil millones) son exactamente eso: nombres cortos para órdenes de magnitud, para no escribir o leer una fila de ceros.

| Prefijo | Símbolo | Factor | Potencia | Nombre |
|---|---|---|---|---|
| nano | n | 0.000000001 | 10⁻⁹ | mil millonésima |
| micro | µ | 0.000001 | 10⁻⁶ | millonésima |
| mili | m | 0.001 | 10⁻³ | milésima |
| kilo | k | 1 000 | 10³ | mil |
| mega | M | 1 000 000 | 10⁶ | millón |
| giga | G | 1 000 000 000 | 10⁹ | mil millones (billón en inglés) |
| tera | T | 1 000 000 000 000 | 10¹² | billón (en español) |

> ⚠️ Trampa de idioma: el inglés *billion* = 10⁹ = mil millones (giga). El *billón* en español = 10¹² (tera). Confundirlos es un error de factor 1000.

## Fórmulas / método

Forma normalizada (estándar) de notación científica:

```
N = m × 10^e      con  1 ≤ |m| < 10  y  e entero
```

- `N` = el número original.
- `m` = mantisa (cuántas unidades), un solo dígito no nulo antes del punto.
- `e` = exponente = **orden de magnitud**.

Operaciones (las reglas que evitan errores de ceros):

```
Multiplicar:  (a×10^p) · (b×10^q) = (a·b) × 10^(p+q)
Dividir:      (a×10^p) / (b×10^q) = (a/b) × 10^(p-q)
Potencia:     (a×10^p)^n          = a^n × 10^(p·n)
Sumar/restar: hay que igualar exponentes ANTES de sumar mantisas
```

Orden de magnitud de un número positivo `N`:

```
orden(N) = floor( log10(N) )      (floor = redondeo hacia abajo al entero)
```

La **mantisa correcta** se obtiene dividiendo: `m = N / 10^orden(N)`.

## Verificación en código

```python
from decimal import Decimal, getcontext
import math

getcontext().prec = 50  # alta precisión para no perder dígitos

def a_cientifica(n: Decimal):
    """Devuelve (mantisa, exponente) en forma normalizada 1<=|m|<10.
    Usa Decimal para NO introducir error de float."""
    if n == 0:
        return (Decimal(0), 0)
    signo = -1 if n < 0 else 1
    x = abs(n)
    # exponente = parte entera inferior del log10
    e = int(math.floor(math.log10(x)))
    m = x / (Decimal(10) ** e)
    # corrección de borde: log10 en float puede dar e equivocado por 1
    if m >= 10:
        m /= 10; e += 1
    elif m < 1:
        m *= 10; e -= 1
    return (signo * m, e)

# Caso: PIB aproximado de Colombia ~ 363,500 millones USD = 363,500,000,000
pib = Decimal("363500000000")
m, e = a_cientifica(pib)
print(f"PIB = {m} x 10^{e}")          # 3.635 x 10^11
print(f"Orden de magnitud: 10^{e}")    # 11 -> cientos de miles de millones

# Multiplicación en notación científica
# (3.635e11) * (2e-3)  -> aplicar inflación del 0.2%? -> ejemplo aritmético puro
a, pa = Decimal("3.635"), 11
b, pb = Decimal("2"), -3
prod_m = a * b
prod_e = pa + pb
# renormalizar
mm, ee = a_cientifica(prod_m * (Decimal(10) ** prod_e))
print(f"Producto = {mm} x 10^{ee}")
```

```python
# ---- VERIFICACIÓN POR SEGUNDA VÍA ----
# Vía 1 (arriba): notación científica con Decimal.
# Vía 2: reconstruir el número entero exacto desde (m, e) y comparar
#        con el original SIN pasar por notación científica.

reconstruido = (m * (Decimal(10) ** e))
assert reconstruido == pib, f"FALLO: {reconstruido} != {pib}"

# Vía 3: chequeo de orden de magnitud por conteo de dígitos.
# Un entero positivo con D dígitos tiene orden de magnitud (D-1).
digitos = len(str(int(pib)))
assert e == digitos - 1, f"orden {e} no coincide con {digitos-1} por conteo"

print("OK: las tres vías concuerdan. PIB = 3.635 x 10^11 USD")
```

Salida esperada:
```
PIB = 3.635 x 10^11
Orden de magnitud: 10^11
Producto = 7.27 x 10^8
OK: las tres vías concuerdan. PIB = 3.635 x 10^11 USD
```

## Ejemplo trabajado

**Problema (LatAm, gastronómico).** GastroLatam quiere estimar cuánto pesa, en bytes, almacenar los pedidos de 5 años si tiene **12.000 pedidos/mes** y cada pedido pesa **2.5 kB** en disco. ¿Cuántos GB necesita?

Paso 1 — Pedidos en 5 años:
```
12.000 pedidos/mes × 12 meses/año × 5 años
= 1.2×10^4 × (12×5)
= 1.2×10^4 × 60
= 1.2×10^4 × 6×10^1
= 7.2 × 10^5 pedidos        (720.000 pedidos)
```

Paso 2 — Bytes totales. `2.5 kB = 2.5 × 10^3 bytes`:
```
7.2×10^5 pedidos × 2.5×10^3 bytes/pedido
= (7.2 × 2.5) × 10^(5+3)
= 18 × 10^8
= 1.8 × 10^9 bytes          (renormalizado: 18 = 1.8×10^1)
```

Paso 3 — Convertir a GB (1 GB = 10^9 bytes, base decimal SI):
```
1.8 × 10^9 bytes ÷ 1 × 10^9 bytes/GB = 1.8 GB
```

Verificación de orden de magnitud (sanity check mental): cientos de miles de pedidos (~10^5) por unos miles de bytes (~10^3) ≈ 10^8 a 10^9 bytes ≈ del orden de **1 GB**. Coincide. ✅

**Resultado: ≈ 1.8 GB** para 5 años de pedidos. (Nada de qué preocuparse: cabe en cualquier disco.)

## Errores comunes / trampas

- **Sumar exponentes al sumar números.** Solo se suman exponentes en la *multiplicación*. Para sumar/restar hay que **igualar exponentes primero**: `1.5×10^6 + 3×10^5 = 1.5×10^6 + 0.3×10^6 = 1.8×10^6`.
- **Olvidar renormalizar.** `18×10^8` no está en forma estándar; lo correcto es `1.8×10^9`. Dejarlo mal te hace leer mal el orden de magnitud.
- **Billón inglés vs español.** *billion* = 10⁹ (giga), *billón* español = 10¹² (tera). Diferencia de 1000×.
- **Mayúsculas/minúsculas de prefijos.** `m` = mili (10⁻³) pero `M` = mega (10⁶): ¡difieren por un factor de mil millones! `k` (kilo) siempre minúscula.
- **kB/KB/KiB.** Base decimal (1 kB = 10³) vs binaria (1 KiB = 2¹⁰ = 1024). Para discos/RAM la diferencia se acumula: 1 TB de disco ≈ 0.909 TiB reales.
- **Confiar en `log10` de float para el exponente.** En bordes (potencias exactas de 10) puede devolver el entero equivocado por error de redondeo. Por eso el código incluye la corrección `if m >= 10 / elif m < 1`.
- **Redondear la mantisa demasiado pronto** y arrastrar el error. Redondea **una sola vez al final** (ver módulo de cifras significativas).

### Mini-checklist de exactitud
- [ ] ¿La mantisa quedó en `1 ≤ |m| < 10` (forma normalizada)?
- [ ] ¿Hice el sanity check de orden de magnitud (el resultado cae donde esperaba la potencia de 10)?
- [ ] ¿Usé el prefijo y la base (decimal SI vs binaria) correctos, sin confundir M con m ni billón ES con billion EN?

## Cruces
- [[05-cifras-significativas-y-redondeo]] — cuántos dígitos de la mantisa son confiables y cuándo redondear.
- [[06-estimacion-y-sanity-checks]] — el orden de magnitud es la herramienta #1 de estimación rápida.
- [[15-potencias-y-raices]] — las potencias de 10 son la base de toda la notación.
- [[16-logaritmos]] — `log10` da directamente el orden de magnitud.
- [[37-conversion-de-unidades]] — los prefijos (k, M, G) son conversiones de unidades disfrazadas.
