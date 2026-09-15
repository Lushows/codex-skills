# 270 — Fitoterapéutico vs. suplemento dietario: la casilla que decide tu negocio

En Colombia hay dos puertas para vender una planta o un hongo en cápsula, y son puertas distintas con
normas distintas: **suplemento dietario** (Decreto 3249 de 2006) o **producto fitoterapéutico**
(Decreto 1156 de 2018). Elegir mal la puerta te cuesta el registro, o peor: te da un registro que no
soporta lo que quieres decir. La diferencia práctica es enorme — el fitoterapéutico **sí** puede tener una
indicación terapéutica aprobada; el suplemento dietario **no**.

Términos: **producto fitoterapéutico (herbal medicinal product)** = medicamento cuyo principio activo es
material vegetal o preparaciones de él, con indicación terapéutica reconocida. · **vademécum** = obra
oficial que recoge las plantas medicinales aceptadas y sus usos. · **monografía** = ficha técnica oficial
de una planta: identidad, composición, ensayos, usos, seguridad. · **indicación** = para qué está aprobado
oficialmente el producto.

## Las dos casillas, lado a lado (a agosto de 2026)

| | Suplemento dietario | Producto fitoterapéutico |
|---|---|---|
| Norma | Decreto 3249 de 2006, modificado por Decreto 3863 de 2008 | Decreto 1156 de 2018 (derogó el Decreto 2266 de 2004) |
| Naturaleza legal | Alimento que adiciona la dieta | **Medicamento** |
| ¿Puede tener indicación terapéutica? | **No** (art. 25 num. 8) | **Sí**, la que soporte su monografía |
| Fuente de lo permitido | Ingredientes permitidos, niveles máximos, referencias Codex/FDA/EFSA | Vademécum Colombiano de Plantas Medicinales + monografías OMS y EMA + listado que elabora y actualiza el INVIMA |
| Exigencia de calidad | Especificación y control de calidad | Mayor: estándar de medicamento |
| Publicidad | Aprobación previa INVIMA (art. 24) | Régimen de publicidad de medicamentos |
| Quién conceptúa | Sala Especializada de la Comisión Revisora | Sala Especializada de la Comisión Revisora |

Fuentes: Decreto 3249 de 2006 y Decreto 1156 de 2018, textos en `minsalud.gov.co` y `funcionpublica.gov.co`;
consultados el 11 de agosto de 2026. **Verifica el texto vigente**: el listado de plantas aceptadas se
actualiza y es lo que decide si tu especie entra o no.

## Lo que el Decreto 1156 de 2018 cambió

Según el propio texto y su exposición de motivos (consultada en `minsalud.gov.co`, agosto de 2026), el
decreto: reglamenta el régimen de registro sanitario de productos fitoterapéuticos, **incorpora referentes
internacionales** (monografías de la Organización Mundial de la Salud y de la Agencia Europea de
Medicamentos, además del Vademécum Colombiano de Plantas Medicinales), **simplifica renovación y
modificación** del registro, y encarga al INVIMA elaborar y actualizar el listado de plantas medicinales
aceptadas con fines terapéuticos. Aplica también a productos con cannabis dentro del marco vigente.

Consecuencia práctica: **si tu planta tiene monografía OMS o EMA, la puerta fitoterapéutica se vuelve
viable**. Si no la tiene y tampoco está en el vademécum, la puerta se cierra y quedas con suplemento
dietario — o con la obligación de generar tú la evidencia.

## El problema específico de los hongos

Aquí hay que ser honesto: **el marco de "plantas medicinales" fue escrito pensando en plantas**. Los hongos
(*Ganoderma*, *Hericium*, *Cordyceps*, *Trametes*, *Inonotus*) no son plantas — son un reino aparte. Que un
hongo sea aceptable como material fitoterapéutico en Colombia **depende del listado y de los conceptos
vigentes de la Sala Especializada, y hay que verificarlo caso por caso con INVIMA**. No asumas por
analogía con la OMS o la EMA.

Ruta práctica cuando no hay claridad:
1. Busca en el listado vigente de plantas aceptadas y en las actas de sala tu especie por **nombre
   científico**, no por nombre común.
