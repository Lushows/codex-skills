# 91 — Métodos colorimétricos y enzimáticos (y el método Megazyme de β-glucano, paso a paso)

Este es el módulo que decide si el negocio de hongos de alguien es honesto o no. Un método **colorimétrico**
mide color; un método **enzimático** usa enzimas específicas para convertir solo el analito que te interesa
en algo medible. La diferencia entre los dos es la diferencia entre "polisacáridos totales" (que incluye el
almidón del grano) y "β-glucano" de verdad. El método enzimático de referencia mundial para hongos es el kit
**Megazyme K-YBGL**, y su lógica es tan simple como brutal: **β-glucano = glucano total − α-glucano**.
Entender esa resta te vacuna contra el fraude más grande del mercado de suplementos de hongos.

Términos: **glucano (glucan)** = polímero de glucosa. **α-glucano (alpha-glucan)** = almidón y glucógeno,
enlaces α; viene del grano y del arroz. **β-glucano (beta-glucan)** = en hongos, cadena 1,3 con ramas 1,6;
es el activo. **GOPOD (glucose oxidase/peroxidase reagent)** = reactivo que convierte glucosa libre en un
color rosado que se lee a 510 nm. **hidrólisis (hydrolysis)** = romper el polímero en sus glucosas.

## Colorimétrico vs enzimático: la diferencia que cuesta plata

| | Colorimétrico clásico | Enzimático (kit) |
|---|---|---|
| Ejemplo | Fenol-sulfúrico, antrona, Folin | Megazyme K-YBGL, K-TSTA (almidón) |
| Qué mide | Cualquier azúcar / cualquier reductor | Solo lo que la enzima corta |
| Especificidad | Baja | Alta (depende de la enzima) |
| Costo por muestra | Muy bajo | Medio |
| Riesgo de inflar | Altísimo | Bajo si se corre completo |
| Sirve para β-glucano de hongo | **No** | **Sí** |

Fenol-sulfúrico y antrona miden **azúcares totales**: cuentan almidón, manitol, trehalosa, quitina
parcialmente hidrolizada y hasta restos de sustrato. Por eso un polvo de micelio sobre arroz puede reportar
"50 % de polisacáridos" con total sinceridad aritmética y ~2 % de β-glucano real
(ver `218-el-fraude-del-micelio-en-grano.md` y `222-polisacaridos-totales-por-que-no-sirve.md`).

## Por qué el kit de β-glucano de CEREALES no sirve para hongos

Hay dos kits Megazyme y se confunden todo el tiempo:

| Kit | Analito | Enzima clave | Matriz |
|---|---|---|---|
| **K-BGLU** (Mixed-Linkage Beta-Glucan) | β-glucano **1,3:1,4** | liquenasa (lichenase) | Avena, cebada, cereales |
| **K-YBGL** (Yeast & Mushroom) | β-glucano **1,3:1,6** | exo-1,3-β-glucanasa + β-glucosidasa | Levadura, hongos, algas |

La liquenasa corta **solo** enlaces β-1,4 adyacentes a un β-1,3. El β-glucano de hongo **no tiene enlaces
1,4**: es 1,3 con ramificaciones 1,6. Resultado: si le corres K-BGLU (o el método oficial de cereales,
AOAC 995.16) a un reishi, te da prácticamente **cero**, no porque no haya β-glucano sino porque la enzima no
lo reconoce. Un COA de hongo que cite "AOAC 995.16" o "mixed-linkage β-glucan" está usando el método
equivocado, y ese solo dato te dice que el laboratorio no sabe lo que está haciendo
(o que sabe demasiado bien lo que está haciendo).

## Megazyme K-YBGL paso a paso

La medición se hace **por diferencia**: dos análisis independientes sobre la misma muestra molida.

### Rama A — Glucano total (β + α)

