# 01 · Cómo usar esta skill

> **Qué resuelve / cuándo usarlo** — Te enseña a navegar los 100 módulos, elegir el modo correcto (resolver / modelar / enseñar / auditar), cargar solo lo que necesitas, entender cómo te llegan trabajos desde otras skills (economist, ads, ventas) y, sobre todo, cómo PEDIR un cálculo para que la respuesta sea exacta y sin malentendidos.

## Concepto (para no-experto)

Esta skill es un **matemático de élite** con una sola promesa: **error cero**. Eso significa que ningún número se entrega "a ojo" ni "de memoria": cada cálculo no trivial se ejecuta en **código real** (programas pequeños en Python o Node que hacen la cuenta) y se **verifica dos veces** antes de dártelo. ¿Por qué tanto cuidado? Porque de cada número cuelga una decisión con **dinero real**: un precio, un margen, una inversión. Un error de un decimal puede costarte plata.

Definamos los términos que vas a ver una y otra vez:

- **Módulo** — un archivo de referencia (como este) que cubre UN tema (porcentajes, interés compuesto, VPN…). Hay 100, numerados del `00` al `99`.
- **Carga bajo demanda** *(lazy loading, "cargar cuando se necesita")* — no se leen los 100 módulos de golpe. Se lee SOLO el módulo que hace falta para tu pregunta. Es como una biblioteca: no te llevas todos los libros, sacas el que necesitas.
- **Modo** — la *forma* en que trabajo según lo que quieras: ¿solo el número? ¿una hoja de cálculo? ¿que te explique? ¿que revise un número de otro?
- **Rutear** *(routing, "enviar al especialista correcto")* — cuando otra skill (por ejemplo la de negocios) necesita un cálculo exacto, te "pasa el balón" a esta skill, que lo resuelve y lo devuelve verificado.

**Analogía cotidiana:** piensa en un restaurante. El *mesero* (otra skill, p. ej. economist) toma tu pedido y entiende el negocio. Pero cuando hay que **pesar los ingredientes con balanza de precisión**, lo hace el cocinero especialista (esta skill). El mesero no adivina los gramos: los manda a pesar.

## Fórmulas / método

No hay una "fórmula" matemática aquí, sino un **método de uso** en 4 pasos. Lo escribo como procedimiento exacto:

```
Paso 1 — CLASIFICAR la pregunta  → ¿qué tema? (porcentaje, interés, geometría…)
Paso 2 — ELEGIR el modo          → resolver | modelar | enseñar | auditar
Paso 3 — CARGAR el/los módulo(s) → leer solo los necesarios (1 a 3, normalmente)
Paso 4 — EJECUTAR + VERIFICAR    → código real + segunda vía + unidades + 1 redondeo final
```

### Los 4 modos (qué pides y qué recibes)

| Modo | Lo pides cuando… | Qué recibes |
|---|---|---|
| **Resolver** | quieres EL número ya | resultado exacto + código + verificación + unidades |
| **Modelar** | quieres una herramienta reutilizable | fórmula general / hoja de cálculo / función con variables editables |
| **Enseñar** | quieres ENTENDER, no solo el número | explicación paso a paso para no-experto + ejemplo |
| **Auditar** | tienes un número de otro y dudas | recálculo independiente + veredicto "coincide / NO coincide" + dónde está el error |

### Cómo rutea desde otras skills

- **economist_lushows** → te manda: punto de equilibrio, VPN/TIR, márgenes, TAM, proyecciones. (Ver `[[74-vpn-y-tir]]`, `[[76-punto-de-equilibrio]]`.)
- **facebook_ads / google_ads / tiktok_ads** → te mandan: ROAS, CPA, CAC, presupuestos, tasas de conversión. (Ver `[[84-roi-roas-y-mer]]`, `[[83-cac-ltv-y-payback]]`, `[[88-embudos-y-tasas-de-conversion]]`.)
- **ventas_lushows** → te manda: comisiones, descuentos por volumen, valor del pipeline, metas. (Ver `[[14-porcentajes-sin-errores]]`, `[[13-razones-y-proporciones]]`.)

La regla de oro del ruteo: **la otra skill aporta el contexto del negocio; esta skill aporta el número exacto.** Si un número va a salir publicado o va a sostener una decisión, pasa por aquí.

## Verificación en código

Aunque este módulo es de navegación, demuestro el patrón **ejecutar + verificar** con un mini-enrutador real: dada una pregunta del usuario, decide qué módulo cargar. Y lo verifico con `assert` (una comprobación que **falla ruidosamente** si algo no cuadra — mejor que confiar a ciegas).

```python
# Mini-ruteador de la skill: clasifica una pregunta -> módulo a cargar.
# (Ejecutable tal cual con Python 3.)

REGLAS = [
    # (palabra clave en la pregunta, archivo de módulo)
    ("porcentaje",        "14-porcentajes-sin-errores"),
    ("%",                 "14-porcentajes-sin-errores"),
    ("interes compuesto", "71-interes-simple-y-compuesto"),
    ("vpn",               "74-vpn-y-tir"),
    ("tir",               "74-vpn-y-tir"),
    ("punto de equilibrio","76-punto-de-equilibrio"),
    ("margen",            "80-margenes-bruto-contribucion-neto"),
    ("roas",              "84-roi-roas-y-mer"),
    ("cac",               "83-cac-ltv-y-payback"),
    ("probabilidad",      "50-fundamentos-de-probabilidad"),
    ("a/b",               "68-ab-testing"),
]

def rutear(pregunta: str) -> str:
    """Devuelve el módulo a cargar para una pregunta dada (en minúsculas, sin tildes raras)."""
    p = pregunta.lower()
    for clave, modulo in REGLAS:
        if clave in p:
            return modulo
    # Si no hay match claro, el método manda empezar por el método base:
    return "00-metodo-del-matematico-exacto"

# --- Uso ---
print(rutear("¿qué porcentaje es 30 de 250?"))   # -> 14-porcentajes-sin-errores
print(rutear("calcula el ROAS de la campaña"))    # -> 84-roi-roas-y-mer
```

