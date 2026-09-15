# 158 — Liposomas y ciclodextrinas (dos tecnologías reales y muy mal usadas en etiqueta)

"Liposomal" y "con ciclodextrina" son sellos que suben el precio de un suplemento entre 30 % y 200 % y que casi
nunca vienen acompañados de un solo dato que los sostenga. Ambas tecnologías son reales, tienen literatura
sólida y resuelven problemas concretos —solubilizar lo insoluble, proteger lo inestable, enmascarar lo
amargo—. Pero también son las dos más fáciles de simular: basta con agregar un poco de lecitina o de
ciclodextrina a la fórmula y escribir la palabra en el frasco. Este módulo te da los ensayos que separan lo
uno de lo otro.

Términos: **liposoma (liposome)** = vesícula de bicapa lipídica (típicamente fosfolípidos) con un núcleo
acuoso. **Fitosoma (phytosome)** = complejo de un extracto con fosfolípidos, no necesariamente vesicular.
**Ciclodextrina (cyclodextrin, CD)** = oligosacárido cíclico con cavidad hidrofóbica interna y exterior
hidrofílico. **Complejo de inclusión (inclusion complex)** = la molécula huésped alojada dentro de la cavidad.
**Constante de asociación (K)** = qué tan fuerte es el complejo.

## Liposomas: qué son y qué no

Un liposoma tiene una **bicapa** de fosfolípidos, un interior acuoso y —esto es lo importante— se forma con
energía (sonicación, extrusión, homogeneización) o con métodos de inyección de solvente. Mezclar lecitina con
un extracto en una licuadora produce una dispersión de fosfolípidos, no liposomas.

| Estructura | Qué contiene | Cómo se hace | ¿Verificable? |
|---|---|---|---|
| Liposoma verdadero | Bicapa + núcleo acuoso | Hidratación de película + extrusión/sonicación | Sí: DLS + microscopía electrónica (crio-TEM) |
| Fitosoma | Complejo activo-fosfolípido | Reacción en solvente + secado | Sí: DSC, FTIR, RMN muestran el complejo |
| "Liposomal" de mercado | Lecitina dispersada | Mezclado | No — porque no hay estructura |

Ventaja real de la ruta fosfolipídica: para activos **lipofílicos**, el complejo con fosfatidilcolina mejora la
dispersión en medio acuoso y ha mostrado mejoras de absorción en varios extractos vegetales `[clínico, en
extractos específicos]`. No se puede extrapolar el resultado de un extracto a otro: cada complejo se estudia.

Y una limitación que las marcas nunca mencionan: **la mayoría de los "liposomales" orales líquidos son
inestables**. Las vesículas se fusionan, sedimentan y se oxidan (los fosfolípidos insaturados enrancian). Un
liposomal serio suele venir en polvo seco o con un sistema de estabilización declarado.

## Ciclodextrinas: la tecnología subestimada

Las ciclodextrinas son anillos de glucosa. Su cavidad interior es hidrofóbica y su exterior hidrofílico:
atrapan una molécula apolar adentro y la vuelven "soluble" en agua. Es la solución más elegante y más barata al
problema de solubilizar cannabinoides o triterpenos.

| Tipo | Unidades de glucosa | Diámetro de cavidad | Solubilidad en agua (25 °C) | Nota |
|---|---|---|---|---|
| α-CD | 6 | ~0,47–0,53 nm | Alta | Cavidad pequeña |
| β-CD | 7 | ~0,60–0,65 nm | **Baja** (~1,85 g/100 mL) | La más usada; su baja solubilidad limita |
| γ-CD | 8 | ~0,75–0,83 nm | Muy alta | Cavidad grande, cara |
| HP-β-CD (hidroxipropil-β) | 7 modificada | ~0,60–0,65 nm | Muy alta | **La versátil**: resuelve el límite de β-CD |
| SBE-β-CD (sulfobutiléter) | 7 modificada | ~0,60–0,65 nm | Muy alta | Grado inyectable, cara |

Tres usos legítimos, con evidencia y medibles:

1. **Solubilizar.** Un cannabinoide complejado con HP-β-CD se dispersa en agua. Se mide por aumento de
   solubilidad aparente.
2. **Enmascarar sabor.** La ciclodextrina secuestra la molécula amarga y el receptor no la ve. Es de las pocas
   rutas de enmascaramiento que funcionan de verdad (`162`).
3. **Estabilizar.** La molécula dentro de la cavidad está protegida de oxígeno y luz. Se mide por estabilidad
   comparativa (`164`).

Estado regulatorio, a agosto de 2026: β-CD, α-CD y γ-CD tienen aceptación como ingredientes/aditivos
alimentarios en varias jurisdicciones, con condiciones y límites que varían por país y por uso. En Colombia hay
que verificar la admisibilidad del ingrediente concreto para la categoría de tu producto ante INVIMA antes de
formular (`266`, `278`). No asumas por analogía con EE. UU. o la UE.

