# 258 — Farmacocinética de psilocibina (ADME: qué le pasa a la molécula dentro del cuerpo)

La farmacocinética de la psilocibina es, en el fondo, la de un profármaco muy bien diseñado por la
naturaleza: se toma oral, se desfosforila en el tracto digestivo y el hígado, y lo que circula y actúa es la
**psilocina**. Sus números —tiempo al pico, vida media, concentraciones— explican por qué las sesiones de
investigación clínica duran entre 6 y 8 horas y por qué el efecto termina solo, sin intervención.

**Alcance (línea roja):** farmacocinética descriptiva a partir de estudios publicados en humanos, en marco de
investigación supervisada. No es una guía de uso ni de dosificación personal (`259`).

Términos: **ADME** = absorción, distribución, metabolismo, excreción. **Cmax** = concentración plasmática
máxima. **Tmax** = tiempo hasta el Cmax. **t½** = vida media de eliminación. **AUC (area under the curve)** =
exposición total. **glucuronidación (glucuronidation)** = conjugación de fase II que facilita la excreción.

## El recorrido, paso a paso

```
Psilocibina oral
   │ desfosforilación por fosfatasa alcalina intestinal y hepática (rápida y casi completa)
   ▼
PSILOCINA (la activa) ──► circulación ──► cruza la barrera hematoencefálica ──► 5-HT2A cortical
   │
   ├── Fase II: glucuronidación por UGT1A10 (intestino) y UGT1A9 (hígado) → psilocina-O-glucurónido
   │            (la forma mayoritaria en circulación y en orina)
   └── Fase I: monoaminooxidasa (MAO) y aldehído deshidrogenasa → 4-hidroxi-indol-3-il-acetaldehído
                → 4-hidroxi-indol-3-il-ácido acético (4-HIAA) y 4-hidroxitriptofol
Excreción: renal, mayoritariamente como conjugado
```

Detalle importante: **la psilocibina prácticamente no se detecta en plasma** tras dosis oral, porque la
conversión es muy eficiente. Si un método analítico busca psilocibina en sangre, no la va a encontrar; se
mide psilocina total (tras hidrólisis del glucurónido) o psilocina libre, y hay que declarar cuál.

## Los números publicados en humanos

Datos de una revisión sistemática de farmacocinética de psilocibina (2025) y de estudios controlados en
sujetos sanos (Holze et al., *Clinical Pharmacology & Therapeutics*, 2023):

| Parámetro | Valor reportado | Nota |
|---|---|---|
| Tmax de psilocina | ~1,8 – 4 h (mediana ~2 h; RIC 1,9–2,1 h) | Vía oral |
| Cmax de psilocina (dosis 25 mg) | ~17 ng/mL (IC ~16–19) | Holze 2023 |
| Cmax de psilocina (rango entre estudios) | ~8,2 – 37,2 ng/mL (mediana 17; RIC 11,9–23,5) | Depende de dosis y método |
| t½ de eliminación | ~1,2 – 3,3 h (mediana ~2,0 h) | Corta |
| Duración de efectos subjetivos | ~4 – 6 h (sesión clínica 6–8 h) | Concordante con la PK |
| Linealidad dosis-exposición | Aproximadamente proporcional en el rango estudiado | Revisión sistemática 2025 |
| Detectabilidad en plasma | ~6 h post-dosis | Depende del LOQ del método |

```
Regla práctica de la vida media (ILUSTRATIVO, cálculo de libro):
  Con t½ ≈ 2 h, tras 5 vidas medias (≈ 10 h) queda ~3 % de la concentración pico.
  Fracción restante = (1/2)^(t/t½) = (1/2)^(10/2) = 0,03125 → 3,1 %
Ese es el fundamento farmacocinético de que las sesiones clínicas se cierren el mismo día.
Ejecuta cualquier cuenta de este tipo en código (Matematicas_lushows).
```

## Qué modifica la exposición

