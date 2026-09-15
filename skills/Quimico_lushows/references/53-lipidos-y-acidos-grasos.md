# 53 — Lípidos y ácidos grasos (el vehículo de tu producto y el primero en dañarse)

Los lípidos aparecen en tu operación de tres maneras: como componente de la materia prima (aceite de semilla
de cannabis, lípidos de la pared fúngica), como **vehículo** de la formulación (MCT, aceite de oliva,
girasol), y como el primer ingrediente que se pone rancio y arruina un lote. Además, la solubilidad de los
cannabinoides en grasa es la razón de que los comestibles funcionen distinto que las tinturas. Entender
lípidos te permite elegir el vehículo correcto, especificarlo con índices reales y diagnosticar un producto
que "sabe raro" antes de perder el inventario.

Términos: **ácido graso (fatty acid)** = cadena hidrocarbonada con -COOH al final. **Triglicérido
(triglyceride, TAG)** = glicerol + 3 ácidos grasos; es lo que llamamos aceite. **MCT (medium-chain
triglycerides)** = triglicéridos de cadena media, C8 y C10. **Insaturación (unsaturation)** = número de
dobles enlaces; más dobles enlaces = más fácil de oxidar. **Insaponificable (unsaponifiable)** = la fracción
del aceite que no es éster: esteroles, tocoferoles, hidrocarburos.

## Nomenclatura de ácidos grasos: cómo se leen los códigos

```
C18:2 n-6      →  18 carbonos, 2 dobles enlaces, el primero en el carbono 6 contando desde el metilo (ω)
                  = ácido linoleico
Notación Δ:    18:2 Δ9,12  →  dobles enlaces en C9 y C12 contando desde el CARBOXILO
Regla: n-x (u ω-x) cuenta desde el CH₃ final; Δx cuenta desde el COOH. No se mezclan.
```

| Ácido graso | Código | M (g/mol) | Punto de fusión (°C) | Dónde |
|---|---|---|---|---|
| Caprílico | C8:0 | 144,21 | ~16 | MCT |
| Cáprico | C10:0 | 172,26 | ~31 | MCT |
| Láurico | C12:0 | 200,32 | ~44 | Coco |
| Palmítico | C16:0 | 256,42 | ~63 | Casi todos |
| Esteárico | C18:0 | 284,48 | ~69 | Grasas sólidas |
| Oleico | C18:1 n-9 | 282,46 | ~13 | Oliva, girasol alto oleico |
| **Linoleico** | C18:2 n-6 | 280,45 | ~−5 | Semilla de cannabis (mayoritario) |
| **α-Linolénico** | C18:3 n-3 | 278,43 | ~−11 | Semilla de cannabis |
| γ-Linolénico | C18:3 n-6 | 278,43 | ~−11 | Semilla de cannabis (minoritario) |

**Aceite de semilla de cáñamo:** la literatura lo reporta con predominio de linoleico y α-linolénico, con
una relación n-6:n-3 comúnmente citada cerca de 3:1 (verificar con el análisis de tu lote). Ese perfil
altamente insaturado es exactamente lo que lo hace **muy susceptible a oxidación**: no sirve como vehículo
de larga vida útil sin antioxidante y envase adecuado (`47`, `61`).

## Elegir el vehículo: la tabla de decisión

| Vehículo | Insaturación | Estabilidad oxidativa | Sabor | Notas para formulación |
|---|---|---|---|---|
| **MCT (C8/C10)** | Saturado | **Alta** | Neutro | El estándar para tinturas de cannabinoides; baja viscosidad |
| Oliva extra virgen | Monoinsaturado | Media-alta | Fuerte | Aporta polifenoles propios; sabor puede tapar o chocar |
| Girasol alto oleico | Monoinsaturado | Alta | Neutro | Buena relación costo/estabilidad |
| Semilla de cáñamo | Poliinsaturado | **Baja** | Herbal | Bonito en marketing, difícil en vida útil |
| Aceite de coco | Saturado | Alta | Coco | Solidifica por debajo de ~24 °C |

Para cannabinoides, la solubilidad en el vehículo es alta en todos los aceites (son muy lipofílicos:
logP reportado por encima de 6). El criterio de decisión no es la solubilidad: es **estabilidad + sabor +
costo + lo que quieras contar en la etiqueta**.

## Los índices que se especifican (y qué significan)

| Índice | Qué mide | Unidad | Interpretación |
|---|---|---|---|
| Índice de acidez (AV) | Ácidos grasos libres | mg KOH/g | Sube con hidrólisis (`46`) |
| Índice de peróxidos (PV) | Hidroperóxidos (oxidación **primaria**) | meq O₂/kg | Alerta temprana; luego baja al degradarse |
| *p*-Anisidina (AnV) | Aldehídos (oxidación **secundaria**) | adimensional | Complementa PV |
| TOTOX = 2·PV + AnV | Oxidación total | adimensional | Vista completa del daño |
| Índice de yodo (IV) | Grado de insaturación | g I₂/100 g | Más alto = más insaturado = más lábil |
| Índice de saponificación | Tamaño medio de cadena | mg KOH/g | (`46`) |
| Insaponificable | Esteroles, ceras, tocoferoles | % p/p | Relevante para ergosterol (`55`) |

