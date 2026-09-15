# 37 — Electroquímica y electrodos (los sensores que usas todos los días y casi nadie calibra)

La electroquímica es la rama que convierte una reacción química en una señal eléctrica que puedes leer en
una pantalla. En tu operación aparece disfrazada de cosas cotidianas: el pHmetro, el conductímetro, el
medidor de oxígeno disuelto, el sensor de ORP del tanque, la titulación Karl Fischer que mide humedad, y el
detector electroquímico que un laboratorio puede usar para cuantificar psilocina a trazas. Todas comparten
la misma física, y todas fallan por la misma razón: **electrodos sucios, viejos o mal calibrados**. Un
sensor que nadie verifica es una fuente de datos falsos con apariencia de dato objetivo.

Términos: **celda electroquímica (electrochemical cell)** = sistema de dos electrodos en un electrolito.
**electrodo de trabajo / indicador (working electrode)** = el que responde al analito. **electrodo de
referencia (reference electrode)** = el que mantiene un potencial fijo (Ag/AgCl, calomel). **potenciometría
(potentiometry)** = medir potencial sin que circule corriente apreciable (pH, iones). **voltamperometría /
amperometría (voltammetry / amperometry)** = aplicar potencial y medir la corriente que pasa. **ORP
(oxidation-reduction potential)** = potencial redox del medio, en mV. **conductividad (conductivity)** =
capacidad de la solución de conducir corriente, en µS/cm.

## La ecuación que gobierna la potenciometría

```
Nernst:   E = E° − (R·T / (n·F)) · ln Q

R = 8,314 J/(mol·K) · F = 96 485 C/mol · n = electrones intercambiados · T en kelvin

Para un electrodo de pH a 25 °C:   E = E° − 59,16 mV × pH

Lectura: cada unidad de pH son ~59 mV. Ese "59,16" es la PENDIENTE ideal (slope).
Un electrodo sano da 95–105 % de esa pendiente. Por debajo de 92 %, se reemplaza.
```

Esta es la métrica que casi nadie mira y que decide si tu pHmetro sirve: **la pendiente y el potencial de
asimetría (offset)** que reporta el equipo al calibrar. Un electrodo con pendiente de 85 % puede seguir
dando números creíbles y estar equivocado en 0,3 unidades de pH en los extremos.

Nota de la ecuación: el término R·T/(n·F) lleva **T**. Por eso el pH depende de la temperatura y el
electrodo debe tener compensación automática (ATC). Un pH sin temperatura no es un dato (`22`).

## Los sensores de tu operación, uno por uno

| Sensor | Qué mide | Unidad | Calibración | Falla típica |
|---|---|---|---|---|
| Electrodo de pH (vidrio combinado) | Actividad de H⁺ | pH | 2–3 buffers, el día de uso | Membrana seca o con grasa; unión líquida tapada |
| ORP (Pt vs Ag/AgCl) | Potencial redox del medio | mV (Eh) | Solución patrón de quinhidrona o ZoBell | Superficie de platino envenenada |
| Conductividad | Iones totales | µS/cm | Patrón KCl 1 413 µS/cm | Constante de celda mal fijada |
| Oxígeno disuelto (Clark u óptico) | O₂ en solución | mg/L o % sat. | Aire saturado y cero con sulfito | Membrana rota; electrolito agotado |
| Electrodos selectivos de iones (ISE) | Na⁺, K⁺, Ca²⁺, F⁻, NO₃⁻ | mg/L | Curva con patrones + ajustador de fuerza iónica | Interferencias específicas por ion |
| Karl Fischer culombimétrico | Agua | µg o % p/p | Verificación con patrón de agua certificado | Reactivo agotado; deriva alta (`98`) |
| Detector electroquímico en HPLC | Compuestos oxidables (fenoles, aminas) | nA vs tiempo | Con estándar del analito | Ensuciamiento del electrodo; deriva de línea base |

## Detección electroquímica en análisis: dónde brilla de verdad

Un detector electroquímico (ECD, o coulométrico tipo array) oxida el analito a la salida de la columna y
mide la corriente. Es **muy sensible y muy selectivo** para compuestos fácilmente oxidables: fenoles,
catecoles, indoles, aminas aromáticas, tioles. Justo la familia de:

- **Psilocina**, que tiene un fenol en C4 muy fácil de oxidar — de hecho, esa misma facilidad es la que la
  degrada en el frasco (`255`). Es una técnica reportada como alternativa sensible a LC-MS/MS para
  psilocibina y psilocina en investigación (`256`).