## Cómo se comprueba que el complejo existe

Este es el corazón del módulo. La palabra "liposomal" o "ciclodextrina" en la etiqueta no prueba nada; estos
ensayos sí:

| Pregunta | Técnica | Qué se ve si es real |
|---|---|---|
| ¿Hay vesículas? | Crio-TEM / microscopía electrónica | Se ven las bicapas |
| ¿Qué tamaño y uniformidad? | DLS: Z-average y PDI (`157`) | Distribución definida, típicamente 50–200 nm |
| ¿Está encapsulado o libre? | **Eficiencia de encapsulación**: separar libre por diálisis/ultrafiltración/SEC y cuantificar | % encapsulado > 0 |
| ¿Se formó el complejo de inclusión? | DSC / TGA (`99`) | Desaparece el pico de fusión del huésped libre |
| ¿Cambió el entorno molecular? | FTIR (`92`), RMN (`94`) | Desplazamientos de señales del huésped |
| ¿Cuánto más soluble es? | Diagrama de solubilidad de fases (Higuchi-Connors) | Curva y constante de asociación K |
| ¿Sirve de verdad? | Estudio de absorción comparativo | El único que sostiene un claim de absorción |

**El ensayo mínimo exigible a un proveedor:** eficiencia de encapsulación + DLS, por lote. Sin eso, estás
comprando una palabra.

## Costo y viabilidad para pyme

| Tecnología | Equipo necesario | ¿Pyme colombiana? |
|---|---|---|
| Liposoma por extrusión | Extrusor + filtros de policarbonato | Laboratorio sí, producción no |
| Liposoma por homogeneización | HPH (`157`) | Maquila |
| Fitosoma | Reactor con solvente + secado | Maquila |
| **Complejo con ciclodextrina por co-molienda** | Molino de bolas | **Sí, a escala pequeña** |
| Complejo por amasado (kneading) | Mortero/amasadora + secado | **Sí** |
| Complejo por liofilización | Liofilizador | Maquila del secado (`150`) |

Dato práctico poco conocido: el método de **amasado (kneading)** —pasta de ciclodextrina + agua/etanol +
activo, amasar, secar— es de los pocos procesos de encapsulación molecular que una pyme puede montar de verdad.
No da la eficiencia de la liofilización, pero da complejo real y medible.

## Ejemplo aplicado — amargo del reishi con HP-β-CD

```
Problema: el extracto alcohólico de reishi es intensamente amargo por los triterpenos.
Objetivo: bebible palatable sin recubrir ni encapsular en cápsula.

Ensayo (ILUSTRATIVO)
  Relación molar activo : HP-β-CD probada 1:1 y 1:2
  Método: amasado 30 min con etanol 50 % → secado 40 °C al vacío → molienda
  Verificación:
    - DSC: reducción del evento térmico del triterpeno libre  → indicio de complejo
    - solubilidad aparente en agua: sube de 0,04 a 0,61 mg/mL (1:2)
    - panel sensorial ciego n = 12: amargor percibido baja de 7,8 a 3,4 en escala 0–10
  Costo del HP-β-CD por porción: calcular con `contador_lushows`; suele ser el limitante.

Etiqueta posible: "con hidroxipropil-β-ciclodextrina para mejorar la dispersión y el sabor".
Etiqueta imposible: cualquier afirmación de que eso mejora un efecto en salud (`267`).
```

## Errores comunes

- Comprar "liposomal" sin eficiencia de encapsulación. Es la pregunta que revienta el 90 % de las ofertas.
- Poner lecitina en la fórmula y escribir "liposomal". Es una afirmación de estructura que no existe.
- Usar β-CD nativa para solubilizar y toparse con su propia baja solubilidad en agua.
- Ignorar la estequiometría: el complejo tiene una relación molar; poner "un poquito" de CD no complejea nada.
- Dar por sentado que la ciclodextrina está permitida en tu categoría de producto en Colombia sin verificarlo.
- Extrapolar el resultado de absorción de un fitosoma de curcumina a tu extracto de hongo. Cada complejo es
  distinto.
- Formular liposomas líquidos y no controlar la oxidación de los fosfolípidos: el producto enrancia.

## Conexión con otros módulos

→ `157-emulsiones-y-nanoemulsiones.md` — la otra vía para lo lipofílico, con sus propios límites.
→ `159-potenciadores-de-biodisponibilidad.md` — el panorama completo de estrategias.
→ `162-enmascaramiento-de-sabor.md` — dónde la ciclodextrina brilla de verdad.
→ `99-analisis-termico-dsc-y-tga.md` — la técnica que demuestra que hay complejo.
→ `122-biodisponibilidad-y-efecto-de-primer-paso.md` — por qué todo esto importa farmacológicamente.
