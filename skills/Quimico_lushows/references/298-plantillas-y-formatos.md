# 298 — Plantillas y formatos (los siete documentos que hay que tener listos para copiar)

Casi todo el desorden químico de una empresa pequeña se arregla con siete documentos. No con software ni
con consultoría: con siete formatos escritos una vez y usados siempre igual. Aquí están completos, para
copiar y reemplazar lo que va entre corchetes, en el lenguaje que un laboratorio, un proveedor o un auditor
esperan leer —que no es el de un correo—. Un formato mal llenado es mejor que ninguno: deja rastro.

Términos: **especificación (specification)** = rango de aceptación con método por parámetro. **OOS (out of
specification)** = resultado fuera de especificación, que obliga a investigar antes de decidir. **LOQ
(limit of quantitation)** = mínima cantidad que el método sabe cuantificar con confianza.

Todos los formatos van con **versión, fecha y firma**. Sin eso son borradores, no registros (`168`).

## 1. Solicitud de análisis a laboratorio

El documento que evita casi todos los COA inútiles: el laboratorio entrega lo que le pides, y si no pides
método, unidad, base y LOQ, no te los va a dar.

```
SOLICITUD DE ANÁLISIS — [EMPRESA]                       Documento: SOL-[AAAA]-[###]  Versión: 1.0
Fecha: [DD/MM/AAAA]        Solicitante: [nombre, cargo, correo, celular]
Laboratorio: [nombre]      Contacto: [nombre]           Cotización aceptada: [N.º]
1. MUESTRA
   Identificación : [código propio, p. ej. M-2608-01]   Lote del material: [ ]
   Material       : [materia prima / producto en proceso / producto terminado]
   Descripción    : [especie con nombre científico completo; parte usada; forma física]
   Cantidad       : [g o mL]   Presentación: [bolsa sellada / frasco ámbar]
   Muestreó       : [nombre]   Fecha y hora: [DD/MM/AAAA HH:MM]   Contramuestra propia: [Sí/No]
   Transporte     : [ambiente / refrigerado 2–8 °C / protegido de luz]
2. ENSAYOS SOLICITADOS
   | # | Parámetro (analito)      | Método solicitado                  | Unidad y base       | LOQ requerido |
   |---|--------------------------|------------------------------------|---------------------|---------------|
   | 1 | [β-glucano]              | [enzimático, glucano total − α]    | [% p/p base seca]   | [—]           |
   | 2 | [Humedad]                | [Karl Fischer / pérdida por secado]| [% p/p]             | [—]           |
   | 3 | [Pb, Cd, As, Hg]         | [ICP-MS]                           | [mg/kg base seca]   | [0,01 mg/kg]  |
   | 4 | [Identidad de especie]   | [secuenciación ITS]                | [confirmación]      | [—]           |
3. REQUISITOS DEL INFORME (obligatorios)
   [ ] Método declarado con su referencia normativa o de kit, por cada resultado
   [ ] Unidad y base explícitas   [ ] LOQ impreso en todo "no detectado"
   [ ] Lote, fecha de recepción y fecha de análisis   [ ] Firma del responsable técnico
   [ ] Indicación de si el ensayo está dentro del alcance acreditado ISO/IEC 17025
   [ ] Remanente: [devolver / conservar hasta DD/MM/AAAA]
4. DECISIÓN QUE DEPENDE DEL RESULTADO
   [p. ej.: liberar o rechazar el lote de materia prima del proveedor X — 300 kg]

Plazo requerido: [días hábiles]        Firma solicitante: ____________________
```

→ Cómo elegir a quién mandarla: `108`. Cómo enviarla: `109`. Cómo leer lo que vuelve: `110`.

## 2. Ficha técnica de producto

La ficha técnica (technical data sheet) es lo que le entregas a un cliente, distribuidor o autoridad. No es
la especificación: es su cara pública. Su versión legal es la etiqueta (`272`, `293`).

