# 153 — Formas farmacéuticas: panorama (elegir el formato antes de enamorarte de él)

La forma farmacéutica es el vehículo: cápsula, tableta, gotero, gomita, polvo, bebida, tópico. Casi todo el
mundo la elige por estética o por lo que hace la competencia, y esa es la razón por la que tantos proyectos
mueren en la maquila. La forma correcta se deduce de cuatro datos: **cuántos mg hay que meter**, **qué tan mal
sabe**, **qué tan estable es el activo** y **cuánto puedes invertir**. Este módulo te da la tabla de decisión
para no gastar seis meses en un formato que tu química no permite.

Términos: **forma farmacéutica (dosage form)** = presentación final del producto. **Carga de activo (drug
load)** = cuántos mg de activo caben por unidad. **Excipiente (excipient)** = todo lo que no es activo (`160`).
**Biodisponibilidad (bioavailability)** = fracción del activo que llega a circulación (`122`).

## La tabla de decisión

| Forma | Carga típica por unidad | Costo de entrada | Sabor | Estabilidad | ¿Pyme colombiana? |
|---|---|---|---|---|---|
| Cápsula dura (gelatina/HPMC) | 300–800 mg de polvo | **Bajo** | Se oculta | Buena | **Sí, la puerta de entrada** (`154`) |
| Tableta comprimida | 200–1200 mg | Alto (troqueles, tableteadora) | Malo si no se recubre | Buena | Maquila (`155`) |
| Polvo a granel (sobre/tarro) | 1–10 g | **Muy bajo** | Expuesto | Buena si hay barrera | **Sí** |
| Tintura / gotero | 20–80 mg/mL | **Bajo** | Alcohólico, fuerte | Buena (alcohol conserva) | **Sí** (`156`) |
| Aceite sublingual | 10–100 mg/mL | Bajo–medio | Aceitoso | Buena, oxidable | Sí (`195`) |
| Jarabe / bebible acuoso | 5–50 mg/mL | Medio | Se enmascara bien | **Frágil**: microbiología | Sí, con conservantes (`156`) |
| Gomita (gummy) | 5–50 mg | Alto (depositadora, moldes) | Excelente | Regular: humedad y migración | Maquila |
| Emulsión / nanoemulsión | 1–50 mg/mL | **Alto** (HPH/microfluidizador) | Neutro | Frágil (Ostwald) | Maquila (`157`) |
| Bebida lista para tomar | 5–30 mg/porción | Muy alto | Excelente | Compleja | Maquila |
| Tópico (crema, bálsamo) | 0,5–5 % p/p | Medio | N/A | Buena | Sí (`196`) |
| Sublingual sólido / film | 1–20 mg | Alto | Difícil | Buena | Maquila |

**Traducción para una pyme:** cápsula, polvo y tintura. Esos tres formatos cubren el 90 % de los casos de
hongos, se hacen con inversión baja y son fáciles de especificar. Todo lo demás es maquila.

## El filtro #1: ¿cuántos mg hay que meter?

Este cálculo mata más ideas de producto que ningún otro. Si tu porción diaria son 3 g de extracto, olvídate de
la gomita: no caben. Si son 20 mg, la cápsula queda medio vacía y necesitas diluyente.

```
CAPACIDAD APROXIMADA DE CÁPSULAS DURAS (volumen nominal, mL)
  tamaño 000  1,37    tamaño 00  0,91    tamaño 0  0,68
  tamaño 1    0,50    tamaño 2   0,37    tamaño 3  0,30

  masa que cabe (mg) ≈ volumen (mL) × densidad compactada del polvo (g/mL) × 1000

Ejemplo (ILUSTRATIVO): polvo de extracto con densidad compactada 0,62 g/mL
  cápsula 0:  0,68 × 0,62 × 1000 = 422 mg de polvo
  Si tu extracto es 32 % de β-glucano  →  135 mg de β-glucano por cápsula.
  Para llegar a 300 mg/día  →  2,2 cápsulas  →  redondea a 2 cápsulas y ajusta el objetivo,
  o sube el % del extracto, o usa cápsula 00.
```

Ese ida y vuelta —mg objetivo ↔ potencia del extracto ↔ tamaño de cápsula— es todo el diseño de un producto en
polvo. Hazlo en `lab-tools/betaglucano_dosis.py` antes de cotizar nada (`161`).

## El filtro #2: sabor

| Material | Problema de sabor | Formato que lo resuelve |
|---|---|---|
| Extracto de reishi | Muy amargo (triterpenos) | Cápsula; jamás polvo suelto sin enmascarar |
| Melena de león | Suave, terroso | Polvo, café funcional, cápsula |
| Cordyceps | Suave | Polvo, bebida |
| Chaga | Amargo-terroso, tolerable | Infusión, polvo |
| Extracto de cannabis | Herbal fuerte, persistente | Aceite saborizado, gomita, cápsula blanda |

