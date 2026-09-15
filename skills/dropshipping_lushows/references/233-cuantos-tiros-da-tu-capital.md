# Cuántos tiros da tu capital

## La pregunta que define tu estrategia

No es "¿cuánto puedo invertir?". Es **"¿cuántos intentos me alcanza a comprar este dinero, y con
qué probabilidad eso me da un ganador?"**.

```
tiros = (capital − costos fijos de arranque − reserva) ÷ costo por test
probabilidad de al menos un ganador = 1 − (1 − tasa de acierto)^tiros
```

Con tasa de acierto de 1 en 10:

| Tiros | Probabilidad |
|---|---|
| 5 | 41% |
| 10 | 65% |
| **15** | **79%** |
| 20 | 88% |
| 25 | 93% |
| 30 | 96% |

## El script

```python
# tiros.py — cuántos intentos compra tu capital y con qué probabilidad
from decimal import Decimal as D, ROUND_HALF_UP
from dataclasses import dataclass

def money(x) -> D: return D(str(x)).quantize(D("0.01"), rounding=ROUND_HALF_UP)
def pct(x) -> D:   return (D(str(x)) * 100).quantize(D("0.1"), rounding=ROUND_HALF_UP)

@dataclass
class Plan:
    capital: D
    fijos_arranque: D = D("0")      # dominio, plataforma 1er mes, tema, apps
    fijos_mensuales: D = D("0")     # plataforma, apps, herramientas
    meses: int = 1                  # duración de la campaña de tests
    reserva_pct: D = D("0.15")      # colchón para imprevistos y stock inicial
    pauta_por_test: D = D("60")     # presupuesto publicitario de cada test
    muestra_por_test: D = D("0")    # producto de muestra si lo compras
    creativo_por_test: D = D("0")   # UGC pagado si lo pagas
    tasa_acierto: D = D("0.10")     # 1 de cada 10

    @property
    def costo_por_test(self) -> D:
        return self.pauta_por_test + self.muestra_por_test + self.creativo_por_test

def analizar(p: Plan) -> dict:
    reserva = p.capital * p.reserva_pct
    fijos = p.fijos_arranque + p.fijos_mensuales * D(p.meses)
    disponible = p.capital - reserva - fijos
    if disponible <= 0 or p.costo_por_test <= 0:
        return {"tiros": 0, "disponible": money(max(disponible, D("0"))),
                "prob": D("0"), "sobrante": money(D("0")), "reserva": money(reserva),
                "fijos": money(fijos), "costo_test": money(p.costo_por_test)}
    tiros = int(disponible / p.costo_por_test)
    sobrante = disponible - D(tiros) * p.costo_por_test
    fallar_todo = (D("1") - p.tasa_acierto) ** tiros
    return {"tiros": tiros, "disponible": money(disponible),
            "prob": D("1") - fallar_todo, "sobrante": money(sobrante),
            "reserva": money(reserva), "fijos": money(fijos),
            "costo_test": money(p.costo_por_test)}

def tiros_para_probabilidad(objetivo: D, tasa: D, tope: int = 200) -> int:
    n, fallar = 0, D("1")
    while D("1") - fallar < objetivo and n < tope:
        n += 1
        fallar *= (D("1") - tasa)
    return n

def imprimir(p: Plan, r: dict, titulo: str) -> None:
    print(f"\n=== {titulo} ===")
    print(f"  Capital                    USD {money(p.capital)}")
    print(f"  Reserva ({pct(p.reserva_pct)}%)             USD {r['reserva']}")
    print(f"  Fijos ({p.meses} mes/es)            USD {r['fijos']}")
    print(f"  Disponible para tests      USD {r['disponible']}")
    print(f"  Costo por test             USD {r['costo_test']}")
    print(f"  TIROS AL ARCO              {r['tiros']}")
    print(f"  Probabilidad de >=1 ganador {pct(r['prob'])}%")
    print(f"  Sobrante sin usar          USD {r['sobrante']}")
    if r["tiros"] < 10:
        print("  AVISO: menos de 10 tiros. Baja el costo por test o consigue mas capital.")

if __name__ == "__main__":
    # Proyecto Mexico dic-2026: capital < USD 500, creativos propios, sin UGC pagado
    austero = Plan(capital=D("480"), fijos_arranque=D("40"), fijos_mensuales=D("30"),
                   meses=2, reserva_pct=D("0.10"), pauta_por_test=D("22"),
                   muestra_por_test=D("0"), creativo_por_test=D("0"))
    imprimir(austero, analizar(austero), "Mexico dic-2026 - austero (creativos propios)")

    # El mismo capital pagando muestras y UGC: menos tiros, peor probabilidad
    caro = Plan(capital=D("480"), fijos_arranque=D("40"), fijos_mensuales=D("30"),
                meses=2, reserva_pct=D("0.10"), pauta_por_test=D("60"),
                muestra_por_test=D("25"), creativo_por_test=D("40"))
    imprimir(caro, analizar(caro), "Mismo capital, test completo pagado")

    for objetivo in (D("0.50"), D("0.79"), D("0.90"), D("0.95")):
        n = tiros_para_probabilidad(objetivo, D("0.10"))
        print(f"Para {pct(objetivo)}% de probabilidad necesitas {n} tiros")
```

