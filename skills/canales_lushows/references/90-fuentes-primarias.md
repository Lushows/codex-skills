# 90 · Fuentes primarias

**Qué resuelve:** de dónde salen los hechos de un episodio. Un documental de dinero se
sostiene sobre documentos públicos, no sobre artículos que citan a otros artículos.

---

## La jerarquía de la prueba

| Nivel | Qué es | Cómo se usa |
|---|---|---|
| **1. Documento judicial o regulatorio** | Acusación, demanda, sentencia, orden de decomiso, designación de sanciones | Es la cifra que se pone en pantalla |
| **2. Informe oficial** | GAO, comisión del Congreso, síndico o examinador de la quiebra, banco central | Da contexto y totales que ningún periodista calculó |
| **3. Nota de prensa del organismo** | Comunicado del DOJ, del SEC, del Tesoro | Resumen fiable **del propio organismo**; siempre lleva enlace al documento nivel 1 |
| **4. Prensa seria** | Reportajes de investigación | Sirve para **encontrar** el documento, no para citarlo. Rastrear hasta el nivel 1 |
| **5. Vídeos, wikis, hilos, recopilaciones** | — | **No son fuente.** Sólo pistas para buscar |

**Regla:** si un dato no puede subir al nivel 1 o 2, o se reformula como atribución
explícita ("según la acusación del fiscal") o se cae del guion.

## El mapa de fuentes