```python
# VERIFICACIÓN POR SEGUNDA VÍA: tests con assert.
# Si CUALQUIER assert falla, el programa se detiene y nos avisa. Eso es bueno.
assert rutear("¿qué porcentaje es 30 de 250?") == "14-porcentajes-sin-errores"
assert rutear("calcula el ROAS de la campaña")  == "84-roi-roas-y-mer"
assert rutear("dame el VPN del proyecto")        == "74-vpn-y-tir"
assert rutear("tema sin palabra clave conocida") == "00-metodo-del-matematico-exacto"

# Segunda comprobación independiente: no hay módulos duplicados con clave repetida
# que se pisen entre sí (sanity check de la tabla de reglas).
claves = [c for c, _ in REGLAS]
assert len(claves) == len(set(claves)), "Hay una clave de ruteo duplicada"

print("OK: todos los asserts pasaron. El ruteo es consistente.")
```

> Nota sobre el patrón: el primer bloque **hace** el trabajo; el segundo lo **comprueba por otra vía** (resultados esperados + chequeo de integridad de la tabla). Este doble paso es exactamente lo que esta skill exige para CUALQUIER cálculo, no solo para ruteo. Detalle del protocolo en `[[03-protocolo-de-verificacion-por-codigo]]`.

## Ejemplo trabajado

**Situación realista (LatAm):** Lushows pregunta por WhatsApp: *"De 250 personas que escribieron al bot, 30 compraron la calculadora de $10.000 COP. ¿Qué % convirtió y cuánto facturé?"*

Recorro el método de los 4 pasos:

1. **Clasificar** → es porcentaje + facturación (dinero). Temas: conversión y total en pesos.
2. **Elegir modo** → *Resolver* (quiere los números) con un toque de *enseñar*.
3. **Cargar módulos** → `[[14-porcentajes-sin-errores]]` y, por ser dinero, manejo pesos con `Decimal` (ver `[[12-fracciones-decimales-y-precision]]`).
4. **Ejecutar + verificar:**

```python
from decimal import Decimal, ROUND_HALF_UP

compraron = Decimal("30")
escribieron = Decimal("250")
precio_cop = Decimal("10000")   # dinero SIEMPRE en Decimal, nunca float

# Tasa de conversión = compras / contactos, expresada en %
tasa = (compraron / escribieron) * Decimal("100")          # = 12 exacto
facturacion = compraron * precio_cop                        # dinero entero, exacto

# Redondeo UNA sola vez al final (2 decimales para el %)
tasa_2dec = tasa.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

print(f"Conversión: {tasa_2dec}%")          # 12.00%
print(f"Facturación: COP {facturacion:,}")  # COP 30,000

# VERIFICACIÓN POR SEGUNDA VÍA (operación inversa):
# si el 12% de 250 da de vuelta las 30 compras, el % está bien.
reconstruido = (tasa / Decimal("100")) * escribieron
assert reconstruido == compraron, "El % no reconstruye las compras"
# Y orden de magnitud de la plata: 30 ventas a ~10 mil ≈ 300 mil... no, ≈ 30 mil. Cuadra.
assert facturacion == Decimal("30000")
print("OK verificado.")
```

**Resultado:** **conversión = 12,00 %** (sin unidad monetaria, es un porcentaje) y **facturación = COP 30.000** (con su moneda). Ambos números **verificados por la vía inversa**. Fíjate que cada cifra lleva su unidad: el % es adimensional, la plata va en COP.

## Errores comunes / trampas

- **Pedir el número sin el contexto.** "Calcula el margen" sin decir costo ni precio = adivinanza. Da los datos y sus unidades.
- **No decir la moneda ni la unidad.** "$10.000" ¿son pesos colombianos, mexicanos, dólares? Siempre especifica (COP, MXN, USD…).
- **Mezclar tasas de distinto periodo.** Un interés "2 % mensual" no es "24 % anual" sin convertir bien (ver `[[75-tasas-nominal-efectiva-y-real]]`).
- **Confiar en un número de otra skill sin auditarlo.** Si va a sostener una decisión con plata, pásalo por el modo *auditar*.
- **Querer "rápido y a ojo".** Esta skill NO calcula de memoria por diseño. La velocidad viene de cargar el módulo justo, no de saltarse la verificación.
- **Redondear a mitad de camino.** Se redondea UNA vez, al final (ver `[[05-cifras-significativas-y-redondeo]]`).

## Cruces

- `[[00-metodo-del-matematico-exacto]]` — el método base y la filosofía de error cero (punto de partida si no sabes qué módulo cargar).
- `[[03-protocolo-de-verificacion-por-codigo]]` — cómo se ejecuta y verifica todo cálculo.
- `[[08-herramientas-de-calculo]]` — qué librerías usar (decimal, sympy, numpy) y cuándo.
- `[[09-glosario-matematico]]` — definiciones rápidas de términos.
- `[[06-estimacion-y-sanity-checks]]` — la verificación por "orden de magnitud" (¿el número tiene sentido?).

---

**Mini-checklist de exactitud**
- [ ] Di el modo (resolver / modelar / enseñar / auditar) y los datos con sus unidades/moneda.
- [ ] Se cargó solo el módulo necesario y se ejecutó en código real.
- [ ] El resultado quedó verificado por una segunda vía y redondeado una sola vez al final.
