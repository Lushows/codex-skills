# DESIGN — Quimico_lushows

> Documento de diseño y **contrato de estilo**. Todo módulo de `references/` debe cumplirlo.
> Fecha de diseño: 11 de agosto de 2026.

## Qué es esta skill

Convierte a Claude en un **químico-farmacéutico de élite** capaz de hablar de tú a tú con un químico
académico (el profesor de la UDCA que acompaña a BIO-SETA) y, al mismo tiempo, de explicarle todo a
Lushows, que no es químico.

Cubre química general, fisicoquímica, orgánica, productos naturales, **química analítica (el corazón)**,
bioquímica, farmacología, toxicología, tecnología farmacéutica/galénica y cumplimiento regulatorio —
con **foco declarado en cannabis y hongos (funcionales/adaptógenos y psilocibios)**.

## La promesa central (no negociable)

> **Ningún dato químico sin método, sin unidad y sin fuente.**

Nunca "el reishi tiene 30% de beta-glucanos". Siempre: *"β-glucano total 30,2 % p/p en base seca, medido
por Megazyme K-YBGL (enzimático, β-glucano = glucano total − α-glucano), sobre extracto de cuerpo
fructífero; este COA lo reporta así y este otro reporta 'polisacáridos', que no es lo mismo."*

## Los 5 pilares del carácter

1. **Método, unidad y fuente.** Un número sin método es publicidad, no ciencia.
2. **Nivel de evidencia explícito.** In vitro ≠ ratón ≠ ensayo clínico ≠ testimonio. Se dice siempre cuál es.
3. **No inventar datos.** Si no se sabe el valor, se dice "hay que medirlo" y se explica **cómo**. Cualquier
   cifra de ejemplo va marcada como **ILUSTRATIVA**.
4. **Cálculos a código.** Toda cuenta que importe se ejecuta y se verifica (regla de `Matematicas_lushows`).
5. **Cumplimiento como parte de la química.** Un producto que no puede sostener su claim con un método
   analítico es un problema legal, no solo científico.

## Línea roja (psilocibios)

Se cubre: química, análisis, estabilidad, farmacología, farmacocinética, dosis usadas en investigación
clínica, screening de seguridad, psicometría, diseño de estudio, ética y estado legal por país.
**No se dan** protocolos de producción, cultivo, extracción o síntesis para uso ilícito, ni guías para
evadir controles. La frontera es: *entender, analizar e investigar legalmente* sí; *producir para el mercado
negro* no.

## Estructura de archivos

```
Quimico_lushows/
  SKILL.md              ← carácter, flujo de trabajo, ruteo, índice
  DESIGN.md             ← este archivo
  references/           ← 300 módulos (000–299)
  lab-tools/            ← calculadoras Python verificadas + README
```

## CONTRATO DE ESTILO (obligatorio para cada módulo)

**Formato del archivo:** `NNN-slug-en-kebab-case.md` (numeración de 2–3 dígitos, sin ceros a la izquierda
más allá de 2 dígitos: `07-…`, `115-…`).

**Extensión:** entre **90 y 170 líneas**. Denso, no relleno. Si un tema no da para 90 líneas, se profundiza
con tabla de datos reales, ejemplo numérico o caso — no se infla con paja.

**Idioma:** español de Colombia, claro, directo, tuteando al lector. Cada término técnico se define la
**primera vez** que aparece y se pone su nombre en inglés entre paréntesis, porque con el laboratorio se
habla en inglés. Ej: *"cuerpo fructífero (fruiting body)"*.

**Esqueleto de cada módulo:**

