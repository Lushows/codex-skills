# 174 — Descarboxilación: la cinética completa y cómo calcularla de verdad

Descarboxilar es quitarle el –COOH al cannabinoide ácido para volverlo neutro: THCA → Δ9-THC + CO₂. Suena
trivial y es donde se pierde más producto en la industria, porque casi todo el mundo lo hace por receta
("180 °C, 30 minutos") sin entender que es una **reacción de primer orden con una reacción competidora de
degradación**. Si te pasas de temperatura conviertes bien y luego quemas el THC hacia CBN; si te quedas
corto, entregas un aceite con la mitad del activo sin activar y una etiqueta que miente. Este módulo te da
la ecuación, los números y el criterio de parada.

Términos:
- **descarboxilación (decarboxylation, "decarb")** = pérdida de CO₂ del grupo carboxilo.
- **cinética de primer orden (first-order kinetics)** = la velocidad es proporcional a lo que queda:
  `-d[THCA]/dt = k·[THCA]`.
- **constante de velocidad k (rate constant)** = cuán rápido va, en `s⁻¹`; depende de la temperatura.
- **Arrhenius** = `k = A · exp(−Ea / (R·T))`, con `T` en kelvin.
- **Ea (energía de activación)** = la barrera, en `kJ/mol`.
- **vida media t½ (half-life)** = tiempo para convertir la mitad: `t½ = ln2 / k`.

## La ecuación

```
[THCA](t) = [THCA]₀ · e^(−k·t)              conversión X = 1 − e^(−k·t)
k(T)      = A · exp( −Ea / (R·T) )          R = 8,314 J·mol⁻¹·K⁻¹ ; T en K
t½        = ln 2 / k
t(X)      = −ln(1 − X) / k                  tiempo para alcanzar conversión X
```

