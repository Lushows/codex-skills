# 201 — Solventes residuales en cannabis (lo que quedó del proceso, no del cultivo)

Los solventes residuales son el único contaminante del panel que **tú mismo fabricas**. No vienen del suelo
ni de la semilla: vienen de tu extracción y de tu secado. Butano, propano, etanol, heptano, acetona,
isopropanol: lo que uses para sacar cannabinoides tiene que salir después, y lo que no sale queda en el
producto. Es también el ensayo con la mejor noticia del panel, porque el fallo casi siempre se corrige con
proceso —más vacío, más tiempo, más temperatura controlada— y no con equipo nuevo.

Términos: **solvente residual (residual solvent)** = solvente del proceso que queda en el producto
terminado. **Headspace (HS)** = inyectar el vapor del vial en vez del líquido; el modo correcto para
solventes. **Clase de solvente (solvent class)** = clasificación de riesgo de ICH Q3C / USP <467>.
**PDE (permitted daily exposure)** = exposición diaria permitida, en mg/día, de la que se derivan los
límites.

## El marco: ICH Q3C y USP <467>

La referencia técnica universal es la guía **ICH Q3C(R9)** sobre impurezas de solventes residuales, recogida
en el capítulo general **USP <467>**. Clasifica los solventes en tres clases según toxicidad:

| Clase | Definición | Ejemplos relevantes en cannabis | Criterio |
|---|---|---|---|
| Clase 1 | Solventes que se deben evitar: carcinógenos o peligro ambiental | Benceno, 1,2-dicloroetano, tetracloruro de carbono | No usar; límites muy bajos (benceno: 2 ppm en el marco USP <467>) |
| Clase 2 | Uso limitado por toxicidad | Metanol, hexano, acetonitrilo, diclorometano, tolueno | Límite derivado del PDE |
| Clase 3 | Baja toxicidad; PDE ≥ 50 mg/día | Etanol, acetona, isopropanol, acetato de etilo, heptano, pentano | Hasta 5.000 ppm (0,5 %) salvo justificación |

Cuidado: **los mercados de cannabis no siempre usan USP <467>**. Muchos estados de EE.UU. y varias
autoridades tienen su propia tabla de solventes y límites, generalmente más restrictiva para butano y
propano, que USP no contempla porque no son solventes farmacéuticos habituales. A agosto de 2026 no hay
armonización internacional; **verifica la tabla vigente de tu mercado de destino** antes de fijar la
especificación.

El butano y el propano son el caso especial: en listas estatales de EE.UU. se manejan límites del orden de
cientos a miles de ppm, con valores distintos por estado. El dato que importa no es la cifra que recuerdes,
sino de dónde la sacaste y su fecha.

## Por qué se quedan: la física de la cosa

Un solvente sale de un extracto por **evaporación**, y eso depende de tres variables:

```
Velocidad de eliminación ∝  presión de vapor del solvente × área expuesta
                            ────────────────────────────────────────────
                                    espesor de capa × viscosidad
```

De ahí las cuatro palancas reales del purgado (purging):

1. **Vacío**: bajar la presión baja el punto de ebullición efectivo. Es la palanca más potente.
2. **Temperatura**: acelera, pero también degrada cannabinoides y evapora terpenos (ver `204`).
3. **Área y espesor**: una capa delgada purga muchísimo mejor que un bloque. Por eso se usan bandejas.
4. **Tiempo**: la parte final de la curva es asintótica; los últimos cientos de ppm cuestan horas.

El error operativo clásico: subir temperatura porque no se tiene vacío suficiente. Sales del problema de
solventes y entras en el de degradación y pérdida de terpenos.

## Cómo se mide / cómo se comprueba

El método correcto es **GC con muestreo de headspace**, con detector FID o MS:

```
Muestra   → 0,1–0,5 g de extracto pesados en vial de headspace sellado
Diluyente → DMSO, DMF o dimetilacetamida (disuelve el extracto sin volatilizarse)
Equilibrio→ 80–105 °C durante 20–60 min (el solvente pasa al espacio de cabeza)
Inyección → alícuota del vapor
Columna   → capilar tipo DB-624 o equivalente (fase específica para volátiles)
Detección → FID (cuantificación) o MS (identificación + cuantificación)
Calibración → estándares de cada solvente en el mismo diluyente y matriz
```

