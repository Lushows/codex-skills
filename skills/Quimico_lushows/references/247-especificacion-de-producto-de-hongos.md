# 247 — Especificación de producto de hongos (el documento que convierte tu producto en un producto)

Una especificación es el contrato técnico de tu producto: qué parámetro se mide, con qué método, cuál es el
límite y cada cuánto se verifica. Sin ella no tienes producto, tienes lotes que se parecen. Con ella puedes
rechazar materia prima, defenderte de un proveedor, sostener una etiqueta ante INVIMA y firmar con un
maquilador sin quedar en sus manos. Este módulo entrega una especificación completa y usable para un
suplemento de hongos, lista para adaptar.

Términos: **especificación (specification)** = tabla de parámetros, métodos y límites de aceptación.
**CoA (certificate of analysis)** = resultado de un lote contra la especificación. **skip-lot** = frecuencia
reducida de ensayo para parámetros históricamente estables. **liberación (release)** = decisión formal de
que el lote puede venderse.

## Las cuatro especificaciones que necesitas

| Nivel | Documento | Quién lo cumple |
|---|---|---|
| 1 | Especificación de materia prima (biomasa/extracto comprado) | Proveedor (`141`, `284`) |
| 2 | Especificación de granel (bulk) — extracto o mezcla en polvo | Tu proceso o el maquilador |
| 3 | Especificación de producto terminado | Tú (`282`) |
| 4 | Especificación de material de envase | Proveedor de envase (`163`) |

Lo que sigue es el nivel 3, que es el que la mayoría no tiene.

## Especificación de producto terminado — cápsulas de extracto de hongo

Producto: cápsulas de 500 mg de extracto seco de cuerpo fructífero. Todos los límites son **(ILUSTRATIVO)**:
se fijan con tus propios datos de 3–5 lotes y con el marco regulatorio de tu país (`282`).

| # | Parámetro | Método (referencia) | Límite de aceptación | Unidad / base | Frecuencia |
|---|---|---|---|---|---|
| 1 | Identidad de especie | ITS PCR-Sanger + filogenia | Coincide con la especie declarada, ≥ 99 % identidad | — | Cada lote de MP |
| 2 | Identidad química (huella) | HPTLC o FTIR contra patrón de referencia | Perfil concordante con el estándar interno | — | Cada lote |
| 3 | Aspecto | Visual | Polvo café claro a café oscuro, libre de partículas extrañas | — | Cada lote |
| 4 | Olor y sabor | Sensorial descriptivo | Característico, sin notas rancias | — | Cada lote |
| 5 | Humedad | Pérdida por secado 105 °C o Karl Fischer | ≤ 8,0 | % p/p | Cada lote |
| 6 | Actividad de agua | Punto de rocío | ≤ 0,60 | aw | Cada lote |
| 7 | Cenizas totales | Gravimetría 550 °C | ≤ 8,0 | % p/p b.s. | Skip-lot (1 de 5) |
| 8 | **β-glucano** | Megazyme K-YBGL (enzimático) | ≥ 25,0 | % p/p base seca | **Cada lote** |
| 9 | **α-glucano** | Megazyme K-YBGL (por diferencia) | ≤ 8,0 | % p/p base seca | **Cada lote** |
| 10 | Marcador específico (ej. triterpenos totales en reishi) | HPLC-DAD 252 nm, patrón ác. ganodérico A | ≥ 8,0 | mg/g b.s. | Cada lote |
| 11 | Ergosterol (opcional, marcador de biomasa fúngica) | HPLC-UV 282 nm | Informativo, registrar | mg/g b.s. | Skip-lot |
| 12 | Peso promedio de cápsula | Balanza analítica, n = 20 | 500 mg ± 7,5 % | mg | Cada lote |
| 13 | Uniformidad de contenido/masa | USP <905> | Cumple criterio USP | — | Cada lote |
| 14 | Desintegración | USP <2040> / <701> | ≤ 30 | minutos | Cada lote |
| 15 | Plomo (Pb) | ICP-MS previa digestión ácida | ≤ 1,0 | mg/kg b.s. | Cada lote |
| 16 | Cadmio (Cd) | ICP-MS | ≤ 0,5 | mg/kg b.s. | Cada lote |
| 17 | Arsénico total (As) | ICP-MS (especiar si supera) | ≤ 1,0 | mg/kg b.s. | Cada lote |
| 18 | Mercurio (Hg) | ICP-MS o analizador directo | ≤ 0,2 | mg/kg b.s. | Cada lote |
| 19 | Aflatoxinas totales (B1+B2+G1+G2) | LC-MS/MS (MRM) | ≤ 4,0 | µg/kg | Cada lote |
| 20 | Aflatoxina B1 | LC-MS/MS | ≤ 2,0 | µg/kg | Cada lote |
| 21 | Ocratoxina A | LC-MS/MS | ≤ 2,0 | µg/kg | Skip-lot (1 de 3) |
| 22 | Aerobios mesófilos totales | ISO 4833 / USP <61> | ≤ 1 × 10⁴ | UFC/g | Cada lote |
| 23 | Mohos y levaduras | ISO 21527 (criterio pactado por matriz fúngica) | ≤ 1 × 10³ | UFC/g | Cada lote |
| 24 | *E. coli* | ISO 16649 | Ausencia | en 1 g | Cada lote |
| 25 | *Salmonella* spp. | ISO 6579 | Ausencia | en 25 g | Cada lote |
| 26 | *S. aureus* | ISO 6888 | ≤ 1 × 10² | UFC/g | Skip-lot |
| 27 | Etanol residual (si hubo extracción alcohólica) | GC-headspace | ≤ 5000 | ppm (ICH Q3C clase 3) | Cada lote con etanol |
| 28 | Pesticidas multiresiduo | LC-MS/MS + GC-MS/MS | Cumple el marco aplicable | mg/kg | Anual o por cambio de proveedor |
| 29 | Alérgenos (si aplica el sustrato) | ELISA | Ausencia declarada | — | Por cambio de proveedor |
| 30 | Estabilidad (vida útil) | ICH Q1A, tiempo real + acelerado | β-glucano ≥ 90 % del valor inicial a 24 meses | % del inicial | Programa anual |

