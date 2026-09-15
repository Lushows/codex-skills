# 203 — Micotoxinas y microbiología en cannabis (el riesgo que se ve, se huele y aun así se ignora)

Una flor de cannabis mal secada es un sustrato perfecto para hongos: material vegetal denso, azúcares, humedad
atrapada dentro del cogollo y poca circulación de aire. El problema no es solo estético. Los mohos del género
*Aspergillus* producen **aflatoxinas** y **ocratoxina A**, que son toxinas termoestables: no se destruyen al
fumar ni al hornear un comestible. Y en producto inhalado hay un riesgo adicional que no existe en alimentos:
las **esporas viables** llegando al pulmón, con el peligro concreto de aspergilosis en personas
inmunocomprometidas, que son parte del público del cannabis medicinal.

Términos: **aW (water activity, actividad de agua)** = agua *disponible* para los microorganismos, de 0 a 1;
distinta de la humedad total. **UFC / CFU (colony forming units)** = unidades formadoras de colonia, la
medida del recuento microbiano. **Aflatoxinas (aflatoxins)** = B1, B2, G1, G2, producidas sobre todo por
*Aspergillus flavus* y *A. parasiticus*. **Ocratoxina A (OTA)** = producida por *Aspergillus* y *Penicillium*.
**qPCR** = PCR cuantitativa, detecta ADN de especies diana.

## Humedad no es actividad de agua (y esto salva lotes)

La **humedad** es cuánta agua hay en total. La **actividad de agua** es cuánta está disponible. Un producto
puede tener 12 % de humedad y estar seguro o estar en riesgo, según cómo esté ligada esa agua.

| aW | Qué crece | Zona para cannabis |
|---|---|---|
| > 0,90 | Casi todas las bacterias | Inaceptable |
| 0,80 – 0,90 | Mohos comunes, algunas levaduras | Riesgo alto |
| 0,70 – 0,80 | Mohos xerófilos | Riesgo |
| 0,55 – 0,65 | Prácticamente nada crece | **Zona objetivo de flor curada** |
| < 0,55 | Nada crece | Producto quebradizo, pierde terpenos |

La ventana habitual de la industria para flor curada está en aW 0,55–0,65, que suele corresponder a una
humedad del orden de 10–12 % según la variedad y la densidad del cogollo. **Verifica esa correlación con tu
propio material**: humedad y aW no se convierten una en otra con una fórmula universal, se relacionan por la
isoterma de sorción de cada matriz (ver `35`).

Consecuencia operativa: si controlas aW, controlas microbiología. Es el parámetro de proceso más barato y más
predictivo que existe en el curado.

## Qué se analiza y por qué

| Ensayo | Qué detecta | Técnica | Unidad |
|---|---|---|---|
| Recuento total aerobio (TAMC/TYMC) | Carga bacteriana y de hongos/levaduras | Placa o sistemas rápidos | UFC/g |
| *Aspergillus* patógenos (*flavus, fumigatus, niger, terreus*) | Especies de riesgo respiratorio | qPCR o cultivo selectivo | Presencia/ausencia en 1 g |
| *Salmonella* spp. | Patógeno entérico | Cultivo o qPCR | Ausencia en 25 g |
| *E. coli* / coliformes / STEC | Contaminación fecal | Cultivo o qPCR | UFC/g o ausencia |
| Aflatoxinas B1, B2, G1, G2 | Micotoxina | LC-MS/MS o HPLC-FLD con derivatización | µg/kg (ppb) |
| Ocratoxina A | Micotoxina | LC-MS/MS o HPLC-FLD | µg/kg (ppb) |
| Actividad de agua | Riesgo de crecimiento | Higrómetro de punto de rocío | aW (adimensional) |

Los límites varían por jurisdicción y **a agosto de 2026 no están armonizados internacionalmente**. Las
referencias que se usan: el monográfico de USP Herbal Medicines Compendium para *Cannabis* Species
Inflorescence (versión final autorizada 1.0, 2025), que ofrece dos opciones de ensayo de contaminantes
microbianos; los capítulos generales USP <61>, <62> y <2023> para productos de origen vegetal; las tablas de
cada estado de EE.UU.; y los requisitos de Health Canada. Para alimentos con derivados no psicoactivos en
Colombia aplica la normativa sanitaria de alimentos y lo que el expediente ante INVIMA sustente (ver `210`).
Confirma el texto vigente en la fuente oficial antes de escribirlo en una especificación.

## El debate del cultivo frente a la qPCR

