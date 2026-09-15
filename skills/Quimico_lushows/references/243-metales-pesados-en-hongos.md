# 243 — Metales pesados en hongos (los hongos acumulan, y ese es el problema)

Los hongos son biorremediadores: absorben metales del sustrato con una eficiencia que los hace útiles para
limpiar suelos y peligrosos para comer si crecieron en el lugar equivocado. Cadmio y mercurio son los dos
que más se concentran en cuerpo fructífero (fruiting body), y el problema se multiplica en un extracto,
porque concentrar biomasa concentra también el metal. Si vendes suplementos de hongos y no tienes ICP-MS
en tu plan de control por lote, tienes un riesgo sanitario abierto.

Términos: **factor de bioconcentración (bioconcentration factor, BCF)** = concentración en el hongo dividida
por la del sustrato. **ICP-MS (inductively coupled plasma mass spectrometry)** = la técnica estándar para
metales traza. **digestión ácida (acid digestion)** = destruir la matriz con ácido nítrico y microondas
antes de medir. **base seca (dry basis)** = sin agua; los límites cambian mucho según la base.

## Por qué acumulan

La pared celular fúngica (quitina y glucanos) tiene grupos que quelan metales, y el micelio explora un
volumen de sustrato enorme por gramo de biomasa. Géneros como *Agaricus*, *Macrolepiota* y *Lepista*
acumulan cadmio y mercurio incluso en zonas no contaminadas (literatura de micología ambiental; verificar
con tu especie y tu sustrato). Los hongos cultivados sobre sustrato controlado (aserrín, paja, granos
auditados) son mucho más predecibles que los silvestres.

| Metal | Riesgo típico en hongos | Origen frecuente |
|---|---|---|
| Cadmio (Cd) | Alto — el que más problemas da | Suelo, fosfatos, sustrato agrícola |
| Mercurio (Hg) | Alto en silvestres | Deposición atmosférica, suelo |
| Plomo (Pb) | Medio | Suelo urbano, vías, pinturas viejas |
| Arsénico (As) | Medio, ojo con As inorgánico | Agua de riego, suelo |
| Cromo, níquel | Bajo/medio | Equipos, acero de proceso |

Ojo con el arsénico: lo que importa toxicológicamente es el **arsénico inorgánico**, no el total. Si tu
arsénico total sale alto, el paso siguiente es especiación por HPLC-ICP-MS, no rechazar el lote de una.

## Límites de referencia — a agosto de 2026

| Marco | Producto | Límite | Base |
|---|---|---|---|
| Unión Europea | Hongos cultivados (Agaricus, Pleurotus, Lentinula) | Pb 0,30 mg/kg | Peso fresco |
| Unión Europea | Hongos silvestres | Pb 0,80 mg/kg | Peso fresco |
| Unión Europea | Hongos (cadmio, según especie) | Cd 0,20–1,0 mg/kg | Peso fresco |
| USP / suplementos | Límites por exposición diaria (ICH Q3D adaptado) | Cd, Pb, As, Hg según dosis | Producto terminado |
| Colombia | Resoluciones de contaminantes del Minsalud + criterio INVIMA en el registro | Se define en el expediente | Producto terminado |

**Verificación obligatoria:** los límites europeos vigentes están en el Reglamento (UE) 2023/915 y sus
modificaciones; los de EE.UU. dependen de si el producto es alimento o suplemento y del enfoque de exposición
diaria; en Colombia se revisan en la normativa de contaminantes del Ministerio de Salud y en el expediente
de registro sanitario. **Consulta la fuente primaria antes de fijar tu especificación** — esta tabla es
orientación con fecha, no norma vigente certificada (`265`, `266`).

Trampa de base: un límite en peso fresco no se compara directo con un COA en base seca. Un hongo con 90 %
de agua concentra ~10× al secarse.

```
Conversión (ILUSTRATIVO):
  Cd = 0,15 mg/kg peso fresco, humedad 90 % → base seca = 0,15 / (1 − 0,90) = 1,50 mg/kg b.s.
  Ese mismo material, extraído a DER 10:1 con recuperación de metal del 60 %:
  Cd en extracto ≈ 1,50 × 10 × 0,60 = 9,0 mg/kg b.s.  → aquí es donde se rompe una especificación.
```

## Cómo se mide / cómo se comprueba

| Paso | Detalle |
|---|---|
| Muestreo | Compuesto y representativo del lote; los metales no se distribuyen uniformes (`66`) |
| Digestión | HNO₃ concentrado (± H₂O₂) en microondas cerrado, 180–200 °C |
| Medición | ICP-MS con estándar interno (Rh, In) y corrección de interferencias |
| Control | Material de referencia certificado (CRM) de matriz vegetal/fúngica en cada corrida |
| Reporte | mg/kg (= ppm) con la **base declarada** y el LOQ del método |
| Laboratorio | Acreditado ISO/IEC 17025 para ese alcance (`107`, `108`) |

LOQ típicos de ICP-MS en matriz de hongo: 0,005–0,05 mg/kg; suficiente para todos los límites de arriba.
Absorción atómica (`89`) sirve, pero con LOQ más altos y sin multi-elemento simultáneo.

## Ejemplo aplicado (ILUSTRATIVO) — decisión de lote

```
Lote GL-2026-014, extracto de reishi, DER 9:1
  Cd 1,80 mg/kg b.s.   Pb 0,42 mg/kg b.s.   As total 0,31 mg/kg b.s.   Hg 0,05 mg/kg b.s.
  Dosis diaria del producto: 2 cápsulas × 500 mg = 1,0 g/día

Exposición diaria a Cd = 1,80 mg/kg × 0,001 kg = 0,0018 mg/día = 1,8 µg/día
Comparar contra la ingesta tolerable de referencia del marco aplicable (EFSA fija una TWI para cadmio;
verificar el valor vigente en efsa.europa.eu). El cálculo se ejecuta, no se estima de memoria.
```

Decisión: el número por sí solo no aprueba ni rechaza. Se compara contra el límite de tu especificación
(`247`) y contra la contribución respecto a la ingesta tolerable, y se documenta.

## Errores comunes

- **Comprar hongo silvestre sin análisis.** Es la fuente #1 de cadmio y mercurio fuera de rango.
- **Analizar la materia prima y no el extracto.** El extracto concentra el metal; es el que va al cliente.
- **Comparar un resultado en base seca contra un límite en peso fresco.** Rechazas o apruebas lotes por error.
- **Pedir "metales pesados" sin especificar cuáles ni por qué método.** El COA vuelve con tres elementos y
  el que te iba a doler no estaba.
- **Aceptar "No detectado" sin LOQ.** "ND" sin límite de cuantificación no significa nada (`73`).
- **Ignorar el equipo y el agua de proceso.** Molinos, tanques y agua aportan níquel, cromo y plomo (`106`).

## Conexión con otros módulos

→ `88-icp-ms-y-metales-pesados.md` — la técnica en detalle.
→ `136-toxicidad-de-metales-pesados.md` — por qué importa toxicológicamente.
→ `135-noael-ida-y-limites-de-exposicion.md` — cómo se convierte un límite en decisión.
→ `230-chaga-riesgos-oxalato-y-radiocesio.md` — el caso especial del chaga.
→ `247-especificacion-de-producto-de-hongos.md` — dónde se fijan los límites de tu producto.
→ `284-auditoria-de-proveedor.md` — cómo se le exige esto al proveedor antes de comprar.
