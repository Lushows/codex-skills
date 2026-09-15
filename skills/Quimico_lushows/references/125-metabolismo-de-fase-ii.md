# 125 — Metabolismo de fase II (la conjugación que se traga los polifenoles y la curcumina)

Si la fase I (CYP450, `124`) es la que oxida, la fase II es la que **etiqueta para la basura**: le pega al
compuesto una molécula grande y polar para que el riñón o la bilis puedan sacarlo. Este módulo importa
mucho en productos naturales porque explica el destino real de polifenoles, flavonoides y curcumina: se
absorben y se conjugan tan rápido que en plasma casi no queda la molécula libre que se estudió `[in vitro]`.
El error caro que evita: construir un producto y un claim sobre una molécula que en sangre prácticamente no
existe en su forma activa.

Términos: **conjugación (conjugation)** = unir el compuesto a un grupo polar (glucurónico, sulfato,
glutatión, acetilo, metilo). **UGT (UDP-glucuronosyltransferase)** = la enzima de glucuronidación, la vía
más importante en volumen. **SULT (sulfotransferase)** = sulfatación. **GST (glutathione S-transferase)** =
conjugación con glutatión, clave en detoxificación de electrófilos. **Circulación enterohepática
(enterohepatic circulation)** = el conjugado sale por bilis, la microbiota lo desconjuga en el intestino y
el compuesto se reabsorbe.

## Las rutas de fase II

| Ruta | Enzima | Cofactor | Qué conjuga típicamente | Consecuencia |
|---|---|---|---|---|
| Glucuronidación | UGT1A, UGT2B | UDPGA | Fenoles, alcoholes, carboxilos, aminas | Vía dominante en masa; produce metabolito muy polar |
| Sulfatación | SULT | PAPS | Fenoles pequeños | Alta afinidad pero **se satura rápido** (poco PAPS) |
| Conjugación con glutatión | GST | Glutatión (GSH) | Electrófilos reactivos, epóxidos | Vía protectora clave (ver `133`) |
| Acetilación | NAT1/NAT2 | Acetil-CoA | Aminas aromáticas | NAT2 es polimórfica: acetiladores lentos y rápidos |
| Metilación | COMT, TPMT | SAM | Catecoles, tioles | COMT metaboliza catecolaminas y catequinas |
| Conjugación con aminoácidos | — | Glicina, taurina | Ácidos carboxílicos | Menos frecuente |

Dos hechos que cambian el diseño de un producto:

1. **La sulfatación se satura.** A dosis bajas domina la sulfatación; a dosis altas se agota el PAPS y pasa
   a dominar la glucuronidación. Por eso la farmacocinética de algunos fenoles **no es lineal con la dosis**.
2. **La conjugación normalmente inactiva, pero no siempre.** El caso emblemático contrario es la morfina:
   su metabolito morfina-6-glucurónido es activo. Nunca asumas que el conjugado no hace nada; hay que
   medirlo.

## El caso que hay que entender: polifenoles y curcumina

Los estudios `[in vitro]` de polifenoles se hacen con la **aglicona libre** en el pozo. En una persona, tras
dosis oral, lo que circula son mayoritariamente **glucurónidos y sulfatos**, y la concentración de la forma
libre suele quedar en el rango nanomolar, órdenes de magnitud por debajo de las concentraciones
micromolares usadas en cultivo `[clínico]`.

Esto tiene tres implicaciones honestas:

- Muchos mecanismos `[in vitro]` de polifenoles no son alcanzables por vía oral tal como se plantearon.
- El efecto real, si existe, puede depender del **metabolito conjugado**, de la **desconjugación local en
  tejido inflamado** o de la acción **en el lumen intestinal** antes de absorberse (ver `131`).
- Cualquier claim que se apoye en un ensayo celular con aglicona libre está mal cimentado.

