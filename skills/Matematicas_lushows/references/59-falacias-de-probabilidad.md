# 59 · Falacias de probabilidad

> **Qué resuelve / cuándo usarlo** — Te protege de los cuatro errores de razonamiento probabilístico que más dinero cuestan en negocios: la falacia del jugador, ignorar la tasa base, confundir P(A|B) con P(B|A) y la regresión a la media. Úsalo siempre que una decisión (apostar a una racha, interpretar un test, evaluar a un empleado, decidir si algo "funcionó") dependa de una probabilidad.

## Concepto (para no-experto)

Una **probabilidad** es un número entre 0 y 1 que mide qué tan posible es que algo pase: 0 = imposible, 1 = seguro, 0.5 = mitad y mitad. Una **falacia** es un razonamiento que *suena* lógico pero da un resultado falso. En probabilidad las falacias son peligrosas porque nuestra intuición fue diseñada para sobrevivir en la sabana, no para calcular bien. Veamos las cuatro más caras.

**1. Falacia del jugador.** Creer que los eventos *independientes* (que no se afectan entre sí) "se deben" entre sí. Si una moneda cae cara 5 veces seguidas, la intuición grita "ya toca sello". Falso: la moneda no tiene memoria. La probabilidad de cara en el sexto lanzamiento sigue siendo 0.5. Ejemplo cotidiano: "llevo 3 meses sin vender por WhatsApp, este mes seguro repunta" — solo es cierto si algo *cambió* (más anuncios, mejor pitch); el calendario por sí solo no debe nada.

**2. Ignorar la tasa base.** La **tasa base** (o *prior*) es qué tan común es algo *antes* de tener evidencia. Si una enfermedad afecta a 1 de cada 1.000 personas, esa es la tasa base. Cuando llega un test positivo, la gente se olvida de que el evento es raro de entrada y sobreestima el resultado. En negocio: "el sistema marcó a este cliente como fraude" significa poco si el fraude real es 0.1% de las transacciones — la mayoría de las alertas serán falsas alarmas.

**3. Confundir P(A|B) con P(B|A).** La notación **P(A|B)** se lee "probabilidad de A *dado* B" (sabiendo que B ocurrió). La falacia (también llamada "del fiscal") es asumir que P(A|B) = P(B|A). No son lo mismo. Ejemplo: P(tiene 4 patas | es perro) ≈ 1, pero P(es perro | tiene 4 patas) es bajísimo (también hay gatos, mesas, vacas). Confundirlas hace condenar inocentes y comprar humo.

**4. Regresión a la media.** La **media** es el promedio. Cuando una medición tiene componente de azar, un valor *extremo* tiende a ser seguido por uno más *normal* — no porque algo lo cause, sino por estadística pura. El mejor mes de ventas suele ir seguido de uno peor; el peor, de uno mejor. El error es atribuir ese rebote a una acción ("regañé al equipo y mejoró") cuando habría pasado solo.

## Fórmulas / método

Definiciones base (símbolos):

- `P(A)` = probabilidad del evento A. Adimensional, en [0, 1].
- **Independencia** entre A y B:
  `P(A y B) = P(A) · P(B)` y `P(A|B) = P(A)`.
  → De ahí la falacia del jugador: el pasado no cambia `P(A)`.

- **Probabilidad condicional**:
  `P(A|B) = P(A y B) / P(B)`, con `P(B) > 0`.

- **Teorema de Bayes** (invierte la condicional, cura los errores 2 y 3):

  `P(A|B) = [ P(B|A) · P(A) ] / P(B)`

  con `P(B) = P(B|A)·P(A) + P(B|¬A)·P(¬A)` (ley de probabilidad total).
  Aquí `P(A)` es la **tasa base**; `¬A` significa "no A".

