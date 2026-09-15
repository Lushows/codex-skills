# 289 — Ética de la investigación y consentimiento informado (lo que se hace ANTES de reclutar a nadie)

En el momento en que tu estudio involucra personas —aunque sea "solo" que 30 clientes tomen tu producto y
llenen un formulario— dejaste el terreno del marketing y entraste al de la investigación con seres humanos.
Eso tiene reglas, y no son opcionales. Saltárselas tiene tres costos: ninguna universidad ni revista te va a
aceptar el dato, el estudio no sirve para sostener nada frente a autoridad, y si algo sale mal la
responsabilidad es personal. La buena noticia: cumplir es más barato y más rápido de lo que la gente cree.

Términos: **comité de ética en investigación (CEI / IRB, institutional review board)** = grupo independiente
que aprueba, observa y puede detener un estudio con humanos. **consentimiento informado (informed consent)**
= proceso (no solo un papel) por el que la persona entiende y acepta participar. **asentimiento (assent)** =
aceptación de un menor, además del consentimiento de sus padres. **riesgo mínimo (minimal risk)** = riesgo
no mayor al de la vida cotidiana o de un examen de rutina. **anonimización (anonymization)** = quitar del
dato todo lo que permita identificar a la persona.

## El marco (a agosto de 2026 — verificar vigencia)

| Norma | Alcance | Qué exige en la práctica |
|---|---|---|
| Declaración de Helsinki (AMM, revisiones sucesivas) | Referencia ética mundial para investigación en humanos | Comité independiente, consentimiento, balance riesgo-beneficio, registro público |
| Resolución 8430 de 1993 (Ministerio de Salud, Colombia) | Normas científicas, técnicas y administrativas para investigación en salud en Colombia | Clasificación por riesgo, comité de ética institucional, consentimiento escrito |
| Ley 1581 de 2012 y decretos reglamentarios (Colombia) | Protección de datos personales (Habeas Data) | Autorización expresa para tratar datos; los datos de salud son **sensibles** |
| Buenas Prácticas Clínicas (ICH E6) | Ensayos clínicos formales | Protocolo, monitoreo, trazabilidad de datos, archivo maestro |
| Convenio de Diversidad Biológica y Decisión 391 de la CAN | Acceso a recursos genéticos y conocimiento tradicional | Contrato de acceso a recursos genéticos si investigas material biológico nativo (`290`) |

Verifica siempre el texto vigente en la fuente oficial antes de diseñar. Para la parte operativa de los
trámites del negocio en Colombia, rutea a `AVIS_lushows`.

## Clasificación por riesgo (define cuánto trámite necesitas)

Siguiendo el espíritu de la Resolución 8430 de 1993:

| Categoría | Ejemplos | Implicación |
|---|---|---|
| **Sin riesgo** | Revisión de historias, encuestas anónimas sin intervención | Consentimiento simple; el comité suele hacer revisión expedita |
| **Riesgo mínimo** | Toma de muestra de sangre venosa de rutina, pruebas psicométricas validadas, consumo de un alimento o suplemento ya comercializado en su dosis usual | Consentimiento escrito + aprobación de comité |
| **Riesgo mayor que el mínimo** | Dosis superiores a las usuales, sustancias no comercializadas, poblaciones vulnerables, procedimientos invasivos | Comité completo, seguro, monitoreo, protocolo formal |

Un piloto de tolerabilidad de un suplemento comercializado suele caer en **riesgo mínimo** — lo que no
significa "sin trámite", significa que el trámite es abordable.

## Los elementos obligatorios del consentimiento informado

El documento debe estar en lenguaje que un adulto sin formación técnica entienda (grado de lectura de
bachillerato), en dos copias, firmado y fechado, y una copia se queda con el participante.

1. Que se trata de una **investigación**, quién la hace y quién la financia (incluido el conflicto de
   interés: "el estudio lo financia el fabricante del producto" se escribe, no se esconde).
2. **Objetivo** del estudio en una frase, y por qué se invita a esa persona.
3. **Qué va a pasar**: qué toma, cuánto, por cuánto tiempo, cuántas visitas, qué le van a medir.
4. **Riesgos e incomodidades conocidos**, incluidos los leves, y qué hacer si aparecen.
5. **Beneficios**: los reales. Si no hay beneficio directo esperado, se dice así.
6. **Alternativas**: que no participar es una opción legítima.
7. **Confidencialidad**: cómo se guardan los datos, quién los ve, por cuánto tiempo, cómo se anonimizan.
8. **Voluntariedad y retiro**: puede retirarse en cualquier momento sin dar explicaciones y sin perder
   ningún derecho ni beneficio comercial.
9. **Compensación**: si se paga transporte o tiempo, cuánto. El pago no puede ser tan alto que induzca a
   participar contra el propio criterio (coerción económica).