```markdown
# NNN — Título claro (qué resuelve, en cristiano)

Párrafo de entrada: qué es esto, por qué le importa a alguien que vende o desarrolla un producto,
y qué error caro evita. 4–8 líneas, sin jerga sin traducir.

Términos: **término (english term)** = definición corta. (Los 2–5 que hacen falta para leer el módulo.)

## [Secciones de fondo — las que el tema pida]

Usa TABLAS para datos comparables (método vs método, especie vs especie, límite vs límite).
Usa BLOQUES DE CÓDIGO para fórmulas, cálculos ejecutables y ejemplos de cromatograma/reporte.
Usa listas solo cuando de verdad es una lista.

## Cómo se mide / cómo se comprueba
(Si el módulo describe una sustancia, propiedad o claim: SIEMPRE la sección de cómo se mide,
con método, técnica, unidad y orden de magnitud esperado.)

## Ejemplo aplicado
Un caso concreto — de preferencia BIO-SETA (hongos) o cannabis — con números marcados
**(ILUSTRATIVO)** si no vienen de una fuente citada.

## Errores comunes
4–6 viñetas de lo que la gente hace mal en la vida real, y qué cuesta.

## Conexión con otros módulos
→ `NNN-otro-modulo.md` — por qué te llevaría ahí.
```

**Reglas duras de contenido:**

- **Unidades siempre**, y con la base explícita: `% p/p base seca`, `mg/g`, `ppm`, `µg/kg`, `mg/mL`.
- **Nada de cifras inventadas presentadas como hechos.** Rangos de literatura → di "reportado en la
  literatura, verificar con tu lote". Cifras de ejemplo → marca **(ILUSTRATIVO)**.
- **Nivel de evidencia marcado** al hablar de efectos: `[in vitro]`, `[animal]`, `[clínico fase N]`,
  `[tradicional/anecdótico]`.
- **Sin claims de enfermedad.** Nunca se escribe que algo "cura", "previene" o "trata" una enfermedad.
  Se describe lo que la evidencia muestra y se aclara qué se puede decir legalmente (ver bloque 265–299).
- **Fechas explícitas** en todo lo regulatorio: "a agosto de 2026…". La regulación cambia; el módulo debe
  envejecer con honestidad y decir dónde verificar el dato vigente.
- **Sin emojis** dentro de los módulos (el SKILL.md sí los usa en tablas de modo).
- **No dupliques otro módulo**: si el tema es de otro, enlázalo. Cada módulo tiene un dueño.

**Ruteo a otras skills del ecosistema (mencionarlo cuando aplique, no duplicar):**
`Matematicas_lushows` (cualquier cálculo que importe) · `contador_lushows` (costos, inventario, papeles
contables) · `economist_lushows` (precio, viabilidad, unit economics) · `AVIS_lushows` (cumplimiento
operativo colombiano) · `directorcreativo_lushows` (etiqueta y empaque) · `ventas_lushows` (cómo se
comunica al cliente) · `desingweb-lushows` (web).

## ÍNDICE COMPLETO — 300 módulos

### A. Método del químico (00–14) — 15
```
00-metodo-del-quimico.md
01-como-usar-esta-skill.md
02-ningun-dato-sin-metodo.md
03-honestidad-cientifica-y-fuentes.md
04-unidades-concentraciones-y-conversiones.md
05-cifras-significativas-e-incertidumbre.md
06-estequiometria-y-balance-de-masa.md
07-base-seca-vs-humeda.md
08-seguridad-de-laboratorio-y-epp.md
09-fichas-de-seguridad-sds-y-ghs.md
10-glosario-quimico-esencial.md
11-como-leer-un-paper-cientifico.md
12-niveles-de-evidencia.md
13-ruteo-a-otras-skills.md
14-como-trabajar-con-un-quimico-de-universidad.md
```

### B. Química general y fisicoquímica (15–39) — 25
```
15-atomo-y-tabla-periodica.md
16-enlace-quimico-y-geometria.md
17-polaridad-y-fuerzas-intermoleculares.md
18-estados-de-la-materia-y-transiciones.md
19-soluciones-y-solubilidad.md
20-parametros-de-solubilidad-y-eleccion-de-solvente.md
21-equilibrio-quimico.md
22-acidos-bases-y-ph.md
23-buffers-y-control-de-ph.md
24-oxido-reduccion.md
25-termodinamica-quimica.md
26-cinetica-de-reaccion.md
27-catalisis-y-enzimas.md
28-gases-y-presion-de-vapor.md
29-destilacion-y-equilibrio-liquido-vapor.md
30-extraccion-liquido-liquido-y-logp.md
31-principio-de-la-cromatografia.md
32-coloides-emulsiones-y-espumas.md
33-tensioactivos-y-hlb.md
34-reologia-y-viscosidad.md
35-actividad-de-agua-y-humedad.md
36-quimica-inorganica-y-metales-relevantes.md
37-electroquimica-y-electrodos.md
38-radiactividad-en-alimentos-y-plantas.md
39-quimica-computacional-para-no-especialistas.md
```

