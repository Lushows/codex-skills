# 142 — Secado y conservación de biomasa (el paso barato donde se pierde el producto)

Secar parece trivial: quitar agua. Pero es el paso donde más activo se destruye por ahorrarse horas, y donde
más lotes se pierden por hongos y mohos si te quedas corto. El agua es a la vez el vehículo de la degradación
(hidrólisis, enzimas, crecimiento microbiano) y el motivo por el que un kilo de fresco no es un kilo de seco.
Si secas mal, todo lo que hagas después —extracción, estandarización, estabilidad— arranca con una materia
prima que ya perdió lo que ibas a vender.

Términos: **humedad (moisture content)** = agua total, en % p/p. **Actividad de agua (water activity, a_w)** =
agua *disponible* para microorganismos y reacciones, escala 0–1; no es lo mismo que humedad (`35`).
**Termolábil (heat-labile)** = que se degrada con calor. **Base seca (dry basis)** = referida a la masa sin
agua (`07`).

## Humedad no es actividad de agua

| Concepto | Qué mide | Cómo se mide | Qué te dice |
|---|---|---|---|
| Humedad (%) | Agua total | Karl Fischer (`98`) o pérdida por secado 105 °C | Cuánto pesa el agua que estás comprando |
| a_w | Agua libre | Higrómetro de punto de rocío | Si crece moho / si el producto se apelmaza |

Órdenes de magnitud reportados en la literatura de alimentos secos (verificar para tu material):

```
a_w > 0,90   bacterias en general
a_w > 0,85   Staphylococcus aureus, límite clásico de alimentos "seguros"
a_w > 0,70   mohos xerófilos; riesgo de micotoxinas (`101`, `244`)
a_w < 0,60   práctica común como objetivo de estabilidad para polvos botánicos
```

Objetivo práctico para polvo de hongo o material vegetal seco **(ILUSTRATIVO)**: humedad ≤ 8 % p/p y
a_w ≤ 0,60. Fija el tuyo con datos de tu producto, no con este número.

## Métodos de secado: qué puede una pyme y qué no

| Método | Rango típico de T | Costo relativo | Riesgo al activo | ¿Pyme? |
|---|---|---|---|---|
| Sol directo | Ambiente, luz UV alta | Casi cero | Fotodegradación, contaminación, lluvia | Solo si no hay otra; poco controlable |
| Sombra con ventilación forzada | 25–35 °C | Bajo | Bajo si el aire es seco | Sí |
| Deshidratador de bandejas con control | 40–60 °C | Bajo–medio | Bajo a 40–50 °C | **Sí, la opción base** |
| Horno de convección | 50–80 °C | Bajo | Alto sobre 60 °C para termolábiles | Sí, con termómetro propio |
| Secado al vacío | 30–50 °C a presión reducida | Medio | Muy bajo | Con equipo pequeño, sí |
| Lecho fluidizado | 40–70 °C | Alto | Bajo, muy rápido | Maquila |
| Liofilización (freeze-drying) | −40 °C → sublimación | Alto | El más bajo | Maquila (`150`) |

Regla honesta para pyme colombiana: **deshidratador de bandejas con control de temperatura real** (termómetro
independiente, no el del panel) resuelve el 90 % de los casos. Lo que no resuelve es el secado del *extracto*
líquido, que sí exige spray dryer o liofilizador (`150`).

## Qué se pierde con el calor

No todos los activos son iguales frente a la temperatura:

| Activo | Sensibilidad térmica | Consecuencia práctica |
|---|---|---|
| β-glucanos (polímeros) | Baja a moderada | Toleran secado y decocción; el enemigo es la hidrólisis prolongada (`219`) |
| Triterpenos ganodéricos | Moderada | Preferir ≤ 50 °C; oxidación con aire caliente (`224`) |
| Hericenonas / erinacinas | Alta (reportada como termolábil) | Secado suave; verificar por HPLC antes/después (`226`) |
| Ergotioneína | Moderada | Estable en seco; se pierde por lixiviación si lavas (`235`) |
| Terpenos volátiles (cannabis) | Muy alta, se evaporan | Secado lento a 18–24 °C es el estándar del sector (`186`) |
| THCA | Se descarboxila con T y tiempo | Secar caliente = perder forma ácida (`174`) |
| Vitamina D2 (post-UV) | Sensible a luz y oxígeno | Proteger de luz (`236`) |

