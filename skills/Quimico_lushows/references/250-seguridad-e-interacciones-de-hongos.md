# 250 — Seguridad e interacciones de hongos funcionales (lo que sí hay que advertir)

"Es natural, no hace daño" es una frase que no existe en química. Los hongos funcionales tienen un perfil de
seguridad razonable en los estudios disponibles, pero hay poblaciones y situaciones donde sí hay que
advertir, y hay riesgos que no vienen del hongo sino de cómo se produjo: metales, micotoxinas, alérgenos del
sustrato y contaminación microbiana. Este módulo separa el riesgo intrínseco (farmacológico) del riesgo
extrínseco (de calidad), porque se controlan de maneras distintas.

Términos: **evento adverso (adverse event, AE)** = cualquier suceso desfavorable durante el uso, cause o no
el producto. **farmacovigilancia (pharmacovigilance)** = sistema para recoger y analizar esos eventos.
**CYP450 (cytochrome P450)** = familia de enzimas hepáticas que metabolizan la mayoría de los fármacos.
**INR** = medida de coagulación en pacientes anticoagulados.

## Riesgo intrínseco vs extrínseco

| Tipo | Origen | Cómo se controla | Módulo |
|---|---|---|---|
| Intrínseco | El compuesto del hongo | Dosis, advertencias, poblaciones excluidas | Este |
| Extrínseco | Metales pesados | ICP-MS y control de sustrato | `243` |
| Extrínseco | Micotoxinas y microbiología | LC-MS/MS, aw, secado | `244` |
| Extrínseco | Alérgenos del sustrato (trigo, soya) | Declaración y ELISA | `137` |
| Extrínseco | Solventes residuales | GC-headspace | `87` |
| Extrínseco | Especie equivocada | ITS | `245` |

En la práctica, **la mayoría de los problemas reales de los suplementos de hongos son extrínsecos**. Un
producto bien fabricado quita el 80 % del riesgo antes de que exista.

## Lo que la evidencia dice sobre seguridad intrínseca

| Tema | Qué se ha observado | Nivel de evidencia |
|---|---|---|
| Tolerancia general | Efectos gastrointestinales leves (náusea, distensión, heces blandas) son los más reportados | `[clínico ECA]` pequeños |
| Reacciones alérgicas | Posibles en personas sensibles a hongos; también por esporas inhaladas en producción | `[casos clínicos]` |
| Reishi y hepatotoxicidad | Reportes de casos aislados asociados a productos en polvo, no reproducidos sistemáticamente | `[casos clínicos]` |
| Efecto sobre coagulación | Se ha sugerido efecto antiagregante con reishi | `[in vitro]` / `[animal]`, poco humano |
| Chaga y oxalato | Alto contenido de oxalato; reportes de nefropatía por oxalato con consumo elevado y prolongado | `[casos clínicos]` — ver `230` |
| Chaga y radiocesio | Riesgo en material de zonas contaminadas | `[analítico]` — ver `230` |
| Interacción con inmunosupresores | Plausible por inmunomodulación; poca evidencia humana directa | `[in vitro]` / plausibilidad |
| Interacción por CYP450 | Datos escasos y poco consistentes en humanos | `[in vitro]` mayormente |

Honestidad obligatoria: **la mayor parte de la señal de interacción es in vitro o mecanicista**. Eso no
significa que no importe; significa que se advierte por precaución y se le dice al usuario que consulte, no
que se afirme una interacción confirmada.

## Advertencias que sí deben ir en la etiqueta

```
Redacción defendible (adaptar al marco de cada país, ver 272):

  "No recomendado durante el embarazo y la lactancia."
  "Consulte a su médico si toma anticoagulantes, antiagregantes, inmunosupresores, hipoglucemiantes
   o si va a someterse a cirugía."
  "No consumir en caso de alergia conocida a los hongos."
  "Manténgase fuera del alcance de los niños."
  "Este producto no reemplaza una alimentación variada y equilibrada."
  "Suspender y consultar si aparece cualquier reacción."
```

