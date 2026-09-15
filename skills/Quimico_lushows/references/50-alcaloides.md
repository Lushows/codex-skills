# 50 — Alcaloides (las moléculas con nitrógeno básico: de la cafeína a la psilocibina)

Los alcaloides son metabolitos secundarios que contienen **nitrógeno básico**, casi siempre en un anillo.
Ese nitrógeno lo cambia todo: los hace solubles en agua cuando están protonados y solubles en solvente
orgánico cuando están neutros, los vuelve visibles en LC-MS positivo con sensibilidad excelente, y los hace
farmacológicamente activos a dosis muy bajas, porque se parecen a los neurotransmisores del cuerpo. En
hongos, la familia que importa es la de las **triptaminas indólicas** —psilocibina, psilocina, baeocistina—
y este módulo las cubre como química analítica y farmacología, nunca como producción.

Términos: **alcaloide (alkaloid)** = metabolito con N básico, de origen natural, activo a dosis bajas.
**Base libre (free base)** = forma neutra, sin protonar; soluble en orgánico. **Sal (salt)** = forma
protonada con un contraión; soluble en agua. **Zwitterión (zwitterion)** = molécula con carga + y − al mismo
tiempo, neta cero. **Indol (indole)** = anillo bicíclico benceno+pirrol, el esqueleto del triptófano.

## Clasificación por esqueleto

| Familia | Precursor biosintético | Ejemplos | Dónde |
|---|---|---|---|
| **Indólicos / triptaminas** | Triptófano | Psilocibina, psilocina, baeocistina, serotonina | Hongos, plantas |
| Isoquinolínicos | Tirosina | Morfina, papaverina | Plantas |
| Tropánicos | Ornitina | Atropina, escopolamina, cocaína | Solanáceas, coca |
| Purínicos | Nucleótidos | Cafeína, teobromina | Café, cacao, té |
| Piridínicos | Ácido nicotínico | Nicotina | Tabaco |
| Terpénicos/esteroidales | Vía mevalonato | Solanina, aconitina | Plantas |
| Ergolinas | Triptófano | Alcaloides del cornezuelo | Hongos (*Claviceps*) |

Cannabis no produce alcaloides relevantes: los cannabinoides **no tienen nitrógeno** y no son alcaloides.
Es un error frecuente en textos divulgativos.

## Los alcaloides fúngicos que importan (química, no producción)

| Compuesto | Estructura | Fórmula | M (g/mol) | Nota |
|---|---|---|---|---|
| **Psilocibina** | 4-fosforiloxi-*N*,*N*-dimetiltriptamina | C₁₂H₁₇N₂O₄P | 284,25 | Zwitteriónica; profármaco |
| **Psilocina** | 4-hidroxi-*N*,*N*-dimetiltriptamina | C₁₂H₁₆N₂O | 204,27 | Fenol libre; la forma activa |
| **Baeocistina** | 4-fosforiloxi-*N*-metiltriptamina | C₁₁H₁₅N₂O₄P | 270,22 | Un metilo menos que psilocibina |
| Norbaeocistina | 4-fosforiloxitriptamina | C₁₀H₁₃N₂O₄P | 256,20 | Sin metilos en el N |
| Aeruginascina | *N*,*N*,*N*-trimetil, amonio cuaternario | C₁₃H₁₉N₂O₄P⁺ | 298,28 | Carga permanente |
| Norpsilocina | 4-hidroxi-*N*-metiltriptamina | C₁₁H₁₄N₂O | 190,24 | Análogo desfosforilado de baeocistina |

Puntos que definen todo el trabajo analítico con ellos:

1. **La psilocibina no es quiral** (`43`): no hay discusión de enantiómeros ni columna quiral. Ahorro real.
2. **Es un zwitterión** con el fosfato (pKa₁ ~1,3, pKa₂ ~6,5 reportados en literatura) y el nitrógeno
   dimetilamino (pKa ~6,5). Consecuencia: **retiene malísimo en C18 clásico**. Los métodos usan C18 polar
   embebido, HILIC o pares iónicos (`256`, `81`).
3. **La psilocina es un fenol** y se oxida rápido a los oligómeros azules (`47`). El manejo de muestra exige
   protección de luz, frío, antioxidante y análisis pronto.
4. **La conversión psilocibina → psilocina** ocurre por fosfatasas y por ácido/calor. Un reporte serio
   informa las dos y su suma como psilocibina equivalente (`46`, `255`).
5. **Familia entera, no un compuesto.** Reportar solo psilocibina cuando el material tiene baeocistina
   apreciable subestima el perfil. Métodos modernos corren un panel de 4–6 triptaminas (`252`).

> Alcance de este módulo y de la skill: química, análisis, estabilidad, farmacología, investigación clínica
> y estado legal. **No** se dan procedimientos de cultivo, extracción, purificación ni síntesis para uso
> ilícito, ni formas de evadir controles. En Colombia, a agosto de 2026, la psilocibina está sujeta a control
> de sustancias; cualquier trabajo requiere autorización del Fondo Nacional de Estupefacientes y aval de
> comité de ética institucional. Verificar la norma vigente antes de cualquier gestión (`263`, `289`).

