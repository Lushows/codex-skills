# 54 — Aminoácidos, péptidos y proteínas (y por qué el factor 6,25 te miente en hongos)

Las proteínas son el metabolito primario que más se declara y peor se mide en el mundo de los suplementos de
hongos. El método clásico —Kjeldahl— no mide proteína: mide **nitrógeno**, y lo multiplica por un factor.
En hongos, buena parte del nitrógeno viene de la **quitina** de la pared celular, no de proteína. Usar el
factor universal 6,25 sobreestima la proteína de manera sistemática. Además, hay compuestos nitrogenados
que sí importan como activos —ergotioneína, PSK/PSP, enzimas propias— y que no son "proteína cruda". Este
módulo te da la química, los métodos y los factores correctos para no poner un número falso en la etiqueta.

Términos: **aminoácido (amino acid)** = molécula con -NH₂ y -COOH; los 20 proteinogénicos son todos **L**.
**Péptido (peptide)** = cadena corta de aminoácidos (< ~50). **Proteína (protein)** = cadena larga plegada.
**Enlace peptídico (peptide bond)** = amida entre el COOH de uno y el NH₂ del siguiente. **Proteína cruda
(crude protein)** = nitrógeno total × un factor; **no** es proteína medida.

## Química esencial en cuatro puntos

1. **Zwitterión.** A pH fisiológico el aminoácido tiene el -NH₃⁺ y el -COO⁻ a la vez, carga neta cero. El
   pH al que la carga neta es cero es el **punto isoeléctrico (pI)**: allí la proteína es menos soluble y
   precipita. Es la base de la precipitación isoeléctrica en purificación (`22`).
2. **Todos L.** Los aminoácidos proteinogénicos son de configuración L (`43`). Encontrar D-aminoácidos en
   un hidrolizado sugiere racemización por proceso térmico agresivo o adulteración.
3. **Solo tres absorben UV a 280 nm**: triptófano, tirosina y fenilalanina (por su anillo aromático). Por eso
   la lectura A₂₈₀ estima proteína **solo** si conoces su composición. El enlace peptídico absorbe a ~205–220 nm.
4. **Se desnaturalizan.** Calor, pH extremo, solventes y agitación despliegan la proteína. Para una enzima
   eso es pérdida de función; para un aminoácido libre no pasa nada. Importa cuando el activo es una enzima
   o un proteoglicano (`231`).

## El problema del factor: por qué 6,25 no aplica a hongos

```
Kjeldahl / Dumas miden NITRÓGENO TOTAL (% N).
  Proteína cruda (%) = % N × FACTOR

Factor 6,25  ⟸ supone que la proteína promedio tiene 16 % de nitrógeno (1/0,16 = 6,25).
  Válido para carne, leche, huevo. NO para hongos.

En HONGOS: parte del N está en QUITINA (poli-N-acetilglucosamina), ácidos nucleicos, urea, quitosano.
  Factor recomendado en la literatura de composición fúngica: 4,38
  (algunos autores usan 4,17–4,7 según especie y método; declarar SIEMPRE cuál se usó).

Impacto (ILUSTRATIVO): un polvo con 4,80 % de N
  × 6,25 → 30,0 % de "proteína"      ← lo que sale en muchas fichas comerciales
  × 4,38 → 21,0 % de proteína         ← el valor defendible en hongos
  Diferencia: 9 puntos porcentuales, o sea 43 % de sobreestimación relativa.
  ⚠ Verificar esta cuenta en código (`Matematicas_lushows`), nunca de memoria.
```

Consecuencia regulatoria: en Colombia, la información nutricional de la etiqueta debe poder sustentarse
(`272`). Declarar 30 % de proteína con el factor equivocado es un dato que no se sostiene ante una
verificación (`267`).

## Métodos de medición y cuándo usar cada uno

| Método | Qué mide | Unidad | Cuándo |
|---|---|---|---|
| **Kjeldahl** (AOAC 991.20 y afines) | N total por digestión ácida | % N → % proteína cruda | Referencia oficial para etiquetado |
| **Dumas** (combustión) | N total | % N → % proteína cruda | Más rápido, sin ácidos; calibrar contra Kjeldahl |
| Bradford | Se une a Arg y aminoácidos aromáticos | mg/mL vs BSA | Solución; sesgo por composición |
| BCA | Reducción de Cu²⁺ por enlace peptídico | mg/mL vs BSA | Solución; interfiere con reductores |
| A₂₈₀ | Trp + Tyr | mg/mL | Rápido, solo si conoces la proteína |
| **Perfil de aminoácidos** | Cada aminoácido tras hidrólisis | mg/g o g/100 g | El dato REAL; caro |
| SDS-PAGE / SEC | Tamaño y distribución | kDa | Caracterización de proteoglicanos |
| LC-MS/MS de péptidos | Identidad de proteína | — | Autenticidad, proteómica |

