# 194 — Remediación de THC (bajar el THC sin matar el espectro)

"Remediación" es el nombre elegante de un problema muy concreto: tienes un extracto lleno de CBD y
cannabinoides menores que te gusta, pero el THC te lo saca del límite legal del país donde quieres vender.
Remediar es **quitar selectivamente el THC** dejando el resto lo más intacto posible. Es la diferencia entre
un producto **broad spectrum (espectro amplio)** vendible y un lote muerto en bodega. También es donde más
se miente en la industria: mucho "THC-free" que en realidad es "por debajo del LOQ del laboratorio barato
que contraté".

Términos: **full spectrum (espectro completo)** = conserva todos los cannabinoides, incluido THC dentro del
límite legal. **Broad spectrum (espectro amplio)** = se le quitó el THC, conserva los demás.
**THC total (total THC)** = Δ9-THC + (THCA × 0,877), ver `175`. **LOQ (limit of quantitation)** = la
concentración mínima que el método puede *cuantificar* con confianza, ver `73`. **ND (not detected)** = por
debajo del LOD de ese método, no "cero".

## Las técnicas, ordenadas por lo que de verdad hacen

| Técnica | Principio | Selectividad CBD/THC | Pérdida de terpenos | Escala práctica |
|---|---|---|---|---|
| Cromatografía flash preparativa | Adsorción diferencial | Alta | Total (ya no hay terpenos a esta altura) | 0,1–5 kg/lote |
| CPC (partición centrífuga) | Reparto líquido-líquido | Alta | Total | 0,1–10 kg/lote |
| Cristalización de CBD + reconstitución | Solubilidad | Muy alta para CBD puro | Total | kg a toneladas |
| Conversión química de THC (p. ej. a CBN o derivados) | Reacción | Variable | Total | Restringida legalmente |
| Destilación fraccionada fina | Punto de ebullición | Baja (Δ9-THC y CBD hierven muy cerca) | Total | No resuelve sola |

El dato incómodo: **la destilación no separa CBD de THC de forma limpia**. Sus volatilidades son demasiado
parecidas. Quien te venda "remediación por destilación" está, en el mejor de los casos, enriqueciendo un
poco; en el peor, vendiéndote humo. La remediación real es cromatográfica o por cristalización.

## El límite objetivo manda sobre la técnica

Antes de elegir equipo hay que fijar el **límite numérico y su base**, porque cambia todo:

| Destino (a agosto de 2026) | Límite que aplica | Base | Verificar en |
|---|---|---|---|
| EE.UU., definición vigente hasta el cambio | 0,3 % Δ9-THC p/p | Base seca, planta | Farm Bill 2018, 7 U.S.C. §1639o |
| EE.UU., definición nueva (Sección 781, P.L. 119-37) | 0,4 mg de THC total y cannabinoides intoxicantes similares **por envase** | Producto terminado, por envase | Ver `211`; fecha de entrada y aplazamientos |
| Colombia, cannabis no psicoactivo | < 1 % de THC en peso seco, incluidos isómeros, sales y formas ácidas | Peso seco | Decreto 811 de 2021, art. 2.8.11.1.3 |
| UE, alimentos de semilla de cáñamo | 3,0 mg/kg (semilla, harina, proteína) y 7,5 mg/kg (aceite de semilla) de Δ9-THC | Producto | Reg. (UE) 2022/1393, aplicable desde 1-ene-2023 |

Fíjate en la trampa: **el límite de EE.UU. cambia de "porcentaje sobre planta" a "miligramos por envase"**.
Un aceite de 30 mL con 0,05 % p/p de THC total cumple el criterio porcentual y **no** cumple 0,4 mg/envase.
Ese cambio de base es lo que vuelve obsoleta media industria (ver `211`).

## Cómo se mide / cómo se comprueba

La remediación **solo existe si el método analítico puede verlo**. Tres exigencias concretas al laboratorio:

1. **Que el LOQ sea suficientemente bajo para tu límite.** Si tu especificación es "THC total < 0,01 % p/p"
   y el laboratorio tiene un LOQ de 0,05 % por HPLC-DAD, ese laboratorio **no puede** certificarte nada. Ahí
   se necesita LC-MS/MS o GC-MS/MS, con LOQ del orden de µg/g (ver `83`).
2. **Que reporte THC total, no solo Δ9-THC.** Si mides únicamente Δ9 y el producto tiene THCA residual, estás
   subestimando. Fórmula: `THC total = Δ9-THC + 0,877 × THCA` (ver `175`).
3. **Que la unidad coincida con la del límite legal.** % p/p, mg/g y mg por envase no son intercambiables sin
   conocer la masa neta y la densidad. Convierte con `lab-tools/unidades.py`, nunca de cabeza.