Una especificación de vehículo bien hecha (ILUSTRATIVO): *"MCT grado alimenticio, C8 ≥ 50 %, C10 ≥ 30 %,
AV ≤ 0,1 mg KOH/g, PV ≤ 1,0 meq O₂/kg, humedad ≤ 0,1 %, sin BHT añadido"* — cada línea es medible (`141`).

## Cómo se mide el perfil: FAME por GC

```
Los ácidos grasos NO se inyectan libres en GC: son polares y dan picos con cola.
Se convierten en METILÉSTERES (FAME, fatty acid methyl esters) por transesterificación (`46`, `64`).

Esquema (ILUSTRATIVO — usar el método oficial aplicable, p. ej. AOCS Ce 1h-05 / AOAC 996.06):
  1. Pesar el aceite (o extraer la grasa de la matriz)
  2. Transesterificar: metóxido de sodio en metanol, o BF₃/metanol, 60–70 °C
  3. Extraer los FAME con hexano
  4. GC-FID, columna polar de alta polaridad (cianopropil), 100 m para separar isómeros cis/trans
  5. Identificar por tiempo de retención contra una mezcla certificada de FAME (37 componentes)
  6. Cuantificar por normalización de áreas (% del total) o con estándar interno (C17:0 o C21:0)

Reporte típico: cada ácido graso como % del total de ácidos grasos, y g/100 g de producto si se conoce
la grasa total. Declarar la mezcla FAME usada como referencia.
```

## Lípidos en hongos y en cannabis: dos usos analíticos

- **Ergosterol**: es un lípido esterólico, marcador de biomasa fúngica. Va en el insaponificable, y requiere
  saponificación previa para liberarlo de sus ésteres (`46`, `238`).
- **Ceras y lípidos en extractos de cannabis**: son los que enturbian un extracto y se quitan por
  **winterización** (disolver en etanol frío y filtrar lo que precipita). Es un proceso lipídico, no
  cannabinoide (`191`).
- **Grasa total en la matriz** condiciona la preparación de muestra de pesticidas: matrices grasas exigen
  limpieza extra en QuEChERS o SPE, o los resultados salen mal (`69`, `102`).

## Ejemplo aplicado — por qué una tintura de cáñamo se puso rancia en 5 meses

```
Formulación (ILUSTRATIVO): 25 mg/mL de CBD en aceite de semilla de cáñamo, frasco ámbar 30 mL con gotero.
Hallazgo a 5 meses: olor a "pintura", sabor amargo, color más oscuro.
Datos medidos:
  PV a t=0: 1,2 meq O₂/kg   →  a 5 meses: 18,6 meq O₂/kg
  AnV a 5 meses: 12,4       →  TOTOX = 2(18,6) + 12,4 = 49,6
  CBD por HPLC: 24,1 mg/mL (dentro de 90–110 % del declarado) ← el activo casi no cambió
Diagnóstico: el problema no era el CBD, era el VEHÍCULO. Aceite muy insaturado + gotero que mete aire
  cada uso + almacenamiento a temperatura ambiente en clima cálido.
Acciones: cambiar a MCT (o girasol alto oleico), añadir tocoferoles mixtos, envase con menos cabeza de aire,
  reformular y repetir estabilidad acelerada (`164`, `165`). Verificar las cuentas en código.
```

## Errores comunes

- Elegir el vehículo por marketing ("aceite de cáñamo suena mejor") y pagarlo con devoluciones por rancidez.
- Medir solo el activo en estabilidad y no el vehículo. El cliente percibe primero el olor, no el mg.
- Reportar índice de peróxidos aislado en un aceite ya muy degradado: PV baja en la etapa tardía y da falsa
  tranquilidad. Por eso existe TOTOX.
- Inyectar ácidos grasos libres en GC y culpar a la columna.
- Olvidar el antioxidante o ponerlo sin quelante cuando hay trazas de hierro o cobre (`44`).
- No declarar el alérgeno cuando el vehículo lo es (soya, maní, sésamo) (`137`, `272`).

## Conexión con otros módulos

→ `46-hidrolisis-esterificacion-y-saponificacion.md` — FAME, saponificación e índices.
→ `47-oxidacion-y-degradacion-de-productos-naturales.md` — el mecanismo de la rancidez.
→ `55-esteroles-y-triterpenos.md` — el insaponificable y el ergosterol.
→ `191-winterizacion-y-desceramiento.md` — quitar ceras de un extracto.
→ `156-liquidos-goteros-y-jarabes.md` — el formato donde todo esto se decide.