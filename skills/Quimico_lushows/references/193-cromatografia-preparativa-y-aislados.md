# 193 — Cromatografía preparativa y aislados (cómo se llega a un CBD del 99 %)

Un destilado de cannabis llega a 80–90 % de cannabinoides totales, pero ahí siguen mezclados CBD, CBG, CBN,
THC y un fondo de material vegetal. Para vender un **aislado (isolate)** de 99 % o para quitarle el THC a un
extracto hay que **separar molécula por molécula**, y eso ya no lo hace la destilación: lo hace la
cromatografía a escala de producción o la cristalización. Este módulo te dice qué técnica sirve para qué,
qué rendimiento real esperar y cuánto cuesta el capricho de "quiero 99,9 %". El error caro clásico es pagar
por un equipo de cromatografía cuando el problema se resolvía cristalizando, o al revés: prometer
"broad spectrum sin THC" con un equipo que no puede alcanzar ese límite.

Términos: **cromatografía preparativa (preparative chromatography)** = separar para *recuperar* la sustancia,
no para medirla. **Fase estacionaria (stationary phase)** = el sólido que retiene. **Carga de columna
(loading)** = gramos de extracto por kilo de fase estacionaria. **CPC (centrifugal partition
chromatography)** = separación líquido-líquido sin sólido, por diferencia de reparto entre dos fases.
**Aislado (isolate)** = un solo cannabinoide, típicamente ≥ 98 % p/p.

## Las cuatro rutas reales a un aislado

| Ruta | Qué logra | Escala típica | Costo relativo | Cuándo tiene sentido |
|---|---|---|---|---|
| Cristalización de CBD | CBD 98–99,9 % p/p | kg a toneladas | Bajo | Materia prima rica en CBD (destilado ≥ 75 % CBD) |
| Cromatografía flash preparativa | Fracciones enriquecidas, 90–98 % | 100 g – 5 kg/lote | Medio | Cannabinoides menores, remediación de THC |
| CPC / partición centrífuga | Separaciones difíciles sin sílice | 100 g – 10 kg/lote | Medio-alto | CBD/CBC, CBD/THC, mezclas de isómeros |
| HPLC preparativa (prep-HPLC) | Pureza analítica, > 99 % | 1 g – 500 g/lote | Alto | Patrones de referencia, cannabinoides raros |

La regla económica: **cristaliza lo que puedas cristalizar y cromatografía solo lo que no**. El CBD es el
cannabinoide más fácil de cristalizar porque es sólido a temperatura ambiente y tiene un punto de fusión
reportado alrededor de 66 °C; el THC es un aceite viscoso que no cristaliza en la práctica industrial.

## Cristalización de CBD, paso a paso

1. Partes de un destilado con CBD alto (por ejemplo 80 % p/p de CBD, medido por HPLC-DAD, ver `198`).
2. Disuelves en un solvente donde el CBD sea poco soluble en frío (típicamente pentano, heptano o mezclas
   con etanol). Relación solvente:destilado según ensayo.
3. Enfrías de forma controlada. La velocidad de enfriamiento gobierna el tamaño de cristal: rápido da
   cristales finos y atrapa impurezas; lento da cristales grandes y más puros.
4. Filtras, lavas el pastel con solvente frío y secas al vacío hasta cumplir el límite de solventes
   residuales (ver `201`).
5. Puedes repetir (recristalización) para subir pureza a costa de rendimiento.

El **licor madre (mother liquor)** —el líquido que queda— concentra el THC y los cannabinoides menores.
Eso es una ventaja regulatoria (el aislado queda muy bajo en THC) y a la vez un residuo que hay que
controlar: es material fiscalizado si supera el umbral de THC de tu país (ver `210`, `211`).

## Cromatografía a escala: lo que de verdad decide el costo

```
Productividad (kg producto / día) =
    carga por ciclo (kg) × ciclos por día × rendimiento de la fracción

Costo por kg de producto ≈
    (solvente consumido × precio) + (fase estacionaria / vida útil en ciclos)
    + energía de evaporación + mano de obra + análisis de fracciones
```

El renglón que sorprende siempre es **la evaporación**: en cromatografía diluyes muchísimo y luego tienes
que quitar todo ese solvente. Si tu columna te entrega la fracción de interés a 5 g/L, para sacar 1 kg de
producto tienes que evaporar 200 L de solvente. Ese es el verdadero cuello de botella, no la columna.
Cualquier cuenta de productividad y costo por kilo debe ejecutarse en código, no de memoria —
rutea a `Matematicas_lushows` o usa `lab-tools/rendimiento_extraccion.py`.

## Fases estacionarias y por qué la sílice es traicionera

- **Sílice normal (normal phase silica)**: barata, alta capacidad, pero es ácida y puede **isomerizar
  cannabinoides**. El CBD sobre sílice ácida y con calor puede convertirse en Δ9-THC y Δ8-THC. Ese es el
  origen de más de un "aislado de CBD" que salió con THC en el COA (ver `180`).
