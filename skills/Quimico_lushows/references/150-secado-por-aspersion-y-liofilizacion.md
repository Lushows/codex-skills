# 150 — Secado por aspersión y liofilización (donde nace el polvo que vas a vender)

Convertir el concentrado líquido en polvo es el paso más caro del proceso y el que casi ninguna pyme puede
hacer en casa. También es donde se define el **soporte** (carrier): el material que se agrega para que el
extracto seque y fluya, y que —según cuánto pongas— diluye tu activo. Aquí nace el truco de etiqueta más
extendido del sector: vender maltodextrina con extracto y llamarlo extracto. Entender este módulo te permite
pedirle al maquilador exactamente lo que necesitas y auditar lo que te entrega.

Términos: **secado por aspersión (spray drying)** = atomizar el líquido en aire caliente; el agua se evapora en
milisegundos. **Liofilización (freeze-drying, lyophilization)** = congelar y sublimar el hielo al vacío.
**Soporte / vehículo (carrier)** = maltodextrina, goma arábiga, almidón, celulosa; ayuda al secado y al flujo.
**Higroscópico (hygroscopic)** = que absorbe humedad del aire. **Temperatura de transición vítrea (Tg)** =
temperatura por encima de la cual un polvo amorfo se ablanda y se pega.

## Las dos tecnologías, cara a cara

| Criterio | Secado por aspersión | Liofilización |
|---|---|---|
| Temperatura del producto | Entrada 150–200 °C, salida 70–90 °C; la gota se mantiene más fría por evaporación | −40 a +30 °C |
| Tiempo de residencia | Segundos | 24–72 h |
| Costo por kg de polvo | Bajo | Alto (5–10× reportado como orden de magnitud típico) |
| Densidad del polvo | Media, esférico, fluye bien | Baja, poroso, esponjoso |
| Reconstitución | Buena | Excelente |
| Termolábiles | Riesgo moderado | Riesgo mínimo |
| Volátiles / aroma | Se pierden | Se conservan mejor |
| Necesita soporte | Casi siempre | A veces no |
| Escala mínima viable | Piloto desde ~1–2 L/h | Bandejas pequeñas |
| ¿Pyme colombiana? | **Maquila** | **Maquila** |

Elección práctica: **spray drying** para β-glucanos y extractos acuosos robustos; **liofilización** cuando el
activo es claramente termolábil (hericenonas, algunos triterpenos) o cuando el valor del producto lo aguanta.

## El soporte: dónde se diluye tu producto

Un extracto acuoso concentrado casi nunca seca solo por aspersión. Es pegajoso, higroscópico y se queda en la
pared de la cámara. Se agrega soporte:

| Soporte | Dosis típica sobre sólidos | Efecto | Nota |
|---|---|---|---|
| Maltodextrina DE 10–20 | 20–60 % p/p | Sube Tg, mejora el secado | Es almidón hidrolizado: **suma α-glucano** (`220`) |
| Goma arábiga | 10–30 % p/p | Buen encapsulante | Más cara |
| Almidón modificado | 20–50 % p/p | Similar a maltodextrina | También α-glucano |
| Celulosa microcristalina | 10–30 % p/p | Fluidez, no aporta glucano | Buena opción si te preocupa el α |
| Fibra de acacia / inulina | 10–40 % p/p | Prebiótico, no α-glucano | Interesante para posicionamiento |
| Sin soporte (0 %) | — | Solo posible con concentrados de alta Tg o liofilización | Ideal, poco frecuente |

**Aquí está el punto crítico para un producto de hongos:** si el maquilador usa maltodextrina, estás sumando
α-glucano a un producto cuya diferenciación es el β-glucano. Un COA que reporte α-glucano alto puede ser
sustrato de grano (fraude, `218`) **o** simplemente soporte de secado (legítimo, si se declara). Distinguir
ambos casos es tarea del expediente, no de la sospecha: pídele al maquilador la fórmula cuantitativa del
secado.

```
Efecto de dilución por soporte (ILUSTRATIVO)

  Concentrado con 62,0 % p/p de β-glucano en sólidos
  + maltodextrina al 40 % sobre sólidos totales

  β-glucano final = 62,0 × (1 − 0,40) = 37,2 % p/p base seca

  El extracto "de 62 %" llega al frasco como 37 %.
  Si tu etiqueta prometía 62 %, acabas de incumplir sin que nadie mintiera.
```

Esa cuenta hay que hacerla **antes** de imprimir etiqueta. Ejecútala en código, no de memoria
(`lab-tools/potencia_formula.py`).

## Parámetros que se especifican al maquilador

