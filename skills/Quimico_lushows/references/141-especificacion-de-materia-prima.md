# 141 — Especificación de materia prima (el documento que te salva del proveedor)

Una especificación de materia prima es la lista de atributos que un lote debe cumplir **antes** de entrar a tu
proceso, cada uno con su método de ensayo y su criterio de aceptación. No es burocracia: es el único mecanismo
que convierte "confío en mi proveedor" en "puedo rechazar este lote y me devuelven la plata". Sin especificación
escrita, cualquier discusión con el proveedor la pierdes tú, porque no hay contra qué comparar. Y en Colombia,
sin especificación de entrada no hay expediente técnico defendible ante INVIMA (`286`).

Términos: **especificación (specification)** = tabla de atributo + método + criterio de aceptación.
**COA (certificate of analysis)** = certificado del lote emitido por quien vende. **Atributo crítico de
calidad (critical quality attribute, CQA)** = el que si se sale, el producto no sirve. **Muestreo (sampling)**
= cómo tomas la porción que representa el lote entero (`66`).

## La estructura de una especificación que sirve

Cada fila necesita **cuatro** columnas. Si falta el método, la fila no vale nada.

| Atributo | Método (referencia) | Unidad y base | Criterio |
|---|---|---|---|
| Identidad de especie | ITS/ADN barcoding (`103`, `245`) | — | Coincidencia ≥ 99 % con *Ganoderma lucidum* |
| Parte usada | Inspección + microscopía / declaración | — | Cuerpo fructífero 100 %, sin grano |
| Aspecto | Visual | — | Polvo pardo claro, sin grumos |
| Humedad | Karl Fischer o pérdida por secado (`98`) | % p/p | ≤ 8,0 % |
| Actividad de agua (a_w) | Higrómetro de punto de rocío (`35`) | — | ≤ 0,60 |
| Cenizas totales | Gravimetría, 550 °C | % p/p base seca | ≤ 3,0 % |
| β-glucano | Megazyme K-YBGL, enzimático (`221`) | % p/p base seca | ≥ 20,0 % |
| α-glucano (almidón) | Mismo kit, fracción α (`220`) | % p/p base seca | ≤ 5,0 % |
| Granulometría | Tamizado (`143`) | % pasa malla 80 | ≥ 95 % |
| Metales pesados (Pb, Cd, As, Hg) | ICP-MS (`88`, `243`) | mg/kg (ppm) | Según límite vigente aplicable |
| Micotoxinas (aflatoxinas B1/total, OTA) | LC-MS/MS (`101`) | µg/kg (ppb) | Según límite vigente aplicable |
| Pesticidas | Multiresiduo GC/LC-MS/MS (`102`) | mg/kg | Según lista aplicable |
| Recuento aerobios mesófilos | ISO 4833 / equivalente (`100`) | UFC/g | ≤ 10⁴ |
| *E. coli* / *Salmonella* | Método oficial | por 25 g | Ausencia |
| Solventes residuales (si es extracto) | GC-headspace (`87`) | ppm | Etanol ≤ límite de clase 3 |

Los criterios de arriba son **(ILUSTRATIVO)**: son órdenes de magnitud razonables para armar una plantilla, no
límites legales. Los límites reales de metales, micotoxinas y microbiología para suplementos dietarios en
Colombia se verifican, a agosto de 2026, contra el Decreto 3249 de 2006 y la normativa sanitaria vigente que
INVIMA aplique al producto concreto (`266`, `271`). Verifica siempre la versión vigente antes de firmar.

## Los cuatro atributos que de verdad definen el negocio

1. **Identidad.** La especie no se confirma "por la foto". Se confirma por ADN/ITS o, mínimo, por huella
   química reproducible (`60`, `104`). En hongos, el fraude de especie es común y barato de cometer.
2. **Parte usada.** Cuerpo fructífero vs micelio en grano cambia toda la química: el micelio cultivado sobre
   arroz o sorgo arrastra almidón, y el almidón es α-glucano, no β-glucano (`217`, `218`, `220`).
3. **β-glucano medido, no "polisacáridos totales".** El ensayo de polisacáridos totales cuenta el almidón
   como si fuera activo. Es el disfraz #1 del mercado (`222`).
