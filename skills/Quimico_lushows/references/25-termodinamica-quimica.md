# 25 — Termodinámica química (qué puede pasar, cuánto cuesta y por qué a veces no pasa igual)

La termodinámica responde una sola pregunta, pero es la más cara del negocio: **¿esto puede ocurrir por sí
solo, y hasta dónde?** Te dice si un solvente va a disolver tu activo, cuánta energía cuesta evaporar 100 L
de etanol, por qué el CO₂ supercrítico tiene ese comportamiento raro, y por qué una reacción "que debería
ir" no va. No te dice cuánto se demora —eso es cinética (`26`)— y confundir las dos cosas es el error
conceptual que hace que la gente caliente más en vez de cambiar la condición.

Términos: **entalpía (enthalpy, ΔH)** = calor intercambiado a presión constante, en kJ/mol; negativo =
libera calor. **entropía (entropy, ΔS)** = medida del desorden o de las formas de repartir energía, en
J/(mol·K). **energía libre de Gibbs (Gibbs free energy, ΔG)** = ΔH − T·ΔS; negativo = el proceso es
espontáneo en esas condiciones. **estado estándar (standard state)** = referencia convenida (1 bar, 1 M,
25 °C) que se marca con °. **calor latente (latent heat)** = energía para cambiar de fase sin cambiar de
temperatura, en kJ/kg.

## Las tres ecuaciones que se usan de verdad

```
ΔG = ΔH − T·ΔS                    T en kelvin. ΔG < 0 → espontáneo en esas condiciones.
ΔG° = −R·T·ln K                   R = 8,314 J/(mol·K). Une termodinámica con equilibrio (`21`).
ΔG = ΔG° + R·T·ln Q               Q = cociente de reacción; explica por qué las condiciones mandan.

Energía para calentar y evaporar:
  Q_sensible = m · cp · ΔT        cp agua ≈ 4,18 kJ/(kg·K); cp etanol ≈ 2,44 kJ/(kg·K)
  Q_latente  = m · ΔHvap          ΔHvap agua ≈ 2 260 kJ/kg; etanol ≈ 841 kJ/kg (a 1 atm)
```

Esa última línea es la que convierte termodinámica en factura de gas: **evaporar agua cuesta 2,7 veces más
energía por kilo que evaporar etanol**. Ahí está la mitad del argumento económico de una extracción
hidroalcohólica frente a una acuosa cuando hay que concentrar (`149`).

## Espontáneo no significa rápido, ni bueno

| Proceso | ΔH | ΔS | ¿Espontáneo? | Lectura práctica |
|---|---|---|---|---|
| Disolución de sal en agua | ligeramente + | ++ | Sí, la entropía manda | Se enfría el vaso y aun así se disuelve |
| Disolución de β-glucano en agua fría | + | + pequeño | Marginal | Por eso hace falta calor: no es solo cinética (`19`) |
| Oxidación de THC a CBN | −− | ~0 | Sí, muy | Es inevitable; solo se puede frenar (cinética) (`204`) |
| Descarboxilación de THCA | + moderado | ++ (se libera CO₂ gas) | Sí, a T alta | La entropía del gas empuja la reacción (`174`) |
| Evaporación de etanol a 78 °C | + | ++ | Sí en el punto de ebullición | Todo el calor va a ΔHvap (`29`) |
| Precipitación de β-glucano con etanol | − | − | Sí, la entalpía manda | Base de la precipitación etanólica (`19`) |
| Emulsión aceite/agua | ~0 | −− (se ordena la interfase) | **No** | Por eso hace falta tensioactivo y energía (`32`, `33`) |

La última fila es clave para formulación: una nanoemulsión de CBD **nunca** es termodinámicamente estable;
es cinéticamente estable, que es otra cosa y tiene fecha de vencimiento (`157`).

## Entalpía de vaporización: la tabla de la factura

| Sustancia | Punto de ebullición a 1 atm (°C) | ΔHvap aproximado (kJ/kg) | Dónde te pega |
|---|---|---|---|
| Agua | 100 | 2 260 | Concentrar decocciones de hongos (`144`, `149`) |
| Etanol | 78,4 | 841 | Recuperación de solvente en tinturas (`145`) |
| Metanol | 64,7 | 1 100 | Solo uso analítico (`87`) |
| Acetato de etilo | 77,1 | 366 | Partición y fracciones (`30`) |
| n-Heptano | 98,4 | 317 | Winterización y lavados (`191`) |
| CO₂ | −78,5 (sublima) | — (supercrítico > 31,1 °C y 73,8 bar) | Extracción supercrítica (`148`) |

Con esos números y `Matematicas_lushows` calculas el costo energético real de tu paso de concentración,
que suele ser el segundo costo variable después de la biomasa (rutea a `economist_lushows` para el efecto
en margen).

