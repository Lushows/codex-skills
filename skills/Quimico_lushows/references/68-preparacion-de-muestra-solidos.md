# 68 — Preparación de muestra en sólidos (pesar, secar, disolver, digerir)

Esta es la etapa donde el laboratorio convierte tu polvo o tu flor en un líquido que un instrumento puede
inyectar. Es también donde se pierde analito sin que nadie se dé cuenta: una extracción incompleta te da un
número bajo y perfectamente reproducible, o sea un error invisible. Como comprador, esta es la sección del
método que más debes leer, porque explica por qué dos laboratorios pueden reportar 18 % y 24 % del mismo
material sin que ninguno esté "mintiendo".

Términos:
- **Alícuota de ensayo (test portion)** = la masa exacta que se pesa para el análisis, típicamente 0,1–2 g.
- **Digestión ácida (acid digestion)** = destruir la matriz orgánica con ácido y calor para dejar los metales
  en solución. Se usa antes de ICP-MS o absorción atómica.
- **Extracción exhaustiva (exhaustive extraction)** = extraer hasta que una repetición ya no aporta analito.
- **Efecto de matriz (matrix effect)** = la matriz altera la señal del instrumento, hacia arriba o hacia abajo.
- **Recuperación (recovery)** = qué fracción del analito añadido a propósito se vuelve a encontrar.

## Las cuatro operaciones y para qué sirve cada una

| Operación | Qué logra | Analitos típicos | Riesgo principal |
|---|---|---|---|
| Pesada | Fija la base del cálculo | Todos | Balanza sin calibrar; muestra higroscópica |
| Secado / determinación de humedad | Permite reportar en base seca | Todos | Sobrecalentar y degradar el analito |
| Extracción con solvente | Pasa el analito a solución | Cannabinoides, triterpenos, psilocibina, pesticidas | Extracción incompleta |
| Digestión ácida | Destruye la materia orgánica | Metales pesados | Pérdida de Hg volátil; contaminación del reactivo |

## Pesar: la base de todo el cálculo

```
Concentración del analito en la muestra:

  C_muestra (mg/g) = (C_extracto [mg/mL] x V_extracto [mL] x factor_dilución) / m_muestra [g]

  Ejemplo (ILUSTRATIVO), cannabinoides:
    C_extracto = 0,0412 mg/mL   (leído contra la curva)
    V_extracto = 50 mL
    dilución   = 10x
    m_muestra  = 0,2500 g
    → (0,0412 x 50 x 10) / 0,2500 = 82,4 mg/g = 8,24 % p/p (base tal cual)

  Con humedad 8,0 % p/p, la base seca es:
    8,24 / (1 - 0,080) = 8,96 % p/p base seca
```
Todo cálculo así debe ejecutarse en código, no de memoria: rutea a `Matematicas_lushows` o usa
`lab-tools/unidades.py` y `lab-tools/base_seca.py`.

Detalle que a nadie le importa hasta que importa: **una balanza analítica pesa a 0,1 mg**; pesar 0,25 g con
±0,0001 g aporta 0,04 % de error, despreciable. Pero una muestra higroscópica que gana 2 mg de agua mientras
está en el platillo aporta 0,8 %. Los polvos de hongos y los extractos secos son higroscópicos.

## Secar: el que define la base

Secado a estufa (105 °C hasta peso constante) es el clásico, pero **destruye o volatiliza algunos analitos**:
los terpenos se van, los cannabinoides ácidos se descarboxilan (`174`). Por eso se usan variantes:

| Método | Condición típica | Cuándo usarlo | Cuidado |
|---|---|---|---|
| Estufa gravimétrica | 105 °C hasta peso constante | Materiales estables | Descarboxila THCA, pierde terpenos |
| Estufa suave / vacío | 40–60 °C a vacío | Cannabis, hongos | Más lento |
| Karl Fischer | Titulación específica de agua | Extractos, aceites | Requiere reactivo, ver `98` |
| Balanza halógena | 105 °C, 10–20 min | Control en planta, rápido | Mide "pérdida por secado", no agua pura |

**Pérdida por secado (loss on drying, LOD… ojo con la sigla)** no es lo mismo que contenido de agua: incluye
todo lo volátil. La sigla LOD también significa límite de detección (`73`); en inglés se distingue por
contexto y se escribe completo para evitar el enredo.

## Extraer: donde se pierde el analito en silencio

La extracción se optimiza por solvente, relación muestra:solvente, temperatura, agitación y tiempo. Ejemplos
reales del oficio:

