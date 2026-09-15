# 292 — Negociar con laboratorios y maquiladores (qué exigir por contrato, cláusula por cláusula)

Casi todos los conflictos con un laboratorio o un maquilador se resuelven antes de que ocurran, en la
página donde se firma. El emprendedor negocia precio y plazo; el químico negocia **método, acreditación,
contramuestra y propiedad de los datos** — que es donde está el riesgo. Este módulo te da las cláusulas
concretas para poner sobre la mesa, en lenguaje que puedes copiar. El error caro que evita: quedarte sin
material para impugnar un resultado, o descubrir que el método que pagaste ahora se lo venden a tu
competencia.

Términos: **maquilador (contract manufacturer / CMO)** = fábrica que produce tu producto con tu marca.
**laboratorio contratado (contract lab / CRO analítica)** = quien hace tus análisis. **acuerdo de calidad
(quality agreement)** = anexo técnico del contrato que reparte responsabilidades. **contramuestra
(retained sample)** = porción sellada del mismo lote que se guarda. **datos crudos (raw data)** =
cromatogramas, espectros, hojas de trabajo — no el PDF resumen. **laboratorio árbitro (umpire lab)** =
tercero pactado para dirimir discrepancias.

## Antes de negociar: sepárate del vendedor

Pide siempre estas cinco cosas antes de hablar de precio. Filtran el 80 % de los problemas:

1. **Alcance de acreditación ISO 17025** en PDF, y señalar en él **el ensayo exacto y la matriz** que
   necesitas. Un laboratorio "acreditado" puede estarlo para agua y no para tu extracto (`107`).
2. **El método** que van a usar, con su referencia (AOAC, USP, EP, kit comercial, o método propio validado).
3. **El LOQ** (límite de cuantificación) para tu matriz. Un "no detectado" sin LOQ no significa nada (`73`).
4. **Un COA de ejemplo** de un producto parecido, con datos borrados. Ahí ves cómo reportan.
5. **Un COA de material de referencia certificado** o su desempeño en ensayos de aptitud
   (*proficiency testing*): la prueba de que su número se parece al del resto del mundo.

## Esqueleto del contrato con un LABORATORIO

Copia estas cláusulas y adáptalas con tu abogado. El lenguaje es el que importa, no la forma.

```
1. OBJETO Y ALCANCE
   1.1 El LABORATORIO ejecutará los ensayos listados en el Anexo A (parámetro, método con su referencia
       normativa, matriz, unidad, LOQ y criterio de aceptación).
   1.2 Cualquier cambio de método requiere aviso escrito y aceptación previa del CLIENTE.

2. COMPETENCIA TÉCNICA
   2.1 El LABORATORIO declara que los ensayos del Anexo A están DENTRO del alcance de su acreditación
       ISO/IEC 17025 vigente (adjunta certificado y alcance como Anexo B) y notificará cualquier
       suspensión o modificación en un plazo de [5] días hábiles.
   2.2 Los ensayos no acreditados se identificarán como tales en cada informe.
   2.3 El LABORATORIO participa en ensayos de aptitud (proficiency testing) para los parámetros
       críticos y entregará los resultados al CLIENTE a solicitud.

3. MUESTRAS Y CONTRAMUESTRAS
   3.1 La cadena de custodia se documentará desde la recepción (fecha, hora, estado, temperatura).
   3.2 El LABORATORIO conservará contramuestra en las condiciones declaradas por [90] días como mínimo,
       o hasta el cierre de cualquier controversia abierta.
   3.3 El CLIENTE conservará su propia contramuestra del mismo lote, sellada y fechada.

4. RESULTADOS Y DATOS
   4.1 El informe incluirá: identificación del lote, método y su referencia, unidad y base, LOQ,
       incertidumbre expandida, fecha de recepción y de análisis, y firma del responsable técnico.
   4.2 Los DATOS CRUDOS (cromatogramas, espectros, hojas de trabajo, curvas de calibración) son
       propiedad del CLIENTE y se entregarán en formato legible a solicitud, sin costo adicional.
   4.3 El LABORATORIO no divulgará resultados a terceros ni los usará en publicidad sin autorización
       escrita del CLIENTE.
   4.4 Si el LABORATORIO desarrolla un método a la medida financiado por el CLIENTE, la titularidad del
       método y su documentación de validación corresponde al CLIENTE.

5. PLAZOS
   5.1 TAT comprometido: [X] días hábiles desde la recepción conforme. Recargo por urgencia: [Y] %.
   5.2 Incumplimiento del TAT sin causa justificada: descuento de [Z] % sobre el valor del ensayo.

6. RESULTADOS FUERA DE ESPECIFICACIÓN Y DISCREPANCIAS
   6.1 Ante un OOS, el LABORATORIO ejecutará su procedimiento de investigación documentado y entregará
       el informe de investigación (no solo el resultado repetido).
   6.2 En caso de discrepancia entre las partes, se enviará la contramuestra al LABORATORIO ÁRBITRO
       [nombre pactado desde ya]. Su resultado será definitivo.
   6.3 Los costos del arbitraje los asume la parte cuyo resultado quede desvirtuado.

7. CONFIDENCIALIDAD, VIGENCIA Y TERMINACIÓN
   7.1 Confidencialidad por [5] años posteriores a la terminación.
   7.2 A la terminación, el LABORATORIO devuelve o destruye muestras y entrega copia de los datos crudos.
```

La cláusula 6.2 es la que más gente olvida y la que más plata salva: **el árbitro se pacta cuando hay buena
relación, no cuando ya hay pleito** (ver `112`).