- **Cultivo en placa**: mide lo que crece en ese medio, en esas condiciones. Barato, aceptado históricamente.
  Subestima organismos exigentes y sobreestima cuando hay flora inofensiva.
- **qPCR**: mide ADN de especies diana. Muy sensible y específico. Problema conocido: **detecta ADN de
  organismos muertos**, así que un producto tratado (por ejemplo con radiación o vapor) puede dar positivo sin
  tener nada viable. Se resuelve con qPCR con tratamiento de viabilidad (PMA-qPCR).

Ninguno es "el bueno". Lo que importa es que el COA diga cuál se usó, porque los resultados **no son
comparables entre sí**.

## Tratamientos de descontaminación y su costo químico

| Tratamiento | Efectividad microbiana | Costo químico |
|---|---|---|
| Irradiación gamma o e-beam | Alta | Pérdida de terpenos reportada; posible cambio de perfil |
| Vapor / calor húmedo | Alta | Pérdida de terpenos, riesgo de descarboxilación parcial |
| Ozono | Media | Oxidación de terpenos y cannabinoides |
| Peróxido de hidrógeno vaporizado | Media-alta | Residuo a controlar |
| Radiofrecuencia | Media-alta | Menor pérdida reportada que gamma |

Regla honesta: **la descontaminación mata microorganismos pero no destruye micotoxinas**. Si el lote ya tiene
aflatoxinas, irradiarlo no lo salva; solo esconde la evidencia biológica del problema y deja la toxina. Ese
es el punto que más se malinterpreta en la industria.

## Cómo se mide / cómo se comprueba

1. **Muestreo representativo**: la contaminación fúngica es focal, un cogollo puede estar tomado y el de al
   lado limpio. Muestra compuesta de varios puntos del lote (ver `66`).
2. **aW medida en el producto en su envase final**, no en la muestra suelta del laboratorio.
3. **Micotoxinas por LC-MS/MS** con LOQ del orden de µg/kg y calibración en matriz; la matriz cannabis
   interfiere y exige limpieza (columnas de inmunoafinidad o QuEChERS modificado).
4. **Declarar el método microbiológico** (cultivo, qPCR, PMA-qPCR) y el tamaño de muestra analizada.
5. **Contramuestra guardada** para poder impugnar (ver `112`).

## Ejemplo aplicado (ILUSTRATIVO)

Lote de flor, dos condiciones de curado:

| Parámetro | Curado A (aW 0,58) | Curado B (aW 0,72) |
|---|---|---|
| Humedad | 10,8 % | 13,9 % |
| Recuento total de hongos y levaduras | 1,2 × 10³ UFC/g | 6,8 × 10⁴ UFC/g |
| *Aspergillus flavus* (qPCR) | No detectado en 1 g | Detectado |
| Aflatoxina B1 (LC-MS/MS) | < 0,5 µg/kg (LOQ) | 4,2 µg/kg |
| Terpenos totales | 16,1 mg/g | 18,4 mg/g |

Cifras **(ILUSTRATIVO)**. La tentación comercial es evidente: el lote B huele mejor y tiene más terpenos,
porque conservó humedad. Y es el lote que hay que rechazar. **El aroma y la seguridad microbiológica tiran en
direcciones opuestas**; el punto de equilibrio se define con aW, no con el olfato del jefe de producción.

## Errores comunes

- **Confundir humedad con actividad de agua.** Son cosas distintas y solo una predice crecimiento.
- **Creer que irradiar resuelve micotoxinas.** No las destruye. La toxina es una molécula, no un ser vivo.
- **Comparar resultados de cultivo con resultados de qPCR** como si fueran el mismo ensayo.
- **Curar húmedo para conservar aroma y peso.** El peso extra es agua y la factura llega en el laboratorio.
- **No analizar micotoxinas porque "el moho se ve".** Aflatoxinas pueden estar sin moho visible en el momento
  del análisis, si el hongo creció y luego el material se secó.
- **Analizar solo la flor y olvidar el comestible.** Una gomita con aW alto es un producto microbiológico por
  derecho propio (ver `195`).

## Conexión con otros módulos

→ `35-actividad-de-agua-y-humedad.md` — el parámetro que gobierna todo esto.
→ `100-microbiologia-de-producto.md` — el marco microbiológico general.
→ `101-analisis-de-micotoxinas.md` — la técnica de micotoxinas por dentro.
→ `186-cosecha-secado-y-curado.md` — dónde se gana o se pierde la batalla.
→ `244-micotoxinas-y-contaminacion-en-hongos.md` — el mismo problema en la otra materia prima.
→ `213-como-leer-un-coa-de-cannabis.md` — cómo se lee la sección microbiológica.