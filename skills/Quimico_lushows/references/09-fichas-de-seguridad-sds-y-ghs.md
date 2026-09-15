# 09 — Fichas de seguridad (SDS) y GHS (cómo leer el papel que viene con cada sustancia)

Cada sustancia química que compras debe llegar con una ficha de datos de seguridad. Ese documento no
es burocracia: contiene, en un orden fijo y universal, el punto de inflamación, la toxicidad, los
incompatibles, qué hacer si se derrama y qué EPP se necesita. Aprender a leerlo toma veinte minutos y
te da autonomía: dejas de preguntar "¿esto es peligroso?" y empiezas a leer la sección 9 y la 10.
También te sirve al revés: si vas a vender un ingrediente a otra empresa, o exportarlo, te van a pedir
tu SDS, y una SDS mal hecha frena un embarque.

Términos: **SDS (safety data sheet)** = ficha de datos de seguridad; en español a veces FDS, y el
formato viejo se llamaba MSDS. **GHS (Globally Harmonized System)** = sistema mundialmente armonizado
de clasificación y etiquetado de productos químicos. **pictograma (pictogram)** = el rombo rojo con el
símbolo. **frase H (hazard statement)** = indicación de peligro, tipo H225. **frase P (precautionary
statement)** = consejo de prudencia, tipo P210. **CAS (CAS number)** = identificador único de una
sustancia química.

## Las 16 secciones de una SDS y para qué sirve cada una

| Sección | Contenido | Cuándo la usas |
|---|---|---|
| 1 | Identificación del producto y del proveedor | Verificar que la SDS es del producto exacto |
| 2 | Identificación de peligros (pictogramas, H y P) | Decisión rápida de riesgo |
| 3 | Composición / CAS | Saber qué es realmente y buscar más datos |
| 4 | Primeros auxilios | Antes de que pase algo, no después |
| 5 | Lucha contra incendios | Qué extintor, qué NO usar (agua a veces empeora) |
| 6 | Derrame accidental | Arma tu kit de derrames con esto |
| 7 | Manipulación y almacenamiento | Temperatura, incompatibles, ventilación |
| 8 | Controles de exposición / EPP | Límites ocupacionales y protección concreta |
| 9 | Propiedades fisicoquímicas | Punto de inflamación, densidad de vapor, solubilidad |
| 10 | Estabilidad y reactividad | **Incompatibles**: la sección que evita explosiones |
| 11 | Información toxicológica | DL50, órgano diana, sensibilización |
| 12 | Información ecológica | Vertidos, biodegradabilidad |
| 13 | Eliminación | Cómo se descarta legalmente |
| 14 | Transporte | Número UN, clase; lo pide el transportador |
| 15 | Información reglamentaria | Controles, restricciones |
| 16 | Otra información | Fecha de revisión: **verifícala siempre** |

Las que más vas a leer en la vida real: **2, 5, 7, 8, 9, 10 y 14**.

## Los pictogramas GHS que verás en este oficio

| Pictograma | Significa | Ejemplo frecuente |
|---|---|---|
| Llama | Inflamable | Etanol, isopropanol, acetona, hexano |
| Calavera | Toxicidad aguda | Metanol, acetonitrilo (en el laboratorio) |
| Signo de exclamación | Irritante, nocivo, sensibilizante | Muchos solventes y polvos |
| Corrosión | Corrosivo para piel y metales | Ácido clorhídrico, hidróxido de sodio |
| Peligro para la salud | Carcinogenicidad, mutagenicidad, sensibilización respiratoria | Hexano (neurotoxicidad), algunos reactivos |
| Llama sobre círculo | Comburente / oxidante | Peróxidos, percloratos |
| Bombona de gas | Gas a presión | Butano, propano, nitrógeno, CO2 |
| Árbol y pez | Peligroso para el medio ambiente | Varios solventes y pesticidas |

Frases H más comunes en una planta de extractos: **H225** (líquido y vapor muy inflamables),
**H319** (irritación ocular grave), **H336** (somnolencia o vértigo), **H315** (irritación cutánea).