```
SECADO POR ASPERSIÓN — lo que va en la orden de maquila
  Temperatura de entrada       160–180 °C (típico para extractos botánicos)
  Temperatura de salida         80–90 °C   ← la que de verdad ve el producto
  Caudal de alimentación        ajustado para mantener la T de salida
  Tipo de atomizador            disco rotatorio o boquilla a presión
  Soporte y %                   DECLARADO y cuantificado
  Sólidos de alimentación       15–30 % p/v
  Humedad objetivo del polvo    ≤ 5 % p/p
  Envasado inmediato            bolsa de barrera + desecante (el polvo es higroscópico)

LIOFILIZACIÓN — lo que va en la orden
  Congelación                   −40 °C, velocidad controlada
  Presión de cámara             < 0,5 mbar
  Temperatura de estante        primaria −20 a 0 °C; secundaria 20–30 °C
  Tiempo total                  24–72 h
  Humedad residual objetivo     ≤ 3 % p/p
```

La temperatura que importa en spray drying es la de **salida**, no la de entrada. La gota se mantiene fría
mientras se evapora agua; el producto solo alcanza la temperatura de salida al final. Un maquilador que solo te
habla de la entrada no está controlando lo que te importa.

## Cómo se comprueba el polvo que te entregan

| Atributo | Método | Criterio orientativo |
|---|---|---|
| Humedad | Karl Fischer (`98`) | ≤ 5 % p/p |
| Actividad de agua | Higrómetro (`35`) | ≤ 0,40 |
| β-glucano | Megazyme K-YBGL (`221`) | Según especificación |
| α-glucano | Megazyme, fracción α (`220`) | Declarado y explicado |
| Densidad aparente y compactada | Probeta / tapped density | Para diseñar la cápsula (`154`) |
| Granulometría | Tamizado (`143`) | Para flujo y llenado |
| Solubilidad / reconstitución | Tiempo de dispersión en agua 40 °C | Producto en polvo bebible |
| Solventes residuales | GC-headspace (`87`) | Si la fracción alcohólica entró al secado |
| Microbiología | Recuentos y patógenos (`100`) | El secado reduce, no esteriliza |

Y el control que casi nadie pide: **balance de activo del secado**. mg de β-glucano que entraron al secador vs
mg que salieron en el polvo, corregido por soporte. Si no cierra, o hubo degradación o hubo pérdida en cámara.

## Ejemplo aplicado — pedir la maquila del secado

```
ORDEN DE MAQUILA (ILUSTRATIVA)
  Material: 6,05 L de concentrado de Ganoderma lucidum, 20,8 % p/v sólidos,
            β-glucano 8,32 g/L, sin conservantes, refrigerado a 4 °C.
  Proceso solicitado: secado por aspersión.
  Soporte: fibra de acacia, 25 % p/p sobre sólidos totales.  ← elegido para NO subir α-glucano
  T de salida solicitada: 85 ± 3 °C.
  Humedad objetivo: ≤ 4,5 % p/p.
  Envase de entrega: bolsa aluminizada 1 kg, sellada al vacío, con desecante.
  Entregables: polvo + balance de masa + registro de proceso + muestra de retención 100 g.

Rendimiento esperado (ILUSTRATIVO):
  sólidos del concentrado 1 258 g + soporte 419 g = 1 677 g teóricos
  polvo obtenido 1 512 g  →  rendimiento del secado 90,2 %
  β-glucano esperado en polvo = 50,3 g / 1 512 g = 3,33 % ... ← REVISAR: no cuadra con el objetivo
```

Ese último renglón es intencional: sirve para mostrar cómo se detecta un error. Si el número no da lo que
esperabas, **no ajustes la etiqueta: revisa el balance**. Puede ser un error de cuenta, un soporte mal dosado o
un concentrado que no tenía la potencia declarada. Rehacer la cuenta en código y con el laboratorio es el paso,
no maquillarla.

## Errores comunes

- Aceptar polvo sin saber qué soporte lleva ni en qué proporción. Es imposible declarar potencia sin ese dato.
- Usar maltodextrina en un producto de hongos y luego no poder explicar el α-glucano alto del COA.
- Especificar solo la temperatura de entrada. Lo que degrada es la de salida.
- Recibir el polvo en bolsa simple y descubrirlo apelmazado a las dos semanas (es higroscópico, Tg baja).
- Creer que el secado esteriliza. Reduce carga microbiana; no es un tratamiento validado de esterilización.
- No pedir muestra de retención al maquilador: sin ella no hay cómo investigar un problema después (`168`).
- Comparar polvos de proveedores distintos sin corregir por soporte y por humedad. No son comparables (`07`).

## Conexión con otros módulos

→ `149-concentracion-y-evaporacion.md` — el paso anterior, que define qué entra al secador.
→ `151-relacion-planta-extracto-y-ratios.md` — por qué el soporte destruye el sentido del "10:1".
→ `152-estandarizacion-de-extractos.md` — cómo se declara un polvo con soporte sin engañar.
→ `220-alfa-glucanos-y-almidon-el-confusor.md` — el problema de la maltodextrina en hongos.
→ `163-envase-primario-y-compatibilidad.md` — cómo se guarda un polvo higroscópico.