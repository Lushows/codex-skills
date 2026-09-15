# 16 — Enlace químico y geometría (por qué el beta-1,3 se disuelve distinto que el alfa-1,4)

La diferencia entre un beta-glucano que te sirve como activo y un almidón que te sirve como relleno es un
solo detalle geométrico: la orientación del oxígeno que une dos glucosas. Misma fórmula, mismos átomos,
misma masa molar — comportamiento biológico y solubilidad completamente distintos. Ese es el mensaje de
este módulo: en productos naturales, la geometría manda tanto como la composición. Si no entiendes enlace
y forma, no vas a entender por qué el agua caliente saca unas cosas y el etanol otras, ni por qué un
"polisacárido total" del 50 % puede ser puro almidón de arroz.

Términos: **enlace covalente (covalent bond)** = par de electrones compartido; el que forma moléculas
orgánicas. **enlace iónico (ionic bond)** = transferencia de electrones; sales, se disocian en agua.
**enlace glicosídico (glycosidic bond)** = puente de oxígeno entre dos azúcares; puede ser α o β según la
orientación. **hibridación (hybridization)** = mezcla de orbitales que fija los ángulos: sp3 tetraédrico
109,5°, sp2 plano 120°, sp lineal 180°. **conformación (conformation)** = forma que adopta la molécula sin
romper enlaces (silla, hélice, ovillo).

## Los tipos de enlace y dónde los ves en el oficio

| Tipo | Energía típica (kJ/mol) | Ejemplo en tu producto | Consecuencia práctica |
|---|---|---|---|
| Covalente C–C, C–O | 300–420 | Esqueleto del THC, del glucano | No se rompe con calor de cocina |
| Covalente C=O | ~750 | Carboxilo del THCA | Se pierde como CO2 al descarboxilar (`174`) |
| Iónico | 600–1000 (red) | KCl, fosfatos de buffer | Se disocia en agua, conduce, mide pH |
| Coordinado (complejo) | 50–200 | Cd unido a tioles del hongo | Explica bioacumulación de metales |
| Puente de hidrógeno | 10–40 | Glucano–agua, glucano–glucano | Manda solubilidad y viscosidad |
| Dispersión de London | 1–10 c/u | Cannabinoide–aceite | Suma mucho en moléculas grandes y grasas |

Fíjate en la última columna: los enlaces débiles son los que decides todos los días. La extracción, la
emulsión y la viscosidad son negocios de puentes de hidrógeno y dispersión, no de romper covalencias.

## Geometría: sp3, sp2 y por qué importa

```
sp3 (tetraédrico, 109,5°)  → carbonos del anillo de glucosa; molécula "gruesa", flexible
sp2 (plano, 120°)          → anillos aromáticos del CBD/THC, el indol de la psilocibina
sp  (lineal, 180°)         → nitrilos, alquinos; poco frecuente en productos naturales
```

El anillo aromático plano es lo que hace que los cannabinoides absorban luz UV a ~220 y ~275 nm — de ahí
que se cuantifiquen por HPLC-UV/DAD (`80`, `198`). El indol de la psilocibina absorbe a ~267 nm y además
fluoresce, lo que abre la detección por fluorescencia (`256`). La geometría define la técnica analítica.

## El caso que lo explica todo: α-1,4 vs β-1,3

La glucosa tiene un carbono anomérico (C1) cuyo –OH puede apuntar "abajo" (α) o "arriba" (β).

| | Almidón (α-1,4 + α-1,6) | Beta-glucano fúngico (β-1,3 con ramas β-1,6) |
|---|---|---|
| Geometría de la cadena | Hélice compacta | Hélice triple rígida / bastón |
| Solubilidad en agua fría | Baja, pero gelatiniza al calentar | Baja; sube con agua caliente prolongada |
| Enzima humana que lo corta | α-amilasa: sí | No hay; llega íntegro al intestino |
| Reconocimiento inmune | No descrito por Dectin-1 | Se une a Dectin-1 `[in vitro]` (`130`) |
| Origen típico en un polvo | Grano del sustrato (arroz, sorgo) | Pared celular del hongo |

