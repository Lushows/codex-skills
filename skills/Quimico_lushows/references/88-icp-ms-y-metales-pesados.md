# 88 — ICP-MS y metales pesados: el análisis que un producto de hongos no puede saltarse

Los hongos son **hiperacumuladores**: absorben del sustrato metales que la planta promedio no absorbe, y los
concentran en el cuerpo fructífero. Eso, que en biorremediación es una virtud, en un suplemento es un
riesgo. Si vendes reishi, melena de león, chaga o cualquier hongo —y con más razón si el sustrato tiene
historia agrícola o industrial— el análisis de metales pesados no es opcional: es la prueba que sostiene que
tu producto es seguro. La técnica de referencia es ICP-MS, y este módulo te da lo que necesitas para
contratarla y auditarla.

Términos:
- **ICP-MS (inductively coupled plasma mass spectrometry)** = plasma de argón a ~6.000–10.000 K que atomiza e
  ioniza la muestra; luego un espectrómetro de masas cuenta los iones atómicos.
- **ICP-OES / ICP-AES (optical emission)** = misma antorcha, pero mide luz emitida. Más barata, menos
  sensible.
- **Digestión (digestion)** = destruir la matriz orgánica con ácido para dejar los metales en solución.
- **Interferencia poliatómica (polyatomic interference)** = un ion molecular con el mismo m/z que el metal
  (p. ej. ⁴⁰Ar³⁵Cl⁺ interfiere ⁷⁵As).
- **Celda de colisión/reacción (collision/reaction cell, CRC/KED)** = accesorio que elimina esas
  interferencias.
- **Los cuatro grandes (the big four)** = cadmio (Cd), plomo (Pb), arsénico (As) y mercurio (Hg).

## Por qué los hongos son un caso aparte

El micelio se comporta como una red de absorción: tiene alta relación superficie/volumen y transportadores
que no discriminan bien entre metales esenciales y tóxicos. Resultado documentado en la literatura de
micología: **los hongos concentran cadmio y mercurio en el cuerpo fructífero por encima de la concentración
del sustrato**, con factores de bioconcentración que pueden superar 10 (`243`).

Consecuencias prácticas: **el sustrato manda** (grano de origen desconocido, aserrín de árbol crecido junto a
una vía, paja de un cultivo tratado — todo eso llega a la seta, `239`); **los silvestres son más riesgosos
que los cultivados** (la chaga es el caso clásico, `230`); **concentrar el extracto concentra el metal** (un
10:1 puede llevar ~10 veces el cadmio de la materia prima; el ratio de masa no protege, `151`, `242`); y **un
COA de materia prima no cubre el producto terminado**, que es lo que se mide.

## Límites vigentes (a agosto de 2026 — verificar antes de usar)

| Marco | Aplicación | Cd | Pb | As | Hg |
|---|---|---|---|---|---|
| **USP <232> / ICH Q3D**, vía oral | PDE en µg/día | 5 | 5 | 15 (inorgánico) | 30 (inorgánico) |
| **UE Reg. 2023/915** (contaminantes en alimentos), setas cultivadas | mg/kg peso fresco | 0,050 general; 0,15 *Pleurotus ostreatus* y *Lentinula edodes*; 0,5 *Agaricus bisporus* | 0,30 (A. bisporus, P. ostreatus, L. edodes) | — | — |
| **Colombia** | Res. de INVIMA aplicable al tipo de producto (suplemento dietario, fitoterapéutico, alimento) | Verificar la norma vigente por categoría | | | |

Dos advertencias que evitan errores caros:

```
1. USP <232> se expresa en ug/DIA (exposicion), no en mg/kg (concentracion).
   Para convertir necesitas la dosis diaria maxima:
       Limite (ug/g) = PDE (ug/dia) / dosis diaria (g/dia)
   Ejemplo (ILUSTRATIVO): capsulas de reishi, dosis 2 g/dia.
       Cd: 5 ug/dia / 2 g/dia = 2,5 ug/g = 2,5 mg/kg ; Pb: 5/2 = 2,5 mg/kg
   Si la dosis sube a 6 g/dia, el limite baja a 0,83 mg/kg. La dosis que
   pongas en la etiqueta CAMBIA tu especificacion. Rutea el calculo a
   Matematicas_lushows y dejalo escrito en el expediente (282, 286).

2. La UE se expresa en PESO FRESCO para setas. Un COA en base seca no se
   compara directo: hay que corregir por humedad (07). Un hongo fresco con
   90 % de humedad concentra ~10x al secarse.
```

