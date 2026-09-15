# 32 — Coloides, emulsiones y espumas (lo que no es solución ni mezcla, y se te separa en la bodega)

Buena parte de tus productos no son soluciones verdaderas: son coloides. Un extracto de hongo concentrado
es una dispersión de polisacáridos; una bebida con CBD es una emulsión; un jarabe turbio es un coloide que
está perdiendo la pelea. La diferencia importa porque **un coloide no es termodinámicamente estable**: se
va a separar, la única pregunta es cuándo. Confundir "se ve homogéneo" con "es estable" produce el
problema más embarazoso del sector: producto que se ve perfecto en la reunión y llega separado a la
estantería del cliente.

Términos: **coloide (colloid)** = dispersión de partículas de ~1 nm a 1 µm que no sedimentan rápido y no
se ven a simple vista. **fase dispersa (dispersed phase)** = lo que está repartido; **fase continua
(continuous phase)** = el medio. **emulsión (emulsion)** = líquido en líquido (aceite en agua, O/W, o agua
en aceite, W/O). **espuma (foam)** = gas en líquido. **potencial zeta (zeta potential)** = carga eléctrica
efectiva de la superficie de la partícula, en mV; predice repulsión y estabilidad. **floculación
(flocculation)** = las gotas se agrupan pero no se fusionan; **coalescencia (coalescence)** = se fusionan y
ya no hay vuelta atrás.

## El zoológico de los coloides que te tocan

| Sistema | Fase dispersa en continua | Ejemplo en tu mundo |
|---|---|---|
| Emulsión O/W | Aceite en agua | Bebida con nanoemulsión de CBD (`157`) |
| Emulsión W/O | Agua en aceite | Cremas y ungüentos tópicos (`196`) |
| Suspensión | Sólido en líquido | Polvo de hongo en agua; "shot" agitable |
| Sol / dispersión polimérica | Macromolécula en agua | β-glucano en decocción concentrada (`219`) |
| Gel | Red sólida con líquido atrapado | Gomas, gummies, geles tópicos |
| Espuma | Gas en líquido | Espuma en el tanque de extracción (problema operativo) |
| Aerosol | Líquido en gas | Cámara de secado por aspersión (`150`) |

## Cómo mueren las emulsiones (y qué hacer con cada muerte)

| Mecanismo | Qué se ve | ¿Reversible? | Cómo se frena |
|---|---|---|---|
| Cremado / sedimentación | Capa arriba o abajo, se reintegra al agitar | Sí | Bajar tamaño de gota, subir viscosidad (`34`) |
| Floculación | Turbidez que crece, grumos finos | A veces | Subir repulsión: potencial zeta o impedimento estérico |
| Maduración de Ostwald | Las gotas grandes crecen a costa de las chicas | No | Distribución estrecha; aceite poco soluble (evitar aceites muy solubles) |
| Coalescencia | Aceite libre en la superficie | No | Película interfacial fuerte: tensioactivo adecuado (`33`) |
| Inversión de fases | Cambia de O/W a W/O | No | Controlar temperatura y proporción de fases |
| Ruptura química (oxidación) | Olor rancio, color | No | Antioxidante, envase, N₂ (`24`, `61`) |

```
Ley de Stokes — velocidad de cremado de una gota:
   v = (2 · r² · (ρ_gota − ρ_medio) · g) / (9 · η)

r = radio (m) · ρ = densidad (kg/m³) · g = 9,81 m/s² · η = viscosidad del medio (Pa·s)

Lo que enseña:  v ∝ r²  →  bajar el diámetro de gota a la mitad reduce el cremado 4 veces
                v ∝ 1/η →  espesar el medio frena el cremado proporcionalmente
                v ∝ Δρ  →  si igualas densidades, el cremado se detiene
```

Esas tres son **todas** las palancas de una emulsión estable, y por eso una nanoemulsión de 50 nm en una
bebida no crema en meses mientras una emulsión gruesa de 5 µm se separa en días (`157`).

## Potencial zeta: el número que predice la estabilidad

Las partículas coloidales suelen tener carga superficial. Si todas tienen la misma carga se repelen y no se
juntan. El **potencial zeta** mide esa carga efectiva:

```
|ζ| > 30 mV   →  repulsión suficiente, sistema estable por vía electrostática
|ζ| 10–30 mV  →  zona gris, estabilidad marginal
|ζ| < 10 mV   →  agregación probable

Cuidado: el potencial zeta depende del pH y de la fuerza iónica. Añadir sal APLASTA la doble capa
eléctrica y puede desestabilizar una emulsión que era estable en agua (`23`).
```