4. **Base.** Todo porcentaje va en base seca o no es comparable entre lotes con humedad distinta (`07`).

## Cómo se comprueba un lote que llega

```
PROTOCOLO DE RECEPCIÓN (pyme, presupuesto real)

Paso 1  Documentos: COA del lote, ficha técnica, declaración de especie y parte usada,
        alérgenos, país de origen, fecha de cosecha/fabricación.  → si falta algo, no se descarga.

Paso 2  Muestreo: √n + 1 sacos si n > 4 (regla práctica de muestreo por atributos);
        muestra compuesta homogeneizada, cuarteo hasta 200 g, contramuestra sellada
        y guardada hasta vencimiento + 6 meses.  → `66`, `109`

Paso 3  Ensayos EN CASA (baratos):
        - aspecto, olor, presencia de granos enteros (lupa)
        - humedad por balanza halógena
        - a_w si tienes higrómetro

Paso 4  Ensayos ENVIADOS (los que deciden):
        - β-glucano / α-glucano (Megazyme)      → identidad económica del lote
        - metales pesados por ICP-MS            → seguridad
        primer lote de cada proveedor: paquete completo.
        lotes siguientes: plan reducido (skip-lot) SOLO si hay historial de ≥ 3 lotes conformes.

Paso 5  Decisión documentada: APROBADO / RECHAZADO / EN CUARENTENA, con firma y fecha (`168`).
```

Costo indicativo del paquete completo por lote en Colombia, **(ILUSTRATIVO)**: pídelo por escrito a dos
laboratorios y compáralo — ver `114` y `291`. No adivines el costo: cotízalo.

## Ejemplo aplicado — rechazar un lote con el papel en la mano

Llega un lote de "extracto de melena de león 8:1" con COA que dice: *"Polysaccharides ≥ 30 %"*.

```
Contra la especificación:
  Atributo exigido: β-glucano ≥ 20,0 % p/p base seca por Megazyme K-YBGL
  Lo que reporta el COA: "polisacáridos ≥ 30 %" por método colorimétrico (fenol-sulfúrico)

Veredicto: NO CONFORME POR MÉTODO. El COA no mide el atributo especificado.
El ensayo de polisacáridos totales incluye α-glucano (almidón) y otros azúcares (`222`).
Acción: cuarentena + ensayo Megazyme sobre contramuestra a cargo del proveedor.
```

Resultado típico de este ejercicio en el mercado real: un producto vendido como micelio-en-grano puede traer
una fracción alta de almidón del sustrato y β-glucano de un solo dígito. Reportes de ensayos independientes de
suplementos de hongos han descrito almidón del orden de 35–60 % y β-glucano de 1–5 % p/p en ese tipo de
material. Verifica siempre con tu lote y tu laboratorio: es un rango reportado, no una constante.

## Errores comunes

- Aceptar el COA del proveedor como resultado propio. El COA es un documento comercial hasta que lo auditas
  (`110`, `111`).
- Especificar el atributo sin el método: "β-glucano ≥ 30 %" sin decir Megazyme deja la puerta abierta al
  método más generoso (`113`).
- No guardar contramuestra. Sin contramuestra no puedes impugnar nada (`112`).
- Poner criterios copiados de internet que tu proveedor real jamás cumplirá: la especificación deja de usarse
  a la semana. Mejor un criterio exigente donde importa y realista donde no.
- Olvidar la base: comparar 30 % (base húmeda, 10 % de agua) con 30 % (base seca) y creer que es lo mismo.
- No fechar la especificación ni versionarla. Si cambia, es un control de cambios (`169`).

## Conexión con otros módulos

→ `110-como-leer-un-coa.md` — cómo se audita el certificado que te mandan.
→ `221-medir-beta-glucanos-metodo-megazyme.md` — el método que sostiene el atributo clave.
→ `247-especificacion-de-producto-de-hongos.md` — la versión específica para hongos.
→ `284-auditoria-de-proveedor.md` — cuando el papel no basta y toca ir a ver la planta.
→ `168-documentacion-de-lote-y-trazabilidad.md` — dónde vive el registro de recepción.