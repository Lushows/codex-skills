# 117 — Playbook: tecnología y hardware

Para montar un negocio de producto físico con tecnología (un gadget, un dispositivo IoT, un equipo, un wearable, un accesorio electrónico). Aquí vive la economía más dura de todas: capital intensivo, ciclo largo, inventario y un margen que el software jamás te cobra. Si vas a fabricar algo, lee esto dos veces.

> Advertencia honesta: el hardware combina lo peor de tres mundos — la logística de un negocio de inventario (ver 110), el ciclo de desarrollo de un producto de software (ver 70), y el riesgo de capital de una fábrica. El upside existe, pero el "valle de la muerte" es real. La regla de oro del sector: **el hardware es difícil, y siempre cuesta el doble y tarda el triple de lo que crees.**

---

## Antes de cualquier número: pregunta país/ciudad

Aranceles de importación de componentes, IVA, certificaciones obligatorias (eléctricas, radio/RF, seguridad), costo de flete y de capital cambian TODO el modelo. No tomes ni una cifra de abajo como verdad para tu país. Para datos reales de costos, aranceles y certificaciones, ver módulo 21. Pregunta siempre: **¿en qué país fabricas, vendes y certificas?** antes de comprometer plata.

---

## Cómo se gana (y se pierde) plata en hardware

El margen de hardware es **flaco comparado con software** y se construye así:

```
Precio de venta
  − BOM (Bill of Materials: costo de todos los componentes)
  − Ensamblaje / mano de obra de fábrica
  − Empaque
  − Flete + aranceles + impuestos de importación
  = Costo unitario "landed" (puesto en bodega)

Precio − Costo landed = MARGEN BRUTO por unidad
```

**Conceptos clave (para no técnicos):**
- **BOM (Bill of Materials):** la lista de TODAS las piezas y su costo. Es el corazón de la economía del hardware.
- **MOQ (Minimum Order Quantity):** cantidad mínima que un proveedor te fabrica. Un chip puede tener MOQ de 5.000 unidades aunque tú quieras 100. Esto te obliga a inmovilizar capital.
- **NRE (Non-Recurring Engineering):** costo único de diseño, moldes (tooling), prototipos. Un molde de inyección de plástico puede costar miles de dólares antes de producir UNA sola unidad.
- **Landed cost:** lo que cuesta la unidad ya en tu bodega, con flete e impuestos incluidos. NUNCA uses solo el precio de fábrica.

**Regla del múltiplo:** en hardware, el precio de venta suele ser **3x a 5x el costo landed** (no 1.5x–2x como en retail simple), porque tienes que cubrir desarrollo, defectos, soporte, marketing y canal. Si tu múltiplo es menor a 3x, probablemente vas a perder plata sin darte cuenta (ver "trampas").

---

## Capital típico de arranque (orientativo, NO dato duro)

Depende brutalmente de la complejidad. Rangos ilustrativos para llevar un primer producto a producción de un lote pequeño:

| Tipo de producto | Capital de arranque orientativo* | Por qué |
|---|---|---|
| Accesorio simple (sin electrónica activa, p. ej. soporte, funda) | bajo (miles de USD) | molde + primer lote |
| Gadget electrónico básico (un PCB, batería, carcasa) | medio-alto (decenas de miles USD) | NRE + certificaciones + MOQ de componentes |
| Dispositivo conectado / IoT con app | alto (decenas a cientos de miles USD) | hardware + firmware + app + nube + certificaciones |
| Equipo regulado (médico, industrial) | muy alto | certificación puede costar más que el producto |

*Cifras orientativas para dimensionar, no presupuesto real. Para tu número exacto: cotiza BOM, moldes y certificaciones de TU producto en TU país (ver 21).

---

## Estructura de costos y márgenes típicos del sector

**Estructura de costos:** mayormente **costo variable alto** (BOM + ensamblaje + flete por unidad) y un **fijo fuerte de desarrollo** al inicio (NRE, certificaciones, prototipos).

**Márgenes brutos típicos (rangos orientativos, no datos duros):**

| Categoría | Margen bruto orientativo |
|---|---|
| Hardware "commodity" (accesorios genéricos) | bajo, ~20–35% |
| Hardware de marca / con diseño propio | ~35–50% |
| Hardware + software/servicio recurrente (modelo "razor + blades") | mixto: hardware ~20–40%, servicio mucho más alto |
| Software puro (comparación) | ~70–90% |

La diferencia es enorme: **por eso el santo grial del hardware es agregarle un ingreso recurrente** (suscripción, consumibles, servicio). El hardware vende la entrada; el software/servicio paga las cuentas. (ver 70 para la economía del software recurrente.)

---

## KPIs clave del sector (mide estos o vas a ciegas)

1. **Costo unitario a escala** — cuánto baja el BOM cuando produces 1.000 vs 100.000 unidades. La curva de costo es tu palanca de margen.
2. **Margen bruto por unidad (landed)** — precio − costo puesto en bodega. Si no es ≥ 3x el costo, alerta.
3. **Tasa de defectos / DPPM** (defectos por millón) o simplemente % de unidades falladas. Cada defecto = devolución + soporte + reputación.
4. **Días de inventario / rotación** — cuánto capital tienes congelado en cajas sin vender (ver 110).
5. **Costo de soporte y devoluciones (RMA)** por unidad vendida — el asesino silencioso del margen.
6. **(Si hay recurrente) LTV del servicio vs CAC** — para saber si el hardware "regalado" se paga con la suscripción (ver 53).