## El método completo, paso a paso

```
1. HOMOGENEIZACION (67): moler todo el lote compuesto, no una seta. La
   variabilidad entre ejemplares domina el resultado (66).

2. DIGESTION POR MICROONDAS (microwave-assisted acid digestion)
   0,25-0,5 g de muestra seca + 5-8 mL HNO3 concentrado (grado trazas)
   + 1-2 mL H2O2 (a veces + HCl para As y Hg, o HF para silicatos).
   Vaso cerrado de PTFE/TFM. Rampa a 180-200 C, 15-20 min de meseta,
   presion 30-60 bar. Enfriar, aforar a 25-50 mL con agua ultrapura.

   POR QUE MICROONDAS Y NO PLANCHA ABIERTA: el vaso cerrado evita la PERDIDA
   DE MERCURIO Y ARSENICO por volatilizacion (una plancha abierta te da un
   "cumple" falso), reduce la contaminacion desde el ambiente y digiere
   completo matrices ricas en quitina y lipidos.
   Metodos de referencia: USP <233>, EPA 3052, AOAC 2015.01.

3. MEDICION POR ICP-MS
   Isotopos tipicos: 111Cd o 114Cd | 208Pb | 75As | 202Hg
   Estandar interno: 103Rh, 115In, 209Bi, 45Sc (corrige deriva y matriz)
   Celda de colision (He, KED) para 75As: elimina la interferencia de
     40Ar35Cl+ que viene del cloro de la matriz. SIN CELDA, EL ARSENICO SALE
     INFLADO. Es el error clasico.
   Para Hg: oro (Au) o HCl en el diluyente, porque se pega a las paredes y
     genera arrastre entre muestras (carryover).

4. CONTROL DE CALIDAD (77)
   Blanco de digestion (los reactivos aportan plomo), CRM de matriz vegetal
   o fungica, spike de recuperacion 80-120 %, duplicado.
```

## ICP-MS vs las alternativas

| Técnica | LOD típico | Multi-elemento | Costo por muestra (ILUSTRATIVO) | Cuándo |
|---|---|---|---|---|
| **ICP-MS** | 0,001–0,01 mg/kg | Sí, 20–60 elementos a la vez | COP 200.000–600.000 | El estándar. Lo que debes pedir |
| **ICP-OES** | 0,05–0,5 mg/kg | Sí | COP 150.000–400.000 | Aceptable si el LOD alcanza tu límite; suele NO alcanzar para Cd y Pb a niveles bajos |
| **AAS horno de grafito (GFAAS)** | 0,005–0,05 mg/kg | No, uno por uno | COP 80.000–200.000 **por elemento** | Laboratorios pequeños; ver `89` |
| **Vapor frío / hidruros** | Muy bajo para Hg y As | No | Similar | Específico para Hg y As |
| **Analizador directo de Hg (DMA)** | 0,001 mg/kg | No | COP 100.000–250.000 | Mercurio sin digestión |

## Especiación: la diferencia entre alarma y problema real

No todos los átomos del mismo elemento son igual de tóxicos:

| Elemento | Forma tóxica | Forma poco tóxica | Cómo se separa |
|---|---|---|---|
| Arsénico | As(III) y As(V) **inorgánicos** | Arsenobetaína (orgánico, en marinos) | **HPLC-ICP-MS** (especiación) |
| Mercurio | Metilmercurio | Hg inorgánico (menos tóxico por vía oral) | HPLC-ICP-MS o GC-ICP-MS |
| Cromo | Cr(VI) | Cr(III), esencial | Cromatografía iónica-ICP-MS |

