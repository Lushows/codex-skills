# 106 — Análisis de agua y materias primas (lo que entra decide lo que sale)

Casi nadie analiza el agua. Y el agua es, por masa, el ingrediente principal de una decocción, de una tintura
diluida, de un jarabe y del lavado de equipos. Si el agua trae dureza, hierro, cloro residual alto o carga
microbiana, se lo trae al producto: precipitados en la tintura, sabor metálico, oxidación acelerada de
polifenoles, y un resultado microbiológico fuera de especificación que se investiga durante semanas mirando
la materia prima equivocada. Este módulo cubre qué se le mide al agua, qué se le mide a cada materia prima
antes de aceptarla, y cómo se escribe eso en un documento de aceptación que el proveedor entienda.

Términos: **materia prima (raw material)** = todo lo que entra al proceso: biomasa, solvente, excipiente,
envase, agua. **agua purificada (purified water)** = agua tratada según monografía farmacopeica.
**dureza (hardness)** = contenido de Ca²⁺ y Mg²⁺, en mg/L de CaCO₃. **conductividad (conductivity)** = medida
global de iones disueltos, en µS/cm. **COT (TOC, total organic carbon)** = carbono orgánico total, en mg/L.
**certificado de análisis del proveedor (supplier CoA)** = el papel que acompaña el lote (ver `110`).

## Los tres tipos de agua y cuándo cada uno

| Tipo | Cómo se obtiene | Se usa para | Controles típicos |
|---|---|---|---|
| Potable | Red pública / pozo tratado | Lavado de equipo, primer enjuague, servicios | Res. 2115 de 2007 (Colombia) |
| Purificada | Ósmosis inversa, intercambio iónico, destilación | Producto, enjuague final, preparación de reactivos | Conductividad, COT, microbiología |
| Grado reactivo (tipo I) | Purificada + pulido | Análisis, HPLC, preparación de patrones | Resistividad 18,2 MΩ·cm a 25 °C |

