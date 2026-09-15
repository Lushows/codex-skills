# 296 — Errores comunes del oficio (los veinte que más caro se pagan)

Este módulo es la memoria de las heridas. Todo lo que enseñan los módulos anteriores existe porque alguien
perdió plata, lote o registro haciendo exactamente una de estas veinte cosas. No son errores de químico
distraído: casi todos los comete gente inteligente que confió en un documento que parecía serio. Léelo
completo una vez y vuelve a él cada vez que estés por firmar una compra, una etiqueta o un lote. Cada error
trae su síntoma, su causa, lo que cuesta y el módulo que lo resuelve de fondo.

Términos: **COA (certificate of analysis)** = certificado de análisis de un lote. **especificación
(specification)** = rango con criterio de aceptación y método por cada parámetro. **contramuestra (retain
sample)** = porción del mismo lote que guardas sellada para poder discutir después.

## Errores al leer un dato (1–7)

### 1. Confundir "polisacáridos" con "beta-glucanos"
**Síntoma:** el COA dice "polisacáridos totales 40 %" y tú lo lees, y lo publicas, como β-glucano.
**Por qué pasa:** ese ensayo colorimétrico cuenta también el α-glucano (almidón) del grano del sustrato. Es barato y es el disfraz #1 del micelio cultivado en grano.
**Qué cuesta:** pagas almidón a precio de activo y la etiqueta queda sin sustento analítico ante INVIMA.
**Lo resuelve:** `222`, `220`, `221` (β-glucano = glucano total − α-glucano, enzimático), `218`.

### 2. Comparar dos COA con humedades distintas
**Síntoma:** "este proveedor da 28 % y el otro 22 %, me quedo con el de 28".
**Por qué pasa:** uno reporta base seca (dry basis) y el otro "tal cual" (as is) con 9 % de humedad. Sin base declarada, un porcentaje no es un dato: es una opinión.
**Qué cuesta:** eliges el peor proveedor creyendo que es el mejor, y con sobreprecio.
**Lo resuelve:** `07`, `04`, `98` (Karl Fischer), `lab-tools/base_seca.py`.

### 3. Creer que "10:1" dice algo del activo
**Síntoma:** te venden "extracto 10:1, máxima concentración" y no reportan ningún activo medido.
**Por qué pasa:** el ratio planta:extracto (plant-to-extract ratio) es una relación de **masa** del proceso, no de potencia. Diez kilos de materia pobre dan un kilo de extracto pobre, y sigue siendo 10:1.
**Qué cuesta:** compras un número de marketing; dos lotes "10:1" pueden diferir tres veces en activo.
**Lo resuelve:** `151`, `242`, `152` (estandarizar por activo medido, no por ratio).

### 4. Leer "no detectado" como "cero"
**Síntoma:** el COA dice "ND" en plomo y tú escribes "libre de metales pesados".
**Por qué pasa:** ND significa "por debajo del límite de detección **de ese** método". Un método flojo no detecta nada, y eso no es limpieza: es ceguera. Sin el LOQ impreso, el ND no se puede interpretar.
**Qué cuesta:** un claim indefendible y un riesgo real que quedó sin cuantificar dentro de tu producto.
**Lo resuelve:** `73`, `111`, `88` (ICP-MS y sus límites reales), `lab-tools/loq_lod.py`.

### 5. Hacer una especificación con un solo lote
**Síntoma:** el primer lote dio 24,1 % de β-glucano y la especificación queda "24,1 %".
**Por qué pasa:** se confunde un resultado con una capacidad de proceso. La variabilidad del hongo, del sustrato, del secado y del propio método ya suma varios puntos porcentuales.
**Qué cuesta:** el segundo lote sale "fuera de especificación" siendo normal, y se termina moviendo el criterio para que pase. Ahí la especificación dejó de significar algo.
**Lo resuelve:** `282`, `247`, `77` (cartas de control), `76` (incertidumbre de medida).

### 6. Aplicar mal el factor 0,877
**Síntoma:** el producto "cumple" con 0,28 % de Δ9-THC, pero el COA traía además 1,5 % de THCA que nadie sumó.
**Por qué pasa:** THC total = Δ9-THC + (THCA × 0,877). El factor es relación de masas molares (el THCA pierde un CO2 al descarboxilarse); se aplica **al THCA**, nunca al total ya calculado, y nunca dos veces.
**Qué cuesta:** volver ilegal un producto legal —o vender como legal lo que no lo es—, con pérdida del lote.
**Lo resuelve:** `175`, `174`, `213`, `lab-tools/thc_total.py`.

