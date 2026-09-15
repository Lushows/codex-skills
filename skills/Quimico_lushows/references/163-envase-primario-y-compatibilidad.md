# 163 — Envase primario y compatibilidad (el envase es parte de la formulación, no del marketing)

El envase primario es el que toca el producto. No es una decisión de diseño: es una decisión química. Define
cuánto oxígeno y cuánta humedad entran, cuánta luz pasa, qué migra del plástico al producto y qué se adsorbe
del producto al plástico. La vida útil que vas a declarar (`164`) es la vida útil **en ese envase**: cambiar el
frasco invalida el estudio. Y el error más caro de este módulo es tan común que tiene nombre propio en el
sector: guardar un aceite de cannabis en PET delgado y descubrir a los seis meses que faltan cannabinoides que
nadie se llevó — se pegaron a la pared.

Términos: **envase primario (primary packaging)** = el que está en contacto directo. **Secundario** = la caja.
**WVTR (water vapour transmission rate)** = velocidad de paso de vapor de agua, g/(m²·día). **OTR (oxygen
transmission rate)** = ídem para oxígeno, cm³/(m²·día). **Migración (leaching)** = algo del envase pasa al
producto. **Sorción / scalping (sorption)** = algo del producto se pega al envase. **Espacio de cabeza
(headspace)** = el aire que queda dentro.

## Materiales y sus propiedades barrera

| Material | Barrera a humedad | Barrera a oxígeno | Barrera a luz | Nota |
|---|---|---|---|---|
| Vidrio ámbar | Total | Total | Muy buena | El patrón oro; pesado y frágil |
| Vidrio claro | Total | Total | **Nula** | Solo con estuche secundario |
| HDPE (polietileno alta densidad) | Buena | Regular | Opaco si es blanco/pigmentado | El estándar de frascos de suplementos |
| PET | Regular | Buena | Nula (claro) / buena (ámbar) | Cuidado con lipofílicos: sorción |
| PP (polipropileno) | Buena | Regular | Según pigmento | Tapas, potes |
| Blíster PVC/aluminio | Regular | Regular | Buena | Barato; barrera media |
| Blíster PVdC o Aclar/aluminio | Muy buena | Muy buena | Buena | Para activos sensibles |
| Sachet aluminio laminado | Excelente | Excelente | Total | La mejor barrera práctica para polvos |
| Bolsa PE simple | **Mala** | **Mala** | Nula | No es envase primario de producto sensible |

Regla rápida por tipo de producto:

- **Polvo higroscópico de extracto** → sachet de aluminio laminado o frasco HDPE/vidrio con **desecante** y
  sello de inducción.
- **Cápsulas** → frasco HDPE opaco con sello de inducción + desecante, o blíster de alta barrera.
- **Tintura hidroalcohólica** → vidrio ámbar con gotero; el etanol ataca ciertos plásticos y adhesivos.
- **Aceite de cannabis** → vidrio ámbar. Punto.
- **Bebible acuoso** → PET o vidrio con cierre hermético; considerar oxígeno disuelto.

## Los tres fenómenos que hay que anticipar

**1. Sorción (el producto se pega al envase).** Las moléculas muy lipofílicas —cannabinoides, terpenos,
triterpenos, aromas— se absorben en las paredes de plásticos poliolefínicos y en sellos de silicona. El
resultado en el análisis: contenido más bajo del que se envasó, sin que haya degradación química. Se detecta
porque el balance no cierra y no aparecen productos de degradación.

**2. Migración (el envase pasa al producto).** Plastificantes, antioxidantes del polímero, tintas y adhesivos.
Con solventes (etanol, aceite) la migración sube mucho. Es el motivo por el que las tinturas van en vidrio.

**3. Permeación (entra lo de afuera).** Humedad y oxígeno. Es lo que arruina polvos higroscópicos y aceites.

```
CÁLCULO DE GANANCIA DE HUMEDAD (orientativo)

  Agua ganada (g) ≈ WVTR [g/(m²·día)] × área del envase (m²) × días × factor de gradiente

  Ejemplo (ILUSTRATIVO): frasco HDPE, área efectiva 0,012 m²,
  WVTR del material a 38 °C/90 % HR ≈ 0,35 g/(m²·día)
    a 24 meses (730 días): 0,35 × 0,012 × 730 ≈ 3,07 g de agua potencial
  Sobre 60 g de polvo, sería una ganancia enorme → por eso va DESECANTE
  y por eso el sello de inducción no es opcional.

  El desecante se dimensiona por su capacidad (g de agua por g de sílica).
  Haz la cuenta, no metas "un sobrecito" al azar.
```

