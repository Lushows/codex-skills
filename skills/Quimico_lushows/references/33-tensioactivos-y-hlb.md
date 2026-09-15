# 33 — Tensioactivos y HLB (elegir el emulsionante con un número, no con suerte)

Un tensioactivo es la molécula que hace posible meter un cannabinoide con logP 7 dentro de una bebida
transparente. Es lo que se para en la frontera entre el aceite y el agua y baja la tensión que las separa.
La pregunta operativa nunca es "¿le pongo emulsionante?" sino **cuál, cuánto y en qué combinación** — y ahí
existe una herramienta vieja, imperfecta y utilísima: el HLB. Con ella se pasa de probar 30 combinaciones a
probar 4. Además, el tensioactivo es un ingrediente declarable, con límites regulatorios y con sabor: se
elige tanto con química como con cumplimiento.

Términos: **tensioactivo / surfactante (surfactant)** = molécula anfifílica con una parte que ama el agua y
otra que ama la grasa. **tensión superficial / interfacial (surface / interfacial tension)** = energía por
unidad de área de una interfase, en mN/m. **CMC (critical micelle concentration)** = concentración a partir
de la cual el tensioactivo forma micelas. **micela (micelle)** = agregado esférico con las colas apolares
adentro. **HLB (hydrophilic-lipophilic balance)** = escala 0–20 que describe qué tan hidrofílico es un
tensioactivo. **cosolvente / cotensioactivo** = alcohol o poliol que ayuda a formar la película.

## Qué hace exactamente un tensioactivo

```
Tensión interfacial aceite/agua sin tensioactivo:  ~30–50 mN/m
Con un tensioactivo bien elegido:                  ~1–5 mN/m
Con tensioactivo + cotensioactivo (microemulsión): < 0,1 mN/m

Menos tensión = menos energía para crear área nueva = gotas más pequeñas con el mismo equipo.

Además forma una película en la interfase que impide la coalescencia (`32`).
```

Dos trabajos distintos: **bajar la tensión** (facilita formar la gota) y **estabilizar la película**
(impide que se vuelvan a unir). Un tensioactivo puede ser bueno en uno y malo en el otro; por eso casi
siempre se usan mezclas.

## La escala HLB, y cómo se usa de verdad

| HLB | Comportamiento | Aplicación |
|---|---|---|
| 1,5–3 | Antiespumante | Control de espuma en tanques |
| 3–6 | Emulsionante W/O | Cremas y ungüentos (agua en aceite) (`196`) |
| 7–9 | Humectante | Dispersar polvos en agua |
| 8–16 | Emulsionante O/W | **Bebidas y emulsiones de cannabinoides** (`157`) |
| 13–15 | Detergente | Limpieza de equipos (`167`) |
| 15–18 | Solubilizante | Soluciones transparentes, microemulsiones |

```
Regla de mezcla (la que se usa en la práctica):
   HLB_mezcla = Σ ( fracción en peso_i × HLB_i )

Ejemplo: 70 % Tween 80 (HLB 15,0) + 30 % Span 80 (HLB 4,3)
   HLB = 0,70 × 15,0 + 0,30 × 4,3 = 10,5 + 1,29 = 11,79

Cada aceite tiene un "HLB requerido". Se busca el HLB de la mezcla que iguale ese requerido,
y se afina experimentalmente probando 2 unidades arriba y abajo.
```

Honestidad sobre el HLB: es un sistema **empírico de los años 50**, definido originalmente para
tensioactivos no iónicos, y no predice el tamaño de gota ni la estabilidad a largo plazo. Sirve para
acotar el campo de búsqueda, no para reemplazar el experimento. Quien te diga que calculó el HLB y por eso
la fórmula "está lista" no ha hecho el estudio de estabilidad (`164`).

## Tensioactivos usados en nutracéuticos y cannabis

| Tensioactivo | Tipo | HLB aprox. | Notas de uso y cumplimiento |
|---|---|---|---|
| Polisorbato 80 (Tween 80) | No iónico | 15,0 | El caballo de batalla de bebidas; declarable; hay debate sobre su uso en algunos mercados |
| Polisorbato 20 | No iónico | 16,7 | Más hidrofílico; sabor más notorio |
| Span 80 (monooleato de sorbitán) | No iónico | 4,3 | Se mezcla con Tween para ajustar HLB |
| Lecitina (soya, girasol) | Anfótero natural | 4–9 según fracción | "Etiqueta limpia"; alérgeno si es de soya (`137`) |
| Quillaja saponaria (saponinas) | Aniónico natural | ~13–15 | Muy usado en bebidas; sabor amargo perceptible |
| Goma arábiga | Polímero anfifílico | — | Estabiliza por impedimento estérico; dosis alta |
| Sucroésteres | No iónico | 1–16 según grado | Rango amplio de HLB en una sola familia |
| Vitamina E TPGS | No iónico | ~13 | Solubilizante; también inhibe glicoproteína P `[in vitro]` (`159`) |
| Aceite de ricino polietoxilado | No iónico | ~13–14 | Uso farmacéutico; historial de reacciones de hipersensibilidad |
| Monoglicéridos y diglicéridos | No iónico | 3–4 | Aceptación amplia en alimentos |