Un ejemplo con nombre propio: la curcumina libre tiene biodisponibilidad muy baja y se conjuga
masivamente; los productos con piperina o formulaciones fosfolipídicas buscan justamente inhibir esa
glucuronidación o mejorar la permeabilidad (ver `159`). Y ahí aparece el efecto secundario del truco: **si
inhibes la glucuronidación, inhibes también la de los fármacos del usuario** (`124`, `139`).

## Circulación enterohepática y microbiota

```
Compuesto → hígado → glucurónido → bilis → intestino
                                              │
                        microbiota (β-glucuronidasa) desconjuga
                                              │
                                    compuesto libre → se reabsorbe
```

Consecuencias: perfil plasmático con **segundo pico**, vida media aparente más larga, y variabilidad
enorme entre personas según su microbiota. Es una de las razones por las que la respuesta a productos
vegetales varía tanto de una persona a otra (ver `131`).

## Cómo se mide

| Pregunta | Método | Unidad | Nivel |
|---|---|---|---|
| ¿Se glucuronida? ¿Por cuál UGT? | Microsomas hepáticos + UDPGA; UGT recombinantes | µL/min/mg (CLint) | `[in vitro]` |
| ¿Qué circula realmente en plasma? | LC-MS/MS con y sin hidrólisis enzimática (β-glucuronidasa/sulfatasa) | ng/mL libre vs total | `[clínico fase 1]` |
| ¿El metabolito es activo? | Sintetizar/aislar el conjugado y ensayarlo | EC50 | `[in vitro]` |
| ¿Hay saturación de vía? | PK a varias dosis, ver si AUC crece de forma no proporcional | AUC vs dosis | `[clínico fase 1]` |

El truco analítico clave: **medir "total" (tras hidrólisis) y "libre" por separado.** Un COA de plasma que
solo reporta "total" oculta que el 95 % está conjugado. Es un error de interpretación muy frecuente en la
literatura de productos naturales.

## Ejemplo aplicado — un extracto de chaga "rico en polifenoles"

Ficha del proveedor **(ILUSTRATIVO)**: "Polifenoles totales 42 mg GAE/g por Folin-Ciocalteu. Potente
actividad antioxidante." Lo que hay que decir:

1. Folin-Ciocalteu no mide polifenoles: mide **poder reductor**, y responde también a azúcares reductores,
   ácido ascórbico y proteínas. Es un método de tamizaje, no de identidad (ver `91`).
2. Aunque hubiera 42 mg GAE/g reales, tras la dosis oral esos fenoles se conjugarán en fase II y la
   concentración libre en plasma será una fracción pequeña.
3. La actividad "antioxidante" medida en tubo (DPPH, ORAC) **no predice** actividad antioxidante en la
   persona; hay consenso regulatorio y científico sobre eso (ver `133`).
4. Conclusión: el dato sirve para control de proceso (comparar lotes entre sí), no para sostener un claim.

## Errores comunes

- Basar un mecanismo en concentraciones de aglicona libre imposibles de alcanzar por vía oral.
- Reportar solo "concentración total" en plasma sin separar libre de conjugado.
- Suponer que el conjugado siempre es inactivo (morfina-6-glucurónido dice lo contrario).
- Usar potenciadores que inhiben UGT sin advertir el riesgo de interacción con medicamentos.
- Ignorar la circulación enterohepática al interpretar un segundo pico como error analítico.
- Confundir un ensayo de poder reductor (Folin, DPPH, ORAC) con evidencia biológica.

## Conexión con otros módulos

→ `124-citocromo-p450-e-interacciones.md` — la fase I y las interacciones.
→ `122-biodisponibilidad-y-efecto-de-primer-paso.md` — por qué la fase II destruye la F oral.
→ `131-eje-intestino-cerebro-y-microbiota.md` — la microbiota que desconjuga y transforma.
→ `133-estres-oxidativo-y-antioxidantes.md` — glutatión, GST y por qué ORAC no vale.
→ `51-polifenoles-y-flavonoides.md` — la química de estos compuestos.