La alternativa a la estabilización electrostática es la **estérica**: polímeros o tensioactivos no iónicos
que forman una barrera física. Es menos sensible a la sal y por eso se prefiere en bebidas con
electrolitos (`33`).

## Cómo se mide

| Pregunta | Método | Unidad |
|---|---|---|
| ¿Qué tamaño tienen mis gotas? | Dispersión dinámica de luz (DLS) o difracción láser | d50, d90 en nm o µm; PDI (índice de polidispersidad) |
| ¿Qué tan estable es? | Potencial zeta por electroforesis láser | mV, con pH y conductividad declarados |
| ¿Se va a separar? | Envejecimiento acelerado: centrífuga (p. ej. 3 000 g, 30 min) y ciclos térmicos 4/40 °C | Presencia de separación visible; % de fase separada |
| ¿Sigue igual a los 6 meses? | Estudio de estabilidad real: tamaño, ζ, turbidez, activo | Deriva de d50 y % de activo (`164`) |
| ¿Cuánta turbidez tiene? | Turbidímetro nefelométrico | NTU |
| ¿Cuánto activo hay en cada fase? | Separar por centrifugación y cuantificar cada fase por HPLC | mg/mL; balance de masa (`06`) |
| ¿Cuánta espuma genera? | Prueba de Ross-Miles o agitación estandarizada | Altura de espuma en mm vs tiempo |

Regla dura: **d50 sin PDI no dice nada**. Una emulsión con d50 de 100 nm y PDI 0,45 tiene una cola de
gotas grandes que van a cremar; con PDI < 0,2 es monodispersa y se comporta.

## Ejemplo aplicado — bebida de CBD: emulsión gruesa vs nanoemulsión

Bebida de 330 mL con 10 mg de CBD, dos rutas de proceso, almacenada a 25 °C **(ILUSTRATIVO)**:

```
Sistema                          d50      PDI    ζ (mV)   Aspecto a 3 meses     CBD en solución a 6 m
Emulsión de alta cizalla         4,2 µm   0,52    −18      Anillo de aceite         62 % del declarado
Nanoemulsión (microfluidizador)   68 nm   0,14    −41      Transparente, sin cambio  97 % del declarado

CBD cuantificado por HPLC-UV 228 nm sobre el líquido, tras descartar el anillo superficial
```

La lectura comercial es dura: la bebida gruesa "tenía" 10 mg de CBD el día que se hizo, pero al tercer mes
buena parte del activo está en un anillo pegado al cuello de la botella y el consumidor no se lo toma.
Legalmente, el contenido declarado debe cumplirse **durante toda la vida útil**, no solo el día 0 (`164`,
`272`). Este es el argumento técnico para invertir en el equipo de nanoemulsión, y el argumento se sostiene
con d50, PDI, ζ y HPLC — no con una foto de la botella.

## Errores comunes

- Evaluar estabilidad "a ojo" a los 15 días. Se necesita estudio de estabilidad con métrica y método.
- Reportar d50 sin PDI ni método de medida. DLS y difracción láser no dan el mismo número.
- Añadir sales o ácidos a una emulsión estabilizada electrostáticamente y no reevaluar el potencial zeta.
- Agitar más fuerte creyendo que eso estabiliza. La energía baja el tamaño, pero sin tensioactivo adecuado
  las gotas coalescen apenas para el equipo (`33`).
- Declarar el contenido de activo medido el día de fabricación como si fuera el de toda la vida útil.
- Ignorar la espuma en planta: arrastra producto, ensucia sensores y hace que el llenado sea inexacto.
- Confundir "transparente" con "disuelto". Una nanoemulsión es transparente y **sigue siendo** una
  dispersión de gotas (`157`).

## Conexión con otros módulos

→ `33-tensioactivos-y-hlb.md` — quién estabiliza la interfase y cómo se elige.
→ `34-reologia-y-viscosidad.md` — la viscosidad como freno del cremado.
→ `157-emulsiones-y-nanoemulsiones.md` — el módulo dueño de la formulación.
→ `25-termodinamica-quimica.md` — por qué una emulsión nunca es estable de verdad.
→ `164-estabilidad-ich-q1-y-vida-util.md` — cómo se demuestra la vida útil.
→ `219-beta-glucanos-quimica-y-estructura.md` — el β-glucano como coloide en solución.
→ `163-envase-primario-y-compatibilidad.md` — el activo que se pega al envase.