2. Si no aparece, pregunta por escrito al INVIMA cuál es la casilla aplicable y guarda la respuesta.
3. Mientras no tengas respuesta, opera en la casilla más conservadora: suplemento dietario, sin claims.

## Cómo se decide la casilla (árbol de decisión)

```
¿Le vas a atribuir una INDICACIÓN TERAPÉUTICA?
├── SÍ → tiene que ser FITOTERAPÉUTICO (o medicamento). Verifica:
│        ¿la especie está en el vademécum / listado INVIMA, o tiene monografía OMS o EMA?
│        ├── SÍ → ruta Decreto 1156 de 2018
│        └── NO → no hay ruta corta. O generas evidencia propia, o retiras la indicación.
└── NO → SUPLEMENTO DIETARIO (Decreto 3249 de 2006). Verifica:
         ¿el ingrediente está permitido y bajo el nivel máximo de ingesta?
         ├── SÍ → ruta registro sanitario de suplemento
         └── NO → reformula o consulta previa al INVIMA
```

La pregunta de arriba no la contesta el químico: la contesta el **modelo de negocio**. Por eso este módulo
se lee junto con `economist_lushows` y `ventas_lushows`.

## Cómo se comprueba la identidad del material, en cualquiera de las dos casillas

Da igual la puerta: si no puedes probar **qué especie** y **qué parte** es tu materia prima, no tienes
producto. La combinación mínima:

| Qué compruebas | Método | Qué te dice |
|---|---|---|
| Especie | Secuenciación de la región ITS (DNA barcoding) | Si de verdad es *Ganoderma lucidum* y no otra especie del género (`103`, `245`) |
| Parte usada | Marcadores químicos: α-glucano alto delata micelio en grano | Cuerpo fructífero vs. micelio (`217`, `218`, `220`) |
| Composición | β-glucano por método enzimático, base seca | El activo declarable (`221`) |
| Autenticidad del extracto | Perfil por HPLC-DAD o HPTLC contra referencia | Adulteración y sustitución (`96`, `246`) |

## Ejemplo aplicado — dos rutas para el mismo reishi

Producto **(ILUSTRATIVO)**: cápsula de 500 mg de extracto acuoso de cuerpo fructífero de *Ganoderma
lucidum*, β-glucano 30 % p/p base seca.

| Ruta | Qué puedes decir | Qué te exige |
|---|---|---|
| Suplemento dietario | Composición, contenido de β-glucano medido, origen del material | Registro sanitario, especificación, sin indicación terapéutica |
| Fitoterapéutico | La indicación que soporte la monografía aplicable | Verificar aceptación de la especie; estándar de calidad de medicamento; expediente mayor |

La ruta fitoterapéutica es más cara y más lenta, pero es **la única** que permite hablar de un uso
terapéutico sin estar violando la ley. Si tu negocio depende de decir para qué sirve, la ruta barata no
existe; existe la ruta ilegal, que es la que BIO-SETA ha estado usando (`268`).

## Errores comunes

- **Elegir suplemento "porque es más barato" y seguir hablando como fitoterapéutico.** Es lo peor de los
  dos mundos: registro que no cubre lo que dices.
- **Usar nombre común.** "Reishi" no identifica una especie; *Ganoderma lucidum* sí, y hay que probarlo.
- **Asumir que lo que vale para plantas vale para hongos.** Verificar con INVIMA.
- **Traer la monografía EMA como si fuera aprobación automática.** Es referente, no autorización.
- **Cambiar de casilla a mitad del trámite.** Se pierde tiempo y plata; se decide antes de radicar.
- **No documentar la consulta previa.** Si preguntaste y no guardaste la respuesta, no preguntaste.

## Conexión con otros módulos

→ `266-invima-y-suplementos-dietarios.md` — la casilla de suplemento en detalle.
→ `269-registro-sanitario-paso-a-paso-colombia.md` — el trámite.
→ `271-ica-y-materia-prima-vegetal.md` — antes del INVIMA está el ICA, si cultivas.
→ `280-farmacopeas-usp-ep-y-monografias.md` — qué es una monografía y cómo se lee.
→ `245-identidad-de-especie-por-its.md` — la prueba de identidad que sostiene todo.