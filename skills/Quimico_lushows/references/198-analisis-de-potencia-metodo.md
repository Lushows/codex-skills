# 198 — Análisis de potencia: el método (por qué dos laboratorios te dan dos números)

"Potencia" en cannabis significa **cuánto cannabinoide hay**, y es el número del que depende el precio, la
legalidad y la etiqueta. También es el número que más varía entre laboratorios: diferencias del 10–20 % entre
labs para la misma muestra son comunes en estudios de comparación entre laboratorios. Casi nunca es fraude
puro: es método, preparación de muestra, patrón y base de cálculo. Este módulo te da el vocabulario para
preguntarle a un laboratorio exactamente lo correcto y para detectar cuándo el número no puede ser cierto.

Términos: **potencia (potency)** = concentración de cannabinoides, en % p/p o mg/g. **Formas ácidas (acidic
forms)** = THCA, CBDA, tal como están en la planta viva. **HPLC-DAD** = cromatografía líquida con detector de
arreglo de diodos. **GC-FID/GC-MS** = cromatografía de gases; el inyector caliente **descarboxila** las formas
ácidas. **Patrón certificado (certified reference standard)** = sustancia de pureza conocida y trazable.

## La decisión que lo define todo: HPLC o GC

| Aspecto | HPLC-DAD (líquida) | GC-FID / GC-MS (gases) |
|---|---|---|
| Ve formas ácidas | Sí, separadas de las neutras | No: el inyector a 250–300 °C las convierte |
| Reporta | THCA y Δ9-THC por separado | "THC total" ya descarboxilado, sin poder separar el origen |
| Descarboxilación en el inyector | No aplica | Incompleta y variable (típicamente no llega al 100 %) |
| Uso correcto | Potencia de flor, extractos y productos | Terpenos, solventes residuales |
| Veredicto | **Método de referencia para potencia** | No usar solo para potencia si importan las formas ácidas |

Regla operativa: **para potencia, HPLC**. Si un COA de flor te reporta potencia por GC y no separa THCA de
Δ9-THC, ese dato no sirve para decidir cumplimiento legal ni para calcular descarboxilación (ver `174`).
El monográfico de USP Herbal Medicines Compendium para *Cannabis* Species Inflorescence (versión final
autorizada 1.0, publicada en 2025) define el contenido en términos de **THC total y CBD total**, incluyendo
las formas ácidas correspondientes, con criterio de 90–110 % de lo declarado en mg/g; verifica la versión
vigente en usp.org antes de citarla en un expediente.

## Anatomía de un método de potencia por HPLC-DAD

```
Muestra          → flor molida, extracto, o producto terminado
Homogeneización  → molienda criogénica o molino; la flor no es homogénea (ver 67)
Pesada           → 0,1–0,5 g, en balanza analítica de 0,1 mg
Extracción       → metanol, etanol o metanol:cloroformo; sonicación o agitación
Aforo            → volumen exacto, dilución conocida
Filtrado         → 0,22 o 0,45 µm PTFE
Inyección        → 1–10 µL
Columna          → C18, típicamente 100–150 mm, 1,7–3,0 µm
Fase móvil       → agua/acetonitrilo con ácido fórmico o ácido acético (el ácido
                   estabiliza los cannabinoides ácidos y mejora la forma de pico)
Detección        → 220–230 nm (principal) y 270–280 nm (confirmación)
Cuantificación   → curva de calibración de 5–7 puntos contra patrón certificado
Cálculo          → concentración en la solución × factor de dilución / masa de muestra
Corrección       → a base seca si el resultado debe compararse (ver 07)
```

El panel mínimo razonable a agosto de 2026 es de 10–16 analitos: Δ9-THC, THCA, Δ8-THC, CBD, CBDA, CBG, CBGA,
CBN, CBC, CBDV, THCV, y según el mercado también CBNA, CBCA, CBDVA, THCVA y CBL.

## El cálculo, sin trampas

```
Concentración en muestra (mg/g) =
    C_solución (mg/mL) × V_aforo (mL) × factor de dilución
    ─────────────────────────────────────────────────────
                     masa de muestra (g)

% p/p = mg/g ÷ 10

THC total (% p/p) = Δ9-THC (%) + 0,877 × THCA (%)
CBD total (% p/p) = CBD (%)    + 0,877 × CBDA (%)

Corrección a base seca:
% base seca = % base tal cual ÷ (1 − humedad expresada en fracción)
```

