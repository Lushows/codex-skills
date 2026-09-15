# 211 — Hemp y CBD en Estados Unidos a 2026 (el cambio de definición que borra una industria)

Entre 2018 y 2025, la industria del hemp en EE.UU. vivió de una sola línea legal: hemp es cannabis con **no
más de 0,3 % de Δ9-THC en base seca**. Esa línea permitió un mercado entero de productos con THCA, Δ8-THC,
HHC y bebidas de THC "de cáñamo", porque el texto solo hablaba de **Δ9** y solo hablaba de **porcentaje sobre
planta**. En noviembre de 2025 el Congreso cerró ambos huecos de un golpe. Este módulo explica exactamente
qué cambió, cuándo entra en vigor, y en qué estado está el aplazamiento a agosto de 2026.

Términos: **hemp (cáñamo)** = cannabis por debajo del umbral legal de THC en EE.UU. **Base seca (dry weight
basis)** = referida a la masa del material sin agua. **THC total (total THC)** = Δ9-THC + 0,877 × THCA.
**Por envase (per container)** = referido al contenido total del empaque, no a la porción.

## La definición vieja y la nueva, lado a lado

| | Definición 2018 (Agriculture Improvement Act, "Farm Bill") | Definición nueva (Sección 781, P.L. 119-37) |
|---|---|---|
| Norma | 7 U.S.C. §1639o | Continuing Appropriations and Extensions Act, 2026 |
| Analito | **Solo Δ9-THC** | **THC total**, incluidos THCA y cannabinoides intoxicantes similares (Δ8-THC entre ellos) |
| Base | 0,3 % **en base seca**, sobre la planta o el material | **0,4 mg por envase** en el producto final de consumo |
| Qué mide | Concentración | **Masa absoluta por empaque** |
| Efecto práctico | Permite flor de THCA y productos de Δ8 | Los cierra a nivel federal |

El punto conceptual que hay que entender bien: **cambió la unidad de medida, no solo el número**. Pasar de
"porcentaje sobre planta" a "miligramos por envase" no es un ajuste de rigor, es otra pregunta. Un producto
puede cumplir 0,3 % p/p y estar 100 veces por encima de 0,4 mg/envase, simplemente porque el envase es
grande.

```
Ejemplo de la trampa de base:
  Aceite de 30 mL, densidad 0,92 g/mL → masa neta 27,6 g
  THC total = 0,10 % p/p = 1,0 mg/g
  Cumple holgadamente "menos de 0,3 %"
  THC total por envase = 1,0 mg/g × 27,6 g = 27,6 mg
  Excede 0,4 mg/envase por un factor de 69
```

Ejecuta siempre esta conversión con `lab-tools/thc_total.py` o `Matematicas_lushows`; es exactamente donde un
error de unidades se convierte en un producto ilegal.

La estimación que circula entre abogados del sector es que **alrededor del 95 % de los productos de extracto
de hemp hoy en el mercado**, incluidos muchos productos de CBD de espectro completo no intoxicantes,
superarían el umbral de 0,4 mg por envase.

## Fechas: qué pasó, qué viene, y dónde está el aplazamiento

Cronología verificable a agosto de 2026:

| Fecha | Hecho |
|---|---|
| Noviembre de 2025 | El Congreso aprueba las restricciones dentro de la ley de financiación del gobierno (P.L. 119-37, Sección 781), con un período de implementación de 365 días |
| **12 de noviembre de 2026** | Fecha en la que la nueva definición entra en vigor si nada la cambia |
| Primer semestre de 2026 | Se presentan en el Congreso varios proyectos para derogar, aplazar o reemplazar la disposición; ninguno prospera |
| 3 de agosto de 2026 | El Senado avanza una medida para aplazar la prohibición |
| **8 de agosto de 2026** | El Senado aprueba un proyecto bipartidista de financiación que **aplaza la prohibición hasta el 11 de diciembre de 2026**, y rechaza 61-32 la enmienda que buscaba eliminar ese aplazamiento |
| Estado a mediados de agosto de 2026 | **El proyecto pasa a la Cámara de Representantes**, que debe votarlo al regresar del receso de agosto; falta también la firma presidencial. Hasta que eso ocurra, la fecha vigente sigue siendo el 12 de noviembre de 2026 |

Fuentes: Congressional Research Service (producto IN12620, sobre el cambio de definición de hemp); cobertura
de *Forbes*, *Marijuana Moment* y MPR News del 3 al 10 de agosto de 2026.

**Cómo verificar el estado vigente**, que es lo que de verdad te sirve dentro de tres meses:
- congress.gov, buscando la ley de financiación en curso y las enmiendas sobre hemp.
- El texto de la Sección 781 de P.L. 119-37 y sus modificaciones.
- Los productos del Congressional Research Service, que se actualizan.

No tomes ninguna decisión de inventario o de formulación sin confirmar la fecha vigente el día que decides.

## Lo que no cambió (y que la gente olvida)