### 7. Arrastrar cifras significativas inventadas
**Síntoma:** el informe dice "22,4137 % de β-glucano".
**Por qué pasa:** se copia la salida cruda del software sin mirar la incertidumbre del método, que en un ensayo enzimático sobre matriz vegetal es de varias décimas.
**Qué cuesta:** credibilidad. Un químico ve cuatro decimales y deja de creerle al informe completo.
**Lo resuelve:** `05`, `76`, y ejecutar toda cuenta con `Matematicas_lushows`.

## Errores al conseguir el dato (8–13)

### 8. Aceptar la muestra que envía el proveedor
**Síntoma:** "él mismo la mandó al laboratorio y salió perfecta".
**Por qué pasa:** la muestra que manda el vendedor es la mejor que tiene, o directamente no es del lote que te va a despachar. Es el fraude más simple que existe y no requiere falsificar ningún papel.
**Qué cuesta:** compras un contenedor de un material distinto al que analizaste, con un COA auténtico.
**Lo resuelve:** `66` (muestreo propio), `109` (cadena de custodia), `284`, `111`.

### 9. Muestrear de encima del bulto
**Síntoma:** se toma un puñado de la boca del saco y se manda a analizar.
**Por qué pasa:** el polvo no es homogéneo; lo fino y lo pesado se separan en el transporte (segregación).
**Qué cuesta:** el resultado no representa el lote. Rechazas material bueno o liberas material malo, y en los dos casos el análisis que pagaste no sirvió para nada.
**Lo resuelve:** `66`, `67` (homogeneizar y moler antes de submuestrear).

### 10. Cuantificar sin patrón de referencia
**Síntoma:** "el laboratorio me dio el porcentaje", pero no hay estándar certificado detrás.
**Por qué pasa:** el patrón de referencia (reference standard) cuesta y a veces no existe comercialmente para el analito exacto; el laboratorio improvisa con un compuesto parecido o un factor de respuesta supuesto.
**Qué cuesta:** el número no es cuantificación sino estimación, y no aguanta impugnación ni auditoría.
**Lo resuelve:** `70`, `71`, `95` (qNMR para asignar contenido a un patrón sin certificar).

### 11. Confiar en la acreditación sin mirar el alcance
**Síntoma:** "el laboratorio es ISO/IEC 17025", en un ensayo que no está en su alcance acreditado.
**Por qué pasa:** la acreditación es **por ensayo y por matriz**, no por laboratorio. El sello del membrete no cubre automáticamente el ensayo que a ti te interesa.
**Qué cuesta:** un COA que no vale ante la autoridad ni ante un cliente institucional.
**Lo resuelve:** `107`, `108` (pedir el anexo de alcance y verificarlo con el organismo acreditador).

### 12. Repetir hasta que salga el número que quiero (lab shopping)
**Síntoma:** tres laboratorios, y en el expediente solo aparece el resultado más alto.
**Por qué pasa:** presión comercial. Es tan común en cannabis que ya se persigue: a 2026 varios estados de EE. UU. exigen auditorías de potencia y muestreo por terceros (cannabisregulations.ai, *Cannabis Lab Testing Standards Tighten in 2026*, 2026).
**Qué cuesta:** cuando aparece el historial —y aparece— deja de ser un error técnico y pasa a ser fraude.
**Lo resuelve:** `113`, `112` (impugnar bien, con laboratorio árbitro pactado de antemano), `77`.

### 13. No guardar contramuestra
**Síntoma:** el resultado salió raro y ya no queda material de ese lote para verificar nada.
**Por qué pasa:** nadie separó y selló una porción en el momento de muestrear.
**Qué cuesta:** te quedas sin poder impugnar; la discusión se vuelve palabra contra papel, y pierde la palabra.
**Lo resuelve:** `109`, `112`, `168`, `295` (bloque G).

## Errores al decidir con el dato (14–20)

### 14. Pedir el análisis después de imprimir la etiqueta
**Síntoma:** 5.000 etiquetas impresas que dicen "30 % de β-glucano", y el primer análisis da 19 %.
**Por qué pasa:** la etiqueta se diseña con el proveedor de arte y el análisis se trata como trámite final.
**Qué cuesta:** reimpresión completa, atraso del lanzamiento y, si el lote salió, retiro de producto. El orden correcto es: medir → especificar → escribir la etiqueta.
**Lo resuelve:** `293`, `272`, `282`, `295` (bloque E) y coordinar con `directorcreativo_lushows`.

### 15. Heredar el estudio clínico del ingrediente para tu producto
**Síntoma:** citas un ensayo con extracto estandarizado a 1.000 mg/día y tu cápsula tiene 200 mg de otra cosa.
**Por qué pasa:** se confunde "el compuesto tiene evidencia" con "mi producto tiene evidencia". Son dos afirmaciones distintas y solo una es tuya.
**Qué cuesta:** un claim sin sustanciación, que es justamente lo que se sanciona.
**Lo resuelve:** `12`, `161`, `293`, `248`, `288`.