Tres exigencias no negociables al laboratorio:

1. **Que la lista incluya los solventes que TÚ usas.** Si extraes con butano y el panel del laboratorio no
   trae n-butano ni isobutano, el "cumple" no significa nada.
2. **Que reporte LOQ por analito**, en ppm (µg/g). "No detectado" sin LOQ no es un resultado (ver `73`).
3. **Que use headspace, no inyección líquida directa.** La inyección directa mete todo el extracto en el
   inyector, ensucia el sistema y da resultados irreproducibles.

Un cuarto punto muy práctico: pídele que reporte también los **solventes que no esperabas**. Los perfiles de
GC-MS completos delatan contaminación cruzada de equipo o solventes técnicos de mala calidad (por ejemplo,
benceno como impureza de un butano industrial: eso es un solvente Clase 1 apareciendo sin que nadie lo haya
comprado).

## Ejemplo aplicado (ILUSTRATIVO)

Extracto BHO purgado en horno de vacío, curva de purgado a 35 °C y 29,5 inHg de vacío:

| Tiempo de purgado (h) | n-butano (ppm) | Isobutano (ppm) | Terpenos totales (mg/g) |
|---|---|---|---|
| 0 | 42.000 | 6.100 | 34,0 |
| 12 | 4.800 | 690 | 28,5 |
| 24 | 1.150 | 180 | 24,1 |
| 48 | 380 | 55 | 19,3 |
| 72 | 210 | 31 | 16,8 |

Cifras **(ILUSTRATIVO)**. Dos lecturas: (1) la curva es asintótica — de 24 h a 72 h ganas poco en butano;
(2) **cada hora de purgado cuesta terpenos**. Entre 0 h y 72 h se perdió la mitad del aroma. La decisión de
"cuánto purgar" es un compromiso, y se toma con datos propios, no con la receta de un foro.

## Estrategia de control

- **Elige el solvente pensando en la salida, no solo en la entrada.** El etanol es Clase 3 con límite
  generoso; el hexano es Clase 2 y te obliga a purgar mucho más.
- **Recupera el solvente.** Además de ahorro, un buen sistema de recuperación reduce el residual.
- **Cualifica el grado del solvente.** Butano "de encendedor" trae mercaptanos y a veces benceno. Exige COA
  del solvente y guarda ese documento (ver `284`).
- **Analiza cada lote de extracto**, no cada tanto. El purgado depende del espesor de capa y del operario.
- **Documenta la curva de purgado de tu equipo** una vez y úsala como parámetro de proceso validado (ver
  `168`).

## Errores comunes

- **Purgar por tiempo fijo sin analizar.** "48 horas siempre" ignora que un lote con más ceras purga distinto.
- **Subir temperatura para compensar falta de vacío.** Cambias un problema por otro: isomerización, pérdida
  de terpenos y degradación a CBN (ver `204`).
- **No incluir el solvente de la limpieza del equipo.** El isopropanol de limpiar el material aparece luego
  en el COA y nadie entiende de dónde salió.
- **Confiar en el olfato.** El butano no huele; el mercaptano del butano comercial sí, y desaparece antes que
  el butano.
- **Aceptar "ND" sin LOQ.** El resultado es el LOQ, no la palabra.
- **Usar la tabla de USP <467> cuando el mercado exige la suya.** Terminas cumpliendo una norma que no te
  aplica.

## Conexión con otros módulos

→ `87-solventes-residuales.md` — el marco analítico general y las clases ICH.
→ `86-gc-ms-y-headspace.md` — la técnica por dentro.
→ `188-extraccion-con-hidrocarburos.md` — de dónde salen el butano y el propano.
→ `187-extraccion-con-etanol.md` — el caso del solvente Clase 3.
→ `204-estabilidad-y-degradacion-del-thc.md` — el costo químico de purgar caliente.
→ `213-como-leer-un-coa-de-cannabis.md` — cómo se lee la sección de solventes.