## Cómo se comprueba que una SDS sirve

```
[ ] ¿Es del producto EXACTO (mismo proveedor, mismo grado, mismo CAS)?
[ ] ¿Está en español? En Colombia, la información de seguridad debe estar en el idioma del trabajador.
[ ] ¿Tiene fecha de revisión reciente? Una SDS de hace 12 años es sospechosa.
[ ] ¿Tiene las 16 secciones? Un PDF de 2 páginas no es una SDS.
[ ] ¿La sección 10 lista los incompatibles con nombre?
[ ] ¿La sección 8 da límites de exposición ocupacional concretos?
[ ] ¿La sección 14 trae número UN y clase, si aplica a transporte?
```

Si el proveedor no puede darte una SDS completa de lo que te vende, esa es información sobre el
proveedor, no solo sobre la sustancia (ver `284`).

## Tu propia SDS: cuándo te toca hacerla

Si vendes un ingrediente a granel, un extracto a otra empresa o exportas, te van a pedir SDS. Un
producto terminado de consumo (una cápsula, una tintura para consumidor final) normalmente no la
requiere, pero un extracto en polvo vendido B2B sí. Necesitas: composición, datos fisicoquímicos
medidos o referenciados, clasificación GHS argumentada y revisión por alguien competente. No se
improvisa copiando otra: una SDS mal clasificada te expone legalmente.

## Ejemplo aplicado (BIO-SETA)

Compras etanol 96 % grado alimenticio para tinturas. Lees la SDS y extraes las decisiones:

```
Sección 2:  H225 líquido y vapor muy inflamables; H319 irritación ocular grave
Sección 5:  extinción con espuma, polvo químico o CO2. NO chorro de agua directo (extiende el fuego)
Sección 7:  almacenar en lugar fresco y ventilado, lejos de fuentes de ignición y de oxidantes
Sección 8:  monogafas, guantes de nitrilo, ventilación; límite ocupacional según norma vigente
Sección 9:  punto de inflamación ~13 °C; densidad de vapor mayor que el aire
Sección 10: incompatible con oxidantes fuertes (peróxidos, ácido nítrico, permanganato)
Sección 14: UN 1170, clase 3
```

Decisiones que salen de ahí, en la misma tarde: extractor con toma **a nivel bajo** (vapor más denso
que el aire); extintor clase B junto al reactor y no en la puerta; el peróxido de la limpieza se muda
a otro armario; el transportador necesita ver UN 1170; se compran monogafas, no gafas abiertas.

Ese es el valor de la SDS: no es un papel para el archivador, es una lista de siete decisiones
concretas por sustancia.

## Errores comunes

- **Bajar una SDS genérica de internet** en vez de exigir la del proveedor real; el grado y los
  aditivos cambian la clasificación.
- **Archivarla sin leerla.** El objetivo no es tenerla; es haberla convertido en decisiones.
- **Ignorar la sección 10** y guardar juntos un inflamable y un oxidante.
- **Tenerla solo en inglés** donde trabaja gente que no lo lee.
- **Confundir el pictograma de exclamación con "inofensivo".** Cubre sensibilizantes, que son un
  riesgo acumulativo.
- **Creer que "natural" o "grado alimenticio" implica sin peligros.** El etanol alimenticio arde igual.
- **No actualizar la carpeta** cuando el proveedor emite una revisión nueva.

## Conexión con otros módulos

→ `08-seguridad-de-laboratorio-y-epp.md` — cómo se traduce la SDS en controles y EPP.
→ `63-quimica-verde-y-solventes.md` — elegir el solvente con mejor perfil de peligro.
→ `87-solventes-residuales.md` — el límite de lo que puede quedar en el producto.
→ `134-toxicologia-basica-dosis-y-riesgo.md` — cómo se leen los datos de la sección 11.
→ `285-importacion-y-documentos-tecnicos.md` — la SDS como documento de comercio exterior.
→ `284-auditoria-de-proveedor.md` — la SDS como señal de la seriedad de quien te vende.