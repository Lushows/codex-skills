# 237 — Nucleósidos y nucleótidos fúngicos: los marcadores pequeños que delatan la especie

Mientras el mundo de los hongos funcionales discute polisacáridos de cientos de kilodaltons, hay una familia
de moléculas pequeñas que se mide fácil, se separa bien en HPLC y sirve para dos cosas que los β-glucanos no
hacen: **identificar de qué especie viene el material** y **detectar que un "cordyceps" no tiene lo que dice
tener**. Son los nucleósidos: adenosina, cordicepina, uridina, guanosina y compañía. Este módulo es el mapa
del grupo; el análisis específico de cordicepina y adenosina en *Cordyceps* vive en `228`.

Términos: **nucleósido (nucleoside)** = base nitrogenada + azúcar (ribosa o desoxirribosa), sin fosfato.
**nucleótido (nucleotide)** = nucleósido + uno o más grupos fosfato. **cordicepina (cordycepin)** =
3'-desoxiadenosina, análogo de adenosina al que le falta el hidroxilo en posición 3'. **HEA** =
N6-(2-hidroxietil)-adenosina, otro nucleósido de *Cordyceps* que coeluye con facilidad. **adenosina
desaminasa (adenosine deaminase, ADA)** = enzima que convierte adenosina en inosina y cordicepina en
3'-desoxiinosina.

## Quién es quién

| Compuesto | Estructura | Dónde aparece | Para qué sirve como marcador |
|---|---|---|---|
| Adenosina | Adenina + ribosa | Casi todos los hongos | Marcador de calidad en farmacopeas para *Cordyceps* |
| **Cordicepina** | 3'-desoxiadenosina | ***Cordyceps militaris*** | Es el diferenciador de especie del género; ver abajo |
| HEA | N6-(2-hidroxietil)-adenosina | *Cordyceps*, *Ophiocordyceps* | Trampa analítica: coeluye con adenosina en métodos flojos |
| Uridina | Uracilo + ribosa | Muy abundante en varios *Cordyceps* | En algunas especies es el nucleósido mayoritario |
| Guanosina, inosina | Purínicos | Amplio | Perfil de huella, no marcador único |
| Nucleótidos 5' (GMP, IMP) | Con fosfato | Shiitake y otros | Responsables del umami; interesan más al sabor que a la potencia |

Detalle bonito que conecta química y cocina: el sabor umami del shiitake seco viene en buena parte de
nucleótidos 5' como el guanilato, que se liberan al rehidratar y calentar. No es un "activo", pero es una
propiedad química medible y una razón real de compra (`162`).

## El diferenciador que importa: cordicepina y las dos "cordyceps"

| Especie | Nombre comercial | Cordicepina |
|---|---|---|
| *Cordyceps militaris* | Cordyceps cultivado (naranja) | **Sí**, es su compuesto característico |
| *Ophiocordyceps sinensis* | "Cordyceps sinensis", el silvestre del Himalaya | **Prácticamente ausente** en la literatura disponible |

Este es uno de los fraudes más rentables del mercado: se vende un producto etiquetado como
*Cordyceps sinensis* y se le atribuye cordicepina, que ese material no aporta. O al revés: se vende
*C. militaris* barato con el nombre y el precio del silvestre. **La cordicepina medida, junto con el ITS
(`245`), resuelve la discusión en una sola tanda de laboratorio.**

## Rangos reportados en la literatura

| Material | Adenosina | Cordicepina | Fuente |
|---|---|---|---|
| Cuerpo fructífero de *C. militaris* (media) | **2,45 ± 0,03 mg/g base seca** | **2,654 ± 0,02 mg/g base seca** | Trabajo de determinación por HPLC citado en el estudio de NIR de *C. militaris* (*ACS Omega*, 2020; PubMed 33134685) |
| Productos comerciales de *Cordyceps* spp. (rango amplio) | **0,28–14,15 mg/g** | **0,006–6,36 mg/g** | Estudio de determinación y análisis de cordicepina y adenosina en productos de *Cordyceps* spp. |
| *Cordyceps cicadae*, poblaciones distintas | Perfil variable de nucleósidos | — | PMC6271799, 2018 |

Ese rango de cordicepina —de 0,006 a 6,36 mg/g— es **un factor de mil**. No hay forma de saber qué compraste
sin medirlo. Y como siempre: rangos de literatura, verifica con tu lote (`02`).

## Cómo se mide / cómo se comprueba

