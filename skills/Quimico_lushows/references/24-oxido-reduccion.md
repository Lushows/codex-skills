# 24 — Óxido-reducción (por qué tu extracto se oscurece y tu activo se pierde en el frasco)

Casi toda la pérdida de valor que ocurre después de que el producto está hecho es una reacción redox: el
aceite de cannabis que se oscurece, la psilocina que pasa a un pigmento azul, la tintura de chaga que se
enturbia, el polvo de melena de león que huele distinto al año. No es "envejecimiento" abstracto: es
oxígeno más un metal de transición más luz, actuando sobre grupos que ceden electrones con facilidad.
Entender redox te da tres palancas concretas y baratas —envase, atmósfera y quelante— que valen más que
cualquier "antioxidante milagroso" en la etiqueta.

Términos: **oxidación (oxidation)** = pérdida de electrones (o ganancia de oxígeno / pérdida de hidrógeno).
**reducción (reduction)** = lo contrario. **agente oxidante (oxidant)** = el que se reduce y oxida a otro.
**potencial redox (E°, standard reduction potential)** = tendencia a reducirse, en voltios frente al
electrodo estándar de hidrógeno. **ROS (reactive oxygen species)** = especies reactivas de oxígeno:
radical superóxido, peróxido de hidrógeno, radical hidroxilo. **autooxidación (autoxidation)** = cadena
radicalaria iniciada por O₂ que se acelera sola.

## La cadena que te está costando plata

```
Iniciación:    RH  +  iniciador (luz, calor, Fe²⁺/Cu⁺)  →  R•
Propagación:   R•  +  O2   →  ROO•
               ROO• + RH   →  ROOH  +  R•        ← ciclo que se realimenta
Ramificación:  ROOH + Fe²⁺ →  RO•  + OH⁻ + Fe³⁺  ← un metal traza multiplica todo
Terminación:   R• + R•, R• + ROO•, o antioxidante donante de H (AH → A•, estable)
```

De ahí salen las tres intervenciones reales: **quitar el iniciador** (luz, calor), **quitar el O₂**
(envase, nitrógeno, vacío) y **secuestrar el metal** (quelante: citrato, EDTA donde esté permitido). Un
antioxidante donante (tocoferol, ácido ascórbico) solo corta la propagación; si el metal y el oxígeno
siguen ahí, se consume y después la degradación arranca igual.

## Quién se oxida en tu materia prima y en qué se convierte

| Compuesto | Grupo vulnerable | Producto de oxidación | Señal visible o analítica |
|---|---|---|---|
| Δ9-THC | Anillo ciclohexeno | CBN (cannabinol) | Pico de CBN que crece en HPLC; potencia que baja (`204`) |
| CBD | Fenoles | Quinonas (HU-331 y otras) | Amarilleo del aceite; balance de masa que no cierra |
| Psilocina | Fenol libre en C4 | Oligómeros azules tipo quinoide | El azuleo clásico; pérdida de psilocina por HPLC (`255`) |
| Terpenos (limoneno, mirceno) | Doble enlace alílico | Hidroperóxidos, p-cimeno, carvona | Olor rancio o "a cáscara vieja"; perfil GC que se mueve (`182`) |
| Ácidos grasos insaturados | Bis-alílico | Peróxidos → aldehídos (hexanal) | Índice de peróxidos; olor a rancio (`53`) |
| Polifenoles de chaga | Catecoles | Quinonas → melaninas | Oscurecimiento; el color no siempre indica pérdida de activo (`229`) |
| Ergotioneína | Tiona/tiol | Disulfuro y derivados | Solo se ve por LC-MS/MS; no hay señal visual (`235`) |
| Ácido ascórbico añadido | Enediol | Dehidroascórbico → furfurales | Pardeamiento; se consume antes que el activo, y eso es su trabajo |

Fíjate en algo incómodo: **el color no es un buen indicador**. Un extracto de chaga oscurece por
polimerización de polifenoles sin perder β-glucano, y un aceite de CBD puede perder 8 % de potencia sin
cambiar visiblemente. El color es una alarma, no una medida (`90`).

## Antioxidantes: qué hace cada tipo y cuál es su límite

| Tipo | Ejemplo | Mecanismo | Límite real |
|---|---|---|---|
| Donante de hidrógeno (primario) | Tocoferoles (vit. E), ácido rosmarínico | Corta la propagación radicalaria | Se consume; a alta dosis puede volverse prooxidante |
| Reductor / secuestrante de O₂ | Ácido ascórbico, ascorbil palmitato | Reacciona antes que el activo | Con Fe/Cu libre se vuelve prooxidante (Fenton) |
| Quelante (sinérgico) | Citrato, EDTA (donde esté permitido), fitato | Inactiva Fe y Cu que ramifican la cadena | No corta radicales; es complemento, no reemplazo |
| Barrera física | Vidrio ámbar, aluminio, N₂ headspace, oxígeno-scavenger | Quita el reactivo, no la reactividad | Depende de que el envase de verdad selle (`163`) |