### C. Orgánica y productos naturales (40–64) — 25
```
40-grupos-funcionales.md
41-nomenclatura-organica.md
42-isomeria-y-estereoquimica.md
43-quiralidad-y-enantiomeros.md
44-mecanismos-de-reaccion-basicos.md
45-reacciones-de-sintesis-frecuentes.md
46-hidrolisis-esterificacion-y-saponificacion.md
47-oxidacion-y-degradacion-de-productos-naturales.md
48-metabolitos-primarios-vs-secundarios.md
49-terpenos-y-terpenoides.md
50-alcaloides.md
51-polifenoles-y-flavonoides.md
52-polisacaridos-y-glucanos.md
53-lipidos-y-acidos-grasos.md
54-aminoacidos-peptidos-y-proteinas.md
55-esteroles-y-triterpenos.md
56-quinonas-y-pigmentos.md
57-vitaminas-y-cofactores.md
58-rutas-biosinteticas-mevalonato-y-mep.md
59-ruta-del-shikimato-y-policetidos.md
60-quimiotaxonomia-y-marcadores.md
61-estabilidad-quimica-luz-calor-oxigeno.md
62-maillard-y-pardeamiento.md
63-quimica-verde-y-solventes.md
64-derivatizacion-para-analisis.md
```

### D. Química analítica (65–114) — 50
```
65-el-metodo-analitico-de-punta-a-punta.md
66-plan-de-muestreo-y-representatividad.md
67-homogeneizacion-y-molienda-de-muestra.md
68-preparacion-de-muestra-solidos.md
69-extraccion-para-analisis-spe-y-quechers.md
70-patrones-de-referencia-y-trazabilidad.md
71-curva-de-calibracion.md
72-estandar-interno-y-adicion-de-estandar.md
73-lod-loq-y-rango-lineal.md
74-exactitud-precision-y-recuperacion.md
75-validacion-de-metodos-ich-q2-r2.md
76-incertidumbre-de-medida.md
77-control-de-calidad-analitico-y-cartas-control.md
78-estadistica-para-el-laboratorio.md
79-hplc-y-uhplc.md
80-deteccion-uv-dad-y-pureza-de-pico.md
81-columnas-fases-y-desarrollo-de-metodo-lc.md
82-espectrometria-de-masas-fundamentos.md
83-lc-ms-ms-y-mrm.md
84-hrms-qtof-orbitrap-e-identificacion.md
85-cromatografia-de-gases.md
86-gc-ms-y-headspace.md
87-solventes-residuales.md
88-icp-ms-y-metales-pesados.md
89-absorcion-atomica-y-alternativas.md
90-espectroscopia-uv-visible.md
91-metodos-colorimetricos-y-enzimaticos.md
92-ftir-y-nir.md
93-espectroscopia-raman.md
94-rmn-fundamentos.md
95-qnmr-cuantificacion-absoluta.md
96-tlc-y-hptlc.md
97-electroforesis-capilar.md
98-karl-fischer-y-humedad.md
99-analisis-termico-dsc-y-tga.md
100-microbiologia-de-producto.md
101-analisis-de-micotoxinas.md
102-pesticidas-multiresiduo.md
103-identidad-por-adn-its-y-barcoding.md
104-metabolomica-y-huella-quimica.md
105-quimiometria-pca-y-modelos.md
106-analisis-de-agua-y-materias-primas.md
107-iso-17025-y-acreditacion.md
108-como-elegir-un-laboratorio.md
109-cadena-de-custodia-y-envio-de-muestras.md
110-como-leer-un-coa.md
111-banderas-rojas-en-un-coa.md
112-como-impugnar-un-resultado.md
113-lab-shopping-e-inflacion-de-potencia.md
114-costos-y-tiempos-de-analisis.md
```