| Factor | Efecto | Nivel de evidencia |
|---|---|---|
| Comida | Puede retrasar el Tmax; los protocolos clínicos usan ayuno para reducir variabilidad | `[clínico]` de diseño |
| Vía oral vs otras | La oral es la estudiada; otras vías cambian la PK por completo | `[clínico]` |
| ISRS crónicos | Se ha estudiado la interacción; los ensayos suelen exigir retiro previo (`260`) | `[clínico]` |
| IMAO | Interacción farmacológica relevante por la vía MAO | `[mecanicista]` / `[casos]` |
| Función renal o hepática alterada | Afecta conjugación y excreción | `[inferido]`, poco estudiado directamente |
| Polimorfismos de UGT | Fuente plausible de variabilidad interindividual | `[in vitro]` / `[hipótesis]` |
| Peso corporal | Base del debate dosis fija vs mg/kg (`259`) | `[clínico]`, evidencia mixta |

## Cómo se mide / cómo se comprueba

| Elemento | Práctica estándar |
|---|---|
| Matriz | Plasma (EDTA o heparina), orina para excreción |
| Analito | Psilocina libre y psilocina total (tras hidrólisis enzimática del glucurónido con β-glucuronidasa) |
| Técnica | LC-MS/MS en MRM con isotopólogo deuterado como estándar interno (`83`, `256`) |
| LOQ típico | 0,1–1 ng/mL en plasma |
| Estabilidad de la muestra | Crítica: la psilocina se oxida; se recomienda antioxidante y congelación inmediata (`255`) |
| Cálculo | Modelo no compartimental (AUC por trapecios, t½ por regresión de la fase terminal) |
| Software | Validado; y toda cuenta verificada por segunda vía |

Trampa específica: **si no reportas si mediste psilocina libre o total, tus valores no son comparables con
la literatura.** La mayor parte de lo que circula es el glucurónido; libre y total difieren en un factor
grande.

## Ejemplo aplicado (ILUSTRATIVO) — perfil de un participante

```
Estudio de PK, dosis oral única de 25 mg de psilocibina sintética, ayuno, sujeto sano
Muestreo: 0; 0,5; 1; 1,5; 2; 3; 4; 6; 8; 12 h

  t (h)   Psilocina libre (ng/mL)
   0,0     < LOQ
   0,5     4,1
   1,0     11,8
   1,5     15,9
   2,0     17,4   ← Cmax, Tmax = 2,0 h
   3,0     14,2
   4,0      9,6
   6,0      4,3
   8,0      1,8
  12,0    < LOQ

  t½ estimada de la fase terminal ≈ 2,1 h   ·  AUC0-12 calculada por trapecios
```

Esos valores son coherentes con la literatura citada arriba, que es exactamente lo que se busca al validar
un método bioanalítico contra datos publicados.

## Errores comunes

- **Buscar psilocibina en plasma.** Casi no está; la conversión es muy eficiente.
- **No distinguir psilocina libre de total.** Sin eso, los números no se comparan.
- **No estabilizar la muestra.** La psilocina se oxida en el tubo y subestimas todo.
- **Extrapolar la duración del efecto de la t½ sola.** La ocupación del receptor y el efecto no siguen la
  curva plasmática de forma lineal.
- **Asumir que la PK oral aplica a otras vías.** No aplica.
- **Ignorar la variabilidad interindividual** al diseñar un estudio: se necesita n suficiente.

## Conexión con otros módulos

→ `121-farmacocinetica-adme.md` y `122-biodisponibilidad-y-efecto-de-primer-paso.md`.
→ `125-metabolismo-de-fase-ii.md` — glucuronidación por UGT.
→ `126-vida-media-y-regimen-de-dosis.md` y `127-barrera-hematoencefalica.md`.
→ `257-farmacologia-de-la-psilocibina.md` — qué hace cuando llega.
→ `259-dosis-en-investigacion-clinica.md` — dosis fija vs mg/kg.
→ `256-analisis-de-psilocibina-hplc-y-lc-ms.md` — el método bioanalítico.
