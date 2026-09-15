# 175 — THC total y el factor 0,877: la cuenta que decide si tu lote es legal

Este es el cálculo más importante del bloque de cannabis. No es opinión, no es "criterio del laboratorio":
es una relación de masas molares. Aplicarlo mal convierte producto legal en ilegal (y al revés, lo que es
peor). Todo comprador, exportador o formulador de cannabis tiene que saber hacerlo a mano, entenderlo y
después ejecutarlo en código. Aquí está de dónde sale el 0,877, cómo se aplica, y en qué se equivoca la
gente.

Términos:
- **THC total (total THC)** = el THC que tendrías si TODO el THCA se descarboxilara: `Δ9-THC + 0,877 × THCA`.
- **Δ9-THC** = el THC neutro que ya está presente.
- **base seca (dry weight basis)** = resultado corregido por humedad; la base legal en casi todas las normas.
- **incertidumbre de medida, MU (measurement of uncertainty)** = el margen del laboratorio; parte del
  resultado, no un adorno (ver `76`).
- **masa molar (molar mass)** = gramos por mol de la molécula.

## De dónde sale 0,877 — la aritmética completa

La descarboxilación quita exactamente una molécula de CO₂:

```
THCA (C22H30O4)  →  Δ9-THC (C21H30O2)  +  CO2
```

Masas molares (pesos atómicos IUPAC: C = 12,011; H = 1,008; O = 15,999):

```
M(THCA)  = 22×12,011 + 30×1,008 + 4×15,999 = 264,242 + 30,240 + 63,996 = 358,478 g/mol
M(Δ9-THC)= 21×12,011 + 30×1,008 + 2×15,999 = 252,231 + 30,240 + 31,998 = 314,469 g/mol
M(CO2)   =  1×12,011 +  2×15,999                                        =  44,009 g/mol

Comprobación de balance:  358,478 − 44,009 = 314,469  ✓
```

El factor es el cociente de masas molares:

```
f = M(Δ9-THC) / M(THCA) = 314,469 / 358,478 = 0,87723…  →  0,877
```

Es decir: **de cada 100 mg de THCA solo pueden salir 87,7 mg de THC**; los 12,3 mg restantes se van como CO₂
(`44,009 / 358,478 = 12,28 %` de la masa). Muchas normas escriben el factor con masas redondeadas
(`314,5 / 358,5 = 0,87727`); da lo mismo a tres decimales.

El **factor inverso**, para ir de THC a THCA equivalente:

```
1 / 0,877 = 1,1403   →   THCA_equivalente = THC × 1,1403
```

Y ojo: el mismo 0,877 aplica a CBDA→CBD, CBCA→CBC (mismas fórmulas) y ~0,878 a CBGA→CBG. **No se usa 0,877
para THCV/CBDV**: las varinas tienen otras masas molares (ver `178`).

## La fórmula legal

```
THC total (% p/p base seca) = Δ9-THC (%) + 0,877 × THCA (%)
```

En Estados Unidos, `7 CFR 990` (Domestic Hemp Production Program, USDA) define el "acceptable hemp THC
level" sobre THC total en base seca, incorporando la incertidumbre del laboratorio: un resultado se acepta
si `0,3 %` cae dentro del intervalo `medida ± MU`. Verifica el texto vigente en eCFR: la regla es de USDA y
se ha ajustado varias veces.

**A agosto de 2026** hay dos cosas moviéndose que debes verificar antes de decidir nada:

| Jurisdicción | Umbral que se usa | Base | Verificar en |
|---|---|---|---|
| EE.UU. federal (cáñamo en campo) | THC total ≤ 0,3 % | base seca | eCFR 7 CFR 990; USDA AMS FAQ |
| EE.UU. federal (producto consumible) | Se incorporó en la ley de apropiaciones agrícolas del año fiscal 2026 (firmada en noviembre de 2025) un límite de **0,4 mg de THC total por envase**, con entrada en vigor diferida cerca de un año. **Verifica el texto y la fecha efectiva antes de exportar.** | mg/envase | Texto de la ley y guía de FDA/USDA |
| Colombia | Decreto 811 de 2021 y Resolución 227 de 2022 fijan el límite operativo de cannabis **no psicoactivo** en **1 % de THC**, mientras entra en vigencia la reglamentación que toma como referencia 0,3 %. Hay desarrollo normativo posterior (Decreto 1138 de 2025). **Verifica lo vigente con Minsalud/FNE antes de un lote.** | base seca | Gestor Normativo, Función Pública |
| Unión Europea (cáñamo agrícola) | 0,3 % de Δ9-THC para variedades del catálogo (PAC) | base seca | Reglamento vigente; ver `212` |