Nota crítica sobre el parámetro 8: el límite se declara **en base seca y con el método nombrado**. "≥ 25 %
de beta-glucanos" sin decir Megazyme y sin decir base seca es una frase publicitaria, no una especificación.

## Cómo se fijan los límites (no se inventan)

```
Procedimiento:
1. Analiza 3–5 lotes reales del proveedor con el método definitivo.
2. Calcula media y desviación estándar (s) de cada parámetro.
3. Límite tentativo para un mínimo:  media − 3s   (redondeado hacia abajo, cifra "vendible")
4. Contrasta contra: (a) el marco regulatorio, (b) lo que dice tu etiqueta, (c) lo que el proveedor
   puede sostener comercialmente.
5. El límite final es el MÁS EXIGENTE de esos tres. Nunca al revés.
6. Documenta la justificación. Un límite sin justificación no sobrevive una auditoría.

Ejemplo (ILUSTRATIVO): β-glucano en 5 lotes = 29,8 / 31,2 / 28,4 / 30,6 / 29,1 % b.s.
  media = 29,82 ; s = 1,08 ; media − 3s = 26,6  → límite declarado ≥ 25,0 % b.s.
  (Ejecuta la estadística en código, no de memoria — Matematicas_lushows.)
```

## Cómo se usa en la vida real

- **En el contrato de compra:** la especificación es un anexo firmado. Sin eso no hay incumplimiento que
  reclamar (`292`).
- **En la recepción:** ningún lote entra a producción sin COA conforme + verificación tuya de al menos
  identidad y glucanos.
- **En la liberación:** una persona nombrada firma la liberación contra la especificación (`283`).
- **En la etiqueta:** solo se declara lo que la especificación garantiza como mínimo, con sobredosificación
  calculada si el activo decae en vida útil (`164`).
- **En una inspección:** especificación + registros de lote + COA es exactamente lo que piden (`286`).

## Errores comunes

- **Copiar la especificación del proveedor.** Está escrita para que él siempre cumpla.
- **Fijar el límite igual al valor típico.** La mitad de tus lotes fallará; deja margen estadístico.
- **Declarar en la etiqueta más de lo que la especificación garantiza al final de la vida útil.**
- **No definir frecuencia.** Un parámetro sin frecuencia no se mide nunca.
- **Olvidar la base.** Base seca y base húmeda cambian el veredicto de un lote.
- **No tener plan para el fuera de especificación (OOS).** Hay que definir de antemano quién investiga, cómo
  se re-muestrea y cuándo se rechaza (`169`, `112`).

## Conexión con otros módulos

→ `282-especificacion-de-producto-terminado.md` — el marco general para cualquier producto.
→ `283-plan-de-control-de-calidad-por-lote.md` — la operación de esta tabla.
→ `141-especificacion-de-materia-prima.md` — el nivel 1.
→ `243-metales-pesados-en-hongos.md`, `244-micotoxinas-y-contaminacion-en-hongos.md`, `245-identidad-de-especie-por-its.md`
→ `164-estabilidad-ich-q1-y-vida-util.md` — de dónde sale el parámetro 30.
→ `266-invima-y-suplementos-dietarios.md` — qué exige Colombia en el expediente.