- **Fase reversa C18 (reversed phase)**: separación excelente CBD/THC, pero cara y su regeneración consume
  mucho solvente acuoso-orgánico.
- **Alúmina y tierras activadas**: se usan más para decoloración que para separación fina.
- **CPC**: no hay sólido, entonces no hay adsorción irreversible ni isomerización por acidez superficial;
  el sistema de solventes se ajusta, y es reutilizable. Su curva de aprendizaje es más empinada.

## Cómo se mide / cómo se comprueba

Un aislado no se acepta por su aspecto (todos los aislados se ven como polvo blanco). Se acepta por
análisis:

| Ensayo | Técnica | Unidad | Criterio típico de un aislado de CBD |
|---|---|---|---|
| Pureza / potencia | HPLC-DAD contra patrón certificado | % p/p | ≥ 98,0 % CBD |
| Perfil de cannabinoides | HPLC-DAD, panel de 10–16 analitos | % p/p | THC total < LOQ o < límite legal del destino |
| Identidad | FTIR o punto de fusión + tiempo de retención | — | Coincide con patrón |
| Solventes residuales | GC-MS headspace o GC-FID | ppm (µg/g) | Según USP <467> clase del solvente |
| Metales pesados | ICP-MS | ppm o µg/kg | Según destino (ver `202`) |
| Pureza cromatográfica de pico | HPLC-DAD, pureza espectral | — | Pico sin coelución |

Ojo con la aritmética de la pureza: **el balance de masa debe cerrar**. Si el COA dice 99,5 % de CBD, ese
0,5 % restante tiene que estar declarado o al menos buscado (agua por Karl Fischer, cenizas, solventes,
otros cannabinoides). Un COA que da 99,9 % y no reporta nada más está afirmando algo que no midió (ver `111`).

## Ejemplo aplicado (ILUSTRATIVO)

Un procesador parte de 10,0 kg de destilado con 78,0 % p/p de CBD y 0,45 % p/p de THC total
(HPLC-DAD, base tal cual). Cristaliza en heptano y obtiene:

- Torta de cristal seca: 6,2 kg con 99,1 % p/p de CBD y THC total 0,03 % p/p.
- Licor madre concentrado: 3,5 kg con 32 % p/p de CBD y 1,1 % p/p de THC total.

Rendimiento de CBD recuperado en el aislado = (6,2 kg × 0,991) / (10,0 kg × 0,780) = 78,8 % del CBD que
entró. Todas estas cifras son **(ILUSTRATIVO)**: el rendimiento real depende del perfil de partida, del
solvente y de la curva de enfriamiento, y hay que determinarlo con tu propia materia prima.

Lo importante del ejemplo no es el número: es que el THC no desapareció, se **concentró en el licor madre**.
Ese subproducto pasa de 0,45 % a 1,1 % de THC total y cambia de categoría regulatoria. Si no lo planeaste,
acabas de crear un residuo fiscalizado que no puedes ni vender ni botar.

## Errores comunes

- **Creer que "99 %" es una sola cosa.** 99 % de pureza cromatográfica por área de pico no es 99 % p/p
  contra patrón certificado. Exige el método y el patrón (ver `70`).
- **Cromatografiar sobre sílice sin controlar acidez ni temperatura** y aparecer con Δ8-THC en el producto
  final. Es una conversión química, no una contaminación.
- **No presupuestar la evaporación.** El equipo de cromatografía se ve barato hasta que sumas el evaporador,
  el chiller y la recuperación de solvente.
- **Olvidar el destino del licor madre.** Ahí queda el THC. Su manejo es parte del diseño del proceso, no un
  problema del final del mes.
- **Comprar aislado por precio sin pedir COA de lote con solventes residuales.** El aislado barato suele
  serlo porque se secó poco: pentano o heptano por encima del límite USP.
- **Suponer que el aislado es estable para siempre.** El CBD aislado se oxida y amarillea con luz y oxígeno
  (ver `204`).

## Conexión con otros módulos

→ `192-destilacion-de-cannabinoides.md` — el paso anterior; sin buen destilado no hay cristalización decente.
→ `194-remediacion-de-thc.md` — cuando el objetivo no es aislar sino bajar el THC de un espectro amplio.
→ `180-delta8-delta10-e-isomerizacion.md` — por qué la sílice ácida te fabrica isómeros sin permiso.
→ `198-analisis-de-potencia-metodo.md` — el método con el que se comprueba la pureza.
→ `201-solventes-residuales-en-cannabis.md` — el ensayo que más reprueba a los aislados baratos.
→ `70-patrones-de-referencia-y-trazabilidad.md` — sin patrón certificado, "99 %" es una opinión.