En Colombia, la calidad del agua para consumo humano se rige por la **Resolución 2115 de 2007** (Ministerio de
la Protección Social y MAVDT), que fija el pH entre **6,5 y 9,0** y define los parámetros básicos de
seguimiento: turbiedad, color aparente, pH, cloro residual libre, coliformes totales y *E. coli*
([texto oficial, Minsalud, consultado a agosto de 2026](https://www.minsalud.gov.co/sites/rid/Lists/BibliotecaDigital/RIDE/DE/DIJ/Resoluci%C3%B3n_2115_de_2007.pdf)).
Que el agua sea potable no significa que sirva para tu producto: potable admite dureza y cloro que a una
tintura le hacen daño. Son dos preguntas distintas.

## Qué medirle al agua del proceso

```
FISICOQUIMICO
  pH                      unidades de pH         objetivo segun formulacion
  Conductividad           uS/cm a 25 C           proxy rapido y barato de sales totales
  Dureza total            mg/L como CaCO3        > ~150 mg/L da precipitados y sarro
  Cloro residual libre    mg/L                   oxidante: degrada polifenoles y aromas
  Hierro                  mg/L                   colorea y cataliza oxidacion (ver 61)
  COT                     mg/L                   materia organica disuelta
MICROBIOLOGICO
  Aerobios mesofilos      UFC/mL                 tendencia, no solo cumplir/no cumplir
  Coliformes totales      UFC/100 mL             indicador de contaminacion fecal/ambiental
  E. coli                 UFC/100 mL             ausencia
```

Un tip que se paga solo: **el conductímetro y el pH-metro se compran una vez** y dan tendencia diaria. Lo caro
—metales, COT, microbiología completa— se hace por muestreo periódico, no por lote. Y siempre se muestrea en
el **punto de uso**, no en la entrada del tanque: el problema casi siempre está en la tubería y en el
almacenamiento, no en el agua que llegó.

## Especificación de entrada por tipo de materia prima

| Materia prima | Identidad | Pureza / potencia | Seguridad | Físico |
|---|---|---|---|---|
| Biomasa fúngica seca | Especie por ITS (`103`, `245`) + macro/micro | β-glucano y α-glucano por K-YBGL (`91`) | Metales (`243`), micotoxinas (`244`), microbiología (`100`) | Humedad (`98`), aW (`35`), granulometría (`143`) |
| Biomasa vegetal | Botánica + HPTLC (`96`) | Marcador por HPLC (`79`) | Pesticidas (`102`), metales, microbiología | Humedad, materia extraña |
| Extracto comprado | Huella HPTLC o HPLC vs referencia | Activo declarado, con método | Solventes residuales (`87`), metales | Solubilidad, pérdida por secado |
| Etanol | Índice de refracción / densidad | Grado (% v/v) | Metanol, congéneres por GC | Aspecto, olor |
| Excipientes (maltodextrina, celulosa) | FTIR vs referencia (`92`) | Según monografía USP/EP (`280`) | Microbiología | Humedad, fluidez |
| Envase primario | Ficha técnica y material | — | Migración/compatibilidad (`163`) | Hermeticidad |

La regla que ordena esta tabla: **identidad, potencia, seguridad y físico**. Si una especificación de entrada
no responde esas cuatro preguntas, está incompleta (ver `141`).

## El CoA del proveedor no es tu control de calidad

El certificado que manda el proveedor es el **punto de partida**. Tu control es la verificación de identidad
en cada lote recibido, más los ensayos de seguridad con frecuencia justificada por riesgo. La práctica
estándar en suplementos —y lo que exige la cGMP estadounidense 21 CFR 111 (`274`)— es que la identidad de cada
componente se verifique con un ensayo propio, y que la confianza en el CoA del proveedor para los demás
parámetros esté **calificada**: auditoría del proveedor (`284`), historial de lotes y verificación periódica.

## Ejemplo aplicado (ILUSTRATIVO)

BIO-SETA recibe un lote de polvo de melena de león. Aceptación en tres niveles:

```
NIVEL 1 - en el muelle (mismo dia, sin laboratorio externo)
  Documentos: CoA del lote (no de la marca), guia, ficha tecnica    -> conforme
  Organoleptico: color crema uniforme, olor caracteristico          -> conforme
  Humedad por balanza halogena: 6,2 % p/p                           -> spec <= 8,0 % p/p, pasa
  Aw: 0,42                                                          -> spec <= 0,60, pasa

NIVEL 2 - identidad (cada lote, laboratorio)
  ITS: Hericium erinaceus, 99,4 % de identidad                      -> conforme (ver 245)

NIVEL 3 - potencia y seguridad (este lote: potencia si, metales por muestreo 1 de cada 3)
  beta-glucano por K-YBGL: 24,8 % p/p base seca                     -> spec >= 20 %, pasa
  alfa-glucano:             5,1 % p/p base seca                     -> spec <= 10 %, pasa (sin sustrato)
  Metales (Pb, Cd, As, Hg) por ICP-MS: pendiente, lote 3 de 3
```

Decisión: lote **liberado condicionalmente** para producción, con retención de la contramuestra y bloqueo de
despacho de producto terminado hasta el resultado de metales. Cifras **(ILUSTRATIVO)**. El α-glucano bajo es
la evidencia de que no hay grano en el polvo — el mismo número que delata el fraude en `218`.

## Errores comunes

- **No analizar el agua nunca** y luego culpar a la biomasa del resultado microbiológico.
- **Muestrear el agua en la entrada y no en el punto de uso.** El biofilm vive en la tubería.
- **Aceptar el CoA de la marca en vez del CoA del lote.** Un CoA sin número de lote no ampara nada (`111`).
- **Especificar solo potencia.** Sin identidad no sabes qué compraste; sin seguridad no sabes qué vendiste.
- **Pedir "análisis completo" a la biomasa** en cada lote sin plan de riesgo: se gasta el presupuesto del año
  en dos entregas (ver `114`, `291`).
- **Olvidar el envase como materia prima.** El frasco es lo que está en contacto con el producto un año (`163`).

## Conexión con otros módulos

→ `141-especificacion-de-materia-prima.md` — cómo se escribe formalmente la especificación de entrada.
→ `284-auditoria-de-proveedor.md` — cómo se califica al proveedor para poder confiar en su CoA.
→ `35-actividad-de-agua-y-humedad.md` — por qué aW predice la estabilidad microbiológica mejor que la humedad.
→ `100-microbiologia-de-producto.md` — el ensayo donde el agua aparece como causa oculta.
→ `110-como-leer-un-coa.md` — cómo se audita el papel que llega con la materia prima.
→ `283-plan-de-control-de-calidad-por-lote.md` — qué se mide en cada lote y qué se mide por muestreo.