Parámetros de trabajo: Perrotin-Brunel et al. reportaron para la descarboxilación de THCA una cinética de
pseudo-primer orden con **Ea ≈ 85 kJ/mol** y factor preexponencial **A ≈ 3,7 × 10⁸ s⁻¹**
(*Journal of Molecular Structure*, 2011, "Decarboxylation of Δ9-tetrahydrocannabinolic acid: kinetics and
molecular modeling"). Otros estudios sobre material vegetal en horno (80–160 °C, 5–120 min) y por
UHPSFC/PDA-MS (Wang et al., *Cannabis and Cannabinoid Research*, 2016) ajustan parámetros algo distintos
porque la matriz, la transferencia de calor y el espesor de la capa cambian todo.

> **Honestidad obligatoria:** los parámetros de arriba describen un sistema modelo. En tu horno, con tu
> biomasa, con tu espesor de bandeja, **k efectiva es otra**. Los números de abajo sirven para diseñar el
> experimento, no para reemplazarlo.

## Tabla calculada con esos parámetros (ILUSTRATIVO)

Calculado con `Ea = 85 kJ/mol`, `A = 3,7 × 10⁸ s⁻¹`. Verificado en código, no de memoria.

| T (°C) | T (K) | k (s⁻¹) | t½ | t para 95 % | t para 99 % |
|---|---|---|---|---|---|
| 80 | 353,15 | 9,9 × 10⁻⁵ | 117 min | 505 min | 776 min |
| 100 | 373,15 | 4,66 × 10⁻⁴ | 24,8 min | 107 min | 165 min |
| 110 | 383,15 | 9,53 × 10⁻⁴ | 12,1 min | 52,4 min | 80,5 min |
| 120 | 393,15 | 1,88 × 10⁻³ | 6,2 min | 26,6 min | 40,9 min |
| 130 | 403,15 | 3,58 × 10⁻³ | 3,2 min | 13,9 min | 21,4 min |
| 140 | 413,15 | 6,63 × 10⁻³ | 1,7 min | 7,5 min | 11,6 min |

Lectura práctica: **cada 10 °C aproximadamente duplica la velocidad** en este rango (eso es un Q10 ≈ 2, ver
`165`). Y por eso la receta popular "115 °C, 30–45 min" cae justo donde debe: conversión alta con poca
degradación.

## La reacción competidora que nadie modela

En paralelo corre `Δ9-THC → CBN` (oxidación/aromatización, ver `204`) y la evaporación de terpenos. Ambas
también son más rápidas con temperatura, pero la de degradación tiene su propia Ea. El resultado neto es una
**curva con máximo**: el THC neutro sube, llega a un pico y luego baja.

```
THC(t) = THCA₀ · (k1/(k2−k1)) · (e^(−k1·t) − e^(−k2·t))     (esquema consecutivo A→B→C)
t_optimo = ln(k2/k1) / (k2 − k1)
```

Consecuencia operativa: **no existe "descarbo completo sin pérdida"**. Existe un punto donde el THC neutro
es máximo, y hay que encontrarlo empíricamente para tu equipo (ver "Ejemplo aplicado").

## Cómo se mide / cómo se comprueba

1. **Curva experimental.** Toma una sola matriz homogénea (misma molienda, mismo lote). Coloca N bandejas
   idénticas. Saca una cada X minutos, enfría rápido en hielo, y analiza por **HPLC-DAD** (nunca GC: el GC
   descarboxila y te borra el experimento — ver `173`).
2. **Qué reportar en cada punto:** `THCA`, `Δ9-THC`, `CBN`, `% p/p base seca` y humedad. La humedad cambia
   durante el proceso, así que **sin base seca la curva miente**.
3. **Ajuste:** regresión de `ln([THCA]/[THCA]₀)` contra `t` → pendiente `= −k`. Si es recta, es primer orden.
   Si se curva, tienes gradiente térmico (capa muy gruesa) o dos poblaciones de material.
4. **Criterio de parada:** máximo de Δ9-THC, no "THCA = 0". Registra también el CBN: si supera tu límite
   interno, te pasaste.
5. **Balance de masa.** Verifica que `THC_total` antes ≈ `THC_total` después (ver `175`). Si cae mucho, no
   estás descarboxilando: estás degradando.

Ejecuta la cinética con `lab-tools/decarboxilacion.py` (Arrhenius, conversión, tiempo objetivo y curva) y el
balance con `lab-tools/thc_total.py`. Aritmética mental: prohibida.

```bash
python lab-tools/decarboxilacion.py --temp-c 115 --minutos 40 --ea 85 --a 3.7e8
python lab-tools/decarboxilacion.py --temp-c 115 --conversion 0.95   # tiempo objetivo
python lab-tools/decarboxilacion.py --test                            # autotest
```

## Ejemplo aplicado

Horno de convección, 2 kg de flor molida (2 mm) en bandejas de 1 cm de espesor, 115 °C (ILUSTRATIVO,
HPLC-DAD, `% p/p base seca`):

| t (min) | THCA | Δ9-THC | CBN | THC total |
|---|---|---|---|---|
| 0 | 21,4 | 0,9 | 0,05 | 19,66 |
| 15 | 12,1 | 9,2 | 0,08 | 19,81 |
| 30 | 5,4 | 14,6 | 0,14 | 19,34 |
| 45 | 1,9 | 17,2 | 0,26 | 18,87 |
| 60 | 0,7 | 17,4 | 0,49 | 18,01 |
| 90 | 0,1 | 16,3 | 1,05 | 16,39 |

Lectura: el **máximo de Δ9-THC está entre 45 y 60 min**. A partir de ahí solo pierdes: el THC total cae de
19,8 a 16,4 y el CBN se multiplica por 20. La decisión correcta es **parar a 50 min**, no "hasta que el THCA
sea cero". Si tu cliente compra por Δ9-THC, 90 min te cuesta 1,1 puntos de potencia sobre 2 kg.

## Errores comunes

- Descarboxilar "hasta que el THCA sea cero". Los últimos 2 % de THCA cuestan más THC del que rescatan.
- Capa gruesa de material: el centro no llega a temperatura y el borde se quema. Espesor y flujo de aire son
  variables del proceso, no detalles.
- Medir por GC y creer que "ya estaba descarboxilado". El GC descarboxila en el inyector.
- No reportar base seca: durante el decarb se pierde agua y el porcentaje sube solo por eso.
- Copiar la receta de otro equipo. Un horno doméstico, un rotavapor y un reactor encamisado tienen
  transferencias de calor incomparables.
- Ignorar el CBN. Es tu indicador de exceso de proceso y además aparece en el COA que verá tu cliente.
- Descarboxilar aceite ya extraído en presencia de oxígeno y luz: multiplicas la degradación (`61`, `204`).

## Conexión con otros módulos

→ `26-cinetica-de-reaccion.md` — la teoría de primer orden y Arrhenius.
→ `173-formas-acidas-thca-y-cbda.md` — qué es exactamente lo que estás convirtiendo.
→ `175-thc-total-y-el-factor-0877.md` — por qué el THC total se conserva y el Δ9 no.
→ `165-estudios-acelerados-y-arrhenius.md` — la misma matemática aplicada a vida útil.
→ `192-destilacion-de-cannabinoides.md` — dónde se descarboxila a escala industrial.
→ `204-estabilidad-y-degradacion-del-thc.md` — la reacción competidora hacia CBN.
→ `198-analisis-de-potencia-metodo.md` — cómo medir cada punto de la curva.
