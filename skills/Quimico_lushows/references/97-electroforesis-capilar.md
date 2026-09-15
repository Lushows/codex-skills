# 97 — Electroforesis capilar (cuando la carga separa mejor que la polaridad)

La electroforesis capilar (CE) separa moléculas por cómo se mueven dentro de un tubo de sílice finísimo
cuando le aplicas alto voltaje. No usa columnas caras, gasta nanolitros de muestra y microlitros de
solvente, y separa cosas que a la cromatografía líquida le cuestan: iones inorgánicos, aminoácidos,
péptidos, ADN, enantiómeros. En el mundo de suplementos y cannabis es una técnica **de nicho**, pero es la
respuesta correcta a preguntas concretas —aniones y cationes, oxalato en chaga, separación quiral— donde
montar un HPLC equivalente sale más caro y más lento.

Términos: **CE (Capillary Electrophoresis)** = separación por movilidad electroforética en un capilar.
**EOF (electroosmotic flow)** = flujo de todo el líquido arrastrado por la pared cargada del capilar; empuja
a todos hacia el detector. **movilidad electroforética (electrophoretic mobility)** = velocidad propia del
ion por unidad de campo; depende de carga/tamaño. **MEKC (Micellar Electrokinetic Chromatography)** = CE con
micelas de surfactante en el buffer, permite separar **neutros**. **CZE (Capillary Zone Electrophoresis)** =
el modo básico.

## Cómo separa

```
Velocidad aparente = (mu_ef + mu_EOF) x E

mu_ef  = movilidad electroforetica del analito (positiva para cationes, negativa para aniones)
mu_EOF = movilidad del flujo electroosmotico (a pH > 3 apunta hacia el catodo)
E      = campo electrico = voltaje / longitud del capilar (V/cm)
```

Consecuencia práctica del orden de salida en CZE a pH básico: **primero los cationes**, después los
**neutros** (todos juntos, sin separar), y de últimos los **aniones**. Si tus analitos son neutros —caso de
los cannabinoides neutros o los triterpenos— CZE no los separa y hay que ir a MEKC.

## Modos y para qué sirve cada uno

| Modo | Separa por | Ejemplo útil |
|---|---|---|
| **CZE** | Carga/tamaño | Aniones (oxalato, cloruro, sulfato), cationes, ácidos orgánicos |
| **MEKC** | Reparto en micelas | Neutros: cannabinoides, conservantes, colorantes |
| **CGE** (gel) | Tamaño | ADN, proteínas; base de la secuenciación Sanger para ITS |
| **cIEF** (isoelectroenfoque) | Punto isoeléctrico | Proteínas, isoformas |
| **CE quiral** (con ciclodextrinas) | Enantiómeros | Separar R/S sin columna quiral cara |

Detección habitual: UV en el propio capilar (camino óptico de ~50 µm, por eso poca sensibilidad),
fluorescencia inducida por láser (LIF, muy sensible), conductividad sin contacto (C⁴D, ideal para iones que
no absorben) o acoplamiento a masas (CE-MS).

## Dónde tiene sentido en cannabis y hongos

- **Oxalato en chaga.** El oxalato es un anión sin cromóforo útil; CE con detección indirecta o C⁴D lo mide
  bien y barato. Es un tema de seguridad real del chaga (ver `230-chaga-riesgos-oxalato-y-radiocesio.md`).
- **Aniones y cationes del agua de proceso**: cloruro, nitrato, sulfato, fosfato (ver `106`).
- **Aminoácidos libres** en extractos, como marcador de proceso o de adulteración.
- **Ergotioneína**, que es un aminoácido modificado con carga: separable por CE, aunque el método más
  reportado sigue siendo HPLC (ver `235-ergotioneina.md`).
- **Perfil de ADN**: la electroforesis capilar de gel es lo que hay dentro del secuenciador Sanger que te
  entrega la secuencia ITS (ver `103`).
- **Cannabinoides por MEKC**: publicado y funcional, pero en la industria manda el HPLC-DAD porque los
  reguladores y los COA están estandarizados ahí (ver `198`).

## Cómo se comprueba

- **Acondicionamiento del capilar**: lavados con NaOH, agua y buffer antes de cada serie. Un capilar mal
  acondicionado mueve el EOF y con él todos los tiempos de migración.
- **Estándar interno obligatorio.** En CE la reproducibilidad de área es peor que en HPLC porque el volumen
  inyectado depende de la viscosidad y de la temperatura; el estándar interno lo corrige (ver `72`).
- **Tiempo de migración relativo** (respecto al estándar interno) en vez de tiempo absoluto.
- **Control de temperatura**: el efecto Joule calienta el buffer; sin refrigeración las bandas se ensanchan.
- **Buffer fresco.** La electrólisis agota el buffer en los viales; se cambia cada N corridas y se declara.
- Validación completa igual que cualquier método: `73`, `74`, `75`.

## Ejemplo aplicado (ILUSTRATIVO)

Oxalato total en polvo de chaga, para decidir si el producto lleva advertencia de consumo.

```
Tecnica     : CE-C4D, capilar de silica 50 um x 60 cm, buffer de fosfato pH 7,5
Inyeccion   : hidrodinamica, 50 mbar x 5 s
Voltaje     : -25 kV (polaridad invertida para aniones)
Estandar    : oxalato de sodio, curva 1-50 mg/L, R2 = 0,998
Estandar interno: tartrato

Muestra     : chaga silvestre molido, lote CH-2605, humedad 7,4 % p/p
Resultado   : 12,8 mg de oxalato / g base seca   (ILUSTRATIVO)
LOQ         : 0,5 mg/g base seca
Interpretacion: valor alto frente a otras matrices; se calcula el aporte por porcion
                y se rutea la decision de advertencia a 230 y 250.
```

Nota de honestidad: este número **es ilustrativo**. El contenido de oxalato del chaga varía muchísimo entre
origen, parte del esclerocio y forma de extracción. Hay que medirlo por lote, no citar un número de internet.

## Errores comunes

- **Comparar tiempos de migración absolutos** entre días o entre equipos. Usa tiempo relativo.
- **Omitir el estándar interno.** Las áreas en CE sin corregir tienen una dispersión que arruina la exactitud.
- **Buffer reutilizado** hasta que la línea base se vuelve loca.
- **Intentar separar neutros por CZE.** No se separan; hay que ir a MEKC.
- **Esperar sensibilidad de HPLC** con detección UV: el camino óptico es 200 veces menor. Para trazas, LIF,
  C⁴D o MS.
- **Vender CE como reemplazo de HPLC en un COA de potencia.** Los reguladores esperan el método aceptado en
  su jurisdicción; cambiar de técnica exige demostrar equivalencia (ver `75`).

## Conexión con otros módulos

→ `37-electroquimica-y-electrodos.md` — la base física del movimiento de iones.
→ `79-hplc-y-uhplc.md` — la técnica que hace el 90 % del trabajo; CE cubre lo que ella no.
→ `230-chaga-riesgos-oxalato-y-radiocesio.md` — el caso concreto donde CE gana.
→ `103-identidad-por-adn-its-y-barcoding.md` — la CE de gel dentro del secuenciador.
→ `106-analisis-de-agua-y-materias-primas.md` — aniones y cationes en agua de proceso.
→ `72-estandar-interno-y-adicion-de-estandar.md` — por qué aquí es obligatorio.