| Paso | Detalle |
|---|---|
| Extracción | Agua o metanol acuoso (10–50 %), con ultrasonido; los nucleósidos son polares e hidrosolubles |
| Separación de rutina | **HPLC-UV a 260 nm**, columna C18, gradiente agua/metanol o agua/acetonitrilo con buffer de fosfato o formiato |
| Separación crítica | Adenosina, HEA y cordicepina eluyen cerca. Un método mal desarrollado los suma y te infla la cordicepina (`80`, `81`) |
| Confirmación | **LC-MS/MS** en MRM con patrones de adenosina y cordicepina | 
| Patrones | Obligatorios, con certificado. Sin patrón hay estimación, no cuantificación (`70`) |
| Unidad y base | `mg/g base seca`; declarar humedad (`07`, `98`) |
| Alternativa rápida | Espectroscopía NIR calibrada contra HPLC, para control en línea (*ACS Omega*, 2020). Es un modelo, no un método primario: requiere validación y recalibración (`92`, `105`) |

**Pureza de pico obligatoria.** Con detección UV a 260 nm, cualquier compuesto con anillo purínico o
pirimidínico absorbe. Sin DAD y evaluación de pureza espectral, o sin confirmación por masas, un "pico de
cordicepina" puede ser cualquier cosa (`80`).

## Estabilidad: el detalle que arruina resultados

La cordicepina y la adenosina son sustrato de la **adenosina desaminasa**, presente en el propio material
biológico. Si extraes en frío y dejas el extracto acuoso reposando a temperatura ambiente, la enzima sigue
trabajando y tu cordicepina se convierte en 3'-desoxiinosina. Consecuencias:

- Extraer con calor suficiente para inactivar la enzima, o acidificar/enfriar y analizar rápido.
- Reportar el tiempo entre extracción e inyección en el protocolo del método (`65`).
- Un mismo lote analizado por dos laboratorios con protocolos distintos puede dar resultados distintos por
  esto y no por "el laboratorio miente" (`112`).

## Ejemplo aplicado — auditar un "Cordyceps sinensis 0,3 % cordicepina" (ILUSTRATIVO)

```
Oferta: "Cordyceps sinensis extract, 0,3 % cordycepin, 10:1"

Banderas rojas antes de pedir muestra:
  1. Ophiocordyceps sinensis practicamente no aporta cordicepina.
     -> O no es sinensis, o el 0,3 % no es cordicepina.
  2. Pedir el cromatograma, no solo el numero (110, 111).
  3. Pedir ITS de la especie (245).

Verificacion propia (lo que se manda a medir):
  cordicepina y adenosina por HPLC-UV 260 nm CON confirmacion LC-MS/MS
  ITS
  beta-glucano / alfa-glucano por Megazyme (220, 221)  -> descarta grano

Cuenta de aporte si el 0,3 % fuera cierto:
  0,3 % p/p = 3 mg/g. Capsula de 500 mg -> 1,5 mg de cordicepina por capsula.
  Porcion de 2 capsulas -> 3,0 mg/dia. Se declara el dato con metodo y base;
  NO se le atribuye ningun efecto.
```

## Qué se puede y qué no se puede afirmar

- **Se puede** declarar contenido medido: "aporta X mg de cordicepina y Y mg de adenosina por porción, por
  HPLC-UV con confirmación por LC-MS/MS, base seca".
- **Se puede** usar el perfil de nucleósidos como argumento de **autenticidad e identidad**, que es un
  argumento técnico legítimo y verificable.
- **No se puede** atribuirle efectos terapéuticos. La cordicepina tiene una literatura enorme `[in vitro]`
  (antitumoral, antiviral, antiinflamatoria) y trabajos `[animal]`; nada de eso se traslada a un suplemento.
- **No se puede** hablar de "energía" o "rendimiento" como si fuera un hecho establecido sin decir el nivel
  de evidencia y sin verificar si esa frase es un claim permitido en tu marco (`267`, `276`).

## Errores comunes

- **Aceptar "cordicepina" sin cromatograma.** Con UV a 260 nm sobra gente absorbiendo.
- **No separar HEA de adenosina** y reportar adenosina inflada.
- **Comprar "sinensis" con claim de cordicepina.** Química y etiqueta no cuadran.
- **Extraer en frío y analizar tarde**: la desaminasa se come tu analito.
- **Usar NIR como método primario** sin la calibración validada detrás (`105`).
- **Confundir nucleósido con nucleótido** en la ficha técnica; no son lo mismo y no se miden igual.
- **Olvidar el patrón de referencia.** Sin él, es una estimación con nombre elegante (`70`).

## Conexión con otros módulos

→ `227-cordyceps-quimica.md` — la especie completa.
→ `228-cordicepina-y-adenosina-analisis.md` — el método en detalle, paso a paso.
→ `79-hplc-y-uhplc.md` — la técnica base de este grupo.
→ `80-deteccion-uv-dad-y-pureza-de-pico.md` — cómo saber si el pico es lo que dices.
→ `245-identidad-de-especie-por-its.md` — el otro lado de la verificación de identidad.
→ `246-adulteracion-y-fraude-en-suplementos-de-hongos.md` — dónde encaja este fraude en el mapa general.