Ninguno de estos "recupera" activo perdido. Todos solo compran tiempo, y ese tiempo se mide, no se supone.

## Cómo se mide

| Pregunta | Método | Unidad |
|---|---|---|
| ¿Cuánto activo perdí? | HPLC-UV o LC-MS/MS del activo en el tiempo | % del valor inicial, con su método (`79`, `83`) |
| ¿Hay peróxidos formados? | Índice de peróxidos (titulación yodométrica, AOCS Cd 8-53) | meq O₂/kg de grasa |
| ¿Hay aldehídos secundarios? | Valor de p-anisidina; hexanal por GC-headspace | Adimensional; µg/kg (`86`) |
| ¿Qué tan "antioxidante" es un extracto in vitro | DPPH, ABTS, FRAP, ORAC | µmol Trolox eq/g — **es un ensayo químico, no un efecto en el cuerpo** |
| ¿Hay metales que catalizan? | ICP-MS para Fe, Cu, Mn | mg/kg (ppm) (`88`) |
| ¿Cuánto O₂ hay en el envase? | Analizador de headspace (O₂ %) o indicador colorimétrico | % v/v de O₂ en el espacio de cabeza |
| ¿Cuál es el potencial redox del medio? | Electrodo ORP (Ag/AgCl), reportado como Eh | mV, con temperatura (`37`) |

Advertencia de cumplimiento: un valor alto de ORAC o DPPH **no autoriza ningún claim de salud**. Es
capacidad antioxidante en tubo de ensayo `[in vitro]` y así se debe presentar (`133`, `267`, `293`).

## Ejemplo aplicado — aceite de CBD con y sin protección

Aceite MCT con CBD, 1 000 mg por frasco de 30 mL, almacenado a 25 °C / 60 % HR, cuantificado por HPLC-UV
228 nm **(ILUSTRATIVO)**:

```
Condición                                   CBD a 0 m   6 m    12 m   Índice de peróxidos 12 m
Vidrio transparente, aire, sin antioxidante   100 %      91 %   79 %        14 meq O2/kg
Vidrio ámbar, aire, sin antioxidante          100 %      96 %   90 %         9 meq O2/kg
Vidrio ámbar, N2 en headspace                 100 %      99 %   96 %         3 meq O2/kg
Vidrio ámbar, N2 + tocoferol 0,05 % p/p       100 %      99 %   98 %       < 2 meq O2/kg
```

Lo que enseña: el salto grande lo dan el ámbar y el nitrógeno —envase y atmósfera—, no el antioxidante.
El tocoferol aporta el último punto y cuesta centavos, pero vender "con antioxidante natural" mientras se
envasa en PET transparente es cobrar por el ingrediente equivocado. Estas curvas se generan con un estudio
de estabilidad real (`164`) y se pueden anticipar con condiciones aceleradas (`165`).

## Errores comunes

- Confiar en el color como control de calidad. Oscurecer y perder potencia son cosas distintas.
- Poner antioxidante y seguir envasando en transparente con aire adentro. Se consume y no alcanza.
- Usar ácido ascórbico en un medio con hierro libre: sin quelante, acelera la oxidación en vez de frenarla.
- Presentar un ORAC alto como beneficio de salud. Es `[in vitro]` y en Colombia es un claim riesgoso (`268`).
- Ignorar el hierro y el cobre que entran por el agua, el molino o el tanque. Se miden por ICP-MS (`88`).
- Hacer el estudio de estabilidad con el frasco lleno hasta el tope y luego vender frascos medio vacíos.
  El espacio de cabeza es parte del experimento.
- Reportar pérdida de activo sin balance de masa. Si el THC bajó, hay que ver si el CBN subió (`06`, `204`).

## Conexión con otros módulos

→ `61-estabilidad-quimica-luz-calor-oxigeno.md` — el módulo dueño de la estabilidad química.
→ `47-oxidacion-y-degradacion-de-productos-naturales.md` — mecanismos orgánicos en detalle.
→ `133-estres-oxidativo-y-antioxidantes.md` — qué significa (y qué no) en el cuerpo.
→ `37-electroquimica-y-electrodos.md` — potencial redox medido con electrodo.
→ `163-envase-primario-y-compatibilidad.md` — el envase como parte de la formulación.
→ `204-estabilidad-y-degradacion-del-thc.md` — el caso THC → CBN con números.
→ `255-estabilidad-y-degradacion-de-psilocibina.md` — el caso de la psilocina que azulea.