## El envase de cierre infantil, la tapa y el sello

- **Sello de inducción** (foil sobre la boca del frasco): es la barrera real. Sin él, la tapa roscada permite
  intercambio de aire con cada apertura y, peor, permanente si la rosca no ajusta.
- **Cierre de seguridad para niños (child-resistant)**: en cannabis es exigencia común en varias
  jurisdicciones; a agosto de 2026 verifica lo aplicable en Colombia para tu categoría (`210`).
- **Gotero**: el bulbo de caucho o silicona **absorbe** y también puede aportar migración. Para tinturas de
  larga vida útil, prefiere goteros con bulbo compatible y verifica compatibilidad en el estudio de estabilidad.
- **Espacio de cabeza**: el oxígeno del headspace es el que oxida. Frascos llenos al máximo, o envasado bajo
  nitrógeno si el producto lo justifica.

## Cómo se comprueba la compatibilidad envase-producto

Este es un estudio propio, y es barato hacerlo bien:

```
ESTUDIO DE COMPATIBILIDAD ENVASE-CONTENIDO

  1. Envasa el producto real en los 2–3 envases candidatos (n ≥ 3 unidades por envase).
  2. Almacena en condiciones aceleradas: 40 °C / 75 % HR (`165`).
  3. Tiempos: 0, 1, 3 y 6 meses.
  4. Mide en cada punto:
       - contenido de activo (HPLC)        → detecta sorción y degradación
       - humedad y a_w del producto         → detecta permeación
       - aspecto, color, olor               → detecta migración y oxidación
       - masa del envase lleno              → detecta pérdida de volátiles/solvente
       - pH (líquidos)
       - opcional: barrido de extraíbles/lixiviables por GC-MS (`86`) si el activo es de alto valor
  5. Criterio: gana el envase donde el activo no baja y el producto no cambia.

Truco de diagnóstico: si el activo baja y NO aparecen productos de degradación
en el cromatograma, sospecha SORCIÓN al envase, no degradación química.
```

## Ejemplo aplicado — dos envases para dos productos

```
PRODUCTO A — cápsulas de extracto de reishi (higroscópico)
  Envase elegido: frasco HDPE blanco opaco 100 mL, tapa con sello de inducción,
                  desecante de sílica 2 g, estuche de cartón secundario.
  Racional: barrera de humedad + opacidad + el desecante absorbe lo que permea.
  Alternativa mejor y más cara: blíster de alta barrera (dosis protegida individualmente).

PRODUCTO B — aceite de CBD 30 mL
  Envase elegido: vidrio ámbar 30 mL, gotero con bulbo compatible, cierre de seguridad,
                  llenado a 30 mL exactos (headspace mínimo).
  Racional: cero sorción, cero migración, barrera total a oxígeno y a luz.
  Lo que NUNCA: PET claro o frasco plástico delgado — sorción de cannabinoides
                y fotodegradación de THC a CBN (`204`).
```

Cifras y elecciones **(ILUSTRATIVAS)**: la decisión final se toma con el estudio de compatibilidad de arriba
sobre tu producto real.

## Errores comunes

- Elegir el envase por estética y descubrir la incompatibilidad con producto ya en el mercado.
- Cambiar de frasco o de proveedor de frasco sin repetir estabilidad. El estudio es del sistema
  producto-envase, no del producto solo (`169`).
- Usar vidrio claro "porque se ve el producto" con un activo fotosensible.
- Omitir el sello de inducción para ahorrar centavos y perder la barrera completa.
- Meter desecante sin dimensionarlo por capacidad de absorción.
- No considerar el transporte: un camión en la vía a la costa puede superar los 50 °C en la carrocería. El
  envase y el producto tienen que aguantar eso, y no aparece en ningún estudio de anaquel.
- Ignorar la sorción en goteros y tapas con bulbo de caucho.
- Declarar vida útil de un envase y vender en otro formato sin datos propios.

## Conexión con otros módulos

→ `164-estabilidad-ich-q1-y-vida-util.md` — el estudio que se hace **en** este envase.
→ `165-estudios-acelerados-y-arrhenius.md` — las condiciones aceleradas del ensayo de compatibilidad.
→ `61-estabilidad-quimica-luz-calor-oxigeno.md` — los tres enemigos que el envase debe frenar.
→ `35-actividad-de-agua-y-humedad.md` — por qué el desecante y el sello importan tanto.
→ `204-estabilidad-y-degradacion-del-thc.md` — el caso donde la luz convierte producto en otro producto.