- **Regresión a la media** — modelo: cada observación `X = μ + ruido`, donde `μ` es el valor verdadero y el ruido tiene media 0. Si observas un `X` muy lejos de `μ`, la siguiente observación, en promedio, estará *más cerca* de `μ`. Cuantitativamente, si dos mediciones tienen correlación `r` (entre -1 y 1), el valor esperado de la segunda, dado que la primera estuvo a `z` desviaciones de la media, es `r · z` desviaciones. Como `|r| < 1`, siempre se acerca a la media.

## Verificación en código

```python
# Python 3 — falacias de probabilidad, exactas con fractions y simulación de control
from fractions import Fraction as F
import random

# --- 1. FALACIA DEL JUGADOR ---
# Tras 5 caras seguidas, ¿P(cara) en el 6º lanzamiento?
p_cara = F(1, 2)
print("1) P(cara | 5 caras antes) =", p_cara, "= 0.5  -> la moneda no tiene memoria")

# Verificación 2ª vía: simular y filtrar SOLO las rachas de 5 caras,
# luego ver la frecuencia de cara en el siguiente lanzamiento.
random.seed(42)
sig_caras = sig_total = 0
hist = []
for _ in range(2_000_000):
    flip = random.random() < 0.5  # True = cara
    if len(hist) >= 5 and all(hist[-5:]):  # las 5 anteriores fueron cara
        sig_total += 1
        if flip:
            sig_caras += 1
    hist.append(flip)
freq = sig_caras / sig_total
assert abs(freq - 0.5) < 0.01, freq
print("   sim: frecuencia de cara tras 5 caras =", round(freq, 4), "(~0.5) OK")

# --- 2 y 3. TASA BASE + invertir la condicional (Bayes) ---
# Fraude: tasa base 0.1%. Detector: sensibilidad 99%, falsos positivos 2%.
P_F   = F(1, 1000)          # P(fraude)  = tasa base
P_noF = 1 - P_F
P_pos_dado_F   = F(99, 100) # P(+|fraude)  = sensibilidad
P_pos_dado_noF = F(2, 100)  # P(+|no fraude) = tasa de falso positivo

# P(+) por ley de probabilidad total
P_pos = P_pos_dado_F * P_F + P_pos_dado_noF * P_noF
# Bayes: lo que de verdad importa = P(fraude | +)
P_F_dado_pos = (P_pos_dado_F * P_F) / P_pos
print("\n2/3) P(fraude|+) =", P_F_dado_pos, "=", round(float(P_F_dado_pos), 4))
print("   La intuición dice ~0.99; la realidad es", f"{float(P_F_dado_pos):.1%}")

# Verificación 2ª vía: conteo bruto sobre 1,000,000 de transacciones (sin Bayes)
N = 1_000_000
fraudes = N * 1 // 1000          # 1,000 fraudes
no_fraudes = N - fraudes         # 999,000
verd_pos = fraudes * 99 // 100               # detector acierta el 99%
falsos_pos = no_fraudes * 2 // 100           # 2% de los limpios
P_check = F(verd_pos, verd_pos + falsos_pos)
assert P_check == P_F_dado_pos, (P_check, P_F_dado_pos)
print("   verificación por conteo =", P_check, "-> coincide con Bayes OK")

# --- 4. REGRESIÓN A LA MEDIA ---
# Ventas mensuales = nivel real 100 + ruido N(0, 20). Tomo el TOP 10% de meses
# y miro el mes siguiente: debe bajar hacia 100 SIN que cambie nada.
import statistics
random.seed(7)
serie = [100 + random.gauss(0, 20) for _ in range(200_001)]
pares = list(zip(serie, serie[1:]))           # (mes, mes_siguiente)
umbral = sorted(s[0] for s in pares)[int(len(pares) * 0.9)]  # corte top 10%
top = [(a, b) for a, b in pares if a >= umbral]
prom_pico = statistics.mean(a for a, b in top)
prom_sig  = statistics.mean(b for a, b in top)
print("\n4) Meses pico: promedio =", round(prom_pico, 1),
      "-> mes siguiente promedio =", round(prom_sig, 1))
assert prom_sig < prom_pico, "debe regresar hacia 100"
print("   Bajó solo, sin causa real -> regresión a la media OK")
```