1. Pesa ~90 mg de muestra molida y homogénea (ver `67-homogeneizacion-y-molienda-de-muestra.md`).
2. **Hidrólisis ácida fuerte en frío** para solubilizar el β-glucano cristalino. Megazyme documenta dos
   variantes según versión del kit: HCl concentrado o **H₂SO₄**. Para *Ganoderma lucidum* y *Poria cocos*
   la ruta con H₂SO₄ dio valores significativamente más altos, es decir, la variante con HCl **subestimaba**
   esos materiales ([Megazyme, nota técnica del kit, consultada a agosto de 2026](https://support.megazyme.com/support/solutions/folders/8000076997)).
3. Dilución con agua y **hidrólisis caliente** (baño hirviendo) para terminar de romper el polímero.
4. Neutralización con KOH y llevado a volumen con buffer de acetato pH ~5.
5. Incubación con **exo-1,3-β-glucanasa + β-glucosidasa** → toda la glucosa liberada.
6. Reacción con **GOPOD** y lectura a **510 nm**.

### Rama B — α-glucano (almidón, glucógeno) + azúcares libres

1. Otra alícuota de la misma muestra, solubilización con KOH 2 M en frío.
2. Buffer de acetato y digestión con **amiloglucosidasa + invertasa** (la invertasa evita que la sacarosa
   se cuente como glucosa).
3. En la versión mejorada del kit se añadió **trehalasa**: sin ella, la trehalosa —azúcar propio de los
   hongos— se contaba de más y **sobreestimaba** el β-glucano final
   ([Megazyme, "Important update to K-YBGL", consultado a agosto de 2026](https://www.megazyme.com/news/important-update-to-the-beta-glucan-assay-kit-yeast-and-mushroom-k-ybgl)).
4. GOPOD y lectura a 510 nm.

### La resta

```
β-glucano (% p/p) = glucano total (% p/p) − α-glucano (% p/p)

Cada rama se calcula así (fórmula tipo Megazyme):

Glucano (%) = ΔA × F × (V/0,1) × (1/1000) × (100/W) × 0,90

ΔA  = absorbancia muestra − absorbancia blanco de reactivo
F   = 100 (µg de glucosa) / absorbancia del estándar de 100 µg de glucosa
V   = volumen final de la dilución (mL)
0,1 = alícuota tomada (mL)
W   = peso de muestra (mg)
0,90 = 162/180, corrección de agua: al hidrolizar, cada anhidroglucosa (162 g/mol)
       se vuelve glucosa libre (180 g/mol). Sin este factor inflas ~11 %.
```

Toda cuenta de estas se ejecuta en código, no de memoria: usa `lab-tools/betaglucano_dosis.py` y rutea a
`Matematicas_lushows` si hay una decisión de plata encima.

### Nota de versión (a agosto de 2026)

Megazyme anunció un kit K-YBGL revisado disponible **desde el 1 de octubre de 2025**, con el tiempo de
reacción reducido de ~7 h a ~4 h 25 min y metodología actualizada que **suele dar valores más altos** en
muestras de hongo ([Megazyme, anuncio del kit mejorado](https://www.megazyme.com/news/introducing-the-new-improved-megazyme-by-neogen-beta-glucan-assay-kit-yeast-and-mushroom)).
Consecuencia práctica: **dos COA del mismo lote pueden diferir por versión del kit**. Exige que el COA diga
la versión y la fecha del método; si comparas proveedores, compáralos con la misma versión.

## Ejemplo aplicado (ILUSTRATIVO)

Polvo de cuerpo fructífero de reishi, lote GL-2608, humedad 5,0 % p/p.

```
Glucano total  : 34,8 % p/p base seca
α-glucano      :  4,1 % p/p base seca
β-glucano      : 30,7 % p/p base seca   ← la resta
Método         : Megazyme K-YBGL (enzimático), versión 2025, hidrólisis H2SO4
Base           : seca (humedad 5,0 % p/p por Karl Fischer, ver 98)
Material       : cuerpo fructífero, sin sustrato
```

El mismo lote reportado por un proveedor con fenol-sulfúrico podría decir "polisacáridos totales 48 %".
No es que uno mienta y el otro no: **miden cosas distintas**. Solo el primero sostiene un claim de β-glucano.
(Cifras ilustrativas; no son un resultado real de BIO-SETA.)

## Errores comunes

- **Aceptar "polisacáridos" como si fuera β-glucano.** Es el disfraz #1 del micelio en grano.
- **Correr solo la rama de glucano total** y llamarlo β-glucano. Sin restar α-glucano, el arroz cuenta.
- **Usar el kit de cereales (liquenasa) en hongos** y concluir "no tiene β-glucano".
- **Olvidar el factor 0,90.** Infla el resultado ~11 % y nadie lo nota en el papel.
- **No declarar la base.** 30 % base húmeda con 8 % de humedad son 32,6 % base seca; en una negociación de
  precio por kilo de activo, esa diferencia es dinero.
- **Comparar COA de versiones distintas del kit** como si fueran el mismo método.
- **Muestreo pobre.** Un polvo mal homogeneizado da 5 puntos de diferencia entre dos tomas (ver `66`, `67`).

## Conexión con otros módulos

→ `221-medir-beta-glucanos-metodo-megazyme.md` — el mismo método visto desde el producto de hongos.
→ `222-polisacaridos-totales-por-que-no-sirve.md` — por qué el ensayo barato no puede sostener el claim.
→ `219-beta-glucanos-quimica-y-estructura.md` / `220-alfa-glucanos-y-almidon-el-confusor.md` — la química.
→ `90-espectroscopia-uv-visible.md` — el detector que lee el color del GOPOD y sus trampas.
→ `07-base-seca-vs-humeda.md` — sin base, el porcentaje no se compara.
→ `110-como-leer-un-coa.md` y `111-banderas-rojas-en-un-coa.md` — cómo auditar el papel que te mandan.