El 0,877 es la razón de masas molares (314,5 / 358,5), no una convención comercial (ver `175`). Ejecuta estas
cuentas con `lab-tools/thc_total.py` y `lab-tools/base_seca.py`, o rutea a `Matematicas_lushows`. Nunca de
memoria: aquí un error del 3 % es la diferencia entre legal e ilegal.

## Cómo se mide / cómo se comprueba (qué le exiges al laboratorio)

Pídele estos ocho puntos por escrito. Si un laboratorio no los puede dar, no es un laboratorio, es un
proveedor de PDF:

1. **Técnica y detector**: HPLC-DAD, longitudes de onda usadas.
2. **Lista de analitos** y su LOD/LOQ individual, en % p/p o mg/g (ver `73`).
3. **Origen de los patrones** y su certificado (trazabilidad, ver `70`).
4. **Método de preparación de muestra**, incluida la homogeneización.
5. **Base del resultado**: tal cual o base seca, y el porcentaje de humedad usado.
6. **Validación**: linealidad (R²), exactitud, precisión (%RSD), recuperación, robustez, según ICH Q2(R2)
   (ver `75`).
7. **Acreditación ISO/IEC 17025** con el alcance que incluya potencia en la matriz que le mandas (ver `107`).
   A agosto de 2026, ISO/IEC 17025 es requisito obligatorio para laboratorios de cannabis en la mayoría de
   los mercados regulados de EE.UU.; acreditadores frecuentes son A2LA y ANAB. Verifica el alcance vigente en
   el directorio del organismo acreditador, no en el logo del PDF.
8. **Participación en ensayos de aptitud (proficiency testing)** y su desempeño. Existen materiales de
   referencia del NIST (programa CannaQAP) y requisitos de desempeño del programa AOAC CASP.

## Ejemplo aplicado (ILUSTRATIVO)

Flor analizada por dos laboratorios:

| Dato | Lab A | Lab B |
|---|---|---|
| Δ9-THC | 0,52 % p/p | 0,61 % p/p |
| THCA | 21,4 % p/p | 19,8 % p/p |
| Humedad reportada | 11,2 % | no reporta |
| Base | base seca | tal cual |
| THC total calculado | 0,52 + 0,877×21,4 = **19,29 %** | 0,61 + 0,877×19,8 = **17,97 %** |

Diferencia aparente: 1,32 puntos porcentuales, un 7 % relativo. Pero el resultado de B está en base tal cual.
Llevado a base seca con la humedad de A: 17,97 % ÷ (1 − 0,112) = **20,24 %**. Ahora B queda **por encima** de
A. Cifras **(ILUSTRATIVO)**.

Conclusión práctica: **la mitad de las discusiones de potencia son discusiones de base, no de laboratorio**.
Antes de acusar a nadie, iguala la base (ver `07`).

## Errores comunes

- **Comparar dos COA sin igualar la base.** Es el error #1 y es puramente aritmético.
- **Aceptar potencia por GC en flor.** No puede decirte cuánto THCA había.
- **Muestrear mal.** Una flor no es homogénea: cogollos distintos de la misma planta difieren. La
  representatividad se resuelve en el muestreo, no en el instrumento (ver `66`, `67`).
- **No mirar el LOQ.** "Δ8-THC: ND" con un LOQ de 0,5 % no dice casi nada; con LOQ de 0,01 % dice bastante.
- **Creer que un panel de 4 cannabinoides es suficiente** para un producto que se vende por su perfil.
- **Lab shopping**: mandar la misma muestra a varios laboratorios y publicar el número más alto. A agosto de
  2026 esto está bajo escrutinio regulatorio en mercados maduros de EE.UU. como California y Colorado, con
  requisitos de trazabilidad de muestras (ver `113`).

## Conexión con otros módulos

→ `175-thc-total-y-el-factor-0877.md` — la fórmula y por qué el factor es masa molar.
→ `174-descarboxilacion-cinetica-y-calculo.md` — qué pasa con las formas ácidas al calentar.
→ `79-hplc-y-uhplc.md` — el instrumento por dentro.
→ `75-validacion-de-metodos-ich-q2-r2.md` — qué significa que un método esté validado.
→ `07-base-seca-vs-humeda.md` — la corrección que resuelve la mitad de las discusiones.
→ `213-como-leer-un-coa-de-cannabis.md` — cómo se lee todo esto en el documento real.