Advertencia regulatoria: la aceptación de cada tensioactivo **depende del mercado y del tipo de producto**
(alimento, suplemento, cosmético, farmacéutico) y cambia con el tiempo. A agosto de 2026, lo correcto es
verificar el ingrediente contra la norma vigente del país de destino antes de formular, no después
(`266`, `272`, `278`).

## Cómo se mide

| Pregunta | Método | Unidad |
|---|---|---|
| ¿Cuál es la tensión interfacial? | Tensiómetro de anillo Du Noüy, placa de Wilhelmy o gota pendiente | mN/m a T declarada |
| ¿Cuál es la CMC? | Tensión superficial vs log(concentración): el quiebre es la CMC | mM o % p/v |
| ¿Qué HLB necesita mi aceite? | Serie de mezclas Tween/Span de HLB 8 a 16, comparar d50 y estabilidad | HLB requerido, empírico |
| ¿Funcionó la emulsión? | DLS: d50 y PDI; potencial zeta | nm; adimensional; mV (`32`) |
| ¿Cuánto tensioactivo quedó libre? | HPLC-ELSD o LC-MS del tensioactivo | mg/L; importa para etiqueta y sabor |
| ¿Cambia el sabor? | Panel sensorial con umbral de detección | Escala hedónica; umbral en ppm (`162`) |
| ¿Es estable en el tiempo? | Estudio de estabilidad completo, no solo visual | d50, activo, aspecto (`164`) |

## Ejemplo aplicado — nanoemulsión de CBD para bebida: encontrar el HLB

Fase oleosa: aceite MCT con CBD al 10 % p/p. Se busca el HLB requerido probando mezclas Tween 80 / Span 80
a 8 % p/p de tensioactivo total, con microfluidizador a 15 000 psi, 3 pasadas **(ILUSTRATIVO)**:

```
HLB de la mezcla   d50 (nm)   PDI    Aspecto        Separación a 3 meses (25 °C)
      9,0            410      0,48   Lechoso        Anillo visible
     11,0            185      0,31   Opalescente    Ligera turbidez arriba
     12,5             72      0,16   Casi claro     Sin cambio
     13,5             58      0,12   Transparente   Sin cambio
     15,0             94      0,22   Opalescente    Sin cambio

HLB requerido estimado para el MCT + CBD en este sistema: ~13,5
Recuperación de CBD tras el proceso (HPLC-UV 228 nm): 98,2 % del teórico
```

Lecturas: (1) el óptimo no es "más hidrofílico es mejor" — hay un máximo y a HLB 15 empeora; (2) el mismo
equipo y la misma energía dan 410 nm o 58 nm solo cambiando la mezcla de tensioactivos: la química vale más
que la presión; (3) el 8 % de tensioactivo es mucho y hay que verificar su aceptabilidad regulatoria y
sensorial antes de celebrar (`162`, `272`). El siguiente paso es bajar la dosis de tensioactivo manteniendo
d50 < 100 nm, que es donde suele estar el trabajo fino.

## Errores comunes

- Elegir el emulsionante por lo que usa el competidor, sin conocer su aceite ni su equipo.
- Calcular el HLB y saltarse el experimento. El HLB acota, no decide.
- Subir la presión del homogeneizador para arreglar una mala elección química. Gasta energía y calienta
  el producto (con activos termolábiles, lo degrada).
- Ignorar el sabor. Quillaja y polisorbatos se perciben; el consumidor devuelve el producto por sabor,
  no por d50 (`162`).
- No verificar el estatus regulatorio del tensioactivo en el mercado de destino, y descubrirlo en aduana.
- Olvidar que la lecitina de soya es alérgeno declarable (`137`, `272`).
- Suponer que "nanoemulsión" implica más biodisponibilidad sin medirlo. Es plausible y hay evidencia
  `[clínico, limitado]` para algunos sistemas, pero es un claim que exige datos propios (`159`, `122`).

## Conexión con otros módulos

→ `32-coloides-emulsiones-y-espumas.md` — el sistema que el tensioactivo estabiliza.
→ `157-emulsiones-y-nanoemulsiones.md` — el módulo dueño de la formulación en cannabis.
→ `34-reologia-y-viscosidad.md` — la otra palanca de estabilidad.
→ `30-extraccion-liquido-liquido-y-logp.md` — por qué el cannabinoide necesita todo esto.
→ `159-potenciadores-de-biodisponibilidad.md` — qué se puede y qué no se puede afirmar.
→ `160-excipientes-y-compatibilidad.md` — el tensioactivo como excipiente en la fórmula.
→ `272-etiquetado-en-colombia.md` — cómo se declara en la etiqueta.