---

## Ejemplo numérico: BOM y margen de un gadget (cifras ILUSTRATIVAS)

Supongamos un dispositivo conectado sencillo. **Todas las cifras son inventadas para ilustrar el cálculo, no datos reales.**

**BOM (por unidad, a un lote moderado):**

| Componente | Costo unitario (ej.) |
|---|---|
| Placa + microcontrolador (PCB) | 8.00 |
| Sensor | 3.50 |
| Batería | 2.00 |
| Carcasa plástica (inyectada) | 2.50 |
| Cables / conectores / tornillería | 1.00 |
| Empaque y manual | 1.50 |
| **Subtotal BOM** | **18.50** |

**De BOM a costo landed (por unidad):**
```
BOM ......................... 18.50
Ensamblaje/mano de obra ...... 4.00
Flete + aranceles (estim.) ... 2.50
Defectos amortizados (~5%) ... 1.25
= Costo landed ............... 26.25
```

**Margen:**
```
Precio de venta sugerido (≈4x BOM) ... 79.00
− Costo landed ....................... 26.25
= Margen bruto por unidad ............ 52.75   (≈ 67% sobre precio)
```

**¡Cuidado! Eso NO es tu ganancia.** Falta restar lo que el ejemplo de margen bruto esconde:
```
Margen bruto/unidad ........... 52.75
− Comisión de canal/marketplace (~15% del precio ≈ 11.85)
− CAC (publicidad) repartido (~12.00 por unidad)
− Soporte/RMA por unidad (~3.00)
− Costos fijos repartidos (NRE, salarios, nube) (~10.00)
= Margen NETO por unidad ...... ~15.90
```

Y recuerda el **NRE inicial** que pagaste ANTES de vender una sola unidad (ej. molde 12.000 + certificaciones 8.000 + prototipos 5.000 = 25.000). A ~15.90 neto por unidad, necesitas vender **~1.575 unidades solo para recuperar el desarrollo** — sin contar el inventario que ya compraste. Ese es el "valle de la muerte" en un número.

---

## Cómo arrancar mínimo viable (MVP de hardware)

El error #1 es saltar directo a fabricar 10.000 unidades. Secuencia sensata:

1. **Prototipo "feo que funciona":** impresión 3D, componentes de desarrollo (Arduino/Raspberry), todo a mano. Solo prueba que la idea funciona.
2. **Valida demanda ANTES de fabricar:** preventa, lista de espera, crowdfunding, o una landing con botón de compra (ver 25). Que la gente prometa plata antes de que tú la gastes.
3. **Lote piloto pequeño:** la tirada más chica posible aunque el costo unitario sea feo. Aprende de fabricación real, defectos y soporte con pocas unidades.
4. **Cotiza el costo a escala** con el lote piloto en mano, para negociar y proyectar el margen real.
5. **Recién entonces** escala el lote, sabiendo BOM real, defectos reales y demanda probada.

Considera **white-label / ODM:** muchos productos exitosos son hardware genérico de fábrica (China u otros) con tu marca y tu software encima. Saltas casi todo el NRE. Validación rápida y barata.

---

## Trampas que matan a este negocio

- **Subestimar el desarrollo:** el firmware, las certificaciones, las iteraciones de molde SIEMPRE cuestan más y tardan más. Presupuesta el doble de tiempo y plata. Es la regla, no la excepción.
- **Inventario muerto:** fabricaste 10.000, vendiste 2.000, tienes 8.000 cajas congelando tu capital y ocupando bodega. El inventario es plata que no puedes usar (ver 110).
- **MOQ que te obliga a sobre-comprar:** componentes con mínimos altos te fuerzan a inmovilizar capital antes de validar demanda.
- **Olvidar el costo de soporte y devoluciones:** cada producto físico falla, se rompe, llega mal. El RMA, el reemplazo y el servicio post-venta se comen el margen que creías tener.
- **Pricing con múltiplo muy bajo (1.5x–2x):** parece competitivo, pero no cubre defectos, soporte ni canal. Vendes y te empobreces.
- **Certificaciones sorpresa:** vender electrónica/radio sin la certificación legal del país puede ser ilegal y costar más que el producto. Verifica requisitos vigentes ANTES de diseñar (ver 21).
- **Solo hardware, sin recurrente:** vendiste una vez y se acabó. Sin consumibles ni servicio, vuelves a empezar de cero cada mes. Diseña un ingreso recurrente desde el día uno (ver 70).
- **Tipo de cambio:** compras componentes en USD, vendes en moneda local. Una devaluación te borra el margen de un lote completo.

---

## Errores comunes

- Enamorarse del producto y no validar demanda antes de gastar en moldes.
- Calcular margen con el precio de fábrica en vez del **costo landed** (con flete, aranceles, defectos).
- No reservar caja para el **segundo lote**: el primero lo financiaste, pero el éxito te exige reponer inventario antes de cobrar todo el primero. Te quedas sin caja en pleno crecimiento (ver 35 sobre flujo de caja).
- Ignorar el soporte post-venta hasta que las devoluciones lo vuelven una crisis.

---

## Siguiente paso típico

Arma el **BOM real de tu producto** (cotiza cada componente en TU país, ver 21) y calcula el costo landed; luego decide tu precio con múltiplo ≥ 3x. Antes de fabricar cualquier lote, **valida demanda con preventa o lista de espera** (ver 25) y diseña desde ya un ingreso recurrente (consumible o servicio) que pague las cuentas que el hardware solo no cubre.