Regla: **si es amargo, encapsúlalo.** El enmascaramiento de sabor real (ciclodextrinas, encapsulación,
recubrimiento) es tecnología cara (`162`); la cápsula lo resuelve por 0 pesos adicionales.

## El filtro #3: estabilidad

| Sensibilidad del activo | Formatos a evitar | Formatos preferidos |
|---|---|---|
| Oxidación (fenoles, aceites) | Polvo suelto en frasco transparente | Cápsula en blíster, aceite en ámbar con poco headspace |
| Humedad (higroscópico) | Gomita, polvo en sobre permeable | Cápsula en frasco con desecante |
| Luz | Cualquier envase claro | Ámbar, opaco, secundario de cartón |
| Hidrólisis (psilocibina, ésteres) | Todo lo acuoso | Sólido seco (`255`) |
| Migración a plástico (cannabinoides) | PET delgado | Vidrio, HDPE de barrera (`163`) |

## El filtro #4: presupuesto y planta

Y el filtro que nadie quiere mirar: en Colombia, a agosto de 2026, la fabricación de suplementos dietarios
requiere planta certificada en BPM, y el certificado se verifica al pedir registro sanitario (`167`, `269`). Eso
significa que **la forma farmacéutica que elijas debe existir en el alcance BPM de tu maquilador**. Un
maquilador certificado para polvos y cápsulas no necesariamente lo está para líquidos o gomitas. Preguntar el
alcance del certificado antes de diseñar el producto ahorra meses.

## Cómo se comprueba que la forma quedó bien

| Forma | Ensayos de control mínimos |
|---|---|
| Cápsula | Uniformidad de masa, contenido de activo, desintegración, humedad |
| Tableta | Masa, dureza, friabilidad, desintegración/disolución, contenido |
| Polvo | Uniformidad de mezcla, granulometría, densidad, contenido, a_w |
| Líquido | Volumen entregado, densidad, pH, contenido, microbiología, conservantes |
| Emulsión | Tamaño de gota (DLS), índice de polidispersidad, potencial ζ, separación |
| Tópico | Viscosidad, pH, contenido, microbiología, prueba de reto |

Los métodos generales de estos ensayos están en las farmacopeas (USP/EP) y son los que un laboratorio local
suele poder correr (`280`).

## Ejemplo aplicado — mismo activo, tres productos posibles

```
Activo: extracto dual de reishi, β-glucano 32 % p/p b.s., triterpenos 1,6 %

OPCIÓN A — cápsula 0, 420 mg de extracto
  aporta 134 mg β-glucano + 6,7 mg triterpenos por cápsula
  porción 2 cápsulas/día → 269 mg β-glucano/día
  costo de entrada: encapsuladora manual + maquila BPM.        VIABLE HOY

OPCIÓN B — polvo 60 g, porción 2 g
  aporta 640 mg β-glucano por porción
  problema: amargor de triterpenos muy marcado.                 VIABLE si se mezcla con cacao
  ventaja: dosis alta, costo por mg mucho menor

OPCIÓN C — gomita 5 g con 200 mg de extracto
  aporta 64 mg β-glucano por gomita → harían falta ~5 gomitas
  azúcar por porción alta, maquila cara, estabilidad de humedad.  NO VIABLE
```

Cifras **(ILUSTRATIVAS)**. La lectura de negocio: la gomita se cae sola por aritmética, no por gusto. Ese
descarte tomó tres renglones y le ahorra a la empresa medio año.

## Errores comunes

- Elegir el formato por tendencia (gomitas, bebidas) sin verificar si la dosis cabe.
- Diseñar la etiqueta y el frasco antes de saber cuántos mg entran por unidad.
- Ignorar el alcance BPM del maquilador y descubrir que no puede hacer tu forma.
- Poner un extracto amargo en polvo suelto y perder al cliente en la primera toma.
- Elegir líquido acuoso sin plan de conservación ni de microbiología (`100`).
- No verificar la densidad del polvo antes de comprar cápsulas vacías: se compran 100 000 del tamaño errado.
- Suponer que "nano" o "liposomal" venden solo por el nombre, sin poder medir tamaño de gota ni sostener el
  claim (`157`, `158`).

## Conexión con otros módulos

→ `154-capsulas-y-encapsulado.md` — el formato base de la pyme, en detalle.
→ `161-dosis-y-tamano-de-porcion.md` — de dónde salen los mg objetivo.
→ `160-excipientes-y-compatibilidad.md` — con qué se completa la unidad.
→ `163-envase-primario-y-compatibilidad.md` — el envase que cada forma exige.
→ `167-bpm-gmp-para-suplementos.md` — el filtro regulatorio que decide qué puedes fabricar.
