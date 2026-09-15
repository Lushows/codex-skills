# 47 — Oxidación y degradación de productos naturales (THC→CBN, psilocina→azul)

Todo producto natural se está degradando desde el momento en que se cosecha. La pregunta no es "si", es "a
qué velocidad y hacia dónde". Dos ejemplos que cualquiera que venda estos productos ha visto: el THC se
oxida a **CBN** —por eso el cannabis viejo se siente distinto y por eso el CBN alto es la huella de un
material mal guardado— y la psilocina se oxida a compuestos azules —por eso los hongos psilocibios se ponen
azules donde se manipulan—. Entender la ruta de degradación te dice qué medir, qué envase usar, qué
declarar y qué NO prometer.

Términos: **autoxidación (autoxidation)** = oxidación en cadena por radicales, iniciada por O₂ y luz.
**Fotooxidación (photo-oxidation)** = la misma, disparada por luz UV/visible. **Quinona (quinone)** =
producto oxidado de un fenol; suele ser coloreado y reactivo. **Producto de degradación (degradant)** =
compuesto que aparece cuando el activo se descompone. **Marcador de envejecimiento (age marker)** =
degradante que sirve para estimar cuánto tiempo/maltrato lleva un material.

## Los cinco caminos de degradación

| Ruta | Disparador | Señal visible | Cómo se corta |
|---|---|---|---|
| Oxidación radicalaria | O₂ + calor + metales (Fe, Cu) | Color pardo, rancidez | Antioxidante + quelante + N₂ |
| Fotooxidación | Luz UV y azul | Decoloración, pérdida de activo | Envase ámbar/opaco, caja |
| Hidrólisis | Agua + pH extremo | Cambio de pH y olor | pH óptimo, secar (`46`) |
| Térmica (incluye descarboxilación) | Calor | Pérdida de forma ácida, aromas | Cadena de frío, secado suave |
| Enzimática | Enzimas propias del material | Pardeamiento rápido al cortar | Inactivación térmica, secado rápido |

## Caso 1 — THC → CBN: la reacción más rentable de entender

```
Δ9-THC  --[O₂, luz UV, calor, tiempo]-->  CBN (cannabinol)  + subproductos

Qué pasa químicamente: se AROMATIZA el anillo ciclohexeno (pierde 4 H, gana aromaticidad).
  Δ9-THC : C₂₁H₃₀O₂ , M = 314,47 g/mol
  CBN    : C₂₁H₂₆O₂ , M = 310,43 g/mol
El CBN es el producto TERMODINÁMICO final del deterioro oxidativo: aromático = muy estable, ya no vuelve.
```

Consecuencias operativas, todas medibles:

1. **CBN es el marcador de envejecimiento del cannabis.** En flor fresca y bien curada el CBN es muy bajo;
   sube con el tiempo, la luz y el aire. Un COA con CBN alto y THC bajo cuenta la historia del
   almacenamiento, aunque nadie te la cuente (`213`).
2. **La ruta se acelera con luz.** La literatura clásica (Fairbairn y col., años 70) identificó la luz como
   el factor más agresivo, por encima de la temperatura, para material almacenado. Envase opaco no es
   estética.
3. **El CBN tiene actividad propia** en CB1 con potencia reportada menor que la del Δ9-THC [in vitro]. Se
   comercializa como "cannabinoide del sueño": a agosto de 2026 esa afirmación **no tiene respaldo clínico
   sólido** y decirla en etiqueta es un riesgo regulatorio (`177`, `268`).
4. **Cuenta para el THC total?** No: el CBN es otra sustancia, con su propio pico. Pero si venías de THC, tu
   potencia declarada ya no es la real (`175`).

```
Ejemplo de lectura de un COA (ILUSTRATIVO):
  Lote A (fresco):   Δ9-THC 0,28 % | THCA 18,4 % | CBN 0,05 %   → ratio CBN/THC-total ≈ 0,003
  Lote B (18 meses): Δ9-THC 1,90 % | THCA  9,1 % | CBN 1,35 %   → ratio CBN/THC-total ≈ 0,13
  Mismo genético, misma cosecha. El lote B se descarboxiló Y se oxidó. El precio no debería ser el mismo.
```

## Caso 2 — Psilocibina → psilocina → azul

```
Paso 1 (defosforilación, `46`): psilocibina --fosfatasa / ácido + calor--> psilocina + fosfato
        C₁₂H₁₇N₂O₄P (284,25 g/mol)                          C₁₂H₁₆N₂O (204,27 g/mol)

Paso 2 (oxidación): psilocina --[lacasa/fenoloxidasa, O₂]--> radical → quinona-imina
        → acoplamiento oxidativo → OLIGÓMEROS AZULES (mezcla de dímeros/trímeros de psilocina)
```

Lo que hay que saber, sin ambigüedad:

- **El azul es psilocina oxidada, no psilocibina.** Es un indicador de manipulación y de pérdida, no de
  potencia. Un material muy azul ha perdido activo.