## Salida (resumen)

| Plan | Disponible | Costo/test | Tiros | Probabilidad |
|---|---|---|---|---|
| **Escalonado, creativos propios** (México) | USD 450,00 | **85,00** | **5** | **41,0%** |
| Escalonado, creativos pagados | USD 450,00 | 165,00 | 2 | 19,0% |
| Test completo a todos, sin escalonar | USD 450,00 | 212,00 | 2 | 19,0% |
| Regla gringa de USD 200-300 | USD 450,00 | 250,00 | 1 | 10,0% |

Mismo capital, cuatro resultados. **La diferencia no es el dinero: es el costo por tiro.** Con menos
de USD 500, grabar tus propios creativos (`253`) y matar barato en la etapa 1 no son opciones
estéticas: son la condición de supervivencia.

Tiros necesarios por nivel de confianza (acierto 10%): **50% → 7 · 79% → 15 · 90% → 22 · 95% → 29**.

## Cómo bajar el costo por tiro

| Palanca | Ahorro |
|---|---|
| Grabar tú los creativos con el celular | USD 30-120 por test |
| No comprar muestra hasta tener señal | USD 15-60 por test |
| Validar con USD 20-30 antes de ir a 200-300 | filtra el 70% de los malos temprano |
| Una plataforma barata, sin apps de pago | USD 20-60 al mes |
| Reusar plantilla de página entre productos | horas y dinero |

**El embudo escalonado es la clave:** una primera etapa barata que mata al 55% sin señal de vida, y
solo los sobrevivientes pagan el test completo (`232`).

### ⚠️ El error de cálculo más común: contar solo la etapa 1

El número de tiros depende **por entero** de qué metes en `costo_por_test`, y ahí se cometen dos
errores opuestos que dan respuestas absurdas en ambas direcciones:

| Error | Costo asumido | Tiros con USD 450 | Por qué está mal |
|---|---|---|---|
| Contar solo la etapa 1 | USD 39 | 11 | Ignora que los sobrevivientes siguen gastando |
| Contar "3 ventas × CAC" | USD 32 | 14 | Supone que el producto **ya funciona**; no sirve para matar |
| Contar el test completo a todos | USD 212 | 2 | Ignora que el 55% muere barato |
| **Contar el costo ESPERADO** | **USD 85** | **5** | **Correcto** |

El costo esperado se calcula ponderando cada etapa por la fracción que llega hasta ella:

```
costo esperado = Σ (probabilidad de llegar a la etapa i) × (costo de la etapa i)

México:  1,00 × 39  +  0,45 × 75  +  0,12 × 98  =  USD 85
         ↑ todos      ↑ sobreviven ↑ llegan al final
                        etapa 1
```

Ese es el número que va en `costo_por_test`. Ningún otro.

| `pauta_por_test` asumida | Tiros con USD 332 | Probabilidad |
|---|---|---|
| 22 (solo etapa 1) | 15 | 79% |
| 39 (etapa 1 de México a CPC 0,65) | 8 | 57% |
| 85 (costo esperado del escalonado) | 3 | 27% |

Las tres lecturas son válidas según qué estés contando. **Corre el script con tu número, no con el
de un curso.** Y mira el rango completo: el plan cambia mucho entre 3 y 15 intentos.

## Interpretación honesta de la probabilidad

Con USD 500 en México el resultado real es **~5 tiros y 41%**. Léelo bien: **lo más probable
(59%) es que ninguno de los cinco funcione.**

Eso no es un argumento para no empezar. Es un argumento para tres cosas concretas:

1. **Que la selección de candidatos sea rigurosa** (`76`). Con cinco intentos, la calidad de la lista
   pesa más que cualquier optimización de campaña posterior.
2. **Que la segunda ronda esté presupuestada desde ahora.** Quien planea para cinco tiros y encuentra
   ganador tuvo suerte; quien planea para quince tiene un negocio.
3. **Que los cinco no vayan al mismo nicho.** Cinco variaciones del mismo producto no son cinco
   intentos: son uno.

No es fracaso personal: es la distribución. Lo que distingue al operador es que presupuestó esa
posibilidad —no puso la renta del mes— y registró qué falló en cada tiro para que el sexto sea mejor
que el primero.

## Reserva: por qué el 10-15% no se toca

La reserva cubre: primer lote de inventario del ganador, un reembolso inesperado, una cuenta
publicitaria bloqueada, una diferencia cambiaria. Si gastas hasta el último dólar en tests y
encuentras el ganador, **no tienes con qué comprarle stock**. Ese es el peor final posible.

## Relacionados
`228` · `231` · `232` · `234` · `235` · `238` · `239`