## La química ácido-base: la propiedad más útil de la familia

```
Alcaloide-N (base libre, neutro)  +  H⁺  ⇄  Alcaloide-NH⁺ (catión, sal)

pH bajo  (pH < pKa − 2)  →  PROTONADO  →  se queda en la fase ACUOSA
pH alto  (pH > pKa + 2)  →  NEUTRO     →  pasa a la fase ORGÁNICA

Extracción ácido-base clásica (para ANÁLISIS de laboratorio, `30`):
  1. Acidificar la muestra → los alcaloides pasan a acuoso; lo apolar (grasas, terpenos) se lava con hexano.
  2. Basificar la acuosa   → los alcaloides vuelven a neutro.
  3. Extraer con solvente orgánico → alcaloides limpios.
  ⚠ Para triptaminas 4-hidroxi (psilocina) el paso básico las expone a oxidación: se trabaja frío,
    bajo N₂ y con antioxidante, o se usa SPE de intercambio catiónico en vez de líquido-líquido (`69`).
```

## Cómo se miden

| Objetivo | Técnica | Detalle | Módulo |
|---|---|---|---|
| Cuantificar psilocibina/psilocina | HPLC-DAD 267/280 nm o LC-MS/MS | Curva 5 puntos, estándar interno deuterado si hay | `256` |
| Panel de triptaminas | LC-MS/MS en MRM | Transiciones específicas por compuesto | `83` |
| Screening rápido | HPTLC con revelador (Ehrlich, van Urk) | Cualitativo; el reactivo de Ehrlich da color con indoles | `96` |
| Confirmación de identidad | HRMS + RMN | Fórmula < 5 ppm + estructura | `84`, `94` |
| Alcaloides en GC | Requiere **derivatización** (sililación) | La psilocibina es termolábil y no volátil | `64` |

```
Ejemplo de reporte correcto (ILUSTRATIVO, material seco y molido):
  Psilocibina  6,4 mg/g base seca   (RSD 4,2 %, n=3)
  Psilocina    1,1 mg/g base seca
  Baeocistina  0,3 mg/g base seca
  Suma como psilocibina equivalente: 6,4 + (1,1 × 284,25/204,27) + 0,3 = 8,23 mg/g
  Método: HPLC-DAD 267 nm, columna C18 polar-embedded, buffer fosfato pH 6,0/acetonitrilo,
  patrones certificados, LOQ 0,05 mg/g. Humedad 6,8 % (Karl Fischer) — resultados en base seca.
  ⚠ El factor 1,3915 y la suma se verifican en código, no de memoria (`Matematicas_lushows`).
```

## Ejemplo aplicado — auditar un dato de potencia

Un artículo divulgativo dice "esta especie tiene 1 % de psilocibina". Preguntas obligadas:

1. ¿**Base seca o húmeda**? Con 90 % de humedad en fresco, el mismo material da un número diez veces
   distinto (`07`).
2. ¿**Qué parte**? Sombrero, estípite y micelio tienen contenidos diferentes; la variabilidad entre
   individuos del mismo cultivo es alta y está documentada (`254`).
3. ¿**Método y patrón**? Sin patrón certificado, no hay cuantificación, hay estimación (`70`).
4. ¿**Se midió psilocina también**? Si no, el número puede estar subestimado o sobreestimado según la
   conversión ocurrida.
5. ¿**Cuántas réplicas**? Un valor único sin RSD no es un dato, es una anécdota (`78`).

## Errores comunes

- Confundir psilocibina con psilocina en cotizaciones y patrones: son CAS distintos (`41`).
- Usar C18 clásico y reportar "no detectado" porque el analito salió en el volumen muerto.
- Guardar extractos de psilocina a temperatura ambiente y con luz: se oxida y el resultado baja (`47`).
- Reportar potencia sin humedad: no se puede convertir a base seca ni comparar (`07`).
- Aplicar el reactivo de Ehrlich y llamarlo cuantificación. Es un screening cualitativo de indoles.
- Llamar "alcaloide" a un cannabinoide. No tiene nitrógeno.
- Hablar de dosis fuera del marco de investigación clínica autorizada (`259`, `263`).

## Conexión con otros módulos

→ `251-psilocibina-y-psilocina-quimica.md` — el módulo dueño de la química fina.
→ `252-baeocistina-y-otros-alcaloides-relacionados.md` — el resto de la familia.
→ `256-analisis-de-psilocibina-hplc-y-lc-ms.md` — el método completo.
→ `59-ruta-del-shikimato-y-policetidos.md` — de dónde sale el triptófano precursor.
→ `22-acidos-bases-y-ph.md` y `30-extraccion-liquido-liquido-y-logp.md` — el manejo ácido-base.