### E. Bioquímica, farmacología y toxicología (115–139) — 25
```
115-bioquimica-celular-esencial.md
116-enzimas-y-cinetica-de-michaelis-menten.md
117-metabolismo-energetico.md
118-receptores-y-transduccion-de-senal.md
119-farmacodinamia-y-dosis-respuesta.md
120-afinidad-eficacia-y-agonismo-parcial.md
121-farmacocinetica-adme.md
122-biodisponibilidad-y-efecto-de-primer-paso.md
123-vias-de-administracion.md
124-citocromo-p450-e-interacciones.md
125-metabolismo-de-fase-ii.md
126-vida-media-y-regimen-de-dosis.md
127-barrera-hematoencefalica.md
128-serotonina-y-receptor-5ht2a.md
129-sistema-endocannabinoide.md
130-inmunomodulacion-y-beta-glucanos.md
131-eje-intestino-cerebro-y-microbiota.md
132-adaptogenos-que-significa-realmente.md
133-estres-oxidativo-y-antioxidantes.md
134-toxicologia-basica-dosis-y-riesgo.md
135-noael-ida-y-limites-de-exposicion.md
136-toxicidad-de-metales-pesados.md
137-alergenos-e-hipersensibilidad.md
138-farmacovigilancia-y-eventos-adversos.md
139-interacciones-planta-farmaco.md
```

### F. Tecnología farmacéutica, galénica y GMP (140–169) — 30
```
140-de-la-materia-prima-al-producto.md
141-especificacion-de-materia-prima.md
142-secado-y-conservacion-de-biomasa.md
143-molienda-y-granulometria.md
144-extraccion-acuosa-y-decoccion.md
145-extraccion-hidroalcoholica-y-tinturas.md
146-extraccion-dual-y-por-que-importa.md
147-ultrasonido-microondas-y-enzimas.md
148-co2-supercritico.md
149-concentracion-y-evaporacion.md
150-secado-por-aspersion-y-liofilizacion.md
151-relacion-planta-extracto-y-ratios.md
152-estandarizacion-de-extractos.md
153-formas-farmaceuticas-panorama.md
154-capsulas-y-encapsulado.md
155-tabletas-y-compresion.md
156-liquidos-goteros-y-jarabes.md
157-emulsiones-y-nanoemulsiones.md
158-liposomas-y-ciclodextrinas.md
159-potenciadores-de-biodisponibilidad.md
160-excipientes-y-compatibilidad.md
161-dosis-y-tamano-de-porcion.md
162-enmascaramiento-de-sabor.md
163-envase-primario-y-compatibilidad.md
164-estabilidad-ich-q1-y-vida-util.md
165-estudios-acelerados-y-arrhenius.md
166-escalado-de-lote.md
167-bpm-gmp-para-suplementos.md
168-documentacion-de-lote-y-trazabilidad.md
169-control-de-cambios-y-desviaciones.md
```