USP <232> e ICH Q3D limitan **arsénico y mercurio inorgánicos**, y permiten usar el total como enfoque
conservador: si el total cumple, no hace falta especiar. Solo cuando el total falla vale la pena pagar
especiación (ILUSTRATIVO: COP 600.000–1.500.000 por muestra) para demostrar que la fracción tóxica es menor.
Es la carta que te puede salvar un lote.

## Ejemplo aplicado — reishi cultivado en sustrato de aserrín

```
Producto: capsulas de extracto de Ganoderma lucidum, dosis declarada 2 g/dia.
Especificacion derivada de USP <232> (ILUSTRATIVO):
    Cd <= 2,5 mg/kg | Pb <= 2,5 mg/kg | As <= 7,5 mg/kg | Hg <= 15 mg/kg
(Y adicionalmente, si se exporta a la UE como alimento, la tabla de 2023/915
 en peso fresco para setas, corregida por humedad — 07.)

Resultados del lote (ICP-MS, digestion por microondas) (ILUSTRATIVO):
    Cd 1,8 mg/kg base seca -> cumple, pero AL 72 % del limite
    Pb 0,42 | As 0,31 | Hg 0,08 mg/kg -> cumplen holgado

Lectura correcta: el Cd al 72 % del limite NO es tranquilizador. Con la
incertidumbre tipica (U ~ 20-30 %, k=2 — ver 76), el intervalo llega a
2,3 mg/kg. Un lote de sustrato peor te saca de especificacion.

Accion: exigir COA de metales AL SUSTRATO y al grano (141, 239, 284), no
solo al producto terminado, y monitorear el Cd lote a lote con carta de
control (77). Cambiar de proveedor de aserrin sale mas barato que
descartar produccion.
```

## Qué preguntarle al laboratorio

1. ¿**ICP-MS o ICP-OES**? ¿Cuál es el **LOQ** de cada elemento en mi matriz?
2. ¿La digestión es **por microondas en vaso cerrado**? (Si es plancha abierta, el Hg no es confiable.)
3. ¿Usan **celda de colisión/reacción** para el arsénico?
4. ¿Corren **CRM de matriz vegetal/fúngica** y cuál fue su valor obtenido vs el certificado?
5. ¿Cuál fue la **recuperación del spike** y el resultado del **blanco de digestión**?
6. ¿El resultado va en **base seca o base húmeda**, y con qué humedad? (`07`, `98`)
7. ¿Pueden hacer **especiación de arsénico** si el total sale alto?

## Errores comunes

- **Medir solo el producto y nunca el sustrato.** El problema entra por el sustrato y se detecta tarde.
- **Comparar un límite de la UE (peso fresco) con un resultado en base seca.** Error de factor ~10.
- **Aplicar USP <232> sin fijar la dosis diaria.** Sin dosis no hay límite en mg/kg.
- **Aceptar arsénico alto sin pedir especiación** y descartar un lote que quizá cumplía.
- **Digestión abierta y reportar mercurio.** Pérdida garantizada, resultado falsamente bajo.
- **Olvidar el blanco.** Reactivos, viales y agua aportan plomo; sin blanco, tu producto "tiene" el del
  laboratorio.
- **Creer que "silvestre" significa limpio.** Es al revés: el silvestre no tiene sustrato controlado.

## Conexión con otros módulos

→ `36-quimica-inorganica-y-metales-relevantes.md` — la química de estos elementos.
→ `68-preparacion-de-muestra-solidos.md` — la digestión como preparación crítica.
→ `76-incertidumbre-de-medida.md` — por qué "cumple al 72 % del límite" merece atención.
→ `89-absorcion-atomica-y-alternativas.md` — cuándo la técnica más barata sirve y cuándo no.
→ `136-toxicidad-de-metales-pesados.md` — qué hacen estos metales en el cuerpo y de dónde salen los PDE.
→ `243-metales-pesados-en-hongos.md` — el caso fúngico completo: especies, sustratos y bioconcentración.
→ `202-metales-pesados-en-cannabis.md` — el equivalente en cannabis, que también acumula.
→ `282-especificacion-de-producto-terminado.md` — cómo se escribe el límite en tu especificación.