## El punto crítico y por qué el CO₂ supercrítico existe

Por encima de su **temperatura y presión críticas** una sustancia deja de tener fases líquida y gaseosa
distintas: es un **fluido supercrítico**, con densidad parecida a un líquido (disuelve) y viscosidad y
difusividad parecidas a un gas (penetra la matriz rápido). Para el CO₂ eso ocurre a 31,1 °C y 73,8 bar,
condiciones alcanzables con equipo comercial. La gracia termodinámica: cambiando presión y temperatura
cambias la **densidad**, y con ella el poder solvente — es un solvente "sintonizable". Al despresurizar,
el CO₂ se va como gas y no queda residuo (`148`, `189`, `87`).

## Cómo se mide

| Propiedad | Método | Unidad |
|---|---|---|
| ΔH de una transición (fusión, deshidratación) | DSC (calorimetría diferencial de barrido) | J/g o kJ/mol (`99`) |
| Pérdida de masa por temperatura | TGA (termogravimetría) | % de masa vs °C (`99`) |
| Solubilidad y su ΔH de disolución | Shake-flask a varias T + van't Hoff (ln S vs 1/T) | mg/mL; pendiente → ΔH |
| Calor de reacción | Calorimetría de reacción o DSC en cápsula sellada | kJ/mol |
| Consumo energético real del proceso | Medidor de gas/electricidad del equipo por lote | kWh o m³ de gas por kg de extracto |
| Constante de equilibrio K | Cuantificar las especies en el equilibrio por HPLC | Adimensional; ΔG° = −RT·ln K (`21`) |

Regla dura: la energía teórica del cálculo y la factura real difieren por la **eficiencia del equipo**
(pérdidas, reflujo, aislamiento). Se usa el cálculo para decidir la ruta y el medidor para presupuestar.

## Ejemplo aplicado — concentrar decocción de reishi: ¿evaporador o liofilizador?

Lote de 100 L de decocción acuosa con 2,5 % de sólidos, se quiere polvo seco **(ILUSTRATIVO)**:

```
Ruta A — evaporación al vacío a 50 °C hasta 10 L + secado por aspersión
  Agua a evaporar: 90 kg
  Energía latente teórica: 90 kg × 2 260 kJ/kg = 203 400 kJ = 56,5 kWh
  Con eficiencia de 60 % del evaporador: ~94 kWh
  Aspersión de los 10 L restantes: ~30 kWh
  Total aproximado: 124 kWh · tiempo ~8 h

Ruta B — liofilización directa de los 100 L
  Congelación + sublimación de 97,5 kg de hielo (ΔHsub ≈ 2 830 kJ/kg) + vacío
  Energía teórica: ~276 000 kJ = 77 kWh, pero la eficiencia de un liofilizador es baja (20–30 %)
  Total aproximado: 260–380 kWh · tiempo 36–72 h
```

Conclusión defendible: la liofilización cuesta 2–3 veces más energía y 6 veces más tiempo, y solo se
justifica si el activo no aguanta 50 °C. Para β-glucano —polímero térmicamente robusto— no se justifica;
para un extracto con psilocibina en investigación o con enzimas activas, sí (`150`, `240`). La decisión es
termodinámica y económica a la vez, y los números finales se ejecutan en código, no de memoria.

## Errores comunes

- Confundir "espontáneo" con "rápido". El diamante debería ser grafito y ahí sigue (`26`).
- Creer que una emulsión bien hecha es estable para siempre. Es metaestable por diseño (`32`, `157`).
- Calcular energía de evaporación sin incluir el calor sensible ni la eficiencia del equipo.
- Elegir liofilización "porque es premium" sin datos de termolabilidad del activo. Es una decisión de
  200 kWh por lote, no de marketing (`150`).
- Escribir ΔG de una reacción sin decir a qué temperatura y en qué condiciones. ΔG depende de Q (`21`).
- Usar ΔH negativo como prueba de que la reacción "va". Sin ΔS y sin T no se concluye nada.

## Conexión con otros módulos

→ `21-equilibrio-quimico.md` — K sale directamente de ΔG°.
→ `26-cinetica-de-reaccion.md` — cuánto se demora lo que la termodinámica permite.
→ `28-gases-y-presion-de-vapor.md` — presión de vapor y ebullición, con Clausius-Clapeyron.
→ `29-destilacion-y-equilibrio-liquido-vapor.md` — la aplicación industrial de todo esto.
→ `99-analisis-termico-dsc-y-tga.md` — cómo se miden ΔH y las transiciones.
→ `149-concentracion-y-evaporacion.md` — el paso de planta que consume la energía.
→ `148-co2-supercritico.md` — el fluido supercrítico en detalle.