## Esqueleto del contrato con un MAQUILADOR (cláusulas adicionales)

```
8.  FÓRMULA Y CONFIDENCIALIDAD
    8.1 La fórmula cuali-cuantitativa es propiedad exclusiva del CLIENTE; el MAQUILADOR no la usará para
        terceros ni para producto propio, durante la vigencia y por [5] años después.
    8.2 NDA firmado antes de recibir cualquier documento técnico (ver 290).

9.  ESPECIFICACIÓN Y CONTROL
    9.1 Anexo técnico con la especificación de producto terminado y de cada materia prima (282, 141).
    9.2 El MAQUILADOR entrega con cada lote: registro de lote, COA completo y trazabilidad de materias
        primas con sus COA de origen (168).
    9.3 El CLIENTE tiene derecho a auditoría en planta con [10] días de aviso, y a auditoría sin aviso
        ante una desviación crítica.

10. CONTROL DE CAMBIOS
    10.1 Ningún cambio de proveedor de materia prima, proceso, equipo, envase o sitio de fabricación se
         ejecuta sin aprobación escrita previa del CLIENTE (169).
    10.2 Un cambio no notificado faculta al CLIENTE a rechazar el lote completo con costo del MAQUILADOR.

11. LOTES, SOBRANTES Y MERMAS
    11.1 Tamaño mínimo de lote, rendimiento esperado y merma máxima aceptada, con su fórmula de cálculo.
    11.2 El excedente de producción es propiedad del CLIENTE y no puede venderse a terceros ni con otra
         marca. El material no conforme se destruye con acta.

12. RESPONSABILIDAD
    12.1 El MAQUILADOR responde por defectos atribuibles a fabricación; el CLIENTE, por el diseño de la
         fórmula y por los claims de etiqueta (293).
    12.2 Póliza de responsabilidad civil de producto vigente, con el CLIENTE como beneficiario adicional.
    12.3 Procedimiento de retiro de producto del mercado (recall) con responsables y tiempos.
```

## La tabla de "quién responde por qué" (acuerdo de calidad)

| Tema | Cliente (marca) | Maquilador |
|---|---|---|
| Diseño de la fórmula y su seguridad | X | |
| Claims de etiqueta y su soporte | X | |
| Especificación acordada | X (aprueba) | X (propone/ejecuta) |
| Compra y calificación de materia prima | Según contrato | Según contrato — **definirlo explícitamente** |
| Fabricación según master batch record | | X |
| Ensayos de liberación | | X (y entrega COA) |
| Decisión de liberar el lote | X (firma final recomendada) | X (técnica) |
| Estabilidad | X (paga y define) | X (ejecuta o coordina) |
| Retiro del mercado | X (decide y comunica) | X (soporta con trazabilidad) |

La fila que más pleitos genera es la cuarta. Déjala escrita en la primera reunión.

## Cómo se negocia el precio sin bajar la calidad

- **Compromete volumen anual**, no lote a lote: es la palanca más fuerte.
- **Agrupa en panel**: el mismo laboratorio hace potencia + microbiología + metales; ahorras logística y
  cadena de custodia (`109`).
- **Cede en plazo, no en método.** Aceptar 15 días en vez de 7 vale un descuento real (`291`).
- **Ofrece previsibilidad**: calendario de lotes del año entregado en enero.
- **Nunca negocies el LOQ ni la acreditación.** Si el precio bajo viene de un método menos específico, no
  estás ahorrando: estás comprando otro dato (`222`).

## Ejemplo aplicado (BIO-SETA)

Negociación con un laboratorio para el paquete anual de `291` (~USD 9.650 ILUSTRATIVO). Se pide: alcance
17025 marcado en β-glucano y metales, LOQ escrito, contramuestra 90 días, datos crudos del CLIENTE,
laboratorio árbitro pactado, TAT 10 días hábiles sin recargo. Se ofrece: 12 envíos programados al año y
pago a 15 días. Resultado esperado: descuento por volumen del 10–20 % **(ILUSTRATIVO)** y, más importante,
un contrato bajo el cual sí puedes impugnar un resultado.

## Errores comunes

- **Firmar solo la cotización.** Una cotización no tiene cláusula de contramuestra, ni de datos, ni de
  árbitro.
- **No verificar que el ensayo esté dentro del alcance** de la acreditación (`107`).
- **Dejar la fórmula en manos del maquilador sin NDA.** La verás en el mercado con otra marca.
- **No pactar el control de cambios**: el maquilador cambia de proveedor de excipiente y tu estabilidad
  deja de ser válida.
- **Aceptar solo el PDF del resultado.** Sin cromatograma no puedes auditar nada.
- **No definir quién compra la materia prima.** Es la ambigüedad más cara del contrato de maquila.
- **Pactar penalidades y no medirlas.** Si nadie lleva el registro de TAT, la cláusula es decorativa.

## Conexión con otros módulos

→ `108-como-elegir-un-laboratorio.md` — la selección previa a la negociación.
→ `107-iso-17025-y-acreditacion.md` — qué significa realmente "acreditado".
→ `112-como-impugnar-un-resultado.md` — el procedimiento que estas cláusulas habilitan.
→ `291-costos-de-analisis-y-presupuesto.md` — el volumen con el que negocias.
→ `290-propiedad-intelectual-y-patentes.md` — propiedad de método, datos y fórmula.
→ `298-plantillas-y-formatos.md` — la solicitud de análisis y la carta de impugnación.