- La psilocibina, que es un **zwitterión** (carga + en el nitrógeno, − en el fosfato), es notablemente más
  estable que la psilocina, que es un **fenol libre** y por eso se oxida rápido. Por eso la naturaleza
  "guarda" el compuesto en su forma fosforilada.
- Para análisis y reporte honesto: se miden **psilocibina y psilocina por separado**, y se puede expresar la
  suma como psilocibina equivalente aplicando la razón de masas molares 284,25/204,27 = 1,3915 al valor de
  psilocina (verificar el cálculo en código, `Matematicas_lushows`).
- Los oligómeros azules **no se cuantifican de rutina**: no hay patrones certificados comerciales. Si
  aparecen, se reporta el balance de masa faltante, no se inventa un número (`256`).
- Este módulo describe química y estabilidad. No cubre producción ni cultivo (línea roja de la skill).

## Caso 3 — Fenoles de hongos y el pardeamiento

Los hongos frescos se oscurecen al cortarse por **polifenol oxidasa (PPO)** actuando sobre fenoles del tejido
(en *Agaricus*, derivados de tirosina). El producto son quinonas que polimerizan a melaninas. En chaga, el
pigmento negro es precisamente un complejo melanínico, y ahí sí es el atributo del producto (`56`, `229`).
Para materia prima destinada a extracto, el pardeamiento es pérdida: se corta con secado rápido a
temperatura controlada (`142`, `240`).

## Cómo se mide la degradación

| Qué | Método | Unidad | Lectura |
|---|---|---|---|
| Activo remanente | HPLC-DAD / LC-MS contra patrón | % p/p base seca | El dato duro |
| Degradantes | HPLC con barrido DAD + HRMS | % área y % p/p si hay patrón | CBN, psilocina, quinonas |
| Oxidación de lípidos | Índice de peróxidos / TBARS / *p*-anisidina | meq O₂/kg | Alarma temprana |
| Color | Colorimetría CIE L*a*b* | ΔE respecto a t=0 | Barato y sensible |
| Capacidad antioxidante remanente | DPPH, ABTS, ORAC | µmol Trolox eq/g | Solo comparativo (`133`) |
| Balance de masa | Suma de activo + degradantes | % | Si no cierra, falta una ruta |

Diseño mínimo de estudio de degradación forzada (ICH Q1A/Q1B, `164`): ácido, base, oxidante (H₂O₂ 3 %),
calor seco (60–80 °C), humedad y luz (cámara con lámpara según Q1B). Objetivo: 5–20 % de degradación, no
destruir la muestra. Con eso demuestras que tu método es **indicador de estabilidad (stability-indicating)**:
separa el activo de todos sus degradantes.

## Ejemplo aplicado — especificación de vida útil sin mentir

```
Producto (ILUSTRATIVO): aceite de espectro amplio, 25 mg/mL de CBD, frasco de vidrio ámbar 30 mL.
Especificación propuesta:
  CBD: 90,0–110,0 % del valor declarado durante la vida útil
  CBN: reportar (marcador de oxidación); Δ9-THC: ≤ límite legal aplicable a la fecha (`210`)
  Color ΔE ≤ 5 respecto al lote de referencia
Condiciones declaradas: "Conservar por debajo de 25 °C, protegido de la luz, bien cerrado."
Soporte: estabilidad acelerada 40 °C/75 % HR 6 meses + tiempo real 12 meses en curso (`165`).
Lo que NO se escribe: ninguna afirmación de que el producto trate, prevenga o cure algo (`268`).
```

## Errores comunes

- Vender "CBN para dormir" como si estuviera demostrado. A agosto de 2026 la evidencia clínica es escasa; es
  claim de riesgo (`177`, `276`).
- Usar el azul de un hongo como prueba de potencia. Es prueba de oxidación, o sea de pérdida.
- Hacer estabilidad midiendo solo el activo. Sin degradantes no hay historia ni método stability-indicating.
- Guardar extractos en frascos transparentes en una vitrina iluminada. Es el peor escenario posible.
- Congelar y descongelar repetidamente: cada ciclo condensa agua y mete oxígeno.
- Reportar "no detectado" para un degradante sin declarar el LOD del método. Ausencia de evidencia ≠ evidencia
  de ausencia (`73`).

## Conexión con otros módulos

→ `61-estabilidad-quimica-luz-calor-oxigeno.md` — el módulo dueño del envase y las condiciones.
→ `204-estabilidad-y-degradacion-del-thc.md` — el caso cannabis completo, con cinética.
→ `255-estabilidad-y-degradacion-de-psilocibina.md` — el caso psilocibios completo.
→ `62-maillard-y-pardeamiento.md` — la otra vía de oscurecimiento, la no oxidativa.
→ `133-estres-oxidativo-y-antioxidantes.md` — antioxidantes: cómo funcionan y qué se puede decir.