## Cómo se comprueba que el secado no destruyó nada

La única forma honesta: **medir el mismo analito antes y después, ambos en base seca**.

```
DISEÑO MÍNIMO DE VERIFICACIÓN DE SECADO

Material: un lote homogéneo dividido en 3 porciones (n = 3 por condición).
Condiciones: A = 40 °C/24 h · B = 50 °C/12 h · C = 60 °C/6 h
Se mide en cada porción:
  - humedad final (% p/p)              → Karl Fischer o balanza halógena
  - a_w
  - analito clave (% p/p BASE SECA)    → Megazyme (β-glucano) o HPLC-DAD (triterpenos)
  - color (L*a*b*) si hay pardeamiento → indicio de Maillard (`62`)

Criterio de decisión: la condición más rápida cuya pérdida de analito
frente a la referencia (40 °C) sea menor que la incertidumbre del método (`76`).
```

Sin la corrección a base seca la comparación es basura: el material más seco parece "más potente" solo porque
tiene menos agua. Ejecuta la corrección con `lab-tools/base_seca.py`.

## Ejemplo aplicado — reishi seco a tres temperaturas

Datos **(ILUSTRATIVOS)** para ilustrar cómo se lee la tabla, no como resultado real:

```
Condición   Humedad final   β-glucano (% p/p b.s.)   Triterpenos (% p/p b.s.)   Tiempo
A 40 °C        7,8 %              24,1                     2,05                 24 h
B 50 °C        7,5 %              23,8                     1,92                 12 h
C 60 °C        7,2 %              23,5                     1,54                  6 h

Lectura: el β-glucano casi no se mueve (polímero robusto).
Los triterpenos caen ~25 % entre 40 y 60 °C.
Si tu claim es de β-glucano, C te sirve y ahorras 18 h.
Si tu claim incluye triterpenos, C te sale carísimo.
```

Traducción de negocio: **la temperatura de secado la decide el analito que vas a declarar**, no el afán.

## Conservación después del secado

- Envasar en cuanto llegue a la humedad objetivo; el material seco reabsorbe agua del aire (es higroscópico).
- Bolsa de barrera (aluminio/PET metalizado) sellada, con desecante si el clima lo exige. Colombia costera y
  Bogotá son problemas distintos: verifica humedad relativa ambiente de tu bodega.
- Oscuridad. Luz + oxígeno degrada fenoles y carotenoides (`61`).
- Rotulado con lote, fecha de secado, humedad final y responsable (`168`).
- Control periódico de a_w en bodega si el almacenamiento supera 3 meses.

## Errores comunes

- Secar a 70–80 °C "porque rinde más rápido" y perder los termolábiles justo antes de extraer.
- Confundir seco al tacto con seco medido. Sin balanza halógena o Karl Fischer, no sabes.
- Comparar potencias entre lotes sin corregir a base seca: la diferencia es agua, no calidad (`07`).
- Guardar en bolsa de polietileno simple: no es barrera de humedad ni de oxígeno (`163`).
- Secar sobre superficies no sanitarias o al sol descubierto y luego sorprenderse con la microbiología (`100`).
- Ignorar que si te quedas en a_w ~0,7 el moho crece aunque el material "parezca" seco — y con el moho vienen
  micotoxinas (`244`).

## Conexión con otros módulos

→ `35-actividad-de-agua-y-humedad.md` — la física detrás de a_w.
→ `240-secado-y-perdida-de-activos.md` — el detalle específico por especie de hongo.
→ `186-cosecha-secado-y-curado.md` — el equivalente en cannabis, con terpenos de por medio.
→ `143-molienda-y-granulometria.md` — el paso siguiente; solo se muele lo que está seco.
→ `150-secado-por-aspersion-y-liofilizacion.md` — cómo se seca el extracto líquido, que es otro problema.