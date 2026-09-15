# 280 — Farmacopeas USP y EP: cómo se lee una monografía y para qué sirve

Una **monografía** es la ficha técnica oficial de una sustancia: qué es, cómo se comprueba que es ella, qué
tanto de lo declarado debe contener y qué no puede tener adentro. Es el documento que convierte "extracto de
reishi" en algo verificable. Para un emprendedor de suplementos la monografía tiene un uso muy práctico:
**es la especificación que no tuviste que inventar**, y es el lenguaje con el que se le habla a un
laboratorio o a un maquilador sin que nadie pueda escurrir el bulto. Cuando existe monografía, se cita.
Cuando no existe —que es el caso de casi todos los hongos funcionales— hay que escribirla uno mismo, y ahí
entra `282`.

Términos: **USP-NF** = United States Pharmacopeia–National Formulary, la farmacopea estadounidense. ·
**HMC (Herbal Medicines Compendium)** = compendio de USP para materiales herbales, de acceso público. ·
**DSC (Dietary Supplements Compendium)** = compendio de USP para suplementos. · **FCC (Food Chemicals
Codex)** = compendio de ingredientes alimentarios. · **estándar de referencia (reference standard)** = la
sustancia patrón contra la cual se calibra el ensayo (`70`).

## 1. Anatomía de una monografía

Da igual si es USP o Ph. Eur.: la estructura es la misma y conviene reconocerla de un vistazo.

| Sección | Qué dice | Por qué importa |
|---|---|---|
| Definición | Qué material es, de qué especie, qué parte, qué proceso | Aquí se cae el 80 % de los proveedores: la parte usada |
| Identificación | Ensayos de identidad (HPTLC, HPLC, espectros, ADN) | Comprueba que es lo que dice ser, no cuánto tiene |
| Ensayo (assay) | Cuantificación del marcador, con límites | El número que sostiene el claim |
| Impurezas / pureza | Materia extraña, cenizas, pérdida por desecación | Calidad del material y del proceso |
| Contaminantes | Metales pesados, plaguicidas, micotoxinas, microbiología | Seguridad |
| Etiquetado | Qué debe declararse | Trazabilidad de lo que compras |
| Estándares de referencia | Qué patrón usar | Sin patrón no hay cuantificación (`70`) |

Regla de oro: **identificación e ensayo no son lo mismo.** Un COA que solo trae identificación no te dice
cuánto activo hay; uno que solo trae assay no te asegura que sea la especie correcta.

## 2. Los compendios de USP y para qué sirve cada uno

| Compendio | Contenido | Uso típico |
|---|---|---|
| **USP-NF** | Fármacos, excipientes, algunos ingredientes dietarios | Referencia oficial en EE. UU. |
| **DSC** | Compendio de suplementos, con del orden de 650 monografías de ingredientes y productos, más capítulos generales | El que usa la industria de suplementos |
| **HMC** | Monografías de materiales herbales, publicación en línea con etapas de borrador y versión final autorizada | Donde vive la monografía de cannabis |
| **FCC** | Ingredientes alimentarios y aditivos | Cuando el ingrediente es alimento, no suplemento |

Fuente: `usp.org`, secciones *Dietary Supplements & Herbal Medicines* y *Dietary Supplements Compendium*;
consultado en agosto de 2026. El DSC se actualiza anualmente: **cita siempre la edición y el año.**

## 3. Capítulos generales de USP que se citan en una especificación de suplementos

| Familia | Para qué |
|---|---|
| Contaminantes elementales en suplementos dietarios | Límites de arsénico (inorgánico), cadmio, plomo y mercurio (metilmercurio) por **exposición diaria permitida (PDE)**, con enfoque basado en riesgo |
| Contaminantes elementales en medicamentos (procedimientos y límites, alineados con ICH Q3D) | Cuando el producto es farmacéutico |
| Enumeración microbiana y microorganismos especificados para suplementos nutricionales y dietarios | Microbiología de producto (`100`) |
| Artículos de origen botánico: métodos de análisis, extractos, identificación | Identidad y pureza de material vegetal |

Dato verificado y útil: el antiguo capítulo de **"Heavy Metals" por método colorimétrico quedó eliminado el
1 de enero de 2018**, reemplazado por los capítulos modernos basados en **ICP-MS / ICP-OES**. Fuente:
`uspnf.com` y documentación de USP. Si un COA de 2026 todavía reporta "heavy metals: passes" sin números ni
técnica instrumental, estás mirando un método obsoleto: bandera roja (`111`).

**Los números de capítulo no los cito de memoria.** Cambian y se revisan. **Toma la numeración exacta del
USP-NF vigente y escríbela en tu especificación con edición y año.**

## 4. La monografía de cannabis de USP: el caso mejor documentado

Es el ejemplo más claro de cómo nace un estándar y por qué conviene seguir el proceso:

| Hito | Fecha |
|---|---|
| Monografía propuesta *Cannabis Species Inflorescence* publicada en el HMC, 90 días de comentarios | Septiembre de 2022 |
| Versión revisada, cierre de comentarios | 1 de noviembre de 2023 |
| Segunda revisión publicada, comentarios | Abril de 2024 (cierre en julio de 2024) |
| **Versión Autorizada Final 1.0** publicada en el HMC | Publicada; verificar la fecha exacta en `usp.org` |

