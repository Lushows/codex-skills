# 22 — Ácidos, bases y pH (la perilla que decide qué se extrae y qué se degrada)

El pH es la variable más barata y más olvidada de tu proceso. Mover el pH dos unidades puede cambiar la
solubilidad de un activo diez veces, decidir si tu tintura se pone turbia a los tres meses, o acelerar la
degradación de la psilocibina hasta volver inútil un lote. No cuesta plata: cuesta medirlo y anotarlo.
Casi nadie lo hace, y luego no puede explicar por qué el lote 07 rindió distinto al lote 06 con el mismo
protocolo. Si vas a controlar una sola variable adicional en tu planta, controla esta.

Términos: **ácido (acid)** = especie que cede un protón H⁺ (definición de Brønsted-Lowry). **base (base)** =
especie que lo acepta. **pH** = −log₁₀[H⁺], escala 0–14 en agua a 25 °C, adimensional. **pKa** = pH al cual
un ácido está 50 % ionizado; es una propiedad de la molécula, no del medio. **ionizado (ionized)** = con
carga eléctrica; **neutro / no ionizado (unionized, free base)** = sin carga. **zwitterión (zwitterion)** =
molécula con carga positiva y negativa a la vez, neutra en total.

## La regla que resuelve el 80 % de los casos

```
Ácido (–COOH, fenol):   pH < pKa  →  predomina la forma NEUTRA (más liposoluble)
                        pH > pKa  →  predomina la forma IONIZADA (más hidrosoluble)

Base (amina):           pH < pKa  →  predomina la forma IONIZADA (protonada, hidrosoluble)
                        pH > pKa  →  predomina la forma NEUTRA (free base, liposoluble)

Henderson-Hasselbalch:  pH = pKa + log10( [forma desprotonada] / [forma protonada] )

Fracción ionizada de un ácido:  f_ion = 1 / (1 + 10^(pKa − pH))
```

Dos unidades de pH por debajo del pKa de un ácido lo dejan ~99 % neutro; dos por encima, ~99 % ionizado.
Ese factor 100 es el que mueve tu extracción, tu partición (`30`) y tu absorción intestinal (`122`).

## pKa de lo que te toca (valores reportados en la literatura, verifica para tu matriz)

| Compuesto | Grupo ionizable | pKa aproximado reportado | Consecuencia práctica |
|---|---|---|---|
| THCA / CBDA | –COOH aromático | ~3–4 | A pH neutro están ionizados: más solubles en agua que el THC/CBD neutros |
| Δ9-THC / CBD | Fenol | ~9–10 | Neutros en todo pH de alimento: prácticamente insolubles en agua (`30`) |
| Ácidos ganodéricos | –COOH | ~4–5 | Extracción alcalina suave sube el rendimiento, con riesgo de hidrólisis de ésteres |
| Psilocibina | Fosfato + amina terciaria | ~1,3 (fosfato 1), ~6,5 (fosfato 2), ~10,4 (amina) | Zwitteriónica a pH fisiológico: muy hidrosoluble, casi nada liposoluble |
| Psilocina | Fenol + amina | ~8 (fenol), ~8,5 (amina) | El fenol libre la vuelve muy sensible a oxidación, sobre todo alcalina (`255`) |
| Ergotioneína | Tiol/tiona + carboxilato + amonio cuaternario | zwitteriónica en todo el rango útil | Se queda en la fase acuosa, siempre |
| Ácido oxálico (chaga) | 2 × –COOH | 1,25 y 4,14 | A pH de bebida está como oxalato, y ahí precipita con calcio (`230`) |
| Cafeína, teobromina | Bases muy débiles | < 1 | No las mueves con pH |

## Qué mueve el pH en tu proceso, en concreto

| Efecto | Mecanismo | Dónde lo ves |
|---|---|---|
| Solubilidad del activo | Cambio de forma neutra ↔ ionizada | Extraer THCA en medio alcalino acuoso vs THC en aceite |
| Selectividad de la extracción | Solo lo ionizable responde al pH | Separar ácidos de neutros sin cromatografía (`30`) |
| Velocidad de degradación | Catálisis ácida o básica de hidrólisis y oxidación | Psilocibina y psilocina se van rápido en alcalino (`255`) |
| Isomerización | Ácido de Lewis o de Brønsted promueve Δ9 → Δ8 | Aceites acidificados o con arcillas (`180`) |
| Estabilidad microbiológica | Muchos patógenos no crecen a pH < 4,2 | Bebidas y jarabes (`100`, `156`) |
| Sabor y astringencia | Ácidos libres se perciben ácidos y amargos | Tinturas y jarabes (`162`) |
| Color | Antocianinas y quinonas cambian con pH | Pardeamiento de extractos (`56`, `62`) |

## Qué es y qué no es "pH" en un no acuoso