### 16. Copiar el claim del competidor
**Síntoma:** "si ellos lo dicen, yo también puedo".
**Por qué pasa:** se asume que el mercado ya validó la frase. Lo que hay en el mercado no es lo permitido: es lo que todavía nadie ha revisado.
**Qué cuesta:** heredas completo el riesgo legal de alguien que ni siquiera conoces.
**Lo resuelve:** `267`, `268`, `276`, `293`.

### 17. Fijar la vida útil por analogía
**Síntoma:** "24 meses, como todos".
**Por qué pasa:** el estudio de estabilidad toma tiempo y nadie quiere esperar; se copia el número del competidor o el que sugirió el maquilador.
**Qué cuesta:** producto que pierde activo o gana humedad antes de vencerse. En Colombia (zona climática cálida-húmeda) un empaque flojo cambia el resultado en meses, no en años.
**Lo resuelve:** `164`, `165`, `163` (envase real), `35`, `lab-tools/vida_util_arrhenius.py`.

### 18. Cambiar sustrato, proveedor o proceso sin volver a medir
**Síntoma:** el lote nuevo "es el mismo producto", pero el sustrato pasó de aserrín a grano.
**Por qué pasa:** el cambio se decide por costo, en compras, y nunca llega a calidad.
**Qué cuesta:** el perfil químico cambia (sube α-glucano, baja β-glucano) y tu especificación deja de cumplirse sin que nadie sepa por qué.
**Lo resuelve:** `169` (control de cambios), `239`, `284`, `283`.

### 19. Escalar el lote suponiendo que el rendimiento se mantiene
**Síntoma:** en 2 kg el extracto rendía 12 %; en 200 kg rinde 7 % y con otro perfil.
**Por qué pasa:** la transferencia de calor, la relación solvente:sólido y los tiempos reales cambian con la escala. La química de laboratorio no es lineal hacia arriba.
**Qué cuesta:** costo por unidad descuadrado y un lote comercial que no cumple la especificación del piloto.
**Lo resuelve:** `166`, `06` (balance de masa), `287` (DoE); el impacto en costos, con `economist_lushows`.

### 20. Tener el sistema de calidad y no dejar rastro
**Síntoma:** "sí lo revisamos", pero no hay firma, ni fecha, ni registro.
**Por qué pasa:** el control se hace de memoria y el papel se llena al final del mes.
**Qué cuesta:** para un auditor, lo que no está escrito no ocurrió. Pierdes el registro por algo que sí hiciste.
**Lo resuelve:** `168`, `283`, `286`, `295`.

## Ejemplo aplicado (BIO-SETA)

Un proveedor ofrece "extracto de reishi 10:1, 40 % de polisacáridos" a USD 38/kg contra otro de "cuerpo
fructífero, β-glucano ≥ 20 % p/p base seca por método enzimático" a USD 96/kg **(ILUSTRATIVO)**. Con los
errores 1, 2 y 3 encima, el primero parece 2,5 veces mejor negocio. Al medir el β-glucano real del primero
—digamos 6 % p/p base seca **(ILUSTRATIVO)**— el costo por gramo de activo se invierte y el caro resulta
más barato. El análisis que resolvió la duda cuesta del orden de USD 120–180 por muestra **(ILUSTRATIVO)**:
menos que un solo saco del material equivocado. Verifica la cuenta con `Matematicas_lushows` antes de comprar.

## Los tres errores que producen los otros diecisiete

1. **Aceptar un número sin método, unidad y base.** Casi todo lo demás sale de ahí (`02`).
2. **Dejar que el documento reemplace la verificación.** Un COA es un papel comercial hasta que lo auditas
   y hasta que la muestra la tomaste tú (`110`, `111`).
3. **Poner el análisis al final.** El análisis no confirma decisiones: las toma. Cuando llega después de la
   etiqueta, del contrato o del contenedor, ya solo sirve para documentar el daño.

## Conexión con otros módulos

→ `295-checklist-de-calidad-quimica.md` — la lista que impide que estos errores ocurran.
→ `297-preguntas-frecuentes-del-emprendedor.md` — las mismas dudas, en forma de pregunta.
→ `111-banderas-rojas-en-un-coa.md` — cómo se ven estos errores dentro de un certificado.
→ `246-adulteracion-y-fraude-en-suplementos-de-hongos.md` — cuando el error es del otro lado y a propósito.
→ `298-plantillas-y-formatos.md` — los formatos que cierran cada hueco.