Cambio técnico que vale oro entender: en el proceso de revisión, la especificación de contenido de THC, CBD
y otros cannabinoides **pasó de 80–120 % a 90–110 % de la cantidad declarada** (en mg/g), y el contenido de
CBD total se define incluyendo el CBD y su ácido correspondiente (CBDA). Fuente: ECA Academy
(`gmp-compliance.org`), notas sobre la monografía de cannabis de USP HMC; `usp.org`. Consultado agosto de
2026.

Por qué importa: ese rango 90–110 % es exactamente el tipo de límite que debes copiar a tu propia
especificación de aceite de cannabis (ver `282`). Y el detalle de "CBD total = CBD + CBDA" es la misma
lógica del factor 0,877 del THC (`175`).

**Sobre una monografía de cannabidiol como sustancia:** USP ha trabajado en estándares de cannabidiol además
de la monografía de inflorescencia. **No confirmo su estado (borrador en Pharmacopeial Forum, propuesta o
final) a agosto de 2026: verifícalo en `usp.org` y en el Pharmacopeial Forum antes de citarlo en un
documento técnico.** Escribir "según monografía USP de CBD" sin haberlo confirmado es el tipo de error que
se descubre en una auditoría.

## 5. Hongos funcionales: lo que hay y lo que no

USP tiene trabajo histórico sobre materiales fúngicos —incluyendo *Ganoderma lucidum* cuerpo fructífero
(reishi) dentro de sus estándares botánicos— pero **el ecosistema de monografías para hongos funcionales es
mucho más pobre que el de plantas medicinales**, y no hay un estándar oficial de beta-glucano de hongo
aceptado de forma universal (ver `281`).

El dato que ilustra el tamaño del problema: un estudio patrocinado por USP y liderado por Li Shao-ping,
publicado en *Scientific Reports* en 2017, analizó 19 suplementos de reishi vendidos en EE. UU. mediante
HPTLC, GC-MS y cromatografía de exclusión por tamaño, y encontró que **solo 5 de los 19 correspondían
realmente al hongo declarado**. Fuente: *Scientific Reports*, 2017; reseñas del estudio. Es evidencia dura
de por qué la identidad (`103`, `245`) va antes que la potencia.

## Cómo se comprueba

Cómo se usa una monografía en la vida real, en orden:

```
1. ¿Existe monografía para MI material exacto? (especie + parte + proceso)
   Sí → cítala en la orden de compra y en la especificación, con compendio, número y año
   No → escribe tu especificación propia (282) tomando prestada la ESTRUCTURA de la monografía
2. ¿El laboratorio tiene el ESTÁNDAR DE REFERENCIA que la monografía exige?
   Si no lo tiene, no puede cuantificar contra ella: solo estimar (70)
3. ¿El COA dice "según USP <capítulo>" o "método interno"?
   "Método interno" no es inválido, pero exige validación documentada (75) y hay que pedirla
4. ¿Los límites que citas son USP o Ph. Eur.? No son iguales. Se declara cuál
```

## Ejemplo aplicado (ILUSTRATIVO)

Orden de compra de BIO-SETA a un proveedor, redactada mal y redactada bien:

```
MAL:  "Extracto de reishi de alta calidad, 30 % polisacáridos, con COA."
BIEN: "Extracto acuoso de cuerpo fructífero de Ganoderma lucidum (identidad confirmada por
       secuenciación ITS). Beta-glucano >= 25 % p/p base seca, método enzimático glucano total
       menos alfa-glucano. Alfa-glucano <= 10 % p/p base seca. Humedad <= 8 % p/p.
       Contaminantes elementales según USP <capítulo vigente>, edición y año declarados.
       Microbiología según USP <capítulo vigente>. COA por lote, con cromatogramas."
```

La segunda versión es más larga y es la única que se puede reclamar. Ver `292` para negociarla.

## Errores comunes

- **Decir "cumple USP" sin decir qué monografía ni qué capítulo.** No significa nada.
- **Mezclar límites de USP y Ph. Eur. en la misma tabla.** Elige un marco y decláralo.
- **Aceptar "heavy metals: passes" sin números.** Método obsoleto o resultado escondido (`111`).
- **Creer que identificación equivale a cuantificación.** Son secciones distintas por una razón.
- **Citar una monografía en borrador como si fuera final.** En HMC hay etapas: verifica cuál estás citando.
- **Suponer que hay monografía para tu hongo porque hay para una planta.** Casi nunca la hay.

## Conexión con otros módulos

→ `279-eu-gmp-y-farmacopea-europea.md` — el lado europeo del mismo problema.
→ `281-metodos-oficiales-aoac.md` — los métodos que llenan los huecos que la farmacopea deja.
→ `282-especificacion-de-producto-terminado.md` — qué hacer cuando no existe monografía.
→ `110-como-leer-un-coa.md` y `111-banderas-rojas-en-un-coa.md` — auditar lo que te mandan.
→ `70-patrones-de-referencia-y-trazabilidad.md` — sin patrón no hay número.
→ `175-thc-total-y-el-factor-0877.md` — la lógica de "total = neutro + ácido".