```
FICHA TÉCNICA — [NOMBRE COMERCIAL DEL PRODUCTO]         Código: FT-[###]  Versión: [1.0]
Fecha de emisión: [DD/MM/AAAA]        Reemplaza a: [versión anterior o "N/A"]
1. IDENTIFICACIÓN
   Nombre comercial : [ ]   Presentación: [60 cápsulas de 500 mg / frasco gotero 30 mL]
   Categoría        : [suplemento dietario / alimento / cosmético]   Registro: [N.º o "en trámite"]
   Fabricante       : [razón social, NIT, dirección, país]
2. COMPOSICIÓN
   | Ingrediente                    | Nombre científico / grado | Cantidad por unidad | Función      |
   |--------------------------------|---------------------------|---------------------|--------------|
   | [Extracto de cuerpo fructífero]| [Ganoderma lucidum]       | [500 mg]            | [activo]     |
   | [Cápsula]                      | [HPMC vegetal]            | [1 unidad]          | [envolvente] |
3. ACTIVO   [β-glucano]   Contenido: [≥ 20 % p/p base seca]   Método: [enzimático, total − α-glucano]
            Porción diaria: [2 cápsulas]   Aporte por porción: [≥ 200 mg]
4. FÍSICAS  Aspecto: [ ]  Color: [ ]  Olor: [ ]  Humedad: [≤ X % p/p]
5. CONSERVACIÓN  [Lugar fresco y seco, ≤ 30 °C, protegido de la luz]   Vida útil: [X meses]
6. ENVASE   Primario: [ ]  Secundario: [ ]  Sellado: [ ]
7. ALÉRGENOS  [Declaración explícita; "no contiene" solo si está verificado]
8. DOCUMENTOS  COA por lote · Especificación ESP-[###] · Estudio de estabilidad EST-[###]

Elaboró: [ ]    Revisó (técnico): [ ]    Firma y fecha: ____________________
```

## 3. Especificación de producto terminado

Un contrato con tu propio producto: qué debe cumplir, medido cómo, y qué pasa si no cumple. Se construye con
**varios lotes**, nunca con uno (`282`).

```
ESPECIFICACIÓN DE PRODUCTO TERMINADO                    Código: ESP-[###]  Versión: [1.0]
Producto: [nombre]   Presentación: [ ]   Vigente desde: [DD/MM/AAAA]   Base de datos: [n.º de lotes]

| # | Parámetro            | Criterio de aceptación   | Método / referencia          | Frecuencia   |
|---|----------------------|--------------------------|------------------------------|--------------|
| 1 | Aspecto              | [descripción exacta]     | [visual, patrón de referencia]| Cada lote   |
| 2 | Identidad de especie | [confirmada]             | [ITS / HPTLC]                | [Cada lote / anual] |
| 3 | [β-glucano]          | [≥ 20,0 % p/p base seca] | [enzimático]                 | Cada lote    |
| 4 | [α-glucano]          | [≤ 10,0 % p/p base seca] | [enzimático]                 | Cada lote    |
| 5 | Humedad              | [≤ 8,0 % p/p]            | [Karl Fischer / secado]      | Cada lote    |
| 6 | Actividad de agua    | [≤ 0,60]                 | [higrómetro de punto de rocío]| Cada lote   |
| 7 | Peso por unidad      | [500 mg ± 5 %]           | [gravimetría, n = 20]        | Cada lote    |
| 8 | Metales pesados      | [Pb ≤ X; Cd ≤ X; As ≤ X; Hg ≤ X mg/kg] | [ICP-MS]       | [Cada lote / cada N] |
| 9 | Microbiología        | [según norma vigente]    | [métodos oficiales]          | Cada lote    |
|10 | Solventes residuales | [si aplica al proceso]   | [GC-headspace]               | [Por proceso]|

BASE DEL CRITERIO   Lotes analizados: [n]   Promedio: [ ]   Desviación estándar: [ ]   Regla: [ ]

MANEJO DE RESULTADO FUERA DE ESPECIFICACIÓN (OOS)
1. No se libera el lote. 2. Investigación escrita en 48 h. 3. Se revisa contramuestra.
4. Solo se reanaliza con causa documentada. 5. La decisión final la firma [cargo].

Elaboró: [ ]   Revisó: [ ]   Aprobó (responsable técnico): [ ]   Firma y fecha: ______________
```

→ Cómo se verifica lote a lote: `283`. Para hongos, con parámetros propios: `247`.

## 4. Protocolo de estudio de estabilidad

Se escribe **antes** de empezar. Un estudio de estabilidad decidido sobre la marcha no sostiene una vida útil.

