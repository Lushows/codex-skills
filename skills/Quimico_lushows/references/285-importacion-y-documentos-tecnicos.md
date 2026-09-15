# 285 — Importación y documentos técnicos (los papeles sin los cuales tu materia prima se queda en el puerto)

Importar materia prima es la parte donde una marca pequeña pierde más plata por razones no químicas: el
contenedor llega, pero falta un documento, la carga se queda en depósito y cada día cuesta. La otra mitad
de las pérdidas es química: la carga entra bien pero el material no cumple, y devolverlo desde Colombia es
prácticamente imposible. Este módulo separa los dos frentes — el paquete documental y el control técnico
de entrada — y te dice qué exigir **antes** de que el proveedor embarque.

Términos: **COA (certificate of analysis)** = certificado de análisis del lote. **SDS/MSDS (safety data
sheet)** = ficha de datos de seguridad (`09`). **partida arancelaria (HS code)** = código de clasificación
aduanera que define impuestos y requisitos. **VUCE** = Ventanilla Única de Comercio Exterior de Colombia.
**certificado fitosanitario (phytosanitary certificate)** = documento sanitario vegetal del país de origen.
**declaración de importación** = documento aduanero con el que la mercancía nacionaliza.

## Los dos paquetes: comercial-aduanero y técnico

```
PAQUETE COMERCIAL/ADUANERO            PAQUETE TÉCNICO (el que te importa como químico)
- Factura comercial (invoice)          - COA del lote específico (110, 111)
- Lista de empaque (packing list)      - Especificación firmada del producto
- Documento de transporte (BL / AWB)   - SDS/MSDS en español si aplica (09)
- Certificado de origen (si hay TLC)   - Certificado GMP del fabricante
- Declaración de importación           - Declaración de composición y alérgenos (137)
- Registro/permiso sanitario si aplica - Declaración de no-OGM / no-irradiado si el cliente lo exige
- Certificado fitosanitario si aplica  - Declaración de solventes usados en la extracción (87, 201)
- Mandato aduanero / agente            - Flujograma del proceso de fabricación
```

Regla: **el paquete técnico se pide y se aprueba ANTES del embarque**, no cuando la carga ya está a bordo.
Una vez zarpó, tu poder de negociación es cero.

## Qué exige cada tipo de material (Colombia, a agosto de 2026)

| Material | Autoridad que suele intervenir | Documento crítico | Nota |
|---|---|---|---|
| Materia prima vegetal seca (hierba, hongo deshidratado) | ICA (sanidad vegetal) e INVIMA según uso | Certificado fitosanitario del país de origen (`271`) | El uso declarado define la autoridad |
| Extracto o polvo para suplemento dietario | INVIMA | Ficha técnica + COA + certificado de libre venta del origen | El producto terminado requiere registro sanitario (`269`) |
| Excipiente / aditivo | INVIMA | Grado alimentario o farmacéutico declarado, con farmacopea de referencia (`280`) | "Grado técnico" no sirve para consumo humano |
| Solvente para extracción | Autoridad de control de sustancias (fiscalización) | Certificado de calidad + control de precursores si aplica | Muchos solventes son sustancias controladas |
| Material de cannabis o derivado | Régimen de cannabis colombiano vigente | Licencias y cupos vigentes (`210`) | Cambió varias veces; verificar norma vigente antes de mover nada |
| Envase primario en contacto con producto | INVIMA | Declaración de aptitud para contacto con alimentos + migración (`163`) | Se olvida casi siempre |

**A agosto de 2026 verifica siempre la norma vigente** en la fuente oficial (INVIMA, ICA, DIAN/VUCE) antes
de comprometer una compra. Los requisitos y las partidas arancelarias cambian, y la responsabilidad de la
clasificación es del importador. Para la ruta operativa y los trámites del negocio, rutea a `AVIS_lushows`;
para el costeo del importe nacionalizado, a `contador_lushows`.

## El control técnico de entrada (lo que haces cuando llega)

Aunque los papeles estén perfectos, el material se verifica. Secuencia mínima:

1. **Inspección de la carga.** Estado de los bultos, sellos, evidencia de humedad, plagas, olor extraño.
   Fotografía todo antes de mover nada. Si hay daño, se deja constancia en el documento de transporte —
   después no se puede reclamar.
2. **Verificación de identidad documental.** Que el lote del COA sea **el mismo** que está impreso en los
   sacos. Un COA de otro lote no vale.
3. **Muestreo representativo.** Según plan de muestreo (`66`): no del bulto de encima. Para N bultos, la
   regla práctica √N + 1 unidades a muestrear es un punto de partida defendible.
