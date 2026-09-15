# 155 — Tabletas y compresión (por qué casi nunca es tu primer formato)

La tableta es el formato más eficiente del mundo para producir a gran escala y el más exigente para producir
bien. Comprimir polvo hasta convertirlo en un sólido que aguante el transporte, se desintegre en el estómago y
tenga la misma cantidad de activo en cada unidad es un problema de ingeniería, no de recetas. Para una pyme que
está empezando con extractos de hongos, este módulo tiene una conclusión incómoda pero honesta: **empieza por
cápsula** (`154`) y pasa a tableta solo cuando el volumen lo justifique.

Términos: **compresión directa (direct compression)** = mezclar y comprimir sin pasos intermedios.
**Granulación (granulation)** = aglomerar el polvo antes de comprimir, húmeda o seca. **Compactación por
rodillos (roller compaction)** = granulación seca. **Dureza (hardness / crushing strength)** = fuerza que
soporta la tableta, en N o kp. **Friabilidad (friability)** = % de masa que pierde al rodar en el friabilómetro.
**Capping / laminación** = la tableta se parte en capas al salir. **Punzones (punches)** y **matriz (die)** =
las herramientas que le dan la forma.

## Las tres rutas de fabricación

| Ruta | Cómo funciona | Ventaja | Cuándo se usa |
|---|---|---|---|
| Compresión directa | Mezclar activo + excipientes → comprimir | Menos pasos, menos costo, sin calor ni agua | Si el polvo fluye y comprime bien |
| Granulación seca (roller compaction) | Compactar entre rodillos → moler a gránulo → comprimir | Sin agua ni calor: ideal para termolábiles e higroscópicos | **La ruta típica de extractos de hongos** |
| Granulación húmeda | Amasar con aglutinante líquido → secar → moler → comprimir | Mejor uniformidad y compresibilidad | Si el activo tolera agua y calor |

Los extractos secos de hongos son higroscópicos, amorfos y suelen fluir mal: rara vez van por compresión
directa sin ayuda, y la granulación húmeda los expone justo a lo que no toleran (agua). Por eso la
**compactación por rodillos** es la ruta habitual — y es equipo de planta, no de garaje.

## La fórmula de una tableta

| Función | Ejemplos | % típico |
|---|---|---|
| Activo | Extracto estandarizado | 30–80 % |
| Diluyente | Celulosa microcristalina, fosfato dicálcico, lactosa, manitol | 10–50 % |
| Aglutinante (binder) | Povidona (PVP), HPMC, almidón pregelatinizado | 2–8 % |
| Desintegrante | Croscarmelosa sódica, glicolato sódico de almidón | 2–6 % |
| Deslizante | Dióxido de silicio coloidal | 0,2–1,0 % |
| Lubricante | Estearato de magnesio | 0,3–1,0 % |
| Recubrimiento (opcional) | HPMC + plastificante + pigmento | 2–4 % sobre masa |

Detalle que cuesta lotes: el **estearato de magnesio en exceso** (o mezclado demasiado tiempo) recubre las
partículas con una película hidrofóbica y **retrasa la desintegración**. Regla práctica: mezclar el lubricante
al final, 2–5 minutos, no más.

## Los cuatro defectos clásicos y su causa

| Defecto | Qué se ve | Causa habitual | Arreglo |
|---|---|---|---|
| Capping / laminación | La tapa se separa en capas | Aire atrapado, compresión muy rápida, poco aglutinante | Bajar velocidad, precompresión, granular |
| Sticking / picking | El polvo se pega al punzón | Humedad alta, lubricante insuficiente, activo pegajoso | Secar, subir lubricante, pulir punzones |
| Mottling | Color moteado | Mezcla no homogénea, migración de colorante | Mejorar mezclado, cambiar colorante |
| Variación de peso | Masas dispersas | Flujo pobre del granulado | Granular, agregar deslizante |

Los extractos de hongos y de cannabis son especialmente propensos a **sticking**: son resinosos e higroscópicos.
Recubrir con celulosa microcristalina antes de comprimir ayuda; controlar la humedad relativa de la sala,
también.

## Cómo se comprueba una tableta