Misma fórmula empírica (C6H10O5)n. Distinta orientación de un solo enlace. Por eso el ensayo de
"polisacáridos totales" —que hidroliza todo a glucosa y la mide— no distingue nada, y por eso existe el
método enzimático que resta α-glucano (`221`, `222`). Toda la industria del micelio en grano vive de que
el comprador no sepa este párrafo (`218`).

## Cómo se comprueba

| Pregunta | Técnica | Qué te dice |
|---|---|---|
| ¿α o β, y en qué posición? | RMN de 13C y 1H (desplazamiento del anómero) | Configuración inequívoca (`94`) |
| ¿Qué enlaces glicosídicos hay? | Análisis de metilación + GC-MS | Mapa de ramificación 1,3 / 1,6 |
| ¿Cuánto β-glucano, en la práctica? | Megazyme K-YBGL: glucano total − α-glucano | % p/p base seca (`221`) |
| ¿Qué grupos funcionales tiene? | FTIR (banda ~890 cm⁻¹ enlace β) | Confirmación rápida, no cuantitativa (`92`) |
| ¿Cuál es la conformación en solución? | Dispersión de luz, viscosimetría | Peso molecular y forma (`34`) |

Orden de magnitud esperado en cuerpo fructífero de hongo bien extraído: β-glucano reportado en la
literatura en decenas de % p/p base seca según especie y proceso — verifica con tu lote, nunca lo asumas.

## Ejemplo aplicado

Te llegan dos polvos rotulados "extracto de melena de león 30 %" **(ILUSTRATIVO)**:

```
Muestra A  Glucano total 32,4 %  α-glucano 2,1 %  → β-glucano 30,3 % p/p b.s.  (K-YBGL)
Muestra B  "Polisacáridos" 31,8 % (fenol-sulfúrico, calculado como glucosa)
```

La A te dice qué es. La B no dice nada: si le corres el ensayo enzimático puede aparecer α-glucano 28 %
(almidón del grano) y β-glucano 3 %. La geometría del enlace, invisible en el ensayo colorimétrico, es
exactamente la diferencia entre un activo y un relleno. La conclusión comercial: el método de la muestra B
no sostiene su etiqueta; hay que repetir con K-YBGL antes de comprar (`110`, `246`).

## Errores comunes

- Creer que "misma fórmula = misma sustancia". Δ8 y Δ9-THC comparten fórmula y difieren en dónde está el
  doble enlace: distinta farmacología, distinta legalidad (`180`).
- Suponer que el calor rompe enlaces covalentes de forma útil. Calentar no convierte almidón en
  beta-glucano; solo gelatiniza y a veces degrada tu activo.
- Pedir "polisacáridos" al laboratorio pensando que es lo mismo que beta-glucanos.
- Ignorar que la conformación (hélice triple) cambia con el solvente y el calor: el mismo polímero puede
  medir distinto según cómo lo hayas tratado antes del ensayo.
- Olvidar que los enlaces débiles, no los fuertes, gobiernan solubilidad, viscosidad y estabilidad física.

## Conexión con otros módulos

→ `17-polaridad-y-fuerzas-intermoleculares.md` — los enlaces débiles en detalle.
→ `42-isomeria-y-estereoquimica.md` — cuando la fórmula es igual y la molécula no.
→ `52-polisacaridos-y-glucanos.md` — la química completa de los glucanos.
→ `219-beta-glucanos-quimica-y-estructura.md` — el activo estrella de los hongos funcionales.
→ `221-medir-beta-glucanos-metodo-megazyme.md` — cómo se mide de verdad.
→ `94-rmn-fundamentos.md` — la técnica que resuelve α vs β sin discusión.