```
PROTOCOLO DE ESTABILIDAD                                Código: EST-[###]  Versión: [1.0]
Producto: [ ]   Lotes en estudio: [mínimo 3: n.º, n.º, n.º]   Inicio: [DD/MM/AAAA]
1. OBJETIVO       Sustentar una vida útil de [X] meses en el envase comercial.
2. ENVASE         El envase primario real de venta: [material, cierre, barrera]. Nunca bolsa de laboratorio.
3. CONDICIONES    Tiempo real: [30 °C ± 2 °C / 75 % HR ± 5 %] (zona cálida-húmeda, Colombia)
                  Acelerado  : [40 °C ± 2 °C / 75 % HR ± 5 %]   Cámara: [equipo, calibración vigente]
4. PUNTOS         Tiempo real: 0, 3, 6, 9, 12, 18, 24 meses    Acelerado: 0, 1, 2, 3, 6 meses
5. PARÁMETROS EN CADA PUNTO
   | Parámetro           | Método            | Criterio de aceptación        |
   |---------------------|-------------------|-------------------------------|
   | [Activo]            | [ ]               | [≥ 90 % del valor declarado]  |
   | Humedad             | [ ]               | [≤ X % p/p]                   |
   | Actividad de agua   | [ ]               | [≤ 0,60]                      |
   | Aspecto, color, olor| [visual/sensorial]| [sin cambio respecto a T0]    |
   | Microbiología       | [ ]               | [según norma vigente]         |
6. CRITERIO DE FIN DE VIDA ÚTIL (definido de antemano)
   [El primero que ocurra: activo < 90 % del declarado, o humedad > X %, o microbiología fuera.]
7. DATOS Y CÁLCULO   Datos crudos archivados en [ubicación]. Extrapolación por [Arrhenius / Q10],
                     ejecutada y verificada (`lab-tools/vida_util_arrhenius.py`, `Matematicas_lushows`).
8. COMPROMISO        Un lote por año en estabilidad de seguimiento (`164`).

Elaboró: [ ]   Aprobó: [ ]   Firma y fecha: ____________________
```

## 5. Registro de lote

Se llena **en el momento**, con lapicero, por quien hace la operación. Llenado después, de memoria, no vale; es lo primero que pide un auditor (`168`, `167`).

```
REGISTRO DE LOTE                                        Lote: [LT-AAMM-###]   Hoja [ ] de [ ]
Producto: [ ]   Fórmula/versión: [ ]   Tamaño de lote teórico: [ ]   Fecha de inicio: [DD/MM/AAAA]
1. MATERIAS PRIMAS UTILIZADAS
   | Material | Proveedor | Lote proveedor | COA verificado | Liberada por | Cantidad usada | Pesó |
   |----------|-----------|----------------|----------------|--------------|----------------|------|
   |          |           |                | [Sí/No]        |              | [kg]           |      |
2. OPERACIONES
   | Paso | Operación   | Equipo | Parámetro (T, tiempo, rpm, relación) | Real | Hora | Operario | Visto |
   |------|-------------|--------|--------------------------------------|------|------|----------|-------|
   | 1    | [Molienda]  |        | [malla ]                             |      |      |          |       |
   | 2    | [Extracción]|        | [ °C /  h / solvente : sólido]       |      |      |          |       |
   | 3    | [Secado]    |        | [ °C /  h]                           |      |      |          |       |
   | 4    | [Encapsulado]|       | [peso objetivo mg ± %]               |      |      |          |       |
3. CONTROLES EN PROCESO   | Control | Criterio | Resultado | Hora | Responsable |
4. RENDIMIENTO            Teórico: [ ]  Real: [ ]  % rendimiento: [ ]  Balance de masa cuadra: [Sí/No]
5. DESVIACIONES           N.º: [ ]  Descripción: [ ]  Investigación: [ ]  Cerrada por: [ ]
6. MUESTRAS               Muestra a laboratorio: [código]   Contramuestra: [cantidad, ubicación, sello]
7. ETIQUETA               Versión de arte usada: [ ]   Cantidad impresa: [ ]   Sobrantes destruidos: [ ]
8. LIBERACIÓN             Resultados dentro de ESP-[###]: [Sí/No]   Fecha de vencimiento asignada: [ ]

Liberado por (responsable técnico): ____________________   Fecha: [DD/MM/AAAA]
```

## 6. Carta de impugnación de resultado

Cuando un resultado no cuadra. El tono importa: se impugna el **dato**, no al laboratorio, y se pide un
procedimiento, no un favor.