```
CONTROLES EN PROCESO (cada 15–30 min durante la compresión)
  masa individual (n = 10–20), dureza (n = 5–10), espesor, friabilidad

CONTROLES DE LOTE
  Uniformidad de masa       criterio farmacopeico según masa media (`280`)
  Dureza                    típicamente 50–150 N, según tamaño y formato
  Friabilidad               ≤ 1,0 % de pérdida (criterio farmacopeico general)
  Desintegración            ≤ 30 min en agua a 37 °C (suplementos no recubiertos)
  Disolución                si aplica al producto y al claim (`280`)
  Contenido de activo       sobre muestra compuesta, método del marcador (`152`)
  Uniformidad de contenido  n = 10 unidades individuales cuando el activo es de baja dosis
  Humedad, microbiología    (`98`, `100`)
```

Un detalle que la gente confunde: **dureza y friabilidad no son lo mismo.** La dureza es cuánta fuerza aguanta
antes de romperse; la friabilidad es cuánto se desgasta al rozarse. Una tableta puede ser dura y friable a la
vez si el borde está mal formado.

## Costo real de entrar a tabletas

| Elemento | Nota |
|---|---|
| Tableteadora rotativa | Inversión de planta; una monopunzón sirve para desarrollo, no para producción |
| Juego de punzones y matriz | Se compra por formato; cambiar de forma = comprar herramienta nueva |
| Compactador de rodillos | Otra inversión completa |
| Durómetro y friabilómetro | Baratos, pero **obligatorios** para controlar |
| Sala con control de humedad | Crítico para extractos higroscópicos |
| Desarrollo de fórmula | 5–15 ensayos antes de una fórmula estable, cada uno con material |

Conclusión honesta para pyme colombiana: **tableta = maquila**, y solo cuando vendas volumen suficiente para
que el costo por unidad baje frente a la cápsula. Si vendes 2 000 frascos al mes, la cápsula gana. La tableta
empieza a tener sentido cuando el costo de la cápsula vacía (que se paga por unidad) supera el costo de
amortizar el desarrollo de la tableta.

## Ejemplo aplicado — ¿tableta o cápsula para el extracto de reishi?

```
Escenario (ILUSTRATIVO)
  Producto: 469 mg de extracto por unidad (de `154`)
  Volumen esperado: 2 500 frascos/mes × 60 unidades = 150 000 unidades/mes

CÁPSULA 00 HPMC
  cápsula vacía: costo unitario que se paga SIEMPRE
  llenado: encapsuladora manual o maquila
  desarrollo: prácticamente nulo (mezclar y llenar)
  tiempo a mercado: semanas

TABLETA 700 mg (469 mg activo + 231 mg excipientes)
  sin cápsula que comprar, pero:
  desarrollo de fórmula: varios ensayos + material perdido
  granulación seca por maquila
  punzones dedicados
  tiempo a mercado: meses

Decisión ILUSTRATIVA: cápsula. Reevaluar tableta al superar ~500 000 unidades/mes,
y hacer la cuenta de costo unitario completo con `contador_lushows` / `economist_lushows`.
```

Nota de producto, no solo de costo: el consumidor de suplementos de hongos tiende a percibir la cápsula
vegetal como más "natural" que la tableta recubierta. Ese factor de percepción es real y lo trabaja
`directorcreativo_lushows`; aquí solo se deja anotado para que no se decida únicamente por centavos.

## Errores comunes

- Empezar por tableta "porque se ve más profesional" y quemar el presupuesto en desarrollo.
- Sobre-lubricar o sobre-mezclar el lubricante y obtener tabletas que no se desintegran.
- Comprimir un extracto sin controlar la humedad de la sala: sticking garantizado.
- Confundir dureza con calidad: una tableta muy dura que no se desintegra es un producto que no libera nada.
- No hacer uniformidad de contenido en activos de baja dosis; la masa uniforme no lo garantiza.
- Cambiar de proveedor de excipiente sin revalidar: el mismo nombre con distinto grado cambia la compresión
  (`160`, `169`).
- Recubrir para tapar un problema de sabor o de aspecto en vez de arreglar la fórmula.

## Conexión con otros módulos

→ `154-capsulas-y-encapsulado.md` — la alternativa que casi siempre gana al principio.
→ `160-excipientes-y-compatibilidad.md` — qué hace cada excipiente y qué reacciona con qué.
→ `166-escalado-de-lote.md` — por qué una fórmula que funciona en 1 kg falla en 100 kg.
→ `280-farmacopeas-usp-ep-y-monografias.md` — de dónde salen los criterios de dureza, friabilidad y
   desintegración.
→ `162-enmascaramiento-de-sabor.md` — cuándo el recubrimiento sí resuelve un problema real.