### G. Cannabis (170–214) — 45
```
170-cannabis-botanica-y-quimiotipos.md
171-genetica-y-variedades.md
172-biosintesis-de-cannabinoides.md
173-formas-acidas-thca-y-cbda.md
174-descarboxilacion-cinetica-y-calculo.md
175-thc-total-y-el-factor-0877.md
176-cbd-quimica-y-propiedades.md
177-cbg-cbc-y-cbn.md
178-thcv-cbdv-y-varinas.md
179-thcp-cbdp-y-homologos.md
180-delta8-delta10-e-isomerizacion.md
181-hhc-thco-y-semisinteticos.md
182-terpenos-del-cannabis.md
183-efecto-sequito-que-dice-la-evidencia.md
184-flavonoides-y-otros-componentes.md
185-cultivo-y-perfil-quimico.md
186-cosecha-secado-y-curado.md
187-extraccion-con-etanol.md
188-extraccion-con-hidrocarburos.md
189-extraccion-co2-en-cannabis.md
190-solventless-rosin-y-hash.md
191-winterizacion-y-desceramiento.md
192-destilacion-de-cannabinoides.md
193-cromatografia-preparativa-y-aislados.md
194-remediacion-de-thc.md
195-formulacion-de-aceites-y-comestibles.md
196-topicos-y-transdermicos.md
197-vapeo-quimica-y-riesgos.md
198-analisis-de-potencia-metodo.md
199-analisis-de-perfil-de-terpenos.md
200-pesticidas-en-cannabis.md
201-solventes-residuales-en-cannabis.md
202-metales-pesados-en-cannabis.md
203-micotoxinas-y-microbiologia-en-cannabis.md
204-estabilidad-y-degradacion-del-thc.md
205-farmacologia-del-thc.md
206-farmacologia-del-cbd.md
207-evidencia-clinica-del-cannabis-2026.md
208-dosificacion-y-titulacion.md
209-seguridad-interacciones-y-contraindicaciones.md
210-cannabis-medicinal-en-colombia.md
211-hemp-y-cbd-en-estados-unidos-2026.md
212-cannabis-y-cbd-en-europa.md
213-como-leer-un-coa-de-cannabis.md
214-montar-una-linea-de-producto-de-cannabis.md
```

### H. Hongos: funcionales, adaptógenos y psilocibios (215–264) — 50
```
215-panorama-de-hongos-funcionales.md
216-biologia-fungica-y-ciclo-de-vida.md
217-micelio-vs-cuerpo-fructifero.md
218-el-fraude-del-micelio-en-grano.md
219-beta-glucanos-quimica-y-estructura.md
220-alfa-glucanos-y-almidon-el-confusor.md
221-medir-beta-glucanos-metodo-megazyme.md
222-polisacaridos-totales-por-que-no-sirve.md
223-reishi-ganoderma-quimica.md
224-triterpenos-ganodericos-analisis.md
225-melena-de-leon-hericium-quimica.md
226-hericenonas-y-erinacinas-analisis.md
227-cordyceps-quimica.md
228-cordicepina-y-adenosina-analisis.md
229-chaga-inonotus-quimica.md
230-chaga-riesgos-oxalato-y-radiocesio.md
231-cola-de-pavo-trametes-psk-y-psp.md
232-maitake-y-fraccion-d.md
233-shiitake-y-lentinan.md
234-agaricus-y-otras-especies.md
235-ergotioneina.md
236-vitamina-d2-y-tratamiento-uv.md
237-nucleosidos-y-nucleotidos-fungicos.md
238-ergosterol-como-marcador.md
239-sustrato-cultivo-y-quimica-resultante.md
240-secado-y-perdida-de-activos.md
241-extraccion-de-hongos-agua-vs-alcohol.md
242-ratios-de-extraccion-y-etiquetado-honesto.md
243-metales-pesados-en-hongos.md
244-micotoxinas-y-contaminacion-en-hongos.md
245-identidad-de-especie-por-its.md
246-adulteracion-y-fraude-en-suplementos-de-hongos.md
247-especificacion-de-producto-de-hongos.md
248-evidencia-clinica-de-hongos-funcionales-2026.md
249-dosificacion-de-hongos-funcionales.md
250-seguridad-e-interacciones-de-hongos.md
251-psilocibina-y-psilocina-quimica.md
252-baeocistina-y-otros-alcaloides-relacionados.md
253-biosintesis-de-psilocibina.md
254-variabilidad-de-potencia-entre-especies.md
255-estabilidad-y-degradacion-de-psilocibina.md
256-analisis-de-psilocibina-hplc-y-lc-ms.md
257-farmacologia-de-la-psilocibina.md
258-farmacocinetica-de-psilocibina.md
259-dosis-en-investigacion-clinica.md
260-screening-de-seguridad-y-contraindicaciones.md
261-psicometria-meq30-5d-asc-y-escalas.md
262-set-setting-y-diseno-de-estudio.md
263-estado-clinico-y-regulatorio-2026.md
264-microdosis-que-dice-la-evidencia.md
```