10. **Qué pasa si ocurre un daño**: quién responde, a quién llamar, y datos de contacto de 24 horas.
11. **Datos del comité de ética** que aprobó el estudio, con teléfono, para que el participante pueda
    quejarse ante alguien que no seas tú.
12. Firmas: participante, testigo (cuando aplique) e investigador.

## Casos especiales

- **Menores de edad**: consentimiento de padre/madre o representante **más** asentimiento del menor en
  lenguaje adecuado a su edad. Para un suplemento comercial, en general no vale la pena: sube el riesgo
  ético y regulatorio sin sumar valor comercial.
- **Personas con capacidad disminuida**: representante legal + asentimiento. Requiere justificación
  específica de por qué esa población.
- **Embarazo y lactancia**: se excluyen salvo justificación fortísima.
- **Empleados de tu empresa como participantes**: relación de poder = riesgo de coerción. Evítalo; si es
  inevitable, el reclutamiento lo hace un tercero y el jefe no sabe quién participó.
- **Psicodélicos**: cualquier estudio con psilocibina exige marco legal específico, comité, autorización de
  la autoridad y screening de seguridad estricto (`260`, `263`). Fuera de ese marco no se hace, punto.

## Datos personales: la parte que casi todos olvidan

Los datos de salud son **datos sensibles** bajo la Ley 1581 de 2012 (Colombia). Consecuencias prácticas:

- Se requiere **autorización previa, expresa e informada** específica para tratar datos de salud; no basta
  la política general de la página web.
- Separa la **base identificada** (nombre ↔ código) de la **base de análisis** (solo códigos). La primera se
  guarda cifrada y con acceso restringido.
- Define desde el inicio **cuánto tiempo** conservas los datos y cómo los destruyes.
- Si publicas fotos, testimonios o casos, necesitas autorización específica para eso, distinta del
  consentimiento del estudio. Y aun con autorización, un testimonio no es evidencia (`12`, `293`).

## Cómo se consigue un comité de ética siendo una empresa pequeña

No necesitas crear uno. Las rutas reales:

1. **Aliarte con una universidad** que ya tenga comité (el camino natural: ver `14`). El investigador
   principal es un docente y tú aportas producto y financiación, declarada.
2. **Comités de ética de clínicas u hospitales** con los que tengas convenio.
3. **Comités de ética independientes acreditados**, que revisan proyectos externos por una tarifa. Órdenes
   de magnitud reportados en el mercado: unos pocos millones de pesos por revisión **(ILUSTRATIVO —
   cotizar)**.

El tiempo típico de revisión va de 4 a 12 semanas. Súmalo al cronograma **antes** de prometerle resultados
a nadie.

## Ejemplo aplicado (BIO-SETA)

Piloto de tolerabilidad de melena de león, n = 30, 8 semanas, producto ya comercializado y en dosis de
etiqueta (`288`). Ruta: convenio con universidad → protocolo y consentimiento redactados → comité de ética
de la universidad (riesgo mínimo, revisión expedita) → autorización de tratamiento de datos firmada aparte
→ reclutamiento por convocatoria abierta, no entre clientes fieles (que están sesgados) → base de datos
codificada. En la publicidad, después, se puede decir que el estudio existió y qué se observó, con su nivel
de evidencia marcado — nada más (`293`).

## Errores comunes

- **Empezar a recoger datos y buscar el comité después.** No hay aprobación retroactiva: el dato ya nació
  inservible.
- **Consentimiento con lenguaje de abogado o de químico.** Si la persona no lo entendió, no consintió.
- **Ocultar quién financia.** Es el conflicto de interés más obvio del mundo y esconderlo destruye la
  credibilidad de todo el estudio.
- **Reclutar entre clientes que ya aman la marca.** Sesgo de selección brutal, sin remedio estadístico.
- **Pagar demasiado por participar.** Convierte el consentimiento en una transacción.
- **Publicar testimonios con nombre y foto** amparándose en el consentimiento del estudio: son
  autorizaciones distintas.
- **Guardar la base con nombres en una hoja de cálculo compartida.** Incidente de datos sensibles asegurado.

## Conexión con otros módulos

→ `288-como-disenar-un-estudio-piloto.md` — el diseño que este marco ético habilita.
→ `12-niveles-de-evidencia.md` — qué peso tiene después el dato que obtengas.
→ `293-como-comunicar-ciencia-sin-mentir.md` — cómo se cuenta el resultado.
→ `290-propiedad-intelectual-y-patentes.md` — de quién son los datos y el material biológico.
→ `138-farmacovigilancia-y-eventos-adversos.md` — qué hacer si alguien reporta un evento.
→ `14-como-trabajar-con-un-quimico-de-universidad.md` — la puerta de entrada al comité.
