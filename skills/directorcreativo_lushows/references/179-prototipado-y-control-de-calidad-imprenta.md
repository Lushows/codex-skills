# 179 — Prototipado y control de calidad de imprenta

Aquí es donde el dinero se gana o se pierde. Mandas a imprimir 5.000 cajas, llegan… y el color está apagado, el troquel no cierra, el foil está corrido. Ya pagaste. Este módulo te enseña a **prototipar antes y controlar durante** para que la tirada salga como la imaginaste. La regla sagrada de la producción gráfica: **nunca apruebes a ciegas, nunca apruebes en pantalla, nunca apruebes "de palabra".** Todo se valida sobre algo físico que puedas tocar y firmar.

**Términos en simple:**
- **Dummy / maqueta:** un ejemplar físico de prueba (caja, etiqueta) para sostener y revisar antes de imprimir miles.
- **Proof / prueba de color:** una impresión de muestra para aprobar el color exacto.
- **Aprobación de máquina (press check):** ir/recibir la primera hoja recién salida de la máquina para dar el OK antes de que corra toda la tirada.
- **Sangrado (bleed):** color que se extiende más allá del corte para que no queden bordes blancos (ver 92).
- **Registro:** que todos los colores/acabados caigan exactamente donde deben.

## Etapa 1 — El dummy físico (antes de imprimir)

Pide SIEMPRE un dummy en blanco (sin gráfica) o con gráfica impresa digital:
- **Estructura:** ¿la caja cierra firme? ¿el producto entra y no baila? ¿se arma rápido? (ver 170)
- **Tamaño real:** un envase se "siente" distinto en mano que en pantalla. Muchos errores de proporción solo se ven en físico.
- **Material:** ¿el gramaje se siente como querés? ¿el papel comunica lo correcto?
- Para e-commerce: arma la caja, mete el producto, **simula el envío** (zarándeala). ¿Protege?

Costo del dummy: bajo. Costo de NO hacerlo: una tirada entera mal. Siempre vale la pena.

## Etapa 2 — La prueba de color (proof)

El color en tu pantalla MIENTE (cada pantalla es distinta, y la pantalla es RGB; la impresión, CMYK — ver 32, 39). Tipos de proof:

| Tipo de proof | Qué tan fiel | Cuándo |
|---|---|---|
| **Proof digital calibrado (contractual)** | Alto, certificado de color | Estándar profesional, sirve como referencia firmada |
| **Proof sobre el sustrato real** | El más fiel | Cuando el color es crítico (color de marca) |
| **Impresión digital de muestra** | Aproximado | Tiradas chicas, validación rápida |

- Pide la prueba **sobre tu sustrato real** cuando puedas: el mismo CMYK se ve distinto en couché brillante vs. kraft (ver 171).
- Para colores de marca exactos, valida contra el **Pantone físico** bajo luz neutra (D50), no bajo luz de oficina.
- **Firma el proof aprobado.** Ese es el estándar contra el cual reclamas si la tirada no coincide.

## Etapa 3 — Aprobación de máquina (press check)

En tiradas grandes/importantes, la primera hoja que sale de la máquina debe aprobarse antes de correr todo:
- Ve a la imprenta o pide que te envíen/muestren la **primera hoja buena**.
- Compárala con tu proof firmado bajo luz neutra.
- Revisa: color, registro, nitidez, acabados (foil, relieve, spot UV en su lugar).
- Da el OK explícito. A partir de ahí corre la tirada — los errores que no detectaste aquí, ya son tuyos.

## Etapa 4 — Control de calidad de la tirada recibida

Cuando llega el lote, NO lo guardes sin revisar:
- [ ] Saca muestras al azar de distintas cajas del lote (inicio/medio/fin de tirada)
- [ ] Compara color contra el proof firmado
- [ ] Revisa registro (textos/acabados alineados)
- [ ] Revisa troquel/dobleces (cierra bien, no se raja el hendido)
- [ ] Revisa acabados (foil pegado, no se descascara; laminado sin burbujas)
- [ ] Verifica info legal completa y legible (registro sanitario, lote, código de barras escanea — ver 178)
- [ ] Cuenta: ¿llegó la cantidad pedida? (las imprentas declaran tolerancia de ±%)
- [ ] Documenta defectos con fotos para reclamar a tiempo

## Qué EXIGIR a la imprenta (tu lista de derechos)

- Dummy físico antes de tirada
- Proof de color sobre sustrato (firmado por ambas partes)
- Acceso o muestra de aprobación de máquina en tiradas grandes
- Especificación clara: sustrato, gramaje, técnica, tintas (CMYK/Pantone), acabados, tolerancia de cantidad y de color
- Cotización detallada (arranque vs. unitario — ver 171)
- Política de reposición si hay defecto de su lado

## Cómo entregar el archivo para que no te culpen a ti

La mitad de los errores son del archivo, no de la imprenta (ver 92, 93, 74):
- [ ] CMYK (no RGB), perfil de color correcto
- [ ] Sangrado de 3–5 mm en todos los bordes
- [ ] Tipografías trazadas/incrustadas, imágenes a resolución correcta (300 dpi en cerca; ver 177 para gran formato)
- [ ] Líneas de corte/dieline en capa separada, no impresas (ver 74)
- [ ] Capas separadas y marcadas para cada acabado (FOIL, SPOT_UV, RELIEVE — ver 172)
- [ ] PDF/X de alta para impresión, según pida la imprenta
- [ ] Negro de textos en negro puro o rico según corresponda

## Errores comunes
- [ ] Aprobar color en pantalla o por foto de celular
- [ ] No pedir dummy y descubrir que la caja no cierra con 5.000 ya hechas
- [ ] No firmar el proof (luego no hay con qué reclamar)
- [ ] Recibir el lote sin revisarlo y descubrir el defecto cuando ya vendiste
- [ ] Entregar archivo en RGB sin sangrado y culpar a la imprenta
- [ ] No verificar que el código de barras escanee de verdad

**Siguiente paso:** antes de tu próxima tirada, exige los tres físicos en orden — dummy estructural, proof de color sobre tu sustrato (fírmalo), y muestra de máquina — y revisa el lote recibido con la checklist. Asegúrate de entregar el archivo en CMYK con sangrado y capas de acabado separadas (ver 92, 74, 172). Esto cierra el bloque de producción física: ya sabes diseñar la estructura (170), imprimirla bien (171), elevarla (172), hacerla sostenible (173) y legal (178), y llevarla al punto de venta (174–177).