Estas advertencias son afirmaciones de precaución, no claims. No dicen que el producto trate nada.

## Poblaciones donde se recomienda precaución

| Población | Motivo | Nivel |
|---|---|---|
| Embarazo y lactancia | Ausencia de datos, no evidencia de daño | Precaución por vacío de datos |
| Anticoagulados / preoperatorio | Posible efecto sobre agregación plaquetaria | `[in vitro]` / plausibilidad |
| Trasplantados y en inmunosupresión | Inmunomodulación teórica en dirección opuesta al tratamiento | Plausibilidad mecanicista |
| Personas con litiasis renal por oxalato | Chaga aporta oxalato | `[casos clínicos]` |
| Diabéticos con medicación | Reportes de efecto sobre glucemia con algunas especies | `[clínico piloto]` |
| Alérgicos a hongos y trabajadores expuestos a esporas | Sensibilización respiratoria | `[casos clínicos]` |

## Cómo se comprueba (seguridad no es opinión, es sistema)

| Elemento | Qué hacer |
|---|---|
| Perfil de contaminantes | Ejecutar la especificación completa por lote (`247`) |
| Farmacovigilancia | Canal para recibir reportes de eventos adversos, registro fechado y trazable (`138`) |
| Trazabilidad | Poder llegar del lote del cliente al lote de materia prima en minutos (`168`) |
| Retiro de producto | Procedimiento escrito de recall probado al menos una vez |
| Revisión de literatura | Búsqueda anual de nuevos reportes de seguridad de tus especies |
| Etiqueta | Advertencias vigentes según el marco de cada mercado (`272`, `273`) |

## Ejemplo aplicado (ILUSTRATIVO) — evaluación de riesgo de un producto

```
Producto: cápsulas de extracto dual de reishi, 1,0 g/día
Riesgo intrínseco: bajo-moderado. Advertencias por anticoagulación y embarazo.
Riesgo extrínseco medido en el lote GL-2026-014:
  Cd 0,31 mg/kg b.s. (límite propio ≤ 0,5)        CONFORME
  Aflatoxinas totales < 1,0 µg/kg (LOQ)            CONFORME
  Mohos y levaduras 3,0 × 10² UFC/g                CONFORME
  Etanol residual 820 ppm (límite 5000)            CONFORME
Decisión: libera. Documentar y archivar el expediente del lote.
```

Sin esa tabla del lado derecho, la conversación sobre seguridad es puramente teórica.

## Errores comunes

- **Decir "no tiene contraindicaciones".** Ningún producto de consumo puede afirmar eso.
- **Confundir ausencia de estudios con evidencia de seguridad.** No es lo mismo "no se ha visto daño" que
  "se estudió y es seguro".
- **No tener canal de farmacovigilancia.** Es requisito de fondo y, en una inspección, de forma.
- **Ignorar el sustrato como fuente de alérgenos.** Trigo, soya o cebada en el sustrato pueden llegar al
  producto, sobre todo en micelio sobre grano.
- **Advertir en la web y no en la etiqueta.** La etiqueta es el documento legal.
- **Usar advertencias como sustituto del control de calidad.** Advertir no arregla un lote con cadmio.

## Conexión con otros módulos

→ `138-farmacovigilancia-y-eventos-adversos.md` — cómo se monta el sistema.
→ `139-interacciones-planta-farmaco.md` y `124-citocromo-p450-e-interacciones.md`.
→ `230-chaga-riesgos-oxalato-y-radiocesio.md` — el caso con más riesgo propio.
→ `243`, `244` — el riesgo extrínseco y sus métodos.
→ `137-alergenos-e-hipersensibilidad.md` — sustrato y alérgenos.
→ `272-etiquetado-en-colombia.md` — dónde van las advertencias.
