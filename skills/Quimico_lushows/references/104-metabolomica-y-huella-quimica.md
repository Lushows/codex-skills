# 104 — Metabolómica y huella química (autenticar sin saber de antemano qué buscar)

Todos los métodos anteriores parten de una pregunta cerrada: "¿cuánto hay de X?". La metabolómica invierte el
planteamiento: mide **todo lo que se pueda medir** en la muestra y luego busca en qué se diferencian dos
grupos. Es la herramienta correcta cuando no sabes qué buscar: detectar adulteración desconocida, distinguir
dos orígenes geográficos, ver si el cambio de proceso alteró el producto, o autenticar un extracto donde ya
no hay ADN. Es cara y exige estadística seria, pero resuelve preguntas que ninguna otra técnica responde.

Términos: **metaboloma (metabolome)** = conjunto de metabolitos de una muestra. **untargeted (no dirigida)**
= se detecta todo lo detectable, sin lista previa. **targeted (dirigida)** = se cuantifican analitos de una
lista. **huella química (chemical fingerprint)** = patrón completo que identifica un material sin identificar
cada compuesto. **feature** = cada señal individual (masa + tiempo de retención) del conjunto de datos.

## Dirigida vs no dirigida

| | Dirigida (targeted) | No dirigida (untargeted) |
|---|---|---|
| Pregunta | "¿Cuánto ácido ganodérico A hay?" | "¿En qué se diferencian estos dos lotes?" |
| Instrumento | LC-MS/MS (MRM) | LC-HRMS (QTOF, Orbitrap), RMN, GC-MS |
| Patrones | Uno por analito | No hacen falta al principio |
| Salida | Números con unidad | Matriz de miles de features, se procesa con quimiometría |
| Cuantitativa | Sí | Semicuantitativa (área relativa) |
| Costo | Medio | Alto |
| Uso | Especificación, cumplimiento | Autenticación, investigación, control de proceso |

## Las tres plataformas

- **LC-HRMS** (QTOF u Orbitrap). La más usada. Detecta miles de features en polaridad positiva y negativa.
  Requiere masa exacta y buena cromatografía (ver `84`).
- **GC-MS**. Para volátiles y semivolátiles derivatizados: azúcares, ácidos orgánicos, aminoácidos, terpenos.
  La ventaja enorme es que existen **bibliotecas de espectros** (NIST, Wiley) con búsqueda confiable.
- **RMN ¹H**. Menos sensible pero **muy reproducible** entre equipos y entre años, y directamente
  cuantitativa. Por eso es la plataforma preferida para autenticación de alimentos (jugos, vinos, mieles) y
  la que mejor aguanta una discusión legal (ver `94`, `95`).

## Flujo de trabajo (donde se cometen los errores)

```
1. DISENO. Definir grupos y n. Minimo ~10 muestras por grupo para que la estadistica signifique algo.
   Un "autentico" y un "sospechoso" no es un estudio: es una anecdota.
2. Muestras de control de calidad (QC): mezcla de TODAS las muestras, inyectada cada 5-10 corridas.
   Sin QC no puedes corregir la deriva del instrumento ni saber si el modelo es real.
3. Aleatorizar el orden de inyeccion. Si corres todos los autenticos primero y los sospechosos despues,
   tu modelo separara por DIA, no por muestra.
4. Preparacion identica para todas: misma masa, mismo solvente, misma dilucion.
5. Adquisicion HRMS: masa exacta, MS/MS en muestras representativas.
6. Procesado: deteccion de picos, alineamiento, llenado de huecos, normalizacion
   (por masa, por suma total, por estandar interno).
7. Filtrado por QC: descartar features con RSD > 20-30 % en los QC. Suele eliminar la mitad.
8. Estadistica: PCA primero (no supervisado), luego PLS-DA / OPLS-DA con VALIDACION CRUZADA
   y prueba de permutacion. Ver 105.
9. Identificacion de los features discriminantes: masa exacta -> formula -> MS/MS -> patron autentico.
```

## Niveles de confianza en la identificación (convención de metabolómica)

