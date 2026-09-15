# 179 — THCP, CBDP y los homólogos de cadena larga: potencia real, cantidades minúsculas

En 2019 se describió en *Cannabis sativa* un cannabinoide con cadena de **siete carbonos**: el Δ9-THCP
(tetrahidrocannabiforol). El titular que circuló fue "33 veces más potente que el THC", y desde entonces el
mercado se llenó de productos "con THCP". La química honesta dice dos cosas al tiempo: la afinidad reportada
por CB1 **sí** es mucho mayor, y la cantidad presente en la planta es **minúscula**. Un producto que declara
porcentajes altos de THCP casi con seguridad no lo sacó de una planta. Este módulo te da los números, el
factor de conversión correcto y cómo auditar el reclamo.

Términos:
- **homólogo (homolog)** = misma estructura, distinta longitud de cadena lateral.
- **THCP (Δ9-tetrahydrocannabiphorol)** = C₂₃H₃₄O₂, **342,52 g/mol**; ácido THCPA, C₂₄H₃₄O₄, **386,53 g/mol**.
- **CBDP (cannabidiphorol)** = C₂₃H₃₄O₂, **342,52 g/mol**; ácido CBDPA, **386,53 g/mol**.
- **THCB (tetrahydrocannabutol)** = cadena butilo (C4), C₂₀H₂₈O₂, **300,44 g/mol**.
- **Ki** = constante de inhibición; a menor Ki, mayor afinidad por el receptor.

## La serie completa de cadenas laterales

| Cadena | Carbonos | Neutro | M (g/mol) | Ácido | M (g/mol) | Factor ácido→neutro |
|---|---|---|---|---|---|---|
| Metilo | C1 | THC-C1 (orcinol) | — | — | — | — |
| Propilo | C3 | THCV | 286,41 | THCVA | 330,42 | 0,867 |
| Butilo | C4 | THCB | 300,44 | THCBA | 344,45 | 0,872 |
| **Pentilo** | **C5** | **Δ9-THC** | **314,47** | **THCA** | **358,48** | **0,877** |
| Heptilo | C7 | **THCP** | 342,52 | THCPA | 386,53 | **0,886** |

Comprobación de balance para la serie heptilo: `386,53 − 44,01 = 342,52` ✓

```
THCP total = THCP + 0,886 × THCPA          (NO 0,877)
CBDP total = CBDP + 0,886 × CBDPA
```

## Qué dice la fuente original

Citti et al., *Scientific Reports* (2019), aislaron Δ9-THCP y THCB de una variedad italiana (FM2) y
reportaron:

- **Ki de Δ9-THCP en CB1 ≈ 1,2 nM**, frente a **≈ 40 nM** para Δ9-THC → aproximadamente **33 veces** más
  afinidad [in vitro, ensayo de unión].
- Comportamiento de agonista completo en el ensayo *in vivo* a la misma dosis (10 mg/kg) a la que el THC se
  comporta como agonista parcial [animal].

Y el dato que casi nunca se cita: **las concentraciones en la planta están típicamente en el orden de
décimas de mg/kg a pocos mg/kg** — es decir, trazas cerca del límite de cuantificación de LC-MS/MS. Trabajos
posteriores (*Talanta*, 2021, sobre el contenido de "phorolic acid cannabinoids" en distintas accesiones;
y publicaciones sobre identificación y cuantificación de Δ9-THCP en productos recreativos) confirman que la
presencia natural es muy baja y muy variable.

## La lectura de auditoría

Con esos dos hechos juntos:

1. **Afinidad alta + cantidad ínfima** = el THCP natural de una flor aporta poco al efecto total, que está
   dominado por el THC presente en porcentajes.
2. **Un producto que declara "5 % de THCP"** no puede haberlo obtenido concentrando planta a escala
   razonable. Lo obtuvo por síntesis o lo está declarando mal. Pídele al proveedor el **balance de masa**:
   cuánta biomasa, con qué contenido de THCPA, para producir cuántos gramos (`06`).