Salida esperada (valores clave): `P(fraude|+) = 99/2097 ≈ 0.0472` (¡4.7%, no 99%!), la simulación de la moneda ≈ 0.5, y el mes pico (~125) seguido de uno cercano a ~100.

## Ejemplo trabajado

**Caso GastroLatam — alerta de "cliente comprador caliente".** El bot Luis marca leads como "alta intención de compra". De cada 100 leads reales, solo **5 compran** (tasa base = 5%). El detector: cuando alguien va a comprar, lo marca el 90% de las veces (sensibilidad); pero también marca al 20% de los que NO van a comprar (falsos positivos). Llega una alerta: ¿cuál es la probabilidad real de que ESE lead compre?

Paso a paso (por conteo, lo más intuitivo, sobre 1.000 leads):

1. Compradores reales: `1.000 × 5% = 50`.
2. No compradores: `1.000 − 50 = 950`.
3. Alertas correctas (verdaderos positivos): `50 × 90% = 45`.
4. Alertas falsas (falsos positivos): `950 × 20% = 190`.
5. Total de alertas: `45 + 190 = 235`.
6. P(compra | alerta) = `45 / 235 = 0.1915…` ≈ **19.1%**.

Verificación por Bayes:
`P(C|A) = (0.90 × 0.05) / (0.90×0.05 + 0.20×0.95) = 0.045 / 0.235 = 0.1915…` → **19.1 %** (coincide).

**Lectura para el negocio:** una alerta NO significa "casi seguro compra" (el error de confundir P(alerta|compra)=90% con P(compra|alerta)). Significa ~1 de cada 5. Conclusión accionable: vale la pena hacer seguimiento (19% es 4× la tasa base de 5%), pero el operador no debe prometerle nada al cliente ni desgastarse asumiendo venta segura. **Unidad: probabilidad adimensional, 19.1% de los alertados compran.**

## Errores comunes / trampas

- **Falacia del jugador / "mano caliente"**: asumir que rachas en eventos independientes obligan un cambio. Pregunta de control: *¿el resultado pasado altera físicamente la probabilidad?* Si no, `P` no se mueve.
- **Olvidar la tasa base**: dejarse impresionar por una sensibilidad alta (90%, 99%) ignorando que el evento es raro. Siempre arranca de cuántos casos reales hay en 1.000.
- **Invertir la condicional**: tratar "casi todos los compradores activan la alerta" como "casi todos los alertados compran". Son cantidades distintas; usa Bayes.
- **Atribuir causa a la regresión a la media**: creer que el rebote tras un extremo prueba que tu intervención funcionó. Sin **grupo de control** (un grupo comparable sin la intervención) no puedes separar el efecto real del rebote estadístico — ver [[68-ab-testing]].
- **Confundir independencia con incorrelación, o falsos positivos con falsos negativos**: define cada probabilidad con palabras completas ("P(positivo dado sano)") antes de meterla en la fórmula.

## Cruces

- [[50-fundamentos-de-probabilidad]] — qué es probabilidad, eventos, independencia.
- [[51-reglas-de-probabilidad]] — suma, producto y probabilidad condicional.
- [[52-teorema-de-bayes]] — la herramienta exacta para invertir P(A|B) y usar la tasa base.
- [[63-correlacion-vs-causalidad]] — por qué la regresión a la media engaña sobre causas.
- [[69-estadistica-enganosa]] — cómo estos errores se usan para manipular números.

---

**Mini-checklist de exactitud**
- [ ] ¿Escribí cada condicional con palabras completas ("P(X dado Y)") antes de calcular, para no invertirla?
- [ ] ¿Incluí la tasa base y verifiqué el resultado por conteo bruto sobre 1.000 casos, además de Bayes?
- [ ] Si interpreto un rebote, ¿tengo grupo de control que descarte la regresión a la media?