```
Perfil de aminoácidos — esquema (ILUSTRATIVO, seguir el método oficial aplicable):
  1. Hidrólisis ácida: HCl 6 M, 110 °C, 24 h, en vial sellado sin oxígeno
     ⚠ Destruye Trp (se hace hidrólisis alcalina aparte) y oxida Cys/Met (se oxidan con ácido perfórmico antes)
  2. Derivatización pre-columna: OPA, AQC o FMOC → los aminoácidos no absorben bien de por sí (`64`)
  3. HPLC con detector de fluorescencia o UV, o UPLC-MS
  4. Cuantificar contra mezcla certificada de aminoácidos + estándar interno (norleucina)
  Reporte: mg de cada aminoácido por g de muestra, base seca, con nota de que Trp/Cys/Met van aparte.
```

## Nitrógeno que sí es activo, y no es "proteína"

| Compuesto | Naturaleza | Por qué importa | Módulo |
|---|---|---|---|
| **Ergotioneína** | Derivado de histidina (betaína tiólica), aminoácido no proteinogénico | Marcador fúngico; se cuantifica por HPLC/LC-MS, no por Kjeldahl | `235` |
| **PSK / PSP** | Proteoglicanos (polisacárido + proteína) de *Trametes versicolor* | El activo es el complejo, no la proteína suelta | `231` |
| Quitina / quitosano | Polisacárido **nitrogenado** | Infla el N total y por eso baja el factor | `52` |
| Nucleósidos (adenosina, cordicepina) | Bases nitrogenadas | Marcadores de *Cordyceps* | `228`, `237` |
| Lectinas | Proteínas que unen azúcares | Termolábiles; interés de investigación [in vitro] | `115` |

Nota de honestidad: para varios de estos compuestos la evidencia de efecto en humanos es limitada o
preliminar. Se describe la química y el método; no se afirma efecto terapéutico (`268`).

## Ejemplo aplicado — corregir la tabla nutricional de un polvo de hongo

```
Dato del laboratorio (ILUSTRATIVO): N total = 4,80 % p/p base seca (Dumas), humedad 6,5 % (KF).

Cálculo correcto:
  Proteína (hongos, factor 4,38) = 4,80 × 4,38 = 21,0 % p/p base seca
  Pasar a base húmeda para etiqueta: 21,0 × (1 − 0,065) = 19,6 % p/p tal cual (`07`)
  Por porción de 2 g: 19,6 % × 2 g = 0,39 g ≈ 0,4 g de proteína por porción

Qué se declara y cómo:
  "Proteína: 0,4 g por porción de 2 g. Determinada como nitrógeno total (Dumas) × 4,38, factor específico
   para hongos por el aporte de nitrógeno no proteico de la quitina."
Qué NO se declara: "alto en proteína" — con 0,4 g por porción no se sostiene ningún descriptor nutricional.
Todos los cálculos ejecutados y verificados en código.
```

## Errores comunes

- Usar 6,25 en hongos e inflar la proteína entre un 30 y un 45 % relativo. Es el error #1 del sector.
- Declarar "aminoácidos esenciales" sin haber corrido un perfil de aminoácidos. Kjeldahl no dice cuáles hay.
- Comparar Bradford entre matrices distintas: el colorante responde según la composición de la proteína.
- Olvidar que la hidrólisis ácida destruye triptófano y por eso el perfil sale incompleto si no se hace aparte.
- Confundir "proteína" con "proteoglicano activo": PSK y PSP no se declaran como proteína cruda.
- Suponer que una enzima sobrevive al secado por aspersión a alta temperatura (`150`).
- Presentar ergotioneína como "aminoácido esencial". No lo es; es un aminoácido no proteinogénico (`235`).

## Conexión con otros módulos

→ `48-metabolitos-primarios-vs-secundarios.md` — dónde encaja la proteína en la composición.
→ `52-polisacaridos-y-glucanos.md` — la quitina y por qué baja el factor.
→ `235-ergotioneina.md` — el compuesto nitrogenado que sí es marcador.
→ `231-cola-de-pavo-trametes-psk-y-psp.md` — proteoglicanos.
→ `272-etiquetado-en-colombia.md` — cómo se declara la información nutricional.