3. La potencia mayor **no es una ventaja de seguridad**: significa que errores de dosificación pequeños
   producen efectos grandes. Reportes de centros toxicológicos en EE.UU. han advertido sobre productos con
   THCP por esa razón. Hay **incertidumbre toxicológica** real: no existe base de datos de seguridad crónica
   comparable a la del THC.

No se dan aquí rutas de síntesis ni de conversión. La frontera de esta skill es analizar y auditar, no
producir (ver `181`).

## Cómo se mide / cómo se comprueba

- **Técnica obligatoria: LC-MS/MS** en MRM, o HRMS. El DAD no alcanza: a niveles de `mg/kg` el pico no se ve
  y, si se ve, no se distingue del THC por UV (`83`, `84`).
- **Patrón certificado de THCP**. Sin patrón no hay cuantificación, solo estimación (`70`).
- **Diferencia de masa**: THCP (342,52) vs THC (314,47) = 28 u. Es una firma clara en HRMS; exige el espectro
  y la fórmula elemental calculada con error en ppm.
- **LOQ explícito**, en `mg/kg` o `µg/g`. Este analito vive en el rango de trazas: sin LOQ el resultado no
  es interpretable (`73`).
- **Producto terminado:** si se declara THCP en la etiqueta, la cuantificación tiene que ser por
  `mg/unidad`, validada según ICH Q2(R2) (`75`), y acompañada del perfil completo de cannabinoides.

## Ejemplo aplicado

Un proveedor ofrece "destilado enriquecido, THCP 3,0 % p/p". Su COA de biomasa dice
`THCPA 2,4 mg/kg base seca` (ILUSTRATIVO, LC-MS/MS). Balance de masa para 1 kg de destilado al 3 %:

```
THCP requerido            = 1.000 g × 0,030            = 30 g = 30.000 mg
THCP disponible por kg    = 2,4 mg/kg × 0,886          = 2,13 mg de THCP por kg de biomasa
Biomasa teórica necesaria = 30.000 / 2,13              ≈ 14.085 kg  (14 toneladas)
Con 60 % de recuperación real                          ≈ 23.475 kg  (23 toneladas)
```

Veintitrés toneladas de flor seca para un kilo de destilado, sin contar que ningún proceso separa THCP del
THC con esa selectividad a esa escala. **El reclamo no es plausible.** Se rechaza el proveedor, o se le pide
que declare el origen sintético con su expediente. Ejecuta el balance con `Matematicas_lushows`, no de
memoria.

## Errores comunes

- Usar 0,877 para THCPA. El factor es 0,886.
- Repetir "33 veces más potente" sin decir que es **afinidad in vitro** y que la cantidad natural es de
  trazas. Es media verdad y en etiqueta es engañosa.
- Aceptar cuantificación de THCP por HPLC-DAD. No tiene sensibilidad ni especificidad para el rango real.
- Comprar producto con THCP sin exigir el perfil completo: casi siempre viene acompañado de otros
  semisintéticos no declarados (`181`).
- Suponer estatus legal por analogía con el THC. Varias jurisdicciones han prohibido THCP explícitamente
  (Francia, por ejemplo, vía ANSM). **Verifica país por país, a la fecha** (`265`).
- Tratar "más potente" como "mejor". En toxicología, mayor potencia con menor margen conocido es peor perfil
  de riesgo (`134`).

## Conexión con otros módulos

→ `178-thcv-cbdv-y-varinas.md` — el otro extremo de la serie de cadenas.
→ `175-thc-total-y-el-factor-0877.md` — la lógica del factor, en general.
→ `181-hhc-thco-y-semisinteticos.md` — el ecosistema de productos donde suele aparecer.
→ `83-lc-ms-ms-y-mrm.md` · `84-hrms-qtof-orbitrap-e-identificacion.md` — cómo se confirma de verdad.
→ `134-toxicologia-basica-dosis-y-riesgo.md` — potencia, margen y riesgo.
→ `284-auditoria-de-proveedor.md` — cómo se audita un reclamo imposible.