4. **Cuarentena.** El material no entra a producción hasta la liberación firmada.
5. **Ensayos de entrada** según `283`: identidad, activo, humedad y, si el proveedor es nuevo o cambió el
   origen, seguridad (metales, micotoxinas, microbiología).
6. **Contramuestra retenida** sellada, con fecha, por al menos la vida útil declarada + 6 meses (`298`).
7. **Liberación o rechazo** firmado, con el resultado adjunto.

## Traducción y validez de los documentos

- Los documentos oficiales extranjeros suelen requerir **traducción oficial** al español y, según el país
  de origen, **apostilla** (Convenio de La Haya) o legalización consular. Pregúntalo antes: una apostilla
  tarda semanas.
- El COA puede venir en inglés; la ficha de seguridad para uso en Colombia debe estar **en español** y
  seguir el Sistema Globalmente Armonizado (SGA/GHS), conforme a la norma vigente a agosto de 2026 (`09`).
- El certificado de libre venta (free sale certificate) demuestra que el producto se comercializa
  legalmente en el país de origen. No demuestra calidad; solo legalidad allá.

## Incoterms: quién asume qué (y por qué le importa al químico)

| Incoterm | Quién paga el flete | Quién asume el riesgo en tránsito | Efecto práctico |
|---|---|---|---|
| EXW | Comprador | Comprador desde la bodega del vendedor | Máximo control, máximo trabajo |
| FOB | Comprador desde el puerto de origen | Comprador desde que sube al buque | El más común en compras pequeñas |
| CIF | Vendedor hasta puerto destino | Comprador desde carga, con seguro | Cuidado: el seguro cubre daño, no *fuera de especificación* |
| DDP | Vendedor | Vendedor hasta tu puerta | Cómodo y caro; útil para primeras compras |

Ningún Incoterm cubre que el material **no cumpla la especificación**. Eso solo lo cubre el contrato y la
cláusula de discrepancia analítica con laboratorio árbitro (`292`).

## Ejemplo aplicado (BIO-SETA)

Importación de 200 kg de extracto de melena de león desde Asia, FOB. Se exige antes del embarque: ficha
técnica firmada con especificación de β-glucano por método enzimático, COA del lote a embarcar, certificado
GMP, SDS en español, declaración de sustrato y declaración de solventes. Al llegar, se muestrea √N+1 sacos,
se analiza β-glucano y humedad y se verifica identidad ITS del primer lote.

Costeo aproximado del control de entrada **(ILUSTRATIVO)**: 1 identidad ITS + 1 β/α-glucano + 1 humedad +
1 paquete de metales, del orden de USD 400–800 por lote importado según laboratorio y país; una referencia
pública de tarifas de laboratorio contratado en EE. UU. muestra ensayos por HPLC en el rango de USD 290–425
por activo y metales por ICP-OES en USD 500–625 (lista de precios de CIA Labs, vigente desde el 2 de febrero
de 2025 — verificar cotización actual). Sobre 200 kg, ese control representa una fracción mínima del valor
de la carga y es la única forma de no descubrir el problema cuando ya está encapsulado.

## Errores comunes

- **Pagar el 100 % por adelantado** sin haber aprobado el paquete técnico ni una muestra pre-embarque.
- **Aceptar un COA de "lote de producción anterior"**. Se exige el COA del lote embarcado.
- **Clasificar mal la partida arancelaria** para pagar menos impuesto: es responsabilidad del importador y
  el ajuste posterior viene con sanción.
- **Olvidar el envase primario**: llega el producto pero no el frasco apto, o el frasco no tiene declaración
  de contacto con alimentos.
- **No pedir la declaración de solventes.** Si el extracto se hizo con metanol o hexano, cambia tu perfil de
  solventes residuales y tu riesgo (`87`).
- **No dejar constancia del daño en el puerto.** Sin la anotación en el documento de transporte, el seguro
  no responde.
- **Comprar "muestra especial" y luego producción distinta.** Analiza siempre el lote comercial.

## Conexión con otros módulos

→ `284-auditoria-de-proveedor.md` — el paso anterior: a quién le compras.
→ `283-plan-de-control-de-calidad-por-lote.md` — qué se ensaya cuando el material entra.
→ `66-plan-de-muestreo-y-representatividad.md` — cómo se muestrea un lote de N bultos.
→ `109-cadena-de-custodia-y-envio-de-muestras.md` — cómo mandar la muestra al laboratorio sin arruinarla.
→ `271-ica-y-materia-prima-vegetal.md` — el frente sanitario vegetal en Colombia.
→ `286-expediente-tecnico-del-producto.md` — dónde se archivan todos estos papeles.