```
[Ciudad], [DD/MM/AAAA]
Señores [LABORATORIO] — Atn.: [Responsable técnico / Dirección de calidad]
Asunto: Solicitud de revisión del informe de ensayo N.º [###], muestra [código], lote [ ]

Respetados señores:

Recibimos el informe de la referencia, con fecha [DD/MM/AAAA], en el cual se reporta [parámetro] =
[valor] [unidad y base]. Solicitamos formalmente su revisión por los siguientes hechos objetivos:
1. El resultado difiere de [n] determinaciones previas del mismo material, cuyo rango histórico es
   [valor–valor] [unidad y base] (informes [###], [###]).
2. [Observación técnica concreta: base no declarada / LOQ no impreso / método distinto al solicitado
   en SOL-[###] / desviación mayor a la incertidumbre declarada del método].

En consecuencia, solicitamos:
a) Datos crudos del ensayo: cromatogramas o espectros, curva de calibración con su R², patrón de
   referencia usado y su certificado, y el control de calidad de la corrida.
b) Método aplicado con su referencia, y confirmación de si el ensayo está dentro del alcance
   acreditado ISO/IEC 17025 del laboratorio.
c) Incertidumbre de medida asociada al resultado.
d) Reanálisis sobre contramuestra sellada ([cantidad], en [condición]), con protocolo acordado.

De persistir la diferencia, proponemos remitir una porción de la misma contramuestra al laboratorio
árbitro [nombre], acreditado para este ensayo, con costos a cargo de [según acuerdo]. Esta solicitud no
cuestiona la idoneidad de su equipo técnico: busca resolver una discrepancia con trazabilidad
documental, conforme a nuestro procedimiento de manejo de resultados fuera de especificación.
Agradecemos su respuesta dentro de [10] días hábiles.

Cordialmente, [Nombre] — [Cargo] — [Empresa] — [NIT] — [correo, celular]
Anexos: informe [###], solicitud SOL-[###], histórico de resultados.
```

→ El procedimiento completo y cuándo NO impugnar: `112`. Por qué no se repite hasta que salga bonito: `113`.

## 7. Checklist de recepción de materia prima

Se llena en el muelle, antes de descargar. Lo que entra sin este papel entra en cuarentena, no a producción.

```
RECEPCIÓN DE MATERIA PRIMA                              Registro: REC-[AAAA]-[###]
Fecha y hora: [ ]   Material: [ ]   Proveedor: [ ]   Lote proveedor: [ ]   Cantidad: [ ]   Recibe: [ ]
DOCUMENTOS
[ ] Factura y remisión coinciden en material, lote y cantidad
[ ] COA del lote recibido (no de otro lote, no sin lote), con método, unidad, base y LOQ
[ ] Ficha técnica vigente y SDS   [ ] Origen / documentos de importación cuando aplique
MATERIAL FÍSICO
[ ] Empaques íntegros, sin humedad, sin rotura, sin plaga
[ ] Rotulado legible: material, lote, fecha, fabricante, condiciones de conservación
[ ] Aspecto, color y olor conformes al patrón; sin olor a solvente, moho o fermentación
[ ] Temperatura de llegada dentro de lo pactado (si aplica)
VERIFICACIÓN PROPIA
[ ] Muestreo representativo hecho por nosotros, no por el transportador
[ ] Contramuestra sellada, identificada y almacenada
[ ] Muestra enviada a laboratorio con SOL-[###] (parámetros: [ ])
[ ] Identidad verificada por [ITS / HPTLC / organoléptico + documento]
DECISIÓN
[ ] CUARENTENA (por defecto, hasta resultados)   Ubicación: [ ]   Etiqueta amarilla puesta: [ ]
[ ] LIBERADA        Resultado dentro de especificación [ESP/MP-###]   Fecha: [ ]
[ ] RECHAZADA       Motivo: [ ]   Acción: [devolución / destrucción]   Acta N.º: [ ]

Recibió: ____________   Verificó calidad: ____________   Decisión firmada por: ____________
```

→ Qué exigirle al proveedor antes de llegar a este punto: `141`, `284`. Qué hacer si falla: `169`.

## Cómo usar estos siete formatos sin volverlos burocracia

Numéralos, ponles versión y guárdalos en una sola carpeta con el expediente del producto (`286`). Llénalos
en el momento, no al final del mes. Y si un formato nunca se usa, quítalo: un sistema de calidad que nadie
llena crea la ilusión de control, que es peor que no tenerlo. El informe final que sale de todo esto: `294`.

## Conexión con otros módulos

→ `295-checklist-de-calidad-quimica.md` — las listas de verificación que acompañan estos formatos.
→ `282-especificacion-de-producto-terminado.md` — cómo se construye el criterio de la plantilla 3.
→ `168-documentacion-de-lote-y-trazabilidad.md` — el marco del registro de lote.
→ `112-como-impugnar-un-resultado.md` — el procedimiento detrás de la carta.
→ `286-expediente-tecnico-del-producto.md` — dónde vive todo esto archivado.