- **Polifenoles** de chaga y otros hongos; también se usa para "índices" de capacidad antioxidante que hay
  que interpretar con cuidado: son `[in vitro]`, no efectos (`133`).
- **Ergotioneína**, por su grupo tiona/tiol (`235`).

Los cannabinoides también son fenoles y responden, pero en la práctica el estándar del sector es HPLC-UV
por robustez y por armonización de métodos (`198`).

Limitación honesta: el ECD es sensible pero **caprichoso**. El electrodo se ensucia con matriz y la
respuesta deriva; exige limpieza frecuente, estándar interno y verificación continua. En un laboratorio
sin disciplina de mantenimiento, un ECD produce peores datos que un UV bien manejado (`77`).

## Cómo se comprueba que el sensor sirve

| Verificación | Cómo | Criterio típico |
|---|---|---|
| Pendiente del electrodo de pH | Leer el reporte de calibración | 95–105 % del teórico; offset dentro de ±30 mV |
| Tiempo de respuesta | Cambiar de buffer y cronometrar la estabilización | < 30 s para llegar a lectura estable |
| Deriva | Dejar en buffer 10 min y registrar | ≤ 0,02 unidades de pH en 10 min |
| Verificación intermedia | Leer un buffer de control a mitad de jornada | Dentro de ±0,05 unidades (`77`) |
| Conductividad | Patrón certificado a T controlada | ±1 % del valor nominal |
| ORP | Solución de referencia | ±15 mV del valor nominal a T declarada |
| Trazabilidad | Buffers y patrones con certificado y fecha de vencimiento | Registro por lote (`70`, `107`) |

Práctica de laboratorio: el electrodo de pH se guarda en solución de KCl 3 M, **nunca en agua destilada**
(el agua lava el electrolito de la unión y arruina la referencia) y **nunca en seco**. Es el error de
cuidado más común y el que más electrodos mata.

## Ejemplo aplicado — el lote que "cambió de pH" y en realidad cambió el electrodo

Tintura hidroalcohólica, control de pH aparente por lote, mismo protocolo **(ILUSTRATIVO)**:

```
Lote   pH aparente reportado   Pendiente del electrodo   Verificación con buffer 4,01   Diagnóstico
 L21           5,12                    99 %                       4,01                  OK
 L22           5,09                    98 %                       4,00                  OK
 L23           4,71                    91 %                       3,88                  Sospechoso
 L24           4,48                    86 %                       3,74                  Electrodo vencido
 L25           5,10                   100 %  (electrodo nuevo)    4,01                  OK, el producto
                                                                                        nunca cambió
```

Lo que enseña: sin registrar la pendiente y sin verificación intermedia con un buffer de control, el
equipo habría abierto una investigación de desviación sobre el proceso de producción (`169`), habría
cambiado la formulación y habría "arreglado" un problema que era del sensor. El registro de la pendiente
en cada calibración cuesta cero pesos y cierra este tipo de casos en un minuto. Es el mismo principio de
las cartas de control aplicado a un instrumento (`77`).

## Errores comunes

- Calibrar el pHmetro "cuando se ve raro". Se calibra el día que se usa, con 2–3 buffers vigentes.
- No registrar pendiente ni offset. Sin eso, no hay forma de saber si el electrodo estaba sano.
- Guardar el electrodo en agua destilada o en seco. Lo daña de forma permanente.
- Medir pH en solventes no acuosos y tratarlo como un pH real. Es un pH aparente (`22`).
- Usar un solo buffer para calibrar. Con uno solo se ajusta el offset, no la pendiente.
- No verificar el sensor de ORP y luego tomar decisiones de antioxidante con datos de mV falsos (`24`).
- Confiar en un detector electroquímico sin estándar interno ni verificación de deriva (`72`, `77`).
- Olvidar la temperatura. Nernst la lleva explícita; los buffers cambian de valor con ella.

## Conexión con otros módulos

→ `22-acidos-bases-y-ph.md` — qué se está midiendo con el electrodo de pH.
→ `23-buffers-y-control-de-ph.md` — los buffers de calibración y de proceso.
→ `24-oxido-reduccion.md` — el potencial redox que el ORP intenta capturar.
→ `98-karl-fischer-y-humedad.md` — titulación electroquímica de agua.
→ `77-control-de-calidad-analitico-y-cartas-control.md` — verificación intermedia de instrumentos.
→ `256-analisis-de-psilocibina-hplc-y-lc-ms.md` — dónde la detección electroquímica compite.
→ `106-analisis-de-agua-y-materias-primas.md` — conductividad como control del agua de proceso.