| Nivel | Qué tienes | Cómo se reporta |
|---|---|---|
| 1 | Coincide con **patrón auténtico** corrido en tu mismo método (masa, tR, MS/MS) | "Identificado" |
| 2 | Coincide con biblioteca o literatura (masa exacta + MS/MS), sin patrón | "Putativamente anotado" |
| 3 | Solo clase de compuesto (p. ej. "un triterpeno") | "Clase de compuesto" |
| 4 | Solo masa y tR | "Desconocido" |

Regla dura: si vas a poner un nombre de compuesto en un COA, en una etiqueta o en un informe a un cliente,
tiene que ser **nivel 1**. Todo lo demás va con la palabra "putativo" escrita.

## Para qué la vas a usar de verdad

- **Autenticar extractos** donde el ADN ya no sirve (ver `103`).
- **Distinguir cuerpo fructífero de micelio en grano** por su perfil completo: los polvos de micelio sobre
  grano llevan la firma del sustrato (almidón, oligosacáridos del cereal). Es un complemento a la medición de
  α-glucano, no un reemplazo (ver `91`, `218`).
- **Diferenciar origen geográfico o quimiotipo** de una misma especie.
- **Control de proceso**: comparar el perfil antes y después de cambiar solvente, temperatura o proveedor.
  Es una forma de demostrar **comparabilidad** sin tener que cuantificar todo.
- **Buscar adulterantes desconocidos**: sintéticos añadidos, colorantes, cargas.

## Ejemplo aplicado (ILUSTRATIVO)

Sospecha de que un proveedor está mezclando cuerpo fructífero de reishi con micelio sobre arroz.

```
Diseno   : 12 lotes verificados de cuerpo fructifero (grupo A) vs 12 lotes del proveedor (grupo B)
Plataforma: LC-HRMS QTOF, positivo y negativo, gradiente 20 min, QC cada 6 inyecciones
Features detectados      : 4.812
Tras filtro por QC (RSD<=20 %): 1.930

PCA (no supervisado): dos nubes claramente separadas en PC1 (38 % de la varianza).
                      La separacion NO fue inducida: aparece sin decirle al modelo los grupos.
OPLS-DA: R2Y = 0,94 ; Q2 = 0,86 ; prueba de permutacion (200) supera -> modelo valido
Features discriminantes en B:
   m/z 365,1054 [M+Na]+  -> maltosa (nivel 1, confirmada con patron)
   m/z 527,1583          -> maltotriosa (nivel 2)
Interpretacion: firma de almidon de cereal hidrolizado -> sustrato de grano.
Confirmacion ortogonal: alfa-glucano por K-YBGL = 38 % p/p b.s. en B vs 4 % en A. Coherente.
```

El resultado que convence a un abogado o a un proveedor no es el PCA: es el **α-glucano del K-YBGL**. La
metabolómica te dijo dónde mirar; la química dirigida dio el número. (Cifras ilustrativas.)

## Errores comunes

- **n pequeño.** Con 3 vs 3, el PLS-DA separa cualquier cosa, incluso ruido. Siempre valida por permutación.
- **Sin muestras QC.** La deriva del instrumento se confunde con biología.
- **Sin aleatorizar** el orden de inyección: el modelo aprende el día, no la muestra.
- **Reportar un nombre de compuesto en nivel 2 como si fuera confirmado.**
- **Usar PLS-DA sin validación cruzada** y presentar un R² alto como prueba. Ver `105`.
- **Creer que el área relativa es concentración.** No lo es hasta que cuantifiques con patrón.
- **Terminar en el gráfico bonito.** La metabolómica sin confirmación ortogonal es una hipótesis costosa.

## Conexión con otros módulos

→ `105-quimiometria-pca-y-modelos.md` — la estadística sin la cual esto no significa nada.
→ `84-hrms-qtof-orbitrap-e-identificacion.md` — el instrumento y la masa exacta.
→ `103-identidad-por-adn-its-y-barcoding.md` — la identidad de especie que la química no da.
→ `60-quimiotaxonomia-y-marcadores.md` — la lógica de usar la química como firma taxonómica.
→ `218-el-fraude-del-micelio-en-grano.md` — el problema que este módulo ayuda a demostrar.
→ `96-tlc-y-hptlc.md` — la huella química de bajo costo cuando no hay presupuesto para HRMS.