### I. Cumplimiento, calidad, negocio y entrega (265–299) — 35
```
265-mapa-regulatorio-global.md
266-invima-y-suplementos-dietarios.md
267-decreto-3249-y-que-puedo-decir.md
268-claims-prohibidos-el-caso-bioseta.md
269-registro-sanitario-paso-a-paso-colombia.md
270-fitoterapeuticos-vs-suplementos.md
271-ica-y-materia-prima-vegetal.md
272-etiquetado-en-colombia.md
273-fda-dshea-y-suplementos.md
274-cgmp-21-cfr-111.md
275-ndi-e-ingredientes-nuevos-en-eeuu.md
276-claims-estructura-funcion-y-ftc.md
277-efsa-y-health-claims.md
278-novel-food-hongos-y-cannabis.md
279-eu-gmp-y-farmacopea-europea.md
280-farmacopeas-usp-ep-y-monografias.md
281-metodos-oficiales-aoac.md
282-especificacion-de-producto-terminado.md
283-plan-de-control-de-calidad-por-lote.md
284-auditoria-de-proveedor.md
285-importacion-y-documentos-tecnicos.md
286-expediente-tecnico-del-producto.md
287-diseno-de-experimentos-doe.md
288-como-disenar-un-estudio-piloto.md
289-etica-de-la-investigacion-y-consentimiento.md
290-propiedad-intelectual-y-patentes.md
291-costos-de-analisis-y-presupuesto.md
292-negociar-con-laboratorios-y-maquiladores.md
293-como-comunicar-ciencia-sin-mentir.md
294-informe-tecnico-y-pdf.md
295-checklist-de-calidad-quimica.md
296-errores-comunes-del-oficio.md
297-preguntas-frecuentes-del-emprendedor.md
298-plantillas-y-formatos.md
299-tendencias-en-quimica-y-analisis-2026.md
```

## lab-tools/ — calculadoras verificadas

Python 3, `decimal` para todo lo que sea dinero o límite regulatorio, cada script ejecutable por CLI y con
autotest (`--test`) que compara contra valores conocidos. Nada de aritmética mental.

```
lab-tools/README.md
lab-tools/decarboxilacion.py        THCA→THC, factor 0,877, cinética por tiempo/temperatura
lab-tools/thc_total.py              THC total y cumplimiento por envase (0,3 % p/p; 0,4 mg/envase EE.UU.)
lab-tools/diluciones.py             C1V1, series, curva de calibración con regresión y R²
lab-tools/rendimiento_extraccion.py rendimiento, factor de concentración, ratio planta:extracto
lab-tools/betaglucano_dosis.py      de % en COA a mg por cápsula y por porción diaria
lab-tools/base_seca.py              base húmeda ↔ base seca, corrección por humedad
lab-tools/vida_util_arrhenius.py    vida útil por estudio acelerado (Arrhenius, Q10)
lab-tools/unidades.py               % ↔ mg/g ↔ ppm ↔ mg/porción, con validación de base
lab-tools/loq_lod.py                LOD/LOQ desde curva y desde ruido, con criterios ICH
lab-tools/potencia_formula.py       cuánto extracto poner para alcanzar X mg de activo por unidad
```

## Verificación de aceptación

- [ ] 300 archivos en `references/`, numeración 000–299 sin huecos ni duplicados
- [ ] Cada módulo entre 90 y 170 líneas, con el esqueleto del contrato
- [ ] Cero claims de enfermedad; toda afirmación de efecto con nivel de evidencia marcado
- [ ] Todo dato regulatorio fechado ("a agosto de 2026")
- [ ] `lab-tools/*.py` pasan su `--test`
- [ ] `SKILL.md` indexa los 300 y explica el ruteo