Aquí se equivoca mucha gente: **el pH solo está definido en soluciones acuosas**. Un aceite MCT con CBD
no tiene pH. Una tintura de etanol 70 % tiene un "pH aparente" que sí se puede medir con electrodo pero
que **no** es comparable a un pH acuoso; se reporta como `pH aparente en EtOH:agua 70:30` y se usa solo
para comparar lotes contra sí mismos. Nunca escribas "pH 5,2" de un aceite en una especificación: es un
dato que ningún laboratorio puede reproducir y te lo van a devolver (`282`).

## Cómo se mide

| Qué | Método | Detalle que importa |
|---|---|---|
| pH de solución acuosa | Potenciometría con electrodo de vidrio combinado | Calibrar con 2–3 buffers que encierren el valor (4,01 / 7,00 / 10,01) el mismo día |
| pH de un sólido o polvo | Suspensión 1:10 p/v en agua tipo II, agitar 5 min, medir | Se reporta como "pH de suspensión al 10 %", nunca como "pH del polvo" |
| pH aparente en hidroalcohólico | Mismo electrodo, resultado marcado como aparente | Solo para comparación intralote |
| Acidez titulable | Titulación con NaOH 0,1 N hasta pH 8,2 | Mide cantidad de ácido, no fuerza; en meq/100 g |
| pKa de un compuesto | Titulación potenciométrica o UV-pH, o valor de literatura | Verifica contra la fuente; los reportados varían |
| Efecto del pH sobre el activo | Estudio de estabilidad forzada a pH 3 / 5 / 7 / 9, HPLC en el tiempo | Es el experimento que decide tu formulación (`164`) |

Regla dura: pH sin temperatura no es un dato. El electrodo debe compensar temperatura (ATC) y el registro
debe decir `pH 5,42 a 22,3 °C`. Un mismo buffer cambia de valor con la temperatura.

## Ejemplo aplicado — separar ácidos ganodéricos de polisacáridos con pH

Extracto acuoso crudo de reishi, se quiere una fracción triterpénica limpia **(ILUSTRATIVO)**:

```
Paso                                   pH    Fase que se lleva el activo
1. Decocción acuosa 95 °C              6,1   β-glucano y ácidos ganodéricos (ionizados) en agua
2. Acidificar con HCl a pH 3,0         3,0   Ácidos ganodéricos pasan a forma neutra
3. Partición con acetato de etilo      3,0   Triterpenos → fase orgánica; glucano se queda en agua
4. Reextraer con NaHCO3 0,5 M          8,2   Triterpenos vuelven a la fase acuosa como sales
5. Reacidificar y filtrar              3,0   Precipitan los triterpenos, se recuperan por filtración

Rendimiento de triterpenos totales recuperados: 71 % (HPLC-UV 252 nm, contra el crudo)
Arrastre de β-glucano a la fracción triterpénica: < 1 % p/p (K-YBGL)
```

Ese ciclo ácido-base es química de primer semestre y hace lo que muchos intentan con columnas caras. Ojo
con el paso 4: los ácidos ganodéricos llevan ésteres acetato que se hidrolizan si te pasas de alcalino o
de tiempo; por eso NaHCO₃ y no NaOH, y por eso frío (`46`, `224`).

## Errores comunes

- No registrar el pH de cada lote. Sin ese dato, una desviación de rendimiento es inexplicable para siempre.
- Calibrar el pHmetro "cada tanto". El electrodo deriva; se calibra el día que se usa, con buffers vigentes.
- Escribir pH de un aceite o de un polvo seco en la especificación. No existe; se mide sobre suspensión.
- Subir el pH para extraer más y no notar que se hidrolizaron los ésteres del activo (`46`).
- Guardar extractos de psilocibina o psilocina en medio neutro-alcalino "porque el ácido daña". Es al
  revés para estas moléculas: lo alcalino y el oxígeno son el problema (`255`).
- Confundir acidez titulable con pH. Un jugo puede tener pH 3,4 y muy poca o mucha acidez total.
- Usar agua destilada vieja o agua de la llave para las suspensiones. El agua debe ser tipo II y su propio
  pH se anota (`106`).

## Conexión con otros módulos

→ `23-buffers-y-control-de-ph.md` — cómo sostener el pH en su sitio, no solo medirlo.
→ `21-equilibrio-quimico.md` — la teoría que hay detrás de Henderson-Hasselbalch.
→ `30-extraccion-liquido-liquido-y-logp.md` — cómo el pH cambia el reparto entre fases.
→ `19-soluciones-y-solubilidad.md` — la otra mitad de la decisión de solvente.
→ `255-estabilidad-y-degradacion-de-psilocibina.md` — el caso donde el pH decide la vida útil.
→ `230-chaga-riesgos-oxalato-y-radiocesio.md` — oxalato y su equilibrio ácido-base.