### Justicia penal de EE.UU.
- **justice.gov** — sala de prensa del Departamento de Justicia y de cada fiscalía de
  distrito (*U.S. Attorney's Office*). Cada comunicado suele adjuntar el PDF de la
  acusación o del acuerdo. Es el punto de entrada más rápido para un caso federal.
- **vault.fbi.gov** — el archivo desclasificado del FBI (*The Vault*). Expedientes
  históricos completos, escaneados. Obra del gobierno federal: **dominio público**.
- **PACER** (`pacer.uscourts.gov`) — el expediente completo de cualquier caso federal.
  De pago por página y con registro.
- **CourtListener** (`courtlistener.com`) — de la Free Law Project. Sentencias y, a
  través de su archivo RECAP, expedientes de PACER ya liberados. **Gratis.** Es la vía
  normal de trabajo; PACER sólo cuando allí no está.
- **govinfo.gov** — publicaciones oficiales autenticadas del gobierno de EE.UU.

### Regulación financiera
- **SEC EDGAR** (`sec.gov/edgar`) — todo lo que una empresa cotizada presentó jamás:
  10-K, 10-Q, 8-K, S-1, proxy. Aquí están las cifras **que la propia empresa firmó**
  antes de caer. Tiene buscador de texto completo sobre los documentos.
- **SEC — litigation releases y administrative proceedings** (en `sec.gov`, sección de
  cumplimiento/litigios). Cada acción de la SEC con su demanda en PDF.
- **CFTC**, **FinCEN**, **OCC**, **FDIC**, **Reserva Federal** — acciones de
  cumplimiento contra intermediarios, bancos y casas de derivados.
- **FTC** (`ftc.gov`) — casos de fraude al consumidor, esquemas piramidales y
  publicidad engañosa, con la demanda y la orden final.

### Dinero, sanciones y activos
- **Departamento del Tesoro / OFAC** — designaciones de personas y empresas (lista
  SDN). Una designación explica **la estructura**: qué sociedad pantalla pertenece a
  quién. Buscador público de sanciones en el sitio del Tesoro.
- **IRS-CI** — la investigación criminal del fisco publica sus casos; en fraudes es
  la unidad que reconstruye el flujo de dinero.
- **Órdenes de decomiso y demandas civiles de decomiso** — el DOJ demanda a los bienes
  ("Estados Unidos contra un apartamento en..."). Estos documentos son un inventario
  detallado de lo comprado con el dinero: oro para el canal.

### Supervisión y contexto
- **GAO** (`gao.gov`) — informes de la oficina de fiscalización del Congreso. Explican
  cómo falló el sistema, con números agregados.
- **congress.gov** — proyectos de ley, y sobre todo **audiencias e informes de
  comisión**: las investigaciones del Senado y de la Cámara producen los mejores
  informes narrativos que existen sobre un escándalo financiero.
- **Informes de examinador o de síndico en la quiebra** — cuando una empresa grande
  cae, el tribunal nombra a alguien a reconstruir qué pasó. Son cientos de páginas de
  contabilidad forense. Se consiguen en el expediente de la quiebra o en la web del
  agente de reclamaciones (*claims agent*) que administra el caso, gratis.

### Fuera de EE.UU.
No hay dominio público federal equivalente. Se busca: el regulador del mercado, el
banco central, la comisión parlamentaria de investigación, el boletín oficial y las
sentencias publicadas. **Ojo:** en muchos países el material oficial **sí** tiene
derechos (Crown copyright y equivalentes). Sirve como *fuente del dato*, no como
*material de archivo* reutilizable.

### Archivo visual libre (dato ≠ imagen)
- **catalog.archives.gov** (NARA), **loc.gov** (Biblioteca del Congreso),
  **images.nasa.gov**, sitios de agencias federales (DEA, FBI, DOJ).
- **commons.wikimedia.org** — con la licencia **verificada pieza por pieza**, nunca por
  el hecho de estar en Commons.
- **archive.org** — útil para localizar; cada ítem tiene su propia licencia.

## Cómo se busca de verdad

1. Del nombre al **caso**: buscar el apellido + "indictment", "complaint",
   "sentenced", "forfeiture" en el sitio del organismo, no en un buscador general.
2. Del caso al **número de expediente** (*docket number*). Con ese número se abre todo
   lo demás en CourtListener.
3. Del expediente a los **documentos con cifras**: acuerdo de culpabilidad, memorandos
   de sentencia, orden de decomiso (§ `91`).
4. De la empresa a **EDGAR**: la última presentación antes del derrumbe suele contener
   la mentira por escrito.
5. Guardar **el PDF**, no el enlace: los sitios se reorganizan y el episodio queda sin
   respaldo. El PDF va a `archivo/` con su ficha.

## Cómo se cita

En `archivo/fuentes.json`, una entrada por pieza:

```json
{
  "id": "doj-acusacion-2019",
  "tipo": "documento",
  "titulo": "Acusación · Estados Unidos v. <nombre>",
  "organismo": "Department of Justice",
  "expediente": "<número de caso y distrito>",
  "fecha": "<fecha del documento>",
  "url": "<URL exacta de descarga>",
  "licencia": "dominio público (obra del gobierno federal de EE.UU.)",
  "archivo_local": "archivo/docs/doj-acusacion-2019.pdf",
  "usado_en": ["dato:total-incautado", "plano:07"]
}
```

En la descripción del vídeo se citan las fuentes de nivel 1 y 2 con su enlace (§ `99`).
En pantalla, la cifra lleva **rótulo de fuente** en pequeño: organismo + año.

## El sondeo de archivo: `sondeo.py`

El criterio 4 del banco (`97`) —*el archivo es libre*— es el que mata más casos y el que
menos se comprueba a tiempo. El script consulta Wikimedia Commons y **sólo deja pasar lo
que tiene licencia libre verificada**. Se ejecuta ANTES de escribir una sola frase.

```bash
python sondeo.py <caso>              # sondea y escribe sondeo.json
python sondeo.py <caso> --descargar  # además baja los archivos
```

**Umbral:** 10 minutos de episodio piden unas 40 piezas útiles. Por debajo, el caso no
se puede ilustrar y hay que decirlo antes de escribir, no después.

### Las dos trampas que lo hacían mentir

**1. La URL lleva parámetros detrás.** Commons devuelve
`…/Enron_Complex.jpg?utm_source=…`, así que exigir que la ruta *termine* en `.jpg`
descartaba **absolutamente todo**. El sondeo daba cero piezas en las 24 búsquedas y
parecía que el caso no tenía archivo. Se corta la cadena de consulta antes de mirar la
extensión.

**2. La búsqueda libre es inservible para nombres propios.** Medido, sobre un caso real:

| Se buscaba | Commons devolvía |
|---|---|
| `Kenneth Lay` | marineros *laying* amarras y tuberías *laying* |
| `Jeffrey Skilling` | gente llamada Jeffrey y *bomb detection **skills*** |
| `Arthur Andersen` | Arthur Rackham y los cuentos de Hans Christian **Andersen** |
| `Sarbanes-Oxley Act` | los Red **Sox** y los White **Sox** |

Salían 277 piezas y casi ninguna era de la historia. **Para nombres propios manda la
CATEGORÍA**, que está curada por personas: `Category:Kenneth Lay`. Si la categoría está
vacía, es que no hay imagen libre — y eso sí es un dato fiable. La búsqueda libre se
reserva para lugares y objetos, y aun así se filtra exigiendo que el término aparezca en
el título.

### Lo que hay que reportar del sondeo

No vale el número total. Se clasifica en tres:

```
DE LA HISTORIA ....  imágenes del caso mismo
CONTEXTO ..........  lugar, época, oficio; sirven de relleno honesto
RUIDO .............  falsos positivos del nombre
```

Un caso con 276 útiles pero sólo 14 de la historia **no es un caso con archivo**: es un
caso que hay que contar de otra manera, y conviene saberlo el primer día.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Dar por bueno un sondeo por su número total | 276 piezas con sólo 14 del caso es un episodio sin protagonista |
| Buscar nombres propios en texto libre | «Lay», «Skilling» y «Sox» son palabras comunes: la categoría es la autoridad |
| Citar un artículo que cita a otro artículo | Se hereda su error; nadie puede verificar el episodio |
| Tomar la cifra del titular de prensa | Los titulares redondean e inflan; el documento dice otra cosa |
| Confiar en el resumen del comunicado sin abrir el PDF | El comunicado dice "millones"; el anexo dice cuántos y de qué |
| Guardar sólo el enlace | El organismo reorganiza el sitio y el respaldo desaparece |
| Dar por libre una imagen porque está en Wikipedia | Commons aloja material con licencias muy distintas: se verifica una por una |
| Suponer que un documento oficial extranjero es dominio público | Fuera de EE.UU. suele tener derechos; sirve el dato, no el escaneo |
| Contar como probado lo que sólo está acusado | Es un problema legal y de credibilidad: la acusación **alega** (§ `91`) |

## Relacionado

`91` leer un expediente · `92` el aporte original · `96` verificación de datos ·
`97` banco de historias · `99` descripción con fuentes