Nótese la trampa: la UE regula históricamente **Δ9-THC** en el campo, no THC total. Estados Unidos regula
**THC total**. Un mismo lote puede cumplir en un lado y no en el otro con los mismos números.

## Cómo se mide / cómo se comprueba

1. **Método:** HPLC/UHPLC-DAD, que separa THCA de Δ9-THC (ver `173`, `198`). El GC sin derivatizar no sirve
   para este cálculo porque ya te entrega el total mezclado.
2. **Humedad:** medida en la misma muestra (pérdida por secado o Karl Fischer, `98`) para llevar a base seca:
   ```
   valor_base_seca = valor_como_recibido / (1 − humedad_fraccion)
   ```
3. **Incertidumbre:** el COA debe reportar MU. Sin MU no puedes discutir un resultado limítrofe (`76`, `112`).
4. **Muestreo:** el resultado depende de dónde tomaste la muestra tanto como del instrumento (`66`).
5. **Ejecutar en código:**
   ```bash
   python lab-tools/thc_total.py --thca 0.62 --thc 0.05 --humedad 0.08
   python lab-tools/thc_total.py --thca 22.0 --thc 0.8 --limite 0.3
   python lab-tools/thc_total.py --test
   ```

## Ejemplo aplicado

**Caso 1 — cáñamo al filo (ILUSTRATIVO).** COA: `THCA 0,300 %`, `Δ9-THC 0,050 %`, base seca, MU ± 0,04 %.

```
THC total = 0,050 + 0,877 × 0,300 = 0,050 + 0,2631 = 0,3131 % p/p base seca
```

Supera 0,300 %. **Pero** con MU ± 0,04 el intervalo es `0,273 – 0,353`, y 0,300 cae dentro: bajo el criterio
de USDA ese lote entra en "acceptable hemp THC level". Ese matiz vale la cosecha entera — y por eso un COA
sin MU no sirve para defenderte (`112`).

¿Cuánto THCA máximo aguantas con ese Δ9? `(0,300 − 0,050) / 0,877 = 0,285 % de THCA`.

**Caso 2 — corrección de base (ILUSTRATIVO).** Un COA reporta `THC total 20,09 %` **como recibido**, con
humedad 8,0 %.

```
base seca = 20,09 / (1 − 0,080) = 21,84 % p/p base seca
```

Casi dos puntos de diferencia. Comparar ese COA con otro en base seca sin corregir es comparar peras con
manzanas (`07`).

**Caso 3 — mg por envase (ILUSTRATIVO).** Gomas: 20 unidades por frasco, cada una con `5,0 mg` de THC total.

```
THC total por envase = 20 × 5,0 = 100 mg
```

Contra un límite de `0,4 mg/envase`, ese producto está 250 veces por encima. La conversión de unidades es
donde se rompen los proyectos de exportación: `1 % p/p = 10 mg/g`; usa `lab-tools/unidades.py`.

## Errores comunes

- **Sumar THCA + THC sin el factor.** Sobreestimas ~12,3 % del THCA y te sacas del mercado solo.
- **Usar 0,877 sobre THCVA o CBDVA.** Otras masas molares, otro factor (`178`).
- **Ignorar la base.** "0,29 %" en base húmeda puede ser 0,32 % en base seca. La norma pide base seca.
- **Ignorar la MU.** Sin incertidumbre no hay defensa ante un resultado limítrofe, ni derecho a réplica.
- **Aplicar el umbral de un país en otro.** Δ9-THC (UE, campo) ≠ THC total (EE.UU.) ≠ 1 % operativo
  (Colombia a agosto de 2026, verificar).
- **Suponer que "THCA no es THC" comercialmente.** El THCA se convierte al calentar; varias jurisdicciones
  ya cerraron ese vacío exigiendo THC total en producto de venta (`211`).
- **Redondear antes de comparar.** Redondea al final, con las cifras significativas del método (`05`).

## Conexión con otros módulos

→ `173-formas-acidas-thca-y-cbda.md` — las masas molares y por qué existe el factor.
→ `174-descarboxilacion-cinetica-y-calculo.md` — qué tan rápido ocurre en la práctica.
→ `07-base-seca-vs-humeda.md` — la corrección por humedad, paso a paso.
→ `76-incertidumbre-de-medida.md` — qué es la MU y por qué es tu defensa.
→ `112-como-impugnar-un-resultado.md` — qué hacer si el lote sale por encima.
→ `210-cannabis-medicinal-en-colombia.md` · `211-hemp-y-cbd-en-estados-unidos-2026.md` · `212-cannabis-y-cbd-en-europa.md`
→ `194-remediacion-de-thc.md` — qué se puede hacer legalmente con un lote fuera de norma.