```
Cannabinoides (flor, para HPLC):
  0,200 g de flor molida + 20 mL de metanol o metanol:cloroformo (9:1)
  Agitación/vórtex o ultrasonido 10-20 min a temperatura ambiente
  Centrifugar, filtrar 0,22 µm, diluir e inyectar
  → NO se calienta: el calor descarboxila THCA y falsea el resultado ácido/neutro (79, 174)

Psilocibina y psilocina (hongo, para LC-MS/MS):
  Extracción con metanol acuoso, en frío y sin luz; la psilocina se oxida rápido (255)
  Se recomienda antioxidante y análisis inmediato

Beta-glucano (hongo):
  NO es extracción con solvente: es hidrólisis enzimática controlada (kit tipo Megazyme K-YBGL),
  glucano total menos alfa-glucano; ver 221

Metales (hongo o flor):
  Digestión con HNO3 (+ H2O2) en microondas a alta presión, 180-200 °C
  → matriz orgánica destruida, metales en solución acuosa, ver 88
```
Cómo se demuestra que la extracción fue completa: **extracción repetida**. Se extrae la misma muestra por
segunda y tercera vez y se mide cuánto aparece. Si la segunda extracción rinde más del 2–5 % de la primera,
el método no es exhaustivo y todos tus números están sesgados hacia abajo.

## Cómo se comprueba la preparación

1. **Blanco de reactivos (reagent blank)**: todo el proceso sin muestra. Detecta contaminación del ácido, del
   solvente o del material de vidrio. Imprescindible en metales.
2. **Muestra fortificada (spike / fortified sample)**: se añade una cantidad conocida de analito a la matriz
   y se calcula la recuperación:
   ```
   % recuperación = (C_fortificada - C_muestra) / C_añadida x 100

   Ejemplo (ILUSTRATIVO): muestra 12,0 mg/g ; añadido 4,00 mg/g ; encontrado 15,6 mg/g
   → (15,6 - 12,0) / 4,00 x 100 = 90,0 %
   ```
   Rangos de aceptación habituales: 95–105 % para analitos mayoritarios; 70–120 % para trazas (pesticidas,
   micotoxinas); ver criterios en `74` y `75`.
3. **Duplicado de preparación**: dos alícuotas de la misma muestra preparadas por separado. Mide la
   precisión real, incluyendo la extracción.
4. **Material de referencia certificado (CRM)** de matriz parecida, cuando exista.

## Ejemplo aplicado — dos laboratorios, un mismo polvo de reishi

```
Lab A: extracción acuosa 60 min a 90 °C, reporta "polisacáridos totales 42 %"  (ILUSTRATIVO)
Lab B: hidrólisis enzimática Megazyme, reporta "beta-glucano 18,7 % p/p base seca" (ILUSTRATIVO)

No se contradicen: miden cosas distintas. El 42 % incluye alfa-glucano (almidón del grano
del sustrato). La diferencia 42 - 18,7 es en buena parte el disfraz del micelio en grano (218, 220, 222).
```
Este es el caso donde entender la preparación de muestra te ahorra comprar materia prima fraudulenta.

## Errores comunes

- **Aceptar un % sin saber si es base seca o base tal cual.** Es la ambigüedad más frecuente de un COA (`07`).
- **Calentar la extracción de cannabis.** Convierte THCA en THC durante la preparación y arruina el reporte
  de formas ácidas (`173`, `174`).
- **No filtrar a 0,22 µm antes de inyectar.** Tapona la columna: el laboratorio lo paga, pero el retraso lo
  pagas tú.
- **Digerir metales en material de vidrio no descontaminado.** El vidrio aporta plomo y aluminio; se usa
  PTFE y lavado ácido.
- **Un solo ciclo de extracción sin verificar exhaustividad.** Sesgo sistemático hacia abajo, invisible.
- **Reportar sin blanco ni recuperación.** Sin esos dos controles, el número no es defendible en auditoría.

## Conexión con otros módulos

→ `69-extraccion-para-analisis-spe-y-quechers.md` — limpieza del extracto cuando la matriz estorba.
→ `07-base-seca-vs-humeda.md` — la conversión que decide si tu producto cumple.
→ `74-exactitud-precision-y-recuperacion.md` — cómo se juzgan los spikes.
→ `88-icp-ms-y-metales-pesados.md` — digestión ácida en detalle.
→ `98-karl-fischer-y-humedad.md` — medir agua de verdad.
→ `221-medir-beta-glucanos-metodo-megazyme.md` — el caso donde "extraer" es hidrolizar.