```
mg de THC total por envase =
    concentración (mg/g) × masa neta del envase (g)

mg de THC total por envase (producto líquido) =
    concentración (mg/mL) × volumen declarado (mL)
    [y ojo: mg/g ≠ mg/mL si la densidad no es 1,000 g/mL]
```

## Ejemplo aplicado (ILUSTRATIVO)

Extracto de espectro amplio destinado a un aceite de 30 mL, densidad 0,92 g/mL.

- Antes de remediar: THC total 0,28 % p/p → 2,8 mg/g.
- Masa del envase = 30 mL × 0,92 g/mL = 27,6 g.
- THC total por envase = 2,8 mg/g × 27,6 g = 77,3 mg. Muy por encima de 0,4 mg/envase.

Para cumplir 0,4 mg/envase hay que llegar a 0,4 mg / 27,6 g = 0,0145 mg/g = 0,00145 % p/p, es decir
**unos 14,5 µg/g**. Eso está fuera del alcance de un HPLC-DAD de rutina y exige LC-MS/MS. Cifras
**(ILUSTRATIVO)**; el punto que importa es de magnitud: pasar de 2,8 mg/g a 0,015 mg/g es una reducción de
unas 190 veces, no un ajuste fino.

Esa cuenta hay que ejecutarla, no estimarla: rutea a `Matematicas_lushows` o usa `lab-tools/thc_total.py`.

## Lo que se pierde al remediar (y cómo se recupera honestamente)

- **Se pierden terpenos.** Cualquier remediación cromatográfica ocurre después de la destilación, donde los
  terpenos ya se fueron. Si quieres un producto aromático, se **reintroducen** terpenos (de cannabis o
  botánicos) y eso se declara en la etiqueta. Reintroducir y callarlo es adulteración (ver `199`).
- **Se pierden cannabinoides menores.** CBC y CBG suelen salir en fracciones vecinas al THC. Un broad
  spectrum mal hecho termina siendo "aislado de CBD con marketing".
- **Se pierde masa.** Rendimientos de 60–85 % del CBD de entrada son lo esperable en la práctica; pídele al
  proveedor su balance de masa por lote, no su promedio comercial.
- **Se pierde color y se gana costo.** Cada paso adicional de cromatografía aclara el producto pero suma
  solvente, evaporación y tiempo. Si tu cliente compara precios contra un espectro completo sin remediar,
  esa diferencia de costo hay que poder explicarla con el COA en la mano.

Una forma honesta de presentarlo al cliente: **espectro amplio no es "espectro completo sin THC"**, es un
producto distinto con un perfil distinto. Quien venda lo primero como lo segundo va a tener una discusión
incómoda el día que alguien compare los dos COA lado a lado (ver `213`).

## Errores comunes

- **Decir "0 % THC" o "THC-free" en la etiqueta.** Analíticamente no existe el cero. Lo defendible es
  "THC no detectado (< LOD de X µg/g por LC-MS/MS)" con el método al lado (ver `73`, `293`).
- **Certificar con el método equivocado.** Un COA por HPLC-DAD no puede sostener un límite en µg/g. Es el
  error #1 de la remediación: método incapaz de ver lo que se afirma.
- **Cambiar de base sin darse cuenta.** Cumplir 0,3 % sobre planta y creer que se cumple 0,4 mg/envase.
  Son magnitudes distintas de cosas distintas.
- **No medir el subproducto.** La fracción rica en THC que sale de la remediación es material fiscalizado.
  Hay que pesarla, analizarla y documentar su destino.
- **Confiar en un solo lote.** La remediación varía lote a lote; la especificación necesita varios lotes y un
  rango (ver `282`).
- **Usar conversión química para "eliminar" THC sin verificar el marco legal.** Convertir THC en otra cosa
  puede crear un cannabinoide semisintético con su propio problema regulatorio (ver `181`).

## Conexión con otros módulos

→ `175-thc-total-y-el-factor-0877.md` — la aritmética que define si cumples o no.
→ `193-cromatografia-preparativa-y-aislados.md` — el equipo con el que se remedia de verdad.
→ `211-hemp-y-cbd-en-estados-unidos-2026.md` — el cambio de base a mg por envase.
→ `210-cannabis-medicinal-en-colombia.md` — el umbral colombiano de < 1 % en peso seco.
→ `83-lc-ms-ms-y-mrm.md` — la técnica que sí llega a µg/g.
→ `199-analisis-de-perfil-de-terpenos.md` — si reintroduces terpenos, cómo se declara y se comprueba.