# 173 — Formas ácidas: THCA y CBDA, o por qué la flor cruda casi no tiene THC

Esta es la confusión que más plata cuesta en cannabis. La planta viva **no produce THC**: produce **THCA**,
la forma con grupo carboxilo. El THCA no es psicoactivo por la vía clásica del receptor CB1, y tiene otra
masa molar, otra solubilidad y otra estabilidad. Si compras, vendes, analizas o declaras cannabis sin
distinguir la forma ácida de la neutra, vas a equivocarte en el número que decide la legalidad del lote
(`175`), en el rendimiento de tu extracción y en la dosis de tu producto final.

Términos:
- **forma ácida (acidic form / carboxylated cannabinoid)** = el cannabinoide con –COOH, tal como lo hace la
  planta: THCA, CBDA, CBGA, CBCA.
- **forma neutra (neutral / decarboxylated form)** = sin el –COOH: THC, CBD, CBG, CBC.
- **descarboxilación (decarboxylation)** = perder ese –COOH como CO₂; ver `174`.
- **THCA** = ácido Δ9-tetrahidrocannabinólico, C₂₂H₃₀O₄, **358,47 g/mol**.
- **Δ9-THC** = Δ9-tetrahidrocannabinol, C₂₁H₃₀O₂, **314,46 g/mol**.

## Los cuatro pares que importan

| Forma ácida | Fórmula | Masa molar (g/mol) | Forma neutra | Fórmula | Masa molar (g/mol) | Factor |
|---|---|---|---|---|---|---|
| THCA | C₂₂H₃₀O₄ | 358,47 | Δ9-THC | C₂₁H₃₀O₂ | 314,46 | 0,877 |
| CBDA | C₂₂H₃₀O₄ | 358,47 | CBD | C₂₁H₃₀O₂ | 314,46 | 0,877 |
| CBGA | C₂₂H₃₂O₄ | 360,49 | CBG | C₂₁H₃₂O₂ | 316,48 | 0,878 |
| CBCA | C₂₂H₃₀O₄ | 358,47 | CBC | C₂₁H₃₀O₂ | 314,46 | 0,877 |

Todos pierden exactamente **CO₂ = 44,01 g/mol**. Por eso el factor de conversión de masa ronda 0,877 en
toda la familia pentilo. De dónde sale ese número, con la aritmética completa, está en `175`.

## Qué cambia además de la masa

**Actividad.** El THCA no activa el receptor CB1 de manera apreciable [in vitro]; el Δ9-THC sí es agonista
parcial de CB1 (ver `205`). Por eso la flor cruda comida no produce el efecto de la flor calentada. Esto es
farmacología, no un claim de salud: no se afirma aquí ningún beneficio terapéutico del THCA.

**Polaridad y solubilidad.** El –COOH aporta acidez (pKa reportado en literatura en torno a 3–4 para el
grupo carboxílico de cannabinoides ácidos; verifica la fuente para tu aplicación). Consecuencias reales:

- El THCA es algo más soluble en solventes polares y en medio alcalino que el THC.
- En extracción con etanol frío se arrastran bien las formas ácidas; en extracción con hidrocarburo apolar
  también, pero el reparto cambia con el pH del agua residual (`187`, `188`).
- En cromatografía de fase reversa las formas ácidas eluyen antes o después según el pH del buffer: el
  método debe fijar el pH o los picos se mueven (`81`).

**Estabilidad.** Las formas ácidas se descarboxilan solas con el tiempo, aún a temperatura ambiente. Una
flor bien guardada pierde THCA lentamente; una mal guardada pierde rápido y además oxida el THC a CBN
(`204`). Un COA de hace un año **no describe el material de hoy**.

**Cristalización.** El THCA cristaliza con facilidad y alta pureza — de ahí los "diamantes" de THCA del
mercado estadounidense. Eso también significa que un producto puede declarar "0 % Δ9-THC" y estar hecho casi
enteramente de precursor de THC. Es el corazón del debate regulatorio del THCA (ver `175` y `211`).

## Cómo se mide / cómo se comprueba

**Regla dura: para ver formas ácidas hay que usar HPLC, no GC.**

| Técnica | ¿Distingue ácido de neutro? | Por qué |
|---|---|---|
| HPLC/UHPLC-DAD | **Sí** | No hay calor; los picos de THCA y Δ9-THC se separan |
| LC-MS/MS | **Sí** | Además confirma por transiciones MRM (`83`) |
| GC-FID / GC-MS sin derivatizar | **No** | El inyector (≈250 °C) descarboxila todo: solo ves "THC total" |
| GC con derivatización (sililación) | Sí, con esfuerzo | Requiere derivatizar; ver `64` |

Reporte mínimo aceptable de un COA de potencia: `THCA`, `Δ9-THC`, `Δ8-THC`, `CBDA`, `CBD`, `CBGA`, `CBG`,
`CBN`, `CBC`, cada uno en `% p/p` con la **base declarada** y el método citado. Si el COA solo dice "THC",
pídelo desglosado o no lo uses (`110`, `111`).

## Ejemplo aplicado

Dos flores, mismo comprador, mismo día (ILUSTRATIVO, HPLC-DAD, `% p/p base seca`):

| Muestra | THCA | Δ9-THC | THC total = Δ9 + 0,877×THCA |
|---|---|---|---|
| A (fresca, bien curada) | 22,0 % | 0,8 % | 0,8 + 19,29 = **20,09 %** |
| B (misma genética, 14 meses en bolsa transparente) | 14,5 % | 4,1 % | 4,1 + 12,72 = **16,82 %** |

La muestra B perdió 3,3 puntos de THC total: parte se descarboxiló (y eso se conserva en el cálculo) y
parte se oxidó a CBN, que **no** se recupera. Si compras B como si fuera A, pagas de más. Verifica la cuenta
con `lab-tools/thc_total.py --thca 22.0 --thc 0.8`.

## Errores comunes

- Sumar THCA y Δ9-THC directamente (`22,0 + 0,8 = 22,8 %`). Está mal: sobreestimas ~12 % del THCA.
- Aceptar un COA hecho por GC para declarar contenido de THCA. Físicamente no puede.
- Creer que "flor cruda, THCA, no psicoactivo" describe el producto después de que el consumidor lo caliente.
  Al calentarlo, el THCA se vuelve THC (`174`).
- Comparar un COA de hace meses con material almacenado sin volver a medir.
- Diseñar una extracción para "THC" cuando lo que entra al equipo es THCA, con otra solubilidad y otra
  estabilidad térmica.
- Reportar potencia sin la base: `22 %` en base húmeda con 12 % de humedad es `25 %` en base seca (`07`).

## Conexión con otros módulos

→ `172-biosintesis-de-cannabinoides.md` — por qué la planta produce la forma ácida.
→ `174-descarboxilacion-cinetica-y-calculo.md` — cómo y cuándo se convierte.
→ `175-thc-total-y-el-factor-0877.md` — la aritmética legal completa.
→ `198-analisis-de-potencia-metodo.md` — HPLC vs GC en detalle.
→ `204-estabilidad-y-degradacion-del-thc.md` — la parte que se pierde y no vuelve.
→ `213-como-leer-un-coa-de-cannabis.md` — qué exigir en el documento.