- **El CBD sigue sin ser un ingrediente alimentario aprobado por la FDA.** La posición de la FDA es que el
  CBD está excluido de la definición de suplemento dietario por la "drug exclusion rule", porque fue
  investigado y aprobado como fármaco (Epidiolex). La FDA ha dicho públicamente que se necesita una vía
  regulatoria nueva del Congreso. Verifica en fda.gov la postura vigente.
- **Los estados regulan por encima de la línea federal.** Varios estados ya prohibieron o restringieron los
  productos intoxicantes de hemp antes que el Congreso; otros crearon marcos con límites por porción y por
  envase, edad mínima y ensayos obligatorios. La ley federal es el piso, no el techo.
- **El cannabis "de marihuana" sigue siendo Lista I federal**, con mercados estatales legales que operan en
  tensión con esa clasificación. Los procesos de reprogramación han sido lentos; verifica el estado en
  dea.gov y en las noticias regulatorias.
- **cGMP 21 CFR Part 111** aplica a suplementos dietarios; **21 CFR Part 117** (Preventive Controls) a
  alimentos. Nada de eso desapareció (ver `274`).

## Qué exige esto del laboratorio

Si tu límite pasa a ser 0,4 mg por envase, tu método analítico tiene que poder demostrarlo:

1. **Reportar THC total, no Δ9-THC.** Con el factor 0,877 sobre el THCA (ver `175`).
2. **Reportar en mg por envase**, además de en % p/p. Eso exige conocer la masa neta o el volumen y la
   densidad del producto.
3. **Tener LOQ suficientemente bajo.** Para un envase de 27,6 g, 0,4 mg equivale a 14,5 µg/g. Un HPLC-DAD de
   rutina no llega ahí con confianza; hace falta **LC-MS/MS** (ver `83`, `194`).
4. **Incluir "cannabinoides intoxicantes similares"** en el panel: Δ8-THC, Δ10-THC, HHC, THCO, THCP y lo que
   la reglamentación defina. El alcance exacto de esa frase es una de las incertidumbres del texto y será
   materia de reglamentación (ver `181`).
5. **Acreditación ISO/IEC 17025** con el alcance correspondiente (ver `107`).

## Ejemplo aplicado (ILUSTRATIVO)

Marca con tres productos, evaluados contra 0,4 mg de THC total por envase:

| Producto | Masa neta | THC total medido | mg por envase | ¿Cumple? |
|---|---|---|---|---|
| Aislado de CBD, 1 g | 1,0 g | < 0,003 % p/p (LC-MS/MS) | < 0,03 mg | Sí |
| Aceite espectro amplio 30 mL | 27,6 g | 0,0010 % p/p | 0,28 mg | Sí, con poco margen |
| Aceite espectro completo 30 mL | 27,6 g | 0,090 % p/p | 24,8 mg | No |
| Gomitas, 30 unidades | 90 g | 0,015 % p/p | 13,5 mg | No |

Cifras **(ILUSTRATIVO)**. Lecturas prácticas: (1) el aislado sobrevive sin problema; (2) el espectro amplio
sobrevive **si** la remediación es agresiva y el laboratorio tiene el LOQ para probarlo; (3) el espectro
completo, que es el producto emblema de la industria, no sobrevive. (4) Los envases múltiples son los más
castigados, porque el límite es por envase, no por unidad: **treinta gomitas de 0,45 mg cada una suman
13,5 mg y reprueban**, aunque cada gomita individual esté por debajo.

Esa última consecuencia es la que más va a cambiar el diseño de empaque: envases más pequeños, unidades
sueltas, y reformulación hacia espectro amplio o aislado.

## Errores comunes

- **Seguir midiendo solo Δ9-THC.** La definición nueva cuenta THCA y otros. Un COA viejo no sirve para
  demostrar cumplimiento nuevo.
- **Confundir porcentaje con masa por envase.** Es el error de fondo y es puramente de unidades.
- **Asumir que el aplazamiento ya es ley.** A agosto de 2026 el Senado lo aprobó; falta la Cámara y la firma.
- **Creer que la ley federal basta.** Los estados pueden ser más restrictivos y muchos lo son.
- **Certificar con un método incapaz.** HPLC-DAD no puede sostener un límite de µg/g.
- **Fabricar inventario con la fecha vieja en la cabeza.** Un lote con vida útil de 24 meses fabricado hoy
  puede quedar invendible a mitad de su vida.

## Conexión con otros módulos

→ `175-thc-total-y-el-factor-0877.md` — la aritmética que ahora define legalidad.
→ `194-remediacion-de-thc.md` — cómo se llega a cumplir 0,4 mg/envase.
→ `181-hhc-thco-y-semisinteticos.md` — los "cannabinoides intoxicantes similares".
→ `273-fda-dshea-y-suplementos.md` — por qué el CBD sigue fuera de la categoría de suplemento.
→ `274-cgmp-21-cfr-111.md` — el marco de manufactura que no cambió.
→ `212-cannabis-y-cbd-en-europa.md` — el contraste con el enfoque europeo.
